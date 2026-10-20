"""Download the Manichaean artworks that have their own English Wikipedia article.

Walks en.wikipedia Category:Manichaean art (and subcategories), skips general
articles, and for each artwork article saves the article's main image (its
"page image", in original resolution) into data_lake/downloads/wikipedia-art/,
with metadata.json (article, image, license, author) and INDEX.md.

Usage: python scripts/fetch_wikipedia_art.py
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

UA = ("manichaean-scripture-compendium/0.1 "
      "(https://github.com/EmmaLeonhart/manichaean-scripture-compendium)")
WP = "https://en.wikipedia.org/w/api.php"
COMMONS = "https://commons.wikimedia.org/w/api.php"
ROOT = "Category:Manichaean art"
# Articles in the category that are about a subject, not one artwork.
NOT_ARTWORKS = {"Manichaean art", "Arzhang", "Turpan Manichaean texts"}
# Articles with no page image set: the image(s) of the artwork itself, as used
# in the article body.
FALLBACK = {
    "Icon of Mani": ["Icon_of_Mani.jpg"],
    "Manichaean Diagram of the Universe": [
        "Yüen_dynasty_Manichaean_diagram_of_the_Universe.jpg"],
    "Manichaean stone reliefs of Shangwan village": [
        "Manichaean_stone_reliefs_of_Shangwan_village_A1_and_A2.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_B.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_C.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_C2.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_d1.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_d2.gif",
        "Manichaean_stone_reliefs_of_Shangwan_village_e.gif"],
}
OUT = Path(__file__).resolve().parent.parent / "data_lake" / "downloads" / "wikipedia-art"


def get(api, **params):
    params["format"] = "json"
    req = urllib.request.Request(api + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=60))


def articles():
    found, seen = [], set()

    def walk(cat):
        if cat in seen:
            return
        seen.add(cat)
        r = get(WP, action="query", list="categorymembers", cmtitle=cat,
                cmlimit=500)
        for m in r["query"]["categorymembers"]:
            if m["ns"] == 14:
                walk(m["title"])
            elif m["ns"] == 0 and m["title"] not in NOT_ARTWORKS:
                found.append(m["title"])

    walk(ROOT)
    return sorted(set(found))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    (OUT / "files").mkdir(parents=True, exist_ok=True)
    records = []
    for title in articles():
        r = get(WP, action="query", prop="pageimages", titles=title,
                piprop="name")
        page = next(iter(r["query"]["pages"].values()))
        names = [page["pageimage"]] if page.get("pageimage") else FALLBACK.get(title)
        if not names:
            print("NO IMAGE", title)
            records.append({"article": title, "image": None})
            continue
        for name in names:
            fetch_one(title, name, records)
    write_index(records)


def fetch_one(title, name, records):
    # Images are on Commons, or uploaded locally to English Wikipedia.
    for api in (COMMONS, WP):
        r = get(api, action="query", prop="imageinfo",
                titles="File:" + name, iiprop="url|extmetadata")
        info = next(iter(r["query"]["pages"].values())).get("imageinfo")
        if info:
            break
    else:
        print("NOT FOUND", title, name)
        records.append({"article": title, "image": name})
        return
    ii, ext = info[0], info[0].get("extmetadata", {})
    local = re.sub(r'[<>:"/\\|?*]', "_", name)
    dest = OUT / "files" / local
    # Non-free (fair use) images never go in the repo: keep them in the
    # gitignored nonfree/ folder as references only.
    if ext.get("LicenseShortName", {}).get("value", "").lower().startswith("fair use"):
        dest = OUT.parent.parent.parent / "nonfree" / "shangwan" / local
        dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        req = urllib.request.Request(ii["url"], headers={"User-Agent": UA})
        dest.write_bytes(urllib.request.urlopen(req, timeout=300).read())
        time.sleep(1)
    records.append({
        "article": title,
        "article_url": "https://en.wikipedia.org/wiki/" + title.replace(" ", "_"),
        "image": name,
        "file": "files/" + local,
        "page": ii.get("descriptionurl"),
        "license": ext.get("LicenseShortName", {}).get("value", ""),
        "artist": ext.get("Artist", {}).get("value", ""),
    })
    print("ok", title, "->", local)


def write_index(records):
    (OUT / "metadata.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = ["# Manichaean artworks with their own Wikipedia article", "",
             f"{len(records)} artworks, each with the main image from its "
             "article. Fetched by `scripts/fetch_wikipedia_art.py`.", "",
             "| Artwork | Image | License |", "|---|---|---|"]
    for r in records:
        img = f"[{r['image']}]({r.get('page')})" if r.get("file") else "none"
        lines.append(f"| [{r['article']}]({r.get('article_url', '')}) | {img} | "
                     f"{r.get('license', '')} |")
    (OUT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
