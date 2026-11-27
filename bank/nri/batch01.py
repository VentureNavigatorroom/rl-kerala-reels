# nri batch 01 (27 Nov refill): first 3D tea-shop reels for the pravasi-founder topic. Max 6 lines, painful moment first, payoff by line 4-5.
# Situations from bank/STORY_THEMES.md (#16, #26) and common online questions; names, sectors, towns invented. Facts only from topics.FACTS_NRI.
# Never promise a loan or subsidy, never say when a subsidy is released, never our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, toon, S, C, T, topics = _h.duo, _h.toon, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA


# crm (#16, Gulf Malayali investing): buys a cousin's co-founder's shares, nobody files FC-TRS
duo("pvd001", "nri_investing", "B", "gulfoffice", "കസിന്റെ കമ്പനിയിൽ\nഷെയർ വാങ്ങി.\nRBI-ക്ക് ആര് പറയും?", [
 ("A","wide","ആസിഫ്, നാട്ടിലെ കസിന്റെ മസാല കമ്പനിയിൽ ഷെയർ വാങ്ങി എന്ന് കേട്ടല്ലോ. കമ്പനി പുതിയ ഷെയർ തന്നതാണോ?"),
 ("V","V","അല്ല ഷഹാന. പോയ ഒരു പാർട്ണറുടെ ഷെയർ ഞാൻ വാങ്ങി. പൈസ അയച്ചു, പേപ്പർ ഒപ്പിട്ടു. കഴിഞ്ഞു."),
 ("A","A","കഴിഞ്ഞില്ല. നാട്ടിലുള്ള ആളിൽ നിന്ന് NRI ഷെയർ വാങ്ങിയാൽ 60 ദിവസത്തിനകം FC-TRS ഫയൽ ചെയ്യണം."),
 ("V","V","അയ്യോ, ഇപ്പോ തന്നെ ഒരു മാസം ആയി. ഇന്ന് കസിനെ വിളിക്കാം."),
 ("A","wide","പൈസ അയച്ചാൽ പകുതി, റിപ്പോർട്ട് ചെയ്താൽ മുഴുവൻ.")],
 "ഷെയർ കൈമാറിയോ?\n60 ദിവസം, FC-TRS", CTA_PRAVASI, theme="crm",
 cap_ml="ഗൾഫിലിരുന്ന് നാട്ടിലെ കമ്പനിയിൽ ഒരാളുടെ ഷെയർ വാങ്ങിയോ? നാട്ടിലുള്ള ആളിൽ നിന്ന് NRI ഷെയർ വാങ്ങിയാൽ 60 ദിവസത്തിനകം FC-TRS ഫയൽ ചെയ്യണം. കമ്പനി പുതിയ ഷെയർ തന്നതാണെങ്കിൽ 30 ദിവസത്തിനകം FC-GPR. നിങ്ങളുടേത് ഏതാണ്?",
 cap_en="A Gulf Malayali buys a departing partner's shares in his cousin's Kerala company, sends the money and thinks it's done. When a non-resident buys shares from a resident, FC-TRS must be filed within 60 days of the transfer; fresh shares issued by the company need FC-GPR within 30 days. Which one was yours?",
 cap_mg="Gulf-il irunnu naattile company-il oraalude share vaangiyo? Naattilulla aalil ninnu NRI share vaangiyaal 60 divasathinakam FC-TRS file cheyyanam. Company puthiya share thannathaanel 30 divasathinakam FC-GPR. Ningaludethu ethaanu?")

