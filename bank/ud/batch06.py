# Udyam / MSME batch 06 (21 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_UD. Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

# FAQ + d904 pattern: myth "one person working from home is not an enterprise"; temple-festival projection artist
duo("yd035", "service_unit", "B", "balcony", "\"ഞാൻ ഒറ്റയ്ക്കല്ലേ?\nഎനിക്കെന്ത്\nMSME?\"", [
 ("A","wide","വിവേകേ, ഉത്സവത്തിന് ഗോപുരത്തിൽ നീ ചെയ്ത ലൈറ്റ് ആനിമേഷൻ ഹിറ്റായി. ഇവന്റ് കമ്പനി പണം തന്നോ?"),
 ("V","V","അമ്മൂ, രണ്ട് മാസമായി. പക്ഷേ ഞാൻ ഒറ്റയ്ക്ക് ബാൽക്കണിയിൽ ഇരുന്ന് ചെയ്യുന്നതല്ലേ. എനിക്കെന്ത് MSME?"),
 ("A","A","ആളെണ്ണം നോക്കിയല്ല ഉദ്യം. സർവീസ് ബിസിനസിനും ഉദ്യം എടുക്കാം."),
 ("A","wide","മൈക്രോ സർവീസ് യൂണിറ്റിന് ബയർ പരമാവധി 45 ദിവസത്തിൽ പണം തരണം. പിന്നെ കൂട്ടുപലിശ."),
 ("V","V","അപ്പോ ഒറ്റയാനും ഒരു യൂണിറ്റാ."),
 ("A","wide","ഗോപുരം തെളിഞ്ഞു, ഇനി നിന്റെ ബില്ലും തെളിയട്ടെ.")],
 "ഒറ്റയ്ക്കാണെങ്കിലും\nയൂണിറ്റ് യൂണിറ്റാ", CTA_MSME, theme="faq",
 cap_ml="ഉത്സവ ഗോപുരത്തിൽ ലൈറ്റ് ആനിമേഷൻ ചെയ്യുന്ന ഒറ്റയാൾ ആർട്ടിസ്റ്റ് കരുതി MSME വലിയ ഫാക്ടറികൾക്കാണെന്ന്. ഉദ്യം ഉള്ള മൈക്രോ സർവീസ് യൂണിറ്റിനും ബയർ എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിൽ പരമാവധി 45 ദിവസത്തിൽ പണം തരണം. നിങ്ങൾ ഒറ്റയ്ക്കാണോ ടീമാണോ?",
 cap_en="A one-person artist who projects light animations on temple towers thought MSME was only for big factories. A one-person service business can register on Udyam, and for a micro or small service unit the buyer must pay within 15 days, or the agreed time up to 45 days, then compound interest applies. Do you work solo or with a team?",
 cap_mg="Utsava gopurathil light animation cheyyunna ottayaal artist karuthi MSME valiya factory-kalkkaanennu. Udyam ulla micro service unit-inum buyer agreement illenkil 15 divasam, undenkil maximum 45 divasathil panam tharanam. Ningal ottaykkaano team aano?")

