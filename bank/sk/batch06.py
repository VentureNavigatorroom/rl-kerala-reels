# Kerala Startup Mission (KSUM) batch 06 (20 Nov, month backlog). Max 6 lines, myth or painful moment first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented). Facts only from topics.FACTS_SK.
# Never state grant amounts or promise selection. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT


duo("md048", "women_founder", "A", "textile", "\"ഗ്രാന്റ് കിട്ടിയാലേ\nഇൻക്യുബേഷൻ ഉള്ളൂ\"", [
 ("A","wide","പ്രകാശേ, കൈത്തറി തുണിയിൽ യോഗ വെയർ. 400 ഓർഡർ കഴിഞ്ഞു. ഇനി ഒരു മെന്ററും ഇൻക്യുബേഷൻ ഇടവും വേണം."),
 ("V","V","രമ്യേ, എന്നിട്ട് എന്താ അപേക്ഷിക്കാത്തത്?"),
 ("A","A","ആദ്യം ഗ്രാന്റ് കിട്ടണ്ടേ? കിട്ടിയവർക്കല്ലേ ഇൻക്യുബേഷനും മെന്ററിംഗും?"),
 ("V","wide","അല്ല. KSUM-ന്റെ ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും ഗ്രാന്റും എല്ലാം യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പിനാ. ഓരോന്നും വേറെ വാതിൽ."),
 ("A","A","അപ്പോ ഗ്രാന്റ് കാത്തിരിക്കണ്ട, ID എടുത്താൽ മതി."),
 ("V","wide","ഗ്രാന്റ് ഒരു വാതിൽ. താക്കോൽ ID.")],
 "ഗ്രാന്റ് ഒരു വാതിൽ,\nതാക്കോൽ ID", CTA_KSUM, theme="crm",
 cap_ml="കൈത്തറി യോഗ വെയർ ബ്രാൻഡ് നടത്തുന്ന ഫൗണ്ടർ കരുതി, ഗ്രാന്റ് കിട്ടിയവർക്കേ KSUM ഇൻക്യുബേഷനും മെന്ററിംഗും ഉള്ളൂ എന്ന്. ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും ഗ്രാന്റുകളും KSUM യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. നിങ്ങൾക്ക് ആദ്യം വേണ്ടത് മെന്ററോ ഗ്രാന്റോ?",
 cap_en="A handloom yogawear founder thought KSUM incubation and mentoring were only for startups that had already won a grant. KSUM's incubation, programmes and grants are each for startups that hold the KSUM Unique ID. What do you need first: a mentor or a grant?",
 cap_mg="Kaithari yoga wear brand nadathunna founder karuthi, grant kittiyavarkke KSUM incubation-um mentoring-um ullu ennu. Incubation-um programmes-um grants-um KSUM Unique ID ulla startup-ukalkkaanu. Ningalkku aadyam vendathu mentor-o grant-o?")

