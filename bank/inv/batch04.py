# Investor batch 04 (20 Nov, month backlog). Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented).
# Facts only from topics.FACTS_INV. No amounts beyond statutory ones, no company values, no promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

# CRM #19 ("I'll talk to my partner and call back"), the money already came in: 60-day allotment clock
duo("vd019", "founder_raising", "A", "juiceshop", "\"പാർട്ണറോട് ചോദിച്ചിട്ട്\nഷെയർ തരാം\"\n70 ദിവസം കഴിഞ്ഞു", [
 ("A","wide","നൗഷാദ്ക്കാ, ആ ഡോക്ടർ ഇട്ട പൈസക്ക് ഷെയർ കൊടുത്തോ? 70 ദിവസമായി."),
 ("V","V","റസിയാ, പാർട്ണർ ഗൾഫിലാ. അവനോട് ചോദിച്ചിട്ട് ചെയ്യാമെന്ന് വെച്ചു."),
 ("A","A","പൈസ കിട്ടി 60 ദിവസത്തിനുള്ളിൽ ഷെയർ കൊടുക്കണം. അത് കഴിഞ്ഞു."),
 ("V","V","ഇനി എന്ത് ചെയ്യും?"),
 ("A","wide","അടുത്ത 15 ദിവസത്തിനുള്ളിൽ പണം തിരികെ കൊടുക്കണം. വൈകിയാൽ 12% പലിശയും."),
 ("V","V","ചോദിച്ച് നിന്നപ്പോൾ ക്ലോക്ക് ഓടി.")],
 "60 ദിവസത്തിൽ ഷെയർ,\nഇല്ലെങ്കിൽ തിരികെ", CTA_FUNDING, theme="crm",
 cap_ml="ഇൻവെസ്റ്ററുടെ പണം കിട്ടിയാൽ 60 ദിവസത്തിനുള്ളിൽ ഷെയർ നൽകണം. ഇല്ലെങ്കിൽ അടുത്ത 15 ദിവസത്തിനുള്ളിൽ പണം തിരികെ, വൈകിയാൽ 12% പലിശ. 'പാർട്ണറോട് ചോദിക്കാം' എന്ന് പറഞ്ഞ് എത്ര ദിവസം പോയി?",
 cap_en="Once investor money reaches the company, shares must be allotted within 60 days, or the money refunded within the next 15 days, else with 12% interest. Waiting to 'ask the partner' does not stop the clock. How many days has your money been waiting?",
 cap_mg="Investor-inte paisa kittiyaal 60 divasathinullil share kodukkanam. Illenkil adutha 15 divasathinullil thirike, vaikiyaal 12% palisha. Partner-inodu chodikkaam ennu paranju ethra divasam poyi?")

# CRM #13 + #18 (family money with no paper), d904 pattern: an uncle's cheque in a wedding envelope
duo("vd020", "family_money", "B", "weddinghall", "കല്യാണ കവറിൽ\nമാമന്റെ ചെക്ക്:\n\"സ്റ്റാർട്ടപ്പിന്, ഷെയർ പിന്നെ\"", [
 ("A","wide","ശരത്തേ, മാമന്റെ കവറിൽ ചെക്ക്! കടയുടെ അക്കൗണ്ടിൽ നിന്നാ. ഷെയർ പിന്നെ മതിയെന്ന്."),
 ("V","V","കാവ്യേ, നാളെ എന്റെ സേവിംഗ്സിൽ ഇടാം. എന്നിട്ട് കമ്പനിയിലേക്ക് മാറ്റാം."),
 ("A","A","അങ്ങനെ പാടില്ല. ഷെയറിനുള്ള പണം നിക്ഷേപകന്റെ സ്വന്തം അക്കൗണ്ടിൽ നിന്ന് വരണം."),
 ("V","V","എങ്ങോട്ട്?"),
 ("A","wide","കമ്പനിയുടെ വേറിട്ട ഒരു ബാങ്ക് അക്കൗണ്ടിലേക്ക്. മാമന്റെ സ്വന്തം പേരിൽ നിന്ന്."),
 ("V","V","സമ്മാനം കവറിൽ, നിക്ഷേപം രേഖയിൽ.")],
 "സ്വന്തം അക്കൗണ്ട് മുതൽ\nവേറിട്ട അക്കൗണ്ട് വരെ", CTA_INVEST, theme="crm",
 cap_ml="ബന്ധുവിന്റെ നിക്ഷേപമായാലും ഷെയറിനുള്ള പണം അദ്ദേഹത്തിന്റെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന് കമ്പനിയുടെ വേറിട്ട അക്കൗണ്ടിലേക്ക് വരണം. കടയുടെ അക്കൗണ്ടോ നിങ്ങളുടെ സേവിംഗ്സോ വഴി പാടില്ല. നിങ്ങളുടെ ആദ്യ നിക്ഷേപം ആരിൽ നിന്ന്?",
 cap_en="Even from family, money for shares must come from the investor's own bank account into a separate company bank account. Not via his shop's account, and not through your savings account. Who was your first investor: family or friend?",
 cap_mg="Bandhuvinte nikshepam aayaalum share-inulla paisa addehathinte swantham bank account-il ninnu company-yude separate account-ilekku varanam. Kadayude account-o ningalude savings-o vazhi paadilla. Ningalude aadya investor aara?")

