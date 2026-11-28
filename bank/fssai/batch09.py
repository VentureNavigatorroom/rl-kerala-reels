# FSSAI batch 09 (28 Nov night refill). Facts only from topics.FACTS_FSSAI (2026 limits: Rs 1.5 crore / Rs 50 crore). No prices. Max 6 lines.
# The fact list is nearly used up: only new situations / angles (food truck pitch, surrender after the new limits, paying the yearly
# amount ahead from abroad, a borrowed number on a delivery app, selling while the application is pending, "perpetual" still ends).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# crm (STORY_THEMES C8): a hotel-management graduate pitches a food truck for funding with no FSSAI planned
duo("fsd004", "cafe_owner", "B", "beach", "ഫുഡ് ട്രക്കിന് ഫണ്ട്\nചോദിച്ചു. ഇൻവെസ്റ്റർ:\n\"FSSAI എവിടെ?\"", [
 ("A","wide","നിഖിലേ, ബീച്ചിലെ ഫുഡ് ട്രക്കിന് ഫണ്ട് ചോദിച്ചു. ഇൻവെസ്റ്റർ ആദ്യം ചോദിച്ചത് FSSAI നമ്പർ!"),
 ("V","V","ദിവ്യേ, ട്രക്ക് പോലും വാങ്ങിയില്ലല്ലോ. നമ്പർ ഒക്കെ പിന്നെ പോരേ?"),
 ("A","A","FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. അതുകൊണ്ട് പ്ലാനിൽ അത് ആദ്യം വേണമെന്ന്."),
 ("V","V","ആദ്യ വർഷം ഒന്നര കോടിക്ക് താഴെയല്ലേ? സാധാരണ ബേസിക് രജിസ്ട്രേഷൻ. പക്ഷേ FoSCoS-ൽ നമ്മുടെ കാറ്റഗറി ആദ്യം നോക്കണം."),
 ("A","A","അപ്പോ ട്രക്കിന്റെ പെയിന്റിന് മുമ്പ് പേപ്പർ."),
 ("V","wide","ചക്രം ഉരുളും മുമ്പ് നമ്പർ ഉറയ്ക്കണം.")],
 "ചക്രം ഉരുളും മുമ്പ്\nFSSAI നമ്പർ", CTA_FSSAI, theme="crm",
 cap_ml="ഫുഡ് ട്രക്കിന് ഫണ്ട് ചോദിക്കും മുമ്പ് FSSAI പ്ലാനിൽ വേണം. FSSAI ഇല്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും. വർഷം 1.5 കോടി വരെ ടേൺഓവറിന് സാധാരണ ബേസിക് രജിസ്ട്രേഷൻ, പക്ഷേ FoSCoS-ൽ കാറ്റഗറി ആദ്യം നോക്കൂ. നിങ്ങളുടെ ട്രക്ക് എവിടെ ഓടും?",
 cap_en="Pitching a food truck to an investor? Put FSSAI in the plan first: selling food without it can mean a penalty up to 5 lakh and up to 6 months in prison. Up to 1.5 crore turnover a year usually means basic registration, but check your category on FoSCoS first. Where will your truck run?",
 cap_mg="Food truck-inu fund chodikkum mumpu FSSAI plan-il venam. FSSAI illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum. Varsham 1.5 crore vare turnover-inu saadhaarana basic registration, pakshe FoSCoS-il category aadyam nokku. Ningalude truck evide odum?")

