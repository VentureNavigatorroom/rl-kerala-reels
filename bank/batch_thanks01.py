# Thank-you reels for followers' suggestions (theme "thanks": posted in the news slots, right after corrections).
# 26 Nov: @dev_onthe.move DM'd "Voice kurach speed akkumo?" -> voiceover made faster (common.load_wav atempo 1.24, shorter pauses).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
_b = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b); _b.loader.exec_module(_m)
CTA_START = _m.CTA_START

toon("thx01", "solo", "B", {"A": "വിഷ്ണു", "B": "അപ്പൂപ്പൻ"}, "@dev_onthe.move\nപറഞ്ഞു: വോയ്സ്\nകുറച്ച് സ്പീഡ് ആക്കൂ", [
 ("A", "അപ്പൂപ്പാ, ദേവ് മെസേജ് അയച്ചു. നമ്മുടെ വോയ്സ് കുറച്ച് പതുക്കെയാണെന്ന്."),
 ("B", "നല്ല നിർദേശം. ഇന്ന് മുതൽ നമ്മുടെ റീലുകൾ കുറച്ച് വേഗത്തിൽ സംസാരിക്കും."),
 ("A", "ഇതാ, ഇപ്പോൾ തന്നെ ഫാസ്റ്റ് ആയില്ലേ?"),
 ("B", "അതെ! നിങ്ങളുടെ നിർദേശങ്ങൾ ഞങ്ങൾ കേൾക്കും. ദേവിന് നന്ദി!")],
 dict(title="നിങ്ങൾ പറഞ്ഞു, ഞങ്ങൾ മാറ്റി", rows=[("വോയ്സ് വേഗം", "കൂട്ടി"), ("വാക്യങ്ങൾക്കിടയിലെ ഇടവേള", "കുറച്ചു"), ("അടുത്ത നിർദേശം", "നിങ്ങളുടേത്")], total=("നിർദേശം അയക്കാൻ", "DM ചെയ്യൂ")),
 ["എന്ത് മാറ്റണം എന്ന് തോന്നിയാലും DM ചെയ്യൂ.", "നല്ല നിർദേശങ്ങൾക്ക് ഞങ്ങൾ റീലിൽ നന്ദി പറയും."],
 "നിർദേശത്തിന്\nനന്ദി, ദേവ്", CTA_START, mentor="B", series="വിഷ്ണുവിന്റെ കട", scene="teashop",
 theme="thanks", collab=["dev_onthe.move"],
 cap_en="Thank you @dev_onthe.move! He told us our voiceover was a bit slow, so from today our reels speak faster. Got a suggestion too? DM us, we read every message.",
 cap_ml="നന്ദി @dev_onthe.move! ഞങ്ങളുടെ വോയ്സ് കുറച്ച് പതുക്കെയാണെന്ന് പറഞ്ഞു. ഇന്ന് മുതൽ റീലുകൾ കുറച്ച് വേഗത്തിൽ. നിങ്ങൾക്കും നിർദേശം ഉണ്ടോ? DM ചെയ്യൂ.",
 cap_mg="Nanni @dev_onthe.move! Njangalude voice kurachu pathukke aanennu paranju. Innu muthal reels kurachu speed-il. Ningalkkum suggestion undo? DM cheyyoo.")
