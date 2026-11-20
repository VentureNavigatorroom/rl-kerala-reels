# NDA batch 05 (20 Nov, month backlog). Facts only from topics.FACTS_NDA. No fees, never promise a court outcome.
# People, firms, towns and numbers invented; CRM situations (C13/C15, C10, #25, #8) only in anonymised form.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

# crm C13 + C15: founder abroad, Kerala freelancer, nothing in writing about remedies
duo("ndd026", "freelancer_nda", "A", "gulfoffice", "ദോഹയിൽ നിന്ന്\nകോഡ് മുഴുവൻ അയച്ചു.\nഡെവലപ്പർ സ്വന്തം ആപ്പ് ഇറക്കി", [
 ("A","wide","ആസിഫ്, തൃശൂരിലെ ഫ്രീലാൻസർക്ക് ട്യൂഷൻ ആപ്പിന്റെ കോഡ് മുഴുവൻ അയച്ചു. ഇന്ന് അവന്റെ പേരിൽ അതേ ആപ്പ്!"),
 ("V","V","ഷഹാന, NDA ഒപ്പിട്ടിരുന്നോ? ലംഘിച്ചാൽ എന്ത് എന്ന് അതിൽ ഉണ്ടോ?"),
 ("A","A","ഒപ്പിട്ടു. പക്ഷേ 'രഹസ്യം സൂക്ഷിക്കണം' എന്ന ഒരു വരി മാത്രം."),
 ("V","V","എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം: ഇതെല്ലാം എഴുതണം. സ്റ്റാമ്പും വേണം."),
 ("A","wide","അടുത്ത ഡെവലപ്പർക്ക് കോഡ് പോകുന്നത് അത് കഴിഞ്ഞ് മാത്രം."),
 ("V","wide","ദൂരം കൂടുമ്പോൾ കരാർ കനക്കണം.")],
 "ഒറ്റ വരി NDA\nഒന്നും കാക്കില്ല", CTA_NDA, theme="crm",
 cap_ml="ഗൾഫിൽ ഇരുന്ന് നാട്ടിലെ ഫ്രീലാൻസർക്ക് കോഡ് അയക്കുന്നുണ്ടോ? NDA-യിൽ എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം എന്നിവ എഴുതണം; സംസ്ഥാന നിയമപ്രകാരം സ്റ്റാമ്പും വേണം. നിങ്ങൾ ഇപ്പോൾ എവിടെ നിന്നാണ്?",
 cap_en="Sending code from the Gulf to a freelancer in Kerala? Your NDA must define what is confidential, for how long, and remedies such as an injunction, and be stamped under the state's stamp law. Where are you based right now?",
 cap_mg="Gulf-il irunnu naattile freelancer-kku code ayakkunnundo? NDA-yil enthaanu rahasyam, ethra kaalam, langhichaal injunction pole ulla remedy ezhuthanam; state stamp law prakaaram stamp-um venam. Ningal ippol evide ninnaanu?")

