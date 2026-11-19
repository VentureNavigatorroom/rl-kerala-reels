# FSSAI batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

duo("fs002", "packaged_food", "A", "juiceshop", "ഇൻവെസ്റ്റർ: \"FSSAI-ക്ക്\nപുറമെ എന്തുണ്ട്?\"\nFSSAI-യും ശരിയല്ല", [
 ("A","wide","നൗഷാദേ, കുൽഫി ബ്രാൻഡിന് ഇൻവെസ്റ്റർ ചോദിച്ചു, FSSAI അല്ലാതെ വേറെ എന്ത് സർട്ടിഫിക്കേഷൻ ഉണ്ടെന്ന്."),
 ("V","V","റസിയാ, ആദ്യം FSSAI തന്നെ ശരിയാണോ എന്ന് നോക്ക്. ഇപ്പോ ഏതാ എടുത്തിരിക്കുന്നത്?"),
 ("A","A","ബേസിക് രജിസ്ട്രേഷൻ. തുടങ്ങിയപ്പോൾ എടുത്തതാ. ഇപ്പോ വിൽപ്പന 30 ലക്ഷം."),
 ("V","wide","ബേസിക് 12 ലക്ഷം വരെ മാത്രം. അതിന് മുകളിൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ് വേണം."),
 ("A","A","വലിയ ചോദ്യത്തിന് മുമ്പ് ചെറിയ ഉത്തരം ശരിയാക്കണം."),
 ("V","wide","കുൽഫി വളർന്നു, ലൈസൻസ് വളർന്നില്ല.")],
 "12 ലക്ഷം കടന്നാൽ\nസ്റ്റേറ്റ് ലൈസൻസ്", CTA_FSSAI, theme="crm",
 cap_ml="കുൽഫി ബ്രാൻഡിനോട് ഇൻവെസ്റ്റർ FSSAI-ക്ക് പുറമെയുള്ള സർട്ടിഫിക്കേഷൻ ചോദിച്ചു, പക്ഷേ FSSAI ലെവൽ തന്നെ പഴയതായിരുന്നു. ബേസിക് രജിസ്ട്രേഷൻ 12 ലക്ഷം വരെ, അതിന് മുകളിൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്. നിങ്ങളുടെ ലെവൽ ഏതാണ്?",
 cap_en="An investor asks a kulfi brand what certifications it has beyond FSSAI, but its FSSAI level is out of date. Basic registration covers turnover up to Rs 12 lakh a year; above that, a state licence (up to Rs 20 crore). Which FSSAI level is yours: basic, state or central?",
 cap_mg="Kulfi brand-inodu investor FSSAI-kku purame ulla certification chodichu, pakshe FSSAI level thanne pazhayathaayirunnu. Basic registration 12 lakh vare, athinu mukalil 20 crore vare state licence. Ningalude level ethaanu?")

duo("fs003", "packaged_food", "B", "pharmacy", "അമ്മയുടെ പേരിൽ\n8 വർഷം. സ്റ്റോർ ചോദിച്ചു:\n\"ലേബലിൽ നമ്പർ എവിടെ?\"", [
 ("A","wide","പ്രവീൺ, അമ്മയുടെ ചവനപ്രാശം ഇനി സൂപ്പർമാർക്കറ്റിൽ വെക്കാൻ പോകുവാ. പക്ഷേ അവർ ലേബൽ മടക്കി."),
 ("V","V","സിനീ, എന്താ കാരണം പറഞ്ഞത്?"),
 ("A","A","FSSAI നമ്പർ ലേബലിൽ ഇല്ല. 8 വർഷം വീട്ടുകാർക്ക് മാത്രം വിറ്റപ്പോൾ ആരും ചോദിച്ചില്ല."),
 ("V","wide","പാക്ക് ചെയ്ത ഫുഡ് ആണെങ്കിൽ 14 അക്ക FSSAI നമ്പർ ഓരോ പാക്കറ്റിലും വേണം."),
 ("A","A","അപ്പോ ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ പുതിയ ലേബൽ."),
 ("V","wide","അമ്മയുടെ കൈപ്പുണ്യം ഷെൽഫിൽ കയറാൻ 14 അക്കം വേണം.")],
 "ഷെൽഫിൽ കയറാൻ\n14 അക്കം", CTA_FOOD, theme="crm",
 cap_ml="വർഷങ്ങളായി വീട്ടുകാർക്ക് വിറ്റ ആയുർവേദ ഫുഡ് സപ്ലിമെന്റ് സ്റ്റോറിൽ എത്തിയപ്പോൾ ലേബൽ മടങ്ങി. പാക്ക് ചെയ്ത ഫുഡിന്റെ ഓരോ പാക്കറ്റിലും 14 അക്ക FSSAI നമ്പർ വേണം. നിങ്ങളുടെ ലേബലിൽ ഉണ്ടോ?",
 cap_en="A family Ayurvedic food supplement sold to relatives for 8 years gets its label rejected by a supermarket: no FSSAI number. Packaged food must carry the 14-digit FSSAI number on every pack. Is it on your label: yes or no?",
 cap_mg="Varshangalaayi veettukaarkku vitta Ayurvedic food supplement store-il ethiyappol label madangi. Pack cheytha food-nte oro packet-ilum 14 akka FSSAI number venam. Ningalude label-il undo?")