# NEW: make or resell? A robotics-kit business learns which part of its work gets the 45-day protection
duo("yd036", "trader_ud", "C", "classroom", "സ്കൂളിന് 300 കിറ്റ്.\nപണം വൈകി.\n\"ഞാൻ ഉദ്യം ഉള്ളയാളാ\"", [
 ("A","wide","ആദർശേ, സ്കൂളിന് കൊടുത്ത റോബോട്ടിക്സ് കിറ്റിന്റെ പണം മൂന്ന് മാസമായില്ലേ? ഉദ്യം ഉണ്ടല്ലോ, പലിശ ചോദിക്ക്."),
 ("V","V","നിമ്മീ, ആ കിറ്റുകൾ ഞാൻ പുറത്തുനിന്ന് വാങ്ങി മറിച്ച് വിൽക്കുന്നതാ. ഉദ്യമിൽ കച്ചവടം എന്നാ കൊടുത്തത്."),
 ("A","A","അത് വേറെ കഥ. കച്ചവടക്കാർക്ക് ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം."),
 ("A","wide","45 ദിവസ സംരക്ഷണം നിർമാണ, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്കാ. സ്വന്തമായി കിറ്റ് ഉണ്ടാക്കിയാൽ കളി മാറും."),
 ("V","V","അപ്പോ സോൾഡറിംഗ് തുടങ്ങണം."),
 ("A","wide","മറിച്ച് വിറ്റാൽ വായ്പ, ഉണ്ടാക്കി വിറ്റാൽ സംരക്ഷണം.")],
 "മറിച്ച് വിറ്റാൽ വായ്പ,\nഉണ്ടാക്കി വിറ്റാൽ\nസംരക്ഷണം", CTA_MSME, theme="new",
 cap_ml="സ്കൂളുകൾക്ക് റോബോട്ടിക്സ് കിറ്റ് വാങ്ങി മറിച്ച് വിൽക്കുന്നയാൾ ഉദ്യം ഉള്ളതുകൊണ്ട് 45 ദിവസ നിയമം കിട്ടുമെന്ന് കരുതി. കച്ചവടക്കാർക്ക് ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം; പണം വൈകുമ്പോഴുള്ള സംരക്ഷണം നിർമാണ, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക്. നിങ്ങൾ ഉണ്ടാക്കുന്നോ മറിച്ച് വിൽക്കുന്നോ?",
 cap_en="A robotics-kit seller assumed his Udyam registration meant schools must pay him within 45 days. But he buys and resells, and registered as a trader: traders get Udyam only for priority sector lending. The 45-day payment protection is for micro and small manufacturing and service units. Do you make it or resell it?",
 cap_mg="School-ukalkku robotics kit vaangi marichu vilkkunna aal Udyam ullathukondu 45 divasa niyamam kittumennu karuthi. Kachavadakkaarkku Udyam priority lending-inu maathram; panam vaikumbol ulla samrakshanam manufacturing, service micro, small unit-ukalkku. Ningal undaakkunno marichu vilkkunno?")

# CRM (supplier paid in part): hospital linen laundry gets half on time, the rest "after audit"
duo("yd037", "supplier_unpaid", "A", "hospital", "പകുതി പണം തന്നു.\nബാക്കി? \"ഓഡിറ്റ്\nകഴിയട്ടെ\"", [
 ("A","wide","ജോസഫേ, നിന്റെ ലോൺഡ്രി യൂണിറ്റ് ഇവിടത്തെ ബെഡ്ഷീറ്റ് മുഴുവൻ കഴുകുന്നതല്ലേ. എന്താ മുഖം വാടിയത്?"),
 ("V","V","ലക്ഷ്മീ, ബില്ലിന്റെ പകുതി തന്നു. ബാക്കി ഓഡിറ്റ് കഴിഞ്ഞിട്ടെന്ന്. നാല് മാസമായി."),
 ("A","A","പകുതി കിട്ടിയതുകൊണ്ട് ബാക്കിയുടെ ദിവസം നിൽക്കില്ല."),
 ("A","wide","ഉദ്യം ഉള്ള മൈക്രോ സർവീസ് യൂണിറ്റിന് പരമാവധി 45 ദിവസം. വൈകിയ തുകയ്ക്ക് RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ."),
 ("V","V","അപ്പോ ബാക്കി പകുതിക്കും കണക്കുണ്ട്."),
 ("A","wide","ഷീറ്റ് പകുതി കഴുകിയാൽ ആരും സമ്മതിക്കില്ലല്ലോ.")],
 "ഷീറ്റ് പകുതി കഴുകിയാൽ\nആരും സമ്മതിക്കില്ലല്ലോ", CTA_MSME, theme="crm",
 cap_ml="ആശുപത്രി ബെഡ്ഷീറ്റ് കഴുകുന്ന ലോൺഡ്രി യൂണിറ്റിന് ബില്ലിന്റെ പകുതി കിട്ടി, ബാക്കി നാല് മാസമായി ഓഡിറ്റ് കാത്ത്. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് പരമാവധി 45 ദിവസം; വൈകിയ തുകയ്ക്ക് RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. നിങ്ങൾക്ക് പകുതി പണം കിട്ടി നിൽക്കുന്ന ബില്ലുണ്ടോ?",
 cap_en="A laundry unit that washes a hospital's linen got half its bill, and the rest has waited four months 'for the audit'. For an Udyam-registered micro or small service unit the buyer must pay within the agreed time of at most 45 days, and the delayed amount carries compound interest at three times the RBI bank rate. Got a half-paid bill: yes or no?",
 cap_mg="Aashupathri bedsheet kazhukunna laundry unit-inu bill-inte pakuthi kitti, baakki naalu maasamaayi audit kaathu. Udyam ulla micro, small service unit-inu maximum 45 divasam; vaikiya thukaykku RBI bank rate-inte moonnirratti koottupalisha. Ningalkku pakuthi panam kitti nilkkunna bill undo?")

