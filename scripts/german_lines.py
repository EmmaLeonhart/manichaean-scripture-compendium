"""Print the German translation lines (and headings) of an interlinear OCR text between two line numbers."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(path, encoding='utf-8').read().split('\n')[a-1:b]
TURK = re.compile(r"[{}^\<>«»#%&@~|]|\(a\)|\(ä\)|'i|'l|y\{|q\{|ä\)|a\)")
for l in L:
    s = l.strip()
    if len(s) < 4 or TURK.search(s):
        continue
    letters = sum(c.isalpha() for c in s)
    if letters < 0.6 * len(s.replace(' ', '')):
        continue
    print(re.sub(r'\s{2,}', ' ', s))
