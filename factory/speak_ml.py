"""Turn on-screen Malayalam text into what the voice should SAY.
The voice model reads digits and Latin-script words badly, so before speaking:
  - numbers become Malayalam number words (180 -> നൂറ്റിയെൺപത്, 50,000 -> അമ്പതിനായിരം, 15% -> പതിനഞ്ച് ശതമാനം,
    7-15 -> ഏഴ് മുതൽ പതിനഞ്ച്, 2-3 -> രണ്ടോ മൂന്നോ, 30-ൽ -> മുപ്പതിൽ)
  - English words written in Latin letters become Malayalam spellings (SAY below; check_bank.py refuses unknown ones)
  - acronyms are spelled letter by letter (NRI -> എൻ ആർ ഐ), except the ones people say as words (PAN, START ...)
On-screen text is not changed."""
import re

U = ["പൂജ്യം", "ഒന്ന്", "രണ്ട്", "മൂന്ന്", "നാല്", "അഞ്ച്", "ആറ്", "ഏഴ്", "എട്ട്", "ഒമ്പത്",
     "പത്ത്", "പതിനൊന്ന്", "പന്ത്രണ്ട്", "പതിമൂന്ന്", "പതിനാല്", "പതിനഞ്ച്", "പതിനാറ്", "പതിനേഴ്", "പതിനെട്ട്", "പത്തൊമ്പത്"]
T = {2: "ഇരുപത്", 3: "മുപ്പത്", 4: "നാൽപ്പത്", 5: "അമ്പത്", 6: "അറുപത്", 7: "എഴുപത്", 8: "എൺപത്", 9: "തൊണ്ണൂറ്"}
TC = {2: "ഇരുപത്തി", 3: "മുപ്പത്തി", 4: "നാൽപ്പത്തി", 5: "അമ്പത്തി", 6: "അറുപത്തി", 7: "എഴുപത്തി", 8: "എൺപത്തി", 9: "തൊണ്ണൂറ്റി"}
H = {1: "നൂറ്", 2: "ഇരുന്നൂറ്", 3: "മുന്നൂറ്", 4: "നാനൂറ്", 5: "അഞ്ഞൂറ്", 6: "അറുന്നൂറ്", 7: "എഴുന്നൂറ്", 8: "എണ്ണൂറ്", 9: "തൊള്ളായിരം"}
HC = {1: "നൂറ്റി", 2: "ഇരുന്നൂറ്റി", 3: "മുന്നൂറ്റി", 4: "നാനൂറ്റി", 5: "അഞ്ഞൂറ്റി", 6: "അറുന്നൂറ്റി", 7: "എഴുന്നൂറ്റി", 8: "എണ്ണൂറ്റി", 9: "തൊള്ളായിരത്തി"}
TH = {1: "ആയിരം", 2: "രണ്ടായിരം", 3: "മൂവായിരം", 4: "നാലായിരം", 5: "അയ്യായിരം", 6: "ആറായിരം", 7: "ഏഴായിരം", 8: "എണ്ണായിരം", 9: "ഒമ്പതിനായിരം", 10: "പതിനായിരം"}
VJ = {"അ": "യ", "ആ": "യാ", "ഇ": "യി", "ഉ": "യു", "എ": "യെ", "ഏ": "യേ", "ഒ": "യൊ", "ഓ": "യോ", "ഐ": "യൈ"}

def _join(prefix, rest):   # ഇരുപത്തി + അഞ്ച് -> ഇരുപത്തിയഞ്ച്
    return prefix + (VJ[rest[0]] + rest[1:] if rest[:1] in VJ else rest)

def words(n):
    n = int(n)
    if n < 20: return U[n]
    if n < 100: t, u = divmod(n, 10); return T[t] if not u else _join(TC[t], U[u])
    if n < 1000: h, r = divmod(n, 100); return H[h] if not r else _join(HC[h], words(r))
    if n < 100000:
        t, r = divmod(n, 1000)
        head = TH[t] if t in TH else words(t)[:-1] + "ിനായിരം"          # ഇരുപത് -> ഇരുപതിനായിരം
        return head if not r else _join(head[:-1] + "ത്തി", words(r))     # ആയിരം -> ആയിരത്തി...
    if n < 10000000:
        l, r = divmod(n, 100000)
        head = ("ഒരു" if l == 1 else words(l)) + " ലക്ഷം"
        return head if not r else head[:-1] + "ത്തി " + words(r)
    c, r = divmod(n, 10000000)
    head = ("ഒരു" if c == 1 else words(c)) + " കോടി"
    return head if not r else head + " " + words(r)

