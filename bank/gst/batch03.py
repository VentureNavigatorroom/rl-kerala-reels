# GST seed batch 03 (19 Nov, backlog). Situations from bank/STORY_THEMES.md (anonymised; names and details invented).
# Facts only from topics.FACTS_GST. No prices, no fees, no company values. Hooks differ from batch01 and batch02.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd008", "trader", "A", "shop", "ഓണം കഴിഞ്ഞപ്പോൾ\nടേൺഓവർ 40 ലക്ഷം\nകടന്നു", [
 ("A","wide","സുരേഷേ, കണക്ക് നോക്കിയോ? ഈ വർഷം അരി കച്ചവടം 40 ലക്ഷം കടന്നു."),
 ("V","V","ബിനുവേ, ആ തുക കടയുടെ ആകെ വിൽപ്പനയല്ലേ? ഞാൻ ഇപ്പോഴും ചെറുതാണെന്ന് കരുതി."),
 ("A","A","കഴിഞ്ഞ വർഷത്തെയും ഇതേ തുകയെയും ചേർത്ത് നോക്കണം. ഗുഡ്സിന് 40 ലക്ഷം കടന്നാൽ GST നിർബന്ധം."),
 ("V","V","അപ്പോ നോട്ടീസ് വരുന്നതിന് മുമ്പ് ഞാൻ തന്നെ രജിസ്റ്റർ ചെയ്യണം."),
 ("A","wide","അതേ. കടന്ന ദിവസം മുതൽ ബില്ലിൽ GST ചേർക്കണം."),
 ("V","wide","കണക്ക് ആദ്യം, പിന്നെ ബില്ല്.")],
 "40 ലക്ഷം കടന്നാൽ\nGST കണക്ക് നോക്കൂ", CTA_GST, theme="faq",
 cap_ml="ഗുഡ്സ് വിൽപ്പന വർഷത്തിൽ 40 ലക്ഷം കടന്നാൽ GST രജിസ്ട്രേഷൻ നിർബന്ധം. നിങ്ങളുടെ ടേൺഓവർ ഇപ്പോൾ എത്രയുണ്ട്?",
 cap_en="A Kerala shop selling goods must register for GST once yearly turnover crosses 40 lakh rupees. Check your turnover before the next billing season: is it close to the limit?",
 cap_mg="Goods vilppana 40 lakh kadannaal GST registration nirbandham. Ningalude turnover ippol ethrayundu?")

duo("gd009", "online_seller", "A", "office", "കേരളത്തിനകത്ത്\nമാത്രം വിറ്റാൽ?\nഒരു നിയമം മാത്രം", [
 ("A","wide","രാഹുൽ, ഓൺലൈനിൽ സോപ്പ് വിൽക്കുന്ന കാര്യം. ലിമിറ്റിന് താഴെയാണ് നമ്മൾ."),
 ("V","V","നേഹ, GST വേണോ അതോ വേണ്ടേ? എല്ലാവരും ഒന്നിച്ച് പറയുന്നു വേണമെന്ന്."),
 ("A","A","2023 ഒക്ടോബർ മുതൽ ഒരു ഇളവുണ്ട്. ലിമിറ്റിന് താഴെ, കേരളത്തിനകത്ത് മാത്രം വിൽക്കുന്നവർക്ക് PAN അടിസ്ഥാനമാക്കിയ നമ്പർ മതി."),
 ("V","V","പക്ഷേ മാർക്കറ്റ്പ്ലേസ് ഈ സൗകര്യം നൽകണം. അതും പരിശോധിക്കണം."),
 ("A","wide","അതേ. മറ്റ് സംസ്ഥാനത്തേക്ക് അയച്ചാൽ ഈ ഇളവ് ബാധകമല്ല."),
 ("V","wide","കേരളത്തിനകത്ത് മാത്രമോ എന്ന് ആദ്യം ചോദിക്കൂ.")],
 "മറ്റ് സംസ്ഥാനത്തേക്ക് അയച്ചാൽ\nGST നിർബന്ധം", CTA_GST, theme="faq",
 cap_ml="കേരളത്തിനകത്ത് മാത്രം വിൽക്കുന്ന ചെറുകിട സെല്ലർമാർക്ക് PAN അടിസ്ഥാനമാക്കിയ എൻറോൾമെന്റ് മതിയാകാം. മറ്റ് സംസ്ഥാനത്തേക്ക് വിറ്റാൽ GST വേണം. നിങ്ങൾ ഏത് സംസ്ഥാനത്തേക്കാണ് അയക്കുന്നത്?",
 cap_en="A small seller who sells only inside Kerala may use a PAN-based enrolment, if the marketplace allows it. Sales to other states need GST. Do your orders ever go outside Kerala?",
 cap_mg="Kerala-kkakathu matram vilkkunna cheriya sellers-kku PAN based enrolment mathi. Pukarathu state-kku ayachaal GST venam. Ningal ethu state-kku ayakkunnu?")

