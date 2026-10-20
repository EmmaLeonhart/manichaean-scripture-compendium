# Devlog

## 2026-10-20

- Work mode started at 11:19 PST, when the user said "go".
- Created the public repo `EmmaLeonhart/manichaean-scripture-compendium`.
- Added the CC BY 4.0 license, which the user chose.
- Refreshed the autonomous-loop skill to cleanvibe v2.0.6.
- Wrote the README, `research/SUMMARY.md` and the first queue.
- Corpus inventory written to `research/notes/corpus.md`, grouped by language
  and find, with editions and English translations. Items marked [verify]
  are still unchecked.
- Copyright audit in `research/notes/copyright.md`. Found a renewal for
  Jackson 1932 (R249768, 1960), so it is US public domain only from 2028.
  Allberry 1938 is URAA-restored until 2034. Three texts can go in English
  as-is now: Le Coq 1911, Sachau 1879 and NPNF 1887.
- Site skeleton in `docs/`: a Jekyll site built by GitHub Pages, with a
  CNAME of manichaeism.order.life and home, texts and about pages. A text
  page is any page with `text: true` in its front matter, plus `source`,
  `original_language`, `rights`, `summary` and `order`.
