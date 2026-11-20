# ROC annual compliance batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_ROC. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rc011", "late_filer", "A", "kitchen", "അമ്മാവന്റെ പണം.\n\"കുടുംബമല്ലേ,\nകണക്ക് എന്തിന്?\"", [
 ("A","wide","രാജേഷേ, നിന്റെ അമ്മാവൻ കമ്പനിയിൽ ഇട്ട പൈസ തിരിച്ചു ചോദിക്കുന്നു. ആദ്യം AOC-4 കാണണം എന്ന്."),
 ("V","V","ബിന്ദൂ, കുടുംബത്തിലെ പൈസയല്ലേ. അതുകൊണ്ട് ഫയലിംഗ് ഒന്നും ചെയ്തില്ല."),
 ("A","A","പൈസ കുടുംബത്തിന്റേതാകാം. പക്ഷേ കമ്പനി നിയമത്തിന്റേതാ."),
 ("V","wide","AOC-4 എപ്പോഴാ വേണ്ടിയിരുന്നത്?"),
 ("A","wide","AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ. വൈകിയ ഓരോ ദിവസവും 100 രൂപ ലേറ്റ് ഫീ, ലിമിറ്റ് ഇല്ല."),
 ("V","A","ബന്ധം രക്തത്തിൽ, കണക്ക് ഫയലിൽ.")],
 "ബന്ധം രക്തത്തിൽ,\nകണക്ക് ഫയലിൽ", CTA_FILING, theme="crm",
 cap_ml="കുടുംബത്തിലെ പൈസ കൊണ്ട് തുടങ്ങിയ ചക്ക ചിപ്സ് കമ്പനി, അമ്മാവൻ പണം തിരിച്ചു ചോദിച്ചപ്പോൾ ആദ്യം AOC-4 ചോദിച്ചു. AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4, വൈകിയാൽ ദിവസം 100 രൂപ, ലിമിറ്റ് ഇല്ല. നിങ്ങളുടെ കമ്പനിയിൽ കുടുംബ പൈസ ഉണ്ടോ?",
 cap_en="Family money started this jackfruit chips company, so nobody filed anything. Then the uncle asked for his money back and wanted to see the AOC-4 first. AOC-4 is due within 30 days of the AGM, and the late fee is Rs 100 a day with no cap. Family money in your company: yes or no?",
 cap_mg="Kudumba paisa kondu thudangiya chakka chips company, ammaavan panam thirichu chodichappol aadyam AOC-4 chodichu. AGM kazhinju 30 divasathinullil AOC-4, vaikiyaal divasam 100 roopa, limit illa. Ningalude company-il kudumba paisa undo?")

duo("rc012", "late_filer", "B", "veranda", "\"മകന്റെ കമ്പനിയിൽ\nഞാൻ പേരിന് മാത്രം\nഡയറക്ടർ\"", [
 ("A","wide","ബാലേട്ടാ, മോന്റെ കയർ കമ്പനിയിൽ എന്നെ ഡയറക്ടർ ആക്കിയത് ഒപ്പിടാൻ മാത്രമല്ലേ?"),
 ("V","V","ശാന്തേ, ഇന്ന് മോൻ വിളിച്ചു. നിന്റെ KYC സെപ്റ്റംബറിൽ ചെയ്തില്ലെന്ന്."),
 ("A","A","എഴുപത് വയസ്സായ എനിക്കും KYC-യോ?"),
 ("V","wide","DIR-3 KYC ഓരോ ഡയറക്ടറും സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. പേരിന് മാത്രമുള്ള ഡയറക്ടറും."),
 ("A","A","അപ്പോ പേര് എന്റേത്, ഡ്യൂട്ടിയും എന്റേത്."),
 ("V","wide","ഒപ്പിട്ട പേനയ്ക്കും ഒരു കലണ്ടർ ഉണ്ട്.")],
 "പേരിന് ഡയറക്ടർ,\nKYC മുഴുവനായി", CTA_ROC, theme="crm",
 cap_ml="മകന്റെ കയർ കമ്പനിയിൽ അമ്മയെ ഒപ്പിടാൻ മാത്രം ഡയറക്ടർ ആക്കി. പക്ഷേ DIR-3 KYC ഓരോ ഡയറക്ടറും സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം, പേരിന് മാത്രമുള്ള ഡയറക്ടറും. നിങ്ങളുടെ കമ്പനിയിൽ എത്ര ഡയറക്ടർമാർ?",
 cap_en="A son made his 70-year-old mother a director of his coir company just for her signature. But DIR-3 KYC is due from every director by 30 September, including a director in name only. How many directors does your company have?",
 cap_mg="Makante coir company-il ammaye oppidaan maathram director aakki. Pakshe DIR-3 KYC oro director-um September 30-nullil cheyyanam, perinu maathramulla director-um. Ningalude company-il ethra directors?")