# CRM #16 (Gulf Malayali investing in a relative's startup): repatriation vs non-repatriation
duo("vd021", "nri_investor", "C", "airport", "മസ്കറ്റിലേക്ക് മടങ്ങും മുമ്പ്:\n\"എന്റെ പൈസക്ക്\nRBI ഫയലിംഗ് വേണോ?\"", [
 ("A","wide","റഫീഖേ, അനിയന്റെ കമ്പനിയിൽ ഇടുന്ന പൈസക്ക് RBI-യിൽ എന്തെങ്കിലും ഫയൽ ചെയ്യണോ?"),
 ("V","V","ഷമീർക്കാ, അത് പണം പിന്നെ പുറത്തേക്ക് കൊണ്ടുപോകുമോ എന്നതിനെ ആശ്രയിച്ചിരിക്കും."),
 ("A","A","തിരിച്ച് ഗൾഫിലേക്ക് കൊണ്ടുപോകാനുള്ള രീതിയിൽ ആണെങ്കിൽ?"),
 ("V","wide","റിപാട്രിയേഷൻ ബേസിസ്. ന്യായമായ മൂല്യ റിപ്പോർട്ട് വേണം, ഷെയർ നൽകി 30 ദിവസത്തിൽ FC-GPR ഫയലിംഗ്."),
 ("A","A","നാട്ടിൽ തന്നെ നിർത്താനാണെങ്കിലോ?"),
 ("V","V","നോൺ-റിപാട്രിയേഷൻ: ആഭ്യന്തര നിക്ഷേപം പോലെ. FC-GPR ഇല്ല. ആദ്യം വഴി, പിന്നെ പണം.")],
 "പണം തിരിച്ചു പോകുമോ?\nഅതാണ് ആദ്യ ചോദ്യം", CTA_INVEST, theme="crm",
 cap_ml="NRI നിക്ഷേപം റിപാട്രിയേഷൻ ബേസിസിൽ ആണെങ്കിൽ ന്യായമായ മൂല്യ റിപ്പോർട്ടും 30 ദിവസത്തിനുള്ളിൽ FC-GPR ഫയലിംഗും വേണം. നോൺ-റിപാട്രിയേഷൻ ആണെങ്കിൽ ആഭ്യന്തര നിക്ഷേപം പോലെ, FC-GPR ഇല്ല. നിങ്ങളുടെ നിക്ഷേപകൻ ഏത് രാജ്യത്ത്?",
 cap_en="An NRI investing on a repatriation basis needs shares at not below fair value (valuation report) and FC-GPR reporting to RBI within 30 days of allotment. On a non-repatriation basis it is treated as domestic investment, with no FC-GPR. Which country is your investor in?",
 cap_mg="NRI investment repatriation basis-il aanenkil fair value report-um 30 divasathinullil FC-GPR filing-um venam. Non-repatriation aanenkil domestic investment pole, FC-GPR illa. Ningalude investor etha raajyathu?")

