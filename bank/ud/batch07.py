# Udyam / MSME batch 07 (28 Nov night). Max 6 lines, painful moment or myth first, payoff by line 4-5, short forwardable punch.
# Fix-it reels on unpaid invoices, each a situation not used in batch01-06. Names, sectors, towns and numbers invented.
# Facts only from topics.FACTS_UD. Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

# FAQ F19 turned around: turnover is under the small limit but investment crossed 25 crore -> medium, so no 45-day protection
duo("yd045", "manufacturer", "A", "mall", "\"ടേൺഓവർ 90 കോടി.\nനമ്മൾ സ്മോൾ.\n45 ദിവസം നമുക്കും\"", [
 ("V","wide","ഷെറിൻ, ആശുപത്രി ചെയിൻ ഗ്ലൗസിന്റെ പണം 70 ദിവസമായി തന്നില്ല. ടേൺഓവർ 90 കോടിയല്ലേ, നമ്മൾ സ്മോൾ. 45 ദിവസ നിയമം പറയാം."),
 ("A","A","ഇർഫാനേ, ടേൺഓവർ മാത്രം നോക്കിയാൽ പോരാ. പുതിയ ലൈനിന് ശേഷം മെഷീനിൽ എത്ര ഇട്ടു?"),
 ("V","V","എല്ലാം കൂടി ഏകദേശം 30 കോടി."),
 ("A","wide","സ്മോൾ ആകാൻ നിക്ഷേപം 25 കോടി വരെയും ടേൺഓവർ 100 കോടി വരെയും വേണം. ഒന്ന് കടന്നാൽ മീഡിയം."),
 ("A","A","45 ദിവസ സംരക്ഷണം മൈക്രോയ്ക്കും സ്മോളിനും മാത്രം. നമുക്ക് ഇനി കരാറിലെ വ്യവസ്ഥ തന്നെ ശ്രദ്ധിക്കണം."),
 ("V","wide","അപ്പോ ഒരു സംഖ്യ കണ്ട് സന്തോഷിച്ചതാ തെറ്റ്.")],
 "ഒരു സംഖ്യ നോക്കി\nനിയമം പറയരുത്", CTA_MSME, names=("ഷെറിൻ", "ഇർഫാൻ"), theme="faq",
 cap_ml="ടേൺഓവർ 90 കോടി മാത്രമുള്ള ഗ്ലൗസ് ഫാക്ടറി സ്മോൾ ആണെന്ന് കരുതി 45 ദിവസ നിയമം പറയാൻ ഒരുങ്ങി. പക്ഷേ മെഷീനിൽ 30 കോടി; നിക്ഷേപം 25 കോടി കടന്നാൽ മീഡിയം. രണ്ട് പരിധിയും പാലിക്കണം, ഒന്ന് കടന്നാൽ മുകളിലെ ക്ലാസ്; 45 ദിവസ സംരക്ഷണം മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക് മാത്രം. നിങ്ങൾ രണ്ട് സംഖ്യയും നോക്കിയോ?",
 cap_en="A glove factory with 90 crore turnover thought it was small and planned to quote the 45-day rule. But it has 30 crore in machinery, and crossing 25 crore of investment makes it medium. Both limits must be met, crossing either moves you up, and the 45-day protection is only for micro and small units. Did you check both numbers?",
 cap_mg="Turnover 90 crore maathramulla glove factory small aanennu karuthi 45 divasa niyamam parayaan orungi. Pakshe machine-il 30 crore; investment 25 crore kadannaal medium. Randu paridhiyum paalikkanam, onnu kadannaal mukalile class; 45 divasa samrakshanam micro, small unit-ukalkku maathram. Ningal randu sankhyayum nokkiyo?")

