# Toon batch 03 for nda (27 Nov evening), episode 7 of "ഹന്നയുടെ ഡിസൈൻ ഏജൻസി". Facts only from topics.FACTS_NDA. General information, no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("ndx07", "agency_client", "B", {"A": "ഹന്ന", "B": "അപ്പൂപ്പൻ", "C": "ആൽബിൻ"}, "ക്ലയന്റ് പറഞ്ഞു:\n\"ഇത് ഞങ്ങളുടെ ഐഡിയ.\nNDA ലംഘിച്ചു\"", [
 ("C", "ഹന്നേ, നീ ഞങ്ങൾക്ക് ചെയ്ത ആപ്പ് ഡിസൈൻ പോലെ ഒന്ന് വേറെ ക്ലയന്റിനും ചെയ്തു. NDA ലംഘിച്ചില്ലേ?"),
 ("A", "അപ്പൂപ്പാ, ആ ഡിസൈൻ സ്റ്റൈൽ ഞങ്ങൾ അവർ വരുന്നതിന് മുമ്പേ ഉണ്ടാക്കിയതാണ്. എന്നിട്ടും?"),
 ("B", "നല്ല NDA-യിൽ ഒഴിവാക്കലുകൾ എഴുതും: ഇതിനകം പബ്ലിക് ആയതും സ്വന്തമായി ഉണ്ടാക്കിയതും. തെളിവ് ആയി പഴയ ഫയലുകൾ സൂക്ഷിക്കണം.")],
 dict(title="NDA-യിൽ ഒഴിവാക്കൽ", rows=[("ഇതിനകം പബ്ലിക്", "പരിരക്ഷയില്ല"), ("സ്വന്തമായി ഉണ്ടാക്കിയത്", "ഒഴിവാക്കാം"), ("തെളിവ്", "തീയതിയുള്ള ഫയലുകൾ")], total=("ഒഴിവാക്കൽ ഇല്ലെങ്കിൽ", "തർക്കം")),
 ["ഒപ്പിടും മുമ്പ് ഒഴിവാക്കലുകൾ NDA-യിൽ ഉണ്ടോ എന്ന് നോക്കുക.", "സ്വന്തം വർക്കിന്റെ തീയതിയുള്ള ഫയലുകൾ സൂക്ഷിക്കുക."],
 "ഒപ്പിടും മുമ്പ്\nഒഴിവാക്കൽ വായിക്കൂ", topics.CTA_NDA, mentor="B", series="ഹന്നയുടെ ഡിസൈൻ ഏജൻസി", ep=7, next="അടുത്ത സീസൺ", scene="office", theme="faq")
