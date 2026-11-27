# Toon batch 03 (27 Nov), episode 7 of "സുമയുടെ ഹോം ബേക്കറി" (ep 6 teased "ലേബൽ"). Facts only from topics.FACTS_FSSAI. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("fsy07", "home_baker", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ", "C": "ജിഷ"}, "ക്രിസ്മസ് ഗിഫ്റ്റ് ബോക്സ്\nഭംഗിയായി.\nനമ്പർ മറന്നു!", [
 ("C", "സുമേ, ക്രിസ്മസ് കേക്ക് ബോക്സ് അടിപൊളി! പക്ഷേ ഇതിൽ FSSAI നമ്പർ എവിടെ?"),
 ("A", "അയ്യോ, പുതിയ ഡിസൈനിൽ അത് വിട്ടുപോയി. പഴയ സ്റ്റിക്കറിൽ ഉണ്ടായിരുന്നു."),
 ("B", "പാക്കറ്റ് ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ വേണം മോളേ. ബോക്സ് മാറിയാലും നമ്പർ മാറാതെ കയറണം."),
 ("A", "അപ്പോ പ്രിന്റിന് കൊടുക്കും മുമ്പ് ഒരു ചെക്ക്.")],
 dict(title="പുതിയ ബോക്സ് ചെക്ക്", rows=[("14 അക്ക നമ്പർ", "ഉണ്ടോ?"), ("പഴയ ഡിസൈനിൽ", "ഉണ്ടായിരുന്നത്"), ("പ്രിന്റിന് മുമ്പ്", "ഒത്തുനോക്കുക")], total=("നമ്പർ ഇല്ലാതെ", "വിൽക്കരുത്")),
 ["ഓരോ പുതിയ പാക്കറ്റ് ഡിസൈനിലും FSSAI നമ്പർ ആദ്യം നോക്കുക.", "സീസൺ ബോക്സിനും സാധാരണ പാക്കറ്റിന്റെ അതേ നിയമം."],
 "ഡിസൈൻ മാറാം,\nനമ്പർ മാറരുത്", topics.CTA_FOOD, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=7, next="കാറ്റഗറി ആദ്യം", scene="home", theme="new")