chat("rcc003", "late_filer", "C", "\"ഞാൻ നാളെ\nവിളിക്കാം\"\n45 ദിവസമായി", ("സോണിയ", "വിനീത്"), [
 (0,"വിനീത്, AOC-4-ഉം MGT-7-ഉം ഒപ്പിടാൻ ഇന്നെങ്കിലും വരുമോ?"),
 (1,"സോണിയാ, ഇന്ന് ടൂർ ബസ് ബുക്കിംഗ് തിരക്കാ. നാളെ വിളിക്കാം."),
 (0,"ഈ 'നാളെ' 45 ദിവസമായി. രണ്ട് ഫോമിനും ദിവസം 100 രൂപ വീതം ലേറ്റ് ഫീ ഓടുന്നുണ്ട്."),
 (1,"45 ദിവസം... എത്രയായി?"),
 (0,"ഒമ്പതിനായിരം. ലിമിറ്റ് ഇല്ല. നാളെ വിളിച്ചാൽ ഇരുന്നൂറ് കൂടി."),
 (1,"ഇപ്പോ തന്നെ വരുന്നു.")],
 "\"നാളെ\" എന്ന\nവാക്കിനും\nലേറ്റ് ഫീ", CTA_ROC, theme="crm",
 cap_ml="ടൂർ ബസ് കമ്പനിയുടെ ഡയറക്ടർ 45 ദിവസമായി 'നാളെ വിളിക്കാം' എന്ന് പറയുന്നു. AOC-4-ഉം MGT-7-ഉം വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ: 45 ദിവസം രണ്ട് ഫോം ഒമ്പതിനായിരം. നിങ്ങളുടെ ടീമിൽ 'നാളെ' പറയുന്നത് ആരാ?",
 cap_en="A tour bus company's co-director has been saying 'I'll call you tomorrow' for 45 days while AOC-4 and MGT-7 wait for his signature. The late fee is Rs 100 a day for each form, so two forms over 45 days is Rs 9,000, and it keeps going. Who says 'tomorrow' in your team?",
 cap_mg="Tour bus company-yude director 45 divasamaayi 'naale vilikkaam' ennu parayunnu. AOC-4-um MGT-7-um vaikiyaal oro form-inum divasam 100 roopa: 45 divasam randu form 9,000. Ningalude team-il 'naale' parayunnathu aaraa?")

