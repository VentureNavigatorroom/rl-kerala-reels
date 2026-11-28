# esop tips 01 (28 Nov night), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ESOP, CTA_OPTIONS = topics.CTA_ESOP, topics.CTA_OPTIONS

duo('est001', 'first_hires', 'B', 'metro', 'ESOP പ്ലാൻ:\n5 ഘട്ടം', [('A', 'wide', 'കിരണേ, ESOP തുടങ്ങാൻ എന്തൊക്കെ ചെയ്യണം?'), ('V', 'V', 'അഞ്ജലീ, പ്രൈവറ്റ് ലിമിറ്റഡ്. ഷെയർഹോൾഡർമാരുടെ സ്പെഷ്യൽ റെസല്യൂഷൻ.'), ('A', 'A', 'പിന്നെ?'), ('V', 'V', 'പൂൾ എത്ര, ആർക്കൊക്കെ എന്ന് തീരുമാനിക്കുക. വെസ്റ്റിംഗ് കുറഞ്ഞത് ഒരു വർഷം.'), ('A', 'wide', 'ക്യാപ് ടേബിളിലും ഫയലിംഗിലും രേഖപ്പെടുത്തുക.'), ('V', 'wide', 'അഞ്ച് ഘട്ടം, ഒരു ടീം.')],
 'അഞ്ച് ഘട്ടം,\nഒരു ടീം', CTA_ESOP, theme='tip',
 cap_ml='ESOP പ്ലാൻ 5 ഘട്ടം: പ്രൈവറ്റ് ലിമിറ്റഡ്, സ്പെഷ്യൽ റെസല്യൂഷൻ, പൂളും ആർക്കൊക്കെ എന്നതും, കുറഞ്ഞത് ഒരു വർഷം വെസ്റ്റിംഗ്, ക്യാപ് ടേബിളിലും ഫയലിംഗിലും രേഖ. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='Setting up an ESOP plan in five steps: a private limited company, a special resolution, decide the pool and who gets it, at least one year to vesting, and record it in the cap table and filings. Which step are you on?',
 cap_mg='ESOP plan 5 ghattam: private limited, special resolution, pool-um aarkkokke ennathum, kuranjathu oru varsham vesting, cap table-ilum filing-ilum rekha. Ningal ethu ghattathilaanu?')

