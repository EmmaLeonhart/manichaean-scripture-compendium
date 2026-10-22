"""Writes the schematic SVG line drawings of the Shangwan reliefs (features only) to docs/art/img/. Run from the repo root."""
import os

OUT = 'docs/art/img'
HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        'role="img" aria-label="{label}">\n<title>{label}</title>\n'
        '<rect width="{w}" height="{h}" fill="#f6f2e9"/>\n'
        '<g fill="none" stroke="#3a3530" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">\n')
TAIL = '</g>\n</svg>\n'


def lotus(cx, y, w, rows=2):
    """Lotus pedestal: rows of petals, widest at the top, then a base."""
    s = ''
    for r in range(rows):
        n = 5 - r
        rw = w * (1 - 0.18 * r)
        pw = rw / n
        x0 = cx - rw / 2
        yy = y + r * 14
        for i in range(n):
            a = x0 + i * pw
            s += f'<path d="M{a:.0f} {yy} Q{a + pw / 2:.0f} {yy + 22} {a + pw:.0f} {yy}"/>\n'
    s += f'<rect x="{cx - w * 0.3:.0f}" y="{y + rows * 14 + 6}" width="{w * 0.6:.0f}" height="12" rx="3"/>\n'
    return s


def standing(cx, top, h, halo=False, cap=None, hands='joined'):
    """Standing robed figure, head at top, feet at top+h."""
    hr = h * 0.075
    hy = top + hr
    s = ''
    if halo:
        s += f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr * 1.9:.0f}" stroke-dasharray="4 4"/>\n'
    s += f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr:.0f}"/>\n'
    if cap == 'pointed':
        s += f'<path d="M{cx - hr:.0f} {hy - hr * 0.4:.0f} L{cx} {top - hr * 1.2:.0f} L{cx + hr:.0f} {hy - hr * 0.4:.0f}"/>\n'
    elif cap == 'hat':
        s += f'<path d="M{cx - hr * 1.1:.0f} {hy - hr * 0.5:.0f} L{cx - hr * 0.8:.0f} {top - hr * 0.8:.0f} L{cx + hr * 0.8:.0f} {top - hr * 0.8:.0f} L{cx + hr * 1.1:.0f} {hy - hr * 0.5:.0f}"/>\n'
    sh = top + 2 * hr + 4
    sw = h * 0.13
    foot = top + h
    hem = h * 0.24
    s += (f'<path d="M{cx - sw:.0f} {sh:.0f} Q{cx - sw * 1.1:.0f} {sh + h * 0.4:.0f} {cx - hem:.0f} {foot - 10:.0f} '
          f'L{cx + hem:.0f} {foot - 10:.0f} Q{cx + sw * 1.1:.0f} {sh + h * 0.4:.0f} {cx + sw:.0f} {sh:.0f} Z"/>\n')
    s += f'<path d="M{cx - sw:.0f} {sh:.0f} Q{cx} {sh + 10:.0f} {cx + sw:.0f} {sh:.0f}"/>\n'
    if hands == 'joined':
        hy2 = sh + h * 0.2
        s += f'<path d="M{cx - sw * 0.9:.0f} {sh + 6:.0f} Q{cx - sw * 0.7:.0f} {hy2:.0f} {cx} {hy2:.0f} Q{cx + sw * 0.7:.0f} {hy2:.0f} {cx + sw * 0.9:.0f} {sh + 6:.0f}"/>\n'
        s += f'<path d="M{cx - 5} {hy2 + 4:.0f} L{cx} {hy2 - 14:.0f} L{cx + 5} {hy2 + 4:.0f}"/>\n'
    s += f'<path d="M{cx - 14} {foot - 10:.0f} l0 8 M{cx + 14} {foot - 10:.0f} l0 8"/>\n'
    return s


