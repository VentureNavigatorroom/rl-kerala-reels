# FSSAI batch 06 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD


# faq / d904: seasonal summer drink stall
duo("fs029", "packaged_food", "B", "busstop", "\"വേനലിൽ 3 മാസം\nസംഭാരം മാത്രം.\nലൈസൻസ് എന്തിന്?\"", [
 ("A","wide","അഖിലേ, ഈ വേനലിൽ ബസ് സ്റ്റാൻഡുകളിൽ കുപ്പി സംഭാരം. ദിവസം 400 കുപ്പി പോകുന്നു."),
 ("V","V","ജിബിനേ, FSSAI എടുത്തോ? കുപ്പിയിൽ നമ്പറും കണ്ടില്ല."),
 ("A","A","മൂന്ന് മാസത്തെ പരിപാടിയല്ലേ. മഴ വന്നാൽ നിർത്തും."),
 ("V","wide","സീസൺ നോക്കിയല്ല നിയമം. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ, 6 മാസം വരെ തടവും ആകാം."),
 ("A","A","അപ്പോ മോര് തണുപ്പിക്കും മുമ്പ് രജിസ്ട്രേഷൻ."),
 ("V","wide","വേനൽ മൂന്ന് മാസം, പിഴ കൊല്ലം മുഴുവൻ.")],
 "വേനൽ മൂന്ന് മാസം,\nപിഴ കൊല്ലം മുഴുവൻ", CTA_FSSAI, theme="faq",
 cap_ml="വേനലിൽ മൂന്ന് മാസം മാത്രം ബസ് സ്റ്റാൻഡുകളിൽ കുപ്പി സംഭാരം വിൽക്കുന്നവർക്കും FSSAI വേണം. ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും ആകാം. നിങ്ങളുടെ ബിസിനസ് സീസണലോ?",
 cap_en="Selling bottled spiced buttermilk at bus stands for just three summer months still needs FSSAI. Selling food without it can mean a penalty up to 5 lakh and up to 6 months in prison. Is your food business seasonal?",
 cap_mg="Venalil moonnu maasam maathram bus standukalil kuppi sambharam vilkkunnavarkkum FSSAI venam. License illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum aakaam. Ningalude business seasonal-o?")

# new / d904: homestay "free" breakfast
duo("fs030", "cafe_owner", "B", "homestay", "\"ബ്രേക്ക്ഫാസ്റ്റ് ഫ്രീ\nആണ്. ഫുഡ് ബിസിനസ്\nഅല്ലല്ലോ\"", [
 ("A","wide","ജോമോനേ, ഗസ്റ്റുകൾക്ക് പുട്ടും കടലയും കൊടുക്കുന്നതിന് FSSAI വേണോ? റൂം വാടകയിൽ ഫ്രീ ആണല്ലോ."),
 ("V","V","ടീനേ, ഫ്രീ എന്ന് ബോർഡിൽ മാത്രം. പൈസ റൂമിന്റെ ബില്ലിൽ കയറിയിട്ടുണ്ട്."),
 ("A","A","ഡിന്നറിന് കരിമീനും ഇപ്പോ ഓർഡർ എടുക്കുന്നുണ്ട്."),
 ("V","wide","എങ്കിൽ ഇത് ഫുഡ് ബിസിനസ് തന്നെ. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി."),
 ("A","A","അപ്പോ റിവ്യൂവിൽ മാത്രമല്ല, പേപ്പറിലും അടുക്കള വേണം."),
 ("V","wide","ബില്ലിൽ ഒളിച്ച പുട്ടും പുട്ട് തന്നെ.")],
 "ബില്ലിൽ ഒളിച്ച പുട്ടും\nപുട്ട് തന്നെ", CTA_FOOD, theme="new",
 cap_ml="റൂം വാടകയ്ക്കൊപ്പം 'ഫ്രീ' ബ്രേക്ക്ഫാസ്റ്റും ഓർഡറിൽ ഡിന്നറും കൊടുക്കുന്ന ഹോംസ്റ്റേ ഒരു ഫുഡ് ബിസിനസ് ആണ്. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് FSSAI ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങളുടെ ഹോംസ്റ്റേയിൽ ഫുഡ് ഉണ്ടോ?",
 cap_en="A homestay that serves 'free' breakfast with the room and cooks dinner to order is running a food business. FSSAI basic registration covers turnover up to 12 lakh a year. Does your homestay serve food?",
 cap_mg="Room vaadakaykkoppam 'free' breakfast-um order-il dinner-um kodukkunna homestay oru food business aanu. Varsham 12 lakh vare turnover-inu FSSAI basic registration mathi. Ningalude homestay-il food undo?")

