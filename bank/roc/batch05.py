# ROC annual compliance batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_ROC. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING


duo("rc019", "late_filer", "A", "bank", "ലോൺ പുതുക്കാൻ ചെന്നു.\nമാനേജർ: \"AOC-4 എവിടെ?\"", [
 ("A","wide","മനോജേ, ലോൺ പുതുക്കാൻ കഴിഞ്ഞ വർഷത്തെ AOC-4-ഉം MGT-7-ഉം ഫയൽ ചെയ്ത കോപ്പി വേണം."),
 ("V","V","ശ്രുതീ, ലോൺ കിട്ടിയിട്ട് AGM നടത്താം എന്നാ കരുതിയത്. ഹോളോ ബ്രിക്സിന് ഇപ്പോ സീസൺ ആണ്."),
 ("A","A","ബാങ്ക് ആദ്യം നോക്കുന്നത് ഫയലിംഗ് ആണ്, ഓർഡർ ബുക്ക് അല്ല."),
 ("V","wide","ശരിക്കും എപ്പോഴായിരുന്നു ഇതൊക്കെ?"),
 ("A","wide","AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ."),
 ("V","V","ബ്ലോക്ക് ഉറയ്ക്കാൻ സിമന്റ്, ലോൺ ഉറയ്ക്കാൻ ഫയലിംഗ്.")],
 "ബ്ലോക്കിന് സിമന്റ്,\nലോണിന് ഫയലിംഗ്", CTA_ROC, theme="crm",
 cap_ml="ഹോളോ ബ്രിക്സ് കമ്പനിയുടെ ലോൺ പുതുക്കാൻ ചെന്നപ്പോൾ ബാങ്ക് ആദ്യം ചോദിച്ചത് AOC-4-ഉം MGT-7-ഉം. AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ; വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ. നിങ്ങളുടെ ബാങ്ക് ഇത് ചോദിച്ചിട്ടുണ്ടോ?",
 cap_en="A hollow-block company went to renew its bank loan, and the manager asked for last year's filed AOC-4 and MGT-7 first. AGM by 30 September, AOC-4 within 30 days of it, MGT-7 within 60 days; late fee Rs 100 a day per form. Has your bank asked for these?",
 cap_mg="Hollow bricks company-yude loan puthukkaan chennappol bank aadyam chodichathu AOC-4-um MGT-7-um. AGM September 30-nullil, AOC-4 30 divasathil, MGT-7 60 divasathil; vaikiyaal form onninu divasam 100 roopa. Ningalude bank ithu chodichittundo?")

duo("rc020", "nri_director", "B", "airport", "നാട്ടിൽ പുതിയ കമ്പനി.\nപഴയ കമ്പനി 3 വർഷമായി\nഉറങ്ങുന്നു", [
 ("A","wide","റഫീഖേ, പന്ത്രണ്ട് വർഷം ദോഹയിൽ. ഇനി നാട്ടിൽ ഒരു സ്പൈസ് പാക്കിംഗ് കമ്പനി തുടങ്ങാനാ പ്ലാൻ."),
 ("V","V","ഷമീറേ, പണ്ട് നമ്മൾ തുടങ്ങിയ ആ ട്രാവൽ കമ്പനി ഓർമ്മയുണ്ടോ? അതിൽ നീ ഇപ്പോഴും ഡയറക്ടറാ."),
 ("A","A","അത് നിന്നുപോയില്ലേ? ബിസിനസ് ഇല്ല, അതുകൊണ്ട് ഒന്നും ഫയൽ ചെയ്തില്ല."),
 ("V","wide","അതാ പ്രശ്നം. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത വരാം. കമ്പനി സ്ട്രൈക്ക് ഓഫും ആകാം."),
 ("A","A","അപ്പോ പുതിയ കമ്പനിക്ക് മുമ്പ് പഴയതിന്റെ കണക്ക് തീർക്കണം."),
 ("V","wide","പഴയ ഉറക്കം പുതിയ സ്വപ്നം തടയരുത്.")],
 "പഴയ ഉറക്കം\nപുതിയ സ്വപ്നം\nതടയരുത്", CTA_FILING, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചു വന്ന് പുതിയ കമ്പനി തുടങ്ങാൻ നോക്കുമ്പോഴാ പഴയ, ഉറങ്ങിക്കിടന്ന കമ്പനി ഓർമ്മ വന്നത്. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത വരാം, കമ്പനി സ്ട്രൈക്ക് ഓഫും ആകാം. നിങ്ങളുടെ പേരിൽ മറന്ന കമ്പനി ഉണ്ടോ?",
 cap_en="Back from Doha with plans for a new company, he learns he is still a director of an old travel company nobody filed for. Three years of non-filing can disqualify directors for 5 years and get the company struck off. Is there a forgotten company in your name?",
 cap_mg="Gulf-il ninnu thirichu vannu puthiya company thudangaan nokkumbozhaa pazhaya, urangikkidanna company orma vannathu. 3 varsham file cheythillenkil director-kku 5 varsham ayogyatha varaam, company strike off-um aakaam. Ningalude peril maranna company undo?")