duo("md049", "kerala_registered", "B", "canteen", "\"ID എന്റെ പേരിലാ.\nപുതിയ കമ്പനിക്കും\nഅത് മതി\"", [
 ("A","wide","അമലേ, നീ ഹൗസ്ബോട്ട് ബുക്കിംഗ് ആപ്പ് വിട്ടോ? ഇപ്പോ ചകിരി ഗ്രോ ബാഗിന്റെ പിന്നാലെയാണല്ലോ."),
 ("V","V","ആതിരേ, ആപ്പ് കമ്പനി അവിടെ ഉണ്ട്. ഗ്രോ ബാഗിന് പുതിയ LLP എടുത്തു. പഴയ KSUM ID ഇതിലും ഇടാം."),
 ("A","A","ആ ID നിന്റെ പേരിലാണോ, ആപ്പ് കമ്പനിയുടെ പേരിലാണോ?"),
 ("V","wide","യുണീക്ക് ID ഫൗണ്ടറുടേതല്ല, ഓരോ സ്റ്റാർട്ടപ്പിന്റേതുമാ. പുതിയ LLP-ക്ക് KSUM പോർട്ടലിൽ സ്വന്തം അപേക്ഷ വേണം."),
 ("A","A","അപ്പോ ബോട്ടിന്റെ ടിക്കറ്റിൽ ബാഗ് കയറില്ല."),
 ("V","wide","ഫൗണ്ടർ ഒന്ന്. ID ഓരോ കമ്പനിക്കും.")],
 "ഫൗണ്ടർ ഒന്ന്,\nID ഓരോ കമ്പനിക്കും", CTA_KSUM, theme="new",
 cap_ml="ഹൗസ്ബോട്ട് ബുക്കിംഗ് ആപ്പിന് KSUM യുണീക്ക് ID ഉള്ള ഫൗണ്ടർ ചകിരി ഗ്രോ ബാഗിനായി പുതിയ LLP തുടങ്ങി, പഴയ ID മതിയെന്ന് കരുതി. ID ഫൗണ്ടറുടേതല്ല, ഓരോ സ്റ്റാർട്ടപ്പിന്റേതുമാണ്; പുതിയ LLP-ക്ക് KSUM പോർട്ടലിൽ സ്വന്തം അപേക്ഷ വേണം. നിങ്ങളുടേത് എത്രാമത്തെ സ്റ്റാർട്ടപ്പ്?",
 cap_en="A founder whose houseboat-booking app holds a KSUM Unique ID started a new LLP for coir grow bags and planned to reuse the old ID. The ID belongs to each startup, not the founder, so the new LLP applies on KSUM's startup portal on its own. Which number startup is yours?",
 cap_mg="Houseboat booking app-inu KSUM Unique ID ulla founder coir grow bag-inaayi puthiya LLP thudangi, pazhaya ID mathiyennu karuthi. ID founder-udethalla, oro startup-intethumaanu; puthiya LLP-kku KSUM portal-il swantham apeksha venam. Ningaludethu ethraamathe startup?")

duo("md050", "idea_stage", "C", "weddinghall", "\"ആദ്യം KSUM ID.\nകമ്പനി പിന്നെ\nനോക്കാം\"", [
 ("A","wide","ശരത്തേ, കല്യാണ സദ്യയുടെ ബാക്കി ഭക്ഷണം അനാഥാലയങ്ങളിൽ എത്തിക്കുന്ന ആപ്പ്. ഇന്ന് തന്നെ KSUM ID എടുക്കും."),
 ("V","V","കാവ്യേ, നല്ലത്. കമ്പനി രജിസ്റ്റർ ചെയ്തോ?"),
 ("A","A","അത് ID കിട്ടിയിട്ട്. ID ആദ്യം, കമ്പനി പിന്നെ."),
 ("V","wide","ക്രമം തിരിച്ചാ. യുണീക്ക് ID സ്റ്റാർട്ടപ്പിനാ, സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതായിരിക്കണം. ആദ്യം കമ്പനിയോ LLP-യോ."),
 ("A","A","അപ്പോ താലി കെട്ടും മുമ്പ് ആൽബം അടിക്കരുത്."),
 ("V","wide","ആദ്യം കല്യാണം. പിന്നെ ആൽബം.")],
 "ആദ്യം കല്യാണം,\nപിന്നെ ആൽബം", CTA_KSUM, theme="faq",
 cap_ml="KSUM യുണീക്ക് ID ആദ്യം, കമ്പനി പിന്നെ എന്നാണോ പ്ലാൻ? ID സ്റ്റാർട്ടപ്പിനാണ്, സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതായിരിക്കണം; അതുകൊണ്ട് ആദ്യം കമ്പനിയോ LLP-യോ, പിന്നെ KSUM പോർട്ടലിൽ ID. നിങ്ങൾ ഏത് സ്റ്റെപ്പിലാ?",
 cap_en="Planning to get the KSUM Unique ID first and register the company later? The ID is for a startup registered in Kerala, so the company or LLP comes first, then the ID on KSUM's startup portal. Which step are you on?",
 cap_mg="KSUM Unique ID aadyam, company pinne ennaano plan? ID startup-inaanu, startup Kerala-yil register cheythathaayirikkanam; athukondu aadyam company-o LLP-yo, pinne KSUM portal-il ID. Ningal ethu step-ilaa?")

