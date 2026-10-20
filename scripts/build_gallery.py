"""Build docs/art.md and docs/art/img/ from data_lake/downloads/wikipedia-art/ (skips non-free images). Run after fetch_wikipedia_art.py."""
import json,re,html,sys
from pathlib import Path
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')
src=Path('data_lake/downloads/wikipedia-art'); out=Path('docs/art/img')
recs=json.load(open(src/'metadata.json',encoding='utf-8'))
def clean(s):
    s=re.sub(r'<span style="display: ?none;?">.*?</span>','',s or '',flags=re.S)
    s=html.unescape(re.sub(r'<[^>]+>',' ',s)); s=re.sub(r'\s+',' ',s).strip()
    return s.replace('Author:','').strip()
items=[]
for r in recs:
    if not r.get('file'): continue
    lic=r['license']
    if lic.lower().startswith('fair use'): continue
    slug=re.sub(r'[^a-z0-9]+','-',r['article'].lower()).strip('-')
    im=Image.open(src/r['file']).convert('RGB'); im.thumbnail((1600,1600))
    im.save(out/f'{slug}.jpg',quality=85)
    items.append((r['article'],r['article_url'],r['page'],lic,clean(r['artist'])[:120],slug))
lines=['---','title: Visual art','permalink: /art/','---','',
"The Manichaean artworks listed in Wikipedia's Manichaeism navigation box. Each image links to its source file on Wikimedia Commons, and each title links to its Wikipedia article.",'',
"*The Stone reliefs of Shangwan village* are left out because Wikipedia's images of them are non-free (fair use). See the [Wikipedia article](https://en.wikipedia.org/wiki/Manichaean_stone_reliefs_of_Shangwan_village). The *Book of Pictures* (Arzhang) is lost.",'']
for a,au,page,lic,art,slug in items:
    credit=f"{art}. " if art and art.lower() not in ('unknown author','anonymous') else ''
    if lic.startswith('CC BY-SA'): lic += f' (this resized copy is also {lic})'
    lines+=[f'### [{a}]({au})','',f'[![{a}](img/{slug}.jpg)]({page})','',f'<p class="sec">{credit}{lic}. Source: <a href="{page}">Wikimedia Commons</a>.</p>','']
open('docs/art.md','w',encoding='utf-8').write('\n'.join(lines))
print(len(items))
