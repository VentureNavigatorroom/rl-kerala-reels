# nri batch 04 (28 Nov night): 3D duo reels. Facts only from topics.FACTS_NRI.
# Never promise a loan or subsidy; banks sanction the loan; never say when a subsidy is released; PMEGP: check the live guidelines.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA

# crm: a Saudi returnee who left school in class 7 plans a 15 lakh rubber-mat unit; PMEGP needs VIII pass for manufacturing above 10 lakh
duo("pvd010", "gulf_returnee", "B", "rubber", "15 ലക്ഷത്തിന്റെ\nറബ്ബർ മാറ്റ് യൂണിറ്റ്.\nഎട്ടാം ക്ലാസ് പാസായില്ല", [
 ("A","wide","തോമസേ, സൗദിയിൽ 14 കൊല്ലം. ഇനി നാട്ടിൽ 15 ലക്ഷത്തിന്റെ റബ്ബർ മാറ്റ് യൂണിറ്റ്, PMEGP വഴി. പക്ഷേ ഞാൻ ഏഴാം ക്ലാസിൽ നിർത്തിയതാ."),
 ("V","V","ജോയിച്ചേട്ടാ, നിർമ്മാണ യൂണിറ്റിന്റെ പ്രോജക്റ്റ് 10 ലക്ഷത്തിന് മുകളിലാണെങ്കിൽ PMEGP-യിൽ എട്ടാം ക്ലാസ് പാസ് വേണം."),
 ("A","A","അപ്പോ എന്റെ പ്ലാൻ അവിടെ തീർന്നോ?"),
 ("V","V","ഇല്ല. 10 ലക്ഷത്തിനുള്ളിൽ ഒരു ചെറിയ തുടക്കം ആലോചിക്കാം. ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കി ഉറപ്പാക്ക്. ലോൺ തീരുമാനം ബാങ്കിന്റേത്."),
 ("A","wide","സർട്ടിഫിക്കറ്റ് ചെറുതാണെങ്കിൽ, തുടക്കം ചെറുതാക്കാം.")],
 "നിർമ്മാണം 10 ലക്ഷം കടന്നാൽ\nഎട്ടാം ക്ലാസ് പാസ്", CTA_PRAVASI, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് വന്ന് PMEGP-യിൽ വലിയ നിർമ്മാണ യൂണിറ്റ് പ്ലാൻ ചെയ്യുന്നുണ്ടോ? 10 ലക്ഷത്തിന് മുകളിലുള്ള നിർമ്മാണ പ്രോജക്റ്റിന് (സർവീസിന് 5 ലക്ഷത്തിന് മുകളിൽ) എട്ടാം ക്ലാസ് പാസ് വേണം. ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കൂ, ലോൺ ബാങ്കിന്റെ തീരുമാനമാണ്. നിങ്ങളുടെ പ്രോജക്റ്റ് എത്രയുടേതാണ്?",
 cap_en="Back from the Gulf and planning a big PMEGP manufacturing unit? Manufacturing projects above 10 lakh (service above 5 lakh) need the applicant to have passed class VIII. Check the live guidelines; the bank decides the loan. What size is your project?",
 cap_mg="Gulf-il ninnu vannu PMEGP-yil valiya nirmaana unit plan cheyyunnundo? 10 lakh-inu mukalilulla nirmaana project-inu (service-inu 5 lakh-inu mukalil) ettaam class pass venam. Live guideline nokku, loan bank-inte theerumaanamaanu. Ningalude project ethrayudethaanu?")

