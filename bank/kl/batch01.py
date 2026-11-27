# Kerala licences batch 01 (27 Nov refill): first 3D duo reels for kl. Max 6 lines, painful moment first, payoff by line 4-5.
# Names, sectors and towns invented. Facts only from topics.FACTS_KL. No prices, no penalties, no home-business rules.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

# faq: one-woman tailoring unit, day 50, thinks Shops Act is only for shops with workers
duo("lcd001", "no_staff_shop", "B", "tailor", "കട തുടങ്ങിയിട്ട് 50 ദിവസം.\nഷോപ്സ് ആക്ട്?\n\"അത് എനിക്കല്ല\"", [
 ("A","wide","മോഹനേട്ടാ, ബ്ലൗസ് സ്റ്റിച്ചിംഗ് യൂണിറ്റ് തുടങ്ങിയിട്ട് 50 ദിവസമായി. ഞാൻ ഒറ്റയ്ക്കാ, പണിക്കാർ ഇല്ല."),
 ("V","V","ഉഷേ, ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ ചെയ്തോ?"),
 ("A","A","അത് പണിക്കാരുള്ള വലിയ കടകൾക്കല്ലേ?"),
 ("V","wide","അല്ല. കേരളത്തിൽ ഒരാളും ഇല്ലാത്ത കടയും രജിസ്റ്റർ ചെയ്യണം. തുടങ്ങി 60 ദിവസത്തിനകം, ഓൺലൈനായി. നിനക്ക് ഇനി 10 ദിവസം."),
 ("A","A","അപ്പോ ഇന്ന് തന്നെ തുടങ്ങാം."),
 ("V","wide","തയ്യൽ അളവ് നോക്കി, നിയമം ദിവസം നോക്കി.")],
 "ഒറ്റയ്ക്കാണെങ്കിലും\n60 ദിവസത്തിനകം", CTA_SHOPS, theme="faq",
 cap_ml="സ്റ്റാഫ് ഇല്ലാത്ത കടയ്ക്ക് ഷോപ്സ് ആക്ട് വേണ്ട എന്ന് കരുതിയോ? കേരള ഷോപ്സ് ആൻഡ് കൊമേഴ്സ്യൽ എസ്റ്റാബ്ലിഷ്മെന്റ്സ് ആക്ട് പ്രകാരം ജോലിക്കാരുടെ എണ്ണം നോക്കാതെ (ഒരാളും ഇല്ലെങ്കിലും) ഓരോ കടയും തുടങ്ങി 60 ദിവസത്തിനകം ഓൺലൈനായി രജിസ്റ്റർ ചെയ്യണം. നിങ്ങളുടെ കട തുടങ്ങിയിട്ട് എത്ര ദിവസമായി?",
 cap_en="A one-woman tailoring unit, 50 days old, thinks the Shops Act is only for shops with staff. In Kerala every shop and commercial establishment registers under the Shops and Commercial Establishments Act whatever the number of workers, even none, online, within 60 days of starting. How many days since you opened?",
 cap_mg="Staff illaatha kadakku Shops Act venda ennu karuthiyo? Kerala Shops and Commercial Establishments Act prakaaram joli-kkaarude ennam nokkaathe (aarum illenkilum) oro kadayum thudangi 60 divasathinakam online aayi register cheyyanam. Ningalude kada thudangiyittu ethra divasamaayi?")

# new: photocopy shop applied for Shops Act first, stuck at the licence-copy field
duo("lcd002", "new_shop", "B", "photocopy", "ഷോപ്സ് ആക്ട് ഫോം\nപാതിയിൽ നിന്നു.\nഒരു കോപ്പി ഇല്ല!", [
 ("A","wide","ഉണ്ണീ, ഷോപ്സ് ആക്ട് അപേക്ഷ പൂരിപ്പിക്കുവായിരുന്നു. ഒരു ഫീൽഡിൽ കുടുങ്ങി: ലൈസൻസ് കോപ്പി."),
 ("V","V","ഏത് ലൈസൻസ്? നമ്മൾ ഇതുവരെ ഒന്നും എടുത്തില്ലല്ലോ, അശ്വതീ."),
 ("A","A","അതാ പ്രശ്നം. പഞ്ചായത്തിന്റെ ലൈസൻസ് കോപ്പി അതിനൊപ്പം വെക്കണം."),
 ("V","wide","അപ്പോ ക്രമം ഇതാണ്: ആദ്യം തദ്ദേശ സ്ഥാപന ലൈസൻസ്, പിന്നെ അതിന്റെ കോപ്പി വെച്ച് ഷോപ്സ് ആക്ട്."),
 ("A","A","ഫോട്ടോകോപ്പി കടക്കാർക്ക് തന്നെ കോപ്പി ഇല്ല!"),
 ("V","wide","ക്രമം തെറ്റിയാൽ ഫോം നിൽക്കും.")],
 "ആദ്യം ലൈസൻസ്,\nപിന്നെ ഷോപ്സ് ആക്ട്", CTA_KSMART, theme="new",
 cap_ml="ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷന് തദ്ദേശ സ്ഥാപനത്തിന്റെ (പഞ്ചായത്ത് / മുനിസിപ്പാലിറ്റി / കോർപ്പറേഷൻ) ലൈസൻസ് കോപ്പി വെക്കണം. അതുകൊണ്ട് ക്രമം: ആദ്യം തദ്ദേശ ലൈസൻസ്, നഗരങ്ങളിൽ K-SMART വഴി; പിന്നെ ഷോപ്സ് ആക്ട്, കട തുടങ്ങി 60 ദിവസത്തിനകം. നിങ്ങൾ ഏത് സ്റ്റെപ്പിലാണ്?",
 cap_en="A photocopy shop starts the Shops Act form and gets stuck at one field: the licence copy. The Shops Act registration needs the local-body licence (panchayat, municipality or corporation; K-SMART in towns) attached, so the order is local-body licence first, then the Shops Act within 60 days of starting. Which step are you on?",
 cap_mg="Shops Act registration-inu local body (panchayat / municipality / corporation) licence copy vekkanam. Athukondu kramam: aadyam local body licence, nagarangalil K-SMART vazhi; pinne Shops Act, kada thudangi 60 divasathinakam. Ningal ethu step-il aanu?")

