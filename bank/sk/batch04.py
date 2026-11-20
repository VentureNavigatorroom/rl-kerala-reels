# Kerala Startup Mission (KSUM) batch 04 (20 Nov, month backlog). Max 6 lines, myth or painful moment first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented). Facts only from topics.FACTS_SK.
# Never state grant amounts or promise selection. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

duo("md030", "kerala_registered", "A", "fishmarket", "മീൻ മണക്കുന്ന\nസ്റ്റാർട്ടപ്പിന്\nKSUM ഉണ്ടോ?", [
 ("V","wide","സുമേച്ചീ, ഐസ് പെട്ടിയിലെ മീനിന്റെ ഫ്രഷ്നസ് അളക്കുന്ന സെൻസർ എന്റെ കമ്പനിയാ. പക്ഷേ KSUM ഒക്കെ ലാപ്ടോപ്പുകാർക്കല്ലേ?"),
 ("A","A","ആന്റണീ, നിന്റെ കമ്പനി കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതല്ലേ? പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലേ?"),
 ("V","V","അതേ, മൂന്ന് വർഷമായി. MCA-യിൽ ആക്ടീവും."),
 ("A","wide","എങ്കിൽ ആദ്യം KSUM-ന്റെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ യുണീക്ക് ഐഡി. KSUM-ന്റെ സ്കീമുകളും ഇൻക്യുബേഷനും ആ ഐഡി ഉള്ളവർക്കാണ്."),
 ("V","V","അപ്പോ ചോദിക്കുന്നത് മാർക്കറ്റിന്റെ മണമല്ല."),
 ("A","wide","കടലാണോ ക്ലൗഡാണോ എന്നല്ല, ഐഡി ഉണ്ടോ എന്നാണ് ചോദ്യം.")],
 "കടലാണോ ക്ലൗഡാണോ\nഎന്നല്ല, ഐഡി\nഉണ്ടോ എന്നാണ്", CTA_KSUM, theme="new",
 cap_ml="മീൻ മാർക്കറ്റിലെ സെൻസർ സ്റ്റാർട്ടപ്പിന് KSUM പറ്റുമോ? KSUM-ന്റെ സ്കീമുകളും ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും KSUM യുണീക്ക് ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്; കമ്പനി കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ്: കടലോ ക്ലൗഡോ?",
 cap_en="Can a fish-freshness sensor startup from a fish market use Kerala Startup Mission? KSUM schemes, incubation and programmes are for startups that hold the KSUM Unique ID, and the company must be registered in Kerala. Your startup: sea or cloud?",
 cap_mg="Meen market-ile sensor startup-inu KSUM pattumo? KSUM schemes, incubation, programmes ellam KSUM Unique ID ulla startup-ukalkkaanu; company Kerala-thil register cheythirikkanam. Ningalude startup: kadalo cloud-o?")

duo("md031", "idea_stage", "B", "tailor", "\"എന്റെ പേരിലുള്ള\nകടയ്ക്ക് സീഡ് ഫണ്ട്\nതരില്ലേ?\"", [
 ("V","wide","ഉഷേ, തയ്യൽക്കാർക്ക് അളവെടുക്കാൻ ഫോൺ ആപ്പ് ഉണ്ടാക്കി. കട എന്റെ പേരിലാ. സീഡ് ഫണ്ടിന് അപേക്ഷിക്കട്ടെ?"),
 ("A","A","മോഹനേട്ടാ, കട പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ? കമ്പനിയോ LLP-യോ ഉണ്ടോ?"),
 ("V","V","എന്തിനാ? കടയും ആപ്പും ഞാൻ തന്നെയല്ലേ."),
 ("A","wide","മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ ചോദിക്കും, MCA-യിൽ ആക്ടീവ് ആയത്. കൂടെ DPIIT-ഉം."),
 ("V","V","അപ്പോ ആദ്യം തുന്നേണ്ടത് കമ്പനിയാ."),
 ("A","wide","കട മോഹനേട്ടന്റെ പേരിൽ, ഗ്രാന്റ് കമ്പനിയുടെ പേരിൽ.")],
 "കട നിങ്ങളുടെ പേരിൽ,\nഗ്രാന്റ് കമ്പനിയുടെ\nപേരിൽ", CTA_GRANT, theme="crm",
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പായി നടത്തുന്ന ബിസിനസിന് KSUM സീഡ് ഫണ്ട് കിട്ടുമോ? മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ, കൂടെ DPIIT അംഗീകാരവും ചോദിക്കും. നിങ്ങളുടെ ബിസിനസ് ഇപ്പോൾ: കടയോ കമ്പനിയോ?",
 cap_en="A tailor built a measuring app but runs everything as a proprietorship. Most KSUM grants and the seed fund ask for a private limited company or LLP that is Active at MCA, plus DPIIT recognition. Your business today: shop or company?",
 cap_mg="Proprietorship aayi nadathunna business-inu KSUM seed fund kittumo? Mikka KSUM grants-um seed fund-um MCA-yil Active aaya Pvt Ltd allenkil LLP, koode DPIIT recognition-um chodikkum. Ningalude business ippol: kadayo company-o?")

