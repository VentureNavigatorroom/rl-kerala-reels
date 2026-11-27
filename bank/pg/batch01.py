# pg batch 01 (27 Nov refill): first 3D duo reels for payment gateway KYC. Max 6 lines, painful moment or myth first, payoff by line 4-5.
# Facts only from topics.FACTS_PG. Never a gateway name, its fees, a recommendation or a promise of activation. Names, sectors, towns invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GATEWAY, CTA_PAYMENT = topics.CTA_GATEWAY, topics.CTA_PAYMENT


# faq: "why does a gateway want my documents?" -> KYC is an RBI / PMLA rule for every gateway
duo("pgd001", "proprietor_pg", "A", "tailor", "\"തയ്യൽ ഓർഡറിന്\nപൈസ വാങ്ങാൻ എന്തിനാ\nഎന്റെ ആധാറും PAN-ഉം?\"", [
 ("A","wide","മോഹനേട്ടാ, ഓൺലൈനിൽ ബ്ലൗസ് ഓർഡറിന് അഡ്വാൻസ് വാങ്ങാൻ ഗേറ്റ്‌വേ നോക്കി. അവർ ID, അഡ്രസ് പ്രൂഫ്, ബാങ്ക് വിവരം എല്ലാം ചോദിക്കുന്നു!"),
 ("V","V","ഉഷേ, അത് അവരുടെ വാശിയല്ല. ലൈവ് പേയ്മെന്റിന് മുമ്പ് ബിസിനസിന്റെ KYC ചെയ്യണം എന്നത് RBI, PMLA നിയമമാണ്."),
 ("A","A","അപ്പോ വേറെ ഗേറ്റ്‌വേയിൽ പോയാൽ ഇത് വേണ്ടേ?"),
 ("V","wide","ഇന്ത്യയിലെ എല്ലാ ഗേറ്റ്‌വേയും KYC ചെയ്യും. ഒറ്റയ്ക്കുള്ള ബിസിനസിന് ID, അഡ്രസ് പ്രൂഫ്, ഒരു ബിസിനസ് രേഖ, ബാങ്ക് വിവരം."),
 ("A","A","ഗേറ്റ്‌വേ മാറിയാലും നിയമം മാറില്ല.")],
 "എല്ലാ ഗേറ്റ്‌വേയിലും\nKYC ഉണ്ട്", CTA_PAYMENT, theme="faq",
 cap_ml="ഓൺലൈൻ ഓർഡറിന് പേയ്മെന്റ് ഗേറ്റ്‌വേ ID-യും ബാങ്ക് വിവരവും ചോദിക്കുന്നത് അവരുടെ വാശിയല്ല. ലൈവ് പേയ്മെന്റിന് മുമ്പ് ബിസിനസിന്റെ KYC ചെയ്യണം എന്നത് RBI, PMLA നിയമമാണ്; ഇന്ത്യയിലെ എല്ലാ ഗേറ്റ്‌വേയും ഇത് ചെയ്യും. ഒറ്റയ്ക്കുള്ള ബിസിനസിന് ID, അഡ്രസ് പ്രൂഫ്, ഒരു ബിസിനസ് രേഖ, ബാങ്ക് വിവരം. നിങ്ങളുടെ രേഖകൾ റെഡിയാണോ?",
 cap_en="A tailor taking blouse orders online is annoyed that a payment gateway wants her ID, address proof and bank details. It isn't the gateway being difficult: RBI and PMLA rules require KYC on the business before live payments, at every gateway in India. A proprietor needs identity and address proof, a business proof and bank details. Are your documents ready?",
 cap_mg="Online order-inu payment gateway ID-um bank details-um chodikkunnathu avarude vaashiyalla. Live payment-inu mumpu business-inte KYC cheyyanam ennathu RBI, PMLA niyamamaanu; Indiayile ella gateway-um ithu cheyyum. Proprietor-inu ID, address proof, oru business proof, bank details. Ningalude documents ready aano?")

