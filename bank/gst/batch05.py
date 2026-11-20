# GST batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd026", "trader", "A", "busstop", "രണ്ട് കട.\nരണ്ടും 40 ലക്ഷത്തിന് താഴെ.\nGST വേണ്ടേ?", [
 ("A","wide","അഖിലേ, ഹാർഡ്‌വെയർ കടയ്ക്ക് 25 ലക്ഷം, പെയിന്റ് കടയ്ക്ക് 22 ലക്ഷം. രണ്ടും ലിമിറ്റിന് താഴെ, അല്ലേ?"),
 ("V","V","ജിബിനേ, രണ്ട് കടയും നിന്റെ പേരിൽ, ഒരേ PAN-ൽ അല്ലേ?"),
 ("A","A","അതെ. ബോർഡ് രണ്ട്, ഉടമ ഒന്ന്."),
 ("V","wide","എങ്കിൽ GST നോക്കുന്നത് ആകെ ടേൺഓവർ. 25-ഉം 22-ഉം ചേർന്നാൽ 47 ലക്ഷം. സാധനങ്ങൾക്ക് ലിമിറ്റ് 40 ലക്ഷം."),
 ("A","A","അപ്പോ രജിസ്ട്രേഷൻ ഇന്നു തന്നെ."),
 ("V","V","ബോർഡ് രണ്ടായാലും കണക്ക് ഒന്നാ.")],
 "ബോർഡ് രണ്ട്,\nകണക്ക് ഒന്ന്", CTA_LIMIT, theme="crm",
 cap_ml="ഒരാൾക്ക് രണ്ട് കട, ഓരോന്നും 40 ലക്ഷത്തിന് താഴെ. പക്ഷേ ഒരേ PAN ആണെങ്കിൽ GST ലിമിറ്റ് നോക്കുന്നത് ആകെ ടേൺഓവർ ആണ്: സാധനങ്ങൾക്ക് കേരളത്തിൽ 40 ലക്ഷം. നിങ്ങൾക്ക് എത്ര കട ഉണ്ട്?",
 cap_en="One owner, two shops, each below 40 lakh a year. But if both run under the same PAN, the GST limit looks at the aggregate turnover, and for goods in Kerala that limit is 40 lakh. How many shops do you run?",
 cap_mg="Oraalkku randu kada, oronnum 40 lakhinu thaazhe. Pakshe ore PAN aanenkil GST limit nokkunnathu aake turnover aanu: saadhanangalkku Kerala-il 40 lakh. Ningalkku ethra kada undu?")

