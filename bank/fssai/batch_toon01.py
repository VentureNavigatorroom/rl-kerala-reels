# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("fsy01", "home_baker", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ", "C": "അഞ്ജലി"}, "സ്വിഗ്ഗി ചോദിച്ചു:\n”FSSAI നമ്പർ?”", [
 ("A", "അമ്മൂമ്മേ, എന്റെ വീട്ടിലെ കേക്ക് ഡെലിവറി ആപ്പിൽ ഇടാൻ നോക്കി. FSSAI നമ്പർ ചോദിക്കുന്നു!"),
 ("C", "വീട്ടിൽ ഉണ്ടാക്കുന്നതിനും ലൈസൻസോ?"),
 ("B", "അതെ മോളേ. ഹോം ബേക്കർമാർക്കും FSSAI വേണം. വർഷം 1.5 കോടി വരെ ടേൺഓവർ ആണെങ്കിൽ ബേസിക് രജിസ്ട്രേഷൻ മതി.")],
 dict(title="ഏത് FSSAI വേണം?\n(2026 ഏപ്രിൽ മുതൽ)", rows=[("1.5 കോടി വരെ", "രജിസ്ട്രേഷൻ"), ("1.5 കോടി - 50 കോടി", "സ്റ്റേറ്റ് ലൈസൻസ്"), ("50 കോടിക്ക് മുകളിൽ", "സെൻട്രൽ ലൈസൻസ്")], total=("ഇല്ലാതെ വിറ്റാൽ പിഴ", "5 ലക്ഷം വരെ")),
 ["ആപ്പിൽ ലിസ്റ്റ് ചെയ്യും മുമ്പ് FSSAI എടുക്കുക.", "പാക്കറ്റിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യുക."],
 "വീട്ടിലെ കേക്കിനും\nFSSAI വേണം", topics.CTA_FSSAI, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=1, next="പഴയ ലൈസൻസ് ഉള്ളവർക്ക്?", scene="home", theme="faq")

toon("fsy02", "cloud_kitchen", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ"}, "ലൈസൻസ് പുതുക്കാൻ\nഓടി. വേണ്ടായിരുന്നു!", [
 ("A", "അമ്മൂമ്മേ, FSSAI അഞ്ച് വർഷം കഴിഞ്ഞു എന്ന് കരുതി പുതുക്കാൻ ഓടി."),
 ("B", "2026-ലെ മാറ്റത്തോടെ FSSAI രജിസ്ട്രേഷനും ലൈസൻസിനും സ്ഥിരം സാധുതയാണ്. നിയമങ്ങൾ പാലിച്ചാൽ മതി."),
 ("A", "അപ്പോ എനിക്ക് ഒന്നും ചെയ്യാനില്ലേ?"),
 ("B", "വിവരങ്ങൾ ശരിയായി സൂക്ഷിക്കുക. ടേൺഓവർ മാറിയാൽ ശരിയായ കാറ്റഗറിയിലേക്ക് മാറുക.")],
 dict(title="2026 ഏപ്രിൽ മുതലുള്ള മാറ്റം", rows=[("സാധുത", "സ്ഥിരം"), ("നിയമം പാലിക്കൽ", "തുടരണം"), ("ടേൺഓവർ മാറിയാൽ", "കാറ്റഗറി മാറണം")], total=("പഴയ വിവരം", "പഴയതാണ്")),
 ["പഴയ നിയമം കേട്ട് ഓടരുത്. FoSCoS-ൽ നോക്കുക.", "ടേൺഓവർ മാറിയാൽ ശരിയായ കാറ്റഗറി ഉറപ്പാക്കുക."],
 "FSSAI ഇനി\nസ്ഥിരം", topics.CTA_FOOD, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=2, next="പാക്കറ്റ് ലേബൽ", scene="shop", theme="faq")

