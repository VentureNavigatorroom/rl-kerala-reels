# IEC seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_IEC. Never mention fees or customs duty amounts. People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo("ied001", "handicraft_export", "A", "photocopy", "ദുബായിൽ നിന്ന് ആദ്യ\nഓർഡർ: 200 സാരി.\nഷിപ്പർ: \"IEC എവിടെ?\"", [
 ("A","wide","ഉണ്ണീ, ഇൻസ്റ്റഗ്രാം വഴി ദുബായിൽ നിന്ന് 200 കസവ് സാരിയുടെ ഓർഡർ!"),
 ("V","V","അശ്വതീ, പാഴ്സൽ അയക്കും മുമ്പ് ഒന്ന് ചോദിക്കട്ടെ. IEC ഉണ്ടോ?"),
 ("A","A","അതെന്താ?"),
 ("V","V","DGFT തരുന്ന 10 അക്ക ഇംപോർട്ട് എക്സ്പോർട്ട് കോഡ്. കച്ചവടത്തിന് സാധനം കയറ്റി അയക്കുമ്പോൾ കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("A","wide","ബിസിനസിന്റെ പാനുമായി ബന്ധിപ്പിച്ചതാണല്ലേ. ഇന്ന് തന്നെ അപേക്ഷിക്കാം."),
 ("V","wide","സാരി മടക്കും മുമ്പ് കോഡ് എടുക്കണം.")],
 "ആദ്യ എക്സ്പോർട്ടിന്\nമുമ്പ് IEC", CTA_EXPORT, theme="crm",
 cap_ml="ഇൻസ്റ്റഗ്രാമിൽ നിന്ന് ആദ്യ വിദേശ ഓർഡർ വന്നോ? കച്ചവടത്തിന് സാധനം കയറ്റി അയക്കാൻ DGFT-യുടെ 10 അക്ക IEC വേണം; കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ ആദ്യ ഓർഡർ ഏത് രാജ്യത്ത് നിന്ന്?",
 cap_en="First overseas order from Instagram? To export goods commercially you need the 10-digit Import Export Code from DGFT, linked to your business PAN; customs and banks ask for it. Where did your first order come from?",
 cap_mg="Instagram-il ninnu aadya videsha order vanno? Kachavadathinu saadhanam kayatti ayakkaan DGFT-yude 10 akka IEC venam; customs-um bank-um chodikkum. Ningalude aadya order ethu raajyathu ninnu?")

duo("ied002", "importer", "B", "mall", "ഇറക്കുമതി ചെയ്ത സാധനം\nതുറമുഖത്ത്.\nIEC ഡിആക്ടിവേറ്റഡ്", [
 ("A","wide","ജാഫറിക്കാ, തുറമുഖത്ത് നിന്ന് വിളിച്ചു. നമ്മുടെ IEC ഡിആക്ടിവേറ്റഡ് ആണെന്ന്."),
 ("V","V","സുമയ്യാ, IEC ഒരിക്കലും എക്സ്പയർ ആകില്ലെന്നല്ലേ പറഞ്ഞത്?"),
 ("A","A","എക്സ്പയർ ആകില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം."),
 ("V","V","ഈ വർഷം നമ്മൾ അത് മറന്നു."),
 ("A","wide","അതാ ഡിആക്ടിവേറ്റ് ആയത്. ഇനി കലണ്ടറിൽ ഏപ്രിൽ ഒന്ന് മാർക്ക് ചെയ്യാം."),
 ("V","wide","കോഡിന് മരണമില്ല, പക്ഷേ ഉറക്കമുണ്ട്.")],
 "എല്ലാ വർഷവും\nഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ്", CTA_IEC, theme="faq",
 cap_ml="IEC ഒരിക്കലും എക്സ്പയർ ആകില്ല, പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ ഡിആക്ടിവേറ്റ് ആകും. നിങ്ങൾ ഈ വർഷം അപ്ഡേറ്റ് ചെയ്തോ?",
 cap_en="An IEC never expires, but it must be updated online every year between April and June or it is deactivated, and goods can get stuck. Did you update yours this year?",
 cap_mg="IEC orikkalum expire aakilla, pakshe ella varshavum April muthal June vare online-aayi update cheyyanam. Illenkil deactivate aakum. Ningal ee varsham update cheytho?")

