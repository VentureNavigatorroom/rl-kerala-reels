# Kerala Startup Mission seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
tip("mt001", "kerala_registered", "കമ്പനി ഉണ്ട്,\nKSUM ഐഡി ഇല്ലേ?", "ഗ്രാന്റ് കോൾ വരുമ്പോൾ ഓടേണ്ട. യുണീക്ക് ഐഡി ഇപ്പോഴേ എടുക്കൂ.")
tip("mt002", "idea_stage", "ഐഡിയ ഗ്രാന്റ്", "കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം. പക്ഷേ പൈസ കിട്ടും മുമ്പ് കമ്പനിയും ഐഡിയും വേണം.")
quiz("mq001", "campus", "മിക്ക KSUM ഗ്രാന്റിനും\nവേണ്ടത്?\n\nA) DPIIT + യുണീക്ക് ഐഡി\nB) ജിഎസ്ടി മാത്രം", "A", "DPIIT റെക്കഗ്നിഷനും KSUM യുണീക്ക് ഐഡിയും.")
contact("mx001", "returnee", "നാട്ടിൽ സ്റ്റാർട്ടപ്പ്\nതുടങ്ങാൻ വരുന്നോ?", "KSUM")
contact("mx002", "idea_stage", "ഗ്രാന്റിന്\nഅപേക്ഷിക്കാൻ\nതയ്യാറാണോ?", "GRANT")
