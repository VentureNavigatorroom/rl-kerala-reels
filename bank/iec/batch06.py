# IEC batch 06 (21 Nov, month backlog). Facts only from topics.FACTS_IEC. No fees. People, firms and towns invented.
# crm scripts use STORY_THEMES C12, C13, #26 (Gulf returnee) and the "too busy, next week" pattern with changed sector, place and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

# CRM C12 (family trade on both sides): goods go out AND come in; one code for both directions
duo("ied043", "importer", "A", "ferry", "ചിപ്സ് ഒമാനിലേക്ക്.\nകുന്തിരിക്കം തിരിച്ച്.\nരണ്ട് കോഡ്?", [
 ("A","wide","ടോണീ, ഒമാനിലുള്ള ആങ്ങള പറയുന്നു: ഏത്തക്ക ചിപ്സ് അങ്ങോട്ട് അയക്ക്, പള്ളിക്കും അമ്പലത്തിനും വിൽക്കാൻ കുന്തിരിക്കം ഇങ്ങോട്ട് അയക്കാം."),
 ("V","V","മീരേ, അപ്പോ ഒന്ന് കയറ്റുമതി, ഒന്ന് ഇറക്കുമതി. രണ്ട് കോഡ് എടുക്കണ്ടേ?"),
 ("A","A","ഒന്ന് പോകും, ഒന്ന് വരും. അതാ എന്റെയും സംശയം."),
 ("V","wide","IEC ഒരു PAN-ന് ഒന്നേ ഉള്ളൂ. ബിസിനസിന്റെ PAN-ലെ ആ പത്തക്ക കോഡ് കയറ്റുമതിക്കും ഇറക്കുമതിക്കും ഒന്നുതന്നെ."),
 ("A","A","അപ്പോ വാതിൽ ഒന്ന്, വഴി രണ്ട്."),
 ("V","wide","ചിപ്സ് പോട്ടെ, കുന്തിരിക്കം വരട്ടെ, കോഡ് ഒന്ന് മതി.")],
 "പോകാനും വരാനും\nകോഡ് ഒന്ന്", CTA_IEC, theme="crm",
 cap_ml="ഗൾഫിലെ ആങ്ങളയ്ക്ക് ഏത്തക്ക ചിപ്സ് അയക്കുന്നു, തിരിച്ച് വിൽക്കാൻ കുന്തിരിക്കം ഇറക്കുമതി ചെയ്യുന്നു. ബിസിനസിന്റെ PAN-ലെ ഒരു IEC കയറ്റുമതിക്കും ഇറക്കുമതിക്കും മതി, ഒരു PAN-ന് ഒരു കോഡ്. നിങ്ങളുടെ കച്ചവടം ഒരു വഴിയോ രണ്ട് വഴിയോ?",
 cap_en="Banana chips go to a brother in Oman, and frankincense comes back to sell in Kerala. One IEC on the business PAN covers both export and import; there is only one code per PAN. Does your trade go one way or both ways?",
 cap_mg="Gulf-ile aangalaykku ethakka chips ayakkunnu, thirichu vilkkaan kunthirikkam import cheyyunnu. Business PAN-ile oru IEC export-inum import-inum mathi, oru PAN-inu oru code. Ningalude kachavadam oru vazhiyo randu vazhiyo?")

