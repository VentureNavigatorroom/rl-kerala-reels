# Kerala Startup Mission (KSUM) batch 05 (20 Nov, month backlog). Max 6 lines, myth or painful moment first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented). Facts only from topics.FACTS_SK.
# Never state grant amounts or promise selection. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

duo("md039", "returnee", "A", "gulfoffice", "മാർച്ചിൽ രാജി.\nഏപ്രിലിൽ ഗ്രാന്റ്.\nപ്ലാൻ ശരിയാണോ?", [
 ("V","wide","ഷഹാനാ, മാർച്ചിൽ രാജി കൊടുക്കും. ഏപ്രിലിൽ നാട്ടിലെത്തി ക്ലിനിക് ബുക്കിംഗ് ആപ്പിന് KSUM ഗ്രാന്റ് വാങ്ങും."),
 ("A","A","ആസിഫ്, പന്ത്രണ്ട് വർഷം ഹോസ്പിറ്റൽ സോഫ്റ്റ്‌വെയർ ചെയ്തയാളാ നീ. പക്ഷേ നാട്ടിൽ കമ്പനി ഉണ്ടോ?"),
 ("V","V","ഇല്ല. എത്തിയിട്ട് എല്ലാം ഒരുമിച്ച് ചെയ്യാം എന്ന് കരുതി."),
 ("A","wide","KSUM ഗ്രാന്റും ഇൻക്യുബേഷനും യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പിനാ. അതിന് ആദ്യം കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത കമ്പനി വേണം."),
 ("V","V","അപ്പോ ഇവിടെ ഇരുന്ന് തന്നെ പേപ്പർ തുടങ്ങണം."),
 ("A","wide","ടിക്കറ്റിന് മുമ്പ് കമ്പനി, ലാൻഡിംഗിന് മുമ്പ് ID.")],
 "ടിക്കറ്റിന് മുമ്പ് കമ്പനി,\nലാൻഡിംഗിന് മുമ്പ് ID", CTA_KSUM, theme="crm",
 cap_ml="ഗൾഫിൽ 12 വർഷം ഹോസ്പിറ്റൽ സോഫ്റ്റ്‌വെയർ ചെയ്ത ആൾ, നാട്ടിലെത്തിയ ഉടൻ KSUM ഗ്രാന്റ് പ്രതീക്ഷിക്കുന്നു, പക്ഷേ കമ്പനി ഇല്ല. KSUM പദ്ധതികൾ കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത, യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. നിങ്ങൾ നാട്ടിലേക്ക് എപ്പോൾ?",
 cap_en="After 12 years building hospital software in the Gulf, he plans to resign in March and get a KSUM grant in April, with no company yet. KSUM grants, incubation and programmes are for startups registered in Kerala that hold the KSUM Unique ID, so start the papers before you fly home. Coming back this year: yes or no?",
 cap_mg="Gulf-il 12 varsham hospital software cheytha aal, naattil ethiya udan KSUM grant pratheekshikkunnu, pakshe company illa. KSUM paddhathikal Keralathil register cheytha, Unique ID ulla startup-ukalkkaanu. Ningal naattilekku eppol?")

duo("md040", "idea_stage", "B", "rubber", "ആനയ്ക്ക് GPS.\nഇതും സ്റ്റാർട്ടപ്പോ?", [
 ("A","wide","തോമസേ, അപ്പൻ ആനപ്പാപ്പാനാ. ഉത്സവത്തിന് ആന എവിടെ എന്നറിയാൻ ഞാൻ ഒരു GPS കാൽത്തള ഉണ്ടാക്കി."),
 ("V","V","ജോയീ, പ്രോട്ടോടൈപ്പ് റെഡി. പിന്നെ എന്തിനാ വൈകുന്നത്? KSUM-ൽ പോ."),
 ("A","A","പോയി. അവർ ആദ്യം ചോദിച്ചത് യുണീക്ക് ID. എനിക്ക് കമ്പനി പോലുമില്ല."),
 ("V","wide","ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം. പക്ഷേ പണം വരും മുമ്പ് കമ്പനിയും യുണീക്ക് ID-യും വേണം."),
 ("A","A","അപ്പോ ആനയെ പോലെ പേപ്പറും മുന്നിൽ നടക്കണം."),
 ("V","wide","ആനയ്ക്ക് ചങ്ങല, ഐഡിയയ്ക്ക് ID.")],
 "ആനയ്ക്ക് ചങ്ങല,\nഐഡിയയ്ക്ക് ID", CTA_GRANT, theme="crm",
 cap_ml="ആനപ്പാപ്പാന്റെ മകൻ ഉത്സവ ആനകൾക്ക് GPS കാൽത്തള ഉണ്ടാക്കി, പ്രോട്ടോടൈപ്പ് റെഡി, പക്ഷേ KSUM യുണീക്ക് ID ഇല്ല. ഐഡിയ ഗ്രാന്റിന് കമ്പനിക്ക് മുമ്പ് അപേക്ഷിക്കാം, പക്ഷേ പണം കിട്ടാൻ കമ്പനിയും ID-യും വേണം. നിങ്ങളുടെ ഐഡിയ ഏത് മേഖലയിൽ?",
 cap_en="A mahout's son built a GPS anklet so temple elephants can be tracked during festivals. The prototype works, but he has no company and no KSUM Unique ID. You may apply for the KSUM idea grant before incorporating, but the company and the Unique ID are needed before money is released. What does your idea track?",
 cap_mg="Aanappaappaante makan ulsava aanakalkku GPS kaalthala undaakki, prototype ready, pakshe KSUM Unique ID illa. Idea grant-nu company-kku mumpu apekshikkaam, pakshe panam kittaan company-um ID-yum venam. Ningalude idea ethu mekhalayil?")