# faq: bakery owner thinks the FSSAI number covers everything
duo("lcd003", "new_shop", "A", "bakery", "FSSAI നമ്പർ ബോർഡിൽ.\nപഞ്ചായത്ത് ലൈസൻസ്?\n\"അത് വേണോ?\"", [
 ("A","wide","സാബുച്ചേട്ടാ, ബേക്കറിയുടെ ബോർഡിൽ FSSAI നമ്പർ വലുതായി എഴുതി. ഇനി എല്ലാം ആയി."),
 ("V","V","ജിഷേ, പഞ്ചായത്തിന്റെ ലൈസൻസ് എടുത്തോ? ഷോപ്സ് ആക്ട്?"),
 ("A","A","FSSAI ഉണ്ടല്ലോ, അത് തന്നെ ലൈസൻസ് അല്ലേ?"),
 ("V","wide","അല്ല. FSSAI ഭക്ഷണത്തിനാണ്. കടയ്ക്ക് തദ്ദേശ സ്ഥാപന ലൈസൻസും ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷനും വേറെ വേണം. GST-യും പകരമല്ല."),
 ("A","A","ഒരു നമ്പർ കൊണ്ട് മൂന്ന് പണി നടക്കില്ല."),
 ("V","wide","കേക്കിന് FSSAI, കടയ്ക്ക് ലൈസൻസ്.")],
 "FSSAI ഭക്ഷണത്തിന്,\nലൈസൻസ് കടയ്ക്ക്", CTA_SHOPS, theme="faq",
 cap_ml="FSSAI ഉണ്ടെങ്കിൽ വേറെ ലൈസൻസ് വേണ്ട എന്ന് കരുതിയോ? FSSAI-യും GST-യും തദ്ദേശ സ്ഥാപന ലൈസൻസിനും ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷനും പകരമാകില്ല. കട നടത്തുന്ന സ്ഥലത്തിന് പഞ്ചായത്ത് / മുനിസിപ്പാലിറ്റി / കോർപ്പറേഷൻ ലൈസൻസ്, പിന്നെ ഷോപ്സ് ആക്ട്. നിങ്ങളുടെ കടയ്ക്ക് ഇതിൽ ഏതൊക്കെ ഉണ്ട്?",
 cap_en="A bakery owner paints the FSSAI number on the board and thinks the paperwork is done. FSSAI and GST do not replace the local-body licence (panchayat, municipality or corporation) or the Shops Act registration; the business place needs those too. Which of these does your shop have?",
 cap_mg="FSSAI undenkil vere licence venda ennu karuthiyo? FSSAI-yum GST-yum local body licence-num Shops Act registration-num pakaramaakilla. Kada nadathunna sthalathinu panchayat / municipality / corporation licence, pinne Shops Act. Ningalude kadakku ithil ethokke undu?")

