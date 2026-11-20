# Udyam / MSME batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_UD. Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

duo("yd016", "loan_seeker", "A", "tailor", "12 തയ്യൽ മെഷീൻ.\n\"ഇത്ര ചെറുതിന്\nMSME ഒക്കെ ഉണ്ടോ?\"", [
 ("A","wide","മോഹനേട്ടാ, യൂണിഫോം തയ്ക്കാൻ 12 മെഷീൻ ഉണ്ട്. 8 എണ്ണം കൂടി വാങ്ങാൻ ബാങ്കിൽ ചെന്നപ്പോൾ ഉദ്യം ചോദിച്ചു."),
 ("V","V","ഉഷേ, ഇതുവരെ ഉദ്യം എടുത്തില്ലേ?"),
 ("A","A","അത് വലിയ ഫാക്ടറികൾക്കല്ലേ? എന്റേത് ഒരു മുറിയിലെ യൂണിറ്റാ."),
 ("V","wide","മൈക്രോ എന്നാൽ നിക്ഷേപം രണ്ടര കോടി വരെ, ടേൺഓവർ 10 കോടി വരെ. മുൻഗണനാ വായ്പയ്ക്ക് ഉദ്യം സഹായിക്കും."),
 ("A","A","അപ്പോ ലോൺ ഉറപ്പ്?"),
 ("V","wide","ലോൺ ബാങ്ക് തീരുമാനിക്കും. പക്ഷേ ചെറുതായതുകൊണ്ടാ നീ മൈക്രോ.")],
 "ചെറുതായതുകൊണ്ട്\nപുറത്തല്ല, ചെറുതായ\nതുകൊണ്ടാ മൈക്രോ", CTA_UDYAM, theme="crm",
 cap_ml="12 മെഷീനുള്ള യൂണിഫോം യൂണിറ്റ് \"MSME വലിയവർക്ക്\" എന്ന് കരുതി ഉദ്യം എടുത്തില്ല. മൈക്രോ എന്നാൽ നിക്ഷേപം രണ്ടര കോടി വരെയും ടേൺഓവർ 10 കോടി വരെയും. ഉദ്യം മുൻഗണനാ വായ്പയ്ക്ക് സഹായിക്കും, ലോൺ തീരുമാനിക്കുന്നത് ബാങ്ക്. നിങ്ങളുടെ യൂണിറ്റ് മൈക്രോയാണോ?",
 cap_en="A 12-machine uniform stitching unit skipped Udyam because it thought MSME means big factories. Micro means investment up to Rs 2.5 crore and turnover up to Rs 10 crore, and Udyam helps with priority sector lending; the bank still decides the loan. Is your unit micro: yes or no?",
 cap_mg="12 machine ulla uniform unit 'MSME valiyavarkku' ennu karuthi Udyam eduthilla. Micro ennaal investment randara crore vare, turnover 10 crore vare. Udyam munganana vaaypaykku sahaayikkum, loan theerumaanikkunnathu bank. Ningalude unit micro aano?")

duo("yd017", "supplier_unpaid", "B", "courier", "\"ഡേറ്റ് എഴുതിയിട്ടില്ലല്ലോ,\nസൗകര്യം പോലെ\nതരാം\"", [
 ("A","wide","അരവിന്ദേ, ഫർണിച്ചർ സെല്ലർക്ക് 3 മാസം ഡെലിവറി ചെയ്തു. പണം ചോദിച്ചപ്പോൾ, പേമെന്റ് ഡേറ്റ് എഴുതിയിട്ടില്ലല്ലോ എന്ന്."),
 ("V","V","ജയേച്ചീ, നിങ്ങളുടെ ഡെലിവറി യൂണിറ്റിന് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ട്, മൈക്രോ സർവീസ് യൂണിറ്റ്. പക്ഷേ എഗ്രിമെന്റ് ഒന്നുമില്ല."),
 ("V","wide","എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസത്തിനുള്ളിൽ തരണം. എഴുതിയാലും പരമാവധി 45 ദിവസം."),
 ("A","A","അപ്പോ എഴുതാത്തത് അവർക്കാ നഷ്ടം."),
 ("V","wide","ഡേറ്റ് നിങ്ങൾ എഴുതിയില്ലെങ്കിൽ, നിയമം എഴുതും: 15.")],
 "ഡേറ്റ് എഴുതിയില്ലെങ്കിൽ\nനിയമം എഴുതും: 15", CTA_MSME, theme="faq",
 cap_ml="പേമെന്റ് ഡേറ്റ് എഴുതിയിട്ടില്ലെങ്കിൽ ബയർക്ക് ഇഷ്ടം പോലെ തരാമോ? ഇല്ല. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റിന് എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിലും പരമാവധി 45. നിങ്ങളുടെ ബില്ലുകളിൽ ഡേറ്റ് ഉണ്ടോ?",
 cap_en="A delivery service unit's client says there was no written payment date, so it will pay whenever. Not so: for Udyam-registered micro and small manufacturing and service units, the buyer must pay within 15 days without an agreement, and within 45 days at most with one. Do your invoices carry a payment date?",
 cap_mg="Payment date ezhuthiyittillenkil buyer-kku ishtam pole tharaamo? Illa. Udyam ulla micro, small manufacturing, service unit-inu agreement illenkil 15 divasam, undenkilum maximum 45. Ningalude bill-il date undo?")