duo("fs004", "cafe_owner", "C", "petrolpump", "പമ്പിനരികെ\nഡ്രൈവ്-ത്രൂ ബിരിയാണി.\n\"ലൈസൻസ് പിന്നെ\"", [
 ("A","wide","ഷിബൂ, പമ്പിന്റെ സൈഡിൽ ഡ്രൈവ്-ത്രൂ ബിരിയാണി കൗണ്ടർ. അടുത്ത ആഴ്ച തുടങ്ങും."),
 ("V","V","സന്തോഷേ, FSSAI എടുത്തോ?"),
 ("A","A","ആദ്യം കച്ചവടം നടക്കുമോ എന്ന് നോക്കട്ടെ. പിന്നെ ലൈസൻസ്."),
 ("V","wide","ലൈസൻസ് ഇല്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ ജയിലും വരാം."),
 ("A","A","ബിരിയാണിക്ക് മുമ്പ് പേപ്പർ ദം ആക്കണം."),
 ("V","wide","കാർ നിർത്തും മുമ്പ് നമ്പർ വേണം.")],
 "ആദ്യം FSSAI,\nപിന്നെ ആദ്യ ബിരിയാണി", CTA_FSSAI, theme="crm",
 cap_ml="ഡ്രൈവ്-ത്രൂ ഫുഡ് കൗണ്ടർ \"തുടങ്ങിയിട്ട് ലൈസൻസ് എടുക്കാം\" എന്ന പ്ലാനിൽ ആണോ? FSSAI ഇല്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ ജയിലും. നിങ്ങൾ എപ്പോൾ തുടങ്ങുന്നു?",
 cap_en="Opening a drive-through biryani counter next week and planning to get the food licence later? Selling food without FSSAI can mean a penalty up to Rs 5 lakh and up to 6 months in prison. Get the number before the first plate. When do you launch?",
 cap_mg="Drive-through food counter 'thudangiyittu licence edukkaam' enna plan-il aano? FSSAI illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare jailum. Ningal eppol thudangunnu?")

duo("fs005", "home_baker", "A", "veranda", "അമ്മൂമ്മയുടെ അച്ചാറിന്\nഹോട്ടലിൽ നിന്ന്\nവലിയ ഓർഡർ", [
 ("A","wide","ബാലേട്ടാ, മൂന്ന് ഹോട്ടലുകാർ ഒരുമിച്ച് അച്ചാർ ചോദിച്ചു. ഈ വർഷം വിൽപ്പന 18 ലക്ഷം കടക്കും."),
 ("V","V","ശാന്തേ, നമ്മുടെ ബേസിക് രജിസ്ട്രേഷൻ മതിയാകുമോ?"),
 ("A","A","അത് തന്നെയാ സംശയം. വീട്ടിലെ കച്ചവടമല്ലേ."),
 ("V","wide","വീടാണോ കടയാണോ എന്നല്ല. ബേസിക് 12 ലക്ഷം വരെ. അതിന് മുകളിൽ സ്റ്റേറ്റ് ലൈസൻസ്."),
 ("A","A","അപ്പോ ഓർഡറിനൊപ്പം ലൈസൻസും അപ്ഗ്രേഡ്."),
 ("V","wide","അച്ചാർ പഴകും തോറും നല്ലത്. ലൈസൻസ് പഴകരുത്.")],
 "അച്ചാർ പഴകും തോറും\nനല്ലത്. ലൈസൻസ് പഴകരുത്", CTA_FSSAI, theme="crm",
 cap_ml="വീട്ടിലെ അച്ചാർ കച്ചവടത്തിന് വലിയ ഹോട്ടൽ ഓർഡർ വന്നു, വിൽപ്പന 12 ലക്ഷം കടക്കും. ബേസിക് FSSAI രജിസ്ട്രേഷൻ 12 ലക്ഷം വരെ മാത്രം, അതിന് മുകളിൽ സ്റ്റേറ്റ് ലൈസൻസ്. നിങ്ങളുടെ വിൽപ്പന ഈ വർഷം എത്ര?",
 cap_en="A grandmother's pickle business gets bulk orders from three hotels and will cross Rs 18 lakh this year. Basic FSSAI registration covers up to Rs 12 lakh; above that you need a state licence, home kitchen or not. Will your sales cross 12 lakh this year?",
 cap_mg="Veettile achaar kachavadathinu valiya hotel order vannu, vilpana 12 lakh kadakkum. Basic FSSAI registration 12 lakh vare maathram, athinu mukalil state licence. Ningalude vilpana ee varsham ethra?")