# NEW (fix-it, afraid of losing the client): a polite written reminder with the Udyam number and the 43B(h) line, then MSME Samadhaan
duo("yd046", "service_unit", "B", "teashop", "\"വഴക്കിട്ടാൽ\nഅടുത്ത ഓർഡർ പോകും\"\n60 ദിവസം, ഒരു ബിൽ", [
 ("A","wide","ജിതിനേ, ജ്വല്ലറിയിലെ ക്യാമറ പണി കഴിഞ്ഞ് 60 ദിവസമായില്ലേ? പണം വന്നോ?"),
 ("V","V","ആരതീ, ഇല്ല. വഴക്കിട്ടാൽ അടുത്ത ബ്രാഞ്ചിന്റെ ഓർഡർ പോകും. അതാ പേടി."),
 ("A","A","വഴക്ക് വേണ്ട. മാന്യമായ ഒരു മെയിൽ മതി. ഉദ്യം നമ്പർ, ബിൽ തീയതി, സമ്മതിച്ച ദിവസം എഴുതണം."),
 ("A","wide","ഒരു വരി കൂടി: മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് വൈകി കൊടുത്താൽ, കൊടുക്കും വരെ ആ ചെലവിന് അവർക്ക് ടാക്സ് കിഴിവ് കിട്ടില്ല."),
 ("V","V","എന്നിട്ടും അനങ്ങിയില്ലെങ്കിൽ?"),
 ("A","wide","MSME സമാധാൻ പോർട്ടലിൽ പരാതി. ആദ്യം മര്യാദ, പിന്നെ പോർട്ടൽ.")],
 "ആദ്യം മര്യാദയുള്ള മെയിൽ,\nപിന്നെ സമാധാൻ", CTA_UDYAM, names=("ആരതി", "ജിതിൻ"), theme="new",
 cap_ml="ജ്വല്ലറിയിൽ ക്യാമറ വെച്ച സർവീസ് യൂണിറ്റിന് 60 ദിവസമായി പണം ഇല്ല, വഴക്കിട്ടാൽ അടുത്ത ഓർഡർ പോകുമെന്ന് പേടി. ആദ്യം ഉദ്യം നമ്പറും ബിൽ തീയതിയും സമ്മതിച്ച ദിവസവും വെച്ച് മാന്യമായ മെയിൽ; 43B(h) പ്രകാരം വൈകി കൊടുക്കുന്ന ബയർക്ക് കൊടുക്കും വരെ ടാക്സ് കിഴിവ് ഇല്ല. പിന്നെയും ഇല്ലെങ്കിൽ MSME സമാധാൻ. ഈ മെയിൽ ആർക്കാ അയക്കേണ്ടത്?",
 cap_en="A service unit that installed cameras at a jewellery store has waited 60 days and fears losing the next order if it fights. Step one is a polite mail with the Udyam number, invoice date and agreed days, plus one line: under section 43B(h) a buyer who pays a micro or small supplier late loses the tax deduction until it pays. Still nothing? A complaint on MSME Samadhaan. Who needs this mail?",
 cap_mg="Jewellery-il camera vecha service unit-inu 60 divasamaayi panam illa, vazhakkittaal adutha order pokumennu pedi. Aadyam Udyam number-um bill theeyathiyum sammathicha divasavum vechu maanyamaaya mail; 43B(h) prakaaram vaiki kodukkunna buyer-kku kodukkum vare tax kizhivu illa. Pinneyum illenkil MSME Samadhaan. Ee mail aarkkaa ayakkendathu?")

# CRM (service business with corporate clients): lorry transport for a cement distributor, "hire is not MSME"
duo("yd047", "service_unit", "A", "railway", "\"ലോറി വാടകയല്ലേ?\nഅതിനെന്ത്\nMSME നിയമം?\"", [
 ("A","wide","റഷീദേ, ഗുഡ്സ് യാർഡിൽ നിന്ന് സിമന്റ് കയറ്റുന്ന നിന്റെ നാല് ലോറിയുടെ പണം ഡിസ്ട്രിബ്യൂട്ടർ തീർത്തോ?"),
 ("V","V","ഷൈനീ, 80 ദിവസമായി. ചോദിച്ചപ്പോൾ പറയുന്നു, ലോറി വാടക മാത്രമല്ലേ, MSME നിയമം ഫാക്ടറിക്കാ എന്ന്."),
 ("A","A","അത് അവരുടെ സൗകര്യത്തിനുള്ള നിയമം. സർവീസ് യൂണിറ്റും MSME ആണ്."),
 ("A","wide","ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിനും കരാറില്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിൽ പരമാവധി 45. പിന്നെ കൂട്ടുപലിശ."),
 ("V","V","അപ്പോ എന്റെ ലോറിയും ഒരു യൂണിറ്റാ."),
 ("A","wide","ചക്രം കറങ്ങുന്നതും സർവീസ് തന്നെ.")],
 "ചക്രം കറങ്ങുന്നതും\nസർവീസ് തന്നെ", CTA_UDYAM, names=("ഷൈനി", "റഷീദ്"), theme="crm",
 cap_ml="ഗുഡ്സ് യാർഡിൽ നിന്ന് സിമന്റ് കയറ്റുന്ന നാല് ലോറിയുടെ പണം 80 ദിവസമായി കിട്ടിയില്ല; ഡിസ്ട്രിബ്യൂട്ടർ പറയുന്നത് MSME നിയമം ഫാക്ടറിക്ക് മാത്രമെന്ന്. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിനും ബയർ 15 ദിവസത്തിൽ, കരാറുണ്ടെങ്കിൽ പരമാവധി 45 ദിവസത്തിൽ പണം തരണം; പിന്നെ RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. നിങ്ങളുടേത് സർവീസ് യൂണിറ്റാണോ?",
 cap_en="A four-lorry transport business has waited 80 days for a cement distributor, who says MSME rules are only for factories. Udyam-registered micro and small service units are covered too: the buyer must pay within 15 days, or the agreed time up to 45 days, and then owes compound interest at three times the RBI bank rate. Is yours a service unit?",
 cap_mg="Goods yard-il ninnu cement kayattunna naalu lorry-yude panam 80 divasamaayi kittiyilla; distributor parayunnathu MSME niyamam factory-kku maathramennu. Udyam ulla micro, small service unit-inum buyer 15 divasathil, karaarundenkil maximum 45 divasathil panam tharanam; pinne RBI bank rate-inte moonnirratti koottupalisha. Ningaludethu service unit aano?")

