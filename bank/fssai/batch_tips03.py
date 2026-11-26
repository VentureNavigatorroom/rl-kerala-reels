# Tips and tricks 03 (26 Nov, refill after the 24 Nov correction): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_FSSAI (2026 limits). No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

lst('fst012', 'cloud_kitchen', "B", 'ലൈസൻസ് കിട്ടിയത്\n2026 ഏപ്രിലിന് മുമ്പോ?\nഈ ചെക്ക് ചെയ്യൂ', [('കിട്ടിയ തീയതി', 'സർട്ടിഫിക്കറ്റിൽ നോക്കൂ: 2026 ഏപ്രിൽ 1-ന് മുമ്പോ ശേഷമോ?'), ('മുമ്പാണെങ്കിൽ', 'FoSCoS-ൽ കാലാവധി തീയതി നോക്കി സമയത്ത് പുതുക്കൂ.'), ('ശേഷമാണെങ്കിൽ', 'പുതുക്കൽ വേണ്ട. വാർഷിക അടവ് മുടക്കരുത്.')],
 'ഊഹിക്കല്ലേ,\nതീയതി നോക്കൂ', CTA_FSSAI, theme="tip",
 cap_ml='FSSAI ലൈസൻസ് എപ്പോൾ കിട്ടി എന്ന് നോക്കൂ. 2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയതിന് സ്ഥിരം സാധുത. അതിന് മുമ്പുള്ളതാണെങ്കിൽ FoSCoS-ൽ കാലാവധി തീയതി നോക്കി സമയത്ത് പുതുക്കൂ. വാർഷിക അടവ് എല്ലാവർക്കും തുടരും. നിങ്ങളുടേത് ഏപ്രിലിന് മുമ്പോ ശേഷമോ?',
 cap_en='Check when your FSSAI licence was issued. Licences issued on or after 1 April 2026 have perpetual validity; for an older one, check the expiry date on FoSCoS and renew on time. The yearly payment to FSSAI continues for everyone. Was yours issued before or after April 2026?',
 cap_mg='FSSAI licence eppol kitti ennu nokku. 2026 April 1 muthal kittiyathinu perpetual validity. Athinu mumpullathaanel FoSCoS-il expiry date nokki samayathu renew cheyyu. Annual payment ellavarkkum thudarum. Ningaludethu April-nu mumpo shesham-o?')

lst('fst013', 'home_baker', "B", 'ഏത് FSSAI വേണം?\nടേൺഓവർ നോക്കി\nഒറ്റ നോട്ടത്തിൽ', [('1.5 കോടി വരെ', 'ബേസിക് രജിസ്ട്രേഷൻ. ഹോം ബേക്കർമാർക്കും ഇത് തന്നെ.'), ('1.5 മുതൽ 50 കോടി വരെ', 'സ്റ്റേറ്റ് ലൈസൻസ്.'), ('50 കോടിക്ക് മുകളിൽ', 'സെൻട്രൽ ലൈസൻസ്. ഇറക്കുമതി ചെയ്യുന്നവർക്ക് എപ്പോഴും സെൻട്രൽ.')],
 'ആദ്യം ടേൺഓവർ,\nപിന്നെ കാറ്റഗറി', CTA_FSSAI, theme="tip",
 cap_ml='2026 ഏപ്രിൽ മുതൽ: വർഷം 1.5 കോടി വരെ ടേൺഓവറിന് FSSAI രജിസ്ട്രേഷൻ, 1.5 മുതൽ 50 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്, 50 കോടിക്ക് മുകളിൽ സെൻട്രൽ. ഇറക്കുമതിക്ക് എപ്പോഴും സെൻട്രൽ. ചില ബിസിനസിന് ടേൺഓവർ നോക്കാതെ ലൈസൻസ് വേണം, FoSCoS-ൽ കാറ്റഗറി നോക്കൂ. നിങ്ങൾ ഏത് ലെവലിലാണ്?',
 cap_en='Since April 2026: FSSAI registration up to 1.5 crore turnover a year, a state licence from 1.5 to 50 crore, and a central licence above 50 crore. Importers always need central. Some kinds of business need a licence whatever the turnover, so check your category on FoSCoS. Which level are you?',
 cap_mg='2026 April muthal: varsham 1.5 crore vare turnover-inu FSSAI registration, 1.5 muthal 50 crore vare State licence, 50 crore-nu mukalil Central. Import-inu eppozhum Central. Chila business-inu turnover nokkaathe licence venam, FoSCoS-il category nokku. Ningal ethu level-il aanu?')

