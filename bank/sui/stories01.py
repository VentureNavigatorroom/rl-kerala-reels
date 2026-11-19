# Startup India seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
tip("ut001", "traditional_innovator", "സ്റ്റാർട്ടപ്പ് എന്നാൽ\nആപ്പ് മാത്രമല്ല", "പുതുമയുള്ള ഫുഡ്, കൃഷി, ആയുർവേദ ബിസിനസിനും DPIIT-ക്ക് അപേക്ഷിക്കാം.")
tip("ut002", "tech_founder", "DPIIT കിട്ടി.\nടാക്സ് പോയോ?", "ഇല്ല. 3 വർഷത്തെ ടാക്സ് ഹോളിഡേയ്ക്ക് വേറെ അപേക്ഷയും അംഗീകാരവും വേണം.")
quiz("uq001", "investor_ready", "പ്രൊപ്രൈറ്റർഷിപ്പിന്\nDPIIT കിട്ടുമോ?\n\nA) കിട്ടും\nB) കിട്ടില്ല", "B", "കമ്പനി, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് എന്നിവയ്ക്ക് മാത്രം.")
contact("ux001", "grant_seeker", "ഗ്രാന്റ് DPIIT\nചോദിച്ചോ?", "DPIIT")
contact("ux002", "tech_founder", "DPIIT കൊണ്ട് എന്ത്\nകിട്ടും എന്ന് അറിയണോ?", "BENEFITS")