# crm C10 (family formula going to stores): contract manufacturer, one-way NDA
duo("ndd027", "vendor_supplier", "B", "veranda", "അമ്മൂമ്മയുടെ എണ്ണക്കൂട്ട്.\nഫാക്ടറി ചോദിച്ചു:\n\"മുഴുവൻ ലിസ്റ്റ് തരൂ\"", [
 ("A","wide","ബാലേട്ടാ, കാച്ചെണ്ണ കടകളിലേക്ക് എത്തിക്കാൻ ഒരു ഫാക്ടറി തയ്യാർ. പക്ഷേ മുഴുവൻ കൂട്ടും ചോദിക്കുന്നു."),
 ("V","V","ശാന്തേ, മുപ്പത് കൊല്ലത്തെ കൂട്ടാ. അത് വാട്സാപ്പിൽ അയക്കാൻ പോകുവാണോ?"),
 ("A","A","അവർ പറയുന്നു, 'ഞങ്ങളെ വിശ്വസിച്ചാൽ മതി' എന്ന്."),
 ("V","V","രഹസ്യം നമ്മൾ മാത്രം കൊടുക്കുന്നതുകൊണ്ട് വൺ-വേ NDA മതി. കൂട്ട്, അളവ്, പാചകരീതി: ഇവ രഹസ്യമെന്ന് പേരെടുത്ത് എഴുതണം."),
 ("A","wide","ഒപ്പും സ്റ്റാമ്പും കഴിഞ്ഞിട്ടേ ലിസ്റ്റ് പോകൂ."),
 ("V","wide","വിശ്വാസം വീട്ടിൽ, ബിസിനസിൽ കരാർ.")],
 "കൂട്ട് കൊടുക്കും മുമ്പ്\nവൺ-വേ NDA", CTA_SECRET, theme="crm",
 cap_ml="കുടുംബത്തിന്റെ പഴയ കൂട്ട് ഒരു ഫാക്ടറിക്ക് നിർമ്മിക്കാൻ കൊടുക്കുമ്പോൾ രഹസ്യം ഒരു വശത്ത് നിന്ന് മാത്രം പോകുന്നു, അതിനാൽ വൺ-വേ NDA മതി. എന്താണ് രഹസ്യം എന്ന് പേരെടുത്ത് എഴുതണം. നിങ്ങളുടെ വീട്ടിൽ ഒരു രഹസ്യ കൂട്ട് ഉണ്ടോ?",
 cap_en="Handing a family formula to a contract manufacturer? Only you are sharing secrets, so a one-way NDA fits. Name exactly what is confidential: ingredients, ratios, method. Does your family have a secret recipe?",
 cap_mg="Family-ude pazhaya koottu factory-kku kodukkumpol rahasyam oru bhaagathu ninnu maathram pokunnu, athukondu one-way NDA mathi. Enthaanu rahasyam ennu peredutthu ezhuthanam. Ningalude veettil oru rahasya koottu undo?")

# crm #25 + C14: student founder at a college demo day, panel won't sign
duo("ndd028", "founder_pitching", "C", "classroom", "\"ജഡ്ജസ് NDA ഒപ്പിടാതെ\nഞാൻ ഡെമോ കാണിക്കില്ല\"", [
 ("A","wide","ആദർശ്, നാളെ ഡെമോ ഡേ ആണ്. ജഡ്ജസിനോട് NDA ഒപ്പിടാൻ പറഞ്ഞെന്ന് കേട്ടല്ലോ?"),
 ("V","V","നിമ്മി ടീച്ചറേ, എന്റെ റോബോട്ടിക്സ് കിറ്റിന്റെ സർക്യൂട്ട് ആരെങ്കിലും കോപ്പി ചെയ്താലോ?"),
 ("A","A","പല ഇൻവെസ്റ്റർമാരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. നിർബന്ധിച്ചാൽ നിനക്ക് സ്ലോട്ട് പോകും."),
 ("V","V","അപ്പോ സർക്യൂട്ട് എങ്ങനെ കാക്കും?"),
 ("A","wide","സ്റ്റേജിൽ പ്രശ്നവും റിസൾട്ടും കാണിക്ക്. ഡയഗ്രം അടുത്ത മീറ്റിംഗിൽ, NDA ഒപ്പിട്ട ശേഷം."),
 ("V","wide","സ്റ്റേജിൽ ഷോ, ലാബിൽ ഡയഗ്രം.")],
 "ഡെമോയിൽ ഫലം,\nNDA-ക്ക് ശേഷം ഡയഗ്രം", CTA_SECRET, theme="crm",
 cap_ml="കോളേജ് ഡെമോ ഡേയിലും പല ഇൻവെസ്റ്റർമാരും ജഡ്ജസും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. സ്റ്റേജിൽ പ്രശ്നവും ഫലവും കാണിക്കൂ, സർക്യൂട്ടും കോഡും NDA ഒപ്പിട്ട ശേഷം മാത്രം. നിങ്ങൾ വിദ്യാർത്ഥി ഫൗണ്ടറാണോ?",
 cap_en="At a college demo day, many investors and judges won't sign an NDA at the pitch stage. Show the problem and the result on stage; share circuits and code only after an NDA. Are you a student founder?",
 cap_mg="College demo day-ilum pala investors-um judges-um pitch ghattathil NDA oppidaarilla. Stage-il problem-um result-um kaanikku, circuit-um code-um NDA oppitta shesham maathram. Ningal student founder aano?")