# new: homestay owner spent a week on policy pages; some major gateways no longer ask for them at onboarding
duo("pgd002", "service_pro_pg", "B", "homestay", "ഒരാഴ്ച ഇരുന്ന്\nപോളിസി പേജ് എഴുതി.\nഗേറ്റ്‌വേ ചോദിച്ചില്ല!", [
 ("V","wide","ടീനേ, ഹോംസ്റ്റേ ബുക്കിംഗ് അഡ്വാൻസിന് ഗേറ്റ്‌വേ വേണം എന്ന് പറഞ്ഞ് ഞാൻ ഒരാഴ്ച റീഫണ്ട് പോളിസി എഴുതി ഇരുന്നു."),
 ("A","A","ജോമോനേ, ചില പ്രധാന ഗേറ്റ്‌വേകൾ ഇപ്പോൾ തുടക്കത്തിൽ പോളിസി പേജ് ചോദിക്കുന്നില്ല. പക്ഷേ വെബ്സൈറ്റ് അല്ലെങ്കിൽ ആപ്പ് വിവരം ചോദിക്കും."),
 ("V","V","അപ്പോ എന്റെ ഒരാഴ്ച വെറുതെയായോ?"),
 ("A","wide","ഇല്ല. ബുക്ക് ചെയ്യുന്ന അതിഥിക്ക് റീഫണ്ട് നിയമം കാണുമ്പോൾ വിശ്വാസം കൂടും. പക്ഷേ ആദ്യം ശരിയാക്കേണ്ടത് KYC രേഖകളാണ്."),
 ("V","V","ആദ്യം രേഖ, പിന്നെ പേജ്.")],
 "ആദ്യം KYC രേഖകൾ,\nപിന്നെ മിനുക്കുപണി", CTA_GATEWAY, theme="new",
 cap_ml="ചില പ്രധാന പേയ്മെന്റ് ഗേറ്റ്‌വേകൾ ഇപ്പോൾ തുടക്കത്തിൽ വെബ്സൈറ്റിലെ പോളിസി പേജുകൾ ചോദിക്കുന്നില്ല. പക്ഷേ വെബ്സൈറ്റ് അല്ലെങ്കിൽ ആപ്പ് വിവരം സാധാരണ ചോദിക്കും, KYC രേഖകൾ നിർബന്ധം. റീഫണ്ട് നിയമം കാണുമ്പോൾ ഉപഭോക്താവിന് വിശ്വാസം കൂടും, അതുകൊണ്ട് പേജ് വെറുതെയല്ല. നിങ്ങൾ ആദ്യം എന്താണ് ശരിയാക്കിയത്?",
 cap_en="A homestay owner spent a week writing refund-policy pages before applying for a payment gateway. Some major gateways no longer ask for policy pages at onboarding, though website or app details are commonly asked and KYC documents are a must. The pages still help guests trust you, so the week wasn't wasted. What did you sort out first?",
 cap_mg="Chila pradhaana payment gateway-kal ippol thudakkathil website-ile policy pages chodikkunnilla. Pakshe website allenkil app details saadhaarana chodikkum, KYC documents nirbandham. Refund policy kaanumbol customer-inu vishwaasam koodum, athukondu page veruthe alla. Ningal aadyam enthaanu sheriyaakkiyathu?")

