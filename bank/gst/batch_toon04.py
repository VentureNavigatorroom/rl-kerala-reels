# Toon batch 04 for gst (28 Nov night), episodes 8-10 of "അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്" (ep 7 teased "അടുത്ത സീസൺ"). Facts only from topics.FACTS_GST.
# Never promise approval. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

# ep 8 (crm, STORY 8): Amal's friend Rizwan gets a REG-03 query on his own GST application and wants to fix his e-mail in the reply
toon("gx08", "trader", "B", {"A": "അമൽ", "B": "അപ്പൂപ്പൻ", "C": "റിസ്വാൻ"}, "കൂട്ടുകാരന്റെ GST\nഅപേക്ഷയ്ക്ക് REG-03.\nഅമലിനോട് സഹായം", [
 ("C", "അമലേ, എന്റെ ചിപ്സ് യൂണിറ്റിന്റെ GST അപേക്ഷയ്ക്ക് REG-03 വന്നു. കൂട്ടത്തിൽ തെറ്റിയ ഇമെയിലും മാറ്റാമല്ലോ?"),
 ("A", "അപ്പൂപ്പാ, മറുപടിയിൽ എന്തൊക്കെ മാറ്റാം?"),
 ("B", "മോനേ, REG-04-ൽ ചോദിച്ച രേഖയും വിശദീകരണവും കൊടുക്കാം. PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ ഈ വഴി മാറ്റാൻ പറ്റില്ല."),
 ("C", "എത്ര ദിവസം ഉണ്ട്?"),
 ("B", "7 പ്രവൃത്തി ദിവസം. മറുപടി ഇല്ലെങ്കിൽ ഓഫീസർക്ക് REG-05-ൽ റിജക്ട് ചെയ്യാം. മറുപടി കിട്ടിയാൽ 7 പ്രവൃത്തി ദിവസത്തിനകം തീരുമാനം.")],
 dict(title="GST ചോദ്യം വന്നാൽ", rows=[("നോട്ടീസ്", "REG-03"), ("മറുപടി", "REG-04, 7 പ്രവൃത്തി ദിവസം"), ("മറുപടി ഇല്ലെങ്കിൽ", "REG-05-ൽ റിജക്ട് ആകാം")], total=("ഈ വഴി മാറ്റാൻ പറ്റാത്തത്", "PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ")),
 ["നോട്ടീസ് മുഴുവൻ വായിച്ച്, ചോദിച്ചതിന് മാത്രം മറുപടി കൊടുക്കുക.", "അപേക്ഷിക്കും മുമ്പ് PAN, മൊബൈൽ, ഇമെയിൽ രണ്ടുതവണ നോക്കുക."],
 "ചോദിച്ചതിന് മറുപടി,\n7 പ്രവൃത്തി ദിവസത്തിൽ", topics.CTA_GST, mentor="B", series="അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്", ep=8, next="ലേറ്റ് ഫീ കണക്ക്", scene="shop", theme="crm",
 cap_ml="GST അപേക്ഷയ്ക്ക് REG-03 വന്നാൽ REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം രേഖയോ വിശദീകരണമോ കൊടുക്കാം. PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ ഈ വഴി മാറ്റാൻ പറ്റില്ല. മറുപടി ഇല്ലെങ്കിൽ REG-05-ൽ റിജക്ട് ആകാം. GST അപേക്ഷിച്ച ഒരു കൂട്ടുകാരന് ഇത് അയക്കൂ.",
 cap_en="Got a REG-03 query on a GST application? Reply in REG-04 within 7 working days with the documents or clarification asked. PAN, State, mobile and e-mail cannot be changed this way, and with no reply the application may be rejected in REG-05. Send this to a friend who just applied.",
 cap_mg="GST apekshaykku REG-03 vannaal REG-04-il 7 working days-inakam rekhayo vishadeekaranamo kodukkaam. PAN, State, mobile, email ee vazhi maattaan pattilla. Marupadi illenkil REG-05-il reject aakaam. GST apekshicha oru koottukaaranu ithu ayakku.")