duo("md051", "kerala_registered", "A", "ferry", "\"KSUM ID ഉണ്ട്.\nഇനി DPIIT\nഎന്തിനാ?\"", [
 ("A","wide","ടോണീ, കുട്ടനാട്ടിലെ വള്ളങ്ങൾക്ക് സോളാർ മോട്ടോർ. കമ്പനിക്ക് KSUM ID കിട്ടി. ഇനി സീഡ് ഫണ്ട് നോക്കാം."),
 ("V","V","മീരേ, DPIIT റെക്കഗ്നിഷൻ എടുത്തോ?"),
 ("A","A","KSUM ID ഉള്ളപ്പോ ഡൽഹിയിലെ പേപ്പർ എന്തിനാ?"),
 ("V","wide","KSUM ID ആദ്യ പടി. മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും DPIIT റെക്കഗ്നിഷനും ചോദിക്കും. ലൈവ് കോൾ നോക്കണം."),
 ("A","A","അപ്പോ ഒരു തുഴ കൊണ്ട് വള്ളം നീങ്ങില്ല."),
 ("V","wide","ഒരു തുഴ KSUM. മറ്റേ തുഴ DPIIT.")],
 "ഒരു തുഴ KSUM,\nമറ്റേ തുഴ DPIIT", CTA_GRANT, theme="faq",
 cap_ml="കുട്ടനാട്ടിലെ വള്ളങ്ങൾക്ക് സോളാർ മോട്ടോർ ഉണ്ടാക്കുന്ന കമ്പനിക്ക് KSUM യുണീക്ക് ID കിട്ടി, ഇനി DPIIT വേണ്ടെന്ന് കരുതി. മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും DPIIT റെക്കഗ്നിഷനും ചോദിക്കും; ഓരോ ലൈവ് കോളും നോക്കണം. നിങ്ങൾക്ക് DPIIT ഉണ്ടോ?",
 cap_en="A company building solar motors for Kuttanad country boats got its KSUM Unique ID and thought DPIIT was no longer needed. Most KSUM grants and the seed fund also ask for DPIIT recognition, so check each live call. Do you have DPIIT recognition?",
 cap_mg="Kuttanadile vallangalkku solar motor undaakkunna company-kku KSUM Unique ID kitti, ini DPIIT vendennu karuthi. Mikka KSUM grants-um seed fund-um DPIIT recognition-um chodikkum; oro live call-um nokkanam. Ningalkku DPIIT undo?")