duo("rc013", "new_company_roc", "A", "classroom", "ഡെമോ ഡേ കഴിഞ്ഞു.\nകമ്പനിക്ക് 170 ദിവസം.\nഒരു ഫോം ബാക്കി", [
 ("A","wide","ആദർശേ, ഡെമോ ഡേയിൽ നമ്മുടെ സ്മാർട്ട് വീൽചെയർ ജയിച്ചു. ഇനി സെമസ്റ്റർ പരീക്ഷ മാത്രം നോക്കിയാൽ മതി."),
 ("V","V","നിമ്മീ, കമ്പനി തുടങ്ങിയിട്ട് 170 ദിവസമായി. ഒരു ഡെഡ്‌ലൈൻ 10 ദിവസത്തിൽ വരുന്നു."),
 ("A","A","ഏത് ഡെഡ്‌ലൈൻ? ഇൻകുബേറ്ററിൽ ആരും പറഞ്ഞില്ലല്ലോ."),
 ("V","wide","INC-20A. കമ്പനി തുടങ്ങി 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ ഡെമോ ഡേ ഫിനിഷ് ലൈൻ അല്ല."),
 ("V","wide","ഡെമോ ഡേ ജയിച്ചു. ഇനി ഡെഡ്‌ലൈൻ ജയിക്കണം.")],
 "ഡെമോ ഡേ ജയിച്ചു,\nഇനി ഡെഡ്‌ലൈൻ", CTA_ROC, theme="crm",
 cap_ml="കോളേജ് ഇൻകുബേറ്ററിലെ ഡെമോ ഡേയ്ക്ക് വേണ്ടി തുടങ്ങിയ കമ്പനി, 170 ദിവസം കഴിഞ്ഞിട്ടും INC-20A ഫയൽ ചെയ്തില്ല. കമ്പനി തുടങ്ങി 180 ദിവസത്തിനുള്ളിൽ INC-20A വേണം. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ദിവസമായി?",
 cap_en="A student team registered a company for their campus incubator demo day, won, and moved on to exams. INC-20A is due within 180 days of incorporation, and they were at day 170. How many days old is your company?",
 cap_mg="College incubator-ile demo day-kku vendi thudangiya company, 170 divasam kazhinjittum INC-20A file cheythilla. Company thudangi 180 divasathinullil INC-20A venam. Ningalude company-kku ethra divasamaayi?")

duo("rc014", "new_company_roc", "B", "railway", "\"സെപ്റ്റംബർ 30-ന്\nAGM കഴിഞ്ഞു, ഇനി\nഅടുത്ത വർഷം\"", [
 ("A","wide","ദിനേശേ, നിന്റെ ഹോം നഴ്സിംഗ് കമ്പനിയുടെ MGT-7 ഫയൽ ചെയ്തോ?"),
 ("V","V","ഷീബേ, സെപ്റ്റംബർ 30-ന് AGM നടത്തി, ഒക്ടോബറിൽ AOC-4-ഉം. ഇനി അടുത്ത വർഷമല്ലേ?"),
 ("A","A","ഒരു ഫോം കൂടി ഉണ്ട്. MGT-7, AGM കഴിഞ്ഞ് 60 ദിവസത്തിനുള്ളിൽ."),
 ("V","wide","സെപ്റ്റംബർ 30-ൽ നിന്ന് 60 ദിവസം... നവംബർ 29!"),
 ("A","A","അതെ. അത് കഴിഞ്ഞാൽ ദിവസം 100 രൂപ ലേറ്റ് ഫീ, ലിമിറ്റ് ഇല്ല."),
 ("V","wide","AGM കഴിഞ്ഞാൽ കഥ കഴിഞ്ഞില്ല.")],
 "AGM കഴിഞ്ഞാൽ\nകഥ കഴിഞ്ഞില്ല", CTA_ROC, theme="faq",
 cap_ml="AGM-ഉം AOC-4-ഉം കഴിഞ്ഞാൽ ഈ വർഷത്തെ ROC ഫയലിംഗ് തീർന്നോ? ഇല്ല. MGT-7 AGM കഴിഞ്ഞ് 60 ദിവസത്തിനുള്ളിൽ: AGM സെപ്റ്റംബർ 30-നാണെങ്കിൽ നവംബർ 29. നിങ്ങളുടെ MGT-7 കഴിഞ്ഞോ?",
 cap_en="Held the AGM and filed AOC-4, so this year's ROC work is done? Not yet. MGT-7 is due within 60 days of the AGM: an AGM on 30 September means MGT-7 by 29 November. Is your MGT-7 filed: yes or no?",
 cap_mg="AGM-um AOC-4-um kazhinjaal ee varshathe ROC filing theerno? Illa. MGT-7 AGM kazhinju 60 divasathinullil: AGM September 30-nu aanenkil November 29. Ningalude MGT-7 kazhinjo?")

