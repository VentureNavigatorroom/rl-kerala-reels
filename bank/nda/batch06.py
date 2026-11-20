# NDA batch 06 (20 Nov, month backlog). Facts only from topics.FACTS_NDA. No fees, never promise a court outcome.
# People, firms, towns and numbers invented; CRM situations (#21, #29, C13, #16) only in anonymised form.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

# crm #21 (traditional farm with a new process): a big buyer wants to walk through the process
duo("ndd036", "vendor_supplier", "A", "farm", "\"ഡീലിന് മുമ്പ്\nഫാം മുഴുവൻ കാണണം\"\nകൂൺ പ്രോസസ് അടക്കം", [
 ("A","wide","ഗോപീ, ആ വലിയ കമ്പനി കൂൺ വാങ്ങാൻ റെഡി. പക്ഷേ ആദ്യം നമ്മുടെ ഷെഡും പ്രോസസും മുഴുവൻ കാണണം എന്ന്."),
 ("V","V","വാസുവേട്ടാ, ആ വൈക്കോൽ വിദ്യ കണ്ടുപിടിക്കാൻ നമുക്ക് രണ്ട് വർഷം എടുത്തു. അവർ കണ്ടിട്ട് സ്വന്തം ഫാം തുടങ്ങിയാലോ?"),
 ("A","A","ഡീൽ പോകുമോ എന്ന് പേടിച്ച് ഒന്നും ചോദിച്ചില്ല."),
 ("V","wide","കാണിക്കും മുമ്പ് വൺ-വേ NDA. ഏത് പ്രോസസ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത്: എല്ലാം എഴുതി, സ്റ്റാമ്പ് ചെയ്ത്."),
 ("A","A","കൂൺ കാണിക്കാം, കൂട്ട് ഒപ്പിന് ശേഷം."),
 ("V","V","ഷെഡിന്റെ വാതിൽ തുറക്കും മുമ്പ് പേനയുടെ അടപ്പ് തുറക്കണം.")],
 "ഷെഡ് തുറക്കും മുമ്പ്\nNDA ഒപ്പിടൂ", CTA_SECRET, theme="crm",
 cap_ml="കൂൺ കൃഷിയിലെ സ്വന്തം പ്രോസസ് ഒരു വലിയ ബയർക്ക് കാണിക്കും മുമ്പ് വൺ-വേ NDA: എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത് പരിഹാരം, സംസ്ഥാന സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ്. നിങ്ങളുടെ ബിസിനസിലെ രഹസ്യ വിദ്യ എന്താണ്?",
 cap_en="Before a big buyer tours your farm and sees your own mushroom process, get a one-way NDA: what is confidential, for how long, the remedy if it is broken, stamped under the state's stamp law. What's the secret method in your business?",
 cap_mg="Koon krishiyile swantham process oru valiya buyer-kku kaanikkum mumpu one-way NDA: enthaanu rahasyam, ethra kaalam, lamghichaal enthu parihaaram, state stamp niyamaprakaaram stamp. Ningalude business-ile rahasya vidya enthaanu?")