# CRM #26 + C13 (Gulf returnee restarting): the old code did not die, it fell asleep
duo("ied044", "first_exporter", "B", "munnar", "8 വർഷം ഗൾഫിൽ.\nപഴയ IEC\nചത്തുപോയോ?", [
 ("A","wide","ബേസിലേ, എട്ട് വർഷം ഗൾഫിൽ. ഇപ്പോ വീണ്ടും ഹോംമെയ്ഡ് ചോക്ലേറ്റ് കയറ്റുമതി തുടങ്ങുവാണോ?"),
 ("V","V","അതേ സെലിനേ. പഴയ IEC ഒക്കെ ചത്തുകാണും. പുതിയത് എടുക്കണം."),
 ("A","A","ബിസിനസ് പഴയതുതന്നെ അല്ലേ? PAN മാറിയോ?"),
 ("V","V","ഇല്ല, PAN അതുതന്നെ. ഒന്നും മാറിയിട്ടില്ല."),
 ("A","wide","IEC-ന് കാലാവധി ഇല്ല. പക്ഷേ ഏപ്രിൽ മുതൽ ജൂൺ വരെയുള്ള വാർഷിക അപ്ഡേറ്റ് മുടങ്ങിയാൽ ഡീആക്ടിവേറ്റ് ആകും. ഒരു PAN-ന് ഒരു കോഡേ ഉള്ളൂ."),
 ("V","wide","അപ്പോ പുതിയത് വേണ്ട, ഉറങ്ങുന്നതിനെ ഉണർത്തിയാൽ മതി.")],
 "കോഡ് ചത്തിട്ടില്ല,\nഉറങ്ങുകയാ", CTA_EXPORT, theme="crm",
 cap_ml="വർഷങ്ങൾ ഗൾഫിൽ കഴിഞ്ഞ് തിരിച്ചെത്തി പഴയ കയറ്റുമതി വീണ്ടും തുടങ്ങുന്നവർ ശ്രദ്ധിക്കുക: IEC-ന് കാലാവധി ഇല്ല, ഒരു PAN-ന് ഒരു കോഡ് മാത്രം. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. നിങ്ങളുടെ പഴയ IEC ഇപ്പോൾ ആക്ടീവ് ആണോ?",
 cap_en="Back from years in the Gulf and restarting an old export business? An IEC never expires and there is only one per PAN, so you don't take a new one. But if the yearly April to June online update was missed, it is deactivated. Is your old IEC active?",
 cap_mg="Varshangal Gulf-il kazhinju thirichethi pazhaya export veendum thudangunnavar shraddhikkuka: IEC-inu kaalaavadhi illa, oru PAN-inu oru code maathram. Pakshe ella varshavum April-June update cheythillenkil deactivate aakum. Ningalude pazhaya IEC ippol active aano?")

# CRM "too busy, next week" pattern: an overseas advance waits while the code waits
duo("ied045", "handicraft_export", "A", "bank", "\"അടുത്താഴ്ച\"\nഎന്ന് എഴുതിയിട്ട്\nമൂന്ന് മാസം", [
 ("A","wide","മനോജേ, ജപ്പാനിലെ സംഗീതക്കട ഓടക്കുഴലിന്റെ അഡ്വാൻസ് അയക്കാമെന്ന് പറഞ്ഞിട്ട് മൂന്ന് മാസമായില്ലേ?"),
 ("V","V","അതേ ശ്രുതീ. ബാങ്ക് ഫോമിൽ ഒരു കോളം: IEC. ഞാൻ അവിടെ എഴുതി, 'അടുത്താഴ്ച'."),
 ("A","A","ആ അടുത്താഴ്ചയ്ക്ക് ഇപ്പോ മൂന്ന് മാസം പ്രായം."),
 ("A","wide","വിദേശത്തേക്ക് സാധനം വിൽക്കുമ്പോൾ ബാങ്കും കസ്റ്റംസും IEC ചോദിക്കും. ബിസിനസിന്റെ PAN വെച്ച് DGFT-യിൽ ഓൺലൈനായി എടുക്കാം."),
 ("V","V","ഓഫീസിൽ പോകണ്ടല്ലോ. എങ്കിൽ ഇന്ന് രാത്രി തന്നെ."),
 ("A","wide","ഓടക്കുഴലിന് ശ്വാസം വേണം, കയറ്റുമതിക്ക് കോഡും.")],
 "ഓടക്കുഴലിന് ശ്വാസം,\nകയറ്റുമതിക്ക് കോഡ്", CTA_IEC, theme="crm",
 cap_ml="ജപ്പാനിലെ കടയിലേക്ക് മുള ഓടക്കുഴൽ അയക്കാൻ ഓർഡർ ഉണ്ട്, പക്ഷേ ബാങ്ക് ഫോമിലെ IEC കോളം മൂന്ന് മാസമായി 'അടുത്താഴ്ച'. വിദേശത്തേക്ക് സാധനം വിൽക്കാൻ ബിസിനസിന്റെ PAN-ൽ DGFT-യുടെ IEC വേണം; ബാങ്കും കസ്റ്റംസും ചോദിക്കും. നിങ്ങൾ എന്താണ് 'അടുത്താഴ്ച'യിലേക്ക് മാറ്റിവെച്ചിരിക്കുന്നത്?",
 cap_en="A Japanese music shop is ready to send an advance for bamboo flutes, but the IEC field on the bank form has said 'next week' for three months. To sell goods abroad you need DGFT's IEC on the business PAN, applied for online; banks and customs ask for it. What have you been putting off till next week?",
 cap_mg="Japan-ile kadayilekku mula odakkuzhal ayakkaan order undu, pakshe bank form-ile IEC column moonnu maasamaayi 'adutha aazhcha'. Videshathekku saadhanam vilkkaan business PAN-il DGFT-yude IEC venam; bank-um customs-um chodikkum. Ningal enthaanu 'adutha aazhcha'-yilekku maattivechirikkunnathu?")

