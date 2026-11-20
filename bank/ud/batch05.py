# Udyam / MSME batch 05 (20 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_UD. Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

# CRM (Gulf returnee starting a small unit): waits a year "to show turnover" before Udyam, while the machine loan is needed now
duo("yd025", "loan_seeker", "A", "airport", "\"ആദ്യം ഒരു വർഷം\nനടത്തട്ടെ,\nഎന്നിട്ട് ഉദ്യം\"", [
 ("A","wide","റഫീഖേ, ഷാർജയിലെ ജോലി വിട്ടു. നാട്ടിൽ ചക്ക ചിപ്സ് യൂണിറ്റ്. ഉദ്യം ഒക്കെ ഒരു വർഷം ടേൺഓവർ കാണിച്ചിട്ട് മതിയല്ലോ."),
 ("V","V","ഷമീറേ, ഫ്രയറിന് ബാങ്ക് ലോൺ ഇപ്പോഴല്ലേ വേണ്ടത്?"),
 ("A","A","അതേ, അടുത്ത മാസം. പക്ഷേ ബിസിനസ് തുടങ്ങിയിട്ടല്ലേ ഉള്ളൂ."),
 ("V","wide","ഉദ്യം ഓൺലൈനാണ്, ആധാറും PAN-ഉം, സ്വയം സാക്ഷ്യം. മുൻഗണനാ വായ്പയ്ക്കും ഈടില്ലാത്ത ലോൺ സ്കീമിനും അത് സഹായിക്കും."),
 ("A","A","അപ്പോ ടേൺഓവർ വരാൻ കാത്തിരിക്കേണ്ട."),
 ("V","wide","ലോൺ ബാങ്ക് തീരുമാനിക്കും. പക്ഷേ ഉദ്യം വൈകിക്കേണ്ടത് നീയല്ല.")],
 "ചിപ്സ് പൊരിയും മുമ്പ്\nഉദ്യം റെഡി", CTA_UDYAM, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് മടങ്ങി ചക്ക ചിപ്സ് യൂണിറ്റ് തുടങ്ങുന്ന ഷമീർ കരുതിയത് ഉദ്യമിന് ഒരു വർഷത്തെ ടേൺഓവർ വേണമെന്നാണ്. ഉദ്യം ഓൺലൈനാണ്, ആധാറും PAN-ഉം സ്വയം സാക്ഷ്യവും. മുൻഗണനാ വായ്പയ്ക്കും CGTMSE സ്കീമിനും സഹായിക്കും, ലോൺ തീരുമാനിക്കുന്നത് ബാങ്ക്. നിങ്ങൾ നാട്ടിലേക്ക് മടങ്ങുകയാണോ?",
 cap_en="A Gulf returnee starting a jackfruit chips unit thought Udyam needs a year of turnover first. Udyam registration is online, Aadhaar-based, with PAN and a self-declaration, and it helps with priority sector lending and the CGTMSE collateral-free scheme; the bank still decides the loan. Coming back to Kerala to start: yes or no?",
 cap_mg="Gulf-il ninnu madangi chakka chips unit thudangunna Shameer karuthiyathu Udyam-inu oru varsham turnover venam ennaanu. Udyam online aanu, Aadhaar-um PAN-um self declaration-um. Priority lending-inum CGTMSE scheme-inum sahaayikkum, loan theerumaanikkunnathu bank. Ningal naattilekku madangukayaano?")