duo("md041", "women_founder", "C", "handloom", "\"100 ഓർഡർ\nകഴിഞ്ഞിട്ട്\nKSUM-ൽ പോകാം\"", [
 ("A","wide","കുമാറേട്ടാ, കൈത്തറി ബേബി ക്യാരിയർ ഓൺലൈനിൽ നല്ലോണം പോകുന്നു. നൂറ് ഓർഡർ ആയിട്ട് മെന്ററെയും ഇൻക്യുബേഷനും നോക്കാം."),
 ("V","V","ലീലേ, ആ നൂറിന് എത്ര മാസം വേണ്ടിവരും?"),
 ("A","A","ആറോ എട്ടോ. അതുവരെ KSUM നമ്മളെ നോക്കില്ലല്ലോ."),
 ("V","wide","KSUM ഓർഡർ എണ്ണുന്നില്ല. ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും യുണീക്ക് ID ഉള്ള, കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പിനാ."),
 ("A","A","അപ്പോ ആദ്യം കമ്പനി, പിന്നെ ID, അതിനിടയിൽ ഓർഡറും."),
 ("V","wide","തറിയിൽ ഇഴ, KSUM-ൽ ID.")],
 "ഓർഡർ എണ്ണം അല്ല,\nID ആണ് ആദ്യം", CTA_KSUM, theme="crm",
 cap_ml="കൈത്തറി ബേബി ക്യാരിയർ വിൽക്കുന്ന വനിതാ ഫൗണ്ടർ, 100 ഓർഡർ കഴിഞ്ഞിട്ട് മെന്ററിംഗിനും ഇൻക്യുബേഷനും പോകാം എന്ന് കരുതി. KSUM നോക്കുന്നത് ഓർഡർ എണ്ണമല്ല: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പും യുണീക്ക് ID-യും. നിങ്ങൾക്ക് ആദ്യം വേണ്ടത് മെന്ററോ സ്ഥലമോ?",
 cap_en="A woman founder selling handloom baby carriers online planned to look for a mentor and incubation only after 100 orders. KSUM doesn't count orders: its incubation and programmes are for startups registered in Kerala that hold the KSUM Unique ID. What do you need first: a mentor or space?",
 cap_mg="Kaithari baby carrier vilkkunna vanitha founder, 100 order kazhinjittu mentoring-inum incubation-inum pokaam ennu karuthi. KSUM nokkunnathu order ennamalla: Keralathil register cheytha startup-um Unique ID-yum. Ningalkku aadyam vendathu mentor-o sthalamo?")

