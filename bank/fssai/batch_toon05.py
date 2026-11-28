# Toon batch 05 (28 Nov night), episodes 9-10 of "സുമയുടെ ഹോം ബേക്കറി" (ep 8 teased "അടുത്ത സീസൺ"). Facts only from topics.FACTS_FSSAI.
# New limits only (Rs 1.5 crore / Rs 50 crore); perpetual validity only for licences issued on/after 1 Apr 2026; yearly amount still payable. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

# ep 9: Suma's registration (2026) vs her friend Jisha's 2024 licence: one needs no renewal, the other checks expiry; both keep paying yearly
toon("fsy09", "home_baker", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ", "C": "ജിഷ"}, "രണ്ട് ബേക്കറി.\nഒന്നിന് പുതുക്കൽ ഇല്ല.\nമറ്റേതിനോ?", [
 ("C", "സുമേ, നിന്റെ FSSAI പുതുക്കേണ്ടല്ലോ. അപ്പോ എന്റെ 2024-ലെ ലൈസൻസും അങ്ങനെ തന്നെ ആയിരിക്കും, അല്ലേ?"),
 ("A", "അമ്മൂമ്മേ, എന്റേത് ഈ വർഷം കിട്ടിയതാ. ജിഷയുടേത് പഴയതാ. രണ്ടും ഒന്നാണോ?"),
 ("B", "2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയതിനാണ് സ്ഥിരം സാധുത ഉറപ്പ്. ജിഷ മോളേ, നിന്റേതിന്റെ കാലാവധി FoSCoS-ൽ നോക്കി സമയത്ത് പുതുക്ക്."),
 ("C", "അപ്പോ സുമയ്ക്ക് ഇനി ഒന്നും അടയ്ക്കാനില്ല!"),
 ("B", "അങ്ങനെയല്ല. FSSAI-ക്കുള്ള വാർഷിക അടവ് രണ്ടുപേർക്കും ഉണ്ട്. വേണമെങ്കിൽ കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് അടയ്ക്കാം.")],
 dict(title="ലൈസൻസ് കിട്ടിയത് എപ്പോൾ?", rows=[("2026 ഏപ്രിൽ 1 മുതൽ", "പുതുക്കൽ അപേക്ഷ ഇല്ല"), ("അതിന് മുമ്പ്", "FoSCoS-ൽ കാലാവധി നോക്കൂ"), ("വാർഷിക അടവ്", "രണ്ടിനും തുടരും")], total=("ഊഹം വേണ്ട", "തീയതി നോക്കൂ")),
 ["കൂട്ടുകാരിയുടെ ലൈസൻസ് തീയതി നിങ്ങളുടേതല്ല.", "വാർഷിക അടവ് കലണ്ടറിൽ എഴുതി വെക്കുക."],
 "തീയതി നോക്കൂ,\nഅടവ് മുടക്കല്ലേ", topics.CTA_FSSAI, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=9, next="ബേക്കറി വളർന്നാൽ", scene="home", theme="faq",
 cap_ml="2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ FSSAI ലൈസൻസിനും രജിസ്ട്രേഷനും പുതുക്കൽ വേണ്ട. അതിന് മുമ്പ് കിട്ടിയതാണെങ്കിൽ FoSCoS-ൽ കാലാവധി തീയതി നോക്കി സമയത്ത് പുതുക്കൂ. FSSAI-ക്കുള്ള വാർഷിക അടവ് എല്ലാവർക്കും തുടരും. നിങ്ങളുടേത് ഏത് വർഷം കിട്ടിയതാണ്?",
 cap_en="Two bakeries, two answers: an FSSAI licence issued on or after 1 April 2026 needs no renewal; an older one, check its expiry on FoSCoS and renew on time. The yearly payment to FSSAI continues for both. Which year was yours issued?",
 cap_mg="2026 April 1 muthal kittiya FSSAI licence-num registration-num renew venda. Athinu mumpu kittiyathaanenkil FoSCoS-il expiry date nokki samayathu renew cheyyu. FSSAI-kkulla annual payment ellavarkkum thudarum. Ningaludethu ethu varsham kittiyathaanu?")