# FAQ F17 (wants to complain, never registered): a steel-trolley maker learns the protection is for Udyam micro / small units; register first
duo("yd048", "manufacturer", "C", "kitchen", "\"45 ദിവസ നിയമം\nഎനിക്കും വേണം\"\nഉദ്യം? \"അതെന്താ?\"", [
 ("V","wide","ദേവികേ, ബിൽഡർ ട്രോളിയുടെ പണം മൂന്ന് മാസമായി പിടിച്ചുവെച്ചിരിക്കുന്നു. 45 ദിവസ നിയമം പറഞ്ഞ് ഞാനും പരാതി കൊടുക്കും."),
 ("A","A","ഫെബിനേ, നല്ലത്. നിന്റെ ഉദ്യം നമ്പർ എന്താ?"),
 ("V","V","ഉദ്യമോ? അത് വലിയ കമ്പനികൾക്കുള്ള എന്തോ അല്ലേ?"),
 ("A","wide","ഉദ്യം സർക്കാരിന്റെ MSME രജിസ്ട്രേഷനാ. ഓൺലൈൻ, ആധാർ വെച്ച്, PAN-ഉം, ഉണ്ടെങ്കിൽ GSTIN-ഉം, സ്വയം പ്രഖ്യാപനം."),
 ("A","A","45 ദിവസ നിയമവും സമാധാൻ പരാതിയും പറയുന്നത് ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾ. ആദ്യം നമ്പർ, പിന്നെ പരാതി."),
 ("V","wide","അപ്പോ ഇന്ന് ട്രോളി അല്ല, ഉദ്യം.")],
 "പരാതിക്ക് മുമ്പ്\nഉദ്യം നമ്പർ", CTA_UDYAM, names=("ദേവിക", "ഫെബിൻ"), theme="faq",
 cap_ml="സ്റ്റീൽ കിച്ചൺ ട്രോളി ഉണ്ടാക്കുന്നയാൾ 45 ദിവസ നിയമം കേട്ട് പരാതിക്ക് ഒരുങ്ങി, പക്ഷേ ഉദ്യം ഇല്ല. ഉദ്യം സർക്കാരിന്റെ MSME രജിസ്ട്രേഷൻ: ഓൺലൈൻ, ആധാർ അടിസ്ഥാനം, PAN, ഉണ്ടെങ്കിൽ GSTIN, സ്വയം പ്രഖ്യാപനം. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റുകൾക്കാണ് 45 ദിവസ സംരക്ഷണവും സമാധാൻ വഴിയും. നിങ്ങൾക്ക് ഉദ്യം നമ്പർ ഉണ്ടോ?",
 cap_en="A steel kitchen-trolley maker heard about the 45-day rule and got ready to complain, but had no Udyam registration. Udyam is the government's MSME registration: online, Aadhaar-based, with PAN and GSTIN where there is one, on self-declaration. The 45-day protection and the MSME Samadhaan route are for micro and small manufacturing and service units. Do you have an Udyam number?",
 cap_mg="Steel kitchen trolley undaakkunna aal 45 divasa niyamam kettu paraathikku orungi, pakshe Udyam illa. Udyam sarkkaarinte MSME registration: online, Aadhaar adisthaanam, PAN, undenkil GSTIN, swayam prakhyaapanam. Udyam ulla micro, small nirmaana, service unit-ukalkkaanu 45 divasa samrakshanavum Samadhaan vazhiyum. Ningalkku Udyam number undo?")