duo("md052", "campus", "B", "hostel", "\"ഡിഗ്രി കഴിഞ്ഞിട്ട്\nKSUM. ഇപ്പോ\nപഠിക്ക്\"", [
 ("A","wide","സഞ്ജൂ, ഹോസ്റ്റൽ മെസ്സിലെ ഭക്ഷണം പാഴാകുന്നത് അളക്കുന്ന നമ്മുടെ സ്കെയിൽ. അച്ഛൻ പറയുന്നു, ഡിഗ്രി കഴിഞ്ഞ് നോക്കാമെന്ന്."),
 ("V","V","അലീനേ, ഫൈനൽ ഇയർ ആണെന്ന് വെച്ച് ഐഡിയ കാത്തിരിക്കുമോ?"),
 ("A","A","കമ്പനി ഇല്ലല്ലോ. അതുകൊണ്ട് അപേക്ഷിക്കാൻ പറ്റില്ല എന്നാ കരുതിയത്."),
 ("V","wide","ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെയും അപേക്ഷിക്കാം. പണം വരും മുമ്പ് കമ്പനിയും KSUM യുണീക്ക് ID-യും വേണം. ലൈവ് കോളിലെ നിബന്ധന നോക്കണം."),
 ("A","A","അപ്പോ പരീക്ഷയും അപേക്ഷയും ഒരേ സെമസ്റ്ററിൽ."),
 ("V","wide","സർട്ടിഫിക്കറ്റ് കാത്താൽ ഐഡിയ തണുക്കും.")],
 "സർട്ടിഫിക്കറ്റ് കാത്താൽ\nഐഡിയ തണുക്കും", CTA_GRANT, theme="faq",
 cap_ml="ഹോസ്റ്റൽ മെസ്സിലെ ഭക്ഷണം പാഴാകുന്നത് അളക്കുന്ന സ്കെയിൽ ഉണ്ടാക്കിയ ഫൈനൽ ഇയർ ടീം, കമ്പനി ഇല്ലാത്തതുകൊണ്ട് ഡിഗ്രി കഴിഞ്ഞ് നോക്കാമെന്ന് കരുതി. ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെയും അപേക്ഷിക്കാം; പണം വരും മുമ്പ് കമ്പനിയും KSUM യുണീക്ക് ID-യും വേണം. നിങ്ങൾ ഏത് വർഷമാ?",
 cap_en="A final-year team built a scale that measures food wasted in the hostel mess, and planned to wait for their degree because they have no company. You may apply for the idea grant before incorporating; the company and KSUM Unique ID are needed before money is released. Which year are you in?",
 cap_mg="Hostel mess-ile bhakshanam paazhaakunnathu alakkunna scale undaakkiya final year team, company illaathathukondu degree kazhinju nokkaamennu karuthi. Idea grant-inu company illaatheyum apekshikkaam; panam varum mumbu company-um KSUM Unique ID-yum venam. Ningal ethu varshamaa?")

duo("md053", "returnee", "C", "gulf", "\"പഴയ കമ്പനി\nതരാം, KSUM-ന്\nഎളുപ്പം\"", [
 ("A","wide","ഫൈസലേ, നാട്ടിൽ ഒരു കൂട്ടുകാരന്റെ ആറ് വർഷം പഴയ കമ്പനി ഉണ്ട്. ഞാൻ അതെടുത്ത് വാട്ടർ പ്യൂരിഫയർ സർവീസ് ആപ്പ് തുടങ്ങും."),
 ("V","V","ഷിജൂ, അത് ഇപ്പോ എന്ത് ചെയ്യുന്നു? എത്ര കാലമായി ഫയലിംഗ്?"),
 ("A","A","അറിയില്ല. പഴയതായാൽ KSUM-ന് കൂടുതൽ വിശ്വാസം തോന്നുമല്ലോ."),
 ("V","wide","പഴക്കത്തിന് മാർക്കില്ല. മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും MCA-യിൽ ആക്ടീവ് സ്റ്റാറ്റസ് ചോദിക്കും. കേരളത്തിൽ രജിസ്റ്ററും വേണം."),
 ("A","A","അപ്പോ വിമാനം കയറും മുമ്പ് MCA-യിൽ ഒന്ന് നോക്കണം."),
 ("V","wide","പഴയ കമ്പനി വാങ്ങാം. പഴയ പ്രശ്നം വാങ്ങരുത്.")],
 "പഴയ കമ്പനി വാങ്ങാം,\nപഴയ പ്രശ്നം വാങ്ങരുത്", CTA_GRANT, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചുവരുന്നയാൾ കൂട്ടുകാരന്റെ ആറ് വർഷം പഴയ കമ്പനി എടുത്താൽ KSUM-ന് എളുപ്പമാകുമെന്ന് കരുതി. പഴക്കത്തിന് മാർക്കില്ല; മിക്ക KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും MCA-യിൽ 'Active' സ്റ്റാറ്റസും കേരള രജിസ്ട്രേഷനും ചോദിക്കും. നിങ്ങൾ MCA സ്റ്റാറ്റസ് നോക്കിയിട്ടുണ്ടോ?",
 cap_en="A Gulf returnee planned to take over a friend's six-year-old company, thinking an older company looks better to KSUM. Age earns no extra points: most KSUM grants and the seed fund ask for 'Active' status at MCA and a startup registered in Kerala. Have you checked the MCA status?",
 cap_mg="Gulf-il ninnu thirichuvarunnayaal koottukaarante aaru varsham pazhaya company eduthaal KSUM-inu eluppamaakumennu karuthi. Pazhakkathinu mark illa; mikka KSUM grants-um seed fund-um MCA-yil 'Active' status-um Kerala registration-um chodikkum. Ningal MCA status nokkiyittundo?")

