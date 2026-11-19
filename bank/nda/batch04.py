# NDA batch 04 (20 Nov, month backlog). Facts only from topics.FACTS_NDA. No fees, never promise a court outcome.
# People, firms, towns and numbers invented; CRM situations (C14/C15, #20, #26, #29) only in anonymised form.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

# d904 pattern: myth + unusual Kerala job + rhythmic punch
duo("ndd016", "vendor_supplier", "B", "handloom", "NDA ഒപ്പിട്ടാൽ\nആരും ഇതുപോലെ\nനെയ്യില്ലേ?", [
 ("A","wide","കുമാരേട്ടാ, എന്റെ പുതിയ കസവ് ഡിസൈൻ സൊസൈറ്റിക്ക് NDA-യോടെ കൊടുത്തു. ഇനി ആരും ഇതുപോലെ നെയ്യില്ലല്ലോ?"),
 ("V","V","ലീലേ, അടുത്ത ഗ്രാമത്തിലെ ഒരു നെയ്ത്തുകാരൻ സ്വന്തമായി ഇതുപോലൊന്ന് ഉണ്ടാക്കിയാലോ?"),
 ("A","A","അതും തടയാൻ പറ്റില്ലേ?"),
 ("V","V","ഇല്ല. സ്വതന്ത്രമായി ഉണ്ടാക്കിയത് NDA-യുടെ ഒഴിവാക്കലാണ്. നീ കൊടുത്ത ഡിസൈൻ സൊസൈറ്റി ചോർത്തിയാൽ, അവിടെ NDA കടിക്കും."),
 ("A","wide","അപ്പോ NDA എന്റെ ഫയലിനെ കാക്കും, ലോകത്തെ മുഴുവൻ തടയില്ല."),
 ("V","wide","നൂല് നിന്റേത്, തറി എല്ലാവരുടേതും.")],
 "NDA കോപ്പി തടയും,\nയാദൃച്ഛികത അല്ല", CTA_NDA, theme="faq",
 cap_ml="NDA നിങ്ങൾ പങ്കുവെച്ച രഹസ്യം ദുരുപയോഗം ചെയ്യുന്നത് തടയും. പക്ഷേ മറ്റൊരാൾ സ്വതന്ത്രമായി ഉണ്ടാക്കിയത് NDA-യുടെ ഒഴിവാക്കലാണ്. നിങ്ങളുടെ ഡിസൈൻ: കൈത്തറിയോ ഡിജിറ്റലോ?",
 cap_en="An NDA stops misuse of what you shared, but something another person develops independently is a standard exclusion. Handloom designers, weavers and makers: know what your NDA covers. Your designs: handloom or digital?",
 cap_mg="NDA ningal share cheytha rahasyam durupayogam cheyyunnathu thadayum. Pakshe vere aal swathanthramaayi undaakkiyathu exclusion aanu. Ningalude design: handloom-o digital-o?")

