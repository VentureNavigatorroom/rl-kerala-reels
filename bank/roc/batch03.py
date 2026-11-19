# ROC annual compliance batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_ROC. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rc003", "new_company_roc", "A", "rubber", "കോംപ്ലയൻസ് പേടിച്ച്\n2 പ്രൊപ്രൈറ്റർഷിപ്പ്.\nഇൻവെസ്റ്റർ: \"ഒരു കമ്പനി മതി\"", [
 ("A","wide","തോമസേ, ഷീറ്റ് കച്ചവടം ഒന്ന് എന്റെ പേരിൽ, ഒന്ന് അമ്മയുടെ പേരിൽ. ഇൻവെസ്റ്റർ പറയുന്നു, ഇത് പറ്റില്ല, ഒറ്റ കമ്പനി വേണം."),
 ("V","V","ജോയിച്ചാ, കമ്പനി ആയാൽ ഫയലിംഗ് ആണ് പേടി, അല്ലേ?"),
 ("A","A","അതേ. എല്ലാ മാസവും ഓഫീസിൽ കയറി ഇറങ്ങണം എന്നാ കേട്ടത്."),
 ("V","wide","വർഷത്തിൽ പ്രധാനമായി 3 തീയതി. സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, 30 ദിവസത്തിനുള്ളിൽ AOC-4, 60 ദിവസത്തിനുള്ളിൽ MGT-7."),
 ("A","A","ഇതിനാണോ ഞാൻ രണ്ട് കട ഉണ്ടാക്കിയത്?"),
 ("V","wide","കോംപ്ലയൻസ് ഭൂതമല്ല, കലണ്ടറാണ്.")],
 "കോംപ്ലയൻസ് ഭൂതമല്ല,\nകലണ്ടറാണ്", CTA_ROC, theme="crm",
 cap_ml="കോംപ്ലയൻസ് പേടിച്ച് രണ്ട് പ്രൊപ്രൈറ്റർഷിപ്പ് നടത്തി, ഇൻവെസ്റ്റർ ഒറ്റ കമ്പനി ചോദിച്ചു. പ്രൈവറ്റ് ലിമിറ്റഡിന്റെ വാർഷിക ഫയലിംഗ്: സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7. ഇത് പേടിയാണോ?",
 cap_en="A rubber sheet trader ran two proprietorships to avoid company compliance, and an investor asked for one clean company. A private limited company's yearly ROC filings are mainly three dates: AGM by 30 September, AOC-4 within 30 days and MGT-7 within 60 days of it. Scared of compliance: yes or no?",
 cap_mg="Compliance pedichu randu proprietorship nadathi, investor otta company chodichu. Pvt Ltd-nte yearly filing: September 30-nullil AGM, 30 divasathil AOC-4, 60 divasathil MGT-7. Ithu pediyaano?")

duo("rc004", "late_filer", "B", "photocopy", "\"ലേറ്റ് ഫീക്ക് ഒരു\nലിമിറ്റ് ഉണ്ടാകുമല്ലോ\"\nഇല്ല", [
 ("A","wide","ഉണ്ണീ, നിന്റെ വെഡ്ഡിംഗ് ഫോട്ടോഗ്രഫി കമ്പനിയുടെ AOC-4 ഫയൽ ചെയ്തോ?"),
 ("V","V","അശ്വതീ, സീസൺ തിരക്കാ. ലേറ്റ് ഫീക്ക് എന്തായാലും ഒരു മാക്സിമം കാണുമല്ലോ."),
 ("A","A","ഇല്ല. ഒരു ഫോമിന് ദിവസം 100 രൂപ. ലിമിറ്റ് ഇല്ല."),
 ("V","wide","AOC-4-ഉം MGT-7-ഉം രണ്ടും വൈകിയാൽ?"),
 ("A","A","രണ്ട് ഫോം, ഓരോന്നിനും ദിവസം 100. ഒരു വർഷം വൈകിയാൽ എഴുപത്തി മൂവായിരം."),
 ("V","wide","ക്യാമറ ക്ലിക്ക് ചെയ്യാത്ത ദിവസവും മീറ്റർ ഓടും.")],
 "ദിവസം 100,\nഒരു ഫോമിന്,\nലിമിറ്റ് ഇല്ല", CTA_ROC, theme="faq",
 cap_ml="ROC ലേറ്റ് ഫീക്ക് ലിമിറ്റ് ഉണ്ടെന്ന് കരുതിയോ? ഒരു ഫോമിന് ദിവസം 100 രൂപ, ലിമിറ്റ് ഇല്ല. AOC-4-ഉം MGT-7-ഉം ഒരു വർഷം വൈകിയാൽ എഴുപത്തി മൂവായിരം. നിങ്ങളുടെ കമ്പനി ഈ വർഷം ഫയൽ ചെയ്തോ?",
 cap_en="Think ROC late fees have a maximum? They don't: Rs 100 a day for each form, with no cap. Two forms a year late (AOC-4 and MGT-7) add up to Rs 73,000. Has your company filed this year: yes or no?",
 cap_mg="ROC late fee-kku limit undennu karuthiyo? Oru form-inu divasam 100 roopa, limit illa. AOC-4-um MGT-7-um oru varsham vaikiyaal 73,000. Ningalude company ee varsham file cheytho?")

