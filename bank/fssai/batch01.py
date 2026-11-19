# FSSAI seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_FSSAI. Amounts are turnover limits / statutory penalties (no rupee word next to them). People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

duo("fsd001", "home_baker", "A", "kitchen", "വീട്ടിലെ കേക്ക്.\n\"ഇതിനൊക്കെ ലൈസൻസ്\nവേണോ?\"", [
 ("A","wide","രാജേഷേട്ടാ, ഈ മാസം 60 കേക്ക് ഓർഡർ. നമ്മുടെ അടുക്കള തന്നെ ഫാക്ടറി."),
 ("V","V","ബിന്ദൂ, FSSAI രജിസ്ട്രേഷൻ എടുത്തോ?"),
 ("A","A","വീട്ടിൽ ഉണ്ടാക്കുന്നതിനും വേണോ?"),
 ("V","V","വേണം. വർഷം 12 ലക്ഷം വരെ ടേൺഓവർ ഉള്ളവർക്ക് ബേസിക് രജിസ്ട്രേഷൻ. ഹോം ബേക്കർമാർക്കും."),
 ("A","wide","ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും ജയിലും ആകാമെന്ന് കേട്ടു."),
 ("V","wide","ക്രീം പൊങ്ങട്ടെ, പിഴ പൊങ്ങരുത്.")],
 "വീട്ടിലെ കേക്കിനും\nFSSAI", CTA_FOOD, theme="faq",
 cap_ml="വീട്ടിൽ കേക്ക് ഉണ്ടാക്കി വിൽക്കുന്നവർക്കും FSSAI വേണം: വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ. നിങ്ങൾ വീട്ടിൽ നിന്ന് ഭക്ഷണം വിൽക്കുന്നുണ്ടോ?",
 cap_en="Home bakers need FSSAI too: basic registration covers turnover up to Rs 12 lakh a year. Selling food without it can mean a penalty up to Rs 5 lakh and up to 6 months in jail. Do you sell food from home?",
 cap_mg="Veettil cake undaakki vilkkunnavarkkum FSSAI venam: varsham 12 laksham vare turnover-nu basic registration. Ningal veettil ninnu food vilkkunnundo?")

duo("fsd002", "cloud_kitchen", "B", "foodcourt", "ഡെലിവറി ആപ്പ് ചോദിച്ചു:\n\"FSSAI നമ്പർ?\"\nമെനു റെഡി, നമ്പർ ഇല്ല", [
 ("A","wide","ഡെന്നിസേ, ആപ്പിൽ ലിസ്റ്റ് ചെയ്യാൻ നോക്കി. FSSAI നമ്പർ ഇല്ലാതെ മുന്നോട്ട് പോകുന്നില്ല."),
 ("V","V","മരിയ, മെനുവും ഫോട്ടോയും എല്ലാം റെഡിയാണല്ലോ."),
 ("A","A","ഫോട്ടോ പോരാ. ഡെലിവറി ആപ്പുകൾ FSSAI നമ്പർ ചോദിക്കും."),
 ("V","V","ഏത് വേണം? നമ്മുടെ ടേൺഓവർ 12 ലക്ഷം കടക്കും."),
 ("A","wide","12 ലക്ഷം കടന്നാൽ ബേസിക് പോരാ, സ്റ്റേറ്റ് ലൈസൻസ്. 20 കോടി വരെ അത് മതി."),
 ("V","wide","അരി കുതിർക്കും മുമ്പ് ലൈസൻസ്.")],
 "ആപ്പിൽ കയറാൻ\nFSSAI നമ്പർ", CTA_FSSAI, theme="new",
 cap_ml="ക്ലൗഡ് കിച്ചൺ ഡെലിവറി ആപ്പിൽ ലിസ്റ്റ് ചെയ്യാൻ FSSAI നമ്പർ വേണം. ടേൺഓവർ 12 ലക്ഷം കടന്നാൽ ബേസിക് രജിസ്ട്രേഷൻ പോരാ, സ്റ്റേറ്റ് ലൈസൻസ് വേണം.",
 cap_en="Delivery apps ask for your FSSAI number before a cloud kitchen goes live. Above Rs 12 lakh turnover, basic registration is not enough: you need a state licence (up to Rs 20 crore). Planning a cloud kitchen in Kerala?",
 cap_mg="Cloud kitchen delivery app-il list cheyyaan FSSAI number venam. Turnover 12 laksham kadannaal basic registration pora, state licence venam.")

