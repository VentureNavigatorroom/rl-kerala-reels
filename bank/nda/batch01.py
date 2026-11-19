# NDA seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_NDA. Never promise a court outcome. People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

duo("ndd001", "founder_pitching", "A", "hotellobby", "ഇൻവെസ്റ്ററോട്:\n\"ആദ്യം NDA ഒപ്പിടൂ\".\nമീറ്റിംഗ് അവിടെ തീർന്നു", [
 ("A","wide","ജെയ്സൺ ചേട്ടാ, ആ ഇൻവെസ്റ്റർ പിച്ച് കേൾക്കാതെ പോയി. ഞാൻ NDA ഒപ്പിടാൻ പറഞ്ഞതേ ഉള്ളൂ."),
 ("V","V","നീതൂ, പല ഇൻവെസ്റ്റർമാരും പിച്ച് സ്റ്റേജിൽ NDA ഒപ്പിടാറില്ല. ദിവസവും ഒരുപാട് പിച്ച് കേൾക്കുന്നവരാ."),
 ("A","A","അപ്പോ എന്റെ ഐഡിയ ആരെങ്കിലും എടുത്താലോ?"),
 ("V","V","പിച്ചിൽ പ്രശ്നവും മാർക്കറ്റും കാണിച്ചാൽ മതി. രഹസ്യമായ കോഡും ഫോർമുലയും പിന്നീട്, NDA-യോടെ."),
 ("A","wide","അടുത്ത മീറ്റിംഗിൽ ആദ്യം പിച്ച്, രഹസ്യം പിന്നീട്."),
 ("V","wide","ഐഡിയ പൂട്ടിയാൽ ഇൻവെസ്റ്ററും പൂട്ടും.")],
 "പിച്ച് സ്റ്റേജിൽ\nNDA അപൂർവം", CTA_SECRET, theme="faq",
 cap_ml="പല ഇൻവെസ്റ്റർമാരും പിച്ച് സ്റ്റേജിൽ NDA ഒപ്പിടാറില്ല. പിച്ചിൽ പ്രശ്നവും മാർക്കറ്റും കാണിക്കുക; രഹസ്യമായ കോഡും പ്രോസസും പിന്നീട്, NDA-യോടെ. നിങ്ങൾ പിച്ചിന് മുമ്പ് NDA ചോദിച്ചിട്ടുണ്ടോ?",
 cap_en="Many investors don't sign NDAs at the pitch stage. Pitch the problem and the market; share secret code or formulas later, under an NDA. Have you ever asked an investor to sign one?",
 cap_mg="Pala investors-um pitch stage-il NDA oppidaarilla. Pitch-il prashnavum market-um kaanikkuka; rahasyamaaya code-um process-um pinneedu, NDA-yode. Ningal pitch-nu mumbu NDA chodichittundo?")

duo("ndd002", "freelancer_nda", "B", "gym", "NDA ഇന്റർനെറ്റിൽ നിന്ന്\nകോപ്പി ചെയ്തു.\nസ്റ്റാമ്പ് ഇല്ല", [
 ("A","wide","ജസ്റ്റിനേ, ആ ഫിറ്റ്നസ് ആപ്പ് ക്ലയന്റിന് NDA അയച്ചു. ഇന്റർനെറ്റിലെ ഒരു ടെംപ്ലേറ്റ്."),
 ("V","V","റിയേ, സ്റ്റാമ്പ് ചെയ്തോ? നമ്മുടെ സംസ്ഥാനത്തെ സ്റ്റാമ്പ് നിയമം അനുസരിച്ച്?"),
 ("A","A","അതൊക്കെ വേണോ? ഒപ്പ് പോരേ?"),
 ("V","V","ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്ത NDA ആണ് നടപ്പാക്കാൻ പറ്റുന്നത്. എന്ത് രഹസ്യം, എത്ര കാലം എന്നും എഴുതണം."),
 ("A","wide","ഈ ടെംപ്ലേറ്റിൽ വേറെ രാജ്യത്തെ നിയമമാണല്ലോ!"),
 ("V","wide","മസിൽ മാത്രം പോരാ, പേപ്പറിനും ബലം വേണം.")],
 "ഒപ്പ് മാത്രം പോരാ\nസ്റ്റാമ്പും വേണം", CTA_NDA, theme="new",
 cap_ml="ഇന്ത്യയിൽ NDA നടപ്പാക്കാൻ ശരിയായി എഴുതണം, സംസ്ഥാനത്തെ സ്റ്റാമ്പ് നിയമം അനുസരിച്ച് സ്റ്റാമ്പ് ചെയ്യണം. ഇന്റർനെറ്റ് ടെംപ്ലേറ്റ് ഉപയോഗിക്കുന്ന ഫ്രീലാൻസർമാർ ശ്രദ്ധിക്കുക.",
 cap_en="A freelancer sends a client an NDA copied from the internet, unstamped, under another country's law. In India an NDA is enforceable when it is properly drafted and stamped under the state's stamp law.",
 cap_mg="India-yil NDA nadappaakkaan shariyaayi ezhuthanam, samsthaanathe stamp niyamam anusarichu stamp cheyyanam. Internet template use cheyyunna freelancers shraddhikkuka.")

