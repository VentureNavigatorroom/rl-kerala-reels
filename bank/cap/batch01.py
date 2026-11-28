# cap batch 01 (28 Nov night): seed 3D reels. Facts only from topics.FACTS_CAP. No prices, no promised results.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_CAPTABLE, CTA_SHARES = topics.CTA_CAPTABLE, topics.CTA_SHARES

duo('ctd001', 'messy_shares', 'A', 'office', 'ക്യാപ് ടേബിളിൽ\n60%. രേഖയിൽ\n50%', [('A', 'wide', 'രാഹുലേ, ഇൻവെസ്റ്റർ ഡ്യൂ ഡിലിജൻസ് ചെയ്തപ്പോൾ ക്യാപ് ടേബിളും ഷെയർ രജിസ്റ്ററും പൊരുത്തപ്പെട്ടില്ല.'), ('V', 'V', 'നേഹ, ഷെയർ കൊടുത്തപ്പോൾ ROC-യിൽ ഫയൽ ചെയ്തിരുന്നോ?'), ('A', 'A', 'ഒരു തവണ മറന്നുപോയി.'), ('V', 'V', 'അതാണ് പ്രശ്നം. ഓരോ ഷെയർ ഇഷ്യൂവിനും PAS-3 ഫയൽ ചെയ്യണം. രജിസ്റ്റർ പുതുക്കണം.'), ('A', 'wide', 'ഇൻവെസ്റ്റർ വരും മുമ്പ് ഇത് ശരിയാക്കണം.'), ('V', 'wide', 'രേഖ ഒത്താൽ ചർച്ച ഒഴുകും.')],
 'രേഖ ഒത്താൽ\nചർച്ച ഒഴുകും', CTA_CAPTABLE, theme='crm',
 cap_ml='ക്യാപ് ടേബിൾ രജിസ്റ്റർ ഓഫ് മെമ്പേഴ്സുമായും ROC ഫയലിംഗുകളുമായും ഒത്തുപോകണം. ഓരോ ഷെയർ ഇഷ്യൂവിനും PAS-3. ഇൻവെസ്റ്റർ വരും മുമ്പ് പരിശോധിക്കൂ. നിങ്ങളുടെ രേഖകൾ ഒത്തുപോകുന്നുണ്ടോ?',
 cap_en="During due diligence his cap table didn't match the share register because one allotment was never filed. Every share issue needs its return of allotment (PAS-3) and an updated register. Do your records match?",
 cap_mg='Cap table register of members-umaayum ROC filings-umaayum otthupokanam. Oro share issue-inum PAS-3. Investor varum mumpu parishodhikku. Ningalude records otthupokunnundo?')

duo('ctd002', 'founder_split', 'B', 'home', 'വാക്കുകൊണ്ട്\n5% ഷെയർ\nകൊടുത്തു', [('A', 'wide', 'അരുണേ, സഹായിച്ച ഒരു സുഹൃത്തിന് അഞ്ച് ശതമാനം ഷെയർ തരാമെന്ന് വാക്ക് പറഞ്ഞിരുന്നു.'), ('V', 'V', 'സ്നേഹേ, എഴുതി വെച്ചോ? ബോർഡും ഷെയർഹോൾഡർമാരും അംഗീകരിച്ചോ?'), ('A', 'A', 'ഇല്ല, വാക്ക് മാത്രം.'), ('V', 'V', 'ഇൻവെസ്റ്റർ വരുമ്പോൾ ഇത് വലിയ ചോദ്യമാകും. ആദ്യം എഴുതി ശരിയായി അംഗീകരിക്കുക.'), ('A', 'wide', 'പിന്നെ ക്യാപ് ടേബിളിൽ കാണിക്കുക.'), ('V', 'wide', 'വാക്ക് അല്ല, രേഖ.')],
 'വാക്ക് അല്ല,\nരേഖ', CTA_SHARES, theme='faq',
 cap_ml='ആർക്കെങ്കിലും ഷെയർ വാഗ്ദാനം ചെയ്തിട്ടുണ്ടെങ്കിൽ എഴുതി, ശരിയായി അംഗീകരിച്ച്, ക്യാപ് ടേബിളിൽ കാണിക്കണം. ഇൻവെസ്റ്റർ വരുമ്പോൾ വാക്കാലുള്ള വാഗ്ദാനം പ്രശ്നമാകും. നിങ്ങൾ ആർക്കെങ്കിലും വാക്ക് കൊടുത്തിട്ടുണ്ടോ?',
 cap_en='She promised a friend five percent by word of mouth. Any promised shares should be written down, approved properly and shown in the cap table before investors arrive. Have you promised shares to anyone?',
 cap_mg='Aarkkenkilum share vaagdaanam cheythittundenkil ezhuthi, shariyaayi angeekarichu, cap table-il kaanikkanam. Ningal aarkkenkilum vaakku koduthittundo?')