# crm C15: projects before registering, nothing written about what was whose
duo("ndd017", "agency_client", "A", "mobileshop", "3 ആപ്പ് ചെയ്തു.\nക്ലയന്റ് പറയുന്നു:\n\"കോഡ് ഞങ്ങളുടേത്\"", [
 ("A","wide","ഫഹദേ, രജിസ്ട്രേഷന് മുമ്പ് നമ്മൾ ചെയ്ത മൂന്ന് ആപ്പിലും നമ്മുടെ സ്വന്തം ലൈബ്രറി ഉണ്ട്. ഇപ്പോ ഒരു ക്ലയന്റ് അത് അവരുടേതെന്ന്."),
 ("V","V","ഹന്നേ, അന്ന് എന്തെങ്കിലും എഴുതിയിരുന്നോ? എന്ത് ആരുടേത് എന്ന്?"),
 ("A","A","ഒന്നുമില്ല. എല്ലാം ഫോൺ കോളിൽ."),
 ("V","V","ഇനി ഓരോ പ്രോജക്റ്റിനും NDA: ക്ലയന്റിന്റെ ഡാറ്റ അവരുടെ രഹസ്യം, നമ്മുടെ മുൻപേ ഉള്ള ടൂളുകൾ നമ്മുടേത്. രണ്ടും പേരെടുത്ത് എഴുതണം."),
 ("A","wide","അപ്പോ രഹസ്യം എന്താണെന്ന് നിർവചിക്കുന്നതാണ് പകുതി രക്ഷ."),
 ("V","wide","കോഡ് നമ്മളെഴുതി, പേപ്പർ ആരും എഴുതിയില്ല.")],
 "ആരുടേത് എന്ന്\nആദ്യം എഴുതൂ", CTA_NDA, theme="crm",
 cap_ml="രജിസ്ട്രേഷന് മുമ്പ് ചെയ്ത പ്രോജക്റ്റുകളിൽ എഴുത്തൊന്നും ഇല്ലെങ്കിൽ എന്ത് ആരുടേത് എന്ന് തെളിയിക്കാൻ പ്രയാസം. NDA-യിൽ ക്ലയന്റിന്റെ രഹസ്യവും നിങ്ങളുടെ മുൻ ടൂളുകളും വ്യക്തമായി നിർവചിക്കൂ. നിങ്ങളുടെ ടീം ഇത് എഴുതിയിട്ടുണ്ടോ?",
 cap_en="App and software teams that work before registering, with nothing in writing, struggle later to show what was theirs. An NDA should define the client's confidential information and keep your pre-existing tools clearly yours. Has your team written this down?",
 cap_mg="Registration-nu mumpu cheytha projects-il ezhuthonnum illenkil enthu aarudethu ennu theliyikkaan prayaasam. NDA-yil client data-um ningalude tools-um vyakthamaayi ezhuthu. Team ithu ezhuthiyo?")

# crm #20: investor asks for the data room after the first meetings
duo("ndd018", "founder_pitching", "A", "weddinghall", "\"ഡാറ്റ റൂം അയക്കൂ\":\n2,000 കസ്റ്റമർ\nഡീറ്റെയിൽസ് അതിൽ", [
 ("A","wide","ശരത്തേ, രണ്ടാം മീറ്റിംഗ് കഴിഞ്ഞു. ഇൻവെസ്റ്റർ ഡാറ്റ റൂം ചോദിച്ചു. നമ്മുടെ ബുക്കിംഗ് ആപ്പിലെ എല്ലാ കസ്റ്റമർ ഡീറ്റെയിൽസും അതിലുണ്ട്."),
 ("V","V","കാവ്യേ, പിച്ചിൽ അവർ NDA ഒപ്പിട്ടില്ലല്ലോ. അത് സാധാരണയാ. പക്ഷേ ഇത് പിച്ച് അല്ല."),
 ("A","A","ഇപ്പോ NDA ചോദിച്ചാൽ ഡീൽ പോകുമോ?"),
 ("V","V","ആഴത്തിലുള്ള രഹസ്യം കൊടുക്കും മുമ്പ് NDA ചോദിക്കാം. കസ്റ്റമർ ഡാറ്റയും കരാറുകളും രഹസ്യം എന്ന് പേരെടുത്ത് എഴുതണം."),
 ("A","wide","പിച്ചിൽ കഥ. ഡാറ്റ റൂമിൽ ഒപ്പ്."),
 ("V","wide","മണ്ഡപം തുറന്നിടാം, അലമാര പൂട്ടണം.")],
 "പിച്ചിൽ തുറന്ന്,\nഡാറ്റയിൽ പൂട്ടി", CTA_SECRET, theme="crm",
 cap_ml="പല ഇൻവെസ്റ്റർമാരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. പക്ഷേ കസ്റ്റമർ ഡാറ്റ പോലുള്ള ആഴത്തിലുള്ള വിവരം പങ്കുവെക്കും മുമ്പ് NDA ചോദിക്കാം, എന്താണ് രഹസ്യം എന്ന് നിർവചിക്കാം. നിങ്ങൾ ഡാറ്റ റൂം ഒരുക്കിയോ?",
 cap_en="Many investors won't sign an NDA at pitch stage, but before you share deep information like customer data in a data room, you can ask for one and define exactly what is confidential. Is your data room ready?",
 cap_mg="Pala investors-um pitch stage-il NDA oppidaarilla. Pakshe customer data pole aazhathilulla vivaram kodukkum mumpu NDA chodikkaam. Data room ready aano?")