# FAQ F17 (service unit, buyer pays late) + myth "MSME means factories": bridal make-up artist and a wedding planner
duo("yd026", "service_unit", "B", "salon", "മേക്കപ്പ് 3 മണിക്കൂർ.\nപണം 3 മാസം.\n\"ഇത് ഫാക്ടറി അല്ലല്ലോ\"", [
 ("A","wide","വിനീതേ, 14 വധുക്കളെ ഒരുക്കി. പ്ലാനർ ഇപ്പോഴും പണം തന്നില്ല. എന്റേത് സർവീസ് അല്ലേ, MSME നിയമം ഫാക്ടറിക്കല്ലേ?"),
 ("V","V","സോണിയേ, നിന്റെ മേക്കപ്പ് സ്റ്റുഡിയോയ്ക്ക് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ട്, മൈക്രോ സർവീസ് യൂണിറ്റ് എന്നാ കിടക്കുന്നത്."),
 ("V","wide","എങ്കിൽ നിയമം നിനക്കും. എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിൽ പരമാവധി 45. പിന്നെ കൂട്ടുപലിശ."),
 ("A","A","അപ്പോ ബ്രഷും ഒരു മെഷീൻ തന്നെ."),
 ("V","wide","മുഖം മിനുങ്ങി, ഇനി ബില്ലും മിനുങ്ങട്ടെ.")],
 "മുഖം മിനുങ്ങി,\nഇനി ബില്ലും\nമിനുങ്ങട്ടെ", CTA_MSME, theme="faq",
 cap_ml="MSME നിയമം ഫാക്ടറികൾക്ക് മാത്രമാണോ? അല്ല. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റുകൾക്കും ബയർ എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസത്തിൽ, ഉണ്ടെങ്കിൽ പരമാവധി 45 ദിവസത്തിൽ പണം നൽകണം. അതിന് ശേഷം കൂട്ടുപലിശ. നിങ്ങളുടേത് സർവീസോ നിർമാണമോ?",
 cap_en="Is the MSME payment rule only for factories? No. Udyam-registered micro and small service units are covered too: the buyer must pay within 15 days without an agreement, or the agreed time up to 45 days, then compound interest applies. Your business: service or manufacturing?",
 cap_mg="MSME niyamam factory-kalkku maathramaano? Alla. Udyam ulla micro, small service unit-kalkkum buyer agreement illenkil 15 divasathil, undenkil maximum 45 divasathil panam nalkanam. Athinu shesham koottupalisha. Ningaludethu service-o manufacturing-o?")

# FAQ: the yearly "renew your Udyam" call; there is no renewal, only keeping details updated
duo("yd027", "manufacturer", "A", "metro", "എല്ലാ വർഷവും\nഒരു കോൾ: \"ഉദ്യം\nപുതുക്കാൻ സമയമായി\"", [
 ("A","wide","കിരണേ, വീണ്ടും ആ കോൾ. ഉദ്യം പുതുക്കിയില്ലെങ്കിൽ ക്യാൻസലാകും, ഡീറ്റെയിൽസ് അയക്കാൻ."),
 ("V","V","അഞ്ജലീ, നിന്റെ അച്ചാർ യൂണിറ്റിന്റെ ഉദ്യം എന്നാ എടുത്തത്?"),
 ("A","A","മൂന്ന് വർഷം മുമ്പ്. ഓരോ വർഷവും ഇവർ വിളിക്കും."),
 ("V","wide","ഉദ്യമിന് പുതുക്കൽ ഇല്ല. വിവരങ്ങൾ മാറിയാൽ നീ തന്നെ പോർട്ടലിൽ അപ്ഡേറ്റ് ചെയ്താൽ മതി."),
 ("A","A","അപ്പോ ആധാറും OTP-യും ചോദിക്കുന്നവർക്ക് ഒന്നും കൊടുക്കേണ്ട."),
 ("V","wide","പുതുക്കേണ്ടത് ഉദ്യമല്ല, ആ നമ്പർ ബ്ലോക്ക് ലിസ്റ്റാ.")],
 "പുതുക്കേണ്ടത്\nഉദ്യമല്ല, ആ കോൾ\nബ്ലോക്ക് ചെയ്യൂ", CTA_UDYAM, theme="faq",
 cap_ml="\"ഉദ്യം പുതുക്കാൻ സമയമായി\" എന്ന കോൾ വന്നോ? ഉദ്യം രജിസ്ട്രേഷന് പുതുക്കൽ ഇല്ല. ബിസിനസ് വിവരങ്ങൾ മാറിയാൽ പോർട്ടലിൽ സ്വയം അപ്ഡേറ്റ് ചെയ്താൽ മതി. ഈ കോൾ നിങ്ങൾക്കും വന്നിട്ടുണ്ടോ?",
 cap_en="Got a call saying your Udyam must be renewed? Udyam registration has no renewal; you only keep your details updated on the portal yourself when they change. Have you had this call too: yes or no?",
 cap_mg="'Udyam puthukkaan samayamaayi' enna call vanno? Udyam registration-inu renewal illa. Business details maariyaal portal-il swayam update cheythaal mathi. Ee call ningalkkum vannittundo?")