# crm (#26 Gulf returnee): mobile shop, registered last year, forgot the yearly renewal
duo("lcd004", "town_business", "B", "mobileshop", "ഗൾഫിൽ ട്രേഡ് ലൈസൻസ്\nഎല്ലാ വർഷവും പുതുക്കി.\nനാട്ടിൽ മറന്നു", [
 ("A","wide","ഫഹദേ, നിന്റെ മൊബൈൽ ഷോപ്പിന് ഒരു വയസ്സായി. ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ പുതുക്കിയോ?"),
 ("V","V","ഹന്നാ, ദുബായിൽ പത്ത് കൊല്ലം കമ്പനിയുടെ ട്രേഡ് ലൈസൻസ് പുതുക്കിയത് ഞാനാ. ഇവിടെ ഒരിക്കൽ എടുത്താൽ മതിയെന്ന് കരുതി."),
 ("A","A","ഇവിടെയും അതേ ശീലം വേണം. ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ എല്ലാ വർഷവും പുതുക്കണം."),
 ("V","V","അപ്പോ പഞ്ചായത്ത് ലൈസൻസിന്റെ തീയതിയും ഒന്ന് നോക്കട്ടെ."),
 ("A","wide","ഗൾഫിലെ ശീലം നാട്ടിലും കൊണ്ടുവാ.")],
 "എല്ലാ വർഷവും\nപുതുക്കൽ, ഓർമ്മയുണ്ടോ?", CTA_SHOPS, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് വന്ന് നാട്ടിൽ കട തുടങ്ങിയോ? കേരളത്തിൽ ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ ഒരിക്കൽ എടുത്താൽ തീരില്ല, എല്ലാ വർഷവും പുതുക്കണം. തദ്ദേശ സ്ഥാപന ലൈസൻസിന്റെ കാലാവധി തീയതിയും നോക്കി വെക്കുക. നിങ്ങളുടെ കടയുടെ പുതുക്കൽ തീയതി ഓർമ്മയുണ്ടോ?",
 cap_en="A Gulf returnee renewed his employer's trade licence every year abroad, then assumed his Kerala mobile shop's registration was one-time. The Shops Act registration in Kerala is renewed every year; check your local-body licence's date too. Do you know your shop's renewal date?",
 cap_mg="Gulf-il ninnu vannu naattil kada thudangiyo? Kerala-yil Shops Act registration orikkal eduthaal theerilla, ella varshavum puthukkanam. Local body licence-inte expiry date-um nokki vekkuka. Ningalude kadayude renewal date ormayundo?")

# new: stylist sees a deduction on her slip and asks why
duo("lcd005", "salaried_staff_kl", "B", "salon", "ശമ്പള സ്ലിപ്പിൽ\nഒരു പിടുത്തം.\n\"ഇതെന്താ ചേട്ടാ?\"", [
 ("A","wide","വിനീതേട്ടാ, ഈ മാസത്തെ ശമ്പള സ്ലിപ്പിൽ പ്രൊഫഷണൽ ടാക്സ് എന്ന് ഒരു പിടുത്തം. ഇത് സലൂണിന്റെ ലാഭത്തിനാണോ?"),
 ("V","V","അല്ല സോണിയ. ഇത് നിയമമാണ്. ശമ്പളത്തിൽ നിന്ന് പിടിച്ച് തദ്ദേശ സ്ഥാപനത്തിൽ അടയ്ക്കേണ്ടത് തൊഴിലുടമയായ ഞാനാണ്."),
 ("A","A","എത്ര വരെ പിടിക്കാം?"),
 ("V","wide","പരമാവധി വർഷം 2,500 രൂപ. 2024 ഒക്ടോബറിൽ നിരക്ക് പുതുക്കി. രസീത് ഞാൻ കാണിച്ചുതരാം."),
 ("A","A","പിടിച്ചതിന് രസീതുണ്ടെങ്കിൽ സംശയമില്ല.")],
 "പിടിക്കുന്നത് ഉടമ,\nഅടയ്ക്കുന്നത് പഞ്ചായത്തിൽ", CTA_SHOPS, theme="new",
 cap_ml="ശമ്പള സ്ലിപ്പിൽ പ്രൊഫഷണൽ ടാക്സ് കണ്ട് സംശയിച്ചോ? കേരളത്തിൽ തൊഴിലുടമ ശമ്പളത്തിൽ നിന്ന് പ്രൊഫഷണൽ ടാക്സ് പിടിച്ച് തദ്ദേശ സ്ഥാപനത്തിൽ അടയ്ക്കണം. പരമാവധി വർഷം 2,500 രൂപ; നിരക്ക് 2024 ഒക്ടോബർ 1-ന് പുതുക്കി. നിങ്ങളുടെ കടയിൽ സ്റ്റാഫ് എത്ര പേരുണ്ട്?",
 cap_en="A salon stylist spots a professional tax deduction on her pay slip and asks if it's the owner's cut. In Kerala the employer deducts professional tax from salary and pays it to the local body; the maximum is Rs 2,500 a year, rates revised on 1 Oct 2024. How many staff do you have?",
 cap_mg="Salary slip-il professional tax kandu samshayicho? Kerala-yil employer salary-il ninnu professional tax pidichu local body-il adakkanam. Paramavadhi varsham 2,500 roopa; nirakku 2024 October 1-nu puthukki. Ningalude kadayil staff ethra perundu?")