# crm (investor asks about licences): tea kiosks crossing the basic limit
duo("fs031", "cafe_owner", "A", "metro", "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"4 കിയോസ്കിനും\nഒരേ ബേസിക്കോ?\"", [
 ("A","wide","കിരണേ, മെട്രോയിലെ 4 സുലൈമാനി കിയോസ്കും കൂടി ഈ വർഷം 30 ലക്ഷം കടക്കും. ഇൻവെസ്റ്റർ ലൈസൻസ് ചോദിച്ചു."),
 ("V","V","അഞ്ജലീ, ആദ്യ കിയോസ്കിന് എടുത്ത ബേസിക് രജിസ്ട്രേഷൻ ആണ് ഇപ്പോഴും ഫയലിൽ."),
 ("A","A","ചായ ചെറുതല്ലേ, ലൈസൻസും ചെറുത് മതിയെന്നാ കരുതിയത്."),
 ("V","wide","ബേസിക് വർഷം 12 ലക്ഷം വരെ മാത്രം. 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ് വേണം."),
 ("A","A","കപ്പ് ചെറുതായാലും കണക്ക് വലുതാ."),
 ("V","wide","ഗ്ലാസ് ചെറുത്, ടേൺഓവർ വലുത്.")],
 "ഗ്ലാസ് ചെറുത്,\nടേൺഓവർ വലുത്", CTA_FSSAI, theme="crm",
 cap_ml="നാല് മെട്രോ സുലൈമാനി കിയോസ്കുകൾ ചേർന്ന് വർഷം 30 ലക്ഷം; ഇൻവെസ്റ്റർ ചോദിച്ചപ്പോഴാണ് ബേസിക് രജിസ്ട്രേഷൻ പോരെന്ന് മനസ്സിലായത്. ബേസിക് 12 ലക്ഷം വരെ, സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി വരെ. നിങ്ങൾക്ക് എത്ര ഔട്ട്‌ലെറ്റ്?",
 cap_en="Four sulaimani tea kiosks at metro stations add up to 30 lakh a year, and an investor's question shows the basic registration is no longer enough. Basic covers up to 12 lakh a year; a state licence covers up to 20 crore. How many outlets do you run?",
 cap_mg="Naalu metro sulaimani kiosk-ukal chernnu varsham 30 lakh; investor chodichappozhaanu basic registration poreennu manassilaayathu. Basic 12 lakh vare, state license 20 crore vare. Ningalkku ethra outlet?")

