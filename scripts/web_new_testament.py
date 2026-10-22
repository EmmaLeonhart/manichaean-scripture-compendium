"""Builds the New Testament pages (docs/texts/nt/*.md and docs/texts/new-testament.md) from the
World English Bible verse-per-line file in data_lake/downloads/web/. Run from the repo root."""
import os
from collections import OrderedDict

SRC = 'data_lake/downloads/web/engwebp_vpl.txt'
OUT = 'docs/texts/nt'

BOOKS = [
    ('MAT', 'matthew', 'Matthew'), ('MAR', 'mark', 'Mark'), ('LUK', 'luke', 'Luke'),
    ('JOH', 'john', 'John'), ('ACT', 'acts', 'Acts'), ('ROM', 'romans', 'Romans'),
    ('1CO', '1-corinthians', '1 Corinthians'), ('2CO', '2-corinthians', '2 Corinthians'),
    ('GAL', 'galatians', 'Galatians'), ('EPH', 'ephesians', 'Ephesians'),
    ('PHI', 'philippians', 'Philippians'), ('COL', 'colossians', 'Colossians'),
    ('1TH', '1-thessalonians', '1 Thessalonians'), ('2TH', '2-thessalonians', '2 Thessalonians'),
    ('1TI', '1-timothy', '1 Timothy'), ('2TI', '2-timothy', '2 Timothy'), ('TIT', 'titus', 'Titus'),
    ('PHM', 'philemon', 'Philemon'), ('HEB', 'hebrews', 'Hebrews'), ('JAM', 'james', 'James'),
    ('1PE', '1-peter', '1 Peter'), ('2PE', '2-peter', '2 Peter'), ('1JO', '1-john', '1 John'),
    ('2JO', '2-john', '2 John'), ('3JO', '3-john', '3 John'), ('JUD', 'jude', 'Jude'),
    ('REV', 'revelation', 'Revelation'),
]

SOURCE = ("'World English Bible, 2020 stable text edition, from the verse-per-line file of eBible.org "
          "(engwebp_vpl), text unchanged. The World English Bible is in the public domain.'")
RIGHTS = ('"Public domain (dedicated to the public domain by its translators). '
          'World English Bible is a trademark of eBible.org."')

verses = {}
for line in open(SRC, encoding='utf-8'):
    code, rest = line.split(' ', 1)
    ref, text = rest.split(' ', 1)
    ch, v = ref.split(':')
    verses.setdefault(code, OrderedDict()).setdefault(int(ch), []).append((v, text.strip()))

os.makedirs(OUT, exist_ok=True)
for i, (code, slug, name) in enumerate(BOOKS):
    chapters = verses[code]
    prev = f'[← {BOOKS[i - 1][2]}]({BOOKS[i - 1][1]}.html) · ' if i else ''
    nxt = f' · [{BOOKS[i + 1][2]} →]({BOOKS[i + 1][1]}.html)' if i + 1 < len(BOOKS) else ''
    nav = f'{prev}[New Testament contents](../new-testament.html){nxt}\n'
    out = ['---', f'title: "{name} (World English Bible)"', 'text: true', 'group: extracanonical',
           f'order: {200 + i}', f'summary: The book of {name} in the World English Bible ({len(chapters)} chapter{"s" if len(chapters) > 1 else ""}).',
           'original_language: Greek', f'source: {SOURCE}', f'rights: {RIGHTS}', '---', '', nav]
    if len(chapters) > 1:
        out.append('Chapters: ' + ' · '.join(f'[{c}](#chapter-{c})' for c in chapters) + '\n')
    for c, vs in chapters.items():
        out.append(f'## Chapter {c}\n')
        out.append('  \n'.join(f'<sup>{v}</sup> {t}' for v, t in vs) + '\n')
    out.append(nav)
    with open(os.path.join(OUT, slug + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))

rows = '\n'.join(f'- [{name}](nt/{slug}.html) ({len(verses[code])} chapter{"s" if len(verses[code]) > 1 else ""})' for code, slug, name in BOOKS)
index = f'''---
title: "The New Testament (World English Bible)"
text: true
group: extracanonical
order: 199
summary: The 27 books of the New Testament in the public-domain World English Bible, one page per book.
original_language: Greek
source: {SOURCE}
rights: {RIGHTS}
---

The Manichaeans read the Gospels and the letters of Paul, and Mani called
himself "apostle of Jesus Christ" after Paul's manner. The New Testament is
given here in the World English Bible, a modern public-domain translation,
so that the Manichaean texts that quote or retell it can be read beside it:
see, for example, [the Passion in Manichaean Middle Persian](turfan-passion.html).

The text is the World English Bible unchanged, one page per book, with
chapter and verse numbers.

{rows}
'''
with open('docs/texts/new-testament.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(index)
print('ok', len(BOOKS), sum(len(verses[c]) for c, _, _ in BOOKS))
