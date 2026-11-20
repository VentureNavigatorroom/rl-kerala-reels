# IEC batch 05 (20 Nov, month backlog). Facts only from topics.FACTS_IEC. No fees. People, firms and towns invented.
# crm scripts use STORY_THEMES #7, C12, C13 and the "too busy" pattern with changed sector, place and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

# CRM C13 (founder abroad supplying Kerala): a sister in Germany, a baby-care shop at home
duo("ied033", "importer", "A", "pharmacy", "ജർമ്മനിയിൽ നിന്ന്\nബേബി ലോഷൻ കാർട്ടൺ.\nകോഡ് ആരുടെ പേരിൽ?", [
 ("A","wide","പ്രവീണേ, ജർമ്മനിയിലുള്ള എന്റെ സഹോദരി എല്ലാ മാസവും ബേബി ലോഷൻ കാർട്ടൺ അയക്കും. നമ്മുടെ കടയിൽ വിൽക്കാൻ."),
 ("V","V","സിനീ, സഹോദരിക്ക് അവിടെ ബിസിനസ് ഉണ്ടല്ലോ. അവരുടെ പേരിൽ മതിയോ?"),
 ("A","A","ഇവിടെ ഇറക്കുമതി ചെയ്യുന്നത് നമ്മുടെ കടയല്ലേ?"),
 ("V","wide","അതേ. വിൽക്കാനുള്ള ഇറക്കുമതിക്ക് IEC വേണം. ഇറക്കുമതി ചെയ്യുന്ന ബിസിനസിന്റെ PAN-ൽ, DGFT-യിൽ നിന്ന്."),
 ("A","A","അപ്പോ കസ്റ്റംസ് ചോദിക്കുന്നത് നമ്മുടെ കോഡ്."),
 ("V","wide","അയക്കുന്നത് സഹോദരി, കോഡ് നമ്മുടേത്.")],
 "അയക്കുന്നത് സഹോദരി,\nകോഡ് നമ്മുടേത്", CTA_IEC, theme="crm",
 cap_ml="വിദേശത്തുള്ള ബന്ധു സാധനം അയച്ചാലും നാട്ടിൽ വിൽക്കാൻ ഇറക്കുമതി ചെയ്യുന്നത് നിങ്ങളുടെ ബിസിനസ് ആണെങ്കിൽ IEC നിങ്ങളുടെ ബിസിനസ് PAN-ൽ വേണം. കസ്റ്റംസും ബാങ്കും അത് ചോദിക്കും. നിങ്ങൾക്ക് വിദേശത്ത് നിന്ന് സാധനം അയക്കുന്ന ആരെങ്കിലും ഉണ്ടോ?",
 cap_en="A sister abroad ships baby-care cartons for the family shop to sell. The importer is the shop, so the IEC must be on the shop's business PAN; customs and banks will ask for it. Does someone abroad send you stock?",
 cap_mg="Videshathulla relative saadhanam ayachaalum naattil vilkkaan import cheyyunnathu ningalude business aanenkil IEC ningalude business PAN-il venam. Customs-um bank-um chodikkum. Ningalkku videshathu ninnu stock ayakkunna aarenkilum undo?")

