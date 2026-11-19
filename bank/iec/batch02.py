# IEC batch 02 (19 Nov, month backlog). Facts only from topics.FACTS_IEC. No fees. People, firms and towns invented.
# Facts only from topics.FACTS_IEC. Never mention fees or customs duty amounts. People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo("ied005", "first_exporter", "A", "courier", "ആദ്യ എക്സ്പോർട്ട്\nപാർസൽ. കസ്റ്റംസ്\nനമ്പർ ചോദിച്ചു", [
 ("A","wide","അരവിന്ദേ, ഖത്തറിലേക്ക് ചക്ക ചിപ്സ് പാർസൽ. കസ്റ്റംസ് ഒരു കോഡ് ചോദിച്ചു."),
 ("V","V","ജയേ, അത് IEC ആണ്. സാധനം കയറ്റി അയക്കാൻ അത് വേണം."),
 ("A","A","ഒരു ചെറിയ ഓർഡറിനും വേണോ?"),
 ("V","V","ബിസിനസ് ആവശ്യത്തിന് കയറ്റുമതിയാണെങ്കിൽ വേണം. സ്വന്തം ഉപയോഗത്തിന് അല്ല."),
 ("A","wide","അപ്പോ അടുത്ത ഓർഡറിന് മുമ്പ് എടുക്കാം."),
 ("V","wide","പാർസൽ റെഡിയാകും മുമ്പ് കോഡ് റെഡിയാക്കൂ.")],
 "ബിസിനസ് കയറ്റുമതിക്ക്\nIEC വേണം", CTA_EXPORT, theme="faq",
 cap_ml="ബിസിനസ് ആവശ്യത്തിന് സാധനം കയറ്റുമതി ചെയ്യാൻ IEC വേണം. കസ്റ്റംസും ബാങ്കും ഇത് ചോദിക്കും. നിങ്ങളുടെ ആദ്യ എക്സ്പോർട്ട് ഓർഡർ വന്നോ?",
 cap_en="Exporting goods for business needs an IEC; customs and banks ask for it. Personal-use shipments do not. Has your first export order arrived yet?",
 cap_mg="Business-nu sadhanam export cheyyaan IEC venam. Customs-um bank-um chodikkum. Ningalude first export order vanno?")

duo("ied006", "importer", "A", "mall", "IEC ഉണ്ട്.\nപക്ഷേ ഡീആക്ടിവേറ്റ്\nആയി", [
 ("A","wide","ജാഫറേ, ചൈനയിൽ നിന്നുള്ള കണ്ടെയ്നർ കസ്റ്റംസിൽ നിർത്തി. IEC ഡീആക്ടിവേറ്റ് എന്ന്."),
 ("V","V","സുമയ്യേ, അത് ഒരിക്കൽ എടുത്താൽ ആജീവനാന്തമല്ലേ?"),
 ("A","A","കാലാവധി തീരില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനിൽ അപ്ഡേറ്റ് ചെയ്യണം."),
 ("V","V","ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും."),
 ("A","wide","അതെ. ഇനി എല്ലാ വർഷവും കലണ്ടറിൽ ഇടണം."),
 ("V","wide","കോഡ് ഉണ്ടായാൽ മാത്രം പോരാ, പുതുക്കണം.")],
 "എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ\nIEC അപ്ഡേറ്റ്", CTA_IEC, theme="faq",
 cap_ml="IEC കാലഹരണപ്പെടില്ല, പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനിൽ അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. ഈ വർഷം നിങ്ങൾ അപ്ഡേറ്റ് ചെയ്തോ?",
 cap_en="An IEC never expires, but it must be updated online every year between April and June or it is deactivated. Did you update yours this year?",
 cap_mg="IEC expire aakilla, pakshe ella varshavum April muthal June vare online update cheyyanam. Illenkil deactivate aakum. Ee varsham update cheytho?")

duo("ied007", "spice_trade", "A", "farm", "രണ്ട് ബിസിനസ്,\nരണ്ട് IEC?\nPAN ഒന്ന്", [
 ("A","wide","ഗോപീ, ഏലക്കായ്ക്കും കുരുമുളകിനും വെവ്വേറെ IEC എടുക്കണോ?"),
 ("V","V","വാസൂ, രണ്ടും ഒരേ PAN-ൽ ആണോ?"),
 ("A","A","അതെ. ഒരേ സ്ഥാപനം."),
 ("V","V","ഒരു PAN-ന് ഒരു IEC മാത്രം. അതിൽ എല്ലാ ഉൽപ്പന്നവും കയറ്റി അയക്കാം."),
 ("A","wide","അപ്പോ രണ്ടാമത്തെ അപേക്ഷ വേണ്ട."),
 ("V","wide","ഒരു PAN, ഒരു കോഡ്, പല സാധനം.")],
 "ഒരു PAN-ന്\nഒരു IEC മാത്രം", CTA_IEC, theme="faq",
 cap_ml="ഒരു PAN-ന് ഒരു IEC മാത്രമാണ്. ആ കോഡിൽ പല ഉൽപ്പന്നങ്ങളും കയറ്റി അയക്കാം. നിങ്ങൾ ഏതൊക്കെ സാധനങ്ങളാണ് കയറ്റുമതി ചെയ്യുന്നത്?",
 cap_en="There is one IEC per PAN, and that single code covers every product you trade. What products are you planning to export?",
 cap_mg="Oru PAN-nu oru IEC maathram. Aa code-il pala products-um export cheyyaam. Ningal enthokke sadhanangal export cheyyunnu?")

