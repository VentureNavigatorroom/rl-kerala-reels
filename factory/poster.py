"""Poster maker: one 1080x1350 (4:5) feed image. Four layouts, same visual system as the carousels.
Text stays inside the centre safe zone (the profile grid trims the sides), one focal point per poster,
keyword pill near the bottom so the post asks for one comment.
  fact     : big number / short fact + one explaining line
  myth     : "people say" (struck through) vs "truth"
  deadline : alert band + date/number + what happens if missed
  check    : title + 3-5 tick lines
"""
from PIL import Image, ImageDraw
from common import *

PW, PH = 1080, 1350
NAVY, GOLD, CREAM, INK, RED, GREEN, ORANGE = (13, 27, 48), (255, 196, 40), (250, 244, 228), (30, 36, 34), (196, 52, 46), (34, 139, 84), (204, 92, 52)
THEMES = {"fact": (NAVY, GOLD, (255, 255, 255)), "myth": (CREAM, ORANGE, INK), "deadline": ((120, 22, 22), GOLD, (255, 255, 255)), "check": ((34, 96, 74), GOLD, (255, 255, 255))}
L, R = 110, PW - 110          # safe zone (centre ~80%)

def _pill(text, size, bg, fg, padx=46, h=None):
    w = int(tlen(text, size)) + padx * 2; h = h or int(size * 1.9)
    p = rrect(w, h, h // 2, bg + (255,)); tdraw(ImageDraw.Draw(p), padx, int(h * 0.68), text, size, fg); return p

def _footer(im, p, acc, fg):
    d = ImageDraw.Draw(im)
    kw = p["cta"][0]; pill = _pill(kw, 52, acc, THEMES[p["layout"]][0] if p["layout"] != "myth" else (255, 255, 255))
    y = PH - 300; im.paste(pill, ((PW - pill.width) // 2, y), pill)
    sb = block(p["cta"][1].split("\n")[0], 40, fg, maxw=860, wt=600); im.paste(sb, ((PW - sb.width) // 2, y + pill.height + 18), sb)
    tdraw(d, (PW - tlen("@" + BRAND, 32, 600)) / 2, PH - 44, "@" + BRAND, 32, tuple(int(c * 0.75) for c in fg) if fg != INK else (120, 120, 120), 600)

def make(p, out):
    bg, acc, fg = THEMES[p["layout"]]; im = Image.new("RGB", (PW, PH), bg); d = ImageDraw.Draw(im)
    tag = _pill(p.get("tag", "അറിയേണ്ടത്"), 40, acc, bg if p["layout"] != "myth" else (255, 255, 255)); im.paste(tag, ((PW - tag.width) // 2, 110), tag)
    top, bottom = 110 + tag.height + 50, PH - 330
    if p["layout"] == "fact":
        big = fit_block(p["big"], 190, acc, R - L, 420, lh=1.15)
        line = fit_block(p["text"], 62, fg, R - L, 330, lh=1.4)
        y = top + max(0, (bottom - top - big.height - 40 - line.height) // 2)
        im.paste(big, ((PW - big.width) // 2, y), big); im.paste(line, ((PW - line.width) // 2, y + big.height + 40), line)
    elif p["layout"] == "myth":
        def card(label, text, col, strike, sz=58):
            t = block(text, sz, INK, maxw=R - L - 80, lh=1.35); h = t.height + 150
            c = rrect(R - L, h, 36, (255, 255, 255, 255)); cd = ImageDraw.Draw(c)
            cd.rounded_rectangle([0, 0, 18, h], 9, fill=col); tdraw(cd, 50, 70, label, 44, col)
            c.paste(t, (50, 100), t)
            return c
        for sz in (58, 52, 47, 43, 39, 36):   # shrink until both cards fit above the keyword
            a, b = card("കേൾക്കുന്നത്", p["myth"], RED, True, sz), card("സത്യം", p["truth"], GREEN, False, sz)
            if a.height + 40 + b.height <= bottom - top: break
        y = top + max(0, (bottom - top - a.height - 40 - b.height) // 2)
        im.paste(a, (L, y), a); im.paste(b, (L, y + a.height + 40), b)
    elif p["layout"] == "deadline":
        big = fit_block(p["big"], 170, acc, R - L, 360, lh=1.15)
        line = fit_block(p["text"], 58, fg, R - L, 300, lh=1.4)
        y = top + max(0, (bottom - top - big.height - 40 - line.height) // 2)
        d.rectangle([0, y - 30, PW, y + big.height + 20], fill=tuple(max(0, c - 40) for c in bg))
        im.paste(big, ((PW - big.width) // 2, y), big); im.paste(line, ((PW - line.width) // 2, y + big.height + 50), line)
    else:   # check
        for sz in (50, 46, 42, 38, 34):
            title = block(p["title"], int(sz * 1.5), fg, maxw=R - L, lh=1.3)   # shrink until the list fits above the keyword
            rows = [block(x, sz, fg, maxw=R - L - 90, wt=600, align="left", lh=1.3) for x in p["items"]]
            h = title.height + 50 + sum(r.height + 24 for r in rows)
            if h <= bottom - top: break
        y = top + max(0, (bottom - top - h) // 2); im.paste(title, ((PW - title.width) // 2, y), title); y += title.height + 50
        for r in rows:
            d.ellipse([L, y + 6, L + 50, y + 56], fill=acc); d.line([(L + 13, y + 32), (L + 22, y + 42), (L + 38, y + 20)], fill=bg, width=6)
            im.paste(r, (L + 80, y), r); y += r.height + 24
    _footer(im, p, acc, fg)
    im.save(out, quality=92); return out