duo("rc021", "dormant_company", "A", "bakery", "രണ്ട് വർഷം കട\nഅടച്ചിട്ടു. \"കമ്പനിയും\nഉറങ്ങിക്കോട്ടെ\"", [
 ("A","wide","സാബൂ, വെഡ്ഡിംഗ് കേക്ക് ഓർഡറുകൾ വീണ്ടും വരുന്നു. രണ്ട് വർഷം അടച്ചിട്ട സ്റ്റുഡിയോ തുറക്കാം."),
 ("V","V","ജിഷേ, ആ രണ്ട് വർഷം നമ്മുടെ കമ്പനി ഒരു ഫയലിംഗും ചെയ്തില്ല. കട അടച്ചാൽ കമ്പനിയും ഉറങ്ങുമെന്ന് കരുതി."),
 ("A","A","ഈ സെപ്റ്റംബർ കൂടി പോയാൽ എന്താകും?"),
 ("V","wide","മൂന്ന് വർഷം. ഫയൽ ചെയ്യാത്ത കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം. നമ്മൾ രണ്ടുപേർക്കും 5 വർഷം ഡയറക്ടർ അയോഗ്യതയും."),
 ("A","A","അപ്പോ ആദ്യ ഓർഡർ കേക്കിനല്ല, ഫയലിംഗിനാ."),
 ("V","wide","ഓവൻ തണുത്താലും കലണ്ടർ തണുക്കില്ല.")],
 "ഓവൻ തണുത്താലും\nകലണ്ടർ തണുക്കില്ല", CTA_FILING, theme="crm",
 cap_ml="രണ്ട് വർഷം അടച്ചിട്ട വെഡ്ഡിംഗ് കേക്ക് സ്റ്റുഡിയോ, ആ കാലത്ത് കമ്പനി ഒന്നും ഫയൽ ചെയ്തില്ല. 3 വർഷം ഫയൽ ചെയ്യാതിരുന്നാൽ കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം, ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യതയും. നിങ്ങളുടെ കമ്പനി എത്ര വർഷമായി ഫയൽ ചെയ്തിട്ട്?",
 cap_en="A wedding-cake studio shut for two years and its company filed nothing, as if the company slept too. A third year without filings can get the company struck off and the directors disqualified for 5 years. How long since your company last filed?",
 cap_mg="Randu varsham adachitta wedding cake studio, aa kaalathu company onnum file cheythilla. 3 varsham file cheyyaathirunnaal company strike off aakaam, directors-nu 5 varsham ayogyathayum. Ningalude company ethra varshamaayi file cheythittu?")

