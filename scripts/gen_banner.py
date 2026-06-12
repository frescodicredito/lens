"""Generate the README header banner (assets/lens-banner.svg + .png).

A precise optical ray diagram (parallel rays -> biconvex lens -> focal point ->
diverging rays) in a Voyager-plaque engraving style. Vector source, rendered to
2048x512 PNG via rsvg-convert. Re-run after edits:

    python scripts/gen_banner.py && rsvg-convert -w 2048 -h 512 assets/lens-banner.svg -o assets/lens-banner.png
"""

W,H = 2048,512
yc = H/2
GOLD = "#CBA975"
x0   = 120      # inizio raggi (sx)
xL   = 600      # piano lente
xF   = 980      # fuoco
xR   = 1620     # fine raggi divergenti (dx)
offs = [-120,-60,60,120]   # altezze raggi simmetriche

def line(x1,y1,x2,y2,w=2.4,extra=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GOLD}" stroke-width="{w}" stroke-linecap="round" {extra}/>'

parts = []
parts.append(f'<rect width="{W}" height="{H}" fill="#0d1117"/>')

# asse ottico tratteggiato
parts.append(f'<line x1="80" y1="{yc}" x2="1660" y2="{yc}" stroke="{GOLD}" stroke-width="2" stroke-dasharray="2 11" stroke-linecap="round" opacity="0.7"/>')

# raggi
for o in offs:
    yin = yc + o
    m = (yc - yin)/(xF - xL)
    yout = yc + m*(xR - xF)
    parts.append(line(x0, yin, xL, yin))        # incoming parallelo
    parts.append(line(xL, yin, xF, yc))          # rifrazione -> fuoco
    parts.append(line(xF, yc, xR, yout))         # divergenza

# lente biconvessa (due archi)
top, bot = 96, 416
b = 130   # offset controllo -> bulge ~ b/2
lens = (f'<path d="M {xL},{top} Q {xL-b},{yc} {xL},{bot} Q {xL+b},{yc} {xL},{top} Z" '
        f'fill="none" stroke="{GOLD}" stroke-width="2.8" stroke-linejoin="round"/>')
parts.append(lens)

# punto fuoco
parts.append(f'<circle cx="{xF}" cy="{yc}" r="3.6" fill="{GOLD}"/>')

# wordmark LENS
parts.append(f'<text x="1716" y="283" fill="{GOLD}" font-family="Helvetica, Arial, sans-serif" '
             f'font-size="80" letter-spacing="14" font-weight="400">LENS</text>')

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + '</svg>'
open("assets/lens-banner.svg","w").write(svg)
print("svg scritto")
