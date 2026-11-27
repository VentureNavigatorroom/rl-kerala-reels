# Toon batch 03 for roc (27 Nov evening), episode 7 of "മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി" (ep 6 teased "LLP കലണ്ടർ"). Facts only from topics.FACTS_ROC. No fees of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("rcx07", "llp_owner", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ", "C": "ശ്വേത"}, "LLP ആണ്, കമ്പനി അല്ല.\nഅപ്പോ ROC ഫയലിംഗ്\nഇല്ലല്ലോ?", [
 ("C", "മനോജേട്ടാ, എന്റെ ട്രാവൽ ബിസിനസ് LLP ആണ്. AGM ഒന്നും ഇല്ല. അപ്പോ ഫയലിംഗും വേണ്ടല്ലോ?"),
 ("A", "അപ്പൂപ്പാ, LLP-ക്കും വർഷത്തിൽ ഫയലിംഗ് ഉണ്ടോ?"),
 ("B", "ഉണ്ട്. ഫോം 11 മെയ് 30-നകം, ഫോം 8 ഒക്ടോബർ 30-നകം. ബിസിനസ് ഇല്ലാത്ത വർഷവും. വൈകിയാൽ ഒരു ഫോമിന് ദിവസം 100 രൂപ.")],
 dict(title="LLP കലണ്ടർ", rows=[("ഫോം 11", "മെയ് 30-നകം"), ("ഫോം 8", "ഒക്ടോബർ 30-നകം"), ("ബിസിനസ് ഇല്ലെങ്കിലും", "രണ്ടും വേണം")], total=("വൈകിയാൽ", "ഫോമിന് ദിവസം 100 രൂപ")),
 ["മെയ്, ഒക്ടോബർ മാസങ്ങൾ കലണ്ടറിൽ അടയാളപ്പെടുത്തുക.", "ബിസിനസ് ഇല്ലാത്ത വർഷവും ഫയലിംഗ് മുടക്കരുത്."],
 "LLP-ക്കും രണ്ട്\nതീയതി ഉണ്ട്", topics.CTA_FILING, mentor="B", series="മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി", ep=7, next="അടുത്ത സീസൺ", scene="teashop", theme="faq")
