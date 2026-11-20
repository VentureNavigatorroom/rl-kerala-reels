# GST batch 06 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd035", "service_pro", "A", "teashop", "പന്തൽ ബുക്കിംഗ്\n26 ലക്ഷം.\n\"ലിമിറ്റ് 40 അല്ലേ?\"", [
 ("A","wide","വിഷ്ണൂ, ഈ ഉത്സവ സീസണിൽ നിങ്ങളുടെ പന്തൽ-സ്റ്റേജ് ടീമിന് എത്ര ബുക്കിംഗ് വന്നു?"),
 ("V","V","അനൂ, 26 ലക്ഷം ആയി. GST ലിമിറ്റ് 40 ലക്ഷം അല്ലേ, ഇനിയും സമയം ഉണ്ട്."),
 ("A","A","40 ലക്ഷം സാധനം വിൽക്കുന്നവർക്കാ. നിങ്ങൾ ചെയ്യുന്നത് പന്തൽ കെട്ടൽ, അതായത് സർവീസ്."),
 ("V","wide","സർവീസിന് എത്രയാ?"),
 ("A","wide","കേരളത്തിൽ സർവീസിന് 20 ലക്ഷം. അത് കടന്നിട്ടും രജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ ടാക്സ്, 18% പലിശ, പിന്നെ പിഴയും."),
 ("V","V","കാൽ തെറ്റിയാൽ പന്തൽ വീഴും, ലിമിറ്റ് തെറ്റിയാൽ ലാഭം വീഴും.")],
 "കാൽ തെറ്റിയാൽ പന്തൽ,\nലിമിറ്റ് തെറ്റിയാൽ ലാഭം", CTA_LIMIT, theme="crm",
 cap_ml="26 ലക്ഷം ബുക്കിംഗ് ആയ ഉത്സവ പന്തൽ ടീം കരുതി GST ലിമിറ്റ് 40 ലക്ഷം ആണെന്ന്. കേരളത്തിൽ 40 ലക്ഷം സാധനങ്ങൾക്കാണ്; സർവീസിന് 20 ലക്ഷം. കടന്നിട്ടും രജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ ടാക്സ്, 18% പലിശ, പിഴ. നിങ്ങളുടേത് സാധനമോ സർവീസോ?",
 cap_en="A festival pandal and stage team with 26 lakh in bookings thought the GST limit was 40 lakh. In Kerala 40 lakh is for goods; for services it is 20 lakh. Cross it without registering and you pay the tax, 18% interest and a penalty. Goods or services: which is yours?",
 cap_mg="26 lakh booking aaya utsava panthal team karuthi GST limit 40 lakh aanennu. Kerala-il 40 lakh saadhanangalkkaanu; service-nu 20 lakh. Kadannittum register cheythillenkil tax, 18% palisha, pizha. Ningaludethu saadhanamo service-o?")

