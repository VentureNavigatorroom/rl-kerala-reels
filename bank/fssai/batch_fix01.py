# FSSAI correction (24 Nov): our reels quoted the old Rs 12 lakh / Rs 20 crore limits and 1-5 year validity.
# From 1 Apr 2026 (amendment regulations, gazette 10 Mar 2026; FSSAI order 13 Mar 2026): registration up to Rs 1.5 crore,
# state licence above that up to Rs 50 crore, central above Rs 50 crore; perpetual validity. A follower pointed it out.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.toon, _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# Thank-you + correction as a collab with the follower who corrected us (owner, 24 Nov). He is named, not drawn.
toon("fsfix02", "cafe_owner", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ"}, "@rishad_pkr\nഞങ്ങളെ തിരുത്തി.\nനന്ദി!", [
 ("A", "അമ്മൂമ്മേ, നമ്മുടെ FSSAI റീലിൽ ഒരു ഫോളോവർ തെറ്റ് ചൂണ്ടിക്കാണിച്ചു!"),
 ("B", "എന്താ പറഞ്ഞത്?"),
 ("A", "2026 ഏപ്രിൽ മുതൽ 1.5 കോടി വരെ ടേൺഓവറിന് രജിസ്ട്രേഷൻ മതി എന്ന്."),
 ("B", "ശരിയാണ്. FSSAI-യുടെ ഉത്തരവ് ഞാൻ നോക്കി. റിഷാദിന് വലിയ നന്ദി!")],
 dict(title="FSSAI: 2026 ഏപ്രിൽ 1 മുതൽ", rows=[("1.5 കോടി വരെ", "രജിസ്ട്രേഷൻ"), ("1.5 - 50 കോടി", "സ്റ്റേറ്റ് ലൈസൻസ്"), ("50 കോടിക്ക് മുകളിൽ", "സെൻട്രൽ")], total=("സാധുത", "ഇനി സ്ഥിരം")),
 ["തെറ്റ് കണ്ടാൽ കമന്റ് ചെയ്യൂ. ഞങ്ങൾ തിരുത്തും.", "ഇംപോർട്ട് ചെയ്യുന്നവർക്ക് എപ്പോഴും സെൻട്രൽ ലൈസൻസ്."],
 "തിരുത്തിയതിന്\nനന്ദി, റിഷാദ്", topics.CTA_FSSAI, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", scene="shop",
 theme="correction", corrects="fsx04", collab=["rishad_pkr"],
 source="https://www.fssai.gov.in/upload/advisories/2026/03/69c6a23234827order_27032026.pdf", as_of="2026-03-13", expires="2027-03-31",
 cap_en="Thank you @rishad_pkr for correcting us! Since 1 April 2026, FSSAI registration covers turnover up to Rs 1.5 crore (it was Rs 12 lakh), a state licence covers Rs 1.5 crore to Rs 50 crore, and a central licence is above Rs 50 crore (importers always need central). Registrations and licences no longer need renewal. Spot something wrong? Comment and we'll fix it.",
 cap_ml="തിരുത്തിയതിന് @rishad_pkr-ന് നന്ദി! 2026 ഏപ്രിൽ 1 മുതൽ 1.5 കോടി വരെ ടേൺഓവറിന് FSSAI രജിസ്ട്രേഷൻ മതി (മുമ്പ് 12 ലക്ഷം). 1.5 മുതൽ 50 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്, 50 കോടിക്ക് മുകളിൽ സെൻട്രൽ. ലൈസൻസ് ഇനി പുതുക്കേണ്ട.",
 cap_mg="Thiruthiyathinu @rishad_pkr-nu nanni! 2026 April 1 muthal 1.5 crore vare turnover-inu FSSAI registration mathi (munpu 12 lakh). 1.5 muthal 50 crore vare State licence, 50 crore-nu mukalil Central. Licence ini renew cheyyendathilla.")

# Follow-up Q&A (25 Nov): @rishad_pkr asked whether licences still need renewal. Perpetual validity is clear only for
# licences issued on or after 1 Apr 2026 (FSSAI FAQ Q12); older ones: check expiry on FoSCoS. Annual fee continues (Q5).
toon("fsfix03", "cafe_owner", "B", {"A": "സുമ", "B": "അമ്മൂമ്മ"}, "@rishad_pkr ചോദിച്ചു:\nലൈസൻസ്\nപുതുക്കണോ?", [
 ("A", "അമ്മൂമ്മേ, ലൈസൻസ് ഇനി പുതുക്കേണ്ടേ എന്ന് റിഷാദ് വീണ്ടും ചോദിച്ചു."),
 ("B", "നല്ല ചോദ്യം. ലൈസൻസ് എപ്പോൾ കിട്ടി എന്ന് നോക്കണം."),
 ("A", "എന്റേത് പഴയതാ. രണ്ട് വർഷം മുമ്പ് എടുത്തത്."),
 ("B", "എങ്കിൽ FoSCoS-ൽ കാലാവധി തീയതി നോക്കി സമയത്ത് പുതുക്കുന്നതാണ് സുരക്ഷിതം.")],
 dict(title="FSSAI: പുതുക്കണോ?", rows=[("2026 ഏപ്രിൽ മുതൽ കിട്ടിയത്", "പുതുക്കൽ വേണ്ട"), ("അതിന് മുമ്പ് കിട്ടിയത്", "തീയതി നോക്കുക"), ("FSSAI വാർഷിക അടവ്", "തുടരും")], total=("വാർഷിക അടവ്", "വർഷങ്ങൾ ഒരുമിച്ച്")),
 ["പഴയ ലൈസൻസ് ആണെങ്കിൽ FoSCoS-ൽ കാലാവധി നോക്കുക.", "FSSAI-ക്കുള്ള വാർഷിക അടവ് മുടക്കരുത്."],
 "ചോദിച്ചതിന് നന്ദി,\nറിഷാദ്", topics.CTA_FOOD, mentor="B", series="സുമയുടെ ഹോം ബേക്കറി", scene="shop",
 theme="correction", corrects="fsy02", collab=["rishad_pkr"],
 source="https://www.fssai.gov.in/upload/advisories/2026/03/69c6a23234827order_27032026.pdf", as_of="2026-03-27", expires="2027-03-31",
 cap_en="@rishad_pkr asked: does an FSSAI licence still need renewal? FSSAI's FAQ says licences and registrations issued on or after 1 April 2026 have perpetual validity, so no renewal. For older licences the FAQ isn't explicit, so check the expiry date on FoSCoS and renew on time. In every case the yearly payment to FSSAI continues, and you can pay several years at once. Thanks Rishad!",
 cap_ml="@rishad_pkr ചോദിച്ചു: FSSAI ലൈസൻസ് പുതുക്കണോ? 2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ ലൈസൻസിന് സ്ഥിരം സാധുത, പുതുക്കൽ വേണ്ട. പഴയ ലൈസൻസ് ആണെങ്കിൽ FoSCoS-ൽ കാലാവധി നോക്കി സമയത്ത് പുതുക്കുക. FSSAI-ക്കുള്ള വാർഷിക അടവ് എല്ലാവർക്കും തുടരും, വർഷങ്ങൾ ഒരുമിച്ച് അടയ്ക്കാം. നന്ദി റിഷാദ്!",
 cap_mg="@rishad_pkr chodichu: FSSAI licence renew cheyyano? 2026 April 1 muthal kittiya licence-inu perpetual validity, renew venda. Pazhaya licence aanel FoSCoS-il expiry nokki samayathu renew cheyyuka. FSSAI-kkulla annual payment ellavarkkum thudarum, varshangal orumichu adakkam. Nanni Rishad!")
