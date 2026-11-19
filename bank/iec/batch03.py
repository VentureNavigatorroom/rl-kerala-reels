# IEC batch 03 (20 Nov, month backlog). Facts only from topics.FACTS_IEC. No fees. People, firms and towns invented.
# crm scripts use STORY_THEMES #7, C12, C13 with changed sector, place and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo("ied015", "handicraft_export", "A", "tailor", "ചിരട്ട കൊണ്ടുള്ള\nകപ്പ്. 300 എണ്ണം\nനോർവേയിലേക്ക്", [
 ("A","wide","മോഹനേട്ടാ, ചിരട്ട കപ്പിന് നോർവേയിൽ നിന്ന് 300 എണ്ണത്തിന്റെ ഓർഡർ! IEC ഒക്കെ വലിയ കമ്പനികൾക്കല്ലേ?"),
 ("V","V","ഉഷേ, കോഡിന് കമ്പനിയുടെ വലിപ്പം നോക്കലില്ല. കച്ചവടത്തിന് സാധനം കയറ്റി അയച്ചാൽ വേണം."),
 ("A","A","മുന്നൂറ് കപ്പിനും?"),
 ("V","V","അതെ. ബിസിനസിന്റെ PAN-ൽ DGFT നൽകുന്ന പത്ത് അക്ക കോഡ്. കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("A","wide","എങ്കിൽ പാക്ക് ചെയ്യും മുമ്പ് എടുക്കാം."),
 ("V","wide","ചിരട്ട ചെറുത്, നിയമം ഒന്ന്.")],
 "ഓർഡർ ചെറുതായാലും\nകയറ്റുമതിക്ക് IEC", CTA_EXPORT, theme="faq",
 cap_ml="ചെറിയ കരകൗശല ബിസിനസ് ആണെങ്കിലും കച്ചവടത്തിന് സാധനം കയറ്റുമതി ചെയ്യാൻ IEC വേണം. ബിസിനസ് PAN-ൽ DGFT നൽകുന്ന 10 അക്ക കോഡാണ് ഇത്. നിങ്ങളുടെ കരകൗശലം വിദേശത്ത് വിറ്റിട്ടുണ്ടോ?",
 cap_en="Even a small handicraft business needs an IEC to export goods for sale. It is a 10-digit code from DGFT linked to the business PAN; customs and banks ask for it. Have you sold your craft abroad yet?",
 cap_mg="Cheriya handicraft business aanelum export cheyyaan IEC venam. Business PAN-il DGFT tharunna 10 digit code. Ningalude craft videshathu vittittundo?")

duo("ied016", "first_exporter", "A", "bakery", "\"ഓരോ വർഷവും\nIEC പുതിയത്\nഎടുക്കണം\"", [
 ("A","wide","സാബുച്ചേട്ടാ, കായ വറുത്തതിന്റെ കയറ്റുമതി അടുത്ത വർഷവും ഉണ്ട്. IEC വീണ്ടും പുതിയതായി അപേക്ഷിക്കണ്ടേ?"),
 ("V","V","ജിഷേ, ആരാ അങ്ങനെ പറഞ്ഞത്?"),
 ("A","A","അടുത്ത കടയിലെ ചേട്ടൻ. വർഷം കഴിഞ്ഞാൽ കോഡ് തീരുമെന്ന്."),
 ("V","V","IEC-ക്ക് കാലാവധി ഇല്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനിൽ അപ്ഡേറ്റ് ചെയ്യണം."),
 ("A","wide","അപ്പോ പുതിയ അപേക്ഷ വേണ്ട, അപ്ഡേറ്റ് മതി."),
 ("V","wide","പുതുക്കേണ്ട, പുതുക്കി പറഞ്ഞാൽ മതി.")],
 "പുതിയ കോഡ് വേണ്ട\nവർഷം തോറും അപ്ഡേറ്റ്", CTA_IEC, theme="faq",
 cap_ml="IEC ഒരിക്കലും എക്സ്പയർ ആകില്ല, വീണ്ടും അപേക്ഷിക്കേണ്ടതില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം, ഇല്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. നിങ്ങൾ ഈ വർഷം അപ്ഡേറ്റ് ചെയ്തോ?",
 cap_en="An IEC never expires and you never re-apply. But it must be updated online every year between April and June, or it is deactivated. Did you update yours this year?",
 cap_mg="IEC expire aakilla, veendum apply cheyyenda. Pakshe ella varshavum April muthal June vare online update cheyyanam. Ee varsham update cheytho?")