# CRM #15 (equity split without vesting), seen from the investor's side; d904 pattern: rubber-tapping robot
duo("vd022", "cofounder_split", "A", "rubber", "\"എന്റെ സ്വന്തം ഷെയറിനും\nവെസ്റ്റിംഗോ?\"\nടേം ഷീറ്റ് കണ്ട് ഞെട്ടി", [
 ("A","wide","തോമസേ, ടാപ്പിംഗ് റോബോട്ടിന് ഇൻവെസ്റ്റർ റെഡി. പക്ഷേ നമ്മുടെ ഷെയറിന് വെസ്റ്റിംഗ് വേണമെന്ന്!"),
 ("V","V","ജോയിച്ചാ, നമ്മൾ രണ്ടാളിൽ ഒരാൾ പകുതിക്ക് ഇറങ്ങിയാലോ? ഇൻവെസ്റ്റർ പേടിക്കുന്നത് അതാ."),
 ("A","A","അപ്പോ അത് വാക്കാൽ മതിയല്ലോ."),
 ("V","wide","പോരാ. ഫൗണ്ടർ വെസ്റ്റിംഗ് SHA-യിൽ എഴുതണം, ആർട്ടിക്കിൾസിലും ചേർക്കണം. എങ്കിലേ കമ്പനിക്ക് ബാധകം."),
 ("A","A","അപ്പോ ഇരിക്കുന്നവന് ഷെയർ, ഇറങ്ങുന്നവന് ഓർമ്മ."),
 ("V","V","പാൽ തുള്ളി തുള്ളിയായി, ഷെയർ മാസം മാസമായി.")],
 "വെസ്റ്റിംഗ് SHA-യിൽ,\nപിന്നെ ആർട്ടിക്കിൾസിൽ", CTA_TERMSHEET, theme="crm",
 cap_ml="ഫൗണ്ടർമാരുടെ ഷെയറിന് വെസ്റ്റിംഗ് ഇൻവെസ്റ്റർ ചോദിക്കുന്നത് ഒരാൾ പകുതിക്ക് ഇറങ്ങുന്ന അപകടം കാരണമാണ്. അത് SHA-യിൽ എഴുതി ആർട്ടിക്കിൾസിൽ ചേർത്താലേ കമ്പനിക്ക് ബാധകമാകൂ. നിങ്ങളുടെ ഷെയറിന് വെസ്റ്റിംഗ് ഉണ്ടോ? അതെ / ഇല്ല?",
 cap_en="Investors ask for founder vesting because a co-founder may leave halfway. It binds the company only when written into the shareholders' agreement and the Articles of Association. Do your shares vest: yes or no?",
 cap_mg="Founders-inte share-nu vesting investor chodikkunnathu oraal pakuthikku irangunna risk kaaranam aanu. Athu SHA-yil ezhuthi Articles-il cherthaale company-kku baadhakam. Ningalude share-nu vesting undo? Yes / No?")

# FAQ: "do I need a special resolution just to give shares to friends?"; d904 pattern: backwater ferry tours
duo("vd023", "angel", "B", "ferry", "3 കൂട്ടുകാർക്ക് ഷെയർ.\n\"ഒരു വാട്സ്ആപ്പ് മെസേജ്\nമതിയല്ലോ\"", [
 ("A","wide","ടോണീ, നമ്മുടെ ഫെറി ടൂറിൽ മൂന്ന് കൂട്ടുകാർ പണം ഇടാമെന്ന്. ഷെയർ കാര്യം വാട്സ്ആപ്പിൽ ഉറപ്പിച്ചു."),
 ("V","V","മീരേ, കൂട്ടുകാർക്കല്ലേ. പേപ്പർ എന്തിനാ?"),
 ("A","A","പുറത്തുള്ളവർക്ക് ഷെയർ നൽകുന്നത് പ്രൈവറ്റ് പ്ലേസ്മെന്റ് ആണ്. ആളുകൾ ആരായാലും."),
 ("V","V","അതിന് എന്തൊക്കെ വേണം?"),
 ("A","wide","സ്പെഷ്യൽ റെസല്യൂഷൻ, ഓരോരുത്തർക്കും PAS-4 ഓഫർ ലെറ്റർ, ഷെയർ നൽകി 15 ദിവസത്തിൽ PAS-3."),
 ("V","V","വള്ളം കയറാൻ ടിക്കറ്റ്, ഷെയർ കയറാൻ റെസല്യൂഷൻ.")],
 "കൂട്ടുകാർക്കും\nPAS-4 ഓഫർ ലെറ്റർ", CTA_INVEST, theme="faq",
 cap_ml="കൂട്ടുകാർക്ക് ഷെയർ നൽകുന്നതും പ്രൈവറ്റ് പ്ലേസ്മെന്റ് ആണ്: സ്പെഷ്യൽ റെസല്യൂഷൻ, PAS-4 ഓഫർ ലെറ്റർ, ഷെയർ നൽകി 15 ദിവസത്തിനുള്ളിൽ PAS-3. വാട്സ്ആപ്പ് മെസേജ് രേഖയല്ല. നിങ്ങളുടെ ആദ്യ നിക്ഷേപകർ കൂട്ടുകാരാണോ?",
 cap_en="Giving shares to friends is still a private placement: a special resolution, a PAS-4 offer letter to each investor, and PAS-3 within 15 days of allotment. A WhatsApp message is not a record. Are your first investors friends?",
 cap_mg="Koottukaarkku share kodukkunnathum private placement aanu: special resolution, PAS-4 offer letter, share koduthu 15 divasathinullil PAS-3. WhatsApp message rekha alla. Ningalude aadya investors koottukaar aano?")

