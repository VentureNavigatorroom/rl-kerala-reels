# ROC annual compliance batch 07 (28 Nov night). Fix-it reels: late fee Rs 100 a day per form (no cap) with arithmetic only in
# check_bank-approved amounts; 3 years of non-filing -> directors disqualified 5 years / strike-off. New situations only.
# Facts only from topics.FACTS_ROC. People, sectors and towns invented. No prices of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rcd006", "late_filer", "A", "foodcourt", "AOC-4 പത്ത് ദിവസം\nവൈകി. \"ഇത്ര ചെറിയ\nകാര്യത്തിന് എന്തിന്?\"", [
 ("A","wide","ഡെന്നിസേ, ചിപ്സ് കമ്പനിയുടെ AOC-4 പത്ത് ദിവസം വൈകി. ക്രിസ്മസ് ഓർഡർ കഴിഞ്ഞ് ഫെബ്രുവരിയിൽ നോക്കാം."),
 ("V","V","മരിയേ, ഇന്ന് നവംബർ 9. AGM സെപ്റ്റംബർ 30-ന് ആയിരുന്നു, അപ്പോ AOC-4-ന്റെ അവസാന ദിവസം ഒക്ടോബർ 30."),
 ("A","A","പത്ത് ദിവസത്തിന് എന്ത് ആകാനാ?"),
 ("V","V","ഒരു ഫോമിന് ദിവസം 100 രൂപ. ഇന്ന് ഫയൽ ചെയ്താൽ 1,000 രൂപ. ഫെബ്രുവരി 7 വരെ നീട്ടിയാൽ 10,000 രൂപ."),
 ("A","wide","അപ്പോ ചിപ്സ് വറുക്കുന്നതിന് മുമ്പ് ഫോം."),
 ("V","wide","വൈകിയ ഫോം ഇന്ന്, ബാക്കി നാളെ.")],
 "ഇന്ന് 1,000.\nഫെബ്രുവരിയിൽ 10,000", CTA_ROC, theme="faq",
 cap_ml="AGM സെപ്റ്റംബർ 30-ന് ആണെങ്കിൽ AOC-4 ഒക്ടോബർ 30-നുള്ളിൽ. പത്ത് ദിവസം വൈകിയാൽ 1,000 രൂപ, 100 ദിവസം വൈകിയാൽ 10,000 രൂപ: ഓരോ ഫോമിനും ദിവസം 100 രൂപ, പരിധിയില്ല. നിങ്ങളുടെ AOC-4 ഫയൽ ചെയ്തോ?",
 cap_en="AGM on 30 September means AOC-4 is due by 30 October. Ten days late costs Rs 1,000; a hundred days late, Rs 10,000: the ROC late fee is Rs 100 a day per form with no cap. Is your AOC-4 filed?",
 cap_mg="AGM September 30-nu aanenkil AOC-4 October 30-nullil. Pathu divasam vaikiyaal 1,000 roopa, 100 divasam vaikiyaal 10,000 roopa: oro form-num divasam 100 roopa, paridhiyilla. Ningalude AOC-4 file cheytho?")

