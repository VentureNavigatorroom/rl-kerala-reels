# Toon batch 04 for roc (28 Nov night), episodes 8-10 of "മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി" (ep 7 teased "അടുത്ത സീസൺ").
# Fix-it episodes: late fee Rs 100 a day per form (approved amounts only), 3 years of non-filing. Facts only from topics.FACTS_ROC. No fees of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
SER = "മനോജിന്റെ ഉറങ്ങുന്ന കമ്പനി"

toon("rcx08", "late_filer", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ"}, "AOC-4 ഒരു മാസം\nവൈകി. MGT-7-ന്\nഇന്ന് അവസാന ദിവസം", [
 ("A", "അപ്പൂപ്പാ, AGM സെപ്റ്റംബർ 30-ന് നടത്തി. AOC-4 മറന്നു. ഇന്ന് നവംബർ 29. രണ്ടും നാളെ ഒന്നിച്ച് ചെയ്താലോ?"),
 ("B", "AOC-4-ന്റെ ദിവസം ഒക്ടോബർ 30-ന് കഴിഞ്ഞു. 30 ദിവസം വൈകി, 3,000 രൂപ. MGT-7-ന് AGM കഴിഞ്ഞ് 60 ദിവസം, അത് ഇന്നാണ് തീരുന്നത്."),
 ("A", "അപ്പോ ഇന്ന് ചെയ്താൽ MGT-7-ന് ലേറ്റ് ഫീ ഇല്ലേ?"),
 ("B", "ഇല്ല. നാളെ ആയാൽ രണ്ട് ഫോമിനും ദിവസം 100 വീതം. ഇന്ന് രാത്രി ഉറങ്ങും മുമ്പ് രണ്ടും ഫയൽ ചെയ്യ്.")],
 dict(title="ഇന്നോ നാളെയോ?", rows=[("AOC-4, 30 ദിവസം വൈകി", "3,000"), ("MGT-7, ഇന്ന് ഫയൽ ചെയ്താൽ", "0"), ("നാളെ മുതൽ", "രണ്ടിനും ദിവസം 100")], total=("ഇന്ന് ഫയൽ ചെയ്താൽ", "3,000 രൂപ")),
 ["സമയം ബാക്കിയുള്ള ഫോം സമയത്തിനുള്ളിൽ തന്നെ തീർക്കുക.", "വൈകിയ ഫോം നാളത്തേക്ക് വെക്കാതെ ഇന്ന് ഫയൽ ചെയ്യുക."],
 "ഒരു ദിവസം വൈകിയാൽ\nരണ്ട് മീറ്റർ", topics.CTA_ROC, mentor="B", series=SER, ep=8, next="കൂട്ടുകാരന്റെ പഴയ കമ്പനി", scene="office", theme="faq",
 cap_ml='AGM സെപ്റ്റംബർ 30-ന് ആണെങ്കിൽ AOC-4 ഒക്ടോബർ 30-നുള്ളിലും MGT-7 AGM കഴിഞ്ഞ് 60 ദിവസത്തിനുള്ളിലും. ROC ലേറ്റ് ഫീ ഓരോ ഫോമിനും ദിവസം 100 രൂപ, പരിധിയില്ല. സമയം ബാക്കിയുള്ള ഫോം ഇന്ന് തന്നെ ഫയൽ ചെയ്യൂ. നിങ്ങളുടെ MGT-7 ഫയൽ ചെയ്തോ?',
 cap_en='With the AGM on 30 September, AOC-4 is due by 30 October and MGT-7 within 60 days of the AGM. The ROC late fee is Rs 100 a day per form, with no cap. File the form that is still on time today. Is your MGT-7 filed?',
 cap_mg='AGM September 30-nu aanenkil AOC-4 October 30-nullilum MGT-7 AGM kazhinju 60 divasathinullilum. ROC late fee oro forminum divasam 100 roopa, parithiyilla. Samayam baakkiyulla form innu thanne file cheyyu. Ningalude MGT-7 file chetho?')

