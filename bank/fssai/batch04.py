# FSSAI batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# d904 pattern: seasonal festival stall
duo("fs010", "cafe_owner", "A", "park", "ഉത്സവത്തിന് 15 ദിവസം\nഉണ്ണിയപ്പം കട.\n\"ലൈസൻസ് എന്തിന്?\"", [
 ("A","wide","അനന്തൂ, ഉത്സവപ്പറമ്പിലെ നിന്റെ ഉണ്ണിയപ്പം കടയ്ക്ക് FSSAI നമ്പർ എടുത്തോ?"),
 ("V","V","ഗായത്രീ, പതിനഞ്ച് ദിവസത്തെ കച്ചവടമല്ലേ. ബാക്കി കൊല്ലം മുഴുവൻ കട അടച്ചിടും."),
 ("A","A","ദിവസം എത്രയായാലും ഭക്ഷണം വിൽക്കുന്നത് ഫുഡ് ബിസിനസ് തന്നെ."),
 ("V","wide","അപ്പോ ഇത്ര ചെറിയ കച്ചവടത്തിനും വേണോ?"),
 ("A","wide","വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ വരാം."),
 ("V","V","കച്ചവടം സീസണിൽ, നിയമം എല്ലാ സീസണിലും.")],
 "ചെറിയ കടയ്ക്കും\nബേസിക് രജിസ്ട്രേഷൻ", CTA_FOOD, theme="new",
 cap_ml="ഉത്സവത്തിന് 15 ദിവസം മാത്രം തുറക്കുന്ന ഉണ്ണിയപ്പം കടയ്ക്കും FSSAI വേണം. വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി; ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങളുടെ കച്ചവടം: സീസണലോ, വർഷം മുഴുവനോ?",
 cap_en="A festival snack stall that opens for just 15 days still needs FSSAI. Basic registration covers turnover up to 12 lakh a year; selling without it can mean a penalty of up to 5 lakh. Your food business: seasonal or year-round?",
 cap_mg="Ulsavathinu 15 divasam maathram thurakkunna unniyappam kadaykkum FSSAI venam. Varsham 12 lakh vare basic registration mathi; illaathe vittaal 5 lakh vare pizha. Ningalude kachavadam: seasonal-o, varsham muzhuvano?")

# d904 pattern: gym-made protein laddoos
duo("fs011", "packaged_food", "B", "gym", "\"ജിമ്മിലെ പിള്ളേർക്ക്\nമാത്രമല്ലേ വിൽക്കുന്നത്?\"\nമാസം 200 പാക്കറ്റ്", [
 ("A","wide","ജസ്റ്റിൻ, കൗണ്ടറിൽ വെച്ച ആ പ്രോട്ടീൻ ലഡ്ഡു പാക്കറ്റിൽ FSSAI നമ്പർ കാണുന്നില്ലല്ലോ."),
 ("V","V","റിയാ, ജിമ്മിലെ മെമ്പർമാർക്ക് മാത്രമല്ലേ. മാസം 200 പാക്കറ്റ്. കടയിൽ വെക്കുന്നില്ലല്ലോ."),
 ("A","A","ആർക്ക് വിൽക്കുന്നു എന്നല്ല, പാക്കറ്റിലാക്കി വിൽക്കുന്നു എന്നതാണ് കാര്യം."),
 ("V","wide","അപ്പോ എന്താ ചെയ്യേണ്ടത്?"),
 ("A","wide","ബേസിക് രജിസ്ട്രേഷൻ എടുക്കണം. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം."),
 ("V","V","മസിലിന് പ്രോട്ടീൻ, പാക്കറ്റിന് നമ്പർ.")],
 "പാക്കറ്റിൽ വിറ്റാൽ\n14 അക്ക നമ്പർ", CTA_FSSAI, theme="new",
 cap_ml="ജിമ്മിലെ അംഗങ്ങൾക്ക് മാത്രം വിൽക്കുന്ന വീട്ടിലുണ്ടാക്കിയ പ്രോട്ടീൻ ലഡ്ഡുവിനും FSSAI വേണം. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം. നിങ്ങളുടെ ജിമ്മിൽ ഇങ്ങനെ വിൽക്കുന്നുണ്ടോ?",
 cap_en="Homemade protein laddoos sold only to gym members still need FSSAI. Packaged food must carry the 14-digit FSSAI number. Does your gym sell snacks like this?",
 cap_mg="Gym members-nu maathram vilkkunna protein laddu-vinum FSSAI venam. Pack cheytha food-il 14 akka number print cheyyanam. Ningalude gym-il ingane vilkkunnundo?")