# crm (#26 Gulf returnee): counts the NDPREM capital subsidy as his own share of the money
duo("pvd002", "returnee_loan", "A", "airport", "സബ്സിഡി കിട്ടും എന്ന്\nകണക്കിൽ എഴുതി.\nബാങ്ക് ചിരിച്ചു", [
 ("A","wide","റഫീഖേ, 12 വർഷം കഴിഞ്ഞ് ഇനി നാട്ടിൽ തന്നെ. ബേക്കറി പ്ലാനിൽ NORKA സബ്സിഡി എന്റെ വിഹിതമായി എഴുതി."),
 ("V","V","ഷമീറേ, അത് ആദ്യം ഉറപ്പിക്കാമോ? NDPREM-ൽ ലോൺ തരുന്നത് ബാങ്കാണ്. ലോൺ ബാങ്ക് അനുവദിച്ചാലല്ലേ സബ്സിഡിയുടെ ചോദ്യം വരൂ."),
 ("A","A","അപ്പോ സബ്സിഡി ഉറപ്പല്ലേ?"),
 ("V","wide","ഒന്നും ഉറപ്പല്ല. ബാങ്ക് നോക്കുന്നത് നിന്റെ പ്ലാനും തിരിച്ചടവും ആണ്. സബ്സിഡി ഇല്ലാതെയും നിൽക്കുന്ന കണക്ക് ഉണ്ടാക്ക്."),
 ("A","A","കിട്ടാത്ത പൈസ കൊണ്ട് കട പണിയരുത്.")],
 "സബ്സിഡി ഇല്ലാതെയും\nനിൽക്കുന്ന പ്ലാൻ", CTA_NORKA, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് സ്ഥിരമായി തിരിച്ചെത്തി ബിസിനസ് പ്ലാൻ ചെയ്യുകയാണോ? NORKA NDPREM-ൽ ലോൺ തീരുമാനിക്കുന്നത് പാർട്ണർ ബാങ്കാണ്; സബ്സിഡി ആരും ഉറപ്പ് തരുന്നില്ല. സബ്സിഡി ഇല്ലാതെയും നിൽക്കുന്ന കണക്കുമായി ബാങ്കിൽ പോകൂ. നിങ്ങളുടെ പ്ലാൻ ഏത് ബിസിനസിനാണ്?",
 cap_en="A Gulf returnee writes the NORKA subsidy into his bakery plan as his own contribution. Under NDPREM the partner bank decides the loan, and nobody can promise the subsidy. Take the bank a plan whose numbers work even without it. What business are you planning?",
 cap_mg="Gulf-il ninnu sthiramaayi thirichethi business plan cheyyukayaano? NORKA NDPREM-il loan theerumaanikkunnathu partner bank aanu; subsidy aarum urappu tharunnilla. Subsidy illaatheyum nilkkunna kanakkumaayi bank-il pokoo. Ningalude plan ethu business-inaanu?")

# faq: "PMEGP is a government scheme, so the loan is sure"
duo("pvd003", "returnee_loan", "B", "akshaya", "സർക്കാർ സ്കീം അല്ലേ,\nലോൺ ഉറപ്പ്!\nഅങ്ങനെയാണോ?", [
 ("V","wide","സുധേ, PMEGP-ക്ക് അപേക്ഷ കൊടുത്തു. സർക്കാർ സ്കീം അല്ലേ, ലോൺ ഉറപ്പല്ലേ?"),
 ("A","A","രമേശേട്ടാ, അപേക്ഷ കൊടുത്താൽ ലോൺ ഉറപ്പാകില്ല. PMEGP ലോൺ തീരുമാനിക്കുന്നത് ബാങ്കാണ്."),
 ("V","V","അപ്പോ ഞാൻ എന്ത് ചെയ്യണം?"),
 ("A","wide","ബാങ്ക് ചോദിക്കുന്ന പ്രോജക്റ്റ് റിപ്പോർട്ട് വൃത്തിയായി റെഡി ആക്കൂ. എന്ത് ഉണ്ടാക്കും, ആർക്ക് വിൽക്കും, എങ്ങനെ തിരിച്ചടയ്ക്കും."),
 ("V","V","സ്കീമിന്റെ പേരല്ല, എന്റെ പ്ലാനാണ് ബാങ്ക് വായിക്കുന്നത്.")],
 "സ്കീം വാതിൽ തുറക്കും,\nപ്ലാൻ അകത്ത് കയറ്റും", CTA_PRAVASI, theme="faq",
 cap_ml="PMEGP-ക്ക് അപേക്ഷിച്ചാൽ ലോൺ ഉറപ്പാണെന്ന് കരുതിയോ? PMEGP ലോൺ തീരുമാനിക്കുന്നത് ബാങ്കാണ്. എന്ത് ഉണ്ടാക്കും, ആർക്ക് വിൽക്കും, എങ്ങനെ തിരിച്ചടയ്ക്കും എന്ന് വ്യക്തമാക്കുന്ന പ്രോജക്റ്റ് റിപ്പോർട്ടാണ് ബാങ്ക് നോക്കുന്നത്. നിങ്ങളുടെ റിപ്പോർട്ട് റെഡിയാണോ?",
 cap_en="Applied for PMEGP and assumed the loan is certain because it is a government scheme? PMEGP loans are decided by banks. What the bank reads is your project report: what you will make, who will buy it and how you will repay. Is your report ready?",
 cap_mg="PMEGP-kku apekshichaal loan urappaanennu karuthiyo? PMEGP loan theerumaanikkunnathu bank aanu. Enthu undaakkum, aarkku vilkkum, engane thirichadakkum ennu vyakthamaakkunna project report aanu bank nokkunnathu. Ningalude report ready aano?")