duo("rc015", "new_company_roc", "C", "juiceshop", "\"ഇൻകം ടാക്സ്\nഫയൽ ചെയ്തു, ROC-യും\nകഴിഞ്ഞല്ലോ?\"", [
 ("A","wide","നൗഷാദേ, ജ്യൂസ് കമ്പനിയുടെ ഇൻകം ടാക്സ് റിട്ടേൺ കഴിഞ്ഞു. ഇനി ROC ഫയലിംഗ് വേണ്ടല്ലോ?"),
 ("V","V","റസിയാ, ടാക്സ് ഓഫീസും ROC-യും രണ്ട് വാതിലാണ്."),
 ("A","A","ഒരേ കണക്കല്ലേ? രണ്ടിടത്ത് എന്തിനാ?"),
 ("V","wide","ROC-ക്ക് AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4, 60 ദിവസത്തിനുള്ളിൽ MGT-7. ടാക്സ് റിട്ടേൺ അതിന് പകരമല്ല."),
 ("A","A","അപ്പോ ഒരു ഗ്ലാസ് ജ്യൂസ്, രണ്ട് ബിൽ."),
 ("V","wide","ടാക്സ് ഫയൽ ചെയ്താൽ ROC തീരില്ല.")],
 "ടാക്സ് ഫയൽ ചെയ്താൽ\nROC തീരില്ല", CTA_FILING, theme="faq",
 cap_ml="ഇൻകം ടാക്സ് റിട്ടേൺ ഫയൽ ചെയ്താൽ ROC ഫയലിംഗും കഴിഞ്ഞോ? ഇല്ല. പ്രൈവറ്റ് ലിമിറ്റഡിന് AGM കഴിഞ്ഞ് 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7, ടാക്സ് റിട്ടേണിന് പുറമേ. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="Filed the company's income tax return, so the ROC filings are done too? No. A private limited company still files AOC-4 within 30 days of the AGM and MGT-7 within 60 days, separately from income tax. Did you know this: yes or no?",
 cap_mg="Income tax return file cheythaal ROC filing-um kazhinjo? Illa. Pvt Ltd-nu AGM kazhinju 30 divasathil AOC-4, 60 divasathil MGT-7, tax return-inu purame. Ithu ariyaamaayirunno?")

duo("rc016", "dormant_company", "A", "thattukada", "\"ROC ഫയലിംഗ്\nകോടി ടേണോവർ\nഉള്ളവർക്കല്ലേ?\"", [
 ("A","wide","ബിജൂ, നിന്റെ തെങ്ങുകയറ്റ യന്ത്രം വാടകയ്ക്ക് കൊടുക്കുന്ന കമ്പനിയുടെ ROC ഫയലിംഗ് ആരാ ചെയ്യുന്നേ?"),
 ("V","V","സിജോ, കുറച്ച് ലക്ഷമേ ടേണോവർ ഉള്ളൂ. ROC ഒക്കെ കോടിക്കാർക്കല്ലേ?"),
 ("A","A","ടേണോവർ ചെറുതായാലും കമ്പനി കമ്പനി തന്നെ."),
 ("V","wide","എന്നാലും എന്തൊക്കെ ഫയൽ ചെയ്യണം?"),
 ("A","wide","സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, പിന്നെ AOC-4, MGT-7. ബിസിനസ് ഇല്ലാത്ത വർഷവും."),
 ("V","A","തെങ്ങ് ചെറുതായാലും കയറണം, കമ്പനി ചെറുതായാലും ഫയൽ ചെയ്യണം.")],
 "തെങ്ങ് ചെറുതായാലും\nകയറണം", CTA_FILING, theme="faq",
 cap_ml="ROC ഫയലിംഗ് കോടി ടേണോവർ ഉള്ള കമ്പനികൾക്ക് മാത്രമാണോ? അല്ല. തെങ്ങുകയറ്റ യന്ത്രം വാടകയ്ക്ക് കൊടുക്കുന്ന ചെറിയ കമ്പനിക്കും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, പിന്നെ AOC-4, MGT-7. നിങ്ങളുടെ കമ്പനി: ചെറുതോ വലുതോ?",
 cap_en="Are ROC filings only for companies with crores in turnover? No. Even a small company renting out coconut-climbing machines holds its AGM by 30 September and files AOC-4 and MGT-7, even in a year with no business. Your company: small or big?",
 cap_mg="ROC filing crore turnover ulla company-kalkku maathramaano? Alla. Thengukayatta yanthram vaadakaykku kodukkunna cheriya company-kkum September 30-nullil AGM, pinne AOC-4, MGT-7. Ningalude company: cheruthO valuthO?")