# CRM C13 (supplying Kerala from abroad): suitcase stock is still business stock
duo("ied046", "importer", "C", "gulf", "ലീവിന് വരുമ്പോൾ\n30 കുപ്പി അത്തർ.\n\"പെട്ടിയിലല്ലേ?\"", [
 ("A","wide","ഫൈസലേ, ഓരോ ലീവിനും പെട്ടിയിൽ മുപ്പത് കുപ്പി അത്തർ. നാട്ടിൽ ഇൻസ്റ്റഗ്രാമിൽ വിൽക്കാം."),
 ("V","V","ഷിജൂ, പെട്ടിയിൽ കൊണ്ടുപോകുന്നത് പേഴ്സണൽ അല്ലേ? കോഡ് ഒന്നും വേണ്ട."),
 ("A","A","വിൽക്കാനാണെങ്കിൽ പിന്നെ എങ്ങനെ പേഴ്സണൽ ആകും?"),
 ("A","wide","സ്വന്തം ഉപയോഗത്തിനുള്ളതിന് മാത്രമേ IEC ഒഴിവുള്ളൂ. വിൽക്കാൻ കൊണ്ടുവരുന്നത് ബിസിനസ് ഇറക്കുമതി. നാട്ടിലെ ബിസിനസിന്റെ PAN-ൽ IEC വേണം."),
 ("V","V","അപ്പോ ആദ്യം നാട്ടിൽ ബിസിനസ്, പിന്നെ കോഡ്, പിന്നെ അത്തർ."),
 ("V","wide","മണം സ്വന്തത്തിന്, കച്ചവടം കോഡിന്.")],
 "മണം സ്വന്തത്തിന്,\nകച്ചവടം കോഡിന്", CTA_IEC, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് ഓരോ ലീവിനും പെട്ടിയിൽ അത്തർ കൊണ്ടുവന്ന് ഇൻസ്റ്റഗ്രാമിൽ വിൽക്കാനാണ് പ്ലാൻ. സ്വന്തം ഉപയോഗത്തിനുള്ളതിന് മാത്രമേ IEC ഒഴിവുള്ളൂ; വിൽക്കാനുള്ളത് ബിസിനസ് ഇറക്കുമതി, നാട്ടിലെ ബിസിനസ് PAN-ൽ IEC വേണം. നിങ്ങൾ ഗൾഫിൽ നിന്ന് എന്ത് കൊണ്ടുവന്ന് വിൽക്കാനാണ് ആലോചിക്കുന്നത്?",
 cap_en="Two friends in the Gulf plan to carry perfume oils home in their suitcases every leave and sell them on Instagram. Only personal-use imports skip the IEC; goods brought in to sell are a business import and need an IEC on the Kerala business's PAN. What would you bring from the Gulf to sell?",
 cap_mg="Gulf-il ninnu oro leave-inum pettiyil attar konduvannu Instagram-il vilkkaanaanu plan. Swantham upayogathinullathinu maathrame IEC ozhivulloo; vilkkaanullathu business import, naattile business PAN-il IEC venam. Ningal Gulf-il ninnu enthu konduvannu vilkkaanaanu aalochikkunnathu?")

