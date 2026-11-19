# Udyam / MSME batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_UD. Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

duo("yd008", "loan_seeker", "A", "rubber", "വികസിപ്പിക്കാൻ ലോൺ.\nബാങ്ക്: \"ഈട് എന്ത്?\"\nവീടിന്റെ ആധാരം മാത്രം", [
 ("A","wide","തോമസേ, റബ്ബർ മാറ്റ് യൂണിറ്റിന് പുതിയ മെഷീന് ലോൺ ചോദിച്ചു. ഈട് ചോദിച്ചപ്പോൾ വീടിന്റെ ആധാരം മാത്രമേയുള്ളൂ."),
 ("V","V","ജോയിച്ചാ, ഉദ്യം രജിസ്ട്രേഷൻ ഉണ്ടോ?"),
 ("A","A","ഇല്ല. അത് വലിയ കമ്പനികൾക്കല്ലേ?"),
 ("V","wide","ചെറിയ യൂണിറ്റുകൾക്കാ. മുൻഗണനാ വായ്പയ്ക്കും CGTMSE പോലെ ഈടില്ലാത്ത സ്കീമുകൾക്കും വഴി തുറക്കും. ലോൺ ഉറപ്പല്ല."),
 ("A","A","ആധാരം അലമാരയിൽ തന്നെ ഇരിക്കട്ടെ."),
 ("V","wide","മെഷീൻ വാങ്ങാൻ വീട് പണയം വെക്കും മുമ്പ് ഉദ്യം.")],
 "വീട് പണയം വെക്കും\nമുമ്പ് ഉദ്യം", CTA_UDYAM, theme="crm",
 cap_ml="ബിസിനസ് വികസിപ്പിക്കാൻ ലോൺ ചോദിച്ചപ്പോൾ ഈടായി വീട് മാത്രം? ഉദ്യം രജിസ്ട്രേഷൻ മുൻഗണനാ വായ്പയ്ക്കും CGTMSE പോലെയുള്ള ഈടില്ലാത്ത വായ്പാ സ്കീമുകൾക്കും വഴി തുറക്കും. ലോൺ ഉറപ്പല്ല. നിങ്ങളുടെ യൂണിറ്റിന് ഉദ്യം ഉണ്ടോ?",
 cap_en="A rubber mat unit asks for an expansion loan and the only collateral is the family home. Udyam registration opens priority sector lending and collateral-free loan schemes such as CGTMSE; it does not guarantee a loan. Does your unit have Udyam: yes or no?",
 cap_mg="Business vikasippikkaan loan chodichappol eedaayi veedu maathram? Udyam registration munganana vaaypaykkum CGTMSE poleyulla eedillaatha loan scheme-kalkkum vazhi thurakkum. Loan urappalla. Ningalude unit-inu Udyam undo?")

duo("yd009", "manufacturer", "B", "gulfroom", "നാട്ടിൽ ഫർണിച്ചർ\nയൂണിറ്റ്. \"ഉദ്യമിന്\nഏജന്റിനെ നോക്കണം\"", [
 ("A","wide","ഷംസൂ, അടുത്ത മാസം നാട്ടിൽ പോയി ഫർണിച്ചർ യൂണിറ്റ് തുടങ്ങും. ഉദ്യമിന് ഒരു ഏജന്റിനെ കണ്ടുവെച്ചു, ഫയൽ കെട്ടുകണക്കിന് വേണമെന്ന്."),
 ("V","V","നസീറിക്കാ, ഫയൽ കെട്ടോ? ഉദ്യം ഓൺലൈൻ അല്ലേ?"),
 ("A","A","ഓൺലൈനോ? അപ്പോ എന്തൊക്കെ വേണം?"),
 ("V","wide","ആധാർ വെച്ചാണ് രജിസ്ട്രേഷൻ. PAN, GST ഉണ്ടെങ്കിൽ അതും, പിന്നെ സ്വയം സാക്ഷ്യപ്പെടുത്തൽ. പുതുക്കലും ഇല്ല."),
 ("A","A","ഫർണിച്ചറിന് മരം വേണം, ഉദ്യമിന് കെട്ട് വേണ്ട."),
 ("V","wide","കെട്ട് ഫയലിനല്ല, കട്ടിലിനാ.")],
 "ആധാർ, PAN,\nസ്വയം സാക്ഷ്യം", CTA_UDYAM, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് മടങ്ങി യൂണിറ്റ് തുടങ്ങുന്നവർ ഉദ്യമിന് ഫയൽ കെട്ട് വേണം എന്ന് കരുതുന്നു. ഉദ്യം ഓൺലൈൻ, ആധാർ അടിസ്ഥാനം: PAN, GST ഉണ്ടെങ്കിൽ അതും, സ്വയം സാക്ഷ്യപ്പെടുത്തൽ. പുതുക്കൽ ഇല്ല, വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്താൽ മതി. നിങ്ങൾ നാട്ടിലേക്ക് മടങ്ങാൻ പ്ലാനുണ്ടോ?",
 cap_en="A Gulf returnee planning a furniture unit in Kerala thinks Udyam needs an agent and a stack of files. Udyam is online and Aadhaar-based: PAN, GSTIN if you have one, and a self-declaration. No renewal, just keep the details updated. Planning to move back and start: yes or no?",
 cap_mg="Gulf-il ninnu madangi unit thudangunnavar Udyam-inu file kettu venam ennu karuthunnu. Udyam online, Aadhaar adisthaanam: PAN, GST undenkil athum, swayam saakshyappeduthal. Puthukkal illa, vivarangal update cheythaal mathi. Ningal naattilekku madangaan plan undo?")