duo("gd027", "online_seller", "B", "handloom", "\"മാർക്കറ്റ്പ്ലേസിൽ\nവിൽക്കാൻ GST\nഇല്ലാതെ പറ്റില്ലേ?\"", [
 ("V","wide","ലീലേ, ഈ വാഴനാര് ബാഗുകൾ ഓൺലൈനിൽ ഇടാത്തത് എന്താ? ഇത്ര നല്ല പണി."),
 ("A","A","കുമാറേ, ഓൺലൈനിൽ വിൽക്കുന്ന എല്ലാവർക്കും GST നിർബന്ധം എന്ന് കേട്ടു. എന്റെ കച്ചവടം അത്രയൊന്നുമില്ല."),
 ("V","V","എല്ലാവർക്കുമല്ല. ലിമിറ്റിന് താഴെ, കേരളത്തിനകത്ത് മാത്രം വിൽക്കുമ്പോൾ, മാർക്കറ്റ്പ്ലേസ് അനുവദിച്ചാൽ PAN വെച്ചുള്ള എൻറോൾമെന്റ് മതി."),
 ("A","A","അപ്പോ മറ്റൊരു സംസ്ഥാനത്ത് നിന്ന് ഓർഡർ വന്നാലോ?"),
 ("V","wide","അന്ന് ആദ്യ വിൽപ്പന മുതൽ GST വേണം. ജില്ല കടക്കാം, സംസ്ഥാനം കടക്കാൻ GST.")],
 "ജില്ല കടക്കാം,\nസംസ്ഥാനം കടക്കാൻ GST", CTA_GST, theme="faq",
 cap_ml="ഓൺലൈനിൽ വിൽക്കുന്ന എല്ലാവർക്കും GST നിർബന്ധമല്ല. ലിമിറ്റിന് താഴെ, കേരളത്തിനകത്ത് മാത്രം വിൽക്കുന്നവർക്ക് മാർക്കറ്റ്പ്ലേസ് അനുവദിച്ചാൽ PAN വെച്ചുള്ള എൻറോൾമെന്റ് മതി. മറ്റൊരു സംസ്ഥാനത്തേക്ക് ആദ്യ ഓർഡർ പോകുമ്പോൾ GST വേണം. നിങ്ങൾ ഓൺലൈനിൽ വിൽക്കുന്നുണ്ടോ?",
 cap_en="A banana-fibre bag maker never listed online because she heard every online seller needs GST. Not quite: below the limit and selling only within Kerala, a PAN-based enrolment can be enough if the marketplace supports it. The first order to another state needs GST from that sale. Do you sell online: yes or no?",
 cap_mg="Online-il vilkkunna ellaavarkkum GST nirbandhamalla. Limit-inu thaazhe, Kerala-kkakathu maathram vilkkunnavarkku marketplace anuvadichaal PAN vechulla enrolment mathi. Vere state-ilekku aadya order pokumpol GST venam. Ningal online-il vilkkunnundo?")

duo("gd028", "new_company", "C", "beach", "ഹോട്ടൽ ഓർഡർ\nഅടുത്ത ആഴ്ച.\nGST: 3 ദിവസം പോരേ?", [
 ("A","wide","നിഖിലേ, ചക്ക ഐസ്ക്രീമിന് റിസോർട്ടുകളുടെ ഓർഡർ കിട്ടി. GST ഇന്ന് അപേക്ഷിച്ചാൽ മൂന്ന് ദിവസത്തിൽ കിട്ടുമല്ലോ."),
 ("V","V","ദിവ്യേ, മൂന്ന് ദിവസം റിസ്ക് കുറഞ്ഞ അപേക്ഷയ്ക്ക് മാത്രമാ. എല്ലാ അപേക്ഷയും അങ്ങനെയല്ല."),
 ("A","A","അല്ലെങ്കിൽ എത്ര എടുക്കും?"),
 ("V","wide","സാധാരണ ഏഴ് പ്രവൃത്തി ദിവസം. നേരിട്ടുള്ള പരിശോധന വേണ്ടി വന്നാൽ 30 ദിവസം വരെ."),
 ("A","A","ഓർഡർ അടുത്ത ആഴ്ച, അപ്രൂവൽ അടുത്ത മാസം!"),
 ("V","wide","ഓർഡർ വന്നിട്ട് അപേക്ഷിച്ചാൽ, അപ്രൂവൽ വരുമ്പോൾ ഓർഡർ പോയിരിക്കും.")],
 "ഓർഡറിന് മുമ്പേ\nഅപേക്ഷ", CTA_GST, theme="new",
 cap_ml="പുതിയ ഐസ്ക്രീം കമ്പനിക്ക് അടുത്ത ആഴ്ച ഓർഡർ, GST മൂന്ന് ദിവസത്തിൽ കിട്ടുമെന്ന് കരുതി. റിസ്ക് കുറഞ്ഞ അപേക്ഷയ്ക്ക് മാത്രമാണ് 3 പ്രവൃത്തി ദിവസം; അല്ലെങ്കിൽ 7 ദിവസം, പരിശോധന വന്നാൽ 30 ദിവസം വരെ. നിങ്ങൾ GST-ക്ക് എത്ര ദിവസം കാത്തു?",
 cap_en="A new jackfruit ice cream company counted on GST in 3 days for next week's resort order. Only low-risk applications are auto-approved within 3 working days; others take 7 working days, or up to 30 if physical verification is needed. How long did your GST take?",
 cap_mg="Puthiya ice cream company-kku adutha aazhcha order, GST moonnu divasathil kittumennu karuthi. Risk kuranja apekshaykku maathramaanu 3 working days; allenkil 7 divasam, verification vannaal 30 divasam vare. Ningal GST-kku ethra divasam kaathu?")