# faq: a Kuwait returnee wants the PMEGP unit in his 17-year-old son's name; the applicant must be 18+
duo("pvd011", "family_business_nri", "B", "home", "\"യൂണിറ്റ് മോന്റെ\nപേരിൽ ആക്കാം\"\nമോന് 17 വയസ്സ്", [
 ("V","wide","സ്നേഹേ, കുവൈത്തിൽ നിന്ന് വന്ന സ്ഥിതിക്ക് PMEGP യൂണിറ്റ് മോന്റെ പേരിൽ എടുക്കാം. അവന്റെ ഭാവിക്ക് നല്ലതല്ലേ?"),
 ("A","A","അരുണേട്ടാ, അവന് 17 വയസ്സേ ആയിട്ടുള്ളൂ. PMEGP-യിൽ അപേക്ഷകന് 18 വയസ്സ് കഴിയണം."),
 ("V","V","അപ്പോ അടുത്ത വർഷം വരെ കാക്കണോ?"),
 ("A","A","ആരുടെ പേരിൽ, ആര് നടത്തും എന്ന് ഒന്നിച്ച് ആലോചിക്കാം. ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കി ഉറപ്പാക്ക്. ലോൺ തീരുമാനം ബാങ്കിന്റേത്."),
 ("V","wide","ഭാവി അവന്റേതാണ്, പക്ഷേ ഒപ്പിടാൻ 18 വേണം.")],
 "PMEGP അപേക്ഷകന്\n18 വയസ്സ് കഴിയണം", CTA_PRAVASI, theme="faq",
 cap_ml="PMEGP യൂണിറ്റ് മക്കളുടെ പേരിൽ എടുക്കാൻ പ്ലാനുണ്ടോ? അപേക്ഷകന് 18 വയസ്സ് കഴിയണം. ആര് നടത്തും എന്ന് ആദ്യം തീരുമാനിക്കൂ, ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കൂ. ലോൺ ബാങ്കിന്റെ തീരുമാനമാണ്. യൂണിറ്റ് ആരുടെ പേരിലാണ് പ്ലാൻ?",
 cap_en="Planning to put a PMEGP unit in your child's name? The applicant must be at least 18. Decide first who will actually run it and check the live guidelines; the bank decides the loan. Whose name is your unit planned in?",
 cap_mg="PMEGP unit makkalude peril edukkaan plan undo? Apekshakanu 18 vayassu kazhiyanam. Aaru nadathum ennu aadyam theerumaanikku, live guideline nokku. Loan bank-inte theerumaanamaanu. Unit aarude perilaanu plan?")

# faq: a Qatar gym trainer wants a 30 lakh gym fully under PMEGP; the subsidy cap for service / business projects is 20 lakh
duo("pvd012", "gulf_returnee", "B", "gym", "30 ലക്ഷത്തിന്റെ ജിം.\nമുഴുവനും PMEGP-യിൽ\nഎന്ന് സ്വപ്നം", [
 ("V","wide","റിയാ, ഖത്തറിൽ ട്രെയിനർ ആയിരുന്നു. ഇനി നാട്ടിൽ 30 ലക്ഷത്തിന്റെ ജിം. മുഴുവൻ PMEGP പ്രോജക്റ്റ് ആയി കൊടുക്കാം."),
 ("A","A","ജസ്റ്റിനേ, ജിം സർവീസ് ആണ്. PMEGP-യിൽ സർവീസ്, ബിസിനസ് പ്രോജക്റ്റിന് സബ്സിഡിക്കുള്ള പരമാവധി ചെലവ് 20 ലക്ഷം."),
 ("V","V","നിർമ്മാണ യൂണിറ്റ് ആണെങ്കിലോ?"),
 ("A","A","അതിന് 50 ലക്ഷം. ജിമ്മിന്റെ പ്ലാൻ ഒതുക്കണോ, ബാക്കി എവിടെ നിന്ന് എന്ന് എഴുതണോ എന്ന് നോക്ക്. ലോൺ ബാങ്കിന്റെ തീരുമാനം."),
 ("V","wide","ഭാരം പൊക്കും മുമ്പ് ഭാരം എത്ര എന്ന് നോക്കണം.")],
 "സർവീസിന് 20 ലക്ഷം,\nനിർമ്മാണത്തിന് 50 ലക്ഷം", CTA_NORKA, theme="faq",
 cap_ml="PMEGP-യിൽ എത്ര വലിയ പ്രോജക്റ്റ് വരെ സബ്സിഡി നോക്കാം? സർവീസ്, ബിസിനസ് പ്രോജക്റ്റിന് പരമാവധി ചെലവ് 20 ലക്ഷം, നിർമ്മാണത്തിന് 50 ലക്ഷം. അതിന് മുകളിലുള്ള ഭാഗം പ്ലാനിൽ വേറെ കാണിക്കണം. ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കൂ, ലോൺ ബാങ്കിന്റെ തീരുമാനം. നിങ്ങളുടേത് സർവീസോ നിർമ്മാണമോ?",
 cap_en="How big can a PMEGP project be for the subsidy? The maximum project cost is 20 lakh for business / service and 50 lakh for manufacturing; anything above has to be planned separately. Check the live guidelines; the bank decides the loan. Is yours service or manufacturing?",
 cap_mg="PMEGP-yil ethra valiya project vare subsidy nokkaam? Service, business project-inu paramaavadhi chelavu 20 lakh, nirmaanathinu 50 lakh. Athinu mukalilulla bhaagam plan-il vere kaanikkanam. Live guideline nokku, loan bank-inte theerumaanam. Ningaludethu service-o nirmaanamo?")