# CRM C12 (family trade on both sides): "use my Sharjah licence"
duo("ied034", "first_exporter", "A", "thattukada", "\"ഷാർജയിൽ എന്റെ\nലൈസൻസ് ഉണ്ട്.\nഅവിടെ IEC വേണ്ട\"", [
 ("A","wide","ബിജൂ, നിന്റെ ഏട്ടന്റെ ഷാർജയിലെ സൂപ്പർമാർക്കറ്റിലേക്ക് നമ്മുടെ ബനാന ചിപ്സ് പോകുന്നു. ഏട്ടന് അവിടെ ലൈസൻസ് ഉണ്ട്."),
 ("V","V","സിജോ, അപ്പോ നമുക്ക് ഒന്നും വേണ്ടല്ലോ. ഏട്ടന്റെ ലൈസൻസ് മതി."),
 ("A","A","പക്ഷേ ഇവിടെ നിന്ന് കയറ്റി അയക്കുന്നത് നമ്മളല്ലേ?"),
 ("V","wide","അതാണ് കാര്യം. ഇന്ത്യയിൽ നിന്ന് സാധനം കയറ്റുമതി ചെയ്യാൻ നമ്മുടെ ബിസിനസ് PAN-ൽ IEC വേണം. കസ്റ്റംസും ബാങ്കും ഇവിടെ ചോദിക്കും."),
 ("A","A","ഏട്ടന്റെ ലൈസൻസ് ഷാർജയിൽ, നമ്മുടെ കോഡ് ഇവിടെ."),
 ("V","wide","അവിടത്തെ പേപ്പർ അവിടെ, ഇവിടത്തെ പേപ്പർ ഇവിടെ.")],
 "അവിടത്തെ പേപ്പർ അവിടെ,\nഇവിടത്തേത് ഇവിടെ", CTA_EXPORT, theme="crm",
 cap_ml="ഗൾഫിലെ ബന്ധുവിന് അവിടെ ട്രേഡ് ലൈസൻസ് ഉണ്ടെങ്കിലും ഇന്ത്യയിൽ നിന്ന് കയറ്റുമതി ചെയ്യുന്ന നിങ്ങളുടെ ബിസിനസിന് IEC വേണം, നിങ്ങളുടെ PAN-ൽ. കസ്റ്റംസും ബാങ്കും ഇവിടെ ചോദിക്കും. കുടുംബത്തിൽ ആരെങ്കിലും ഗൾഫിൽ കച്ചവടം ചെയ്യുന്നുണ്ടോ?",
 cap_en="A brother's trade licence in Sharjah does not cover the exporter in Kerala. The business shipping goods out of India needs its own IEC on its PAN, and customs and banks here will ask for it. Does anyone in your family trade in the Gulf?",
 cap_mg="Gulf-ile relative-inu avide trade licence undenkilum India-yil ninnu export cheyyunna ningalude business-inu IEC venam, ningalude PAN-il. Customs-um bank-um ivide chodikkum. Family-il aarenkilum Gulf-il kachavadam cheyyunnundo?")

# FAQ: sold to an exporter for 20 years, now going direct
duo("ied035", "first_exporter", "A", "veranda", "20 വർഷം കയർ മാറ്റ്\nഎക്സ്പോർട്ടർക്ക് വിറ്റു.\nഇനി നേരിട്ട്", [
 ("A","wide","ബാലേട്ടാ, 20 വർഷമായി നമ്മുടെ കയർ മാറ്റ് ആലപ്പുഴയിലെ എക്സ്പോർട്ടർക്കാ കൊടുത്തത്. അന്ന് നമുക്ക് IEC വേണ്ടിവന്നില്ലല്ലോ."),
 ("V","V","ശാന്തേ, അന്ന് കയറ്റുമതി അവരുടെ പേരിലായിരുന്നു. നമ്മൾ നാട്ടിൽ വിറ്റു, അത്രേ."),
 ("A","A","ഇപ്പോ ഓസ്ട്രേലിയയിലെ കട നേരിട്ട് ഓർഡർ തരുന്നു. അതേ മാറ്റ്."),
 ("V","wide","മാറ്റ് അതേ, പക്ഷേ കയറ്റുമതിക്കാരൻ ഇനി നമ്മൾ. നമ്മുടെ ബിസിനസ് PAN-ൽ IEC വേണം."),
 ("A","A","അപ്പോ വാങ്ങുന്നവൻ മാറിയപ്പോൾ പേപ്പറും മാറി."),
 ("V","wide","നേരിട്ട് അയച്ചാൽ, കോഡും നേരിട്ട് വേണം.")],
 "നേരിട്ട് അയച്ചാൽ\nകോഡും നേരിട്ട്", CTA_EXPORT, theme="faq",
 cap_ml="നാട്ടിലെ എക്സ്പോർട്ടർക്ക് വിൽക്കുമ്പോൾ കയറ്റുമതി അവരുടെ പേരിലാണ്. നിങ്ങൾ തന്നെ വിദേശത്തേക്ക് നേരിട്ട് അയക്കാൻ തുടങ്ങുമ്പോൾ നിങ്ങളുടെ ബിസിനസ് PAN-ൽ IEC വേണം. നിങ്ങൾ ഇപ്പോൾ എക്സ്പോർട്ടർ വഴിയാണോ നേരിട്ടാണോ?",
 cap_en="Selling to a local exporter means the export is in their name. The day you ship abroad yourself, your business needs its own IEC on its PAN. Do you sell through an exporter or direct?",
 cap_mg="Naattile exporter-nu vilkkumbol export avarude perilaanu. Ningal thanne videshathekku nerittu ayakkaan thudangumbol ningalude business PAN-il IEC venam. Ningal ippol exporter vazhiyaano nerittaano?")