duo("gd029", "nri_business", "A", "gulfroom", "മസ്കറ്റിൽ ഇരുന്ന്\nനാട്ടിലെ ഇവന്റ് ബിസിനസ്.\n45 ലക്ഷം, GST ഇല്ല", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ കല്യാണ ഡെക്കറേഷൻ ബിസിനസ് അനിയനാ നോക്കുന്നത്. ഈ വർഷം 45 ലക്ഷത്തിന്റെ പണി."),
 ("V","V","നസീറേ, അത് സർവീസ് അല്ലേ? സർവീസിന് കേരളത്തിൽ ലിമിറ്റ് 20 ലക്ഷമാ. GST എടുത്തോ?"),
 ("A","A","ഇല്ല. എടുത്താൽ എല്ലാ മാസവും വലിയ കണക്കുകൾ. ഇവിടെ ഇരുന്ന് എനിക്ക് പറ്റില്ല."),
 ("V","wide","ചെറിയവർക്ക് ലളിതമായ വഴിയുണ്ട്: കോമ്പോസിഷൻ സ്കീം. സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ ഉള്ളവർക്ക്."),
 ("A","A","അപ്പോ ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ കോമ്പോസിഷൻ."),
 ("V","wide","ദൂരം ഒഴികഴിവല്ല. ലിമിറ്റ് കടന്നാൽ കടന്നതാ.")],
 "ദൂരം\nഒഴികഴിവല്ല", CTA_LIMIT, theme="crm",
 cap_ml="മസ്കറ്റിലുള്ള ഉടമയുടെ നാട്ടിലെ ഡെക്കറേഷൻ ബിസിനസ് സർവീസ് ലിമിറ്റ് ആയ 20 ലക്ഷം കടന്നു, GST ഇല്ല. കണക്ക് പേടിയാണെങ്കിൽ കോമ്പോസിഷൻ സ്കീം ഉണ്ട്: സർവീസിന് 50 ലക്ഷം വരെ, സാധനങ്ങൾക്ക് 1.5 കോടി വരെ. നിങ്ങളുടെ ബിസിനസ് സർവീസോ സാധനമോ?",
 cap_en="A Gulf-based owner's wedding decoration business in Kerala crossed the 20 lakh services limit with no GST. Scared of the paperwork? The composition scheme covers turnover up to 50 lakh for services and 1.5 crore for goods. Is your business services or goods?",
 cap_mg="Muscat-il ulla udamayude naattile decoration business service limit aaya 20 lakh kadannu, GST illa. Kanakku pediyaanenkil composition scheme undu: service-nu 50 lakh vare, saadhanangalkku 1.5 kodi vare. Ningalude business service-o saadhanamo?")