# faq: a general-category man in town heard "35% subsidy"; the share depends on category and urban / rural
duo("pvd013", "returnee_loan", "B", "fishmarket", "\"PMEGP-ൽ 35%\nസബ്സിഡി ഉറപ്പ്\"\nഎല്ലാവർക്കുമാണോ?", [
 ("V","wide","സുമേ, ടൗണിൽ ഒരു ഉണക്കമീൻ യൂണിറ്റ് തുടങ്ങണം. PMEGP-ൽ 35% സബ്സിഡി ഉണ്ടെന്ന് ഒരാൾ പറഞ്ഞു."),
 ("A","A","ആന്റണിച്ചേട്ടാ, 35% എല്ലാവർക്കുമല്ല. പ്രത്യേക വിഭാഗങ്ങൾക്ക് ഗ്രാമത്തിലാണ് 35%. നഗരത്തിൽ അവർക്ക് 25%."),
 ("V","V","ഞാൻ ജനറൽ വിഭാഗമാ, യൂണിറ്റ് ടൗണിലും."),
 ("A","A","എങ്കിൽ ജനറൽ വിഭാഗത്തിന് നഗരത്തിൽ 15%, ഗ്രാമത്തിൽ 25%. അതും ബാങ്ക് ലോൺ അനുവദിച്ചാൽ മാത്രം. ലൈവ് ഗൈഡ്‌ലൈൻ നോക്ക്."),
 ("V","wide","കേട്ട ശതമാനം അല്ല, എന്റെ ശതമാനം നോക്കണം.")],
 "വിഭാഗവും സ്ഥലവും\nനോക്കിയേ ശതമാനം", CTA_PRAVASI, theme="faq",
 cap_ml="PMEGP-ൽ 35% സബ്സിഡി എല്ലാവർക്കുമാണോ? അല്ല. ജനറൽ വിഭാഗം: നഗരം 15%, ഗ്രാമം 25%. സ്ത്രീകൾ ഉൾപ്പെടെ പ്രത്യേക വിഭാഗങ്ങൾ: നഗരം 25%, ഗ്രാമം 35%. ലോൺ ബാങ്ക് അനുവദിക്കണം, ലൈവ് ഗൈഡ്‌ലൈൻ നോക്കൂ. നിങ്ങളുടെ യൂണിറ്റ് നഗരത്തിലോ ഗ്രാമത്തിലോ?",
 cap_en="Is the PMEGP subsidy 35% for everyone? No. General category: 15% urban, 25% rural. Special categories, including women: 25% urban, 35% rural. The bank has to sanction the loan; check the live guidelines. Is your unit urban or rural?",
 cap_mg="PMEGP-il 35% subsidy ellaavarkkumaano? Alla. General vibhaagam: nagaram 15%, graamam 25%. Sthreekal ulppede prathyeka vibhaagangal: nagaram 25%, graamam 35%. Loan bank anuvadikkanam, live guideline nokku. Ningalude unit nagarathilo graamathilo?")