duo("yd010", "service_unit", "C", "weddinghall", "70 കല്യാണം വിളമ്പി.\nഇവന്റ് കമ്പനി:\n\"പേമെന്റ് പ്രോസസിംഗിലാ\"", [
 ("A","wide","ശരത്തേ, ഇവന്റ് കമ്പനിക്ക് വേണ്ടി 70 സദ്യ വിളമ്പിയിട്ട് 70 ദിവസമായി. ഇപ്പോഴും 'പ്രോസസിംഗ്'."),
 ("V","V","കാവ്യേ, നിന്റെ കാറ്ററിംഗിന് ഉദ്യം ഉണ്ടോ?"),
 ("A","A","ഉണ്ട്. സർവീസ് യൂണിറ്റ്, മൈക്രോ."),
 ("V","wide","എങ്കിൽ 45 ദിവസം കഴിഞ്ഞാൽ അവർ ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ തരണം. MSME സമാധാൻ പോർട്ടലിൽ പരാതി കൊടുക്കാം."),
 ("A","A","പ്രോസസിംഗിന് ഇനി പലിശയും പ്രോസസ് ചെയ്യട്ടെ."),
 ("V","wide","സദ്യ തണുത്തു, പലിശ ചൂടായി.")],
 "സദ്യ തണുത്തു,\nപലിശ ചൂടായി", CTA_MSME, theme="faq",
 cap_ml="ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സർവീസ് യൂണിറ്റിന് ബയർ 45 ദിവസത്തിനുള്ളിൽ പണം തരണം. വൈകിയാൽ ബാങ്ക് നിരക്കിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ, പരാതി MSME സമാധാൻ പോർട്ടലിൽ. നിങ്ങളുടെ ബയർ എത്ര ദിവസം എടുക്കുന്നു?",
 cap_en="A caterer served 70 wedding meals for an event company and 70 days later the payment is still 'processing'. Udyam-registered micro and small service units must be paid within 45 days at most; after that the buyer owes compound interest at three times the RBI bank rate, and you can complain on the MSME Samadhaan portal. How many days does your buyer take?",
 cap_mg="Udyam ulla micro, small service unit-inu buyer 45 divasathinullil panam tharanam. Vaikiyaal bank nirakkinte 3 iratti koottupalisha, paraathi MSME Samadhaan portal-il. Ningalude buyer ethra divasam edukkunnu?")