duo("gd030", "new_company", "B", "rooftop", "ആദ്യ വിൽപ്പന\nപോലും ആയില്ല.\n\"പിന്നെന്ത് റിട്ടേൺ?\"", [
 ("V","wide","ആര്യേ, നമ്മുടെ ഇലക്ട്രിക് വള്ളം മോട്ടോറിന്റെ പ്രോട്ടോടൈപ്പ് റെഡി. GST എടുത്തത് പാർട്സ് വാങ്ങാനാ."),
 ("A","A","ശ്യാമേ, വിൽപ്പന തുടങ്ങിയിട്ട് മതി റിട്ടേൺ എന്നല്ലേ? ഇതുവരെ ഒന്നും വിറ്റില്ലല്ലോ."),
 ("V","V","രജിസ്റ്റർ ചെയ്ത മാസം മുതൽ റിട്ടേൺ വേണം. വിൽപ്പന ഇല്ലാത്ത മാസം നിൽ റിട്ടേൺ."),
 ("A","A","നാല് മാസമായി ഒന്നും ഫയൽ ചെയ്തില്ല..."),
 ("V","wide","നിൽ GSTR-3B വൈകിയാൽ ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ. ഇന്ന് തന്നെ ഫയൽ ചെയ്യാം."),
 ("A","wide","മോട്ടോർ ഓഫ് ആണെങ്കിലും ഫയലിംഗ് ഓൺ.")],
 "മോട്ടോർ ഓഫ്,\nഫയലിംഗ് ഓൺ", CTA_PENALTY, theme="faq",
 cap_ml="ഇലക്ട്രിക് വള്ളം മോട്ടോർ സ്റ്റാർട്ടപ്പ് പാർട്സ് വാങ്ങാൻ GST എടുത്തു, പക്ഷേ ആദ്യ വിൽപ്പന ആകും വരെ റിട്ടേൺ വേണ്ടെന്ന് കരുതി. വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ വേണം; വൈകിയാൽ ദിവസം 20 രൂപ, ഒന്നിന് 500 വരെ. നിങ്ങളുടെ ആദ്യ വിൽപ്പന കഴിഞ്ഞോ?",
 cap_en="An electric boat-motor startup took GST to buy parts and thought returns could wait until the first sale. A nil return is due even in months with no sales, and a late nil GSTR-3B costs 20 rupees a day, up to 500 per return. Have you made your first sale yet?",
 cap_mg="Electric vallam motor startup parts vaangaan GST eduthu, pakshe aadya vilppana aakum vare return venda ennu karuthi. Vilppana illaatha maasavum nil return venam; vaikiyaal divasam 20 roopa, onninu 500 vare. Ningalude aadya vilppana kazhinjo?")

duo("gd031", "trader", "C", "courier", "\"വാട്സാപ്പ് ഓർഡർ\nകൊറിയറിൽ ആണേ,\nGST എന്തിന്?\"", [
 ("V","wide","ജയേ, ഈ ലോഹക്കണ്ണാടി പാഴ്സൽ മുംബൈയിലേക്കാണോ? ഈ മാസം അഞ്ചാമത്തേതാ."),
 ("A","A","അരവിന്ദേ, ഇത് വാട്സാപ്പ് ഓർഡറാ, മാർക്കറ്റ്പ്ലേസ് അല്ല. അതുകൊണ്ട് GST വേണ്ടല്ലോ."),
 ("V","V","ഓർഡർ എങ്ങനെ വന്നു എന്നല്ല, സാധനം എങ്ങോട്ട് പോകുന്നു എന്നാ നിയമം നോക്കുന്നത്."),
 ("A","A","അതായത്?"),
 ("V","wide","മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിൽക്കാൻ ടേൺഓവർ നോക്കാതെ ആദ്യ വിൽപ്പന മുതൽ GST നിർബന്ധം."),
 ("A","wide","കണ്ണാടി മുഖം കാണിക്കും. ബില്ല് GSTIN കാണിക്കണം.")],
 "മുഖം കണ്ണാടിയിൽ,\nGSTIN ബില്ലിൽ", CTA_GST, theme="crm",
 cap_ml="ലോഹക്കണ്ണാടി ഉണ്ടാക്കുന്നയാൾ വാട്സാപ്പ് ഓർഡറുകൾ മറ്റ് സംസ്ഥാനങ്ങളിലേക്ക് കൊറിയർ ചെയ്യുന്നു, മാർക്കറ്റ്പ്ലേസ് അല്ലാത്തതുകൊണ്ട് GST വേണ്ടെന്ന് കരുതി. മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിറ്റാൽ ടേൺഓവർ എത്രയായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം. നിങ്ങളുടെ ഓർഡറുകൾ വാട്സാപ്പിലാണോ?",
 cap_en="A metal-mirror maker couriers WhatsApp orders to other states and thought GST was only for marketplace sellers. Selling goods to another state needs GST from the first sale, whatever the turnover and however the order came in. Do your orders come on WhatsApp: yes or no?",
 cap_mg="Lohakkannaadi undaakkunnayaal WhatsApp orders vere state-ilekku courier cheyyunnu, marketplace allaathathukondu GST venda ennu karuthi. Vere state-ilekku saadhanam vittaal turnover ethrayaayaalum aadya vilppana muthal GST venam. Ningalude orders WhatsApp-il aano?")