# CRM #4 / #26 (returnee starting a food business), changed sector and numbers
duo("fs012", "cafe_owner", "A", "gulfoffice", "ദുബായ് വിട്ട് നാട്ടിൽ\nഷവർമ കട. പ്ലാൻ:\n\"ആദ്യം ബേസിക് മതി\"", [
 ("A","wide","ആസിഫ്, നാട്ടിലെ ഷവർമ കടയുടെ പേപ്പറുകൾ റെഡിയായോ? അടുത്ത മാസം അല്ലേ തുടക്കം?"),
 ("V","V","ഷഹാനാ, FSSAI ബേസിക് രജിസ്ട്രേഷൻ എടുക്കാം. ചെറിയ തുടക്കമല്ലേ."),
 ("A","A","ആദ്യ വർഷം എത്ര വിൽപ്പനയാണ് കണക്കാക്കിയത്?"),
 ("V","wide","30 ലക്ഷം. പ്ലാനിൽ അങ്ങനെയാ എഴുതിയത്."),
 ("A","wide","ബേസിക് വർഷം 12 ലക്ഷം വരെ മാത്രം. 30 ലക്ഷം ആണെങ്കിൽ തുടക്കം മുതൽ സ്റ്റേറ്റ് ലൈസൻസ്."),
 ("V","V","പ്ലാൻ വലുതെങ്കിൽ ലൈസൻസും വലുത്.")],
 "പ്ലാനിലെ വിൽപ്പന\nലൈസൻസ് തീരുമാനിക്കും", CTA_FSSAI, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തി ഷവർമ കട തുടങ്ങുന്നു, ആദ്യ വർഷം 30 ലക്ഷം വിൽപ്പന പ്രതീക്ഷിക്കുന്നു. FSSAI ബേസിക് 12 ലക്ഷം വരെ മാത്രം; അതിന് മുകളിൽ സ്റ്റേറ്റ് ലൈസൻസ്. നിങ്ങളുടെ പ്ലാൻ എത്ര?",
 cap_en="A Gulf returnee opening a shawarma shop expects 30 lakh in sales in year one. FSSAI basic registration only covers up to 12 lakh a year, so he needs a state licence from day one. What turnover does your plan show?",
 cap_mg="Gulf-il ninnu thiricheththi shawarma kada thudangunnu, aadya varsham 30 lakh vilppana. FSSAI basic 12 lakh vare maathram; athinu mukalil state licence. Ningalude plan ethra?")

