# pg tips 01 (27 Nov): tip reels as duo3d scenes (not lists), theme="tip". Facts only from topics.FACTS_PG. No gateway names, fees or promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GATEWAY, CTA_PAYMENT = topics.CTA_GATEWAY, topics.CTA_PAYMENT

# tip: 2-minute spelling check of the three documents before applying
duo("pgt001", "proprietor_pg", "B", "akshaya", "ഗേറ്റ്‌വേ അപേക്ഷയ്ക്ക്\nമുമ്പ് 2 മിനിറ്റ്:\nമൂന്ന് രേഖ ഒരുമിച്ച്", [
 ("V","wide","സുധേ, ഗേറ്റ്‌വേ അപേക്ഷ കൊടുക്കും മുമ്പ് ഒരു ചെക്ക് പറഞ്ഞുതരാമോ?"),
 ("A","A","രമേശേട്ടാ, PAN, ബാങ്ക് പാസ്ബുക്ക്, ബിസിനസ് രജിസ്ട്രേഷൻ. മൂന്നും അടുത്തടുത്ത് വെച്ച് പേര് അക്ഷരം അക്ഷരമായി നോക്കൂ."),
 ("V","V","ഒരു അക്ഷരം മാറിയാലും പ്രശ്നമാണോ?"),
 ("A","wide","പേര് ഒത്തില്ലെങ്കിൽ ആക്ടിവേഷൻ വൈകുകയോ റിജക്ട് ആകുകയോ ചെയ്യാം. ആദ്യം ഇത് ശരിയാക്കിയിട്ട് അപേക്ഷിക്കൂ.")],
 "മൂന്ന് രേഖ,\nഒരേ പേര്", CTA_GATEWAY, theme="tip",
 cap_ml="പേയ്മെന്റ് ഗേറ്റ്‌വേ അപേക്ഷയ്ക്ക് മുമ്പ് 2 മിനിറ്റ് ചെക്ക്: PAN, ബാങ്ക് പാസ്ബുക്ക്, ബിസിനസ് രജിസ്ട്രേഷൻ മൂന്നും അടുത്തടുത്ത് വെച്ച് പേര് അക്ഷരം അക്ഷരമായി നോക്കുക. പേര് ഒത്തില്ലെങ്കിൽ ആക്ടിവേഷൻ വൈകുകയോ റിജക്ട് ആകുകയോ ചെയ്യാം. നിങ്ങളുടെ മൂന്നിലും പേര് ഒരുപോലെയാണോ?",
 cap_en="A 2-minute check before you apply for a payment gateway: put your PAN, bank passbook and business registration side by side and compare the name letter by letter. If the names don't match, activation can be delayed or rejected. Is the name the same on all three of yours?",
 cap_mg="Payment gateway application-inu mumpu 2 minute check: PAN, bank passbook, business registration moonnum aduthaduthu vechu peru aksharam aksharamaayi nokkuka. Peru othillenkil activation vaikukayo reject aakukayo cheyyaam. Ningalude moonnilum peru orupole aano?")

# tip: one folder for a private limited company before the gateway asks
duo("pgt002", "new_company_pg", "B", "photocopy", "കമ്പനിക്ക് ഗേറ്റ്‌വേ?\nഒരു ഫോൾഡറിൽ\nഇത് റെഡിയാക്കൂ", [
 ("V","wide","അശ്വതീ, കമ്പനിയുടെ ഗേറ്റ്‌വേ അപേക്ഷയ്ക്ക് എല്ലാ രേഖയുടെയും കോപ്പി വേണം. എന്തൊക്കെയാ?"),
 ("A","A","ഉണ്ണിയേട്ടാ, കമ്പനി PAN, ഇൻകോർപ്പറേഷൻ രേഖ, MOA, AOA. പിന്നെ ബോർഡ് റെസല്യൂഷൻ അല്ലെങ്കിൽ ഓതറൈസേഷൻ."),
 ("V","V","അത്രയും മതിയോ?"),
 ("A","wide","ഒപ്പിടുന്ന ആളിന്റെ KYC, 10%-ൽ കൂടുതൽ ഷെയർ ഉള്ളവരുടെ ഡിക്ലറേഷൻ, കമ്പനി പേരിൽ ബാങ്ക് അക്കൗണ്ട്. ഇതും ചേർക്കൂ.")],
 "ഒരു ഫോൾഡർ,\nഒറ്റ അപേക്ഷ", CTA_GATEWAY, theme="tip",
 cap_ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് ഗേറ്റ്‌വേ അപേക്ഷിക്കും മുമ്പ് ഒരു ഫോൾഡർ: കമ്പനി PAN, ഇൻകോർപ്പറേഷൻ രേഖ (CIN), MOA, AOA, ബോർഡ് റെസല്യൂഷൻ അല്ലെങ്കിൽ ഓതറൈസേഷൻ, ഒപ്പിടുന്ന ആളിന്റെ KYC, 10%-ൽ കൂടുതൽ ഷെയർ ഉള്ളവരുടെ ഡിക്ലറേഷൻ, കമ്പനി പേരിൽ ബാങ്ക് അക്കൗണ്ട്. ഇതിൽ ഏതാണ് നിങ്ങളുടെ ഫോൾഡറിൽ ഇല്ലാത്തത്?",
 cap_en="One folder before a private limited company applies for a payment gateway: company PAN, incorporation record (CIN), MOA and AOA, a board resolution or authorisation, the signatory's KYC, a declaration of everyone holding above 10%, and a bank account in the company's name. Which one is missing from your folder?",
 cap_mg="Pvt Ltd company-kku gateway apply cheyyum mumpu oru folder: company PAN, incorporation record (CIN), MOA, AOA, board resolution allenkil authorisation, oppidunna aalinte KYC, 10%-il kooduthal share ullavarude declaration, company peril bank account. Ithil ethaanu ningalude folder-il illaathathu?")