duo("gd032", "service_pro", "A", "munnar", "ലിമിറ്റിന് താഴെ,\nസ്വമേധയാ GST.\nറിട്ടേൺ വേണോ?", [
 ("A","wide","ബേസിലേ, ഹൗസ്ബോട്ട് മരപ്പണിക്ക് റിസോർട്ട് ക്ലയന്റിന് വേണ്ടി സ്വമേധയാ GST എടുത്തതല്ലേ. റിട്ടേൺ കൃത്യമാണോ?"),
 ("V","V","സെലിനേ, എന്റെ വരുമാനം 20 ലക്ഷത്തിനും താഴെയാ. അപ്പോ റിട്ടേൺ ഒന്നും വേണ്ടല്ലോ."),
 ("A","A","രജിസ്റ്റർ ചെയ്യണോ എന്ന് തീരുമാനിക്കാനാ ലിമിറ്റ്. രജിസ്റ്റർ ചെയ്താൽ റിട്ടേൺ വേണം, പണിയില്ലാത്ത മാസവും."),
 ("V","wide","മഴക്കാലത്ത് മൂന്ന് മാസം ഒരു പണിയും ഇല്ലായിരുന്നു..."),
 ("A","wide","എങ്കിൽ ആ മാസങ്ങൾക്കും നിൽ റിട്ടേൺ. ഇഷ്ടത്തിന് കയറാം, പക്ഷേ ഉള്ളിടത്തോളം ഫയൽ ചെയ്യണം.")],
 "ഇഷ്ടത്തിന് കയറാം,\nഉള്ളിടത്തോളം ഫയൽ", CTA_PENALTY, theme="faq",
 cap_ml="ഹൗസ്ബോട്ട് മരപ്പണിക്കാരൻ റിസോർട്ട് ക്ലയന്റിന് വേണ്ടി ലിമിറ്റിന് താഴെ സ്വമേധയാ GST എടുത്തു, റിട്ടേൺ വേണ്ടെന്ന് കരുതി. രജിസ്റ്റർ ചെയ്തിരിക്കുന്നിടത്തോളം റിട്ടേൺ വേണം, പണിയില്ലാത്ത മാസം നിൽ റിട്ടേൺ. നിങ്ങൾ സ്വമേധയാ GST എടുത്തതാണോ?",
 cap_en="A houseboat woodworker took GST voluntarily for a resort client, below the 20 lakh limit, and assumed no returns were due. The limit decides whether you must register; once registered, returns are due every month, nil returns included. Did you register voluntarily: yes or no?",
 cap_mg="Houseboat marappanikkaaran resort client-inu vendi limit-inu thaazhe swamedhaya GST eduthu, return venda ennu karuthi. Register cheythirikkunnidatholam return venam, paniyillaatha maasam nil return. Ningal swamedhaya GST eduthathaano?")

