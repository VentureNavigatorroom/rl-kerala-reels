# FSSAI batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD


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
