"""Follower shout-out image (1080x1350): welcome or monthly top supporters. Names come only from people who said yes
(worker /public/shoutqueue). Usernames are drawn in Latin script; the voice never reads them (images only)."""
from PIL import Image, ImageDraw
from common import *

PW, PH = 1080, 1350
NAVY, GOLD = (13, 27, 48), (255, 196, 40)

def make(q, out):
    im = Image.new("RGB", (PW, PH), NAVY); d = ImageDraw.Draw(im)
    title = "ഞങ്ങളുടെ കുടുംബത്തിലേക്ക് സ്വാഗതം" if q["kind"] == "welcome" else "ഈ മാസത്തെ ടോപ്പ് സപ്പോർട്ടേഴ്സ്"
    sub = "Thank you for following!" if q["kind"] == "welcome" else "Thank you for being with us!"
    tb = block(title, 60, (255, 255, 255), maxw=900); im.paste(tb, ((PW - tb.width) // 2, 90), tb)
    tdraw(d, (PW - tlen(sub, 40, 700)) / 2, 90 + tb.height + 70, sub, 40, GOLD, 700)
    names = ["@" + n for n in q["names"]]; cols = 2 if len(names) > 10 else 1
    size = 44 if cols == 1 else 36; top = 0.34 * PH
    for i, n in enumerate(names):
        cx = PW / 2 if cols == 1 else (PW * (0.72 if i % 2 else 0.28)); y = top + (i if cols == 1 else i // 2) * 0.055 * PH + 30
        while tlen(n, size, 700) > (900 if cols == 1 else 440) and size > 22: size -= 2
        tdraw(d, cx - tlen(n, size, 700) / 2, y, n, size, (255, 255, 255), 700)
    foot = "അടുത്ത തവണ നിങ്ങളുടെ പേര് ഇവിടെ വേണോ? ഏത് പോസ്റ്റിലും WELCOME എന്ന് കമന്റ് ചെയ്യൂ"
    fb = block(foot, 34, GOLD, maxw=900, wt=700); im.paste(fb, ((PW - fb.width) // 2, PH - 120 - fb.height), fb)
    tdraw(d, (PW - tlen("@" + BRAND, 30, 600)) / 2, PH - 44, "@" + BRAND, 30, (150, 160, 180), 600)
    im.save(out, quality=92)