duo("yd018", "supplier_unpaid", "C", "akshaya", "കയർ മാറ്റിന്റെ പണം\n80 ദിവസം. \"കേസിന്\nപോയാൽ വർഷങ്ങൾ\"", [
 ("A","wide","രമേശേ, ആ റിസോർട്ട് ഗ്രൂപ്പ് കയർ മാറ്റിന്റെ പണം 80 ദിവസമായി തന്നിട്ടില്ല. കേസിന് പോയാൽ വർഷങ്ങൾ എടുക്കില്ലേ?"),
 ("V","V","സുധേച്ചീ, നമ്മുടേത് ഉദ്യം ഉള്ള മൈക്രോ യൂണിറ്റല്ലേ?"),
 ("A","A","അതേ. പക്ഷേ വക്കീലും കോടതിയും ഒന്നും നമുക്ക് പറ്റില്ല."),
 ("V","wide","ആദ്യപടി വക്കീലല്ല. MSME സമാധാൻ പോർട്ടലിൽ പരാതി. അത് ഫെസിലിറ്റേഷൻ കൗൺസിലിലേക്ക് പോകും."),
 ("A","A","അപ്പോ ഇവിടെ ഇരുന്ന് ഓൺലൈനായി തുടങ്ങാം."),
 ("V","wide","കോടതി കയറും മുമ്പ് പോർട്ടൽ കയറാം.")],
 "കോടതി കയറും മുമ്പ്\nപോർട്ടൽ കയറാം", CTA_MSME, theme="faq",
 cap_ml="വലിയ ബയർ പണം തരാതിരുന്നാൽ ആദ്യം കോടതിയല്ല. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റുകൾക്ക് MSME സമാധാൻ പോർട്ടലിൽ പരാതി കൊടുക്കാം, ഫെസിലിറ്റേഷൻ കൗൺസിൽ കേൾക്കും. ഈ പോർട്ടൽ അറിയാമായിരുന്നോ?",
 cap_en="A coir mat unit has waited 80 days for a resort group's payment and fears a court case would take years. The first step is not a lawyer: Udyam-registered micro and small manufacturing and service units can complain on the MSME Samadhaan portal, which goes to the facilitation council. Had you heard of this portal: yes or no?",
 cap_mg="Valiya buyer panam tharaathirunnaal aadyam court alla. Udyam ulla micro, small manufacturing, service units-nu MSME Samadhaan portal-il paraathi kodukkaam, facilitation council kelkkum. Ee portal ariyaamaayirunno?")