# CRM ("too busy to look"): the accountant who did the yearly update has left
duo("ied036", "importer", "B", "rooftop", "അക്കൗണ്ടന്റ് പോയി.\nIEC അപ്ഡേറ്റ്\nആര് ഓർക്കും?", [
 ("A","wide","ശ്യാമേ, കശുവണ്ടി ഇറക്കുമതിയുടെ എല്ലാ പേപ്പറും നോക്കിയിരുന്ന അക്കൗണ്ടന്റ് മാർച്ചിൽ ജോലി വിട്ടു."),
 ("V","V","ആര്യേ, IEC അപ്ഡേറ്റ് അയാളാ എല്ലാ വർഷവും ചെയ്തിരുന്നത്. ഇത്തവണ ആര്?"),
 ("A","A","കോഡ് ഒരിക്കലും എക്സ്പയർ ആകില്ലല്ലോ. പിന്നെന്താ?"),
 ("V","wide","എക്സ്പയർ ആകില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും."),
 ("A","A","അപ്പോ അത് ആളുടെ ഓർമ്മയിലല്ല, കമ്പനിയുടെ കലണ്ടറിൽ വേണം."),
 ("V","wide","ആള് പോകും, ഏപ്രിൽ വരും.")],
 "ആള് പോകും,\nഏപ്രിൽ വരും", CTA_IEC, theme="crm",
 cap_ml="IEC അപ്ഡേറ്റ് ഒരാളുടെ ഓർമ്മയിൽ മാത്രം വെക്കരുത്. കോഡ് എക്സ്പയർ ആകില്ല, പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. നിങ്ങളുടെ കമ്പനിയിൽ ഇത് ആരുടെ ജോലിയാണ്?",
 cap_en="Do not leave the IEC update to one person's memory. The code never expires, but it is deactivated if it is not updated online every year between April and June. Whose job is this in your company?",
 cap_mg="IEC update oraalude ormayil maathram vekkaruthu. Code expire aakilla, pakshe ella varshavum April muthal June vare online update cheythillenkil deactivate aakum. Ningalude company-il ithu aarude joliyaanu?")

# FAQ: a video editor paid by foreign creators
duo("ied037", "service_export", "A", "canteen", "അമേരിക്കൻ യൂട്യൂബർക്ക്\nവീഡിയോ എഡിറ്റ്.\n\"ഇത് കയറ്റുമതിയോ?\"", [
 ("A","wide","അമലേ, എനിക്ക് അമേരിക്കയിലെ മൂന്ന് യൂട്യൂബർമാർക്ക് വീഡിയോ എഡിറ്റിംഗ് ഉണ്ട്. പെട്ടി ഒന്നും അയക്കുന്നില്ല."),
 ("V","V","ആതിരേ, പണം വിദേശത്ത് നിന്ന് വരുന്നു. അത് സർവീസ് കയറ്റുമതിയാ."),
 ("A","A","സാധനം ഇല്ലാത്തതിന് എന്തിനാ IEC? കസ്റ്റംസ് ഒന്നുമില്ലല്ലോ."),
 ("V","wide","കസ്റ്റംസ് ഇല്ല. പക്ഷേ സർവീസ് കയറ്റുമതിയുടെ ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ IEC വേണം."),
 ("A","A","അപ്പോ പെട്ടിയില്ലെങ്കിലും കോഡ് ഉപകാരം."),
 ("V","wide","ഫയൽ പോകുന്നത് ക്ലൗഡിൽ, ആനുകൂല്യം വരുന്നത് കോഡിൽ.")],
 "ഫയൽ ക്ലൗഡിൽ,\nആനുകൂല്യം കോഡിൽ", CTA_IEC, theme="faq",
 cap_ml="വിദേശ ക്ലയന്റുകൾക്ക് വീഡിയോ എഡിറ്റിംഗ് പോലുള്ള സർവീസ് ചെയ്യുന്നതും സർവീസ് കയറ്റുമതിയാണ്. സാധനം ഇല്ലാത്തതിനാൽ കസ്റ്റംസ് ഇല്ല, പക്ഷേ എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ IEC വേണം. നിങ്ങൾക്ക് വിദേശ ക്ലയന്റുകൾ ഉണ്ടോ?",
 cap_en="Editing videos for foreign creators is a service export. No goods means no customs, but service exporters need an IEC to claim export benefits. Do you have clients abroad?",
 cap_mg="Videsha clients-nu video editing pole service cheyyunnathum service export aanu. Saadhanam illaathathinaal customs illa, pakshe export benefits claim cheyyaan IEC venam. Ningalkku foreign clients undo?")

