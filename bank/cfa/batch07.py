# Co-founder agreements batch 07 (27 Nov, owner's idea): partner disputes, deadlock, "prevent it with the agreement".
# Situations: STORY_THEMES.md F23-F30 (forum patterns, mixed; names, sectors and towns invented). Never one real person's story.
# Facts only from topics.FACTS_CFA "Partner disputes". General information, never advice on a case: every reel says a lawyer
# must see the documents. Never promise an outcome, never say police / court WILL act, never criticise police or lawyers. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

# F23 + F29: 50/50 LLP deadlock; the agreement is silent, so the First Schedule default (majority, one vote each) gives no answer
duo("cf039", "friends_cofounders", "A", "handloom", "50/50 എൽഎൽപി.\nഅവൻ 'വേണം', ഞാൻ 'വേണ്ട'.\nഇനി ആര് തീരുമാനിക്കും?", [
 ("A","wide","കുമാരേട്ടാ, കൈത്തറി യൂണിറ്റിന് പുതിയ ഷോറൂം വേണമെന്ന് പാർട്ണർ. വേണ്ടെന്ന് ഞാൻ. രണ്ടുപേർക്കും 50%."),
 ("V","V","ലീലേ, നിങ്ങളുടെ എൽഎൽപി എഗ്രിമെന്റ് ഇതിനെക്കുറിച്ച് എന്ത് പറയുന്നു?"),
 ("A","A","ഷെയറും ലാഭവും മാത്രം എഴുതി. തീരുമാനം, തർക്കം ഒന്നിനെക്കുറിച്ചും ഒരു വരി പോലുമില്ല."),
 ("V","V","എഗ്രിമെന്റ് മിണ്ടാത്ത കാര്യത്തിൽ എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ വരും. അവിടെ ഒരാൾക്ക് ഒരു വോട്ട്, തീരുമാനം ഭൂരിപക്ഷത്തിന്."),
 ("A","wide","രണ്ടുപേർ, രണ്ട് വോട്ട്. ഭൂരിപക്ഷം ഇല്ലല്ലോ."),
 ("V","wide","അതാ കുരുക്ക്. തീരാത്ത തർക്കം ആർബിട്രേഷനിലേക്ക് എന്നും ഷെഡ്യൂളിൽ ഉണ്ട്. നിങ്ങളുടെ കാര്യം ഒരു വക്കീൽ രേഖകൾ നോക്കി പറയട്ടെ.")],
 "ടൈ വന്നാൽ എന്ത്?\nഎഗ്രിമെന്റിൽ എഴുതൂ", CTA_COFOUNDER, theme="faq",
 cap_ml="രണ്ട് പാർട്ണർമാർ, 50/50 എൽഎൽപി, ഒരു തീരുമാനത്തിൽ ഉടക്ക്. എഗ്രിമെന്റ് മിണ്ടാത്ത കാര്യങ്ങളിൽ എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ ആണ് വരുന്നത്: ഒരാൾക്ക് ഒരു വോട്ട്, ഭൂരിപക്ഷ തീരുമാനം; എഗ്രിമെന്റിൽ നിന്നുള്ള തർക്കം അതിനുള്ളിൽ തീർന്നില്ലെങ്കിൽ ആർബിട്രേഷൻ. ഇത് പൊതുവായ വിവരം മാത്രം; നിങ്ങളുടെ കേസ് ഒരു വക്കീൽ രേഖകൾ നോക്കിയേ പറയാവൂ. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ടൈ ബ്രേക്കർ ഉണ്ടോ?",
 cap_en="Two partners, a 50/50 LLP, and one decision they can't agree on. Where the LLP agreement is silent, the LLP Act's First Schedule applies: one vote per partner, decisions by majority, and disputes arising out of the agreement that can't be resolved under it go to arbitration. General information only, not legal advice: a lawyer must look at your documents. Our team can connect you with one. Does your agreement say what happens in a tie?",
 cap_mg="Randu partners, 50/50 LLP, oru theerumaanathil udakku. Agreement mindaatha kaaryangalil LLP niyamathile First Schedule aanu varunnathu: oraalkku oru vote, bhooripaksha theerumaanam; agreement-il ninnulla tharkkam athinullil theernnillenkil arbitration. Ithu pothuvaaya vivaram maathram; ningalude case oru vakeel rekhakal nokkiye parayaavoo. Njangalude team-nu vakeelumaayi bandhippikkaam. Ningalude agreement-il tie breaker undo?")

