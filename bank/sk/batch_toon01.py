# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("mx01", "idea_stage", "B", {"A": "അഞ്ജലി", "B": "അപ്പൂപ്പൻ", "C": "കിരൺ"}, "ഗ്രാന്റിന്\nസെലക്ട് ആയി.\nപൈസ നിന്നു", [
 ("A", "അപ്പൂപ്പാ, ഐഡിയ ഗ്രാന്റിന് ഞാൻ സെലക്ട് ആയി! പക്ഷേ പൈസ റിലീസ് ആകുന്നില്ല."),
 ("C", "കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ടില്ലല്ലോ അവൾ."),
 ("B", "ഐഡിയ ഗ്രാന്റിന് കമ്പനിക്ക് മുമ്പ് അപേക്ഷിക്കാം. പക്ഷേ പൈസ റിലീസ് ആകും മുമ്പ് കമ്പനിയും KSUM യുണീക്ക് ID-യും വേണം.")],
 dict(title="ഗ്രാന്റ് പൈസയ്ക്ക് മുമ്പ്", rows=[("കേരളത്തിൽ രജിസ്റ്റർ", "വേണം"), ("Pvt Ltd / LLP, ആക്ടീവ്", "വേണം"), ("KSUM യുണീക്ക് ID", "വേണം")], total=("ഇല്ലെങ്കിൽ", "പൈസ നിൽക്കും")),
 ["സെലക്ഷൻ കാത്തിരിക്കാതെ കമ്പനി രജിസ്ട്രേഷൻ തുടങ്ങുക.", "KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ യുണീക്ക് ID-ക്ക് അപേക്ഷിക്കുക."],
 "സെലക്ഷൻ കിട്ടിയാൽ\nകമ്പനി റെഡി ആക്കൂ", topics.CTA_GRANT, mentor="B", series="അഞ്ജലിയുടെ ഐഡിയ", ep=1, next="DPIIT-യും വേണോ?", scene="busstop", theme="faq")

toon("mx02", "kerala_registered", "B", {"A": "അഞ്ജലി", "B": "അപ്പൂപ്പൻ"}, "KSUM ID മാത്രം\nപോരാ?", [
 ("A", "അപ്പൂപ്പാ, KSUM യുണീക്ക് ID കിട്ടി. ഇനി ഏത് ഗ്രാന്റിനും അപേക്ഷിക്കാമല്ലോ?"),
 ("B", "മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും DPIIT റെക്കഗ്നിഷനും ചോദിക്കും."),
 ("A", "തുക എത്ര കിട്ടും?"),
 ("B", "തുകയും കോളുകളും മാറും. ലൈവ് കോൾ നോക്കിയിട്ടേ ഉറപ്പിക്കാവൂ.")],
 dict(title="KSUM ഗ്രാന്റ് ചെക്ക്ലിസ്റ്റ്", rows=[("KSUM യുണീക്ക് ID", "വേണം"), ("DPIIT", "മിക്കതിനും"), ("MCA സ്റ്റാറ്റസ്", "ആക്ടീവ്")], total=("ലൈവ് കോൾ", "എപ്പോഴും നോക്കുക")),
 ["യുണീക്ക് ID-യും DPIIT-യും ഒരുമിച്ച് റെഡി ആക്കുക.", "ഗ്രാന്റ് തുകയ്ക്ക് ലൈവ് കോൾ മാത്രം വിശ്വസിക്കുക."],
 "ID + DPIIT =\nറെഡി", topics.CTA_KSUM, mentor="B", series="അഞ്ജലിയുടെ ഐഡിയ", ep=2, next="ഇൻകുബേഷൻ", scene="office", theme="faq")
