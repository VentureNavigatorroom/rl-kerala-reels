# GST batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd018", "online_seller", "A", "tailor", "\"ഇൻസ്റ്റഗ്രാം\nകടയല്ലല്ലോ,\nപിന്നെന്തിന് GST?\"", [
 ("A","wide","മോഹനേട്ടാ, കസവ് സാരിക്ക് ബംഗളൂരുവിൽ നിന്ന് ഓർഡർ! ഇൻസ്റ്റഗ്രാമിൽ മാത്രമേ വിൽക്കുന്നുള്ളൂ, കട ഇല്ലല്ലോ."),
 ("V","V","ഉഷേ, കട ഇല്ലെങ്കിലും സാരി കേരളം കടന്നാണ് പോകുന്നത്."),
 ("A","A","എന്റെ ടേൺഓവർ ചെറുതാ. ലിമിറ്റ് ഒന്നും എത്തിയിട്ടില്ല."),
 ("V","wide","മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം വിറ്റാൽ ലിമിറ്റ് നോക്കില്ല. ആദ്യ വിൽപ്പന മുതൽ GST വേണം."),
 ("A","A","അപ്പോ ആപ്പ് ഏതായാലും നിയമം ഒന്ന്."),
 ("V","wide","ഫോളോവേഴ്സിന് അതിർത്തിയില്ല, GST-ക്ക് ഉണ്ട്.")],
 "ഫോളോവേഴ്സിന് അതിർത്തിയില്ല,\nGST-ക്ക് ഉണ്ട്", CTA_GST, names=("ഉഷ", "മോഹനൻ"), theme="faq",
 cap_ml="ഇൻസ്റ്റഗ്രാമിൽ മാത്രം വിൽക്കുന്നവർക്ക് GST വേണോ? സാധനം മറ്റൊരു സംസ്ഥാനത്തേക്ക് പോകുന്നെങ്കിൽ ടേൺഓവർ എത്രയായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം. നിങ്ങളുടെ ഓർഡറുകൾ കേരളത്തിന് പുറത്ത് പോകാറുണ്ടോ?",
 cap_en="Do you need GST if you only sell on Instagram? If the goods go to another state, GST registration is needed from the first sale, whatever your turnover. Do your Instagram orders ever leave Kerala: yes or no?",
 cap_mg="Instagram-il maathram vilkkunnavarkku GST veno? Saadhanam vere state-ilekku pokunnenkil turnover ethrayaayaalum aadya vilppana muthal GST venam. Ningalude orders Kerala-kku purathu pokaarundo?")

duo("gd019", "trader", "B", "kitchen", "സൂപ്പർമാർക്കറ്റ് ഓർഡർ.\nGST അപേക്ഷ നിന്നു:\nവാടക അടുക്കള", [
 ("A","wide","രാജേഷേ, അച്ചാറിന് സൂപ്പർമാർക്കറ്റ് ഓർഡർ കിട്ടി. GST ബില്ല് വേണമെന്ന്. പക്ഷേ ഈ അടുക്കള വാടകയ്ക്കാ."),
 ("V","V","ബിന്ദു ചേച്ചീ, ലിമിറ്റിന് താഴെയാണെങ്കിലും സ്വമേധയാ GST എടുക്കാം. വാടക സ്ഥലമാണെങ്കിൽ മൂന്ന് പേപ്പർ."),
 ("A","A","ഏതൊക്കെ?"),
 ("V","wide","വാടക എഗ്രിമെന്റ്, ഉടമയുടെ NOC, ഒരു ബില്ല്. കൂടെ PAN, ആധാർ, ഫോട്ടോ, ബാങ്ക് പ്രൂഫ്."),
 ("A","A","വീട്ടുടമയെ ഇന്നുതന്നെ വിളിക്കാം."),
 ("V","wide","അച്ചാറിന് ഉപ്പ് പോലെ, അപേക്ഷയ്ക്ക് NOC.")],
 "അച്ചാറിന് ഉപ്പ് പോലെ,\nഅപേക്ഷയ്ക്ക് NOC", CTA_GST, theme="crm",
 cap_ml="വാടക അടുക്കളയിൽ നിന്ന് അച്ചാർ വിൽക്കുന്നയാൾക്ക് സൂപ്പർമാർക്കറ്റ് GST ബില്ല് ചോദിച്ചു. വാടക സ്ഥലത്തിന് വാടക എഗ്രിമെന്റ്, ഉടമയുടെ NOC, ബില്ല് എന്നിവ വേണം; കൂടെ PAN, ആധാർ, ഫോട്ടോ, ബാങ്ക് പ്രൂഫ്. നിങ്ങളുടെ ബിസിനസ് സ്ഥലം: സ്വന്തമോ വാടകയോ?",
 cap_en="A home pickle maker in a rented kitchen gets a supermarket order that needs a GST bill. For a rented address you need the rent agreement, the owner's NOC and a utility bill, plus PAN, Aadhaar, a photo and bank proof. Your business address: owned or rented?",
 cap_mg="Vaadaka adukkalayil ninnu achaar vilkkunnayaalkku supermarket GST bill chodichu. Vaadaka sthalathinu rent agreement, udamayude NOC, bill venam; koode PAN, Aadhaar, photo, bank proof. Ningalude business sthalam: swanthamo vaadakayo?")

