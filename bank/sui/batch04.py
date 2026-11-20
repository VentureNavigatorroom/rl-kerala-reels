# Startup India / DPIIT batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_SUI. No promises of approval or benefits. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

duo("ud030", "tech_founder", "A", "bakery", "\"ആദ്യ 3 വർഷം നഷ്ടം.\nടാക്സ് ഹോളിഡേ\nപാഴായോ?\"", [
 ("A","wide","സാബൂ, നമ്മുടെ ബേക്കറി വേസ്റ്റ് കുറയ്ക്കുന്ന ആപ്പിന് DPIIT കിട്ടി. പക്ഷേ ആദ്യ മൂന്ന് വർഷവും നഷ്ടം തന്നെ."),
 ("V","V","ജിഷേ, അപ്പോ ടാക്സ് ഹോളിഡേ പാഴായി. നഷ്ടത്തിന് എന്ത് ഇളവ്?"),
 ("A","A","ആദ്യ മൂന്ന് വർഷം തന്നെ എടുക്കണമെന്ന് ആരാ പറഞ്ഞേ?"),
 ("A","wide","80-IAC: ആദ്യ പത്ത് വർഷത്തിനുള്ളിൽ തുടർച്ചയായ ഏതെങ്കിലും 3 വർഷം, ലാഭത്തിന്റെ 100 ശതമാനം."),
 ("V","V","അതും DPIIT-നൊപ്പം തനിയെ വരില്ലല്ലോ, ബോർഡിന് വേറെ അപേക്ഷ."),
 ("A","wide","അതേ. ഹോളിഡേ കലണ്ടർ നോക്കിയല്ല, ലാഭം നോക്കി.")],
 "ഹോളിഡേ കലണ്ടർ നോക്കിയല്ല,\nലാഭം നോക്കി", CTA_BENEFITS, theme="crm",
 cap_ml="സ്റ്റാർട്ടപ്പിന്റെ ആദ്യ വർഷങ്ങൾ നഷ്ടത്തിലാണെങ്കിൽ 80-IAC ടാക്സ് ഹോളിഡേ പാഴാകുമോ? ആദ്യ പത്ത് വർഷത്തിനുള്ളിൽ തുടർച്ചയായ ഏതെങ്കിലും 3 വർഷമാണ്; അത് ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡിന്റെ വേറെ അപേക്ഷയുമാണ്. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ് ഇപ്പോൾ: ലാഭമോ നഷ്ടമോ?",
 cap_en="Is the 80-IAC tax holiday wasted if a startup makes losses in its first years? It covers any 3 consecutive years out of the first 10, and it is a separate application to the Inter-Ministerial Board, not automatic with DPIIT recognition. Your startup right now: profit or loss?",
 cap_mg="Startup-nte aadya varshangal nashtathilaanenkil 80-IAC tax holiday paazhaakumo? Aadya 10 varshathinullil thudarchayaaya ethenkilum 3 varsham; athu Inter-Ministerial Board-nu vere apekshayumaanu. Ningalude startup ippol: laabhamo nashtamo?")

duo("ud031", "traditional_innovator", "B", "textile", "പാർട്ണർഷിപ്പിന്\nDPIIT കിട്ടി.\nടാക്സ് ഹോളിഡേയും?", [
 ("A","wide","പ്രകാശേ, നമ്മുടെ പ്രകൃതി ചായം ഉറപ്പിക്കുന്ന പുതിയ രീതിക്ക് ഫേമിന് DPIIT റെക്കഗ്നിഷൻ കിട്ടി!"),
 ("V","V","രമ്യേ, ഇനി മൂന്ന് വർഷം ലാഭത്തിന് ടാക്സ് വേണ്ടല്ലോ. ഞാൻ ഇപ്പഴേ കാർ ബുക്ക് ചെയ്യാം."),
 ("A","A","ബ്രേക്ക് ഇട്. നമ്മൾ രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് ഫേം ആണ്."),
 ("V","V","അതിനെന്താ? റെക്കഗ്നിഷൻ കിട്ടിയല്ലോ."),
 ("A","wide","റെക്കഗ്നിഷൻ ഫേമിനും കിട്ടും. പക്ഷേ 80-IAC ടാക്സ് ഹോളിഡേ പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കും, അതും വേറെ അപേക്ഷ."),
 ("V","wide","അപ്പോ ആദ്യം കാർ അല്ല, ഘടന.")],
 "ആദ്യം ഘടന,\nപിന്നെ ഹോളിഡേ", CTA_BENEFITS, theme="crm",
 cap_ml="രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് ഫേമിന് DPIIT റെക്കഗ്നിഷൻ കിട്ടാം. പക്ഷേ 80-IAC ടാക്സ് ഹോളിഡേ പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കുമാണ്, അതും വേറെ അപേക്ഷ. നിങ്ങളുടെ ബിസിനസ്: ഫേമോ കമ്പനിയോ?",
 cap_en="A registered partnership firm making sarees with a new natural-dye fixing process got DPIIT recognition and assumed the tax holiday came with it. Recognition is open to registered partnerships, but the 80-IAC tax holiday is for a Pvt Ltd or LLP, and it is a separate application. Your business: firm or company?",
 cap_mg="Registered partnership firm-nu DPIIT recognition kittaam. Pakshe 80-IAC tax holiday Pvt Ltd-num LLP-kkum aanu, athum vere apeksha. Ningalude business: firm-o company-o?")