duo("md032", "women_founder", "C", "salon", "\"ആദ്യം ഓഫീസ്\nവാടകയ്ക്ക് എടുക്കാം,\nപിന്നെ ഇൻക്യുബേഷൻ\"", [
 ("A","wide","വിനീതേ, എന്റെ ഹെർബൽ ഹെയർ ഓയിൽ സബ്സ്ക്രിപ്ഷന് തിരുവനന്തപുരത്ത് ഒരു ഓഫീസ് വാടകയ്ക്ക് നോക്കുവാ. എന്നിട്ട് ഇൻക്യുബേഷന് പോകാം."),
 ("V","V","സോണിയേ, വാടക കൊടുക്കും മുമ്പ് KSUM യുണീക്ക് ഐഡി എടുത്തോ?"),
 ("A","A","ഐഡി ഒക്കെ ഓഫീസ് കഴിഞ്ഞിട്ട് പോരേ?"),
 ("V","wide","KSUM-ന്റെ ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും യുണീക്ക് ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. അപേക്ഷ KSUM-ന്റെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ."),
 ("A","A","അപ്പോ ആദ്യത്തെ മുറി പോർട്ടലിലാണ്."),
 ("V","wide","താക്കോലിന് മുമ്പ് ഐഡി, വാടകയ്ക്ക് മുമ്പ് പോർട്ടൽ.")],
 "താക്കോലിന് മുമ്പ്\nഐഡി", CTA_KSUM, theme="crm",
 cap_ml="ഇൻക്യുബേഷൻ സ്പേസ് നോക്കുന്ന വനിതാ ഫൗണ്ടർ ആദ്യം ഓഫീസ് വാടകയ്ക്ക് എടുക്കണോ? KSUM-ന്റെ ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും യുണീക്ക് ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്, അപേക്ഷ KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ. നിങ്ങൾ ആദ്യം എടുത്തത്: ഓഫീസോ ഐഡിയോ?",
 cap_en="A woman founder with a herbal hair-oil subscription was about to rent an office before thinking of incubation. KSUM incubation and programmes are for startups that hold the KSUM Unique ID, applied for on KSUM's startup portal. What came first for you: office or ID?",
 cap_mg="Incubation space nokkunna women founder aadyam office vaadakaykku edukkano? KSUM incubation-um programmes-um Unique ID ulla startup-ukalkkaanu, apeksha KSUM startup portal-il. Ningal aadyam eduthath: office-o ID-yo?")