duo("gd020", "service_pro", "A", "homestay", "റിസോർട്ട് ഷൂട്ട് കഴിഞ്ഞു.\n\"GSTIN ഇല്ലേ?\nപേമെന്റ് പിന്നെ\"", [
 ("A","wide","ജോമോനേ, ഡ്രോൺ വീഡിയോ സൂപ്പർ. പക്ഷേ ഞങ്ങളുടെ റിസോർട്ട് ഗ്രൂപ്പിന് GSTIN ഉള്ള ഇൻവോയ്സ് വേണം."),
 ("V","V","ടീനേ, എന്റെ വരുമാനം 20 ലക്ഷത്തിന്റെ അടുത്തുപോലും ഇല്ല. GST വലിയവർക്കല്ലേ?"),
 ("A","A","നിർബന്ധമില്ലായിരിക്കാം. പക്ഷേ ഞങ്ങളുടെ അക്കൗണ്ട്സ് ടീമിന് അതില്ലാതെ ബില്ല് പാസാക്കാൻ പറ്റില്ല."),
 ("V","wide","ലിമിറ്റിന് താഴെയാണെങ്കിലും ആർക്കും സ്വമേധയാ GST എടുക്കാം. ടാക്സ് ക്രെഡിറ്റും രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം."),
 ("A","A","അടുത്ത ഷൂട്ടിന് മുമ്പ് എടുത്തോ."),
 ("V","wide","ക്ലയന്റ് നോക്കുന്നത് ടേൺഓവർ അല്ല, GSTIN ആണ്.")],
 "ക്ലയന്റ് നോക്കുന്നത്\nടേൺഓവർ അല്ല,\nGSTIN ആണ്", CTA_GST, theme="crm",
 cap_ml="റിസോർട്ട് ഗ്രൂപ്പ് ഡ്രോൺ വീഡിയോഗ്രാഫറോട് GSTIN ഉള്ള ഇൻവോയ്സ് ചോദിച്ചു. 20 ലക്ഷത്തിന് താഴെയാണെങ്കിലും സ്വമേധയാ GST എടുക്കാം; ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം. ക്ലയന്റ് നിങ്ങളോട് GSTIN ചോദിച്ചിട്ടുണ്ടോ?",
 cap_en="A resort group asks a drone videographer for an invoice with a GSTIN before it pays. Even below the Rs 20 lakh services limit you can register voluntarily, and only registered businesses get input tax credit. Has a client ever asked you for a GSTIN: yes or no?",
 cap_mg="Resort group drone videographer-odu GSTIN ulla invoice chodichu. 20 lakh-inu thaazheyaanenkilum swamedhaya GST edukkaam; input tax credit register cheythavarkku maathram. Client ningalodu GSTIN chodichittundo?")

