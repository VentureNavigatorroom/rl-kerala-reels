# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

lst('ut001', 'tech_founder', "B", 'DPIIT യോഗ്യത:\n4 ചെക്ക്\n30 സെക്കൻഡിൽ', [('ഘടന', 'പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റർ ചെയ്ത പങ്കാളിത്തം.'), ('പ്രായം', 'പത്ത് വർഷത്തിൽ താഴെ.'), ('പുതുമ', 'ഇന്നൊവേഷൻ അല്ലെങ്കിൽ സ്കെയിലബിൾ മാതൃക.')],
 'മൂന്നും ഉണ്ടെങ്കിൽ\nഅപേക്ഷിക്കാം', CTA_DPIIT, theme="tip",
 cap_ml='DPIIT അംഗീകാരത്തിന്: ശരിയായ ഘടന, പത്ത് വർഷത്തിൽ താഴെ പ്രായം, ഇന്നൊവേഷൻ അല്ലെങ്കിൽ സ്കെയിലബിൾ മാതൃക, ടേൺഓവർ പരിധിക്ക് താഴെ. അംഗീകാരം ഉറപ്പല്ല. നിങ്ങൾ എത്രയെണ്ണം ടിക്ക് ചെയ്യുന്നു?',
 cap_en='DPIIT checks: the right structure, under 10 years old, innovation or a scalable model, and turnover within the limit. Recognition is never guaranteed. How many can you tick?',
 cap_mg='DPIIT-nu: shariyaaya structure, 10 varshathil thaazhe, innovation allenkil scalable model, turnover paridhikku thaazhe. Ningal ethra tick cheyyum?')

lst('ut002', 'grant_seeker', "B", 'DPIIT കിട്ടിയാൽ\nആദ്യം ഉപയോഗിക്കേണ്ട\n3 ഗുണം', [('പേറ്റന്റ്', 'ഫയലിംഗിൽ എൺപത് ശതമാനം ഇളവ്.'), ('ട്രേഡ്മാർക്ക്', 'അമ്പത് ശതമാനം ഇളവ്.'), ('സ്കീമുകൾ', 'പല സർക്കാർ സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും യോഗ്യത.')],
 'അംഗീകാരം കിട്ടി,\nഇനി ഉപയോഗിക്കൂ', CTA_BENEFITS, theme="tip",
 cap_ml='DPIIT അംഗീകാരമുണ്ടെങ്കിൽ പേറ്റന്റ് ഫയലിംഗിൽ 80 ശതമാനവും ട്രേഡ്മാർക്കിൽ 50 ശതമാനവും ഇളവ്, പല സ്കീമുകൾക്കും യോഗ്യത. ഇതിൽ ഏതാണ് നിങ്ങൾ ഉപയോഗിച്ചത്?',
 cap_en='With DPIIT recognition: 80 percent off patent filing, 50 percent off trademark filing, and eligibility for many schemes and tenders. Which have you used?',
 cap_mg='DPIIT undel patent filing-il 80 percent, trademark-il 50 percent ilavu, pala scheme-kalkkum yogyatha. Ethaanu ningal upayogichathu?')

lst('ut003', 'investor_ready', "B", 'ടാക്സ് ഹോളിഡേ:\nDPIIT-നൊപ്പം\nസ്വയം വരില്ല', [('80-IAC', 'മൂന്ന് വർഷം ലാഭത്തിന് ഒഴിവ്.'), ('എപ്പോൾ', 'ആദ്യ പത്ത് വർഷത്തിൽ ഏതെങ്കിലും മൂന്ന്.'), ('ട്രിക്ക്', 'പ്രത്യേക അപേക്ഷ, ബോർഡ് അംഗീകരിക്കണം.')],
 'അംഗീകാരം ഒന്ന്,\nടാക്സ് ഒഴിവ് മറ്റൊന്ന്', CTA_BENEFITS, theme="tip",
 cap_ml='80-IAC ടാക്സ് ഒഴിവ് DPIIT-നൊപ്പം സ്വയം കിട്ടില്ല. ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കുന്ന പ്രത്യേക അപേക്ഷയാണ്. നിങ്ങൾ അപേക്ഷിച്ചോ?',
 cap_en='The 80-IAC tax holiday does not come automatically with DPIIT. It is a separate application approved by an inter-ministerial board. Have you applied?',
 cap_mg='80-IAC tax ilavu DPIIT-nodoppam swayam kittilla. Board angeekarikkunna separate apekshayaanu. Ningal apply cheytho?')