# crm (#5, two businesses under one name): catering proprietorship and a new decor company share one gateway
duo("pgd003", "new_company_pg", "C", "weddinghall", "കാറ്ററിംഗിന്റെ ഗേറ്റ്‌വേയിൽ\nപുതിയ കമ്പനിയുടെ\nപൈസ വാങ്ങിയാലോ?", [
 ("V","wide","കാവ്യേ, ഡെക്കറേഷന് പുതിയ പ്രൈവറ്റ് ലിമിറ്റഡ് തുടങ്ങി. പൈസ നമ്മുടെ പഴയ കാറ്ററിംഗ് ഗേറ്റ്‌വേയിൽ തന്നെ വാങ്ങിയാൽ പോരേ?"),
 ("A","A","ശരത്തേട്ടാ, കാറ്ററിംഗ് നിങ്ങളുടെ പേരിലുള്ള പ്രൊപ്രൈറ്റർ ബിസിനസ്സാ. കമ്പനി വേറൊരു ആളാണ്, അതിന് വേറെ PAN."),
 ("V","V","രണ്ടിനും ഉടമ ഞാൻ തന്നെയല്ലേ?"),
 ("A","wide","ഗേറ്റ്‌വേ KYC ബിസിനസിനാണ്. കമ്പനിക്ക് സ്വന്തം PAN, CIN, കമ്പനി പേരിൽ ബാങ്ക് അക്കൗണ്ട്. പേര് ഒത്തില്ലെങ്കിൽ ആക്ടിവേഷൻ വൈകും."),
 ("V","V","രണ്ട് ബിസിനസ്, രണ്ട് KYC.")],
 "ഓരോ ബിസിനസിനും\nസ്വന്തം KYC", CTA_GATEWAY, theme="crm",
 cap_ml="കാറ്ററിംഗ് പ്രൊപ്രൈറ്റർ ബിസിനസ്സായി നടത്തുന്നു, ഡെക്കറേഷന് പുതിയ പ്രൈവറ്റ് ലിമിറ്റഡ് തുടങ്ങി. പുതിയ കമ്പനിയുടെ പൈസ പഴയ ഗേറ്റ്‌വേയിൽ വാങ്ങരുത്. ഗേറ്റ്‌വേ KYC ബിസിനസിനാണ്: കമ്പനിക്ക് സ്വന്തം PAN, CIN, കമ്പനി പേരിൽ ബാങ്ക് അക്കൗണ്ട്. നിങ്ങൾക്ക് ഒന്നിൽ കൂടുതൽ ബിസിനസ് ഉണ്ടോ?",
 cap_en="A caterer runs his catering as a proprietorship and just started a private limited company for wedding decor. He wants the company's money collected through the old catering gateway. Gateway KYC is done on the business: the company needs its own PAN, CIN and a bank account in the company's name, and names must match or activation is delayed. Do you run more than one business?",
 cap_mg="Catering proprietor business aayi nadathunnu, decoration-inu puthiya Pvt Ltd thudangi. Puthiya company-yude paisa pazhaya gateway-il vaangaruthu. Gateway KYC business-inaanu: company-kku swantham PAN, CIN, company peril bank account. Ningalkku onnil kooduthal business undo?")

# faq: director lives in the Gulf; who signs the gateway application for the Kerala company?
duo("pgd004", "app_founder_pg", "B", "gulfroom", "ഡയറക്ടർ ദുബായിൽ.\nകമ്പനി കൊച്ചിയിൽ.\nഗേറ്റ്‌വേ ആര് ഒപ്പിടും?", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ ആപ്പ് കമ്പനിക്ക് ഗേറ്റ്‌വേ വേണം. ഞാൻ ഇവിടെ ദുബായിൽ, മാനേജർ കൊച്ചിയിൽ. അവന് ഒപ്പിടാമോ?"),
 ("V","V","നസീറേ, കമ്പനി ബോർഡ് റെസല്യൂഷൻ വഴിയോ ഓതറൈസേഷൻ വഴിയോ ഒരാളെ ചുമതലപ്പെടുത്തണം. ഒപ്പിടുന്ന ആളിന്റെ KYC-യും വേണം."),
 ("A","A","അപ്പോ അവന്റെ ID-യും ചോദിക്കും?"),
 ("V","wide","ചോദിക്കും. കൂടെ കമ്പനി PAN, CIN, MOA, AOA. 10%-ൽ കൂടുതൽ ഷെയർ ഉള്ള നിന്റെ വിവരവും ഡിക്ലയർ ചെയ്യണം."),
 ("A","A","ദൂരെ ഇരുന്നാലും പേപ്പർ അടുത്ത് വേണം.")],
 "ഒപ്പിടുന്ന ആളെ\nകടലാസിൽ ഉറപ്പിക്കൂ", CTA_GATEWAY, theme="faq",
 cap_ml="ഡയറക്ടർ ഗൾഫിൽ, കമ്പനി കേരളത്തിൽ, ഗേറ്റ്‌വേ അപേക്ഷ ആര് ഒപ്പിടും? കമ്പനി ബോർഡ് റെസല്യൂഷൻ അല്ലെങ്കിൽ ഓതറൈസേഷൻ വഴി ഒരാളെ ചുമതലപ്പെടുത്തണം, ആ ആളിന്റെ KYC-യും വേണം. കൂടെ കമ്പനി PAN, CIN, MOA, AOA, 10%-ൽ കൂടുതൽ ഷെയർ ഉള്ളവരുടെ ഡിക്ലറേഷൻ. നിങ്ങളുടെ കമ്പനിയിൽ ആരാണ് ഒപ്പിടുന്നത്?",
 cap_en="The director lives in Dubai, the app company is in Kochi, and the manager wants to sign the payment gateway application. The company has to authorise the signatory by a board resolution or an authorisation, and the signatory's own KYC is needed too, along with the company PAN, CIN, MOA, AOA and a declaration of everyone holding above 10%. Who signs for your company?",
 cap_mg="Director Gulf-il, company Keralathil, gateway application aaru oppidum? Company board resolution allenkil authorisation vazhi oraale chumathalappeduthanam, aa aalinte KYC-um venam. Koode company PAN, CIN, MOA, AOA, 10%-il kooduthal share ullavarude declaration. Ningalude company-yil aaraanu oppidunnathu?")

