# Kerala licences tips 01 (27 Nov refill): tip reels as duo3d scenes (not lists). theme="tip". Facts only from topics.FACTS_KL. No prices, no penalties.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

duo("lct001", "new_shop", "B", "akshaya", "പുതിയ കട?\nലൈസൻസ് ക്രമം\n3 സ്റ്റെപ്പിൽ", [
 ("V","wide","സുധേ, പുതിയ കട തുടങ്ങുന്നവർക്ക് ഏത് ആദ്യം എന്ന് ഒറ്റ വാക്കിൽ പറ."),
 ("A","A","ഒന്ന്: പഞ്ചായത്ത്, മുനിസിപ്പാലിറ്റി അല്ലെങ്കിൽ കോർപ്പറേഷൻ ലൈസൻസ്. നഗരങ്ങളിൽ K-SMART വഴി."),
 ("A","A","രണ്ട്: ആ ലൈസൻസ് കോപ്പി വെച്ച് ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ, തുടങ്ങി 60 ദിവസത്തിനകം."),
 ("A","wide","മൂന്ന്: ഷോപ്സ് ആക്ട് എല്ലാ വർഷവും പുതുക്കുക. GST-യും FSSAI-യും ഇതിന് പകരമല്ല."),
 ("V","V","ക്രമം ഓർത്താൽ ഓട്ടം കുറയും.")],
 "ലൈസൻസ്, ഷോപ്സ് ആക്ട്,\nപുതുക്കൽ", CTA_KSMART, theme="tip",
 cap_ml="പുതിയ കടയ്ക്ക് ലൈസൻസ് ക്രമം: 1) തദ്ദേശ സ്ഥാപന ലൈസൻസ് (നഗരങ്ങളിൽ K-SMART). 2) ആ ലൈസൻസ് കോപ്പി വെച്ച് ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ, തുടങ്ങി 60 ദിവസത്തിനകം, സ്റ്റാഫ് ഇല്ലെങ്കിലും. 3) എല്ലാ വർഷവും പുതുക്കൽ. GST-യും FSSAI-യും ഇവയ്ക്ക് പകരമല്ല. നിങ്ങൾ ഏത് സ്റ്റെപ്പിലാണ്?",
 cap_en="Licence order for a new shop in Kerala: 1) the local-body licence (K-SMART in towns); 2) the Shops Act registration with that licence copy attached, within 60 days of starting, even with no staff; 3) renew the Shops Act registration every year. GST and FSSAI don't replace these. Which step are you on?",
 cap_mg="Puthiya kadakku licence kramam: 1) local body licence (nagarangalil K-SMART). 2) aa licence copy vechu Shops Act registration, thudangi 60 divasathinakam, staff illenkilum. 3) ella varshavum renewal. GST-yum FSSAI-yum ivakku pakaramalla. Ningal ethu step-il aanu?")

duo("lct002", "salaried_staff_kl", "B", "courier", "ആദ്യ സ്റ്റാഫിന്\nശമ്പളം കൊടുക്കും മുമ്പ്\nഈ ഒറ്റ ചെക്ക്", [
 ("A","wide","അരവിന്ദേ, കൊറിയർ ഓഫീസിൽ ആദ്യ സ്റ്റാഫിന് നാളെ ശമ്പളം. പ്രൊഫഷണൽ ടാക്സ് ഓർമ്മയുണ്ടോ?"),
 ("V","V","അത് സ്റ്റാഫ് തന്നെ അടച്ചോളില്ലേ, ജയേ?"),
 ("A","A","ഇല്ല. തൊഴിലുടമ ശമ്പളത്തിൽ നിന്ന് പിടിക്കണം, തദ്ദേശ സ്ഥാപനത്തിൽ അടയ്ക്കണം. പരമാവധി വർഷം 2,500 രൂപ."),
 ("V","V","അപ്പോ ശമ്പള സ്ലിപ്പിൽ അത് വേറെ കാണിക്കാം."),
 ("A","wide","പിടിച്ചാൽ മാത്രം പോരാ, അടയ്ക്കണം.")],
 "പിടിക്കുക,\nഅടയ്ക്കുക, കാണിക്കുക", CTA_SHOPS, theme="tip",
 cap_ml="ആദ്യ സ്റ്റാഫിനെ എടുത്തോ? കേരളത്തിൽ പ്രൊഫഷണൽ ടാക്സ് തൊഴിലുടമ ശമ്പളത്തിൽ നിന്ന് പിടിച്ച് തദ്ദേശ സ്ഥാപനത്തിൽ അടയ്ക്കണം. പരമാവധി വർഷം 2,500 രൂപ (2024 ഒക്ടോബർ 1-ന് പുതുക്കിയ നിരക്ക്). ശമ്പള സ്ലിപ്പിൽ വേറെ കാണിക്കുക. നിങ്ങൾ ആദ്യ ശമ്പളം കൊടുത്തോ?",
 cap_en="Hired your first staff member? In Kerala the employer deducts professional tax from salary and pays it to the local body; the maximum is Rs 2,500 a year (rates revised 1 Oct 2024). Show it as a separate line on the pay slip. Have you paid your first salary yet?",
 cap_mg="Aadya staff-ine eduttho? Kerala-yil professional tax employer salary-il ninnu pidichu local body-il adakkanam. Paramavadhi varsham 2,500 roopa (2024 October 1-nu puthukkiya nirakku). Salary slip-il vere kaanikkuka. Ningal aadya salary koduttho?")