# NEW + d904 pattern: March-end, a buyer who ignored a canoe builder for months suddenly pays (section 43B(h))
duo("yd038", "supplier_unpaid", "B", "ferry", "മാർച്ച് 28.\nനാല് മാസം മിണ്ടാത്ത\nബയർ: \"ഇന്ന് തരാം\"", [
 ("A","wide","ടോണീ, ഫൈബർ വള്ളത്തിന്റെ ബാക്കി പണം ആ ടൂർ കമ്പനി ഇന്ന് അയച്ചെന്ന്? നാല് മാസം മിണ്ടാത്തവരല്ലേ?"),
 ("V","V","മീരേ, എനിക്കും അത്ഭുതം. അവരുടെ അക്കൗണ്ടന്റ് രാവിലെ വിളിച്ചു, മാർച്ചിന് മുമ്പ് തീർക്കണമെന്ന്."),
 ("A","A","കാരണം നിന്റെ ഉദ്യം നമ്പരാ."),
 ("A","wide","ഇൻകം ടാക്സ് നിയമപ്രകാരം മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് സമയത്ത് പണം കൊടുക്കാത്ത ബയർക്ക് കൊടുക്കും വരെ ആ ചെലവിന് ടാക്സ് കിഴിവില്ല."),
 ("V","V","അപ്പോ എന്റെ വള്ളം അവരുടെ ടാക്സിലും തുഴയുന്നു."),
 ("A","wide","വള്ളം വെള്ളത്തിൽ, ബിൽ ബുക്കിൽ, പണം സമയത്ത്.")],
 "നിന്റെ വള്ളം\nഅവരുടെ ടാക്സിലും\nതുഴയുന്നു", CTA_UDYAM, theme="new",
 cap_ml="നാല് മാസം മിണ്ടാതിരുന്ന ടൂർ കമ്പനി മാർച്ച് അവസാനം ഫൈബർ വള്ളം ഉണ്ടാക്കുന്നയാളെ വിളിച്ച് പണം അയച്ചു. കാരണം 43B(h): ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് സമയത്ത് പണം കൊടുക്കാത്ത ബയർക്ക് കൊടുക്കും വരെ ആ തുകയ്ക്ക് ഇൻകം ടാക്സ് കിഴിവ് കിട്ടില്ല. നിങ്ങളുടെ ബയർ മാർച്ചിൽ വിളിക്കാറുണ്ടോ?",
 cap_en="A tour company that ignored a fibre-canoe builder for four months suddenly paid in late March. The reason is section 43B(h): a buyer who pays an Udyam-registered micro or small supplier late loses the income-tax deduction for that expense until it pays. Does your buyer suddenly call in March?",
 cap_mg="Naalu maasam mindaathirunna tour company March avasaanam fibre vallam undaakkunna aale vilichu panam ayachu. Kaaranam 43B(h): Udyam ulla micro, small supplier-kku samayathu panam kodukkaatha buyer-kku kodukkum vare aa thukaykku income tax kizhivu kittilla. Ningalude buyer March-il vilikkaarundo?")