duo("ied003", "service_export", "A", "library", "സോഫ്റ്റ്വെയർ കയറ്റുമതിക്ക്\nIEC വേണ്ട?\nപകുതി ശരി", [
 ("A","wide","അനൂപേ, നമ്മുടെ ആനിമേഷൻ സ്റ്റുഡിയോയുടെ ക്ലയന്റുകൾ എല്ലാം കാനഡയിൽ. IEC വേണോ?"),
 ("V","V","ഗ്രീഷ്മേ, സാധനമൊന്നും കയറ്റി അയക്കുന്നില്ലല്ലോ. വേണ്ട."),
 ("A","A","കസ്റ്റംസിന് വേണ്ട, ശരി. പക്ഷേ എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ സർവീസ് എക്സ്പോർട്ടർക്കും IEC വേണം."),
 ("V","V","ആനുകൂല്യം വേണ്ടെന്ന് പറയാൻ നമ്മൾ ആരാ?"),
 ("A","wide","ഒരു പാനിന് ഒരു IEC. എടുത്താൽ വർഷം തോറും അപ്ഡേറ്റ് മാത്രം."),
 ("V","wide","ഫ്രെയിം നമ്മുടേത്, കോഡും നമ്മുടേത്.")],
 "സർവീസ് എക്സ്പോർട്ടിനും\nIEC ഉപകാരം", CTA_IEC, theme="faq",
 cap_ml="ഐടി, ആനിമേഷൻ, ഡിസൈൻ സേവനങ്ങൾ വിദേശത്തേക്ക് ചെയ്യുന്നവർക്ക് കസ്റ്റംസിന് IEC വേണ്ട. പക്ഷേ എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ വേണം. നിങ്ങളുടെ ക്ലയന്റുകൾ ഏത് രാജ്യത്ത്?",
 cap_en="Service exporters (IT, animation, design) don't need an IEC for customs, but they need one to claim export benefits. One IEC per PAN, updated every year. Where are your clients?",
 cap_mg="IT, animation, design services videshathekku cheyyunnavarkku customs-nu IEC venda. Pakshe export benefits claim cheyyaan venam. Ningalude clients ethu raajyathu?")

duo("ied004", "spice_trade", "B", "rubber", "കുരുമുളകിന് ഒരു IEC.\nകാപ്പിക്ക് വേറൊന്ന്?", [
 ("A","wide","തോമസേ, കുരുമുളക് ബ്രാൻഡിന് IEC ഉണ്ട്. കാപ്പി ബ്രാൻഡിന് പുതിയത് എടുക്കണം."),
 ("V","V","ജോയിച്ചേട്ടാ, രണ്ട് ബ്രാൻഡും ഒരേ ബിസിനസിന്റെ പാനിൽ അല്ലേ?"),
 ("A","A","അതേ."),
 ("V","V","എങ്കിൽ ഒരു പാനിന് ഒരു IEC മാത്രം. രണ്ട് ബ്രാൻഡിനും അതുതന്നെ."),
 ("A","wide","അപ്പോ രണ്ടാമത്തെ അപേക്ഷ വേണ്ട."),
 ("V","wide","ബ്രാൻഡ് രണ്ട്, കോഡ് ഒന്ന്.")],
 "ഒരു പാൻ,\nഒരു IEC", CTA_IEC, theme="new",
 cap_ml="ഒരു ബിസിനസ് പാനിന് ഒരു IEC മാത്രം. കുരുമുളകും കാപ്പിയും വേറെ ബ്രാൻഡായാലും ഒരേ പാൻ ആണെങ്കിൽ ഒരേ കോഡ്. നിങ്ങൾ എത്ര ഉൽപ്പന്നങ്ങൾ കയറ്റി അയക്കുന്നു?",
 cap_en="One PAN, one IEC. A spice trader exporting pepper and coffee under two brands uses the same code if both run under the same business PAN. How many products do you export?",
 cap_mg="Oru business PAN-nu oru IEC maathram. Kurumulakum kaappiyum vere brand aayaalum ore PAN aanenkil ore code. Ningal ethra products kayatti ayakkunnu?")

chat("iec001", "importer", "A", "ലണ്ടനിൽ നിന്ന്\nലാപ്ടോപ്പ് വരുന്നു.\nഇതിനും IEC വേണോ?", ("ഗായത്രി", "അനന്തു"), [
 (0,"അനന്തു, ചേട്ടൻ ലണ്ടനിൽ നിന്ന് ഒരു ലാപ്ടോപ്പ് അയക്കുന്നു. IEC എടുക്കണോ?"),
 (1,"നീ അത് വിൽക്കാൻ പോവുകയാണോ?"),
 (0,"ഇല്ല, എനിക്ക് ഉപയോഗിക്കാൻ."),
 (1,"സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണ്ട. കച്ചവടത്തിനാണെങ്കിൽ വേണം."),
 (0,"അപ്പോ 50 ലാപ്ടോപ്പ് കൊണ്ടുവന്ന് വിറ്റാലോ?"),
 (1,"അത് സ്വന്തം ഉപയോഗമല്ല, ബിസിനസ്. അപ്പോ IEC.")],
 "ഉപയോഗിക്കാൻ: വേണ്ട\nവിൽക്കാൻ: വേണം", CTA_IEC, theme="faq",
 cap_ml="സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണ്ട. വിൽക്കാനാണെങ്കിൽ, ഒന്നായാലും അമ്പതായാലും, ബിസിനസ് ഇറക്കുമതിക്ക് IEC വേണം. ഗൾഫിൽ നിന്ന് സാധനം കൊണ്ടുവന്ന് വിൽക്കാൻ പ്ലാനുണ്ടോ?",
 cap_en="Importing a laptop for yourself? No IEC needed. Importing goods to sell is business, and that needs an Import Export Code. Planning to bring goods from the Gulf to sell?",
 cap_mg="Swantham upayogathinulla import-nu IEC venda. Vilkkaanaanenkil, business import-nu IEC venam. Gulf-il ninnu saadhanam konduvannu vilkkaan plan undo?")