duo("md054", "women_founder", "A", "balcony", "\"അപേക്ഷിക്കും മുമ്പ്\nകമ്പനി വേണം.\nഇല്ലെങ്കിൽ നാണക്കേട്\"", [
 ("A","wide","വിവേകേ, പാള കൊണ്ട് സദ്യ പ്ലേറ്റ്. ക്ഷേത്ര ഉത്സവങ്ങൾക്ക് പ്ലാസ്റ്റിക് വേണ്ട. ഐഡിയ ഗ്രാന്റ് കോൾ തുറന്നിട്ടുണ്ട്."),
 ("V","V","അമ്മൂ, എന്നിട്ട് അപേക്ഷിച്ചില്ലേ?"),
 ("A","A","കമ്പനി ഇല്ലാതെ അപേക്ഷിച്ചാൽ അവർ ചിരിക്കില്ലേ? ആദ്യം രജിസ്റ്റർ ചെയ്യാം, അടുത്ത കോളിന് നോക്കാം."),
 ("V","wide","ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം. കമ്പനിയും യുണീക്ക് ID-യും പണം വരും മുമ്പ് മതി. കോൾ കാത്തിരിക്കില്ല."),
 ("A","A","അപ്പോ നാണം അടുത്ത കോളിലേക്ക് മാറ്റാം."),
 ("V","wide","പാള വീഴും മുമ്പ് പെറുക്കണം.")],
 "പാള വീഴും മുമ്പ്\nപെറുക്കണം", CTA_GRANT, theme="faq",
 cap_ml="പാള കൊണ്ട് സദ്യ പ്ലേറ്റ് ഉണ്ടാക്കാൻ ഐഡിയ ഉള്ളയാൾ, കമ്പനി ഇല്ലാതെ അപേക്ഷിച്ചാൽ നാണക്കേടാണെന്ന് കരുതി കോൾ വിട്ടു. ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം; കമ്പനിയും KSUM യുണീക്ക് ID-യും പണം വരും മുമ്പ് വേണം. നിങ്ങൾ ഏതെങ്കിലും കോൾ ഇങ്ങനെ വിട്ടിട്ടുണ്ടോ?",
 cap_en="A founder with an arecanut-sheath plate idea for temple feasts skipped the idea grant call, thinking applying without a company would look bad. You may apply for the idea grant before incorporating; the company and KSUM Unique ID are needed before the money is released. Have you skipped a call like this?",
 cap_mg="Paala kondu sadya plate undaakkaan idea ullayaal, company illaathe apekshichaal naanakkedaanennu karuthi call vittu. Idea grant-inu company illaathe apekshikkaam; company-um KSUM Unique ID-yum panam varum mumbu venam. Ningal ethenkilum call ingane vittittundo?")