duo("ied017", "spice_trade", "A", "gulfoffice", "ദുബായിൽ നിന്ന്\nഈന്തപ്പഴം നാട്ടിലെ\nകടയിലേക്ക്. കോഡ്?", [
 ("A","wide","ആസിഫ്, ഇവിടത്തെ ഈന്തപ്പഴം നാട്ടിലെ നമ്മുടെ കടയിൽ വിൽക്കാനാ പ്ലാൻ. ഇക്കാക്കയുടെ കൈയിൽ കൊടുത്തുവിട്ടാൽ പോരേ?"),
 ("V","V","ഷഹാനാ, അത് വിൽക്കാനുള്ള സ്റ്റോക്കല്ലേ? സ്വന്തം ഉപയോഗമല്ല."),
 ("A","A","അതെ, മാസം തോറും വേണം."),
 ("V","V","കച്ചവടത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണം. നാട്ടിലെ കടയുടെ ബിസിനസ് PAN-ൽ എടുക്കണം."),
 ("A","wide","അപ്പോ ആദ്യം കോഡ്, പിന്നെ കണ്ടെയ്നർ."),
 ("V","wide","പെട്ടിയിൽ കൊണ്ടുവരുന്നത് സമ്മാനം. കച്ചവടത്തിന് കോഡ്.")],
 "വിൽക്കാനുള്ള ഇറക്കുമതി\nIEC ഇല്ലാതെ ഇല്ല", CTA_IEC, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് സാധനം കൊണ്ടുവന്ന് നാട്ടിലെ കടയിൽ വിൽക്കാനാണെങ്കിൽ അത് ബിസിനസ് ഇറക്കുമതിയാണ്. നാട്ടിലെ ബിസിനസിന്റെ PAN-ൽ IEC വേണം. സ്വന്തം ഉപയോഗത്തിന് മാത്രം വേണ്ട. നിങ്ങൾ എന്താണ് ഇറക്കുമതി ചെയ്യാൻ ആലോചിക്കുന്നത്?",
 cap_en="Bringing goods from the Gulf to sell in your Kerala shop is a business import, so you need an IEC on the Kerala business's PAN. Only personal-use imports are exempt. What are you planning to import?",
 cap_mg="Gulf-il ninnu sadhanam konduvannu naattile kadayil vilkkaan aanel IEC venam, naattile business PAN-il. Swantham upayogathinu maathram venda. Enthaanu import cheyyaan plan?")

duo("ied018", "importer", "A", "home", "അച്ഛന്റെ IEC\nഉണ്ട്. പുതിയ\nകമ്പനിക്കും അത് മതി?", [
 ("A","wide","അരുൺ, അച്ഛന്റെ പഴയ കയറ്റുമതി സ്ഥാപനത്തിന് IEC ഉണ്ടല്ലോ. നമ്മുടെ പുതിയ പ്രൈവറ്റ് ലിമിറ്റഡിനും അത് ഉപയോഗിക്കാം, അല്ലേ?"),
 ("V","V","സ്നേഹേ, പുതിയ കമ്പനിക്ക് പുതിയ PAN അല്ലേ?"),
 ("A","A","അതെ, കമ്പനിയുടെ പേരിൽ വേറെ PAN."),
 ("V","V","IEC PAN-ന്റേതാണ്. ഒരു PAN-ന് ഒരു IEC. പുതിയ PAN-ന് സ്വന്തം കോഡ് വേണം."),
 ("A","wide","അപ്പോ അച്ഛന്റെ കോഡ് അച്ഛന്റെ സ്ഥാപനത്തിന് മാത്രം."),
 ("V","wide","കുടുംബം ഒന്ന്, PAN രണ്ട്, കോഡ് രണ്ട്.")],
 "പുതിയ PAN-ന്\nപുതിയ IEC", CTA_IEC, theme="crm",
 cap_ml="കുടുംബ ബിസിനസിന് IEC ഉണ്ടെങ്കിലും പുതിയ കമ്പനിക്ക് അത് ഉപയോഗിക്കാൻ പറ്റില്ല. IEC ബിസിനസ് PAN-മായി ബന്ധിപ്പിച്ചതാണ്: ഒരു PAN-ന് ഒരു IEC. നിങ്ങളുടെ കുടുംബത്തിൽ എത്ര സ്ഥാപനങ്ങളുണ്ട്?",
 cap_en="A family firm's IEC cannot be used by a new company. The IEC is tied to the business PAN, one IEC per PAN, so the new company needs its own. How many businesses run in your family?",
 cap_mg="Kudumba business-nte IEC puthiya company-kku use cheyyaan pattilla. IEC PAN-umaayi linked: oru PAN-nu oru IEC. Ningalude kudumbathil ethra business und?")