duo("rc022", "late_filer", "C", "pharmacy", "സെപ്റ്റംബർ 28.\nഅക്കൗണ്ടന്റ്\nജോലി വിട്ടു", [
 ("A","wide","പ്രവീൺ, നമ്മുടെ ആയുർവേദ സോപ്പ് കമ്പനിയുടെ അക്കൗണ്ടന്റ് ഇന്ന് ജോലി വിട്ടു. ബാക്കി അടുത്ത മാസം നോക്കാം."),
 ("V","V","സിനീ, ഇന്ന് സെപ്റ്റംബർ 28. രണ്ട് കാര്യം രണ്ട് ദിവസത്തിൽ തീരണം."),
 ("A","A","രണ്ട് ദിവസത്തിൽ എന്താ?"),
 ("V","wide","AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. നമ്മൾ രണ്ട് ഡയറക്ടർമാരുടെയും DIR-3 KYC-യും 30-നുള്ളിൽ."),
 ("A","A","അക്കൗണ്ടന്റ് പോയി, ഡെഡ്‌ലൈൻ പോയില്ല."),
 ("V","wide","അക്കൗണ്ടന്റ് രാജി വെക്കും, ഡെഡ്‌ലൈൻ രാജി വെക്കില്ല.")],
 "ഡെഡ്‌ലൈൻ\nരാജി വെക്കില്ല", CTA_ROC, theme="new",
 cap_ml="സെപ്റ്റംബർ 28-ന് ആയുർവേദ സോപ്പ് കമ്പനിയുടെ അക്കൗണ്ടന്റ് ജോലി വിട്ടു. പക്ഷേ AGM-ഉം ഓരോ ഡയറക്ടറുടെയും DIR-3 KYC-യും സെപ്റ്റംബർ 30-നുള്ളിൽ തന്നെ. നിങ്ങളുടെ കമ്പനിയിൽ ഇത് ആര് ഓർക്കുന്നു?",
 cap_en="On 28 September the accountant of an ayurvedic soap company quits, and the founder plans to sort things out next month. But the AGM and every director's DIR-3 KYC are due by 30 September. Who tracks these dates in your company?",
 cap_mg="September 28-nu ayurveda soap company-yude accountant joli vittu. Pakshe AGM-um oro director-udeyum DIR-3 KYC-um September 30-nullil thanne. Ningalude company-il ithu aaru orkkunnu?")

chat("rcc004", "new_company_roc", "B", "അമ്മയുടെ പേരിലെ\nകട ഇപ്പോ കമ്പനി.\n\"ഇനി എന്ത്?\"", ("ആരതി", "ഗോകുൽ"), [
 (1,"ആരതീ, ഇൻവെസ്റ്റർ പറഞ്ഞപോലെ അമ്മയുടെ പേരിലെ മസാല കട കമ്പനിയാക്കി. സർട്ടിഫിക്കറ്റ് ഇന്നലെ കിട്ടി."),
 (0,"ഗോകുൽ, ഇനി കോംപ്ലയൻസ് പേടിച്ച് മാറി നിൽക്കാൻ പറ്റില്ല. ആദ്യ മാസം തന്നെ ഒരു പണിയുണ്ട്."),
 (1,"പ്രൊപ്രൈറ്റർഷിപ്പിൽ ഇതൊന്നും ഇല്ലായിരുന്നല്ലോ. എന്ത് പണി?"),
 (0,"30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ. 180 ദിവസത്തിനുള്ളിൽ INC-20A. പിന്നെ എല്ലാ വർഷവും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM."),
 (1,"അപ്പോ കട പഴയത്, കലണ്ടർ പുതിയത്."),
 (0,"പേര് മാറിയാൽ പോരാ, ശീലവും മാറണം.")],
 "പേര് മാറിയാൽ പോരാ,\nശീലവും മാറണം", CTA_ROC, theme="crm",
 cap_ml="കോംപ്ലയൻസ് പേടിച്ച് അമ്മയുടെ പേരിൽ നടത്തിയ മസാല കട, ഇൻവെസ്റ്റർ പറഞ്ഞപ്പോൾ കമ്പനിയാക്കി. ഇനി 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ, 180 ദിവസത്തിനുള്ളിൽ INC-20A, എല്ലാ വർഷവും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM. നിങ്ങളുടെ ബിസിനസ് ആരുടെ പേരിലാ?",
 cap_en="A spice shop run in a mother's name to avoid compliance became a company because an investor asked. Now: first auditor within 30 days, INC-20A within 180 days, and an AGM by 30 September every year. Whose name is your business in?",
 cap_mg="Compliance pedichu ammayude peril nadathiya masala kada, investor paranjappol company aakki. Ini 30 divasathinullil aadya auditor, 180 divasathinullil INC-20A, ella varshavum September 30-nullil AGM. Ningalude business aarude peril aa?")