duo("gd010", "service_pro", "B", "hotellobby", "കേരളത്തിന് പുറത്ത്\nജോലി ചെയ്യുമ്പോൾ\nബില്ലിൽ എന്ത്?", [
 ("A","wide","ജെയ്സാ, ബംഗളൂരുവിലെ ക്ലയന്റിന് സർവീസ് ബില്ല് അയച്ചു. GST ചേർക്കണോ?"),
 ("V","V","നീതൂ, സർവീസ് ആണെങ്കിൽ 20 ലക്ഷം വരെ ഇളവുണ്ടല്ലോ?"),
 ("A","A","അതേ. കേരളത്തിന് പുറത്തേക്കുള്ള സർവീസിന് 20 ലക്ഷം വരെ ഒഴിവുണ്ട്. കടന്നാൽ രജിസ്ട്രേഷൻ വേണം."),
 ("V","V","അപ്പോ വർഷാവസാനം കണക്ക് നോക്കിയാൽ മതി."),
 ("A","wide","മാസം തോറും നോക്കണം. മൊത്തം തുക ഒന്നിച്ച് കൂട്ടണം."),
 ("V","wide","ഒഴിവ് ആണെന്ന് ഉറപ്പാക്കിയ ശേഷം മാത്രം ബില്ല്.")],
 "സർവീസിന് 20 ലക്ഷം ഒഴിവ്\nകണക്ക് മുടക്കരുത്", CTA_GST, theme="new",
 cap_ml="കേരളത്തിന് പുറത്തേക്കുള്ള സർവീസിന് 20 ലക്ഷം വരെ GST ഇളവുണ്ട്. മാസം തോറും മൊത്തം തുക കൂട്ടി നോക്കണം. നിങ്ങളുടെ സർവീസ് വരുമാനം മാസം എത്രയാണ്?",
 cap_en="Inter-state services stay exempt up to 20 lakh rupees a year. Add up the total each month, not just at year end. How much service income do you book in a typical month?",
 cap_mg="Keralathinu purathulla service-nu 20 lakh vare GST ilavundu. Maasam thorum total koottanam. Ningalude service varumaanam maasam ethra?")

duo("gd011", "trader", "B", "bakery", "ഒരു B2B ക്ലയന്റ്\nGSTIN ചോദിച്ചു\nപിന്നെ എന്ത്?", [
 ("A","wide","സാബുച്ചേട്ടാ, ഹോട്ടൽ ക്ലയന്റ് GSTIN ഇല്ലാതെ ഓർഡർ തരില്ലെന്ന്."),
 ("V","V","ജിഷേ, ചെറിയ കടയ്ക്ക് GST നിർബന്ധമല്ലല്ലോ. പിന്നെ എന്തിന് രജിസ്റ്റർ?"),
 ("A","A","ആർക്കും സ്വമേധയാ രജിസ്റ്റർ ചെയ്യാം. ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് കിട്ടുന്നത് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം."),
 ("V","V","അപ്പോ ക്ലയന്റിന്റെ ടാക്സ് കുറയും, നമ്മുടെ ഓർഡറും കിട്ടും."),
 ("A","wide","അതെ. രണ്ടും നോക്കി തീരുമാനിക്കണം."),
 ("V","wide","ഓർഡർ വേണോ, സ്വമേധയാ വേണോ എന്ന് കണക്കാക്കൂ.")],
 "ക്ലയന്റ് GSTIN ചോദിച്ചാൽ\nസ്വമേധയാ രജിസ്റ്റർ ചെയ്യാം", CTA_GST, theme="new",
 cap_ml="ചെറിയ കച്ചവടക്കാർക്കും GST രജിസ്ട്രേഷൻ സ്വമേധയാ എടുക്കാം. ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രമാണ്. നിങ്ങളുടെ ക്ലയന്റുകൾ GSTIN ചോദിക്കാറുണ്ടോ?",
 cap_en="Anyone may register for GST voluntarily, and input tax credit is only for registered persons. Do your business clients ever ask for a GSTIN before ordering?",
 cap_mg="Cheriya kachavadakkarkkum GST registration swamedhayaa edukkam. Input tax credit registered persons-kku maathram. Ningalude clients GSTIN chodikkarundo?")