# faq / d904: small coffee roaster importing beans
duo("fs032", "spice_exporter", "C", "garage", "ഗാരേജിൽ കോഫി\nറോസ്റ്റിംഗ്. \"ചെറിയ\nബിസിനസ്, ബേസിക് മതി\"", [
 ("A","wide","ജിതിനേ, ഗാരേജിലെ റോസ്റ്റർ റെഡി. ആദ്യ ലോട്ട് ബീൻസ് വിയറ്റ്നാമിൽ നിന്ന് ഇറക്കുന്നു."),
 ("V","V","ഐശ്വര്യേ, വിൽപ്പന വർഷം 6 ലക്ഷം. ബേസിക് രജിസ്ട്രേഷൻ എടുക്കാം അല്ലേ?"),
 ("A","A","ഞാനും അതാ കരുതിയത്. പിന്നെ എന്താ പ്രശ്നം?"),
 ("V","wide","ഫുഡ് ഇറക്കുമതി ചെയ്താൽ ടേൺഓവർ ചെറുതായാലും സെൻട്രൽ ലൈസൻസ് വേണം."),
 ("A","A","അപ്പോ ബീൻസ് കപ്പലിൽ കയറും മുമ്പ് ലൈസൻസ് റെഡിയാക്കണം."),
 ("V","wide","ബീൻസ് ഇറക്കിയാൽ ലൈസൻസ് സെൻട്രൽ.")],
 "ബീൻസ് ഇറക്കിയാൽ\nലൈസൻസ് സെൻട്രൽ", CTA_FSSAI, theme="faq",
 cap_ml="ഗാരേജിൽ കോഫി റോസ്റ്റ് ചെയ്യുന്ന ചെറിയ ബ്രാൻഡ്, വിൽപ്പന 6 ലക്ഷം മാത്രം. പക്ഷേ ബീൻസ് സ്വയം ഇറക്കുമതി ചെയ്യുന്നതിനാൽ FSSAI സെൻട്രൽ ലൈസൻസ് വേണം; ഇറക്കുമതിക്കാർക്ക് ടേൺഓവർ നോക്കാതെ സെൻട്രൽ. നിങ്ങൾ എന്തെങ്കിലും ഇറക്കുമതി ചെയ്യുന്നുണ്ടോ?",
 cap_en="A small garage coffee roaster with just 6 lakh in sales assumes basic registration will do. Because it imports its own green beans, it needs an FSSAI central licence: food importers need central whatever their turnover. Do you import any ingredient yourself?",
 cap_mg="Garage-il coffee roast cheyyunna cheriya brand, vilppana 6 lakh maathram. Pakshe beans swayam import cheyyunnathinaal FSSAI central license venam; importers-nu turnover nokkaathe central. Ningal enthenkilum import cheyyunnundo?")

# crm (family business in a relative's name): grandfather's old halwa shop certificate
duo("fs033", "packaged_food", "B", "gulfroom", "\"ഉപ്പൂപ്പയുടെ ഹൽവ\nകടയ്ക്ക് ലൈസൻസ്\nപണ്ടേ ഉണ്ട്\"", [
 ("A","wide","ഷംസൂ, ലീവിന് പോയി ഉപ്പൂപ്പയുടെ ഹൽവ കട ഞാൻ ഏറ്റെടുക്കുന്നു. ഓൺലൈനിലും വിൽക്കണം."),
 ("V","V","നസീറേ, FSSAI ഉണ്ടോ? ഓൺലൈൻ ആപ്പ് ആദ്യം അതാ ചോദിക്കുക."),
 ("A","A","ഉണ്ടല്ലോ. ചുമരിൽ ഫ്രെയിം ചെയ്ത് തൂക്കിയിട്ടുണ്ട്, വർഷങ്ങളായി."),
 ("V","wide","അതാ പ്രശ്നം. FSSAI 1 മുതൽ 5 വർഷം വരെ മാത്രം. തീരും മുമ്പ് പുതുക്കണം. ഫ്രെയിമിലെ തീയതി നോക്ക്."),
 ("A","A","ഹൽവയ്ക്ക് പഴക്കം നല്ലതാ. ലൈസൻസിന് അല്ല."),
 ("V","wide","ചുമരിലെ ഫ്രെയിം ലൈസൻസല്ല, ഓർമ്മയാ.")],
 "ചുമരിലെ ഫ്രെയിം\nലൈസൻസല്ല, ഓർമ്മയാ", CTA_FOOD, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് വന്ന് ഉപ്പൂപ്പയുടെ പഴയ ഹൽവ കട ഏറ്റെടുക്കുമ്പോൾ ചുമരിലെ ഫ്രെയിം ചെയ്ത FSSAI സർട്ടിഫിക്കറ്റ് വർഷങ്ങൾക്ക് മുമ്പേ തീർന്നിരിക്കാം. FSSAI 1 മുതൽ 5 വർഷം വരെയാണ്; തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടെ കടയിലെ സർട്ടിഫിക്കറ്റിൽ തീയതി നോക്കിയോ?",
 cap_en="Taking over a grandfather's old halwa shop, the framed FSSAI certificate on the wall may have expired years ago. FSSAI registration and licences are valid for 1 to 5 years and must be renewed before expiry. Have you checked the date on yours?",
 cap_mg="Gulf-il ninnu vannu uppooppayude pazhaya halwa kada etteduthappol chumaril frame cheytha FSSAI certificate varshangalkku mumpe theernnirikkaam. FSSAI 1 muthal 5 varsham vare; theerum mumpu puthukkanam. Ningalude kadayile certificate-il theeyathi nokkiyo?")