duo("rc005", "dormant_company", "C", "handloom", "നഷ്ടത്തിലാണ് കമ്പനി.\n\"കണക്ക് ഫയൽ\nചെയ്യേണ്ടല്ലോ?\"", [
 ("A","wide","കുമാറേ, കഥകളി വേഷത്തിന്റെ കമ്പനി ഈ വർഷം നഷ്ടത്തിലാ. ലാഭമില്ലെങ്കിൽ കണക്ക് ആരെ കാണിക്കാൻ?"),
 ("V","V","ലീലേച്ചീ, ലാഭം ഉള്ളവർ മാത്രമാണ് ഫയൽ ചെയ്യുന്നത് എന്ന് ആരാ പറഞ്ഞേ?"),
 ("A","A","നഷ്ടം കാണിക്കാൻ നാണക്കേടല്ലേ?"),
 ("V","wide","AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4. ബിസിനസ് ഇല്ലെങ്കിലും നഷ്ടമാണെങ്കിലും ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ വേഷം അഴിച്ചാലും കണക്ക് അഴിക്കാൻ പറ്റില്ല."),
 ("V","wide","നഷ്ടവും ഒരു നമ്പറാണ്. അതും ഫയൽ ചെയ്യണം.")],
 "നഷ്ടവും ഒരു നമ്പറാണ്,\nഅതും ഫയൽ ചെയ്യണം", CTA_FILING, theme="new",
 cap_ml="കമ്പനി നഷ്ടത്തിലാണെങ്കിൽ കണക്ക് ഫയൽ ചെയ്യേണ്ടേ? വേണം. AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4, ബിസിനസ് ഇല്ലാത്ത വർഷവും. നിങ്ങളുടെ കമ്പനി ഈ വർഷം: ലാഭമോ നഷ്ടമോ?",
 cap_en="A Kathakali costume company made a loss this year: does it still file accounts with the ROC? Yes. AOC-4 is due within 30 days of the AGM, even in a year with a loss or no business at all. Your company this year: profit or loss?",
 cap_mg="Company nashtathilaanenkil kanakku file cheyyende? Venam. AGM kazhinju 30 divasathinullil AOC-4, business illaatha varshavum. Ningalude company ee varsham: laabhamo nashtamo?")

duo("rc006", "dormant_company", "A", "petrolpump", "\"കമ്പനി പൂട്ടാൻ\nഎളുപ്പവഴി: ഫയൽ\nചെയ്യാതിരിക്കുക\"", [
 ("A","wide","ഷിബൂ, നമ്മുടെ ടയർ റീട്രെഡിംഗ് കമ്പനി നിർത്തി. ഇനി ഫയലിംഗ് വേണ്ട, തനിയെ പൂട്ടിക്കോളും."),
 ("V","V","സന്തോഷേ, അങ്ങനെ തനിയെ പൂട്ടുന്ന കമ്പനിയൊന്നുമില്ല."),
 ("A","A","ഫയൽ ചെയ്തില്ലെങ്കിൽ ഗവൺമെന്റ് തന്നെ എടുത്തു കളയില്ലേ?"),
 ("V","wide","കളയാം. പക്ഷേ 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാരായ നമ്മൾക്ക് 5 വർഷം അയോഗ്യത വരാം."),
 ("A","A","അപ്പോ പുതിയ കമ്പനി തുടങ്ങാൻ?"),
 ("V","wide","കമ്പനി ഉറങ്ങും, ശിക്ഷ ഉണരും.")],
 "ഫയൽ ചെയ്യാതിരിക്കൽ\nപൂട്ടലല്ല", CTA_FILING, theme="faq",
 cap_ml="ഫയൽ ചെയ്യാതിരുന്നാൽ കമ്പനി തനിയെ പൂട്ടുമോ? 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം, ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യതയും വരാം. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="Planning to close a company by simply not filing? Three years without ROC filings can get the company struck off, and the directors can be disqualified for 5 years. Stopping filings is not closing. Did you know this: yes or no?",
 cap_mg="File cheyyaathirunnaal company thaniye pootumo? 3 varsham file cheythillenkil company strike off aakaam, directors-nu 5 varsham ayogyathayum varaam. Ithu ariyaamaayirunno?")

