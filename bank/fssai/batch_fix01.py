# FSSAI correction (24 Nov): our reels quoted the old Rs 12 lakh / Rs 20 crore limits and 1-5 year validity.
# From 1 Apr 2026 (amendment regulations, gazette 10 Mar 2026; FSSAI order 13 Mar 2026): registration up to Rs 1.5 crore,
# state licence above that up to Rs 50 crore, central above Rs 50 crore; perpetual validity. A follower pointed it out.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

lst("fsfix01", "cafe_owner", "B", "തിരുത്ത്: FSSAI\nലിമിറ്റ് മാറി", [
 ("1.5 കോടി വരെ: രജിസ്ട്രേഷൻ", "2026 ഏപ്രിൽ 1 മുതൽ. മുമ്പ് 12 ലക്ഷം ആയിരുന്നു."),
 ("1.5 കോടി - 50 കോടി: സ്റ്റേറ്റ് ലൈസൻസ്", "50 കോടിക്ക് മുകളിൽ സെൻട്രൽ. ഇംപോർട്ടർക്ക് എപ്പോഴും സെൻട്രൽ."),
 ("സാധുത ഇനി സ്ഥിരം", "പുതുക്കൽ വേണ്ട, പക്ഷേ നിയമങ്ങൾ പാലിക്കണം.")],
 "തെറ്റ് ചൂണ്ടിക്കാണിച്ച\nഫോളോവർക്ക് നന്ദി", CTA_FSSAI, theme="correction", corrects="fsx04",
 source="https://www.fssai.gov.in/upload/advisories/2026/03/69c6a23234827order_27032026.pdf", as_of="2026-03-13", expires="2027-03-31",
 cap_en="Correction: our earlier FSSAI reels used the old limits. Since 1 April 2026, FSSAI registration covers turnover up to Rs 1.5 crore (was Rs 12 lakh), a state licence covers Rs 1.5 crore to Rs 50 crore, and a central licence is above Rs 50 crore. Registrations and licences now have perpetual validity. Thank you to the follower who pointed this out.",
 cap_ml="തിരുത്ത്: ഞങ്ങളുടെ മുൻ FSSAI റീലുകളിൽ പഴയ ലിമിറ്റ് ആയിരുന്നു. 2026 ഏപ്രിൽ 1 മുതൽ 1.5 കോടി വരെ ടേൺഓവറിന് രജിസ്ട്രേഷൻ, 1.5 മുതൽ 50 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്, 50 കോടിക്ക് മുകളിൽ സെൻട്രൽ. സാധുത ഇനി സ്ഥിരം. ചൂണ്ടിക്കാണിച്ചതിന് നന്ദി.",
 cap_mg="Thiruthu: njangalude munpathe FSSAI reels-il pazhaya limit aayirunnu. 2026 April 1 muthal 1.5 crore vare registration, 1.5 muthal 50 crore vare state licence, 50 crore-nu mukalil central. Validity ini sthiram. Choondikkaanichathinu nanni.")
