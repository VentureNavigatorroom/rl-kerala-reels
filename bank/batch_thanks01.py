# Thank-you reels for followers' suggestions (theme "thanks": posted in the news slots, right after corrections).
# 26 Nov: @dev_onthe.move DM'd three things: the voice is slow, it's hard to follow, and asked for a payment-gateway reel.
# Owner: ONE thank-you reel per person covering everything they said (thx01 + thx02 merged into thx03).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
_b = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b); _b.loader.exec_module(_m)
CTA_START = _m.CTA_START

toon("thx03", "solo", "B", {"A": "വിഷ്ണു", "B": "അപ്പൂപ്പൻ"}, "@dev_onthe.move\nപറഞ്ഞു, ഞങ്ങൾ\nമാറ്റി!", [
 ("A", "അപ്പൂപ്പാ, ദേവ് മൂന്ന് കാര്യം പറഞ്ഞു. വോയ്സ് പതുക്കെ, കേട്ട് മനസ്സിലാക്കാൻ പ്രയാസം."),
 ("A", "പിന്നെ പേയ്മെന്റ് ഗേറ്റ്‌വേയെ കുറിച്ച് ഒരു റീൽ വേണമെന്നും."),
 ("B", "മൂന്നും ചെയ്തു. വോയ്സ് വേഗം കൂട്ടി, ശബ്ദം കൂടുതൽ വ്യക്തമാക്കി."),
 ("A", "ഗേറ്റ്‌വേയോ?"),
 ("B", "ഏത് ഗേറ്റ്‌വേ ആയാലും KYC വേണം. ബിസിനസ് പേര് PAN-ലും ബാങ്കിലും ഒരുപോലെ ആയിരിക്കണം.")],
 dict(title="ദേവ് പറഞ്ഞു, ഞങ്ങൾ മാറ്റി", rows=[("വോയ്സ് വേഗം", "കൂട്ടി"), ("ശബ്ദം", "കൂടുതൽ വ്യക്തം"), ("പേയ്മെന്റ് ഗേറ്റ്‌വേ", "പുതിയ സീരീസ്")], total=("നിങ്ങളുടെ നിർദേശം", "DM ചെയ്യൂ")),
 ["ഗേറ്റ്‌വേയ്ക്ക് മുമ്പ് ബിസിനസ് പേര് എല്ലാ രേഖകളിലും ഒരുപോലെ ആക്കുക.", "എന്ത് മാറ്റണം എന്ന് തോന്നിയാലും DM ചെയ്യൂ. ഞങ്ങൾ കേൾക്കും."],
 "എല്ലാത്തിനും\nനന്ദി, ദേവ്", CTA_START, mentor="B", series="വിഷ്ണുവിന്റെ കട", scene="office",
 theme="thanks", collab=["dev_onthe.move"],
 cap_en="Thank you @dev_onthe.move! He told us three things: our voice was slow, it was hard to follow, and he wanted a reel on payment gateways. Done, done and done: the voice is faster and clearer, and payment gateways now have their own series. Quick tip: every gateway runs KYC, and your business name must match on PAN, bank and registration. Got a suggestion? DM us.",
 cap_ml="നന്ദി @dev_onthe.move! ദേവ് മൂന്ന് കാര്യം പറഞ്ഞു: വോയ്സ് പതുക്കെ, കേട്ട് മനസ്സിലാക്കാൻ പ്രയാസം, പേയ്മെന്റ് ഗേറ്റ്‌വേ റീൽ വേണം. മൂന്നും ചെയ്തു: വോയ്സ് വേഗത്തിലും വ്യക്തമായും, ഗേറ്റ്‌വേയ്ക്ക് പുതിയ സീരീസും. നിർദേശം ഉണ്ടോ? DM ചെയ്യൂ.",
 cap_mg="Nanni @dev_onthe.move! Dev moonnu kaaryam paranju: voice pathukke, kettu manassilaakkaan prayaasam, payment gateway reel venam. Moonnum cheythu: voice speed-ilum clear-aayum, gateway-kku puthiya series-um. Suggestion undo? DM cheyyoo.")