lst('fst014', 'cafe_owner', "B", 'സ്ഥിരം സാധുത\nകിട്ടിയാലും\nതുടരുന്ന 3 കാര്യം', [('വാർഷിക അടവ്', 'FSSAI-ക്കുള്ള അടവ് എല്ലാ വർഷവും. കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് അടയ്ക്കാം.'), ('വാർഷിക റിട്ടേൺ', 'സമയത്ത് ഫയൽ ചെയ്യണം.'), ('ലേബൽ', 'പാക്കറ്റിൽ 14 അക്ക FSSAI നമ്പർ.')],
 'സ്ഥിരം ലൈസൻസ്,\nസ്ഥിരം ഉത്തരവാദിത്തം', CTA_FOOD, theme="tip",
 cap_ml='2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ FSSAI രജിസ്ട്രേഷനും ലൈസൻസിനും പുതുക്കൽ വേണ്ട. പക്ഷേ FSSAI-ക്കുള്ള വാർഷിക അടവ്, വാർഷിക റിട്ടേൺ, പാക്കറ്റിലെ 14 അക്ക നമ്പർ എന്നിവ തുടരും. വാർഷിക അടവ് കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് അടയ്ക്കാം. ഇതിൽ ഏതാണ് നിങ്ങൾ മറന്നത്?',
 cap_en='FSSAI registrations and licences issued on or after 1 April 2026 need no renewal, but three things continue: the yearly payment to FSSAI (you can pay several years at once), annual returns, and the 14-digit number on every packet. Which one had you forgotten?',
 cap_mg='2026 April 1 muthal kittiya FSSAI registration-num licence-num renew venda. Pakshe FSSAI-kkulla annual payment, annual return, packet-ile 14 akka number ivayellaam thudarum. Annual payment kurachu varshathethu orumichu adakkaam. Ithil ethaanu ningal marannathu?')

lst('fst015', 'spice_exporter', "B", 'ടേൺഓവർ മാറിയാൽ\nFSSAI-യിൽ\nഎന്ത് ചെയ്യണം?', [('1.5 കോടി കടന്നാൽ', 'രജിസ്ട്രേഷൻ പോരാ, സ്റ്റേറ്റ് ലൈസൻസ് എടുക്കണം.'), ('50 കോടി കടന്നാൽ', 'സെൻട്രൽ ലൈസൻസിലേക്ക് മാറണം.'), ('താഴേക്ക് പോയാൽ', 'ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം. ആദ്യം FoSCoS-ൽ കാറ്റഗറി നോക്കൂ.')],
 'വർഷാവസാനം\nകണക്കും കാറ്റഗറിയും', CTA_FSSAI, theme="tip",
 cap_ml='വർഷ ടേൺഓവർ 1.5 കോടി കടന്നാൽ സ്റ്റേറ്റ് FSSAI ലൈസൻസ്, 50 കോടി കടന്നാൽ സെൻട്രൽ. ടേൺഓവർ കുറഞ്ഞ് താഴ്ന്ന കാറ്റഗറിയിൽ ആയാൽ ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം; ആദ്യം FoSCoS-ൽ കാറ്റഗറി നോക്കൂ. ഈ വർഷം നിങ്ങളുടെ ടേൺഓവർ കൂടിയോ കുറഞ്ഞോ?',
 cap_en='Turnover crossed 1.5 crore? You need a state FSSAI licence; above 50 crore, a central one. Turnover fell into a lower category? You can surrender the licence for a registration, after checking your category on FoSCoS. Did your turnover go up or down this year?',
 cap_mg='Varsha turnover 1.5 crore kadannaal State FSSAI licence, 50 crore kadannaal Central. Turnover kuranju thaazhnna category-il aayaal licence surrender cheythu registration edukkaam; aadyam FoSCoS-il category nokku. Ee varsham ningalude turnover koodiyo kuranjo?')