duo("ndd003", "agency_client", "A", "metro", "NDA ഒപ്പിട്ടു. എന്നിട്ടും\nഐഡിയ മറ്റൊരു പരസ്യത്തിൽ", [
 ("A","wide","കിരണേ, നമ്മുടെ ഏജൻസിയുടെ ക്യാമ്പെയിൻ ഐഡിയ വേറൊരു പരസ്യത്തിൽ കണ്ടു. NDA ഉണ്ടായിരുന്നല്ലോ."),
 ("V","V","അഞ്ജലീ, ആ ഐഡിയ നമ്മൾ മുമ്പ് എവിടെയെങ്കിലും പോസ്റ്റ് ചെയ്തിരുന്നോ?"),
 ("A","A","ഉം... കഴിഞ്ഞ വർഷം നമ്മുടെ ഒരു റീലിൽ."),
 ("V","V","എങ്കിൽ അത് പബ്ലിക് ആയി. നേരത്തെ പബ്ലിക് ആയത് NDA-ക്ക് സംരക്ഷിക്കാൻ പറ്റില്ല."),
 ("A","wide","അപ്പോ ആദ്യം NDA, പിന്നെ പോസ്റ്റ്. തിരിച്ചല്ല."),
 ("V","wide","റീൽ ആദ്യം ഇട്ടാൽ രഹസ്യം റീലായി.")],
 "പബ്ലിക് ആയത്\nരഹസ്യമല്ല", CTA_NDA, theme="faq",
 cap_ml="നേരത്തെ പബ്ലിക് ആയ കാര്യം NDA-ക്ക് സംരക്ഷിക്കാൻ പറ്റില്ല. ഏജൻസികളും ക്രിയേറ്റർമാരും ഐഡിയ പോസ്റ്റ് ചെയ്യും മുമ്പ് ഇത് ഓർക്കുക. നിങ്ങളുടെ ഐഡിയ ആരെങ്കിലും കോപ്പി ചെയ്തിട്ടുണ്ടോ?",
 cap_en="An agency sees its campaign idea in someone else's ad, but it had already posted the idea in a reel. An NDA cannot protect what is already public. Has anyone copied your idea?",
 cap_mg="Nerathe public aaya kaaryam NDA-kku samrakshikkaan pattilla. Agencies-um creators-um idea post cheyyum mumbu ithu orkkuka. Ningalude idea aarenkilum copy cheythittundo?")

