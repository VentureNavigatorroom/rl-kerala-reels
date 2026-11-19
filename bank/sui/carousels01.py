# Startup India seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
car("uk001", "tech_founder", "ഗുണങ്ങൾ", "DPIIT കിട്ടിയാൽ\nശരിക്കും എന്ത്?", [
 ("IP ഇളവ്", "പേറ്റന്റ്, ട്രേഡ്മാർക്ക് അപേക്ഷകളിൽ സർക്കാർ ഇളവും വേഗത്തിലുള്ള പരിശോധനയും."),
 ("സെൽഫ് സർട്ടിഫിക്കേഷൻ", "ചില തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ."),
 ("സ്കീമുകൾ", "പല സർക്കാർ സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും യോഗ്യത."),
 ("ടാക്സ് ഹോളിഡേ", "അപേക്ഷിക്കാനുള്ള യോഗ്യത മാത്രം. അംഗീകാരം വേറെ.")],
 "ഗുണം അറിഞ്ഞ്\nഅപേക്ഷിക്കൂ", topics.CTA_BENEFITS,
 cap_ml="DPIIT സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷന്റെ ഗുണങ്ങൾ: പേറ്റന്റ്, ട്രേഡ്മാർക്ക് ഇളവുകൾ, സെൽഫ് സർട്ടിഫിക്കേഷൻ, സ്കീമുകൾക്ക് യോഗ്യത. ടാക്സ് ഹോളിഡേയ്ക്ക് വേറെ അംഗീകാരം വേണം.",
 cap_en="What DPIIT recognition really gives: government rebates and faster examination for patents and trademarks, self-certification under some labour and environment laws, eligibility for schemes and tenders. The 80-IAC tax holiday needs a separate approval.",
 cap_mg="DPIIT recognition-nte gunangal: patent, trademark ilavukal, self certification, schemes-nu eligibility. Tax holiday-kku vere approval venam.")
car("uk002", "grant_seeker", "യോഗ്യത", "DPIIT-ക്ക് നിങ്ങൾ\nയോഗ്യരാണോ?", [
 ("രൂപം", "Pvt Ltd, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്. പ്രൊപ്രൈറ്റർഷിപ്പിന് പറ്റില്ല."),
 ("പ്രായം", "രജിസ്റ്റർ ചെയ്ത് 10 വർഷത്തിൽ താഴെ."),
 ("ടേൺഓവർ", "ഒരു വർഷവും 200 കോടി കടന്നിട്ടില്ല."),
 ("പുതുമ", "പുതിയ പ്രോഡക്റ്റ്, പ്രോസസ് അല്ലെങ്കിൽ വളരുന്ന മോഡൽ.")],
 "എല്ലാം ശരിയാണോ?", topics.CTA_DPIIT,
 cap_ml="DPIIT സ്റ്റാർട്ടപ്പ് ഇന്ത്യ യോഗ്യത: Pvt Ltd, LLP അല്ലെങ്കിൽ രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്; 10 വർഷത്തിൽ താഴെ; 200 കോടി കടക്കാത്ത ടേൺഓവർ; പുതുമ.",
 cap_en="Are you eligible for DPIIT Startup India recognition? Pvt Ltd, LLP or registered partnership; under 10 years old; turnover never above Rs 200 crore; innovation or a scalable model.",
 cap_mg="DPIIT eligibility: Pvt Ltd, LLP, registered partnership; 10 varshathil thaazhe; 200 crore kadakkatha turnover; puthuma.")