# ep 9 (faq): Amal files a month's GSTR-3B late during the festival rush; nil vs with-sales late fees
toon("gx09", "online_seller", "B", {"A": "അമൽ", "B": "അപ്പൂപ്പൻ"}, "ഉത്സവ ഓർഡറിന്റെ\nതിരക്കിൽ 3B മറന്നു.\nലേറ്റ് ഫീ എത്ര?", [
 ("A", "അപ്പൂപ്പാ, ഉത്സവ ഓർഡറിന്റെ തിരക്കിൽ ഒരു മാസത്തെ GSTR-3B വൈകി. നിൽ റിട്ടേണിന്റെ ലേറ്റ് ഫീ തന്നെയാണോ?"),
 ("B", "ആ മാസം വിൽപ്പന ഉണ്ടായിരുന്നോ മോനേ? ഉണ്ടെങ്കിൽ ദിവസം 50 രൂപ. ഒന്നര കോടി വരെ ടേൺഓവറിന് ഒരു റിട്ടേണിന് 2,000 വരെ."),
 ("A", "ഒന്നും വിൽക്കാത്ത മാസമായിരുന്നെങ്കിലോ?"),
 ("B", "നിൽ റിട്ടേണിന് ദിവസം 20 രൂപ, 500 വരെ. പക്ഷേ ഓരോ ദിവസവും കൂടും. ഇന്ന് തന്നെ ഫയൽ ചെയ്യ്.")],
 dict(title="GSTR-3B വൈകിയാൽ", rows=[("വിൽപ്പന ഉള്ള മാസം", "ദിവസം 50 രൂപ"), ("നിൽ റിട്ടേൺ", "ദിവസം 20 രൂപ"), ("ഒരു റിട്ടേണിന് പരമാവധി", "2,000 / നിൽ 500")], total=("ഓരോ റിട്ടേണിനും", "വെവ്വേറെ")),
 ["ഫയലിംഗ് തീയതി ഫോണിൽ റിമൈൻഡറാക്കുക.", "തിരക്കുള്ള മാസം ആദ്യം റിട്ടേൺ, പിന്നെ ഓർഡർ."],
 "തിരക്ക് കൂടിയാലും\nറിട്ടേൺ മുടക്കല്ലേ", topics.CTA_PENALTY, mentor="B", series="അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്", ep=9, next="PAN എൻറോൾമെന്റ്", scene="home", theme="faq",
 cap_ml="GSTR-3B വൈകിയാൽ: വിൽപ്പന ഉള്ള മാസം ദിവസം 50 രൂപ ലേറ്റ് ഫീ (ഒന്നര കോടി വരെ ടേൺഓവറിന് ഒരു റിട്ടേണിന് 2,000 വരെ), നിൽ റിട്ടേണിന് ദിവസം 20 രൂപ (500 വരെ). ഓരോ റിട്ടേണിനും വെവ്വേറെ. നിങ്ങൾക്ക് റിമൈൻഡർ ഉണ്ടോ?",
 cap_en="A late GSTR-3B costs 50 a day in a month with sales (capped at 2,000 per return for turnover up to 1.5 crore) and 20 a day for a nil return (capped at 500). Each return counts separately. Do you have a reminder set?",
 cap_mg="GSTR-3B vaikiyaal: vilpana ulla maasam divasam 50 roopa late fee (onnara crore vare turnover-inu oru return-inu 2,000 vare), nil return-inu divasam 20 roopa (500 vare). Oro return-inum vevvere. Ningalkku reminder undo?")

