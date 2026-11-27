# FSSAI batch 08 (27 Nov refill). Facts only from topics.FACTS_FSSAI (2026 limits). No prices. Max 6 lines.
# new: the category on FoSCoS decides before the turnover does (some kinds of business need a licence whatever the turnover)
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# new: two farmers start a small unit together; one assumes "small turnover = basic registration" without checking the category
duo("fs048", "packaged_food", "B", "farm", "ടേൺഓവർ കുറവാ.\n\"ബേസിക് മതി\"\nകാറ്റഗറി നോക്കിയോ?", [
 ("A","wide","ഗോപീ, നമ്മുടെ പുതിയ യൂണിറ്റിന് ടേൺഓവർ ഒരു കോടി പോലും ആകില്ല. FSSAI ബേസിക് രജിസ്ട്രേഷൻ മതിയല്ലോ."),
 ("V","V","വാസുവേട്ടാ, ടേൺഓവർ മാത്രം നോക്കിയാൽ പോരാ. ചില തരം ബിസിനസിന് ടേൺഓവർ എത്രയായാലും ലൈസൻസ് വേണം."),
 ("A","A","അത് എങ്ങനെ അറിയും?"),
 ("V","wide","FoSCoS-ൽ നമ്മുടെ ബിസിനസ് ഏത് കാറ്റഗറി എന്ന് ആദ്യം നോക്കണം. അതിന് ശേഷം മാത്രം അപേക്ഷ."),
 ("A","A","ആദ്യം കാറ്റഗറി, പിന്നെ കണക്ക്."),
 ("V","wide","ഊഹിച്ച് എടുത്ത രജിസ്ട്രേഷൻ, പിന്നെ തിരുത്തേണ്ടി വരും.")],
 "ആദ്യം കാറ്റഗറി,\nപിന്നെ ടേൺഓവർ", CTA_FSSAI, theme="new",
 cap_ml="ടേൺഓവർ ചെറുതാണ്, അതുകൊണ്ട് FSSAI ബേസിക് രജിസ്ട്രേഷൻ മതി എന്ന് കരുതിയോ? ചില തരം ഫുഡ് ബിസിനസിന് ടേൺഓവർ എത്രയായാലും ലൈസൻസ് വേണം. അപേക്ഷിക്കും മുമ്പ് FoSCoS-ൽ നിങ്ങളുടെ ബിസിനസിന്റെ കാറ്റഗറി നോക്കൂ. നിങ്ങളുടെ ബിസിനസ് ഏത് കാറ്റഗറിയിലാണ്?",
 cap_en="Two farmers starting a small food unit assume a low turnover means basic FSSAI registration is enough. Some kinds of food business need a licence whatever the turnover, so check your business category on FoSCoS before you apply. Which category is your business in?",
 cap_mg="Turnover cheruthaanu, athukondu FSSAI basic registration mathi ennu karuthiyo? Chila tharam food business-inu turnover ethrayaayaalum licence venam. Apekshikkum mumpu FoSCoS-il ningalude business-inte category nokku. Ningalude business ethu category-il aanu?")