# crm (food delivery concept "starting soon", no licence planned): Ramadan snack boxes
duo("fs034", "cloud_kitchen", "A", "home", "നോമ്പുതുറ ബോക്സ്.\n30 ദിവസം മാത്രം.\n\"ലൈസൻസ് അടുത്ത വർഷം\"", [
 ("A","wide","അരുണേ, കമ്പനി ടീമുകൾക്ക് നോമ്പുതുറ സ്നാക്ക് ബോക്സ്. 30 ദിവസത്തെ ഓർഡർ ഇപ്പോഴേ 4 ലക്ഷം."),
 ("V","V","സ്നേഹേ, FSSAI നമ്പർ ഇല്ലാതെ ഇത്രയും ഓർഡർ എങ്ങനെ എടുത്തു?"),
 ("A","A","വാട്സാപ്പിൽ. ഒരു മാസത്തേക്ക് ആര് ചോദിക്കാൻ? ബാക്കി അടുത്ത വർഷം നോക്കാം."),
 ("V","wide","4 ലക്ഷം ബേസിക് രജിസ്ട്രേഷനിൽ ഒതുങ്ങും, 12 ലക്ഷം വരെ. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ."),
 ("A","A","അപ്പോ പിഴ ഓർഡറിനേക്കാൾ വലുതാകും."),
 ("V","wide","ബോക്സ് നിറയ്ക്കും മുമ്പ് ഫയൽ നിറയ്ക്ക്.")],
 "ബോക്സ് നിറയ്ക്കും മുമ്പ്\nഫയൽ നിറയ്ക്ക്", CTA_FSSAI, theme="crm",
 cap_ml="30 ദിവസത്തേക്ക് മാത്രം നോമ്പുതുറ സ്നാക്ക് ബോക്സ്, 4 ലക്ഷത്തിന്റെ ഓർഡർ, പക്ഷേ FSSAI ഇല്ല. 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി; ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങളുടെ ഓർഡറുകൾ എവിടെ വരുന്നു?",
 cap_en="Ramadan snack boxes for office groups, only for 30 days, already 4 lakh in orders, and no FSSAI yet. Basic registration covers up to 12 lakh a year; selling without it can mean a penalty up to 5 lakh. Where do your orders come from?",
 cap_mg="30 divasathekku maathram nombuthura snack box, 4 lakhinte order, pakshe FSSAI illa. 12 lakh vare basic registration mathi; illaathe vittaal 5 lakh vare pizha. Ningalude orders evide varunnu?")

# faq: "a women's group unit needs no FSSAI"
duo("fs035", "packaged_food", "C", "akshaya", "\"വനിതാ ഗ്രൂപ്പിന്റെ\nഅച്ചാറാ. FSSAI\nവേണ്ടല്ലോ\"", [
 ("A","wide","രമേശേ, ഞങ്ങൾ പത്ത് സ്ത്രീകളുടെ ഗ്രൂപ്പ് ചെമ്മീൻ അച്ചാർ കുപ്പിയിലാക്കുന്നു. ഗ്രൂപ്പിന് FSSAI വേണ്ടല്ലോ?"),
 ("V","V","സുധേ, ആരാണ് ഉണ്ടാക്കുന്നത് എന്നല്ല, എന്താണ് വിൽക്കുന്നത് എന്നാ നോട്ടം."),
 ("A","A","കുപ്പിയിൽ ഗ്രൂപ്പിന്റെ പേര് വലുതായി അടിച്ചിട്ടുണ്ട്."),
 ("V","wide","പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ വേണം. ഗ്രൂപ്പായാലും ബേസിക് രജിസ്ട്രേഷൻ എടുക്കണം."),
 ("A","A","പേര് വലുതാക്കിയത് പോരാ, നമ്പറും വേണം."),
 ("V","wide","പത്ത് കൈ, ഒരു നമ്പർ.")],
 "പത്ത് കൈ,\nഒരു നമ്പർ", CTA_FOOD, theme="faq",
 cap_ml="പത്ത് സ്ത്രീകളുടെ ഗ്രൂപ്പ് ഉണ്ടാക്കുന്ന ചെമ്മീൻ അച്ചാറിനും FSSAI വേണം. പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ നിർബന്ധം; വിൽപ്പന 12 ലക്ഷം വരെയെങ്കിൽ ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങളുടെ ഗ്രൂപ്പ് എന്ത് ഉണ്ടാക്കുന്നു?",
 cap_en="A women's self-help group bottling prawn pickle still needs FSSAI: who makes it doesn't matter, what is sold does. Packaged food must carry the 14-digit FSSAI number, and basic registration covers sales up to 12 lakh a year. What does your group make?",
 cap_mg="Pathu sthreekalude group undaakkunna chemmeen achaarinum FSSAI venam. Pack cheytha food-il 14 akka FSSAI number nirbandham; vilppana 12 lakh vare-enkil basic registration mathi. Ningalude group enthu undaakkunnu?")