duo("rcd007", "llp_owner", "B", "balcony", "ഹൗസ്ബോട്ട് സീസൺ\nതുടങ്ങി. LLP ഫോം 8\nഒരു മാസം വൈകി", [
 ("A","wide","വിവേകേ, ബോട്ട് ബുക്കിംഗ് എല്ലാം ഫുൾ. LLP-യുടെ ഫോം 8 സീസൺ കഴിഞ്ഞ് മാർച്ചിൽ ചെയ്യാം."),
 ("V","V","അമ്മൂ, ഫോം 8-ന്റെ അവസാന ദിവസം ഒക്ടോബർ 30 ആയിരുന്നു. ഇന്ന് നവംബർ 29, 30 ദിവസം കഴിഞ്ഞു."),
 ("A","A","LLP-ക്കും ദിവസക്കണക്കിൽ ലേറ്റ് ഫീ ഉണ്ടോ?"),
 ("V","V","ഉണ്ട്. ഫോമിന് ദിവസം 100 രൂപ. ഇന്ന് ചെയ്താൽ 3,000 രൂപ. ഡിസംബർ 29 ആയാൽ 6,000 രൂപ. മാർച്ച് വരെ ഓർക്കണ്ട."),
 ("A","wide","ശരി, അടുത്ത ഗസ്റ്റ് വരും മുമ്പ് ഇന്ന് തന്നെ ഫയൽ ചെയ്യാം."),
 ("V","wide","ബോട്ടിന് സീസൺ ഉണ്ട്, മീറ്ററിന് ഇല്ല.")],
 "ബുക്കിംഗ് ഫുൾ ആയാലും\nഫോം 8 മറക്കല്ലേ", CTA_FILING, theme="new",
 cap_ml="LLP-യുടെ ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. ഒരു മാസം വൈകിയാൽ 3,000 രൂപ, രണ്ട് മാസം ആയാൽ 6,000 രൂപ: ഫോമിന് ദിവസം 100 രൂപ ലേറ്റ് ഫീ. സീസൺ തിരക്കിലുള്ള LLP ഉടമയ്ക്ക് ഇത് അയച്ചുകൊടുക്കൂ.",
 cap_en="An LLP's Form 8 is due by 30 October. One month late costs Rs 3,000 and two months Rs 6,000: the late fee is Rs 100 a day per form. Send this to an LLP owner busy with the tourist season.",
 cap_mg="LLP-yude Form 8 October 30-nullil. Oru maasam vaikiyaal 3,000 roopa, randu maasam aayaal 6,000 roopa: form-nu divasam 100 roopa late fee. Season thirakkulla LLP owner-kku ithu ayachukodukkoo.")

duo("rcd008", "late_filer", "A", "mall", "\"രണ്ട് വർഷത്തേത്\nഒന്നിച്ച് ചെയ്താൽ\nപണി കുറയും\"", [
 ("A","wide","ജാഫറേ, പെർഫ്യൂം കിയോസ്ക് കമ്പനിയുടെ കഴിഞ്ഞ വർഷത്തെ AOC-4, MGT-7 വിട്ടുപോയി. ഈ വർഷത്തേതിനൊപ്പം ഒന്നിച്ച് ചെയ്യാം."),
 ("V","V","സുമയ്യാ, ആ രണ്ട് ഫോമും ഇപ്പോൾ തന്നെ 150 ദിവസം വൈകി. ഓരോന്നിനും ദിവസം 100 രൂപ."),
 ("A","A","അപ്പോ ഇപ്പോ എത്ര ആയി?"),
 ("V","V","ഓരോന്നിനും 15,000. രണ്ടിനും കൂടി 30,000 രൂപ. പരിധി ഇല്ല. ഒന്നിച്ച് ചെയ്യാൻ കാത്തിരിക്കുന്ന ഓരോ ദിവസവും കൂടും."),
 ("A","wide","ഒന്നിച്ച് ചെയ്താൽ പണി കുറയും, പക്ഷേ ലേറ്റ് ഫീ കൂടും."),
 ("V","wide","പഴയ ഫോം ഇന്ന്, പുതിയത് സമയത്ത്.")],
 "കാത്തിരിക്കുന്ന ഓരോ\nദിവസവും കൂടും", CTA_ROC, theme="faq",
 cap_ml="വിട്ടുപോയ AOC-4, MGT-7 അടുത്ത വർഷത്തേതിനൊപ്പം ചെയ്യാൻ കാത്തിരിക്കരുത്. രണ്ട് ഫോം 150 ദിവസം വൈകിയാൽ തന്നെ 30,000 രൂപ ലേറ്റ് ഫീ, പരിധിയില്ല. പഴയ ഫോമുകൾ ഇന്ന് തന്നെ ഫയൽ ചെയ്യൂ.",
 cap_en="Missed last year's AOC-4 and MGT-7? Don't wait to file them with next year's. Two forms 150 days late already cost Rs 30,000 in late fees, and there is no cap. File the old forms today.",
 cap_mg="Vittupoya AOC-4, MGT-7 adutha varshathethinoppam cheyyaan kaathirikkaruthu. Randu form 150 divasam vaikiyaal thanne 30,000 roopa late fee, paridhiyilla. Pazhaya forms innu thanne file cheyyoo.")