# FAQ: "Udyam means subsidy money" (it opens doors; never a promised subsidy)
duo("yd028", "loan_seeker", "B", "thattukada", "\"ഉദ്യം എടുത്താൽ\nസബ്സിഡി വരും\"\nകാത്തിരുന്നത് 8 മാസം", [
 ("A","wide","ബിജുവേ, ഉദ്യം എടുത്ത് 8 മാസമായി. പുട്ടുപൊടി മില്ലിന് സബ്സിഡി അക്കൗണ്ടിൽ വരും എന്നാ ആ ചേട്ടൻ പറഞ്ഞത്."),
 ("V","V","സിജോ, ഉദ്യം ഒരു രജിസ്ട്രേഷനാ. അത് പണം അയക്കുന്ന സ്കീമല്ല."),
 ("A","A","പിന്നെ എന്തിനാ എടുത്തത്?"),
 ("V","wide","മുൻഗണനാ വായ്പ, ഈടില്ലാത്ത ലോൺ സ്കീം, സർക്കാർ ടെൻഡറിൽ മുൻഗണന. ഇതിനൊക്കെ അപേക്ഷിക്കുമ്പോൾ അത് വാതിൽ തുറക്കും."),
 ("A","A","അപ്പോ അക്കൗണ്ട് നോക്കി ഇരുന്നിട്ട് കാര്യമില്ല."),
 ("V","wide","ഉദ്യം താക്കോലാണ്, ലോട്ടറിയല്ല.")],
 "ഉദ്യം താക്കോലാണ്,\nലോട്ടറിയല്ല", CTA_UDYAM, theme="faq",
 cap_ml="ഉദ്യം എടുത്താൽ സബ്സിഡി തനിയെ അക്കൗണ്ടിൽ വരുമോ? ഇല്ല. ഉദ്യം മുൻഗണനാ വായ്പയ്ക്കും CGTMSE ഈടില്ലാത്ത ലോൺ സ്കീമിനും സർക്കാർ ടെൻഡർ മുൻഗണനയ്ക്കും സഹായിക്കും; ഓരോന്നിനും അപേക്ഷിക്കണം, തീരുമാനം അവരുടേത്. നിങ്ങൾ ഇതുവരെ ഏതിന് അപേക്ഷിച്ചു?",
 cap_en="Does a subsidy land in your account once you get Udyam? No. Udyam helps when you apply for priority sector lending, the CGTMSE collateral-free loan scheme and government tender preferences; you still apply for each, and they decide. Which one have you applied for?",
 cap_mg="Udyam eduthaal subsidy thaniye account-il varumo? Illa. Udyam priority lending-inum CGTMSE collateral-free loan scheme-inum government tender preference-inum sahaayikkum; oronninum apekshikkanam, theerumaanam avarudethu. Ningal ithuvare ethinu apekshichu?")

