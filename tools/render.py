#!/usr/bin/env python3
"""Render the 20 November 2026 world-news front page (1024x1024 PNG).

REVISED: fixes the draft's layout bugs — hero explosion bursts no longer
overlap the headline (moved down beside the bridges), the 2x2 grid rows are
taller with shorter body copy so no text crosses a panel border, and the
EU-UK / COP31 strip copy fits inside its boxes. Deterministic: no
timestamps, no randomness, no network. Run: python3 tools/render.py
writes entry.png next to this script's parent directory.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "entry.png")

PAPER = (246, 241, 229)
INK = (17, 17, 17)
RED = (163, 22, 33)
NAVY = (27, 42, 74)
GREY = (90, 88, 80)
LIGHT = (255, 255, 255)
HERO_BG = (28, 30, 40)
ORANGE = (255, 150, 40)
YELLOW = (255, 210, 60)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, max_w, text, fnt, fill=INK, leading=1.25):
    lines = wrap(draw, text, fnt, max_w)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def rule(draw, x0, y, x1, wdt=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def burst(d, ex, ey, r):
    """Explosion starburst; kept low in the hero so it never covers text."""
    for k in range(8):
        a = math.pi * k / 4
        d.line([(ex, ey), (ex + int(r * 1.5 * math.cos(a)),
                           ey + int(r * 1.5 * math.sin(a)))],
               fill=ORANGE, width=5)
    d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=ORANGE)
    d.ellipse([ex - r // 2, ey - r // 2, ex + r // 2, ey + r // 2], fill=YELLOW)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- masthead ----
    d.rectangle([10, 10, W - 11, 96], fill=NAVY)
    d.text((512, 30), "THE WORLD IN ONE IMAGE", font=font(SERIF_B, 44),
           fill=LIGHT, anchor="ma")
    d.text((512, 74), "A NEWSPAPER OF FRIDAY'S NEWS  •  ONE PAGE, THE WHOLE WORLD",
           font=font(SANS, 15), fill=(200, 205, 220), anchor="ma")

    # ---- date line ----
    d.text((512, 108), "FRIDAY 20 NOVEMBER 2026", font=font(SERIF_B, 46),
           fill=RED, anchor="ma")
    rule(d, 60, 164, 964, 2)
    rule(d, 60, 168, 964, 1)

    # ---- hero: Kyiv under fire ----
    hx0, hy0, hx1, hy1 = 24, 178, 1000, 440
    d.rectangle([hx0, hy0, hx1, hy1], fill=HERO_BG)
    # river + bridges silhouette (low, below the text)
    d.rectangle([hx0, 384, hx1, hy1], fill=(52, 68, 96))
    for bx in (180, 500, 820):
        d.arc([bx - 110, 322, bx + 110, 462], start=180, end=360,
              fill=(140, 150, 170), width=6)
        d.line([(bx - 110, 392), (bx + 110, 392)], fill=(140, 150, 170), width=4)
    # bursts sit between the bridges, clear of every text line
    burst(d, 340, 350, 26)
    burst(d, 660, 340, 30)
    burst(d, 940, 352, 22)
    d.text((512, 190), "KYIV UNDER FIRE", font=font(SERIF_B, 58),
           fill=LIGHT, anchor="ma", stroke_width=2, stroke_fill=HERO_BG)
    d.text((512, 260), "Russia's overnight missiles and drones hit three bridges",
           font=font(SANS_B, 24), fill=LIGHT, anchor="ma")
    d.text((512, 292), "over the Dnipro — 9 killed",
           font=font(SANS_B, 24), fill=LIGHT, anchor="ma")
    d.text((512, 404), "Missiles fall in Poland  •  Ukraine says Kerch Bridge road span is down",
           font=font(SANS, 19), fill=(220, 225, 235), anchor="ma")

    # ---- 2x2 grid (rows tall enough for headline + 3 body lines) ----
    panels = [
        ("SHENZHEN SUMMIT", RED, "Trump, Xi & Putin: joint peace declaration",
         "First-ever three-way meeting. Germany rejects a 'new Yalta' over Europe's "
         "future; US and China agree humans keep control of military AI."),
        ("ICJ GENOCIDE RULING", NAVY, "Myanmar guilty of genocide",
         "The World Court finds Myanmar responsible for genocide against the Rohingya "
         "in the 2017 campaign — the first such ruling against a state."),
        ("GAZA & THE GULF", RED, "Israel crosses ceasefire line",
         "Israeli forces push past the Yellow Line in central Gaza. A Houthi missile "
         "damages Riyadh's PIF tower; tanker attacks surge in the Strait of Hormuz."),
        ("MARKETS & TECH", NAVY, "Stocks fall, GTA VI makes $3.79bn",
         "S&P 500 down 2% for a fifth straight day, Nikkei -4.8% after Anthropic's "
         "IPO. White House fires its cyber chief after a wave of tech outages."),
    ]
    boxes = [(24, 452, 504, 608), (520, 452, 1000, 608),
             (24, 616, 504, 772), (520, 616, 1000, 772)]
    for (x0, y0, x1, y1), (kick, col, head, body) in zip(boxes, panels):
        d.rectangle([x0, y0, x1, y1], outline=INK, width=2)
        d.rectangle([x0, y0, x1, y0 + 28], fill=col)
        d.text((x0 + 12, y0 + 4), kick, font=font(SANS_B, 16), fill=LIGHT)
        y = para(d, x0 + 12, y0 + 36, x1 - x0 - 24, head,
                 font(SERIF_B, 25), leading=1.12)
        para(d, x0 + 12, y + 4, x1 - x0 - 24, body, font(SANS, 17), leading=1.28)

    # ---- EU-UK + COP31 strip ----
    sy0, sy1 = 784, 856
    d.rectangle([24, sy0, 500, sy1], outline=INK, width=2)
    d.text((36, sy0 + 6), "EU–UK RESET DEAL", font=font(SANS_B, 17), fill=RED)
    para(d, 36, sy0 + 30, 500 - 36 - 12,
         "Trade reset and youth mobility: ages 18–31, 100,000 places each side.",
         font(SANS, 17), leading=1.25)
    d.rectangle([524, sy0, 1000, sy1], outline=INK, width=2)
    d.text((536, sy0 + 6), "COP31 ANTALYA", font=font(SANS_B, 17), fill=NAVY)
    para(d, 536, sy0 + 30, 1000 - 536 - 12,
         "Draft deal drops any call to phase out fossil fuels.",
         font(SANS, 17), leading=1.25)

    # ---- ALSO TODAY ----
    ay0 = 868
    d.text((512, ay0), "ALSO TODAY", font=font(SANS_B, 18), fill=INK, anchor="ma")
    rule(d, 380, ay0 + 26, 644, 1)
    also = ("Haiti: 34 suspected gang members killed  •  Bukele registers for a third term in "
            "El Salvador  •  Migrant boat sinks off Senegal, dozens missing  •  Drone strike kills "
            "10 at a gold mine in Sudan  •  US–Venezuela sign military cooperation deal  •  "
            "Indonesia wildfire losses top $30bn  •  Trump pardons Pete Rose")
    para(d, 40, ay0 + 34, 944, also, font(SANS, 16), fill=GREY, leading=1.3)

    # ---- footer ----
    rule(d, 24, 986, 1000, 1)
    d.text((512, 992), "Sources: AP · Reuters · UN News · Euronews · OneTurn · Open Chronicle  •  make.fun/news-image-20261120",
           font=font(SANS, 13), fill=GREY, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
