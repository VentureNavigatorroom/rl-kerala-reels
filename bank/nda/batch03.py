# NDA batch 03 (19 Nov, month backlog). Facts only from topics.FACTS_NDA. No fees. People, firms and towns invented.
# Facts only from topics.FACTS_NDA. Never promise a court outcome. People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

duo("ndd006", "founder_pitching", "B", "cafe", "ഇൻവെസ്റ്റർ NDA\nഒപ്പിടാൻ\nവിസമ്മതിച്ചു", [
 ("A","wide","റോഷാ, പിച്ചിന് മുമ്പ് NDA ചോദിച്ചു. ഇൻവെസ്റ്റർ ഒപ്പിടില്ലെന്ന് പറഞ്ഞു."),
 ("V","V","ആൽവിനേ, അത് സാധാരണയാണ്. പല ഇൻവെസ്റ്റർമാരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല."),
 ("A","A","അപ്പോ എന്റെ ഐഡിയ സുരക്ഷിതമല്ലേ?"),
 ("V","V","പിച്ചിൽ പ്രധാന ആശയം പറയാം. രഹസ്യ വിവരങ്ങൾ പിന്നീടുള്ള ഘട്ടത്തിൽ."),
 ("A","wide","അപ്പോ എന്ത് പറയണം എന്ന് മുൻകൂട്ടി തീരുമാനിക്കണം."),
 ("V","wide","എല്ലാം ആദ്യ മീറ്റിംഗിൽ പറയേണ്ട.")],
 "പിച്ചിൽ ആശയം,\nരഹസ്യം പിന്നീട്", CTA_SECRET, theme="faq",
 cap_ml="പല നിക്ഷേപകരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. ആദ്യ മീറ്റിംഗിൽ എന്ത് പങ്കുവെക്കണം എന്ന് മുൻകൂട്ടി തീരുമാനിക്കൂ. നിങ്ങൾ പിച്ചിന് തയ്യാറെടുക്കുകയാണോ?",
 cap_en="Many investors won't sign an NDA at pitch stage. Decide in advance what to share in a first meeting and what to keep for later. Are you preparing a pitch?",
 cap_mg="Pala investors-um pitch stage-il NDA oppidaarilla. Aadya meeting-il enthu parayanam ennu munkootti theerumaanikku. Ningal pitch-nu thayyaaraakunnundo?")

duo("ndd007", "agency_client", "B", "photocopy", "ഇന്റർനെറ്റിലുള്ള\nകാര്യത്തിന്\nNDA?", [
 ("A","wide","ഉണ്ണീ, ക്ലയന്റ് NDA-യിൽ അവരുടെ വെബ്സൈറ്റിലെ വിവരങ്ങളും രഹസ്യമെന്ന് എഴുതി."),
 ("V","V","അശ്വതീ, എല്ലാവർക്കും കാണാവുന്നത് എങ്ങനെ രഹസ്യമാകും?"),
 ("A","A","അതെ. ഇതിനകം പൊതുവായ വിവരം NDA കൊണ്ട് സംരക്ഷിക്കാനാവില്ല."),
 ("V","V","അപ്പോ ആ ഭാഗം ഒഴിവാക്കണമെന്ന് ആവശ്യപ്പെടാം."),
 ("A","wide","അതെ. ഒഴിവാക്കലുകൾ വ്യക്തമായി എഴുതണം."),
 ("V","wide","എല്ലാം രഹസ്യമാക്കിയാൽ ഒന്നും രഹസ്യമല്ല.")],
 "പൊതുവായത്\nരഹസ്യമാകില്ല", CTA_NDA, theme="faq",
 cap_ml="ഇതിനകം പൊതുവായ വിവരം NDA കൊണ്ട് സംരക്ഷിക്കാനാവില്ല. പൊതു വിവരവും സ്വതന്ത്രമായി വികസിപ്പിച്ചതും ഒഴിവാക്കലായി എഴുതണം. നിങ്ങളുടെ NDA-യിൽ ഒഴിവാക്കലുകൾ ഉണ്ടോ?",
 cap_en="An NDA cannot protect what is already public. Good NDAs list exclusions such as public and independently developed information. Does yours have exclusions?",
 cap_mg="Ithinakam public aaya vivaram NDA kondu samrakshikkaan pattilla. Exclusions vyakthamaayi ezhuthanam. Ningalude NDA-yil exclusions undo?")

