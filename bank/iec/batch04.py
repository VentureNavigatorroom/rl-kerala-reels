# IEC batch 04 (20 Nov, month backlog). Facts only from topics.FACTS_IEC. No fees. People, firms and towns invented.
# crm scripts use STORY_THEMES #7, #11, C12 with changed sector, place and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

# CRM C12 (family trade on both sides), d904 pattern: Onam mundu "gifts" that are really stock
duo("ied024", "handicraft_export", "B", "textile", "\"ഗിഫ്റ്റ്\" എന്നെഴുതി\n40 പെട്ടി കസവുമുണ്ട്\nമസ്കറ്റിലേക്ക്", [
 ("A","wide","പ്രകാശേട്ടാ, ഓണത്തിന് 40 പെട്ടി കസവുമുണ്ട് വീണ്ടും 'ഗിഫ്റ്റ്' എന്നെഴുതി അയക്കുകയാണോ?"),
 ("V","V","രമ്യേ, അത് കസിന്റെ കടയിലേക്കാ. ബന്ധുവിന് കൊടുക്കുന്നത് സമ്മാനമല്ലേ?"),
 ("A","A","അവിടെ വിറ്റ് പണം തിരിച്ചുവരുന്നുണ്ടല്ലോ. അത് സമ്മാനമല്ല, കച്ചവടത്തിനുള്ള കയറ്റുമതി."),
 ("V","V","അപ്പോ എന്ത് വേണം?"),
 ("A","wide","കടയുടെ PAN-ൽ DGFT-യുടെ 10 അക്ക IEC. കസ്റ്റംസും ബാങ്കും അത് ചോദിക്കും."),
 ("V","V","സമ്മാനത്തിന് ബിൽ വേണ്ട, കച്ചവടത്തിന് കോഡ് വേണം.")],
 "വിൽക്കാനുള്ളത്\nസമ്മാനമല്ല", CTA_IEC, theme="crm",
 cap_ml="ഗൾഫിലെ ബന്ധുവിന്റെ കടയിൽ വിൽക്കാൻ അയക്കുന്ന മുണ്ട് 'ഗിഫ്റ്റ്' അല്ല, കച്ചവടത്തിനുള്ള കയറ്റുമതിയാണ്. ബിസിനസ് PAN-ൽ 10 അക്ക IEC വേണം; കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ നാട്ടിലെ സാധനം ഗൾഫിൽ വിൽക്കുന്നുണ്ടോ?",
 cap_en="Mundus sent to a relative's shop in the Gulf for sale are not gifts; they are a business export. You need the 10-digit IEC on the business PAN, and customs and banks ask for it. Do your products sell in the Gulf?",
 cap_mg="Gulf-ile bandhuvinte kadayil vilkkan ayakkunna mundu gift alla, business export aanu. Business PAN-il 10 akka IEC venam; customs-um bank-um chodikkum. Ningalude nattile sadhanam Gulf-il vilkkunnundo?")