duo("rc023", "new_company_roc", "B", "home", "AGM കഴിഞ്ഞു,\nമിനിറ്റ്സും എഴുതി.\n\"ഇനി ഒന്നും വേണ്ട\"", [
 ("A","wide","അരുണേ, ട്യൂഷൻ ആപ്പ് കമ്പനിയുടെ AGM ഇന്ന് ഡൈനിംഗ് ടേബിളിൽ നടത്തി, മിനിറ്റ്സും എഴുതി. ഈ വർഷം തീർന്നു!"),
 ("V","V","സ്നേഹേ, AGM തുടക്കം മാത്രമാ. അതിന്റെ തീയതി മുതൽ രണ്ട് ക്ലോക്ക് ഓടിത്തുടങ്ങി."),
 ("A","A","രണ്ട് ക്ലോക്കോ?"),
 ("V","wide","AOC-4 30 ദിവസത്തിനുള്ളിൽ, MGT-7 60 ദിവസത്തിനുള്ളിൽ ROC-യിൽ ഫയൽ ചെയ്യണം. വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ."),
 ("A","A","അപ്പോ ഇന്നത്തേത് ആദ്യ സ്റ്റെപ്പ് മാത്രം."),
 ("V","wide","ഊണ് മേശയിൽ AGM തീരും. ഫയലിംഗ് തീരില്ല.")],
 "ഊണ് മേശയിൽ\nAGM തീരും,\nഫയലിംഗ് തീരില്ല", CTA_ROC, theme="faq",
 cap_ml="AGM നടത്തി മിനിറ്റ്സ് എഴുതിയാൽ ഈ വർഷത്തെ ROC പണി തീർന്നോ? ഇല്ല. AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4, 60 ദിവസത്തിനുള്ളിൽ MGT-7; വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ. നിങ്ങളുടെ AGM എവിടെയാ നടന്നത്?",
 cap_en="Held the AGM at the dining table and wrote the minutes, so the year's ROC work is done? No. AOC-4 is due within 30 days of the AGM and MGT-7 within 60 days, with a late fee of Rs 100 a day per form. Where did your AGM happen?",
 cap_mg="AGM nadathi minutes ezhuthiyaal ee varshathe ROC pani theerno? Illa. AGM kazhinju 30 divasathinullil AOC-4, 60 divasathinullil MGT-7; vaikiyaal form onninu divasam 100 roopa. Ningalude AGM evideyaa nadannathu?")

duo("rc024", "late_filer", "C", "munnar", "\"സീസൺ കഴിഞ്ഞിട്ട്\nAGM പോരേ?\"", [
 ("A","wide","ബേസിലേ, ജീപ്പ് സഫാരി ബുക്കിംഗ് നിറഞ്ഞു. ഒരു ഡ്രൈവർ കുറവും. AGM ഡിസംബറിൽ സീസൺ കഴിഞ്ഞ് വെക്കാം."),
 ("V","V","സെലിനേ, മൂന്നാറിൽ സീസൺ ഉണ്ട്. കമ്പനി നിയമത്തിന്റെ കലണ്ടറിൽ സീസൺ ഇല്ല."),
 ("A","A","ടൂറിസം കമ്പനിക്ക് ഒരു ഇളവും ഇല്ലേ?"),
 ("V","wide","സീസൺ ഒരു കാരണമല്ല. AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. പിന്നെ AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ."),
 ("A","A","അപ്പോ ജീപ്പിന് മുമ്പ് ഫയൽ മല കയറണം."),
 ("V","wide","കോട മാറും, സെപ്റ്റംബർ 30 മാറില്ല.")],
 "കോട മാറും,\nസെപ്റ്റംബർ 30\nമാറില്ല", CTA_ROC, theme="faq",
 cap_ml="മൂന്നാറിലെ ജീപ്പ് സഫാരി കമ്പനി ടൂറിസം സീസൺ കഴിഞ്ഞ് ഡിസംബറിൽ AGM വെക്കാമെന്ന് കരുതി. പക്ഷേ AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, പിന്നെ AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ. നിങ്ങളുടെ ബിസിനസിന്റെ തിരക്ക് ഏത് മാസം?",
 cap_en="A Munnar jeep-safari company wanted to push its AGM to December, after the tourist season. The season is not a reason: AGM by 30 September, AOC-4 within 30 days and MGT-7 within 60 days of it. Which month is your busiest?",
 cap_mg="Munnar-ile jeep safari company tourism season kazhinju December-il AGM vekkaamennu karuthi. Pakshe AGM September 30-nullil, pinne AOC-4 30 divasathil, MGT-7 60 divasathil. Ningalude business-inte thirakku ethu maasam?")