duo("ndd008", "vendor_supplier", "A", "bakery", "റെസിപ്പി സപ്ലയറിന്.\nNDA ഒരു\nവശത്ത് മാത്രം", [
 ("A","wide","സാബുച്ചേട്ടാ, നമ്മുടെ കേക്ക് റെസിപ്പി പുതിയ ഫാക്ടറിക്ക് കൊടുക്കണം."),
 ("V","V","ജിഷേ, അവർ നമ്മോട് ഒന്നും പറയുന്നില്ലല്ലോ, പിന്നെ രണ്ട് വശത്തുള്ള NDA വേണോ?"),
 ("A","A","വേണ്ട. ഒരു വശം മാത്രം വിവരം കൊടുക്കുമ്പോൾ വൺ-വേ NDA മതി."),
 ("V","V","രണ്ടുപേരും രഹസ്യം പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ."),
 ("A","wide","അതെ. ആര് എന്ത് കൊടുക്കുന്നു എന്ന് നോക്കി തീരുമാനിക്കാം."),
 ("V","wide","രഹസ്യം ആരുടേത്, സംരക്ഷണം അവർക്ക്.")],
 "വൺ-വേയോ മ്യൂച്വലോ,\nആര് പങ്കുവെക്കുന്നു?", CTA_NDA, theme="new",
 cap_ml="NDA ഒരു വശത്ത് മാത്രം (വൺ-വേ) അല്ലെങ്കിൽ രണ്ട് വശത്തും (മ്യൂച്വൽ) ആകാം. ആര് രഹസ്യം പങ്കുവെക്കുന്നു എന്ന് നോക്കി തീരുമാനിക്കൂ. നിങ്ങളുടെ കാര്യത്തിൽ ആരാണ് വിവരം നൽകുന്നത്?",
 cap_en="An NDA can be one-way or mutual. Choose based on who is sharing confidential information. In your deal, who is sharing the secrets?",
 cap_mg="NDA one-way allenkil mutual aakaam. Aaru rahasyam share cheyyunnu ennu nokki theerumaanikku. Ningalude kaaryathil aaru vivaram kodukkunnu?")

duo("ndd009", "freelancer_nda", "A", "hostel", "NDA-യിൽ\nകാലാവധി ഇല്ല.\nഎത്ര കാലം?", [
 ("A","wide","സഞ്ജൂ, ഈ ക്ലയന്റിന്റെ NDA-യിൽ എത്ര കാലം രഹസ്യം സൂക്ഷിക്കണം എന്ന് ഇല്ല."),
 ("V","V","അലീനേ, അപ്പോ എന്നെന്നേക്കുമാണോ?"),
 ("A","A","അത് വ്യക്തമല്ലെങ്കിൽ പിന്നീട് തർക്കമാകും. കാലാവധി എഴുതണം."),
 ("V","V","എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത്, മൂന്നും വേണം."),
 ("A","wide","അതെ. ഒപ്പിടും മുമ്പ് ചോദിക്കാം."),
 ("V","wide","അവ്യക്തമായ NDA ആർക്കും ഗുണമില്ല.")],
 "എന്ത്, എത്ര കാലം,\nലംഘിച്ചാൽ എന്ത്", CTA_NDA, theme="faq",
 cap_ml="നല്ല NDA-യിൽ രഹസ്യ വിവരം എന്താണ്, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത് പരിഹാരം എന്നിവ വ്യക്തമായിരിക്കണം. നിങ്ങളുടെ NDA-യിൽ കാലാവധി എഴുതിയിട്ടുണ്ടോ?",
 cap_en="A good NDA defines what is confidential, for how long, and the remedy if it is broken. Does your NDA state a duration?",
 cap_mg="Nalla NDA-yil rahasya vivaram enthu, ethra kaalam, lamghichaal enthu ennivavyaktham venam. Ningalude NDA-yil kaalaavadhi undo?")