duo("yd011", "service_unit", "A", "hotellobby", "ഹോട്ടൽ ഉടമയുടെ CA:\n\"ഈ ബിൽ വൈകിയാൽ\nടാക്സ് കൂടും\"", [
 ("A","wide","ജെയ്സൺ, ലോൺഡ്രി സപ്ലയറുടെ ബിൽ അടുത്ത മാസം കൊടുക്കാം എന്ന് പറഞ്ഞപ്പോൾ CA വേണ്ട എന്ന് പറഞ്ഞു."),
 ("V","V","നീതൂ, എന്താ കാരണം?"),
 ("A","A","അവർ ഉദ്യം ഉള്ള മൈക്രോ യൂണിറ്റാണത്രേ."),
 ("V","wide","അതുതന്നെ. നാല്പത്തിമൂന്ന് ബി എച്ച് പ്രകാരം മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് വൈകി കൊടുത്താൽ, കൊടുക്കും വരെ ടാക്സ് ഡിഡക്ഷൻ ഇല്ല."),
 ("A","A","അപ്പോ വൈകിക്കുന്നത് നമുക്ക് തന്നെ നഷ്ടം."),
 ("V","wide","തുണി വൈകി വന്നാൽ പ്രശ്നം. പണം വൈകി പോയാലും പ്രശ്നം.")],
 "വൈകി കൊടുത്താൽ\nബയർക്കും നഷ്ടം", CTA_MSME, theme="new",
 cap_ml="മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് പണം വൈകിച്ചാൽ ബയർക്കും നഷ്ടം: 43B(h) പ്രകാരം കൊടുക്കും വരെ ആ ചെലവിന്റെ ഇൻകം ടാക്സ് ഡിഡക്ഷൻ കിട്ടില്ല. അതുകൊണ്ടാണ് വലിയ ബയർമാർ \"MSME ആണോ?\" എന്ന് ചോദിക്കുന്നത്. നിങ്ങൾ ബയറോ സപ്ലയറോ?",
 cap_en="A hotel owner wants to pay a laundry supplier next month, and her CA says no. Under section 43B(h), a buyer who pays a micro or small supplier late loses the income-tax deduction for that expense until payment. That is why big buyers ask if you are MSME-registered. Are you the buyer or the supplier?",
 cap_mg="Micro, small supplier-kku panam vaikichaal buyer-kkum nashtam: 43B(h) prakaaram kodukkum vare aa chelavinte income tax deduction kittilla. Athukondaanu valiya buyers 'MSME aano?' ennu chodikkunnathu. Ningal buyer-o supplier-o?")

duo("yd012", "manufacturer", "B", "farm", "മെഷീൻ 2 കോടി.\nടേൺഓവർ 12 കോടി.\n\"നമ്മൾ മൈക്രോ അല്ലേ?\"", [
 ("A","wide","ഗോപീ, നമ്മുടെ റൈസ് മില്ലിന്റെ മെഷീൻ 2 കോടിയേ ഉള്ളൂ. അപ്പോ നമ്മൾ മൈക്രോ തന്നെ, അല്ലേ?"),
 ("V","V","വാസുവേട്ടാ, ഈ വർഷം ടേൺഓവർ എത്രയായി?"),
 ("A","A","12 കോടി. നല്ല കൊല്ലമായിരുന്നു."),
 ("V","wide","മൈക്രോ ആകാൻ നിക്ഷേപം രണ്ടര കോടി വരെയും ടേൺഓവർ 10 കോടി വരെയും വേണം. രണ്ടും. ഒന്ന് കടന്നാൽ സ്മോൾ."),
 ("A","A","നെല്ല് കൂടി, വിഭാഗവും കൂടി."),
 ("V","wide","ഒരു ലിമിറ്റ് മാത്രം നോക്കിയാൽ കണക്ക് പതിര്.")],
 "രണ്ട് ലിമിറ്റും,\nഒന്ന് കടന്നാൽ സ്മോൾ", CTA_MSME, theme="faq",
 cap_ml="മെഷീൻ നിക്ഷേപം 2 കോടി, പക്ഷേ ടേൺഓവർ 12 കോടി: മൈക്രോ അല്ല, സ്മോൾ. മൈക്രോ ആകാൻ നിക്ഷേപം രണ്ടര കോടി വരെയും ടേൺഓവർ 10 കോടി വരെയും വേണം; ഏതെങ്കിലും ഒന്ന് കടന്നാൽ അടുത്ത വിഭാഗം. നിങ്ങളുടേത് ഏത്?",
 cap_en="A rice mill with Rs 2 crore of machinery but Rs 12 crore turnover is not micro: it is small. Since April 2025, micro means investment up to Rs 2.5 crore AND turnover up to Rs 10 crore; crossing either moves you up. Which is your unit: micro, small or medium?",
 cap_mg="Machine nikshepam 2 crore, pakshe turnover 12 crore: micro alla, small. Micro aakaan nikshepam randara crore vareyum turnover 10 crore vareyum venam; ethenkilum onnu kadannaal adutha vibhaagam. Ningaludethu eth?")