# crm #26: returnee in the Gulf hires a Kerala app agency
duo("ndd019", "agency_client", "B", "gulfroom", "ദുബായിൽ ഇരുന്ന്\nനാട്ടിലെ ഏജൻസിക്ക്\nആപ്പ് ഐഡിയ", [
 ("A","wide","ഷംസൂ, നാട്ടിൽ വന്ന് തുടങ്ങാനുള്ള ആപ്പിന്റെ മുഴുവൻ പ്ലാനും കൊച്ചിയിലെ ഒരു ഏജൻസിക്ക് അയക്കാൻ പോകുവാ."),
 ("V","V","നസീറേ, അതിന് മുമ്പ് NDA? അവർക്ക് നിന്റെ പ്ലാൻ മാത്രമല്ലേ കിട്ടുന്നത്?"),
 ("A","A","അതെ, അവർ ഒന്നും തിരിച്ച് തരുന്നില്ല."),
 ("V","V","എങ്കിൽ വൺ-വേ NDA. എഴുതി, സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്താൽ ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാർ. എത്ര കാലം എന്നും എഴുതണം."),
 ("A","wide","ഇവിടെ ഇരുന്നാലും പേപ്പർ നാട്ടിൽ ശക്തമാകണം."),
 ("V","wide","ദൂരം കൂടിയാൽ, കരാർ മുറുക്കണം.")],
 "ദൂരെ ഇരുന്നാലും\nരഹസ്യം അടുത്ത്", CTA_NDA, theme="crm",
 cap_ml="ഗൾഫിൽ ഇരുന്ന് കേരളത്തിലെ ഏജൻസിക്ക് ആപ്പ് പ്ലാൻ അയക്കുന്നുണ്ടോ? നിങ്ങൾ മാത്രം പങ്കുവെക്കുമ്പോൾ വൺ-വേ NDA മതി; ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്യണം, കാലാവധിയും എഴുതണം. നിങ്ങൾ എവിടെ നിന്നാണ്?",
 cap_en="Sending your app plan from the Gulf to an agency in Kerala? If only you share information, a one-way NDA fits; it must be properly drafted, stamped under the state's stamp law and state a duration. Where are you based?",
 cap_mg="Gulf-il irunnu Kerala agency-kku app plan ayakkunnundo? Ningal maathram share cheyyumpol one-way NDA mathi; shariyaayi ezhuthi stamp cheyyanam, kaalavadhiyum ezhuthanam. Ningal evide ninnaanu?")

# crm #29: woman founder, health-food formula to a contract manufacturer
duo("ndd020", "vendor_supplier", "A", "kitchen", "ഫോർമുലയ്ക്ക്\n10 വർഷത്തെ രഹസ്യം.\nNDA ഒരു വർഷം", [
 ("A","wide","രാജേഷേ, എന്റെ റാഗി മിക്സിന്റെ ഫോർമുല ഫാക്ടറിക്ക് കൊടുക്കാൻ NDA കിട്ടി. കാലാവധി ഒരു വർഷം."),
 ("V","V","ബിന്ദൂ, ഈ ഫോർമുല എത്ര കാലം നിന്റെ രഹസ്യമായി നിൽക്കണം?"),
 ("A","A","ബ്രാൻഡ് ഉള്ളിടത്തോളം. കുറഞ്ഞത് പത്ത് വർഷം."),
 ("V","V","എങ്കിൽ ഒരു വർഷം കഴിഞ്ഞാൽ അവരുടെ ബാധ്യതയും തീരാം. കാലാവധി രഹസ്യത്തിന്റെ ആയുസ്സിനൊപ്പം എഴുതണം."),
 ("A","wide","ഒപ്പിടും മുമ്പ് ആ ഒരു വരി മാറ്റിക്കാം."),
 ("V","wide","മിക്സ് പഴകില്ല, NDA പഴകരുത്.")],
 "കാലാവധി രഹസ്യത്തിന്റെ\nആയുസ്സിനൊപ്പം", CTA_SECRET, theme="crm",
 cap_ml="NDA-യുടെ കാലാവധി തീർന്നാൽ രഹസ്യം സൂക്ഷിക്കാനുള്ള ബാധ്യതയും തീരാം. ഫോർമുലയോ റെസിപ്പിയോ കൊടുക്കുമ്പോൾ അത് എത്ര കാലം രഹസ്യമായി നിൽക്കണം എന്ന് നോക്കി കാലാവധി എഴുതൂ. നിങ്ങളുടെ ഉൽപ്പന്നം: ഫുഡോ കോസ്മെറ്റിക്കോ?",
 cap_en="When an NDA's duration ends, the duty to keep your secret can end with it. Sharing a formula or recipe with a manufacturer? Set the duration to how long it must stay secret. Your product: food or cosmetics?",
 cap_mg="NDA-yude kaalavadhi theernnaal rahasyam sookshikkaanulla baadhyathayum theeraam. Formula kodukkumpol ethra kaalam rahasyamaayi nilkkanam ennu nokki kaalavadhi ezhuthu. Food-o cosmetic-o?")