# crm #8 (hotel order for a home food seller): chef wants the masala recipe "for quality"
duo("ndd029", "vendor_supplier", "A", "fishmarket", "ഹോട്ടൽ ഓർഡർ കിട്ടി.\nഷെഫ് പറഞ്ഞു:\n\"മസാല കൂട്ട് കാണിക്ക്\"", [
 ("A","wide","ആന്റണി, ഹോട്ടലിന് ദിവസം 40 കിലോ മീൻ പൊള്ളിച്ചത്. ഷെഫ് മസാലക്കൂട്ട് എഴുതി ചോദിക്കുന്നു."),
 ("V","V","സുമേച്ചീ, ക്വാളിറ്റി നോക്കാനാണെന്ന് പറഞ്ഞാലും അത് നിങ്ങളുടെ സ്വന്തം മുതലാ."),
 ("A","A","കൊടുത്തില്ലെങ്കിൽ ഓർഡർ പോകും."),
 ("V","V","കൊടുക്കാം, പക്ഷേ NDA ആദ്യം. കൂട്ട് രഹസ്യമെന്ന് എഴുതി, ആവശ്യത്തിന് മാത്രം ഉപയോഗിക്കാമെന്ന് ഒപ്പിടട്ടെ."),
 ("A","wide","ഷെഫ് ജോലി മാറിയാലും കൂട്ട് കൂടെ പോകരുത്."),
 ("V","wide","മീൻ വിൽക്കാം, മസാല ഒപ്പിട്ടേ.")],
 "ഓർഡറിന് മസാല ചോദിച്ചാൽ\nആദ്യം NDA", CTA_NDA, theme="crm",
 cap_ml="വലിയ ഹോട്ടൽ ഓർഡറിന് മസാലക്കൂട്ട് ചോദിച്ചോ? കൂട്ട് രഹസ്യമെന്ന് നിർവചിച്ച്, ഓർഡറിന് മാത്രം ഉപയോഗിക്കാമെന്ന് എഴുതിയ NDA ആദ്യം. നിങ്ങളുടെ സ്പെഷ്യൽ: മീനോ ഇറച്ചിയോ?",
 cap_en="A hotel order comes with a request for your masala recipe? First an NDA that defines the recipe as confidential and limits its use to the order. Your speciality: fish or meat?",
 cap_mg="Valiya hotel order-nu masala koottu chodicho? Koottu rahasyam ennu define cheythu, order-nu maathram upayogikkaam ennu ezhuthiya NDA aadyam. Ningalude special: meeno irachiyo?")

# faq: "I'll make them sign later" after already showing it in public (d904: thattukada)
duo("ndd030", "vendor_supplier", "B", "thattukada", "ഫുഡ് വ്ലോഗിൽ ബീഫ് ഫ്രൈ\nകൂട്ട് പറഞ്ഞു.\nഇപ്പോ NDA ചോദിക്കുന്നു", [
 ("A","wide","ബിജൂ, ക്ലൗഡ് കിച്ചൺ ബ്രാൻഡ് നമ്മുടെ ബീഫ് ഫ്രൈ എടുക്കും. NDA ഒപ്പിട്ടിട്ട് കൂട്ട് കൊടുക്കാം."),
 ("V","V","സിജോ, കഴിഞ്ഞ മാസം വ്ലോഗറോട് നീ തന്നെ കൂട്ട് മുഴുവൻ പറഞ്ഞില്ലേ? രണ്ട് ലക്ഷം പേര് കണ്ടു."),
 ("A","A","അത് വെറും വീഡിയോ അല്ലേ?"),
 ("V","V","ഇതിനകം പൊതുവായത് NDA-ക്ക് സംരക്ഷിക്കാനാവില്ല. വീഡിയോയിൽ പറയാത്ത രഹസ്യം മാത്രമേ കാക്കാൻ പറ്റൂ."),
 ("A","wide","അപ്പോ ആ തേങ്ങാക്കൊത്തിന്റെ ട്രിക്ക് ഞാൻ പറഞ്ഞില്ല!"),
 ("V","wide","വ്ലോഗിൽ പറഞ്ഞത് നാട്ടുകാരുടേത്.")],
 "പൊതുവായത്\nരഹസ്യമാകില്ല", CTA_SECRET, theme="faq",
 cap_ml="വ്ലോഗിലോ റീലിലോ പറഞ്ഞ കൂട്ട് പിന്നീട് NDA കൊണ്ട് സംരക്ഷിക്കാനാവില്ല; ഇതിനകം പൊതുവായത് രഹസ്യമല്ല. ക്യാമറയ്ക്ക് മുന്നിൽ എന്ത് പറയണമെന്ന് ആദ്യം തീരുമാനിക്കൂ. നിങ്ങളുടെ കടയിലെ സ്പെഷ്യൽ എന്താ?",
 cap_en="A recipe you revealed in a food vlog or reel cannot be protected by an NDA later: what is already public is not confidential. Decide what to say on camera first. What is your shop's special?",
 cap_mg="Vlog-ilo reel-ilo paranja koottu pinneedu NDA kondu samrakshikkaan aavilla; already public aayathu rahasyamalla. Camera-kku munnil enthu parayanam ennu aadyam theerumaanikku. Ningalude kadayile special entha?")

