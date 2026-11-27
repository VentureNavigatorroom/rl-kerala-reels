# web tips 02 (27 Nov evening): tip reel as a duo3d scene. theme="tip". Facts only from topics.FACTS_WEB (+ FACTS_PG: gateways ask website details).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_WEBSITE, CTA_WEBPLAN = topics.CTA_WEBSITE, topics.CTA_WEBPLAN

duo("wbt003", "online_shop", "B", "mall", "ഓൺലൈൻ പേയ്മെന്റ്\nതുടങ്ങും മുമ്പ്\nസൈറ്റിൽ 3 കാര്യം", [
 ("A","wide","ജാഫറേ, ഗേറ്റ്‌വേ അപേക്ഷയിൽ സാധാരണ വെബ്സൈറ്റ് അല്ലെങ്കിൽ ആപ്പ് വിവരം ചോദിക്കും. അതിന് മുമ്പ് മൂന്ന് കാര്യം."),
 ("A","A","ഒന്ന്: എന്ത് വിൽക്കുന്നു എന്ന് യഥാർത്ഥ ഫോട്ടോയോടെ വ്യക്തമായി."),
 ("V","V","രണ്ട്: അഡ്രസ്, ഫോൺ, വാട്സ്ആപ്പ് ബട്ടൺ, എല്ലാം ഇപ്പോഴത്തേത്."),
 ("A","A","മൂന്ന്: റിഫണ്ട്, ടേംസ്, പ്രൈവസി പേജുകൾ. കസ്റ്റമർക്കും വിശ്വാസം."),
 ("V","wide","എന്ത്, എവിടെ, എങ്ങനെ. മൂന്നും സൈറ്റിൽ.")],
 "എന്ത് വിൽക്കുന്നു,\nഎവിടെ, എന്ത് നിയമം", CTA_WEBSITE, theme="tip",
 cap_ml="ഓൺലൈൻ പേയ്മെന്റ് തുടങ്ങും മുമ്പ് സൈറ്റിൽ 3 കാര്യം: എന്ത് വിൽക്കുന്നു എന്ന് യഥാർത്ഥ ഫോട്ടോയോടെ, ഇപ്പോഴത്തെ അഡ്രസും ഫോണും വാട്സ്ആപ്പ് ബട്ടണും, റിഫണ്ട് / ടേംസ് / പ്രൈവസി പേജുകൾ. ഗേറ്റ്‌വേകൾ സാധാരണ വെബ്സൈറ്റ് വിവരം ചോദിക്കാറുണ്ട്. ഇതിൽ ഏതാണ് നിങ്ങളുടെ സൈറ്റിൽ ഇല്ലാത്തത്?",
 cap_en="Three things on your site before you start online payments: what you sell, with real photos; your current address, phone and a WhatsApp button; refund, terms and privacy pages. Gateways commonly ask for website details. Which one is missing on yours?",
 cap_mg="Online payment thudangum mumbu site-il 3 kaaryam: enthu vilkkunnu ennu yathaartha photo-yode, ippozhathe address-um phone-um WhatsApp button-um, refund / terms / privacy pages. Gateways saadhaarana website vivaram chodikkaarundu. Ithil ethaanu ningalude site-il illaathathu?")
