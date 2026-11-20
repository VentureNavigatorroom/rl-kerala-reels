# Tips and tricks 03 (20 Nov, writer run 17: keep 10 unposted). theme="tip". Facts only from topics.FACTS_UD.
# Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

lst('yt011', 'manufacturer', "B", 'മീഡിയം ആയി\nവളർന്നു. 45 ദിവസ\nസംരക്ഷണം ബാക്കിയോ?', [('മൈക്രോ, സ്മോൾ', 'മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്ക് 45 ദിവസ പേയ്മെന്റ് സംരക്ഷണം.'), ('മീഡിയം', 'MSME തന്നെ, പക്ഷേ ഈ പേയ്മെന്റ് സംരക്ഷണം ഇല്ല.'), ('ട്രിക്ക്', 'വിഭാഗം മാറിയാൽ ഉദ്യം പുതുക്കി, ബയർ കരാറിലെ പേയ്മെന്റ് സമയം വീണ്ടും നോക്കൂ.')],
 'വളർച്ച നല്ലത്,\nകരാർ പുതുക്കണം', CTA_MSME, theme="tip",
 cap_ml='നിക്ഷേപം 25 കോടിയോ ടേൺഓവർ 100 കോടിയോ കടന്നാൽ യൂണിറ്റ് മീഡിയം ആകും. അപ്പോഴും MSME തന്നെ, പക്ഷേ 45 ദിവസ പേയ്മെന്റ് സംരക്ഷണം മൈക്രോയ്ക്കും സ്മോളിനും മാത്രം. നിങ്ങളുടെ യൂണിറ്റ് ഏത് വിഭാഗം?',
 cap_en='Cross 25 crore of investment or 100 crore of turnover and your unit becomes medium. It is still MSME, but the 45-day payment protection covers only micro and small units, so update Udyam and recheck payment terms with buyers. Which category is your unit?',
 cap_mg='Investment 25 crore-o turnover 100 crore-o kadannaal unit medium aakum. Appozhum MSME thanne, pakshe 45 divasa payment protection micro-kkum small-inum maathram. Ningalude unit ethu category?')