duo("yd019", "trader_ud", "A", "mobileshop", "\"കച്ചവടക്കാർക്ക്\nഉദ്യമേ ഇല്ല\"\n2021-ൽ മാറി", [
 ("A","wide","ഫഹദേ, കവറും കേബിളും ഹോൾസെയിൽ കൊടുക്കുന്ന നമ്മളെപ്പോലുള്ളവർക്ക് ഉദ്യം കിട്ടില്ലെന്നാ അയൽക്കട പറഞ്ഞത്."),
 ("V","V","ഹന്നാ, അത് പഴയ കഥ. 2021 ജൂലൈ മുതൽ റീട്ടെയിൽ, ഹോൾസെയിൽ കച്ചവടക്കാർക്കും ഉദ്യം എടുക്കാം."),
 ("A","A","അപ്പോ കടക്കാർ പണം വൈകിച്ചാൽ 45 ദിവസ നിയമവും നമുക്കുണ്ടോ?"),
 ("V","wide","അതില്ല. കച്ചവടക്കാർക്ക് മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം. 45 ദിവസം നിർമാണ, സർവീസ് യൂണിറ്റുകൾക്കാ."),
 ("A","A","ഒരു വാതിൽ മാത്രം തുറക്കും, അല്ലേ?"),
 ("V","wide","ഒരു വാതിൽ മതി, അത് ബാങ്കിന്റേതാണെങ്കിൽ.")],
 "ഒരു വാതിൽ മതി,\nഅത് ബാങ്കിന്റേതാണെങ്കിൽ", CTA_UDYAM, theme="faq",
 cap_ml="കച്ചവടക്കാർക്ക് ഉദ്യം കിട്ടില്ല എന്നത് പഴയ കഥ. 2021 ജൂലൈ മുതൽ റീട്ടെയിൽ, ഹോൾസെയിൽ കച്ചവടക്കാർക്കും രജിസ്റ്റർ ചെയ്യാം, പക്ഷേ മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം; 45 ദിവസ പേമെന്റ് സംരക്ഷണം ഇല്ല. നിങ്ങൾ റീട്ടെയിലോ ഹോൾസെയിലോ?",
 cap_en="A mobile accessories wholesaler was told traders can't get Udyam at all. Since July 2021, retail and wholesale traders can register, but only for priority sector lending; the 45-day payment protection is for manufacturing and service units. Are you retail or wholesale?",
 cap_mg="Kachavadakkaarkku Udyam kittilla ennathu pazhaya katha. 2021 July muthal retail, wholesale traders-num register cheyyaam, pakshe munganana vaaypaykku maathram; 45 divasa payment protection illa. Ningal retail-o wholesale-o?")

duo("yd020", "service_unit", "B", "rooftop", "ഉത്സവ ലൈറ്റ് അണഞ്ഞു.\n\"ലൈറ്റുകാരന്\nMSME ഉണ്ടോ?\"", [
 ("A","wide","ശ്യാമേ, ഉത്സവത്തിന് ലൈറ്റും സൗണ്ടും ചെയ്തിട്ട് ഇവന്റ് കമ്പനി 60 ദിവസമായി പണം തന്നില്ല, അല്ലേ?"),
 ("V","V","ആര്യേ, ഉദ്യം ഒക്കെ ഫാക്ടറിക്കാർക്കാ. ഞാൻ വെറും ലൈറ്റ് ചേട്ടൻ."),
 ("A","A","സർവീസ് യൂണിറ്റിനും ഉദ്യം എടുക്കാം. നിന്റെ ലൈറ്റും സൗണ്ടും സർവീസാ."),
 ("V","wide","അതുകൊണ്ട് എന്ത് കിട്ടും?"),
 ("A","A","മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് 45 ദിവസത്തിനുള്ളിൽ പണം. പിന്നെ ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ."),
 ("V","wide","ഉത്സവം കഴിഞ്ഞാൽ ലൈറ്റ് അണയും. ബിൽ അണയരുത്.")],
 "ലൈറ്റ് അണയും,\nബിൽ അണയരുത്", CTA_UDYAM, theme="new",
 cap_ml="ഉത്സവങ്ങൾക്ക് ലൈറ്റും സൗണ്ടും ചെയ്യുന്നവരും സർവീസ് യൂണിറ്റാണ്, ഉദ്യം എടുക്കാം. ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് 45 ദിവസത്തിനുള്ളിൽ പണം കിട്ടണം, വൈകിയാൽ ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ. നിങ്ങളുടെ ജോലി സർവീസോ നിർമാണമോ?",
 cap_en="A festival lighting and sound operator thinks Udyam is only for factories. Service units can register too, and Udyam-registered micro and small service units must be paid within 45 days at most, or the buyer owes compound interest at three times the RBI bank rate. Your work: service or manufacturing?",
 cap_mg="Utsavangalkku light-um sound-um cheyyunnavarum service unit aanu, Udyam edukkaam. Udyam ulla micro, small service unit-inu 45 divasathinullil panam kittanam, vaikiyaal bank nirakkinte 3 iratti koottupalisha. Ningalude joli service-o manufacturing-o?")