def seated(cx, top, h, halo=True, cap=None):
    """Seated cross-legged figure, hands in lap."""
    hr = h * 0.14
    hy = top + hr
    s = ''
    if halo:
        s += f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr * 1.8:.0f}" stroke-dasharray="4 4"/>\n'
    s += f'<circle cx="{cx}" cy="{hy:.0f}" r="{hr:.0f}"/>\n'
    if cap == 'hat':
        s += f'<path d="M{cx - hr * 1.1:.0f} {hy - hr * 0.4:.0f} L{cx - hr * 0.9:.0f} {top - hr * 0.6:.0f} L{cx + hr * 0.9:.0f} {top - hr * 0.6:.0f} L{cx + hr * 1.1:.0f} {hy - hr * 0.4:.0f}"/>\n'
    if cap == 'hood':
        s += f'<path d="M{cx - hr * 1.3:.0f} {hy + hr * 1.6:.0f} Q{cx - hr * 1.5:.0f} {top - hr * 0.5:.0f} {cx} {top - hr * 0.4:.0f} Q{cx + hr * 1.5:.0f} {top - hr * 0.5:.0f} {cx + hr * 1.3:.0f} {hy + hr * 1.6:.0f}"/>\n'
    sh = top + 2 * hr + 3
    w = h * 0.32
    base = top + h
    s += (f'<path d="M{cx - w * 0.6:.0f} {sh:.0f} Q{cx - w * 0.9:.0f} {sh + h * 0.3:.0f} {cx - w * 0.75:.0f} {base - h * 0.2:.0f} '
          f'Q{cx - w * 1.4:.0f} {base:.0f} {cx} {base:.0f} Q{cx + w * 1.4:.0f} {base:.0f} {cx + w * 0.75:.0f} {base - h * 0.2:.0f} '
          f'Q{cx + w * 0.9:.0f} {sh + h * 0.3:.0f} {cx + w * 0.6:.0f} {sh:.0f}"/>\n')
    ly = base - h * 0.22
    s += f'<path d="M{cx - w * 0.6:.0f} {ly - 10:.0f} Q{cx} {ly + 8:.0f} {cx + w * 0.6:.0f} {ly - 10:.0f}"/>\n'
    s += f'<ellipse cx="{cx}" cy="{ly - 4:.0f}" rx="{w * 0.22:.0f}" ry="7"/>\n'
    return s


def clouds(x, y, w, h, n=6):
    """Row of small cloud scrolls along a frame edge."""
    s = ''
    for i in range(n):
        cx = x + (i + 0.5) * w / n
        s += f'<path d="M{cx - 10:.0f} {y + 6:.0f} q0 -10 10 -10 q10 0 10 10 q-6 -4 -10 0" stroke-width="1.8"/>\n'
    return s


def write(name, w, h, label, body):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(HEAD.format(w=w, h=h, label=label) + body + TAIL)


# A1 and A2: two upright slabs.
b = '<rect x="10" y="10" width="200" height="300" rx="6"/>\n<rect x="230" y="10" width="200" height="300" rx="6"/>\n'
# A1: worn standing figure with halo, cloud border, flame shapes at the foot.
b += clouds(20, 30, 180, 20)
b += standing(110, 70, 170, halo=True)
b += '<path d="M40 290 q10 -30 0 -50 q20 20 15 50 M165 290 q-8 -25 4 -45 q12 22 -2 45" stroke-width="1.8"/>\n'
# A2: hooded seated figure on a tall lotus throne on a pedestal.
b += clouds(240, 30, 180, 20)
b += seated(330, 55, 105, cap='hood')
b += lotus(330, 165, 110, rows=4)
b += '<path d="M300 247 L300 290 L360 290 L360 247 M285 290 L375 290 L375 302 L285 302 Z"/>\n'
write('shangwan-a.svg', 440, 320, 'Shangwan reliefs A1 and A2: standing figure; seated figure on lotus throne', b)

# B: three figures on lotuses under a canopy, centre seated in an official's cap.
b = '<rect x="10" y="10" width="420" height="260" rx="6"/>\n'
b += clouds(165, 28, 110, 10, n=4)
b += standing(90, 55, 150, cap='hat') + lotus(90, 210, 80, rows=2)
b += seated(220, 55, 140, halo=True, cap='hat') + lotus(220, 200, 90, rows=2)
b += standing(350, 60, 145, halo=True) + lotus(350, 210, 80, rows=2)
write('shangwan-b.svg', 440, 280, 'Shangwan relief B: three figures on lotus seats, the central one seated', b)

