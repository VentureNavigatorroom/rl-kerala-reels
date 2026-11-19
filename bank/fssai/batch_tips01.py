# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

lst('fst002', 'packaged_food', "B", 'പാക്കറ്റിൽ\nനിർബന്ധം:\n14 അക്ക നമ്പർ', [('എവിടെ', 'പാക്കേജ് ചെയ്ത ഭക്ഷണത്തിന്റെ ലേബലിൽ.'), ('ആര് ചോദിക്കും', 'ഡെലിവറി ആപ്പുകളും കടകളും.'), ('ട്രിക്ക്', 'പ്രിന്റിന് മുമ്പ് നമ്പർ കിട്ടണം.')],
 'നമ്പർ ഇല്ലാത്ത പാക്കറ്റ്\nഷെൽഫിൽ കയറില്ല', CTA_FOOD, theme="tip",
 cap_ml='പാക്കേജ് ചെയ്ത ഭക്ഷണത്തിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ വേണം. ഡെലിവറി ആപ്പുകളും ഇത് ചോദിക്കും. നിങ്ങളുടെ ലേബലിൽ നമ്പർ ഉണ്ടോ?',
 cap_en='Packaged food must show the 14-digit FSSAI number on its label, and delivery apps ask for it too. Is yours on the label?',
 cap_mg='Packaged food label-il 14 digit FSSAI number venam. Delivery apps-um chodikkum. Ningalude label-il number undo?')

lst('fst003', 'cloud_kitchen', "B", 'FSSAI പുതുക്കൽ:\nകാലാവധി തീരും\nമുമ്പ്', [('കാലാവധി', 'ഒന്ന് മുതൽ അഞ്ച് വർഷം വരെ.'), ('എപ്പോൾ', 'കാലാവധി തീരുന്നതിന് മുമ്പ് പുതുക്കണം.'), ('ഇല്ലെങ്കിൽ', 'വിൽപ്പന നിയമവിരുദ്ധമാകും.')],
 'തീയതി ഇന്ന് തന്നെ\nനോക്കൂ', CTA_FSSAI, theme="tip",
 cap_ml='FSSAI രജിസ്ട്രേഷൻ 1 മുതൽ 5 വർഷം വരെ സാധുവാണ്. കാലാവധി തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടെ FSSAI എന്ന് തീരും?',
 cap_en='FSSAI registration is valid for 1 to 5 years; renew before it expires. When does yours expire?',
 cap_mg='FSSAI 1 muthal 5 varsham vare saadhu. Kaalaavadhi theerum mumpu puthukkanam. Ningalude FSSAI ennu theerum?')