# faq: worked abroad 18 months, wants NDPREM
duo("pvd004", "gulf_returnee", "B", "gulfroom", "ഒന്നര വർഷം ഗൾഫിൽ.\nNORKA സ്കീമിന്\nഅപേക്ഷിക്കാമോ?", [
 ("A","wide","ഷംസൂ, ഒന്നര വർഷം ഇവിടെ നിന്നു. മതിയായി. നാട്ടിൽ പോയി NORKA സ്കീമിൽ ഒരു വർക്ക്ഷോപ്പ് തുടങ്ങാം എന്ന് വിചാരിക്കുന്നു."),
 ("V","V","നസീറേ, NDPREM-ന് 2 വർഷമെങ്കിലും വിദേശത്ത് ജോലി ചെയ്തിരിക്കണം. ഒന്നര വർഷം പോരാ."),
 ("A","A","ആറ് മാസം കൂടി നിന്നാലോ?"),
 ("V","wide","അത് നിന്റെ തീരുമാനം. പക്ഷേ വിദേശ ജോലിയുടെ രേഖകൾ ശരിയാണോ എന്ന് നോക്കിയിട്ട് ടിക്കറ്റ് എടുക്ക്. ലോൺ പിന്നെയും ബാങ്കിന്റെ തീരുമാനം."),
 ("A","A","ടിക്കറ്റിന് മുമ്പ് കലണ്ടർ നോക്കണം.")],
 "2 വർഷം തികഞ്ഞോ?\nടിക്കറ്റിന് മുമ്പ് നോക്കൂ", CTA_NORKA, theme="faq",
 cap_ml="NORKA NDPREM 2 വർഷമെങ്കിലും വിദേശത്ത് ജോലി ചെയ്ത് സ്ഥിരമായി നാട്ടിൽ തിരിച്ചെത്തിയവർക്കാണ്. ഒന്നര വർഷം പോരാ. തിരിച്ചു വരുന്നതിന് മുമ്പ് വിദേശ ജോലിയുടെ രേഖകൾ നോക്കൂ. ലോൺ തീരുമാനിക്കുന്നത് ബാങ്കാണ്. നിങ്ങൾ എത്ര വർഷം വിദേശത്ത് ജോലി ചെയ്തു?",
 cap_en="NORKA NDPREM is for Keralites who return for good after at least 2 years of work abroad; 18 months is not enough. Check your overseas work records before you book the ticket home, and remember the bank decides the loan. How many years have you worked abroad?",
 cap_mg="NORKA NDPREM 2 varshamenkilum videshathu joli cheythu sthiramaayi naattil thirichethiyavarkkaanu. Onnara varsham pora. Thirichu varunnathinu mumpu videsha joliyude rekhakal nokkoo. Loan theerumaanikkunnathu bank aanu. Ningal ethra varsham videshathu joli cheythu?")

# new: quiet year at a family homestay company with a Gulf son as shareholder; FLA still due
duo("pvd005", "family_business_nri", "C", "veranda", "ഈ കൊല്ലം ഒന്നും\nമാറിയില്ല. എന്നിട്ടും\nRBI-ക്ക് റിട്ടേൺ?", [
 ("A","wide","ബാലേട്ടാ, മോൻ ഖത്തറിൽ നിന്ന് വിളിച്ചു. നമ്മുടെ ഹോംസ്റ്റേ കമ്പനിയുടെ FLA റിട്ടേൺ കൊടുത്തോ എന്ന്."),
 ("V","V","ശാന്തേ, ഈ കൊല്ലം പുതിയ ഷെയറും ഇല്ല, പുതിയ പൈസയും ഇല്ല. പിന്നെ എന്തിനാ റിട്ടേൺ?"),
 ("A","A","മോൻ NRI ആയി ഷെയർ ഉള്ളിടത്തോളം FLA റിട്ടേൺ എല്ലാ വർഷവും ജൂലൈ 15-നകം കൊടുക്കണം എന്നാ അവൻ പറഞ്ഞത്."),
 ("V","V","എങ്കിൽ കലണ്ടറിൽ ജൂലൈ 15 ചുവപ്പിൽ എഴുതാം."),
 ("A","wide","കണക്ക് മാറിയില്ലെങ്കിലും തീയതി മാറില്ല.")],
 "NRI ഷെയർ ഉണ്ടോ?\nFLA, ജൂലൈ 15", CTA_PRAVASI, theme="new",
 cap_ml="ഗൾഫിലുള്ള മകനോ ബന്ധുവോ നിങ്ങളുടെ കമ്പനിയിൽ ഷെയർ ഉടമയാണോ? ആ വർഷം പുതിയ നിക്ഷേപം ഒന്നും ഇല്ലെങ്കിലും FLA റിട്ടേൺ ജൂലൈ 15-നകം RBI-ക്ക് കൊടുക്കണം. നിങ്ങളുടെ കമ്പനിയിൽ NRI ഷെയർ ഉടമ ഉണ്ടോ?",
 cap_en="A son in Qatar holds shares in his parents' homestay company, and they skip the FLA return because nothing changed this year. With a non-resident shareholder, the FLA return is due to the RBI by 15 July every year, even in a quiet year. Does your company have an NRI shareholder?",
 cap_mg="Gulf-ilulla makano bandhuvo ningalude company-il share udamayaano? Aa varsham puthiya nikshepam onnum illenkilum FLA return July 15-nakam RBI-kku kodukkanam. Ningalude company-il NRI share udama undo?")