# crm (bank / investor diligence): seafood processor crossing 20 crore
duo("fs036", "spice_exporter", "A", "bank", "പുതിയ കോൺട്രാക്ട്.\nടേൺഓവർ 23 കോടി.\nബാങ്ക് ലൈസൻസ് നോക്കി", [
 ("A","wide","മനോജേ, ഫ്രോസൺ ചെമ്മീൻ യൂണിറ്റിന് പുതിയ സൂപ്പർമാർക്കറ്റ് കോൺട്രാക്ട് കിട്ടി. ഈ വർഷം 23 കോടി കടക്കും."),
 ("V","V","ശ്രുതീ, ലോൺ ഫയലിൽ FSSAI സ്റ്റേറ്റ് ലൈസൻസ് ആണല്ലോ കാണുന്നത്."),
 ("A","A","കഴിഞ്ഞ വർഷം 18 കോടി ആയിരുന്നു. അത് മതിയായിരുന്നു."),
 ("V","wide","സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി വരെ. അതിന് മുകളിൽ സെൻട്രൽ ലൈസൻസ് വേണം."),
 ("A","A","കോൺട്രാക്ട് സൈൻ ചെയ്യും മുമ്പ് ലൈസൻസ് മാറ്റണം."),
 ("V","wide","ബിസിനസ് വളർന്നാൽ ലൈസൻസും വളരണം.")],
 "ബിസിനസ് വളർന്നാൽ\nലൈസൻസും വളരണം", CTA_FSSAI, theme="crm",
 cap_ml="ഫ്രോസൺ ചെമ്മീൻ യൂണിറ്റ് പുതിയ കോൺട്രാക്ടിൽ 18 കോടിയിൽ നിന്ന് 23 കോടിയിലേക്ക്. FSSAI സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി വരെ മാത്രം; അതിന് മുകളിൽ സെൻട്രൽ ലൈസൻസ് വേണം. നിങ്ങളുടെ ലൈസൻസ് ടേൺഓവറിനൊപ്പം വളർന്നോ?",
 cap_en="A frozen-prawn unit's new supermarket contract takes sales from 18 crore to 23 crore, and the bank notices the licence on file is a state licence. The state licence covers up to 20 crore; above that you need a central licence. Has your licence grown with your turnover?",
 cap_mg="Frozen chemmeen unit puthiya contract-il 18 crore-il ninnu 23 crore-ilekku. FSSAI state license 20 crore vare maathram; athinu mukalil central license venam. Ningalude license turnover-inoppam valarnno?")