# crm #29 (woman founder, activewear) + both sides bring specs: mutual NDA with a fabric mill
duo("ndd037", "vendor_supplier", "B", "balcony", "തുണി മില്ലിന്\nഎന്റെ ഡിസൈൻ.\nഅവരുടെ ഫോർമുല എനിക്ക്", [
 ("A","wide","വിവേകേ, മിൽ എന്റെ യോഗ പാന്റിനായി പുതിയ തുണി ഉണ്ടാക്കും. ഞാൻ ഡിസൈൻ കൊടുക്കും, അവർ നൂലിന്റെ ഫോർമുല പറയും."),
 ("V","V","അമ്മൂ, NDA ഒപ്പിടുന്നുണ്ടോ? അതോ അവരുടെ ഫോം മാത്രമോ?"),
 ("A","A","അവർ അയച്ചത് വൺ-വേ. അവരുടെ ഫോർമുല മാത്രം രഹസ്യം. എന്റെ ഡിസൈൻ അതിൽ ഇല്ല."),
 ("V","wide","രണ്ടുപേരും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ NDA. നിന്റെ ഡിസൈനും അവരുടെ ഫോർമുലയും പേരെടുത്ത് എഴുതണം."),
 ("A","A","അപ്പോ തുണി ഒന്ന്, പക്ഷേ സംരക്ഷണം രണ്ട് വശത്തും."),
 ("V","V","തുന്നൽ രണ്ടറ്റത്തും വേണം, അല്ലെങ്കിൽ അഴിയും.")],
 "രണ്ടുപേരും പങ്കുവെച്ചാൽ\nമ്യൂച്വൽ NDA", CTA_NDA, theme="crm",
 cap_ml="ആക്ടീവ്‌വെയർ ഫൗണ്ടർ ഡിസൈൻ കൊടുക്കുന്നു, മിൽ തുണി ഫോർമുല പറയുന്നു. മില്ലിന്റെ വൺ-വേ NDA അവരെ മാത്രം കാക്കും. രണ്ടുപേരും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ NDA, രണ്ട് രഹസ്യവും പേരെടുത്ത് എഴുതി. നിങ്ങൾ ഒപ്പിട്ട NDA ഏത് തരം?",
 cap_en="An activewear founder shares her designs; the mill shares its fabric formula. The mill's one-way NDA protects only the mill. When both sides share secrets, use a mutual NDA that names both. Which kind did you sign?",
 cap_mg="Activewear founder design kodukkunnu, mill thuni formula parayunnu. Mill-inte one-way NDA avare maathram kaakkum. Randuperum rahasyam pankuvekkumbol mutual NDA, randu rahasyavum perueduthu ezhuthi. Ningal oppitta NDA ethu tharam?")

# crm C13 (founder abroad running a Kerala business): a travel partner wants the guest list
duo("ndd038", "agency_client", "C", "homestay", "\"ജോയിന്റ് പാക്കേജിന്\nഗസ്റ്റ് ലിസ്റ്റ് മുഴുവൻ\nഅയക്കൂ\"", [
 ("A","wide","ജോമോനേ, ഞാൻ കാനഡയിൽ ഇരുന്നാ ഹോംസ്റ്റേ നോക്കുന്നത്. ട്രാവൽ ഏജൻസി ജോയിന്റ് പാക്കേജിന് 900 ഗസ്റ്റുകളുടെ ലിസ്റ്റ് ചോദിക്കുന്നു."),
 ("V","V","ടീനേ, അവരും അവരുടെ റേറ്റും റൂട്ടും നമുക്ക് തരുമല്ലോ. രണ്ട് വശത്തും രഹസ്യം ഉണ്ട്."),
 ("A","A","വാട്സ്ആപ്പിൽ \"ആരോടും പറയില്ല\" എന്ന് അവർ എഴുതിയിട്ടുണ്ട്."),
 ("V","wide","അത് പോരാ. മ്യൂച്വൽ NDA: ഗസ്റ്റ് ലിസ്റ്റും അവരുടെ റേറ്റും രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം."),
 ("A","A","ദൂരെ ഇരുന്നാലും ഒപ്പ് അടുത്ത് വേണം."),
 ("V","V","ഗസ്റ്റ് നിന്റേത്, ലിസ്റ്റ് അവർക്ക് വാടകയ്ക്കല്ല.")],
 "ലിസ്റ്റ് അയക്കും മുമ്പ്\nമ്യൂച്വൽ NDA", CTA_NDA, theme="crm",
 cap_ml="വിദേശത്തിരുന്ന് നാട്ടിലെ ഹോംസ്റ്റേ നടത്തുന്ന ഉടമയോട് ട്രാവൽ ഏജൻസി ജോയിന്റ് പാക്കേജിന് ഗസ്റ്റ് ലിസ്റ്റ് ചോദിക്കുന്നു. രണ്ടുപേരും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ NDA, രഹസ്യം എന്ത്, കാലാവധി, പരിഹാരം എഴുതി. നിങ്ങളുടെ കസ്റ്റമർ ലിസ്റ്റ് ആരുടെ കയ്യിലുണ്ട്?",
 cap_en="A homestay owner abroad is asked by a travel agency for the full guest list for a joint package. When both sides share secrets, sign a mutual NDA that names them, the duration and the remedy. Who holds your customer list?",
 cap_mg="Videshathirunnu naattile homestay nadathunna udamayodu travel agency joint package-inu guest list chodikkunnu. Randuperum rahasyam pankuvekkumbol mutual NDA, rahasyam enthu, kaalaavadhi, parihaaram ezhuthi. Ningalude customer list aarude kayyil undu?")

