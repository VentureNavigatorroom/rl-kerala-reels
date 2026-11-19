# Co-founder agreements batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_CFA. Never decide a split. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

duo("cf010", "tech_nontech", "A", "photocopy", "8 പ്രൊജക്റ്റ്\nകമ്പനിക്ക് മുമ്പ്.\nഇൻവെസ്റ്റർ: \"ഇത് ആരുടേത്?\"", [
 ("A","wide","ഉണ്ണീ, ഇൻവെസ്റ്റർ ചോദിച്ചു: കമ്പനി ഉണ്ടാകും മുമ്പ് ചെയ്ത 8 ക്ലയന്റ് ഡിസൈനുകൾ ആരുടെ പേരിലാണെന്ന്."),
 ("V","V","അശ്വതീ, ഫയലൊക്കെ എന്റെ ലാപ്ടോപ്പിലുണ്ട്. അപ്പോ എന്റേതല്ലേ?"),
 ("A","A","അതാണ് പ്രശ്നം. ഇൻവെസ്റ്റർ പണം ഇടുന്നത് കമ്പനിയിലാണ്, നിന്റെ ലാപ്ടോപ്പിലല്ല."),
 ("V","wide","എങ്കിൽ കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതാം: മുമ്പ് ചെയ്തതടക്കം എല്ലാ IP-യും കമ്പനിക്ക് അസൈൻ ചെയ്യുന്നു."),
 ("A","A","ലാപ്ടോപ്പ് നിന്റേത്, ഡിസൈൻ കമ്പനിയുടേത്.")],
 "ലാപ്ടോപ്പ് നിന്റേത്,\nഡിസൈൻ കമ്പനിയുടേത്", CTA_COFOUNDER, theme="crm",
 cap_ml="കമ്പനി രജിസ്റ്റർ ചെയ്യും മുമ്പ് ചെയ്ത ക്ലയന്റ് ജോലികൾ ഒരു കോ-ഫൗണ്ടറുടെ ലാപ്ടോപ്പിൽ. ഇൻവെസ്റ്റർ ചോദിക്കുന്നു: ഇത് ആരുടേത്? കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ മുമ്പ് ചെയ്തതടക്കം എല്ലാ IP-യും കമ്പനിക്ക് അസൈൻ ചെയ്യണം. നിങ്ങളുടെ ഫയലുകൾ ആരുടെ പേരിൽ?",
 cap_en="A design studio did 8 client projects before registering the company, and the files sit on one co-founder's laptop. The investor asks who owns them. A co-founder agreement should assign all IP to the company, including work done before incorporation. Whose name are your files under?",
 cap_mg="Company register cheyyum mumpu cheytha client joli oru co-founder-nte laptop-il. Investor chodikkunnu: ithu aarudethu? Co-founder agreement-il mumpu cheythathadakkam ella IP-yum company-kku assign cheyyanam. Ningalude files aarude peril?")

duo("cf011", "family_cofounders", "B", "homestay", "കസിൻസ് ചേർന്ന്\nഹോംസ്റ്റേ കമ്പനി.\nഇപ്പോ വക്കീൽ നോട്ടീസ്", [
 ("A","wide","ജോമോനേ, ഒരു മുറിയുടെ ബുക്കിംഗിന് തുടങ്ങിയ വഴക്ക് ഇപ്പോ വക്കീൽ നോട്ടീസ് വരെ എത്തി."),
 ("V","V","ടീനാ, നമ്മൾ കസിൻസ് അല്ലേ. വഴക്ക് വരുമെന്ന് ആര് കരുതി?"),
 ("A","A","വഴക്ക് വന്നാൽ എങ്ങനെ തീർക്കും എന്ന് നമ്മൾ ഒരിടത്തും എഴുതിയില്ല."),
 ("V","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തർക്ക പരിഹാര രീതി വേണം. അത് സ്നേഹമുള്ള സമയത്ത് എഴുതണം."),
 ("A","A","അടുത്ത തവണ ആദ്യം കരാർ, പിന്നെ കേക്ക്."),
 ("V","wide","ബുക്കിംഗ് ഒരു മുറി, വഴക്ക് മുഴുവൻ വീട്.")],
 "ബുക്കിംഗ് ഒരു മുറി,\nവഴക്ക് മുഴുവൻ വീട്", CTA_COFOUNDER, theme="crm",
 cap_ml="കസിൻസ് ചേർന്ന് തുടങ്ങിയ ഹോംസ്റ്റേ കമ്പനി. ചെറിയ വഴക്ക് വക്കീൽ നോട്ടീസ് വരെ എത്തി, കാരണം തർക്കം എങ്ങനെ തീർക്കും എന്ന് എഴുതിയിരുന്നില്ല. കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തർക്ക പരിഹാര രീതി വേണം. നിങ്ങളുടെ കോ-ഫൗണ്ടർ ബന്ധുവാണോ?",
 cap_en="Two cousins run a homestay company, and a fight over one room booking reached a lawyer's notice because nobody wrote down how disputes would be settled. A co-founder agreement needs a dispute resolution clause, written while everyone still gets along. Is your co-founder a relative?",
 cap_mg="Cousins chernnu thudangiya homestay company. Cheriya vazhakku vakkeel notice vare ethi, kaaranam tharkkam engane theerkkum ennu ezhuthiyirunnilla. Co-founder agreement-il dispute resolution venam. Ningalude co-founder bandhuvaano?")