duo("gd021", "trader", "C", "ferry", "വള്ളംകളി സീസൺ.\n\"സീസൺ കച്ചവടത്തിന്\nലിമിറ്റ് ബാധകമോ?\"", [
 ("A","wide","ടോണീ, നിന്റെ തുഴ കച്ചവടം ഈ വള്ളംകളി സീസണിൽ 46 ലക്ഷം കടന്നെന്ന് കേട്ടു. GST എടുത്തോ?"),
 ("V","V","മീരേ, സീസണിൽ മാത്രമല്ലേ വിൽപ്പന? ബാക്കി മാസം ഒന്നുമില്ല. ലിമിറ്റ് എനിക്ക് ബാധകമല്ല."),
 ("A","A","വർഷത്തിലെ ആകെ കണക്കാ നോക്കുന്നത്. സാധനങ്ങൾക്ക് 40 ലക്ഷം കടന്നാൽ രജിസ്ട്രേഷൻ നിർബന്ധം."),
 ("V","wide","ഇനി വൈകിയാൽ എന്ത് പറ്റും?"),
 ("A","A","ടാക്സ്, 18% പലിശ, പിന്നെ 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ."),
 ("V","wide","വള്ളം ജയിച്ചു, കണക്ക് തോറ്റു.")],
 "വള്ളം ജയിച്ചു,\nകണക്ക് തോറ്റു", CTA_PENALTY, theme="crm",
 cap_ml="വള്ളംകളി സീസണിൽ തുഴ വിൽക്കുന്ന ആളുടെ വിൽപ്പന 40 ലക്ഷം കടന്നു, GST ഇല്ലാതെ. സീസൺ ആണെങ്കിലും വർഷത്തിലെ ആകെ ടേൺഓവർ ആണ് നോക്കുന്നത്; വൈകിയാൽ ടാക്സ്, 18% പലിശ, 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10% പിഴ. നിങ്ങളുടെ കച്ചവടം: സീസണലോ സ്ഥിരമോ?",
 cap_en="A boat-race oar maker sold Rs 46 lakh of goods in one season without GST. The limit counts the whole year's turnover, seasonal or not; registering late means the tax, 18% interest and a penalty of Rs 10,000 or 10% of the tax, whichever is higher. Your business: seasonal or year-round?",
 cap_mg="Vallamkali season-il thuzha vilkkunna aalude vilppana 40 lakh kadannu, GST illaathe. Season aanenkilum varshathile aake turnover aanu nokkunnathu; vaikiyaal tax, 18% palisha, 10,000 allenkil tax-nte 10% pizha. Ningalude kachavadam: seasonal-o sthiramo?")

duo("gd022", "trader", "B", "juiceshop", "4 മാസം കട അടച്ചു.\n\"ഷട്ടർ താഴ്ത്തിയാൽ\nGST-യും അടയില്ലേ?\"", [
 ("A","wide","നൗഷാദിക്കാ, പുതുക്കിപ്പണിക്ക് ജ്യൂസ് കട 4 മാസം അടച്ചിട്ടല്ലേ? GST റിട്ടേൺ ഫയൽ ചെയ്യുന്നുണ്ടോ?"),
 ("V","V","റസിയാ, കട അടഞ്ഞാൽ GST-യും അടഞ്ഞു എന്നാ ഞാൻ കരുതിയത്."),
 ("A","A","GSTIN ഇപ്പോഴും ആക്ടീവ് അല്ലേ?"),
 ("V","wide","അതേ. അപ്പോ വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ ഫയൽ ചെയ്യണം, അല്ലേ?"),
 ("A","A","അതെ. വൈകിയാൽ ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ."),
 ("V","wide","ഷട്ടർ താഴ്ത്തിയാൽ GSTIN താഴില്ല.")],
 "ഷട്ടർ താഴ്ത്തിയാൽ\nGSTIN താഴില്ല", CTA_PENALTY, theme="faq",
 cap_ml="കട കുറച്ചു മാസം അടച്ചാൽ GST റിട്ടേൺ വേണ്ടേ? രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ വേണം; വൈകിയാൽ ദിവസം 20 രൂപ, 500 വരെ. നിങ്ങളുടെ കട ഇപ്പോൾ: തുറന്നതോ അടച്ചതോ?",
 cap_en="Shut your shop for a few months: is GST filing paused too? No. As long as the registration is active, a nil return is due even in months with no sales, and a late nil GSTR-3B costs Rs 20 a day up to Rs 500. Your shop right now: open or shut?",
 cap_mg="Kada kurachu maasam adachaal GST return vende? Registration ullidatholam vilppana illaatha maasavum nil return venam; vaikiyaal divasam 20 roopa, 500 vare. Ningalude kada ippol: thurannatho adachatho?")