duo("gd036", "trader", "B", "fishmarket", "ഹോട്ടൽ ചെയിൻ ഓർഡർ.\nGST അപേക്ഷ നിന്നു:\nOTP പഴയ സിമ്മിൽ", [
 ("A","wide","ആന്റണീ, ഹോട്ടലുകാർക്ക് ചെമ്മീൻ ചമ്മന്തിപ്പൊടിക്ക് GST ബില്ല് വേണം എന്നല്ലേ പറഞ്ഞത്? അപേക്ഷ എന്തായി?"),
 ("V","V","സുമേ, പകുതിക്ക് നിന്നു. OTP പോയത് ആധാറിൽ കൊടുത്ത പഴയ നമ്പറിലേക്ക്. ആ സിം പണ്ടേ കളഞ്ഞു."),
 ("A","A","അപ്പോ ആദ്യം ആധാറിലെ മൊബൈൽ നമ്പർ ശരിയാക്കണം."),
 ("V","wide","അത് ശരിയായാൽ പിന്നെ എത്ര ദിവസം?"),
 ("A","wide","GST-യുടെ OTP ആധാറുമായി ലിങ്ക് ചെയ്ത നമ്പറിലേ വരൂ. ലോ-റിസ്ക് അപേക്ഷ 3 പ്രവൃത്തി ദിവസത്തിൽ ഓട്ടോ-അപ്രൂവ് ആകും."),
 ("V","V","പഴയ സിം കളഞ്ഞാലും ആധാർ അത് ഓർത്തിരിക്കും.")],
 "പഴയ സിം കളഞ്ഞാലും\nആധാർ മറക്കില്ല", CTA_GST, theme="crm",
 cap_ml="ഹോട്ടൽ ചെയിനിന്റെ ഓർഡറിന് GST ബില്ല് വേണം, പക്ഷേ അപേക്ഷയുടെ OTP പോയത് ആധാറിലെ പഴയ നമ്പറിലേക്ക്. GST OTP ആധാറുമായി ലിങ്ക് ചെയ്ത മൊബൈലിലേ വരൂ; ലോ-റിസ്ക് അപേക്ഷ 3 പ്രവൃത്തി ദിവസത്തിൽ അപ്രൂവ് ആകും. നിങ്ങളുടെ ആധാറിലെ നമ്പർ ഇപ്പോഴും നിങ്ങളുടെ കയ്യിലുണ്ടോ?",
 cap_en="A hotel chain wants a GST bill for a dried-prawn chutney powder order, but the application stalls: the OTP went to the old number linked to Aadhaar. The GST OTP only goes to the Aadhaar-linked mobile; low-risk applications are auto-approved within 3 working days. Is your Aadhaar number still in your hand?",
 cap_mg="Hotel chain-nte order-nu GST bill venam, pakshe application-nte OTP poyathu Aadhaar-ile pazhaya number-ilekku. GST OTP Aadhaar-umaayi link cheytha mobile-ile varoo; low-risk application 3 working days-il approve aakum. Ningalude Aadhaar-ile number ippozhum kayyil undo?")

duo("gd037", "online_seller", "A", "gym", "ബെംഗളൂരു ജിം ചെയിൻ:\n\"500 ടീ-ഷർട്ട് വേണം\"\nGST ഇല്ല", [
 ("A","wide","ജസ്റ്റിനേ, നമ്മുടെ ജിം-വെയർ പേജിന് രണ്ട് മെസേജ്. ബെംഗളൂരുവിലെ ജിം ചെയിനും സിംഗപ്പൂരിലെ ഒരു ഷോപ്പും."),
 ("V","V","റിയേ, ആദ്യം സിംഗപ്പൂർ. ബെംഗളൂരു ഇന്ത്യ തന്നെയല്ലേ, അതിന് ഒന്നും വേണ്ട."),
 ("A","A","ഇൻസ്റ്റഗ്രാമിൽ ഇതുവരെ കേരളത്തിനകത്ത് മാത്രമേ വിറ്റിട്ടുള്ളൂ."),
 ("V","wide","അപ്പോ ബെംഗളൂരുവിന് എന്താ പ്രശ്നം?"),
 ("A","wide","മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം അയച്ചാൽ ടേൺഓവർ എത്രയായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം. സിംഗപ്പൂരിന് അതിനു പുറമെ IEC-യും."),
 ("V","V","അതിർത്തി കടക്കുന്നത് കടൽ കടക്കുമ്പോൾ മാത്രമല്ല.")],
 "അതിർത്തി കടക്കാൻ\nകടൽ വേണ്ട", CTA_GST, theme="crm",
 cap_ml="ഇൻസ്റ്റഗ്രാം ജിം-വെയർ ബ്രാൻഡിന് ബെംഗളൂരുവിലെ ജിം ചെയിനിൽ നിന്നും സിംഗപ്പൂരിലെ ഷോപ്പിൽ നിന്നും ഓർഡർ. മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിറ്റാൽ ടേൺഓവർ എത്രയായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം; എക്സ്പോർട്ടിന് IEC-യും. നിങ്ങളുടെ ഓർഡറുകൾ ഏതൊക്കെ സംസ്ഥാനത്തു നിന്നാ?",
 cap_en="An Instagram gym-wear brand gets orders from a Bengaluru gym chain and a Singapore shop, and plans to sort out only the export. Selling goods to another state needs GST from the first sale, whatever the turnover; exporting also needs an IEC. Which states do your orders come from?",
 cap_mg="Instagram gym-wear brand-nu Bengaluru-ile gym chain-il ninnum Singapore-ile shop-il ninnum order. Mattoru samsthaanathekku saadhanam vittaal turnover ethrayaayaalum aadya vilpana muthal GST venam; export-nu IEC-um. Ningalude orders ethokke samsthaanathu ninnaa?")