# FAQ: ordering stock on a foreign shopping app is still an import
duo("ied047", "importer", "A", "busstop", "ആപ്പിൽ ഒരു ക്ലിക്ക്.\n500 പട്ടം\nവിദേശത്ത് നിന്ന്", [
 ("A","wide","അഖിലേ, ബീച്ച് ഫെസ്റ്റിവലിന് 500 എൽഇഡി പട്ടം ഒരു വിദേശ ആപ്പിൽ ഓർഡർ ചെയ്തെന്ന് കേട്ടു?"),
 ("V","V","ജിബിനേ, ബട്ടൺ ഞെക്കി, പൈസ അടച്ചു. അത്ര തന്നെ. ഇതിന് എന്ത് കോഡ്?"),
 ("A","A","500 പട്ടവും നീ തന്നെ പറത്തുമോ?"),
 ("A","wide","ആപ്പ് വഴി ആയാലും വിൽക്കാനുള്ള സാധനം ബിസിനസ് ഇറക്കുമതിയാ. ബിസിനസിന്റെ PAN-ൽ IEC വേണം. സ്വന്തം ഉപയോഗത്തിന് മാത്രമേ ഒഴിവുള്ളൂ."),
 ("V","V","ബട്ടൺ എളുപ്പം, കസ്റ്റംസ് അങ്ങനെയല്ല, അല്ലേ?"),
 ("A","wide","പട്ടത്തിന് ചരട്, ഇറക്കുമതിക്ക് കോഡ്.")],
 "പട്ടത്തിന് ചരട്,\nഇറക്കുമതിക്ക് കോഡ്", CTA_IEC, theme="faq",
 cap_ml="വിദേശ ഷോപ്പിംഗ് ആപ്പിൽ ഒരു ക്ലിക്കിൽ 500 പട്ടം കച്ചവടത്തിന് ഓർഡർ ചെയ്താലും അത് ബിസിനസ് ഇറക്കുമതിയാണ്. ബിസിനസിന്റെ PAN-ൽ IEC വേണം; സ്വന്തം ഉപയോഗത്തിനുള്ള സാധനത്തിന് മാത്രമാണ് ഒഴിവ്. നിങ്ങൾ കടയിലേക്കുള്ള സ്റ്റോക്ക് ഓൺലൈനായി വിദേശത്ത് നിന്ന് വാങ്ങാറുണ്ടോ?",
 cap_en="Ordering 500 kites for a beach festival stall on a foreign shopping app is still a business import, even if it takes one click. You need an IEC on the business PAN; only goods for personal use are exempt. Do you buy shop stock from abroad online?",
 cap_mg="Videsha shopping app-il oru click-il 500 pattam kachavadathinu order cheythaalum athu business import aanu. Business PAN-il IEC venam; swantham upayogathinulla saadhanathinu maathramaanu ozhivu. Ningal kadayilekkulla stock online-aayi videshathu ninnu vaangaarundo?")

# FAQ: "nothing changed, so no yearly update"
duo("ied048", "spice_trade", "B", "cafe", "\"ഒന്നും മാറിയില്ല.\nപിന്നെന്തിന്\nഅപ്ഡേറ്റ്?\"", [
 ("A","wide","റോഷനേ, മെയ് മാസമായി. നമ്മുടെ IEC ഈ വർഷം അപ്ഡേറ്റ് ചെയ്തോ?"),
 ("V","V","ആൽവിനേ, വിലാസം മാറിയില്ല, ബാങ്ക് മാറിയില്ല, ഒന്നും മാറിയില്ല. പിന്നെന്ത് അപ്ഡേറ്റ്?"),
 ("A","A","കൊറിയയിലേക്കുള്ള കാപ്പിക്കുരു അടുത്ത മാസമല്ലേ പോകുന്നത്?"),
 ("A","wide","ഒന്നും മാറിയില്ലെങ്കിലും എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ IEC ഡീആക്ടിവേറ്റ് ആകും."),
 ("V","V","അപ്പോ ഒന്നും മാറിയില്ലെന്ന് പറയാനും ഒരു അപ്ഡേറ്റ്."),
 ("V","wide","മാറ്റമില്ലെങ്കിലും അപ്ഡേറ്റ് മാറ്റരുത്.")],
 "മാറ്റമില്ലെങ്കിലും\nഅപ്ഡേറ്റ് മാറ്റരുത്", CTA_EXPORT, theme="faq",
 cap_ml="വിലാസവും ബാങ്കും ഒന്നും മാറിയില്ലെങ്കിൽ IEC അപ്ഡേറ്റ് വേണ്ടെന്ന് കരുതരുത്. എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം, ഇല്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. ഈ വർഷത്തെ അപ്ഡേറ്റ് ചെയ്തോ: അതെ അല്ലെങ്കിൽ ഇല്ല?",
 cap_en="A coffee roastery exporting beans to Korea thought the IEC update was only for when details change. It is yearly: update online between April and June every year even if nothing changed, or the code is deactivated. Did you do this year's update: yes or no?",
 cap_mg="Vilaasavum bank-um onnum maariyillenkil IEC update vendennu karutharuthu. Ella varshavum April muthal June vare online-aayi update cheyyanam, illenkil deactivate aakum. Ee varshathe update cheytho: athe allenkil illa?")

