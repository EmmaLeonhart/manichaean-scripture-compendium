"""Download Manichaean art from Wikimedia Commons, with license metadata.

Walks the category tree under Category:Manichaeism, skipping font-glyph
categories, and saves each file's original into
data_lake/downloads/commons/files/. It writes metadata.json (license,
author, description, source page and categories for each file) and
INDEX.md. Files already present are skipped, so re-running it only fetches
what is new.

Usage: python scripts/fetch_commons_art.py [--dry-run]
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
API = "https://commons.wikimedia.org/w/api.php"
ROOT = "Category:Manichaeism"
MAX_DEPTH = 6
# Font glyph sheets, not art.
SKIP = {
    "Category:Noto Sans Manichaean",
    "Category:GNU Unifont Manichaean",
    "Category:Unicode 10AC0-10AFF Manichaean",
    "Category:Manichaean letters",
}
OUT = Path(__file__).resolve().parent.parent / "data_lake" / "downloads" / "commons"


def get(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            time.sleep(2 ** attempt)
    raise RuntimeError("API request failed: " + url)


def members(cat):
    params = {"action": "query", "list": "categorymembers", "cmtitle": cat,
              "cmlimit": 500}
    while True:
        r = get(params)
        yield from r["query"]["categorymembers"]
        if "continue" not in r:
            return
        params.update(r["continue"])


def crawl():
    files, seen = {}, set()

    def walk(cat, depth):
        if cat in seen or cat in SKIP or depth > MAX_DEPTH:
            return
        seen.add(cat)
        for m in members(cat):
            if m["ns"] == 6:
                files.setdefault(m["title"], set()).add(cat)
            elif m["ns"] == 14:
                walk(m["title"], depth + 1)

    walk(ROOT, 0)
    return files


def imageinfo(titles):
    info = {}
    for i in range(0, len(titles), 40):
        r = get({"action": "query", "prop": "imageinfo",
                 "titles": "|".join(titles[i:i + 40]),
                 "iiprop": "url|size|mime|extmetadata"})
        for page in r["query"]["pages"].values():
            if "imageinfo" in page:
                info[page["title"]] = page["imageinfo"][0]
    return info


def meta_value(ext, key):
    return ext.get(key, {}).get("value", "")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    dry = "--dry-run" in sys.argv
    files = crawl()
    titles = sorted(files)
    info = imageinfo(titles)
    total = sum(i["size"] for i in info.values())
    print(f"{len(titles)} files, {total / 1e6:.1f} MB")
    if dry:
        return
    (OUT / "files").mkdir(parents=True, exist_ok=True)
    records = []
    for t in titles:
        ii = info.get(t)
        if not ii:
            continue
        # Windows forbids some characters that Commons titles allow.
        name = re.sub(r'[<>:"/\|?*]', "_", t.split(":", 1)[1].replace(" ", "_"))
        dest = OUT / "files" / name
        if not dest.exists():
            try:
                req = urllib.request.Request(ii["url"], headers={"User-Agent": UA})
                dest.write_bytes(urllib.request.urlopen(req, timeout=300).read())
            except Exception as e:
                print("FAILED", name, e)
                continue
            time.sleep(1)
        ext = ii.get("extmetadata", {})
        records.append({
            "file": f"files/{name}",
            "title": t,
            "page": ii.get("descriptionurl"),
            "mime": ii.get("mime"),
            "width": ii.get("width"),
            "height": ii.get("height"),
            "bytes": ii.get("size"),
            "license": meta_value(ext, "LicenseShortName"),
            "license_url": meta_value(ext, "LicenseUrl"),
            "artist": meta_value(ext, "Artist"),
            "credit": meta_value(ext, "Credit"),
            "description": meta_value(ext, "ImageDescription"),
            "date": meta_value(ext, "DateTimeOriginal"),
            "categories": sorted(files[t]),
        })
        print("ok", name)
    (OUT / "metadata.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = ["# Manichaean art from Wikimedia Commons", "",
             f"{len(records)} files, fetched by `scripts/fetch_commons_art.py` "
             f"from {ROOT}. Per-file metadata is in `metadata.json`.", "",
             "| File | License | Categories |", "|---|---|---|"]
    for r in records:
        cats = "; ".join(c.split(":", 1)[1] for c in r["categories"])
        lines.append(f"| [{r['file'][6:]}]({r['page']}) | {r['license']} | {cats} |")
    (OUT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