duo("gd038", "trader", "B", "petrolpump", "ഐസ് പ്ലാന്റ് വലുതാക്കാൻ\nലോൺ. ബാങ്ക്:\n\"GST റിട്ടേൺ കാണിക്കൂ\"", [
 ("A","wide","ഷിബൂ, ബോട്ടുകാർക്ക് ഐസ് കൊടുക്കുന്ന പ്ലാന്റ് വലുതാക്കാൻ ലോൺ ചോദിച്ചു. ബാങ്ക് GST റിട്ടേൺ ചോദിക്കുന്നു."),
 ("V","V","സന്തോഷേ, നിനക്ക് GST ഇല്ലല്ലോ. കഴിഞ്ഞ വർഷം വിറ്റത് എത്രയാ?"),
 ("A","A","ട്രോളിംഗ് സീസൺ കഴിഞ്ഞപ്പോ 48 ലക്ഷം. നോക്കാൻ സമയം കിട്ടിയില്ല."),
 ("V","wide","സാധനത്തിന് ലിമിറ്റ് 40 ലക്ഷം. രജിസ്റ്റർ ചെയ്യാതിരുന്നാൽ ടാക്സ്, 18% പലിശ, 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ, അത് പിഴ."),
 ("A","A","ലോണിന് മുമ്പ് ആദ്യം രജിസ്ട്രേഷൻ."),
 ("V","V","ഐസ് ഉരുകും, പിഴ ഉരുകില്ല.")],
 "ഐസ് ഉരുകും,\nപിഴ ഉരുകില്ല", CTA_PENALTY, theme="crm",
 cap_ml="ബോട്ടുകൾക്ക് ഐസ് കൊടുക്കുന്ന പ്ലാന്റ് വലുതാക്കാൻ ലോൺ ചോദിച്ചപ്പോൾ ബാങ്ക് ചോദിച്ചത് GST റിട്ടേൺ. വിൽപ്പന 48 ലക്ഷം, രജിസ്ട്രേഷൻ ഇല്ല. സാധനങ്ങൾക്ക് ലിമിറ്റ് 40 ലക്ഷം; വൈകിയാൽ ടാക്സ്, 18% പലിശ, 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10% പിഴ. നിങ്ങളുടെ കഴിഞ്ഞ വർഷത്തെ ടേൺഓവർ നോക്കിയോ?",
 cap_en="An ice plant supplying fishing boats asks for a loan to expand, and the bank wants GST returns. Sales hit 48 lakh, with no registration. The goods limit is 40 lakh; registering late means the tax, 18% interest and a penalty of 10,000 rupees or 10% of the tax, whichever is higher. Have you checked last year's turnover?",
 cap_mg="Boat-ukalkku ice kodukkunna plant valuthaakkaan loan chodichappol bank chodichathu GST return. Vilpana 48 lakh, registration illa. Saadhanangalkku limit 40 lakh; vaikiyaal tax, 18% palisha, 10,000 allenkil tax-nte 10% pizha. Kazhinja varshathe turnover nokkiyo?")