# d904: myth "an NDA is just a formality"
duo("ndd021", "freelancer_nda", "B", "tailor", "\"NDA വെറും\nഫോർമാലിറ്റി,\nആരും നടപ്പാക്കില്ല\"", [
 ("A","wide","മോഹനേട്ടാ, എന്റെ ആരി എംബ്രോയ്ഡറി മോട്ടിഫ് ബൊട്ടീക്കിന് കൊടുത്തപ്പോൾ NDA ഒപ്പിട്ടു. അതൊക്കെ ഫോർമാലിറ്റി അല്ലേ?"),
 ("V","V","ഉഷേ, അവർ അത് മറ്റൊരു കടയുടെ കാറ്റലോഗിന് കൊടുത്താലോ?"),
 ("A","A","പിന്നെ ഞാൻ എന്ത് ചെയ്യാനാ?"),
 ("V","V","ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്ത NDA ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാറാണ്. ഉപയോഗം തടയാൻ ഇൻജങ്ഷൻ ചോദിക്കാം."),
 ("A","wide","അപ്പോ ആ പേപ്പർ അലമാരയിൽ അല്ല, ഫയലിൽ വെക്കണം."),
 ("V","wide","സൂചി ചെറുതാ, കരാറിന് പല്ലുണ്ട്.")],
 "ഒപ്പിട്ട NDA\nഅലങ്കാരമല്ല", CTA_NDA, theme="faq",
 cap_ml="ശരിയായി എഴുതി സംസ്ഥാന സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്ത NDA ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാറാണ്; ലംഘനം തടയാൻ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം ചോദിക്കാം. ഡിസൈനർമാർ ഇത് അറിയണം. നിങ്ങളുടെ കല: എംബ്രോയ്ഡറിയോ പെയിന്റിംഗോ?",
 cap_en="A properly drafted NDA, stamped under the state's stamp law, is an enforceable contract in India, and remedies such as an injunction can be sought. Embroidery artists and designers, it's not just a formality. Your craft: embroidery or painting?",
 cap_mg="Shariyaayi ezhuthi stamp cheytha NDA India-yil nadappaakkaavunna karaar aanu; injunction chodikkaam. Designers ithu ariyanam. Ningalude kala: embroidery-o painting-o?")

