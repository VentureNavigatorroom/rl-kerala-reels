# kl batch 03 (27 Nov night): Shops Act auto-renewal via LCAS, from the verified line added to topics.FACTS_KL (27 Nov).
# Never a fee amount, never a validity period, never a penalty. Invented names and places.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

# new: a bakery waits for the expiry date to renew; applying 30+ days early gets automatic renewal
duo("lcd007", "new_shop", "B", "bakery", "\"കാലാവധി കഴിയുന്ന\nദിവസം പുതുക്കാം\"\nഅത് വൈകിയില്ലേ?", [
 ("A","wide","സാബൂ, ഷോപ്സ് ആക്ട് സർട്ടിഫിക്കറ്റിന്റെ കാലാവധി അടുത്ത മാസം തീരും. തീരുന്ന ദിവസം പുതുക്കാം എന്നാണോ?"),
 ("V","V","ജിഷേ, അത് പോരേ? അന്ന് ഓഫീസിൽ പോയി കൊടുക്കാം."),
 ("A","A","അപേക്ഷ LCAS പോർട്ടലിൽ ഓൺലൈനാണ്. കാലാവധി തീരുന്നതിന് 30 ദിവസം മുമ്പെങ്കിലും അപേക്ഷിച്ചാൽ ഓട്ടോമാറ്റിക് ആയി പുതുക്കും."),
 ("V","V","അപ്പോ ഈ ആഴ്ച തന്നെ അപേക്ഷിക്കാം. സർട്ടിഫിക്കറ്റിലെ തീയതി ഒന്ന് നോക്കട്ടെ."),
 ("A","wide","അവസാന ദിവസമല്ല, 30 ദിവസം മുമ്പ്.")],
 "30 ദിവസം മുമ്പ് അപേക്ഷ,\nഓട്ടോമാറ്റിക് പുതുക്കൽ", CTA_SHOPS, theme="new",
 cap_ml="ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ പുതുക്കാൻ അവസാന ദിവസം വരെ കാത്തിരിക്കല്ലേ. ലേബർ വകുപ്പിന്റെ LCAS പോർട്ടലിൽ, കാലാവധി തീരുന്നതിന് 30 ദിവസം മുമ്പെങ്കിലും അപേക്ഷിച്ചാൽ സർട്ടിഫിക്കറ്റ് ഓട്ടോമാറ്റിക് ആയി പുതുക്കും. നിങ്ങളുടെ സർട്ടിഫിക്കറ്റിലെ കാലാവധി തീയതി ഓർമ്മയുണ്ടോ?",
 cap_en="A bakery plans to renew its Shops Act registration on the day it expires. Renewal is applied for online on the Labour Department's LCAS portal, and an application made at least 30 days before expiry is renewed automatically. Do you remember your certificate's expiry date?",
 cap_mg="Shops Act registration puthukkaan avasaana divasam vare kaathirikkalle. Labour department-inte LCAS portal-il, kaalaavadhi theerunnathinu 30 divasam mumbenkilum apekshichaal certificate automatic aayi puthukkum. Ningalude certificate-ile kaalaavadhi theeyathi ormayundo?")
