# esop batch 01 (28 Nov night): seed 3D reels. Facts only from topics.FACTS_ESOP. No prices, no promised results.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ESOP, CTA_OPTIONS = topics.CTA_ESOP, topics.CTA_OPTIONS

duo('esd001', 'key_hire', 'A', 'office', 'വലിയ ശമ്പളം\nകൊടുക്കാൻ ഇല്ല.\nനല്ല ആളെ വേണം', [('A', 'wide', 'രാഹുലേ, നല്ല ഒരു ഡെവലപ്പറെ വേണം. പക്ഷേ വലിയ ശമ്പളം കൊടുക്കാൻ പണമില്ല.'), ('V', 'V', 'നേഹ, ESOP നോക്കിയോ? കമ്പനി വളർന്നാൽ അവർക്കും പങ്ക് കിട്ടും.'), ('A', 'A', 'അതിന് എന്ത് ചെയ്യണം?'), ('V', 'V', 'പ്രൈവറ്റ് ലിമിറ്റഡ് ആയിരിക്കണം. ഷെയർഹോൾഡർമാർ സ്പെഷ്യൽ റെസല്യൂഷൻ വഴി സ്കീം അംഗീകരിക്കണം.'), ('A', 'wide', 'ഗ്രാന്റിനും വെസ്റ്റിംഗിനും ഇടയിൽ കുറഞ്ഞത് ഒരു വർഷം.'), ('V', 'wide', 'ശമ്പളം കുറവ്, പങ്ക് ഉണ്ട്.')],
 'ശമ്പളം കുറവ്,\nപങ്ക് ഉണ്ട്', CTA_ESOP, theme='crm',
 cap_ml='വലിയ ശമ്പളം കൊടുക്കാൻ പറ്റാത്ത സ്റ്റാർട്ടപ്പുകൾക്ക് ESOP വഴി നല്ല ആളുകളെ നിലനിർത്താം. പ്രൈവറ്റ് ലിമിറ്റഡ്, സ്പെഷ്യൽ റെസല്യൂഷൻ, കുറഞ്ഞത് ഒരു വർഷം വെസ്റ്റിംഗ്. നിങ്ങൾ ആർക്കാണ് ESOP നൽകാൻ ആലോചിക്കുന്നത്?',
 cap_en="He can't afford a big salary for a strong developer. An ESOP gives key people a share in the company's growth; it needs a private limited company, a special resolution and at least a year between grant and vesting. Who are you thinking of?",
 cap_mg='Valiya shambalam kodukkaan pattaatha startups-inu ESOP vazhi nalla aalukale nilanirthaam. Private limited, special resolution, kuranjathu oru varsham vesting. Ningal aarkkaanu ESOP nalkaan aalochikkunnathu?')

