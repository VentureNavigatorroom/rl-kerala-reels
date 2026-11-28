# Startup India / DPIIT batch 07 (28 Nov night). Max 6 lines, painful moment or myth first, payoff by line 4-5, short forwardable punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented). Facts only from topics.FACTS_SUI. No promises of approval or benefits. No prices.
# Only 5 this run: the sui fact list is small and the bank already holds ~57 scripts on it; these are the situations not yet used.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

# CRM #2 (runs it as a trust): assistive wheelchair attachment made by a charitable trust; a trust is not one of the four forms DPIIT recognises
duo("ud058", "grant_seeker", "A", "busstop", "\"ട്രസ്റ്റ് നല്ല\nകാര്യമല്ലേ? അപ്പോ\nDPIIT-ഉം തരുമല്ലോ\"", [
 ("A","wide","അഖിലേ, നിങ്ങളുടെ ട്രസ്റ്റ് ഉണ്ടാക്കിയ വീൽചെയർ അറ്റാച്ച്മെന്റ് സ്റ്റാൻഡിൽ എല്ലാരും നോക്കി നിന്നു. ഗ്രാന്റ് അപേക്ഷ അയച്ചോ?"),
 ("V","V","ജിബിനേ, ഫോമിൽ ആദ്യം DPIIT ചോദിക്കുന്നു. ട്രസ്റ്റിന്റെ പേരിൽ അപേക്ഷിക്കാൻ നോക്കിയിട്ട് വഴി കാണുന്നില്ല."),
 ("A","A","വഴി കാണാത്തതിന് കാരണമുണ്ട്. DPIIT നോക്കുന്നത് നാല് ഘടന മാത്രം."),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, സഹകരണ സംഘം. ട്രസ്റ്റ് ആ ലിസ്റ്റിൽ ഇല്ല. നല്ല ഉദ്ദേശ്യം മാത്രം പോരാ."),
 ("V","V","അപ്പോ ഇന്നൊവേഷൻ ഉണ്ട്, ഘടന ശരിയല്ല."),
 ("A","wide","നല്ല വണ്ടിക്കും ശരിയായ റൂട്ട് വേണം.")],
 "നല്ല വണ്ടിക്കും\nശരിയായ റൂട്ട് വേണം", CTA_DPIIT, theme="crm",
 cap_ml="വീൽചെയർ അറ്റാച്ച്മെന്റ് ഉണ്ടാക്കുന്ന ചാരിറ്റബിൾ ട്രസ്റ്റ് ഗ്രാന്റ് ഫോമിൽ DPIIT ചോദ്യത്തിൽ കുടുങ്ങി. DPIIT റെക്കഗ്നിഷൻ പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, സഹകരണ സംഘം എന്നിവയ്ക്കാണ്; ട്രസ്റ്റ് ആ ലിസ്റ്റിൽ ഇല്ല. നിങ്ങളുടെ സ്ഥാപനം ഏത് ഘടനയിലാ?",
 cap_en="A charitable trust that builds a wheelchair attachment got stuck at the DPIIT question on a grant form. DPIIT recognition is for a private limited company, LLP, registered partnership or cooperative society; a trust is not on that list. What structure is your organisation in?",
 cap_mg="Wheelchair attachment undaakkunna charitable trust grant form-il DPIIT chodyathil kudungi. DPIIT recognition Pvt Ltd, LLP, registered partnership, sahakarana sangham ennivaykkaanu; trust aa list-il illa. Ningalude sthaapanam ethu ghadanayilaa?")