duo("ud032", "traditional_innovator", "C", "fishmarket", "\"സൊസൈറ്റിക്ക്\nസ്റ്റാർട്ടപ്പ് ആകാമോ?\"\nഉണക്കമീൻ ചോദിക്കുന്നു", [
 ("A","wide","ആന്റണീ, ഞങ്ങളുടെ മത്സ്യത്തൊഴിലാളി സൊസൈറ്റിയുടെ സൂര്യതാപ ഡ്രയർ മഴക്കാലത്തും മീൻ ഉണക്കും. പക്ഷേ സ്റ്റാർട്ടപ്പ് കമ്പനികൾക്കല്ലേ?"),
 ("V","V","സുമേ, ആരാ പറഞ്ഞേ? കോഓപ്പറേറ്റീവ് സൊസൈറ്റിക്കും DPIIT-ന് അപേക്ഷിക്കാം."),
 ("A","A","സത്യമായും? ഞങ്ങൾ കരുതി ടൈ കെട്ടിയവർക്ക് മാത്രമാണെന്ന്."),
 ("V","wide","പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, കോഓപ്പറേറ്റീവ് സൊസൈറ്റി. പത്ത് വർഷത്തിൽ താഴെ, പുതിയ രീതിയും വേണം."),
 ("A","A","അപ്പോ ഉണക്കമീനിലും ഇന്നൊവേഷൻ ആകാം."),
 ("V","wide","ടൈ അല്ല നോക്കുന്നത്, ഐഡിയയാണ്.")],
 "ടൈ അല്ല നോക്കുന്നത്,\nഐഡിയയാണ്", CTA_DPIIT, theme="crm",
 cap_ml="മത്സ്യത്തൊഴിലാളി സൊസൈറ്റിക്ക് സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷന് അപേക്ഷിക്കാമോ? കോഓപ്പറേറ്റീവ് സൊസൈറ്റിയും യോഗ്യമായ ഘടനയാണ്; പത്ത് വർഷത്തിൽ താഴെ പ്രായവും ഇന്നൊവേഷനും വേണം. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="Can a fishers' cooperative with a new solar fish dryer apply for Startup India recognition? Yes: a cooperative society is an eligible structure, alongside Pvt Ltd, LLP and registered partnership, if it is under 10 years old and works on innovation. Did you know this: yes or no?",
 cap_mg="Matsyathozhilaali society-kku Startup India recognition-nu apekshikkaamo? Cooperative society-um eligible aanu; 10 varshathil thaazhe praayavum innovation-um venam. Ithu ariyaamaayirunno?")