# FAQ (buyer's excuse): "your certificate says small, the 45-day rule is only for micro"; it covers micro and small alike
duo("yd049", "supplier_unpaid", "B", "office", "ബയർ: \"നിങ്ങൾ സ്മോൾ\nആണല്ലോ. 45 ദിവസം\nമൈക്രോയ്ക്ക് മാത്രം\"", [
 ("V","wide","അനഘേ, ബോക്സ് ഓർഡറിന്റെ പണം ചോദിച്ചപ്പോൾ അവരുടെ ഫിനാൻസ് ടീം നമ്മുടെ ഉദ്യം സർട്ടിഫിക്കറ്റ് നോക്കി ചിരിച്ചു."),
 ("A","A","നിതിനേ, എന്താ അവർ പറഞ്ഞത്?"),
 ("V","V","നമ്മൾ സ്മോൾ ആണ്, 45 ദിവസ നിയമം മൈക്രോയ്ക്ക് മാത്രം എന്ന്."),
 ("A","wide","തെറ്റ്. നിർമാണ, സർവീസ് മൈക്രോ യൂണിറ്റിനും സ്മോൾ യൂണിറ്റിനും ഒരേ നിയമം. സമ്മതിച്ച സമയം കഴിഞ്ഞാൽ കൂട്ടുപലിശ."),
 ("V","V","അപ്പോ ചിരിക്കേണ്ടത് അവരല്ല."),
 ("A","wide","സർട്ടിഫിക്കറ്റ് അവർ വായിച്ചു, നിയമം നമ്മൾ വായിക്കണം.")],
 "സ്മോൾ ആയാലും\nഅവകാശം ചെറുതല്ല", CTA_MSME, names=("അനഘ", "നിതിൻ"), theme="faq",
 cap_ml="കോറുഗേറ്റഡ് ബോക്സ് യൂണിറ്റിന്റെ ഉദ്യം സർട്ടിഫിക്കറ്റിൽ 'സ്മോൾ' എന്ന് കണ്ട ബയർ 45 ദിവസ നിയമം മൈക്രോയ്ക്ക് മാത്രമെന്ന് പറഞ്ഞു. തെറ്റ്: ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റുകൾക്ക് ഒരേ സംരക്ഷണം; സമ്മതിച്ച സമയം കഴിഞ്ഞാൽ RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. നിങ്ങളുടെ സർട്ടിഫിക്കറ്റിൽ ഏത് ക്ലാസാ?",
 cap_en="A buyer saw 'small' on a box maker's Udyam certificate and said the 45-day rule is only for micro units. Wrong: micro and small manufacturing and service units get the same protection, and after the agreed time the buyer owes compound interest at three times the RBI bank rate. Which class does your certificate show?",
 cap_mg="Corrugated box unit-inte Udyam certificate-il 'small' ennu kanda buyer 45 divasa niyamam micro-kku maathramennu paranju. Thettu: Udyam ulla micro, small nirmaana, service unit-ukalkku ore samrakshanam; sammathicha samayam kazhinjaal RBI bank rate-inte moonnirratti koottupalisha. Ningalude certificate-il ethu class aa?")

# CRM (Gulf returnee's unit): resort pays with a cheque dated four months later; a later cheque date does not stretch the 45-day limit
duo("yd050", "supplier_unpaid", "A", "home", "40 കട്ടിൽ കൊടുത്തു.\nകിട്ടിയത് നാല് മാസം\nകഴിഞ്ഞുള്ള ചെക്ക്", [
 ("A","wide","ജോർജേ, റിസോർട്ടിലേക്ക് 40 തേക്ക് കട്ടിൽ കൊടുത്തതിന്റെ പണം കിട്ടിയോ?"),
 ("V","V","ഡെൽനേ, കിട്ടി, ചെക്കായി. തീയതി നാല് മാസം കഴിഞ്ഞിട്ട്. അതാ അവരുടെ രീതി എന്ന്."),
 ("A","A","രീതി അവരുടേത്, നിയമം എല്ലാവരുടേതും."),
 ("A","wide","ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റിന് സമ്മതിക്കാവുന്ന സമയം പരമാവധി 45 ദിവസം. ചെക്കിലെ തീയതി കൊണ്ട് അത് നീളില്ല."),
 ("V","V","അപ്പോ അതിന് ശേഷമുള്ള ദിവസങ്ങൾക്ക്?"),
 ("A","wide","RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. തീയതി എഴുതിയാൽ നിയമം മാറില്ല.")],
 "ചെക്കിൽ തീയതി മാറ്റാം,\nനിയമം മാറില്ല", CTA_MSME, names=("ഡെൽന", "ജോർജ്"), theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചുവന്ന് തുടങ്ങിയ ഫർണിച്ചർ യൂണിറ്റ് റിസോർട്ടിന് 40 തേക്ക് കട്ടിൽ കൊടുത്തു; കിട്ടിയത് നാല് മാസം കഴിഞ്ഞുള്ള തീയതിയിട്ട ചെക്ക്. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റിന് ബയർ സമ്മതിക്കാവുന്ന സമയം പരമാവധി 45 ദിവസം; അത് കഴിഞ്ഞാൽ RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ. നിങ്ങൾക്ക് ഇങ്ങനെ ഒരു ചെക്ക് കിട്ടിയിട്ടുണ്ടോ?",
 cap_en="A furniture unit started by a Gulf returnee supplied 40 teak cots to a resort and got a cheque dated four months later. For an Udyam-registered micro or small unit the agreed time can be at most 45 days; after that the buyer owes compound interest at three times the RBI bank rate. A later date on the cheque does not stretch that. Ever been handed a cheque like this?",
 cap_mg="Gulf-il ninnu thirichuvannu thudangiya furniture unit resort-inu 40 thekku kattil koduthu; kittiyathu naalu maasam kazhinjulla theeyathiyitta cheque. Udyam ulla micro, small unit-inu buyer sammathikkaavunna samayam maximum 45 divasam; athu kazhinjaal RBI bank rate-inte moonnirratti koottupalisha. Ningalkku ingane oru cheque kittiyittundo?")