chat("mc003", "campus", "B", "\"കോളേജിന്റെ\nഇൻക്യുബേറ്റർ ID\nനമുക്കും മതിയോ?\"", ("ഗായത്രി", "അനന്തു"), [
 (0,"അനന്തൂ, നമ്മുടെ ഡ്രിപ്പ് ഇറിഗേഷൻ സെൻസർ കോളേജ് ഇൻകുബേറ്ററിൽ ആണല്ലോ. അപ്പോ KSUM ID-യും അവരുടേത് മതിയല്ലോ?"),
 (1,"ഗായത്രീ, ഞാനും അങ്ങനെയാ കരുതിയത്. പക്ഷേ സീനിയർ പറഞ്ഞു അത് പറ്റില്ലെന്ന്."),
 (0,"പിന്നെ? കോളേജിന്റെ പേര് വെച്ചാൽ എളുപ്പമല്ലേ?"),
 (1,"യുണീക്ക് ID സ്റ്റാർട്ടപ്പിന്റെ സ്വന്തം ഐഡന്റിറ്റിയാ. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത നമ്മുടെ കമ്പനിയോ LLP-യോ വേണം."),
 (0,"അപ്പോ ഇൻകുബേറ്റർ വീട്, പക്ഷേ വിലാസം നമ്മുടേത്."),
 (1,"ഹോസ്റ്റൽ കോളേജിന്റേത്, കമ്പനി നമ്മുടേത്.")],
 "ഹോസ്റ്റൽ കോളേജിന്റേത്,\nകമ്പനി നമ്മുടേത്", CTA_KSUM, theme="crm",
 cap_ml="കോളേജ് ഇൻകുബേറ്ററിലെ ടീം കരുതി, കോളേജിന്റെ രജിസ്ട്രേഷൻ മതി KSUM-ന് എന്ന്. യുണീക്ക് ID സ്റ്റാർട്ടപ്പിന്റെ സ്വന്തം ഐഡന്റിറ്റിയാണ്: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്വന്തം കമ്പനിയോ LLP-യോ വേണം. നിങ്ങളുടെ കോളേജിൽ ഇൻകുബേറ്റർ ഉണ്ടോ?",
 cap_en="A campus team in their college incubator thought the college's registration would cover them for KSUM. The KSUM Unique ID is the startup's own identity: the team needs its own private limited company or LLP registered in Kerala. Does your college have an incubator?",
 cap_mg="College incubator-ile team karuthi, college-inte registration mathi KSUM-nu ennu. Unique ID startup-inte swantham identity aanu: Keralathil register cheytha swantham company-o LLP-yo venam. Ningalude college-il incubator undo?")

duo("md042", "kerala_registered", "A", "shop", "പാർട്ണർഷിപ്പ് ഡീഡ്\nഉണ്ട്. ഗ്രാന്റിന്\nപോരേ?", [
 ("A","wide","സുരേഷേ, വാഴനാര് കൊണ്ടുള്ള ബാഗിന് ഗൾഫിൽ നിന്ന് വരെ ഓർഡർ. KSUM സീഡ് ഫണ്ടിന് നമ്മൾ അപേക്ഷിക്കുന്നു."),
 ("V","V","ബിനൂ, നമ്മുടേത് രജിസ്റ്റർ ചെയ്ത പാർട്ണർഷിപ്പ് ഫേം ആണ്. അത് പോരേ?"),
 ("A","A","ഡീഡ് ഉണ്ട്, സ്റ്റാമ്പ് ഉണ്ട്, രണ്ട് സഹോദരന്മാരുടെ ഒപ്പും ഉണ്ട്."),
 ("V","wide","മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും ചോദിക്കുന്നത് MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ ആണ്. ഒപ്പം DPIIT-യും."),
 ("A","A","അപ്പോ ഫേം മാറ്റിയിട്ട് വേണം ഫണ്ട് നോക്കാൻ."),
 ("V","wide","ഡീഡിൽ സൗഹൃദം, ഗ്രാന്റിന് കമ്പനി.")],
 "ഡീഡിൽ സൗഹൃദം,\nഗ്രാന്റിന് കമ്പനി", CTA_GRANT, theme="faq",
 cap_ml="വാഴനാര് ബാഗ് ഉണ്ടാക്കുന്ന സഹോദരന്മാരുടെ പാർട്ണർഷിപ്പ് ഫേം KSUM സീഡ് ഫണ്ടിന് ഒരുങ്ങി. മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ, ഒപ്പം DPIIT-യും ചോദിക്കുന്നു. നിങ്ങളുടെ ബിസിനസ്: ഫേമോ കമ്പനിയോ?",
 cap_en="Two brothers make banana-fibre bags as a registered partnership firm and wanted the KSUM seed fund. Most KSUM grants and the seed fund ask for a private limited company or LLP that is Active at MCA, plus DPIIT recognition. Your business: firm or company?",
 cap_mg="Vaazhanaaru bag undaakkunna sahodaranmaarude partnership firm KSUM seed fund-inu orungi. Mikka KSUM grant-ukalum seed fund-um MCA-yil active aaya private limited-o LLP-yo, oppam DPIIT-yum chodikkunnu. Ningalude business: firm-o company-o?")