# new: a home caterer took a state licence long ago for hotel orders; under the 2026 limits her turnover sits in the lower category
duo("fsd005", "home_baker", "B", "kitchen", "70 ലക്ഷം ടേൺഓവർ.\nകയ്യിൽ സ്റ്റേറ്റ് ലൈസൻസ്.\nഇനിയും അത് വേണോ?", [
 ("A","wide","രാജേഷേ, പണ്ട് ഹോട്ടൽ ഓർഡറിന് വേണ്ടി എടുത്ത സ്റ്റേറ്റ് ലൈസൻസ് ഇപ്പോഴും കയ്യിലുണ്ട്. ടേൺഓവർ 70 ലക്ഷമേ ഉള്ളൂ."),
 ("V","V","ബിന്ദൂ, 2026 ഏപ്രിൽ മുതൽ 1.5 കോടി വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി. താഴ്ന്ന കാറ്റഗറിയിൽ ആയാൽ ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം."),
 ("A","A","അപ്പോ ഇന്ന് തന്നെ സറണ്ടർ ചെയ്യാം!"),
 ("V","V","ആദ്യം FoSCoS-ൽ നമ്മുടെ ബിസിനസ് കാറ്റഗറി നോക്ക്. ചില തരം ബിസിനസിന് ടേൺഓവർ നോക്കാതെ ലൈസൻസ് വേണം."),
 ("A","A","കാറ്റഗറി ശരിയായാൽ മാത്രം മാറ്റം."),
 ("V","wide","വലിയ ലൈസൻസ് അല്ല, ശരിയായ ലൈസൻസ്.")],
 "ടേൺഓവർ താഴെയോ?\nകാറ്റഗറി നോക്കി മാറാം", CTA_FSSAI, theme="new",
 cap_ml="പണ്ട് എടുത്ത സ്റ്റേറ്റ് FSSAI ലൈസൻസ് ഇപ്പോഴും കയ്യിലുണ്ടോ? 2026 ഏപ്രിൽ മുതൽ 1.5 കോടി വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. താഴ്ന്ന കാറ്റഗറിയിൽ ആയ ബിസിനസിന് ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം, പക്ഷേ ആദ്യം FoSCoS-ൽ കാറ്റഗറി നോക്കൂ. നിങ്ങളുടെ കയ്യിൽ ഏതാണ്?",
 cap_en="Still holding a state FSSAI licence you took years ago? Since April 2026, basic registration covers turnover up to 1.5 crore. A business that now falls in a lower category can surrender its licence for a registration, but check your category on FoSCoS first: some kinds of business need a licence whatever the turnover. Which one do you hold?",
 cap_mg="Pandu eduttha State FSSAI licence ippozhum kayyil undo? 2026 April muthal 1.5 crore vare turnover-inu basic registration mathi. Thaazhnna category-il aaya business-inu licence surrender cheythu registration edukkaam, pakshe aadyam FoSCoS-il category nokku. Ningalude kayyil ethaanu?")

# crm: a Gulf worker's mother runs the snack shop; the licence came after April 2026; he is away for two years
duo("fsd006", "cafe_owner", "B", "gulf", "ലൈസൻസ് നാട്ടിൽ.\nഞാൻ രണ്ട് കൊല്ലം ദുബായിൽ.\nവാർഷിക അടവ് ആര്?", [
 ("A","wide","ഫൈസലേ, ഉമ്മയുടെ പലഹാരക്കടയുടെ FSSAI കാര്യം ആര് നോക്കും? നീ രണ്ട് കൊല്ലം ഇവിടെ അല്ലേ?"),
 ("V","V","ഷിജൂ, 2026 മേയിൽ കിട്ടിയ ലൈസൻസാ. സ്ഥിരം സാധുതയുണ്ട്. പുതുക്കൽ വേണ്ട."),
 ("A","A","പുതുക്കൽ വേണ്ട, ശരി. പക്ഷേ FSSAI-ക്കുള്ള വാർഷിക അടവ് എല്ലാ കൊല്ലവും ഉണ്ട്. വാർഷിക റിട്ടേണും."),
 ("V","V","ഉമ്മ അത് മറക്കും. ഞാൻ ഇവിടെ ഇരുന്ന് എന്ത് ചെയ്യും?"),
 ("A","A","അടവ് കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് മുൻകൂട്ടി അടയ്ക്കാം. റിട്ടേൺ നോക്കാൻ നാട്ടിൽ ഒരാളെ ഏൽപ്പിക്ക്."),
 ("V","wide","ദൂരം കൂടിയാൽ, അടവ് മുൻകൂട്ടി.")],
 "ദൂരെ പോകും മുമ്പ്\nഅടവ് മുൻകൂട്ടി", CTA_FSSAI, theme="crm",
 cap_ml="2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ FSSAI ലൈസൻസിന് പുതുക്കൽ വേണ്ട, പക്ഷേ FSSAI-ക്കുള്ള വാർഷിക അടവും വാർഷിക റിട്ടേണും തുടരും. ഗൾഫിലേക്ക് പോകുന്നെങ്കിൽ കുറച്ച് വർഷത്തെ അടവ് ഒരുമിച്ച് മുൻകൂട്ടി അടയ്ക്കാം. പ്രവാസിയായ ഒരാൾക്ക് ഇത് അയച്ചുകൊടുക്കൂ. നിങ്ങളുടെ കടയുടെ FSSAI ആരാണ് നോക്കുന്നത്?",
 cap_en="An FSSAI licence issued on or after 1 April 2026 needs no renewal, but the yearly payment to FSSAI and the annual return continue. Leaving for the Gulf? You can pay several years of the yearly amount ahead. Send this to someone who runs a family food shop from abroad. Who looks after your shop's FSSAI?",
 cap_mg="2026 April 1 muthal kittiya FSSAI licence-inu renew venda, pakshe FSSAI-kkulla annual payment-um annual return-um thudarum. Gulf-ilekku pokunnenkil kurachu varshathe adavu orumichu munkootti adakkaam. Pravaasiyaaya oraalkku ithu ayachukodukku. Ningalude kadayude FSSAI aaraanu nokkunnathu?")