# FAQ (myth: Startup India is only for Bengaluru app founders): honey traceability LLP in a hill hamlet; DPIIT checks structure, age, turnover, innovation, not the place
duo("ud059", "traditional_innovator", "B", "autostand", "\"അട്ടപ്പാടിയിൽ\nഇരുന്ന് സ്റ്റാർട്ടപ്പ്\nഇന്ത്യയോ?\"", [
 ("A","wide","സിബീ, നിന്റെ കാട്ടുതേൻ കുപ്പിയിൽ ഫോൺ കാണിച്ചാൽ ഏത് ഊരിലെ തേനാണെന്ന് കാണാമെന്ന്? അത് കൊള്ളാമല്ലോ."),
 ("V","V","ബിജോയ്ചേട്ടാ, LLP ഉണ്ട്. DPIIT-ന് അപേക്ഷിക്കാൻ ഇരുന്നപ്പോൾ എല്ലാരും പറയുന്നു, അത് ബെംഗളൂരുവിലെ ആപ്പുകാർക്കാ എന്ന്."),
 ("A","A","എന്നിട്ട് നീ അത് വിശ്വസിച്ചോ? DPIIT നോക്കുന്നത് നിന്റെ പിൻകോഡ് അല്ല."),
 ("A","wide","ശരിയായ ഘടന, 10 വർഷത്തിൽ താഴെ പ്രായം, ഒരു വർഷവും 200 കോടി കടക്കാത്ത ടേൺഓവർ, ഇന്നൊവേഷനോ വളരാവുന്ന മോഡലോ. ഇതാ ചെക്ക്."),
 ("V","V","അപ്പോ തേനീച്ചയ്ക്ക് പിൻകോഡ് പ്രശ്നമല്ല."),
 ("A","wide","തേൻ കാട്ടിലേതാ, പുതുമ നിന്റേതാ.")],
 "പിൻകോഡ് അല്ല,\nപുതുമയാണ് ചെക്ക്", CTA_DPIIT, names=("ബിജോയ്", "സിബി"), theme="faq",
 cap_ml="മലയോര ഊരുകളിലെ കാട്ടുതേൻ ഫോൺ കാണിച്ചാൽ ഉറവിടം അറിയുന്ന കുപ്പിയിൽ വിൽക്കുന്ന LLP. സ്റ്റാർട്ടപ്പ് ഇന്ത്യ നഗരത്തിലെ ആപ്പുകാർക്ക് മാത്രമാണെന്ന് കേട്ട് മടിച്ചു. DPIIT നോക്കുന്നത് ഘടന, പ്രായം, ടേൺഓവർ, ഇന്നൊവേഷൻ; സ്ഥലം ആ ലിസ്റ്റിൽ ഇല്ല. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ് ഏത് നാട്ടിലാ?",
 cap_en="An LLP sells wild honey from hill hamlets in bottles that show the source when you point a phone at them, but held back because 'Startup India is for city app founders'. DPIIT checks the structure, age under 10 years, turnover never above 200 crore, and innovation or a scalable model. The place is not on that list. Where is your startup based?",
 cap_mg="Malayora oorukalile kaattuthen phone kaanichaal uravidam ariyunna kuppiyil vilkkunna LLP. Startup India nagarathile app-kaarkku maathramaanennu kettu madichu. DPIIT nokkunnathu ghadana, praayam, turnover, innovation; sthalam aa list-il illa. Ningalude startup ethu naattilaa?")

# CRM #25 (student founder wants credibility): a hackathon prize is not DPIIT recognition; recognition is for an entity
duo("ud060", "student_founder", "C", "balcony", "ഹാക്കത്തോൺ സമ്മാനം.\nബയോയിൽ: \"സർക്കാർ\nഅംഗീകൃത സ്റ്റാർട്ടപ്പ്\"", [
 ("A","wide","ആദിത്യാ, പാടത്തെ വെള്ളം അളക്കുന്ന സെൻസറിന് സമ്മാനം കിട്ടിയത് സന്തോഷം. പക്ഷേ ബയോയിൽ 'സർക്കാർ അംഗീകൃത സ്റ്റാർട്ടപ്പ്' എന്തിനാ?"),
 ("V","V","ദീപ്തിച്ചേച്ചീ, മന്ത്രി തന്നെയല്ലേ സർട്ടിഫിക്കറ്റ് തന്നത്? അതിലും വലിയ അംഗീകാരം എന്താ?"),
 ("A","A","സമ്മാനം നിന്റെ പ്രോജക്റ്റിനാ. DPIIT റെക്കഗ്നിഷൻ ഒരു സ്ഥാപനത്തിനാ കിട്ടുന്നത്."),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, സഹകരണ സംഘം. ഇതിലൊന്ന് ആദ്യം, പിന്നെ അപേക്ഷ."),
 ("V","V","അപ്പോ ബയോ ഇന്ന് തിരുത്താം, കമ്പനി അടുത്ത പടി."),
 ("A","wide","സമ്മാനം ചുമരിൽ വെക്കാം, ബയോയിൽ സത്യം മാത്രം.")],
 "സമ്മാനം പ്രോജക്റ്റിന്,\nഅംഗീകാരം കമ്പനിക്ക്", CTA_DPIIT, names=("ദീപ്തി", "ആദിത്യൻ"), theme="crm",
 cap_ml="പാടത്തെ ജലനിരപ്പ് അളക്കുന്ന സെൻസറിന് ഹാക്കത്തോൺ സമ്മാനം കിട്ടിയ വിദ്യാർത്ഥി ബയോയിൽ 'സർക്കാർ അംഗീകൃത സ്റ്റാർട്ടപ്പ്' എന്ന് എഴുതി. സമ്മാനം പ്രോജക്റ്റിനാണ്; DPIIT റെക്കഗ്നിഷൻ പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് അല്ലെങ്കിൽ സഹകരണ സംഘത്തിനാണ്. നിങ്ങളുടെ പ്രോജക്റ്റിന് ഇപ്പോൾ കമ്പനി ഉണ്ടോ?",
 cap_en="A student won a hackathon prize for a paddy-field water sensor and wrote 'government-recognised startup' in his bio. A prize is for the project; DPIIT recognition is for an entity: a private limited company, LLP, registered partnership or cooperative society. Does your project have a company yet?",
 cap_mg="Paadathe jalanirappu alakkunna sensor-inu hackathon sammaanam kittiya vidyaarthi bio-il 'sarkkaar angeekritha startup' ennu ezhuthi. Sammaanam project-inaanu; DPIIT recognition Pvt Ltd, LLP, registered partnership allenkil sahakarana sanghathinaanu. Ningalude project-inu ippol company undo?")