duo("yd021", "manufacturer", "C", "veranda", "പ്ലാന്റ് വലുതായി.\n\"ഇനി നമ്മൾ\nMSME അല്ലേ?\"", [
 ("A","wide","ബാലേട്ടാ, പുതിയ പ്ലാന്റ് വന്നാൽ വെളിച്ചെണ്ണ മില്ലിന്റെ നിക്ഷേപം 30 കോടിയാകും. നമ്മൾ MSME-യിൽ നിന്ന് പുറത്താകുമോ?"),
 ("V","V","ശാന്തേ, സ്മോളിന്റെ ലിമിറ്റ് നിക്ഷേപം 25 കോടി, ടേൺഓവർ 100 കോടി. അത് നമ്മൾ കടക്കും."),
 ("A","A","അപ്പോ പുറത്ത്."),
 ("V","wide","അല്ല. മീഡിയം: നിക്ഷേപം 125 കോടി വരെ, ടേൺഓവർ 500 കോടി വരെ. അതും MSME തന്നെ. ഉദ്യമിലെ വിവരം പുതുക്കണം."),
 ("A","A","എന്തെങ്കിലും മാറുമോ?"),
 ("V","wide","45 ദിവസ നിയമം മൈക്രോയ്ക്കും സ്മോളിനും മാത്രം. പക്ഷേ മീഡിയവും MSME-യിലെ ഒരു അക്ഷരമാ.")],
 "മീഡിയവും\nMSME-യിലെ\nഒരു അക്ഷരമാണ്", CTA_MSME, theme="crm",
 cap_ml="വളരുന്ന യൂണിറ്റ് സ്മോൾ ലിമിറ്റ് കടന്നാൽ MSME-യിൽ നിന്ന് പുറത്താകില്ല. നിക്ഷേപം 125 കോടി വരെയും ടേൺഓവർ 500 കോടി വരെയും മീഡിയം. പക്ഷേ 45 ദിവസ പേമെന്റ് സംരക്ഷണം മൈക്രോയ്ക്കും സ്മോളിനും മാത്രം. നിങ്ങളുടെ ബിസിനസ് ഈ വർഷം വളർന്നോ?",
 cap_en="A family coconut oil mill expanding to Rs 30 crore of investment fears it will drop out of MSME. It won't: medium means investment up to Rs 125 crore and turnover up to Rs 500 crore, and it is still MSME, though the 45-day payment protection is only for micro and small units. Update your Udyam details when you move up. Did your business grow this year?",
 cap_mg="Valarunna unit small limit kadannaal MSME-yil ninnu purathaakilla. Investment 125 crore vareyum turnover 500 crore vareyum medium. Pakshe 45 divasa payment protection micro-kkum small-inum maathram. Ningalude business ee varsham valarnno?")

duo("yd022", "supplier_unpaid", "A", "beach", "4 മാസം കഴിഞ്ഞ് ബയർ:\n\"കുറച്ച് പലിശ കൂടി\nതരാം, പോരേ?\"", [
 ("A","wide","നിഖിലേ, ബോട്ട് കമ്പനി വലയുടെ പണം 4 മാസമായി തന്നില്ല. ഇപ്പോ പറയുന്നു, ബാങ്ക് ഡെപ്പോസിറ്റ് പോലെ കുറച്ച് പലിശ തരാമെന്ന്."),
 ("V","V","ദിവ്യേ, നിന്റെ വല നെയ്ത്ത് യൂണിറ്റിന് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ട്, മൈക്രോ. കുറച്ച് പലിശ കിട്ടിയാലും മതിയായിരുന്നു."),
 ("V","wide","കുറച്ചല്ല. 45 ദിവസം കഴിഞ്ഞാൽ RBI ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി, അതും കൂട്ടുപലിശ."),
 ("A","A","അപ്പോ അവരുടെ 'കുറച്ച്' ശരിക്കും കുറച്ചാ."),
 ("V","wide","വല നമ്മൾ നെയ്യും. പലിശ നിയമം നെയ്യും.")],
 "വല നമ്മൾ നെയ്യും,\nപലിശ നിയമം നെയ്യും", CTA_MSME, theme="faq",
 cap_ml="പണം വൈകിച്ച ബയർ \"കുറച്ച് പലിശ\" ഓഫർ ചെയ്താൽ? ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റിന് 45 ദിവസം കഴിഞ്ഞാൽ RBI ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശയാണ് നിയമം. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="A fishing-net weaving unit unpaid for 4 months is offered 'a little interest, like a bank deposit'. The law says more: an Udyam-registered micro or small manufacturer is owed compound interest at three times the RBI bank rate once 45 days have passed. Did you know this: yes or no?",
 cap_mg="Panam vaikicha buyer 'kurachu palisha' offer cheythaal? Udyam ulla micro, small unit-inu 45 divasam kazhinjaal RBI bank nirakkinte 3 iratti koottupalishayaanu niyamam. Ithu ariyaamaayirunno?")

