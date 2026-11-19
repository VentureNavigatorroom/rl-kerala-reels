# Udyam stories seed (19 Nov). Facts only from topics.FACTS_UD; no fees; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
tip("yt001", "supplier_unpaid", "ബയർ 90 ദിവസം\nഎടുക്കുന്നോ?", "ഉദ്യം ഉള്ള മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്ക് 45 ദിവസത്തിനുള്ളിൽ പണം കിട്ടണം.")
tip("yt002", "trader_ud", "കടയ്ക്ക്\nഉദ്യം?", "എടുക്കാം. പക്ഷേ ലോൺ മുൻഗണനയ്ക്ക് മാത്രം, 45 ദിവസ സംരക്ഷണം ഇല്ല.")
quiz("yq001", "manufacturer", "ടേൺഓവർ 8 കോടി,\nനിക്ഷേപം 3 കോടി.\n\nA) മൈക്രോ\nB) സ്മോൾ", "B", "മൈക്രോയ്ക്ക് നിക്ഷേപം 2.5 കോടിയിൽ താഴെ വേണം.")
contact("yx001", "supplier_unpaid", "പണം വൈകിക്കുന്ന\nബയർ ഉണ്ടോ?", "UDYAM")
contact("yx002", "loan_seeker", "ബിസിനസ് ലോൺ\nനോക്കുന്നോ?", "UDYAM")