duo("gd012", "new_company", "B", "salon", "പുതിയ സലൂൺ\nജി.എസ്.ടി. കാത്തിരിപ്പ്\nഎത്ര ദിവസം?", [
 ("A","wide","വിനീതേ, ഓപ്പണിംഗ് അടുത്തു. GST അപേക്ഷ കൊടുത്തിട്ട് കുറെ ദിവസമായി."),
 ("V","V","സോണിയാ, ഇപ്പോ എന്തിന് ഇത്ര ടെൻഷൻ? മുൻപ് മാസങ്ങളെടുത്തല്ലോ."),
 ("A","A","ഈ നവംബർ മുതൽ കുറഞ്ഞ റിസ്ക് ഉള്ള അപേക്ഷകൾ മൂന്ന് പ്രവൃത്തി ദിവസത്തിനുള്ളിൽ ഓട്ടോ-അപ്രൂവ് ആകും."),
 ("V","V","അപ്പോ നമ്മുടെ അപേക്ഷ വേഗം തീരുമല്ലോ."),
 ("A","wide","അതെ, എല്ലാ രേഖയും ശരിയാണെങ്കിൽ."),
 ("V","wide","രേഖ ഒന്നുകൂടി നോക്കി സമർപ്പിക്കൂ.")],
 "മൂന്ന് പ്രവൃത്തി ദിവസത്തിൽ\nഅപ്രൂവൽ, രേഖ ശരിയാക്കൂ", CTA_GST, theme="new",
 cap_ml="കുറഞ്ഞ റിസ്ക് ഉള്ള GST അപേക്ഷകൾ 2025 നവംബർ മുതൽ മൂന്ന് പ്രവൃത്തി ദിവസത്തിനുള്ളിൽ ഓട്ടോ-അപ്രൂവ് ആകും. അപേക്ഷയിലെ രേഖകൾ ഒന്നുകൂടി പരിശോധിച്ചോ?",
 cap_en="Low-risk GST applications have been auto-approved within 3 working days since November 2025. Did you check every document before you submitted your application?",
 cap_mg="Low risk GST applications 2025 Nov muthal moonnu pravarthi divasathinullil auto-approve aakum. Application-ile rekhakal onnukoodi nokkiyo?")

duo("gd013", "trader", "A", "textile", "\"ഓൺലൈൻ ഓർഡർ\nമറ്റൊരു സംസ്ഥാനത്ത്\nഇന്നലെ\"", [
 ("A","wide","പ്രകാശേട്ടാ, ബെംഗളൂരുവിൽ നിന്ന് ഒരു ഓർഡർ. ഡെലിവറി ആ നഗരത്തിലേക്ക്."),
 ("V","V","രമ്യേ, ഞാൻ ചെറിയ കടയല്ലേ. ലിമിറ്റിന് താഴെ അല്ലേ?"),
 ("A","A","ലിമിറ്റ് ബാധകമല്ല. മറ്റൊരു സംസ്ഥാനത്തേക്ക് സാധനം അയച്ചാൽ GST വേണം."),
 ("V","V","ആദ്യ വിൽപ്പനയിൽ നിന്ന് തന്നെയോ?"),
 ("A","wide","അതെ. ഓൺലൈനിൽ ആണെങ്കിൽ ആദ്യ വിൽപ്പന മുതൽ."),
 ("V","wide","അയക്കുന്നതിന് മുമ്പ് രജിസ്ട്രേഷൻ ഉറപ്പാക്കൂ.")],
 "മറ്റൊരു സംസ്ഥാനത്തേക്ക്\nഅയച്ചാൽ ലിമിറ്റ് ബാധകമല്ല", CTA_GST, theme="faq",
 cap_ml="മറ്റൊരു സംസ്ഥാനത്തേക്കുള്ള സാധന വിൽപ്പനയ്ക്ക് വിൽപ്പന തുകയുടെ ലിമിറ്റ് ബാധകമല്ല. GST ആദ്യ വിൽപ്പന മുതൽ വേണം. നിങ്ങളുടെ ഓർഡറുകൾ ഏത് സംസ്ഥാനങ്ങളിലേക്കാണ്?",
 cap_en="For goods sent to another state, the turnover limit does not apply. GST is needed from the first sale. Which states do your orders go to?",
 cap_mg="Matta state-kku sadhanam ayachaal turnover limit baadhakamalla. GST aadya vilppana muthal venam. Ningalude orders etha state-kkaanu pokunnathu?")