# CRM (service unit, no written terms): homestay rooms supplied to a travel agency that "settles after the season"
duo("yd039", "service_unit", "A", "homestay", "സീസൺ മുഴുവൻ\nമുറി കൊടുത്തു.\n\"സീസൺ കഴിഞ്ഞ് തരാം\"", [
 ("A","wide","ജോമോനേ, ട്രാവൽ ഏജൻസിക്ക് ഈ സീസണിൽ 40 രാത്രി മുറി കൊടുത്തു. അവർ പറയുന്നു, സീസൺ കഴിഞ്ഞ് ഒന്നിച്ച് തരാമെന്ന്."),
 ("V","V","ടീനേ, എഴുതി ഒപ്പിട്ട എഗ്രിമെന്റ് വല്ലതും ഉണ്ടോ?"),
 ("A","A","ഇല്ല, എല്ലാം ഫോണിലാ. ഹോംസ്റ്റേ ഒക്കെ MSME ആണോ എന്നും അറിയില്ല."),
 ("V","wide","ഉദ്യം ഉള്ള മൈക്രോ സർവീസ് യൂണിറ്റാ. സമയം എഴുതി സമ്മതിച്ചിട്ടില്ലെങ്കിൽ 15 ദിവസത്തിൽ പണം തരണം."),
 ("A","A","സീസൺ നാല് മാസമാ, നിയമം 15 ദിവസവും."),
 ("V","wide","മുറി രാത്രിക്ക്, പണം പതിനഞ്ചിന്.")],
 "മുറി രാത്രിക്ക്,\nപണം പതിനഞ്ചിന്", CTA_MSME, theme="crm",
 cap_ml="ഹോംസ്റ്റേ ഉടമ ട്രാവൽ ഏജൻസിക്ക് 40 രാത്രി മുറി കൊടുത്തു, പണം സീസൺ കഴിഞ്ഞ് എന്ന് ഫോണിൽ മാത്രം. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് എഴുതി സമ്മതിച്ച സമയം ഇല്ലെങ്കിൽ ബയർ 15 ദിവസത്തിൽ പണം തരണം. നിങ്ങളുടെ പേമെന്റ് സമയം എഴുതിയിട്ടുണ്ടോ?",
 cap_en="A homestay owner gave a travel agency 40 room-nights this season, and the agency says it will settle 'after the season', agreed only by phone. A homestay can be an Udyam-registered micro service unit, and with no agreed payment time the buyer must pay within 15 days. Is your payment time written down: yes or no?",
 cap_mg="Homestay udama travel agency-kku 40 raathri muri koduthu, panam season kazhinju ennu phone-il maathram. Udyam ulla micro, small service unit-inu ezhuthi sammathicha samayam illenkil buyer 15 divasathil panam tharanam. Ningalude payment samayam ezhuthiyittundo?")

# FAQ: myth "Udyam is my food licence"; a hill-town chocolate maker
duo("yd040", "manufacturer", "C", "munnar", "\"ഉദ്യം കിട്ടി.\nഇനി ചോക്ലേറ്റ്\nഎവിടെയും വിൽക്കാം\"", [
 ("A","wide","ബേസിലേ, നിന്റെ ഹോംമെയ്ഡ് ചോക്ലേറ്റ് ഇനി കടകളിലേക്ക് അല്ലേ? പേപ്പറൊക്കെ റെഡിയാണോ?"),
 ("V","V","സെലിനേ, ഉദ്യം കിട്ടിയല്ലോ. ഇനി ഇതാ എന്റെ ലൈസൻസ്, എവിടെയും വിൽക്കാം."),
 ("A","A","ഉദ്യം സർക്കാരിന്റെ MSME രജിസ്ട്രേഷനാ, ഭക്ഷണത്തിന്റെ ലൈസൻസ് അല്ല."),
 ("A","wide","അത് വായ്പ, ടെൻഡർ, പണം വൈകിയാലുള്ള സംരക്ഷണം ഇവയ്ക്ക്. ഭക്ഷണം വിൽക്കാൻ FSSAI വേറെ വേണം."),
 ("V","V","അപ്പോ ഒരു പേപ്പർ രണ്ട് ജോലി ചെയ്യില്ല."),
 ("A","wide","ചോക്ലേറ്റിന് പൊതി വേണം, ബിസിനസിന് രണ്ടും വേണം.")],
 "ഉദ്യം MSME-യുടേത്,\nഭക്ഷണത്തിന്\nFSSAI വേറെ", CTA_UDYAM, theme="faq",
 cap_ml="ഹോംമെയ്ഡ് ചോക്ലേറ്റ് ഉണ്ടാക്കുന്നയാൾ കരുതി ഉദ്യം കിട്ടിയാൽ അത് ഭക്ഷണ ലൈസൻസ് ആണെന്ന്. ഉദ്യം സർക്കാരിന്റെ MSME രജിസ്ട്രേഷൻ: മുൻഗണനാ വായ്പ, ടെൻഡർ മുൻഗണന, മൈക്രോ, സ്മോൾ നിർമാണ യൂണിറ്റിന് പണം വൈകിയാലുള്ള സംരക്ഷണം. ഭക്ഷണം വിൽക്കാൻ FSSAI രജിസ്ട്രേഷൻ വേറെ. നിങ്ങൾ ഭക്ഷണം ഉണ്ടാക്കി വിൽക്കുന്നുണ്ടോ?",
 cap_en="A homemade chocolate maker thought his new Udyam registration was his licence to sell food anywhere. Udyam is the government's MSME registration: it helps with priority sector lending, tender preferences and late-payment protection for micro and small manufacturers. Selling food still needs FSSAI registration separately. Do you make and sell food?",
 cap_mg="Homemade chocolate undaakkunna aal karuthi Udyam kittiyaal athu food licence aanennu. Udyam sarkkarinte MSME registration: priority lending, tender munganana, micro, small manufacturing unit-inu panam vaikiyaal ulla samrakshanam. Food vilkkaan FSSAI registration vere. Ningal food undaakki vilkkunnundo?")

