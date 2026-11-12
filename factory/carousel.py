"""Carousel maker: 1080x1350 slides (cover, 3-6 content slides, CTA). Same visual system as the reels."""
from PIL import Image, ImageDraw
from common import *

CW, CH = 1080, 1350
CREAM, INK, ORANGE, GREEN, NAVY, GOLD = (250, 244, 228), (30, 36, 34), (204, 92, 52), (34, 139, 84), (13, 27, 48), (255, 196, 40)
THEMES = [(NAVY, GOLD, (255, 255, 255)), ((204, 92, 52), (255, 236, 200), (255, 255, 255)), ((34, 110, 84), (255, 222, 70), (255, 255, 255))]

def _brand(d, fill):
    tdraw(d, (CW - tlen("@" + BRAND, 34, 600)) / 2, CH - 50, "@" + BRAND, 34, fill, 600)

def make(c, outdir, seed=0):
    bg, acc, fg = THEMES[seed % len(THEMES)]
    files = []; n = len(c["slides"]) + 2
    # cover
    im = Image.new("RGB", (CW, CH), bg); d = ImageDraw.Draw(im)
    tag = c.get("tag", "അറിയേണ്ടത്"); tw = int(tlen(tag, 44)) + 60
    pill = rrect(tw, 80, 40, acc + (255,)); tdraw(ImageDraw.Draw(pill), 30, 56, tag, 44, bg)
    im.paste(pill, ((CW - tw) // 2, 230), pill)
    hb = fit_block(c["hook"], 96, fg, 940, 640, lh=1.35); im.paste(hb, ((CW - hb.width) // 2, 380), hb)
    tdraw(d, (CW - tlen("സ്വൈപ്പ് ചെയ്യൂ  >>", 44, 700)) / 2, CH - 170, "സ്വൈപ്പ് ചെയ്യൂ  >>", 44, acc, 700)
    _brand(d, (200, 200, 200)); files.append(im)
    # content slides
    for i, (title, body) in enumerate(c["slides"]):
        im = Image.new("RGB", (CW, CH), CREAM); d = ImageDraw.Draw(im)
        d.rectangle([0, 0, CW, 18], fill=bg)
        tb = block(title, 80, INK, maxw=900, align="left", lh=1.3)
        bb = block(body, 56, (70, 80, 76), maxw=900, wt=600, align="left", lh=1.55)
        y0 = max(170, (CH - (130 + tb.height + 30 + bb.height)) // 2)
        tdraw(d, 80, y0 + 100, f"{i + 1:02d}", 110, acc if acc != (255, 236, 200) else ORANGE)
        d.rounded_rectangle([80, y0 + 125, 200, y0 + 135], 5, fill=acc if acc != (255, 236, 200) else ORANGE)
        im.paste(tb, (60, y0 + 150), tb); im.paste(bb, (60, y0 + 170 + tb.height), bb)
        tdraw(d, CW - 160, CH - 50, f"{i + 2}/{n}", 34, (150, 150, 150), 600); _brand(d, (150, 150, 150)); files.append(im)
    # CTA
    im = Image.new("RGB", (CW, CH), bg); d = ImageDraw.Draw(im)
    eb = fit_block(c["end"], 74, fg, 940, 420); im.paste(eb, ((CW - eb.width) // 2, 330), eb)
    kw = c["cta"][0]; pw = int(tlen(kw, 58)) + 100; pill = rrect(pw, 136, 68, acc + (255,)); tdraw(ImageDraw.Draw(pill), 50, 90, kw, 58, bg)
    y = 330 + eb.height + 50; im.paste(pill, ((CW - pw) // 2, y), pill)
    sb = block(c["cta"][1], 46, fg, maxw=900, wt=600); im.paste(sb, ((CW - sb.width) // 2, y + 176), sb)
    _brand(d, (200, 200, 200)); files.append(im)
    out = []
    for k, im in enumerate(files):
        p = f"{outdir}/{c['id']}_{k + 1}.jpg"; im.save(p, quality=90); out.append(p)
    return out
