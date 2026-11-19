# FSSAI batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

duo("fs001", "cafe_owner", "A", "thattukada", "ഫുഡ് ട്രക്കിന്\nഇൻവെസ്റ്റർ റെഡി.\n\"FSSAI നമ്പർ?\"", [
 ("A","wide","ബിജു, നമ്മുടെ ഫുഡ് ട്രക്കിന് ഒരു ഇൻവെസ്റ്റർ താല്പര്യം കാണിച്ചു! പക്ഷേ ആദ്യ ചോദ്യം FSSAI നമ്പർ."),
 ("V","V","നമുക്ക് ഇതുവരെ ഇല്ലല്ലോ. ട്രക്ക് ഓടി തുടങ്ങിയിട്ട് എടുക്കാം എന്നല്ലേ വെച്ചത്?"),
 ("A","A","അതില്ലാതെ വിറ്റാൽ എന്താ പ്രശ്നം?"),
 ("V","wide","5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. ഡെലിവറി ആപ്പുകളും നമ്പർ ചോദിക്കും."),
 ("A","A","വർഷം 12 ലക്ഷത്തിൽ താഴെ ആണെങ്കിലോ?"),
 ("V","wide","ബേസിക് രജിസ്ട്രേഷൻ മതി. ആദ്യം ലൈസൻസ്, പിന്നെ ദോശ.")],
 "ആദ്യം FSSAI,\nപിന്നെ ആദ്യ ഓർഡർ", CTA_FSSAI, theme="crm",
 cap_ml="ഫുഡ് ട്രക്കിന് ഇൻവെസ്റ്റർ റെഡി, പക്ഷേ FSSAI ഇല്ല. ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും; വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി.",
 cap_en="A food truck founder has an interested investor but no FSSAI registration yet. Selling food without it can mean a penalty up to Rs 5 lakh and up to 6 months in prison. Up to Rs 12 lakh turnover a year, basic registration is enough. Get it before the first order.",
 cap_mg="Food truck-nu investor ready, pakshe FSSAI illa. License illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum; varsham 12 lakh vare turnover-nu basic registration mathi.")