# FAQ: a second branch in another city
duo("ied038", "spice_trade", "A", "shop", "ബാംഗ്ലൂരിൽ രണ്ടാം\nബ്രാഞ്ച്. \"അവിടെയും\nപുതിയ IEC\"", [
 ("A","wide","സുരേഷേ, നമ്മുടെ മസാല കമ്പനിക്ക് ബാംഗ്ലൂരിൽ ബ്രാഞ്ച് തുടങ്ങുന്നു. അവിടെ നിന്നും കയറ്റുമതി ഉണ്ടാകും."),
 ("V","V","ബിനുവേട്ടാ, അപ്പോ ബാംഗ്ലൂരിന് വേറെ ഒരു IEC എടുക്കണം, അല്ലേ?"),
 ("A","A","കമ്പനി ഒന്ന് തന്നെയല്ലേ? PAN-ഉം ഒന്ന്."),
 ("V","wide","എങ്കിൽ ഒരു PAN-ന് ഒരു IEC മാത്രം. പുതിയ കോഡ് അല്ല, ബ്രാഞ്ച് അതേ കമ്പനിയുടെ ഭാഗം."),
 ("A","A","അപ്പോ നഗരം രണ്ട്, കോഡ് ഒന്ന്."),
 ("V","wide","കട എത്ര തുറന്നാലും, PAN ഒന്നെങ്കിൽ കോഡും ഒന്ന്.")],
 "കട എത്ര തുറന്നാലും\nPAN ഒന്നെങ്കിൽ കോഡ് ഒന്ന്", CTA_IEC, theme="faq",
 cap_ml="പുതിയ നഗരത്തിൽ ബ്രാഞ്ച് തുടങ്ങുമ്പോൾ പുതിയ IEC എടുക്കേണ്ടതില്ല. IEC ബിസിനസിന്റെ PAN-ഉമായി ബന്ധിപ്പിച്ചതാണ്, ഒരു PAN-ന് ഒരു IEC മാത്രം. നിങ്ങളുടെ ബിസിനസിന് എത്ര ബ്രാഞ്ച് ഉണ്ട്?",
 cap_en="Opening a branch in another city does not mean a new IEC. The IEC is linked to the business PAN, and there is only one per PAN. How many branches does your business have?",
 cap_mg="Puthiya nagarathil branch thudangumbol puthiya IEC edukkendathilla. IEC business PAN-umaayi link cheythathaanu, oru PAN-nu oru IEC maathram. Ningalude business-inu ethra branch undu?")

# CRM #7 (a women's brand wants to export): the resort says it will handle customs
duo("ied039", "handicraft_export", "A", "hotellobby", "മാലിദ്വീപിലെ റിസോർട്ട്:\n\"കസ്റ്റംസ് ഞങ്ങൾ\nനോക്കിക്കോളാം\"", [
 ("A","wide","ജെയ്സണേ, എന്റെ ഹാൻഡ്മേഡ് സോപ്പിന് മാലിദ്വീപിലെ റിസോർട്ടിൽ നിന്ന് 2000 എണ്ണത്തിന്റെ ഓർഡർ. കസ്റ്റംസ് അവർ നോക്കുമെന്ന്."),
 ("V","V","നീതൂ, അവർ നോക്കുന്നത് അവിടത്തെ കസ്റ്റംസ്. ഇവിടെ നിന്ന് കയറ്റി അയക്കുന്നത് ആരാ?"),
 ("A","A","ഞാൻ. എന്റെ ബ്രാൻഡ്, എന്റെ പെട്ടി."),
 ("V","wide","എങ്കിൽ ഇവിടത്തെ കസ്റ്റംസും ബാങ്കും നിന്റെ IEC ചോദിക്കും. ബിസിനസ് PAN-ൽ, DGFT-യിൽ ഓൺലൈനായി."),
 ("A","A","അപ്പോ അവരുടെ വാക്ക് അവരുടെ തുറമുഖത്ത് മാത്രം."),
 ("V","wide","അവിടെ അവരുടെ കസ്റ്റംസ്, ഇവിടെ നിന്റെ കോഡ്.")],
 "അവിടെ അവരുടെ കസ്റ്റംസ്,\nഇവിടെ നിന്റെ കോഡ്", CTA_EXPORT, theme="crm",
 cap_ml="വിദേശത്തെ ബയർ അവിടത്തെ കസ്റ്റംസ് നോക്കിക്കോളാം എന്ന് പറഞ്ഞാലും ഇന്ത്യയിൽ നിന്ന് അയക്കുന്ന നിങ്ങളുടെ ബിസിനസിന് IEC വേണം. ഇവിടത്തെ കസ്റ്റംസും ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ ഉൽപ്പന്നത്തിന് വിദേശ ഓർഡർ വന്നിട്ടുണ്ടോ?",
 cap_en="A resort abroad says it will handle customs, but that is customs at their end. The business shipping from India still needs its own IEC, and customs and banks here will ask for it. Has your product had a foreign order yet?",
 cap_mg="Videshathe buyer avide customs nokkikkolaam ennu paranjaalum India-yil ninnu ayakkunna ningalude business-inu IEC venam. Ivide customs-um bank-um chodikkum. Ningalude product-inu foreign order vannittundo?")