duo("ied019", "first_exporter", "A", "metro", "ഇൻസ്റ്റഗ്രാമിൽ\nകുർത്ത. സിംഗപ്പൂർ\nഓർഡർ കൊറിയറിൽ", [
 ("A","wide","കിരൺ, സിംഗപ്പൂരിലെ കസ്റ്റമേഴ്സ് മാസം നാല്പത് കുർത്ത ചോദിക്കുന്നു. കൊറിയർ അല്ലേ, കയറ്റുമതി ആവില്ലല്ലോ?"),
 ("V","V","അഞ്ജലീ, ഇന്ത്യയ്ക്ക് പുറത്ത് വിൽക്കാൻ സാധനം പോകുന്നു. വഴി കൊറിയർ ആയാലും കപ്പൽ ആയാലും."),
 ("A","A","അപ്പോ എനിക്ക് IEC വേണോ?"),
 ("V","V","വേണം. കച്ചവട കയറ്റുമതിക്ക് IEC. കസ്റ്റംസും വിദേശ പണം വരുമ്പോൾ ബാങ്കും ചോദിക്കും."),
 ("A","wide","പാക്കറ്റ് ചെറുതാണെന്ന് കരുതി ഞാൻ വിട്ടു."),
 ("V","wide","പെട്ടി ചെറുതാകാം, കയറ്റുമതി കയറ്റുമതി തന്നെ.")],
 "കൊറിയറിൽ വിറ്റാലും\nകയറ്റുമതി തന്നെ", CTA_EXPORT, theme="crm",
 cap_ml="ഇൻസ്റ്റഗ്രാം വഴി വിദേശത്തേക്ക് വസ്ത്രം വിൽക്കുന്നത് കൊറിയറിൽ ആണെങ്കിലും കയറ്റുമതിയാണ്. കച്ചവടത്തിനുള്ള കയറ്റുമതിക്ക് IEC വേണം, കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ ഓർഡറുകൾ ഏത് രാജ്യത്ത് നിന്നാണ്?",
 cap_en="Selling clothes abroad through Instagram is still an export, even by courier. Exporting goods for business needs an IEC, and customs and banks ask for it. Which country do your orders come from?",
 cap_mg="Instagram vazhi videshathekku dress vilkkunnathu courier-il aanelum export aanu. Business export-nu IEC venam. Ningalude order ethu raajyathu ninnaanu?")

duo("ied020", "importer", "A", "airport", "ഡ്രോൺ പാർട്സ്\nബാഗിൽ കൊണ്ടുവന്നു.\nകസ്റ്റംസ് നിർത്തി", [
 ("A","wide","റഫീഖേ, ദോഹയിൽ നിന്ന് കൊച്ചിയിലെ സ്റ്റാർട്ടപ്പിന് ഡ്രോൺ പാർട്സ് ബാഗിൽ കൊണ്ടുവന്നു. കസ്റ്റംസ് ചോദ്യം ചെയ്തു."),
 ("V","V","ഷമീറേ, അത് നിന്റെ സ്വന്തം ഉപയോഗത്തിനാണോ?"),
 ("A","A","അല്ല, കമ്പനി അസംബിൾ ചെയ്ത് വിൽക്കാൻ."),
 ("V","V","അപ്പോ ബിസിനസ് ഇറക്കുമതി. കമ്പനിയുടെ PAN-ൽ IEC എടുത്ത് ആ വഴി വരുത്തണം."),
 ("A","wide","പ്രവാസിയുടെ ബാഗ് വഴി എളുപ്പമാകുമെന്ന് കരുതി."),
 ("V","wide","ബാഗ് യാത്രയ്ക്ക്. സ്റ്റോക്കിന് കോഡ്.")],
 "കമ്പനിയുടെ സാധനത്തിന്\nകമ്പനിയുടെ IEC", CTA_IEC, theme="crm",
 cap_ml="വിദേശത്ത് നിന്ന് കമ്പനിക്ക് വേണ്ടി പാർട്സ് കൊണ്ടുവരുന്നത് സ്വന്തം ഉപയോഗമല്ല, ബിസിനസ് ഇറക്കുമതിയാണ്. കമ്പനിയുടെ PAN-ൽ IEC വേണം. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പിന് പാർട്സ് പുറത്ത് നിന്നാണോ?",
 cap_en="Carrying parts from abroad for your company is not a personal-use import; it is a business import, and the company needs an IEC on its PAN. Do your startup's parts come from abroad?",
 cap_mg="Videshathu ninnu company-kku parts konduvarunnathu personal use alla, business import aanu. Company PAN-il IEC venam. Ningalude startup-nte parts purathu ninnaano?")

