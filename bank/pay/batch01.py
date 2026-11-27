# Pay batch 01 (27 Nov, first 3D tea-shop reels for the new topic). Max 6 lines, painful moment first, payoff by line 4-5.
# Facts only from topics.FACTS_PAY. Invented names, sectors and towns. Never a fee, price or promised incentive.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ESIC, CTA_PAYROLL = topics.CTA_ESIC, topics.CTA_PAYROLL

# faq: "a message saying 'come from tomorrow' is the appointment"
duo("pyd001", "first_hire", "A", "salon", "\"നാളെ മുതൽ വന്നോ\"\nഎന്ന മെസേജ്.\nഅതാണോ ജോലി ഓർഡർ?", [
 ("A","wide","വിനീതേ, പുതിയ ബ്യൂട്ടീഷ്യന് ഞാൻ ഫോണിൽ മെസേജ് അയച്ചു: നാളെ മുതൽ വന്നോ. അത്ര മതിയല്ലോ?"),
 ("V","V","സോണിയ ചേച്ചീ, അത് മതിയാകില്ല. പുതിയ ലേബർ കോഡ് പ്രകാരം എല്ലാ സ്റ്റാഫിനും അപ്പോയിന്റ്മെന്റ് ലെറ്റർ കൊടുക്കണം."),
 ("A","A","രണ്ട് പേർ മാത്രമുള്ള സലൂണിനും?"),
 ("V","wide","അതെ. ജോലി, ശമ്പളം, തുടങ്ങിയ തീയതി എഴുതിയ ഒരു ലെറ്റർ. പിന്നീട് തർക്കം വന്നാൽ അതാണ് തെളിവ്."),
 ("A","A","മെസേജ് മായും, ലെറ്റർ നിൽക്കും.")],
 "ആദ്യ സ്റ്റാഫ് മുതൽ\nഅപ്പോയിന്റ്മെന്റ് ലെറ്റർ", CTA_PAYROLL, theme="faq",
 cap_ml="ഫോണിൽ \"നാളെ മുതൽ വന്നോ\" എന്ന് അയച്ചാൽ ജോലി ഓർഡർ ആകില്ല. 2025 നവംബർ 21 മുതൽ നിലവിലുള്ള ലേബർ കോഡ് പ്രകാരം എല്ലാ സ്റ്റാഫിനും അപ്പോയിന്റ്മെന്റ് ലെറ്റർ കൊടുക്കണം, ചെറിയ സ്ഥാപനത്തിലും. നിങ്ങളുടെ സ്റ്റാഫിന് ലെറ്റർ കിട്ടിയിട്ടുണ്ടോ?",
 cap_en="A salon owner hires a beautician with a one-line phone message: come from tomorrow. Under the Labour Codes in force since 21 November 2025, every employee needs an appointment letter, even in a two-person business. It records the job, the pay and the start date, and it is the proof if there is ever a dispute. Have all your staff got one?",
 cap_mg="Phone-il \"naale muthal vanno\" ennu ayachaal job order aakilla. 2025 November 21 muthal ulla Labour Code prakaaram ella staff-inum appointment letter kodukkanam, cheriya sthaapanathilum. Ningalude staff-inu letter kittiyittundo?")

# new: Munnar homestay hires for the season and crosses 10 staff
duo("pyd002", "ten_staff", "B", "homestay", "സീസൺ വന്നു,\nസ്റ്റാഫ് 7-ൽ നിന്ന് 11.\nആരും ശ്രദ്ധിച്ചില്ല", [
 ("A","wide","ജോമോനേ, ക്രിസ്മസ് സീസണിന് മൂന്ന് കുക്കും ഒരു ഡ്രൈവറും കൂടി എടുത്തു. ഇപ്പോൾ ഹോംസ്റ്റേയിൽ 11 പേർ."),
 ("V","V","ടീനേ, അപ്പോൾ ESIC നോക്കിയോ? 10 പേരോ അതിൽ കൂടുതലോ ആയാൽ ESIC രജിസ്ട്രേഷൻ വേണം."),
 ("A","A","സീസൺ കഴിഞ്ഞാൽ അവർ പോകും. എന്നിട്ടും?"),
 ("V","wide","എണ്ണം 10 കടക്കുന്ന സമയമാണ് നോക്കുന്നത്. മാസം 21,000 രൂപ വരെ ശമ്പളമുള്ളവർ അതിൽ വരും."),
 ("A","A","അപ്പോൾ ഇന്ന് തന്നെ സ്റ്റാഫ് ലിസ്റ്റ് എണ്ണാം."),
 ("V","wide","സീസൺ തീരും, നിയമം തീരില്ല.")],
 "10 കടന്നാൽ\nESIC നോക്കൂ", CTA_ESIC, theme="new",
 cap_ml="സീസണിൽ സ്റ്റാഫ് കൂട്ടിയപ്പോൾ ഹോംസ്റ്റേയിൽ 11 പേരായി. 10 പേരോ കൂടുതലോ ഉള്ള സ്ഥാപനത്തിന് ESIC രജിസ്ട്രേഷൻ വേണം; മാസം 21,000 രൂപ വരെ ശമ്പളമുള്ളവർ അതിൽ വരും. നിങ്ങളുടെ സ്ഥാപനത്തിൽ ഇപ്പോൾ എത്ര സ്റ്റാഫ്?",
 cap_en="A Munnar homestay hires extra cooks and a driver for the Christmas season and quietly goes from 7 to 11 staff. Establishments with 10 or more employees need ESIC registration, covering staff earning up to 21,000 a month. How many people work with you right now?",
 cap_mg="Season-il staff koottiyappol homestay-il 11 perayi. 10 pero kooduthalo ulla sthaapanathinu ESIC registration venam; maasam 21,000 roopa vare shambalamullavar athil varum. Ningalude sthaapanathil ippol ethra staff?")