lst("rcl002", "dormant_company", "B", "ഫയൽ ചെയ്യാത്ത കമ്പനി:\nസ്ട്രൈക്ക് ഓഫിലേക്ക്\n3 പടികൾ", [
 ("വർഷം 1", "AOC-4, MGT-7 വിട്ടു. ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ, ലിമിറ്റ് ഇല്ല."),
 ("വർഷം 2", "ലേറ്റ് ഫീ കൂടിക്കൊണ്ടിരിക്കും. ബിസിനസ് ഇല്ലെന്നത് ഒഴിവല്ല."),
 ("വർഷം 3", "കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം. ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത വരാം.")],
 "ഏത് പടിയിലാണ്\nനിങ്ങളുടെ കമ്പനി?", CTA_FILING, theme="faq",
 cap_ml="ഫയൽ ചെയ്യാത്ത കമ്പനി സ്ട്രൈക്ക് ഓഫിലേക്ക് പോകുന്നത് 3 പടിയായാണ്: ആദ്യം ദിവസം 100 രൂപ ലേറ്റ് ഫീ, ബിസിനസ് ഇല്ലെങ്കിലും. 3 വർഷമായാൽ സ്ട്രൈക്ക് ഓഫും ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യതയും. നിങ്ങൾ ഏത് പടിയിൽ: 1, 2, 3?",
 cap_en="A company that stops filing slides toward strike-off in three steps. Year 1: a late fee of Rs 100 a day per form, with no cap, even with no business. By year 3 the company can be struck off and its directors disqualified for 5 years. Which step are you on: 1, 2 or 3?",
 cap_mg="File cheyyaatha company strike off-ilekku pokunnathu 3 padiyaayaanu: aadyam divasam 100 roopa late fee, business illenkilum. 3 varshamaayaal strike off-um directors-nu 5 varsham ayogyathayum. Ningal ethu padiyil: 1, 2, 3?")