# CRM + d904 pattern: palm-leaf manuscript digitisation for a research institute; "the grant money comes late"
duo("yd041", "supplier_unpaid", "B", "library", "താളിയോല 2000.\nസ്കാൻ ചെയ്തു.\n\"ഫണ്ട് വന്നിട്ട് തരാം\"", [
 ("A","wide","അനൂപേ, നിന്റെ ടീം 2000 താളിയോല സ്കാൻ ചെയ്തിട്ട് അഞ്ച് മാസമായില്ലേ? ഇൻസ്റ്റിറ്റ്യൂട്ട് പണം തന്നോ?"),
 ("V","V","ഗ്രീഷ്മേ, ഇല്ല. അവർക്ക് ഗ്രാന്റ് വരണം പോലും. അവരോട് തർക്കിക്കാനും പറ്റില്ലല്ലോ."),
 ("A","A","അവരുടെ ഫണ്ട് വൈകുന്നത് നിന്റെ നിയമം മാറ്റില്ല."),
 ("A","wide","ഉദ്യം ഉള്ള മൈക്രോ സർവീസ് യൂണിറ്റിന് പരമാവധി 45 ദിവസം. പിന്നെ MSME സമാധാൻ പോർട്ടലിൽ പരാതിപ്പെടാം."),
 ("V","V","തർക്കം വേണ്ട, പോർട്ടൽ മതി."),
 ("A","wide","ഓല പഴയതാകാം, നിന്റെ ബിൽ പഴകരുത്.")],
 "ഓല പഴയതാകാം,\nബിൽ പഴകരുത്", CTA_MSME, theme="crm",
 cap_ml="2000 താളിയോലകൾ സ്കാൻ ചെയ്ത ഡിജിറ്റൈസേഷൻ ടീമിന് അഞ്ച് മാസമായി പണമില്ല, കാരണം ഇൻസ്റ്റിറ്റ്യൂട്ടിന് ഗ്രാന്റ് വരണം പോലും. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് പരമാവധി 45 ദിവസം; പിന്നെ MSME സമാധാൻ പോർട്ടലിലോ ഫെസിലിറ്റേഷൻ കൗൺസിലിലോ പരാതി. നിങ്ങളുടെ ജോലി: പഴയതോ പുതിയതോ?",
 cap_en="A team that digitised 2,000 palm-leaf manuscripts for a research institute has waited five months, because the institute says its grant hasn't come. The buyer's funding delay doesn't change the rule: an Udyam-registered micro or small service unit must be paid within at most 45 days, and can then complain on the MSME Samadhaan portal or to the facilitation council. Your work: old or new?",
 cap_mg="2000 thaaliyolakal scan cheytha digitisation team-inu anchu maasamaayi panamilla, kaaranam institute-inu grant varanam polum. Udyam ulla micro, small service unit-inu maximum 45 divasam; pinne MSME Samadhaan portal-ilo facilitation council-ilo paraathi. Ningalude joli: pazhayatho puthiyatho?")