# faq: "once she leaves, the NDA ends" (d904: bridal makeup artist's herbal pack)
duo("ndd031", "employee_nda", "C", "salon", "അസിസ്റ്റന്റ് പോയി.\nഅടുത്ത തെരുവിൽ\nഅതേ ബ്രൈഡൽ പാക്ക്", [
 ("A","wide","വിനീത്, എന്റെ അസിസ്റ്റന്റ് സ്വന്തം സലൂൺ തുടങ്ങി. എന്റെ മഞ്ഞൾ-ചന്ദന ബ്രൈഡൽ പാക്ക് തന്നെ."),
 ("V","V","സോണിയ, അവൾ ജോലി വിട്ടല്ലോ. NDA അതോടെ തീർന്നില്ലേ?"),
 ("A","A","അതാണ് ഞാനും പേടിക്കുന്നത്."),
 ("V","V","കാലാവധി NDA-യിൽ എഴുതുന്നതാണ്. ജോലി വിട്ട ശേഷവും രഹസ്യം തുടരുമെന്ന് എഴുതിയിട്ടുണ്ടെങ്കിൽ ബാധകം."),
 ("A","wide","ഇനി ജോയിൻ ചെയ്യുന്ന ദിവസം തന്നെ, കാലാവധി എഴുതി ഒപ്പ്."),
 ("V","wide","കത്രിക അവളുടേത്, കൂട്ട് നിന്റേത്.")],
 "ജോലി തീർന്നാലും\nരഹസ്യം തീരരുത്", CTA_NDA, theme="faq",
 cap_ml="ജീവനക്കാരി പോയാൽ NDA തീരുമോ? NDA-യിൽ എഴുതിയ കാലാവധി അനുസരിച്ചാണ്. ജോലി വിട്ട ശേഷവും രഹസ്യം തുടരുമെന്ന് എഴുതൂ. നിങ്ങളുടെ ബിസിനസ്: സലൂണോ സ്പായോ?",
 cap_en="Does an employee NDA end when she leaves? It depends on the duration written in it. Write that confidentiality continues after the job ends. Your business: salon or spa?",
 cap_mg="Jeevanakkaari poyaal NDA theerumo? NDA-yil ezhuthiya duration anusarichaanu. Joli vitta sheshavum rahasyam thudarum ennu ezhuthu. Ningalude business: salon-o spa-yo?")