duo("rcd009", "dormant_company", "B", "busstop", "\"രണ്ട് വർഷമേ\nആയുള്ളൂ. മൂന്ന്\nആകട്ടെ, നോക്കാം\"", [
 ("A","wide","അഖിലേ, കൂൺ ഫാം കമ്പനി രണ്ട് വർഷമായി ഒന്നും ഫയൽ ചെയ്തില്ല. പ്രശ്നം മൂന്ന് വർഷം ആകുമ്പോഴല്ലേ?"),
 ("V","V","ജിബിനേ, ലേറ്റ് ഫീ ആദ്യ ദിവസം മുതൽ ഓടുന്നുണ്ട്. ഓരോ ഫോമിനും ദിവസം 100 രൂപ, പരിധിയില്ല."),
 ("A","A","എന്നാലും മൂന്നാം വർഷം എന്താ പ്രത്യേകത?"),
 ("V","V","3 വർഷം ഫയൽ ചെയ്യാതിരുന്നാൽ ഡയറക്ടർമാർ 5 വർഷത്തേക്ക് അയോഗ്യരാകാം. കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം."),
 ("A","wide","അപ്പോ മൂന്നാം വർഷം കാത്തിരിക്കേണ്ട തീയതിയല്ല, ഒഴിവാക്കേണ്ട കുഴിയാ."),
 ("V","wide","രണ്ടാം വർഷം തന്നെ കയറി വരണം.")],
 "മൂന്നാം വർഷം\nകാത്തിരിക്കല്ലേ", CTA_FILING, theme="crm",
 cap_ml="ഫയലിംഗ് മുടങ്ങിയ കമ്പനിക്ക് ലേറ്റ് ഫീ ആദ്യ ദിവസം മുതൽ: ഓരോ ഫോമിനും ദിവസം 100 രൂപ. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത, കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം. രണ്ട് വർഷം മുടങ്ങിയ കൂട്ടുകാരന് അയച്ചുകൊടുക്കൂ.",
 cap_en="A company that stops filing pays late fees from day one: Rs 100 a day per form. After 3 years of non-filing, directors can be disqualified for 5 years and the company struck off. Send this to the friend who is two years behind.",
 cap_mg="Filing mudangiya company-kku late fee aadya divasam muthal: oro form-num divasam 100 roopa. 3 varsham file cheythillenkil directors-nu 5 varsham ayogyatha, company strike off aakaam. Randu varsham mudangiya koottukaaranu ayachukodukkoo.")

duo("rcd010", "new_company_roc", "A", "office", "\"ഭർത്താവ് KYC\nചെയ്തല്ലോ. കമ്പനിക്ക്\nഅത് പോരേ?\"", [
 ("A","wide","രാഹുലേ, നമ്മുടെ കാറ്ററിംഗ് കമ്പനിയിൽ നമ്മൾ രണ്ടുപേരും ഡയറക്ടർമാർ. നീ KYC ചെയ്തല്ലോ, അത് മതിയല്ലോ?"),
 ("V","V","നേഹേ, അത് എന്റെ DIR-3 KYC മാത്രമാ. ഓരോ ഡയറക്ടറും സ്വന്തം KYC ചെയ്യണം."),
 ("A","A","കമ്പനി ഒന്നല്ലേ? എന്നിട്ടും രണ്ടോ?"),
 ("V","V","കമ്പനിക്ക് ഒരു AGM. ഡയറക്ടർക്ക് ഓരോരുത്തർക്കും ഓരോ KYC. എല്ലാവരുടേതും സെപ്റ്റംബർ 30-നുള്ളിൽ."),
 ("A","wide","ഒരേ അടുക്കള, ഒരേ കമ്പനി, KYC മാത്രം വെവ്വേറെ."),
 ("V","wide","ഡയറക്ടർ രണ്ട്, KYC രണ്ട്.")],
 "ഡയറക്ടർ രണ്ട്,\nKYC രണ്ട്", CTA_ROC, theme="faq",
 cap_ml="ഭാര്യയും ഭർത്താവും ഡയറക്ടർമാരാണോ? ഒരാൾ DIR-3 KYC ചെയ്താൽ പോരാ: ഓരോ ഡയറക്ടറും സ്വന്തം KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. നിങ്ങളുടെ കമ്പനിയിൽ എത്ര ഡയറക്ടർമാർ?",
 cap_en="Husband and wife both directors? One DIR-3 KYC is not enough: every director must complete their own KYC by 30 September. How many directors does your company have?",
 cap_mg="Bharyayum bharthaavum directors aano? Oraal DIR-3 KYC cheythaal poraa: oro director-um swantham KYC September 30-nullil cheyyanam. Ningalude company-il ethra directors?")