duo("ud033", "student_founder", "A", "hostel", "\"കമ്പനിക്ക് 2 മാസം.\nDPIIT-ന് ഒരു വർഷം\nകാത്തിരിക്കണോ?\"", [
 ("A","wide","സഞ്ജൂ, ആംഗ്യഭാഷ പഠിപ്പിക്കുന്ന നിന്റെ ആപ്പ് ഡെമോ ഡേയിൽ ഹിറ്റായല്ലോ. DPIIT അപേക്ഷിച്ചോ?"),
 ("V","V","അലീനേ, കമ്പനിക്ക് രണ്ട് മാസമേ ആയുള്ളൂ. ഒന്നുരണ്ട് വർഷം കഴിഞ്ഞ് നോക്കാം."),
 ("A","A","എന്തിന്? പ്രായപരിധി മുകളിലാണ്, താഴെയല്ല."),
 ("A","wide","ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് പത്ത് വർഷത്തിൽ താഴെ ആകണം. ഒപ്പം ഇന്നൊവേഷനോ സ്കെയിലബിൾ മാതൃകയോ."),
 ("V","V","അപ്പോ പ്രായം കുറവല്ല പ്രശ്നം, കൂടുതലാണ്."),
 ("A","wide","ഇവിടെ ചെറുപ്പം കുറവല്ല, യോഗ്യതയാണ്.")],
 "ചെറുപ്പം കുറവല്ല,\nയോഗ്യതയാണ്", CTA_DPIIT, theme="crm",
 cap_ml="രണ്ട് മാസം പ്രായമുള്ള കമ്പനിക്ക് DPIIT-ന് അപേക്ഷിക്കാൻ ഒരു വർഷം കാത്തിരിക്കണോ? നിബന്ധന ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് പത്ത് വർഷത്തിൽ താഴെ എന്നതാണ്, ഒപ്പം ഇന്നൊവേഷനോ സ്കെയിലബിൾ മാതൃകയോ. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര മാസം?",
 cap_en="A student founder's sign-language app company is two months old, and he thinks he must wait a year or two before applying for DPIIT recognition. The rule is an upper limit: under 10 years since incorporation, plus innovation or a scalable model. How many months old is your company?",
 cap_mg="2 maasam praayamulla company-kku DPIIT-nu apekshikkaan oru varsham kaathirikkano? Niyamam incorporation kazhinju 10 varshathil thaazhe ennathaanu, oppam innovation-o scalable model-o. Ningalude company-kku ethra maasam?")

duo("ud034", "tech_founder", "B", "ferry", "\"13 വയസ്സായ കമ്പനി.\nസ്റ്റാർട്ടപ്പ് പ്രായം\nകഴിഞ്ഞോ?\"", [
 ("A","wide","ടോണീ, മീൻകൂട്ടം കണ്ടുപിടിക്കുന്ന നിന്റെ സോണാർ ചെറുവള്ളക്കാർ വാങ്ങിത്തുടങ്ങിയല്ലോ. DPIIT നോക്കിയോ?"),
 ("V","V","മീരേ, കമ്പനിക്ക് 13 വയസ്സായി. പത്ത് കഴിഞ്ഞാൽ സ്റ്റാർട്ടപ്പ് അല്ലല്ലോ."),
 ("A","A","സാധാരണ സ്റ്റാർട്ടപ്പിന് അങ്ങനെയാണ്. നിന്റേത് ഡീപ് ടെക് ആണോ എന്ന് നോക്ക്."),
 ("A","wide","ഡീപ് ടെക് സ്റ്റാർട്ടപ്പിന് പ്രായപരിധി 20 വർഷം, ടേൺഓവർ പരിധി 300 കോടി."),
 ("V","V","അപ്പോ ആഴമുള്ള ടെക്കിന് ആയുസ്സും കൂടുതൽ."),
 ("A","wide","കടലിന്റെ ആഴം അളക്കുന്നവൻ നിയമവും ആഴത്തിൽ വായിക്കണം.")],
 "ഡീപ് ടെക്കിന്\nപരിധി 20 വർഷം", CTA_DPIIT, theme="faq",
 cap_ml="പത്ത് വർഷം കഴിഞ്ഞ കമ്പനിക്ക് DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷൻ ഇല്ലേ? സാധാരണ പരിധി 10 വർഷം, പക്ഷേ ഡീപ് ടെക് സ്റ്റാർട്ടപ്പിന് 20 വർഷവും 300 കോടി ടേൺഓവർ പരിധിയുമാണ്. നിങ്ങളുടെ ടെക്: ഡീപ്പോ സാധാരണയോ?",
 cap_en="A 13-year-old company making fish-finding sonar for small boats assumed it was too old for Startup India. The usual limit is 10 years, but a Deep Tech startup gets 20 years and a 300 crore turnover limit. Your tech: deep or regular?",
 cap_mg="10 varsham kazhinja company-kku DPIIT startup recognition ille? Saadhaarana paridhi 10 varsham, pakshe Deep Tech startup-nu 20 varshavum 300 crore turnover paridhiyum. Ningalude tech: deep-o saadhaaranayo?")

