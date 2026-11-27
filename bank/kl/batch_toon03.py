# Toon batch 03 for kl (27 Nov evening refill): episode 7 of "ബിനുവിന്റെ പുതിയ കട". Facts only from topics.FACTS_KL.
# Never a home-business rule, a penalty or our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("lcx07", "town_business", "B", {"A": "ബിനു", "B": "അപ്പൂപ്പൻ", "C": "ശ്രുതി"}, "\"ഇത് കടയല്ല,\nഓഫീസാ.\nഷോപ്സ് ആക്ട് വേണ്ട\"", [
 ("C", "ബിനൂ, ഞാൻ മുകളിലത്തെ നിലയിൽ ഒരു ചെറിയ ഡിസൈൻ ഓഫീസ് തുടങ്ങി. ഇത് കട അല്ലല്ലോ, ഷോപ്സ് ആക്ട് വേണ്ടല്ലോ?"),
 ("A", "അപ്പൂപ്പാ, സാധനം വിൽക്കാത്ത ഓഫീസിനും അത് വേണോ?"),
 ("B", "ഷോപ്പുകൾക്ക് മാത്രമല്ല, കൊമേഴ്സ്യൽ സ്ഥാപനങ്ങൾക്കും ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ വേണം. സ്റ്റാഫ് ഇല്ലെങ്കിലും, തുടങ്ങി 60 ദിവസത്തിനകം.")],
 dict(title="ആർക്കൊക്കെ ഷോപ്സ് ആക്ട്", rows=[("കടകൾ", "വേണം"), ("ഓഫീസ്, സ്റ്റുഡിയോ", "വേണം"), ("സ്റ്റാഫ് ഇല്ലെങ്കിലും", "വേണം")], total=("സമയം", "തുടങ്ങി 60 ദിവസത്തിനകം")),
 ["ആദ്യം തദ്ദേശ സ്ഥാപന ലൈസൻസ്, പിന്നെ അതിന്റെ കോപ്പി വെച്ച് ഓൺലൈനായി ഷോപ്സ് ആക്ട്.", "ബോർഡ് ഇല്ലെങ്കിലും നിയമം ഒന്നുതന്നെ."],
 "കടയായാലും ഓഫീസായാലും\nഷോപ്സ് ആക്ട്", topics.CTA_SHOPS, mentor="B", series="ബിനുവിന്റെ പുതിയ കട", ep=7, next="അടുത്ത സീസൺ", scene="office", theme="faq")
