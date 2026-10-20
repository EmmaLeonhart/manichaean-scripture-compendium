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
- First text online: `docs/texts/xwastwanift.md`, Le Coq's public-domain 1911
  English translation of the Uyghur confession of the hearers. The text was
  extracted from the DLI scan's OCR and corrected from context, but not yet
  proofread against the page images, which is queued.
- Downloaded all the Manichaean art on Wikimedia Commons with
  `scripts/fetch_commons_art.py`: 211 files, 316 MB, with per-file license
  metadata, in `data_lake/downloads/commons/` (the user asked for this). Fixed
  Windows filename and console-encoding errors along the way.
- Translation plan written to `research/notes/translation-plan.md`: ten
  texts in order of work, Chinese first (the base texts are entirely public
  domain), then the Coptic Psalm-Book (the Giversen facsimiles are on
  archive.org) and the Cologne Mani Codex.
- Proofread the Xwāstwānīft page against a second, independent OCR
  (`dli.ministry.15623`). It agrees on every doubtful reading checked
  (Zephyr, Raimast, merit-attaining, Preta, unavailableness and others).
  Fixed "Qutluγ pads". The page images themselves were not viewed.
- Added two public-domain text pages: `docs/texts/al-biruni-quotations.md`
  (Mani's Šābuhragān, Gospel, Mysteries and Treasure as quoted by al-Bīrūnī,
  Sachau 1879/1888) and `docs/texts/fundamental-epistle.md` (the Fundamental
  Epistle and Treasure VII as quoted by Augustine, NPNF 1887). Every
  Augustine quotation was checked word for word against the 1887 scan. New
  Advent's revised text was used only to locate them.
- Started a new CC BY translation of the Chinese Traité (Sermon of the
  Light-Nous) from Taishō 54 no. 2141B: introduction, key-terms table, and
  §§1–7 (Adda's question, the building of the world, the body as a
  microcosm, the five prisons and dead trees, the cage of snakes, the ships,
  the Light-Nous entering the old house). Marked as a draft.
- Traité §§8–10 drafted: the three days and two nights, the five battles of the old and new man, and the Light-Nous in the five cities, with the Gospel and Epistles quotations.
- Traité §§11–12 drafted: the Light-Nous as gardener (the five dead trees and five living trees, given root to colour) and Compassion as king of the virtues.
- Traité §§13–17 drafted: the four days and two nights, the twelve kings of light, the twelve signs of the Elect (five marks for each), the Envoy's charge and the closing hymn. The first-pass translation is complete. Queued: check it against Chavannes & Pelliot.
- Started checking the Traité against Chavannes & Pelliot 1911. Corrected 有礙無礙 to "bounded and unbounded", corrected the subject of the sifting in §8, and identified the transcription in §7. The rest of the check is queued.
- Traité check: §§2–6 compared with the French. Fixed §4 (the five passions copy the five sons of the Living Spirit; greed and lust copy the Call and Answer) and §6 ("Demon of Enmity").
- Traité check: in §8, restored the dropped clause (Faith from the Mind, added to the Wind) following Chavannes & Pelliot, and noted their rendering of 具足 as "contentment".
- Traité check: §10 compared. Corrected "great minister" (大相), marked a four-character gap, and softened the identification of 應輪經 and 寧萬經 to "probably", adding C&P's literal titles.
- Traité check: §9 compared and matches. §8 now reads "signs that there are two realms", following C&P.
- Traité check: §11 dead and living trees compared. Corrected 謟惰, 增上 and 羔眾 following C&P.
- Traité check: the fourth sign corrected (does not resent those above him), and C&P's reading of 言通再受 noted.
