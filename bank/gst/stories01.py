# GST seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
tip("gt001", "trader", "ലിമിറ്റിൽ താഴെ,\nഎന്നിട്ടും GST?", "വലിയ ബയർമാർ GST ബില്ല് ചോദിക്കും. ലിമിറ്റിൽ താഴെയും സ്വമേധയാ രജിസ്റ്റർ ചെയ്യാം.")
tip("gt002", "online_seller", "പുറത്തേക്ക്\nഓൺലൈൻ ഓർഡർ?", "സാധനം മറ്റ് സംസ്ഥാനത്തേക്ക് വിൽക്കാൻ ടേൺഓവർ നോക്കാതെ GST വേണം.")
quiz("gq001", "service_pro", "സർവീസ് ബിസിനസിന്\nGST ലിമിറ്റ്?\n\nA) 20 ലക്ഷം\nB) 40 ലക്ഷം", "A", "സർവീസിന് 20 ലക്ഷം. സാധനങ്ങൾക്ക് കേരളത്തിൽ 40 ലക്ഷം.")
contact("gx001", "trader", "ടേൺഓവർ ലിമിറ്റ്\nഅടുത്തെത്തിയോ?", "LIMIT")
contact("gx002", "nri_business", "ഗൾഫിലിരുന്ന് നാട്ടിലെ\nകടയ്ക്ക് GST?", "GST")