duo("gd014", "trader", "B", "rubber", "കച്ചവടം കുറഞ്ഞ\nവർഷത്തിലും\nരജിസ്ട്രേഷൻ ഉണ്ടോ?", [
 ("A","wide","തോമസേ, ഈ വർഷം കച്ചവടം പാതിയായി. ഇനി GST അടയ്ക്കണോ?"),
 ("V","V","ജോയീ, അതിന് GST ഇല്ലാതെ തന്നെ നടക്കുമല്ലോ. കണക്ക് നോക്കാം."),
 ("A","A","ടേൺഓവർ കുറഞ്ഞാൽ രജിസ്ട്രേഷൻ തനിയെ ഇല്ലാതാകില്ല. പുതിയ വർഷത്തെ കണക്ക് നോക്കി തീരുമാനിക്കണം."),
 ("V","V","അപ്പോ മുൻ വർഷത്തിന്റെ കണക്ക് കൂടി വേണം."),
 ("A","wide","അതെ. രജിസ്റ്റർ ചെയ്തവരെ ബാധിക്കുന്ന റിട്ടേണുകളും ഉണ്ട്."),
 ("V","wide","തുടങ്ങുന്ന മാസം മുതൽ രേഖ സൂക്ഷിക്കൂ.")],
 "ടേൺഓവർ കുറഞ്ഞാലും\nറിട്ടേൺ തീരുമാനിക്കണം", CTA_GST, theme="faq",
 cap_ml="ടേൺഓവർ കുറഞ്ഞാലും GST രജിസ്ട്രേഷൻ തനിയെ റദ്ദാകില്ല. റിട്ടേണുകൾ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ രജിസ്ട്രേഷൻ ഉണ്ടോ?",
 cap_en="Falling turnover does not cancel your GST registration automatically, and returns still need filing. Are you registered right now?",
 cap_mg="Turnover kuranjaalum GST registration thaanee cancel aakilla. Returns file cheyyanam. Ningalkku registration undo?")

duo("gd015", "service_pro", "A", "weddinghall", "വിവാഹ ഓർഡർ\nകേരളത്തിന് പുറത്ത്.\nGST പറ്റുമോ?", [
 ("A","wide","ശരത്തേ, മംഗലാപുരത്തെ ഒരു വീട്ടിൽ ഫോട്ടോഗ്രാഫി ബുക്കിങ്. ബില്ല് എങ്ങനെ?"),
 ("V","V","കാവ്യേ, സർവീസ് ആണല്ലോ. ഇരുപത് ലക്ഷം കടന്നോ എന്ന് നോക്കണം."),
 ("A","A","കേരളത്തിന് പുറത്തേക്കുള്ള സർവീസ് ഇരുപത് ലക്ഷം വരെ ഒഴിവാണ്. അതിന് മുകളിൽ രജിസ്ട്രേഷൻ."),
 ("V","V","മുഴുവൻ വർഷത്തെ തുക ഒന്നിച്ചാണോ കൂട്ടേണ്ടത്?"),
 ("A","wide","അതെ. ഓരോ ബുക്കിങ്ങും വെവ്വേറെയല്ല, ആകെ."),
 ("V","wide","ബുക്കിങ് ലിസ്റ്റ് ഒരുമിച്ച് സൂക്ഷിക്കൂ.")],
 "ഓരോ ബുക്കിങ്ങും അല്ല,\nആകെ തുകയാണ് നോക്കേണ്ടത്", CTA_GST, theme="new",
 cap_ml="കേരളത്തിന് പുറത്തേക്കുള്ള സർവീസിന് 20 ലക്ഷം വരെ ഒഴിവുണ്ട്. ഓരോ ബുക്കിങ്ങും അല്ല, വർഷത്തെ ആകെ തുകയാണ് നോക്കേണ്ടത്. നിങ്ങളുടെ ബുക്കിങ് ലിസ്റ്റ് സൂക്ഷിക്കാറുണ്ടോ?",
 cap_en="Inter-state service income is exempt up to 20 lakh rupees, and the test is the yearly total, not each booking. Do you keep a list of all your bookings?",
 cap_mg="Keralathinu purathulla service-nu 20 lakh vare ilavundu. Oro booking-um alla, varshathe aakethuka nokkanam. Ningal booking list sookshikkarundo?")