# FAQ: "it's for our own outlets, not to sell"
duo("ied040", "importer", "A", "juiceshop", "6 ജ്യൂസ് കടയ്ക്ക്\n40 ബ്ലെൻഡർ.\n\"വിൽക്കാനല്ലല്ലോ\"", [
 ("A","wide","നൗഷാദേ, നമ്മുടെ ആറ് കടയ്ക്കും വേണ്ടി 40 ബ്ലെൻഡർ തായ്‌ലൻഡിൽ നിന്ന് ഇറക്കുമതി ചെയ്യുന്നു."),
 ("V","V","റസിയാ, വിൽക്കാനല്ലല്ലോ, നമ്മൾ തന്നെ ഉപയോഗിക്കാനല്ലേ? സ്വന്തം ഉപയോഗം. IEC വേണ്ട."),
 ("A","A","സ്വന്തം ഉപയോഗം എന്ന് പറഞ്ഞാൽ വീട്ടിലെ ഉപയോഗമല്ലേ?"),
 ("V","wide","ശരിയാ. വീട്ടിലെ ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് മാത്രമാണ് IEC വേണ്ടാത്തത്. കടയിലെ മെഷീൻ ബിസിനസ് ഇറക്കുമതി, IEC വേണം."),
 ("A","A","അപ്പോ ജ്യൂസ് വിൽക്കുന്ന മെഷീനും ബിസിനസിന്റേത്."),
 ("V","wide","അടുക്കളയിലേതാണെങ്കിൽ വേണ്ട, കൗണ്ടറിലേതാണെങ്കിൽ വേണം.")],
 "അടുക്കളയിലേതിന് വേണ്ട,\nകൗണ്ടറിലേതിന് വേണം", CTA_IEC, theme="faq",
 cap_ml="സ്വന്തം കടകളിൽ ഉപയോഗിക്കാൻ മെഷീൻ ഇറക്കുമതി ചെയ്യുന്നത് സ്വകാര്യ ഉപയോഗമല്ല, ബിസിനസ് ഇറക്കുമതിയാണ്. വ്യക്തിപരമായ ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് മാത്രമാണ് IEC വേണ്ടാത്തത്. നിങ്ങളുടെ ബിസിനസിന് വിദേശ മെഷീൻ ഉണ്ടോ?",
 cap_en="Importing machines for your own outlets is still a business import, not personal use. Only imports for personal use skip the IEC. Does your business run on imported machines?",
 cap_mg="Swantham kadakalil upayogikkaan machine import cheyyunnathu personal use alla, business import aanu. Personal use import-nu maathramaanu IEC vendaathathu. Ningalude business-inu foreign machine undo?")