# faq: a new burger kitchen wants to list on a delivery app with a cousin's hotel number
duo("fsd007", "cloud_kitchen", "B", "foodcourt", "\"ആപ്പിൽ കസിന്റെ\nFSSAI നമ്പർ\nഇട്ടാൽ പോരേ?\"", [
 ("A","wide","ഡെന്നിസേ, നമ്മുടെ ബർഗർ കിച്ചൺ ഡെലിവറി ആപ്പിൽ ഇടാൻ നോക്കി. ആദ്യം ചോദിച്ചത് FSSAI നമ്പർ."),
 ("V","V","മരിയേ, കസിന്റെ ഹോട്ടലിന് നമ്പർ ഉണ്ടല്ലോ. തൽക്കാലം അത് ഇട്ടാലോ?"),
 ("A","A","അത് അവന്റെ അടുക്കളയുടെ നമ്പറാ. നമ്മുടേത് വേറെ ബിസിനസ് അല്ലേ?"),
 ("V","V","എങ്കിൽ നമുക്ക് സ്വന്തം വേണം. ടേൺഓവർ ചെറുതാ, ബേസിക് രജിസ്ട്രേഷൻ മതിയാകുമോ?"),
 ("A","A","1.5 കോടി വരെ സാധാരണ അതെ, FoSCoS-ൽ കാറ്റഗറി ഉറപ്പാക്കണം. സ്വന്തം FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ."),
 ("V","wide","കടം വാങ്ങിയ നമ്പർ, കടം കയറ്റും.")],
 "സ്വന്തം അടുക്കളയ്ക്ക്\nസ്വന്തം നമ്പർ", CTA_FOOD, theme="faq",
 cap_ml="ഡെലിവറി ആപ്പുകൾ FSSAI നമ്പർ ചോദിക്കും. കസിന്റെയോ കൂട്ടുകാരന്റെയോ ഹോട്ടലിന്റെ നമ്പർ നിങ്ങളുടെ അടുക്കളയുടേതല്ല. വർഷം 1.5 കോടി വരെ ടേൺഓവറിന് സാധാരണ ബേസിക് രജിസ്ട്രേഷൻ, FoSCoS-ൽ കാറ്റഗറി നോക്കൂ. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. ആപ്പിൽ ലിസ്റ്റ് ചെയ്യാൻ പോകുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="Delivery apps ask for your FSSAI number, and a cousin's hotel number belongs to his kitchen, not yours. Up to 1.5 crore turnover a year usually means basic registration; check your category on FoSCoS. Selling without FSSAI can mean a penalty up to 5 lakh. Send this to a friend about to list a kitchen on an app.",
 cap_mg="Delivery apps FSSAI number chodikkum. Cousin-inteyo koottukaarenteyo hotel-inte number ningalude adukkalayudethalla. Varsham 1.5 crore vare turnover-inu saadhaarana basic registration, FoSCoS-il category nokku. FSSAI illaathe vittaal 5 lakh vare pizha. App-il list cheyyaan pokunna oraalkku ithu ayakku.")