# FAQ: a friend wants to borrow your IEC number
duo("ied049", "handicraft_export", "A", "hostel", "\"നിന്റെ IEC നമ്പർ\nഒന്ന് തരുമോ?\nഫോമിൽ എഴുതാനാ\"", [
 ("A","wide","സഞ്ജൂ, നിന്റെ ക്രോഷേ പാവകൾ അയക്കാൻ എന്റെ IEC നമ്പർ ചോദിച്ചല്ലോ. എന്തിനാ?"),
 ("V","V","അലീനേ, നിനക്ക് ചെരിപ്പ് കയറ്റുമതി ഉണ്ടല്ലോ. ഫോമിൽ ഒരു നമ്പർ എഴുതാനല്ലേ, അത് കുറയില്ലല്ലോ."),
 ("A","A","നമ്പർ കുറയില്ല. പക്ഷേ ഷിപ്പ്മെന്റ് ആരുടേതാകും?"),
 ("A","wide","IEC എന്റെ ബിസിനസ് PAN-ന്റേതാ. അതിൽ പോകുന്നതെല്ലാം എന്റെ കയറ്റുമതി. കസ്റ്റംസും ബാങ്കും ചോദിക്കുന്നത് എന്നോടാകും."),
 ("V","V","അപ്പോ എനിക്ക് എന്റെ PAN-ൽ എന്റെ കോഡ്."),
 ("A","wide","കോഡ് കടം കൊടുത്താൽ കയറ്റുമതിക്കാരിയും ഞാനാകും.")],
 "കോഡ് കടം കൊടുത്താൽ\nകയറ്റുമതിക്കാരനും നിങ്ങൾ", CTA_IEC, theme="faq",
 cap_ml="സുഹൃത്തിന്റെ പാവകൾ അയക്കാൻ നിങ്ങളുടെ IEC നമ്പർ ചോദിച്ചാൽ ആലോചിക്കണം. IEC നിങ്ങളുടെ ബിസിനസ് PAN-മായി ബന്ധിച്ചതാണ്; അതിൽ പോകുന്ന ഷിപ്പ്മെന്റ് നിങ്ങളുടെ ബിസിനസിന്റെ കയറ്റുമതിയാകും, കസ്റ്റംസും ബാങ്കും നിങ്ങളോട് ചോദിക്കും. ആരെങ്കിലും നിങ്ങളുടെ കോഡ് ചോദിച്ചിട്ടുണ്ടോ?",
 cap_en="A friend wants your IEC number to ship his crochet dolls. The IEC is linked to your business PAN, so anything shipped under it becomes your business's export, and customs and banks will come to you. Each exporter takes their own code on their own PAN. Has anyone asked to use yours?",
 cap_mg="Suhruthinte paavakal ayakkaan ningalude IEC number chodichaal aalochikkanam. IEC ningalude business PAN-umaayi bandhichathaanu; athil pokunna shipment ningalude business-inte export aakum, customs-um bank-um ningalodu chodikkum. Aarenkilum ningalude code chodichittundo?")