duo("gd039", "service_pro", "A", "library", "\"കോമ്പോസിഷൻ\nപലചരക്ക് കടയ്ക്ക്\nമാത്രം അല്ലേ?\"", [
 ("A","wide","അനൂപേ, മൈലാഞ്ചി ടീമിന്റെ ബുക്കിംഗ് 28 ലക്ഷം ആയി. GST എടുക്കണം, പക്ഷേ കണക്ക് നോക്കാൻ പേടി."),
 ("V","V","ഗ്രീഷ്മേ, കോമ്പോസിഷൻ സ്കീം നോക്കിയോ? അതിൽ കാര്യങ്ങൾ ലളിതമാ."),
 ("A","A","അത് പലചരക്ക് കടക്കാർക്ക് മാത്രം ഉള്ളതല്ലേ? ഞങ്ങൾ കൈയിൽ ഡിസൈൻ വരയ്ക്കുന്നവരാ."),
 ("V","wide","അല്ല. സാധനങ്ങൾക്ക് 1.5 കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ ഉള്ളവർക്ക് കോമ്പോസിഷൻ നോക്കാം."),
 ("A","A","അപ്പോ 28 ലക്ഷം ഉള്ള ഞങ്ങൾക്കും വഴിയുണ്ട്."),
 ("V","V","മൈലാഞ്ചി കൈയിൽ, കോമ്പോസിഷൻ കണക്കിൽ.")],
 "മൈലാഞ്ചി കൈയിൽ,\nകോമ്പോസിഷൻ കണക്കിൽ", CTA_LIMIT, theme="faq",
 cap_ml="GST കോമ്പോസിഷൻ സ്കീം കടകൾക്ക് മാത്രമാണോ? അല്ല. സാധനങ്ങൾക്ക് 1.5 കോടി വരെയും സർവീസിന് 50 ലക്ഷം വരെയും ടേൺഓവർ ഉള്ളവർക്ക് കോമ്പോസിഷൻ നോക്കാം. 28 ലക്ഷം ബുക്കിംഗ് ഉള്ള മൈലാഞ്ചി ടീമിനും. നിങ്ങൾ കോമ്പോസിഷൻ നോക്കിയിട്ടുണ്ടോ?",
 cap_en="Is the GST composition scheme only for grocery shops? No. Businesses with turnover up to 1.5 crore for goods or 50 lakh for services can look at composition, including a mehendi team with 28 lakh in bookings. Have you checked composition for your business?",
 cap_mg="GST composition scheme kadakalkku maathramaano? Alla. Saadhanangalkku 1.5 crore vareyum service-nu 50 lakh vareyum turnover ullavarkku composition nokkaam. 28 lakh booking ulla mylanchi team-num. Ningal composition nokkiyittundo?")

duo("gd040", "service_pro", "B", "classroom", "ഓൺലൈൻ സംഗീത ക്ലാസ്.\nകുട്ടികൾ പുണെയിലും\nഡൽഹിയിലും. GST?", [
 ("A","wide","ആദർശേ, എന്റെ ഓൺലൈൻ കർണാടക സംഗീത ക്ലാസിൽ ഇപ്പോ പുണെയിലും ഡൽഹിയിലും കുട്ടികൾ ഉണ്ട്."),
 ("V","V","നിമ്മീ, സൂക്ഷിക്കണം. ഓൺലൈൻ വിൽപ്പനക്കാർക്ക് മറ്റൊരു സംസ്ഥാനമായാൽ ആദ്യ ദിവസം മുതൽ GST എന്ന് കേട്ടിട്ടുണ്ട്."),
 ("A","A","വർഷം 9 ലക്ഷം വരുമാനമേ ഉള്ളൂ. അപ്പോഴും വേണോ?"),
 ("V","wide","ആ നിയമം സാധനങ്ങൾക്കാ. മറ്റ് സംസ്ഥാനങ്ങളിലേക്കുള്ള സർവീസിന് 20 ലക്ഷം വരെ ഇളവുണ്ട്. ആകെ വർഷത്തെ തുക നോക്കിയാൽ മതി."),
 ("A","A","അപ്പോ പാട്ട് പുണെയിലേക്ക് പോയാലും പേടി വേണ്ട."),
 ("V","V","സാധനം അതിർത്തി കടന്നാൽ GST, സ്വരം കടന്നാൽ ലിമിറ്റ്.")],
 "സാധനം കടന്നാൽ GST,\nസ്വരം കടന്നാൽ ലിമിറ്റ്", CTA_GST, theme="faq",
 cap_ml="ഓൺലൈൻ സംഗീത ക്ലാസിൽ മറ്റ് സംസ്ഥാനങ്ങളിലെ കുട്ടികൾ ഉണ്ടെങ്കിൽ ആദ്യ ദിവസം മുതൽ GST വേണോ? വേണ്ട. ആദ്യ വിൽപ്പന മുതലുള്ള നിയമം മറ്റ് സംസ്ഥാനങ്ങളിലേക്ക് വിൽക്കുന്ന സാധനങ്ങൾക്കാണ്; സർവീസിന് വർഷം 20 ലക്ഷം വരെ ഇളവുണ്ട്. നിങ്ങളുടെ ക്ലാസിൽ ഏതൊക്കെ സംസ്ഥാനക്കാർ?",
 cap_en="An online Carnatic music teacher with students in Pune and Delhi fears she needs GST from day one. No: the first-sale rule is for goods sold to other states; inter-state services stay exempt up to 20 lakh a year. Which states are your students from?",
 cap_mg="Online sangeetha class-il mattu samsthaanangalile kuttikal undenkil aadya divasam muthal GST veno? Venda. Aadya vilpana muthalulla niyamam mattu samsthaanangalilekku vilkkunna saadhanangalkkaanu; service-nu varsham 20 lakh vare ilavundu. Ningalude class-il ethokke samsthaanakkaar?")