# faq: an Oman returnee wants only 50,000 for a juice cart from NORKA; NDPREM loans run from 1 lakh to 30 lakh
duo("pvd014", "gulf_returnee", "B", "busstop", "\"50,000 മതി.\nNORKA ലോൺ\nകിട്ടുമോ?\"", [
 ("A","wide","അഖിലേ, ഒമാനിൽ നിന്ന് വന്നിട്ട് മൂന്ന് മാസം. ഒരു ജ്യൂസ് വണ്ടിക്ക് 50,000 മതി. NORKA ലോൺ എടുക്കാം."),
 ("V","V","ജിബിനേ, NORKA NDPREM-ൽ ബാങ്ക് ലോൺ 1 ലക്ഷം മുതൽ 30 ലക്ഷം വരെയാണ്. 50,000 ആ പട്ടികയിൽ വരില്ല."),
 ("A","A","അപ്പോ ഒരു ലക്ഷം ചോദിച്ചാലോ? ബാക്കി കയ്യിൽ ഇരിക്കും."),
 ("V","V","ആവശ്യമില്ലാത്ത ലോൺ എടുക്കരുത്. 50,000-ന് എന്ത് വഴി എന്ന് ബാങ്കിനോട് ചോദിക്ക്. തീരുമാനം അവരുടേത്."),
 ("A","wide","ആവശ്യത്തിന് ലോൺ, ലോണിന് വേണ്ടി ആവശ്യം അല്ല.")],
 "NDPREM: 1 ലക്ഷം\nമുതൽ 30 ലക്ഷം വരെ", CTA_NORKA, theme="faq",
 cap_ml="ചെറിയ തുകയ്ക്ക് NORKA ലോൺ നോക്കുന്നുണ്ടോ? NDPREM-ൽ ബാങ്ക് ലോൺ 1 ലക്ഷം മുതൽ 30 ലക്ഷം വരെയാണ്. ആവശ്യമില്ലാത്ത തുക ലോൺ എടുക്കരുത്. ചെറിയ തുകയ്ക്കുള്ള വഴി ബാങ്കിനോട് ചോദിക്കൂ. നിങ്ങൾക്ക് എത്ര വേണം?",
 cap_en="Looking at a NORKA loan for a small amount? NDPREM bank loans run from 1 lakh to 30 lakh. Don't borrow more than you need; ask the bank what fits a smaller amount. How much do you need?",
 cap_mg="Cheriya thukaykku NORKA loan nokkunnundo? NDPREM-il bank loan 1 lakh muthal 30 lakh vare aanu. Aavashyamillaatha thuka loan edukkaruthu. Cheriya thukaykkulla vazhi bank-inodu chodikku. Ningalkku ethra venam?")