# faq: a retired couple applied for FSSAI for their pickles and want to sell while the number is pending
duo("fsd008", "packaged_food", "B", "veranda", "\"അപേക്ഷ കൊടുത്തല്ലോ.\nനമ്പർ വരും വരെ\nവിറ്റാൽ എന്താ?\"", [
 ("A","wide","ബാലേട്ടാ, മാങ്ങാ അച്ചാറിന്റെ FSSAI അപേക്ഷ കൊടുത്തു. പള്ളിപ്പെരുന്നാളിന് 200 കുപ്പി ഇപ്പോഴേ വിറ്റാലോ?"),
 ("V","V","ശാന്തേ, നമ്പർ വന്നോ? കുപ്പിയുടെ ലേബലിൽ എന്ത് അടിക്കും?"),
 ("A","A","നമ്പറിന്റെ സ്ഥലം ഒഴിച്ചിട്ടു. വന്നിട്ട് പേന കൊണ്ട് എഴുതാം."),
 ("V","V","പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം. നമ്പർ ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 ("A","A","അപ്പോ പെരുന്നാൾ അടുത്ത കൊല്ലവും വരും. നമ്പർ ആദ്യം."),
 ("V","wide","അച്ചാർ കാത്തിരിക്കും, നിയമം കാത്തിരിക്കില്ല.")],
 "അപേക്ഷയല്ല,\nനമ്പർ കിട്ടിയിട്ട് വിൽപ്പന", CTA_FOOD, theme="faq",
 cap_ml="FSSAI അപേക്ഷ കൊടുത്തു, നമ്പർ വന്നിട്ടില്ല. അപ്പോഴേ അച്ചാർ വിൽക്കാമോ? പാക്ക് ചെയ്ത ഫുഡിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ വേണം. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും. ലേബലിൽ നമ്പറിന്റെ സ്ഥലം ഒഴിച്ചിട്ടവർക്ക് ഇത് അയക്കൂ.",
 cap_en="Applied for FSSAI and the number hasn't come yet: can you start selling? Packaged food must carry the 14-digit FSSAI number on the label, and selling without FSSAI can mean a penalty up to 5 lakh and up to 6 months in prison. Send this to someone who left a blank space for the number on their label.",
 cap_mg="FSSAI apeksha koduthu, number vannittilla. Appozhe achaar vilkkaamo? Pack cheytha food-inte label-il 14 akka FSSAI number venam. FSSAI illaathe vittaal 5 lakh vare pizhayum 6 maasam vare thadavum. Label-il number-inte sthalam ozhichittavarkku ithu ayakku.")

# faq: "perpetual" read as "can never be lost": valid until suspended, cancelled or surrendered
duo("fsd009", "cafe_owner", "B", "cafe", "\"സ്ഥിരം ലൈസൻസ് അല്ലേ.\nഇനി എന്ത് ചെയ്താലും\nപോകില്ല\"", [
 ("A","wide","റോഷാ, നമ്മുടെ കഫേക്ക് ജൂണിൽ കിട്ടിയ FSSAI ലൈസൻസ് സ്ഥിരമല്ലേ? ഇനി ആര് വന്നാലും പേടിക്കണ്ട."),
 ("V","V","ആൽവിനേ, സ്ഥിരം എന്നാൽ പുതുക്കാൻ അപേക്ഷിക്കേണ്ട എന്നേ ഉള്ളൂ."),
 ("A","A","പിന്നെ? അത് തന്നെയല്ലേ സ്ഥിരം?"),
 ("V","V","സസ്പെൻഡ് ചെയ്യുകയോ റദ്ദാക്കുകയോ സറണ്ടർ ചെയ്യുകയോ ചെയ്യുന്നത് വരെയാണ് സാധുത. വാർഷിക അടവും റിട്ടേണും മുടക്കരുത്."),
 ("A","A","അപ്പോ സ്ഥിരം എന്ന വാക്കിൽ ഉറങ്ങരുത്."),
 ("V","wide","പുതുക്കൽ പോയി. ശ്രദ്ധ പോകരുത്.")],
 "സ്ഥിരം ലൈസൻസ്,\nസ്ഥിരം ശ്രദ്ധ", CTA_FSSAI, theme="faq",
 cap_ml="2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ FSSAI രജിസ്ട്രേഷനും ലൈസൻസിനും സ്ഥിരം സാധുത എന്നാൽ പുതുക്കാൻ അപേക്ഷിക്കേണ്ട എന്നാണ്. സസ്പെൻഡ് ചെയ്യുകയോ റദ്ദാക്കുകയോ സറണ്ടർ ചെയ്യുകയോ ചെയ്യുന്നത് വരെയാണ് സാധുത. വാർഷിക അടവും വാർഷിക റിട്ടേണും തുടരും. 'സ്ഥിരം' എന്ന് കേട്ട് എല്ലാം മറന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="Perpetual validity for FSSAI registrations and licences issued on or after 1 April 2026 means no renewal application. The licence stays valid until it is suspended, cancelled or surrendered, and the yearly payment and annual return continue. Send this to someone who heard 'perpetual' and stopped worrying about everything.",
 cap_mg="2026 April 1 muthal kittiya FSSAI registration-num licence-num perpetual validity ennaal renew cheyyaan apekshikkenda ennaanu. Suspend cheyyukayo cancel cheyyukayo surrender cheyyukayo cheyyunnathu vareyaanu validity. Annual payment-um annual return-um thudarum. 'Sthiram' ennu kettu ellaam maranna oraalkku ithu ayakku.")
