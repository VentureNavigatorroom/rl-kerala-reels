# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
from importlib import util as _u
_b = _u.spec_from_file_location('b1', os.path.join(os.path.dirname(__file__), 'batch01.py')); _m = _u.module_from_spec(_b); _b.loader.exec_module(_m)
CTA_START, CTA_NAME = _m.CTA_START, _m.CTA_NAME

toon("kx01", "proprietor", "B", {"A": "വിഷ്ണു", "B": "അപ്പൂപ്പൻ", "C": "അനു"}, "ഇൻവെസ്റ്റർ റെഡി.\nപക്ഷേ എന്റേത്\nപ്രൊപ്രൈറ്റർഷിപ്പ്", [
 ("A", "അപ്പൂപ്പാ, ഒരു ഇൻവെസ്റ്റർ ഷെയർ വാങ്ങാൻ റെഡി. പക്ഷേ എന്റെ കട പ്രൊപ്രൈറ്റർഷിപ്പ് ആണ്."),
 ("C", "ഷെയർ ഇല്ലാത്ത ബിസിനസിന് എങ്ങനെ ഷെയർ കൊടുക്കും?"),
 ("B", "അതാണ് കാര്യം. ഷെയർ കൊടുത്ത് ഇക്വിറ്റി എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്കേ പറ്റൂ.")],
 dict(title="ഷെയർ കൊടുക്കാൻ പറ്റുമോ?", rows=[("പ്രൊപ്രൈറ്റർഷിപ്പ്", "ഇല്ല"), ("പാർട്ണർഷിപ്പ്", "ഇല്ല"), ("LLP", "ഇല്ല")], total=("പ്രൈവറ്റ് ലിമിറ്റഡ്", "പറ്റും")),
 ["ഇൻവെസ്റ്റ്മെന്റ് വേണമെങ്കിൽ നേരത്തെ പ്രൈവറ്റ് ലിമിറ്റഡ് ആക്കുക.", "ഇൻവെസ്റ്റർ വരുന്നതിന് മുമ്പ് സ്ട്രക്ചർ റെഡി ആക്കുക."],
 "ഇൻവെസ്റ്റർ വരും മുമ്പ്\nകമ്പനി", CTA_START, mentor="B", series="വിഷ്ണുവിന്റെ കട", ep=1, next="കമ്പനി പേര് റിജക്ട്", scene="shop", theme="faq")

toon("kx02", "solo", "B", {"A": "വിഷ്ണു", "B": "അപ്പൂപ്പൻ", "C": "റിയ"}, "പേര് അപ്രൂവ് ആയി.\nഎന്നിട്ടും ബ്രാൻഡ്\nപോയി", [
 ("A", "അപ്പൂപ്പാ, കമ്പനി പേര് അപ്രൂവ് ആയി. പക്ഷേ അതേ പേരിൽ വേറെ ഒരാൾക്ക് ട്രേഡ്മാർക്ക്!"),
 ("C", "പേര് അപ്രൂവ് ആയാൽ അത് നമ്മുടേതല്ലേ?"),
 ("B", "കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡ് സംരക്ഷിക്കില്ല. പേരിന് മുമ്പ് ട്രേഡ്മാർക്ക് സെർച്ചും നോക്കണം.")],
 dict(title="പേര് തിരഞ്ഞെടുക്കും മുമ്പ്", rows=[("സമാന കമ്പനി പേരുകൾ", "നോക്കണം"), ("ട്രേഡ്മാർക്ക് സെർച്ച്", "നോക്കണം"), ("ബ്രാൻഡ് സംരക്ഷണം", "ട്രേഡ്മാർക്ക്")], total=("നോക്കാതിരുന്നാൽ", "റീബ്രാൻഡിംഗ്")),
 ["പേര് ഉറപ്പിക്കും മുമ്പ് ട്രേഡ്മാർക്ക് സെർച്ച് ചെയ്യുക.", "ബ്രാൻഡിന് പ്രത്യേകം ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യുക."],
 "പേര് അപ്രൂവൽ ≠\nബ്രാൻഡ്", CTA_NAME, mentor="B", series="വിഷ്ണുവിന്റെ കട", ep=2, next="കമ്പനിക്ക് ശേഷം എന്ത്?", scene="teashop", theme="faq")