# d904: subtitle writer for an unreleased film
duo("ndd022", "freelancer_nda", "A", "ferry", "\"സിനിമയെ കുറിച്ച്\nഒരു വാക്കും\nമിണ്ടരുത്\"", [
 ("A","wide","ടോണീ, റിലീസ് ആകാത്ത സിനിമയുടെ സബ്ടൈറ്റിൽ എഴുതാൻ കിട്ടി. NDA-യിൽ സിനിമയെ കുറിച്ച് എല്ലാം രഹസ്യം എന്ന്."),
 ("V","V","മീരേ, ട്രെയിലർ ഇന്നലെ ഇറങ്ങിയല്ലോ. അതിനെ കുറിച്ച് പോലും മിണ്ടാൻ പറ്റില്ലേ?"),
 ("A","A","അതാ എനിക്കും സംശയം."),
 ("V","V","ഇതിനകം പൊതുവായത് NDA-ക്ക് സംരക്ഷിക്കാനാവില്ല. സ്ക്രിപ്റ്റും ക്ലൈമാക്സും ആണ് രഹസ്യം. അത് ഒരിക്കലും പുറത്ത് പറയരുത്."),
 ("A","wide","ഒപ്പിടും മുമ്പ് ഒഴിവാക്കലുകൾ വായിക്കാം."),
 ("V","wide","ട്രെയിലർ പബ്ലിക്, ക്ലൈമാക്സ് രഹസ്യം.")],
 "ട്രെയിലർ പബ്ലിക്,\nക്ലൈമാക്സ് രഹസ്യം", CTA_SECRET, theme="new",
 cap_ml="NDA ഒപ്പിടുന്ന ഫ്രീലാൻസർമാർ അറിയണം: ഇതിനകം പൊതുവായത് NDA-ക്ക് സംരക്ഷിക്കാനാവില്ല, പക്ഷേ നിങ്ങൾക്ക് കിട്ടിയ രഹസ്യം സൂക്ഷിക്കണം. ഒഴിവാക്കലുകൾ വായിച്ചിട്ട് ഒപ്പിടൂ. നിങ്ങൾ ഏത് ഫീൽഡിൽ ഫ്രീലാൻസ് ചെയ്യുന്നു?",
 cap_en="Freelancers signing an NDA: what is already public cannot be protected, but the confidential material you were given must stay secret. Read the exclusions before you sign. What field do you freelance in?",
 cap_mg="NDA oppidunna freelancers ariyanam: ithinakam public aayathu NDA-kku samrakshikkaan pattilla, pakshe kittiya rahasyam sookshikkanam. Exclusions vaayichittu oppidu. Ningal ethu field-il freelance cheyyunnu?")

# faq: vendor sees customer numbers
duo("ndd023", "vendor_supplier", "A", "courier", "4,000 കസ്റ്റമർ\nനമ്പർ. ഡെലിവറി\nപാർട്ണറുടെ കയ്യിൽ", [
 ("A","wide","അരവിന്ദേ, നമ്മുടെ മീൻ ഡെലിവറി ആപ്പിലെ നാലായിരം കസ്റ്റമർ നമ്പർ പുതിയ ഡെലിവറി പാർട്ണർക്ക് കൊടുക്കണം."),
 ("V","V","ജയേ, NDA ഉണ്ടോ? അതിൽ കസ്റ്റമർ ഡാറ്റ രഹസ്യം എന്ന് എഴുതിയിട്ടുണ്ടോ?"),
 ("A","A","ബിസിനസ് വിവരം രഹസ്യം എന്ന് മാത്രം."),
 ("V","V","അത് പോരാ. എന്താണ് രഹസ്യം എന്ന് വ്യക്തമായി നിർവചിക്കണം: പേര്, നമ്പർ, ഓർഡർ ഹിസ്റ്ററി. ലംഘിച്ചാൽ എന്ത് എന്നും."),
 ("A","wide","അവ്യക്തമായ വരി തർക്കത്തിൽ സഹായിക്കില്ല."),
 ("V","wide","നമ്പർ കൊടുക്കും മുമ്പ് നിർവചനം.")],
 "എന്താണ് രഹസ്യം?\nപേരെടുത്ത് എഴുതൂ", CTA_NDA, theme="faq",
 cap_ml="ഡെലിവറി പാർട്ണർക്കോ വെണ്ടർക്കോ കസ്റ്റമർ ഡാറ്റ കൊടുക്കും മുമ്പ് NDA-യിൽ എന്താണ് രഹസ്യം എന്ന് വ്യക്തമായി നിർവചിക്കൂ: പേര്, നമ്പർ, ഓർഡർ വിവരം. നിങ്ങൾ ആരുമായാണ് ഡാറ്റ പങ്കുവെക്കുന്നത്?",
 cap_en="Before giving customer data to a delivery partner or vendor, the NDA should define exactly what is confidential: names, phone numbers, order history, and what happens on a breach. Who do you share data with?",
 cap_mg="Delivery partner-kko vendor-kko customer data kodukkum mumpu NDA-yil enthaanu rahasyam ennu vyakthamaayi ezhuthu: peru, number, order vivaram. Aarumaayaanu data share cheyyunnathu?")

