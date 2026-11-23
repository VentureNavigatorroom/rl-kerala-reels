# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("iex01", "first_exporter", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ", "C": "റസിയ"}, "ദുബായിലേക്ക് ആദ്യ\nഷിപ്പ്മെന്റ്. കസ്റ്റംസിൽ\nനിന്നു", [
 ("A", "അപ്പൂപ്പാ, ദുബായിലേക്ക് ആദ്യത്തെ സ്പൈസ് ഷിപ്പ്മെന്റ്. കസ്റ്റംസ് IEC ചോദിക്കുന്നു!"),
 ("C", "അത് GST പോലെ എന്തെങ്കിലും ആണോ?"),
 ("B", "അല്ല. IEC ഇംപോർട്ട് എക്സ്പോർട്ട് കോഡ്. DGFT തരുന്ന 10 അക്ക കോഡ്, ബിസിനസിന്റെ PAN-മായി ലിങ്ക്.")],
 dict(title="IEC ഇല്ലാതെ", rows=[("സാധനം എക്സ്പോർട്ട്", "പറ്റില്ല"), ("സാധനം ഇംപോർട്ട്", "പറ്റില്ല"), ("ഒരു PAN-ന്", "ഒരു IEC")], total=("നിന്ന് പോയത്", "ആദ്യ ഷിപ്പ്മെന്റ്")),
 ["ഓർഡർ ഉറപ്പിക്കും മുമ്പ് IEC എടുക്കുക.", "സ്വന്തം ആവശ്യത്തിനുള്ള ഇംപോർട്ടിന് IEC വേണ്ട. ബിസിനസിന് വേണം."],
 "ഷിപ്പ്മെന്റിന് മുമ്പ്\nIEC", topics.CTA_EXPORT, mentor="B", series="ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്", ep=1, next="IEC ഡീആക്ടിവേറ്റ് ആയാൽ?", scene="shop", theme="faq")

toon("iex02", "spice_trade", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ"}, "IEC ഉണ്ടായിരുന്നു.\nഇപ്പോ ഡീആക്ടിവേറ്റ്!", [
 ("A", "അപ്പൂപ്പാ, IEC ഒരിക്കലും എക്സ്പയർ ആകില്ലെന്നല്ലേ? എന്നിട്ടും ഡീആക്ടിവേറ്റ് ആയി!"),
 ("B", "എക്സ്പയർ ആകില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം."),
 ("A", "ഞാൻ അത് ചെയ്തില്ല..."),
 ("B", "അതാ കാരണം. അപ്ഡേറ്റ് മറന്നാൽ IEC ഡീആക്ടിവേറ്റ് ആകും.")],
 dict(title="IEC വർഷാവർഷം", rows=[("കാലാവധി", "ഇല്ല"), ("അപ്ഡേറ്റ്", "ഏപ്രിൽ-ജൂൺ"), ("അപ്ഡേറ്റ് മറന്നാൽ", "ഡീആക്ടിവേറ്റ്")], total=("നിന്ന് പോകുന്നത്", "ഷിപ്പ്മെന്റ്")),
 ["എല്ലാ ഏപ്രിലിലും IEC അപ്ഡേറ്റ് റിമൈൻഡർ ഇടുക.", "സർവീസ് എക്സ്പോർട്ടർമാർക്കും ബെനഫിറ്റിന് IEC വേണം."],
 "ഏപ്രിൽ-ജൂൺ:\nIEC അപ്ഡേറ്റ്", topics.CTA_IEC, mentor="B", series="ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്", ep=2, next="സർവീസ് എക്സ്പോർട്ട്", scene="office", theme="faq")