# faq: "visit first, sign later" (d904: cardamom estate curing method)
duo("ndd032", "vendor_supplier", "A", "munnar", "ബയർ എസ്റ്റേറ്റ് മുഴുവൻ\nകണ്ടു. NDA പിറ്റേന്ന്\nഒപ്പിടാമെന്ന്", [
 ("A","wide","ബേസിൽ, ഏലം ഉണക്കുന്ന നമ്മുടെ ഡ്രയർ രീതി കയറ്റുമതിക്കാരൻ മുഴുവൻ വീഡിയോ എടുത്തു."),
 ("V","V","സെലിൻ, NDA ഒപ്പിട്ടിട്ടാണോ അകത്ത് കയറ്റിയത്?"),
 ("A","A","നാളെ ഓഫീസിൽ വന്ന് ഒപ്പിടാമെന്നാ പറഞ്ഞത്."),
 ("V","V","രഹസ്യം കാണിക്കും മുമ്പാണ് ഒപ്പ്. എന്താണ് രഹസ്യം എന്ന് NDA-യിൽ നിർവചിക്കണം: ഡ്രയർ, ചൂട്, സമയം."),
 ("A","wide","അടുത്ത സന്ദർശകന് ഗേറ്റിൽ തന്നെ പേപ്പർ."),
 ("V","wide","ഗേറ്റ് തുറക്കും മുമ്പ് ഒപ്പ്.")],
 "കാണിക്കും മുമ്പ്\nഒപ്പിടീക്കൂ", CTA_NDA, theme="faq",
 cap_ml="ബയറോ പാർട്ണറോ നിങ്ങളുടെ രീതി കാണാൻ വരുന്നുണ്ടോ? NDA ഒപ്പിടേണ്ടത് കാണിക്കുന്നതിന് മുമ്പാണ്, എന്താണ് രഹസ്യം എന്ന് അതിൽ നിർവചിക്കണം. നിങ്ങൾ എന്ത് കൃഷി ചെയ്യുന്നു?",
 cap_en="A buyer or partner coming to see your process? The NDA is signed before you show anything, and it must define what is confidential. What do you grow or make?",
 cap_mg="Buyer-o partner-o ningalude reethi kaanaan varunnundo? NDA oppidendathu kaanikkunnathinu munpaanu, enthaanu rahasyam ennu athil define cheyyanam. Ningal enthu krishi cheyyunnu?")

# faq: list before sending a deck
lst("ndd033", "founder_pitching", "B", "പിച്ച് ഡെക്ക് അയക്കും മുമ്പ്\n3 ചോദ്യം", [
 ("\"ഇതിനകം പൊതുവായോ?\"", "വെബ്സൈറ്റിലോ റീലിലോ ഉള്ളത് NDA കാക്കില്ല."),
 ("\"ഇത് ആദ്യ മീറ്റിംഗിൽ വേണോ?\"", "പല ഇൻവെസ്റ്റർമാരും പിച്ചിൽ NDA ഒപ്പിടില്ല. കോഡും ഫോർമുലയും പിന്നീട്."),
 ("\"NDA എഴുത്ത് ശരിയാണോ?\"", "രഹസ്യം, ഒഴിവാക്കലുകൾ, കാലാവധി, പരിഹാരം. പിന്നെ സ്റ്റാമ്പ്.")],
 "ഡെക്കിൽ കഥ,\nNDA-യിൽ രഹസ്യം", CTA_SECRET, theme="faq",
 cap_ml="ഡെക്ക് അയക്കും മുമ്പ് മൂന്ന് ചോദ്യം: ഇതിനകം പൊതുവായോ, ആദ്യ മീറ്റിംഗിൽ വേണോ, NDA ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്തോ. നിങ്ങളുടെ ഡെക്കിൽ എത്ര സ്ലൈഡ്?",
 cap_en="Three questions before you send a pitch deck: is it already public, is it needed in a first meeting, and is your NDA properly drafted and stamped? How many slides in your deck?",
 cap_mg="Deck ayakkum munpu moonnu chodyam: already public aayo, aadya meeting-il veno, NDA shariyaayi ezhuthi stamp cheytho. Ningalude deck-il ethra slide?")