duo("gd041", "new_company", "A", "metro", "\"പ്രൈവറ്റ് ലിമിറ്റഡ്\nആയാൽ GST\nനിർബന്ധം അല്ലേ?\"", [
 ("A","wide","കിരണേ, കമ്പനി സർട്ടിഫിക്കറ്റ് കിട്ടി. ഇനി GST നിർബന്ധം ആണെന്ന് എല്ലാരും പറയുന്നു."),
 ("V","V","അഞ്ജലീ, ആര് പറഞ്ഞു? നിന്റെ ആപ്പ് ഇതുവരെ ഒരു രൂപ പോലും സമ്പാദിച്ചിട്ടില്ലല്ലോ."),
 ("A","A","കമ്പനി ആയാൽ എല്ലാം വേണം എന്നാ കരുതിയത്."),
 ("V","wide","GST പേര് നോക്കിയല്ല, ടേൺഓവർ നോക്കിയാ. കേരളത്തിൽ സാധനത്തിന് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം. വേണമെങ്കിൽ സ്വമേധയാ എടുക്കാം."),
 ("A","A","അപ്പോ കമ്പനി ആയതുകൊണ്ട് മാത്രം GST വേണ്ട."),
 ("V","V","പേരിന്റെ കൂടെ Ltd വരും, GST വരില്ല.")],
 "പേരിനൊപ്പം Ltd വരും,\nGST വരില്ല", CTA_GST, theme="faq",
 cap_ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി തുടങ്ങിയാൽ GST നിർബന്ധമാണോ? അല്ല. GST നോക്കുന്നത് ടേൺഓവർ: കേരളത്തിൽ സാധനങ്ങൾക്ക് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം; മറ്റ് സംസ്ഥാനങ്ങളിലേക്ക് സാധനം വിറ്റാൽ ആദ്യ വിൽപ്പന മുതൽ. വേണമെങ്കിൽ സ്വമേധയാ എടുക്കാം. നിങ്ങളുടെ കമ്പനിക്ക് GST ഉണ്ടോ?",
 cap_en="Does a new private limited company need GST straight away? Not by itself. GST depends on turnover: in Kerala 40 lakh for goods and 20 lakh for services, or from the first sale when goods go to another state. You may still register voluntarily. Does your company have GST?",
 cap_mg="Private limited company thudangiyaal GST nirbandhamaano? Alla. GST nokkunnathu turnover: Kerala-il saadhanangalkku 40 lakh, service-nu 20 lakh; mattu samsthaanangalilekku saadhanam vittaal aadya vilpana muthal. Venamenkil swamedhayaa edukkaam. Ningalude company-kku GST undo?")