duo('esd002', 'esop_employee', 'B', 'gym', 'ESOP എക്സർസൈസ്\nചെയ്തു. പിന്നാലെ\nനികുതി!', [('A', 'wide', 'ജസ്റ്റിനേ, ESOP എക്സർസൈസ് ചെയ്തു. ഷെയർ വിറ്റിട്ടില്ല, എന്നിട്ടും നികുതി വന്നു!'), ('V', 'V', 'റിയാ, എക്സർസൈസ് ചെയ്യുമ്പോൾ ഷെയറിന്റെ ഫെയർ വാല്യുവും നിങ്ങൾ കൊടുത്ത വിലയും തമ്മിലുള്ള വ്യത്യാസം ശമ്പളമായി കണക്കാക്കും.'), ('A', 'A', 'വിൽക്കുമ്പോൾ വീണ്ടും?'), ('V', 'V', 'വിൽക്കുമ്പോൾ പിന്നീട് കൂടിയ ഭാഗത്തിന് ക്യാപിറ്റൽ ഗെയിൻസ്.'), ('A', 'wide', 'IMB സർട്ടിഫിക്കറ്റുള്ള സ്റ്റാർട്ടപ്പുകളിൽ മാത്രം ആദ്യത്തെ നികുതി മാറ്റിവെക്കാം.'), ('V', 'wide', 'എക്സർസൈസിന് മുമ്പ് നികുതി കണക്കാക്കുക.')],
 'എക്സർസൈസിന് മുമ്പ്\nനികുതി കണക്കാക്കുക', CTA_OPTIONS, theme='faq',
 cap_ml='ESOP-ന് രണ്ട് തവണ നികുതി: എക്സർസൈസ് ചെയ്യുമ്പോൾ ശമ്പളമായി, വിൽക്കുമ്പോൾ ക്യാപിറ്റൽ ഗെയിൻസ്. IMB സർട്ടിഫിക്കറ്റുള്ള സ്റ്റാർട്ടപ്പുകളിൽ മാത്രം ആദ്യത്തേത് മാറ്റിവെക്കാം; DPIIT മാത്രം പോരാ. നിങ്ങൾക്ക് ESOP ഉണ്ടോ?',
 cap_en='She exercised her ESOPs and got a tax bill without selling anything. The gap between fair value and what they paid is taxed as salary at exercise, and later gains as capital gains on sale; only startups with the IMB certificate let employees defer the first tax. Do you hold ESOPs?',
 cap_mg='ESOP-inu randu thavana tax: exercise cheyyumbol salary aayi, vilkkumbol capital gains. IMB certificate ulla startups-il maathram aadyathe tax maattivekkaam; DPIIT maathram poraa. Ningalkku ESOP undo?')

duo('esd003', 'founder_esop', 'A', 'rooftop', 'ഫൗണ്ടർക്ക്\nESOP കിട്ടുമോ?\nസാധാരണ ഇല്ല', [('A', 'wide', 'ശ്യാമേ, ഞാൻ ഡയറക്ടറാണ്, പതിനഞ്ച് ശതമാനം ഷെയറുണ്ട്. എനിക്കും ESOP എടുക്കാമോ?'), ('V', 'V', 'ആര്യേ, സാധാരണ പ്രൊമോട്ടർമാർക്കും പത്ത് ശതമാനത്തിൽ കൂടുതൽ ഉള്ള ഡയറക്ടർമാർക്കും ESOP കിട്ടില്ല.'), ('A', 'A', 'അപ്പോ വഴിയില്ലേ?'), ('V', 'V', 'DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പാണെങ്കിൽ കമ്പനി തുടങ്ങി പത്ത് വർഷം വരെ നൽകാം.'), ('A', 'wide', 'അതുകൊണ്ട് ആദ്യം DPIIT സ്റ്റാറ്റസ് നോക്കുക.'), ('V', 'wide', 'നിയമം നോക്കി പ്ലാൻ.')],
 'നിയമം നോക്കി\nപ്ലാൻ', CTA_ESOP, theme='new',
 cap_ml='സാധാരണ പ്രൊമോട്ടർമാർക്കും 10%-ൽ കൂടുതൽ ഷെയറുള്ള ഡയറക്ടർമാർക്കും ESOP നൽകാൻ പറ്റില്ല. DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പിന് കമ്പനി തുടങ്ങി 10 വർഷം വരെ ഇളവുണ്ട്. നിങ്ങളുടെ കമ്പനിക്ക് DPIIT ഉണ്ടോ?',
 cap_en="A director with fifteen percent asks whether he can get ESOPs. Normally promoters and directors holding over 10% can't, but a DPIIT-recognised startup can grant them for up to 10 years from incorporation. Is your company DPIIT-recognised?",
 cap_mg='Saadhaarana promoters-inum 10%-il kooduthal share ulla directors-inum ESOP nalkaan pattilla. DPIIT angeekaaramulla startup-inu 10 varsham vare ilavundu. Ningalude company-kku DPIIT undo?')