# New, d904 pattern: a festival-umbrella maker importing silk
duo("ied041", "importer", "B", "petrolpump", "പൂരക്കുടയ്ക്ക്\nചൈനീസ് സിൽക്ക്.\n\"തുണിയല്ലേ, കോഡ് എന്തിന്?\"", [
 ("A","wide","ഷിബൂ, നിന്റെ കുടമാറ്റം കുടകൾക്ക് ഈ വർഷം സിൽക്ക് നേരിട്ട് ഇറക്കുമതി ചെയ്യുകയാണോ?"),
 ("V","V","അതേ സന്തോഷേട്ടാ. 30 റോൾ. വെറും തുണിയല്ലേ, ഒരു കോഡും വേണ്ടല്ലോ."),
 ("A","A","തുണിയായാലും കുടയാക്കി ക്ഷേത്രങ്ങൾക്ക് വിൽക്കുകയല്ലേ?"),
 ("V","wide","അതെ. ബിസിനസിനുള്ള ഇറക്കുമതിക്ക് IEC വേണം. കസ്റ്റംസ് ആദ്യം ചോദിക്കുന്നത് അതാ."),
 ("A","A","അപ്പോ പൂരത്തിന് മുമ്പ് കോഡ് റെഡി."),
 ("V","wide","കുട ആകാശത്ത് ഉയരാൻ, കോഡ് ആദ്യം കടലാസിൽ.")],
 "കുട ആകാശത്ത് ഉയരാൻ,\nകോഡ് ആദ്യം കടലാസിൽ", CTA_IEC, theme="new",
 cap_ml="ഉത്സവ കുടകൾക്കുള്ള സിൽക്ക് പോലെ അസംസ്കൃത വസ്തുവായാലും ബിസിനസിന് വേണ്ടി ഇറക്കുമതി ചെയ്യുമ്പോൾ IEC വേണം. കസ്റ്റംസ് ചോദിക്കും, ബാങ്കും ചോദിക്കും. നിങ്ങളുടെ ഉൽപ്പന്നത്തിനുള്ള എന്തെങ്കിലും വിദേശത്ത് നിന്ന് വരുന്നുണ്ടോ?",
 cap_en="Even raw material, like silk for temple-festival umbrellas, needs an IEC when it is imported for a business. Customs and banks will ask for it. Does anything in your product come from abroad?",
 cap_mg="Utsava kudakalkkulla silk pole raw material aayaalum business-inu vendi import cheyyumbol IEC venam. Customs-um bank-um chodikkum. Ningalude product-inulla enthenkilum videshathu ninnu varunnundo?")

# New, d904 pattern: a tattoo artist importing ink for his studio
duo("ied042", "importer", "B", "salon", "ടാറ്റൂ ഇങ്ക്\nഅമേരിക്കയിൽ നിന്ന്.\n\"സ്റ്റുഡിയോയിൽ മാത്രം\"", [
 ("A","wide","വിനീതേ, നിന്റെ ടാറ്റൂ സ്റ്റുഡിയോയ്ക്ക് ഇങ്ക് അമേരിക്കയിൽ നിന്ന് വരുത്തുന്നുണ്ടല്ലോ. IEC ഉണ്ടോ?"),
 ("V","V","സോണിയേ, ഇങ്ക് ഞാൻ വിൽക്കുന്നില്ല. സ്റ്റുഡിയോയിൽ മാത്രം. സ്വന്തം ഉപയോഗം."),
 ("A","A","പക്ഷേ ആ ഇങ്ക് കൊണ്ടല്ലേ ഓരോ കസ്റ്റമറിൽ നിന്നും പണം വാങ്ങുന്നത്?"),
 ("V","wide","ശരി. അത് ബിസിനസ് ഉപയോഗമാ. വ്യക്തിപരമായ ഉപയോഗത്തിന് മാത്രമേ IEC ഇല്ലാതെ പറ്റൂ."),
 ("A","A","അപ്പോ സ്റ്റുഡിയോയുടെ PAN-ൽ ഒരു കോഡ്."),
 ("V","wide","തൊലിയിൽ ഇടുന്നത് കലയാ, കസ്റ്റംസിൽ അത് കച്ചവടം.")],
 "തൊലിയിൽ കല,\nകസ്റ്റംസിൽ കച്ചവടം", CTA_IEC, theme="new",
 cap_ml="വിൽക്കുന്നില്ലെങ്കിലും സ്റ്റുഡിയോയിൽ കസ്റ്റമർക്ക് വേണ്ടി ഉപയോഗിക്കുന്ന ഇറക്കുമതി ബിസിനസ് ഉപയോഗമാണ്. വ്യക്തിപരമായ ഉപയോഗത്തിന് മാത്രമാണ് IEC വേണ്ടാത്തത്; ബിസിനസ് PAN-ൽ ഒരു IEC മതി. നിങ്ങളുടെ ജോലിക്കുള്ള സാധനം വിദേശത്ത് നിന്നാണോ?",
 cap_en="Ink a tattoo studio uses on paying customers is a business import, even if it is never resold. Only personal-use imports skip the IEC; one IEC on the business PAN covers it. Do your work supplies come from abroad?",
 cap_mg="Vilkkunnillenkilum studio-yil customer-nu vendi upayogikkunna import business use aanu. Personal use-nu maathramaanu IEC vendaathathu; business PAN-il oru IEC mathi. Ningalude jolikkulla saadhanam videshathu ninnaano?")
