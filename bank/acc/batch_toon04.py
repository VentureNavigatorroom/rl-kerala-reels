# Toon batch 04 for acc (28 Nov night): episodes 9-10 of "സനലിന്റെ കണക്കുപുസ്തകം".
# Facts only from topics.FACTS_ACC. No fixed due dates, no tax amounts, no fees of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("acx09", "small_trader_acc", "B", {"A": "സനൽ", "B": "അമ്മൂമ്മ", "C": "അജ്മൽ"}, "\"GST 40% ആയി!\"\nഒരു വീഡിയോ,\nകടയിൽ പരിഭ്രാന്തി", [
 ("C", "സനലേ, ഫോണിൽ ഒരു വീഡിയോ കണ്ടു. GST ഇനി 40% ആണത്രേ. നിന്റെ ബില്ലിംഗ് മുഴുവൻ മാറ്റണ്ടേ?"),
 ("A", "അമ്മൂമ്മേ, ഇനി എല്ലാ സാധനത്തിനും 40% ആണോ?"),
 ("B", "പകുതി കേട്ട് ഓടല്ലേ മോനേ. 2025 സെപ്റ്റംബർ 22-ന് റേറ്റുകൾ മാറി. മിക്കതും 5% അല്ലെങ്കിൽ 18%. 40% കുറച്ച് സാധനങ്ങൾക്ക് മാത്രം."),
 ("A", "അപ്പോ ഓരോ ഐറ്റത്തിന്റെയും റേറ്റ് ടീമിനോട് ഉറപ്പാക്കിയിട്ട് മാത്രം ബില്ലിംഗ് മാറ്റാം.")],
 dict(title="2025 സെപ്റ്റംബർ 22 മുതൽ", rows=[("മിക്ക സാധനങ്ങൾക്കും", "5% അല്ലെങ്കിൽ 18%"), ("കുറച്ച് സാധനങ്ങൾക്ക്", "40%"), ("നിങ്ങളുടെ ഐറ്റം", "ടീമിനോട് ഉറപ്പാക്കുക")], total=("വീഡിയോ കണ്ട്", "ബിൽ മാറ്റരുത്")),
 ["കേട്ട വാർത്ത ബില്ലിൽ കയറ്റും മുമ്പ് ഐറ്റം തിരിച്ച് റേറ്റ് നോക്കുക.", "റേറ്റ് മാറ്റിയാൽ അടുത്ത ബിൽ ഒന്ന് പരിശോധിക്കുക."],
 "40% എല്ലാത്തിനുമല്ല,\nഐറ്റം നോക്കൂ", topics.CTA_ACCOUNTS, mentor="B", series="സനലിന്റെ കണക്കുപുസ്തകം", ep=9, next="ഫോർവേഡ് വന്ന ഡ്യൂ ഡേറ്റ്", scene="shop", theme="faq",
 cap_ml="GST 40% ആയി എന്ന വീഡിയോ കണ്ട് പേടിച്ചോ? 2025 സെപ്റ്റംബർ 22 മുതൽ മിക്ക സാധനങ്ങൾക്കും 5% അല്ലെങ്കിൽ 18% ആണ്. 40% കുറച്ച് സാധനങ്ങൾക്ക് മാത്രം. നിങ്ങളുടെ ഓരോ ഐറ്റത്തിന്റെയും റേറ്റ് ഉറപ്പാക്കിയിട്ട് ബിൽ മാറ്റൂ. നിങ്ങളുടെ ബില്ലിംഗ് പുതുക്കിയോ?",
 cap_en="Panicked by a video saying GST is now 40%? Since 22 Sep 2025 most goods are at 5% or 18%; 40% applies only to a few goods. Confirm the rate of each of your items before changing your bills. Has your billing been updated?",
 cap_mg="GST 40% aayi enna video kandu pediccho? 2025 September 22 muthal mikka saadhanangalkkum 5% allenkil 18% aanu. 40% kurachu saadhanangalkku maathram. Ningalude oro item-inteyum rate urappaakkiyittu bill maattu. Ningalude billing puthukkiyo?")