duo("yd023", "manufacturer", "B", "pharmacy", "ടേൺഓവർ 11 കോടി.\n\"ഉദ്യമിൽ 9 എന്ന്\nഎഴുതിയാലോ?\"", [
 ("A","wide","പ്രവീണേ, ഹെർബൽ സോപ്പിന്റെ ടേൺഓവർ ഈ വർഷം 11 കോടി. ഉദ്യമിൽ 9 എന്ന് എഴുതിയാലോ? സ്വയം സാക്ഷ്യമല്ലേ."),
 ("V","V","സിനീ, മൈക്രോയിൽ തന്നെ നിൽക്കാനാണോ?"),
 ("A","A","അതേ. 10 കടന്നാൽ സ്മോളാകും."),
 ("V","wide","സ്വയം സാക്ഷ്യം എന്നാൽ ശരിയായ വിവരം നമ്മൾ തന്നെ ഉറപ്പിക്കണം. ടേൺഓവർ 10 കോടി കടന്നാൽ സ്മോൾ, ഉദ്യം പുതുക്കണം."),
 ("A","A","സ്മോളായാലും 45 ദിവസ സംരക്ഷണം ഉണ്ടല്ലോ, അല്ലേ?"),
 ("V","wide","ഉണ്ട്. സോപ്പ് പതയട്ടെ, കണക്ക് പതയരുത്.")],
 "സോപ്പ് പതയട്ടെ,\nകണക്ക് പതയരുത്", CTA_MSME, theme="new",
 cap_ml="ഉദ്യം സ്വയം സാക്ഷ്യമാണ്, അതുകൊണ്ട് ശരിയായ വിവരം നൽകേണ്ടത് നിങ്ങൾ തന്നെ. ടേൺഓവർ 10 കോടി കടന്നാൽ മൈക്രോയിൽ നിന്ന് സ്മോളിലേക്ക്; വിവരം പുതുക്കണം. സ്മോളിനും 45 ദിവസ പേമെന്റ് സംരക്ഷണം ഉണ്ട്. നിങ്ങൾ ഉദ്യം അവസാനം എപ്പോൾ നോക്കി?",
 cap_en="A herbal soap maker with Rs 11 crore turnover wonders about writing 9 on Udyam to stay micro. Udyam is a self-declaration, so the correct details are your responsibility: past Rs 10 crore turnover you are small, and you update the record. Small units keep the 45-day payment protection too. When did you last check your Udyam?",
 cap_mg="Udyam swayam saakshyamaanu, athukondu shariyaaya vivaram nalkendathu ningal thanne. Turnover 10 crore kadannaal micro-yil ninnu small-ilekku; vivaram puthukkanam. Small-inum 45 divasa payment protection undu. Ningal Udyam avasaanam eppol nokki?")