duo("fs006", "spice_exporter", "B", "airport", "ദുബായിൽ നിന്ന്\nഈന്തപ്പഴം ഇറക്കി\nവിൽക്കാൻ പ്ലാൻ", [
 ("A","wide","റഫീഖേ, ഗൾഫ് മതിയാക്കി. ഇനി ഈന്തപ്പഴം ഇറക്കുമതി ചെയ്ത് നാട്ടിൽ വിൽക്കും."),
 ("V","V","ഷമീറേ, നല്ല ഐഡിയ. ഫുഡ് ലൈസൻസ്?"),
 ("A","A","ചെറിയ കച്ചവടമല്ലേ, സ്റ്റേറ്റ് ലൈസൻസ് എടുക്കാം."),
 ("V","wide","ഇമ്പോർട്ട് ചെയ്യുന്നവർക്ക് ടേൺഓവർ എത്ര ആയാലും സെൻട്രൽ ലൈസൻസ് വേണം."),
 ("A","A","ചെറിയ കച്ചവടം, പക്ഷേ വലിയ ലൈസൻസ്."),
 ("V","wide","പഴം ചെറുത്, കടൽ കടന്നാൽ നിയമം വലുത്.")],
 "ഇമ്പോർട്ട് ചെയ്യുന്നവർക്ക്\nസെൻട്രൽ ലൈസൻസ്", CTA_FSSAI, theme="faq",
 cap_ml="ഗൾഫിൽ നിന്ന് ഈന്തപ്പഴമോ ചോക്ലേറ്റോ ഇറക്കി വിൽക്കാൻ പ്ലാനുണ്ടോ? ഫുഡ് ഇമ്പോർട്ട് ചെയ്യുന്നവർക്ക് സ്റ്റേറ്റ് ലൈസൻസ് പോരാ, സെൻട്രൽ FSSAI ലൈസൻസ് വേണം. നിങ്ങൾ എന്താണ് ഇറക്കുന്നത്?",
 cap_en="A Gulf returnee plans to import dates and sell them in Kerala, and assumes a state licence will do because the business is small. Food importers need a central FSSAI licence. Planning to import food: yes or no?",
 cap_mg="Gulf-il ninnu eenthappazhamo chocolate-o irakki vilkkaan plan undo? Food import cheyyunnavarkku state licence poraa, central FSSAI licence venam. Ningal enthaanu irakkunnathu?")

duo("fs007", "cafe_owner", "C", "teashop", "\"ചായക്കടയ്ക്ക് എന്ത്\nFSSAI? പാക്കറ്റ് ഫുഡ്\nഅല്ലല്ലോ\"", [
 ("A","wide","വിഷ്ണൂ, പുതിയ ചായക്കടയുടെ ബോർഡിൽ FSSAI നമ്പർ എവിടെ?"),
 ("V","V","അനൂ, ചായയും പഴംപൊരിയുമല്ലേ. പാക്കറ്റ് ഫുഡ് വിൽക്കുന്നവർക്കല്ലേ അത്?"),
 ("A","A","ഫുഡ് വിൽക്കുന്ന എല്ലാവർക്കും വേണം. ചെറിയ കടയാണെങ്കിൽ ബേസിക് രജിസ്ട്രേഷൻ, 12 ലക്ഷം വരെ."),
 ("V","wide","ഇല്ലെങ്കിൽ?"),
 ("A","A","5 ലക്ഷം വരെ പിഴ, 6 മാസം വരെ ജയിൽ."),
 ("V","wide","പഴംപൊരിയെക്കാൾ ചൂട് പിഴയ്ക്ക്.")],
 "ചായക്കടയ്ക്കും\nFSSAI", CTA_FOOD, theme="faq",
 cap_ml="ചായക്കടയ്ക്കും തട്ടുകടയ്ക്കും FSSAI വേണോ? വേണം. ചെറിയ കടകൾക്ക് 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ ജയിലും. നിങ്ങളുടെ കടയിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="Does a small tea shop need FSSAI if it doesn't sell packaged food? Yes: every food business needs it, and basic registration covers turnover up to Rs 12 lakh a year. Selling without it can mean a penalty up to Rs 5 lakh and up to 6 months in prison. Does your shop have its number?",
 cap_mg="Chaayakkadaykkum thattukadaykkum FSSAI veno? Venam. Cheriya kadakalkku 12 lakh vare basic registration. Illaathe vittaal 5 lakh vare pizhayum 6 maasam vare jailum. Ningalude kadayil number undo?")