duo("gd042", "online_seller", "B", "balcony", "\"വീട്ടിലെ അഡ്രസ്സിൽ\nGST കിട്ടില്ല\"\nഅങ്ങനെ കേട്ടു", [
 ("A","wide","വിവേകേ, കേക്ക് ടോപ്പർ ബിസിനസിന് GST എടുക്കണം. പക്ഷേ വീട്ടിലെ അഡ്രസ്സിൽ കിട്ടില്ലെന്ന് കേട്ടു."),
 ("V","V","അമ്മൂ, വീട് നമ്മുടെ സ്വന്തം അല്ലേ? അതിന്റെ കരം അടച്ച രസീത് അലമാരയിൽ ഉണ്ട്."),
 ("A","A","അതുകൊണ്ട് പറ്റുമോ? ഞാൻ കട വാടകയ്ക്ക് എടുക്കണം എന്ന് കരുതി."),
 ("V","wide","സ്വന്തം സ്ഥലമാണെങ്കിൽ ബില്ലോ കരം രസീതോ മതി. വാടകയ്ക്കാണെങ്കിൽ വാടക കരാർ, ഉടമയുടെ NOC, ബില്ല്."),
 ("A","A","അപ്പോ കടമുറി അന്വേഷണം നിർത്താം."),
 ("V","V","കട തുടങ്ങാൻ ഷട്ടർ വേണ്ട, രസീത് മതി.")],
 "കട തുടങ്ങാൻ ഷട്ടർ വേണ്ട,\nരസീത് മതി", CTA_GST, theme="faq",
 cap_ml="വീട്ടിലെ അഡ്രസ്സിൽ GST രജിസ്ട്രേഷൻ കിട്ടില്ലേ? സ്വന്തം സ്ഥലമാണെങ്കിൽ ബില്ലോ കരം രസീതോ അഡ്രസ്സ് പ്രൂഫ് ആയി മതി; വാടകയ്ക്കാണെങ്കിൽ വാടക കരാർ, ഉടമയുടെ NOC, ബില്ല്. നിങ്ങളുടെ ബിസിനസ് വീട്ടിൽ നിന്നാണോ?",
 cap_en="Can you get GST registration at your home address? If the place is your own, a utility bill or property-tax receipt is the address proof; if it is rented, the rent agreement, the owner's NOC and a bill. Do you run your business from home?",
 cap_mg="Veettile address-il GST registration kittille? Swantham sthalamaanenkil bill-o karam receipt-o address proof aayi mathi; vaadakaykkaanenkil rent agreement, udamayude NOC, bill. Ningalude business veettil ninnaano?")

duo("gd043", "trader", "A", "thattukada", "തട്ടുകടയിലെ മസാല\nകോയമ്പത്തൂരിലേക്ക്.\n\"ചെറിയ കച്ചവടം അല്ലേ?\"", [
 ("A","wide","ബിജൂ, എന്റെ ഓംലെറ്റ് മസാല ഒരു ലോറി ഡ്രൈവർ കോയമ്പത്തൂരിലെ കടകളിൽ കൊടുക്കാമെന്ന് പറഞ്ഞു. മാസം 100 പാക്കറ്റ്."),
 ("V","V","സിജോ, കൊള്ളാം! ഇവിടെ കൗണ്ടറിൽ വിൽക്കുന്ന പോലെ തന്നെയല്ലേ, GST ഒന്നും വേണ്ടല്ലോ."),
 ("A","A","വർഷം 6 ലക്ഷം പോലും തികയില്ല. ചെറിയ കച്ചവടം."),
 ("V","wide","കോയമ്പത്തൂർ തമിഴ്നാടല്ലേ?"),
 ("A","wide","അതാ കാര്യം. മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിറ്റാൽ ടേൺഓവർ എത്ര ചെറുതായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം."),
 ("V","V","മസാലയ്ക്ക് എരിവ് പോരെങ്കിൽ കുഴപ്പമില്ല, GST പോരെങ്കിൽ കുഴപ്പമാ.")],
 "എരിവ് കുറഞ്ഞാൽ സഹിക്കാം,\nGST കുറഞ്ഞാൽ പറ്റില്ല", CTA_GST, theme="new",
 cap_ml="തട്ടുകടയിലെ ഓംലെറ്റ് മസാല പാക്കറ്റുകൾ കോയമ്പത്തൂരിലെ കടകളിലേക്ക്, വർഷം 6 ലക്ഷം പോലും ഇല്ല. പക്ഷേ മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിറ്റാൽ ടേൺഓവർ എത്രയായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം. നിങ്ങളുടെ സാധനം കേരളം കടക്കുന്നുണ്ടോ?",
 cap_en="A thattukada owner's omelette masala packs are heading to shops in Coimbatore, under 6 lakh a year. But selling goods to another state needs GST from the first sale, however small the turnover. Do your goods leave Kerala?",
 cap_mg="Thattukadayile omelette masala packet-ukal Coimbatore-ile kadakalilekku, varsham 6 lakh polum illa. Pakshe mattoru samsthaanathekku saadhanam vittaal turnover ethrayaayaalum aadya vilpana muthal GST venam. Ningalude saadhanam Keralam kadakkunnundo?")

