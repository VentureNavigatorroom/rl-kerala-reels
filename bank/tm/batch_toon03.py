# Toon batch 03 for tm (27 Nov evening), episode 7 of "ദിവ്യയുടെ കേക്ക് ബ്രാൻഡ്" (ep 6 teased "പുതുക്കൽ"). Facts only from topics.FACTS_TM. No fees, never promise registration.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("tmx07", "food_brand", "B", {"A": "ദിവ്യ", "B": "അമ്മൂമ്മ", "C": "ഗായത്രി"}, "ട്രേഡ്മാർക്ക് കിട്ടി.\nഇനി ജീവിതകാലം\nമുഴുവൻ എന്റേത്?", [
 ("C", "ദിവ്യേ, കേക്ക് ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് രജിസ്ട്രേഷൻ കിട്ടിയല്ലോ! ഇനി അത് എന്നും നിന്റേതല്ലേ?"),
 ("A", "അമ്മൂമ്മേ, ഒരിക്കൽ കിട്ടിയാൽ പിന്നെ ഒന്നും ചെയ്യേണ്ടല്ലോ?"),
 ("B", "രജിസ്ട്രേഷന് 10 വർഷമാണ് കാലാവധി മോളേ. പിന്നെ പുതുക്കണം. പുതുക്കിയാൽ വീണ്ടും 10 വർഷം.")],
 dict(title="ട്രേഡ്മാർക്ക് കാലാവധി", rows=[("രജിസ്ട്രേഷൻ", "10 വർഷം"), ("പിന്നെ", "പുതുക്കൽ"), ("പുതുക്കിയാൽ", "വീണ്ടും 10 വർഷം")], total=("മറന്നാൽ", "സംരക്ഷണം നഷ്ടപ്പെടാം")),
 ["രജിസ്ട്രേഷൻ തീയതി കലണ്ടറിൽ 10 വർഷത്തേക്ക് ഇടുക.", "ബ്രാൻഡ് രേഖകൾ ഒരു ഫോൾഡറിൽ സൂക്ഷിക്കുക."],
 "10 വർഷം കഴിഞ്ഞാൽ\nപുതുക്കൽ", topics.CTA_TRADEMARK, mentor="B", series="ദിവ്യയുടെ കേക്ക് ബ്രാൻഡ്", ep=7, next="അടുത്ത സീസൺ", scene="shop", theme="faq")