duo("rcd011", "late_filer", "B", "mobileshop", "\"MGT-7 ഫയൽ ചെയ്തു.\nകണക്കും അതിൽ\nപോയി, കഴിഞ്ഞു\"", [
 ("A","wide","ഷഫീഖേ, മൊബൈൽ ആക്സസറീസ് കമ്പനിയുടെ MGT-7 കസിൻ ഫയൽ ചെയ്തു. കണക്ക് കൊടുക്കലും കഴിഞ്ഞല്ലോ?"),
 ("V","V","സൽമാ, MGT-7 വാർഷിക റിട്ടേൺ ആണ്. കമ്പനിയുടെ കണക്കുകൾ പോകുന്നത് AOC-4-ൽ."),
 ("A","A","അത് വേറെ ഫോമോ? അതിന്റെ തീയതി?"),
 ("V","V","AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4. MGT-7 60 ദിവസത്തിനുള്ളിൽ. ഒന്ന് ചെയ്താൽ മറ്റേത് തീരില്ല."),
 ("A","wide","AOC-4 വൈകിയെങ്കിൽ ദിവസം 100 രൂപ വീതം ഓടുന്നുണ്ട്. ഇന്ന് തന്നെ ചെയ്യാം."),
 ("V","wide","ഒരു ഫോം ചെയ്താൽ രണ്ടും ആകില്ല.")],
 "AOC-4 കണക്ക്,\nMGT-7 റിട്ടേൺ", CTA_ROC, names=("സൽമ", "ഷഫീഖ്"), theme="faq",
 cap_ml="MGT-7 ഫയൽ ചെയ്താൽ കണക്ക് കൊടുത്തതാകില്ല. കമ്പനിയുടെ കണക്കുകൾ AOC-4-ൽ, AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ; MGT-7 60 ദിവസത്തിനുള്ളിൽ. രണ്ടും ചെയ്തോ?",
 cap_en="Filing MGT-7 does not file your accounts. A company's accounts go in AOC-4 within 30 days of the AGM; MGT-7 is due within 60 days. Have you filed both?",
 cap_mg="MGT-7 file cheythaal kanakku koduthathaakilla. Company-yude kanakkukal AOC-4-il, AGM kazhinju 30 divasathinullil; MGT-7 60 divasathinullil. Randum cheytho?")

