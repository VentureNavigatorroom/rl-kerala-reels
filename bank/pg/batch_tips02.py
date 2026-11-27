# pg tips 02 (27 Nov evening): tip reel as a duo3d scene (not a list, per the 26 Nov review). theme="tip". Facts only from topics.FACTS_PG.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_GATEWAY, CTA_PAYMENT = topics.CTA_GATEWAY, topics.CTA_PAYMENT

duo("pgt003", "online_seller_pg", "B", "pharmacy", "ഗേറ്റ്‌വേ KYC:\nഒരേ പേര് വേണ്ട\n3 സ്ഥലം", [
 ("A","wide","പ്രവീണേ, ഗേറ്റ്‌വേ അപേക്ഷിക്കും മുമ്പ് ബിസിനസ് പേര് മൂന്ന് സ്ഥലത്ത് ഒന്ന് നോക്കാം."),
 ("A","A","ഒന്ന്: PAN. രണ്ട്: പൈസ വരേണ്ട ബാങ്ക് അക്കൗണ്ട്."),
 ("V","V","മൂന്ന്: GST, ഉദ്യം പോലുള്ള ബിസിനസ് രജിസ്ട്രേഷൻ. ഒരു അക്ഷരം മാറിയാലും പ്രശ്നം."),
 ("A","A","മൂന്നിലും ഒരേ പേര് ആണെങ്കിൽ ആക്ടിവേഷൻ വൈകാനുള്ള ഒരു പ്രധാന കാരണം ഒഴിവാകും."),
 ("V","wide","PAN, ബാങ്ക്, രജിസ്ട്രേഷൻ. ഒരേ പേര്.")],
 "PAN, ബാങ്ക്,\nരജിസ്ട്രേഷൻ: ഒരേ പേര്", CTA_GATEWAY, theme="tip",
 cap_ml="ഗേറ്റ്‌വേ അപേക്ഷയ്ക്ക് മുമ്പ് ബിസിനസ് പേര് 3 സ്ഥലത്ത് ഒത്തുനോക്കൂ: PAN, പൈസ വരേണ്ട ബാങ്ക് അക്കൗണ്ട്, ബിസിനസ് രജിസ്ട്രേഷൻ. ഒരു അക്ഷരം മാറിയാലും ആക്ടിവേഷൻ വൈകാം. നിങ്ങളുടെ മൂന്നിലും ഒരേ പേരാണോ?",
 cap_en="Before a payment gateway application, check your business name in 3 places: PAN, the settlement bank account and the business registration. Even one letter off can delay activation. Is yours the same in all three?",
 cap_mg="Gateway apekshaykku mumbu business peru 3 sthalathu othunokku: PAN, paisa varenda bank account, business registration. Oru aksharam maariyaalum activation vaikaam. Ningalude moonnilum ore peraano?")