# CRM #29 (woman founder, health food, incubation), changed product and numbers
duo("fs013", "packaged_food", "B", "rooftop", "ഡെമോ ഡേയിൽ ബയർ\n500 പാക്കറ്റ് ചോദിച്ചു.\nലേബലിൽ നമ്പർ ഇല്ല", [
 ("A","wide","ശ്യാം, ഡെമോ ഡേയിൽ ഒരു സൂപ്പർമാർക്കറ്റ് ബയർ നമ്മുടെ റാഗി മിക്സ് 500 പാക്കറ്റ് ചോദിച്ചു!"),
 ("V","V","ആര്യേ, സൂപ്പർ! ഡെലിവറി എന്നാ?"),
 ("A","A","ആദ്യം ലേബലിലെ FSSAI നമ്പർ അയക്കാൻ പറഞ്ഞു. നമ്മുടെ പാക്കറ്റിൽ അതില്ല."),
 ("V","wide","പാക്ക് ചെയ്ത ഭക്ഷണത്തിന് 14 അക്ക നമ്പർ ലേബലിൽ നിർബന്ധം. ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ പ്രിന്റ്."),
 ("A","wide","അപ്പോ 500 ലേബലും വീണ്ടും അടിക്കണം."),
 ("V","V","നമ്പർ ആദ്യം, പാക്കറ്റ് പിന്നെ.")],
 "ലേബൽ അടിക്കും മുമ്പ്\nFSSAI നമ്പർ", CTA_FOOD, theme="crm",
 cap_ml="ഇൻകുബേറ്റർ ഡെമോ ഡേയിൽ സൂപ്പർമാർക്കറ്റ് 500 പാക്കറ്റ് റാഗി മിക്സ് ചോദിച്ചു, പക്ഷേ ലേബലിൽ FSSAI നമ്പർ ഇല്ല. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ നിർബന്ധം. നിങ്ങളുടെ ലേബലിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="At an incubator demo day a supermarket asked for 500 packs of a ragi mix, but the label had no FSSAI number. Packaged food must carry the 14-digit number. Is it on your label?",
 cap_mg="Incubator demo day-il supermarket 500 packet ragi mix chodichu, pakshe label-il FSSAI number illa. Pack cheytha food-il 14 akka number nirbandham. Ningalude label-il number undo?")

# CRM #21 (farm switching to a new product), d904 pattern: mushroom pickle
duo("fs014", "packaged_food", "C", "farm", "\"കൂൺ നമ്മുടെ ഫാമിലേത്.\nഅച്ചാറിന് എന്ത്\nലൈസൻസ്?\"", [
 ("A","wide","ഗോപീ, ബാക്കി വന്ന കൂൺ അച്ചാറാക്കി. ഞായറാഴ്ച ചന്തയിൽ 300 കുപ്പി വിറ്റു!"),
 ("V","V","വാസുവേട്ടാ, കുപ്പിയിൽ FSSAI നമ്പർ ഉണ്ടോ?"),
 ("A","A","കൂൺ നമ്മുടെ ഫാമിലേതല്ലേ. ഫാമിലെ സാധനത്തിന് എന്ത് ലൈസൻസ്?"),
 ("V","wide","അച്ചാറാക്കി കുപ്പിയിലാക്കിയാൽ അത് പാക്ക് ചെയ്ത ഭക്ഷണം. 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷനും ലേബലിൽ 14 അക്ക നമ്പറും വേണം."),
 ("A","wide","അപ്പോ അടുത്ത ഞായറിന് മുമ്പ് രജിസ്ട്രേഷൻ."),
 ("V","V","കൂൺ മണ്ണിൽ, അച്ചാർ നിയമത്തിൽ.")],
 "കുപ്പിയിലാക്കിയാൽ\nFSSAI വേണം", CTA_FOOD, theme="crm",
 cap_ml="സ്വന്തം ഫാമിലെ കൂൺ അച്ചാറാക്കി കുപ്പിയിൽ വിൽക്കുമ്പോൾ അത് പാക്ക് ചെയ്ത ഭക്ഷണമാണ്. 12 ലക്ഷം വരെ ബേസിക് FSSAI രജിസ്ട്രേഷനും ലേബലിൽ 14 അക്ക നമ്പറും വേണം. നിങ്ങളുടെ ഫാമിൽ നിന്ന് എന്ത് ഉൽപ്പന്നം?",
 cap_en="Turning your own farm's mushrooms into bottled pickle makes it packaged food: you need FSSAI basic registration (up to 12 lakh a year) and the 14-digit number on the label. What does your farm make?",
 cap_mg="Swantham farm-ile koon achaar aakki kuppiyil vilkkumpol athu pack cheytha food aanu. 12 lakh vare basic FSSAI registration-um label-il 14 akka number-um venam. Ningalude farm-il ninnu enthu product?")