duo("rc025", "llp_owner", "A", "shop", "\"LLP-യുടെ ടാക്സ്\nഫയൽ ചെയ്തു.\nഫോം 8 വേറെയോ?\"", [
 ("A","wide","സുരേഷേ, നമ്മുടെ ഹാർഡ്‌വെയർ LLP-യുടെ ഇൻകം ടാക്സ് റിട്ടേൺ ഫയൽ ചെയ്തു. ഇനി ഈ വർഷം ഒന്നുമില്ല."),
 ("V","V","ബിനൂ, ടാക്സ് ഓഫീസ് ഒന്ന്. ROC വേറെ ഓഫീസ്."),
 ("A","A","രണ്ടിടത്തും വേറെ വേറെ ഫയലോ?"),
 ("V","wide","അതെ. LLP-ക്ക് ഫോം 11 മെയ് 30-നുള്ളിൽ, ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. കച്ചവടം കുറഞ്ഞ വർഷവും."),
 ("A","A","അപ്പോ ഒരു രസീത് കൊണ്ട് രണ്ട് ഓഫീസും തൃപ്തരാകില്ല."),
 ("V","wide","ഒരു ഷട്ടർ, രണ്ട് പൂട്ട്.")],
 "ഒരു ഷട്ടർ,\nരണ്ട് പൂട്ട്", CTA_FILING, theme="faq",
 cap_ml="LLP-യുടെ ഇൻകം ടാക്സ് റിട്ടേൺ ഫയൽ ചെയ്താൽ ROC ഫയലിംഗ് കഴിഞ്ഞോ? ഇല്ല. LLP-ക്ക് ഫോം 11 മെയ് 30-നുള്ളിൽ, ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ, ബിസിനസ് കുറഞ്ഞ വർഷവും. നിങ്ങളുടെ ബിസിനസ് LLP ആണോ?",
 cap_en="Filed the LLP's income tax return, so the ROC filings are done? No. An LLP files Form 11 by 30 May and Form 8 by 30 October with the ROC, even in a slow year. Is your business an LLP?",
 cap_mg="LLP-yude income tax return file cheythaal ROC filing kazhinjo? Illa. LLP-kku Form 11 May 30-nullil, Form 8 October 30-nullil, business kuranja varshavum. Ningalude business LLP aano?")

duo("rc026", "late_filer", "B", "metro", "പാവക്കൂത്ത് ടീം\nജർമ്മനിയിൽ. \"KYC\nതിരിച്ചു വന്നിട്ട്\"", [
 ("A","wide","കിരണേ, ജർമ്മനി ടൂർ ഒക്ടോബർ പകുതി വരെയല്ലേ? അപ്പോ സെപ്റ്റംബർ 30-ന്റെ കാര്യം?"),
 ("V","V","അഞ്ജലീ, തോൽപ്പാവകൾ പെട്ടിയിലാക്കി. KYC-യും AGM-ഉം തിരിച്ചു വന്നിട്ട് നോക്കാം."),
 ("A","A","ടൂർ നമ്മുടെ കലണ്ടറിൽ. ഡെഡ്‌ലൈൻ കമ്പനി നിയമത്തിൽ."),
 ("V","wide","വിദേശത്താണെങ്കിലും വേണോ?"),
 ("A","wide","വേണം. ഓരോ ഡയറക്ടറുടെയും DIR-3 KYC-യും കമ്പനിയുടെ AGM-ഉം സെപ്റ്റംബർ 30-നുള്ളിൽ."),
 ("V","V","പാവ ആടുന്നത് ജർമ്മനിയിൽ, ഡെഡ്‌ലൈൻ ഓടുന്നത് ഇവിടെ.")],
 "പാവ ആടുന്നത് അവിടെ,\nഡെഡ്‌ലൈൻ ഓടുന്നത്\nഇവിടെ", CTA_ROC, theme="new",
 cap_ml="തോൽപ്പാവക്കൂത്ത് കമ്പനിയുടെ ഡയറക്ടർമാർ സെപ്റ്റംബർ മുഴുവൻ ജർമ്മനി ടൂറിൽ. പക്ഷേ ഓരോ ഡയറക്ടറുടെയും DIR-3 KYC-യും AGM-ഉം സെപ്റ്റംബർ 30-നുള്ളിൽ തന്നെ, നാട്ടിലില്ലെങ്കിലും. നിങ്ങളുടെ ഡയറക്ടർമാർ ഇപ്പോൾ എവിടെ?",
 cap_en="A shadow-puppet troupe's company has all its directors on a tour in Germany through September. Every director's DIR-3 KYC and the company's AGM are still due by 30 September, wherever they are. Where are your directors right now?",
 cap_mg="Tholpaavakkoothu company-yude directors September muzhuvan Germany tour-il. Pakshe oro director-udeyum DIR-3 KYC-um AGM-um September 30-nullil thanne, naattil illenkilum. Ningalude directors ippol evide?")