toon("rcx09", "dormant_company", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ", "C": "ഷഹീൻ"}, "\"എന്റെ പഴയ കമ്പനി\nഎടുത്തോ, പുതിയത്\nതുടങ്ങേണ്ട\"", [
 ("C", "മനോജേ, എന്റെ ഇവന്റ് കമ്പനി മൂന്ന് വർഷമായി വെറുതെ കിടക്കുന്നു. നീ അത് എടുത്ത് നിന്റെ ബിസിനസ് നടത്തിക്കോ."),
 ("A", "അപ്പൂപ്പാ, റെഡിമെയ്ഡ് കമ്പനി! ഇത് നല്ല ഡീൽ അല്ലേ?"),
 ("B", "ആദ്യം ചോദിക്ക്: മൂന്ന് വർഷം ഫയൽ ചെയ്തോ? ഇല്ലെങ്കിൽ ഡയറക്ടർമാർ 5 വർഷം അയോഗ്യരാകാം, കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം."),
 ("A", "ലേറ്റ് ഫീയോ?"),
 ("B", "ഓരോ ഫോമിനും ദിവസം 100 രൂപ, പരിധിയില്ല. ഫയൽ ചെയ്യാത്ത ഫോമുകൾ കമ്പനിക്കൊപ്പം നിന്റെ മേശയിലെത്തും.")],
 dict(title="പഴയ കമ്പനി എടുക്കും മുമ്പ്", rows=[("AOC-4, MGT-7", "എല്ലാ വർഷവും ഫയൽ ചെയ്തോ?"), ("ഡയറക്ടർ KYC", "സെപ്റ്റംബർ 30-നുള്ളിൽ?"), ("3 വർഷം ഫയലിംഗ് ഇല്ലെങ്കിൽ", "അയോഗ്യത, സ്ട്രൈക്ക് ഓഫ്")], total=("ലേറ്റ് ഫീ", "ഫോമിന് ദിവസം 100, പരിധിയില്ല")),
 ["ഏത് കമ്പനി ഏറ്റെടുക്കും മുമ്പും അതിന്റെ ഫയലിംഗ് ചരിത്രം നോക്കുക.", "വെറുതെ കിട്ടുന്ന കമ്പനിക്കും പഴയ കുടിശ്ശിക ഉണ്ടാകാം."],
 "പഴയ കമ്പനിക്കൊപ്പം\nപഴയ കുടിശ്ശികയും", topics.CTA_FILING, mentor="B", series=SER, ep=9, next="ഇനി ഉറങ്ങാതിരിക്കാൻ", scene="teashop", theme="faq",
 cap_ml='വെറുതെ കിട്ടുന്ന പഴയ കമ്പനി എടുക്കും മുമ്പ് ഫയലിംഗ് ചരിത്രം നോക്കൂ. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർ 5 വർഷം അയോഗ്യരാകാം, കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം, ലേറ്റ് ഫീ ഫോമിന് ദിവസം 100 രൂപ. ഈ ഓഫർ കിട്ടിയ കൂട്ടുകാരന് അയക്കൂ.',
 cap_en='Offered an old company for free? Check its filing history first. Three years of non-filing can disqualify its directors for 5 years and get the company struck off, and late fees run at Rs 100 a day per form. Send this to a friend who got such an offer.',
 cap_mg='Veruthe kittunna pazhaya company edukkum mumpu filing charithram nokku. 3 varsham file cheythillenkil directors 5 varsham ayogyaraakaam, company strike off aakaam, late fee formin divasam 100 roopa. Ee offer kittiya koottukaaranu ayakku.')

toon("rcx10", "dormant_company", "B", {"A": "മനോജ്", "B": "അപ്പൂപ്പൻ"}, "കമ്പനി ഉണർന്നു.\nഇനി ഉറങ്ങാതിരിക്കാൻ\nഎന്ത് ചെയ്യും?", [
 ("A", "അപ്പൂപ്പാ, പഴയ ഫോമുകൾ എല്ലാം ഫയൽ ചെയ്തു. ഇനി അടുത്ത വർഷം വീണ്ടും മറക്കാതിരിക്കാൻ എന്ത് ചെയ്യും?"),
 ("B", "ഒരു കലണ്ടർ. AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. അതിന് ശേഷം 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7."),
 ("A", "ഇനി ബിസിനസ് കുറഞ്ഞ വർഷം വന്നാലോ?"),
 ("B", "അപ്പോഴും എല്ലാം വേണം. ഓരോ ഡയറക്ടറുടെയും KYC-യും സെപ്റ്റംബർ 30-നുള്ളിൽ. ഓരോ തീയതിക്കും രണ്ടാഴ്ച മുമ്പ് ഫോണിൽ ഓർമ്മ.")],
 dict(title="മനോജിന്റെ പുതിയ കലണ്ടർ", rows=[("AGM", "സെപ്റ്റംബർ 30-നുള്ളിൽ"), ("AOC-4 / MGT-7", "AGM + 30 / + 60 ദിവസം"), ("DIR-3 KYC", "ഓരോ ഡയറക്ടറും, സെപ്റ്റംബർ 30")], total=("ബിസിനസ് ഇല്ലാത്ത വർഷവും", "എല്ലാം വേണം")),
 ["ഓരോ തീയതിക്കും രണ്ടാഴ്ച മുമ്പ് ഫോണിൽ റിമൈൻഡർ വെക്കുക.", "ഒരു ഫോം വൈകിയാൽ അന്ന് തന്നെ ഫയൽ ചെയ്യുക."],
 "കലണ്ടർ ഉണർന്നാൽ\nകമ്പനി ഉറങ്ങില്ല", topics.CTA_ROC, mentor="B", series=SER, ep=10, next="പുതിയ സീസൺ", scene="office", theme="faq",
 cap_ml='കമ്പനിക്ക് ഒരു ഫയലിംഗ് കലണ്ടർ: AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, AOC-4 AGM കഴിഞ്ഞ് 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ, ഓരോ ഡയറക്ടറുടെയും DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ. ബിസിനസ് ഇല്ലാത്ത വർഷവും എല്ലാം വേണം. നിങ്ങളുടെ ഫോണിൽ ഈ തീയതികൾ ഉണ്ടോ?',
 cap_en="A filing calendar for your company: AGM by 30 September, AOC-4 within 30 days of it, MGT-7 within 60 days, and every director's DIR-3 KYC by 30 September. All of it is due even in a year with no business. Are these dates in your phone?",
 cap_mg='Companykku oru filing calendar: AGM September 30-nullil, AOC-4 AGM kazhinju 30 divasathil, MGT-7 60 divasathil, oro directorudeyum DIR-3 KYC September 30-nullil. Business illaatha varshavum ellaam venam. Ningalude phone-il ee theeyathikal undo?')