# FAQ F15 variant (does recognition bring money?): founder waves the certificate at the bank counter expecting a loan
duo("ud061", "tech_founder", "B", "bank", "ബാങ്ക് കൗണ്ടറിൽ\nDPIIT സർട്ടിഫിക്കറ്റ്:\n\"ലോൺ ഇന്ന് തന്നെ?\"", [
 ("V","wide","ശ്വേതേ, ഇതാ DPIIT സർട്ടിഫിക്കറ്റ്. കപ്പത്തൊലിയിൽ നിന്നുള്ള പാക്കിംഗ് ബോക്സിന് ഇനി ലോൺ ഇന്ന് തന്നെ ശരിയാക്കാമല്ലോ?"),
 ("A","A","സനലേ, സർട്ടിഫിക്കറ്റ് നല്ലതാ. പക്ഷേ ഇത് ലോൺ അനുമതിയല്ല."),
 ("V","V","പിന്നെ ഇതുകൊണ്ട് എന്ത് കിട്ടും?"),
 ("A","wide","പേറ്റന്റ് ഫയലിംഗിൽ 80%, ട്രേഡ്മാർക്കിൽ 50% ഇളവ്, സ്വയം സാക്ഷ്യപ്പെടുത്തൽ, പല സ്കീമിനും ടെൻഡറിനും അപേക്ഷിക്കാനുള്ള യോഗ്യത."),
 ("A","A","ലോണിന് ബാങ്ക് സ്വന്തം പരിശോധന നടത്തും. സർട്ടിഫിക്കറ്റ് കൊണ്ട് മാത്രം അത് ഉറപ്പാകില്ല."),
 ("V","wide","അപ്പോ സർട്ടിഫിക്കറ്റിനൊപ്പം കണക്കും കൊണ്ടുവരാം.")],
 "സർട്ടിഫിക്കറ്റ് യോഗ്യത,\nലോൺ വേറെ കണക്ക്", CTA_BENEFITS, names=("ശ്വേത", "സനൽ"), theme="faq",
 cap_ml="കപ്പത്തൊലിയിൽ നിന്ന് പാക്കിംഗ് ബോക്സ് ഉണ്ടാക്കുന്ന സ്റ്റാർട്ടപ്പ് DPIIT സർട്ടിഫിക്കറ്റുമായി ബാങ്കിൽ ചെന്ന് അന്ന് തന്നെ ലോൺ പ്രതീക്ഷിച്ചു. റെക്കഗ്നിഷൻ തുറക്കുന്നത് പേറ്റന്റ്, ട്രേഡ്മാർക്ക് ഫയലിംഗ് ഇളവ്, സ്വയം സാക്ഷ്യപ്പെടുത്തൽ, സ്കീമുകൾക്കുള്ള യോഗ്യത എന്നിവയാണ്; ലോൺ ഉറപ്പല്ല. നിങ്ങൾ DPIIT കൊണ്ട് ആദ്യം എന്ത് ഉപയോഗിച്ചു?",
 cap_en="A startup making packing boxes from tapioca peel took its DPIIT certificate to the bank and expected a same-day loan. Recognition opens an 80% rebate on patent filing, 50% on trademark filing, self-certification and eligibility for schemes and tenders. It does not guarantee a loan. What did you use DPIIT for first?",
 cap_mg="Kappathholiyil ninnu packing box undaakkunna startup DPIIT certificate-umaayi bank-il chennu annu thanne loan pratheekshichu. Recognition thurakkunnathu patent, trademark filing ilavu, swayam saakshyappeduthal, scheme-ukalkkulla yogyatha ennivayaanu; loan urappalla. Ningal DPIIT kondu aadyam enthu upayogichu?")