duo("rcd012", "late_filer", "A", "metro", "പിച്ചിന് മുമ്പ്\nകമ്പനി ചെക്ക് ചെയ്തു.\n2 ഫോം 250 ദിവസം വൈകി", [
 ("A","wide","കിരണേ, കഴിഞ്ഞ പിച്ചിൽ അവർ ചോദിച്ചത് പേപ്പറുകൾ. ഇത്തവണ ആദ്യം നോക്കി: കഴിഞ്ഞ വർഷത്തെ AOC-4, MGT-7 ഇല്ല."),
 ("V","V","അഞ്ജലീ, രണ്ടും 250 ദിവസം വൈകി. ഓരോന്നിനും 25,000, രണ്ടിനും കൂടി 50,000 രൂപ."),
 ("A","A","പിച്ച് കഴിഞ്ഞിട്ട് ഫയൽ ചെയ്താൽ പോരേ?"),
 ("V","V","ഇനിയും 250 ദിവസം കാത്താൽ 1 ലക്ഷം രൂപ ആകും. പരിധിയില്ല. ഇന്ന് ഫയൽ ചെയ്താൽ മീറ്റർ അവിടെ നിൽക്കും."),
 ("A","wide","ശരി. പിച്ച് ഡെക്കിന് മുമ്പ് പെൻഡിംഗ് ഫോമുകൾ."),
 ("V","wide","പേപ്പർ ശരിയായാൽ പിച്ചിനും ധൈര്യം.")],
 "പിച്ചിന് മുമ്പ്\nപെൻഡിംഗ് ഫോം", CTA_ROC, theme="crm",
 cap_ml="ഇൻവെസ്റ്ററെ കാണും മുമ്പ് കമ്പനിയുടെ ഫയലിംഗ് നോക്കൂ. രണ്ട് ഫോം 250 ദിവസം വൈകിയാൽ 50,000 രൂപ ലേറ്റ് ഫീ; 500 ദിവസം ആയാൽ 1 ലക്ഷം രൂപ. ഇന്ന് ഫയൽ ചെയ്താൽ അവിടെ നിൽക്കും.",
 cap_en="Check your company's ROC filings before you meet an investor. Two forms 250 days late cost Rs 50,000 in late fees; at 500 days it becomes Rs 1 lakh. Filing today stops the count.",
 cap_mg="Investor-e kaanum mumbu company-yude filing nokku. Randu form 250 divasam vaikiyaal 50,000 roopa late fee; 500 divasam aayaal 1 laksham roopa. Innu file cheythaal avide nilkkum.")

duo("rcd013", "new_company_roc", "B", "hospital", "ഡ്യൂ ഡേറ്റ്\nസെപ്റ്റംബർ 26. KYC\nഡ്യൂ ഡേറ്റ് 30", [
 ("A","wide","ജോസഫേ, ഡോക്ടർ പറഞ്ഞ തീയതി സെപ്റ്റംബർ 26. കമ്പനിയുടെ കാര്യം ഒക്ടോബറിൽ നോക്കാം."),
 ("V","V","ലക്ഷ്മീ, നീയും ഡയറക്ടറാ. നിന്റെ DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ വേണം. AGM-ഉം അതിനുള്ളിൽ."),
 ("A","A","കുഞ്ഞ് വരുന്ന ആഴ്ച ഞാൻ ഫോം ഒപ്പിടാനോ?"),
 ("V","V","വേണ്ട. ഓഗസ്റ്റിൽ തന്നെ KYC-യും AGM-ഉം തീർക്കാം. സെപ്റ്റംബറിൽ കുഞ്ഞ് മാത്രം."),
 ("A","wide","ആശുപത്രി ബാഗിനൊപ്പം ഡെഡ്ലൈനും പാക്ക് ചെയ്യാം."),
 ("V","wide","വലിയ ദിവസത്തിന് മുമ്പ് ചെറിയ ഡെഡ്ലൈൻ.")],
 "സെപ്റ്റംബർ തിരക്കാണോ?\nഓഗസ്റ്റിൽ തീർക്കൂ", CTA_ROC, theme="new",
 cap_ml="AGM-ഉം എല്ലാ ഡയറക്ടർമാരുടെയും DIR-3 KYC-യും സെപ്റ്റംബർ 30-നുള്ളിൽ. സെപ്റ്റംബറിൽ വലിയ തിരക്ക് വരുമെങ്കിൽ ഓഗസ്റ്റിൽ തന്നെ തീർക്കൂ. സെപ്റ്റംബറിൽ തിരക്കുള്ള ഡയറക്ടർക്ക് അയച്ചുകൊടുക്കൂ.",
 cap_en="The AGM and every director's DIR-3 KYC are due by 30 September. If September will be busy, finish both in August. Send this to a director with a big September ahead.",
 cap_mg="AGM-um ella directors-nteyum DIR-3 KYC-yum September 30-nullil. September-il valiya thirakku varumenkil August-il thanne theerkkoo. September-il thirakkulla director-kku ayachukodukkoo.")