duo("rc027", "dormant_company", "C", "farm", "\"AGM വെച്ചില്ലെങ്കിൽ\nAOC-4-ന്റെ ക്ലോക്കും\nഓടില്ലല്ലോ?\"", [
 ("A","wide","ഗോപീ, ഒരു ബുദ്ധി. ഞണ്ട് ഫാം കമ്പനിയുടെ AGM നടത്തിയില്ലെങ്കിൽ AOC-4-ന്റെ 30 ദിവസം തുടങ്ങുകയേ ഇല്ലല്ലോ."),
 ("V","V","വാസുവേട്ടാ, ആ ബുദ്ധി ഞണ്ടിനെപ്പോലെ പിന്നോട്ടാ നടക്കുന്നത്."),
 ("A","A","എന്താ, നിയമത്തിൽ ഒരു ഓട്ടയും ഇല്ലേ?"),
 ("V","wide","AGM തന്നെ സെപ്റ്റംബർ 30-നുള്ളിൽ നിർബന്ധം. അപ്പോ AOC-4 ഒക്ടോബർ 30-നും MGT-7 നവംബർ 29-നും ഉള്ളിൽ."),
 ("A","A","മീറ്റിംഗ് ഒഴിവാക്കിയാൽ ഡെഡ്‌ലൈൻ ഒഴിവാകില്ല അല്ലേ."),
 ("V","wide","ഞണ്ട് പിന്നോട്ട് പോകും, കലണ്ടർ പോകില്ല.")],
 "ഞണ്ട് പിന്നോട്ട്,\nകലണ്ടർ മുന്നോട്ട്", CTA_ROC, theme="faq",
 cap_ml="AGM നടത്തിയില്ലെങ്കിൽ AOC-4-ന്റെ 30 ദിവസം തുടങ്ങില്ലല്ലോ എന്ന് ഒരു ഞണ്ട് ഫാം കമ്പനി കരുതി. പക്ഷേ AGM തന്നെ സെപ്റ്റംബർ 30-നുള്ളിൽ വേണം; അപ്പോ AOC-4 ഒക്ടോബർ 30-നും MGT-7 നവംബർ 29-നും ഉള്ളിൽ. ഈ ഓട്ട ആരെങ്കിലും പറഞ്ഞു തന്നിട്ടുണ്ടോ?",
 cap_en="A mud-crab farm company thought skipping the AGM would stop the AOC-4 clock from starting. It doesn't: the AGM itself is due by 30 September, so AOC-4 is due by 30 October and MGT-7 by 29 November anyway. Has anyone sold you this loophole?",
 cap_mg="AGM nadathiyillenkil AOC-4-inte 30 divasam thudangillallo ennu oru njandu farm company karuthi. Pakshe AGM thanne September 30-nullil venam; appo AOC-4 October 30-num MGT-7 November 29-num ullil. Ee otta aarenkilum paranju thannittundo?")