# CRM (small business expanding): crossed 10 crore turnover, thinks the 45-day protection is gone; small units keep it
duo("yd029", "supplier_unpaid", "B", "handloom", "ടേൺഓവർ 10 കോടി\nകടന്നു. \"ഇനി 45\nദിവസം നമുക്കില്ല\"", [
 ("A","wide","കുമാറേട്ടാ, ഈ വർഷം 10 കോടി കടന്നു. ഇനി മൈക്രോ അല്ലല്ലോ, ആ 45 ദിവസ സംരക്ഷണവും പോയി എന്ന് അക്കൗണ്ടന്റ്."),
 ("V","V","ലീലേ, കടന്നത് മൈക്രോ ലിമിറ്റല്ലേ? ഇപ്പോൾ നമ്മൾ സ്മോൾ."),
 ("A","A","സ്മോൾ ആയാലും ബയർ വൈകിച്ചാൽ നമുക്ക് ഒന്നും പറയാൻ പറ്റില്ലേ?"),
 ("V","wide","പറ്റും. മൈക്രോയ്ക്കും സ്മോളിനും 45 ദിവസ നിയമമുണ്ട്. സ്മോൾ എന്നാൽ 25 കോടി നിക്ഷേപം, 100 കോടി ടേൺഓവർ വരെ."),
 ("A","A","അപ്പോ ഉദ്യമിൽ പുതിയ കണക്ക് ചേർത്താൽ മതി."),
 ("V","wide","വളർന്നത് തറി, സംരക്ഷണം ചുരുങ്ങിയില്ല.")],
 "വളർന്നത് തറി,\nസംരക്ഷണം\nചുരുങ്ങിയില്ല", CTA_MSME, theme="crm",
 cap_ml="ടേൺഓവർ 10 കോടി കടന്നാൽ മൈക്രോയിൽ നിന്ന് സ്മോളിലേക്ക്. പക്ഷേ 45 ദിവസ പേമെന്റ് സംരക്ഷണം മൈക്രോയ്ക്കും സ്മോളിനും ഉണ്ട്. സ്മോൾ: നിക്ഷേപം 25 കോടി വരെ, ടേൺഓവർ 100 കോടി വരെ. ഉദ്യമിൽ വിവരം അപ്ഡേറ്റ് ചെയ്യൂ. നിങ്ങൾ മൈക്രോയോ സ്മോളോ?",
 cap_en="Crossing Rs 10 crore turnover moves a unit from micro to small, but the 45-day payment protection covers both micro and small manufacturing and service units. Small means investment up to Rs 25 crore and turnover up to Rs 100 crore. Keep your Udyam details updated. Micro or small?",
 cap_mg="Turnover 10 crore kadannaal micro-il ninnu small-ilekku. Pakshe 45 divasa payment samrakshanam micro-kkum small-inum undu. Small: investment 25 crore vare, turnover 100 crore vare. Udyam-il vivaram update cheyyoo. Ningal micro-o small-o?")

# NEW: the buyer is a tiny business too ("I'm also small, why 45 days?")
duo("yd030", "supplier_unpaid", "C", "petrolpump", "\"ഞാനും ചെറിയ\nആളാ, എനിക്കെന്തിന്\n45 ദിവസ നിയമം?\"", [
 ("A","wide","ഷിബൂ, പമ്പിന്റെ ഷെഡ് വെൽഡ് ചെയ്ത പയ്യൻ 50 ദിവസമായി പണം ചോദിക്കുന്നു. ഞാനും ചെറിയ ബിസിനസല്ലേ?"),
 ("V","V","സന്തോഷേ, അവന്റെ വെൽഡിംഗ് യൂണിറ്റിന് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ടെന്ന് ബില്ലിൽ എഴുതിയിട്ടുണ്ട്. മൈക്രോ."),
 ("V","wide","എങ്കിൽ ബയർ നീ ആണ്. എഴുതിയ കാലാവധി പരമാവധി 45 ദിവസം. കഴിഞ്ഞാൽ RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ."),
 ("A","A","ചെറുതായാലും വാങ്ങിയാൽ ബയർ തന്നെ, അല്ലേ?"),
 ("V","wide","വലിപ്പം നോക്കില്ല, ബില്ലിന്റെ തീയതി നോക്കും.")],
 "വലിപ്പം നോക്കില്ല,\nബില്ലിന്റെ\nതീയതി നോക്കും", CTA_MSME, theme="new",
 cap_ml="ബയർ ചെറിയ ബിസിനസ് ആണെങ്കിൽ 45 ദിവസ നിയമം ബാധകമല്ലേ? സപ്ലയർ ഉദ്യം ഉള്ള മൈക്രോ അല്ലെങ്കിൽ സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റാണെങ്കിൽ ബയർ എഗ്രിമെന്റ് ഇല്ലാതെ 15 ദിവസത്തിൽ, ഉണ്ടെങ്കിൽ പരമാവധി 45 ദിവസത്തിൽ പണം നൽകണം. അതിന് ശേഷം RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="Does the 45-day rule skip small buyers? If the supplier is an Udyam-registered micro or small manufacturing or service unit, the buyer must pay within 15 days without an agreement, or the agreed time up to 45 days; after that, compound interest at three times the RBI bank rate. Did you know this: yes or no?",
 cap_mg="Buyer cheriya business aanenkil 45 divasa niyamam baadhakamalle? Supplier Udyam ulla micro allenkil small manufacturing, service unit aanenkil buyer agreement illaathe 15 divasathil, undenkil maximum 45 divasathil panam nalkanam. Athinu shesham RBI bank rate-inte moonnirratti koottupalisha. Ithu ariyaamaayirunno?")