# crm #16 (Gulf Malayali investor in a relative's Kerala startup), twist: the investor shares his own secret
duo("ndd039", "founder_pitching", "A", "railway", "ഇൻവെസ്റ്റർ കസിൻ:\n\"എന്റെ ഡിസ്ട്രിബ്യൂട്ടർ\nലിസ്റ്റിന് NDA വേണം\"", [
 ("A","wide","ദിനേശേട്ടാ, ദുബായിൽ നിന്ന് വന്നതേ ഉള്ളൂ, ആദ്യം ചോദിക്കുന്നത് NDA ആണോ? നമ്മൾ കസിൻസ് അല്ലേ?"),
 ("V","V","ഷീബേ, എന്റെ 40 ഡിസ്ട്രിബ്യൂട്ടർമാരുടെ ലിസ്റ്റ് നിന്റെ ഫുഡ് ബ്രാൻഡിന് തരാൻ പോകുവാ. അത് എന്റെ 20 വർഷത്തെ പണിയാ."),
 ("A","A","അപ്പോ ഇത്തവണ രഹസ്യം നിങ്ങളുടേതാണ്, എന്റേതല്ല."),
 ("V","wide","അതെ. നീ മാത്രം സ്വീകരിക്കുന്നു, അതുകൊണ്ട് വൺ-വേ NDA. ലിസ്റ്റ് പേരെടുത്ത് എഴുതി, കാലാവധിയും പരിഹാരവും വെച്ച്."),
 ("A","A","ബന്ധം ഉള്ളതുകൊണ്ട് കരാർ വേണ്ടാന്നില്ല."),
 ("V","V","കുടുംബം വിശ്വാസം, NDA ഉറപ്പ്.")],
 "കുടുംബം വിശ്വാസം,\nNDA ഉറപ്പ്", CTA_SECRET, theme="crm",
 cap_ml="ഗൾഫിലെ ബന്ധുവായ ഇൻവെസ്റ്റർ സ്വന്തം ഡിസ്ട്രിബ്യൂട്ടർ ലിസ്റ്റ് സ്റ്റാർട്ടപ്പിന് കൊടുക്കും മുമ്പ് NDA ചോദിച്ചു. ഒരാൾ മാത്രം പങ്കുവെക്കുമ്പോൾ വൺ-വേ NDA മതി, രഹസ്യം പേരെടുത്ത് എഴുതണം. കുടുംബത്തിനുള്ളിൽ NDA: ശരിയോ തെറ്റോ?",
 cap_en="A Gulf-based relative investing in a Kerala startup asked for an NDA before handing over his own distributor list. When only one side shares, a one-way NDA that names the secret is enough. NDA within the family: fair or awkward?",
 cap_mg="Gulf-ile bandhuvaaya investor swantham distributor list startup-inu kodukkum mumpu NDA chodichu. Oraal maathram pankuvekkumbol one-way NDA mathi, rahasyam perueduthu ezhuthanam. Kudumbathinullil NDA: shariyo thetto?")