duo("md033", "returnee", "A", "gulfroom", "ദുബായിലെ കമ്പനി\nവെച്ച് കേരളത്തിലെ\nഗ്രാന്റ്?", [
 ("A","wide","ഷംസൂ, എന്റെ ഫ്ലീറ്റ് ട്രാക്കിംഗ് ആപ്പിന് ഇവിടെ ഫ്രീ സോൺ കമ്പനി ഉണ്ട്. നാട്ടിൽ ചെന്ന് അതുവെച്ച് KSUM-ന് അപേക്ഷിക്കാം."),
 ("V","V","നസീർക്കാ, ആ കമ്പനി ദുബായിൽ അല്ലേ രജിസ്റ്റർ ചെയ്തത്?"),
 ("A","A","കമ്പനി കമ്പനി തന്നെ അല്ലേ?"),
 ("V","wide","KSUM-ന് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം. മിക്ക ഗ്രാന്റുകൾക്കും കേരളത്തിൽ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ വേണം."),
 ("A","A","അപ്പോ ടിക്കറ്റിനൊപ്പം ഒരു കേരള കമ്പനിയും."),
 ("V","wide","വിസ ദുബായിലേത്, ഐഡി കേരളത്തിലേത്.")],
 "വിസ ദുബായിലേത്,\nഐഡി കേരളത്തിലേത്", CTA_KSUM, theme="crm",
 cap_ml="ഗൾഫിൽ രജിസ്റ്റർ ചെയ്ത കമ്പനി വെച്ച് KSUM-ന് അപേക്ഷിക്കാമോ? KSUM-ന് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം; മിക്ക ഗ്രാന്റുകൾക്കും പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ വേണം. നിങ്ങൾ ഇപ്പോൾ: ഗൾഫിലോ നാട്ടിലോ?",
 cap_en="A Gulf returnee planned to use his Dubai free-zone company for Kerala Startup Mission. KSUM asks that the startup is registered in Kerala, and most KSUM grants need a private limited company or LLP. Where are you right now: Gulf or Kerala?",
 cap_mg="Gulf-il register cheytha company vechu KSUM-inu apekshikkaamo? KSUM-inu startup Kerala-thil register cheythirikkanam; mikka grants-inum Pvt Ltd allenkil LLP venam. Ningal ippol: Gulf-ilo naattilo?")

duo("md034", "kerala_registered", "B", "mobileshop", "DPIIT സർട്ടിഫിക്കറ്റ്\nഫ്രെയിം ചെയ്തു.\n\"KSUM ഐഡി ഓട്ടോ ആണോ?\"", [
 ("V","wide","ഹന്നാ, ഫോൺ റിപ്പയർ ബുക്കിംഗ് ആപ്പിന് DPIIT കിട്ടി. ഇനി KSUM ഐഡി തനിയെ വരുമല്ലോ?"),
 ("A","A","ഫഹദേ, അത് ഒരു സിം രണ്ട് ഫോണിൽ ഇടുന്ന പോലെയല്ല."),
 ("V","V","രണ്ടും സ്റ്റാർട്ടപ്പിന്റെ സർട്ടിഫിക്കറ്റ് അല്ലേ?"),
 ("A","wide","DPIIT വേറെ. KSUM യുണീക്ക് ഐഡി KSUM-ന്റെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ വേറെ അപേക്ഷിക്കണം. KSUM സ്കീമുകൾ ആ ഐഡി ഉള്ളവർക്ക്."),
 ("V","V","അപ്പോ ഫ്രെയിമിന് അടുത്ത് ഒരു ആണി കൂടി."),
 ("A","wide","ഡൽഹിയുടെ പേപ്പർ ഒന്ന്, കേരളത്തിന്റെ ഐഡി വേറെ.")],
 "ഡൽഹിയുടെ പേപ്പർ ഒന്ന്,\nകേരളത്തിന്റെ ഐഡി\nവേറെ", CTA_KSUM, theme="faq",
 cap_ml="DPIIT അംഗീകാരം കിട്ടിയാൽ KSUM യുണീക്ക് ഐഡി തനിയെ കിട്ടുമോ? ഇല്ല. KSUM യുണീക്ക് ഐഡിക്ക് KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ വേറെ അപേക്ഷിക്കണം; KSUM സ്കീമുകൾ ആ ഐഡി ഉള്ളവർക്കാണ്. നിങ്ങൾക്ക് ഏതുണ്ട്: DPIIT, KSUM, രണ്ടും?",
 cap_en="Does DPIIT recognition give you the KSUM Unique ID automatically? No. The KSUM Unique ID is a separate application on KSUM's startup portal, and KSUM schemes are for startups that hold it. Which do you have: DPIIT, KSUM or both?",
 cap_mg="DPIIT recognition kittiyaal KSUM Unique ID thaniye kittumo? Illa. KSUM Unique ID-kku KSUM startup portal-il vere apekshikkanam; KSUM schemes aa ID ullavarkkaanu. Ningalkku ethund: DPIIT, KSUM, randum?")