duo("rcd014", "llp_owner", "A", "teashop", "പൂരം കഴിഞ്ഞു.\nനെറ്റിപ്പട്ടം ഓർഡർ\nതീർന്നു. മെയ് 30?", [
 ("A","wide","വിഷ്ണൂ, പൂരം സീസണിൽ നെറ്റിപ്പട്ടം ഓർഡർ ഇരട്ടിയായി. ഇനി കുറച്ച് ദിവസം വിശ്രമം."),
 ("V","V","അനൂ, നമ്മുടെ LLP-യുടെ ഫോം 11 മെയ് 30-നുള്ളിൽ വേണം. ഇന്ന് മെയ് 22, എട്ട് ദിവസം കൂടി."),
 ("A","A","അയ്യോ, ആനയുടെ പട്ടം നോക്കി, ഫോം നോക്കിയില്ല."),
 ("V","V","മെയ് 30 കഴിഞ്ഞാൽ ഫോമിന് ദിവസം 100 രൂപ. ഫോം 8 ഒക്ടോബർ 30-ന്. വിശ്രമം ഫോം 11 കഴിഞ്ഞ്."),
 ("A","wide","പൂരത്തിന് വെടിക്കെട്ട്, മെയ് 30-ന് മുമ്പ് ഫോം 11."),
 ("V","wide","പൂരം കഴിഞ്ഞാൽ അടുത്തത് ഫോം 11.")],
 "പൂരം കഴിഞ്ഞാൽ\nഫോം 11", CTA_FILING, theme="new",
 cap_ml="ഉത്സവ സീസൺ കഴിയുമ്പോൾ LLP-യുടെ ഫോം 11 മെയ് 30-നുള്ളിൽ; ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. മെയ് 30 കഴിഞ്ഞാൽ ഫോമിന് ദിവസം 100 രൂപ ലേറ്റ് ഫീ. നിങ്ങളുടെ LLP ഫോം 11 ചെയ്തോ?",
 cap_en="Festival season over? An LLP's Form 11 is due by 30 May and Form 8 by 30 October. Miss 30 May and the late fee is Rs 100 a day per form. Has your LLP filed Form 11?",
 cap_mg="Ulsava season kazhiyumbol LLP-yude Form 11 May 30-nullil; Form 8 October 30-nullil. May 30 kazhinjaal form-nu divasam 100 roopa late fee. Ningalude LLP Form 11 cheytho?")

duo("rcd015", "new_company_roc", "B", "cafe", "\"ബാങ്ക് അക്കൗണ്ട്\nതുറന്ന ദിവസം മുതൽ\nഅല്ലേ 30 ദിവസം?\"", [
 ("A","wide","റോഷാ, കോഫി റോസ്റ്ററി കമ്പനിക്ക് ബാങ്ക് അക്കൗണ്ട് ഇന്നലെ കിട്ടി. ഓഡിറ്ററെ ഇനി 30 ദിവസത്തിനുള്ളിൽ നോക്കിയാൽ മതി."),
 ("V","V","ആൽവിനേ, ആ 30 ദിവസം ബാങ്കിൽ നിന്നല്ല. കമ്പനി രജിസ്റ്റർ ആയ തീയതി മുതലാ."),
 ("A","A","സർട്ടിഫിക്കറ്റ് വന്നിട്ട് 25 ദിവസമായി!"),
 ("V","V","അപ്പോ അഞ്ച് ദിവസമേ ബാക്കി. ആദ്യ ഓഡിറ്ററെ ഈ ആഴ്ച തന്നെ. INC-20A-യുടെ 180 ദിവസവും അതേ തീയതി മുതൽ."),
 ("A","wide","കാപ്പിക്കുരു വറക്കും മുമ്പ് ഓഡിറ്റർ."),
 ("V","wide","ദിവസം എണ്ണുന്നത് സർട്ടിഫിക്കറ്റിൽ നിന്ന്.")],
 "എണ്ണം തുടങ്ങുന്നത്\nസർട്ടിഫിക്കറ്റ് തീയതിയിൽ", CTA_ROC, theme="faq",
 cap_ml="പുതിയ കമ്പനിക്ക് ആദ്യ ഓഡിറ്റർ 30 ദിവസത്തിനുള്ളിൽ, INC-20A 180 ദിവസത്തിനുള്ളിൽ. എണ്ണം തുടങ്ങുന്നത് ഇൻകോർപ്പറേഷൻ തീയതി മുതൽ, ബാങ്ക് അക്കൗണ്ട് തുറന്ന ദിവസം മുതലല്ല. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ദിവസമായി?",
 cap_en="A new company appoints its first auditor within 30 days and files INC-20A within 180 days, counted from the incorporation date, not from the day the bank account opened. How old is your company?",
 cap_mg="Puthiya company-kku aadya auditor 30 divasathinullil, INC-20A 180 divasathinullil. Ennam thudangunnathu incorporation theeyathi muthal, bank account thuranna divasam muthalalla. Ningalude company-kku ethra divasamaayi?")