# FAQ: "Udyam needs a CA and audited accounts first" (it is an online self-declaration)
duo("yd031", "service_unit", "A", "hostel", "\"ഉദ്യമിന് ഓഡിറ്റ്\nചെയ്ത കണക്ക്\nവേണ്ടേ? CA എവിടെ?\"", [
 ("A","wide","സഞ്ജൂ, ഹോസ്റ്റലിൽ ഇരുന്ന് ഞാൻ നടത്തുന്ന ഗ്രാഫിക് ഡിസൈൻ സർവീസിന് ഉദ്യം വേണം. പക്ഷേ ഓഡിറ്റ് ചെയ്ത കണക്കില്ല."),
 ("V","V","അലീനാ, ഉദ്യം ചോദിക്കുന്നത് ഓഡിറ്റ് റിപ്പോർട്ടല്ല."),
 ("A","A","പിന്നെ? ഒരു CA ഒപ്പിടേണ്ടേ?"),
 ("V","wide","ഓൺലൈൻ, ആധാർ അടിസ്ഥാനം, PAN, GST ഉണ്ടെങ്കിൽ അതും. നിക്ഷേപവും ടേൺഓവറും നീ തന്നെ സ്വയം സാക്ഷ്യപ്പെടുത്തും."),
 ("A","A","അപ്പോ ഫോണിൽ ആധാർ OTP മതി."),
 ("V","wide","സത്യം എഴുതിയാൽ മതി, സ്റ്റാമ്പ് വേണ്ട.")],
 "സത്യം എഴുതിയാൽ\nമതി, സ്റ്റാമ്പ്\nവേണ്ട", CTA_UDYAM, theme="faq",
 cap_ml="ഉദ്യം രജിസ്ട്രേഷന് ഓഡിറ്റ് ചെയ്ത കണക്കോ CA ഒപ്പോ വേണോ? ഇല്ല. ഓൺലൈൻ, ആധാർ അടിസ്ഥാനമാക്കി, PAN, GSTIN ഉണ്ടെങ്കിൽ അതും, പിന്നെ സ്വയം സാക്ഷ്യം. വിവരം സത്യമായിരിക്കണം. നിങ്ങൾ എടുത്തോ?",
 cap_en="Do you need audited accounts or a CA's signature for Udyam? No. It is online and Aadhaar-based, with PAN (and GSTIN if you have one) and a self-declaration; the details must be true. Have you registered yet: yes or no?",
 cap_mg="Udyam registration-inu audit cheytha kanakko CA oppo veno? Illa. Online, Aadhaar adisthaanamaakki, PAN, GSTIN undenkil athum, pinne self declaration. Vivaram sathyamaayirikkanam. Ningal eduttho?")