duo("md043", "idea_stage", "B", "akshaya", "\"ഗ്രാന്റ് എന്റെ\nസേവിംഗ്സ്\nഅക്കൗണ്ടിലേക്കോ?\"", [
 ("V","wide","സുധേ, KSUM ഗ്രാന്റ് ഫോമിൽ എന്റെ സേവിംഗ്സ് അക്കൗണ്ട് കൊടുത്താൽ മതിയോ? കമ്പനി പിന്നെ നോക്കാം."),
 ("A","A","രമേശേ, ഇത് നിന്റെ തേങ്ങ ഉണക്കുന്ന സോളാർ ഡ്രയറിന്റെ ഗ്രാന്റ് അല്ലേ? അത് നിനക്കാണോ, സ്റ്റാർട്ടപ്പിനാണോ?"),
 ("V","V","സ്റ്റാർട്ടപ്പ് ഞാൻ തന്നെയല്ലേ?"),
 ("A","wide","ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം. പക്ഷേ കമ്പനിയും KSUM യുണീക്ക് ID-യും ഇല്ലാതെ പണം റിലീസ് ആകില്ല."),
 ("V","V","അപ്പോ ഞാനല്ല, കമ്പനിയാ ഗ്രാന്റിന്റെ ആൾ."),
 ("A","wide","പോക്കറ്റ് നിന്റേത്, ഗ്രാന്റ് കമ്പനിയുടേത്.")],
 "പോക്കറ്റ് നിന്റേത്,\nഗ്രാന്റ് കമ്പനിയുടേത്", CTA_GRANT, theme="faq",
 cap_ml="തേങ്ങ ഉണക്കുന്ന സോളാർ ഡ്രയർ ഉണ്ടാക്കിയ ആൾ ചോദിച്ചു: KSUM ഗ്രാന്റ് എന്റെ സേവിംഗ്സ് അക്കൗണ്ടിൽ വരുമോ? ഐഡിയ ഗ്രാന്റിന് കമ്പനിക്ക് മുമ്പ് അപേക്ഷിക്കാം, പക്ഷേ കമ്പനിയും യുണീക്ക് ID-യും ഇല്ലാതെ പണം റിലീസ് ആകില്ല. കമ്പനി തുടങ്ങിയോ: അതെ അല്ലെങ്കിൽ ഇല്ല?",
 cap_en="A founder who built a solar coconut dryer asked if the KSUM grant could go to his personal savings account. You may apply for the idea grant before incorporating, but no money is released until the company and the KSUM Unique ID exist. Company registered yet: yes or no?",
 cap_mg="Thenga unakkunna solar dryer undaakkiya aal chodichu: KSUM grant ente savings account-il varumo? Idea grant-nu company-kku mumpu apekshikkaam, pakshe company-um Unique ID-yum illaathe panam release aakilla. Company thudangiyo: athe allenkil illa?")

duo("md044", "kerala_registered", "C", "homestay", "ട്രസ്റ്റ് ആയി\nതുടങ്ങി. KSUM\nനോക്കുമോ?", [
 ("A","wide","ജോമോനേ, വയസ്സായവർക്ക് മരുന്ന് സമയം ഓർമിപ്പിക്കുന്ന സ്പീക്കർ, ഞങ്ങൾ ഒരു ട്രസ്റ്റ് ആയിട്ടാ തുടങ്ങിയത്."),
 ("V","V","ടീനാ, നല്ല കാര്യം. ഇനി KSUM ഗ്രാന്റിന് അപേക്ഷിക്കുന്നുണ്ടോ?"),
 ("A","A","ലാഭം നോക്കാത്ത ട്രസ്റ്റ് അല്ലേ. അവർക്ക് ഇഷ്ടമാകും എന്ന് കരുതി."),
 ("V","wide","മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും ചോദിക്കുന്നത് MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP ആണ്."),
 ("A","A","അപ്പോ നല്ല മനസ്സ് മാത്രം പോരാ, ശരിയായ ഘടനയും വേണം."),
 ("V","wide","മനസ്സ് ട്രസ്റ്റിന്, ഫോം കമ്പനിക്ക്.")],
 "മനസ്സ് ട്രസ്റ്റിന്,\nഫോം കമ്പനിക്ക്", CTA_GRANT, theme="faq",
 cap_ml="വയസ്സായവർക്ക് മരുന്ന് ഓർമിപ്പിക്കുന്ന സ്പീക്കർ ഉണ്ടാക്കിയ ടീം ട്രസ്റ്റ് ആയിട്ടാണ് തുടങ്ങിയത്. മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ ചോദിക്കുന്നു. ഓരോ കോളിന്റെയും നിബന്ധന നോക്കൂ. നിങ്ങളുടെ സംരംഭം: ട്രസ്റ്റോ കമ്പനിയോ?",
 cap_en="A team that built a speaker reminding elderly people to take their medicines started as a trust. Most KSUM grants and the seed fund ask for a private limited company or LLP that is Active at MCA, so check each call's conditions before applying. Your venture: trust or company?",
 cap_mg="Vayassaayavarkku marunnu ormippikkunna speaker undaakkiya team trust aayittaanu thudangiyathu. Mikka KSUM grant-ukalum seed fund-um MCA-yil active aaya private limited-o LLP-yo chodikkunnu. Oro call-inteyum nibandhana nokkoo. Ningalude samrambham: trust-o company-o?")

