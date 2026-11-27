# Toon batch 03 for ud (27 Nov evening), episode 7 of "ബിനുവിന്റെ വർക്ക്ഷോപ്പ്" (ep 6 teased "ക്ലാസ് മാറ്റം"). Facts only from topics.FACTS_UD. No fees, never promise a loan or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("yx07", "manufacturer", "B", {"A": "ബിനു", "B": "അപ്പൂപ്പൻ", "C": "സുരേഷ്"}, "പുതിയ മെഷീൻ വാങ്ങി.\nഇപ്പോഴും\nമൈക്രോ തന്നെയോ?", [
 ("C", "ബിനൂ, പുതിയ CNC മെഷീൻ വന്നല്ലോ! ടേൺഓവർ ഇപ്പോഴും കുറവാണ്. അപ്പോ ഇപ്പോഴും മൈക്രോ അല്ലേ?"),
 ("A", "അപ്പൂപ്പാ, ടേൺഓവർ മാത്രം നോക്കിയാൽ പോരേ?"),
 ("B", "പോരാ. മൈക്രോ ആകാൻ നിക്ഷേപം രണ്ടര കോടി വരെയും ടേൺഓവർ 10 കോടി വരെയും വേണം. ഏതെങ്കിലും ഒന്ന് കടന്നാൽ മുകളിലെ ക്ലാസ്.")],
 dict(title="മൈക്രോയിൽ നിന്ന് സ്മോൾ", rows=[("മൈക്രോ", "നിക്ഷേപം 2.5 കോടി, ടേൺഓവർ 10 കോടി വരെ"), ("സ്മോൾ", "25 കോടി, 100 കോടി വരെ"), ("ഒന്ന് കടന്നാൽ", "മുകളിലെ ക്ലാസ്")], total=("ഉദ്യമിൽ", "വിവരം പുതുക്കി വെക്കുക")),
 ["വലിയ മെഷീൻ വാങ്ങിയാൽ നിക്ഷേപ കണക്ക് ഒന്ന് നോക്കുക.", "ഉദ്യം വിവരങ്ങൾ എപ്പോഴും പുതുക്കി വെക്കുക."],
 "രണ്ട് പരിധിയും\nഒരുമിച്ച് നോക്കൂ", topics.CTA_MSME, mentor="B", series="ബിനുവിന്റെ വർക്ക്ഷോപ്പ്", ep=7, next="അടുത്ത സീസൺ", scene="shop", theme="faq")