duo("cf012", "friends_cofounders", "A", "courier", "\"പാർട്ണറോട് ചോദിച്ചിട്ട്\nവിളിക്കാം.\" 3 ഓർഡർ\nഅങ്ങനെ പോയി", [
 ("A","wide","അരവിന്ദേ, ഇന്നും ഒരു ബൾക്ക് ക്ലയന്റ് പോയി. ഞാൻ നിന്നെ വിളിച്ചു, നീ കല്യാണത്തിലായിരുന്നു."),
 ("V","V","ജയേ, ഓരോ വലിയ ഓർഡറും രണ്ടുപേരും ഓക്കെ പറയണം എന്നല്ലേ നമ്മൾ പറഞ്ഞത്?"),
 ("A","A","പറഞ്ഞു. എഴുതിയില്ല. ഇപ്പോ ഒരു ഫോൺ കോൾ കാരണം മൂന്ന് ഓർഡർ പോയി."),
 ("V","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ റോളും തീരുമാനവും എഴുതാം: ഓർഡർ നിന്റെ റോൾ, പുതിയ പാർട്ണർ നമ്മൾ രണ്ടുപേരും."),
 ("A","A","കൊറിയർ വേഗത്തിൽ പോകും, തീരുമാനം മാത്രം പോസ്റ്റലിൽ."),
 ("V","wide","റോൾ എഴുതിയാൽ റിംഗ് കുറയും.")],
 "റോൾ എഴുതിയാൽ\nറിംഗ് കുറയും", CTA_COFOUNDER, theme="crm",
 cap_ml="ഓരോ വലിയ ഓർഡറിനും രണ്ട് കോ-ഫൗണ്ടർമാരുടെയും സമ്മതം വേണം എന്ന വാക്കാലുള്ള നിയമം. ഒരാൾ ഫോൺ എടുത്തില്ല, മൂന്ന് ഓർഡർ പോയി. കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ ആര് എന്ത് തീരുമാനിക്കും എന്ന് എഴുതണം. നിങ്ങളുടെ ടീമിൽ ആരാണ് അവസാന വാക്ക്?",
 cap_en="A courier startup's founders agreed verbally that every big order needs both of them, and three bulk orders were lost waiting for one phone call. A co-founder agreement should set out roles and who decides what. Who has the final say in your team?",
 cap_mg="Oro valiya order-num randu co-founders-nteyum sammatham venam enna vaakkaal niyamam. Oraal phone eduthilla, moonnu order poyi. Co-founder agreement-il aaru enthu theerumaanikkum ennu ezhuthanam. Ningalude team-il aaraanu avasaana vaakku?")