duo("ud035", "traditional_innovator", "C", "handloom", "\"തെയ്യത്തിന്റെ\nകിരീടം സ്റ്റാർട്ടപ്പ്\nആകുമോ?\"", [
 ("A","wide","കുമാറേ, തെയ്യം കിരീടം മരത്തിന് പകരം ഭാരം കുറഞ്ഞ നാരിൽ ഞങ്ങളുടെ കമ്പനി ഉണ്ടാക്കി. കോലക്കാരന്റെ കഴുത്ത് രക്ഷപ്പെട്ടു."),
 ("V","V","ലീലേച്ചീ, നല്ല കാര്യം. പക്ഷേ നൂറ്റാണ്ട് പഴക്കമുള്ള കല എങ്ങനെ സ്റ്റാർട്ടപ്പ് ആകും?"),
 ("A","A","കല പഴയതാകാം. ഉണ്ടാക്കുന്ന രീതി പുതിയതാണ്."),
 ("A","wide","പുതിയ ഉൽപ്പന്നം മാത്രമല്ല, ഉള്ളതിനെ മെച്ചപ്പെടുത്തുന്നതും DPIIT നോക്കും. ഘടനയും പത്ത് വർഷവും വേറെ നിബന്ധന."),
 ("V","V","അപ്പോ കല പഴയത്, കിരീടം പുതിയ വേർഷൻ."),
 ("A","wide","പാരമ്പര്യം പിന്നോട്ട് വലിക്കില്ല, പരിഷ്കാരം മുന്നോട്ട് കൊണ്ടുപോകും.")],
 "കല പഴയതാകാം,\nരീതി പുതിയതാകണം", CTA_DPIIT, theme="new",
 cap_ml="പഴയ കലയിലെ ഉൽപ്പന്നം സ്റ്റാർട്ടപ്പ് ആകുമോ? DPIIT നോക്കുന്നത് ഇന്നൊവേഷനോ ഉൽപ്പന്നത്തിന്റെ മെച്ചപ്പെടുത്തലോ സ്കെയിലബിൾ മാതൃകയോ ആണ്; ഒപ്പം കമ്പനി / LLP പോലുള്ള ഘടനയും പത്ത് വർഷ പരിധിയും. നിങ്ങളുടെ ബിസിനസിൽ പഴയതിൽ പുതിയത് എന്താണ്?",
 cap_en="Can a company making lighter Theyyam crowns from fibre instead of wood count as a startup? DPIIT looks at innovation or improvement of products or services, or a scalable model, along with an eligible structure and the 10-year limit. What's the new twist in your traditional business?",
 cap_mg="Pazhaya kalayile product startup aakumo? DPIIT nokkunnathu innovation-o product improvement-o scalable model-o aanu; oppam company / LLP pole ghadanayum 10 varsha paridhiyum. Ningalude business-il pazhayathil puthiyathu enthaanu?")

duo("ud036", "tech_founder", "A", "garage", "\"പേറ്റന്റ് കിട്ടാൻ\nവർഷങ്ങൾ. അതുവരെ\nകോപ്പി അടിക്കും\"", [
 ("A","wide","ജിതിനേ, പഴയ ഓട്ടോ ഇലക്ട്രിക് ആക്കുന്ന നിന്റെ കിറ്റ് ജംഗ്ഷനിൽ മുഴുവൻ സംസാരമാണ്."),
 ("V","V","ഐശ്വര്യേ, അതാ പേടി. പേറ്റന്റ് പരിശോധന വർഷങ്ങൾ എടുക്കും, അതിനിടെ ആരെങ്കിലും പകർത്തും."),
 ("A","A","നിന്റെ കമ്പനിക്ക് DPIIT റെക്കഗ്നിഷൻ ഉണ്ടോ?"),
 ("V","V","ഇല്ല. അതിന് പേറ്റന്റുമായി എന്ത് ബന്ധം?"),
 ("A","wide","റെക്കഗ്നിഷൻ ഉള്ള സ്റ്റാർട്ടപ്പിന് IP പരിശോധന വേഗത്തിലാക്കാം, പേറ്റന്റ് ഫയലിംഗ് തുകയിൽ 80 ശതമാനം ഇളവും."),
 ("V","wide","ഓട്ടോ ഇലക്ട്രിക്, പേറ്റന്റ് എക്സ്പ്രസ്.")],
 "ഓട്ടോ ഇലക്ട്രിക്,\nപേറ്റന്റ് എക്സ്പ്രസ്", CTA_BENEFITS, theme="faq",
 cap_ml="പേറ്റന്റ് കിട്ടാൻ വർഷങ്ങൾ എടുക്കുമെന്ന പേടിയുണ്ടോ? DPIIT റെക്കഗ്നിഷൻ ഉള്ള സ്റ്റാർട്ടപ്പിന് വേഗത്തിലുള്ള IP പരിശോധനയും പേറ്റന്റ് ഫയലിംഗിൽ 80 ശതമാനം ഇളവും കിട്ടാനുള്ള വഴി തുറക്കും. നിങ്ങളുടെ ഐഡിയ: പേറ്റന്റ് ചെയ്തോ?",
 cap_en="An EV conversion kit for old autorickshaws, and the founder fears copycats while the patent waits for years. DPIIT recognition opens faster IP examination and an 80% rebate on patent filing for recognised startups. Is your idea patented: yes or no?",
 cap_mg="Patent kittaan varshangal edukkumenna pediyundo? DPIIT recognition ulla startup-nu vegathilulla IP parishodhanayum patent filing-il 80 shathamaanam ilavum kittaanulla vazhi thurakkum. Ningalude idea: patent cheytho?")