# crm: a Dubai uncle puts money into a cafe company a second time; every fresh issue of shares to a non-resident needs its own FC-GPR
duo("pvd015", "nri_investing", "B", "cafe", "ദുബായിലെ അങ്കിൾ\nരണ്ടാമതും പൈസ ഇട്ടു.\n\"റിപ്പോർട്ട് ഒരിക്കൽ മതി\"", [
 ("A","wide","റോഷാ, ദുബായിലെ അങ്കിൾ കഫേ കമ്പനിയിൽ രണ്ടാമതും പൈസ ഇട്ടു. പുതിയ ഷെയർ കൊടുത്തു. RBI റിപ്പോർട്ട് ആദ്യ തവണ ചെയ്തതാണല്ലോ."),
 ("V","V","ആൽവിനേ, അത് ആദ്യത്തെ ഷെയറിന്. NRI-ക്ക് പുതിയ ഷെയർ കൊടുക്കുന്ന ഓരോ തവണയും 30 ദിവസത്തിനകം FC-GPR വേണം."),
 ("A","A","ഷെയർ കൊടുത്തിട്ട് മൂന്നാഴ്ച ആയി!"),
 ("V","V","എങ്കിൽ ഇന്ന് തന്നെ പേപ്പറുകൾ എടുക്ക്. NRI ഷെയർ ഉള്ളിടത്തോളം ജൂലൈ 15-നകം FLA റിട്ടേണും മറക്കരുത്."),
 ("A","wide","പൈസ രണ്ടാമതും വന്നാൽ, റിപ്പോർട്ടും രണ്ടാമതും.")],
 "ഓരോ പുതിയ ഷെയറിനും\n30 ദിവസം, FC-GPR", CTA_PRAVASI, theme="crm",
 cap_ml="ഗൾഫിലെ ബന്ധു രണ്ടാമതും കമ്പനിയിൽ പൈസ ഇട്ടോ? NRI-ക്ക് പുതിയ ഷെയർ കൊടുക്കുന്ന ഓരോ തവണയും 30 ദിവസത്തിനകം FC-GPR ഫയൽ ചെയ്യണം. ഒരിക്കൽ ചെയ്തത് അടുത്ത തവണത്തേക്ക് മതിയാകില്ല. എല്ലാ വർഷവും ജൂലൈ 15-നകം FLA റിട്ടേണും. നിങ്ങളുടെ കമ്പനിയിൽ NRI ഷെയർ ഉടമ ഉണ്ടോ?",
 cap_en="A relative in the Gulf put money into your company a second time? Every fresh issue of shares to a non-resident needs its own FC-GPR within 30 days; the first filing doesn't cover the next. The FLA return is due by 15 July every year too. Does your company have an NRI shareholder?",
 cap_mg="Gulf-ile bandhu randaamathum company-il paisa itto? NRI-kku puthiya share kodukkunna oro thavanayum 30 divasathinakam FC-GPR file cheyyanam. Orikkal cheythathu adutha thavanathekku mathiyaakilla. Ellaa varshavum July 15-nakam FLA returnum. Ningalude company-il NRI share udama undo?")

# faq: a returnee went to a local finance firm for the NORKA loan; NDPREM loans come through partner banks
duo("pvd016", "returnee_loan", "B", "bank", "NORKA ലോണിന്\nനാട്ടിലെ ഫിനാൻസ്\nകമ്പനിയിൽ പോയി", [
 ("V","wide","ശ്രുതീ, NORKA ലോണിന് നാട്ടിലെ ഒരു ഫിനാൻസ് കമ്പനിയിൽ ചെന്നു. അവർ പറഞ്ഞു, ഇത് ഞങ്ങളുടെ പരിപാടി അല്ല എന്ന്."),
 ("A","A","മനോജേട്ടാ, NDPREM ലോൺ വരുന്നത് പാർട്ണർ ബാങ്കുകൾ വഴിയാണ്. ഏത് സ്ഥാപനത്തിലും കിട്ടില്ല."),
 ("V","V","അപ്പോ ആദ്യം ഏതൊക്കെ ബാങ്ക് എന്ന് അറിയണം."),
 ("A","A","അതെ. NORKA-യിൽ നിന്നോ ബാങ്കിൽ നിന്നോ ഉറപ്പാക്ക്. റിപ്പോർട്ടും വിദേശ ജോലിയുടെ രേഖയും വെക്ക്. ലോൺ ബാങ്കിന്റെ തീരുമാനം."),
 ("V","wide","ശരിയായ വാതിൽ മുട്ടിയാലേ ശരിയായ ഉത്തരം കിട്ടൂ.")],
 "NDPREM ലോൺ\nപാർട്ണർ ബാങ്ക് വഴി", CTA_NORKA, theme="faq",
 cap_ml="NORKA NDPREM ലോണിന് ഏത് ബാങ്കിൽ പോകണം? ലോൺ വരുന്നത് പാർട്ണർ ബാങ്കുകൾ വഴിയാണ്. ഏതൊക്കെ എന്ന് NORKA-യിൽ നിന്നോ ബാങ്കിൽ നിന്നോ ഉറപ്പാക്കൂ, പ്രോജക്റ്റ് റിപ്പോർട്ട് റെഡിയാക്കൂ. ലോൺ ബാങ്കിന്റെ തീരുമാനമാണ്. നിങ്ങൾ ഏത് ജില്ലയിലാണ്?",
 cap_en="Which bank do you go to for a NORKA NDPREM loan? The loans come through partner banks. Confirm which ones with NORKA or the bank and have your project report ready; the bank decides the loan. Which district are you in?",
 cap_mg="NORKA NDPREM loan-inu ethu bank-il pokanam? Loan varunnathu partner bank-ukal vazhiyaanu. Ethokke ennu NORKA-yil ninno bank-il ninno urappaakku, project report ready aakku. Loan bank-inte theerumaanamaanu. Ningal ethu jillayilaanu?")