# ep 10 (crm, STORY 11): Amal's cousin sells pickles on a marketplace only within Kerala, below the limit
toon("gx10", "online_seller", "B", {"A": "അമൽ", "B": "അപ്പൂപ്പൻ", "C": "ആരതി"}, "മാർക്കറ്റ്പ്ലേസിൽ\nകേരളത്തിൽ മാത്രം വിൽപ്പന.\nGST വേണോ?", [
 ("C", "അമലേട്ടാ, എന്റെ അച്ചാർ മാർക്കറ്റ്പ്ലേസിൽ ഇടണം. കേരളത്തിൽ മാത്രം. വർഷം 8 ലക്ഷം പോലും ഇല്ല. GST വേണോ?"),
 ("A", "അപ്പൂപ്പാ, എനിക്ക് ആദ്യ വിൽപ്പന മുതൽ GST വേണ്ടി വന്നല്ലോ. ആരതിക്കും അങ്ങനെയല്ലേ?"),
 ("B", "നീ മറ്റ് സംസ്ഥാനത്തേക്ക് അയച്ചു. ലിമിറ്റിന് താഴെ, കേരളത്തിൽ മാത്രം വിൽക്കുന്നവർക്കാണ് PAN വെച്ചുള്ള എൻറോൾമെന്റ്."),
 ("C", "ബെംഗളൂരുവിൽ നിന്ന് ഓർഡർ വന്നാലോ?"),
 ("B", "അന്ന് മുതൽ GST രജിസ്ട്രേഷൻ വേണം മോളേ. സംസ്ഥാനം കടക്കും മുമ്പ് GSTIN.")],
 dict(title="മാർക്കറ്റ്പ്ലേസിൽ സാധനം", rows=[("കേരളത്തിൽ മാത്രം, ലിമിറ്റിന് താഴെ", "PAN എൻറോൾമെന്റ് ആകാം"), ("മാർക്കറ്റ്പ്ലേസ് അനുവദിക്കണം", "ആദ്യം ചോദിക്കൂ"), ("മറ്റ് സംസ്ഥാനത്തേക്ക്", "ആദ്യ വിൽപ്പന മുതൽ GST")], total=("40 ലക്ഷം കടന്നാൽ", "GST രജിസ്ട്രേഷൻ")),
 ["കൂട്ടുകാരന്റെ നിയമം നിങ്ങളുടേതാകണമെന്നില്ല. എവിടേക്ക് വിൽക്കുന്നു എന്ന് നോക്കുക.", "ലിസ്റ്റ് ചെയ്യും മുമ്പ് മാർക്കറ്റ്പ്ലേസിനോട് ചോദിക്കുക."],
 "കേരളത്തിനകത്ത് PAN,\nപുറത്തേക്ക് GSTIN", topics.CTA_LIMIT, mentor="B", series="അമലിന്റെ ഓൺലൈൻ ഷോപ്പ്", ep=10, next="അടുത്ത സീസൺ", scene="home", theme="crm",
 cap_ml="മാർക്കറ്റ്പ്ലേസിൽ സാധനം വിൽക്കാൻ സാധാരണ ആദ്യ വിൽപ്പന മുതൽ GST വേണം. പക്ഷേ ലിമിറ്റിന് താഴെ, കേരളത്തിനകത്ത് മാത്രം വിൽക്കുന്നവർക്ക് മാർക്കറ്റ്പ്ലേസ് അനുവദിച്ചാൽ PAN വെച്ചുള്ള എൻറോൾമെന്റ് മതിയാകാം. മറ്റ് സംസ്ഥാനത്തേക്ക് അയച്ചാൽ GST വേണം. നിങ്ങൾ എവിടേക്കാണ് അയക്കുന്നത്?",
 cap_en="Selling goods on a marketplace usually needs GST from the first sale, but a seller below the limit who sells only within Kerala may use a PAN-based enrolment number if the marketplace supports it. Ship to another state and GST registration is needed. Where do you ship?",
 cap_mg="Marketplace-il goods vilkkaan saadhaarana aadya vilpana muthal GST venam. Pakshe limit-inu thaazhe, Keralathinakathu maathram vilkkunnavarkku marketplace anuvadichaal PAN vechulla enrolment mathiyaakaam. Mattu state-lekku ayachaal GST venam. Ningal evidekkaanu ayakkunnathu?")