# C: a tall pole at the left edge, a small figure in a pointed cap.
b = '<rect x="10" y="10" width="220" height="270" rx="6"/>\n'
b += '<path d="M25 25 L25 255 M18 255 L40 255 L40 268 L18 268 Z M25 30 l14 0"/>\n'
b += standing(160, 80, 150, cap='pointed')
write('shangwan-c.svg', 240, 290, 'Shangwan relief C: pole at left, figure in pointed cap with hands joined', b)

# C2: standing figure holding a staff across the body; pole at the right.
b = '<rect x="10" y="10" width="240" height="270" rx="6"/>\n'
b += standing(80, 60, 175, cap='pointed', hands=None)
b += '<path d="M40 210 L125 110"/>\n<path d="M65 140 q12 10 25 -3" />\n'
b += '<path d="M225 40 L225 250 M212 250 L238 250 L238 264 L212 264 Z"/>\n'
write('shangwan-c2.svg', 260, 290, 'Shangwan relief C2: figure holding a staff, pole at right', b)

# D1: figure holding a tall staff with a flower-shaped finial, sash, on a lotus.
b = '<rect x="10" y="10" width="200" height="320" rx="6"/>\n'
b += standing(125, 90, 190, hands=None)
b += '<path d="M70 40 L76 300"/>\n'
b += '<circle cx="70" cy="40" r="7"/><path d="M70 33 l0 -12 M63 40 l-10 0 M77 40 l10 0 M65 30 q5 -6 10 0 M70 48 l0 8"/>\n'
b += '<path d="M73 165 q30 5 45 -10 M73 172 q20 4 30 -2"/>\n'
b += '<path d="M160 190 q15 30 0 55 q15 15 5 30 M90 200 q-10 30 5 60" stroke-width="1.8"/>\n'
b += lotus(125, 288, 90, rows=1)
write('shangwan-d1.svg', 220, 340, 'Shangwan relief D1: figure holding a staff with a flower finial, on a lotus', b)

# D2: haloed monk-like figure, hands joined, on a lotus.
b = '<rect x="10" y="10" width="200" height="320" rx="6"/>\n'
b += standing(105, 60, 225, halo=True)
b += lotus(105, 285, 90, rows=1)
b += '<path d="M165 280 q10 -15 22 -5 q-5 15 -22 5" stroke-width="1.8"/>\n'
write('shangwan-d2.svg', 220, 340, 'Shangwan relief D2: haloed figure with hands joined, on a lotus', b)

# E: horizontal frieze, a small figure with arms raised holding two round objects, between interlaced scrolls.
b = '<rect x="10" y="10" width="520" height="160" rx="6"/>\n<rect x="25" y="22" width="490" height="136" rx="40"/>\n'
b += '<circle cx="270" cy="62" r="13"/>\n'
b += '<path d="M255 80 L285 80 L290 120 L250 120 Z"/>\n'
b += '<path d="M255 85 L215 62 M285 85 L325 62"/>\n<circle cx="208" cy="56" r="10"/><circle cx="332" cy="56" r="10"/>\n'
b += '<path d="M255 120 L225 150 M285 120 L315 150"/>\n<path d="M258 120 q12 18 24 0" />\n'
for sx in (1, -1):
    ox = 270 - 155 * sx
    # two wavy stems crossing each other, with spiral curls off them
    b += f'<path d="M{ox - 75 * sx} 90 C{ox - 50 * sx} 40 {ox - 25 * sx} 140 {ox} 90 S{ox + 50 * sx} 40 {ox + 75 * sx} 90"/>\n'
    b += f'<path d="M{ox - 75 * sx} 90 C{ox - 50 * sx} 140 {ox - 25 * sx} 40 {ox} 90 S{ox + 50 * sx} 140 {ox + 75 * sx} 90"/>\n'
    for cx, cy in ((ox - 45, 50), (ox + 30, 50), (ox - 30, 130), (ox + 45, 130)):
        b += f'<path d="M{cx - 14} {cy} a14 14 0 1 1 14 14 a9 9 0 1 1 -9 -9 a4 4 0 1 1 4 4" stroke-width="1.8"/>\n'
write('shangwan-e.svg', 540, 180, 'Shangwan relief E: small figure holding two round objects between interlaced scrolls', b)
print('ok')