# CRM ("busy, call back later"): a buyer's MSME vendor form was not returned, so the unit was treated as non-MSME
duo("yd032", "supplier_unpaid", "A", "canteen", "\"വെള്ളിയാഴ്ചക്കുള്ളിൽ\nഉദ്യം അയക്കൂ\"\nഅവൻ മറന്നു", [
 ("A","wide","അമലേ, ഹോട്ടൽ ഗ്രൂപ്പ് മസാലപ്പൊടിയുടെ പണം 90 ദിവസത്തിലാ ഇട്ടത്. ഉദ്യം നമ്പർ ചോദിച്ച മെയിൽ ഓർമ്മയുണ്ടോ?"),
 ("V","V","ആതിരേ, തിരക്കായിരുന്നു. അത് വെറും ഫോമല്ലേ?"),
 ("A","A","ആ ഫോം വെച്ചാ അവർ MSME സപ്ലയർമാരെ വേർതിരിക്കുന്നത്."),
 ("V","wide","ശരിയാ. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റിന് 45 ദിവസം. വൈകിയാൽ അവരുടെ ടാക്സ് കിഴിവും പോകും."),
 ("A","A","നമ്പർ നമുക്കുണ്ടായിരുന്നു, അയച്ചില്ല എന്ന് മാത്രം."),
 ("V","wide","നമ്പർ പോക്കറ്റിലിരുന്നാൽ നിയമം ഉറങ്ങും.")],
 "നമ്പർ പോക്കറ്റിൽ\nഇരുന്നാൽ നിയമം\nഉറങ്ങും", CTA_MSME, theme="crm",
 cap_ml="വലിയ ബയർ ഉദ്യം നമ്പർ ചോദിക്കുന്നത് വെറുതെയല്ല. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റുകൾക്ക് 45 ദിവസത്തിനുള്ളിൽ പണം; വൈകിയാൽ ബയർക്ക് സെക്ഷൻ 43B(h) പ്രകാരം ആദായനികുതി കിഴിവ് പണം കൊടുക്കും വരെ നഷ്ടം. ബയറിന്റെ ഫോമിൽ നിങ്ങൾ നമ്പർ നൽകിയോ?",
 cap_en="When a big buyer asks for your Udyam number, it matters. Udyam-registered micro and small manufacturing and service units must be paid within 45 days at most, and a buyer who pays late loses the income-tax deduction until payment (section 43B(h)). Did you send your number on the buyer's vendor form?",
 cap_mg="Valiya buyer Udyam number chodikkunnathu veruthe alla. Udyam ulla micro, small manufacturing, service unit-kalkku 45 divasathinullil panam; vaikiyaal buyer-kku 43B(h) prakaaram income tax deduction panam kodukkum vare nashtam. Buyer-inte form-il ningal number nalkiyo?")

# CRM (service business with corporate clients): a two-founder Pvt Ltd thinks MSME is only for traditional units
duo("yd033", "service_unit", "C", "cafe", "\"നമ്മൾ സ്റ്റാർട്ടപ്പാ,\nMSME ഒക്കെ\nപപ്പടക്കാർക്കല്ലേ?\"", [
 ("A","wide","റോഷാ, ആ ഇൻഷുറൻസ് കമ്പനി ആപ്പ് ടെസ്റ്റിംഗിന്റെ ബിൽ 120 ദിവസമായി പിടിച്ചുവെച്ചിരിക്കുന്നു. MSME ഒക്കെ പപ്പടക്കാർക്കല്ലേ?"),
 ("V","V","ആൽവിനേ, നമ്മുടെ പ്രൈവറ്റ് ലിമിറ്റഡിന് ഉദ്യം എടുത്തിട്ടുണ്ടല്ലോ, മൈക്രോ സർവീസ്."),
 ("A","A","കമ്പനിക്കും അത് ബാധകമോ?"),
 ("V","wide","ബാധകം. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് 45 ദിവസം കഴിഞ്ഞാൽ കൂട്ടുപലിശ. MSME സമാധാൻ പോർട്ടലിൽ പരാതിയും നൽകാം."),
 ("A","A","കോഡ് എഴുതുന്നതും സർവീസ് തന്നെ."),
 ("V","wide","പപ്പടമായാലും ആപ്പായാലും, ബിൽ ബില്ല് തന്നെ.")],
 "പപ്പടമായാലും\nആപ്പായാലും,\nബിൽ ബില്ല് തന്നെ", CTA_MSME, theme="crm",
 cap_ml="ആപ്പ് ടെസ്റ്റിംഗ് നടത്തുന്ന പ്രൈവറ്റ് ലിമിറ്റഡ് സ്റ്റാർട്ടപ്പിനും MSME പേമെന്റ് സംരക്ഷണം ഉണ്ടോ? ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റാണെങ്കിൽ ഉണ്ട്: 45 ദിവസം കഴിഞ്ഞാൽ കൂട്ടുപലിശ, MSME സമാധാൻ പോർട്ടലിൽ പരാതി. നിങ്ങളുടെ ക്ലയന്റ് എത്ര ദിവസം എടുക്കുന്നു?",
 cap_en="Does a Pvt Ltd app-testing startup get MSME payment protection? Yes, if it is an Udyam-registered micro or small service unit: compound interest after 45 days, and complaints on the MSME Samadhaan portal. How many days does your client take to pay?",
 cap_mg="App testing nadathunna Pvt Ltd startup-inum MSME payment samrakshanam undo? Udyam ulla micro, small service unit aanenkil undu: 45 divasam kazhinjaal koottupalisha, MSME Samadhaan portal-il paraathi. Ningalude client ethra divasam edukkunnu?")