# faq: new hire asks whether to sign
chat("ndd024", "employee_nda", "A", "ജോയിൻ ദിവസം\nNDA കിട്ടി.\nഒപ്പിടണോ?", ("ദിവ്യ", "അഖിൽ"), [
 (1,"ചേച്ചി, പുതിയ ജോലിയിൽ ആദ്യ ദിവസം തന്നെ NDA തന്നു. ഒപ്പിടണോ?"),
 (0,"അതിൽ എന്താണ് രഹസ്യം എന്ന് എഴുതിയിട്ടുണ്ട്?"),
 (1,"കമ്പനിയുടെ കസ്റ്റമർ ലിസ്റ്റും സോഫ്റ്റ്‌വെയർ കോഡും. ജോലി വിട്ട് രണ്ട് വർഷം വരെ."),
 (0,"അത് സാധാരണയാ. ഇതിനകം പൊതുവായ കാര്യങ്ങൾ ഒഴിവാക്കലായി ഉണ്ടോ എന്ന് മാത്രം നോക്ക്."),
 (1,"ഉണ്ട്. അപ്പോ ഒപ്പിടാം."),
 (0,"വായിച്ചിട്ട് ഒപ്പിടുന്നവനാണ് ബുദ്ധിമാൻ.")],
 "വായിച്ചിട്ട് മാത്രം\nഒപ്പ്", CTA_NDA, theme="faq",
 cap_ml="ജോലിയിൽ ചേരുമ്പോൾ NDA കിട്ടിയാൽ മൂന്ന് കാര്യം നോക്കൂ: എന്താണ് രഹസ്യം, എത്ര കാലം, പൊതുവായ വിവരം ഒഴിവാക്കിയിട്ടുണ്ടോ. നിങ്ങൾ ജോലിയിൽ NDA ഒപ്പിട്ടിട്ടുണ്ടോ?",
 cap_en="Got an NDA on your first day at work? Check three things: what is defined as confidential, for how long, and whether public information is excluded. Have you signed one at work?",
 cap_mg="Joliyil cherumpol NDA kittiyaal moonnu kaaryam nokku: enthaanu rahasyam, ethra kaalam, public vivaram exclude cheythittundo. Ningal joliyil NDA oppittittundo?")

# new: NDA myths in one list
lst("ndd025", "founder_pitching", "B", "NDA-യെ കുറിച്ച്\nഎല്ലാവരും വിശ്വസിക്കുന്ന\n3 മിഥ്യ", [
 ("\"ഇൻവെസ്റ്റർ പിച്ചിൽ ഒപ്പിടും\"", "പലരും പിച്ച് ഘട്ടത്തിൽ ഒപ്പിടാറില്ല."),
 ("\"ഒപ്പ് മാത്രം മതി\"", "ശരിയായി എഴുതി സംസ്ഥാന നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്യണം."),
 ("\"എല്ലാം രഹസ്യമാക്കാം\"", "ഇതിനകം പൊതുവായത് സംരക്ഷിക്കാനാവില്ല.")],
 "മിഥ്യ മാറ്റൂ,\nരഹസ്യം കാക്കൂ", CTA_SECRET, theme="new",
 cap_ml="NDA മിഥ്യകൾ: എല്ലാ ഇൻവെസ്റ്റർമാരും പിച്ചിൽ ഒപ്പിടും, ഒപ്പ് മാത്രം മതി, എല്ലാം രഹസ്യമാക്കാം. മൂന്നും തെറ്റാണ്. ഇതിൽ ഏതാണ് നിങ്ങൾ വിശ്വസിച്ചിരുന്നത്?",
 cap_en="Three NDA myths: every investor signs one at the pitch, a signature is enough, and anything can be made confidential. All three are wrong. Which one did you believe?",
 cap_mg="NDA myths: ellaa investors-um pitch-il oppidum, oppu maathram mathi, ellaam rahasyamaakkaam. Moonnum thettaanu. Ethaanu ningal vishwasichirunnathu?")
