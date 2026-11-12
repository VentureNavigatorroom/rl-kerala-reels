"""Chat-story reel: a message conversation with both people's voices."""
import math, os
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say, voice_for

NAVY, NAVY2, CREAM, INK, BLUE, GREY, TEAL = (13, 27, 48), (22, 44, 78), (246, 242, 233), (20, 28, 44), (47, 91, 234), (120, 130, 150), (38, 166, 154)
PX0, PX1, PY0, PY1 = 70, 1010, 560, 1560

def bg():
    g = np.linspace(0, 1, H)[:, None, None]
    arr = (np.array(NAVY)[None, None] * (1 - g) + np.array(NAVY2)[None, None] * g).astype(np.uint8)
    return Image.fromarray(np.repeat(arr, W, axis=1), "RGB").convert("RGBA")

def build(s, out, seed=0):
    names = s["names"]; vo = [voice_for(names[0], 0), voice_for(names[1], 1)]
    if vo[0][0] == vo[1][0]: vo[1] = vo[1][0] + "2"; vo[0] = vo[0][0] + "1"
    t = 0.05; ev = []; aud = []   # first message starts typing at once; the hook is pinned at the top
    hook_im = fit_block(s["hook"], 68, (255, 255, 255), 920, 300)
    for i, (who, txt) in enumerate(s["lines"]):
        w = say(txt, vo[who]); d = wav_len(w)
        lines = wrap(txt, 44, 600, 700); tw = int(max(tlen(l, 44, 700) for l in lines))
        b = rrect(tw + 64, len(lines) * 64 + 40, 34, (BLUE if who == 0 else (255, 255, 255)) + (255,))
        bd = ImageDraw.Draw(b)
        for j, l in enumerate(lines): tdraw(bd, 32, 20 + 48 + j * 64, l, 44, (255, 255, 255) if who == 0 else INK, 700)
        ev.append(dict(who=who, img=b, t=t + 0.22, typing=t)); aud.append((t + 0.22, w, who)); t += 0.25 + d + 0.05
    t_end = t + 0.3; DUR = t_end + 4.5
    base = bg(); paste(base, hook_im, (W - hook_im.width) // 2, 230)
    panel = rrect(PX1 - PX0, PY1 - PY0, 48, CREAM + (255,)); d = ImageDraw.Draw(panel)
    d.ellipse([34, 26, 114, 106], fill=TEAL); tdraw(d, 136, 72, names[1], 40, INK); tdraw(d, 136, 112, "online", 28, GREY, 600)
    d.line([(0, 132), (PX1 - PX0, 132)], fill=(222, 216, 204), width=2)
    ini = names[1][0]; tdraw(d, 74 - tlen(ini, 44) / 2, 82, ini, 44, (255, 255, 255))
    paste(base, panel, PX0, PY0)
    AH, AW = PY1 - PY0 - 162, PX1 - PX0
    y = 26
    for e in ev: e["y"] = y; y += e["img"].height + 22
    END, PILL, (PX, PY) = end_card(s); dotb = rrect(130, 70, 35, (225, 220, 210, 255))

    def frame(tt):
        im = base.copy(); area = Image.new("RGBA", (AW, AH), (0, 0, 0, 0)); key = None
        shown = [e for e in ev if tt >= e["t"]]
        need = lambda e: max(0, e["y"] + e["img"].height + 26 - AH)
        off = 0.0
        if shown:
            cur = need(shown[-1]); prev = need(shown[-2]) if len(shown) > 1 else 0
            off = prev + (cur - prev) * ease((tt - shown[-1]["t"]) / 0.3)
        typing = next((e for e in ev if e["typing"] <= tt < e["t"]), None)
        if typing: off = max(off, max(0, typing["y"] + 96 - AH))
        for e in shown:
            p = ease((tt - e["t"]) / 0.22); b = e["img"]
            x = AW - b.width - 30 if e["who"] == 0 else 30; yy = e["y"] - off + (1 - p) * 26
            if yy + b.height > 0: paste(area, b, x, yy, alpha=p, scale=0.9 + 0.1 * p)
        if typing:
            x = AW - 160 if typing["who"] == 0 else 30; yy = typing["y"] - off; paste(area, dotb, x, yy); dd = ImageDraw.Draw(area)
            for k in range(3):
                bob = math.sin(tt * 9 - k * 0.9) * 6; dd.ellipse([x + 30 + k * 28, yy + 28 + bob, x + 44 + k * 28, yy + 42 + bob], fill=GREY)
        im.alpha_composite(area, (PX0, PY0 + 140))
        if tt >= t_end:
            a = ease((tt - t_end) / 0.35); paste(im, END, 0, 0, alpha=a); paste(im, PILL, PX, PY, alpha=a, scale=1 + 0.03 * math.sin((tt - t_end) * 5))
        elif not typing and shown and tt - shown[-1]["t"] > 0.35: key = ("hold", len(shown))
        return im, key

    mx = Mixer(DUR, seed); mx.room(0.03, 0)
    for t0, w, who in aud: mx.blip(t0, 660 if who == 0 else 880); mx.add(t0 + 0.04, load_wav(w))
    wav = out + ".wav"; mx.save(wav); encode(frame, DUR, wav, out); os.remove(wav)
    cov, _ = frame(ev[min(3, len(ev) - 1)]["t"] + 0.5)
    return dict(duration=round(DUR, 1), cover_frame=cov)