duo("gd033", "nri_business", "B", "gulf", "ദുബായിൽ നിന്ന്\nഇൻസ്റ്റഗ്രാം ഹൽവ ഷോപ്പ്.\nആദ്യം GST വേണോ?", [
 ("V","wide","ഷിജൂ, ഉമ്മ ഉണ്ടാക്കുന്ന ഹൽവ ഗിഫ്റ്റ് ബോക്സ് ഇൻസ്റ്റഗ്രാമിൽ ഇടാൻ പോകുന്നു. ഡെലിവറി നാട്ടിൽ മാത്രം. ആദ്യം GST എടുക്കണോ?"),
 ("A","A","ഫൈസലേ, ആരുടെ വീട്ടിലേക്കാ ബോക്സ് പോകുന്നത്? കേരളത്തിൽ മാത്രമാണോ?"),
 ("V","V","അതെ. ഇവിടത്തെ പ്രവാസികൾ നാട്ടിലെ വീട്ടിലേക്ക് ഓർഡർ ചെയ്യും. ഒരു വർഷം 10 ലക്ഷം കടക്കില്ല."),
 ("A","wide","കേരളത്തിനകത്ത് മാത്രം, നേരിട്ട് വിറ്റ്, 40 ലക്ഷത്തിന് താഴെയാണെങ്കിൽ GST നിർബന്ധമില്ല."),
 ("V","V","ചെന്നൈയിലെ അമ്മായി ഓർഡർ ചെയ്താലോ?"),
 ("A","wide","അന്ന് മുതൽ GST. ഹൽവ അതിർത്തി കടന്നാൽ, GST കൂടെ വരും.")],
 "ഹൽവ അതിർത്തി കടന്നാൽ,\nGST കൂടെ വരും", CTA_GST, theme="faq",
 cap_ml="ദുബായിൽ നിന്ന് ഇൻസ്റ്റഗ്രാം വഴി നാട്ടിലെ വീടുകളിലേക്ക് ഹൽവ. കേരളത്തിനകത്ത് മാത്രം നേരിട്ട് വിൽക്കുന്നു, 40 ലക്ഷത്തിന് താഴെ: GST നിർബന്ധമില്ല. ഒരു ബോക്സ് മറ്റൊരു സംസ്ഥാനത്തേക്ക് പോയാൽ ആദ്യ വിൽപ്പന മുതൽ GST. നിങ്ങളുടെ ഡെലിവറി എവിടെയൊക്കെ?",
 cap_en="A Dubai Malayali plans an Instagram halwa gift-box page delivering only to homes in Kerala. Selling directly within Kerala and below 40 lakh a year, GST is not compulsory; the first box to another state needs GST from that sale. Where do your deliveries go?",
 cap_mg="Dubai-il ninnu Instagram vazhi naattile veedukalilekku halwa. Kerala-kkakathu maathram nerittu vilkkunnu, 40 lakhinu thaazhe: GST nirbandhamilla. Oru box vere state-ilekku poyaal aadya vilppana muthal GST. Ningalude delivery evideyokke?")

duo("gd034", "trader", "C", "park", "\"GST വാങ്ങിയില്ല,\nപിന്നെ ഞാൻ\nഎന്തിന് അടയ്ക്കണം?\"", [
 ("A","wide","അനന്തൂ, ഉത്സവക്കുട കച്ചവടം ഇക്കൊല്ലം 52 ലക്ഷം കടന്നെന്ന് കേട്ടു. GST ഉണ്ടല്ലോ, അല്ലേ?"),
 ("V","V","ഗായത്രീ, ഇല്ല. പക്ഷേ ആരുടെ കയ്യിൽ നിന്നും GST വാങ്ങിയിട്ടില്ല. അപ്പോ അടയ്ക്കാനും ഒന്നുമില്ല."),
 ("A","A","അത് നിന്റെ കണക്ക്. നിയമത്തിന്റെ കണക്ക് വേറെയാ."),
 ("V","wide","എന്ത് കണക്ക്?"),
 ("A","wide","ലിമിറ്റ് കടന്നിട്ടും രജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ ടാക്സ്, 18% പലിശ, 10,000 രൂപയോ ടാക്സിന്റെ 10%-ഓ, ഏതാണോ കൂടുതൽ അത് പിഴ."),
 ("V","V","കുട വിറ്റു, പിഴയിൽ നനഞ്ഞു.")],
 "കുട വിറ്റു,\nപിഴയിൽ നനഞ്ഞു", CTA_PENALTY, theme="new",
 cap_ml="ഉത്സവക്കുട കച്ചവടം 52 ലക്ഷം കടന്നു, GST വാങ്ങിയിട്ടില്ലാത്തതുകൊണ്ട് അടയ്ക്കാനും ഇല്ലെന്ന് കരുതി. രജിസ്റ്റർ ചെയ്യേണ്ടിയിരുന്നിട്ടും ചെയ്തില്ലെങ്കിൽ ടാക്സ്, 18% പലിശ, 10,000 രൂപയോ ടാക്സിന്റെ 10%-ഓ ഏതാണോ കൂടുതൽ അത് പിഴ. നിങ്ങളുടെ ടേൺഓവർ 40 ലക്ഷത്തിന് അടുത്തോ?",
 cap_en="A festival-umbrella maker crossed 52 lakh in sales and thought that since he never collected GST, he owed none. If registration was required, you still pay the tax, 18% interest, and a penalty of 10,000 rupees or 10% of the tax, whichever is higher. Is your turnover near 40 lakh?",
 cap_mg="Utsavakkuda kachavadam 52 lakh kadannu, GST vaangiyittillaathathukondu adaykkaanum illa ennu karuthi. Register cheyyendiyirunnittum cheythillenkil tax, 18% palisha, 10,000 roopayo taxinte 10%-o ethaano kooduthal athu pizha. Ningalude turnover 40 lakhinu aduttho?")