duo("cf013", "late_joiner", "B", "munnar", "\"കമ്പനിക്ക് മുമ്പ്\n2 വർഷം ഞാൻ പണിതു.\nഎനിക്ക് കൂടുതൽ വേണം\"", [
 ("A","wide","ബേസിലേ, ടീ ടേസ്റ്റിംഗ് ടൂർ ഞാൻ രണ്ട് വർഷം ഒറ്റയ്ക്ക് നടത്തി. എനിക്ക് കൂടുതൽ ഷെയർ വേണ്ടേ?"),
 ("V","V","സെലിനേ, ഇനി ഫുൾ ടൈം ഞാനാണ്. ഭാവിയിലെ പണി കൂടുതൽ എന്റേതല്ലേ?"),
 ("A","A","എത്ര ശതമാനം എന്ന് പുറത്തുള്ള ആർക്കും നമുക്ക് വേണ്ടി തീരുമാനിക്കാൻ പറ്റില്ല."),
 ("V","wide","ശരി. പക്ഷേ നമ്മൾ സമ്മതിക്കുന്ന വിഭജനം എഴുതണം, കൂടെ വെസ്റ്റിംഗും: വരും വർഷങ്ങളിലെ പണിയും കണക്കിൽ വരും."),
 ("A","A","പഴയ രണ്ട് വർഷവും പുതിയ നാല് വർഷവും ഒരേ പേപ്പറിൽ."),
 ("V","wide","ചായ കടുപ്പം പോലെ, ഷെയറും ചർച്ച ചെയ്ത് മതി.")],
 "ശതമാനം നിങ്ങളുടേത്,\nവെസ്റ്റിംഗ് രണ്ടുപേരുടേത്", CTA_VESTING, theme="crm",
 cap_ml="ഒരാൾ കമ്പനിക്ക് മുമ്പ് രണ്ട് വർഷം പണിതു, മറ്റേയാൾ ഇനി ഫുൾ ടൈം വരുന്നു. ഷെയർ വിഭജനം അവർ തന്നെ തീരുമാനിക്കണം; അത് വെസ്റ്റിംഗോടെ കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ ടീമിൽ ആരാണ് ആദ്യം തുടങ്ങിയത്?",
 cap_en="One founder ran the business alone for 2 years before the company; the other is now joining full-time. Only they can decide the equity split, but it should be written down with vesting, so future work counts too. Who started first in your team?",
 cap_mg="Oraal company-kku mumpu randu varsham panithu, mattoraal ini full time varunnu. Share vibhajanam avar thanne theerumaanikkanam; athu vesting-ode co-founder agreement-il ezhuthanam. Ningalude team-il aaraanu aadyam thudangiyathu?")

duo("cf014", "friends_cofounders", "B", "farm", "\"വെസ്റ്റിംഗ്\nജീവനക്കാർക്കല്ലേ?\nഞങ്ങൾ ഫൗണ്ടർമാരാ\"", [
 ("A","wide","ഗോപീ, തെങ്ങ് കയറുന്ന മെഷീൻ കമ്പനിക്ക് വെസ്റ്റിംഗ്? അത് ജീവനക്കാർക്കല്ലേ, നമ്മൾ ഫൗണ്ടർമാരല്ലേ?"),
 ("V","V","വാസുവേട്ടാ, ഫൗണ്ടർ ആറാം മാസം പോയാലും ഷെയർ മുഴുവൻ കൊണ്ടുപോകും. അതാണ് പ്രശ്നം."),
 ("A","A","അപ്പോ ബാക്കി ഇരിക്കുന്നവൻ മുഴുവൻ പണിയും ചെയ്യണം?"),
 ("V","wide","അതിനാണ് ഫൗണ്ടർ വെസ്റ്റിംഗ്. സാധാരണ രീതി നാല് വർഷം, ഒരു വർഷ ക്ലിഫ്. ഷെയർ സമയം കൊണ്ട് സ്വന്തമാകും."),
 ("A","A","അപ്പോ ഷെയറും തെങ്ങ് പോലെ, പടിപടിയായി."),
 ("V","wide","തെങ്ങ് കയറാൻ സമയം വേണം, ഷെയറിനും.")],
 "തെങ്ങ് കയറാൻ സമയം,\nഷെയറിനും സമയം", CTA_VESTING, theme="faq",
 cap_ml="വെസ്റ്റിംഗ് ജീവനക്കാർക്ക് മാത്രമാണോ? അല്ല. ഫൗണ്ടർമാർക്കും വെസ്റ്റിംഗ് വേണം; സാധാരണ രീതി നാല് വർഷം, ഒരു വർഷ ക്ലിഫ്. അല്ലെങ്കിൽ ആറാം മാസം പോകുന്ന ആളും മുഴുവൻ ഷെയർ കൊണ്ടുപോകും. നിങ്ങളുടെ ടീമിന് വെസ്റ്റിംഗ് ഉണ്ടോ?",
 cap_en="Is vesting only for employees? No. Founders need it too; a common practice is 4 years with a 1-year cliff. Without it, a co-founder who leaves in month 6 walks away with all their shares. Does your team have founder vesting?",
 cap_mg="Vesting jeevanakkaarkku maathramaano? Alla. Founders-num vesting venam; saadhaarana reethi 4 varsham, 1 varsha cliff. Allenkil aaraam maasam pokunna aalum muzhuvan share kondupokum. Ningalude team-nu vesting undo?")

