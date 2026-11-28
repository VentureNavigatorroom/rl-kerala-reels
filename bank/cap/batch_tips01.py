# cap tips 01 (28 Nov night), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_CAPTABLE, CTA_SHARES = topics.CTA_CAPTABLE, topics.CTA_SHARES

duo('ctt001', 'pre_round', 'B', 'metro', 'റൗണ്ടിന് മുമ്പ്\nക്യാപ് ടേബിൾ:\n5 ചെക്ക്', [('A', 'wide', 'കിരണേ, ഇൻവെസ്റ്റർ റൗണ്ടിന് മുമ്പ് ഷെയർ രേഖകളിൽ എന്ത് നോക്കണം?'), ('V', 'V', 'അഞ്ജലീ, ക്യാപ് ടേബിളും രജിസ്റ്റർ ഓഫ് മെമ്പേഴ്സും ഒത്തുപോകുന്നുണ്ടോ.'), ('A', 'A', 'പിന്നെ?'), ('V', 'V', 'ഓരോ ഇഷ്യൂവിനും PAS-3, ബാധകമെങ്കിൽ ഡീമാറ്റ്, വാഗ്ദാനം ചെയ്ത ഷെയർ രേഖയിൽ.'), ('A', 'wide', 'പുതിയ റൗണ്ടിൽ ഓരോരുത്തരുടെ ശതമാനം എത്ര കുറയും എന്നും കണക്കാക്കുക.'), ('V', 'wide', 'അഞ്ച് ചെക്ക്, ഒരു വൃത്തിയുള്ള റൗണ്ട്.')],
 'അഞ്ച് ചെക്ക്,\nഒരു വൃത്തിയുള്ള റൗണ്ട്', CTA_CAPTABLE, theme='tip',
 cap_ml='ഇൻവെസ്റ്റർ റൗണ്ടിന് മുമ്പ് 5 ചെക്ക്: ക്യാപ് ടേബിൾ രജിസ്റ്ററുമായി ഒത്തുപോകുന്നു, ഓരോ ഇഷ്യൂവിനും PAS-3, ബാധകമെങ്കിൽ ഡീമാറ്റ്, വാഗ്ദാനം ചെയ്ത ഷെയർ രേഖയിൽ, ഡൈല്യൂഷൻ കണക്ക്. നിങ്ങൾ എത്ര എണ്ണം ചെയ്തു?',
 cap_en='Five checks before a round: cap table matches the register, PAS-3 filed for every issue, demat where it applies, promised shares in writing, and dilution worked out. How many have you done?',
 cap_mg='Investor round-inu mumpu 5 check: cap table register-umaayi otthupokunnu, oro issue-inum PAS-3, baadhakamenkil demat, promise cheytha share rekhayil, dilution kanakku. Ningal ethra ennam cheythu?')

