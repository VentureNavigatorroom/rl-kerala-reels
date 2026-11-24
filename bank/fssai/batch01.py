# FSSAI seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_FSSAI. Amounts are turnover limits / statutory penalties (no rupee word next to them). People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD



duo("fsd003", "packaged_food", "A", "fishmarket", "ഉണക്കമീൻ പാക്കറ്റ്.\nസൂപ്പർമാർക്കറ്റ്\nതിരിച്ചയച്ചു", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, സൂപ്പർമാർക്കറ്റ് നമ്മുടെ ഉണക്കമീൻ പാക്കറ്റുകൾ തിരിച്ചയച്ചു."),
 ("V","V","സുമേ, മീൻ നല്ലതല്ലേ? എന്താ പ്രശ്നം?"),
 ("A","A","പാക്കറ്റിൽ FSSAI നമ്പർ ഇല്ല."),
 ("V","V","പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം. അതാണ് ആദ്യം നോക്കുന്നത്."),
 ("A","wide","അപ്പോ ആദ്യം ലൈസൻസ്, പിന്നെ പുതിയ ലേബൽ."),
 ("V","wide","മീനിന് ഉപ്പ്, പാക്കറ്റിന് നമ്പർ.")],
 "പാക്കറ്റിൽ\n14 അക്ക നമ്പർ", CTA_FSSAI, theme="new",
 cap_ml="പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം. ഉണക്കമീൻ മുതൽ അച്ചാർ വരെ. നിങ്ങളുടെ പാക്കറ്റിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="A supermarket returns a batch of dried-fish packets: no FSSAI number on the label. Packaged food must carry the 14-digit FSSAI number. Is it on your packets?",
 cap_mg="Pack cheythu vilkkunna food-il 14 akka FSSAI number print cheyyanam. Unakkameen muthal achaar vare. Ningalude packet-il number undo?")