duo("rc007", "new_company_roc", "B", "library", "\"ലാഭം വരുമ്പോൾ\nഓഡിറ്ററെ വെക്കാം\"\n30 ദിവസം കഴിഞ്ഞു", [
 ("A","wide","അനൂപേ, ട്യൂഷൻ ആപ്പ് കമ്പനി തുടങ്ങിയിട്ട് 40 ദിവസമായി. ഓഡിറ്റർ ആരാ?"),
 ("V","V","ഗ്രീഷ്മേ, ഇതുവരെ ഒരു രൂപ വരുമാനമില്ല. ലാഭം വരുമ്പോൾ ഓഡിറ്ററെ നോക്കാം."),
 ("A","A","ലാഭം നോക്കിയല്ല നിയമം. തീയതി നോക്കിയാണ്."),
 ("V","wide","എന്ത് തീയതി?"),
 ("A","A","കമ്പനി തുടങ്ങി 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം. നമ്മൾ 10 ദിവസം വൈകി."),
 ("V","wide","ക്ലാസ് തുടങ്ങും മുമ്പേ ഹോംവർക്ക് പെൻഡിംഗ്.")],
 "ആദ്യ ഓഡിറ്റർ:\n30 ദിവസത്തിനുള്ളിൽ", CTA_ROC, theme="new",
 cap_ml="പുതിയ കമ്പനിക്ക് ലാഭം വരുമ്പോൾ മാത്രം ഓഡിറ്റർ മതിയോ? ഇല്ല. കമ്പനി തുടങ്ങി 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ദിവസമായി?",
 cap_en="Waiting for profits before appointing an auditor? A new private limited company must appoint its first auditor within 30 days of incorporation, revenue or not. How old is your company in days?",
 cap_mg="Puthiya company-kku laabham varumpol maathram auditor mathiyo? Illa. Company thudangi 30 divasathinullil aadya auditor-e niyamikkanam. Ningalude company-kku ethra divasamaayi?")

chat("rcc002", "llp_owner", "C", "മെയിൽ ഫോം 11\nഫയൽ ചെയ്തു.\n\"ഈ വർഷം കഴിഞ്ഞു\"", ("ഗായത്രി", "അനന്തു"), [
 (1,"ഗായത്രീ, LLP-യുടെ ഫോം 11 മെയ് 30-ന് മുമ്പ് ചെയ്തു. ഇനി അടുത്ത വർഷം നോക്കിയാൽ മതി."),
 (0,"അനന്തൂ, പകുതിയേ ആയുള്ളൂ. ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ വേണം."),
 (1,"രണ്ടോ? അക്വേറിയം മീൻ വളർത്തലിന് ഇത്ര ഫോമോ?"),
 (0,"LLP-ക്ക് വർഷത്തിൽ രണ്ട്: മെയ് 30, ഒക്ടോബർ 30. ബിസിനസ് ഇല്ലെങ്കിലും."),
 (1,"ഇന്ന് നവംബർ ആയല്ലോ..."),
 (0,"മീൻ ടാങ്കിൽ, ഫോം പെൻഡിംഗിൽ.")],
 "LLP: മെയ് 30-ഉം\nഒക്ടോബർ 30-ഉം", CTA_FILING, theme="faq",
 cap_ml="LLP-ക്ക് വർഷത്തിൽ ഒരു ഫയലിംഗ് അല്ല, രണ്ട്: Form 11 മെയ് 30-നുള്ളിൽ, Form 8 ഒക്ടോബർ 30-നുള്ളിൽ. ബിസിനസ് ഇല്ലാത്ത വർഷവും. നിങ്ങൾ രണ്ടും ചെയ്തോ?",
 cap_en="An LLP files twice a year, not once: Form 11 by 30 May and Form 8 by 30 October, even in a year with no business. Filed Form 11 and stopped there? Did you file both: yes or no?",
 cap_mg="LLP-kku varshathil oru filing alla, randu: Form 11 May 30-nullil, Form 8 October 30-nullil. Business illaatha varshavum. Ningal randum cheytho?")