duo("fs008", "cloud_kitchen", "A", "weddinghall", "\"കല്യാണ സീസണിൽ\nമാത്രമല്ലേ സദ്യ?\nലൈസൻസ് അപ്പോ നോക്കാം\"", [
 ("A","wide","ശരത്തേ, നിന്റെ സദ്യ കാറ്ററിംഗിന്റെ ലൈസൻസ് കഴിഞ്ഞ മാസം തീർന്നല്ലോ."),
 ("V","V","കാവ്യേ, ഇനി ചിങ്ങം വരെ കല്യാണം കുറവാ. സീസൺ വരുമ്പോൾ പുതുക്കാം."),
 ("A","A","തീർന്ന ലൈസൻസുമായി ഒരു സദ്യ പോലും വിളമ്പാൻ പറ്റില്ല."),
 ("V","wide","എത്ര വർഷത്തേക്ക് എടുക്കാം?"),
 ("A","A","1 മുതൽ 5 വർഷം വരെ. തീരുന്നതിന് മുമ്പ് പുതുക്കണം."),
 ("V","wide","സദ്യ തീരാം. ലൈസൻസ് തീരരുത്.")],
 "സദ്യ തീരാം,\nലൈസൻസ് തീരരുത്", CTA_FSSAI, theme="new",
 cap_ml="സീസണൽ കാറ്ററിംഗ് ആണെങ്കിലും FSSAI ലൈസൻസ് തീർന്നാൽ വിളമ്പാൻ പറ്റില്ല. ലൈസൻസ് 1 മുതൽ 5 വർഷം വരെ എടുക്കാം, തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടെ ലൈസൻസ് എന്ന് തീരും?",
 cap_en="A wedding sadya caterer lets his FSSAI licence lapse in the off-season. Registrations and licences are valid for 1 to 5 years and must be renewed before expiry, busy season or not. Do you know your expiry date: yes or no?",
 cap_mg="Seasonal catering aanenkilum FSSAI licence theernnaal vilampaan pattilla. Licence 1 muthal 5 varsham vare edukkaam, theerum mumbu puthukkanam. Ningalude licence ennu theerum?")

chat("fsc001", "home_baker", "B", "വിൽപ്പന 15 ലക്ഷം.\nബേസിക് മതിയോ,\nസ്റ്റേറ്റ് വേണോ?", ("ജിഷ", "സാബു"), [
 (1,"ജിഷേ, നമ്മുടെ ബേക്കറിക്ക് ഈ വർഷം 15 ലക്ഷം കടന്നു. FSSAI ബേസിക് തന്നെ മതിയല്ലോ?"),
 (0,"സാബുച്ചേട്ടാ, ബേസിക് 12 ലക്ഷം വരെ മാത്രം."),
 (1,"അതിന് മുകളിൽ സെൻട്രൽ ആണോ? അത് വലിയ കമ്പനികൾക്കല്ലേ?"),
 (0,"അല്ല. 12 ലക്ഷം മുതൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്. അതിന് മുകളിലും ഇമ്പോർട്ടിനും സെൻട്രൽ."),
 (1,"അപ്പോ നമ്മൾ സ്റ്റേറ്റ്."),
 (0,"കേക്ക് മൂന്ന് തട്ട്, ലൈസൻസും മൂന്ന് തട്ട്.")],
 "12 ലക്ഷം വരെ ബേസിക്,\n20 കോടി വരെ സ്റ്റേറ്റ്", CTA_FSSAI, theme="faq",
 cap_ml="ബേക്കറി വിൽപ്പന 15 ലക്ഷം ആയാൽ ഏത് FSSAI? ബേസിക് 12 ലക്ഷം വരെ, സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി വരെ, അതിന് മുകളിലും ഇമ്പോർട്ടിനും സെൻട്രൽ. നിങ്ങൾ ഏത് തട്ടിൽ?",
 cap_en="Bakery sales crossed Rs 15 lakh: which FSSAI do you need? Basic registration up to Rs 12 lakh, state licence up to Rs 20 crore, central licence above that and for importers. Which tier are you in: basic, state or central?",
 cap_mg="Bakery vilpana 15 lakh aayaal ethu FSSAI? Basic 12 lakh vare, state licence 20 crore vare, athinu mukalilum import-inum central. Ningal ethu thattil?")