duo("gd016", "online_seller", "B", "mobileshop", "\"ചെന്നൈയിൽ\nഓർഡർ വന്നു\nഇതാദ്യം\"", [
 ("A","wide","ഫഹദേ, ചെന്നൈയിൽ നിന്ന് ആദ്യ ഓർഡർ. ബില്ലിൽ എന്ത് ചേർക്കണം?"),
 ("V","V","ഹന്നേ, ഞാൻ ഇപ്പോഴും ചെറിയ സെല്ലറല്ലേ? ഇവിടത്തെ ഒഴിവ് ബാധകമല്ലേ?"),
 ("A","A","ഇല്ല. കേരളത്തിന് പുറത്തേക്ക് ഓൺലൈനിൽ അയച്ചാൽ GST ആദ്യ വിൽപ്പന മുതൽ വേണം."),
 ("V","V","അപ്പോ ഈ ഓർഡർ തന്നെ GST ഉള്ള ബില്ലിൽ."),
 ("A","wide","അതെ. രജിസ്ട്രേഷൻ ഇല്ലാതെ ഇന്റർസ്റ്റേറ്റ് ഓർഡർ വേണ്ട."),
 ("V","wide","ഇന്ന് തന്നെ രജിസ്ട്രേഷൻ തുടങ്ങൂ.")],
 "ചെന്നൈ ഓർഡർ ആദ്യമേ\nGST ബില്ലിൽ", CTA_GST, theme="new",
 cap_ml="കേരളത്തിന് പുറത്തേക്ക് ഓൺലൈനിൽ അയക്കുന്ന സാധനങ്ങൾക്ക് ആദ്യ വിൽപ്പന മുതൽ GST വേണം. രജിസ്ട്രേഷൻ ഇല്ലാതെ ഇന്റർസ്റ്റേറ്റ് ഓർഡർ അയക്കരുത്. നിങ്ങളുടെ ആദ്യ ഓർഡർ ഏത് സംസ്ഥാനത്തേക്ക്?",
 cap_en="Goods sent interstate from an online store need GST from the first sale. Do not ship an interstate order without registration. Which state was your first order sent to?",
 cap_mg="Keralathinu purathekku online-il ayakkunna sadhanangalkku aadya vilppana muthal GST venam. Ningalude aadya order etha state-kku?")

duo("gd017", "trader", "A", "farm", "ഒരു വർഷം കൊണ്ട്\nകച്ചവടം ഇരട്ടി.\nരജിസ്ട്രേഷൻ എവിടെ?", [
 ("A","wide","ഗോപീ, ഈ വർഷം കച്ചവടം ഇരട്ടിയായി. ഇനി നിയമം ബാധകമെന്ന് നീ പറയുന്നു."),
 ("V","V","വാസൂ, കണക്ക് നോക്കിയോ? ഇരുപത് ലക്ഷം കടന്നോ?"),
 ("A","A","ചരക്കിന് നാല്പത് ലക്ഷം കടന്നാൽ മാത്രം രജിസ്ട്രേഷൻ. സേവനമാണെങ്കിൽ ഇരുപത് ലക്ഷം."),
 ("V","V","ഞങ്ങളുടേത് ചരക്കാണ്, അപ്പോ നാല്പത് ലക്ഷം മാത്രം നോക്കിയാൽ മതി."),
 ("A","wide","അതെ. മിശ്രമാണെങ്കിൽ രണ്ടും നോക്കണം."),
 ("V","wide","കണക്ക് വേറെ വേറെ സൂക്ഷിക്കൂ.")],
 "ചരക്ക് 40 ലക്ഷം,\nസേവനം 20 ലക്ഷം", CTA_GST, theme="faq",
 cap_ml="ചരക്ക് വിൽപ്പനയ്ക്ക് 40 ലക്ഷം, സേവനത്തിന് 20 ലക്ഷം എന്നിങ്ങനെയാണ് കേരളത്തിലെ GST ലിമിറ്റ്. മിശ്ര ബിസിനസ് ആണെങ്കിൽ രണ്ടും വെവ്വേറെ നോക്കണം. നിങ്ങളുടേത് ചരക്കോ സേവനമോ?",
 cap_en="In Kerala the GST limit is 40 lakh for goods and 20 lakh for services. If you do both, track them separately. Is your business goods, services, or both?",
 cap_mg="Kerala-yil GST limit chararkku 40 lakh, sevanathinu 20 lakh. Randum undel vevvere nokkanam. Ningalude business chararkko sevanamo?")