duo("rc008", "late_filer", "A", "hotellobby", "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"കഴിഞ്ഞ 3 വർഷത്തെ\nAOC-4?\" ഒന്നുമില്ല", [
 ("A","wide","ജെയ്സൺ, ഇൻവെസ്റ്റർ മീറ്റിംഗ് നന്നായി പോയി. പക്ഷേ അവസാനം ചോദിച്ചു, 3 വർഷത്തെ AOC-4 കാണിക്കാൻ."),
 ("V","V","നീതൂ, കമ്പനി വെറുതെ കിടക്കുകയായിരുന്നല്ലോ. അപ്പോ ഫയലിംഗ് ഇല്ല."),
 ("A","A","അതാണ് പ്രശ്നം. വെറുതെ കിടന്ന വർഷവും ഫയലിംഗ് വേണമായിരുന്നു."),
 ("V","wide","ഇനി?"),
 ("A","A","ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ, ലിമിറ്റ് ഇല്ല. ഇൻവെസ്റ്റ്മെന്റിന് മുമ്പ് ഇത് ശരിയാക്കണം."),
 ("V","wide","പൈസ വരും മുമ്പ് പഴയ കടം തീർക്കണം.")],
 "ഉറങ്ങിയ വർഷവും\nഫയലിംഗ് വേണം", CTA_ROC, theme="crm",
 cap_ml="കമ്പനി കുറച്ച് കാലം വെറുതെ കിടന്നു, ആരും ഫയൽ ചെയ്തില്ല. ഇൻവെസ്റ്റ്മെന്റിന്റെ സമയത്ത് ഇൻവെസ്റ്റർ 3 വർഷത്തെ AOC-4 ചോദിച്ചു. ലേറ്റ് ഫീ ഒരു ഫോമിന് ദിവസം 100 രൂപ, ലിമിറ്റ് ഇല്ല. നിങ്ങളുടെ ഫയലിംഗ് അപ്ഡേറ്റ് ആണോ?",
 cap_en="A company sat idle for a while and nobody filed; the founder found out when an investor asked for three years of AOC-4. Filings are due even in idle years, and the late fee is Rs 100 a day per form with no cap. Are your filings up to date: yes or no?",
 cap_mg="Company kurachu kaalam veruthe kidannu, aarum file cheythilla. Investment samayathu investor 3 varshathe AOC-4 chodichu. Late fee oru form-inu divasam 100 roopa, limit illa. Ningalude filing update aano?")

lst("rcl001", "new_company_roc", "B", "പ്രൈവറ്റ് ലിമിറ്റഡ്:\nകലണ്ടറിൽ വെക്കേണ്ട\n3 തീയതി", [
 ("സെപ്റ്റംബർ 30", "AGM നടത്തണം. ഓരോ ഡയറക്ടറുടെയും DIR-3 KYC-യും ഇതിനുള്ളിൽ."),
 ("AGM + 30 ദിവസം", "AOC-4: കമ്പനിയുടെ കണക്കുകൾ."),
 ("AGM + 60 ദിവസം", "MGT-7: വാർഷിക റിട്ടേൺ. വൈകിയാൽ ദിവസം 100 രൂപ, ലിമിറ്റ് ഇല്ല.")],
 "ഇതിൽ ഏതാണ്\nനിങ്ങൾ മറന്നത്?", CTA_ROC, theme="faq",
 cap_ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയുടെ വർഷത്തിലെ 3 തീയതി: സെപ്റ്റംബർ 30-നുള്ളിൽ AGM-ഉം DIR-3 KYC-യും, AGM കഴിഞ്ഞ് 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7. ഏതാണ് നിങ്ങൾ മറന്നത്: 1, 2, 3?",
 cap_en="Three dates for every private limited company: AGM and each director's DIR-3 KYC by 30 September, AOC-4 within 30 days of the AGM, MGT-7 within 60 days. Late fee Rs 100 a day per form, no cap. Which one did you forget: 1, 2 or 3?",
 cap_mg="Pvt Ltd company-yude varshathile 3 theeyathi: September 30-nullil AGM-um DIR-3 KYC-yum, AGM kazhinju 30 divasathil AOC-4, 60 divasathil MGT-7. Ethaanu ningal marannathu: 1, 2, 3?")