duo("md035", "kerala_registered", "C", "farm", "തെങ്ങുകയറ്റ\nയന്ത്രം. ഗ്രാമത്തിൽ.\nKSUM കൊച്ചിക്ക് മാത്രമോ?", [
 ("A","wide","ഗോപിയേ, നിന്റെ തെങ്ങുകയറ്റ യന്ത്രത്തിന്റെ കമ്പനി എന്തായി? KSUM-ൽ ചേർന്നോ?"),
 ("V","V","വാസുവേട്ടാ, അതൊക്കെ കൊച്ചിയിലെ ടെക്ക് പാർക്കുകാർക്കല്ലേ? നമ്മൾ മലയോരത്തല്ലേ?"),
 ("A","A","നിന്റെ കമ്പനി എവിടെയാ രജിസ്റ്റർ ചെയ്തത്?"),
 ("V","wide","ഇവിടെ തന്നെ, പഞ്ചായത്തിലെ വീട്ടുവിലാസത്തിൽ. പ്രൈവറ്റ് ലിമിറ്റഡ്."),
 ("A","wide","KSUM ചോദിക്കുന്നത് കേരളത്തിൽ രജിസ്ട്രേഷൻ. യുണീക്ക് ഐഡിക്ക് അപേക്ഷ ഓൺലൈൻ, KSUM-ന്റെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ."),
 ("V","wide","തെങ്ങ് ഗ്രാമത്തിൽ, പോർട്ടൽ ഫോണിൽ.")],
 "തെങ്ങ് ഗ്രാമത്തിൽ,\nപോർട്ടൽ ഫോണിൽ", CTA_KSUM, theme="faq",
 cap_ml="ഗ്രാമത്തിലെ സ്റ്റാർട്ടപ്പിന് KSUM പറ്റില്ലെന്ന് കരുതിയോ? KSUM ചോദിക്കുന്നത് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പ്; യുണീക്ക് ഐഡിക്ക് KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ ഓൺലൈനായി അപേക്ഷിക്കാം. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ്: നഗരമോ ഗ്രാമമോ?",
 cap_en="A coconut-climbing machine maker in a hill village thought KSUM was only for Kochi tech parks. KSUM asks that the startup is registered in Kerala, and the Unique ID is applied for online on KSUM's startup portal. Your startup: city or village?",
 cap_mg="Graamathile startup-inu KSUM pattillennu karuthiyo? KSUM chodikkunnath Kerala-thil register cheytha startup; Unique ID-kku KSUM startup portal-il online aayi apekshikkaam. Ningalude startup: nagaramo graamamo?")

duo("md036", "idea_stage", "A", "courier", "\"ഗ്രാന്റ് ജയിച്ചാൽ\nKSUM ഐഡി സമ്മാനമായി\nകിട്ടും\"", [
 ("V","wide","ജയേ, നമ്മുടെ ഇലക്ട്രിക് കാർഗോ സൈക്കിൾ ഡെലിവറിക്ക് ഗ്രാന്റ് കിട്ടിയാൽ KSUM ഐഡിയും കൂടെ തരുമല്ലോ."),
 ("A","A","അരവിന്ദേ, ഐഡി ഒരു മെഡൽ ആണെന്നാണോ വിചാരം?"),
 ("V","V","അല്ലേ? ജയിച്ചവർക്കല്ലേ ഐഡി?"),
 ("A","wide","തിരിച്ചാ. KSUM-ന്റെ ഗ്രാന്റുകളും പ്രോഗ്രാമുകളും ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. ഐഡിയ ഗ്രാന്റിൽ പോലും പണം വരും മുമ്പ് ഐഡി വേണം."),
 ("V","V","അപ്പോ പാർസൽ അയക്കും മുമ്പ് വിലാസം."),
 ("A","wide","ഐഡി സമ്മാനമല്ല, ടിക്കറ്റാണ്.")],
 "ഐഡി സമ്മാനമല്ല,\nടിക്കറ്റാണ്", CTA_GRANT, theme="faq",
 cap_ml="ഗ്രാന്റ് ജയിച്ചതിന് ശേഷമാണോ KSUM യുണീക്ക് ഐഡി? അല്ല. KSUM-ന്റെ ഗ്രാന്റുകളും പ്രോഗ്രാമുകളും ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്; ഐഡിയ ഗ്രാന്റിൽ പോലും പണം റിലീസ് ആകും മുമ്പ് കമ്പനിയും ഐഡിയും വേണം. ഐഡി: സമ്മാനമോ ടിക്കറ്റോ?",
 cap_en="An electric cargo-cycle delivery startup thought the KSUM Unique ID is handed out after winning a grant. It's the other way round: KSUM grants and programmes are for startups that hold the ID, and even the idea grant needs the company and the ID before money is released. The ID: prize or ticket?",
 cap_mg="Grant jayichathinu sheshamaano KSUM Unique ID? Alla. KSUM grants-um programmes-um ID ulla startup-ukalkkaanu; idea grant-il polum panam release aakum munpu company-um ID-yum venam. ID: sammaanamo ticket-o?")

