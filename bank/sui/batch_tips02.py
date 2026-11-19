# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_SUI. Never promise approval or a benefit.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

lst('ut004', 'investor_ready', "B", 'ടേൺഓവർ പരിധി\nമാറി: 100 അല്ല,\nഇപ്പോൾ 200 കോടി', [('സാധാരണ സ്റ്റാർട്ടപ്പ്', 'ഒരു വർഷവും ഇരുനൂറ് കോടി കടക്കരുത്.'), ('ഡീപ് ടെക്', 'മുന്നൂറ് കോടി വരെ.'), ('ഓർക്കൂ', 'ഏതെങ്കിലും ഒരു വർഷം കടന്നാൽ മതി, യോഗ്യത പോകും.')],
 'വളരും മുമ്പ്\nപരിധി അറിയൂ', CTA_DPIIT, theme="tip",
 cap_ml='2026 ഫെബ്രുവരി 4-ലെ വിജ്ഞാപനം മുതൽ DPIIT ടേൺഓവർ പരിധി 200 കോടി (ഡീപ് ടെക്കിന് 300 കോടി); മുമ്പ് 100 കോടി ആയിരുന്നു. ഒരു വർഷവും ഇത് കടക്കരുത്. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ് ഡീപ് ടെക് ആണോ?',
 cap_en='Since the 4 Feb 2026 notification, the DPIIT turnover limit is 200 crore in any year (300 crore for Deep Tech); it used to be 100 crore. Is your startup Deep Tech?',
 cap_mg='2026 Feb 4 notification muthal DPIIT turnover paridhi 200 kodi (Deep Tech-nu 300 kodi); mumpu 100 kodi aayirunnu. Oru varshavum ithu kadakkaruthu. Ningalude startup Deep Tech aano?')

lst('ut005', 'traditional_innovator', "B", 'DPIIT-ന്റെ 10 വർഷം:\nഎണ്ണുന്നത്\nഏത് ദിവസം മുതൽ?', [('തുടക്കം', 'ഇൻകോർപ്പറേഷൻ അല്ലെങ്കിൽ രജിസ്ട്രേഷൻ തീയതി.'), ('സാധാരണ', 'പത്ത് വർഷം; ഡീപ് ടെക്കിന് ഇരുപത്.'), ('ട്രിക്ക്', 'അവസാന തീയതി ഇന്ന് തന്നെ കലണ്ടറിൽ ഇടൂ.')],
 'ആശയം പഴയതാകില്ല,\nതീയതി പഴയതാകും', CTA_DPIIT, theme="tip",
 cap_ml='DPIIT അംഗീകാരത്തിനുള്ള പത്ത് വർഷം (ഡീപ് ടെക്കിന് ഇരുപത്) കണക്കാക്കുന്നത് കമ്പനി അല്ലെങ്കിൽ LLP രജിസ്റ്റർ ചെയ്ത തീയതി മുതലാണ്. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര വയസ്സായി?',
 cap_en='The 10-year window for DPIIT recognition (20 for Deep Tech) counts from the date of incorporation or registration. How old is your company?',
 cap_mg='DPIIT-nu 10 varsham (Deep Tech-nu 20) kanakkaakkunnathu company allenkil LLP register cheytha theeyathi muthalaanu. Ningalude company-kku ethra vayassaayi?')

lst('ut006', 'traditional_innovator', "B", 'DPIIT-ന്റെ\nഅധികം പേർ അറിയാത്ത\n3 ഗുണം', [('IP പരിശോധന', 'പേറ്റന്റിനും ട്രേഡ്മാർക്കിനും വേഗത്തിലുള്ള പരിശോധന.'), ('തൊഴിൽ നിയമങ്ങൾ', 'ചിലതിൽ സ്വയം സാക്ഷ്യപ്പെടുത്താം.'), ('പരിസ്ഥിതി നിയമങ്ങൾ', 'ചിലതിൽ സ്വയം സാക്ഷ്യപ്പെടുത്താം.')],
 'അംഗീകാരം കിട്ടിയാൽ\nഇതും ഉപയോഗിക്കൂ', CTA_BENEFITS, theme="tip",
 cap_ml='DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പുകൾക്ക് IP അപേക്ഷകളിൽ വേഗത്തിലുള്ള പരിശോധനയും ചില തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ സ്വയം സാക്ഷ്യപ്പെടുത്തലും ലഭ്യമാണ്. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് പുതിയത്?',
 cap_en='DPIIT-recognised startups can get faster examination of IP applications and self-certification under some labour and environment laws. Which of these was new to you?',
 cap_mg='DPIIT recognition ulla startup-kalkku IP application-il vegathilulla parishodhanayum chila thozhil, paristhithi niyamangalil self-certification-um labhyamaanu. Ethaanu ningalkku puthiyathu?')

lst('ut007', 'grant_seeker', "B", 'DPIIT കിട്ടി =\nപണം കിട്ടി?\nഅല്ല, ഇതാണ് സത്യം', [('എന്താണ്', 'സർക്കാർ നൽകുന്ന സ്റ്റാർട്ടപ്പ് അംഗീകാരം.'), ('തുറക്കുന്നത്', 'പല സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും അപേക്ഷിക്കാനുള്ള യോഗ്യത.'), ('അല്ലാത്തത്', 'ഗ്രാന്റിന്റെയോ തിരഞ്ഞെടുപ്പിന്റെയോ ഉറപ്പ്.')],
 'യോഗ്യത ഒരു താക്കോൽ,\nവാതിൽ വേറെ', CTA_DPIIT, theme="tip",
 cap_ml='DPIIT അംഗീകാരം പണമല്ല: പല സർക്കാർ സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും അപേക്ഷിക്കാനുള്ള യോഗ്യതയാണ്. ഓരോ സ്കീമിനും സ്വന്തം നിബന്ധനയും തിരഞ്ഞെടുപ്പും ഉണ്ട്. നിങ്ങൾ ഇതുവരെ എത്ര സ്കീമിന് അപേക്ഷിച്ചു?',
 cap_en='DPIIT recognition is not money: it makes you eligible to apply for many government schemes and tenders, each with its own conditions and selection. How many schemes have you applied for so far?',
 cap_mg='DPIIT recognition panamalla: pala sarkkaar scheme-kalkkum tender-ukalkkum apekshikkaanulla yogyathayaanu. Oro scheme-num swantham nibandhanayum selection-um undu. Ningal ithuvare ethra scheme-nu apekshichu?')