duo("rcd016", "nri_director", "A", "bank", "\"ബാങ്കിൽ KYC\nകൊടുത്തല്ലോ. ഡയറക്ടർ\nKYC-യും അതല്ലേ?\"", [
 ("A","wide","സനലേ, ഷാർജയിൽ നിന്ന് വന്നത് ബാങ്കിൽ KYC പുതുക്കാനല്ലേ? കമ്പനിയുടെ DIR-3 KYC-യും ചെയ്തോ?"),
 ("V","V","ദീപ്തീ, ഇവിടെ ആധാറും പാസ്പോർട്ടും കൊടുത്തല്ലോ. എല്ലായിടത്തും ഒരു KYC പോരേ?"),
 ("A","A","ഇല്ല. ബാങ്ക് KYC ബാങ്കിന്. DIR-3 KYC ഓരോ ഡയറക്ടറും സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യേണ്ടത്."),
 ("V","V","ഞാൻ ഗൾഫിലല്ലേ, എനിക്കും ബാധകമാണോ?"),
 ("A","A","ഡയറക്ടർ ആണെങ്കിൽ എവിടെ ആയാലും വേണം. നാട്ടിലുള്ള ഈ ആഴ്ച തന്നെ ചെയ്തേക്ക്."),
 ("V","wide","ബാങ്കിന് ഒരു KYC, കമ്പനിക്ക് വേറൊന്ന്.")],
 "ബാങ്ക് KYC വേറെ,\nഡയറക്ടർ KYC വേറെ", CTA_ROC, names=("ദീപ്തി", "സനൽ"), theme="faq",
 cap_ml="ബാങ്കിൽ കൊടുത്ത KYC ഡയറക്ടർ KYC അല്ല. കമ്പനിയിലെ ഓരോ ഡയറക്ടറും, ഗൾഫിലുള്ളവരും, DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. നാട്ടിൽ വരുന്ന പ്രവാസി ഡയറക്ടർക്ക് അയച്ചുകൊടുക്കൂ.",
 cap_en="Your bank KYC is not your director KYC. Every director of a company, including those in the Gulf, must complete DIR-3 KYC by 30 September. Send this to an NRI director visiting home.",
 cap_mg="Bank-il kodutha KYC director KYC alla. Company-ile oro director-um, Gulf-il ullavarum, DIR-3 KYC September 30-nullil cheyyanam. Naattil varunna pravasi director-kku ayachukodukkoo.")

