"""2D cartoon 'story series' reel (owner, 23 Nov; inspired by the flat-cartoon money reels that do well in Kerala).
Flow: hook + short story between 2-3 characters -> breakdown card (where it went wrong, row by row)
-> the mentor's rules (Rule #1, #2...) -> episode ribbon + the usual keyword end card.
The cast is never fixed: each reel draws its people from a pool of types (appooppan, auntie, young man / woman,
uncle, student, NRI, shop owner) with random skin, clothes, hair and specs, matched to the script's names by gender."""
import math, os, random
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say, voice_for, is_female

SS = 2   # draw at 2x, shrink for smooth edges
SKINS = [(242, 200, 166), (236, 188, 150), (222, 172, 132), (214, 160, 120), (198, 144, 104), (190, 135, 95), (172, 118, 80), (160, 108, 72), (146, 96, 64), (132, 86, 58)]
SHIRTS = [(242, 242, 238), (56, 118, 204), (214, 64, 72), (246, 190, 52), (70, 160, 110), (136, 90, 168), (232, 130, 80), (40, 44, 56), (120, 196, 230), (250, 160, 180),
          (30, 90, 80), (150, 40, 60), (200, 210, 90), (90, 70, 140), (245, 225, 190), (110, 150, 200), (220, 100, 140), (60, 140, 160)]
PANTS = [(46, 52, 70), (60, 80, 130), (92, 70, 52), (70, 72, 78), (120, 100, 70), (40, 40, 44), (90, 110, 150)]
SAREES = [(214, 64, 72), (40, 140, 120), (246, 190, 52), (136, 90, 168), (232, 120, 150), (60, 110, 200), (250, 140, 60), (120, 40, 80), (60, 160, 90), (90, 200, 210), (200, 80, 40)]
SCARVES = [(40, 50, 90), (120, 40, 70), (60, 110, 100), (180, 150, 120), (90, 90, 100), (200, 120, 140)]
HAIR, GREY = (28, 24, 24), (196, 196, 192)

# person types; "f" = female. Mentors are usually the elders.
TYPES = {
    "elder":      dict(f=False, hair="bald", grey=True, must=True, specs=0.6, wear="mundu", shirt="white", h=1.0),
    "uncle":      dict(f=False, hair="short", grey=False, must=True, specs=0.3, wear="mundu", belly=True, h=0.98),
    "young_man":  dict(f=False, hair="puff", must=False, beard=0.35, wear="pants", h=1.0),
    "student_m":  dict(f=False, hair="puff", must=False, wear="pants", bag=True, h=0.94),
    "nri":        dict(f=False, hair="short", must=True, specs=0.5, wear="pants", tuck=True, h=1.0),
    "shopkeeper": dict(f=False, hair="short", must=True, wear="mundu", towel=True, belly=True, h=0.98),
    "ammachi":    dict(f=True, hair="bun", grey=True, specs=0.7, wear="saree", h=0.95),
    "auntie":     dict(f=True, hair="bun", wear="saree", h=0.97),
    "young_woman":dict(f=True, hair="long", wear="churidar", h=0.97),
    "student_f":  dict(f=True, hair="braid", wear="churidar", bag=True, h=0.93),
    "pro_woman":  dict(f=True, hair="bob", specs=0.4, wear="pants", h=0.98),
    "farmer":     dict(f=False, hair="short", grey=False, must=True, wear="lungi", towel_head=True, h=0.97),
    "fisherman":  dict(f=False, hair="short", must=True, beard=0.4, wear="lungi", towel=True, h=0.98),
    "auto_driver":dict(f=False, hair="short", must=True, wear="pants", khaki=True, h=0.99),
    "chef":       dict(f=False, hair="short", must=0.5, wear="pants", apron=True, chef_cap=True, h=1.0),
    "doctor_m":   dict(f=False, hair="short", specs=0.5, wear="pants", coat=True, h=1.0),
    "it_pro":     dict(f=False, hair="puff", beard=0.5, wear="pants", lanyard=True, h=1.0),
    "gulf_returnee": dict(f=False, hair="short", must=True, wear="pants", shades=True, tuck=True, belly=True, h=0.99),
    "hijab_woman":dict(f=True, hair="none", hijab=True, wear="churidar", h=0.96),
    "teacher_f":  dict(f=True, hair="bun", specs=0.7, wear="saree", bag=True, h=0.96),
    "doctor_f":   dict(f=True, hair="bun", specs=0.4, wear="churidar", coat=True, h=0.97),
    "college_girl": dict(f=True, hair="long", wear="pants", bag=True, h=0.94),
    "ammachi_kasavu": dict(f=True, hair="bun", grey=True, specs=0.5, wear="kasavu", h=0.94),
}
MALE_T = ["young_man", "uncle", "student_m", "nri", "shopkeeper", "elder", "farmer", "fisherman", "auto_driver", "chef", "doctor_m", "it_pro", "gulf_returnee"]
FEMALE_T = ["young_woman", "auntie", "student_f", "pro_woman", "ammachi", "hijab_woman", "teacher_f", "doctor_f", "college_girl", "ammachi_kasavu"]