duo("yd013", "manufacturer", "C", "garage", "ഫാക്ടറി മാറി,\nGST എടുത്തു. ഉദ്യമിൽ\nഇപ്പോഴും പഴയ വിലാസം", [
 ("A","wide","ജിതിനേ, വെൽഡിംഗ് യൂണിറ്റ് പുതിയ ഷെഡിലേക്ക് മാറി, GST-യും എടുത്തു. ഉദ്യമിൽ ഇതൊക്കെ മാറ്റിയോ?"),
 ("V","V","ഐശ്വര്യേ, ഉദ്യം ഒരിക്കൽ എടുത്താൽ കഴിഞ്ഞില്ലേ? പുതുക്കൽ ഇല്ലല്ലോ."),
 ("A","A","പുതുക്കൽ ഇല്ല. പക്ഷേ അപ്ഡേറ്റ് ഉണ്ട്."),
 ("V","wide","ശരിയാ. വിലാസം, GST, ടേൺഓവർ മാറിയാൽ ഉദ്യമിലെ വിവരങ്ങളും അപ്ഡേറ്റ് ചെയ്യണം."),
 ("A","A","ടെൻഡറിൽ പഴയ വിലാസം കണ്ടാൽ ചോദ്യം വരും."),
 ("V","wide","ഷെഡ് മാറിയാൽ സർട്ടിഫിക്കറ്റും വണ്ടി കയറണം.")],
 "പുതുക്കൽ ഇല്ല,\nഅപ്ഡേറ്റ് ഉണ്ട്", CTA_UDYAM, theme="new",
 cap_ml="ഉദ്യമിന് പുതുക്കൽ ഇല്ല, പക്ഷേ വിലാസം, GST, ടേൺഓവർ പോലെ വിവരങ്ങൾ മാറിയാൽ അപ്ഡേറ്റ് ചെയ്യണം. നിങ്ങളുടെ ഉദ്യം സർട്ടിഫിക്കറ്റിലെ വിവരങ്ങൾ ഇപ്പോഴും ശരിയാണോ?",
 cap_en="A welding unit moved to a new shed and took GST registration, but its Udyam record still shows the old details. Udyam has no renewal, but you must keep the details updated when they change. Is your Udyam certificate still accurate: yes or no?",
 cap_mg="Udyam-inu puthukkal illa, pakshe vilaasam, GST, turnover pole vivarangal maariyaal update cheyyanam. Ningalude Udyam certificate-ile vivarangal ippozhum shariyaano?")