duo("rcd017", "new_company_roc", "B", "veranda", "\"ഒക്ടോബർ 5-ന് നല്ല\nമുഹൂർത്തം. AGM\nഅന്ന് വെക്കാം\"", [
 ("A","wide","സുജിത്തേ, ജ്യോത്സ്യൻ പറഞ്ഞു ഒക്ടോബർ 5 നല്ല ദിവസമാണെന്ന്. ഈ വർഷത്തെ AGM അന്ന് വെക്കാം."),
 ("V","V","ഷൈനീ, AGM-ന് അവസാന തീയതി സെപ്റ്റംബർ 30. ഒക്ടോബർ 5 എത്ര നല്ല ദിവസമായാലും വൈകിയ AGM ആകും."),
 ("A","A","AGM കഴിഞ്ഞാൽ പിന്നെ എന്തൊക്കെ?"),
 ("V","V","AOC-4 AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ, MGT-7 60 ദിവസത്തിനുള്ളിൽ. ഡയറക്ടർ KYC-യും സെപ്റ്റംബർ 30-നുള്ളിൽ."),
 ("A","wide","എങ്കിൽ സെപ്റ്റംബറിലെ നല്ല ദിവസം ജ്യോത്സ്യനോട് ചോദിക്കാം."),
 ("V","wide","മുഹൂർത്തം സെപ്റ്റംബർ 30-നുള്ളിൽ.")],
 "മുഹൂർത്തം നോക്കൂ,\nസെപ്റ്റംബർ 30-നുള്ളിൽ", CTA_ROC, names=("ഷൈനി", "സുജിത്"), theme="new",
 cap_ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയുടെ AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. പിന്നെ AOC-4 30 ദിവസത്തിനുള്ളിൽ, MGT-7 60 ദിവസത്തിനുള്ളിൽ. നല്ല ദിവസം നോക്കുന്നെങ്കിൽ സെപ്റ്റംബർ 30-ന് മുമ്പുള്ളത് നോക്കൂ.",
 cap_en="A private limited company must hold its AGM by 30 September; AOC-4 follows within 30 days and MGT-7 within 60. Picking an auspicious date? Pick one before 30 September.",
 cap_mg="Private limited company-yude AGM September 30-nullil. Pinne AOC-4 30 divasathinullil, MGT-7 60 divasathinullil. Nalla divasam nokkunnenkil September 30-nu mumbullathu nokkoo.")

duo("rcd018", "late_filer", "A", "autostand", "\"ദിവസം 100 രൂപയല്ലേ?\nഒരു ചായക്കാശ്\"", [
 ("A","wide","ഷാജീ, ഓട്ടോ സ്പെയർസ് കമ്പനിയുടെ AOC-4 വൈകിയാൽ ദിവസം 100 രൂപയല്ലേ? ഒരു ചായക്കാശ്."),
 ("V","V","സജീ, ആ ചായ എന്നും കുടിച്ചാൽ? 250 ദിവസം ആകുമ്പോൾ ഒരു ഫോമിന് മാത്രം 25,000 രൂപ."),
 ("A","A","അത്രയൊക്കെ ആകുമോ? എവിടെയെങ്കിലും നിൽക്കില്ലേ?"),
 ("V","V","പരിധി ഇല്ല. MGT-7-ഉം വൈകിയാൽ അതിനും വേറെ. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത."),
 ("A","wide","ചായക്കാശല്ല, ചായക്കട തന്നെ പോകും!"),
 ("V","wide","100 ചെറുതാ, പരിധി ഇല്ലാത്തതാ പ്രശ്നം.")],
 "100 ചെറുതാണ്,\nപരിധി ഇല്ലാത്തതാ പ്രശ്നം", CTA_ROC, theme="faq",
 cap_ml="ROC ലേറ്റ് ഫീ ദിവസം 100 രൂപ ചെറുതായി തോന്നും. പക്ഷേ ഓരോ ഫോമിനും വെവ്വേറെ, പരിധിയില്ല: 250 ദിവസം ആയാൽ ഒരു ഫോമിന് 25,000 രൂപ. 3 വർഷം ആയാൽ ഡയറക്ടർക്ക് അയോഗ്യതയും.",
 cap_en="Rs 100 a day sounds small. But the ROC late fee is per form with no cap: 250 days late is Rs 25,000 for one form, and 3 years of non-filing can disqualify directors.",
 cap_mg="ROC late fee divasam 100 roopa cheruthaayi thonnum. Pakshe oro form-num vevvere, paridhiyilla: 250 divasam aayaal oru form-nu 25,000 roopa. 3 varsham aayaal director-kku ayogyathayum.")
