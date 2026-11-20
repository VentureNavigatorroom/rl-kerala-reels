# Tips and tricks 03 (20 Nov evening): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_IEC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

lst('iet011', 'spice_trade', "B", 'IEC-ന് കാലാവധി\nതീരുമോ?\nഒരു മിഥ്യ', [('കാലാവധി', 'ഇല്ല. IEC ഒരിക്കലും എക്സ്പയർ ആകില്ല.'), ('പക്ഷേ', 'എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈൻ അപ്ഡേറ്റ്.'), ('ട്രിക്ക്', 'ഈ വർഷത്തെ അപ്ഡേറ്റ് ചെയ്തോ എന്ന് DGFT-യിൽ ഇന്ന് തന്നെ നോക്കൂ.')],
 'പുതുക്കേണ്ട,\nപക്ഷേ മറക്കരുത്', CTA_IEC, theme="tip",
 cap_ml='IEC-ന് കാലാവധി ഇല്ല, പുതുക്കേണ്ടതുമില്ല. പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനായി അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. ഈ വർഷത്തെ അപ്ഡേറ്റ് ചെയ്തോ?',
 cap_en='An IEC never expires and needs no renewal, but it must be updated online every year between April and June, or it is deactivated. Did you do this year\'s update?',
 cap_mg='IEC-nu kaalaavadhi illa, puthukkendathumilla. Pakshe ella varshavum April muthal June vare online update cheythillenkil deactivate aakum. Ee varshathe update cheytho?')