lst("fsl002", "packaged_food", "C", "ഫുഡ് ബിസിനസിലെ\n3 FSSAI തെറ്റിദ്ധാരണ", [
 ("\"ചെറിയ കച്ചവടത്തിന് വേണ്ട\"", "തെറ്റ്. 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ വേണം."),
 ("\"നമ്പർ സർട്ടിഫിക്കറ്റിൽ മതി\"", "തെറ്റ്. പാക്കറ്റിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം."),
 ("\"ഒരിക്കൽ എടുത്താൽ മതി\"", "തെറ്റ്. 1-5 വർഷം. തീരും മുമ്പ് പുതുക്കണം.")],
 "ഏതാണ് നിങ്ങൾ\nവിശ്വസിച്ചിരുന്നത്?", CTA_FOOD, theme="faq",
 cap_ml="FSSAI-യെക്കുറിച്ചുള്ള 3 തെറ്റിദ്ധാരണ: ചെറിയ കച്ചവടത്തിന് വേണ്ട, നമ്പർ സർട്ടിഫിക്കറ്റിൽ മാത്രം മതി, ഒരിക്കൽ എടുത്താൽ മതി. മൂന്നും തെറ്റ്. ഏതാണ് നിങ്ങൾ വിശ്വസിച്ചിരുന്നത്: 1, 2, 3?",
 cap_en="Three FSSAI myths: small sellers don't need it (basic registration covers up to Rs 12 lakh), the number only goes on the certificate (the 14-digit number goes on every pack), and it lasts forever (1-5 years, renew before expiry). Which did you believe: 1, 2 or 3?",
 cap_mg="FSSAI-ye kurichulla 3 thettidhaarana: cheriya kachavadathinu venda, number certificate-il maathram mathi, orikkal eduthaal mathi. Moonnum thettu. Ethaanu ningal viswasichirunnathu: 1, 2, 3?")

duo("fs009", "cloud_kitchen", "B", "hostel", "20 പേർക്ക് മാത്രം\nഹോസ്റ്റൽ ടിഫിൻ.\n\"ആര് ചോദിക്കാൻ?\"", [
 ("A","wide","സഞ്ജൂ, നിന്റെ ടിഫിൻ സർവീസിന് ഇപ്പോ 20 കുട്ടികളായി. FSSAI എടുത്തോ?"),
 ("V","V","അലീനേ, 20 പാത്രം ചോറിനാണോ ലൈസൻസ്? ആര് ചോദിക്കാൻ വരാനാ?"),
 ("A","A","ഒരു കുട്ടിക്ക് വയറുവേദന വന്നാൽ മതി, എല്ലാരും ചോദിക്കും."),
 ("V","wide","എടുക്കാതിരുന്നാൽ എന്താ സംഭവിക്കുക?"),
 ("A","A","ലൈസൻസ് ഇല്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ ജയിലും. ബേസിക് രജിസ്ട്രേഷൻ മതി നിനക്ക്."),
 ("V","wide","ചോറ് 20 പാത്രം. റിസ്ക് 5 ലക്ഷം.")],
 "ചോറ് 20 പാത്രം,\nറിസ്ക് 5 ലക്ഷം", CTA_FOOD, theme="new",
 cap_ml="20 കുട്ടികൾക്ക് മാത്രം ഹോസ്റ്റൽ ടിഫിൻ നൽകുന്നതിനും FSSAI വേണം. ചെറിയ കച്ചവടത്തിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ ജയിലും. നിങ്ങൾ വീട്ടിൽ നിന്ന് ടിഫിൻ നൽകുന്നുണ്ടോ?",
 cap_en="A tiffin service for 20 hostel students still needs FSSAI: basic registration is enough at that size. Selling food without it can mean a penalty up to Rs 5 lakh and up to 6 months in prison. Do you run a tiffin or meal service: yes or no?",
 cap_mg="20 kuttikalkku maathram hostel tiffin nalkunnathinum FSSAI venam. Cheriya kachavadathinu basic registration mathi. Illaathe vittaal 5 lakh vare pizhayum 6 maasam vare jailum. Ningal veettil ninnu tiffin nalkunnundo?")