# faq: "every page says CONFIDENTIAL, so I don't need an NDA"
duo("ndd040", "agency_client", "B", "bank", "എല്ലാ പേജിലും\n\"കോൺഫിഡൻഷ്യൽ\"\nഎന്ന് സീൽ. അത് പോരേ?", [
 ("A","wide","മനോജേ, ലോൺ കൺസൾട്ടന്റിന് ബിസിനസ് പ്ലാൻ അയച്ചു. എല്ലാ പേജിലും വലിയ അക്ഷരത്തിൽ കോൺഫിഡൻഷ്യൽ എന്ന് ഇട്ടിട്ടുണ്ട്."),
 ("V","V","ശ്രുതീ, അയാൾ എന്തെങ്കിലും ഒപ്പിട്ടോ? അതോ സീൽ മാത്രമോ?"),
 ("A","A","സീൽ മാത്രം. അത് കണ്ടാൽ ആരും പുറത്ത് പറയില്ലല്ലോ."),
 ("V","wide","സീൽ ഒരു മുന്നറിയിപ്പ് മാത്രം. NDA ഒരു കരാർ: എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത്, ഒപ്പും സ്റ്റാമ്പും."),
 ("A","A","അപ്പോ സീൽ പേജിൽ, ഉറപ്പ് ഒപ്പിൽ."),
 ("V","V","ചുവന്ന മഷി പേടിപ്പിക്കും, NDA തടയും.")],
 "സീൽ മുന്നറിയിപ്പ്,\nNDA കരാർ", CTA_NDA, theme="faq",
 cap_ml="എല്ലാ പേജിലും കോൺഫിഡൻഷ്യൽ എന്ന് അടിച്ചാൽ NDA ആകുമോ? ഇല്ല. NDA ഒരു കരാറാണ്: രഹസ്യം എന്ത്, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത്, സംസ്ഥാന നിയമപ്രകാരം സ്റ്റാമ്പ്. നിങ്ങൾ സീലിലാണോ ഒപ്പിലാണോ വിശ്വസിക്കുന്നത്?",
 cap_en="Does stamping CONFIDENTIAL on every page make it an NDA? No. An NDA is a contract: what is confidential, for how long, the remedy, stamped under the state's stamp law. Do you rely on the label or on a signature?",
 cap_mg="Ella page-ilum confidential ennu adichaal NDA aakumo? Illa. NDA oru karaar aanu: rahasyam enthu, ethra kaalam, lamghichaal enthu, state niyamaprakaaram stamp. Ningal seal-ilaano oppilaano viswasikkunnathu?")

# faq: "an NDA that says 'all information' is the safest"
duo("ndd041", "freelancer_nda", "C", "akshaya", "NDA-യിൽ ഒറ്റ വരി:\n\"എല്ലാ വിവരവും\nരഹസ്യം\"", [
 ("A","wide","രമേശേ, പുതിയ ക്ലയന്റിന്റെ NDA-യിൽ ഒറ്റ വരിയേ ഉള്ളൂ: എല്ലാ വിവരവും രഹസ്യം. അത് ഏറ്റവും സേഫ് അല്ലേ?"),
 ("V","V","സുധേച്ചീ, അപ്പോ നിങ്ങൾ മുമ്പേ അറിയാവുന്ന ടാലി ട്രിക്കുകളും അവരുടെ രഹസ്യമാകുമോ?"),
 ("A","A","അയ്യോ, അത് എന്റെ പത്ത് വർഷത്തെ പണിയാ."),
 ("V","wide","നല്ല NDA രഹസ്യം പേരെടുത്ത് നിർവചിക്കും. ഇതിനകം പൊതുവായതും സ്വതന്ത്രമായി ഉണ്ടാക്കിയതും ഒഴിവാക്കലായി എഴുതും."),
 ("A","A","എല്ലാം എന്ന് എഴുതിയാൽ ഒന്നും വ്യക്തമല്ല."),
 ("V","V","എല്ലാം പൂട്ടിയാൽ താക്കോലും അകത്താകും.")],
 "എല്ലാം പൂട്ടിയാൽ\nതാക്കോലും അകത്ത്", CTA_SECRET, theme="faq",
 cap_ml="\"എല്ലാ വിവരവും രഹസ്യം\" എന്ന ഒറ്റ വരി NDA സേഫ് ആണോ? നല്ല NDA രഹസ്യം നിർവചിക്കും, ഇതിനകം പൊതുവായതും സ്വതന്ത്രമായി ഉണ്ടാക്കിയതും ഒഴിവാക്കും. നിങ്ങളുടെ NDA-യിൽ ഒഴിവാക്കലുകൾ ഉണ്ടോ?",
 cap_en="Is a one-line NDA that makes 'all information' confidential the safest? A good NDA defines the confidential information and excludes what is already public or independently developed. Does your NDA list exclusions?",
 cap_mg="'Ella vivaravum rahasyam' enna otta vari NDA safe aano? Nalla NDA rahasyam nirvachikkum, ithinakam pothuvaayathum swathanthramaayi undaakkiyathum ozhivaakkum. Ningalude NDA-yil ozhivaakkalukal undo?")