# FAQ: myth "I pay you when my customer pays me" (back-to-back payment); cloud kitchen supplying a food-court chain
duo("yd042", "supplier_unpaid", "A", "foodcourt", "\"കസ്റ്റമർ ഞങ്ങൾക്ക്\nതന്നിട്ട് നിങ്ങൾക്ക്\nതരാം\"", [
 ("A","wide","ഡെന്നിസേ, ഫുഡ് കോർട്ട് ചെയിനിന് ബിരിയാണി സപ്ലൈ ചെയ്തിട്ട് 70 ദിവസം. അവർ പറയുന്നു, അവരുടെ സെറ്റിൽമെന്റ് വന്നിട്ടെന്ന്."),
 ("V","V","മരിയേ, അത് അവരും അവരുടെ കസ്റ്റമറും തമ്മിലുള്ള കാര്യമല്ലേ?"),
 ("A","A","അതേ. പക്ഷേ ഞാൻ വിചാരിച്ചു അങ്ങനെയാ ബിസിനസിന്റെ രീതി എന്ന്."),
 ("V","wide","നിന്റെ കിച്ചണിന് ഉദ്യം ഉണ്ടെങ്കിൽ, മൈക്രോ യൂണിറ്റിന് ബയർ പരമാവധി 45 ദിവസത്തിൽ പണം തരണം. അവരുടെ കസ്റ്റമർ തന്നാലും ഇല്ലെങ്കിലും."),
 ("A","A","അവരുടെ പണം വൈകിയാൽ അവരുടെ പ്രശ്നം."),
 ("V","wide","ബിരിയാണി ചൂടോടെ പോയി, പണം തണുക്കരുത്.")],
 "ബിരിയാണി ചൂടോടെ\nപോയി, പണം\nതണുക്കരുത്", CTA_MSME, theme="faq",
 cap_ml="ഫുഡ് കോർട്ട് ചെയിൻ ക്ലൗഡ് കിച്ചണോട് പറയുന്നു: ഞങ്ങളുടെ കസ്റ്റമർ തന്നിട്ട് നിങ്ങൾക്ക് തരാം. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റിന് ബയർ എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിൽ പരമാവധി 45 ദിവസത്തിൽ പണം തരണം. ബയറിന്റെ കസ്റ്റമർ വൈകിയാലും. ഈ മറുപടി നിങ്ങൾ കേട്ടിട്ടുണ്ടോ?",
 cap_en="A food-court chain tells the cloud kitchen supplying it: we'll pay you when our customers pay us. Not how the MSME rule works: an Udyam-registered micro or small manufacturing or service unit must be paid within 15 days, or the agreed time up to 45 days, whether or not the buyer's own customer has paid. Heard this line before: yes or no?",
 cap_mg="Food court chain cloud kitchen-inodu parayunnu: njangalude customer thannittu ningalkku tharaam. Udyam ulla micro, small manufacturing, service unit-inu buyer agreement illenkil 15 divasam, undenkil maximum 45 divasathil panam tharanam. Buyer-inte customer vaikiyaalum. Ee marupadi ningal kettittundo?")

# CRM (Gulf returnee, loan without property): coir doormat unit planned from the Gulf
duo("yd043", "loan_seeker", "C", "gulfoffice", "\"നാട്ടിൽ വീടില്ല.\nഈടില്ലാതെ ആര്\nലോൺ തരും?\"", [
 ("A","wide","ആസിഫേ, നീ നാട്ടിൽ കയർ ചവിട്ടി യൂണിറ്റ് തുടങ്ങുന്നെന്ന് കേട്ടു. മെഷീനിന് ലോൺ നോക്കിയോ?"),
 ("V","V","ഷഹാനേ, ഈടായി കൊടുക്കാൻ വീടോ സ്ഥലമോ ഇല്ല. അതുകൊണ്ട് ആ സ്വപ്നം മാറ്റിവെച്ചു."),
 ("A","A","ആദ്യം യൂണിറ്റിന് ഉദ്യം എടുക്ക്. ഓൺലൈനാ, ആധാറും PAN-ഉം മതി."),
 ("A","wide","ഉദ്യം മുൻഗണനാ വായ്പയ്ക്കും CGTMSE പോലുള്ള ഈടില്ലാത്ത ലോൺ സ്കീമുകൾക്കും വഴി തുറക്കും. തീരുമാനം ബാങ്കിന്റേത്."),
 ("V","V","അപ്പോ വീടില്ലെന്ന് വെച്ച് വാതിൽ അടയില്ല."),
 ("A","wide","ഈട് വീടല്ല, ആദ്യത്തെ പടി രജിസ്ട്രേഷൻ.")],
 "ഈട് വീടല്ല,\nആദ്യത്തെ പടി\nരജിസ്ട്രേഷൻ", CTA_UDYAM, theme="crm",
 cap_ml="ഗൾഫിലിരുന്ന് നാട്ടിൽ കയർ ചവിട്ടി യൂണിറ്റ് പ്ലാൻ ചെയ്യുന്നയാൾ ഈടായി വീടില്ലാത്തതുകൊണ്ട് ലോൺ സ്വപ്നം മാറ്റിവെച്ചു. ഉദ്യം രജിസ്ട്രേഷൻ മുൻഗണനാ വായ്പയ്ക്കും CGTMSE പോലുള്ള ഈടില്ലാത്ത ലോൺ സ്കീമുകൾക്കും സഹായിക്കും; ലോൺ തീരുമാനിക്കുന്നത് ബാങ്ക്. നിങ്ങൾ ഗൾഫിൽ നിന്ന് മടങ്ങാൻ പ്ലാനുണ്ടോ?",
 cap_en="A Gulf worker planning a coir doormat unit back home shelved the idea because he has no house or land to pledge. Udyam registration helps with priority sector lending and collateral-free loan schemes such as CGTMSE; the bank still decides the loan. Planning to move back from the Gulf: yes or no?",
 cap_mg="Gulf-il irunnu naattil kayar chavitti unit plan cheyyunna aal eedaayi veedillaathathukondu loan swapnam maattivechu. Udyam registration priority lending-inum CGTMSE polulla eedillaatha loan scheme-ukalkkum sahaayikkum; loan theerumaanikkunnathu bank. Ningal Gulf-il ninnu madangaan plan undo?")

