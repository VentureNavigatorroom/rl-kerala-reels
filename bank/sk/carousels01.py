# Kerala Startup Mission seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
car("mk001", "idea_stage", "പടികൾ", "ഐഡിയയിൽ നിന്ന്\nKSUM ഗ്രാന്റിലേക്ക്\n4 പടി", [
 ("കമ്പനി", "കേരളത്തിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP."),
 ("DPIIT", "മിക്ക KSUM ഗ്രാന്റുകളും ചോദിക്കും."),
 ("യുണീക്ക് ഐഡി", "KSUM സ്കീമുകൾക്ക് ഇത് വേണം."),
 ("പിച്ച്", "പ്രോട്ടോടൈപ്പ്, പ്ലാൻ, പൈസ എങ്ങനെ ഉപയോഗിക്കും.")],
 "ഏത് പടിയിലാണ്?", topics.CTA_GRANT,
 cap_ml="ഐഡിയയിൽ നിന്ന് KSUM ഗ്രാന്റിലേക്ക്: കേരളത്തിൽ കമ്പനി അല്ലെങ്കിൽ LLP, DPIIT റെക്കഗ്നിഷൻ, KSUM യുണീക്ക് ഐഡി, നല്ല പിച്ച്.",
 cap_en="From idea to a Kerala Startup Mission grant in four steps: a Pvt Ltd or LLP in Kerala, DPIIT recognition, the KSUM Unique ID and a clear pitch with a plan for the money.",
 cap_mg="Idea-yil ninnu KSUM grant-ilekku: Kerala-yil company allenkil LLP, DPIIT, KSUM unique ID, nalla pitch.")
car("mk002", "returnee", "NRI", "ഗൾഫിൽ നിന്ന്\nതിരിച്ചെത്തി സ്റ്റാർട്ടപ്പ്\nതുടങ്ങുന്നവർക്ക്", [
 ("ആദ്യം", "കേരളത്തിൽ കമ്പനി. NRI-ക്കും ഡയറക്ടർ ആകാം."),
 ("പിന്നെ", "DPIIT സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷൻ."),
 ("KSUM", "യുണീക്ക് ഐഡി എടുത്ത് ഗ്രാന്റുകളും ഇൻക്യുബേഷനും നോക്കാം.")],
 "നാട്ടിൽ ശരിയായ\nതുടക്കം", topics.CTA_KSUM,
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തി സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്നവർക്ക്: കേരളത്തിൽ കമ്പനി, DPIIT റെക്കഗ്നിഷൻ, KSUM യുണീക്ക് ഐഡി.",
 cap_en="Back from the Gulf to start up in Kerala? Register the company in Kerala, get DPIIT recognition, then the KSUM Unique ID to access grants and incubation.",
 cap_mg="Gulf-il ninnu thirichethi startup thudangunnavarkku: Kerala-yil company, DPIIT, KSUM unique ID.")
