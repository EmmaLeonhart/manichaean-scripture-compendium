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
- Reorganized around `research/SCOPE.md` as the master list (user's order). The corpus, copyright and translation-plan notes are now supporting notes. The queue was rewritten in scope order, with translation items held for the 6am–3pm window.
- Texts page (`docs/texts/index.md`) now follows SCOPE.md: three groups, every in-scope item, links to the four pages and "Planned" for the rest. Each text page has a `group` field.
- Gallery page `docs/art.md` (/art/): 17 artworks with resized images, linking to Commons and Wikipedia, built by `scripts/build_gallery.py`. The Shangwan reliefs are left out because their images are fair-use/non-free (recorded in SCOPE.md). Added an Art link to the site nav.
- SCOPE.md: sources filled in for every "—" item, saying in each case whether there is a public-domain translation or a base text, and which scans exist. The four sources still missing are queued.
- Irk Bitig: confirmed that Thomsen's 1912 English translation (JRAS 1912, art. VIII) is in the DLI scan `in.ernet.dli.2015.70560` and is public domain. It is the next candidate for a page, since putting it up is reproduction, not translation.
- Sources located: Müller 1904 is in the open scan `abhandlungenderk1904kn`; the Cologne Codex Greek is only available as lending scans (ZPE 19; Koenen & Römer 1985). Le Coq's *Türkische Manichaica* is not on archive.org. Queued the Irk Bitig page.
- Irk Bitig page (`docs/texts/irk-bitig.md`): Thomsen's public-domain 1912 translation of all 65 omens plus the colophon, read from the page images of JRAS 1912 (pp. 196–209) because the OCR runs the columns together. Unverified shelfmark and date claims were taken out before committing.
- Checks: the Irk Bitig colophon was verified against its page image ("Itä-chuq"). The unverifiable shelfmark "Or. 8212/178" and the IDP claim were removed from the Xwāstwānīft page; only Stein's Ch. 0015 is kept.
- Le Coq's *Türkische Manichaica*: part I is in archive.org `abhandlungenderk1911akaduoft` and part II in `abhandlungenderk1919akaduoft` (both public domain, German). Part III (1922) was not found. Recorded in SCOPE.md.
- 2026-10-21 Traité check: §§12–14 compared with Chavannes & Pelliot. §13 now keeps "three great days" (三大) and restores 說聽 "Preaching and Hearing"; added a note on 平等 vs 真實 in §14.
- 2026-10-21 Compendium page (`docs/texts/compendium.md`): new CC BY draft translation of the whole Taishō text (London part, Stein 3969: chapters 1–6, to the four tranquil Dharma-bodies). The Paris part (Pelliot chinois 3884) is not in CBETA and is still to do.
- 2026-10-21 Hymnscroll page (`docs/texts/hymnscroll.md`): new CC BY draft translation of the first three hymns (Hymn to Jesus, parts 1 and 2; Lament on impermanence by Mār Sīsin). The opening Iranian transcription is noted but not translated.
- 2026-10-21 Hymnscroll: hymn 4, the Hymn of universal invocation by Mo-ye mōžak, translated and added, with a note on the order of the gods invoked.
- 2026-10-21 Hymnscroll: hymns 5–8 (Praise of Mani; the twelve hours; the verse for receiving food; the first-voice hymn, noted as an untranslated Iranian transcription).
- 2026-10-21 Hymnscroll: hymn 9, the Hymn in praise of the Envoys of Light who guard the Law (three parts).
- 2026-10-21 Hymnscroll: hymns 10 (praise of the supreme Venerable of Light) and 11 (praise of the Five Lights, two parts).
- 2026-10-21 Hymnscroll: hymn 12, the 78-stanza Hymn in praise of the realm of light.
- 2026-10-21 Hymnscroll: closing vows 13(a)–(l) and the colophon translated. The whole scroll now has a first-pass translation.
- 2026-10-21 Traité check finished: §14 end, §15 signs 1–3 and 5–12, §16 and §17 compared with Chavannes & Pelliot 1911 (which covers the whole Traité, so no 1913 part is needed for it). Fixed "rare understanding" (別識, §14), "Lord of the Law" (法主, sign 11) and "adorn these jewelled trees" (§16); noted three places where they read differently.
- 2026-10-21 Šābuhragān page (`docs/texts/shabuhragan.md`): new CC BY English translation of the Turfan eschatology fragments (M 475, 477, 482, 472, 470, 473, 473b) from Müller 1904's readings and German (public domain), with al-Nadīm's parallel summary from Kessler's German as Müller quotes it.
- 2026-10-21 New page `docs/texts/turfan-gospel-epistles.md`: CC BY English draft of Turfan M 17 (the opening of the Living Gospel, "I, Mani, the apostle of Jesus the Friend"), M 733 and M 731 (extracts from the Epistles), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-cosmogony.md`: CC BY English draft of the Middle Persian cosmogony M 98–99 (the sun and moon as ships of light, the heavens, earths, walls and prisons), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-hymnbook-m4.md`: CC BY English draft of the hymnbook M 4 (hymns of the last days, body and soul, the going out; Mani's hymn of Babel; prayers to the angels), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-mani-legends.md`: CC BY English draft of M 3 (Mani at the court), M 47 (Mihršāh's garden, and the parable of the lamps), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-passion.md`: CC BY English draft of M 18 and M 132 (the trial, mocking and empty tomb in a Manichaean Gospel harmony), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-hymns-prayers.md`: CC BY English draft of M 383, "M. liturg." (Mani's song "I am the first stranger"), M 442, M 2 (Mār Ammō and the spirit of the frontier), M 75 and M 331 (the Sanctus), M 43 (prayer for an Uyghur khan), from Müller 1904. The rest of Müller's small fragments are listed in SCOPE.md as still to do.
- 2026-10-21 New page `docs/texts/turfan-fragments-2.md`: CC BY English draft of M 14 and M 34 (the twelve aeons of light and darkness), M 20, 33, 309, 8, 40, 730 (angels, heavens, hymns), M 176 (new-moon and full-moon hymns to Jesus and Mani) and M 32 (hymn to the god Naresaf), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-fragments-3.md`: CC BY English draft of M 102, 311, 551, 789, 554, 544, 555, 324, 74, 38, 173, 543 (prayers to Mani and Jesus, "what eye has not seen", a third Sanctus, an alphabetic hymn, prayers for a patron and a leader), from Müller 1904.
- 2026-10-21 New page `docs/texts/turfan-fragments-4.md`: CC BY English draft of M 48, M 566 (the Apostle and Ardāv; "a physician from the land of Babel"), a conversion story, M 45 (Khebrā the hearer), M 64 (a chanted song), M 16 (fast days), M 28 (polemic), M 50 (calendar table), from Müller 1904.
- 2026-10-21 Müller 1904 finished: added M 172 (the Gospel doxology in Middle Persian and Parthian) to `turfan-gospel-epistles`, and Müller's addenda verses ("I am a man, a seed of light", "I am a ruler's son … a stranger", M 7 "From the light and from the gods am I") to `turfan-hymns-prayers`. Only pieces Müller printed without any translation are left.
- 2026-10-21 New page `docs/texts/turkish-manichaica-1.md`: CC BY English draft of all of Le Coq, *Türkische Manichaica aus Chotscho* I (1911): the legend T II D 176, the sermon book T II D 173 (parables, the rescue of Ohrmizd and the making of heaven, the prayer dated 522 years after Mani), T Ia, bundle 172, the prayer-book colophon T II D 171, the možak fragment, and Mār Ammō and the sorcerer.
- 2026-10-21 New page `docs/texts/turkish-manichaica-2.md`: CC BY English draft of all of Le Coq, *Türkische Manichaica* II (1919): T M 180, T II D 75a, the song of Aprin Čor Tigin (T M 419), the three hymns of T II D 169 (dawn, the four majesties, the soul after death) and T II D 178 (the judgement).
- 2026-10-21 New page `docs/texts/mahrnamag.md`: CC BY English draft of M 1, the *Mahrnāmag* (Müller 1912): the blessing on the Uyghur khan and court, the account of the book's making (begun in the year 546 after Mani's birth), and the table of contents.
- 2026-10-21 Correction: the Compendium page said Taishō prints only the London manuscript and that the Paris part was still to do. The CBETA note shows Taishō supplements chapters 5–6 from the Paris copy (P.3884), so the page already has the whole surviving text. Fixed the page, SCOPE.md and the index.
- 2026-10-21 New page `docs/texts/le-coq-1909.md`: CC BY English draft of Le Coq's 1909 SPAW pieces: the Manichaean Bodhisattva-prince leaf (T II D 178e) and the runic-script hymn and story fragments. Checked the Coptic sources: Allberry 1938 and the Giversen facsimiles are all lending-only on archive.org (BLOCKED-ON-EXTERNAL, recorded in SCOPE.md).
- 2026-10-21 New page `docs/texts/zarathustra-in-babel.md`: CC BY English draft of Le Coq's 1908 Uyghur-script fragment on Zrušč Burxan (Zarathustra) in Babel. Checked Müller 1904 part I: mostly about the script, samples re-edited in part II; not translated separately.
- 2026-10-21 Mahrnāmag: applied Müller's addenda (*kes* as "teacher" in the account of the book's making; Mār Zakū a disciple of Mani). T II D 135 (the Bögü Khan leaf) is printed in the 1912 appendix only in the original script, without a translation; Müller's translation is in the Thomsen Festschrift (1912), not yet located online.
- 2026-10-21 Found Le Coq, *Türkische Manichaica* III (1922) on archive.org (`AbhandDerPreussAkadDerWissen1922`). New page `docs/texts/turkish-sermon-light-nous.md`: CC BY English draft of its no. 8, the Old Turkish version of the Sermon of the Light-Nous (T II D 119, T M 300, T M 423a–e, a leaf from ruin α), with the parallels to the Traité; linked from the Traité page. The rest of TM III is queued.
- 2026-10-21 New page `docs/texts/turkish-hymn-to-mani.md`: CC BY English draft of TM III no. 9 (T II D 78a–k), the penitent's hymn to Mani ("our new day, our new month"); pieces vi–xi are only described, as Le Coq gave almost no German for them.
- 2026-10-21 New page `docs/texts/turkish-manichaica-3a.md`: CC BY English draft of TM III nos. 1–7 (gods of light, the moon's palaces, the demon under the mountains, the body as a stormy sea, the day of death, sermon-book leaves with sayings of Mšiha Burxan and the question about the moon-god in the Great Gospel, Mani on the Maiden of Light).
- 2026-10-21 New page `docs/texts/turkish-manichaica-3b.md`: CC BY English draft of TM III nos. 10–14 (hymns to the new day and the shining soul, against false Elect, the parable book with the astrologer and the tree of wisdom, the book of the fairy queen, a fable of Aesop).
- 2026-10-21 New page `docs/texts/turkish-manichaica-3c.md`: CC BY English draft of TM III nos. 15–19 (the blessing on a new Iduq-qut of Qočo, T M 417; the hymn on the god who brought Noydar the mahistak; a blessing for a možak; sermon and cosmogony fragments).
- 2026-10-21 New page `docs/texts/turkish-manichaica-3d.md`: CC BY English draft of TM III nos. 20–25 (rules and fast days, Mani's commandments, the sinless lamb, prayers for the Tängrikän of Qočo and to Mani who came to the Uyghur land).
- 2026-10-21 New page `docs/texts/turkish-manichaica-3e.md`: CC BY English draft of TM III nos. 26–39 ("this earth is not eternal", the blessing on the hearers in the Manistan, the colophon of the scribe Aïduq, the drying river, Ānanda and the Burxan).