duo("cf015", "late_joiner", "A", "mall", "\"നമ്മുടെ എഗ്രിമെന്റ്\nഉണ്ടല്ലോ. ആർട്ടിക്കിൾസ്\nവെറും ഫോർമാലിറ്റി\"", [
 ("A","wide","ജാഫർ, ഇൻവെസ്റ്റർ ലോയർ പറയുന്നു: നമ്മുടെ എഗ്രിമെന്റിലെ ഷെയർ നിയമം ആർട്ടിക്കിൾസിൽ ഇല്ല."),
 ("V","V","സുമയ്യ, നമ്മൾ രണ്ടുപേരും ഒപ്പിട്ടതല്ലേ. ആർട്ടിക്കിൾസ് വെറും ഫോർമാലിറ്റി അല്ലേ?"),
 ("A","A","കമ്പനി ആദ്യം നോക്കുന്നത് ആർട്ടിക്കിൾസ് ആണ്. അവിടെ ഇല്ലെങ്കിൽ നമ്മുടെ നിയമം ദുർബലം."),
 ("V","wide","അപ്പോ കോ-ഫൗണ്ടർ എഗ്രിമെന്റിലെ ഷെയർ അവകാശങ്ങൾ SHA-യിലും ആർട്ടിക്കിൾസിലും അതേപോലെ ചേർക്കണം."),
 ("A","A","ഒരു വാക്ക്, മൂന്ന് രേഖ, ഒരേ അർത്ഥം."),
 ("V","wide","എഗ്രിമെന്റ് പറയും, ആർട്ടിക്കിൾസ് ഉറപ്പിക്കും.")],
 "എഗ്രിമെന്റ് പറയും,\nആർട്ടിക്കിൾസ് ഉറപ്പിക്കും", CTA_COFOUNDER, theme="faq",
 cap_ml="കോ-ഫൗണ്ടർ എഗ്രിമെന്റ് ഉണ്ടെങ്കിൽ ആർട്ടിക്കിൾസ് വെറും ഫോർമാലിറ്റിയാണോ? അല്ല. എഗ്രിമെന്റിലെ ഷെയർ അവകാശങ്ങൾ SHA-യിലും കമ്പനി ആർട്ടിക്കിൾസിലും അതേപോലെ വരണം. നിങ്ങളുടെ ആർട്ടിക്കിൾസ് അപ്ഡേറ്റ് ആണോ?",
 cap_en="If you have a co-founder agreement, are the articles just a formality? No. The share rights in the agreement should be mirrored in the shareholders' agreement and the company's articles. Are your articles up to date?",
 cap_mg="Co-founder agreement undenkil articles verum formality aano? Alla. Agreement-ile share rights SHA-yilum company articles-ilum athepole varanam. Ningalude articles update aano?")

duo("cf016", "tech_nontech", "B", "park", "കോ-ഫൗണ്ടർ പോയി.\n\"എന്റെ ഷെയർ തിരികെ\nവാങ്ങാൻ ആര് പറഞ്ഞു?\"", [
 ("A","wide","അനന്തൂ, തോൽപ്പാവക്കൂത്ത് ആനിമേഷൻ സ്റ്റുഡിയോ വിട്ട് കിരൺ പോയി. ഷെയർ മുഴുവൻ കയ്യിൽ വെക്കുമെന്ന്."),
 ("V","V","ഗായത്രീ, അവൻ ഒന്നര വർഷമേ നിന്നുള്ളൂ. ബാക്കി ഷെയർ എങ്ങനെ അവന്റേതാകും?"),
 ("A","A","വെസ്റ്റിംഗ് പറഞ്ഞിരുന്നു. പക്ഷേ പോകുമ്പോൾ എന്ത് എന്ന് എഴുതിയില്ല."),
 ("V","wide","അതിനാണ് ലീവർ ക്ലോസ്: പോകുമ്പോൾ വെസ്റ്റ് ആകാത്ത ഷെയർ കമ്പനി എങ്ങനെ തിരികെ വാങ്ങും എന്ന് എഴുതണം."),
 ("A","A","പാവ ആടുന്നത് ചരടിൽ, ഷെയർ ആടുന്നത് കരാറിൽ.")],
 "പാവ ആടുന്നത് ചരടിൽ,\nഷെയർ കരാറിൽ", CTA_VESTING, theme="faq",
 cap_ml="കോ-ഫൗണ്ടർ പോയാൽ വെസ്റ്റ് ആകാത്ത ഷെയർ തിരികെ വാങ്ങാമോ? കോ-ഫൗണ്ടർ എഗ്രിമെന്റിലെ ലീവർ ക്ലോസിൽ എഴുതിയിട്ടുണ്ടെങ്കിൽ. വെസ്റ്റിംഗ് മാത്രം പോരാ, പോകുമ്പോൾ എന്ത് എന്നതും വേണം. നിങ്ങളുടെ കരാറിൽ ലീവർ ക്ലോസ് ഉണ്ടോ?",
 cap_en="A co-founder of a shadow-puppet animation studio leaves after 18 months and wants to keep all his shares. Unvested shares can be bought back only if the leaver clause in the co-founder agreement says how. Does your agreement have one?",
 cap_mg="Co-founder poyaal vest aakaatha share thirike vaangaamo? Co-founder agreement-ile leaver clause-il ezhuthiyittundenkil. Vesting maathram poraa, pokumbol enthu ennathum venam. Ningalude agreement-il leaver clause undo?")

