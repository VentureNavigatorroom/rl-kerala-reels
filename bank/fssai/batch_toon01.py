# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("fsx01", "home_baker", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ", "C": "അഞ്ജലി"}, "സ്വിഗ്ഗി ചോദിച്ചു:\n\"FSSAI നമ്പർ?\"", [
 ("A", "അമ്മൂമ്മേ, എന്റെ വീട്ടിലെ കേക്ക് ഡെലിവറി ആപ്പിൽ ഇടാൻ നോക്കി. FSSAI നമ്പർ ചോദിക്കുന്നു!"),
 ("C", "വീട്ടിൽ ഉണ്ടാക്കുന്നതിനും ലൈസൻസോ?"),
 ("B", "അതെ മോളേ. ഹോം ബേക്കർമാർക്കും വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ വേണം.")],
 dict(title="ഏത് FSSAI വേണം?", rows=[("12 ലക്ഷം വരെ", "ബേസിക് രജിസ്ട്രേഷൻ"), ("20 കോടി വരെ", "സ്റ്റേറ്റ് ലൈസൻസ്"), ("അതിന് മുകളിൽ, ഇംപോർട്ടർ", "സെൻട്രൽ ലൈസൻസ്")], total=("ഇല്ലാതെ വിറ്റാൽ പിഴ", "5 ലക്ഷം വരെ")),
 ["ആപ്പിൽ ലിസ്റ്റ് ചെയ്യും മുമ്പ് FSSAI എടുക്കുക.", "പാക്കറ്റിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യുക."],
 "വീട്ടിലെ കേക്കിനും\nFSSAI വേണം", topics.CTA_FSSAI, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=1, next="കാലാവധി കഴിഞ്ഞാൽ?", scene="home", theme="faq")

toon("fsx02", "cloud_kitchen", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ"}, "ലൈസൻസ് കാലാവധി\nകഴിഞ്ഞത് അറിഞ്ഞില്ല", [
 ("A", "അമ്മൂമ്മേ, കിച്ചൺ നല്ല ഓട്ടമാ. പക്ഷേ FSSAI കാലാവധി കഴിഞ്ഞിട്ട് ഒരു മാസമായി!"),
 ("B", "FSSAI 1 മുതൽ 5 വർഷം വരെയേ ഉള്ളൂ. കാലാവധി തീരും മുമ്പ് പുതുക്കണം."),
 ("A", "ഇപ്പോ ഞാൻ വിൽക്കുന്നത് പ്രശ്നമാണോ?"),
 ("B", "സാധുവായ FSSAI ഇല്ലാതെ വിൽക്കുന്നത് റിസ്ക്കാണ്. ഇന്ന് തന്നെ നോക്കണം.")],
 dict(title="FSSAI കാലാവധി", rows=[("സാധുത", "1-5 വർഷം"), ("പുതുക്കേണ്ടത്", "കാലാവധിക്ക് മുമ്പ്"), ("ഡെലിവറി ആപ്പുകൾ", "നമ്പർ ചോദിക്കും")], total=("ഇല്ലാതെ വിറ്റാൽ", "6 മാസം വരെ തടവ്")),
 ["കാലാവധി തീയതി ഫോണിൽ റിമൈൻഡർ ഇടുക.", "പുതുക്കൽ കാലാവധിക്ക് മുമ്പ് തന്നെ ചെയ്യുക."],
 "കാലാവധിക്ക് മുമ്പ്\nപുതുക്കൂ", topics.CTA_FOOD, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=2, next="പാക്കറ്റ് ലേബൽ", scene="shop", theme="faq")