# FAQ (wrong structure): a proprietorship tries to give an investor shares; d904 pattern: kasavu weaving unit
duo("vd024", "founder_raising", "C", "textile", "കസവ് യൂണിറ്റിൽ 20% ചോദിച്ചു.\n\"പ്രൊപ്രൈറ്റർഷിപ്പിൽ\nഎഴുതിക്കൊടുക്കാം\"", [
 ("A","wide","പ്രകാശേട്ടാ, ബാംഗ്ലൂരിലെ ഒരാൾ നമ്മുടെ കസവ് യൂണിറ്റിൽ 20% ഷെയർ ചോദിച്ചു."),
 ("V","V","രമ്യേ, നമ്മുടെ പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ. ഒരു പേപ്പറിൽ 20% എന്ന് എഴുതിക്കൊടുക്കാം."),
 ("A","A","പ്രൊപ്രൈറ്റർഷിപ്പിന് ഷെയറേ ഇല്ല. പാർട്ണർഷിപ്പിനും LLP-ക്കും ഷെയർ ഇറക്കാൻ പറ്റില്ല."),
 ("V","V","അപ്പോ ഇക്വിറ്റി ആര് എടുക്കും?"),
 ("A","wide","ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി തന്നെ വേണം."),
 ("V","V","നൂല് ശരിയല്ലെങ്കിൽ കസവ് നിൽക്കില്ല.")],
 "ഷെയർ വേണോ?\nആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്", CTA_FUNDING, theme="faq",
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പിനും പാർട്ണർഷിപ്പിനും LLP-ക്കും ഷെയർ ഇറക്കാൻ കഴിയില്ല. ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. ഒരു പേപ്പറിൽ '20%' എഴുതിയാൽ അത് ഷെയറാകില്ല. നിങ്ങളുടെ ബിസിനസ് ഏത് ഘടന?",
 cap_en="A proprietorship, partnership or LLP cannot issue shares. To take equity investment you need a private limited company. Writing '20%' on a paper does not create a share. What structure is your business today?",
 cap_mg="Proprietorship-num partnership-num LLP-kkum share irakkaan pattilla. Equity investment edukkaan private limited company venam. Oru paper-il 20% ezhuthiyaal athu share aakilla. Ningalude business etha structure?")