duo("ndd010", "agency_client", "A", "metro", "NDA ലംഘിച്ചു.\nഇനി എന്ത് ചെയ്യാം?", [
 ("A","wide","കിരണേ, മുൻ പങ്കാളി നമ്മുടെ ക്ലയന്റ് ലിസ്റ്റ് മറ്റൊരു കമ്പനിക്ക് കൊടുത്തു. NDA ഉണ്ട്."),
 ("V","V","അഞ്ജലീ, NDA-യിൽ പരിഹാരം എന്ത് എഴുതിയിട്ടുണ്ട്?"),
 ("A","A","ഇൻജങ്ഷൻ എന്ന് എഴുതിയിട്ടുണ്ട്."),
 ("V","V","അപ്പോ ഉപയോഗം തടയാൻ കോടതിയെ സമീപിക്കാം. വക്കീലിനോട് ഉടൻ ചോദിക്കൂ."),
 ("A","wide","അതെ. നന്നായി എഴുതിയ NDA ഇവിടെ സഹായിക്കും."),
 ("V","wide","എഴുതിയതാണ് രക്ഷ.")],
 "ലംഘിച്ചാൽ ഇൻജങ്ഷൻ,\nഎഴുതിയിട്ടുണ്ടോ?", CTA_SECRET, theme="new",
 cap_ml="NDA ലംഘിച്ചാൽ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരങ്ങൾ NDA-യിൽ എഴുതിയിരിക്കണം. ലംഘനം കണ്ടാൽ ഉടൻ വക്കീലിനോട് ചോദിക്കൂ. നിങ്ങളുടെ NDA-യിൽ പരിഹാരം എഴുതിയിട്ടുണ്ടോ?",
 cap_en="Remedies such as an injunction should be written into the NDA. If it is breached, speak to a lawyer quickly. Does your NDA state a remedy?",
 cap_mg="NDA lamghichaal injunction pole ulla parihaarangal NDA-yil ezhuthanam. Lamghanam kandaal udan vakkeelinodu chodikku. Ningalude NDA-yil parihaaram undo?")

duo("ndd011", "employee_nda", "B", "hospital", "പുതിയ ജീവനക്കാരന്\nNDA വേണോ?\nഡാറ്റ ഉണ്ട്", [
 ("A","wide","ജോസഫേ, ക്ലിനിക്കിൽ പുതിയ റിസപ്ഷനിസ്റ്റ്. രോഗികളുടെ വിവരം കാണും."),
 ("V","V","ലക്ഷ്മീ, അപ്പോ ജോലിയിൽ ചേരുമ്പോൾ തന്നെ NDA ഒപ്പിടുവിക്കാം."),
 ("A","A","ജോലി വിട്ടാലും രഹസ്യം സൂക്ഷിക്കണം എന്ന് എഴുതാമോ?"),
 ("V","V","എഴുതാം. രഹസ്യാത്മകത ജോലിക്ക് ശേഷവും ബാധകമാക്കാം."),
 ("A","wide","അതെ. ആദ്യ ദിവസം തന്നെ ഒപ്പിടൽ."),
 ("V","wide","വിവരം കാണും മുമ്പ് ഒപ്പ്.")],
 "വിവരം കാണും മുമ്പ്\nNDA ഒപ്പിടൂ", CTA_NDA, theme="new",
 cap_ml="ജീവനക്കാർ രഹസ്യ വിവരം കാണുന്നതിന് മുമ്പ് NDA ഒപ്പിടുവിക്കൂ. രഹസ്യാത്മക ബാധ്യത ജോലി വിട്ട ശേഷവും തുടരാം. നിങ്ങളുടെ ജീവനക്കാർ NDA ഒപ്പിട്ടിട്ടുണ്ടോ?",
 cap_en="Have staff sign an NDA before they see confidential information. Confidentiality can continue after they leave. Have your employees signed one?",
 cap_mg="Jeevanakkar rahasya vivaram kaanunnathinu mumpu NDA oppiduvikku. Confidentiality joli vitta seshavum thudaraam. Ningalude staff NDA oppittittundo?")