duo("cf017", "friends_cofounders", "A", "hostel", "കോ-ഫൗണ്ടർ പോയി.\nകൂടെ 140 പേരന്റ്സിന്റെ\nനമ്പറും", [
 ("A","wide","സഞ്ജൂ, നമ്മുടെ ട്യൂഷൻ ആപ്പ് വിട്ട് നിഖിൽ പോയി. ഇപ്പോ നമ്മുടെ പേരന്റ്സിനെ ഓരോന്നായി വിളിക്കുന്നു."),
 ("V","V","അലീനാ, അവൻ സ്വന്തം ട്യൂഷൻ തുടങ്ങുന്നത് തടയാൻ പറ്റുമോ?"),
 ("A","A","പോയ ശേഷമുള്ള നോൺ-കോമ്പീറ്റ് ഇന്ത്യയിൽ പൊതുവെ നടപ്പാകില്ല."),
 ("V","wide","പക്ഷേ നമ്മുടെ ലിസ്റ്റ് രഹസ്യമാണ്. രഹസ്യാത്മകതയും ക്ലയന്റിനെ വിളിച്ചെടുക്കില്ല എന്ന ക്ലോസും നടപ്പാക്കാം."),
 ("A","A","അവന് പഠിപ്പിക്കാം, നമ്മുടെ ലിസ്റ്റ് വെച്ചല്ല."),
 ("V","wide","അറിവ് അവന്റേത്, ലിസ്റ്റ് കമ്പനിയുടേത്.")],
 "അറിവ് അവന്റേത്,\nലിസ്റ്റ് കമ്പനിയുടേത്", CTA_COFOUNDER, theme="faq",
 cap_ml="പോയ കോ-ഫൗണ്ടർ ക്ലയന്റ് ലിസ്റ്റ് കൊണ്ടുപോയി വിളിക്കുന്നു. പോയ ശേഷമുള്ള നോൺ-കോമ്പീറ്റ് ഇന്ത്യയിൽ പൊതുവെ നടപ്പാകില്ല, പക്ഷേ രഹസ്യാത്മകതയും നോൺ-സോളിസിറ്റും നടപ്പാക്കാം. നിങ്ങളുടെ കരാറിൽ ഇവ ഉണ്ടോ?",
 cap_en="A co-founder of a tuition app leaves and starts calling the parents on the company's list. A post-exit non-compete is generally not enforceable in India, but confidentiality and non-solicit clauses can be. Does your co-founder agreement have them?",
 cap_mg="Poya co-founder client list kondupoyi vilikkunnu. Poya shesham ulla non-compete India-yil pothuve nadappaakilla, pakshe confidentiality-um non-solicit-um nadappaakkaam. Ningalude agreement-il iva undo?")