# FAQ + d904 pattern: registered as a juice shop (trader) years ago, now bottles tender-coconut water for supermarkets
duo("yd044", "manufacturer", "B", "juiceshop", "ഇപ്പോ ഫാക്ടറി.\nഉദ്യമിൽ ഇപ്പോഴും\n\"ജ്യൂസ് കട\"", [
 ("A","wide","നൗഷാദേ, സൂപ്പർമാർക്കറ്റ് ഇളനീർ കുപ്പിയുടെ പണം രണ്ട് മാസമായി തരുന്നില്ല. 45 ദിവസ നിയമം ഉണ്ടല്ലോ."),
 ("V","V","റസിയേ, നിന്റെ ഉദ്യം കട തുടങ്ങിയ കാലത്ത് എടുത്തതല്ലേ? അതിൽ എന്താ കൊടുത്തിരിക്കുന്നത്?"),
 ("A","A","ചില്ലറ കച്ചവടം. അന്ന് ജ്യൂസ് കട മാത്രമായിരുന്നു."),
 ("V","wide","കച്ചവടക്കാർക്ക് സംരക്ഷണം ഇല്ല. ഇപ്പോ കുപ്പിയിലാക്കുന്ന നിർമാണ യൂണിറ്റാ, ഉദ്യമിലെ വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്യണം."),
 ("A","A","കട വളർന്നു, കടലാസ് വളർന്നില്ല."),
 ("V","wide","ഇളനീർ കുപ്പിയിലായി, ഉദ്യമും പുതുതാകട്ടെ.")],
 "കട വളർന്നു,\nകടലാസ്\nവളർന്നില്ല", CTA_UDYAM, theme="faq",
 cap_ml="ജ്യൂസ് കടയായി തുടങ്ങിയപ്പോൾ ചില്ലറ കച്ചവടം എന്ന് ഉദ്യം എടുത്തു; ഇപ്പോ സൂപ്പർമാർക്കറ്റിന് ഇളനീർ കുപ്പിയിലാക്കി കൊടുക്കുന്നു. കച്ചവടക്കാർക്ക് ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം, 45 ദിവസ സംരക്ഷണം ഇല്ല. ബിസിനസ് മാറിയാൽ ഉദ്യമിലെ വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്യണം; പുതുക്കൽ ഇല്ല. നിങ്ങളുടെ ഉദ്യം അവസാനം നോക്കിയത് എന്ന്?",
 cap_en="A juice shop registered on Udyam as a retail trader years ago; today it bottles tender-coconut water for supermarkets. Traders get Udyam only for priority sector lending, without the 45-day payment protection, and Udyam has no renewal but its details must be kept up to date when the business changes. When did you last check your Udyam details?",
 cap_mg="Juice kada aayi thudangiyappol chillara kachavadam ennu Udyam eduthu; ippo supermarket-inu ilaneer kuppiyilaakki kodukkunnu. Kachavadakkaarkku Udyam priority lending-inu maathram, 45 divasa samrakshanam illa. Business maariyaal Udyam-ile vivarangal update cheyyanam; renewal illa. Ningalude Udyam avasaanam nokkiyathu ennu?")