duo("ied008", "service_export", "B", "office", "സോഫ്റ്റ്‌വെയർ സർവീസ്\nവിദേശത്തേക്ക്.\nIEC വേണോ?", [
 ("A","wide","രാഹുലേ, അമേരിക്കയിലെ ക്ലയന്റിന് ആപ്പ് ഉണ്ടാക്കുന്നു. IEC വേണോ?"),
 ("V","V","നേഹ, സർവീസിന് കസ്റ്റംസ് ഇല്ലല്ലോ, പിന്നെന്തിന്?"),
 ("A","A","സർവീസ് കയറ്റുമതിക്ക് എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ IEC വേണം."),
 ("V","V","അപ്പോ ആനുകൂല്യം വേണമെങ്കിൽ എടുക്കണം."),
 ("A","wide","അതെ. എല്ലാവർക്കും നിർബന്ധമല്ല, ആനുകൂല്യത്തിന് വേണം."),
 ("V","wide","സാധനം ഇല്ലെങ്കിലും കോഡ് ഉപകാരപ്പെടും.")],
 "സർവീസ് എക്സ്പോർട്ട്\nആനുകൂല്യത്തിന് IEC", CTA_IEC, theme="new",
 cap_ml="സർവീസ് കയറ്റുമതിക്കാർക്ക് എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ IEC വേണം. നിങ്ങൾ വിദേശ ക്ലയന്റുകൾക്ക് സർവീസ് നൽകുന്നുണ്ടോ?",
 cap_en="Service exporters need an IEC to claim export benefits, even with no goods crossing customs. Do you serve clients abroad?",
 cap_mg="Service exporters-nu export benefits claim cheyyaan IEC venam. Ningal videsha clients-nu service kodukkunnundo?")

duo("ied009", "importer", "B", "mobileshop", "സ്വന്തം ഫോൺ\nഗൾഫിൽ നിന്ന്.\nIEC വേണോ?", [
 ("A","wide","ഫഹദേ, ഇക്കാക്ക ദുബായിൽ നിന്ന് എനിക്ക് ഒരു ഫോൺ അയക്കുന്നു. IEC വേണോ?"),
 ("V","V","ഹന്നേ, നീ വിൽക്കാൻ ആണോ, സ്വന്തം ഉപയോഗത്തിനോ?"),
 ("A","A","സ്വന്തം ഉപയോഗത്തിന്."),
 ("V","V","സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണ്ട. കടയിൽ വിൽക്കാനാണെങ്കിൽ വേണം."),
 ("A","wide","അപ്പോ കടയ്ക്ക് സ്റ്റോക്ക് വരുത്തുമ്പോൾ എടുക്കണം."),
 ("V","wide","ആവശ്യം നോക്കി തീരുമാനിക്കൂ.")],
 "സ്വന്തം ഉപയോഗത്തിന് വേണ്ട,\nകച്ചവടത്തിന് വേണം", CTA_IEC, theme="faq",
 cap_ml="സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണ്ട. വിൽക്കാൻ വേണ്ടി ഇറക്കുമതി ചെയ്യുമ്പോൾ വേണം. നിങ്ങൾ കടയ്ക്ക് വേണ്ടി സാധനം വരുത്തുന്നുണ്ടോ?",
 cap_en="Importing for personal use does not need an IEC. Importing stock to sell does. Are you bringing in goods for a shop?",
 cap_mg="Swantham upayogathinulla import-nu IEC venda. Vilkkaan import cheyyumbol venam. Ningal kadakku vendi sadhanam varuthunnundo?")