# FAQ: "what if the founders sell the company?" (tag-along); d904 pattern: retired couple, first angel cheque
duo("vd025", "angel", "A", "veranda", "\"അവർ കമ്പനി വിറ്റാൽ\nനമ്മുടെ ഷെയർ\nആര് വാങ്ങും?\"", [
 ("A","wide","ബാലേട്ടാ, പെൻഷൻ പണം അടുത്ത വീട്ടിലെ പയ്യന്റെ സ്റ്റാർട്ടപ്പിൽ ഇട്ടു. അവർ നാളെ കമ്പനി വിറ്റാലോ?"),
 ("V","V","ശാന്തേ, അവർ മാത്രം വിറ്റ് പോയാൽ നമ്മൾ പുതിയ ആളുടെ കൂടെ പെടും."),
 ("A","A","അത് തടയാൻ എന്തെങ്കിലും വഴി?"),
 ("V","wide","SHA-യിൽ ടാഗ്-അലോംഗ്: ഫൗണ്ടർമാർ വിൽക്കുമ്പോൾ നമുക്കും അതേ നിബന്ധനയിൽ കൂടെ വിൽക്കാം."),
 ("A","A","അത് SHA-യിൽ മാത്രം മതിയോ?"),
 ("V","V","ആർട്ടിക്കിൾസിലും വേണം. അവർ വിറ്റാൽ, നമ്മളും കൂടെ.")],
 "അവർ വിറ്റാൽ\nനമ്മളും കൂടെ", CTA_TERMSHEET, theme="faq",
 cap_ml="ചെറിയ നിക്ഷേപകനെ സംരക്ഷിക്കുന്ന ഒരു SHA വ്യവസ്ഥയാണ് ടാഗ്-അലോംഗ്: ഫൗണ്ടർമാർ ഷെയർ വിൽക്കുമ്പോൾ നിങ്ങൾക്കും കൂടെ വിൽക്കാം. ആർട്ടിക്കിൾസിൽ എഴുതിയാലേ കമ്പനിക്ക് ബാധകം. നിങ്ങളുടെ SHA-യിൽ ടാഗ്-അലോംഗ് ഉണ്ടോ?",
 cap_en="Tag-along is a shareholders' agreement right that protects a small investor: when the founders sell, you can sell alongside. It binds the company only if written into the Articles of Association. Does your SHA have tag-along?",
 cap_mg="Cheriya investor-e samrakshikkunna oru SHA right aanu tag-along: founders share vilkkumpol ningalkkum koode vilkkaam. Articles-il ezhuthiyaale company-kku baadhakam. Ningalude SHA-yil tag-along undo?")

# FAQ: "the term sheet is non-binding, so can I talk to a better investor?" (no-shop); d904 pattern: dried-fish brand
duo("vd026", "founder_raising", "B", "fishmarket", "ടേം ഷീറ്റ് ഒപ്പിട്ട് 1 ആഴ്ച.\nവേറെ ഇൻവെസ്റ്റർ വിളിച്ചു:\n\"ഇരട്ടി തരാം\"", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, ഉണക്കമീൻ ബ്രാൻഡിന് വേറൊരു ഇൻവെസ്റ്റർ വിളിച്ചു. ഇരട്ടി തരാമെന്ന്!"),
 ("V","V","സുമേ, കഴിഞ്ഞ ആഴ്ച ഒരു ടേം ഷീറ്റ് ഒപ്പിട്ടതല്ലേ?"),
 ("A","A","അത് നോൺ-ബൈൻഡിംഗ് അല്ലേ. എനിക്ക് ആരോടും സംസാരിക്കാം."),
 ("V","wide","മിക്കതും ബൈൻഡിംഗ് അല്ല. പക്ഷേ എക്സ്ക്ലൂസിവിറ്റി, നോ-ഷോപ്പ്, ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം."),
 ("A","A","അപ്പോ ആ സമയം കഴിയും വരെ മിണ്ടരുത്."),
 ("V","V","മീൻ ഉണങ്ങും മുമ്പ് വിൽക്കരുത്, ഷീറ്റ് ഒപ്പിട്ടാൽ ഓടരുത്.")],
 "നോ-ഷോപ്പ് ഒപ്പിട്ട\nദിവസം മുതൽ", CTA_TERMSHEET, theme="faq",
 cap_ml="ടേം ഷീറ്റ് മിക്കവാറും ബൈൻഡിംഗ് അല്ല, പക്ഷേ എക്സ്ക്ലൂസിവിറ്റി (നോ-ഷോപ്പ്) ഒപ്പിട്ട ദിവസം മുതൽ ബാധകമാണ്. ആ സമയത്ത് മറ്റൊരു ഇൻവെസ്റ്ററോട് സംസാരിക്കാൻ പറ്റില്ല. ഒപ്പിടും മുമ്പ് ആ കാലാവധി വായിച്ചോ?",
 cap_en="A term sheet is mostly non-binding, but exclusivity (no-shop) usually binds from the day you sign: during that period you cannot talk to another investor. Did you read the no-shop period before signing?",
 cap_mg="Term sheet mikkavaarum binding alla, pakshe exclusivity (no-shop) ozhippitta divasam muthal baadhakam. Aa samayathu vere investor-odu samsaarikkaan pattilla. Ozhippidum munpu aa kaalavadhi vaayicho?")