lst('ut008', 'traditional_innovator', "B", 'പാർട്ണർഷിപ്പ്\nഫേമിന് DPIIT?\nഒരു വാക്ക് നോക്കൂ', [('രജിസ്റ്റർ ചെയ്ത ഫേം', 'അപേക്ഷിക്കാം.'), ('രജിസ്റ്റർ ചെയ്യാത്ത ഫേം', 'ആദ്യം രജിസ്ട്രേഷൻ വേണം.'), ('കോഓപ്പറേറ്റീവ് സൊസൈറ്റി', 'അതും യോഗ്യമായ ഘടനയാണ്.')],
 'ആ ഒറ്റ വാക്ക്:\n"രജിസ്റ്റർ ചെയ്ത"', CTA_DPIIT, theme="tip",
 cap_ml='DPIIT അംഗീകാരത്തിന് പാർട്ണർഷിപ്പ് ഫേം രജിസ്റ്റർ ചെയ്തതായിരിക്കണം. പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, കോഓപ്പറേറ്റീവ് സൊസൈറ്റി എന്നിവയും യോഗ്യമാണ്. നിങ്ങളുടെ ഫേം രജിസ്റ്റർ ചെയ്തതാണോ?',
 cap_en='For DPIIT recognition a partnership firm must be registered. Private limited companies, LLPs and cooperative societies are eligible structures too. Is your firm registered?',
 cap_mg='DPIIT recognition-nu partnership firm register cheythathaayirikkanam. Pvt Ltd, LLP, cooperative society ennivayum yogyamaanu. Ningalude firm register cheythathaano?')

lst('ut009', 'student_founder', "B", 'പ്രോട്ടോടൈപ്പ് ഉണ്ട്,\nകമ്പനി ഇല്ല:\nDPIIT-ലേക്ക് 3 പടി', [('ഒന്ന്', 'പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP രജിസ്റ്റർ ചെയ്യൂ.'), ('രണ്ട്', 'ഇന്നൊവേഷൻ എന്തെന്ന് ലളിതമായി എഴുതി വെക്കൂ.'), ('മൂന്ന്', 'സ്റ്റാർട്ടപ്പ് ഇന്ത്യയിൽ അപേക്ഷിക്കൂ.')],
 'ക്ലാസ് പ്രൊജക്റ്റിൽ\nനിന്ന് സ്റ്റാർട്ടപ്പിലേക്ക്', CTA_DPIIT, theme="tip",
 cap_ml='പ്രോട്ടോടൈപ്പ് മാത്രമുള്ള വിദ്യാർത്ഥി ഫൗണ്ടർമാർക്ക്: ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP, പിന്നെ ഇന്നൊവേഷൻ വ്യക്തമായി എഴുതി DPIIT അപേക്ഷ. അംഗീകാരം ഉറപ്പല്ല. നിങ്ങൾ ഏത് പടിയിലാണ്?',
 cap_en='Student founders with just a prototype: register a private limited company or LLP first, write down the innovation clearly, then apply for DPIIT recognition. Approval is never guaranteed. Which step are you on?',
 cap_mg='Prototype maathram ulla student founders-nu: aadyam Pvt Ltd allenkil LLP, pinne innovation vyakthamaayi ezhuthi DPIIT apeksha. Recognition urappalla. Ningal ethu padiyilaanu?')

lst('ut010', 'tech_founder', "B", 'പേറ്റന്റ് ഫയൽ\nചെയ്യാൻ പോകുന്നോ?\nആദ്യം ഇത് നോക്കൂ', [('ആദ്യം', 'DPIIT അംഗീകാരത്തിന് അപേക്ഷിക്കൂ.'), ('പിന്നെ', 'അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പിന്റെ ഇളവോടെ ഫയൽ ചെയ്യൂ.'), ('ഓർക്കൂ', 'ട്രേഡ്മാർക്ക് ഫയലിംഗിനും ഇതേ ക്രമം.')],
 'ക്രമം മാറിയാൽ\nഇളവ് പോകും', CTA_BENEFITS, theme="tip",
 cap_ml='DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പുകൾക്ക് പേറ്റന്റ് ഫയലിംഗിൽ 80% ഇളവും ട്രേഡ്മാർക്കിൽ 50% ഇളവും ഉണ്ട്. അതുകൊണ്ട് ഫയൽ ചെയ്യും മുമ്പ് അംഗീകാരം നോക്കൂ. നിങ്ങൾ ആദ്യം ഫയൽ ചെയ്യുന്നത് പേറ്റന്റോ ട്രേഡ്മാർക്കോ?',
 cap_en='DPIIT-recognised startups get an 80% rebate on patent filing and 50% on trademark filing, so look at recognition before you file. Patent or trademark first?',
 cap_mg='DPIIT recognition ulla startup-kalkku patent filing-il 80% ilavum trademark-il 50% ilavum undu. Athukondu file cheyyum mumpu recognition nokku. Ningal aadyam file cheyyunnathu patent-o trademark-o?')
