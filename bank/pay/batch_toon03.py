# Toon batch 03 for pay (27 Nov evening refill): episode 7 of "ലിജോയുടെ ബേക്കറി". Facts only from topics.FACTS_PAY.
# Never promise an incentive, never our fee; disputes / inspections go to a labour-law professional.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("pyx07", "ten_staff", "B", {"A": "ലിജോ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "ശമ്പളം കൂട്ടി.\nദിവ്യ ചോദിച്ചു:\n\"എന്റെ ESI പോകുമോ?\"", [
 ("C", "ലിജോ, ശമ്പളം 24,000 ആക്കിയതിന് നന്ദി. പക്ഷേ ഇനി എനിക്ക് ESI ഉണ്ടാകുമോ?"),
 ("A", "അമ്മൂമ്മേ, ബേക്കറിയിൽ 12 പേരുണ്ട്. ESIC ഉള്ള സ്ഥാപനമല്ലേ നമ്മുടേത്?"),
 ("B", "ESI കവറേജിന് മാസ വേതന പരിധി 21,000 രൂപയാണ്. അതിന് മുകളിലായാൽ കവറേജ് വിട്ടുപോകും. എപ്പോൾ മുതൽ എന്ന് ടീമിനോട് ചോദിക്കാം.")],
 dict(title="ESIC ഒറ്റ നോട്ടത്തിൽ", rows=[("സ്ഥാപനം", "10-ഓ അതിലധികമോ ജീവനക്കാർ"), ("വേതന പരിധി", "മാസം 21,000 രൂപ വരെ"), ("ശമ്പളം കൂടിയാൽ", "പരിധി നോക്കുക")], total=("കാര്യം", "സ്റ്റാഫിനോട് മുൻകൂട്ടി പറയുക")),
 ["ശമ്പളം കൂട്ടുമ്പോൾ ESI, PF പരിധികൾ ഒന്ന് നോക്കുക.", "മാറ്റം എന്ത് എന്ന് ജീവനക്കാരനോട് നേരത്തെ പറയുക."],
 "ശമ്പളം കൂട്ടും മുമ്പ്\nപരിധി നോക്കൂ", topics.CTA_ESIC, mentor="B", series="ലിജോയുടെ ബേക്കറി", ep=7, next="അടുത്ത സീസൺ", scene="shop", theme="faq")