duo("md045", "kerala_registered", "B", "teashop", "കഴിഞ്ഞ കോളിൽ\nറിജക്റ്റ്. ഇനി\nഒരിക്കലും ഇല്ലേ?", [
 ("V","wide","അനൂ, KSUM കോളിൽ എന്റെ മത്സ്യകൃഷി സെൻസർ റിജക്റ്റ് ആയി. ഇനി എന്റെ പേര് കണ്ടാൽ തന്നെ തള്ളും."),
 ("A","A","വിഷ്ണൂ, ഒരു കോൾ എന്നാൽ ഒരു കോൾ. എന്താ റിജക്ഷന്റെ കാരണം പറഞ്ഞത്?"),
 ("V","V","DPIIT റെക്കഗ്നിഷൻ ഇല്ല എന്ന്. അത് പിന്നെ എടുക്കാം എന്ന് കരുതി."),
 ("A","wide","കോളുകളും നിബന്ധനകളും മാറും, സെലക്ഷൻ ആർക്കും ഉറപ്പില്ല. പക്ഷേ മിക്ക ഗ്രാന്റുകളും ആക്ടീവ് കമ്പനിയും DPIIT-യും ചോദിക്കും."),
 ("V","V","അപ്പോ അടുത്ത കോളിന് മുമ്പ് DPIIT എടുത്ത് വെക്കണം."),
 ("A","wide","കോൾ തീർന്നു, കഥ തീർന്നിട്ടില്ല.")],
 "കോൾ തീർന്നു,\nകഥ തീർന്നിട്ടില്ല", CTA_GRANT, theme="faq",
 cap_ml="മത്സ്യകൃഷി സെൻസർ സ്റ്റാർട്ടപ്പ് KSUM കോളിൽ റിജക്റ്റ് ആയി, കാരണം DPIIT റെക്കഗ്നിഷൻ ഇല്ലാത്തത്. കോളുകൾ മാറും, സെലക്ഷൻ ഉറപ്പില്ല, പക്ഷേ മിക്ക ഗ്രാന്റുകളും ആക്ടീവ് കമ്പനിയും DPIIT-യും ചോദിക്കും. അടുത്ത കോളിന് റെഡിയാണോ?",
 cap_en="A fish-farming sensor startup was rejected in a KSUM call because it had no DPIIT recognition yet. Calls and conditions change and selection is never guaranteed, but most grants ask for an Active company and DPIIT recognition. Ready for the next call: yes or no?",
 cap_mg="Malsyakrishi sensor startup KSUM call-il reject aayi, kaaranam DPIIT recognition illaathathu. Call-ukal maarum, selection urappilla, pakshe mikka grant-ukalum active company-um DPIIT-yum chodikkum. Adutha call-inu ready aano?")