duo("gd023", "trader", "A", "pharmacy", "40 ലക്ഷം കടന്നു.\n\"GST എടുത്താൽ കണക്കിൽ\nമുങ്ങിപ്പോകുമോ?\"", [
 ("A","wide","പ്രവീണേ, മെഡിക്കൽ ഷോപ്പ് 40 ലക്ഷം കടന്നു. GST എടുക്കണം. പക്ഷേ കണക്ക് നോക്കാൻ ആളില്ല."),
 ("V","V","സിനി, നിനക്ക് കോമ്പോസിഷൻ സ്കീം അറിയാമോ?"),
 ("A","A","അതെന്താ? വലിയ കമ്പനികൾക്കുള്ളതാണോ?"),
 ("V","wide","അല്ല, ചെറിയവർക്കാ. സാധനങ്ങൾക്ക് ഒന്നര കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ ഉള്ളവർക്ക്."),
 ("A","A","അപ്പോ എന്റെ കട അതിൽ വരും."),
 ("V","wide","ചെറിയ കടയ്ക്ക് ചെറിയ വഴിയുമുണ്ട്.")],
 "ചെറിയ കടയ്ക്ക്\nചെറിയ വഴിയുമുണ്ട്", CTA_LIMIT, theme="faq",
 cap_ml="40 ലക്ഷം കടന്ന കടയ്ക്ക് GST കണക്ക് പേടിയാണോ? സാധനങ്ങൾക്ക് ഒന്നര കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ ഉള്ളവർക്ക് കോമ്പോസിഷൻ സ്കീം ഉണ്ട്. ഈ സ്കീം കേട്ടിട്ടുണ്ടോ?",
 cap_en="Crossed Rs 40 lakh and scared of GST paperwork? The composition scheme is open to businesses with turnover up to Rs 1.5 crore for goods and Rs 50 lakh for services. Had you heard of the composition scheme: yes or no?",
 cap_mg="40 lakh kadanna kadakku GST kanakku pediyaano? Goods-nu 1.5 crore vare, service-nu 50 lakh vare turnover ullavarkku composition scheme undu. Ee scheme kettittundo?")

duo("gd024", "trader", "C", "mall", "ചെന്നൈയിൽ 10 ദിവസം\nനെറ്റിപ്പട്ടം സ്റ്റാൾ.\n\"അതിനും GST?\"", [
 ("A","wide","ജാഫറിക്കാ, ചെന്നൈ എക്സ്പോയിൽ നമ്മുടെ നെറ്റിപ്പട്ടം സ്റ്റാൾ 10 ദിവസം. GST വേണോ?"),
 ("V","V","സുമയ്യാ, 10 ദിവസത്തെ കച്ചവടത്തിന് എന്ത് GST? ടേൺഓവർ ചെറുതല്ലേ?"),
 ("A","A","പക്ഷേ ഇത് മറ്റൊരു സംസ്ഥാനത്തെ താൽക്കാലിക സ്റ്റാൾ ആണ്."),
 ("V","wide","എങ്കിൽ കാഷ്വൽ ടാക്സബിൾ പേഴ്സൺ ആയി രജിസ്ട്രേഷൻ വേണം. ടേൺഓവർ നോക്കാതെ നിർബന്ധം."),
 ("A","A","ടിക്കറ്റ് ബുക്ക് ചെയ്യുന്നതിന് മുമ്പ് അത് ചെയ്യാം."),
 ("V","wide","സ്റ്റാൾ താൽക്കാലികം, നിയമം സ്ഥിരം.")],
 "സ്റ്റാൾ താൽക്കാലികം,\nനിയമം സ്ഥിരം", CTA_GST, theme="new",
 cap_ml="മറ്റൊരു സംസ്ഥാനത്തെ എക്സ്പോയിൽ 10 ദിവസത്തെ സ്റ്റാളിന് GST വേണോ? താൽക്കാലികമായി കച്ചവടം ചെയ്യുന്നവർക്ക് കാഷ്വൽ ടാക്സബിൾ പേഴ്സൺ രജിസ്ട്രേഷൻ ടേൺഓവർ നോക്കാതെ നിർബന്ധം. അടുത്ത എക്സ്പോ എവിടെ?",
 cap_en="A Kerala nettipattam maker takes a 10-day stall at an expo in Chennai: does that need GST? Yes. A casual taxable person must register whatever the turnover. Where is your next expo?",
 cap_mg="Vere state-ile expo-yil 10 divasathe stall-inu GST veno? Thaalkaalikamaayi kachavadam cheyyunnavarkku casual taxable person registration turnover nokkaathe nirbandham. Adutha expo evide?")