# CRM #21 (traditional sector, new product): fish-scale collagen made from harbour waste by an LLP; DPIIT asks about innovation, not how old the sector is
duo("ud062", "traditional_innovator", "A", "teashop", "\"മീൻചെതുമ്പൽ\nവിറ്റ് സ്റ്റാർട്ടപ്പോ?\"\nചായക്കടയിൽ ചിരി", [
 ("A","wide","ആന്റണീ, ചാക്ക് നിറയെ മീൻചെതുമ്പൽ! ഇതും കൊണ്ടാണോ DPIIT-ന് അപേക്ഷിക്കാൻ പോകുന്നത്?"),
 ("V","V","ആൻസീ, ഹാർബറിൽ കളയുന്ന ചെതുമ്പലിൽ നിന്ന് കൊളാജൻ പൊടി. ഞങ്ങളുടെ LLP-യുടെ സ്വന്തം പ്രോസസ്."),
 ("A","A","മീൻ പണ്ടേ ഉള്ളതല്ലേ? അതിൽ എന്ത് പുതുമ?"),
 ("V","wide","DPIIT നോക്കുന്നത് മേഖല പഴയതാണോ എന്നല്ല. ഉൽപ്പന്നത്തിലോ സേവനത്തിലോ ഉള്ള ഇന്നൊവേഷനോ മെച്ചപ്പെടുത്തലോ ആണ്."),
 ("V","V","പിന്നെ LLP, 10 വർഷത്തിൽ താഴെ പ്രായം, ടേൺഓവർ പരിധി. അതും നോക്കി."),
 ("A","wide","അപ്പോ ചിരിച്ചത് ഞാൻ, മണം നിനക്ക്, പുതുമയും നിനക്ക്.")],
 "പഴയ മേഖല,\nപുതിയ ഉൽപ്പന്നം", CTA_DPIIT, names=("ആൻസി", "ആന്റണി"), theme="crm",
 cap_ml="ഹാർബറിൽ കളയുന്ന മീൻചെതുമ്പലിൽ നിന്ന് കൊളാജൻ പൊടി ഉണ്ടാക്കുന്ന LLP-യെ നോക്കി 'ഇതും സ്റ്റാർട്ടപ്പോ' എന്ന് ചിരിച്ചു. DPIIT നോക്കുന്നത് ഉൽപ്പന്നത്തിലോ സേവനത്തിലോ ഉള്ള ഇന്നൊവേഷനോ മെച്ചപ്പെടുത്തലോ ആണ്, മേഖലയുടെ പ്രായമല്ല; ഒപ്പം ഘടന, 10 വർഷ പ്രായം, ടേൺഓവർ പരിധി. നിങ്ങളുടെ മേഖലയിൽ ആരും കാണാത്ത പുതുമ എന്താ?",
 cap_en="People laughed at an LLP that turns fish scales thrown away at the harbour into collagen powder: 'is this a startup?'. DPIIT looks at innovation or improvement of a product or service, not at how old the sector is, along with the structure, age under 10 years and the turnover limit. What new thing are you doing in an old trade?",
 cap_mg="Harbour-il kalayunna meenchethumbalil ninnu collagen podi undaakkunna LLP-ye nokki 'ithum startup-o' ennu chirichu. DPIIT nokkunnathu ulpannathilo sevanathilo ulla innovation-o mechappeduthalo aanu, mekhalayude praayamalla; oppam ghadana, 10 varsha praayam, turnover paridhi. Ningalude mekhalayil aarum kaanaatha puthuma enthaa?")