duo("ied021", "first_exporter", "A", "beach", "അലങ്കാര മത്സ്യം\nസിംഗപ്പൂരിലേക്ക്.\n\"മീൻ സാധനമല്ലല്ലോ\"", [
 ("A","wide","നിഖിലേ, നിന്റെ ഗപ്പിയും ഗോൾഡ് ഫിഷും സിംഗപ്പൂരിലേക്ക് പോകുന്നെന്ന് കേട്ടു. കോഡ് എടുത്തോ?"),
 ("V","V","ദിവ്യേ, ജീവനുള്ള മീനല്ലേ. അത് സാധനമൊന്നുമല്ലല്ലോ."),
 ("A","A","വിറ്റ് പണം വാങ്ങുന്നില്ലേ?"),
 ("V","V","ഉണ്ട്. ഓ, വിൽക്കാൻ അയച്ചാൽ അത് കയറ്റുമതി. അപ്പോ IEC വേണം, ബാങ്കും ചോദിക്കും."),
 ("A","wide","അതെ. ബിസിനസ് PAN-ൽ പത്ത് അക്ക കോഡ്."),
 ("V","wide","മീൻ നീന്തും, രേഖ നീന്തില്ല.")],
 "ജീവനുള്ളതായാലും\nവിൽപ്പനയ്ക്ക് IEC", CTA_EXPORT, theme="faq",
 cap_ml="അലങ്കാര മത്സ്യം പോലെ ജീവനുള്ളതായാലും വിൽക്കാൻ വിദേശത്തേക്ക് അയച്ചാൽ അത് കയറ്റുമതിയാണ്. ബിസിനസ് PAN-ൽ IEC വേണം. നിങ്ങളുടെ ഹോബി ഒരു കയറ്റുമതി ബിസിനസ് ആയോ?",
 cap_en="Even live ornamental fish count as goods when you ship them abroad for sale. That is an export, so you need an IEC on the business PAN. Has your hobby turned into an export business?",
 cap_mg="Alankaara malsyam pole jeevanullathaayalum vilkkaan videshathekku ayachaal export aanu. Business PAN-il IEC venam. Ningalude hobby export business aayo?")

duo("ied022", "handicraft_export", "A", "weddinghall", "നെറ്റിപ്പട്ടം\nഅമേരിക്കയിലെ\nക്ഷേത്രത്തിലേക്ക്", [
 ("A","wide","ശരത്തേ, അമേരിക്കയിലെ ഒരു ക്ഷേത്രം പന്ത്രണ്ട് നെറ്റിപ്പട്ടം ചോദിച്ചു. ഇത് ഭക്തിയല്ലേ, കച്ചവടമാണോ?"),
 ("V","V","കാവ്യേ, അവർ പണം തരുന്നുണ്ടോ?"),
 ("A","A","ഉണ്ട്. ഓരോന്നിനും ബിൽ അയക്കണം."),
 ("V","V","എങ്കിൽ കച്ചവട കയറ്റുമതി. നിന്റെ ബിസിനസ് PAN-ൽ IEC വേണം. ബാങ്കും പണം വരുമ്പോൾ ചോദിക്കും."),
 ("A","wide","എങ്കിൽ ആദ്യം കോഡ്, പിന്നെ പട്ടം."),
 ("V","wide","പട്ടം തിളങ്ങും, കോഡ് ഇല്ലെങ്കിൽ പെട്ടി ഇരുട്ടിൽ.")],
 "പണം വാങ്ങി അയച്ചാൽ\nഅത് കയറ്റുമതി", CTA_EXPORT, theme="new",
 cap_ml="നെറ്റിപ്പട്ടം പോലുള്ള കരകൗശലം വിദേശത്ത് വിറ്റ് പണം വാങ്ങിയാൽ അത് കയറ്റുമതിയാണ്. ബിസിനസ് PAN-ൽ IEC വേണം, കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ നാട്ടിലെ ഏത് കരകൗശലമാണ് പുറത്ത് പോകേണ്ടത്?",
 cap_en="Selling a craft like a nettipattam abroad for payment is an export. You need an IEC on your business PAN; customs and banks ask for it. Which craft from your town should go global?",
 cap_mg="Nettipattam pole ulla craft videshathu vittu panam vaangiyaal export aanu. Business PAN-il IEC venam. Ningalude naattile ethu craft aanu purathu pokendathu?")