duo("yd024", "manufacturer", "C", "kitchen", "ബിസിനസ് കമ്പനിയായി.\nഉദ്യം ഇപ്പോഴും\nഅമ്മയുടെ പേരിൽ", [
 ("A","wide","രാജേഷേ, എണ്ണ യൂണിറ്റ് ഇപ്പോ കമ്പനിയായി. അമ്മയുടെ പേരിലുള്ള ഉദ്യം സർട്ടിഫിക്കറ്റ് തന്നെ ബാങ്കിൽ കൊടുക്കാം, അല്ലേ?"),
 ("V","V","ബിന്ദൂ, ആ ഉദ്യം ആരുടെ PAN വെച്ചാ?"),
 ("A","A","അമ്മയുടെ. പത്ത് വർഷമായി അമ്മയുടെ പേരിലായിരുന്നു ബിസിനസ്."),
 ("V","wide","ഉദ്യം PAN വെച്ചാണ്. കമ്പനിക്ക് സ്വന്തം PAN ഉണ്ട്, അപ്പോ കമ്പനിയുടെ പേരിൽ ഉദ്യം വേണം."),
 ("A","A","അമ്മയുടെ സർട്ടിഫിക്കറ്റ് ഇനി ഓർമയ്ക്ക്."),
 ("V","wide","എണ്ണയുടെ കൂട്ട് പഴയതാകാം. രജിസ്ട്രേഷൻ പുതിയ ഉടമയുടേതാകണം.")],
 "കൂട്ട് പഴയത്,\nരജിസ്ട്രേഷൻ\nപുതിയ ഉടമയുടേത്", CTA_UDYAM, theme="crm",
 cap_ml="അമ്മയുടെ പേരിൽ വർഷങ്ങൾ നടത്തിയ ബിസിനസ് കമ്പനിയാക്കിയാൽ പഴയ ഉദ്യം മതിയോ? ഉദ്യം PAN വെച്ചാണ്; കമ്പനിക്ക് സ്വന്തം PAN, അതിനാൽ കമ്പനിയുടെ പേരിൽ ഉദ്യം വേണം. നിങ്ങളുടെ ബിസിനസ് ആരുടെ പേരിലാണ്?",
 cap_en="A family hair-oil business ran in the mother's name for ten years and is now a company, but the bank is still being shown the mother's Udyam. Udyam is tied to PAN, and the company has its own PAN, so the company needs Udyam in its own name. Whose name is your business in?",
 cap_mg="Ammayude peril varshangal nadathiya business company aakkiyaal pazhaya Udyam mathiyo? Udyam PAN vechaanu; company-kku swantham PAN, athinaal company-yude peril Udyam venam. Ningalude business aarude perilaanu?")

chat("yc003", "supplier_unpaid", "A", "50 ദിവസമായി\nക്ലയന്റ്: \"നാളെ\nവിളിക്കാം\"", ("ഷബ്ന", "ഷഹീൻ"), [
 (0,"ഷഹീനിക്കാ, ആ ക്ലയന്റ് 50 ദിവസമായി 'നാളെ വിളിക്കാം' എന്ന് മാത്രം പറയുന്നു. ടെസ്റ്റിംഗ് ബിൽ ഇപ്പോഴും ബാക്കി."),
 (1,"ഷബ്നാ, നിന്റെ സോഫ്റ്റ്‌വെയർ ടെസ്റ്റിംഗ് യൂണിറ്റിന് ഉദ്യം ഉണ്ടല്ലോ, മൈക്രോ സർവീസ്?"),
 (0,"ഉണ്ട്. പക്ഷേ വഴക്കിടാൻ പേടി, ക്ലയന്റ് പോകും."),
 (1,"വഴക്ക് വേണ്ട. 45 ദിവസം കഴിഞ്ഞാൽ നാല്പത്തിമൂന്ന് ബി എച്ച് പ്രകാരം, പണം തരും വരെ അവർക്ക് ടാക്സ് ഡിഡക്ഷൻ ഇല്ല. ഓർമിപ്പിക്കൂ."),
 (0,"അപ്പോ നാളെ വിളിക്കേണ്ടത് അവരുടെ ആവശ്യമാകും."),
 (1,"'നാളെ' അവർക്കും ചെലവാ.")],
 "\"നാളെ വിളിക്കാം\"\nഅവർക്കും ചെലവാണ്", CTA_MSME, theme="crm",
 cap_ml="ക്ലയന്റ് \"നാളെ വിളിക്കാം\" എന്ന് പറഞ്ഞ് 50 ദിവസം? ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് വൈകി പണം കൊടുത്താൽ 43B(h) പ്രകാരം പണം കൊടുക്കും വരെ ബയർക്ക് ആ ചെലവിന്റെ ഇൻകം ടാക്സ് ഡിഡക്ഷൻ ഇല്ല. വഴക്ക് വേണ്ട, മര്യാദയ്ക്ക് ഓർമിപ്പിച്ചാൽ മതി. നിങ്ങളുടെ ക്ലയന്റ് എത്ര ദിവസം എടുക്കുന്നു?",
 cap_en="A software testing micro unit's client has said 'I'll call tomorrow' for 50 days. No need to fight: under section 43B(h), a buyer who pays a micro or small supplier late loses the income-tax deduction for that expense until it pays. A polite reminder of that often helps. How many days does your client take?",
 cap_mg="Client 'naale vilikkaam' ennu paranju 50 divasam? Udyam ulla micro, small supplier-kku vaiki panam koduthaal 43B(h) prakaaram kodukkum vare buyer-kku aa chelavinte income tax deduction illa. Vazhakku venda, maryaadaykku ormippichaal mathi. Ningalude client ethra divasam edukkunnu?")
