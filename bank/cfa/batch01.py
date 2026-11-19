# Co-founder agreement seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_CFA. Never decide anyone's split. cfd001 is built on STORY_THEMES #15 with changed numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

duo("cfd001", "friends_cofounders", "A", "railway", "60/40 വാട്സാപ്പിൽ.\n5 മാസം കഴിഞ്ഞ് അവൻ പോയി.\n40% കൂടെ പോയി", [
 ("A","wide","ദിനേശേട്ടാ, കോ-ഫൗണ്ടർ ജോലി വിട്ട് പോയി. പക്ഷേ 40% ഷെയർ ഇപ്പോഴും അവന്റെ പേരിൽ."),
 ("V","V","ഷീബേ, എഗ്രിമെന്റിൽ വെസ്റ്റിംഗ് ഉണ്ടായിരുന്നോ?"),
 ("A","A","എഗ്രിമെന്റ് ഇല്ല. വാട്സാപ്പിൽ 60/40 എന്ന് ഒരു മെസേജ് മാത്രം."),
 ("V","V","വെസ്റ്റിംഗ് ഉണ്ടെങ്കിൽ ഷെയർ സമയം കൊണ്ട് കിട്ടും. സാധാരണ 4 വർഷം, ഒരു വർഷം ക്ലിഫ്. നേരത്തെ പോയാൽ ബാക്കി തിരിച്ചുവാങ്ങാം."),
 ("A","wide","5 മാസം കൊണ്ട് പോയാൽ ക്ലിഫ് പോലും കടന്നില്ലല്ലോ."),
 ("V","wide","ട്രെയിൻ പോയി, ടിക്കറ്റ് അവന്റെ കയ്യിൽ.")],
 "വാട്സാപ്പ് മെസേജ്\nഎഗ്രിമെന്റ് അല്ല", CTA_VESTING, theme="crm",
 cap_ml="കോ-ഫൗണ്ടർമാരുടെ ഷെയർ വാട്സാപ്പിൽ മാത്രം തീരുമാനിച്ചാൽ, ഒരാൾ പോകുമ്പോൾ ഷെയറും കൂടെ പോകും. വെസ്റ്റിംഗ് (സാധാരണ 4 വർഷം, ഒരു വർഷം ക്ലിഫ്) എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ സ്പ്ലിറ്റ് എഴുതിയിട്ടുണ്ടോ?",
 cap_en="A 60/40 split agreed on WhatsApp, and the co-founder leaves after 5 months still holding 40%. Vesting (commonly 4 years with a 1-year cliff) in a written co-founder agreement prevents this. Is your split in writing?",
 cap_mg="Co-founders-nte share WhatsApp-il maathram theerumaanichaal, oraal pokumbol share-um koode pokum. Vesting (saadhaarana 4 varsham, oru varsham cliff) agreement-il ezhuthanam. Ningalude split ezhuthiyittundo?")

duo("cfd002", "tech_nontech", "B", "classroom", "കോഡ് എഴുതിയത് അവൻ.\nഅവൻ പോയപ്പോൾ\nകോഡും കൊണ്ടുപോയി", [
 ("A","wide","ആദർശേ, ആപ്പിന്റെ കോഡ് മുഴുവൻ എഴുതിയ കോ-ഫൗണ്ടർ പോയി. ഇപ്പോ പറയുന്നു കോഡ് അവന്റേതാണെന്ന്."),
 ("V","V","നിമ്മീ, കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ ഐപി കമ്പനിക്ക് എന്ന് എഴുതിയിരുന്നോ?"),
 ("A","A","എഗ്രിമെന്റോ? ഞങ്ങൾ ഒരേ ബെഞ്ചിൽ ഇരുന്നവരാ."),
 ("V","V","ബെഞ്ച് സൗഹൃദം രേഖയല്ല. കോഡും ഡിസൈനും ബ്രാൻഡും തുടക്കത്തിൽ തന്നെ കമ്പനിക്ക് അസൈൻ ചെയ്യണം."),
 ("A","wide","ഇനി പുതിയ ഡെവലപ്പർ വന്നാൽ ആദ്യം അത്."),
 ("V","wide","ക്ലാസ് നോട്ട് ഷെയർ ചെയ്യാം, കോഡ് അങ്ങനെയല്ല.")],
 "കോഡ് കമ്പനിയുടേത്\nഎന്ന് എഴുതണം", CTA_COFOUNDER, theme="new",
 cap_ml="ടെക് കോ-ഫൗണ്ടർ എഴുതിയ കോഡ് കമ്പനിയുടേതാകാൻ എഗ്രിമെന്റിൽ ഐപി കമ്പനിക്ക് അസൈൻ ചെയ്യണം. കോഡ്, ഡിസൈൻ, ബ്രാൻഡ് എല്ലാം. നിങ്ങളുടെ ടീമിൽ ആരാണ് കോഡ് എഴുതുന്നത്?",
 cap_en="The co-founder who wrote all the code leaves and says the code is his. A co-founder agreement should assign all IP (code, design, brand) to the company from day one. Who writes the code in your team?",
 cap_mg="Tech co-founder ezhuthiya code company-yudethaakaan agreement-il IP company-kku assign cheyyanam. Code, design, brand ellaam. Ningalude team-il aaranu code ezhuthunnathu?")