duo("ndd012", "freelancer_nda", "B", "rooftop", "സ്റ്റാമ്പ് പേപ്പർ\nഇല്ലാത്ത NDA\nകോടതിയിൽ?", [
 ("A","wide","ശ്യാമേ, ഈമെയിലിൽ ഒപ്പിട്ട NDA മതിയോ? സ്റ്റാമ്പ് ഒന്നും ഇല്ല."),
 ("V","V","ആര്യേ, ഇന്ത്യയിൽ NDA ഒരു കരാറാണ്. സംസ്ഥാനത്തിന്റെ സ്റ്റാമ്പ് നിയമം പാലിക്കണം."),
 ("A","A","സ്റ്റാമ്പ് ഇല്ലെങ്കിൽ എന്ത് സംഭവിക്കും?"),
 ("V","V","തർക്കം വന്നാൽ തെളിവായി ഉപയോഗിക്കുമ്പോൾ പ്രശ്നം വരാം. ശരിയായി സ്റ്റാമ്പ് ചെയ്യൂ."),
 ("A","wide","അപ്പോ എഴുത്തും സ്റ്റാമ്പും രണ്ടും ശരിയാകണം."),
 ("V","wide","ഒപ്പ് മാത്രം പോരാ.")],
 "എഴുത്ത് ശരി,\nസ്റ്റാമ്പും ശരി", CTA_NDA, theme="faq",
 cap_ml="ഇന്ത്യയിൽ NDA നടപ്പാക്കാൻ ശരിയായി എഴുതുകയും സംസ്ഥാനത്തിന്റെ സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്യുകയും വേണം. നിങ്ങളുടെ NDA സ്റ്റാമ്പ് ചെയ്തതാണോ?",
 cap_en="In India, an NDA is enforceable when properly drafted and stamped under the state's stamp law. Is your NDA stamped?",
 cap_mg="India-yil NDA nadappakkaan shariyaayi ezhuthanam, state stamp niyamam prakaaram stamp cheyyanam. Ningalude NDA stamp cheythatho?")

duo("ndd013", "founder_pitching", "A", "home", "കോ-ഫൗണ്ടറെ\nതേടുന്നു. ഐഡിയ\nപറയും മുമ്പ്", [
 ("A","wide","അരുണേ, ഒരു ടെക്കിയെ കോ-ഫൗണ്ടറായി കാണുന്നു. ഐഡിയ മുഴുവൻ പറയണോ?"),
 ("V","V","സ്നേഹേ, ആദ്യം ഒരു ലളിതമായ NDA ഒപ്പിടാമോ എന്ന് ചോദിക്കാം."),
 ("A","A","അത് ചോദിച്ചാൽ മോശമാകുമോ?"),
 ("V","V","ഇല്ല. പങ്കാളിയാകാൻ പോകുന്നവർ സാധാരണ സമ്മതിക്കും. മ്യൂച്വൽ ആക്കാം."),
 ("A","wide","അതെ. രണ്ടുപേരുടെയും ആശയം സുരക്ഷിതം."),
 ("V","wide","വിശ്വാസം ഉണ്ട്, രേഖയും വേണം.")],
 "പങ്കാളിയോടും\nമ്യൂച്വൽ NDA", CTA_SECRET, theme="crm",
 cap_ml="കോ-ഫൗണ്ടറായേക്കാവുന്നവരുമായി വിശദമായ ഐഡിയ പങ്കുവെക്കുന്നതിന് മുമ്പ് മ്യൂച്വൽ NDA ഒപ്പിടാം. നിങ്ങൾ കോ-ഫൗണ്ടറെ തേടുകയാണോ?",
 cap_en="Before sharing the full idea with a possible co-founder, a mutual NDA protects both of you. Are you looking for a co-founder?",
 cap_mg="Co-founder aakaan saadhyathayullavarodu idea share cheyyunnathinu mumpu mutual NDA oppidaam. Ningal co-founder-ne thedunnundo?")

