"""Malayalam voices with AI4Bharat Indic Parler-TTS (Apache-2.0). Caches every line by content hash."""
import os, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get("VOICE_CACHE", f"{ROOT}/.voice_cache")
os.makedirs(CACHE, exist_ok=True)

FEMALE = {"അനു", "ഫാത്തിമ", "അഞ്ജലി", "മീര", "ലക്ഷ്മി", "അമ്മ", "നിമ്മി", "ഗ്രീഷ്മ", "സാറ", "ദിവ്യ", "റിയ", "ആതിര"}
STYLE = "speaks casually and expressively at a slightly fast pace with a natural, conversational delivery. The recording is close-sounding with very little background noise, like chatting with a friend."
VOICES = {
    "F1": f"Anjali {STYLE} Her pitch is moderate.",
    "F2": f"Anjali {STYLE} Her pitch is slightly high and her tone is bright.",
    "M1": f"Harish {STYLE} His tone is friendly and teasing, with a moderate pitch.",
    "M2": f"Harish {STYLE} His pitch is slightly low and his tone is calm.",
    "NARRATOR": "Anjali speaks clearly and confidently at a moderate pace, like explaining something useful to a friend. The recording is close-sounding with very little background noise.",
}

def voice_for(name, slot):
    g = "F" if name in FEMALE else "M"
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

def say(text, voice):
    key = hashlib.sha1(f"{voice}|{VOICES[voice]}|{text}".encode()).hexdigest()[:16]
    out = f"{CACHE}/{key}.wav"
    if os.path.exists(out): return out
    import torch, soundfile as sf
    model, tok, dtok = _load()
    torch.manual_seed(int(key[:6], 16))
    d = dtok(VOICES[voice], return_tensors="pt"); p = tok(text, return_tensors="pt")
    a = model.generate(input_ids=d.input_ids, attention_mask=d.attention_mask, prompt_input_ids=p.input_ids, prompt_attention_mask=p.attention_mask)
    sf.write(out + ".tmp.wav", a.cpu().numpy().squeeze(), model.config.sampling_rate); os.replace(out + ".tmp.wav", out)
    return out