duo("cfd003", "family_cofounders", "A", "veranda", "രണ്ട് മക്കൾ, ഒരു കമ്പനി.\nഓണത്തിന് പോലും\nമിണ്ടുന്നില്ല", [
 ("A","wide","ബാലേട്ടാ, മക്കൾ രണ്ടുപേരും ഓണസദ്യയ്ക്ക് പോലും ഒരുമിച്ചിരുന്നില്ല. കമ്പനിയുടെ കാര്യത്തിൽ വഴക്ക്."),
 ("V","V","ശാന്തേ, ആര് എന്ത് തീരുമാനിക്കും എന്ന് ആദ്യമേ എഴുതിയില്ലല്ലോ."),
 ("A","A","സ്വന്തം ചേട്ടനും അനിയനുമല്ലേ, എന്തിനാ എഴുത്ത്?"),
 ("V","V","അതുകൊണ്ടാ എഴുതേണ്ടത്. റോളുകൾ, തീരുമാനങ്ങൾ, തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും. എല്ലാം കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ."),
 ("A","wide","ഇനിയെങ്കിലും രണ്ടുപേരെയും ഒരുമിച്ചിരുത്തി എഴുതിക്കാം."),
 ("V","wide","രക്തബന്ധം ഉണ്ട്, രേഖാബന്ധം കൂടി വേണം.")],
 "കുടുംബമാണെങ്കിലും\nഎഴുതി വെക്കണം", CTA_COFOUNDER, theme="new",
 cap_ml="സഹോദരങ്ങൾ ഒരുമിച്ച് തുടങ്ങുന്ന കമ്പനിക്കും കോ-ഫൗണ്ടർ എഗ്രിമെന്റ് വേണം: റോളുകൾ, തീരുമാനങ്ങൾ, തർക്കം എങ്ങനെ തീർക്കും. കുടുംബ ബിസിനസ് ആണോ നിങ്ങളുടേത്?",
 cap_en="Two brothers, one company, and now they don't speak even at Onam. Family co-founders need a written agreement too: roles, decisions and how disputes are settled. Is yours a family business?",
 cap_mg="Sahodarangal orumichu thudangunna company-kkum co-founder agreement venam: roles, theerumaanangal, tharkkam engane theerkkum. Kudumba business aano ningaludethu?")

duo("cfd004", "late_joiner", "B", "rooftop", "രണ്ട് വർഷം കഴിഞ്ഞ്\nവന്ന CTO ചോദിച്ചു:\n\"എനിക്കും 33%?\"", [
 ("A","wide","ശ്യാമേ, പുതിയ CTO ചേർന്നു. ഞങ്ങൾ മൂന്നു പേർക്കും തുല്യ ഷെയർ വേണമെന്ന്."),
 ("V","V","ആര്യേ, എത്ര ഷെയർ എന്ന് നിങ്ങൾ തന്നെ തീരുമാനിക്കണം. പക്ഷേ എത്ര കൊടുത്താലും വെസ്റ്റിംഗോടെ."),
 ("A","A","അവൻ നല്ലവനാ. വെസ്റ്റിംഗ് വേണോ?"),
 ("V","V","നല്ലവരുടെ ജീവിതവും മാറും. 4 വർഷം, ഒരു വർഷം ക്ലിഫ്. നേരത്തെ പോയാൽ കിട്ടാത്ത ഷെയർ തിരിച്ചുവാങ്ങാം."),
 ("A","wide","പിന്നെ അത് ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിലും ആർട്ടിക്കിൾസിലും ചേർക്കണം."),
 ("V","wide","വൈകി വന്നാലും വ്യക്തമായി വരണം.")],
 "പുതിയ കോ-ഫൗണ്ടർക്കും\nവെസ്റ്റിംഗ്", CTA_VESTING, theme="new",
 cap_ml="വൈകി ചേരുന്ന കോ-ഫൗണ്ടർക്ക് എത്ര ഷെയർ എന്നത് നിങ്ങളുടെ തീരുമാനം. പക്ഷേ എത്രയായാലും വെസ്റ്റിംഗോടെ, പിന്നെ SHA-യിലും ആർട്ടിക്കിൾസിലും. നിങ്ങൾ എത്ര കോ-ഫൗണ്ടർമാർ?",
 cap_en="A CTO joins two years in and asks for an equal share. How much is your call, but give it with vesting (commonly 4 years, 1-year cliff) and mirror it in the SHA and articles. How many co-founders are you?",
 cap_mg="Vaiki cherunna co-founder-kku ethra share ennathu ningalude theerumaanam. Pakshe ethrayaayaalum vesting-ode, pinne SHA-yilum articles-ilum. Ningal ethra co-founders?")

