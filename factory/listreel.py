"""Checklist reel: hook, three numbered cards, narrator voice."""
import math, os
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say
from chat import bg

GOLD, NAVY, INK = (255, 184, 28), (13, 27, 48), (20, 28, 44)
NUM = ["ഒന്ന്", "രണ്ട്", "മൂന്ന്", "നാല്", "അഞ്ച്"]

SAFE_BOTTOM = 1590   # below this Instagram draws the caption, buttons and progress bar over the reel

def card_layout(items):
    """Largest text scale at which all cards fit between y=640 and SAFE_BOTTOM. Returns (scale, gap, [(title lines, sub lines, height)])."""
    for k in (1.0, 0.94, 0.88, 0.82, 0.77, 0.72, 0.67, 0.62, 0.58):
        gap = int(30 * k); rows = []
        for title, sub in items:
            tl, sl = wrap(title, round(54 * k), 680), wrap(sub, round(42 * k), 680, 600)
            rows.append((tl, sl, int(50 * k + len(tl) * 72 * k + 16 * k + len(sl) * 60 * k + 44 * k)))
        if 640 + sum(r[2] for r in rows) + gap * (len(rows) - 1) <= SAFE_BOTTOM: return k, gap, rows
    return k, gap, rows

def build(s, out, seed=0):
    hw = say(s["hook"].replace("\n", " "), "NARRATOR"); t = 0.05; aud = [(t, hw)]; t += wav_len(hw) + 0.4
    hook_im = fit_block(s["hook"], 74, (255, 255, 255), 920, 300)
    cards = []; y = 640
    k, gap, layout = card_layout(s["items"])   # shrink to fit: every card must end above Instagram's caption overlay
    for i, (title, sub) in enumerate(s["items"]):
        w = say(f"{NUM[i]}. {title}. {sub}", "NARRATOR")
        tl, sl, ch = layout[i]
        c = rrect(900, ch, 40, (255, 255, 255, 255)); d = ImageDraw.Draw(c)
        r = 55 * k; cy = 44 * k + r; d.ellipse([91 - r, cy - r, 91 + r, cy + r], fill=GOLD); tdraw(d, 91 - tlen(str(i + 1), round(66 * k)) / 2, cy + 26 * k, str(i + 1), round(66 * k), NAVY)
        for j, l in enumerate(tl): tdraw(d, 180, 44 * k + 58 * k + j * 72 * k, l, round(54 * k), INK)
        for j, l in enumerate(sl): tdraw(d, 180, 44 * k + len(tl) * 72 * k + 16 * k + 46 * k + j * 60 * k, l, round(42 * k), (70, 80, 100), 600)
        cards.append(dict(img=c, y=y, t=t)); aud.append((t + 0.1, w)); t += 0.1 + wav_len(w) + 0.3; y += ch + gap
    t_end = t + 0.3; DUR = t_end + 4.5
    base = bg(); paste(base, hook_im, (W - hook_im.width) // 2, 250)
    ImageDraw.Draw(base).rounded_rectangle([440, 590, 640, 602], 6, fill=GOLD)
    END, PILL, (PX, PY) = end_card(s)

    def frame(tt):
        im = base.copy(); key = None; moving = False
        for c in cards:
            if tt < c["t"]: continue
            p = ease((tt - c["t"]) / 0.35); moving |= p < 1; paste(im, c["img"], 90 + (1 - p) * 120, c["y"], alpha=p)
        if tt >= t_end:
            a = ease((tt - t_end) / 0.35); paste(im, END, 0, 0, alpha=a); paste(im, PILL, PX, PY, alpha=a, scale=1 + 0.03 * math.sin((tt - t_end) * 5))
        elif not moving: key = ("hold", sum(tt >= c["t"] for c in cards))
        return im, key

    mx = Mixer(DUR, seed); mx.room(0.03, 0)
    for i, (t0, w) in enumerate(aud):
        if i: mx.blip(t0 - 0.05, 740)
        mx.add(t0, load_wav(w))
    wav = out + ".wav"; mx.save(wav); encode(frame, DUR, wav, out); os.remove(wav)
    return dict(duration=round(DUR, 1), cover_frame=frame(t_end - 0.1)[0])