# NEW (d904 pattern): "it's art, not trade" - Pulikali masks for a carnival abroad
duo("ied050", "handicraft_export", "B", "park", "\"ഇത് കലയല്ലേ,\nകച്ചവടമല്ലല്ലോ\"\n60 പുലിമുഖം ബ്രസീലിലേക്ക്", [
 ("A","wide","അനന്തൂ, ബ്രസീലിലെ കാർണിവൽ ടീമിന് 60 പുലിക്കളി മുഖംമൂടി? അവർ പൈസ തരുമോ?"),
 ("V","V","തരും ഗായത്രീ. പക്ഷേ ഇത് കലയല്ലേ? കച്ചവടമല്ലല്ലോ. കോഡ് ഒന്നും വേണ്ട."),
 ("A","A","കല നിന്റേത്. പക്ഷേ പെട്ടി കടക്കുന്നത് അതിർത്തിയാ."),
 ("A","wide","പൈസയ്ക്ക് വിദേശത്തേക്ക് സാധനം അയച്ചാൽ അത് കയറ്റുമതി. ബിസിനസിന്റെ PAN-ൽ DGFT-യുടെ പത്തക്ക IEC വേണം. കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("V","V","അപ്പോ പുലി ബ്രസീലിലേക്ക് ചാടും മുമ്പ് ഒരു കോഡ്."),
 ("A","wide","പുലിക്ക് വര, പെട്ടിക്ക് കോഡ്.")],
 "പുലിക്ക് വര,\nപെട്ടിക്ക് കോഡ്", CTA_EXPORT, theme="new",
 cap_ml="പുലിക്കളി മുഖംമൂടികൾ ബ്രസീലിലെ കാർണിവൽ ടീമിന് പൈസയ്ക്ക് അയക്കുന്നത് കലയാണ്, പക്ഷേ നിയമത്തിൽ അത് കയറ്റുമതിയാണ്. ബിസിനസിന്റെ PAN-ൽ DGFT-യുടെ പത്തക്ക IEC വേണം; കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ നാട്ടിലെ ഏത് കലാരൂപം ലോകം കാണണം?",
 cap_en="Pulikali tiger masks sold to a carnival troupe in Brazil are art, but shipping them abroad for payment is an export. You need DGFT's 10-digit IEC on the business PAN; customs and banks ask for it. Which Kerala art form should the world see?",
 cap_mg="Pulikali mukhamoodikal Brazil-ile carnival team-inu paisaykku ayakkunnathu kalayaanu, pakshe niyamathil athu export aanu. Business PAN-il DGFT-yude pathakka IEC venam; customs-um bank-um chodikkum. Ningalude naattile ethu kalaaroopam lokam kaananam?")

# NEW (d904 pattern): "the neighbour country needs no code" - coconut-climbing belts to Sri Lanka
duo("ied051", "first_exporter", "A", "foodcourt", "\"ശ്രീലങ്ക\nതൊട്ടടുത്തല്ലേ,\nകോഡ് എന്തിന്?\"", [
 ("A","wide","ഡെന്നിസേ, നിന്റെ തെങ്ങുകയറ്റ ബെൽറ്റ് ശ്രീലങ്കയിലെ തോട്ടക്കാർ 80 എണ്ണം ചോദിച്ചെന്ന്?"),
 ("V","V","അതേ മരിയേ. പക്ഷേ ശ്രീലങ്ക തൊട്ടടുത്തല്ലേ. അയൽക്കാർക്ക് എന്ത് കോഡ്?"),
 ("A","A","അടുത്താണെങ്കിലും കടൽ കടക്കില്ലേ?"),
 ("A","wide","ഏത് രാജ്യത്തേക്കായാലും ബിസിനസിനായി സാധനം കയറ്റി അയച്ചാൽ IEC വേണം. ബിസിനസിന്റെ PAN-ലെ പത്തക്ക കോഡ്. കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("V","wide","തെങ്ങ് കയറാൻ ബെൽറ്റ്, കടൽ കടക്കാൻ കോഡ്.")],
 "തെങ്ങ് കയറാൻ ബെൽറ്റ്,\nകടൽ കടക്കാൻ കോഡ്", CTA_EXPORT, theme="new",
 cap_ml="തെങ്ങുകയറ്റ ബെൽറ്റ് ഉണ്ടാക്കുന്ന ഒരാൾക്ക് ശ്രീലങ്കയിലെ തോട്ടങ്ങളിൽ നിന്ന് ഓർഡർ. അയൽരാജ്യമായാലും ബിസിനസിനായി സാധനം കയറ്റുമതി ചെയ്യാൻ ബിസിനസിന്റെ PAN-ൽ പത്തക്ക IEC വേണം; കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ ഉൽപ്പന്നം ആദ്യം ഏത് രാജ്യത്തേക്ക്?",
 cap_en="A coconut-climbing belt maker gets an order from plantations in Sri Lanka. Even for a neighbouring country, exporting goods for business needs a 10-digit IEC on the business PAN; customs and banks ask for it. Which country would your product go to first?",
 cap_mg="Thengukayatta belt undaakkunna oraalkku Sri Lanka-yile thottangalil ninnu order. Ayalraajyamaayaalum business-inaayi saadhanam export cheyyaan business PAN-il pathakka IEC venam; customs-um bank-um chodikkum. Ningalude ulpannam aadyam ethu raajyathekku?")

# FAQ: "I have Udyam, that's my export licence"
duo("ied052", "first_exporter", "C", "teashop", "\"ഉദ്യം ഉണ്ടല്ലോ.\nകയറ്റുമതിക്ക്\nഅത് പോരേ?\"", [
 ("A","wide","വിഷ്ണൂ, ദുബായിലെ ഹോട്ടലിന് 300 ഇഡ്ഡലിച്ചെമ്പ് അയക്കാൻ എല്ലാം റെഡിയായോ?"),
 ("V","V","അനൂ, ഉദ്യം സർട്ടിഫിക്കറ്റ് ഫ്രെയിം ചെയ്ത് ചുവരിൽ വെച്ചിട്ടുണ്ട്. സർക്കാർ രജിസ്ട്രേഷൻ ഒന്ന് മതിയല്ലോ."),
 ("A","A","അത് ചെറുകിട സംരംഭം ആണെന്നതിന്. കസ്റ്റംസ് ചോദിക്കുന്ന നമ്പർ വേറെയാ."),
 ("A","wide","സാധനം കയറ്റുമതി ചെയ്യാൻ DGFT-യുടെ പത്തക്ക IEC വേണം, ബിസിനസിന്റെ PAN-മായി ബന്ധിച്ചത്. ഉദ്യം അതിന് പകരമാവില്ല."),
 ("V","wide","ചുവരിൽ സർട്ടിഫിക്കറ്റ്, പെട്ടിയിൽ കോഡ്.")],
 "ചുവരിൽ സർട്ടിഫിക്കറ്റ്,\nപെട്ടിയിൽ കോഡ്", CTA_IEC, theme="faq",
 cap_ml="ഉദ്യം സർട്ടിഫിക്കറ്റ് ഉണ്ടെങ്കിൽ കയറ്റുമതിക്ക് വേറൊന്നും വേണ്ടെന്ന് കരുതരുത്. സാധനം കയറ്റുമതി ചെയ്യാൻ DGFT-യുടെ പത്തക്ക IEC വേണം, ബിസിനസ് PAN-മായി ബന്ധിച്ചത്; കസ്റ്റംസും ബാങ്കും അതാണ് ചോദിക്കുക. നിങ്ങളുടെ ചുവരിൽ ഏതൊക്കെ സർട്ടിഫിക്കറ്റുണ്ട്?",
 cap_en="An Udyam certificate on the wall is not an export code. To export goods, like 300 idli steamers for a hotel in Dubai, you need DGFT's 10-digit IEC linked to the business PAN; customs and banks ask for that. Which certificates hang on your wall?",
 cap_mg="Udyam certificate undenkil export-inu veronnum vendennu karutharuthu. Saadhanam export cheyyaan DGFT-yude pathakka IEC venam, business PAN-umaayi bandhichathu; customs-um bank-um athaanu chodikkuka. Ningalude chuvaril ethokke certificate-undu?")