duo("md055", "kerala_registered", "B", "petrolpump", "\"ഓഫീസ് ബെംഗളൂരുവിലേക്ക്\nമാറ്റി. KSUM ID\nകൂടെ വരും\"", [
 ("A","wide","ഷിബൂ, ഓട്ടോകൾക്ക് ബാറ്ററി മാറ്റാനുള്ള സ്റ്റേഷൻ. ഇൻവെസ്റ്റർ പറഞ്ഞു, രജിസ്റ്റേർഡ് ഓഫീസ് ബെംഗളൂരുവിലേക്ക് മാറ്റാൻ."),
 ("V","V","സന്തോഷേ, അപ്പോ കേരളത്തിലെ KSUM കാര്യങ്ങൾ?"),
 ("A","A","വിലാസം മാത്രമല്ലേ മാറുന്നത്? ഓട്ടോയും സ്റ്റേഷനും ഇവിടെ തന്നെ."),
 ("V","wide","KSUM നോക്കുന്നത് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതാണോ എന്നാ. ഓഫീസ് മാറിയാൽ രജിസ്ട്രേഷൻ കർണാടകയിലാകും."),
 ("A","A","അപ്പോ ഒപ്പിടും മുമ്പ് ഇതും ചോദിക്കണം."),
 ("V","wide","ഓട്ടോ ഇവിടെ ഓടും. രജിസ്ട്രേഷൻ അവിടെ ഇരിക്കും.")],
 "ഓട്ടോ ഇവിടെ,\nരജിസ്ട്രേഷൻ അവിടെ", CTA_KSUM, theme="new",
 cap_ml="ഓട്ടോ ബാറ്ററി സ്വാപ്പിംഗ് സ്റ്റാർട്ടപ്പിനോട് ഇൻവെസ്റ്റർ രജിസ്റ്റേർഡ് ഓഫീസ് ബെംഗളൂരുവിലേക്ക് മാറ്റാൻ പറഞ്ഞു; വിലാസം മാത്രമല്ലേ എന്ന് ഫൗണ്ടർ. KSUM സ്കീമുകൾക്ക് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതായിരിക്കണം; ഓഫീസ് മാറിയാൽ രജിസ്ട്രേഷൻ കർണാടകയിലാകും. നിങ്ങളുടെ കമ്പനി ഏത് സംസ്ഥാനത്താ?",
 cap_en="An investor asked an auto battery-swapping startup to shift its registered office to Bengaluru, and the founder thought only the address changes. KSUM schemes need a startup registered in Kerala; shifting the registered office moves the registration to Karnataka. Which state is your company registered in?",
 cap_mg="Auto battery swapping startup-inodu investor registered office Bengaluru-vilekku maattaan paranju; vilaasam maathramalle ennu founder. KSUM schemes-inu startup Kerala-yil register cheythathaayirikkanam; office maariyaal registration Karnataka-yilaakum. Ningalude company ethu samsthaanathaa?")

duo("md056", "idea_stage", "C", "autostand", "\"ഓട്ടോക്കാരന്\nഇൻക്യുബേഷനോ?\nഅത് എഞ്ചിനീയർമാർക്ക്\"", [
 ("A","wide","ഷാജീ, പതിനഞ്ച് കൊല്ലം ഓട്ടോ ഓടിച്ചു. ഇപ്പോ സ്റ്റാൻഡിലെ ഓട്ടം ബുക്ക് ചെയ്യാൻ ഒരു ആപ്പ് ഉണ്ടാക്കി. പ്രോട്ടോടൈപ്പ് റെഡി."),
 ("V","V","സജീ, എന്നാ KSUM ഇൻക്യുബേഷന് പോ. അവിടെ മെന്റർമാരുണ്ട്."),
 ("A","A","അത് എഞ്ചിനീയർമാരുടെ സ്ഥലമല്ലേ? എനിക്ക് ഡിഗ്രിയും ഇല്ല, ID-യും ഇല്ല."),
 ("V","wide","KSUM ഇൻക്യുബേഷൻ യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പിനാ. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത്, KSUM പോർട്ടലിൽ ID-ക്ക് അപേക്ഷിക്കാം."),
 ("A","A","അപ്പോ ബാഡ്ജ് അല്ല, ID ആണ് ചോദ്യം."),
 ("V","wide","മീറ്റർ നീ ഇട്ടു. ഇനി ID ഇട്.")],
 "മീറ്റർ നീ ഇട്ടു,\nഇനി ID ഇട്", CTA_KSUM, theme="crm",
 cap_ml="പതിനഞ്ച് കൊല്ലം ഓട്ടോ ഓടിച്ചയാൾ സ്റ്റാൻഡിലെ ഓട്ടം ബുക്ക് ചെയ്യാൻ ആപ്പ് ഉണ്ടാക്കി, പക്ഷേ ഇൻക്യുബേഷൻ എഞ്ചിനീയർമാർക്കാണെന്ന് കരുതി. KSUM ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്; കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത്, KSUM പോർട്ടലിൽ ID-ക്ക് അപേക്ഷിക്കാം. നിങ്ങളുടെ പ്രോട്ടോടൈപ്പ് റെഡിയാണോ?",
 cap_en="An autorickshaw driver of fifteen years built an app to book rides from his stand, but thought incubation was only for engineers. KSUM's incubation and programmes are for startups that hold the Unique ID: register the startup in Kerala and apply for the ID on KSUM's startup portal. Is your prototype ready?",
 cap_mg="Pathinanchu kollam auto odichayaal stand-ile ottam book cheyyaan app undaakki, pakshe incubation engineer-markkaanennu karuthi. KSUM incubation-um programmes-um Unique ID ulla startup-ukalkkaanu; Kerala-yil register cheythu, KSUM portal-il ID-kku apekshikkaam. Ningalude prototype ready aano?")