# NEW (d904 pattern, unusual Kerala job): miniature Kerala-bus model maker; gift chain "settles every six months"
duo("yd034", "supplier_unpaid", "C", "busstop", "മിനിയേച്ചർ ബസ്\n200 എണ്ണം. \"ആറ്\nമാസം കൂടുമ്പോൾ തരാം\"", [
 ("A","wide","അഖിലേ, എന്റെ കുഞ്ഞൻ KSRTC ബസ് മോഡലുകൾ ആ ഗിഫ്റ്റ് ഷോപ്പ് ചെയിൻ എടുത്തു. പണം ആറ് മാസം കൂടുമ്പോൾ ഒന്നിച്ചാണത്രെ."),
 ("V","V","ജിബിനേ, നിന്റെ വർക്ക്ഷോപ്പിന് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ട്, മൈക്രോ നിർമാണം. പക്ഷേ അവരുടെ രീതി അതാണെന്ന്."),
 ("V","wide","അവരുടെ രീതിയേക്കാൾ വലുതാണ് നിയമം. എഴുതിയാലും പരമാവധി 45 ദിവസം. പിന്നെ കൂട്ടുപലിശ, സമാധാൻ പോർട്ടലും."),
 ("A","A","അപ്പോ ആറ് മാസം എന്ന സ്റ്റോപ്പ് നിയമത്തിലില്ല."),
 ("V","wide","ബസ് ചെറുതാകാം, റൂട്ട് 45 ദിവസം.")],
 "ബസ് ചെറുതാകാം,\nറൂട്ട് 45 ദിവസം", CTA_MSME, theme="new",
 cap_ml="കുഞ്ഞൻ ബസ് മോഡൽ ഉണ്ടാക്കുന്ന മൈക്രോ യൂണിറ്റിനോട് ബയർ \"ആറ് മാസം കൂടുമ്പോൾ\" പണം എന്ന് പറഞ്ഞാൽ? ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റിന് എഴുതിയ കാലാവധി പരമാവധി 45 ദിവസം; പിന്നെ കൂട്ടുപലിശ, MSME സമാധാൻ പോർട്ടലിൽ പരാതി. നിങ്ങളുടെ ബയറിന്റെ 'രീതി' എത്ര ദിവസം?",
 cap_en="A micro unit making miniature Kerala bus models is told the gift chain settles every six months. For Udyam-registered micro and small manufacturing and service units, the agreed time can be 45 days at most; after that compound interest applies, and complaints go to the MSME Samadhaan portal. How many days does your buyer's 'system' take?",
 cap_mg="Kunjan bus model undaakkunna micro unit-inodu buyer 'aaru maasam koodumbol' panam ennu paranjaal? Udyam ulla micro, small manufacturing, service unit-inu ezhuthiya kaalavadhi maximum 45 divasam; pinne koottupalisha, MSME Samadhaan portal-il paraathi. Ningalude buyer-inte 'reethi' ethra divasam?")
