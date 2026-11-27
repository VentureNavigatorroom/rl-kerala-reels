# Toon batch 03 for sk (27 Nov evening), episode 7 of "അഞ്ജലിയുടെ ഐഡിയ" (ep 6 teased "ഇൻകുബേഷൻ"). Facts only from topics.FACTS_SK.
# Never grant amounts, never promise selection.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("mx07", "kerala_registered", "B", {"A": "അഞ്ജലി", "B": "അപ്പൂപ്പൻ", "C": "കിരൺ"}, "ഇൻകുബേഷന്\nഅപേക്ഷിക്കും മുമ്പ്\nMCA-യിൽ ഒരു വാക്ക്", [
 ("C", "അഞ്ജലീ, ഇൻകുബേഷൻ അപേക്ഷ നാളെ കൊടുക്കാം. കമ്പനി രേഖകൾ എല്ലാം ഞാൻ എടുത്തു വെച്ചു."),
 ("A", "അപ്പൂപ്പാ, ഇനി എന്തെങ്കിലും നോക്കാൻ ഉണ്ടോ?"),
 ("B", "MCA-യിൽ കമ്പനിയുടെ സ്റ്റാറ്റസ് 'ആക്ടീവ്' എന്ന് ആണോ എന്ന് നോക്കൂ. മിക്ക KSUM സ്കീമുകളും അത് ചോദിക്കും. KSUM യുണീക്ക് ഐഡിയും വേണം.")],
 dict(title="KSUM അപേക്ഷയ്ക്ക് മുമ്പ്", rows=[("KSUM യുണീക്ക് ഐഡി", "ഉണ്ടോ?"), ("MCA സ്റ്റാറ്റസ്", "ആക്ടീവ്"), ("കേരളത്തിൽ രജിസ്ട്രേഷൻ", "വേണം")], total=("സെലക്ഷൻ", "ഉറപ്പില്ല, ഒരുക്കം നമ്മുടേത്")),
 ["അപേക്ഷയുടെ തലേന്ന് MCA-യിൽ കമ്പനി സ്റ്റാറ്റസ് നോക്കുക.", "ഓരോ കോളിന്റെയും നിബന്ധന ടീമിനെ കൊണ്ട് ഒത്തുനോക്കുക."],
 "അപേക്ഷയ്ക്ക് മുമ്പ്\nസ്റ്റാറ്റസ് ആക്ടീവ്", topics.CTA_KSUM, mentor="B", series="അഞ്ജലിയുടെ ഐഡിയ", ep=7, next="അടുത്ത സീസൺ", scene="office", theme="faq")