toon("acx10", "freelancer_itr", "B", {"A": "സനൽ", "B": "അമ്മൂമ്മ", "C": "മീര"}, "\"ITR ഡേറ്റ് നീട്ടി\"\nഗ്രൂപ്പിൽ ഫോർവേഡ്.\nആര് അയച്ചതാ?", [
 ("C", "സനലേ, ഗ്രൂപ്പിൽ ഫോർവേഡ് വന്നു: ITR ലാസ്റ്റ് ഡേറ്റ് നീട്ടി. ഡിസൈൻ ജോലി തീർത്തിട്ട് പതുക്കെ ഫയൽ ചെയ്യാം."),
 ("A", "അമ്മൂമ്മേ, ഫോർവേഡ് വിശ്വസിച്ച് കാത്തിരിക്കാമോ?"),
 ("B", "ആര് ഉണ്ടാക്കിയ മെസേജാ എന്ന് ആർക്കും അറിയില്ല. കഴിഞ്ഞ വർഷത്തേതും ആകാം. ഡ്യൂ ഡേറ്റ് ടീമിനോട് ഉറപ്പാക്ക്."),
 ("C", "തെറ്റിയാൽ? വരുമാനം 5 ലക്ഷത്തിന് മുകളിലാ."),
 ("B", "എങ്കിൽ ലേറ്റ് ഫീ 5,000 രൂപ. 5 ലക്ഷം വരെയാണെങ്കിൽ 1,000 രൂപ. ഫോർവേഡ് അത് അടച്ചുതരില്ല.")],
 dict(title="ഫോർവേഡ് വന്നാൽ", rows=[("ഫോർവേഡ് മെസേജ്", "തെളിവല്ല"), ("ഡ്യൂ ഡേറ്റ്", "ടീമിനോട് ഉറപ്പാക്കുക"), ("വൈകിയാൽ", "1,000 / 5,000 രൂപ ലേറ്റ് ഫീ")], total=("ഉറപ്പില്ലെങ്കിൽ", "നേരത്തെ ഫയൽ ചെയ്യുക")),
 ["ഡ്യൂ ഡേറ്റ് ഫോർവേഡിൽ നിന്നല്ല, ടീമിൽ നിന്ന് ഉറപ്പാക്കുക.", "സംശയമുള്ള വർഷം കാത്തിരിക്കാതെ നേരത്തെ ഫയൽ ചെയ്യുക."],
 "ഫോർവേഡ് ഫ്രീ,\nലേറ്റ് ഫീ അല്ല", topics.CTA_ITR, mentor="B", series="സനലിന്റെ കണക്കുപുസ്തകം", ep=10, next="അടുത്ത സീസൺ", scene="office", theme="faq",
 cap_ml="ITR ഡേറ്റ് നീട്ടി എന്ന ഫോർവേഡ് കണ്ട് കാത്തിരിക്കുകയാണോ? ആ മെസേജ് ആര് ഉണ്ടാക്കിയതെന്ന് അറിയില്ല. ഡ്യൂ ഡേറ്റ് ടീമിനോട് ഉറപ്പാക്കൂ. വൈകിയാൽ ലേറ്റ് ഫീ 1,000 രൂപ (വരുമാനം 5 ലക്ഷം വരെ) അല്ലെങ്കിൽ 5,000 രൂപ. നിങ്ങൾക്കും ഇങ്ങനെ ഒരു ഫോർവേഡ് വന്നോ?",
 cap_en="Waiting because a forward said the ITR date was extended? Nobody knows who made that message. Confirm the due date with the team. A late ITR costs a late fee of 1,000 rupees (income up to 5 lakh) or 5,000 rupees. Did you get a forward like this too?",
 cap_mg="ITR date neetti enna forward kandu kaathirikkukayaano? Aa message aaru undaakkiyathennu ariyilla. Due date team-inodu urappaakku. Vaikiyaal late fee 1,000 rupees (varumaanam 5 lakh vare) allenkil 5,000 rupees. Ningalkkum ingane oru forward vanno?")