# New: the handshake myth at a homestay breakfast; the document order
duo("vd027", "angel", "C", "homestay", "പുട്ടും കടലയും കഴിഞ്ഞ്\nഗസ്റ്റ് കൈ തന്നു:\n\"ഞാൻ ഇൻവെസ്റ്റ് ചെയ്യാം\"", [
 ("A","wide","ജോമോനേ, ബെംഗളൂരുവിലെ ആ ഗസ്റ്റ് നമ്മുടെ ഹോംസ്റ്റേ ചെയിനിൽ നിക്ഷേപിക്കാമെന്ന്. കൈ തന്നു!"),
 ("V","V","ടീനേ, കൈ തന്നാൽ ഡീൽ ആയില്ലേ?"),
 ("A","A","കൈ തന്നത് തുടക്കം മാത്രം. രേഖകൾക്ക് ഒരു ക്രമമുണ്ട്."),
 ("V","V","എന്ത് ക്രമം?"),
 ("A","wide","ആദ്യം ടേം ഷീറ്റ്, പിന്നെ ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്, അവസാനം ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്."),
 ("V","V","ചെക്ക്-ഇൻ കൈകൊണ്ട്, ഡീൽ പേപ്പർകൊണ്ട്.")],
 "ടേം ഷീറ്റ്, SSA,\nപിന്നെ SHA", CTA_FUNDING, theme="new",
 cap_ml="ഒരു ഇൻവെസ്റ്റർ കൈ തന്നത് ഡീൽ അല്ല. രേഖകൾ ഈ ക്രമത്തിൽ: ടേം ഷീറ്റ്, ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ് (SSA), പിന്നെ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ് (SHA). നിങ്ങൾ ഇപ്പോൾ ഏത് ഘട്ടത്തിൽ?",
 cap_en="An investor's handshake is not a deal. The documents come in order: term sheet, then the share subscription agreement (SSA), then the shareholders' agreement (SHA). Which step are you at?",
 cap_mg="Oru investor kai thannathu deal alla. Rekhakal ee kramathil: term sheet, share subscription agreement (SSA), pinne shareholders agreement (SHA). Ningal ippol etha step-il?")

# New: the angel's side before a second tranche (chat)
chat("vc002", "angel", "A", "\"രണ്ടാം ഗഡു അയക്കും മുമ്പ്\nരണ്ട് പേപ്പർ കാണിക്ക്\"", ("ഹന്ന", "ഫഹദ്"), [
 (1,"ഹന്ന, രണ്ടാം ഗഡു റെഡിയാണ്. അയക്കും മുമ്പ് രണ്ട് കാര്യം കാണണം."),
 (0,"ഫഹദ്, എന്താ? ആദ്യ ഗഡുവിന് ഷെയർ തന്നല്ലോ."),
 (1,"ആ ഷെയറിന്റെ PAS-3 ഫയൽ ചെയ്തോ? 15 ദിവസത്തിനുള്ളിൽ വേണം. അതുവരെ പണം ഉപയോഗിക്കാൻ പാടില്ല."),
 (0,"ചെയ്തു. രണ്ടാമത്തേത്?"),
 (1,"എന്റെ ബോർഡ് സീറ്റ് ആർട്ടിക്കിൾസിൽ ചേർത്തോ? അല്ലെങ്കിൽ SHA കടലാസിൽ മാത്രം."),
 (0,"ഈ ആഴ്ച തന്നെ അയക്കാം. ഫയലിംഗ് ആദ്യം, ഗഡു പിന്നെ.")],
 "PAS-3 ഫയൽ ചെയ്തോ?\nആർട്ടിക്കിൾസ് മാറ്റിയോ?", CTA_INVEST, theme="new",
 cap_ml="നല്ല ഇൻവെസ്റ്റർ രണ്ടാം ഗഡുവിന് മുമ്പ് രണ്ട് കാര്യം നോക്കും: ഷെയർ നൽകി 15 ദിവസത്തിനുള്ളിൽ PAS-3 ഫയൽ ചെയ്തോ, ബോർഡ് സീറ്റ് പോലുള്ള അവകാശങ്ങൾ ആർട്ടിക്കിൾസിൽ ചേർത്തോ. നിങ്ങളുടെ ഫയലിംഗ് റെഡിയാണോ?",
 cap_en="A careful investor checks two things before the next tranche: was PAS-3 filed within 15 days of allotment, and are rights such as a board seat written into the Articles of Association. Are your filings ready?",
 cap_mg="Nalla investor randaam gaduvinu munpu randu kaaryam nokkum: share koduthu 15 divasathinullil PAS-3 file cheytho, board seat pole ulla rights Articles-il cherttho. Ningalude filing ready aano?")
