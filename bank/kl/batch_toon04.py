# Toon batch 04 for kl (28 Nov night): episode 8 of "ബിനുവിന്റെ പുതിയ കട". Facts only from topics.FACTS_KL.
# Never a home-business rule, a penalty, a fee amount or a validity period (check the certificate's expiry date).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("lcx08", "town_business", "B", {"A": "ബിനു", "B": "അപ്പൂപ്പൻ", "C": "ജോമോൻ"}, "\"ഒരു വർഷം മാത്രം!\"\n\"അല്ല, അഞ്ച്!\"\nചായക്കടയിൽ തർക്കം", [
 ("C", "ബിനൂ, ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ അഞ്ച് വർഷത്തേക്കാ എന്ന് ഒരാൾ പറഞ്ഞു. നീ എല്ലാ കൊല്ലവും ഓടുന്നത് വെറുതെയാ."),
 ("A", "അപ്പൂപ്പാ, ഞാൻ കേട്ടത് വേറെയാ. ആര് പറഞ്ഞതാ ശരി?"),
 ("B", "തർക്കിക്കണ്ട മോനേ. നിന്റെ സർട്ടിഫിക്കറ്റിൽ കാലാവധി തീരുന്ന തീയതി എഴുതിയിട്ടുണ്ട്. അതാണ് നിന്റെ ഉത്തരം."),
 ("A", "അപ്പോ ആ തീയതിക്ക് 30 ദിവസം മുമ്പെങ്കിലും LCAS പോർട്ടലിൽ പുതുക്കാൻ അപേക്ഷിക്കാം."),
 ("B", "അങ്ങനെ സമയത്ത് അപേക്ഷിച്ചാൽ ഓട്ടോമാറ്റിക് ആയി പുതുക്കും.")],
 dict(title="എത്ര കാലം?", rows=[("ചായക്കടയിലെ കഥ", "ഒന്നോ? അഞ്ചോ?"), ("ശരിയായ ഉത്തരം", "സർട്ടിഫിക്കറ്റിലെ തീയതി"), ("പുതുക്കാൻ", "30 ദിവസം മുമ്പ്, LCAS-ൽ")], total=("നേരത്തെ അപേക്ഷിച്ചാൽ", "ഓട്ടോമാറ്റിക് പുതുക്കൽ")),
 ["സർട്ടിഫിക്കറ്റിലെ കാലാവധി തീയതി നോക്കി ഫോണിൽ ഓർമ്മപ്പെടുത്തൽ വെക്കുക.", "കേട്ട കഥ അല്ല, കയ്യിലുള്ള രേഖ വിശ്വസിക്കുക."],
 "തർക്കം വേണ്ട,\nസർട്ടിഫിക്കറ്റ് നോക്കൂ", topics.CTA_SHOPS, mentor="B", series="ബിനുവിന്റെ പുതിയ കട", ep=8, next="അടുത്ത സീസൺ", scene="teashop", theme="faq",
 cap_ml="ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ എത്ര കാലത്തേക്ക് എന്ന് തർക്കിക്കുകയാണോ? ഉത്തരം നിങ്ങളുടെ സർട്ടിഫിക്കറ്റിലെ കാലാവധി തീയതിയിലുണ്ട്. ആ തീയതിക്ക് 30 ദിവസം മുമ്പെങ്കിലും LCAS പോർട്ടലിൽ അപേക്ഷിച്ചാൽ ഓട്ടോമാറ്റിക് ആയി പുതുക്കും. നിങ്ങളുടേത് എന്ന് തീരും?",
 cap_en="Arguing over how long a Shops Act registration lasts? The answer is the expiry date printed on your own certificate. Apply on the LCAS portal at least 30 days before that date and it is renewed automatically. When does yours expire?",
 cap_mg="Shops Act registration ethra kaalathekku ennu tharkkikkukayaano? Utharam ningalude certificate-ile kaalaavadhi theeyathiyilundu. Aa theeyathikku 30 divasam munpenkilum LCAS portal-il apekshichaal automatic aayi puthukkum. Ningaludethu ennu theerum?")