def make_look(kind, rng):
    t = dict(TYPES[kind]); t["kind"] = kind
    t["skin"] = SKINS[rng.integers(len(SKINS))]
    t["shirt_c"] = (242, 242, 238) if t.get("shirt") == "white" else SHIRTS[rng.integers(len(SHIRTS))]
    t["pant_c"] = PANTS[rng.integers(len(PANTS))]
    t["saree_c"] = SAREES[rng.integers(len(SAREES))]
    t["specs"] = rng.random() < t.get("specs", 0.0)
    t["beard"] = rng.random() < t.get("beard", 0.0)
    t["hair_c"] = GREY if t.get("grey") else HAIR
    if t.get("khaki"): t["shirt_c"] = (196, 170, 110)
    t["check"] = not t.get("coat") and not t.get("khaki") and t["wear"] not in ("saree", "kasavu") and rng.random() < 0.3        # checked shirt
    t["pottu"] = t["f"] and not t.get("hijab") and rng.random() < 0.6
    t["scarf_c"] = SCARVES[rng.integers(len(SCARVES))]
    if isinstance(t.get("must"), float): t["must"] = rng.random() < t["must"]
    return t

# ---------------- person drawing (2x canvas, 460 x 980 at 1x) ----------------
PW, PH = 460, 980
def person(L, mouth=0.0, blink=False):
    s = SS; im = Image.new("RGBA", (PW * s, PH * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    S = lambda *v: [int(x * s) for x in v]
    sk, sh, hc = L["skin"], L["shirt_c"], L["hair_c"]; dk = tuple(int(c * 0.78) for c in sk)
    cx = PW // 2; top = int(PH * (1 - L["h"]))           # shorter people start lower
    hy = top + 150                                       # head centre
    # legs / lower garment
    if L["wear"] == "mundu":
        d.polygon(S(cx - 95, 560, cx + 95, 560, cx + 110, 930, cx - 110, 930), fill=(248, 246, 236))
        d.rectangle(S(cx - 112, 905, cx + 112, 930), fill=(214, 170, 60))
        d.line(S(cx + 10, 570, cx + 30, 905), fill=(222, 220, 210), width=4 * s)
        for x in (-50, 50): d.rounded_rectangle(S(cx + x - 30, 925, cx + x + 34, 958), 12 * s, fill=(90, 60, 40))
    elif L["wear"] == "lungi":   # folded checked lungi above the knee
        c = L["pant_c"] if L["kind"] == "farmer" else (60, 90, 160)
        d.polygon(S(cx - 95, 560, cx + 95, 560, cx + 104, 760, cx - 104, 760), fill=c)
        for k in range(6): d.line(S(cx - 95 + k * 38, 560, cx - 100 + k * 40, 760), fill=(240, 240, 240), width=3 * s)
        d.line(S(cx - 100, 640, cx + 100, 640), fill=(240, 240, 240), width=3 * s)
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 26, 750, cx + x + 26, 935), 14 * s, fill=sk)
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 30, 925, cx + x + 34, 958), 12 * s, fill=(90, 60, 40))
    elif L["wear"] == "kasavu":   # white set-saree with a gold border
        d.polygon(S(cx - 100, 540, cx + 100, 540, cx + 125, 935, cx - 125, 935), fill=(250, 246, 232))
        d.rectangle(S(cx - 126, 900, cx + 126, 935), fill=(214, 170, 60)); d.polygon(S(cx - 100, 300, cx - 40, 300, cx + 100, 600, cx + 60, 640), fill=(250, 246, 232))
        d.line(S(cx - 40, 300, cx + 100, 600), fill=(214, 170, 60), width=8 * s)
        for x in (-45, 45): d.rounded_rectangle(S(cx + x - 28, 935, cx + x + 32, 962), 12 * s, fill=(110, 60, 50))
    elif L["wear"] in ("saree", "churidar"):
        c = L["saree_c"]; cc = tuple(min(255, int(v * 1.15)) for v in c)
        d.polygon(S(cx - 100, 540, cx + 100, 540, cx + 125, 935, cx - 125, 935), fill=c if L["wear"] == "saree" else cc)
        if L["wear"] == "saree": d.rectangle(S(cx - 126, 905, cx + 126, 935), fill=(230, 180, 60)); d.polygon(S(cx - 100, 300, cx - 40, 300, cx + 100, 600, cx + 60, 640), fill=c)
        else:
            for x in (-45, 45): d.rectangle(S(cx + x - 26, 880, cx + x + 26, 945), fill=(245, 240, 230))
        for x in (-45, 45): d.rounded_rectangle(S(cx + x - 28, 935, cx + x + 32, 962), 12 * s, fill=(110, 60, 50))
    else:   # pants
        pc = L["pant_c"]
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 44, 540, cx + x + 44, 935), 20 * s, fill=pc)
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 46, 925, cx + x + 52, 960), 14 * s, fill=(50, 40, 36))
    # torso
    bw = 128 if L.get("belly") else 112
    top_c = sh if L["wear"] not in ("saree", "kasavu") else (L["saree_c"] if L["wear"] == "saree" else (250, 246, 232))
    d.rounded_rectangle(S(cx - bw, 280, cx + bw, 580), 60 * s, fill=top_c)
    if L.get("check"):
        lc = tuple(max(0, int(c * 0.72)) for c in sh)
        for k in range(1, 6): d.line(S(cx - bw + k * bw // 3, 290, cx - bw + k * bw // 3, 570), fill=lc, width=3 * s); d.line(S(cx - bw + 10, 280 + k * 50, cx + bw - 10, 280 + k * 50), fill=lc, width=3 * s)
    if L.get("belly"): d.ellipse(S(cx - bw + 6, 380, cx + bw - 6, 600), fill=sh)
    if L["wear"] == "pants" and not L["f"]:
        d.rectangle(S(cx - bw + 10, 540, cx + bw - 10, 560), fill=(40, 36, 34))
        for y in (340, 400, 460): d.ellipse(S(cx - 5, y, cx + 5, y + 10), fill=tuple(int(c * 0.7) for c in sh))
        d.polygon(S(cx - 40, 282, cx, 330, cx + 40, 282), fill=tuple(min(255, int(c * 1.1) + 20) for c in sh))
    if L["wear"] == "churidar": d.polygon(S(cx - 120, 300, cx - 60, 290, cx + 110, 520, cx + 70, 540), fill=(250, 236, 200))   # dupatta
    if L.get("towel"): d.polygon(S(cx - 115, 290, cx - 60, 285, cx - 20, 560, cx - 70, 560), fill=(250, 250, 245)); d.line(S(cx - 112, 300, cx - 66, 560), fill=(200, 60, 60), width=5 * s)
    if L.get("coat"):
        for side in (-1, 1): d.polygon(S(cx + side * 10, 285, cx + side * (bw + 6), 290, cx + side * (bw + 10), 640, cx + side * 30, 640), fill=(250, 250, 252))
        d.line(S(cx - 60, 380, cx - 30, 470), fill=(60, 140, 180), width=4 * s)            # pen in the pocket
    if L.get("apron"): d.rounded_rectangle(S(cx - 80, 330, cx + 80, 700), 20 * s, fill=(250, 250, 248)); d.line(S(cx - 60, 330, cx - 30, 280), fill=(250, 250, 248), width=6 * s); d.line(S(cx + 60, 330, cx + 30, 280), fill=(250, 250, 248), width=6 * s)
    if L.get("lanyard"): d.line(S(cx - 40, 285, cx, 420), fill=(40, 90, 200), width=5 * s); d.line(S(cx + 40, 285, cx, 420), fill=(40, 90, 200), width=5 * s); d.rounded_rectangle(S(cx - 28, 420, cx + 28, 490), 6 * s, fill=(250, 250, 250), outline=(40, 90, 200), width=3 * s)
    if L.get("bag"): d.rounded_rectangle(S(cx + bw - 20, 300, cx + bw + 40, 500), 18 * s, fill=(60, 90, 160))
    # arms
    for side in (-1, 1):
        x0 = cx + side * (bw - 14)
        d.rounded_rectangle(S(min(x0, x0 + side * 52), 300, max(x0, x0 + side * 52), 470), 26 * s, fill=sh if L["wear"] not in ("saree", "kasavu") else sk)
        d.rounded_rectangle(S(min(x0, x0 + side * 48) + 2, 450, max(x0, x0 + side * 48) - 2, 560), 22 * s, fill=sk)
        d.ellipse(S(x0 + side * 24 - 30, 540, x0 + side * 24 + 30, 600), fill=sk)
    # neck + head
    d.rectangle(S(cx - 30, 230, cx + 30, 300), fill=dk)
    if L["hair"] in ("long", "braid"):   # hair falls behind the head and down both sides, never over the chin
        d.rounded_rectangle(S(cx - 112, hy - 70, cx + 112, hy + 60), 60 * s, fill=hc)
        if L["hair"] == "long":
            for side in (-1, 1): d.rounded_rectangle(S(cx + side * 112 - (0 if side < 0 else 46), hy - 20, cx + side * 112 + (46 if side < 0 else 0), hy + 230), 22 * s, fill=hc)
    if L["hair"] == "braid": d.rounded_rectangle(S(cx + 70, hy + 60, cx + 110, hy + 330), 18 * s, fill=hc)
    for side in (-1, 1): d.ellipse(S(cx + side * 102 - 18, hy - 10, cx + side * 102 + 18, hy + 40), fill=sk)   # ears
    if L.get("hijab"):
        sc = L["scarf_c"]; d.polygon(S(cx - 125, hy + 40, cx + 125, hy + 40, cx + 150, 330, cx - 150, 330), fill=sc)
        d.ellipse(S(cx - 126, hy - 140, cx + 126, hy + 130), fill=sc)
    d.ellipse(S(cx - 100, hy - 120, cx + 100, hy + 110) if not L.get("hijab") else S(cx - 88, hy - 96, cx + 88, hy + 108), fill=sk)
    if L["hair"] == "bald":
        for side in (-1, 1): d.chord(S(cx + side * 60 - 50, hy - 70, cx + side * 60 + 50, hy + 20), 90 if side > 0 else 270, 270 if side > 0 else 90, fill=hc)
        d.pieslice(S(cx - 100, hy - 120, cx + 100, hy + 80), 200, 340, fill=sk)
    elif L["hair"] == "puff":
        d.ellipse(S(cx - 108, hy - 150, cx + 108, hy - 10), fill=hc); d.ellipse(S(cx - 60, hy - 175, cx + 70, hy - 80), fill=hc)
        d.rectangle(S(cx - 104, hy - 60, cx - 84, hy + 10), fill=hc); d.rectangle(S(cx + 84, hy - 60, cx + 104, hy + 10), fill=hc)
    elif L["hair"] == "short":
        d.chord(S(cx - 106, hy - 135, cx + 106, hy + 30), 180, 360, fill=hc)
        d.rectangle(S(cx - 104, hy - 45, cx - 84, hy + 10), fill=hc); d.rectangle(S(cx + 84, hy - 45, cx + 104, hy + 10), fill=hc)
    elif L["hair"] == "bun":
        d.chord(S(cx - 106, hy - 128, cx + 106, hy + 40), 180, 360, fill=hc); d.ellipse(S(cx - 50, hy - 190, cx + 50, hy - 100), fill=hc)
        d.line(S(cx, hy - 122, cx, hy - 60), fill=tuple(min(255, c + 30) for c in hc), width=4 * s)
    elif L["hair"] == "bob":
        d.chord(S(cx - 114, hy - 130, cx + 114, hy + 120), 180, 360, fill=hc); d.rectangle(S(cx - 114, hy - 10, cx - 80, hy + 70), fill=hc); d.rectangle(S(cx + 80, hy - 10, cx + 114, hy + 70), fill=hc)
    elif L["hair"] != "none":   # long / braid: fringe on top
        d.chord(S(cx - 106, hy - 128, cx + 106, hy + 30), 180, 360, fill=hc)
    if L.get("hijab"): d.chord(S(cx - 92, hy - 104, cx + 92, hy + 10), 180, 360, fill=L["scarf_c"])     # the scarf frames the forehead
    if L.get("towel_head"): d.rounded_rectangle(S(cx - 110, hy - 105, cx + 110, hy - 55), 22 * s, fill=(250, 250, 245)); d.line(S(cx - 106, hy - 80, cx + 106, hy - 80), fill=(200, 60, 60), width=4 * s)
    if L.get("chef_cap"): d.rounded_rectangle(S(cx - 80, hy - 150, cx + 80, hy - 95), 10 * s, fill=(252, 252, 252)); [d.ellipse(S(cx + x - 55, hy - 230, cx + x + 55, hy - 120), fill=(252, 252, 252)) for x in (-45, 0, 45)]
    # face
    ey = hy + 5
    for side in (-1, 1):
        ex = cx + side * 38
        if blink: d.line(S(ex - 16, ey, ex + 16, ey), fill=(30, 26, 26), width=5 * s)
        else: d.ellipse(S(ex - 18, ey - 20, ex + 18, ey + 20), fill=(255, 255, 255)); d.ellipse(S(ex - 9, ey - 8, ex + 9, ey + 12), fill=(30, 26, 26))
        d.line(S(ex - 20, ey - 36, ex + 18, ey - 40 + side * 2), fill=tuple(int(c * 0.9) for c in hc) if L["hair"] != "bald" else (90, 90, 90), width=7 * s)
    if L["f"] and L.get("pottu"): d.ellipse(S(cx - 7, ey - 62, cx + 7, ey - 48), fill=(200, 40, 50))     # bindi / pottu (some women, never with a hijab)
    d.polygon(S(cx, ey + 6, cx - 12, ey + 42, cx + 10, ey + 44), fill=dk)              # nose
    my = ey + 68
    if L.get("beard"): d.chord(S(cx - 92, hy - 10, cx + 92, hy + 128), 0, 180, fill=hc)
    if L.get("must"): d.chord(S(cx - 44, my - 26, cx + 44, my + 6), 180, 360, fill=hc)
    if mouth > 0.15:
        o = int(10 + 22 * mouth); d.ellipse(S(cx - 24, my - 4, cx + 24, my + o), fill=(110, 30, 40)); d.ellipse(S(cx - 12, my + o - 12, cx + 12, my + o), fill=(220, 100, 110))
    else: d.arc(S(cx - 26, my - 18, cx + 26, my + 10), 20, 160, fill=(110, 40, 40), width=5 * s)
    if L.get("shades"):
        for side in (-1, 1): d.rounded_rectangle(S(cx + side * 38 - 32, ey - 22, cx + side * 38 + 32, ey + 20), 14 * s, fill=(30, 30, 36))
        d.line(S(cx - 8, ey - 6, cx + 8, ey - 6), fill=(30, 30, 36), width=5 * s)
    elif L.get("specs"):
        for side in (-1, 1): d.rounded_rectangle(S(cx + side * 38 - 30, ey - 26, cx + side * 38 + 30, ey + 24), 12 * s, outline=(30, 30, 34), width=5 * s)
        d.line(S(cx - 8, ey - 4, cx + 8, ey - 4), fill=(30, 30, 34), width=5 * s)
    return im.resize((PW, PH), Image.LANCZOS)

# ---------------- backgrounds ----------------
def palm(d, x, y, h, rng):
    for k in range(24): d.ellipse([x + math.sin(k / 6) * 14 - 13, y - k * h / 24 - 13, x + math.sin(k / 6) * 14 + 13, y - k * h / 24 + 13], fill=(140, 104, 70))
    tx, ty = x + math.sin(4) * 14, y - h
    for a in range(0, 360, 40):
        r = math.radians(a + rng.integers(-10, 10)); ex, ey = tx + math.cos(r) * 170, ty + math.sin(r) * 80 + 40
        d.polygon([tx, ty, ex, ey, (tx + ex) / 2 + 20, (ty + ey) / 2 + 26], fill=(54, 140, 70))
INDOOR = ("office", "home", "shop", "bank", "hospital", "college", "cafe", "kitchen", "gulf_office")
# a script's scene stands for a family of look-alike places, so the same script type doesn't always get the same backdrop
SCENE_GROUPS = {
    "teashop": ["teashop", "market", "ksrtc", "paddy", "backwater", "road", "beach"],
    "busstop": ["busstop", "railway", "ksrtc", "road", "market"],
    "road": ["road", "paddy", "backwater", "beach", "rooftop"],
    "home": ["home", "kitchen", "rooftop"],
    "office": ["office", "bank", "college", "cafe", "hospital", "gulf_office"],
    "shop": ["shop", "market", "cafe"],
    "classroom": ["college", "office"],
}
def _sky(d, top, horizon=1240):
    for y in range(0, horizon, 4): k = y / horizon; d.rectangle([0, y, W, y + 4], fill=tuple(int(top[i] * (1 - k * 0.3) + 255 * k * 0.3) for i in range(3)))
def _clouds(d, rng, n=3, night=False):
    for k in range(n):
        cx, cy = rng.integers(80, 1000), rng.integers(560, 900)
        for j in range(3): d.ellipse([cx + j * 50 - 70, cy - 30 - (j % 2) * 20, cx + j * 50 + 70, cy + 40], fill=(90, 100, 140) if night else (255, 255, 255))
def _floor(d, col, line):
    d.rectangle([0, 1420, W, H], fill=col)
    for x in range(0, W + 200, 120): d.line([x, 1420, x - 160, H], fill=line, width=3)
def _window(d, x0, y0, x1, y1, glass=(170, 214, 240)):
    d.rounded_rectangle([x0, y0, x1, y1], 10, fill=glass, outline=(255, 255, 255), width=18); d.line([(x0 + x1) // 2, y0, (x0 + x1) // 2, y1], fill=(255, 255, 255), width=10)
def background(scene, rng):
    im = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(im)
    pick = lambda a: a[rng.integers(len(a))]
    if scene in INDOOR:
        wall = pick([(246, 232, 200), (214, 232, 240), (240, 220, 226), (224, 238, 214), (236, 226, 246), (250, 240, 214), (220, 228, 236)])
        d.rectangle([0, 0, W, 1420], fill=wall)
        wood, tile = ((196, 160, 120), (180, 146, 110)), ((190, 196, 204), (176, 182, 190))
        _floor(d, *(tile if scene in ("office", "bank", "hospital", "college", "gulf_office") else wood))
        if scene == "office": _window(d, 90, 720, 470, 1080); d.rectangle([600, 1150, 1040, 1190], fill=(150, 110, 80)); d.rounded_rectangle([700, 960, 940, 1140], 12, fill=(40, 44, 52))
        elif scene == "home": _window(d, 90, 720, 470, 1080); d.rounded_rectangle([560, 1180, 1060, 1400], 40, fill=pick([(120, 80, 140), (60, 120, 160), (180, 90, 70), (70, 130, 90)])); d.rectangle([620, 760, 920, 980], fill=(200, 160, 90), outline=(120, 90, 60), width=10)
        elif scene == "shop":
            for k in range(3): d.rectangle([60, 760 + k * 170, 1060, 780 + k * 170], fill=(150, 110, 80))
            for k in range(26): d.rounded_rectangle([80 + (k % 13) * 76, 690 + (k // 13) * 170, 130 + (k % 13) * 76, 760 + (k // 13) * 170], 8, fill=pick(SHIRTS))
        elif scene == "bank":
            d.rectangle([0, 1100, W, 1420], fill=(150, 110, 80)); d.rectangle([0, 760, W, 1100], fill=(210, 230, 240))
            for x in range(0, W, 270): d.rectangle([x, 760, x + 12, 1100], fill=(160, 170, 180))
            d.rounded_rectangle([340, 600, 740, 690], 14, fill=(30, 80, 150))
        elif scene == "hospital":
            d.rectangle([0, 1000, W, 1040], fill=(120, 190, 200)); _window(d, 640, 700, 1000, 1000, (200, 230, 240))
            d.rounded_rectangle([120, 720, 360, 960], 20, fill=(255, 255, 255)); d.rectangle([215, 760, 265, 920], fill=(220, 60, 60)); d.rectangle([160, 815, 320, 865], fill=(220, 60, 60))
        elif scene == "college":
            d.rounded_rectangle([140, 640, 940, 1000], 16, fill=(40, 70, 60), outline=(150, 110, 80), width=20)
            for k in range(3): d.line([200, 720 + k * 80, 200 + rng.integers(300, 600), 720 + k * 80], fill=(230, 230, 220), width=8)
        elif scene == "cafe":
            for x in (200, 540, 880): d.line([x, 0, x, 620], fill=(60, 60, 60), width=4); d.pieslice([x - 70, 560, x + 70, 700], 180, 360, fill=(240, 180, 60))
            d.rectangle([0, 1180, W, 1420], fill=(120, 80, 50)); d.rounded_rectangle([640, 760, 1000, 1000], 20, fill=(40, 40, 40))
        elif scene == "kitchen":
            d.rectangle([0, 1120, W, 1420], fill=(220, 220, 214)); d.rectangle([0, 1100, W, 1130], fill=(90, 90, 96))
            for k in range(4): d.ellipse([140 + k * 220, 1040, 260 + k * 220, 1110], fill=pick([(180, 60, 40), (60, 60, 70), (200, 160, 60)]))
            _window(d, 360, 640, 720, 940, (190, 230, 200))
        else:   # gulf office: tall glass and a skyline
            d.rectangle([60, 600, 1020, 1200], fill=(210, 220, 230))
            for k in range(9): hh = rng.integers(200, 520); d.rectangle([80 + k * 104, 1200 - hh, 160 + k * 104, 1200], fill=(150, 170, 190))
            for x in range(60, 1020, 240): d.rectangle([x, 600, x + 14, 1200], fill=(255, 255, 255))
        return im
    night = scene == "rooftop"
    _sky(d, (40, 50, 100) if night else pick([(150, 210, 245), (170, 220, 250), (250, 200, 160), (130, 200, 240), (255, 190, 140)]))
    if night:
        for k in range(40): x, y = rng.integers(0, W), rng.integers(0, 900); d.ellipse([x, y, x + 5, y + 5], fill=(255, 250, 220))
        d.ellipse([820, 220, 940, 340], fill=(255, 245, 200))
    _clouds(d, rng, 3, night)
    ground = {"beach": (236, 214, 160), "backwater": (92, 160, 80), "paddy": (120, 180, 70), "rooftop": (150, 140, 140)}.get(scene, (196, 138, 90))
    d.rectangle([0, 1240, W, H], fill=ground)
    if scene not in ("rooftop", "beach"): d.rectangle([0, 1200, W, 1250], fill=(92, 160, 80))
    if scene not in ("rooftop",):
        for x in pick([(60, 1000), (140, 940), (40, 820), (260, 1040)]): palm(d, x, 1260, int(rng.integers(440, 560)), rng)
    if scene == "teashop":
        d.rectangle([300, 860, 1000, 1260], fill=(236, 214, 170)); d.polygon([260, 880, 650, 720, 1040, 880], fill=(186, 72, 52))
        d.rectangle([360, 940, 940, 1010], fill=(250, 240, 220)); d.rectangle([360, 1060, 940, 1110], fill=(120, 80, 50))
        for k in range(5): d.ellipse([400 + k * 100, 1020, 450 + k * 100, 1058], fill=(250, 250, 250))
    elif scene == "busstop":
        d.rectangle([260, 900, 280, 1260], fill=(120, 120, 130)); d.rectangle([800, 900, 820, 1260], fill=(120, 120, 130)); d.polygon([220, 900, 860, 900, 820, 840, 260, 840], fill=(52, 120, 180))
        d.rectangle([300, 1130, 780, 1160], fill=(150, 110, 70)); d.rounded_rectangle([880, 960, 1040, 1040], 10, fill=(240, 240, 240)); d.rectangle([955, 1040, 965, 1260], fill=(120, 120, 130))
    elif scene == "ksrtc":
        d.rounded_rectangle([120, 900, 960, 1220], 30, fill=(200, 40, 40)); d.rectangle([120, 1100, 960, 1130], fill=(250, 220, 60))
        for k in range(6): d.rectangle([160 + k * 130, 950, 260 + k * 130, 1060], fill=(170, 214, 240))
        for x in (260, 820): d.ellipse([x - 60, 1170, x + 60, 1290], fill=(30, 30, 30))
    elif scene == "railway":
        d.rectangle([0, 1080, W, 1250], fill=(170, 160, 150)); d.rectangle([0, 860, W, 900], fill=(200, 170, 60)); d.rectangle([0, 900, W, 920], fill=(120, 60, 40))
        for x in (120, 960): d.rectangle([x, 900, x + 20, 1080], fill=(90, 90, 100))
        d.rounded_rectangle([380, 940, 700, 1010], 10, fill=(250, 220, 60))
    elif scene == "market":
        for k in range(3):
            x = 60 + k * 340; c = pick([(214, 64, 72), (40, 140, 120), (60, 110, 200), (246, 190, 52)])
            d.polygon([x, 960, x + 160, 900, x + 320, 960], fill=c); d.rectangle([x + 10, 960, x + 310, 1180], fill=(230, 210, 170))
            for j in range(5): d.ellipse([x + 30 + j * 55, 1100, x + 75 + j * 55, 1145], fill=pick([(240, 120, 40), (90, 170, 60), (220, 50, 50), (250, 210, 60)]))
    elif scene == "paddy":
        for y in range(1250, H, 40): d.line([0, y, W, y], fill=(100, 160, 60), width=6)
        d.rectangle([700, 1000, 960, 1240], fill=(240, 230, 210)); d.polygon([670, 1020, 830, 920, 990, 1020], fill=(186, 72, 52))
    elif scene == "backwater":
        d.rectangle([0, 1150, W, 1260], fill=(70, 150, 190)); d.polygon([300, 1150, 820, 1150, 760, 1200, 360, 1200], fill=(120, 70, 40))
        d.pieslice([360, 1040, 760, 1220], 180, 360, fill=(200, 160, 90))
    elif scene == "beach":
        d.rectangle([0, 1080, W, 1240], fill=(60, 150, 200))
        for x in range(0, W, 120): d.arc([x, 1210, x + 120, 1270], 180, 360, fill=(255, 255, 255), width=6)
        d.polygon([700, 1080, 880, 1080, 860, 1110, 720, 1110], fill=(120, 70, 40))
    elif scene == "rooftop":
        for k in range(8): hh = rng.integers(160, 420); x = k * 140; d.rectangle([x, 1240 - hh, x + 120, 1240], fill=(50, 60, 90)); [d.rectangle([x + 20 + (j % 3) * 30, 1260 - hh + (j // 3) * 50, x + 36 + (j % 3) * 30, 1280 - hh + (j // 3) * 50], fill=(255, 220, 120)) for j in range(6)]
        d.rectangle([0, 1200, W, 1240], fill=(120, 110, 110))
    else:   # village road
        d.polygon([440, 1250, 640, 1250, 1000, H, 80, H], fill=(120, 120, 126)); d.rectangle([380, 980, 700, 1240], fill=(240, 230, 210)); d.polygon([350, 1000, 540, 880, 730, 1000], fill=(186, 72, 52))
    return im

# ---------------- reel ----------------
def mouth_track(wav, t0):
    """Per-frame mouth opening from the voice's loudness."""
    n = len(wav) // (SR // FPS); out = {}
    for i in range(n):
        seg = wav[i * (SR // FPS):(i + 1) * (SR // FPS)]; v = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0
        out[int(round(t0 * FPS)) + i] = min(1.0, v * 6)
    return out

def build(s, out, seed=0):
    rng = np.random.default_rng(abs(hash(s["id"])) % (2 ** 31) + seed)
    cast = s["cast"]                     # {"A": "name" or ("name", "type"), ...}
    people = {}
    used = set()
    for k, v in cast.items():
        nm, kind = (v if isinstance(v, (tuple, list)) else (v, None))
        if not kind and k == s.get("mentor", "B" if "B" in cast else None):
            kind = "ammachi" if is_female(nm) else "elder"        # the mentor is the appooppan / ammachi
        # a series keeps its people: the same name in the same series always looks the same; one-off reels vary
        import hashlib
        prng = np.random.default_rng(int(hashlib.md5(f"{s.get('series') or s['id']}|{nm}".encode()).hexdigest()[:8], 16))
        if not kind:
            pool = [t for t in (FEMALE_T if is_female(nm) else MALE_T) if t not in used and (t not in ("elder", "ammachi", "ammachi_kasavu") or k == s.get("mentor"))]
            kind = pool[prng.integers(len(pool))]
        used.add(kind); people[k] = dict(name=nm, look=make_look(kind, prng))
    keys = list(cast)
    voice = {k: voice_for(people[k]["name"], i) for i, k in enumerate(keys)}
    for i, k in enumerate(keys[1:], 1):
        if voice[k] == voice[keys[0]]: voice[k] = voice[k][0] + ("2" if voice[k][-1] != "2" else "1")
    full = {k: [person(p["look"], m) for m in (0.0, 0.5, 1.0)] + [person(p["look"], 0, True)] for k, p in people.items()}
    SC = 0.74 if len(cast) > 2 else 0.8; SPW, SPH = int(PW * SC), int(PH * SC)
    sprites = {k: [im.resize((SPW, SPH), Image.LANCZOS) for im in v] for k, v in full.items()}
    fam = SCENE_GROUPS.get(s.get("scene") or "teashop", [s.get("scene")]); bgname = fam[rng.integers(len(fam))]
    BG = background(bgname, rng)
    n = len(keys); xs = {k: int(W / (n + 1) * (i + 1) - SPW / 2) + (i - (n - 1) / 2) * 40 for i, k in enumerate(keys)}
    flip = {k: xs[k] + SPW / 2 > W / 2 + 10 for k in keys}                                   # people on the right face left
    for k in keys:
        if flip[k]: sprites[k] = [im.transpose(Image.FLIP_LEFT_RIGHT) for im in sprites[k]]

    aud, mouths, t = [], {}, 0.15
    hook_box = None
    if s.get("hook"):
        hb = fit_block(s["hook"], 70, (20, 20, 24), 860, 330); hook_box = rrect(hb.width + 40, hb.height + 20, 34, (255, 214, 64, 255)); hook_box.alpha_composite(hb, (20, 10))
    story = []
    for who, txt in s["lines"]:
        w = load_wav(say(txt, voice[who])); aud.append((t, w)); mouths.setdefault(who, {}).update(mouth_track(w, t))
        story.append(dict(who=who, txt=txt, t0=t, t1=t + len(w) / SR + 0.12)); t = story[-1]["t1"]
    t_story = t + 0.2
    card = s.get("card"); rows = []
    if card:
        t += 0.5; tw = load_wav(say(card["title"].replace("\n", " "), "NARRATOR")); aud.append((t, tw)); t_card = t; t += len(tw) / SR + 0.2
        for lab, val in card["rows"] + ([card["total"]] if card.get("total") else []):
            w = load_wav(say(f"{lab}, {val}", "NARRATOR")); aud.append((t, w)); rows.append(dict(lab=lab, val=val, t=t)); t += len(w) / SR + 0.25
        t_card_end = t + 0.4; t = t_card_end
    m = s.get("mentor", keys[0]); rules = []
    for i, r in enumerate(s.get("rules", [])):
        w = load_wav(say(r, voice[m])); t += 0.4; aud.append((t, w)); mouths.setdefault("R" + m, {}).update(mouth_track(w, t))
        rules.append(dict(n=i + 1, txt=r, t0=t, t1=t + len(w) / SR)); t = rules[-1]["t1"] + 0.3
    t_end = t + 0.3; DUR = t_end + 4.5

    END, PILL, (PX, PY) = end_card(s)
    if s.get("series"):
        rib = rrect(760, 96, 48, (204, 92, 52, 255)); tdraw(ImageDraw.Draw(rib), (760 - tlen(f"{s['series']} · Episode {s.get('ep', 1)}", 40)) / 2, 64, f"{s['series']} · Episode {s.get('ep', 1)}", 40, (255, 255, 255))
        END.alpha_composite(rib, ((W - 760) // 2, 220))
        if s.get("next"):
            nb = block("അടുത്ത എപ്പിസോഡ്: " + s["next"], 42, (204, 92, 52), maxw=900, wt=800); END.alpha_composite(nb, ((W - nb.width) // 2, 1560))
    subs = {}
    def sub_img(txt):
        if txt not in subs:
            b = fit_block(txt, 54, (255, 255, 255), 940, 250, stroke=7, sfill=(20, 20, 24)); subs[txt] = b
        return subs[txt]
    rule_bg = Image.new("RGBA", (W, H), (252, 246, 232, 255)); ImageDraw.Draw(rule_bg).ellipse([W / 2 - 300, 1290, W / 2 + 300, 1360], fill=(232, 222, 200))
    card_bg = Image.new("RGBA", (W, H), (250, 250, 252, 255))
    big_m = [im.resize((int(PW * 0.86), int(PH * 0.86)), Image.LANCZOS) for im in full[m]]
    if flip[m]: big_m = [im.transpose(Image.FLIP_LEFT_RIGHT) for im in big_m]
    small_m = [im.resize((int(PW * 0.5), int(PH * 0.5)), Image.LANCZOS).transpose(Image.FLIP_LEFT_RIGHT) for im in full[m][:1]]   # the mentor watches the card

    def mouth_at(k, fr): v = k.get(fr, 0); return 0 if v < 0.12 else (1 if v < 0.45 else 2)
    def frame(tt):
        fr = int(round(tt * FPS)); blink = (fr % 97) < 4
        if tt < t_story:
            im = BG.copy(); cur = next((x for x in story if x["t0"] <= tt < x["t1"]), story[-1] if tt >= story[-1]["t0"] else None)
            for k in keys:
                sp = sprites[k][3] if blink and not (cur and cur["who"] == k) else sprites[k][mouth_at(mouths.get(k, {}), fr)]
                hop = -10 * abs(math.sin(tt * 7)) if cur and cur["who"] == k else 0
                paste(im, sp, xs[k], 1600 - SPH + hop)
            if hook_box: paste(im, hook_box, (W - hook_box.width) // 2, 150)
            if cur:
                b = sub_img(cur["txt"]); paste(im, b, (W - b.width) // 2, 400 if hook_box is None else 150 + hook_box.height + 20)
                nm = people[cur["who"]]["name"]; tg = rrect(int(tlen(nm, 36)) + 40, 60, 30, (20, 20, 24, 220)); tdraw(ImageDraw.Draw(tg), 20, 43, nm, 36, (255, 214, 64))
                paste(im, tg, xs[cur["who"]] + SPW // 2 - tg.width // 2, 1600 - SPH * people[cur["who"]]["look"]["h"] - 75)
            return im, None
        if card and tt < t_card_end:
            im = card_bg.copy(); d = ImageDraw.Draw(im)
            tb = fit_block(card["title"], 64, (20, 24, 40), 900, 300); paste(im, tb, (W - tb.width) // 2, 160)
            y = 200 + tb.height + 30; shown = 0
            for i, r in enumerate(rows):
                if tt < r["t"]: break
                shown += 1; last = card.get("total") and i == len(rows) - 1
                p = ease((tt - r["t"]) / 0.3); vw = tlen(r["val"], 54); room = 920 - 104 - vw - 50
                ll = wrap(r["lab"], 46, room if room >= 300 else 780, 600); below = room < 300
                hh = 70 + 60 * len(ll) + (66 if below else 0)
                c = rrect(940, hh, 30, (255, 234, 234, 255) if last else (238, 243, 250, 255)); cd = ImageDraw.Draw(c)
                cd.ellipse([28, hh / 2 - 26, 80, hh / 2 + 26], fill=(210, 50, 50) if last else (255, 196, 40)); tdraw(cd, 54 - tlen(str(i + 1), 34) / 2, hh / 2 + 12, "!" if last else str(i + 1), 34, (255, 255, 255) if last else (20, 24, 40))
                for j, l in enumerate(ll): tdraw(cd, 104, 82 + j * 60, l, 46, (40, 44, 60), 600)
                tdraw(cd, 912 - vw, (hh - 26) if below else hh / 2 + 18, r["val"], 54, (210, 50, 50) if last else (20, 120, 70))
                paste(im, c, 70 + (1 - p) * 80, y, alpha=p); y += hh + 24
            mo = mouth_at(mouths.get("N", {}), fr); paste(im, small_m[0], W - small_m[0].width - 30, 1600 - small_m[0].height)
            return im, ("card", shown, int(tt * 4) if any(tt - r["t"] < 0.35 for r in rows) else 0)
        if tt < t_end:
            im = rule_bg.copy(); cur = next((r for r in rules if tt >= r["t0"] - 0.4), None); cur = [r for r in rules if tt >= r["t0"] - 0.4][-1] if rules and tt >= rules[0]["t0"] - 0.4 else None
            mo = mouth_at(mouths.get("R" + m, {}), fr); sp = big_m[3] if blink and mo == 0 else big_m[mo]
            paste(im, sp, (W - sp.width) // 2, 1310 - sp.height + 20)
            if cur:
                pl = rrect(330, 100, 50, (20, 24, 40, 255)); tdraw(ImageDraw.Draw(pl), (330 - tlen(f"Rule #{cur['n']}", 54)) / 2, 70, f"Rule #{cur['n']}", 54, (255, 214, 64)); paste(im, pl, (W - 330) // 2, 120)
                b = fit_block(cur["txt"], 58, (20, 24, 40), 940, 250); paste(im, b, (W - b.width) // 2, 230)
            return im, None
        a = ease((tt - t_end) / 0.35); im = END.copy(); paste(im, PILL, PX, PY, scale=1 + 0.03 * math.sin((tt - t_end) * 5))
        return im, None if a < 1 else ("end", int(tt * 10))

    mx = Mixer(DUR, seed); mx.room(0.025, 0.015 if bgname not in INDOOR else 0)
    if bgname not in INDOOR: mx.birds(t_story)
    for t0, w in aud: mx.add(t0, w)
    for r in rows: mx.blip(r["t"] - 0.05, 760)
    wav = out + ".wav"; mx.save(wav); encode(frame, DUR, wav, out); os.remove(wav)
    return dict(duration=round(DUR, 1), cover_frame=frame(0.6)[0])