chat("mc002", "returnee", "B", "ജർമ്മനിയിലെ കോ-ഫൗണ്ടർ:\n\"സീഡ് ഫണ്ടിന്\nഎന്തൊക്കെ വേണം?\"", ("ആതിര", "അമൽ"), [
 (1, "ആതിരേ, ഇവിടെ ഇരുന്ന് ഞാൻ പിച്ച് ഡെക്ക് തീർത്തു. KSUM സീഡ് ഫണ്ടിന് നമ്മുടെ കയ്യിൽ എന്തൊക്കെ വേണം?"),
 (0, "അമലേ, ഡെക്ക് മാത്രം പോരാ. മൂന്ന് കാര്യം ചെക്ക് ചെയ്യണം."),
 (1, "പറ, ഞാൻ എഴുതിയെടുക്കാം."),
 (0, "കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത പ്രൈവറ്റ് ലിമിറ്റഡ്, MCA-യിൽ ആക്ടീവ്. DPIIT അംഗീകാരം. പിന്നെ KSUM യുണീക്ക് ഐഡി."),
 (1, "ഡെക്ക് റെഡി, പേപ്പർ പകുതി. ഞാൻ ഇന്ന് തന്നെ DPIIT നോക്കാം."),
 (0, "മൂന്ന് പേപ്പർ, പിന്നെ ഒരു അപേക്ഷ.")],
 "മൂന്ന് പേപ്പർ,\nപിന്നെ ഒരു അപേക്ഷ", CTA_GRANT, theme="crm",
 cap_ml="കോ-ഫൗണ്ടർ വിദേശത്ത്, പിച്ച് ഡെക്ക് റെഡി. KSUM സീഡ് ഫണ്ടിന് മുമ്പ് ചെക്ക് ചെയ്യൂ: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത്, MCA-യിൽ ആക്ടീവ് ആയ പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ, DPIIT അംഗീകാരം, KSUM യുണീക്ക് ഐഡി. നിങ്ങൾക്ക് ഇതിൽ എത്ര റെഡി?",
 cap_en="One co-founder abroad, pitch deck ready, but are the papers? Before the KSUM seed fund, check three things: a Kerala-registered private limited company or LLP that is Active at MCA, DPIIT recognition and the KSUM Unique ID. How many of the three do you have?",
 cap_mg="Co-founder videshathu, pitch deck ready. KSUM seed fund-inu munpu check cheyyu: Kerala-thil register cheythu MCA-yil Active aaya Pvt Ltd allenkil LLP, DPIIT recognition, KSUM Unique ID. Ningalkku ithil ethra ready?")

duo("md037", "idea_stage", "C", "veranda", "62 വയസ്സിൽ ആപ്പ്.\n\"KSUM ചെറുപ്പക്കാർക്ക്\nമാത്രമല്ലേ?\"", [
 ("V","wide","ശാന്തേ, ഗൾഫിലെ കുട്ടികൾക്ക് മലയാളം പഠിക്കാൻ ഞാൻ ഉണ്ടാക്കിയ ആപ്പ് ഹിറ്റാവുന്നു. പക്ഷേ KSUM ഒക്കെ പിള്ളേർക്കല്ലേ?"),
 ("A","A","ബാലൻ മാഷേ, മുപ്പത് കൊല്ലം പിള്ളേരെ പഠിപ്പിച്ച ആൾ ഇപ്പോ അവരെ പേടിക്കുന്നോ?"),
 ("V","V","പേടിയല്ല. ഫോമിൽ വയസ്സ് ചോദിച്ചാലോ?"),
 ("A","wide","KSUM ചോദിക്കുന്നത് വയസ്സല്ല. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പും KSUM യുണീക്ക് ഐഡിയും."),
 ("V","V","അപ്പോ ചോക്ക് താഴെ വെച്ച്, കമ്പനി എടുക്കാം."),
 ("A","wide","മുടി നരച്ചാലും ഐഡി പുതിയതാകാം.")],
 "മുടി നരച്ചാലും\nഐഡി പുതിയതാകാം", CTA_KSUM, theme="new",
 cap_ml="62 വയസ്സുള്ള റിട്ടയേഡ് അധ്യാപകന്റെ മലയാളം പഠന ആപ്പ്. KSUM ചോദിക്കുന്നത് വയസ്സല്ല: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പും KSUM യുണീക്ക് ഐഡിയും. സ്റ്റാർട്ടപ്പ് തുടങ്ങാൻ വൈകിയോ: അതെ / ഇല്ല?",
 cap_en="A retired teacher, 62, built an app that teaches Malayalam to children in the Gulf and assumed KSUM is only for the young. KSUM asks for a startup registered in Kerala and the KSUM Unique ID, not your age. Too late to start: yes or no?",
 cap_mg="62 vayassulla retired teacher-inte Malayalam padana app. KSUM chodikkunnath vayassalla: Kerala-thil register cheytha startup-um KSUM Unique ID-yum. Startup thudangaan vaikiyo: athe / illa?")