duo("ied023", "spice_trade", "A", "homestay", "ഈ വർഷം\nഒരു ഷിപ്പ്മെന്റും\nഇല്ല. അപ്ഡേറ്റ്?", [
 ("A","wide","ജോമോനേ, ഹോംസ്റ്റേ തിരക്കിൽ ഈ വർഷം അച്ചാർ കയറ്റുമതി ഒന്നും നടന്നില്ല. IEC അപ്ഡേറ്റ് വേണ്ടല്ലോ?"),
 ("V","V","ടീനേ, അടുത്ത സീസണിൽ വീണ്ടും അയക്കില്ലേ?"),
 ("A","A","അയക്കും. ദുബായിലെ ഓർഡർ ജനുവരിയിൽ."),
 ("V","V","എങ്കിൽ ഏപ്രിൽ മുതൽ ജൂൺ വരെ അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ IEC ഡീആക്ടിവേറ്റ് ആകും."),
 ("A","wide","ഷിപ്പ്മെന്റ് ഇല്ലെങ്കിലും അപ്ഡേറ്റ് വേണം."),
 ("V","wide","കച്ചവടം ഉറങ്ങിയാലും അപ്ഡേറ്റ് ഉണരണം.")],
 "ഷിപ്പ്മെന്റ് ഇല്ലെങ്കിലും\nവർഷത്തെ അപ്ഡേറ്റ്", CTA_IEC, theme="faq",
 cap_ml="ഈ വർഷം ഒരു കയറ്റുമതിയും ഇല്ലെങ്കിലും IEC എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ അടുത്ത ഓർഡർ വരുമ്പോൾ കോഡ് ഡീആക്ടിവേറ്റ് ആയിരിക്കും. നിങ്ങളുടെ കയറ്റുമതി സീസണൽ ആണോ?",
 cap_en="Even in a year with no shipments, the IEC must be updated online between April and June, or it will be deactivated when the next order comes. Is your export business seasonal?",
 cap_mg="Ee varsham oru export-um illenkilum IEC April muthal June vare update cheyyanam. Illenkil next order varumbol code deactivate aayirikkum. Ningalude export seasonal aano?")

chat("iec002", "importer", "A", "ഇറ്റലിയിൽ നിന്ന്\nകാപ്പിക്കുരു. ബാങ്ക്:\n\"IEC നമ്പർ?\"", ("ആൽവിൻ", "നീതു"), [
 (0,"നീതു, കഫേയിൽ പായ്ക്ക് ചെയ്ത് വിൽക്കാൻ ഇറ്റലിയിൽ നിന്ന് കാപ്പിക്കുരു വരുത്തുന്നു. ബാങ്ക് പണം അയക്കാൻ IEC ചോദിച്ചു."),
 (1,"കസ്റ്റംസ് മാത്രമല്ല, ഇറക്കുമതിക്ക് പണം അയക്കുമ്പോൾ ബാങ്കും IEC ചോദിക്കും."),
 (0,"കഫേയിൽ ഉപയോഗിക്കാനും കൂടിയാണ്. എന്നിട്ടും?"),
 (1,"വിൽക്കാനുള്ളതും ബിസിനസിന് വേണ്ടിയുള്ളതുമാണ്. കഫേയുടെ PAN-ൽ IEC എടുക്കണം."),
 (0,"അപ്പോ ആദ്യം കോഡ്, പിന്നെ പേമെന്റ്."),
 (1,"അതെ. കോഡ് ഇല്ലെങ്കിൽ കാപ്പി കപ്പലിൽ തന്നെ.")],
 "ബാങ്കും IEC ചോദിക്കും", CTA_IEC, theme="new",
 cap_ml="കച്ചവടത്തിന് സാധനം ഇറക്കുമതി ചെയ്യുമ്പോൾ കസ്റ്റംസ് മാത്രമല്ല, വിദേശത്തേക്ക് പണം അയക്കുന്ന ബാങ്കും IEC ചോദിക്കും. ബിസിനസ് PAN-ൽ എടുക്കണം. നിങ്ങളുടെ കഫേയിലോ കടയിലോ ഇറക്കുമതി സാധനങ്ങളുണ്ടോ?",
 cap_en="When you import goods for business, the bank sending your payment abroad asks for the IEC too, not just customs. Take it on the business PAN. Does your cafe or shop sell imported goods?",
 cap_mg="Business-nu import cheyyumbol customs maathramalla, panam ayakkunna bank-um IEC chodikkum. Business PAN-il edukkanam. Ningalude cafe-il imported sadhanam undo?")