duo("md046", "idea_stage", "C", "thattukada", "പുലിക്കളി ചായം.\nഗ്രാന്റ് ലിസ്റ്റിൽ.\nകമ്പനി \"ഓണം കഴിഞ്ഞ്\"", [
 ("V","wide","സിജോ, പുലിക്കളിക്കാരുടെ തൊലി പൊള്ളാത്ത ചായം എന്റെ ഐഡിയ, KSUM ഐഡിയ ഗ്രാന്റ് ലിസ്റ്റിൽ വന്നു!"),
 ("A","A","ബിജൂ, കൊള്ളാം. കമ്പനി രജിസ്റ്റർ ചെയ്തോ?"),
 ("V","V","ഓണം കഴിഞ്ഞ് നോക്കാം. ഇപ്പോ ചായം അരയ്ക്കുന്ന തിരക്കാ."),
 ("A","wide","കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം, ശരി. പക്ഷേ പണം വരും മുമ്പ് കമ്പനിയും KSUM യുണീക്ക് ID-യും വേണം."),
 ("V","V","അപ്പോ ഓണം കാത്താൽ ഗ്രാന്റ് കാത്തിരിക്കില്ല."),
 ("A","wide","പുലി ഇറങ്ങും മുമ്പ് പേപ്പർ ഇറങ്ങണം.")],
 "പുലി ഇറങ്ങും മുമ്പ്\nപേപ്പർ ഇറങ്ങണം", CTA_GRANT, theme="new",
 cap_ml="പുലിക്കളിക്കാരുടെ തൊലിക്ക് പൊള്ളൽ വരാത്ത ചായം ഉണ്ടാക്കുന്ന ഐഡിയ KSUM ലിസ്റ്റിൽ വന്നു, പക്ഷേ കമ്പനി 'ഓണം കഴിഞ്ഞ്'. ഐഡിയ ഗ്രാന്റിന് കമ്പനിക്ക് മുമ്പ് അപേക്ഷിക്കാം, പക്ഷേ പണത്തിന് കമ്പനിയും യുണീക്ക് ID-യും വേണം. നിങ്ങളുടെ നാട്ടിൽ പുലിക്കളി ഉണ്ടോ?",
 cap_en="An idea for skin-safe paint for Pulikali tiger dancers made the KSUM idea grant list, but the company was planned for 'after Onam'. You may apply before incorporating, but the company and the KSUM Unique ID are needed before money is released. Pulikali in your town: yes or no?",
 cap_mg="Pulikalikkaarude tholikku pollal varaatha chaayam undaakkunna idea KSUM list-il vannu, pakshe company 'Onam kazhinju'. Idea grant-nu company-kku mumpu apekshikkaam, pakshe panathinu company-um Unique ID-yum venam. Ningalude naattil pulikali undo?")

duo("md047", "kerala_registered", "B", "garage", "പാമ്പ് പിടിക്കാൻ\nആപ്പ്. KSUM-ന്\nപേടിയാണോ?", [
 ("A","wide","ജിതിനേ, നിന്റെ പാമ്പ് റെസ്ക്യൂ ആപ്പ് ഇപ്പോ മൂന്ന് ജില്ലയിൽ ഉണ്ടല്ലോ. KSUM-ൽ പോയോ?"),
 ("V","V","ഐശ്വര്യേ, പാമ്പും ഗ്രാന്റും? അവർ ചിരിക്കും. KSUM ഫിൻടെക്കിനൊക്കെയാ."),
 ("A","A","നിന്റെ കമ്പനി കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതല്ലേ? അത് മതി തുടങ്ങാൻ."),
 ("V","wide","KSUM യുണീക്ക് ID അവരുടെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ അപേക്ഷിക്കാം. സ്കീമുകളും ഇൻക്യുബേഷനും ID ഉള്ളവർക്കാ."),
 ("A","A","അപ്പോ ആപ്പ് റെഡി, ഇനി ID."),
 ("V","wide","പാമ്പിനെ പേടിക്കാം, ഫോമിനെ വേണ്ട.")],
 "പാമ്പിനെ പേടിക്കാം,\nഫോമിനെ വേണ്ട", CTA_KSUM, theme="new",
 cap_ml="പാമ്പ് റെസ്ക്യൂ ചെയ്യുന്നവരെ വിളിക്കാനുള്ള ആപ്പ് ഉണ്ടാക്കിയ ആൾ കരുതി KSUM ഫിൻടെക്കിന് മാത്രമാണെന്ന്. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പിന് KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ യുണീക്ക് ID-ക്ക് അപേക്ഷിക്കാം. നിങ്ങളുടെ ആപ്പ് എന്ത് പ്രശ്നം തീർക്കുന്നു?",
 cap_en="A founder whose app alerts snake rescuers near a sighting thought KSUM was only for fintech. A startup registered in Kerala applies for the KSUM Unique ID on KSUM's startup portal, and KSUM schemes and incubation are for startups that hold it. What problem does your app solve?",
 cap_mg="Paampu rescue cheyyunnavare vilikkaanulla app undaakkiya aal karuthi KSUM fintech-nu maathramaanennu. Keralathil register cheytha startup-nu KSUM startup portal-il Unique ID-kku apekshikkaam. Ningalude app enthu prashnam theerkkunnu?")