def _o(w): return (w[:-1] + "ോ") if w.endswith("്") else w + "ോ"          # രണ്ട് -> രണ്ടോ

def _suffix(w, suf):   # 30 + ൽ -> മുപ്പതിൽ ; 20A-യും stays
    if not suf: return w
    if w.endswith("്") and not suf.startswith(("യ", "ാ", "ി", "ു", "െ", "േ", "ൊ", "ോ")): return w[:-1] + "ി" + suf
    if w.endswith("ം") and suf[:1] in ("ത", "ൽ", "ന"): return w[:-1] + "ത്തി" + suf.lstrip("ത")
    return w + suf

NUM = r"\d{1,3}(?:,\d{2,3})+|\d+"
ML = r"[ഀ-ൿ‌‍]+"

def numbers(text):
    text = re.sub(rf"({NUM})\s*%", lambda m: words(m.group(1).replace(",", "")) + " ശതമാനം", text)
    def rng(m):
        a, b = int(m.group(1).replace(",", "")), int(m.group(2).replace(",", ""))
        return f"{_o(words(a))} {_o(words(b))}" if b - a == 1 else f"{words(a)} മുതൽ {words(b)}"
    text = re.sub(rf"(?<![\d,])({NUM})\s*[–—-]\s*({NUM})(?![\d,])", rng, text)
    text = re.sub(rf"({NUM})-?({ML})?", lambda m: _suffix(words(m.group(1).replace(",", "")), (m.group(2) or "")), text)
    return text

# English words people write in Latin letters, as a Malayali says them. Keys are matched case-insensitively.
SAY = {
    "pvt": "പ്രൈവറ്റ്", "ltd": "ലിമിറ്റഡ്", "private": "പ്രൈവറ്റ്", "limited": "ലിമിറ്റഡ്", "bank": "ബാങ്ക്", "insurance": "ഇൻഷുറൻസ്",
    "pan": "പാൻ", "start": "സ്റ്റാർട്ട്", "name": "നെയിം", "after": "ആഫ്റ്റർ", "checklist": "ചെക്ക്‌ലിസ്റ്റ്", "done": "ഡൺ", "stop": "സ്റ്റോപ്പ്",
    "company": "കമ്പനി", "director": "ഡയറക്ടർ", "startup": "സ്റ്റാർട്ടപ്പ്", "client": "ക്ലയന്റ്", "freelancer": "ഫ്രീലാൻസർ",
    "3d": "ത്രീ ഡി", "ok": "ഓക്കെ", "okay": "ഓക്കെ", "dm": "ഡി എം", "app": "ആപ്പ്", "online": "ഓൺലൈൻ", "office": "ഓഫീസ്",
}
# Malayalam-script words the voice says wrongly, respelled the way it says them right. Filled from the voice-audit
# reports (misheard in 2+ lines). On-screen text keeps the normal spelling.
RESPELL = {
    "ഒ": "ഓ",   # letter O in OPC / NOC / ROC: short ഒ ran into the next word (OPC heard as ഓഫീസി, NOC as എന്നോസി); audit 13 Nov
}
# Words already checked and found fine (the recogniser just spells them differently). Never flagged again.
# audit 13 Nov: recogniser joins words (കമ്പനി ആകണം -> കമ്പനിയാകണം), runs spelled letters together (എൽ എൽ പി -> എൽഎൽപി)
# or spells loanwords its own way (ഫയലിംഗ് -> ഫൈലിങ്, മുമ്പ് -> മുൻപ്); the voice said these right.
REVIEWED_OK = {
    "ആകണം", "ഫയലിംഗും", "മാസം", "പിക്ക്", "ഇട്ടോ", "ഐക്കും", "ആയ", "എൽ", "ആക്കാം", "ആർ", "എൻ", "ഫീ", "നാട്ടിൽ", "പിഴ", "അല്ലേ", "ഒക്കെ", "മുമ്പ്", "ഷെയർഹോൾഡർ", "ഇല്ല", "രജിസ്റ്റേർഡ്", "സി", "എ", "ഐ", "ഫയലിംഗ്", "പിക്കും", "വരുമാനം", "അതിന്", "ഒറ്റയ്ക്ക്", "റിജക്ട്", "ആകാം", "പിയോടോ", "ഇരുപത്", "പിയോ", "ഈ", "പി", "എടുക്കാൻ", "നൂറ്", "ഫയൽ", "ഓഫീസ്", "കമ്പനി", "പേര്", "പറ്റില്ല", "രൂപ", "ഷെയർ", "ഒരു", "പക്ഷേ",
}
def decided(word):
    """True when a word has already been fixed (RESPELL / SAY) or judged fine: the audit skips it."""
    return word in RESPELL or word in RESPELL.values() or word in REVIEWED_OK or word in SAY.values()