duo("cfd005", "remote_cofounder", "A", "airport", "കോ-ഫൗണ്ടർ പോയി.\n\"2 വർഷം ഇതേ ബിസിനസ്\nചെയ്യരുത്\" നടക്കുമോ?", [
 ("A","wide","റഫീഖേ, ഖത്തറിലുള്ള നമ്മുടെ കോ-ഫൗണ്ടർ വിട്ടുപോയി. 2 വർഷം ഇതേ ബിസിനസ് ചെയ്യരുതെന്ന് എഗ്രിമെന്റിൽ ഉണ്ട്."),
 ("V","V","ഷമീറേ, ഇന്ത്യയിൽ പോയ ശേഷമുള്ള നോൺ-കോംപീറ്റ് സാധാരണ നടപ്പാക്കാൻ പറ്റില്ല."),
 ("A","A","അപ്പോ ആ വരി വെറുതെയോ?"),
 ("V","V","പക്ഷേ രഹസ്യം സൂക്ഷിക്കണമെന്നതും നമ്മുടെ ക്ലയന്റിനെയും സ്റ്റാഫിനെയും പിടിക്കരുതെന്നതും നടപ്പാക്കാൻ കഴിയും."),
 ("A","wide","അപ്പോ എഗ്രിമെന്റിൽ ബലമുള്ളത് ആ രണ്ട് വരികളാണ്."),
 ("V","wide","അവനെ തടയാൻ പറ്റില്ല, രഹസ്യം കൊണ്ടുപോകുന്നത് തടയാം.")],
 "നോൺ-കോംപീറ്റ് ദുർബലം\nരഹസ്യം ശക്തം", CTA_COFOUNDER, theme="faq",
 cap_ml="ഇന്ത്യയിൽ കോ-ഫൗണ്ടർ പോയ ശേഷമുള്ള നോൺ-കോംപീറ്റ് സാധാരണ നടപ്പാക്കാൻ പറ്റില്ല. രഹസ്യം സൂക്ഷിക്കലും ക്ലയന്റിനെയും സ്റ്റാഫിനെയും പിടിക്കാതിരിക്കലും എഴുതാം. ഇത് നിങ്ങൾക്ക് പുതിയ അറിവാണോ?",
 cap_en="A co-founder in Qatar leaves; the agreement says no competing business for 2 years. In India a post-exit non-compete is generally not enforceable, but confidentiality and non-solicit clauses can be. Did you know this?",
 cap_mg="India-yil co-founder poya sheshamulla non-compete saadhaarana nadappaakkaan pattilla. Rahasyam sookshikkalum client-ineyum staff-ineyum pidikkaathirikkalum ezhuthaam. Ithu ningalkku puthiya arivaano?")

lst("cfl001", "friends_cofounders", "B", "കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ\nഇല്ലെങ്കിൽ വഴക്കാകുന്ന\n3 കാര്യം", [
 ("വെസ്റ്റിംഗ്", "സാധാരണ 4 വർഷം, ഒരു വർഷം ക്ലിഫ്. നേരത്തെ പോകുന്നവർ മുഴുവൻ ഷെയറുമായി പോകില്ല."),
 ("ഐപി", "കോഡ്, ഡിസൈൻ, ബ്രാൻഡ് എല്ലാം കമ്പനിയുടെ പേരിൽ."),
 ("തർക്കം", "തീരുമാനം ആര് എടുക്കും, തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും.")],
 "നിങ്ങളുടേതിൽ\nഎത്ര ഉണ്ട്?", CTA_COFOUNDER, theme="faq",
 cap_ml="കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ നിർബന്ധം: വെസ്റ്റിംഗ്, ഐപി കമ്പനിക്ക്, തർക്കം തീർക്കാനുള്ള വഴി. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ഇതിൽ എത്ര ഉണ്ട്: 0, 1, 2, 3?",
 cap_en="Three things every co-founder agreement needs: vesting, IP assigned to the company, and how decisions and disputes are settled. How many does yours have: 0, 1, 2 or 3?",
 cap_mg="Co-founder agreement-il nirbandham: vesting, IP company-kku, tharkkam theerkkaanulla vazhi. Ningalude agreement-il ithil ethra undu: 0, 1, 2, 3?")