duo("fsd003", "packaged_food", "A", "fishmarket", "ഉണക്കമീൻ പാക്കറ്റ്.\nസൂപ്പർമാർക്കറ്റ്\nതിരിച്ചയച്ചു", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, സൂപ്പർമാർക്കറ്റ് നമ്മുടെ ഉണക്കമീൻ പാക്കറ്റുകൾ തിരിച്ചയച്ചു."),
 ("V","V","സുമേ, മീൻ നല്ലതല്ലേ? എന്താ പ്രശ്നം?"),
 ("A","A","പാക്കറ്റിൽ FSSAI നമ്പർ ഇല്ല."),
 ("V","V","പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം. അതാണ് ആദ്യം നോക്കുന്നത്."),
 ("A","wide","അപ്പോ ആദ്യം ലൈസൻസ്, പിന്നെ പുതിയ ലേബൽ."),
 ("V","wide","മീനിന് ഉപ്പ്, പാക്കറ്റിന് നമ്പർ.")],
 "പാക്കറ്റിൽ\n14 അക്ക നമ്പർ", CTA_FSSAI, theme="new",
 cap_ml="പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം. ഉണക്കമീൻ മുതൽ അച്ചാർ വരെ. നിങ്ങളുടെ പാക്കറ്റിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="A supermarket returns a batch of dried-fish packets: no FSSAI number on the label. Packaged food must carry the 14-digit FSSAI number. Is it on your packets?",
 cap_mg="Pack cheythu vilkkunna food-il 14 akka FSSAI number print cheyyanam. Unakkameen muthal achaar vare. Ningalude packet-il number undo?")

duo("fsd004", "cafe_owner", "B", "cafe", "കഫേ തുടങ്ങി 5 വർഷം.\nലൈസൻസ് തീർന്നത്\nആരും അറിഞ്ഞില്ല", [
 ("A","wide","റോഷാ, ചുമരിലെ FSSAI ലൈസൻസ് ഒന്ന് നോക്കിയേ. തീയതി കഴിഞ്ഞു."),
 ("V","V","ആൽവിനേ, അത് ഒരിക്കൽ എടുത്താൽ പോരേ?"),
 ("A","A","ഇല്ല. ഒന്ന് മുതൽ അഞ്ച് വർഷം വരെയാണ് സാധുത. തീരും മുമ്പ് പുതുക്കണം."),
 ("V","V","അപ്പോ ഇത്രയും ദിവസം നമ്മൾ ലൈസൻസില്ലാതെയാണോ കോഫി വിറ്റത്?"),
 ("A","wide","അതേ. ഇന്ന് തന്നെ നോക്കാം. അടുത്ത തവണ തീയതി ഫോണിൽ റിമൈൻഡർ."),
 ("V","wide","കോഫി ഫ്രഷ്, ലൈസൻസ് പഴകി.")],
 "ലൈസൻസിനും\nഎക്സ്പയറി ഡേറ്റ്", CTA_FSSAI, theme="faq",
 cap_ml="FSSAI ലൈസൻസ് ഒന്ന് മുതൽ അഞ്ച് വർഷം വരെ മാത്രം. കാലാവധി തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടെ ലൈസൻസ് എന്ന് തീരും എന്ന് അറിയാമോ?",
 cap_en="A cafe's FSSAI licence quietly expired. Registrations and licences are valid for 1 to 5 years and must be renewed before expiry. Do you know when yours ends?",
 cap_mg="FSSAI licence onnu muthal anchu varsham vare maathram. Kaalaavadhi theerum mumbu puthukkanam. Ningalude licence ennu theerum ennu ariyaamo?")

