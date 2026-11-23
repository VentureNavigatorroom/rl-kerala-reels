# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("ux01", "traditional_innovator", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ", "C": "അമൽ"}, "പ്രൊപ്രൈറ്റർഷിപ്പിന്\nDPIIT റിജക്ട്", [
 ("A", "അമ്മൂമ്മേ, എന്റെ പുതിയ കയർ മെഷീന് DPIIT അപേക്ഷിച്ചു. റിജക്ട് ആയി!"),
 ("C", "ഇന്നൊവേഷൻ ഉണ്ടല്ലോ. പിന്നെന്താ പ്രശ്നം?"),
 ("B", "ബിസിനസ് പ്രൊപ്രൈറ്റർഷിപ്പ് ആണ്. DPIIT-ക്ക് പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് പോലുള്ളവ വേണം.")],
 dict(title="DPIIT കിട്ടാൻ", rows=[("സ്ട്രക്ചർ", "Pvt Ltd / LLP / പാർട്ണർഷിപ്പ്"), ("പ്രായം", "10 വർഷത്തിൽ താഴെ"), ("ടേൺഓവർ", "200 കോടി വരെ")], total=("പ്രൊപ്രൈറ്റർഷിപ്പ്", "പറ്റില്ല")),
 ["DPIIT-ക്ക് മുമ്പ് ശരിയായ സ്ട്രക്ചർ ആക്കുക.", "ഇന്നൊവേഷൻ അല്ലെങ്കിൽ സ്കെയിൽ ആകുന്ന മോഡൽ വ്യക്തമായി കാണിക്കുക."],
 "ആദ്യം സ്ട്രക്ചർ,\nപിന്നെ DPIIT", topics.CTA_DPIIT, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=1, next="DPIIT കൊണ്ട് എന്ത് കിട്ടും?", scene="road", theme="faq")

toon("ux02", "tech_founder", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ"}, "DPIIT കിട്ടി.\nഇനി എന്ത് ഗുണം?", [
 ("A", "അമ്മൂമ്മേ, DPIIT സർട്ടിഫിക്കറ്റ് കിട്ടി. ഇത് ഫ്രെയിം ചെയ്ത് വെക്കാനാണോ?"),
 ("B", "അല്ല മോനേ. പേറ്റന്റിനും ട്രേഡ്മാർക്കിനും ഫയലിംഗിൽ ഇളവ്, പല സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും യോഗ്യത."),
 ("A", "പേറ്റന്റ് ഫയൽ ചെയ്യാനിരിക്കുകയായിരുന്നു ഞാൻ!")],
 dict(title="DPIIT കൊണ്ടുള്ള ഗുണങ്ങൾ", rows=[("പേറ്റന്റ് ഫയലിംഗ്", "80% ഇളവ്"), ("ട്രേഡ്മാർക്ക് ഫയലിംഗ്", "50% ഇളവ്"), ("IP പരിശോധന", "വേഗത്തിൽ")], total=("ഉപയോഗിച്ചില്ലെങ്കിൽ", "ഗുണം പോകും")),
 ["പേറ്റന്റും ട്രേഡ്മാർക്കും DPIIT കിട്ടിയ ശേഷം ഫയൽ ചെയ്യുക.", "കേന്ദ്ര, സംസ്ഥാന സ്കീമുകളും ടെൻഡറുകളും നോക്കുക."],
 "സർട്ടിഫിക്കറ്റ്\nഉപയോഗിക്കൂ", topics.CTA_BENEFITS, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=2, next="KSUM ID", scene="office", theme="faq")