# CRM #20 (investor asks for a data room), cloud kitchen with an expired licence
duo("fs015", "cloud_kitchen", "A", "office", "ഇൻവെസ്റ്റർ ഡാറ്റാ റൂം.\nലൈസൻസ് കോപ്പി ഇട്ടു.\nതീർന്നിട്ട് 2 മാസം", [
 ("A","wide","രാഹുൽ, ഇൻവെസ്റ്റർ ഡാറ്റാ റൂമിൽ FSSAI ലൈസൻസ് കോപ്പി ചോദിച്ചു. ഇടാൻ നോക്കിയപ്പോഴാ കണ്ടത്."),
 ("V","V","നേഹാ, അത് ഫോൾഡറിൽ ഉണ്ടല്ലോ. എന്താ പ്രശ്നം?"),
 ("A","A","കാലാവധി രണ്ട് മാസം മുമ്പ് തീർന്നു. ആരും ശ്രദ്ധിച്ചില്ല."),
 ("V","wide","ഒരിക്കൽ എടുത്താൽ പോരേ?"),
 ("A","wide","ഇല്ല. ഒന്ന് മുതൽ അഞ്ച് വർഷം വരെയാണ് കാലാവധി. തീരും മുമ്പ് പുതുക്കണം."),
 ("V","V","പണം ചോദിക്കും മുമ്പ് തീയതി നോക്കണം.")],
 "കാലാവധി 1-5 വർഷം\nതീരും മുമ്പ് പുതുക്കൂ", CTA_FSSAI, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റാ റൂമിനായി FSSAI ലൈസൻസ് എടുത്തപ്പോൾ അത് രണ്ട് മാസം മുമ്പ് തീർന്നിരുന്നു. ലൈസൻസ് 1 മുതൽ 5 വർഷം വരെ; കാലാവധി തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടെ ലൈസൻസ് എന്ന് തീരും?",
 cap_en="A cloud kitchen opened its investor data room and found its FSSAI licence had expired two months earlier. Licences are valid for 1 to 5 years and must be renewed before expiry. When does yours expire?",
 cap_mg="Investor data room-inu FSSAI licence eduthappol athu randu maasam mumpu theernnirunnu. Licence 1 muthal 5 varsham vare; theerum mumpu puthukkanam. Ningalude licence ennu theerum?")

# FAQ: "only on Instagram, so no FSSAI"
duo("fs016", "home_baker", "B", "balcony", "\"ഡെലിവറി ആപ്പ് ഇല്ല,\nഇൻസ്റ്റഗ്രാം മാത്രം.\nFSSAI വേണ്ടല്ലോ?\"", [
 ("A","wide","വിവേക്, ഈ ആഴ്ച 80 ബ്രൗണി ബോക്സ്. എല്ലാം ഇൻസ്റ്റഗ്രാം മെസേജ് വഴി!"),
 ("V","V","അമ്മൂ, FSSAI രജിസ്ട്രേഷൻ എടുത്തോ?"),
 ("A","A","ഡെലിവറി ആപ്പിൽ ഇല്ലല്ലോ. ആപ്പുകാരല്ലേ നമ്പർ ചോദിക്കുന്നത്?"),
 ("V","wide","ആപ്പ് ചോദിക്കുന്നതുകൊണ്ടല്ല നിയമം. വീട്ടിലെ ബേക്കർമാർക്കും വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ വേണം."),
 ("A","wide","ശരി. അടുത്ത ബാച്ചിന് മുമ്പ് അപേക്ഷിക്കാം."),
 ("V","V","ഫോളോവേഴ്സ് ഉണ്ടായാൽ പോരാ, നമ്പറും വേണം.")],
 "വീട്ടിലെ ബേക്കർക്കും\nFSSAI", CTA_FOOD, theme="faq",
 cap_ml="ഇൻസ്റ്റഗ്രാം വഴി മാത്രം ബ്രൗണി വിൽക്കുന്നവർക്കും FSSAI വേണം; ഡെലിവറി ആപ്പ് ഇല്ലെങ്കിലും. വീട്ടിലെ ബേക്കർമാർക്ക് വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ. നിങ്ങൾ എവിടെയാണ് വിൽക്കുന്നത്?",
 cap_en="Selling brownies only through Instagram messages still needs FSSAI, even with no delivery app. Home bakers need basic registration for turnover up to 12 lakh a year. Where do you sell?",
 cap_mg="Instagram vazhi maathram brownie vilkkunnavarkkum FSSAI venam; delivery app illenkilum. Veettile baker-maarkku varsham 12 lakh vare basic registration. Ningal evideyaanu vilkkunnathu?")