# NEW: chips made by the family's micro unit, but invoiced through the brother's wholesale shop (a trader): that bill gets no 45-day protection
duo("yd051", "manufacturer", "C", "gulf", "ചിപ്സ് ഉണ്ടാക്കുന്നത്\nനമ്മൾ. ബിൽ പോകുന്നത്\nഅനിയന്റെ കടയിൽ നിന്ന്", [
 ("A","wide","സലീമേ, നാട്ടിലെ ചിപ്സ് യൂണിറ്റിന് സൂപ്പർമാർക്കറ്റ് പണം തരാതെ 90 ദിവസമായില്ലേ? 45 ദിവസ നിയമം പറഞ്ഞില്ലേ?"),
 ("V","V","ഷാനവാസേ, പറഞ്ഞു. പക്ഷേ ബിൽ പോകുന്നത് അനിയന്റെ ഹോൾസെയിൽ കടയുടെ പേരിലാ. കണക്ക് എളുപ്പത്തിന്."),
 ("A","A","അവിടെയാ കുരുക്ക്. ആ കട ഉദ്യമിൽ കച്ചവടമല്ലേ?"),
 ("A","wide","കച്ചവടക്കാർക്ക് ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം. 45 ദിവസ സംരക്ഷണം ഉണ്ടാക്കുന്ന മൈക്രോ, സ്മോൾ യൂണിറ്റിനാ."),
 ("V","V","അപ്പോ ഇനി ബിൽ യൂണിറ്റിന്റെ പേരിൽ, ഉദ്യം നമ്പറോടെ."),
 ("A","wide","ഉണ്ടാക്കുന്നവന്റെ പേരിൽ ബിൽ, എങ്കിലേ നിയമം കൂടെ.")],
 "ഉണ്ടാക്കുന്നവന്റെ\nപേരിൽ ബിൽ", CTA_MSME, names=("ഷാനവാസ്", "സലീം"), theme="new",
 cap_ml="കുടുംബത്തിന്റെ ചിപ്സ് യൂണിറ്റ് ഉണ്ടാക്കുന്നു, പക്ഷേ സൂപ്പർമാർക്കറ്റിലേക്കുള്ള ബിൽ പോകുന്നത് അനിയന്റെ ഹോൾസെയിൽ കടയുടെ പേരിൽ. കച്ചവടക്കാർക്ക് ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം; 45 ദിവസ സംരക്ഷണം നിർമാണ, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക്. നിങ്ങളുടെ ബിൽ ആരുടെ പേരിലാ പോകുന്നത്?",
 cap_en="The family's micro unit makes the chips, but the invoices to the supermarket go out in the name of the brother's wholesale shop. Traders can register on Udyam only for priority sector lending; the 45-day payment protection is for micro and small manufacturing and service units. Whose name is on your invoice?",
 cap_mg="Kudumbathinte chips unit undaakkunnu, pakshe supermarket-ilekkulla bill pokunnathu aniyante wholesale kadayude peril. Kachavadakkaarkku Udyam priority lending-inu maathram; 45 divasa samrakshanam nirmaana, service micro, small unit-ukalkku. Ningalude bill aarude perilaa pokunnathu?")