# faq: the other party is in another state and signs a PDF; nobody stamped it
duo("ndd042", "vendor_supplier", "A", "shop", "മറ്റൊരു സംസ്ഥാനത്തെ\nസപ്ലയർ PDF-ൽ ഒപ്പിട്ടു.\nസ്റ്റാമ്പ്? ആരും ഇല്ല", [
 ("A","wide","സുരേഷേ, നമ്മുടെ സോപ്പ് കൂട്ടിന് NDA വേറെ സംസ്ഥാനത്തെ സപ്ലയർ PDF-ൽ ഒപ്പിട്ട് അയച്ചു. തീർന്നില്ലേ?"),
 ("V","V","ബിനുവേട്ടാ, സ്റ്റാമ്പ് ആര് ചെയ്തു? അവരോ നമ്മളോ?"),
 ("A","A","ആരും ചെയ്തില്ല. ഒപ്പ് ഉണ്ടല്ലോ."),
 ("V","wide","ശരിയായി എഴുതി, സംസ്ഥാന സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്ത NDA ആണ് ഇന്ത്യയിൽ നടപ്പാക്കാവുന്നത്. ഒപ്പിനൊപ്പം സ്റ്റാമ്പും."),
 ("A","A","ഒപ്പ് പകുതി, സ്റ്റാമ്പ് ബാക്കി പകുതി."),
 ("V","V","PDF പറന്നുപോകും, സ്റ്റാമ്പ് പിടിച്ചുനിർത്തും.")],
 "ഒപ്പ് പകുതി,\nസ്റ്റാമ്പ് ബാക്കി പകുതി", CTA_NDA, theme="faq",
 cap_ml="മറ്റൊരു സംസ്ഥാനത്തെ സപ്ലയർ NDA PDF-ൽ ഒപ്പിട്ടു, ആരും സ്റ്റാമ്പ് ചെയ്തില്ല. ശരിയായി എഴുതി, സംസ്ഥാന സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്ത NDA ആണ് ഇന്ത്യയിൽ നടപ്പാക്കാവുന്നത്. നിങ്ങളുടെ NDA സ്റ്റാമ്പ് ചെയ്തോ?",
 cap_en="A supplier in another state signed the NDA as a PDF, and nobody stamped it. An NDA is enforceable in India when properly drafted and stamped under the state's stamp law. Is your NDA stamped: yes or no?",
 cap_mg="Mattoru samsthaanathe supplier NDA PDF-il oppittu, aarum stamp cheythilla. Shariyaayi ezhuthi, state stamp niyamaprakaaram stamp cheytha NDA aanu India-yil nadappaakkaavunnathu. Ningalude NDA stamp cheytho?")