# FAQ: small importer assumes basic is enough
duo("fs017", "spice_exporter", "C", "mall", "ഇറക്കുമതി ചോക്ലേറ്റ് കിയോസ്ക്.\nവിൽപ്പന 8 ലക്ഷം.\n\"ബേസിക് മതി\"?", [
 ("A","wide","ജാഫർ, മാളിലെ ആ ചോക്ലേറ്റ് കിയോസ്കിലേക്ക് നീ തന്നെയാണോ ഇറക്കുമതി ചെയ്യുന്നത്?"),
 ("V","V","അതേ സുമയ്യാ. വർഷം 8 ലക്ഷമേ വിൽപ്പന വരൂ. ബേസിക് രജിസ്ട്രേഷൻ മതിയല്ലോ."),
 ("A","A","ടേൺഓവർ മാത്രമല്ല നോക്കേണ്ടത്. നീ ഇറക്കുമതിക്കാരനാണ്."),
 ("V","wide","അതിനെന്താ?"),
 ("A","wide","ഭക്ഷണം ഇറക്കുമതി ചെയ്യുന്നവർക്ക് സെൻട്രൽ ലൈസൻസ് വേണം, വിൽപ്പന ചെറുതായാലും."),
 ("V","V","ചോക്ലേറ്റ് ചെറുത്, ലൈസൻസ് സെൻട്രൽ.")],
 "ഇറക്കുമതിക്കാർക്ക്\nസെൻട്രൽ ലൈസൻസ്", CTA_FSSAI, theme="faq",
 cap_ml="വർഷം 8 ലക്ഷം മാത്രം വിൽപ്പനയുള്ള ചോക്ലേറ്റ് കിയോസ്ക് ആണെങ്കിലും സ്വന്തമായി ഇറക്കുമതി ചെയ്യുന്നുണ്ടെങ്കിൽ FSSAI സെൻട്രൽ ലൈസൻസ് വേണം. ബേസിക് രജിസ്ട്രേഷൻ മതിയാകില്ല. ഇത് നിങ്ങൾക്ക് അറിയാമായിരുന്നോ?",
 cap_en="Even a chocolate kiosk with just 8 lakh a year in sales needs an FSSAI central licence if it imports the food itself. Basic registration is not enough for importers. Did you know this?",
 cap_mg="Varsham 8 lakh maathram vilppana ulla chocolate kiosk aanenkilum swanthamaayi import cheyyunnundenkil FSSAI central licence venam. Basic registration mathiyaakilla. Ithu ningalkku ariyaamaayirunno?")