duo("gd044", "trader", "B", "photocopy", "\"ഞാൻ കടക്കാരനാ,\nലിമിറ്റ് 40 ലക്ഷം\"\nവരുമാനം പ്രിന്റിംഗിൽ", [
 ("A","wide","ഉണ്ണീ, നിന്റെ DTP സെന്ററിന്റെ കണക്ക് നോക്കി. സ്റ്റേഷനറി 8 ലക്ഷം, പ്രിന്റിംഗും ഡിസൈനും 23 ലക്ഷം."),
 ("V","V","അശ്വതീ, ആകെ 31 ലക്ഷം. ഞാൻ കടക്കാരനല്ലേ, ലിമിറ്റ് 40 ലക്ഷം."),
 ("A","A","ബോർഡ് കടയുടേതാ, പക്ഷേ വരുമാനം കൂടുതലും പ്രിന്റിംഗിൽ നിന്നാ."),
 ("V","wide","അതിന് എന്താ വ്യത്യാസം?"),
 ("A","wide","പ്രിന്റിംഗും ഡിസൈനും സർവീസ് ആണ്. കേരളത്തിൽ സർവീസിന് 20 ലക്ഷം, സാധനത്തിന് 40 ലക്ഷം. ബോർഡ് നോക്കിയല്ല, ജോലി നോക്കിയാ ലിമിറ്റ്."),
 ("V","V","ഷോപ്പ് എന്ന് ബോർഡിൽ, സർവീസ് എന്ന് കണക്കിൽ.")],
 "ബോർഡിൽ ഷോപ്പ്,\nകണക്കിൽ സർവീസ്", CTA_LIMIT, theme="new",
 cap_ml="DTP സെന്റർ: സ്റ്റേഷനറി 8 ലക്ഷം, പ്രിന്റിംഗും ഡിസൈനും 23 ലക്ഷം. 'കടയല്ലേ, ലിമിറ്റ് 40 ലക്ഷം' എന്ന് കരുതി. കേരളത്തിൽ സാധനങ്ങൾക്ക് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം; നിങ്ങളുടെ വരുമാനം എവിടെ നിന്ന് എന്നതാണ് കാര്യം. നിങ്ങളുടെ വരുമാനം കൂടുതലും സാധനമോ സർവീസോ?",
 cap_en="A DTP centre sells 8 lakh of stationery and earns 23 lakh from printing and design, and the owner assumes the 40 lakh shop limit. In Kerala the GST limit is 40 lakh for goods but 20 lakh for services, so what you earn from matters more than the board. Mostly goods or services?",
 cap_mg="DTP centre: stationery 8 lakh, printing-um design-um 23 lakh. 'Kadayalle, limit 40 lakh' ennu karuthi. Kerala-il saadhanangalkku 40 lakh, service-nu 20 lakh; ningalude varumaanam evide ninnu ennathaanu kaaryam. Ningalude varumaanam kooduthalum saadhanamo service-o?")
