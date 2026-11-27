# Toon batch 03 for iec (27 Nov evening), episode 7 of "ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്" (ep 6 teased "ഷിപ്പ്മെന്റ് ദിവസം"). Facts only from topics.FACTS_IEC. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("iex07", "spice_trade", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ", "C": "ഷഫീഖ്"}, "ഷിപ്പ്മെന്റ് ദിവസം\nബാങ്ക് ചോദിച്ചു:\n\"IEC നമ്പർ?\"", [
 ("C", "ഫൈസലേ, കണ്ടെയ്നർ റെഡി. ബാങ്കും കസ്റ്റംസ് ഏജന്റും IEC നമ്പർ ചോദിക്കുന്നു. ഞാൻ പറഞ്ഞു, അത് PAN തന്നെയല്ലേ എന്ന്."),
 ("A", "അപ്പൂപ്പാ, IEC എന്റെ PAN-മായി ലിങ്ക് ആണല്ലോ. പ്രശ്നം ഉണ്ടോ?"),
 ("B", "IEC 10 അക്ക കോഡ് ആണ്, PAN-മായി ലിങ്ക് ചെയ്തത്. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും.")],
 dict(title="ഷിപ്പ്മെന്റിന് മുമ്പ്", rows=[("IEC നമ്പർ", "കയ്യിൽ"), ("ഈ വർഷത്തെ അപ്ഡേറ്റ്", "ചെയ്തോ?"), ("ബാങ്ക്, കസ്റ്റംസ്", "ചോദിക്കും")], total=("ഡീആക്ടിവേറ്റ് ആണെങ്കിൽ", "ഷിപ്പ്മെന്റ് നിൽക്കാം")),
 ["ഷിപ്പ്മെന്റിന് ഒരാഴ്ച മുമ്പ് IEC സ്റ്റാറ്റസ് നോക്കുക.", "ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് കലണ്ടറിൽ ഇടുക."],
 "ഷിപ്പ്മെന്റിന് മുമ്പ്\nIEC സ്റ്റാറ്റസ്", topics.CTA_EXPORT, mentor="B", series="ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്", ep=7, next="അടുത്ത സീസൺ", scene="shop", theme="new")