# new / d904: cooking YouTuber selling masala packets through a link
duo("fs037", "packaged_food", "C", "mobileshop", "2 ലക്ഷം സബ്സ്ക്രൈബേഴ്സ്.\n\"ഞാൻ യൂട്യൂബറാ,\nഫുഡ് ബിസിനസ് അല്ല\"", [
 ("A","wide","ഫഹദേ, ചാനലിലെ ഫിഷ് മസാല ഇനി പാക്കറ്റിൽ. ഡിസ്ക്രിപ്ഷനിൽ ലിങ്ക് ഇട്ടാൽ മതി."),
 ("V","V","ഹന്നാ, പാക്കറ്റിൽ FSSAI നമ്പർ എവിടെ?"),
 ("A","A","ഞാൻ യൂട്യൂബർ അല്ലേ, കമ്പനി അല്ലല്ലോ. റെസിപ്പി എന്റേതാ."),
 ("V","wide","പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ വേണം. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ."),
 ("A","A","അപ്പോ ലിങ്കിന് മുമ്പ് ലൈസൻസ്."),
 ("V","wide","ലൈക്ക് ചാനലിന്, നമ്പർ പാക്കറ്റിന്.")],
 "ലൈക്ക് ചാനലിന്,\nനമ്പർ പാക്കറ്റിന്", CTA_FOOD, theme="new",
 cap_ml="കുക്കിംഗ് യൂട്യൂബർ സ്വന്തം ഫിഷ് മസാല പാക്കറ്റിലാക്കി ഡിസ്ക്രിപ്ഷൻ ലിങ്കിൽ വിൽക്കുന്നു, പക്ഷേ FSSAI ഇല്ല. പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ വേണം; ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങൾ ഓൺലൈനിൽ ഫുഡ് വിൽക്കുന്നുണ്ടോ?",
 cap_en="A cooking YouTuber puts her fish masala in packets and sells it through a description link, without FSSAI. Packaged food must carry the 14-digit FSSAI number, and selling food without it can mean a penalty up to 5 lakh. Do you sell food online?",
 cap_mg="Cooking YouTuber swantham fish masala packet-ilaakki description link-il vilkkunnu, pakshe FSSAI illa. Pack cheytha food-il 14 akka FSSAI number venam; illaathe vittaal 5 lakh vare pizha. Ningal online-il food vilkkunnundo?")

# faq: "the delivery app will give us the licence"
chat("fsc003", "cloud_kitchen", "B", "\"ആപ്പിൽ ചേർന്നാൽ\nലൈസൻസ് അവർ\nതരും\"", ("ഗ്രീഷ്മ", "അനൂപ്"), [
 (1,"ഗ്രീഷ്മേ, ജെട്ടിയിലെ കല്ലുമ്മക്കായ ഫ്രൈ ഇനി ഡെലിവറി ആപ്പിൽ. ലൈസൻസ് അവർ ശരിയാക്കി തരുമെന്ന് കേട്ടു."),
 (0,"അനൂപേ, ആപ്പ് ലൈസൻസ് തരില്ല. ആപ്പ് FSSAI നമ്പർ ചോദിക്കുകയാ ചെയ്യുക."),
 (1,"അപ്പോ നമ്പർ ഇല്ലെങ്കിൽ?"),
 (0,"ലിസ്റ്റിംഗ് അവിടെ നിൽക്കും. വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി. അത് നമ്മൾ എടുക്കണം."),
 (1,"ആപ്പ് വഴി കാണിക്കും, ലൈസൻസ് നമ്മൾ കൊണ്ടുവരണം."),
 (0,"ആപ്പ് റോഡ് തരും, ലൈസൻസ് നമ്മൾ.")],
 "ആപ്പ് റോഡ് തരും,\nലൈസൻസ് നമ്മൾ", CTA_FSSAI, theme="faq",
 cap_ml="ഡെലിവറി ആപ്പിൽ ചേർന്നാൽ അവർ FSSAI ലൈസൻസ് തരുമോ? ഇല്ല. ആപ്പുകൾ FSSAI നമ്പർ ചോദിക്കും; വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ സ്വന്തമായി എടുക്കണം. നിങ്ങൾ ഏത് ആപ്പിലാ?",
 cap_en="Will the delivery app get you your FSSAI licence? No. Delivery apps ask for your FSSAI number before you go live; basic registration for turnover up to 12 lakh a year is yours to get. Which app are you on?",
 cap_mg="Delivery app-il chernnaal avar FSSAI license tharumo? Illa. Apps FSSAI number chodikkum; varsham 12 lakh vare turnover-inu basic registration swanthamaayi edukkanam. Ningal ethu app-ilaa?")