# F24 + F23: still a partner, runs a competing shop and pulls the firm's customers (First Schedule paras 11-12, LLP only)
duo("cf040", "friends_cofounders", "B", "petrolpump", "പാർട്ണർ സ്വന്തം കട\nതുടങ്ങി. നമ്മുടെ\nകസ്റ്റമേഴ്സുമായി", [
 ("A","wide","ഷിബൂ, നമ്മുടെ എൽഎൽപിയിൽ പാർട്ണർ ആയിരിക്കെ തന്നെ അവൻ അടുത്ത ടൗണിൽ സ്വന്തം ടയർ റീട്രെഡിംഗ് കട തുടങ്ങി."),
 ("V","V","സന്തോഷേട്ടാ, നമ്മുടെ ലോറി ക്ലയന്റ്സിനെ അങ്ങോട്ട് വിളിക്കുന്നുമുണ്ട്. പോയ ആളെ തടയാൻ എളുപ്പമല്ലെന്നല്ലേ കേട്ടത്?"),
 ("A","A","പക്ഷേ അവൻ പോയിട്ടില്ല. ഇപ്പോഴും പാർട്ണറാ. എഗ്രിമെന്റ് ഇതിനെക്കുറിച്ച് മിണ്ടുന്നില്ലെങ്കിൽ നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ നോക്കണം."),
 ("V","V","അതിൽ എന്താ പറയുന്നത്?"),
 ("A","wide","സമ്മതമില്ലാതെ എൽഎൽപിയോട് മത്സരിക്കുന്ന ബിസിനസിലെ ലാഭത്തിന് കണക്ക് പറയണം. എൽഎൽപിയുടെ പേരോ ക്ലയന്റ് ബന്ധമോ ഉപയോഗിച്ചാലും."),
 ("V","wide","അപ്പോ മെസേജും ബില്ലും സൂക്ഷിച്ച്, എഗ്രിമെന്റുമായി ഒരു വക്കീലിനെ കാണാം. തീരുമാനം അവർ നോക്കിയിട്ട്.")],
 "പാർട്ണർ ആയിരിക്കെ മത്സരം:\nലാഭത്തിന് കണക്ക്", CTA_COFOUNDER, theme="faq",
 cap_ml="എൽഎൽപിയിൽ പാർട്ണർ ആയിരിക്കെ തന്നെ ഒരാൾ അതേ ബിസിനസ് സ്വന്തമായി തുടങ്ങി, ഫേമിന്റെ ക്ലയന്റ്സിനെ വിളിക്കുന്നു. എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പറയുന്നത്: സമ്മതമില്ലാതെ മത്സരിക്കുന്ന ബിസിനസിലെ ലാഭത്തിനും, എൽഎൽപിയുടെ പേരോ ബിസിനസ് ബന്ധമോ ഉപയോഗിച്ച് കിട്ടിയ നേട്ടത്തിനും കണക്ക് പറയണം. ഇത് പൊതുവായ വിവരം; നിങ്ങളുടെ കേസ് ഒരു വക്കീൽ രേഖകൾ നോക്കി പറയണം. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം.",
 cap_en="Still a partner in the LLP, he opens the same business on his own and calls the firm's clients. Where the LLP agreement is silent, the LLP Act's First Schedule says a partner who runs a competing business without consent must account for its profits, and for any benefit from using the LLP's name or business connections. General information only: a lawyer must look at your documents. Our team can connect you with one.",
 cap_mg="LLP-il partner aayirikke thanne oraal athe business swanthamaayi thudangi, firm-nte clients-ne vilikkunnu. Agreement mindaathidathu LLP niyamathile First Schedule parayunnathu: sammathamillaathe malsarikkunna business-ile laabhathinum, LLP-yude pero business bandhamo upayogichu kittiya nettathinum kanakku parayanam. Ithu pothuvaaya vivaram; ningalude case oru vakeel rekhakal nokki parayanam. Njangalude team-nu vakeelumaayi bandhippikkaam.")