duo("ndd014", "vendor_supplier", "B", "textile", "ഡിസൈൻ അയച്ചു.\nഅടുത്ത മാസം\nഎതിരാളിയുടെ കടയിൽ", [
 ("A","wide","പ്രകാശേട്ടാ, നമ്മുടെ സാരി ഡിസൈൻ തറിക്കാരന് അയച്ചു. ഇപ്പോൾ മറ്റൊരു കടയിൽ കണ്ടു."),
 ("V","V","രമ്യേ, അയക്കുമ്പോൾ എന്തെങ്കിലും ഒപ്പിടുവിച്ചോ?"),
 ("A","A","ഇല്ല. വിശ്വാസമായിരുന്നു."),
 ("V","V","ഇനി ഡിസൈൻ അയക്കും മുമ്പ് NDA. രഹസ്യ വിവരം എന്താണെന്ന് വ്യക്തമാക്കി."),
 ("A","wide","അതെ. ഇതുവരെ പോയത് പഠിക്കാനുള്ള പാഠം."),
 ("V","wide","ഡിസൈൻ അയക്കും മുമ്പ് ഒപ്പ്.")],
 "ഡിസൈൻ അയക്കും മുമ്പ്\nNDA ഒപ്പിടൂ", CTA_SECRET, theme="crm",
 cap_ml="ഡിസൈനോ റെസിപ്പിയോ സപ്ലയർക്ക് അയക്കുന്നതിന് മുമ്പ് NDA ഒപ്പിടുവിക്കൂ. രഹസ്യ വിവരം എന്താണെന്ന് വ്യക്തമാക്കണം. നിങ്ങൾ ഇതുവരെ ഡിസൈൻ ആരുമായി പങ്കുവെച്ചു?",
 cap_en="Get an NDA signed before sending designs or recipes to a supplier, and define what counts as confidential. Who have you shared your designs with?",
 cap_mg="Design-o recipe-o supplier-nu ayakkunnathinu mumpu NDA oppiduvikku. Rahasya vivaram enthu ennu vyakthamaakkanam. Ningal design aarumaayi share cheythu?")

duo("ndd015", "freelancer_nda", "A", "library", "ക്ലയന്റിന്റെ NDA\nപോർട്ട്‌ഫോളിയോ\nതടയുമോ?", [
 ("A","wide","അനൂപേ, NDA ഒപ്പിട്ട പ്രോജക്റ്റ് എന്റെ പോർട്ട്‌ഫോളിയോയിൽ ഇടാമോ?"),
 ("V","V","ഗ്രീഷ്മേ, NDA-യിൽ എന്താണ് രഹസ്യം എന്ന് എഴുതിയിരിക്കുന്നത് നോക്കണം."),
 ("A","A","എല്ലാം രഹസ്യം എന്നാണ് എഴുതിയത്."),
 ("V","V","അപ്പോ ക്ലയന്റിന്റെ എഴുതിയ സമ്മതം വാങ്ങിയ ശേഷം മാത്രം. അടുത്ത തവണ ഇത് ആദ്യമേ ചോദിക്കൂ."),
 ("A","wide","അതെ. ഒപ്പിടും മുമ്പ് പോർട്ട്‌ഫോളിയോ ക്ലോസ് ചേർക്കാം."),
 ("V","wide","ഒപ്പിട്ട ശേഷം ചോദിക്കുന്നതിനേക്കാൾ നല്ലത് മുമ്പ്.")],
 "പോർട്ട്‌ഫോളിയോ ഉപയോഗം\nഒപ്പിടും മുമ്പ് ചോദിക്കൂ", CTA_NDA, theme="new",
 cap_ml="NDA ഒപ്പിട്ട പ്രോജക്റ്റ് പോർട്ട്‌ഫോളിയോയിൽ ഇടുന്നതിന് മുമ്പ് ക്ലയന്റിന്റെ എഴുതിയ സമ്മതം വേണം. ഒപ്പിടുന്നതിന് മുമ്പേ ഇത് ചർച്ച ചെയ്യൂ. നിങ്ങൾ ഫ്രീലാൻസറാണോ?",
 cap_en="Before putting NDA-covered work in your portfolio, get the client's written consent, or agree it before signing. Are you a freelancer?",
 cap_mg="NDA oppitta project portfolio-il idunnathinu mumpu client-nte ezhuthiya sammatham venam. Oppidunnathinu mumpe ithu charcha cheyyu. Ningal freelancer aano?")
