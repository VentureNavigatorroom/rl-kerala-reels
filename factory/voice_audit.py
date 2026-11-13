"""Pronunciation audit: the voice reads real script lines, a Malayalam speech recogniser (thennal/whisper-medium-ml)
writes down what it heard, and words that come back different are reported. A word is flagged only when it is
misheard in at least 2 different lines (one-off recogniser mistakes are ignored).
Run on GitHub (voice-audit workflow). Output: audit/report.json and audit/report.md, plus the audio of the worst lines."""
import os, sys, re, json, random, collections, difflib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build, voice, speak_ml

N = int(os.environ.get("AUDIT_LINES", "120"))
OUT = os.path.join(build.ROOT, "audit"); os.makedirs(OUT, exist_ok=True)
ML = re.compile(r"[ഀ-ൿ‌‍]+")
def toks(t): return ML.findall(t.replace("‌", "").replace("‍", ""))

# lines: prefer ones with English loanwords, numbers or acronyms, then a random sample of the rest
lines = []
for s in build.load_bank():
    for t in build.spoken_texts(s):
        sp = speak_ml.spoken(t)
        if len(toks(sp)) >= 3: lines.append((s["id"], t, sp))
random.seed(7); random.shuffle(lines)
def score(x): return bool(re.search(r"[A-Za-z0-9]", x[1])) * 2 + sum(1 for w in toks(x[2]) if re.search("[ഫഷ]|്റ്റ|്ഡ|ോ", w))
# daily runs test the newest scripts first (highest batch numbers), so every new batch gets heard once
order = {sid: k for k, sid in enumerate(reversed([s["id"] for s in build.load_bank()]))}
if os.environ.get("AUDIT_NEW_FIRST"): lines.sort(key=lambda x: (order.get(x[0], 9e9), -score(x)))
else: lines.sort(key=score, reverse=True)
lines = lines[:N]

def write_report():
    global still
    flag = {w: v for w, v in bad.items() if len({x['line'] for x in v}) >= 2 and not speak_ml.decided(w)}
    still = {w: v for w, v in bad.items() if len({x['line'] for x in v}) >= 2 and w in speak_ml.RESPELL.values()}   # fixed but still misheard
    total = collections.Counter(w for r in rows for w in toks(r["said"]))
    rep = sorted(({"word": w, "misheard": len(v), "seen": total[w], "heard_as": collections.Counter(x["heard"] for x in v).most_common(3)} for w, v in flag.items()),
                 key=lambda r: (-r["misheard"] / max(1, r["seen"]), -r["misheard"]))
    json.dump({"lines": len(rows), "flagged": rep, "fixed_but_still_misheard": sorted(still), "rows": rows}, open(f"{OUT}/report.json", "w"), ensure_ascii=False, indent=1)
    with open(f"{OUT}/report.md", "w") as f:
        f.write(f"# Pronunciation audit ({len(rows)} lines)\n\n| word | misheard / seen | heard as |\n|---|---|---|\n")
        for r in rep: f.write(f"| {r['word']} | {r['misheard']}/{r['seen']} | {', '.join(h for h, _ in r['heard_as'])} |\n")
        if still: f.write("\nAlready respelled but still misheard (try a different respelling, do not add a second entry): " + ", ".join(sorted(still)) + "\n")


from transformers import pipeline
asr = pipeline("automatic-speech-recognition", model="thennal/whisper-medium-ml", device="cpu")
bad = collections.defaultdict(list); rows = []
for k, (sid, raw, sp) in enumerate(lines):
    wav = voice.say(raw, "F1" if k % 2 else "M1")
    heard = asr(wav, generate_kwargs={"language": "malayalam", "task": "transcribe"})["text"]
    a, b = toks(sp), toks(heard)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    miss = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal": continue
        for i in range(i1, i2):
            w = a[i]; cand = " ".join(b[j1:j2])
            if difflib.SequenceMatcher(a=w, b=cand).ratio() < 0.6: miss.append((w, cand))
    for w, c in miss: bad[w].append({"line": sid, "heard": c})
    rows.append({"id": sid, "said": sp, "heard": heard, "missed": miss, "audio": wav})
    print(f"{k+1}/{len(lines)} {sid} missed {len(miss)}", flush=True)
    if (k + 1) % 10 == 0: write_report()   # partial report survives a timeout

# words already fixed or already judged fine are never reported again (a fix is permanent)
write_report()
os.makedirs(f"{OUT}/audio", exist_ok=True)
for r in sorted(rows, key=lambda r: -len(r["missed"]))[:15]: shutil.copy(r["audio"], f"{OUT}/audio/{r['id']}_{len(r['missed'])}.wav")
print(open(f"{OUT}/report.md").read())