# new: verbal promise vs written NDA (juice syrup, franchise partner)
duo("ndd034", "vendor_supplier", "C", "juiceshop", "\"ഞാൻ ആരോടും പറയില്ല\"\nഫ്രാഞ്ചൈസി പാർട്ണർ\nകൈ കൊടുത്തു", [
 ("A","wide","നൗഷാദേ, കോഴിക്കോട് ഫ്രാഞ്ചൈസിക്ക് നമ്മുടെ കുലുക്കി സർബത്ത് സിറപ്പ് പഠിപ്പിക്കണം. അവൻ കൈ തന്ന് സത്യം ചെയ്തു."),
 ("V","V","റസിയാ, കൈ കൊടുത്തത് കോടതിയിൽ കാണിക്കാൻ പറ്റുമോ?"),
 ("A","A","നാട്ടുകാരനാ, വാക്ക് മതി."),
 ("V","V","ശരിയായി എഴുതി, സംസ്ഥാന നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്ത NDA ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാറാണ്. വാക്ക് അങ്ങനെയല്ല."),
 ("A","wide","സിറപ്പ് പഠിപ്പിക്കുന്നത് ഒപ്പിട്ട പേപ്പറിന് ശേഷം."),
 ("V","wide","വാക്ക് പറന്നുപോകും, കരാർ നിൽക്കും.")],
 "കൈ കൊടുത്താൽ പോരാ,\nNDA എഴുതണം", CTA_NDA, theme="new",
 cap_ml="ഫ്രാഞ്ചൈസി പാർട്ണർക്ക് രഹസ്യ റെസിപ്പി പഠിപ്പിക്കുന്നുണ്ടോ? വാക്കിനെക്കാൾ ശക്തം ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്ത NDA ആണ്; അത് ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാറാണ്. നിങ്ങൾ ഫ്രാഞ്ചൈസി നൽകുന്നുണ്ടോ?",
 cap_en="Teaching a secret recipe to a franchise partner? A properly drafted NDA, stamped under the state's stamp law, is an enforceable contract in India; a handshake is not. Do you give franchises?",
 cap_mg="Franchise partner-nu rahasya recipe padippikkunnundo? Vaakkinekkaal shaktham shariyaayi ezhuthi stamp cheytha NDA aanu; athu India-yil nadappaakkaavunna contract aanu. Ningal franchise kodukkunnundo?")

# new: auto driver's app idea, developer passenger (one-way NDA)
duo("ndd035", "freelancer_nda", "A", "autostand", "സവാരിക്കിടെ ആപ്പ് ഐഡിയ\nപറഞ്ഞു. യാത്രക്കാരൻ\nഡെവലപ്പർ ആയിരുന്നു", [
 ("A","wide","ഷാജീ, സ്റ്റാൻഡിലെ ഓട്ടോകൾ ഒരുമിച്ച് ബുക്ക് ചെയ്യാനുള്ള എന്റെ ആപ്പ് ഐഡിയ ഒരു യാത്രക്കാരനോട് പറഞ്ഞു. അവൻ ഡെവലപ്പറാ!"),
 ("V","V","സജീ, അവനെക്കൊണ്ട് ഉണ്ടാക്കിക്കാമല്ലോ. ബാക്കി പ്ലാൻ കൂടി പറയ്."),
 ("A","A","ബാക്കി പറഞ്ഞാൽ അവൻ തന്നെ ഇറക്കിയാലോ?"),
 ("V","V","എങ്കിൽ ആദ്യം വൺ-വേ NDA. നീ മാത്രമാണ് രഹസ്യം കൊടുക്കുന്നത്. എന്താണ് രഹസ്യം, എത്ര കാലം എന്ന് എഴുതണം."),
 ("A","wide","ഇനി പ്ലാൻ മീറ്റർ ഇട്ടിട്ട്, NDA ഒപ്പിട്ടിട്ട്."),
 ("V","wide","മീറ്റർ ഓടട്ടെ, ഐഡിയ ഓടിപ്പോകരുത്.")],
 "ഐഡിയ മുഴുവൻ പറയും മുമ്പ്\nവൺ-വേ NDA", CTA_SECRET, theme="new",
 cap_ml="ഡെവലപ്പറോട് ആപ്പ് പ്ലാൻ മുഴുവൻ പറയും മുമ്പ് വൺ-വേ NDA ഒപ്പിടീക്കൂ. നിങ്ങൾ മാത്രം രഹസ്യം കൊടുക്കുമ്പോൾ അത് മതി; എന്താണ് രഹസ്യം, എത്ര കാലം എന്ന് എഴുതണം. നിങ്ങളുടെ ആപ്പ് ഐഡിയ ഏത് മേഖലയിൽ?",
 cap_en="Before telling a developer your whole app plan, get a one-way NDA signed. When only you share secrets, that is enough; define what is confidential and for how long. What field is your app idea in?",
 cap_mg="Developer-odu app plan muzhuvan parayum munpu one-way NDA oppideekku. Ningal maathram rahasyam kodukkumpol athu mathi; enthaanu rahasyam, ethra kaalam ennu ezhuthanam. Ningalude app idea ethu mekhalayil?")
