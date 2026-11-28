# kl tips 03 (28 Nov night): tip reels as duo3d scenes. theme="tip". Facts only from topics.FACTS_KL.
# Never a home-business rule, a penalty, a fee amount, a validity period or "renewed every year".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

# tip: three Shops Act myths in one go
duo("lct004", "no_staff_shop", "B", "textile", "ഷോപ്സ് ആക്ട്:\nആളുകൾ വിശ്വസിക്കുന്ന\n3 തെറ്റ്", [
 ("A","wide","പ്രകാശേട്ടാ, ഷോപ്സ് ആക്ടിനെ കുറിച്ച് കടക്കാർ പറയുന്ന മൂന്ന് തെറ്റ് ഞാൻ എണ്ണിവെച്ചു."),
 ("A","A","ഒന്ന്: 'സ്റ്റാഫ് ഇല്ലെങ്കിൽ വേണ്ട.' തെറ്റ്. ഒരാളും ഇല്ലാത്ത കടയും രജിസ്റ്റർ ചെയ്യണം."),
 ("V","V","രണ്ട്: 'GST-യോ FSSAI-യോ ഉണ്ടല്ലോ.' അവ രണ്ടും ഇതിന് പകരമല്ല."),
 ("A","A","മൂന്ന്: 'സൗകര്യം പോലെ ചെയ്യാം.' തുടങ്ങി 60 ദിവസത്തിനകം, തദ്ദേശ ലൈസൻസ് കോപ്പി വെച്ച്, ഓൺലൈനായി."),
 ("V","wide","സ്റ്റാഫ് ഇല്ലെങ്കിലും, GST ഉണ്ടെങ്കിലും, 60 ദിവസം.")],
 "സ്റ്റാഫ് ഇല്ലെങ്കിലും,\n60 ദിവസത്തിനകം", CTA_SHOPS, theme="tip",
 cap_ml="ഷോപ്സ് ആക്ടിനെ കുറിച്ചുള്ള 3 തെറ്റിദ്ധാരണ: സ്റ്റാഫ് ഇല്ലെങ്കിലും രജിസ്ട്രേഷൻ വേണം. GST-യും FSSAI-യും ഇതിന് പകരമല്ല. തുടങ്ങി 60 ദിവസത്തിനകം, തദ്ദേശ സ്ഥാപന ലൈസൻസ് കോപ്പി വെച്ച്, ഓൺലൈനായി ചെയ്യണം. ഇതിൽ ഏതാണ് നിങ്ങൾ കേട്ടിട്ടുള്ളത്?",
 cap_en="Three Shops Act myths in Kerala: no staff means no registration (wrong, even a shop with nobody employed registers); GST or FSSAI covers it (they don't); do it whenever (it's within 60 days of starting, online, with the local-body licence copy). Which one have you heard?",
 cap_mg="Shops Act-ine kurichulla 3 thettiddhaarana: staff illenkilum registration venam. GST-yum FSSAI-yum ithinu pakaramalla. Thudangi 60 divasathinakam, thadesha sthaapana licence copy vechu, online-aayi cheyyanam. Ithil ethaanu ningal kettittullathu?")

# tip: which paper goes to which office (local body licence, Shops Act on LCAS, professional tax to the local body)
duo("lct005", "new_shop", "B", "library", "കടയുടെ മൂന്ന് രേഖ:\nഏത് ആരുടെ അടുത്ത്?", [
 ("V","wide","ഗ്രീഷ്മേ, കടയുടെ ഓരോ രേഖയും ഏത് ഓഫീസിലാ എന്ന് ഒന്ന് പറഞ്ഞുതരാമോ?"),
 ("A","A","ട്രേഡ് ലൈസൻസ്: പഞ്ചായത്ത്, മുനിസിപ്പാലിറ്റി അല്ലെങ്കിൽ കോർപ്പറേഷൻ. നഗരങ്ങളിൽ K-SMART വഴി."),
 ("A","A","ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷനും പുതുക്കലും: ലേബർ കമ്മീഷണറേറ്റിന്റെ LCAS പോർട്ടലിൽ, ഓൺലൈനായി."),
 ("V","V","സ്റ്റാഫിന്റെ പ്രൊഫഷണൽ ടാക്സ്?"),
 ("A","A","തദ്ദേശ സ്ഥാപനത്തിലേക്ക്. ശമ്പളത്തിൽ നിന്ന് പിടിക്കുന്നത് തൊഴിലുടമ, വർഷം പരമാവധി 2,500 രൂപ."),
 ("V","wide","മൂന്ന് രേഖ, മൂന്ന് വഴി. ഇനി ഓടേണ്ടത് എങ്ങോട്ട് എന്ന് അറിയാം.")],
 "മൂന്ന് രേഖ,\nമൂന്ന് വഴി", CTA_KSMART, theme="tip",
 cap_ml="കടയുടെ രേഖകൾ ഏത് ഓഫീസിൽ? ട്രേഡ് ലൈസൻസ് പഞ്ചായത്ത് / മുനിസിപ്പാലിറ്റി / കോർപ്പറേഷനിൽ (നഗരങ്ങളിൽ K-SMART). ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷനും പുതുക്കലും LCAS പോർട്ടലിൽ ഓൺലൈനായി. പ്രൊഫഷണൽ ടാക്സ് തദ്ദേശ സ്ഥാപനത്തിലേക്ക്, തൊഴിലുടമ പിടിക്കുന്നു, വർഷം പരമാവധി 2,500 രൂപ. നിങ്ങൾക്ക് ഇതിൽ ഏതാണ് ബാക്കി?",
 cap_en="Which shop paper goes where in Kerala: the trade licence to the panchayat, municipality or corporation (K-SMART in towns); Shops Act registration and renewal online on the LCAS portal; professional tax to the local body, deducted by the employer, at most 2,500 rupees a year. Which one is still pending for you?",
 cap_mg="Kadayude rekhakal ethu office-il? Trade licence panchayat / municipality / corporation-il (nagarangalil K-SMART). Shops Act registration-um puthukkalum LCAS portal-il online-aayi. Professional tax thadesha sthaapanathilekku, thozhiludama pidikkunnu, varsham paramaavadhi 2,500 rupees. Ningalkku ithil ethaanu baakki?")