# crm (small business expanding): garage owner adds a second branch, EPF ceiling changed
duo("pyd003", "twenty_staff", "B", "garage", "രണ്ടാമത്തെ ഷോപ്പ്.\nസ്റ്റാഫ് 20.\nPF പഴയ കണക്കിൽ", [
 ("A","wide","ജിതിനേ, പുതിയ ബ്രാഞ്ച് തുറന്നപ്പോൾ നമ്മൾ 20 പേരായി. EPF എടുക്കണം എന്ന് അക്കൗണ്ടന്റ് പറഞ്ഞു."),
 ("V","V","ഐശ്വര്യേ, ശരി. 15,000 രൂപയ്ക്ക് മുകളിൽ ശമ്പളമുള്ള മെക്കാനിക്കുകൾ അതിൽ വരില്ലല്ലോ?"),
 ("A","A","ആ പരിധി മാറി. 2026 സെപ്റ്റംബർ 17 മുതൽ EPF ശമ്പള പരിധി 25,000 രൂപയാണ്."),
 ("V","V","അപ്പോൾ ലിസ്റ്റ് പുതിയ പരിധി വെച്ച് വീണ്ടും നോക്കണം."),
 ("A","wide","പഴയ പരിധി ഓർമ്മയിൽ, പുതിയത് നിയമത്തിൽ.")],
 "EPF പരിധി ഇപ്പോൾ\n25,000 രൂപ", CTA_ESIC, theme="crm",
 cap_ml="ഗാരേജിന് രണ്ടാമത്തെ ബ്രാഞ്ച് തുറന്നപ്പോൾ സ്റ്റാഫ് 20 ആയി. 20 പേരായാൽ EPF നിർബന്ധം. EPF ശമ്പള പരിധി 2026 സെപ്റ്റംബർ 17 മുതൽ 25,000 രൂപ (മുമ്പ് 15,000). പഴയ പരിധി വെച്ചാണോ നിങ്ങൾ ഇപ്പോഴും കണക്ക് നോക്കുന്നത്?",
 cap_en="A garage opens a second branch and reaches 20 staff, so EPF applies. The owner assumes mechanics earning above 15,000 stay outside it, but the EPF wage ceiling is 25,000 a month from 17 September 2026 (it was 15,000). Are you still checking your staff list against the old limit?",
 cap_mg="Garage-inu randaamathe branch thurannappol staff 20 aayi. 20 peraayaal EPF nirbandham. EPF wage ceiling 2026 September 17 muthal 25,000 roopa (mumpu 15,000). Pazhaya limit vechaano ningal ippozhum kanakku nokkunnathu?")

