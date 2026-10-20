# What this project is for

_Maintained by Claude: a running read of what the user is trying to do. It is
analysis, not a transcript, and it changes as understanding improves._

Work mode started: 2026-10-20 11:19 PST (user said "go").

## Current understanding

A compendium of Manichaean scripture, released under Creative Commons, with
new translations where existing ones are not freely licensed. Hosted from this
public repository at https://manichaeism.order.life.

## What supports it

- User, 2026-10-20: "We're trying to make a compendium of Manichaean
  scripture. Released under Creative Commons. Translating again if need be.
  Original hosting at https://manichaeism.order.life public repo"
- Folder name chosen by the user: `manichaean-library`.
- `data_lake/` is empty: no user material yet.

## Constraints from the user

- **License: CC BY 4.0** for the compendium's own content. The user replied
  "Credit go" to a choice between CC BY-SA, CC BY ("credit") and CC0, and then
  confirmed "go".
- **The repository is public** ("public repo"). This overrides the
  private-by-default rule in CLAUDE.md.
- **Hosting:** manichaeism.order.life.
- **Keep chat replies short.** Long answers made the user angry.
- **No translation work until 2026-10-21 06:00, and only until 15:00 that
  day.** User, 2026-10-20: "No translations until a cron job fires at 6am and
  stops at 3pm tomorrow". This includes checking the Traité. One-shot crons
  open the window at 06:00 and close it at 15:00. Until then, loop ticks do
  only non-translation queue items.
- **No DNS work until 2026-10-21 about 11:35 PST.** User, 2026-10-20: "ignore
  dns stuff for 24 hours". Don't raise it or work on it before then.
- **Manichaean art from Wikimedia Commons.** User, 2026-10-20: "we download
  all of the manichaean art too that's around from wikimedia commons and
  later we will make svg renditions and AI fillings of them." For now that
  means download everything, with each file's license and author metadata.
  The SVG renditions and AI fillings come later and need their own
  instructions; my reading is that "AI fillings" means AI restoration of
  damaged or missing areas. Downloaded 2026-10-20: 211 files in
  `data_lake/downloads/commons/`. 162 are public domain or CC0 and 49 are
  CC BY-SA, so SVG and AI derivatives of those 49 must be released under
  CC BY-SA, not CC BY.
- **Correction (2026-10-20): "the art" means the artworks that have their own
  Wikipedia articles.** User: "The art piecea I believe all have wikipedia
  articles". The Commons category dump pulled in maps, European paintings
  about Manichaeans, temple photos and so on, and the user was angry about
  it. The working set is now `data_lake/downloads/wikipedia-art/`: 19
  artworks from en.wikipedia Category:Manichaean art, 25 images
  (`scripts/fetch_wikipedia_art.py`). The Commons dump was deleted at the user's
  order ("Delete it all"), along with its fetch script.

## Assumptions (not yet confirmed)

- The site is a Jekyll GitHub Pages site built from `docs/` on `main`, with
  a CNAME of `manichaeism.order.life`. Pages was switched on 2026-10-20. DNS
  is BLOCKED-ON-USER-ACTION: the user has to add a CNAME record for
  `manichaeism` on order.life pointing to `emmaleonhart.github.io`. Until
  then the github.io address redirects to a domain that does not resolve.
- Scope is the Manichaean canon and the surviving scriptural corpus: Mani's
  seven works (only fragments survive), the Coptic Medinet Madi codices
  (Psalm-Book, Kephalaia, Homilies), the Cologne Mani Codex, the Middle
  Iranian and Uyghur Turfan texts, and the Chinese texts (Hymnscroll,
  Compendium, Traité). Other material is secondary.
- Texts go in only if they are clearly free to use: (a) public-domain older
  translations, (b) new translations made for this project from original-
  language texts, released CC BY 4.0. Modern copyrighted translations are
  used only as reference and are never copied or closely paraphrased.

## Open questions

- Which texts should come first? (Default: start with public-domain material
  and the most complete witnesses.)
- Is there an order.life house style the site should match?

## Confidence

High on the goal, license and hosting. Medium on scope and site format.
