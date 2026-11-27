# Toon batch 03 for gst (27 Nov evening), episode 7 of "അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്" (ep 6 teased "ഡോക്യുമെന്റുകൾ"). Facts only from topics.FACTS_GST. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("gx07", "trader", "B", {"A": "അമൽ", "B": "അപ്പൂപ്പൻ", "C": "ഷെറിൻ"}, "വാടക ഗോഡൗണിൽ\nനിന്ന് GST അപേക്ഷ.\nഒരു പേപ്പർ കുറവ്", [
 ("C", "അമലേ, പുതിയ വാടക ഗോഡൗണിന്റെ അഡ്രസിൽ GST അപേക്ഷിച്ചില്ലേ? വാടക കരാർ മാത്രം കൊടുത്തു എന്ന് കേട്ടു."),
 ("A", "അപ്പൂപ്പാ, കരാർ ഉണ്ടല്ലോ. അത് പോരേ?"),
 ("B", "വാടക സ്ഥലമാണെങ്കിൽ കരാറിനൊപ്പം ഉടമയുടെ NOC-യും ഒരു ബില്ലും വേണം. ആധാർ OTP വരുന്ന മൊബൈലും കയ്യിൽ വേണം.")],
 dict(title="പ്രൊപ്രൈറ്ററുടെ GST രേഖകൾ", rows=[("PAN, ആധാർ, ഫോട്ടോ", "വേണം"), ("വാടക സ്ഥലം", "കരാർ + NOC + ബിൽ"), ("ബാങ്ക് രേഖ", "ചെക്ക് / പാസ്ബുക്ക്")], total=("ഒന്ന് കുറഞ്ഞാൽ", "അപേക്ഷ വൈകും")),
 ["വാടകയ്ക്ക് എടുക്കുമ്പോൾ തന്നെ ഉടമയുടെ NOC വാങ്ങി വെക്കുക.", "ആധാറിലെ മൊബൈൽ നമ്പർ ആക്ടീവ് ആണോ എന്ന് നോക്കുക."],
 "കരാർ മാത്രം പോരാ,\nNOC-യും ബില്ലും", topics.CTA_GST, mentor="B", series="അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്", ep=7, next="അടുത്ത സീസൺ", scene="shop", theme="faq")