duo('ctd003', 'demat_due', 'A', 'library', 'ഷെയർ സർട്ടിഫിക്കറ്റ്\nപേപ്പറിൽ. പുതിയ\nറൗണ്ട് നടക്കുമോ?', [('A', 'wide', 'അനൂപേ, ഞങ്ങളുടെ ഷെയറുകൾ ഇപ്പോഴും പേപ്പർ സർട്ടിഫിക്കറ്റിലാണ്. പുതിയ റൗണ്ട് എടുക്കാമോ?'), ('V', 'V', 'ഗ്രീഷ്മേ, ചെറുകിട കമ്പനി അല്ലെങ്കിൽ പ്രൈവറ്റ് കമ്പനികൾ ഷെയർ ഇഷ്യൂവും കൈമാറ്റവും ഡീമാറ്റിൽ ചെയ്യണം.'), ('A', 'A', 'ചെറുകിട കമ്പനിയാണെങ്കിൽ?'), ('V', 'V', 'ചെറുകിട കമ്പനികൾക്ക് ഇളവുണ്ട്. പക്ഷേ ആദ്യം നിങ്ങൾ ഏതിൽ പെടും എന്ന് ഉറപ്പാക്കണം.'), ('A', 'wide', 'പുതിയ ഇഷ്യൂവിന് മുമ്പ് പ്രൊമോട്ടർമാരുടെയും ഡയറക്ടർമാരുടെയും ഷെയർ ഡീമാറ്റ് ചെയ്യണം.'), ('V', 'wide', 'ആദ്യം ഡീമാറ്റ്, പിന്നെ റൗണ്ട്.')],
 'ആദ്യം ഡീമാറ്റ്,\nപിന്നെ റൗണ്ട്', CTA_SHARES, theme='new',
 cap_ml='MCA നിയമപ്രകാരം ചെറുകിട കമ്പനി അല്ലാത്ത പ്രൈവറ്റ് കമ്പനികൾ ഷെയർ ഇഷ്യൂവും കൈമാറ്റവും ഡീമാറ്റിൽ ചെയ്യണം. പുതിയ ഇഷ്യൂവിന് മുമ്പ് പ്രൊമോട്ടർമാരുടെയും ഡയറക്ടർമാരുടെയും ഷെയർ ഡീമാറ്റ് ചെയ്യണം. നിങ്ങളുടെ ഷെയർ പേപ്പറിലാണോ?',
 cap_en="Their shares are still on paper certificates. Under MCA rules, private companies other than small companies must issue and transfer shares only in demat form, and demat promoters' and directors' shares before a new issue. Are yours on paper?",
 cap_mg='MCA niyamaprakaaram small company allaatha private company-kal share issue-um transfer-um demat-il cheyyanam. Puthiya issue-inu mumpu promoters-inteyum directors-inteyum share demat cheyyanam. Ningalude share paper-ilaano?')