duo("ied010", "handicraft_export", "B", "handloom", "കൈത്തറി ഓർഡർ\nയൂറോപ്പിൽ നിന്ന്.\nബാങ്ക് നിർത്തി", [
 ("A","wide","കുമാരേട്ടാ, ജർമ്മനിയിൽ നിന്ന് മുണ്ടിന് ഓർഡർ. ബാങ്ക് പണം വാങ്ങാൻ IEC ചോദിച്ചു."),
 ("V","V","ലീലേ, കസ്റ്റംസ് മാത്രമല്ല, ബാങ്കും ചോദിക്കുമോ?"),
 ("A","A","അതെ. കയറ്റുമതി പണം സ്വീകരിക്കുമ്പോൾ ബാങ്കും IEC ചോദിക്കും."),
 ("V","V","ഇത് ബിസിനസ് PAN-ൽ ബന്ധിപ്പിച്ചതാണല്ലോ."),
 ("A","wide","അതെ. പത്ത് അക്ക കോഡ്, DGFT-ൽ നിന്ന്."),
 ("V","wide","ഓർഡർ വരും മുമ്പ് കോഡ് എടുക്കൂ.")],
 "കസ്റ്റംസും ബാങ്കും\nIEC ചോദിക്കും", CTA_EXPORT, theme="crm",
 cap_ml="IEC DGFT നൽകുന്ന പത്ത് അക്ക കോഡാണ്, ബിസിനസ് PAN-ൽ ബന്ധിപ്പിച്ചത്. കസ്റ്റംസും ബാങ്കും ഇത് ചോദിക്കും. നിങ്ങളുടെ ആദ്യ വിദേശ ഓർഡർ ഏത് രാജ്യത്ത് നിന്നാണ്?",
 cap_en="An IEC is a 10-digit code from DGFT linked to the business PAN. Customs and banks both ask for it. Which country did your first overseas order come from?",
 cap_mg="IEC DGFT kodukkunna 10 digit code aanu, business PAN-il link cheythathu. Customs-um bank-um chodikkum. Ningalude first videsha order etha raajyathu ninnu?")

duo("ied011", "first_exporter", "B", "gulfroom", "ഗൾഫിൽ ഇരുന്ന്\nനാട്ടിൽ നിന്ന്\nകയറ്റുമതി", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ കമ്പനി വഴി ഇവിടത്തേക്ക് അച്ചാർ കയറ്റി അയക്കാനാണ് പ്ലാൻ."),
 ("V","V","നസീറേ, IEC ആരുടെ പേരിലാണ് എടുക്കേണ്ടത്?"),
 ("A","A","കയറ്റി അയക്കുന്ന ബിസിനസിന്റെ PAN-ൽ. അതായത് നാട്ടിലെ കമ്പനിയുടെ പേരിൽ."),
 ("V","V","എന്റെ സ്വന്തം PAN അല്ല."),
 ("A","wide","അതെ. ബിസിനസ് ഏതോ അതിന്റെ PAN."),
 ("V","wide","ആര് അയക്കുന്നു, അവരുടെ കോഡ്.")],
 "IEC കയറ്റി അയക്കുന്ന\nബിസിനസിന്റെ PAN-ൽ", CTA_EXPORT, theme="crm",
 cap_ml="IEC എടുക്കേണ്ടത് കയറ്റുമതി ചെയ്യുന്ന ബിസിനസിന്റെ PAN-ലാണ്. ഗൾഫിലിരുന്ന് നാട്ടിലെ കമ്പനി വഴി കയറ്റുമതി ചെയ്യുമ്പോൾ ആ കമ്പനിയുടെ PAN. നിങ്ങൾ ഗൾഫിലേക്ക് എന്താണ് അയക്കാൻ ആലോചിക്കുന്നത്?",
 cap_en="The IEC is taken on the PAN of the business that exports. If a Kerala company ships to the Gulf, it is that company's PAN. What are you planning to send to the Gulf?",
 cap_mg="IEC edukkendathu export cheyyunna business-nte PAN-il. Naattile company vazhi export aanel aa company PAN. Ningal Gulf-ilekku enthu ayakkaan aalochikkunnu?")

duo("ied012", "spice_trade", "B", "fishmarket", "ഉണക്കമീൻ\nഗൾഫിലേക്ക്.\nകോഡ് മാത്രം പോരാ", [
 ("A","wide","ആന്റണീ, ഉണക്കമീൻ ദുബായിലേക്ക് അയക്കാൻ IEC എടുത്തു. ഇനി എല്ലാം റെഡിയല്ലേ?"),
 ("V","V","സുമേ, IEC കയറ്റുമതിക്ക് ആദ്യ പടി മാത്രം."),
 ("A","A","പിന്നെ ഭക്ഷണത്തിന് വേറെ എന്തെങ്കിലും?"),
 ("V","V","ഭക്ഷ്യ ഉൽപ്പന്നങ്ങൾക്ക് മറ്റ് ലൈസൻസുകളും ചോദിക്കാം. അത് വേറെ നോക്കണം."),
 ("A","wide","അപ്പോ ഒരു കോഡ് കൊണ്ട് എല്ലാം തീരില്ല."),
 ("V","wide","IEC വാതിൽ, ബാക്കി അകത്ത്.")],
 "IEC ആദ്യ പടി,\nഅവസാനമല്ല", CTA_EXPORT, theme="new",
 cap_ml="IEC കയറ്റുമതിയുടെ ആദ്യ പടിയാണ്. ഭക്ഷ്യ ഉൽപ്പന്നങ്ങൾക്ക് മറ്റ് ലൈസൻസുകളും ആവശ്യപ്പെടാം. നിങ്ങൾ എന്ത് ഉൽപ്പന്നമാണ് കയറ്റി അയക്കുന്നത്?",
 cap_en="An IEC is only the first step for exporters; food products may need other licences too. What product are you exporting?",
 cap_mg="IEC export-nte aadya padi maathram. Food products-nu vere licence-um chodikkaam. Ningal enthu product export cheyyunnu?")