duo("gd025", "service_pro", "B", "railway", "ഉത്സവ സീസൺ തിരക്ക്.\n3B മൂന്ന് മാസം മറന്നു.\nഓരോ ദിവസവും 50", [
 ("A","wide","ദിനേശേട്ടാ, തോൽപ്പാവക്കൂത്ത് ട്രൂപ്പിന്റെ GSTR-3B മൂന്ന് മാസമായി ഫയൽ ചെയ്തിട്ടില്ല."),
 ("V","V","ഷീബേ, ഉത്സവ സീസണിൽ ആരാ കണക്ക് നോക്കുന്നത്? ഷോ കഴിഞ്ഞിട്ട് ചെയ്യാം."),
 ("A","A","ഷോയ്ക്ക് വേണ്ടി നിയമം കാത്തുനിൽക്കില്ല."),
 ("V","wide","വൈകിയാൽ ഒരു റിട്ടേണിന് ദിവസം 50 രൂപ. ഒന്നര കോടി വരെ ടേൺഓവർ ഉള്ളവർക്ക് 2,000 വരെ."),
 ("A","A","മൂന്ന് മാസം, മൂന്ന് റിട്ടേൺ. ഇന്ന് രാത്രി തന്നെ ഇരിക്കാം."),
 ("V","wide","കർട്ടൻ വീണാലും ഫയലിംഗ് തീയതി വീഴില്ല.")],
 "കർട്ടൻ വീണാലും\nഫയലിംഗ് തീയതി\nവീഴില്ല", CTA_PENALTY, theme="new",
 cap_ml="ഉത്സവ സീസണിൽ GSTR-3B മറന്ന തോൽപ്പാവക്കൂത്ത് ട്രൂപ്പ്. വൈകിയ ഓരോ റിട്ടേണിനും ദിവസം 50 രൂപ, ഒന്നര കോടി വരെ ടേൺഓവർ ഉള്ളവർക്ക് 2,000 വരെ. നിങ്ങളുടെ ഫോണിൽ GST റിമൈൻഡർ ഉണ്ടോ?",
 cap_en="A shadow-puppet troupe forgot its GSTR-3B through the festival season. Each late return costs Rs 50 a day, capped at Rs 2,000 for turnover up to Rs 1.5 crore. Is the GST due date in your phone: yes or no?",
 cap_mg="Ulsava season-il GSTR-3B marannu poya tholpaavakoothu troupe. Vaikiya oro return-inum divasam 50 roopa, 1.5 crore vare turnover ullavarkku 2,000 vare. Ningalude phone-il GST reminder undo?")