duo("yd014", "manufacturer", "A", "park", "\"ചെണ്ട ഉണ്ടാക്കുന്നത്\nകലയല്ലേ? അത്\nMSME ആകുമോ?\"", [
 ("A","wide","അനന്തൂ, അച്ഛന്റെ ചെണ്ട പണിശാലയ്ക്ക് സർക്കാർ ടെൻഡർ വന്നു. പക്ഷേ ഉദ്യം ചോദിക്കുന്നു."),
 ("V","V","ഗായത്രീ, ചെണ്ട ഉണ്ടാക്കുന്നത് കലയല്ലേ? അത് MSME-യിൽ വരുമോ?"),
 ("A","A","തോലും മരവും വാങ്ങി ഉണ്ടാക്കി വിൽക്കുന്നു. അത് മാനുഫാക്ചറിംഗ് തന്നെ."),
 ("V","wide","ശരിയാ. ചെറിയ നിർമാണ യൂണിറ്റിനും ഉദ്യം എടുക്കാം. സർക്കാർ ടെൻഡറുകളിൽ മുൻഗണനയ്ക്ക് അത് സഹായിക്കും."),
 ("A","A","താളം കലയാണ്, ബിസിനസും."),
 ("V","wide","ചെണ്ട കൊട്ടുന്നത് കോലുകൊണ്ട്, ടെൻഡർ കൊട്ടുന്നത് ഉദ്യം കൊണ്ട്.")],
 "താളം കലയാണ്,\nബിസിനസും", CTA_UDYAM, theme="new",
 cap_ml="ചെണ്ട, കഥകളി വേഷം, കൈത്തറി പോലെയുള്ള കലാ ഉൽപ്പന്നങ്ങൾ ഉണ്ടാക്കുന്നവരും ചെറിയ നിർമാണ യൂണിറ്റുകളാണ്. ഉദ്യം സർക്കാർ ടെൻഡറുകളിലെ മുൻഗണനയ്ക്ക് സഹായിക്കും; ടെൻഡർ ഉറപ്പല്ല. നിങ്ങളുടെ കുടുംബത്തിൽ ഇങ്ങനെ ഒരു പണിശാല ഉണ്ടോ?",
 cap_en="A family chenda workshop gets a government tender that asks for Udyam, and the daughter wonders whether a traditional craft counts as MSME. Making and selling instruments is manufacturing, and Udyam helps with preferences in government tenders (no guarantee). Does your family run a craft workshop: yes or no?",
 cap_mg="Chenda, Kathakali vesham, kaithari poleyulla kala ulpannangal undaakkunnavarum cheriya nirmaana unit-ukal aanu. Udyam sarkkaar tender-ukalile munganaykku sahaayikkum; tender urappalla. Ningalude kudumbathil ingane oru panishaala undo?")

duo("yd015", "manufacturer", "B", "photocopy", "സ്കൂൾ നോട്ട്ബുക്ക്\nടെൻഡർ. ഫോമിലെ ആദ്യ\nകോളം: ഉദ്യം നമ്പർ", [
 ("A","wide","ഉണ്ണീ, നമ്മുടെ പ്രസ്സിന് പഞ്ചായത്തിലെ സ്കൂൾ നോട്ട്ബുക്ക് ടെൻഡർ എടുക്കാൻ പറ്റുമോ എന്ന് നോക്കുവാ."),
 ("V","V","അശ്വതീ, 15 വർഷത്തെ പ്രസ്സല്ലേ, എന്താ പ്രശ്നം?"),
 ("A","A","ഫോമിൽ ആദ്യം ചോദിക്കുന്നത് ഉദ്യം നമ്പർ. നമ്മുടെ കയ്യിൽ ഇല്ല."),
 ("V","wide","ഓൺലൈനിൽ ആധാർ വെച്ച് എടുക്കാം. സർക്കാർ ടെൻഡറുകളിൽ MSME-കൾക്ക് മുൻഗണനകളുണ്ട്. ആദ്യം നമ്പർ, പിന്നെ ടെൻഡർ."),
 ("A","A","അച്ചടിക്കുന്നവർക്ക് സ്വന്തം നമ്പർ ഇല്ല."),
 ("V","wide","പേജ് നമ്പർ ഇട്ടു മടുത്തു, ഉദ്യം നമ്പർ മറന്നു.")],
 "ടെൻഡറിന് മുമ്പ്\nഉദ്യം നമ്പർ", CTA_UDYAM, theme="crm",
 cap_ml="15 വർഷത്തെ പ്രിന്റിംഗ് പ്രസ് സർക്കാർ ടെൻഡറിന് ഒരുങ്ങുമ്പോൾ ഫോമിലെ ആദ്യ ചോദ്യം ഉദ്യം നമ്പർ. ഉദ്യം ഓൺലൈനിൽ ആധാർ വെച്ച് എടുക്കാം; സർക്കാർ ടെൻഡറുകളിൽ MSME-കൾക്ക് മുൻഗണനകളുണ്ട്. നിങ്ങൾ ടെൻഡറിന് അപേക്ഷിച്ചിട്ടുണ്ടോ?",
 cap_en="A 15-year-old printing press wants to bid for a school notebook tender, and the first field on the form asks for an Udyam number. Udyam is online and Aadhaar-based, and it helps with preferences in government tenders. Have you ever bid for a tender: yes or no?",
 cap_mg="15 varshathe printing press sarkkaar tender-inu orungumpol form-ile aadya chodyam Udyam number. Udyam online-il Aadhaar vechu edukkaam; sarkkaar tender-ukalil MSME-kalkku munganakalundu. Ningal tender-inu apekshichittundo?")