# F26 + F27: money leaving the firm's account, statements withheld (First Schedule para 10: true accounts to any partner)
duo("cf041", "friends_cofounders", "A", "hospital", "50:50 പാർട്ണർ.\nസ്റ്റേറ്റ്മെന്റ് ചോദിച്ചാൽ\nമറുപടി ഇല്ല", [
 ("A","wide","ജോസഫ് സാറേ, ഞങ്ങളുടെ ലാബ് എൽഎൽപിയുടെ അക്കൗണ്ടിൽ നിന്ന് പാർട്ണർ വലിയ തുക എടുക്കുന്നു. സ്റ്റേറ്റ്മെന്റ് ചോദിച്ചിട്ട് തരുന്നില്ല."),
 ("V","V","ലക്ഷ്മീ, എൽഎൽപി എഗ്രിമെന്റിൽ കണക്ക് കാണിക്കുന്നതിനെക്കുറിച്ച് എന്താ എഴുതിയിരിക്കുന്നത്?"),
 ("A","A","ഒന്നുമില്ല. വിശ്വാസത്തിലാണ് തുടങ്ങിയത്."),
 ("V","V","എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് ഫസ്റ്റ് ഷെഡ്യൂൾ: എൽഎൽപിയുടെ ശരിയായ കണക്കും മുഴുവൻ വിവരവും ഓരോ പാർട്ണറും മറ്റ് പാർട്ണർക്ക് കൊടുക്കണം."),
 ("A","wide","അപ്പോ ഞാൻ ഇപ്പോൾ എന്ത് ചെയ്യണം?"),
 ("V","wide","കയ്യിലുള്ളത് ഒരുമിച്ച് വെക്കൂ: എഗ്രിമെന്റ്, മെസേജുകൾ, കണ്ട എൻട്രികൾ, തീയതി സഹിതം. എന്നിട്ട് വക്കീലിനെ കാണിക്കൂ. വഴി അവർ പറയും.")],
 "കണക്ക് ചോദിക്കാൻ\nപാർട്ണർക്ക് അവകാശം", CTA_COFOUNDER, theme="faq",
 cap_ml="50:50 എൽഎൽപി, അക്കൗണ്ടിൽ നിന്ന് പണം പോകുന്നു, സ്റ്റേറ്റ്മെന്റ് ചോദിച്ചാൽ മറുപടി ഇല്ല. എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പറയുന്നത്: ഓരോ പാർട്ണറും എൽഎൽപിയെ ബാധിക്കുന്ന എല്ലാറ്റിന്റെയും ശരിയായ കണക്കും വിവരവും മറ്റ് പാർട്ണർക്ക് കൊടുക്കണം. രേഖകൾ തീയതി സഹിതം സൂക്ഷിക്കൂ, ഒരു വക്കീലിനെ കാണിക്കൂ. ഇത് പൊതുവായ വിവരം മാത്രം. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം.",
 cap_en="A 50:50 LLP, money leaving the account, and no answer when you ask for the statements. Where the LLP agreement is silent, the LLP Act's First Schedule says every partner must give true accounts and full information of everything affecting the LLP to any partner. Keep your documents with dates and show them to a lawyer. General information only, not legal advice. Our team can connect you with a lawyer.",
 cap_mg="50:50 LLP, account-il ninnu panam pokunnu, statement chodichaal marupadi illa. Agreement mindaathidathu LLP niyamathile First Schedule parayunnathu: oro partner-um LLP-ye baadhikkunna ellaattinteyum shariyaaya kanakkum vivaravum mattu partner-kku kodukkanam. Rekhakal theeyathi sahitham sookshikkoo, oru vakeeline kaanikkoo. Ithu pothuvaaya vivaram maathram. Njangalude team-nu vakeelumaayi bandhippikkaam.")