# faq: "small basic, big allowances, so PF stays low"
duo("pyd004", "salary_split", "A", "textile", "ബേസിക് ചെറുത്,\nഅലവൻസ് വലുത്.\nഇനി ആ ട്രിക്ക് ഇല്ല", [
 ("A","wide","പ്രകാശേട്ടാ, ടെക്സ്റ്റൈൽസിലെ സെയിൽസ് സ്റ്റാഫിന് ബേസിക് കുറച്ച്, ബാക്കി എല്ലാം അലവൻസ് ആക്കിയാൽ PF കുറയില്ലേ?"),
 ("V","V","രമ്യേ, പുതിയ ലേബർ കോഡിൽ അലവൻസ് ശമ്പളത്തിന്റെ 50%-ൽ കൂടിയാൽ ആ അധികം 'വേജസി'ൽ തിരികെ കൂട്ടും."),
 ("A","A","അപ്പോൾ പേര് മാറ്റിയിട്ട് കാര്യമില്ല."),
 ("V","wide","ഇല്ല. ആദ്യം ഇപ്പോഴത്തെ ശമ്പള ഘടന പുതിയ നിയമം വെച്ച് ഒന്ന് നോക്ക്."),
 ("A","wide","പേര് മാറിയാലും കണക്ക് മാറില്ല.")],
 "അലവൻസ് 50% കടന്നാൽ\nവേജസിൽ കൂട്ടും", CTA_PAYROLL, theme="faq",
 cap_ml="ബേസിക് കുറച്ച് അലവൻസ് കൂട്ടി PF കുറയ്ക്കാമെന്ന് കരുതുന്നുണ്ടോ? 2025 നവംബർ 21 മുതൽ നിലവിലുള്ള ലേബർ കോഡ് പ്രകാരം അലവൻസ് ശമ്പളത്തിന്റെ 50%-ൽ കൂടിയാൽ ആ അധിക ഭാഗം വേജസിൽ തിരികെ കൂട്ടും. നിങ്ങളുടെ സ്റ്റാഫിന്റെ ശമ്പള ഘടന പുതിയ നിയമം വെച്ച് നോക്കിയോ?",
 cap_en="A textile shop plans to keep the basic small and call the rest allowances, so PF stays low. Under the Labour Codes, allowances above 50% of pay are added back to wages, so renaming pay changes nothing. Have you checked your salary structure against the new rule?",
 cap_mg="Basic kurachu allowance kootti PF kurakkaam ennu karuthunnundo? 2025 November 21 muthal ulla Labour Code prakaaram allowance shambalathinte 50%-il koodiyaal aa adhika bhaagam wages-il thirike koottum. Ningalude staff-inte salary structure puthiya niyamam vechu nokkiyo?")

# new: courier office still running on "the old Acts"
duo("pyd005", "ten_staff", "C", "courier", "\"പഴയ നിയമം അല്ലേ?\"\nലേബർ കോഡ് വന്നിട്ട്\nഒരു വർഷം", [
 ("A","wide","അരവിന്ദേ, നമ്മുടെ കൊറിയർ ഓഫീസിലെ ശമ്പള രീതി പത്ത് വർഷമായി ഒന്നാണ്. ആരും ഒന്നും പറഞ്ഞിട്ടില്ല."),
 ("V","V","ജയേ, 2025 നവംബർ 21 മുതൽ നാല് ലേബർ കോഡുകൾ നിലവിൽ വന്നു. പഴയ രീതി അതേപടി തുടരാൻ പറ്റില്ല."),
 ("A","A","എവിടെ നിന്ന് തുടങ്ങും?"),
 ("V","wide","മൂന്ന് കാര്യം: എല്ലാവർക്കും അപ്പോയിന്റ്മെന്റ് ലെറ്റർ, അലവൻസ് 50% കടക്കുന്നുണ്ടോ, സ്റ്റാഫ് എണ്ണം ESIC-നും EPF-നും."),
 ("A","A","പത്ത് വർഷത്തെ ശീലം, ഒരു വർഷത്തെ നിയമം."),
 ("V","wide","ശീലം പഴയതാകാം, നിയമം പുതിയതാണ്.")],
 "പഴയ ശമ്പള രീതി?\nലേബർ കോഡ് നോക്കൂ", CTA_PAYROLL, theme="new",
 cap_ml="നാല് ലേബർ കോഡുകൾ 2025 നവംബർ 21 മുതൽ നിലവിലുണ്ട്. പഴയ ശമ്പള രീതി ഒന്ന് നോക്കൂ: എല്ലാവർക്കും അപ്പോയിന്റ്മെന്റ് ലെറ്റർ ഉണ്ടോ, അലവൻസ് ശമ്പളത്തിന്റെ 50% കടക്കുന്നുണ്ടോ, സ്റ്റാഫ് എണ്ണം ESIC (10+), EPF (20+) പരിധിയിൽ എത്തിയോ. ഇതിൽ ഏതാണ് നിങ്ങൾ ഇനിയും നോക്കാത്തത്?",
 cap_en="A courier office has paid staff the same way for ten years. The four Labour Codes have been in force since 21 November 2025, so start with three checks: an appointment letter for everyone, allowances above 50% of pay, and staff count against ESIC (10+) and EPF (20+). Which one haven't you checked yet?",
 cap_mg="Naalu Labour Code-kal 2025 November 21 muthal nilavilundu. Pazhaya salary reethi onnu nokku: ellavarkkum appointment letter undo, allowance shambalathinte 50% kadakkunnundo, staff ennam ESIC (10+), EPF (20+) limit-il ethiyo. Ithil ethaanu ningal iniyum nokkaathathu?")