duo("ied013", "importer", "A", "garage", "മെഷീൻ ഇറക്കുമതി.\nഏജന്റിന്റെ\nIEC ഉപയോഗിച്ചു", [
 ("A","wide","ജിതിനേ, ജപ്പാനിൽ നിന്നുള്ള മെഷീൻ ഏജന്റിന്റെ IEC-ൽ വരുത്തി. പ്രശ്നമുണ്ടോ?"),
 ("V","V","ഐശ്വര്യേ, രേഖയിൽ ഇറക്കുമതിക്കാരൻ ആര് എന്ന് വരും?"),
 ("A","A","ഏജന്റിന്റെ പേര്. നമ്മുടെ ബിസിനസിന്റേതല്ല."),
 ("V","V","അപ്പോ നമ്മുടെ ബിസിനസിന്റെ രേഖയിൽ ഇറക്കുമതി ഇല്ല. ഇനി സ്വന്തം IEC എടുക്കൂ."),
 ("A","wide","അതെ. ബിസിനസ് PAN-ൽ സ്വന്തം കോഡ്."),
 ("V","wide","കടം വാങ്ങിയ കോഡിൽ കച്ചവടം വേണ്ട.")],
 "സ്വന്തം ബിസിനസിന്\nസ്വന്തം IEC", CTA_IEC, theme="crm",
 cap_ml="മറ്റൊരാളുടെ IEC ഉപയോഗിച്ച് ഇറക്കുമതി ചെയ്താൽ രേഖയിൽ അവരാണ് ഇറക്കുമതിക്കാർ. ബിസിനസ് PAN-ൽ സ്വന്തം IEC എടുക്കൂ. നിങ്ങൾ ആരുടെ IEC-ലാണ് ഇപ്പോൾ ഇറക്കുമതി ചെയ്യുന്നത്?",
 cap_en="Importing on someone else's IEC makes them the importer on record. Take your own IEC on your business PAN. Whose IEC are your imports on now?",
 cap_mg="Vere aalude IEC-il import cheythaal rekhayil avaraanu importer. Business PAN-il swantham IEC edukku. Ningal ippol aarude IEC-il import cheyyunnu?")

duo("ied014", "first_exporter", "A", "akshaya", "IEC അപേക്ഷ\nഎവിടെ കൊടുക്കും?\nഓൺലൈൻ", [
 ("A","wide","രമേശേ, IEC-ക്ക് ഏത് ഓഫീസിൽ പോകണം?"),
 ("V","V","സുധേ, DGFT-യുടെ വെബ്സൈറ്റിൽ ഓൺലൈനായി അപേക്ഷിക്കാം."),
 ("A","A","എന്ത് രേഖ വേണം?"),
 ("V","V","ബിസിനസിന്റെ PAN ആണ് അടിസ്ഥാനം. ബാക്കി വിവരങ്ങളും ഓൺലൈനിൽ."),
 ("A","wide","അപ്പോ യാത്ര വേണ്ട."),
 ("V","wide","ഓഫീസ് കയറേണ്ട, വെബ്സൈറ്റ് മതി.")],
 "IEC DGFT വെബ്സൈറ്റിൽ\nഓൺലൈനായി", CTA_IEC, theme="faq",
 cap_ml="IEC DGFT-യുടെ വെബ്സൈറ്റിൽ ഓൺലൈനായി അപേക്ഷിക്കാം, ബിസിനസിന്റെ PAN ആണ് അടിസ്ഥാനം. നിങ്ങൾ IEC-ക്ക് അപേക്ഷിച്ചോ?",
 cap_en="You apply for an IEC online on the DGFT website, based on the business PAN. No office visit is needed. Have you applied yet?",
 cap_mg="IEC DGFT website-il online aayi apekshikkaam, business PAN aanu adisthaanam. Ningal IEC-kku apply cheytho?")
