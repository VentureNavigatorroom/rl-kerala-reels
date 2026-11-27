# kl batch 02 (27 Nov evening refill): 3D duo reel. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns. Facts only from topics.FACTS_KL. Never a home-business rule, a penalty or our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

# new: a mobile shop moves from a panchayat junction into the municipality town; the old licence was for the old place
duo("lcd006", "town_business", "B", "mobileshop", "കട ടൗണിലേക്ക് മാറ്റി.\nപഞ്ചായത്ത് ലൈസൻസ്\nകൂടെ വരുമോ?", [
 ("A","wide","ഫഹദേ, പുതിയ കട മുനിസിപ്പാലിറ്റി ടൗണിലാണ്. പഴയ പഞ്ചായത്ത് ലൈസൻസ് ചുമരിൽ തൂക്കിയാൽ പോരേ?"),
 ("V","V","ഹന്നാ, ആ ലൈസൻസ് പഴയ സ്ഥലത്തെ കടയ്ക്കുള്ളതാണ്. ബിസിനസ് നടക്കുന്ന സ്ഥലത്തെ തദ്ദേശ സ്ഥാപനം തന്നെ ലൈസൻസ് തരണം."),
 ("A","A","അപ്പോ പുതിയ സ്ഥലത്ത് മുനിസിപ്പാലിറ്റി ലൈസൻസ്. ടൗണിൽ അത് K-SMART വഴിയല്ലേ?"),
 ("V","V","അതെ. പിന്നെ ഷോപ്സ് ആക്ട് രേഖയിലും പുതിയ ലൈസൻസ് കോപ്പി വേണം."),
 ("A","wide","കട മാറിയാൽ ലൈസൻസും മാറണം.")],
 "പുതിയ സ്ഥലം,\nപുതിയ ലൈസൻസ്", CTA_KSMART, theme="new",
 cap_ml="കട ഒരു പഞ്ചായത്തിൽ നിന്ന് മുനിസിപ്പാലിറ്റി ടൗണിലേക്ക് മാറ്റിയോ? ലൈസൻസ് ബിസിനസ് നടക്കുന്ന സ്ഥലത്തെ തദ്ദേശ സ്ഥാപനത്തിന്റേതാണ്; ടൗണുകളിൽ K-SMART വഴി. ഷോപ്സ് ആക്ട് രേഖയിലും പുതിയ ലൈസൻസ് കോപ്പി വേണം. നിങ്ങളുടെ കട ഏത് തദ്ദേശ സ്ഥാപനത്തിലാണ്?",
 cap_en="A mobile shop moves from a panchayat junction into a municipality town and plans to keep the old licence on the wall. The licence comes from the local body where the business runs; towns use K-SMART. The Shops Act record needs the new licence copy too. Which local body is your shop in?",
 cap_mg="Kada oru panchayat-il ninnu municipality town-ilekku maattiyo? Licence business nadakkunna sthalathe local body-yudethaanu; town-ukalil K-SMART vazhi. Shops Act rekhayilum puthiya licence copy venam. Ningalude kada ethu local body-yilaanu?")