duo("cf018", "tech_nontech", "B", "ferry", "\"ക്ലിഫ് കടന്നു.\nഇനി ഷെയർ മുഴുവൻ\nഎന്റേത്\" ശരിയോ?", [
 ("A","wide","ടോണീ, കുട്ടനാട്ടിലെ ഡ്രോൺ സ്പ്രേയിംഗിന് ഒരു വർഷം തികഞ്ഞു. ക്ലിഫ് കടന്നു, ഇനി എന്റെ ഷെയർ മുഴുവൻ എന്റേതല്ലേ?"),
 ("V","V","മീരേ, ക്ലിഫ് എന്നാൽ ഫിനിഷ് ലൈൻ അല്ല. ആദ്യ ഭാഗം മാത്രം അപ്പോൾ സ്വന്തമാകും."),
 ("A","A","അപ്പോ ബാക്കിയോ?"),
 ("V","wide","നമ്മുടെ എഗ്രിമെന്റിൽ നാല് വർഷം, ഒരു വർഷ ക്ലിഫ്. ബാക്കി ഷെയർ പിന്നീടുള്ള മാസങ്ങളിൽ പടിപടിയായി വെസ്റ്റ് ആകും."),
 ("A","A","അപ്പോ ഞാൻ പറന്നു തുടങ്ങിയതേയുള്ളൂ."),
 ("V","wide","ക്ലിഫ് കടന്നാൽ ലാൻഡിംഗ് അല്ല, ടേക്ക്ഓഫ്.")],
 "ക്ലിഫ് കടന്നാൽ\nലാൻഡിംഗ് അല്ല, ടേക്ക്ഓഫ്", CTA_VESTING, theme="new",
 cap_ml="ഒരു വർഷ ക്ലിഫ് കടന്നാൽ ഷെയർ മുഴുവൻ സ്വന്തമാകുമോ? ഇല്ല. നാല് വർഷം, ഒരു വർഷ ക്ലിഫ് എന്ന സാധാരണ രീതിയിൽ ക്ലിഫിൽ ആദ്യ ഭാഗം, ബാക്കി പിന്നീട് പടിപടിയായി. നിങ്ങളുടെ ക്ലിഫ് എത്ര മാസം?",
 cap_en="Does crossing the 1-year cliff make all your shares yours? No. Under the common 4-year vesting with a 1-year cliff, the first part vests at the cliff and the rest step by step after that. How long is your cliff?",
 cap_mg="Oru varsha cliff kadannaal share muzhuvan swanthamaakumo? Illa. 4 varsham, 1 varsha cliff enna saadhaarana reethiyil cliff-il aadya bhaagam, baakki pinneedu padipadiyaayi. Ningalude cliff ethra maasam?")

duo("cf019", "family_cofounders", "A", "balcony", "\"ഭാര്യയും ഭർത്താവുമാ.\nഞങ്ങൾക്കെന്തിന്\nഎഗ്രിമെന്റ്?\"", [
 ("A","wide","വിവേക്, അലങ്കാര മീൻ വളർത്തൽ കമ്പനിക്ക് കോ-ഫൗണ്ടർ എഗ്രിമെന്റ് വേണോ? നമ്മൾ ഭാര്യയും ഭർത്താവുമല്ലേ."),
 ("V","V","അമ്മൂ, ഇൻവെസ്റ്റർ ചോദിക്കും: ബ്രീഡിംഗ് രീതി ആരുടേത്, ആര് എന്ത് തീരുമാനിക്കും."),
 ("A","A","അതൊക്കെ നമുക്ക് അറിയാമല്ലോ."),
 ("V","wide","നമുക്കറിയാം, പേപ്പറിന് അറിയില്ല. റോളും IP കമ്പനിക്ക് എന്നതും ഒരാൾ മാറിയാൽ എന്തെന്നും എഴുതണം."),
 ("A","A","വീട്ടിൽ ഒരു താക്കോൽ, കമ്പനിയിൽ ഒരു കരാർ.")],
 "വീട്ടിൽ ഒരു താക്കോൽ,\nകമ്പനിയിൽ ഒരു കരാർ", CTA_COFOUNDER, theme="new",
 cap_ml="ഭാര്യയും ഭർത്താവും കോ-ഫൗണ്ടർമാർ ആണെങ്കിൽ എഗ്രിമെന്റ് വേണോ? വേണം: റോളുകൾ, എല്ലാ IP-യും കമ്പനിക്ക്, ഒരാൾ മാറിയാൽ എന്ത് എന്നിവ എഴുതണം. നിങ്ങൾ കുടുംബത്തോടൊപ്പം ബിസിനസ് ചെയ്യുന്നുണ്ടോ?",
 cap_en="Do a husband and wife running an ornamental fish startup need a co-founder agreement? Yes: roles, all IP assigned to the company, and what happens if one steps away should be written down. Do you run a business with family?",
 cap_mg="Bhaaryayum bharthavum co-founders aanenkil agreement veno? Venam: role-ukal, ella IP-yum company-kku, oraal maariyaal enthu enniva ezhuthanam. Ningal kudumbathodoppam business cheyyunnundo?")