LETTER = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "എ ബി സി ഡി ഇ എഫ് ജി എച്ച് ഐ ജെ കെ എൽ എം എൻ ഒ പി ക്യു ആർ എസ് ടി യു വി ഡബ്ല്യു എക്സ് വൈ സെഡ്".split()))

def latin(text):
    def one(m):
        w, suf = m.group(1), m.group(2) or ""
        key = w.lower()
        if key in SAY: out = SAY[key]
        elif w.isupper() and len(w) <= 6: out = " ".join(LETTER[c] for c in w)        # NRI -> എൻ ആർ ഐ
        else: return m.group(0)                                                       # unknown: left as is (check_bank flags it)
        return out + suf
    text = re.sub(r"(?<![A-Za-z])(\d?[A-Za-z]+)-?(" + ML + ")?", one, text)
    return text

def before_respell(text):
    """spoken() up to the RESPELL step: tells which texts a RESPELL entry changes."""
    text = re.sub(r"(?<![A-Za-z\d])3D(?![A-Za-z])", "ത്രീ ഡി", text)
    text = re.sub(r"(?<=[A-Za-z])-(?=\d)", " ", text)                                                 # INC-20A -> INC 20A
    text = re.sub(r"(\d)([A-Z])(?![A-Za-z])-?(" + ML + ")?", lambda m: m.group(1) + " " + LETTER[m.group(2)] + (m.group(3) or ""), text)   # 20A-യും -> 20 എയും
    text = re.sub(r"(?<![\d,])1\s+(ലക്ഷം|കോടി)", r"ഒരു \1", text)                                    # 1 ലക്ഷം -> ഒരു ലക്ഷം
    return latin(text)

def spoken(text):
    text = before_respell(text)
    if RESPELL: text = re.sub(ML, lambda m: RESPELL.get(m.group(0), m.group(0)), text)
    text = numbers(text)
    text = re.sub(r"(?<=[\u0d00-\u0d7f])-(?=[\u0d00-\u0d7f])", " ", text)   # പെയ്ഡ്-അപ്പ് -> two words, not one
    text = re.sub(r"-(?=[\u0d00-\u0d7f])", "", text)
    text = re.sub(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]", "", text)   # emoji are not spoken
    text = re.sub(r"\s*/\s*", " ഒരു ", text)                     # 1,000 രൂപ / ദിവസം -> ... ഒരു ദിവസം
    text = re.sub(r"\s*\+\s*", ", പിന്നെ ", text)               # ബിൽ + NOC -> ബിൽ, പിന്നെ ...
    text = re.sub(r"\s*[()]\s*", ", ", text)                     # brackets become a short pause
    text = re.sub(r"\s*:\s*", ", ", text).replace("…", ", ").replace("...", ", ")
    text = re.sub(r"(,\s*)+", ", ", text).strip(" ,")
    return re.sub(r"[ \t]+", " ", text.replace("-", " ")).strip()

def unknown_latin(text):
    """Latin-letter words the voice has no Malayalam spelling for (check_bank.py reports them)."""
    t = re.sub(r"(?<![A-Za-z])3D(?![A-Za-z])", "", text)
    return [w for w in re.findall(r"(?<![A-Za-z\d])[A-Za-z]+", t) if w.lower() not in SAY and not (w.isupper() and len(w) <= 6)]

if __name__ == "__main__":
    for t in ["180 ദിവസത്തിനുള്ളിൽ INC-20A", "50,000 രൂപ പിഴ", "1,000 രൂപ / ദിവസം", "7-15 ദിവസം", "2-3 പേരുകൾ", "30-ൽ", "20-ന്",
              "15% വളർച്ച", "1 ലക്ഷം", "2,50,000", "NRI-ക്കും Pvt Ltd", "3D ആനിമേഷൻ", "Bank, Insurance", "24 മണിക്കൂർ", "6,000", "120", "101", "999"]:
        print(t, "->", spoken(t))