chat("yc002", "service_unit", "C", "\"GST ഇല്ല. അപ്പോ\nഉദ്യം കിട്ടില്ലല്ലോ\"", ("സുമയ്യ", "ജാഫർ"), [
 (1,"സുമയ്യാ, എന്റെ AC റിപ്പയർ സർവീസിന് GST ഇല്ല. അപ്പോ ഉദ്യം എടുക്കാൻ പറ്റില്ലല്ലോ?"),
 (0,"ജാഫറിക്കാ, ആര് പറഞ്ഞു? ഉദ്യമിന് ആധാറും PAN-ഉം മതി."),
 (1,"GST നമ്പർ ചോദിക്കില്ലേ?"),
 (0,"GST ഉള്ള ബിസിനസ് ആണെങ്കിൽ അതും കൊടുക്കണം. ഇല്ലെങ്കിൽ ആധാർ, PAN, സ്വയം സാക്ഷ്യം."),
 (1,"അപ്പോ ഇന്ന് തന്നെ."),
 (0,"AC തണുപ്പിക്കും, ഉദ്യം ബിസിനസിനെ.")],
 "GST ഇല്ലെങ്കിലും\nഉദ്യം എടുക്കാം", CTA_UDYAM, theme="faq",
 cap_ml="GST ഇല്ലാത്ത ചെറിയ സർവീസ് ബിസിനസിനും ഉദ്യം എടുക്കാം: ആധാർ, PAN, സ്വയം സാക്ഷ്യപ്പെടുത്തൽ. GST ഉള്ള ബിസിനസ് ആണെങ്കിൽ GSTIN-ഉം കൊടുക്കണം. നിങ്ങളുടെ ബിസിനസിന് GST ഉണ്ടോ?",
 cap_en="No GST registration, so no Udyam? Not true. Udyam needs Aadhaar, PAN and a self-declaration; you add your GSTIN only if the business has one. Does your business have GST: yes or no?",
 cap_mg="GST illaatha cheriya service business-inum Udyam edukkaam: Aadhaar, PAN, swayam saakshyappeduthal. GST ulla business aanenkil GSTIN-um kodukkanam. Ningalude business-inu GST undo?")

lst("yl002", "supplier_unpaid", "A", "ബയർ പണം\nതരുന്നില്ല: ആദ്യം\nനോക്കേണ്ട 3 കാര്യം", [
 ("നിങ്ങളുടെ വിഭാഗം", "ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റാണോ? കച്ചവടക്കാർക്ക് ഈ സംരക്ഷണം ഇല്ല."),
 ("ദിവസം എണ്ണുക", "എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം. ഉണ്ടെങ്കിലും പരമാവധി 45."),
 ("പരാതി", "MSME സമാധാൻ പോർട്ടലിലോ ഫെസിലിറ്റേഷൻ കൗൺസിലിലോ.")],
 "നിങ്ങളുടെ ബിൽ\nഎത്ര ദിവസം പഴയത്?", CTA_MSME, theme="faq",
 cap_ml="ബയർ പണം തരുന്നില്ലെങ്കിൽ 3 കാര്യം: നിങ്ങൾ ഉദ്യം ഉള്ള മൈക്രോ/സ്മോൾ നിർമാണ, സർവീസ് യൂണിറ്റാണോ, എത്ര ദിവസമായി (15, പരമാവധി 45), പരാതി MSME സമാധാൻ പോർട്ടലിൽ. നിങ്ങളുടെ ഏറ്റവും പഴയ ബിൽ എത്ര ദിവസം?",
 cap_en="Buyer not paying? Check three things: are you an Udyam-registered micro or small manufacturing or service unit (traders don't get this protection), how many days have passed (15 without an agreement, 45 at most with one), and where to complain (MSME Samadhaan or the facilitation council). How old is your oldest unpaid bill?",
 cap_mg="Buyer panam tharunnillenkil 3 kaaryam: ningal Udyam ulla micro/small nirmaana, service unit aano, ethra divasamaayi (15, paramaavadhi 45), paraathi MSME Samadhaan portal-il. Ningalude ettavum pazhaya bill ethra divasam?")