chat("gc002", "trader", "A", "HR ചോദിച്ചു:\n\"ദീപാവലി ഹാമ്പറിന്\nGST ബില്ല് തരുമോ?\"", ("ആതിര", "ദിവ്യ"), [
 (0,"ദിവ്യേച്ചീ, ഒരു IT കമ്പനി 300 ചോക്ലേറ്റ് ഹാമ്പർ ചോദിച്ചു. GST ബില്ല് വേണമെന്ന്."),
 (1,"ആതിരേ, നിന്റെ വിൽപ്പന ലിമിറ്റിന് താഴെയല്ലേ? എന്നാലും സ്വമേധയാ GST എടുക്കാം."),
 (0,"എന്തൊക്കെ രേഖ വേണം? ഡിസംബർ ഒന്നിന് ഡെലിവറിയാ."),
 (1,"PAN, ആധാർ, ഫോട്ടോ, അഡ്രസ്സ് പ്രൂഫ്, ബാങ്ക് പ്രൂഫ്. റിസ്ക് കുറവാണെങ്കിൽ 3 വർക്കിംഗ് ദിവസത്തിൽ അപ്രൂവൽ."),
 (0,"ഇന്ന് തന്നെ എല്ലാം സ്കാൻ ചെയ്യാം!"),
 (1,"ഓർഡർ വലുതാകുമ്പോൾ ബില്ലും ഔദ്യോഗികമാകണം.")],
 "ഓർഡർ വലുതായാൽ\nബില്ലും വലുതാകണം", CTA_GST, theme="crm",
 cap_ml="വീട്ടിൽ ചോക്ലേറ്റ് ഉണ്ടാക്കുന്നയാളോട് IT കമ്പനി GST ബില്ല് ചോദിച്ചു. ലിമിറ്റിന് താഴെയാണെങ്കിലും സ്വമേധയാ എടുക്കാം: PAN, ആധാർ, ഫോട്ടോ, അഡ്രസ്സ് പ്രൂഫ്, ബാങ്ക് പ്രൂഫ്. നിങ്ങൾക്ക് കോർപ്പറേറ്റ് ഓർഡർ കിട്ടിയിട്ടുണ്ടോ?",
 cap_en="A home chocolatier gets a 300-hamper Diwali order from an IT company that wants a GST bill. Below the limit you can still register voluntarily with PAN, Aadhaar, a photo, address proof and bank proof; low-risk applications are auto-approved within 3 working days. Ever had a corporate order: yes or no?",
 cap_mg="Veettil chocolate undaakkunnayaalodu IT company GST bill chodichu. Limit-inu thaazheyaanenkilum swamedhaya edukkaam: PAN, Aadhaar, photo, address proof, bank proof. Ningalkku corporate order kittiyittundo?")

lst("gl002", "new_company", "B", "GST അപേക്ഷ\nകുടുങ്ങുന്ന\n3 ഇടങ്ങൾ", [
 ("ആധാർ മൊബൈൽ", "OTP ആധാറുമായി ബന്ധിപ്പിച്ച നമ്പറിൽ. ആ സിം ഇപ്പോഴും ഉണ്ടോ എന്ന് നോക്കൂ."),
 ("വാടക സ്ഥലം", "വാടക എഗ്രിമെന്റ്, ഉടമയുടെ NOC, ഒരു ബില്ല്: മൂന്നും വേണം."),
 ("ഫിസിക്കൽ വെരിഫിക്കേഷൻ", "ഓഫീസർ സ്ഥലം നോക്കാൻ വന്നാൽ അപ്രൂവൽ 30 ദിവസം വരെ നീളാം.")],
 "പേപ്പർ റെഡി,\nഅപേക്ഷ റെഡി", CTA_GST, theme="faq",
 cap_ml="GST അപേക്ഷ വൈകുന്ന 3 ഇടങ്ങൾ: ആധാറുമായി ബന്ധിപ്പിച്ച മൊബൈൽ, വാടക സ്ഥലത്തിന്റെ NOC, ഫിസിക്കൽ വെരിഫിക്കേഷൻ (30 ദിവസം വരെ). ഇതിൽ ഏതിലാണ് നിങ്ങൾ കുടുങ്ങിയത്?",
 cap_en="Three places a GST application gets stuck: the mobile linked to Aadhaar (the OTP goes there), the owner's NOC for a rented address, and physical verification, which can stretch approval to 30 days. Which one held you up?",
 cap_mg="GST apeksha vaikunna 3 idangal: Aadhaar-umaayi link cheytha mobile, vaadaka sthalathinte NOC, physical verification (30 divasam vare). Ithil ethilaanu ningal kudungiyathu?")