# faq: "the NDA is signed, so I can send the whole source code now"
duo("ndd043", "agency_client", "B", "mall", "\"NDA ഒപ്പിട്ടു.\nഇനി കോഡ് മുഴുവൻ\nഅയക്കാം!\"", [
 ("A","wide","ജാഫറേ, ആശുപത്രി ഗ്രൂപ്പ് NDA ഒപ്പിട്ടു. ഇനി നമ്മുടെ ബുക്കിംഗ് സോഫ്റ്റ്‌വെയറിന്റെ കോഡ് മുഴുവൻ അയക്കാം."),
 ("V","V","സുമയ്യാ, അവർക്ക് ടെസ്റ്റ് ചെയ്യാൻ വേണ്ടത് ഡെമോ ലോഗിനും ഡാറ്റാ ഫോർമാറ്റും മാത്രമല്ലേ?"),
 ("A","A","NDA ഉള്ളപ്പോൾ എന്തിന് പേടിക്കണം?"),
 ("V","wide","NDA എഴുതിയ രഹസ്യം മാത്രം കാക്കും, അത് ലംഘിച്ചാൽ പരിഹാരം തരും. പക്ഷേ ആവശ്യമുള്ളത് മാത്രം അയക്കുന്നതാണ് ആദ്യ സുരക്ഷ."),
 ("A","A","NDA പൂട്ട്, പക്ഷേ വാതിൽ തുറന്നിടേണ്ട."),
 ("V","V","ഒപ്പ് കിട്ടിയാൽ മുഴുവൻ കൊടുക്കണം എന്നില്ല.")],
 "NDA പൂട്ട്,\nവാതിൽ തുറന്നിടേണ്ട", CTA_SECRET, theme="faq",
 cap_ml="ക്ലയന്റ് NDA ഒപ്പിട്ടാൽ മുഴുവൻ കോഡും അയക്കണോ? NDA നിർവചിച്ച രഹസ്യം മാത്രം കാക്കും, ലംഘിച്ചാൽ പരിഹാരം തരും. ജോലിക്ക് വേണ്ടത് മാത്രം അയക്കൂ. നിങ്ങൾ കഴിഞ്ഞ തവണ അധികം അയച്ചോ?",
 cap_en="The client signed the NDA, so should you send the whole codebase? An NDA protects only what it defines and gives a remedy if broken. Send only what the work needs. Ever sent more than you had to?",
 cap_mg="Client NDA oppittaal muzhuvan code-um ayakkano? NDA nirvachicha rahasyam maathram kaakkum, lamghichaal parihaaram tharum. Joliykku vendathu maathram ayakkoo. Ningal kazhinja thavana adhikam ayacho?")

# new (d904 pattern): a surfboard shaper's coconut-fibre resin mix and a foreign brand's workshop tour
duo("ndd044", "freelancer_nda", "C", "beach", "വിദേശ ബ്രാൻഡ്:\n\"വർക്ക്ഷോപ്പ് കാണണം\".\nചകിരി റെസിൻ കൂട്ട്", [
 ("A","wide","നിഖിലേ, ആ വിദേശ സർഫ് ബ്രാൻഡ് നിന്റെ ബോർഡ് വർക്ക്ഷോപ്പ് കാണാൻ നാളെ വരുന്നു. ചകിരി റെസിൻ കൂട്ട് അവർക്ക് ഇഷ്ടപ്പെട്ടു."),
 ("V","V","ദിവ്യേ, അവർക്ക് ആ കൂട്ട് കണ്ടാൽ മതി. കടലിൽ എല്ലാരും എന്റെ ബോർഡ് കണ്ടിട്ടുണ്ടല്ലോ."),
 ("A","A","ബോർഡ് എല്ലാരും കണ്ടു. കൂട്ട് ആരും കണ്ടില്ല. അതാ വ്യത്യാസം."),
 ("V","wide","അപ്പോ ടൂറിന് മുമ്പ് വൺ-വേ NDA. പൊതുവായ ബോർഡ് ഡിസൈൻ സംരക്ഷിക്കാനാവില്ല, പക്ഷേ റെസിൻ അനുപാതം രഹസ്യമായി എഴുതാം."),
 ("A","A","ആകൃതി കടലിന്, കൂട്ട് കരാറിന്."),
 ("V","V","തിര എല്ലാവർക്കും, കൂട്ട് എനിക്ക് മാത്രം.")],
 "തിര എല്ലാവർക്കും,\nകൂട്ട് നിനക്ക് മാത്രം", CTA_SECRET, theme="new",
 cap_ml="ബീച്ചിൽ എല്ലാവരും കണ്ട സർഫ്ബോർഡിന്റെ ആകൃതി രഹസ്യമല്ല; പൊതുവായത് NDA-യ്ക്ക് കാക്കാനാവില്ല. പക്ഷേ ചകിരി റെസിൻ അനുപാതം വൺ-വേ NDA-യിൽ രഹസ്യമായി എഴുതാം, വർക്ക്ഷോപ്പ് ടൂറിന് മുമ്പ്. നിങ്ങളുടെ കൈപ്പണിയിലെ രഹസ്യം?",
 cap_en="A surfboard shape everyone has seen on the beach is not a secret, and an NDA cannot protect what is already public. The coconut-fibre resin ratio can be named as confidential in a one-way NDA before the workshop tour. What's the secret in your craft?",
 cap_mg="Beach-il ellaavarum kanda surfboard-inte aakruthi rahasyamalla; pothuvaayathu NDA-kku kaakkaanaavilla. Pakshe chakiri resin anupaatham one-way NDA-yil rahasyamaayi ezhuthaam, workshop tour-inu mumpu. Ningalude kaippaniyile rahasyam?")