duo("md057", "kerala_registered", "A", "hotellobby", "\"അടുത്ത കോളിൽ\nആദ്യ മണിക്കൂറിൽ\nഅപേക്ഷിച്ചാൽ ജയിക്കും\"", [
 ("A","wide","ജെയ്സണേ, ഹോട്ടൽ മുറിയിൽ ആളില്ലെങ്കിൽ AC ഓഫാക്കുന്ന നമ്മുടെ സെൻസർ. കഴിഞ്ഞ KSUM കോൾ നമ്മൾ കണ്ടതേയില്ല."),
 ("V","V","നീതൂ, അടുത്ത കോൾ തുറന്നാൽ ആദ്യ മണിക്കൂറിൽ അപേക്ഷിക്കാം. നേരത്തെ വരുന്നവർക്കല്ലേ കിട്ടുക?"),
 ("A","A","അതിന് നമുക്ക് യുണീക്ക് ID പോലും ഇല്ലല്ലോ."),
 ("V","wide","അപ്പോ ആദ്യം ID. പിന്നെ, കോളുകളും നിബന്ധനകളും മാറും, സെലക്ഷൻ ആർക്കും ഉറപ്പില്ല. സമയമല്ല, തയ്യാറെടുപ്പാ നോക്കുന്നത്."),
 ("A","A","അപ്പോ അലാറം അല്ല, ഫയൽ റെഡിയാക്കണം."),
 ("V","wide","ആദ്യം എത്തിയാൽ പോരാ. റെഡിയായി എത്തണം.")],
 "ആദ്യം എത്തിയാൽ പോരാ,\nറെഡിയായി എത്തണം", CTA_GRANT, theme="crm",
 cap_ml="ഹോട്ടൽ മുറികളിലെ AC സെൻസർ ഉണ്ടാക്കുന്ന കേരള കമ്പനി കഴിഞ്ഞ KSUM കോൾ കണ്ടില്ല; അടുത്തതിൽ ആദ്യ മണിക്കൂറിൽ അപേക്ഷിച്ചാൽ മതിയെന്ന് കരുതി. ആദ്യം യുണീക്ക് ID വേണം; കോളുകളും നിബന്ധനകളും മാറും, സെലക്ഷൻ ആർക്കും ഉറപ്പില്ല. നിങ്ങളുടെ ഫയൽ റെഡിയാണോ?",
 cap_en="A Kerala company making room AC sensors for hotels missed the last KSUM call and planned to apply in the first hour of the next one. First comes the Unique ID; calls and conditions change and selection is never guaranteed, so preparation matters more than timing. Is your file ready?",
 cap_mg="Hotel murikalile AC sensor undaakkunna Kerala company kazhinja KSUM call kandilla; aduthathil aadya manikkooril apekshichaal mathiyennu karuthi. Aadyam Unique ID venam; calls-um nibandhanakalum maarum, selection aarkkum urappilla. Ningalude file ready aano?")