# d904 pattern: railway platform snack packets
duo("fs018", "home_baker", "B", "railway", "\"ട്രെയിനിൽ ആര്\nലേബൽ വായിക്കാനാ?\"\nദിവസം 100 പാക്കറ്റ്", [
 ("A","wide","ദിനേശേട്ടാ, പ്ലാറ്റ്ഫോമിലെ സ്റ്റാളിൽ നമ്മുടെ ഇലയട പാക്കറ്റ് ദിവസം 100 എണ്ണം പോകുന്നുണ്ട്."),
 ("V","V","ഷീബേ, നല്ലത്. പാക്കറ്റിൽ FSSAI നമ്പർ ഉണ്ടോ?"),
 ("A","A","ട്രെയിൻ പിടിക്കാൻ ഓടുന്നവർ ലേബൽ വായിക്കുമോ? ആരും നോക്കില്ല."),
 ("V","wide","യാത്രക്കാരൻ നോക്കിയില്ലെങ്കിലും നിയമം നോക്കും. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ വേണം. ഇല്ലെങ്കിൽ 5 ലക്ഷം വരെ പിഴ."),
 ("A","wide","അപ്പോ ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ പുതിയ ലേബൽ."),
 ("V","V","ട്രെയിൻ ഓടും, പിഴ കാത്തുനിൽക്കും.")],
 "ആരും വായിച്ചില്ലെങ്കിലും\nനമ്പർ വേണം", CTA_FOOD, theme="faq",
 cap_ml="റെയിൽവേ സ്റ്റാളിൽ ദിവസം 100 ഇലയട പാക്കറ്റ് വിൽക്കുന്നു, ലേബലിൽ FSSAI നമ്പർ ഇല്ല. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ നിർബന്ധം; ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങൾ ലേബൽ വായിക്കാറുണ്ടോ?",
 cap_en="A home cook sells 100 packets of ela ada a day at a railway stall, with no FSSAI number on the label. Packaged food must carry the 14-digit number; selling without registration can mean a penalty of up to 5 lakh. Do you read food labels?",
 cap_mg="Railway stall-il divasam 100 elayada packet vilkkunnu, label-il FSSAI number illa. Pack cheytha food-il 14 akka number nirbandham; illaathe vittaal 5 lakh vare pizha. Ningal label vaayikkaarundo?")

# FAQ: "first time it's only a warning"
chat("fs019", "cloud_kitchen", "C", "\"ആദ്യം പിടിച്ചാൽ\nവാണിംഗ് മാത്രം\"\nശരിക്കും?", ("ഹന്ന", "ഫഹദ്"), [
 (1,"ഹന്നാ, ക്ലൗഡ് കിച്ചൺ തുടങ്ങി 3 മാസമായി. FSSAI ഇപ്പോഴും ആയിട്ടില്ല."),
 (0,"ഫഹദേ, ഇതുവരെ അപേക്ഷിച്ചില്ലേ?"),
 (1,"ആദ്യം പിടിച്ചാൽ വാണിംഗ് മാത്രം എന്നാ എല്ലാരും പറയുന്നേ."),
 (0,"എല്ലാരും പറയുന്നത് നിയമമല്ല. ലൈസൻസ് ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 (1,"ശരി. ഇന്ന് തന്നെ അപേക്ഷിക്കാം."),
 (0,"വാണിംഗ് കേട്ടുകേൾവി, പിഴ നിയമം.")],
 "കേട്ടുകേൾവി വിട്ട്\nരജിസ്ട്രേഷൻ എടുക്കൂ", CTA_FSSAI, theme="faq",
 cap_ml="\"ആദ്യം പിടിച്ചാൽ വാണിംഗ് മാത്രം\" എന്ന് കരുതി FSSAI ഇല്ലാതെ ക്ലൗഡ് കിച്ചൺ നടത്തരുത്. ലൈസൻസ് ഇല്ലാതെ ഭക്ഷണം വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. ഈ കേട്ടുകേൾവി നിങ്ങൾ കേട്ടിട്ടുണ്ടോ?",
 cap_en="Don't run a cloud kitchen without FSSAI on the belief that the first time is only a warning. Selling food without a licence can mean a penalty of up to 5 lakh and up to 6 months in prison. Have you heard this myth?",
 cap_mg="\"Aadyam pidichaal warning maathram\" ennu karuthi FSSAI illaathe cloud kitchen nadatharuthu. Licence illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Ee kettukelvi ningal kettittundo?")