# new (d904 pattern): a snake-boat race team's training plan and a rival's "friendly visit"
duo("ndd045", "employee_nda", "A", "canteen", "എതിർ ടീമിന്റെ\nതുഴക്കാരൻ ചോദിച്ചു:\n\"പ്രാക്ടീസിന് വരാമോ?\"", [
 ("A","wide","അമലേ, എതിർ വള്ളത്തിലെ ഒരു തുഴക്കാരൻ നമ്മുടെ ടീമിൽ ചേരാൻ വരുന്നു. ആദ്യ ദിവസം മുതൽ പ്രാക്ടീസ് കാണണം എന്ന്."),
 ("V","V","ആതിരേ, നമ്മുടെ സ്റ്റാർട്ടിംഗ് താളവും ഡയറ്റ് പ്ലാനും അയാൾ അങ്ങോട്ട് കൊണ്ടുപോയാലോ?"),
 ("A","A","വള്ളംകളി എല്ലാരും ടിവിയിൽ കാണുന്നതല്ലേ? എന്ത് രഹസ്യം?"),
 ("V","wide","റേസ് പൊതുവാണ്, അത് കാക്കാനാവില്ല. പക്ഷേ പ്രാക്ടീസ് പ്ലാൻ രഹസ്യമായി NDA-യിൽ എഴുതാം, എത്ര കാലം എന്നും."),
 ("A","A","തുഴ കൊടുക്കും മുമ്പ് ഒപ്പ് വാങ്ങാം."),
 ("V","V","റേസ് എല്ലാവർക്കും കാണാം, താളം ടീമിന് മാത്രം.")],
 "റേസ് പൊതു,\nതാളം ടീമിന് മാത്രം", CTA_NDA, theme="new",
 cap_ml="വള്ളംകളി റേസ് എല്ലാവരും കാണും, അത് NDA-യ്ക്ക് കാക്കാനാവില്ല. പക്ഷേ ടീമിന്റെ പ്രാക്ടീസ് പ്ലാനും താളവും രഹസ്യമായി NDA-യിൽ എഴുതാം, കാലാവധിയോടെ. പുതിയ ആൾ ചേരും മുമ്പ് ഒപ്പ്. നിങ്ങളുടെ ടീമിന്റെ രഹസ്യം എന്താണ്?",
 cap_en="Everyone watches the snake-boat race, and an NDA cannot protect what is public. But a team's practice plan and rhythm can be named as confidential in an NDA, with a duration, signed before a new member joins. What's your team's secret?",
 cap_mg="Vallamkali race ellaavarum kaanum, athu NDA-kku kaakkaanaavilla. Pakshe team-inte practice plan-um thaalavum rahasyamaayi NDA-yil ezhuthaam, kaalaavadhiyode. Puthiya aal cherum mumpu oppu. Ningalude team-inte rahasyam enthaanu?")
