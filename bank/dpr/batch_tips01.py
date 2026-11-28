# dpr tips 01 (28 Nov night), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTREPORT, CTA_DPR = topics.CTA_PROJECTREPORT, topics.CTA_DPR

duo('dpt001', 'working_capital', 'B', 'metro', 'ബാങ്ക്\nപ്രോജക്ട് റിപ്പോർട്ട്:\n5 ഭാഗങ്ങൾ', [('A', 'wide', 'കിരണേ, പ്രോജക്ട് റിപ്പോർട്ടിൽ എന്തൊക്കെ വേണം?'), ('V', 'V', 'അഞ്ജലീ, ഒന്ന്, നിങ്ങളെയും ബിസിനസിനെയും കുറിച്ച്. രണ്ട്, പ്രോജക്ട് ചെലവ്.'), ('A', 'A', 'ബാക്കി?'), ('V', 'V', 'മൂന്ന്, ഫണ്ടിംഗ്. നാല്, വിൽപ്പനയും ലാഭവും പ്രൊജക്ഷൻ. അഞ്ച്, തിരിച്ചടവ്.'), ('A', 'wide', 'വലിയ ലോണുകൾക്ക് ബാങ്ക് CMA ഡാറ്റയും ചോദിക്കാം.'), ('V', 'wide', 'അഞ്ചും ഒത്തുപോകണം.')],
 'അഞ്ചും\nഒത്തുപോകണം', CTA_PROJECTREPORT, theme='tip',
 cap_ml='ബാങ്ക് പ്രോജക്ട് റിപ്പോർട്ടിന്റെ 5 ഭാഗങ്ങൾ: നിങ്ങളും ബിസിനസും, പ്രോജക്ട് ചെലവ്, ഫണ്ടിംഗ്, പ്രൊജക്ഷൻ, തിരിച്ചടവ്. വർക്കിംഗ് ക്യാപിറ്റലിനോ വലിയ ലോണിനോ CMA ഡാറ്റയും ചോദിക്കാം. നിങ്ങളുടെ ലോൺ ഏതാണ്?',
 cap_en='A bank project report has five parts: you and the business, project cost, means of finance, projections and repayment. For working capital or larger loans, banks may also ask for CMA data. Which loan is yours?',
 cap_mg='Bank project report-inte 5 bhaagangal: ningalum business-um, project chelavu, funding, projection, thiricchadavu. Valiya loan-inu CMA data-um chodikkaam. Ningalude loan ethaanu?')