# new: courier startup founder filled in his personal PAN on the company's gateway form
duo("pgd005", "new_company_pg", "A", "courier", "കമ്പനിയുടെ അപേക്ഷയിൽ\nകൊടുത്തത്\nസ്വന്തം PAN!", [
 ("A","wide","അരവിന്ദേ, കൊറിയർ കമ്പനിയുടെ ഗേറ്റ്‌വേ അപേക്ഷ എന്തായി? ഇതുവരെ ആക്ടിവേറ്റ് ആയില്ലല്ലോ."),
 ("V","V","ജയേച്ചീ, ഞാൻ എന്റെ സ്വന്തം PAN കൊടുത്തു. കമ്പനിക്ക് വേറെ PAN ഉണ്ടെന്ന് ഓർത്തില്ല."),
 ("A","A","കമ്പനിക്ക് സ്വന്തം PAN ഉണ്ട്. ഗേറ്റ്‌വേ ചോദിക്കുന്നത് അതാണ്. നിന്റെ PAN ഒപ്പിടുന്ന ആളിന്റെ KYC-ക്കാണ്."),
 ("V","V","അപ്പോ ബാങ്ക് അക്കൗണ്ടും കമ്പനി പേരിൽ തന്നെ വേണം, അല്ലേ?"),
 ("A","wide","അതെ. കമ്പനി PAN, കമ്പനി അക്കൗണ്ട്, കമ്പനി പേര്. മൂന്നും ഒന്നാകണം.")],
 "കമ്പനി PAN,\nകമ്പനി അക്കൗണ്ട്", CTA_PAYMENT, theme="new",
 cap_ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയുടെ പേയ്മെന്റ് ഗേറ്റ്‌വേ അപേക്ഷയിൽ ഡയറക്ടറുടെ സ്വന്തം PAN കൊടുക്കരുത്. ഗേറ്റ്‌വേ ചോദിക്കുന്നത് കമ്പനിയുടെ PAN ആണ്; ഡയറക്ടറുടെ PAN ഒപ്പിടുന്ന ആളിന്റെ KYC-ക്ക്. സെറ്റിൽമെന്റ് ബാങ്ക് അക്കൗണ്ടും കമ്പനി പേരിൽ വേണം, പേര് എല്ലായിടത്തും ഒരുപോലെ. നിങ്ങൾ ഏത് PAN ആണ് കൊടുത്തത്?",
 cap_en="A courier startup's gateway application stalls because the founder entered his personal PAN instead of the company's. A private limited company applies with the company PAN; the director's PAN is for the signatory's KYC. The settlement bank account must also be in the company's name, with the name matching everywhere. Which PAN did you enter?",
 cap_mg="Pvt Ltd company-yude payment gateway application-il director-inte swantham PAN kodukkaruthu. Gateway chodikkunnathu company-yude PAN aanu; director-inte PAN oppidunna aalinte KYC-kku. Settlement bank account-um company peril venam, peru ellaayidathum orupole. Ningal ethu PAN aanu koduthathu?")