duo("rc017", "llp_owner", "C", "fishmarket", "ട്രോളിംഗ് നിരോധനം.\n\"ബോട്ടിന് മാത്രമല്ല,\nഫയലിംഗിനും?\"", [
 ("A","wide","ആന്റണീ, നമ്മുടെ ബോട്ടുകളുടെ LLP-യുടെ ഫോം 11 മെയ് 30-ന് മുമ്പ് ചെയ്തോ?"),
 ("V","V","സുമേ, മൺസൂണിൽ ട്രോളിംഗ് നിരോധനം വരുമല്ലോ. ബോട്ട് കരയിൽ, ഫയലിംഗും കരയിൽ."),
 ("A","A","നിരോധനം കടലിലാണ്, ഓഫീസിലല്ല."),
 ("V","wide","എന്നാൽ എന്തൊക്കെയാ വേണ്ടത്?"),
 ("A","wide","LLP-ക്ക് ഫോം 11 മെയ് 30-നുള്ളിൽ, ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. മീൻ കിട്ടാത്ത വർഷവും."),
 ("V","A","ട്രോളിംഗിന് നിരോധനം ഉണ്ട്, ഫയലിംഗിന് ഇല്ല.")],
 "ട്രോളിംഗിന് നിരോധനം,\nഫയലിംഗിന് ഇല്ല", CTA_FILING, theme="new",
 cap_ml="മത്സ്യബന്ധന ബോട്ടുകളുടെ LLP, ട്രോളിംഗ് നിരോധന കാലത്ത് ഫയലിംഗും നിർത്താമോ? ഇല്ല. LLP-ക്ക് ഫോം 11 മെയ് 30-നുള്ളിൽ, ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ, ബിസിനസ് ഇല്ലാത്ത വർഷവും. നിങ്ങളുടെ ബിസിനസ്: സീസണൽ ആണോ?",
 cap_en="A fishing boat LLP thought the monsoon trawling ban paused its filings too. It doesn't: an LLP files Form 11 by 30 May and Form 8 by 30 October, even in a year with no catch. Is your business seasonal: yes or no?",
 cap_mg="Malsyabandhana boat-kalude LLP, trawling nirodhana kaalathu filing-um nirthaamo? Illa. LLP-kku Form 11 May 30-nullil, Form 8 October 30-nullil, business illaatha varshavum. Ningalude business: seasonal aano?")

duo("rc018", "late_filer", "A", "garage", "\"എല്ലാം CA നോക്കും\"\n3 വർഷം. ഇപ്പോ\nഅയോഗ്യത ആർക്ക്?", [
 ("A","wide","ജിതിനേ, നമ്മുടെ വിന്റേജ് ബൈക്ക് റീസ്റ്റോറേഷൻ കമ്പനിയുടെ ഫയലിംഗ് ആരാ നോക്കുന്നേ?"),
 ("V","V","ഐശ്വര്യേ, അതൊക്കെ CA നോക്കിക്കോളും. നമ്മൾ എൻജിൻ നോക്കിയാൽ മതി."),
 ("A","A","CA മൂന്ന് വർഷമായി ഫോൺ എടുക്കുന്നില്ല. ഒരു ഫയലിംഗും നടന്നിട്ടില്ല."),
 ("V","wide","അത് CA-യുടെ പ്രശ്നമല്ലേ?"),
 ("A","wide","അല്ല. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ 5 വർഷം അയോഗ്യത വരാവുന്നത് ഡയറക്ടർമാർക്കാണ്, CA-ക്കല്ല."),
 ("V","A","എൻജിൻ ആര് നന്നാക്കിയാലും, ഒപ്പ് നമ്മുടേതാ.")],
 "അയോഗ്യത CA-ക്കല്ല,\nഡയറക്ടർക്കാണ്", CTA_ROC, theme="new",
 cap_ml="വിന്റേജ് ബൈക്ക് റീസ്റ്റോറേഷൻ കമ്പനി 'എല്ലാം CA നോക്കും' എന്ന് കരുതി, 3 വർഷം ഒരു ഫയലിംഗും നടന്നില്ല. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ 5 വർഷത്തെ അയോഗ്യത ഡയറക്ടർമാർക്കാണ്, CA-ക്കല്ല. അവസാന ഫയലിംഗ് എന്നാണെന്ന് അറിയാമോ?",
 cap_en="A vintage bike restoration company left everything to its CA, and three years went by with no ROC filings. Three years of non-filing can disqualify the directors for 5 years, not the CA, and the company can be struck off. Do you know your company's last filing date: yes or no?",
 cap_mg="Vintage bike restoration company 'ellaam CA nokkum' ennu karuthi, 3 varsham oru filing-um nadannilla. 3 varsham file cheythillenkil 5 varshathe ayogyatha directors-nu aanu, CA-kkalla. Avasaana filing ennaanennu ariyaamo?")