lst('fst016', 'packaged_food', "B", 'ഫുഡ് എക്സ്പോയിൽ\nസ്റ്റാൾ ബുക്ക് ചെയ്തോ?\n3 ചെക്ക്', [('രജിസ്ട്രേഷൻ', 'സ്റ്റാളിൽ ഫുഡ് വിൽക്കാനും FSSAI വേണം.'), ('പാക്കറ്റ്', 'പാക്ക് ചെയ്തതിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം.'), ('ഇല്ലെങ്കിൽ', 'അഞ്ച് ലക്ഷം വരെ പിഴ, ആറ് മാസം വരെ തടവ്.')],
 'സ്റ്റാൾ ഒരുക്കും മുമ്പ്\nനമ്പർ ഒരുക്കൂ', CTA_FOOD, theme="tip",
 cap_ml='ഫുഡ് എക്സ്പോയിലോ മേളയിലോ സ്റ്റാൾ ഇടുന്നുണ്ടോ? അവിടെ വിൽക്കാനും FSSAI വേണം, പാക്ക് ചെയ്തതിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും. അടുത്ത മേള എവിടെ?',
 cap_en='Booked a stall at a food expo or fair? Selling there still needs FSSAI, and packaged items must carry the 14-digit number. Selling without it can mean a penalty up to 5 lakh and up to 6 months in prison. Where is your next fair?',
 cap_mg='Food expo-yilo melayilo stall idunnundo? Avide vilkkaanum FSSAI venam, pack cheythathil 14 akka number print cheyyanam. Illaathe vittaal 5 lakh vare pizhayum 6 maasam vare thadavum. Adutha mela evide?')

lst('fst017', 'cloud_kitchen', "B", '2026-ലും വാട്സ്ആപ്പിൽ\nഓടുന്ന 3 FSSAI\nകേട്ടുകേൾവി', [('"പഴയ ലൈസൻസും സ്ഥിരമായി"', 'ഉറപ്പില്ല. FoSCoS-ൽ കാലാവധി തീയതി നോക്കൂ.'), ('"ചെറിയ കച്ചവടത്തിന് എപ്പോഴും രജിസ്ട്രേഷൻ"', 'ചില ബിസിനസിന് ലൈസൻസ് വേണം. കാറ്റഗറി നോക്കൂ.'), ('"ചെറിയ ഇറക്കുമതിക്ക് സ്റ്റേറ്റ് മതി"', 'ഇറക്കുമതിക്ക് എപ്പോഴും സെൻട്രൽ ലൈസൻസ്.')],
 'കേട്ടതല്ല,\nFoSCoS പറയുന്നത്', CTA_FSSAI, theme="tip",
 cap_ml='FSSAI-യെ കുറിച്ച് ഇപ്പോഴും കേൾക്കുന്ന 3 തെറ്റുകൾ: പഴയ ലൈസൻസും സ്ഥിരമായി (ഉറപ്പില്ല, FoSCoS-ൽ കാലാവധി നോക്കൂ), ചെറിയ കച്ചവടത്തിന് എപ്പോഴും രജിസ്ട്രേഷൻ (ചില ബിസിനസിന് ലൈസൻസ് വേണം), ചെറിയ ഇറക്കുമതിക്ക് സ്റ്റേറ്റ് മതി (എപ്പോഴും സെൻട്രൽ). ഇതിൽ ഏതാണ് നിങ്ങൾ കേട്ടത്?',
 cap_en='Three FSSAI myths still going round: "old licences became perpetual too" (not certain: check the expiry on FoSCoS), "a small business always needs only registration" (some kinds need a licence), and "a small importer can use a state licence" (importers always need central). Which one have you heard?',
 cap_mg='FSSAI-ye kurichu ippozhum kelkkunna 3 thettukal: pazhaya licence-um sthiramaayi (urappilla, FoSCoS-il expiry nokku), cheriya kachavadathinu eppozhum registration (chila business-inu licence venam), cheriya import-inu State mathi (eppozhum Central). Ithil ethaanu ningal kettathu?')