# faq: a salon owner repaid a smaller Mudra loan and asks straight for Tarun Plus; Tarun Plus comes only after repaying a Tarun loan
duo("pvd017", "mudra_repeat", "B", "salon", "ചെറിയ മുദ്ര ലോൺ\nഅടച്ചുതീർത്തു.\nഇനി നേരെ 20 ലക്ഷം?", [
 ("A","wide","വിനീതേ, സലൂണിന്റെ ചെറിയ മുദ്ര ലോൺ മുഴുവൻ അടച്ചുതീർത്തു. രണ്ടാമത്തെ ബ്രാഞ്ചിന് ഇനി തരുൺ പ്ലസ് 20 ലക്ഷം ചോദിക്കാം."),
 ("V","V","സോണിയ ചേച്ചീ, അടച്ചുതീർത്തത് നല്ല കാര്യം. പക്ഷേ തരുൺ പ്ലസ് ഒരു തരുൺ ലോൺ എടുത്ത് തിരിച്ചടച്ചവർക്കാണ്."),
 ("A","A","എന്റേത് തരുൺ അല്ലായിരുന്നു. അതിലും ചെറിയ തുകയുടേത്."),
 ("V","V","എങ്കിൽ ഇപ്പോഴത്തെ അടുത്ത പടി ഏതാണെന്ന് ബാങ്കിനോട് ചോദിക്ക്. തിരിച്ചടവ് രേഖകൾ കയ്യിൽ വെക്ക്. തീരുമാനം ബാങ്കിന്റേത്."),
 ("A","wide","കോണി കയറുന്നത് ഓരോ പടിയായിട്ടാണ്, ചാടിയല്ല.")],
 "തരുൺ പ്ലസിന് മുമ്പ്\nതരുൺ അടച്ചുതീർക്കണം", CTA_PRAVASI, theme="faq",
 cap_ml="ഒരു ചെറിയ മുദ്ര ലോൺ അടച്ചുതീർത്തു, ഇനി നേരെ തരുൺ പ്ലസ്? മുദ്ര തരുൺ പ്ലസ് (20 ലക്ഷം) ഒരു തരുൺ ലോൺ തിരിച്ചടച്ചവർക്ക് മാത്രമാണ്. അടുത്ത പടി ഏതെന്ന് ബാങ്കിനോട് ചോദിക്കൂ, തിരിച്ചടവ് രേഖകൾ സൂക്ഷിക്കൂ. നിങ്ങളുടെ ഇപ്പോഴത്തെ ലോൺ ഏതാണ്?",
 cap_en="Repaid a small Mudra loan and want to go straight to Tarun Plus? Mudra Tarun Plus (20 lakh) is only for those who have repaid a Tarun loan. Ask the bank what your next step is and keep your repayment records. Which loan do you have now?",
 cap_mg="Oru cheriya Mudra loan adachutheerthu, ini nere Tarun Plus? Mudra Tarun Plus (20 lakh) oru Tarun loan thirichadachavarkku maathramaanu. Adutha padi ethennu bank-inodu chodikku, thirichadavu rekhakal sookshikku. Ningalude ippozhathe loan ethaanu?")