# CRM #7 (GST in hand, now exporting), hair oil brand
duo("ied025", "first_exporter", "A", "salon", "\"GST ഉണ്ടല്ലോ,\nകയറ്റുമതിക്ക്\nഅത് മതി\"", [
 ("A","wide","വിനീതേ, മലേഷ്യയിലെ ഒരു വിതരണക്കാരൻ നമ്മുടെ ഹെയർ ഓയിൽ 1,000 കുപ്പി ചോദിച്ചു!"),
 ("V","V","സോണിയ, GST നമ്പർ ഉണ്ടല്ലോ. അത് കൊടുത്താൽ കയറ്റി അയക്കാം."),
 ("A","A","അത് പോരാ. സാധനം കയറ്റുമതി ചെയ്യാൻ IEC വേണം, GST നമ്പർ വേറെയാണ്."),
 ("V","V","IEC എന്ന് പറഞ്ഞാൽ?"),
 ("A","wide","DGFT നൽകുന്ന 10 അക്ക കോഡ്, ബിസിനസിന്റെ PAN-ൽ. കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("V","V","GST നാട്ടിലേക്ക്, IEC കടലിനക്കരേക്ക്.")],
 "GST നമ്പർ\nIEC അല്ല", CTA_EXPORT, theme="crm",
 cap_ml="GST രജിസ്ട്രേഷൻ ഉണ്ടെങ്കിലും സാധനം കയറ്റുമതി ചെയ്യാൻ IEC വേറെ വേണം. DGFT നൽകുന്ന 10 അക്ക കോഡ്, ബിസിനസ് PAN-ൽ. നിങ്ങളുടെ ബ്രാൻഡിന് വിദേശത്ത് നിന്ന് അന്വേഷണം വന്നോ?",
 cap_en="A GST registration is not an export code. To export goods you need the IEC, a separate 10-digit code from DGFT on the business PAN. Has your brand had an enquiry from abroad yet?",
 cap_mg="GST registration undenkilum export-nu IEC vere venam. DGFT tharunna 10 akka code, business PAN-il. Ningalude brand-nu videshathu ninnu enquiry vanno?")

# CRM C12 (family trade), two siblings' firms, one container
duo("ied026", "spice_trade", "C", "kitchen", "ഒരു കണ്ടെയ്നർ.\nചേച്ചിയുടെ അച്ചാർ,\nഅനിയന്റെ മസാല", [
 ("A","wide","രാജേഷേ, ഖത്തറിലേക്ക് ഒരേ കണ്ടെയ്നർ. എന്റെ അച്ചാറും നിന്റെ മസാലയും."),
 ("V","V","ബിന്ദുചേച്ചി, എന്റെ ഫേമിന് IEC ഉണ്ട്. ചേച്ചിയുടെ അച്ചാറും അതിൽ പോകട്ടെ."),
 ("A","A","എന്റെ ബിസിനസിന് വേറെ PAN അല്ലേ? നിന്റെ കോഡിൽ എന്റെ സാധനം എങ്ങനെ?"),
 ("V","V","അപ്പോ രണ്ട് കോഡ് വേണോ?"),
 ("A","wide","അതെ. IEC ഓരോ ബിസിനസ് PAN-നും ഒന്ന്. നിന്റേത് നിന്റെ ഫേമിന് മാത്രം."),
 ("V","V","കണ്ടെയ്നർ പങ്കിടാം, കോഡ് പങ്കിടാൻ പറ്റില്ല.")],
 "കണ്ടെയ്നർ ഒന്ന്\nIEC രണ്ട്", CTA_IEC, theme="crm",
 cap_ml="രണ്ട് ബിസിനസിന്റെ സാധനം ഒരേ കണ്ടെയ്നറിൽ പോയാലും ഓരോ ബിസിനസിനും സ്വന്തം PAN-ൽ IEC വേണം. ഒരു PAN-ന് ഒരു IEC. നിങ്ങളുടെ കുടുംബത്തിൽ എത്ര ബിസിനസ്?",
 cap_en="Two family businesses can share a container, but not an IEC. The code is one per business PAN, so each business exporting needs its own. How many businesses run in your family?",
 cap_mg="Randu business-inte sadhanam ore container-il poyalum oro business-num swantham PAN-il IEC venam. Oru PAN-nu oru IEC. Ningalude kudumbathil ethra business?")

# CRM #11 (selling through a marketplace), now to another country
duo("ied027", "first_exporter", "B", "gym", "\"ആഗോള വിൽപ്പന\"\nബട്ടൺ ഓൺ ചെയ്തു.\nകോഡ് ചോദിച്ചു", [
 ("A","wide","ജസ്റ്റിനേ, നമ്മുടെ റെസിസ്റ്റൻസ് ബാൻഡ് യുഎഇയിലേക്ക് വിൽക്കാൻ മാർക്കറ്റ്പ്ലേസ് IEC ചോദിക്കുന്നു."),
 ("V","V","റിയേ, മാർക്കറ്റ്പ്ലേസ് വലിയ കമ്പനിയല്ലേ? അവരുടെ കോഡ് പോരേ?"),
 ("A","A","അയക്കുന്നത് നമ്മുടെ സാധനം, പണം വരുന്നതും നമ്മുടെ അക്കൗണ്ടിലേക്ക്. കയറ്റുമതിക്കാരൻ നമ്മളാണ്."),
 ("V","V","അപ്പോ നമുക്ക് സ്വന്തം IEC?"),
 ("A","wide","അതെ, നമ്മുടെ ബിസിനസ് PAN-ൽ. DGFT-യിൽ ഓൺലൈനായി എടുക്കാം."),
 ("V","V","കട അവരുടേത്, കോഡ് നമ്മുടേത്.")],
 "പ്ലാറ്റ്ഫോം അവരുടേത്\nIEC നിങ്ങളുടേത്", CTA_EXPORT, theme="crm",
 cap_ml="ഓൺലൈൻ മാർക്കറ്റ്പ്ലേസ് വഴി വിദേശത്തേക്ക് വിൽക്കുമ്പോഴും കയറ്റുമതിക്കാരൻ നിങ്ങളുടെ ബിസിനസ് ആണ്. ബിസിനസ് PAN-ൽ സ്വന്തം IEC വേണം. നിങ്ങൾ ഏത് രാജ്യത്തേക്ക് വിൽക്കാൻ ആഗ്രഹിക്കുന്നു?",
 cap_en="Selling abroad through an online marketplace? The exporter is still your business, so you need your own IEC on the business PAN, not the platform's. Which country do you want to sell to?",
 cap_mg="Online marketplace vazhi videshathekku vilkkumpozhum exporter ningalude business aanu. Business PAN-il swantham IEC venam. Ethu rajyathekku vilkkan aagrahikkunnu?")

# FAQ: does every partner need an IEC? cashew firm, three partners
duo("ied028", "spice_trade", "A", "railway", "മൂന്ന് പാർട്ണർ.\n\"മൂന്ന് IEC\nഎടുക്കണം\"", [
 ("A","wide","ദിനേശേ, കശുവണ്ടി ഫേമിൽ നമ്മൾ മൂന്ന് പാർട്ണർ. ഓരോരുത്തരും IEC എടുക്കണോ?"),
 ("V","V","ഷീബേ, ഞാനും അങ്ങനെ കേട്ടു. മൂന്ന് പേരുടെയും പേരിൽ മൂന്ന് കോഡ്."),
 ("A","A","കയറ്റുമതി ചെയ്യുന്നത് ഫേം ആണല്ലോ, നമ്മൾ മൂന്നു പേരും വെവ്വേറെയല്ല."),
 ("V","V","അപ്പോ ഫേമിന് ഒന്ന് മതിയോ?"),
 ("A","wide","അതെ. IEC ബിസിനസിന്റെ PAN-ൽ, ഒരു PAN-ന് ഒന്ന്. ഫേമിന്റെ PAN, ഫേമിന്റെ IEC."),
 ("V","V","പാർട്ണർ മൂന്ന്, കോഡ് ഒന്ന്.")],
 "ഫേമിന് ഒരു PAN\nഒരു IEC", CTA_IEC, theme="faq",
 cap_ml="പാർട്ണർഷിപ്പ് ഫേം കയറ്റുമതി ചെയ്യുമ്പോൾ ഓരോ പാർട്ണർക്കും IEC വേണ്ട. ഫേമിന്റെ PAN-ൽ ഒരു IEC. ഒരു PAN-ന് ഒന്ന് മാത്രം. നിങ്ങളുടെ ബിസിനസിൽ എത്ര പാർട്ണർ?",
 cap_en="In a partnership firm that exports, each partner does not need an IEC. The firm takes one IEC on its own PAN; it is one per PAN. How many partners does your business have?",
 cap_mg="Partnership firm export cheyyumpol oro partner-num IEC venda. Firm-inte PAN-il oru IEC. Oru PAN-nu onnu maathram. Ningalude business-il ethra partner?")

# FAQ, d904 pattern: online Mohiniyattam classes for students abroad (service export)
duo("ied029", "service_export", "C", "classroom", "അമേരിക്കയിലെ\n30 കുട്ടികൾക്ക്\nഓൺലൈൻ മോഹിനിയാട്ടം", [
 ("A","wide","ആദർശേ, എന്റെ മോഹിനിയാട്ടം ക്ലാസിൽ ഇപ്പോൾ അമേരിക്കയിൽ നിന്ന് 30 കുട്ടികൾ!"),
 ("V","V","നിമ്മിടീച്ചറേ, സാധനം ഒന്നും പോകുന്നില്ലല്ലോ. IEC എന്ന വാക്കേ വേണ്ട."),
 ("A","A","കസ്റ്റംസിന് വേണ്ടായിരിക്കാം. പക്ഷേ ഇതും സർവീസ് കയറ്റുമതിയല്ലേ?"),
 ("V","V","അതിന് എന്ത് വ്യത്യാസം?"),
 ("A","wide","സർവീസ് കയറ്റുമതിക്കാർക്ക് എക്സ്പോർട്ട് ആനുകൂല്യം ക്ലെയിം ചെയ്യാൻ IEC വേണം."),
 ("V","V","ചുവട് കടൽ കടന്നാലും കോഡ് കൂടെ വേണം.")],
 "സർവീസ് കയറ്റുമതിക്കും\nIEC ഉപകാരം", CTA_IEC, theme="faq",
 cap_ml="വിദേശത്തെ വിദ്യാർത്ഥികൾക്ക് ഓൺലൈൻ ക്ലാസ് എടുക്കുന്നതും സർവീസ് കയറ്റുമതിയാണ്. സാധനം പോകുന്നില്ലെങ്കിലും എക്സ്പോർട്ട് ആനുകൂല്യം ക്ലെയിം ചെയ്യാൻ IEC വേണം. നിങ്ങൾ ഓൺലൈനായി എന്ത് പഠിപ്പിക്കുന്നു?",
 cap_en="Teaching online classes to students abroad is a service export. No goods cross customs, but service exporters need an IEC to claim export benefits. What do you teach online?",
 cap_mg="Videshathe students-nu online class edukkunnathum service export aanu. Sadhanam pokunnillenkilum export benefit claim cheyyan IEC venam. Ningal online-aayi enthu padippikkunnu?")

# FAQ: one-time import for a clinic
duo("ied030", "importer", "B", "hospital", "\"ഒറ്റ മെഷീൻ,\nഒരിക്കൽ മാത്രം.\nഅതിനും IEC?\"", [
 ("A","wide","ജോസഫ് ഡോക്ടറേ, ക്ലിനിക്കിലേക്കുള്ള സ്കാനിംഗ് മെഷീൻ ജർമനിയിൽ നിന്ന് വരുന്നു. IEC ഉണ്ടോ?"),
 ("V","V","ലക്ഷ്മി, ഒരു മെഷീൻ, ഒരിക്കൽ മാത്രം. അതിന് ഒരു കോഡ് എന്തിന്?"),
 ("A","A","എണ്ണം നോക്കിയല്ല. ക്ലിനിക്ക് എന്ന ബിസിനസിന് വേണ്ടിയുള്ള ഇറക്കുമതിയാണ്."),
 ("V","V","വീട്ടിലേക്കാണെങ്കിൽ?"),
 ("A","wide","സ്വന്തം ഉപയോഗത്തിന് മാത്രം IEC വേണ്ട. ക്ലിനിക്കിന് വേണ്ടതിന് ക്ലിനിക്കിന്റെ PAN-ൽ IEC."),
 ("V","V","ഒരു പെട്ടിയായാലും ബിസിനസ് ബിസിനസ് തന്നെ.")],
 "ഒരു തവണയായാലും\nബിസിനസ് ഇറക്കുമതി", CTA_IEC, theme="faq",
 cap_ml="ഒരു തവണ മാത്രം ക്ലിനിക്കിലേക്കോ കടയിലേക്കോ മെഷീൻ ഇറക്കുമതി ചെയ്താലും അത് ബിസിനസ് ഇറക്കുമതിയാണ്, IEC വേണം. സ്വന്തം ഉപയോഗത്തിന് മാത്രമാണ് ഒഴിവ്. നിങ്ങളുടെ ബിസിനസിൽ വിദേശ മെഷീൻ ഉണ്ടോ?",
 cap_en="Even a one-time import of a machine for your clinic or shop is a business import and needs an IEC on the business PAN. Only imports for personal use are exempt. Does your business use machines from abroad?",
 cap_mg="Oru thavana maathram clinic-ilekko kadayilekko machine import cheythalum athu business import aanu, IEC venam. Swantham upayogathinu maathram ozhivu. Ningalude business-il videsha machine undo?")

# FAQ: deactivated IEC, "take a new one on my wife's PAN"
chat("iec003", "importer", "A", "IEC ഡീആക്ടിവേറ്റ്.\n\"ഭാര്യയുടെ പേരിൽ\nപുതിയത് എടുക്കാം\"", ("സന്തോഷ്", "ഷിബു"), [
 (0,"ഷിബൂ, എന്റെ സ്പെയർ പാർട്സ് കടയുടെ IEC ഡീആക്ടിവേറ്റ് ആയി. ഭാര്യയുടെ പേരിൽ പുതിയൊരെണ്ണം എടുത്താലോ?"),
 (1,"സന്തോഷേ, ഇറക്കുമതി ചെയ്യുന്നത് നിന്റെ കടയല്ലേ? ഭാര്യയുടെ PAN-ൽ എടുത്താൽ ഇറക്കുമതിക്കാരി അവളാകും."),
 (0,"പിന്നെ എന്ത് ചെയ്യും?"),
 (1,"IEC ഒരിക്കലും കാലഹരണപ്പെടില്ല. ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈൻ അപ്ഡേറ്റ് ചെയ്യാത്തതുകൊണ്ടാണ് ഡീആക്ടിവേറ്റ് ആയത്."),
 (0,"അപ്പോ പുതിയ കോഡ് വേണ്ട, പഴയത് അപ്ഡേറ്റ് ചെയ്താൽ മതി."),
 (1,"അതെ. പേര് മാറ്റല്ല, അപ്ഡേറ്റ് ആണ് മരുന്ന്.")],
 "പുതിയ കോഡ് അല്ല\nഅപ്ഡേറ്റ്", CTA_IEC, theme="faq",
 cap_ml="IEC ഡീആക്ടിവേറ്റ് ആയാൽ മറ്റൊരാളുടെ PAN-ൽ പുതിയത് എടുക്കേണ്ട. IEC ബിസിനസ് PAN-ൽ ഒന്ന്; ഒരിക്കലും കാലഹരണപ്പെടില്ല, പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂണിൽ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്യണം. നിങ്ങളുടെ IEC ആക്ടീവ് ആണോ?",
 cap_en="If your IEC is deactivated, don't take a new one on a relative's PAN; that would make them the importer. The IEC never expires, but it must be updated online every year between April and June. Is yours active?",
 cap_mg="IEC deactivate aayal mattoralude PAN-il puthiyathu edukkenda. IEC business PAN-il onnu; orikkalum expire aakilla, pakshe ella varshavum April-June-il online update cheyyanam. Ningalude IEC active aano?")

# NEW, d904 pattern: an auto driver's snake-boat models for a museum shop abroad
duo("ied031", "handicraft_export", "C", "autostand", "ഓട്ടോ ഡ്രൈവറുടെ\nചുണ്ടൻവള്ളം മോഡൽ.\n50 എണ്ണം ഹോളണ്ടിലേക്ക്", [
 ("A","wide","ഷാജീ, ഒരു ഡച്ച് ടൂറിസ്റ്റ് മ്യൂസിയം കടയിലേക്ക് എന്റെ 50 ചുണ്ടൻവള്ളം മോഡൽ ചോദിച്ചു!"),
 ("V","V","സജിയേട്ടാ, ടൂറിസ്റ്റുകൾ ബാഗിൽ കൊണ്ടുപോകുന്ന സുവനീർ അല്ലേ? അയച്ചാ മതി."),
 ("A","A","ഒന്ന് സമ്മാനമായി കൊണ്ടുപോയാൽ ശരി. പക്ഷേ 50 എണ്ണം വിൽക്കാൻ അയക്കുമ്പോൾ?"),
 ("V","V","അത് കയറ്റുമതിയാകുമോ?"),
 ("A","wide","അതെ. കച്ചവടത്തിന് സാധനം അയക്കാൻ ബിസിനസ് PAN-ൽ IEC വേണം. കസ്റ്റംസും ബാങ്കും ചോദിക്കും."),
 ("V","V","വള്ളം ചെറുതാണ്, കയറ്റുമതി വലുതാണ്.")],
 "സുവനീറും വിൽക്കാൻ\nഅയച്ചാൽ കയറ്റുമതി", CTA_EXPORT, theme="new",
 cap_ml="കൈകൊണ്ടുണ്ടാക്കിയ ചുണ്ടൻവള്ളം മോഡലുകൾ വിദേശത്തെ കടയിൽ വിൽക്കാൻ അയക്കുന്നതും കയറ്റുമതിയാണ്. ബിസിനസ് PAN-ൽ IEC വേണം; കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ നാട്ടിലെ ഏത് കരകൗശലം ലോകം കാണണം?",
 cap_en="Shipping handmade snake-boat models to a shop abroad for sale is an export, however small the item. You need an IEC on the business PAN; customs and banks ask for it. Which craft from your town should the world see?",
 cap_mg="Kaikondu undakkiya chundan vallam models videshathe kadayil vilkkan ayakkunnathum export aanu. Business PAN-il IEC venam; customs-um bank-um chodikkum. Ningalude nattile ethu craft lokam kananam?")

# NEW, d904 pattern: Kalaripayattu practice sticks for a school in France
duo("ied032", "first_exporter", "A", "balcony", "\"വെറും വടിയല്ലേ\"\n120 ഒറ്റക്കോൽ\nഫ്രാൻസിലേക്ക്", [
 ("A","wide","വിവേകേ, ഫ്രാൻസിലെ കളരി സ്കൂൾ നിന്റെ 120 ഒറ്റക്കോൽ ചോദിച്ചെന്ന് കേട്ടല്ലോ!"),
 ("V","V","അമ്മൂ, വെറും മരത്തിന്റെ വടിയല്ലേ. കൊറിയറിൽ അങ്ങ് അയക്കും."),
 ("A","A","വടിയായാലും വിൽക്കാൻ അയക്കുന്നത് കയറ്റുമതിയാണ്. പണം വരുമ്പോൾ ബാങ്കും ചോദിക്കും."),
 ("V","V","എന്ത് ചോദിക്കും?"),
 ("A","wide","IEC. DGFT നൽകുന്ന 10 അക്ക കോഡ്, നിന്റെ ബിസിനസ് PAN-ൽ. ഓൺലൈനായി എടുക്കാം."),
 ("V","V","കോൽ എന്റേത്, കോഡ് ആദ്യം.")],
 "മരത്തിന്റെ വടിക്കും\nകയറ്റുമതി കോഡ്", CTA_EXPORT, theme="new",
 cap_ml="കളരി ഒറ്റക്കോൽ പോലുള്ള ലളിതമായ സാധനം വിദേശത്ത് വിൽക്കാൻ അയക്കുന്നതും കയറ്റുമതിയാണ്. DGFT-യുടെ 10 അക്ക IEC ബിസിനസ് PAN-ൽ വേണം; ബാങ്കും കസ്റ്റംസും ചോദിക്കും. നിങ്ങളുടെ ആദ്യ വിദേശ ഓർഡർ വന്നോ?",
 cap_en="Even a simple item like a Kalaripayattu practice stick is an export when you ship it abroad for sale. You need DGFT's 10-digit IEC on the business PAN; banks and customs ask for it. Has your first overseas order come?",
 cap_mg="Kalari ottakkol pole simple sadhanam videshathu vilkkan ayakkunnathum export aanu. DGFT-yude 10 akka IEC business PAN-il venam; bank-um customs-um chodikkum. Ningalude aadya videsha order vanno?")