# F30 (generalised): an arbitral tribunal's interim order about the firm's money is not being followed (s.17(2); CPC O39 R2A)
duo("cf042", "friends_cofounders", "B", "akshaya", "'കേസ് തീരും വരെ\nഅക്കൗണ്ട് തൊടരുത്'\nഎന്നിട്ടും പണം പോയി", [
 ("A","wide","രമേശേട്ടാ, ആർബിട്രേഷൻ തീരും വരെ ഫേമിന്റെ അക്കൗണ്ടിൽ നിന്ന് ആരും പണം എടുക്കരുതെന്ന് ഓർഡർ ഉണ്ട്. എന്നിട്ടും എടുത്തു."),
 ("V","V","സുധേ, ആ ഓർഡർ ആരുടേതാ? കോടതിയുടേതോ ആർബിട്രൽ ട്രിബ്യൂണലിന്റേതോ?"),
 ("A","A","ട്രിബ്യൂണലിന്റേത്. അത് വെറും പേപ്പറല്ലേ എന്നാ മറുവശം പറയുന്നത്."),
 ("V","V","അല്ല. ട്രിബ്യൂണലിന്റെ ഇടക്കാല ഓർഡർ കോടതി ഓർഡർ പോലെ നടപ്പാക്കാം. ലംഘിച്ചാൽ ജപ്തി, സിവിൽ ജയിൽ പോലുള്ള നടപടി കോടതിക്ക് എടുക്കാം."),
 ("A","wide","അത് കോടതി തീരുമാനിക്കും. ഞാൻ ഇപ്പോൾ എന്ത് കയ്യിൽ വെക്കണം?"),
 ("V","wide","ഓർഡറിന്റെ കോപ്പി, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, ഓരോ തീയതിയും. ഇതുമായി വൈകാതെ നിങ്ങളുടെ വക്കീലിനെ കാണൂ.")],
 "ഓർഡർ വെറും പേപ്പറല്ല.\nകോപ്പി കയ്യിൽ വെക്കൂ", CTA_COFOUNDER, theme="new",
 cap_ml="പാർട്ണർ തർക്കത്തിൽ ഇടക്കാല ഓർഡർ ഉണ്ട്, പക്ഷേ മറുവശം പാലിക്കുന്നില്ല. ആർബിട്രേഷൻ നിയമത്തിലെ സെക്ഷൻ 17 പ്രകാരം ട്രിബ്യൂണലിന്റെ ഇടക്കാല ഓർഡർ കോടതി ഓർഡർ പോലെ നടപ്പാക്കാം. കോടതിയുടെ ഇൻജങ്ഷൻ ലംഘിച്ചാൽ സ്വത്ത് ജപ്തി ചെയ്യാനും മൂന്ന് മാസം വരെ സിവിൽ ജയിലിനും കോടതിക്ക് ഉത്തരവിടാം; എന്ത് ചെയ്യണം എന്ന് കോടതി തീരുമാനിക്കും. ഓർഡറിന്റെ കോപ്പിയും തെളിവും തീയതി സഹിതം സൂക്ഷിച്ച് വക്കീലിനെ കാണൂ. ഇത് പൊതുവായ വിവരം മാത്രം. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം.",
 cap_en="There is an interim order in a partner dispute, and the other side is not following it. Under section 17 of the Arbitration and Conciliation Act, an arbitral tribunal's interim order is enforceable like a court order. For disobeying a court injunction, the court may order the person's property attached and civil prison for up to 3 months; what happens is the court's decision. Keep the order copy and your evidence with dates and see your lawyer. General information only, not legal advice. Our team can connect you with a lawyer.",
 cap_mg="Partner tharkkathil idakkaala order undu, pakshe maruvasham paalikkunnilla. Arbitration niyamathile section 17 prakaaram tribunal-nte idakkaala order court order pole nadappaakkaam. Court-nte injunction langhichaal swathu japthi cheyyaanum moonnu maasam vare civil jail-num court-nu uthharavidaam; enthu cheyyanam ennu court theerumaanikkum. Order-nte copy-um thelivum theeyathi sahitham sookshichu vakeeline kaanoo. Ithu pothuvaaya vivaram maathram. Njangalude team-nu vakeelumaayi bandhippikkaam.")

