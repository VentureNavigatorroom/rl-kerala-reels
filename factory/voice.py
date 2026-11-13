"""Malayalam voices with AI4Bharat Indic Parler-TTS (Apache-2.0). Caches every line by content hash."""
import re, os, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get("VOICE_CACHE", f"{ROOT}/.voice_cache")
os.makedirs(CACHE, exist_ok=True)

FEMALE_V4 = {"അനു", "ഫാത്തിമ", "അഞ്ജലി", "മീര", "ലക്ഷ്മി", "അമ്മ", "നിമ്മി", "ഗ്രീഷ്മ", "സാറ", "ദിവ്യ", "റിയ", "ആതിര", "നേഹ", "സ്നേഹ", "ഷബ്ന", "ജിഷ", "ആൻസി", "നസ്രിൻ", "ഉമ്മ", "ചേച്ചി"}
# v5: every woman's name used by a location or a script, plus relation words; checked word by word ("ഡോ. ആൻസി", "മകൾ ടീന")
FEMALE = FEMALE_V4 | {"രേഷ്മ", "അഞ്ജന", "അനഘ", "അമ്മു", "അമ്മൂമ്മ", "അലീന", "അശ്വതി", "ആരതി", "ആര്യ", "ഉഷ", "ഐശ്വര്യ", "കാവ്യ", "ഗായത്രി", "ജയ", "ടീന", "ഡെയ്സി",
    "ഡെൽന", "ദീപ്തി", "ദേവിക", "നിള", "നീതു", "ബിന്ദു", "മരിയ", "രമ്യ", "റസിയ", "ലീല", "ശരണ്യ", "ശാന്ത", "ശ്രുതി", "ശ്വേത", "ഷഹാന", "ഷീബ",
    "ഷൈനി", "സിനി", "സുധ", "സുമ", "സുമയ്യ", "സെലിൻ", "സോണിയ", "ഹന്ന", "മകൾ", "ഭാര്യ", "അനിയത്തി", "അമ്മായി", "ഇത്ത"}
STYLE = "speaks in a very lively, animated and expressive way at a fast pace, with natural rises and falls in pitch, like excitedly chatting with a close friend. The audio is very clear and close-sounding with no background noise."
VOICES = {
    "F1": f"Anjali {STYLE} Her pitch is moderate.",
    "F2": f"Anjali {STYLE} Her pitch is slightly high and her tone is bright.",
    "M1": f"Harish {STYLE} His tone is friendly and teasing, with a moderate pitch.",
    "M2": f"Harish {STYLE} His pitch is slightly low and his tone is calm.",
    "NARRATOR": "Anjali speaks clearly and confidently at a moderate pace, like explaining something useful to a friend. The recording is close-sounding with very little background noise.",
}

# every man's name / relation word in use; a name in neither set is an error in check_bank.py (so its voice is never guessed)
MALE = {"മുനീർ", "ഹരി", "വിപിൻ", "അഖിൽ", "അച്ഛൻ", "അനന്തു", "അനിയൻ", "അനൂപ്", "അപ്പ", "അപ്പൂപ്പൻ", "അമ്മാവൻ", "അമൽ", "അരവിന്ദ്", "അരുൺ", "അർജുൻ", "ആദിത്യൻ", "ആദിൽ", "ആദർശ്", "ആന്റണി", "ആഷിക്", "ആസിഫ്", "ആൽബിൻ", "ആൽവിൻ", "ഇക്ക", "ഇർഫാൻ", "ഉണ്ണി", "ഉപ്പ", "ഏട്ടൻ", "കിരൺ", "കുമാർ", "ഗോകുൽ", "ഗോപി", "ചേട്ടൻ", "ജസ്റ്റിൻ", "ജാഫർ", "ജിതിൻ", "ജിബിൻ", "ജിഷ്ണു", "ജെയ്സൺ", "ജോ", "ജോബി", "ജോമോൻ", "ജോയി", "ജോസഫ്", "ജോർജ്", "ടോണി", "ടോമി", "ഡെന്നിസ്", "തോമസ്", "ദിനേശ്", "നസീർ", "നിഖിൽ", "നിതിൻ", "നൗഷാദ്", "പ്രകാശ്", "പ്രവീൺ", "ഫഹദ്", "ഫെബിൻ", "ഫൈസൽ", "ബാലൻ", "ബിജു", "ബിജോയ്", "ബിനു", "ബേസിൽ", "ഭർത്താവ്", "മകൻ", "മനോജ്", "മാമൻ", "മുഹ്സിൻ", "മോഹനൻ", "രമേശ്", "രാജേഷ്", "രാഹുൽ", "റഫീഖ്", "റഷീദ്", "റിസ്വാൻ", "റോഷൻ", "വരുൺ", "വാസു", "വിനീത്", "വിവേക്", "വിഷ്ണു", "ശരത്", "ശ്യാം", "ശ്രീനാഥ്", "ഷംസു", "ഷഫീഖ്", "ഷമീർ", "ഷഹീൻ", "ഷാജി", "ഷാനവാസ്", "ഷിജു", "ഷിബു", "സജി", "സഞ്ജു", "സന്തോഷ്", "സനൽ", "സലീം", "സാബു", "സിജോ", "സിബി", "സുജിത്", "സുരേഷ്", "ഹാരിസ്"}