duo("fsd005", "spice_exporter", "A", "munnar", "ഏലക്ക കച്ചവടം\n25 കോടി കടന്നു.\nസ്റ്റേറ്റ് ലൈസൻസ് മതിയോ?", [
 ("A","wide","ബേസിലേ, ഈ വർഷം ഏലക്ക വിറ്റുവരവ് 25 കോടി കടന്നു."),
 ("V","V","സെലിൻ ചേച്ചി, നമുക്ക് സ്റ്റേറ്റ് FSSAI ലൈസൻസ് ഉണ്ടല്ലോ."),
 ("A","A","സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി വരെ മാത്രം. അതിന് മുകളിൽ സെൻട്രൽ ലൈസൻസ്."),
 ("V","V","ഈന്തപ്പഴം ഇറക്കുമതി ചെയ്യാനും പ്ലാനുണ്ട്."),
 ("A","wide","ഇറക്കുമതിക്കും സെൻട്രൽ ലൈസൻസ് തന്നെ. രണ്ടിനും ഒരേ ഉത്തരം."),
 ("V","wide","ഏലക്ക വളർന്നു, ലൈസൻസും വളരണം.")],
 "20 കോടി കടന്നാൽ\nസെൻട്രൽ ലൈസൻസ്", CTA_FSSAI, theme="new",
 cap_ml="FSSAI സ്റ്റേറ്റ് ലൈസൻസ് 20 കോടി ടേൺഓവർ വരെ. അതിന് മുകളിലും ഭക്ഷണം ഇറക്കുമതി ചെയ്യുന്നവർക്കും സെൻട്രൽ ലൈസൻസ് വേണം. സ്പൈസ് ബിസിനസുകൾ ശ്രദ്ധിക്കുക.",
 cap_en="A cardamom trader crosses Rs 25 crore turnover. The FSSAI state licence covers up to Rs 20 crore; above that, and for all food importers, you need a central licence.",
 cap_mg="FSSAI state licence 20 crore turnover vare. Athinu mukalilum food import cheyyunnavarkkum central licence venam. Spice businesses shraddhikkuka.")

lst("fsl001", "home_baker", "B", "FSSAI: നിങ്ങൾക്ക്\nഏത് വേണം?", [
 ("ബേസിക് രജിസ്ട്രേഷൻ", "വർഷം 12 ലക്ഷം വരെ ടേൺഓവർ. ഹോം ബേക്കർമാർക്കും ചെറിയ കടകൾക്കും."),
 ("സ്റ്റേറ്റ് ലൈസൻസ്", "12 ലക്ഷം മുതൽ 20 കോടി വരെ ടേൺഓവർ."),
 ("സെൻട്രൽ ലൈസൻസ്", "20 കോടിക്ക് മുകളിൽ. പിന്നെ എല്ലാ ഇറക്കുമതിക്കാർക്കും.")],
 "നിങ്ങൾ ഏത്\nലെവലിൽ?", CTA_FSSAI, theme="faq",
 cap_ml="FSSAI മൂന്ന് തരം: 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ, 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്, അതിന് മുകളിലും ഇറക്കുമതിക്കും സെൻട്രൽ ലൈസൻസ്. നിങ്ങൾ ഏതിൽ: 1, 2, 3?",
 cap_en="Three FSSAI levels: basic registration up to Rs 12 lakh turnover, state licence up to Rs 20 crore, central licence above that and for importers. Which one are you: 1, 2 or 3?",
 cap_mg="FSSAI moonnu tharam: 12 laksham vare basic registration, 20 crore vare state licence, athinu mukalilum import-num central licence. Ningal ethil: 1, 2, 3?")