duo("md038", "kerala_registered", "A", "juiceshop", "\"KSUM ഗ്രാന്റ് എത്രയാ\nഎന്ന് ഗ്രൂപ്പിൽ\nകണ്ടു\"", [
 ("V","wide","റസിയാ, ഫ്രൂട്ട് വേസ്റ്റിൽ നിന്ന് പാക്കിംഗ് ഉണ്ടാക്കുന്ന നമ്മുടെ കമ്പനിക്ക് ഗ്രാന്റ് ഇത്ര കിട്ടും എന്ന് ഒരു ഗ്രൂപ്പിൽ കണ്ടു."),
 ("A","A","നൗഷാദേ, ആ മെസേജ് ഏത് വർഷത്തേതാ?"),
 ("V","V","അറിയില്ല. എല്ലാവരും ഫോർവേഡ് ചെയ്യുന്നുണ്ട്."),
 ("A","wide","തുകയും കോളും മാറും. ഇപ്പോഴത്തെ ലൈവ് കോൾ KSUM-ൽ നോക്കണം. മിക്കതിനും DPIIT-ഉം ആക്ടീവ് കമ്പനിയും യുണീക്ക് ഐഡിയും ചോദിക്കും."),
 ("V","V","അപ്പോ ഫോർവേഡ് അല്ല, ഫയൽ റെഡിയാക്കണം."),
 ("A","wide","ഗ്രാന്റിന്റെ തുക ഗ്രൂപ്പിലല്ല, ലൈവ് കോളിലാണ്.")],
 "ഗ്രാന്റിന്റെ കണക്ക്\nഗ്രൂപ്പിലല്ല,\nലൈവ് കോളിൽ", CTA_GRANT, theme="faq",
 cap_ml="ഗ്രൂപ്പിൽ ഫോർവേഡ് ആയി വന്ന KSUM ഗ്രാന്റ് തുക വിശ്വസിക്കാമോ? തുകയും കോളും മാറും; ഇപ്പോഴത്തെ ലൈവ് കോൾ KSUM-ൽ തന്നെ നോക്കണം, തിരഞ്ഞെടുപ്പ് ഉറപ്പുമല്ല. മിക്ക കോളുകൾക്കും DPIIT, ആക്ടീവ് കമ്പനി, KSUM യുണീക്ക് ഐഡി വേണം. നിങ്ങൾ ആദ്യം നോക്കുന്നത്: ഗ്രൂപ്പോ പോർട്ടലോ?",
 cap_en="A fruit-waste packaging startup saw a forwarded message with a fixed KSUM grant figure. Grant amounts and calls change, so check the live call with KSUM itself; selection is never guaranteed. Most calls also ask for DPIIT recognition, an Active company and the KSUM Unique ID. Where do you check first: group or portal?",
 cap_mg="Group-il forward aayi vanna KSUM grant thuka vishwasikkaamo? Thukayum call-um maarum; ippozhathe live call KSUM-il thanne nokkanam, selection urappumalla. Mikka calls-inum DPIIT, Active company, KSUM Unique ID venam. Ningal aadyam nokkunnath: group-o portal-o?")