def gender_known(name):
    w = name.replace(".", " ").split()
    return any(x in FEMALE or x in MALE for x in w + [name])

def is_female(name, names=None):
    names = FEMALE if names is None else names
    return name in names or any(w in names for w in name.replace(".", " ").split())

def voice_for(name, slot, names=None):
    g = "F" if is_female(name, names) else "M"
    return f"{g}{1 + slot % 2}"

_model = None
def _load():
    global _model
    if _model is None:
        import torch
        from parler_tts import ParlerTTSForConditionalGeneration
        from transformers import AutoTokenizer
        torch.set_num_threads(int(os.environ.get("TTS_THREADS", "2")))
        m = "ai4bharat/indic-parler-tts"
        model = ParlerTTSForConditionalGeneration.from_pretrained(m)
        _model = (model, AutoTokenizer.from_pretrained(m), AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path))
    return _model

# Acronyms are spelled out letter by letter in Malayalam (NRI -> എൻ ആർ ഐ), otherwise the model reads them as one word.
LETTER = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "എ ബി സി ഡി ഇ എഫ് ജി എച്ച് ഐ ജെ കെ എൽ എം എൻ ഒ പി ക്യു ആർ എസ് ടി യു വി ഡബ്ല്യു എക്സ് വൈ സെഡ്".split()))
AS_WORD = {"START", "AFTER", "NAME", "PAN", "CHECKLIST", "DONE", "STOP"}
ACR = re.compile(r"(?<![A-Za-z])([A-Z]{2,6})(?![a-z])")
from speak_ml import spoken   # numbers -> Malayalam words, English words -> Malayalam spelling, acronyms letter by letter
HAS_ACR = lambda t: bool(ACR.search(t)) and any(w not in AS_WORD for w in ACR.findall(t))

def say(text, voice):
    text = spoken(text)
    key = hashlib.sha1(f"{voice}|{VOICES[voice]}|{text}".encode()).hexdigest()[:16]
    out = f"{CACHE}/{key}.wav"
    if os.path.exists(out): return out
    import torch, soundfile as sf
    model, tok, dtok = _load()
    d = dtok(VOICES[voice], return_tensors="pt"); p = tok(text, return_tensors="pt")
    for tryno in range(4):   # the model now and then returns (almost) no audio: try other seeds
        torch.manual_seed(int(key[:6], 16) + tryno * 7919)
        a = model.generate(input_ids=d.input_ids, attention_mask=d.attention_mask, prompt_input_ids=p.input_ids, prompt_attention_mask=p.attention_mask)
        a = a.cpu().numpy().reshape(-1)
        if a.size > 0.3 * model.config.sampling_rate: break
    else:
        raise RuntimeError(f"no audio for line: {text[:40]}")
    sf.write(out + ".tmp.wav", a, model.config.sampling_rate); os.replace(out + ".tmp.wav", out)
    return out