# FAQ: "Can I change my lawyer in the middle of the case?" (CPC Order III Rule 4(2); consent or the court's leave). Respectful to every lawyer.
duo("cf043", "family_cofounders", "A", "home", "പാർട്ണർ കേസ്\nപകുതി വഴിയിൽ.\nവക്കീലിനെ മാറ്റാമോ?", [
 ("A","wide","അരുണേ, കസിനുമായുള്ള പാർട്ണർ കേസ് കോടതിയിലാ. ഞങ്ങളുടെ വക്കീൽ കൂടുതലും കുടുംബ കേസുകൾ നോക്കുന്ന ആളാണ്."),
 ("V","V","സ്നേഹേ, ബിസിനസ് തർക്കങ്ങൾ പതിവായി നോക്കുന്ന ഒരാളെ വേണമെന്നാണോ?"),
 ("A","A","അതെ. പക്ഷേ കേസ് പകുതിക്ക് വക്കീലിനെ മാറ്റാൻ പറ്റുമോ? അത് ശരിയാണോ?"),
 ("V","V","പറ്റും. കക്ഷിക്ക് മറ്റൊരു വക്കീലിനെ വെക്കാം. പഴയ വക്കീലിന്റെ സമ്മതത്തോടെയോ കോടതിയുടെ അനുമതിയോടെയോ പുതിയ ആൾ കേസിൽ വരും."),
 ("A","wide","അപ്പോ ആദ്യം എല്ലാ ഫയലുകളും ഓർഡറുകളും ഒരുമിച്ച് വെക്കാം."),
 ("V","wide","നന്ദി പറഞ്ഞ് മാന്യമായി മാറാം. ഫയലുകൾ കയ്യിൽ ഉണ്ടെങ്കിൽ പുതിയ വക്കീലിന് വേഗം മനസ്സിലാകും.")],
 "വക്കീലിനെ മാറ്റാം.\nഫയലുകൾ കയ്യിൽ വെക്കൂ", CTA_COFOUNDER, theme="faq",
 cap_ml="പാർട്ണർ തർക്കം കോടതിയിൽ, ഇനി ബിസിനസ് തർക്കങ്ങൾ പതിവായി നോക്കുന്ന വക്കീലിനെ വേണം. കേസിന്റെ ഇടയ്ക്കും കക്ഷിക്ക് മറ്റൊരു വക്കീലിനെ വെക്കാം: പഴയ വക്കീലിന്റെ സമ്മതത്തോടെയോ കോടതിയുടെ അനുമതിയോടെയോ പുതിയ ആൾ കേസിൽ വരും. എല്ലാ ഫയലുകളുടെയും ഓർഡറുകളുടെയും കോപ്പി കയ്യിൽ വെക്കൂ. ഇത് പൊതുവായ വിവരം മാത്രം. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം.",
 cap_en="A partner dispute is in court and you want a lawyer who handles business disputes. A party can engage another advocate even in the middle of a case: the new advocate comes on record with the former advocate's consent or the court's permission. Keep copies of every file and order. General information only, not legal advice. Our team can connect you with a lawyer.",
 cap_mg="Partner tharkkam court-il, ini business tharkkangal pathivaayi nokkunna vakeeline venam. Case-nte idaykkum kakshikku mattoru vakeeline vekkaam: pazhaya vakeelinte sammathathodeyo court-nte anumathiyodeyo puthiya aal case-il varum. Ella files-nteyum orders-nteyum copy kayyil vekkoo. Ithu pothuvaaya vivaram maathram. Njangalude team-nu vakeelumaayi bandhippikkaam.")