duo("ud037", "investor_ready", "B", "juiceshop", "ട്രേഡ്മാർക്ക് ആദ്യമോ\nDPIIT ആദ്യമോ?\nക്രമം പ്രധാനം", [
 ("A","wide","നൗഷാദേ, ചക്കക്കുരു പ്രോട്ടീൻ ഡ്രിങ്കിന് പേരിട്ടു. അടുത്ത ആഴ്ച ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യാം."),
 ("V","V","റസിയാ, ഒരു മിനിറ്റ്. നമ്മുടെ കമ്പനിയുടെ DPIIT അപേക്ഷ എവിടെ എത്തി?"),
 ("A","A","അത് പിന്നെ നോക്കാം. പേരാണ് ഇപ്പോൾ പ്രധാനം."),
 ("V","wide","റെക്കഗ്നിഷൻ ഉള്ള സ്റ്റാർട്ടപ്പിന് ട്രേഡ്മാർക്ക് ഫയലിംഗ് തുകയിൽ 50 ശതമാനം ഇളവുണ്ട്. പേറ്റന്റിൽ 80."),
 ("A","A","അപ്പോ ജ്യൂസ് പോലെ, ചേരുവയുടെ ക്രമം തെറ്റിയാൽ രുചി പോകും."),
 ("V","wide","പേര് വൈകിക്കേണ്ട. പക്ഷേ പേരിനൊപ്പം പദവിയും നോക്ക്.")],
 "പേരിനൊപ്പം\nപദവിയും നോക്കൂ", CTA_BENEFITS, theme="faq",
 cap_ml="ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യാൻ പോകുന്നോ? DPIIT റെക്കഗ്നിഷൻ ഉള്ള സ്റ്റാർട്ടപ്പിന് ട്രേഡ്മാർക്ക് ഫയലിംഗിൽ 50 ശതമാനവും പേറ്റന്റിൽ 80 ശതമാനവും ഇളവുണ്ട്, അതുകൊണ്ട് രണ്ടും ഒരുമിച്ച് പ്ലാൻ ചെയ്യൂ. നിങ്ങളുടെ ബ്രാൻഡ് പേര് രജിസ്റ്റർ ചെയ്തോ?",
 cap_en="About to file a trademark for a new jackfruit-seed protein drink? DPIIT-recognised startups get a 50% rebate on trademark filing and 80% on patent filing, so plan the brand and the recognition together. Is your brand name registered: yes or no?",
 cap_mg="Brand-nu trademark file cheyyaan pokunno? DPIIT recognition ulla startup-nu trademark filing-il 50 shathamaanavum patent-il 80 shathamaanavum ilavundu, athukondu randum orumichu plan cheyyoo. Ningalude brand peru register cheytho?")