duo("ndd004", "vendor_supplier", "B", "garage", "സപ്ലയർ ചോദിച്ചു:\n\"ഞങ്ങളുടെ രഹസ്യത്തിന്\nആര് NDA തരും?\"", [
 ("A","wide","ജിതിനേ, ഇലക്ട്രിക് ഓട്ടോ കിറ്റിന്റെ ഡിസൈൻ സപ്ലയർക്ക് കൊടുക്കും മുമ്പ് NDA അയച്ചു."),
 ("V","V","ഐശ്വര്യേ, അവർ തിരിച്ചു ചോദിച്ചു: അവരുടെ മോൾഡിംഗ് പ്രോസസ് നമ്മളും കാണും. അതിനോ?"),
 ("A","A","നമ്മുടെ NDA ഒരു വഴിക്കുള്ളതാ. നമ്മുടെ രഹസ്യം മാത്രം."),
 ("V","V","രണ്ടു പേരും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ NDA. രണ്ടു പേർക്കും ഒരേ സംരക്ഷണം."),
 ("A","wide","അത് ന്യായം. ഡ്രാഫ്റ്റ് മാറ്റാം."),
 ("V","wide","സ്ക്രൂ രണ്ട് വശത്തും മുറുക്കണം.")],
 "ഒരു വഴിയോ\nരണ്ട് വഴിയോ?", CTA_NDA, theme="new",
 cap_ml="NDA ഒരു വഴിക്കോ (one-way) രണ്ട് വഴിക്കോ (mutual) ആകാം. സപ്ലയറും നിങ്ങളും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ NDA ആണ് ന്യായം. നിങ്ങളുടെ NDA ഏതാണ്?",
 cap_en="An EV kit maker sends a one-way NDA, and the supplier asks who protects its process. When both sides share secrets, a mutual NDA protects both. Which kind do you use: one-way or mutual?",
 cap_mg="NDA oru vazhikko randu vazhikko aakaam. Supplier-um ningalum rahasyam pankuvekkumbol mutual NDA aanu nyaayam. Ningalude NDA ethaanu?")

duo("ndd005", "employee_nda", "A", "pharmacy", "പോയ ജീവനക്കാരൻ\nഡോക്ടർമാരുടെ ലിസ്റ്റുമായി\nഎതിരാളിക്കൊപ്പം", [
 ("A","wide","പ്രവീൺ സാറേ, പോയ സെയിൽസ് എക്സിക്യൂട്ടീവ് നമ്മുടെ ഡോക്ടർമാരുടെ ലിസ്റ്റുമായി എതിരാളിക്കൊപ്പം ചേർന്നു."),
 ("V","V","സിനീ, അവൻ ചേർന്നപ്പോൾ NDA ഒപ്പിട്ടിരുന്നോ?"),
 ("A","A","ഒപ്പിട്ടു. ഏതൊക്കെ വിവരം രഹസ്യം എന്നും എഴുതിയിട്ടുണ്ട്."),
 ("V","V","എങ്കിൽ ആ ലിസ്റ്റ് ഉപയോഗിക്കുന്നത് തടയാൻ കോടതിയിൽ ഇൻജംഗ്ഷൻ ചോദിക്കാം."),
 ("A","wide","NDA ഇല്ലാത്ത പുതിയ രണ്ടു പേരെക്കൊണ്ട് ഇന്ന് തന്നെ ഒപ്പിടീക്കാം."),
 ("V","wide","മരുന്ന് കുറിപ്പടിയിൽ, രഹസ്യം NDA-യിൽ.")],
 "ജോയിൻ ചെയ്യുന്ന\nദിവസം NDA", CTA_SECRET, theme="new",
 cap_ml="ജീവനക്കാർ ചേരുമ്പോൾ തന്നെ NDA: ഏത് വിവരം രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത് എന്ന് എഴുതണം. ലംഘിച്ചാൽ ഇൻജംഗ്ഷൻ പോലുള്ള പരിഹാരം ചോദിക്കാം. നിങ്ങളുടെ ടീമിന് NDA ഉണ്ടോ?",
 cap_en="A sales executive leaves with the client list. A signed employee NDA that defines confidential information lets the company ask a court for remedies such as an injunction. Does your team sign NDAs when they join?",
 cap_mg="Jeevanakkaar cherumbol thanne NDA: ethu vivaram rahasyam, ethra kaalam ennu ezhuthanam. Langhichaal injunction pole ulla parihaaram chodikkaam. Ningalude team-nu NDA undo?")