chat("gc003", "trader", "A", "ബെംഗളൂരു ഓർഡർ:\n200 പാക്കറ്റ് കപ്പ ചിപ്സ്.\n\"ടേൺഓവർ ചെറുതല്ലേ?\"", ("സുമ", "ആന്റണി"), [
 (1,"സുമേ, ബെംഗളൂരുവിലെ ഒരു സൂപ്പർമാർക്കറ്റ് 200 പാക്കറ്റ് കപ്പ ചിപ്സ് ചോദിച്ചു. GST ബില്ല് വേണമെന്ന്."),
 (0,"ആന്റണീ, നമ്മുടെ ടേൺഓവർ 12 ലക്ഷമല്ലേ ഉള്ളൂ. 40 ആകാതെ GST എടുക്കണോ?"),
 (1,"എടുക്കാമോ എന്നല്ല, എടുക്കണം. ഇത് കർണാടകയിലേക്കുള്ള വിൽപ്പനയാ."),
 (0,"അതിനും ലിമിറ്റ് ഇല്ലേ?"),
 (1,"മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിൽക്കുമ്പോൾ ലിമിറ്റ് നോക്കില്ല. ആദ്യ ലോഡ് മുതൽ GST നിർബന്ധം."),
 (0,"എങ്കിൽ ഇന്ന് അപേക്ഷ, പിന്നെ ചിപ്സ്.")],
 "ലോഡ് അതിർത്തി കടക്കും\nമുമ്പ് GST", CTA_GST, theme="crm",
 cap_ml="വീട്ടിലെ കപ്പ ചിപ്സ് യൂണിറ്റിന് ബെംഗളൂരുവിലെ സൂപ്പർമാർക്കറ്റിൽ നിന്ന് ഓർഡർ. ടേൺഓവർ 40 ലക്ഷത്തിന് താഴെയാണെങ്കിലും മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിൽക്കാൻ ആദ്യ വിൽപ്പന മുതൽ GST വേണം. നിങ്ങൾക്ക് കേരളത്തിന് പുറത്ത് നിന്ന് ഓർഡർ വന്നിട്ടുണ്ടോ?",
 cap_en="A home tapioca chips unit gets an order from a Bengaluru supermarket that wants a GST bill. Turnover is far below 40 lakh, but selling goods to another state needs GST registration from the first sale. Ever had an order from outside Kerala: yes or no?",
 cap_mg="Veettile kappa chips unit-inu Bengaluru-ile supermarket-il ninnu order. Turnover 40 lakhinu thaazheyaanenkilum vere state-ilekku saadhanam vilkkaan aadya vilppana muthal GST venam. Ningalkku Kerala-kku purathu ninnu order vannittundo?")