duo("rc009", "dormant_company", "C", "ferry", "വള്ളംകളി ടീമിന്റെ\nകമ്പനി. \"ഓഗസ്റ്റിൽ\nമാത്രമല്ലേ പണി?\"", [
 ("A","wide","ടോണീ, നമ്മുടെ ചുണ്ടൻ വള്ളം ടീമിന്റെ കമ്പനിക്ക് AGM നടത്തിയോ?"),
 ("V","V","മീരേ, വള്ളംകളി കഴിഞ്ഞാൽ കമ്പനിയും വിശ്രമിക്കും. 11 മാസം ഒന്നുമില്ല."),
 ("A","A","വിശ്രമിക്കാം. പക്ഷേ സെപ്റ്റംബർ 30-നുള്ളിൽ AGM വേണം. പിന്നെ 30 ദിവസത്തിൽ AOC-4, 60-ൽ MGT-7."),
 ("V","wide","ട്രോഫി കിട്ടിയ മാസം തന്നെ ഡെഡ്‌ലൈനും?"),
 ("A","A","അതെ. ബിസിനസ് ഇല്ലാത്ത മാസവും ഫയലിംഗ് ഉണ്ട്."),
 ("V","wide","വള്ളം കരയ്ക്ക് കയറും, ഫയലിംഗ് കയറില്ല.")],
 "വള്ളം കരയ്ക്ക് കയറും,\nഫയലിംഗ് കയറില്ല", CTA_FILING, theme="new",
 cap_ml="വർഷത്തിൽ ഒരു സീസൺ മാത്രം പണിയുള്ള കമ്പനിക്കും AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, പിന്നെ AOC-4-ഉം MGT-7-ഉം. ബിസിനസ് ഇല്ലാത്ത മാസങ്ങളിലും ഫയലിംഗ് ഉറങ്ങില്ല. നിങ്ങളുടെ ബിസിനസ് സീസണലാണോ?",
 cap_en="A snake-boat race team's company only works in August, so can it skip the AGM? No: AGM by 30 September, AOC-4 within 30 days and MGT-7 within 60 days, busy season or not. Is your business seasonal or year-round?",
 cap_mg="Varshathil oru season maathram paniyulla company-kkum AGM September 30-nullil, pinne AOC-4-um MGT-7-um. Business illaatha maasangalilum filing urangilla. Ningalude business seasonal aano?")

duo("rc010", "nri_director", "A", "gulfoffice", "ഭർത്താവിന്റെ കമ്പനിയിൽ\nഡയറക്ടർ. \"ഞാൻ\nറിയാദിലല്ലേ?\"", [
 ("A","wide","ആസിഫ്, നാട്ടിലെ കമ്പനിയിൽ എന്നെയും ഡയറക്ടർ ആക്കിയില്ലേ? ഞാൻ ഇവിടെ നഴ്സ് ആയതുകൊണ്ട് എനിക്ക് ഒന്നും ചെയ്യാനില്ലല്ലോ."),
 ("V","V","ഷഹാനാ, എല്ലാം ഞാൻ നോക്കിക്കോളാം എന്നാ ഞാനും കരുതിയത്."),
 ("A","A","പിന്നെ എന്താ പ്രശ്നം?"),
 ("V","wide","DIR-3 KYC ഓരോ ഡയറക്ടറും സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. ഗൾഫിൽ ആണെങ്കിലും."),
 ("A","A","അപ്പോ ഡയറക്ടർ എന്ന പേര് മാത്രമല്ല, ഡ്യൂട്ടിയും ഉണ്ട്."),
 ("V","wide","വിസ ഏത് നാട്ടിലായാലും KYC നാട്ടിലെ കലണ്ടറിൽ.")],
 "ഗൾഫിലെ ഡയറക്ടർക്കും\nസെപ്റ്റംബർ 30", CTA_ROC, theme="crm",
 cap_ml="ഗൾഫിൽ ജോലി ചെയ്യുന്ന ഭാര്യ നാട്ടിലെ കമ്പനിയിൽ ഡയറക്ടർ. വിദേശത്താണെങ്കിലും ഓരോ ഡയറക്ടറും DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. നിങ്ങളുടെ കമ്പനിയിൽ ഗൾഫിലുള്ള ഡയറക്ടർ ഉണ്ടോ?",
 cap_en="A nurse in Riyadh is a director in her husband's Kerala company and assumes there is nothing for her to do. Every director, including NRI directors, must complete DIR-3 KYC by 30 September. Does your company have a director abroad: yes or no?",
 cap_mg="Gulf-il joli cheyyunna bhaarya naattile company-il director. Videshathaanenkilum oro director-um DIR-3 KYC September 30-nullil cheyyanam. Ningalude company-il Gulf-ilulla director undo?")
