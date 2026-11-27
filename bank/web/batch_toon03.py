# Toon batch 03 for web (27 Nov evening refill), episode 9 of "റിയയുടെ ബുട്ടീക്". Facts only from topics.FACTS_WEB.
# Our service: never a price, instalment amount or delivery date; never promise rankings or sales.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("wbx09", "online_shop", "B", {"A": "റിയ", "B": "അമ്മൂമ്മ", "C": "സോണിയ"}, "കാർട്ടിൽ ചുരിദാർ ഇട്ടു.\nപിന്നെ കസ്റ്റമർ\nപോയി", [
 ("C", "റിയേ, ഞാൻ നിന്റെ സൈറ്റിൽ ചുരിദാർ എടുത്തു. പക്ഷേ സൈസ് ശരിയായില്ലെങ്കിൽ എന്ത് ചെയ്യും എന്ന് എവിടെയും ഇല്ല."),
 ("A", "അമ്മൂമ്മേ, ചോദിച്ചാൽ ഞാൻ മാറ്റിക്കൊടുക്കും. അത് എഴുതി വെക്കണോ?"),
 ("B", "കാണാത്ത കടയിൽ നിന്ന് വാങ്ങുന്നവർക്ക് എഴുതിയത് വേണം. റിഫണ്ട്, ടേംസ്, പ്രൈവസി പേജുകൾ വിശ്വാസം കൂട്ടും.")],
 dict(title="ഓൺലൈൻ കടയ്ക്ക് 3 പേജ്", rows=[("റിഫണ്ട് / മാറ്റൽ", "എങ്ങനെ എന്ന്"), ("ടേംസ്", "ഓർഡർ നിയമങ്ങൾ"), ("പ്രൈവസി", "നമ്പർ എന്ത് ചെയ്യും")], total=("എഴുതിയാൽ", "കസ്റ്റമർക്ക് ധൈര്യം")),
 ["വായിൽ പറയുന്ന നിയമം സൈറ്റിൽ എഴുതി വെക്കുക.", "ഓർഡർ ബട്ടണിന് അടുത്ത് ആ പേജിന്റെ ലിങ്ക് കൊടുക്കുക."],
 "പറയുന്ന വാക്ക്\nസൈറ്റിൽ എഴുതൂ", topics.CTA_WEBSITE, mentor="B", series="റിയയുടെ ബുട്ടീക്", ep=9, next="അടുത്ത സീസൺ", scene="shop", theme="faq")
