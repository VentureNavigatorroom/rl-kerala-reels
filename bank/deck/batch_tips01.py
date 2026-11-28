# deck tips 01 (28 Nov night), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PITCHDECK, CTA_DECK = topics.CTA_PITCHDECK, topics.CTA_DECK

duo('dkt001', 'grant_deck', 'B', 'metro', 'ഇൻവെസ്റ്റർ ഡെക്ക്:\n8 സ്ലൈഡ്\nക്രമം', [('A', 'wide', 'കിരണേ, ഇൻവെസ്റ്റർ ഡെക്കിന്റെ ക്രമം എന്താണ്?'), ('V', 'V', 'അഞ്ജലീ, പ്രശ്നം, പരിഹാരം, മാർക്കറ്റ്, ട്രാക്ഷൻ.'), ('A', 'A', 'പിന്നെ?'), ('V', 'V', 'ബിസിനസ് മോഡൽ, മത്സരം, ടീം, അവസാനം എത്ര വേണം, എന്തിന്.'), ('A', 'wide', 'മീറ്റിംഗിന് മുമ്പ് ഒരു വൺ പേജറും അയയ്ക്കാം.'), ('V', 'wide', 'എട്ട് സ്ലൈഡ്, ഒരു കഥ.')],
 'എട്ട് സ്ലൈഡ്,\nഒരു കഥ', CTA_PITCHDECK, theme='tip',
 cap_ml='ഇൻവെസ്റ്റർ പിച്ച് ഡെക്കിന്റെ 8 സ്ലൈഡ് ക്രമം: പ്രശ്നം, പരിഹാരം, മാർക്കറ്റ്, ട്രാക്ഷൻ, ബിസിനസ് മോഡൽ, മത്സരം, ടീം, ആവശ്യവും ഉപയോഗവും. നിങ്ങളുടെ ഡെക്ക് തയ്യാറാണോ?',
 cap_en='An investor pitch deck in eight slides: problem, solution, market, traction, business model, competition, team, and the ask with use of funds. Is yours ready?',
 cap_mg='Investor pitch deck-inte 8 slide kramam: problem, solution, market, traction, business model, competition, team, the ask. Ningalude deck ready aano?')

