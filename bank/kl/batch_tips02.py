# kl tips 02 (27 Nov night): Shops Act renewal check as a duo3d scene, from the verified LCAS line in topics.FACTS_KL. theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

duo("lct003", "town_business", "B", "photocopy", "ഷോപ്സ് ആക്ട്\nപുതുക്കൽ:\n3 കാര്യം", [
 ("A","wide","ഉണ്ണീ, ഷോപ്സ് ആക്ട് പുതുക്കലിന് മൂന്ന് കാര്യം ഓർത്താൽ മതി."),
 ("A","A","ഒന്ന്: സർട്ടിഫിക്കറ്റിലെ കാലാവധി തീയതി കലണ്ടറിൽ ഇടുക."),
 ("V","V","രണ്ട്: അപേക്ഷ ലേബർ വകുപ്പിന്റെ LCAS പോർട്ടലിൽ, ഓൺലൈനായി."),
 ("A","A","മൂന്ന്: കാലാവധി തീരുന്നതിന് 30 ദിവസം മുമ്പെങ്കിലും അപേക്ഷിക്കുക. എങ്കിൽ ഓട്ടോമാറ്റിക് ആയി പുതുക്കും."),
 ("V","wide","തീയതി, പോർട്ടൽ, 30 ദിവസം.")],
 "തീയതി, LCAS,\n30 ദിവസം മുമ്പ്", CTA_SHOPS, theme="tip",
 cap_ml="ഷോപ്സ് ആക്ട് പുതുക്കൽ, 3 കാര്യം: സർട്ടിഫിക്കറ്റിലെ കാലാവധി തീയതി കലണ്ടറിൽ ഇടുക; അപേക്ഷ ലേബർ വകുപ്പിന്റെ LCAS പോർട്ടലിൽ ഓൺലൈനായി; കാലാവധി തീരുന്നതിന് 30 ദിവസം മുമ്പെങ്കിലും അപേക്ഷിച്ചാൽ ഓട്ടോമാറ്റിക് പുതുക്കൽ. നിങ്ങളുടെ കലണ്ടറിൽ ഈ തീയതി ഉണ്ടോ?",
 cap_en="Shops Act renewal in 3 steps: put the certificate's expiry date in your calendar; apply online on the Labour Department's LCAS portal; apply at least 30 days before expiry and the renewal is automatic. Is that date in your calendar?",
 cap_mg="Shops Act puthukkal, 3 kaaryam: certificate-ile kaalaavadhi theeyathi calendar-il iduka; apeksha labour department-inte LCAS portal-il online aayi; kaalaavadhi theerunnathinu 30 divasam mumbenkilum apekshichaal automatic puthukkal. Ningalude calendar-il ee theeyathi undo?")