# ep 10: the bakery opens a second counter and delivery orders; turnover heads past Rs 1.5 crore
toon("fsy10", "home_baker", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ", "C": "ഡെയ്സി"}, "ഹോം ബേക്കറി ഇപ്പോ\nരണ്ട് കൗണ്ടർ.\nടേൺഓവർ 1.7 കോടി", [
 ("C", "സുമേ, ടൗണിലെ പുതിയ കൗണ്ടറും ഡെലിവറി ഓർഡറും ചേർത്ത് ഈ കൊല്ലം ഒന്നേമുക്കാൽ കോടിയോളം ആയില്ലേ?"),
 ("A", "അമ്മൂമ്മേ, 1.7 കോടി ആകും. എന്റെ ബേസിക് രജിസ്ട്രേഷൻ ഇനിയും മതിയോ?"),
 ("B", "1.5 കോടി കടന്നാൽ സ്റ്റേറ്റ് ലൈസൻസ് വേണം മോളേ. 50 കോടി വരെ അത്. അതിന് മുകളിൽ സെൻട്രൽ."),
 ("A", "വിദേശ ചോക്ലേറ്റ് ഞാൻ തന്നെ ഇറക്കിയാലോ?"),
 ("B", "ഇറക്കുമതി ചെയ്യുന്നവർക്ക് ടേൺഓവർ എത്രയായാലും സെൻട്രൽ ലൈസൻസ്. അപേക്ഷയ്ക്ക് മുമ്പ് FoSCoS-ൽ കാറ്റഗറിയും നോക്കണം.")],
 dict(title="ബേക്കറി വളരുമ്പോൾ", rows=[("1.5 കോടി വരെ", "ബേസിക് രജിസ്ട്രേഷൻ"), ("1.5 മുതൽ 50 കോടി", "സ്റ്റേറ്റ് ലൈസൻസ്"), ("50 കോടിക്ക് മുകളിൽ", "സെൻട്രൽ ലൈസൻസ്")], total=("ഇറക്കുമതി", "എപ്പോഴും സെൻട്രൽ")),
 ["ഓരോ വർഷവും ടേൺഓവർ നോക്കി ലൈസൻസ് ഒത്തുനോക്കുക.", "പുതിയ കൗണ്ടർ തുറക്കും മുമ്പ് FoSCoS-ൽ കാറ്റഗറി ഉറപ്പാക്കുക."],
 "കട വളർന്നാൽ\nലൈസൻസും വളരണം", topics.CTA_FSSAI, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", ep=10, next="അടുത്ത സീസൺ", scene="shop", theme="new",
 cap_ml="ഹോം ബേക്കറി വളർന്ന് ടേൺഓവർ 1.5 കോടി കടന്നാൽ FSSAI സ്റ്റേറ്റ് ലൈസൻസ് വേണം, 50 കോടി വരെ. അതിന് മുകളിൽ സെൻട്രൽ. ഇറക്കുമതി ചെയ്യുന്നവർക്ക് ടേൺഓവർ നോക്കാതെ സെൻട്രൽ. FoSCoS-ൽ കാറ്റഗറിയും നോക്കൂ. നിങ്ങളുടെ ബേക്കറി ഈ വർഷം എത്ര വളർന്നു?",
 cap_en="When a home bakery grows past 1.5 crore turnover, it needs a state FSSAI licence (up to 50 crore); above 50 crore, a central licence. Importing ingredients yourself needs a central licence whatever the turnover. Check your category on FoSCoS too. How much did your bakery grow this year?",
 cap_mg="Home bakery valarnnu turnover 1.5 crore kadannaal FSSAI State licence venam, 50 crore vare. Athinu mukalil Central. Import cheyyunnavarkku turnover nokkaathe Central. FoSCoS-il category-um nokku. Ningalude bakery ee varsham ethra valarnnu?")