chat("uc002", "investor_ready", "C", "\"140 കോടി ടേൺഓവർ,\nഅന്ന് DPIIT ഇല്ല\"\nഇന്ന്?", ("ഹന്ന", "ഫഹദ്"), [
 (1,"ഹന്നാ, രണ്ട് വർഷം മുമ്പ് DPIIT നോക്കി. ടേൺഓവർ 140 കോടി ആയതുകൊണ്ട് പറ്റില്ലെന്ന് പറഞ്ഞു."),
 (0,"ഫഹദേ, അന്ന് പരിധി 100 കോടി ആയിരുന്നു. 2026 ഫെബ്രുവരി 4-ലെ നോട്ടിഫിക്കേഷൻ മുതൽ 200 കോടി."),
 (1,"അപ്പോ ഇപ്പോൾ വീണ്ടും നോക്കാമോ?"),
 (0,"ഒരു വർഷവും 200 കോടി കടന്നിട്ടില്ല, കമ്പനിക്ക് 10 വയസ്സായിട്ടില്ല, ഇന്നൊവേഷനും ഉണ്ടെങ്കിൽ അപേക്ഷിക്കാം."),
 (1,"പഴയ ഇല്ല, ഇന്ന് നോക്കാം ആയി."),
 (0,"നിയമം മാറുമ്പോൾ ഉത്തരവും മാറും.")],
 "പഴയ ഇല്ല,\nഇന്ന് നോക്കാം", CTA_DPIIT, theme="new",
 cap_ml="പഴയ 100 കോടി ടേൺഓവർ പരിധി കാരണം DPIIT വേണ്ടെന്ന് വെച്ചോ? 2026 ഫെബ്രുവരി 4-ലെ നോട്ടിഫിക്കേഷൻ മുതൽ പരിധി 200 കോടിയാണ് (ഡീപ് ടെക്കിന് 300); ഒരു വർഷവും അത് കടന്നിട്ടില്ലെങ്കിൽ വീണ്ടും നോക്കാം. നിങ്ങൾ അന്ന് അപേക്ഷിച്ചിരുന്നോ?",
 cap_en="Turned away from DPIIT recognition earlier because turnover was above the old 100 crore limit? Since the 4 Feb 2026 notification the limit is 200 crore in any year (300 crore for Deep Tech), so check again if you never crossed it and are under 10 years old. Did you apply back then: yes or no?",
 cap_mg="Pazhaya 100 crore turnover paridhi kaaranam DPIIT vendennu vecho? 2026 February 4-le notification muthal paridhi 200 crore aanu (Deep Tech-nu 300); oru varshavum athu kadannittillenkil veendum nokkaam. Ningal annu apekshichirunno?")

duo("ud038", "investor_ready", "A", "kitchen", "\"പാർട്ണർഷിപ്പ്\nആണ്, DPIIT\nകിട്ടില്ലല്ലോ?\"", [
 ("A","wide","രാജേഷേ, നമ്മുടെ മുളപ്പിച്ച ചാമ ബേബി ഫുഡിന് ഇൻവെസ്റ്റർക്ക് മുമ്പ് DPIIT വേണമെന്ന് മെന്റർ പറഞ്ഞു."),
 ("V","V","ബിന്ദൂ, നമ്മൾ രണ്ടുപേരുടെ പാർട്ണർഷിപ്പ് അല്ലേ? അതിന് DPIIT ഇല്ല. കമ്പനി തന്നെ വേണം."),
 ("A","A","പാർട്ണർഷിപ്പിനും പറ്റും. ഒരു വാക്ക് ശ്രദ്ധിക്കണം: രജിസ്റ്റേർഡ്."),
 ("V","V","നമ്മുടെ ഡീഡ് ഇതുവരെ രജിസ്റ്റർ ചെയ്തിട്ടില്ലല്ലോ."),
 ("A","wide","അതാ കുഴപ്പം. രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് ഫേം യോഗ്യമാണ്. ഇൻവെസ്റ്ററും വരുന്നെങ്കിൽ ഘടന ഒന്നുകൂടി ആലോചിക്കണം."),
 ("V","wide","രജിസ്റ്റർ ചെയ്യാത്ത വിശ്വാസം വീട്ടിൽ മതി, ബിസിനസിൽ പോരാ.")],
 "രജിസ്റ്റർ ചെയ്യാത്ത\nപാർട്ണർഷിപ്പ് പോരാ", CTA_DPIIT, theme="faq",
 cap_ml="പാർട്ണർഷിപ്പ് ബിസിനസിന് DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷൻ കിട്ടുമോ? രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് ഫേം യോഗ്യമായ ഘടനയാണ്; ഡീഡ് രജിസ്റ്റർ ചെയ്യാത്ത പാർട്ണർഷിപ്പ് അല്ല. നിങ്ങളുടെ പാർട്ണർഷിപ്പ് ഡീഡ് രജിസ്റ്റർ ചെയ്തോ?",
 cap_en="A couple making sprouted-millet baby food in a partnership thought only a company can get DPIIT recognition. A registered partnership firm is an eligible structure, but an unregistered one is not, and if investors are coming the structure needs a second look. Is your partnership deed registered: yes or no?",
 cap_mg="Partnership business-nu DPIIT startup recognition kittumo? Registered partnership firm eligible aanu; deed register cheyyaatha partnership alla. Ningalude partnership deed register cheytho?")
