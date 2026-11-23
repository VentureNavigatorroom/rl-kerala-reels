# Toon batch 01 (23 Nov): 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("rcx01", "dormant_company", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ", "C": "ലക്ഷ്മി"}, "ബിസിനസ് ഇല്ല.\nഎന്നിട്ടും പിഴ\nനോട്ടീസ്", [
 ("A", "അപ്പൂപ്പാ, രണ്ട് വർഷമായി കമ്പനിയിൽ ഒരു ബിസിനസും ഇല്ല. എന്നിട്ടും ROC പിഴ!"),
 ("C", "ബിസിനസ് ഇല്ലെങ്കിൽ ഫയലിംഗും വേണ്ടല്ലോ എന്നാ ഞങ്ങൾ വിചാരിച്ചത്."),
 ("B", "അത് തെറ്റാ. ബിസിനസ് ഇല്ലെങ്കിലും വർഷത്തിലെ ഫയലിംഗുകൾ വേണം. ലേറ്റ് ഫീ ദിവസം 100 രൂപ, ഓരോ ഫോമിനും.")],
 dict(title="ഫയൽ ചെയ്യാതിരുന്നാൽ", rows=[("ലേറ്റ് ഫീ, ഓരോ ഫോമിനും", "100/ദിവസം"), ("ലേറ്റ് ഫീക്ക് പരിധി", "ഇല്ല"), ("3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ", "ഡയറക്ടർ അയോഗ്യത")], total=("കമ്പനി", "സ്ട്രൈക്ക് ഓഫ് ആകാം")),
 ["ബിസിനസ് ഇല്ലെങ്കിലും AOC-4, MGT-7 ഫയൽ ചെയ്യുക.", "എല്ലാ ഡയറക്ടർമാരുടെയും DIR-3 KYC സെപ്റ്റംബർ 30-ന് മുമ്പ്."],
 "ബിസിനസ് ഇല്ല ≠\nഫയലിംഗ് ഇല്ല", topics.CTA_FILING, mentor="B", series="മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി", ep=1, next="AGM കലണ്ടർ", scene="teashop", theme="faq")

toon("rcx02", "new_company_roc", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ"}, "AGM കഴിഞ്ഞു.\nഇനി ഒന്നും\nവേണ്ടല്ലോ?", [
 ("A", "അപ്പൂപ്പാ, സെപ്റ്റംബറിൽ AGM നടത്തി. ഇനി അടുത്ത വർഷം വരെ ഫ്രീ അല്ലേ?"),
 ("B", "ഇല്ല മോനേ. AGM-ന് ശേഷമാണ് രണ്ട് പ്രധാന ഫോമുകൾ വരുന്നത്."),
 ("A", "ഏതൊക്കെ? എത്ര ദിവസത്തിനുള്ളിൽ?")],
 dict(title="AGM-ന് ശേഷമുള്ള\nകലണ്ടർ", rows=[("AGM", "സെപ്റ്റംബർ 30"), ("AOC-4", "AGM + 30 ദിവസം"), ("MGT-7/7A", "AGM + 60 ദിവസം")], total=("വൈകിയാൽ", "100/ദിവസം")),
 ["AGM തീയതി മുതൽ 30-ഉം 60-ഉം ദിവസം എണ്ണി കലണ്ടറിൽ ഇടുക.", "LLP ആണെങ്കിൽ ഫോം 11 മെയ് 30, ഫോം 8 ഒക്ടോബർ 30."],
 "AGM കഴിഞ്ഞാൽ\nകൗണ്ട്ഡൗൺ തുടങ്ങും", topics.CTA_ROC, mentor="B", series="മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി", ep=2, next="LLP ആണെങ്കിൽ?", scene="office", theme="faq")
