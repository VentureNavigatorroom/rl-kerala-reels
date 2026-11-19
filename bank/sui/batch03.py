# Startup India / DPIIT seed batch 03 (19 Nov, backlog). Situations from bank/STORY_THEMES.md (anonymised; invented details).
# Facts only from topics.FACTS_SUI. No promises of approval or benefits. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

duo("ud020", "traditional_innovator", "A", "office", "ഒറ്റയ്ക്കുള്ള\nപ്രൊപ്രൈറ്റർഷിപ്പ്\nDPIIT-ന് അർഹമല്ല", [
 ("A","wide","രാഹുലേ, ഞാൻ ഒറ്റയ്ക്ക് ബിസിനസ് നടത്തുന്നു. DPIIT കിട്ടുമോ?"),
 ("V","V","നേഹ, കമ്പനി വേണ്ടേ? പ്രൊപ്രൈറ്റർഷിപ്പ് അംഗീകാരത്തിന് പറ്റില്ലല്ലോ."),
 ("A","A","അതെ. പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റർ ചെയ്ത പങ്കാളിത്തം, സഹകരണ സംഘം എന്നിവ മാത്രം."),
 ("V","V","അപ്പോ ആദ്യം ഘടന മാറ്റണം."),
 ("A","wide","അതെ. ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ അപേക്ഷ."),
 ("V","wide","ഘടന ശരിയല്ലെങ്കിൽ അപേക്ഷ തന്നെ പറ്റില്ല.")],
 "ഘടന ശരിയാകണം,\nDPIIT പിന്നീട്", CTA_DPIIT, theme="faq",
 cap_ml="DPIIT അംഗീകാരത്തിന് പ്രൊപ്രൈറ്റർഷിപ്പ് യോഗ്യമല്ല. പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റർ ചെയ്ത പങ്കാളിത്തം അല്ലെങ്കിൽ സഹകരണ സംഘം ആണ് യോഗ്യം. നിങ്ങളുടെ ബിസിനസ് ഏത് ഘടനയിലാണ്?",
 cap_en="A sole proprietorship cannot get DPIIT recognition. Only a private limited company, LLP, registered partnership or cooperative society qualifies. What structure is your business in?",
 cap_mg="DPIIT angeekaaram proprietorship-nu yogyatha illa. Private limited, LLP, registered partnership allenkil cooperative sangham venam. Ningalude business etha structure-il aanu?")

duo("ud021", "tech_founder", "B", "cafe", "ഇന്നൊവേഷൻ ഇല്ലെങ്കിൽ\nDPIIT കിട്ടുമോ?\nപല കാര്യം", [
 ("A","wide","റോഷാ, നമ്മുടെ കഫേ ഒരു ചായ മാത്രമാണ്. DPIIT കിട്ടുമോ?"),
 ("V","V","ആൽവിനേ, പുതിയ ഉൽപ്പന്നമോ സേവനമോ മെച്ചപ്പെടുത്തുന്നുണ്ടോ?"),
 ("A","A","ഇല്ല. പക്ഷേ നല്ല വിപുലീകരണ മാതൃകയുണ്ടെങ്കിൽ കണക്കിലെടുക്കും."),
 ("V","V","അപ്പോ അത് തെളിയിക്കണം."),
 ("A","wide","അതെ. മെച്ചപ്പെടുത്തൽ അല്ലെങ്കിൽ സ്കെയിലബിൾ മാതൃക, ഏതെങ്കിലും ഒന്ന് വേണം."),
 ("V","wide","അംഗീകാരം ഉറപ്പല്ല. യോഗ്യത വ്യക്തമായി കാണിക്കൂ.")],
 "ഇന്നൊവേഷനോ സ്കെയിലബിൾ\nമാതൃകയോ ഏതെങ്കിലും ഒന്ന്", CTA_DPIIT, theme="new",
 cap_ml="DPIIT യോഗ്യതയ്ക്ക് നൂതന ഉൽപ്പന്നമോ സേവനമോ മെച്ചപ്പെടുത്തലോ, അല്ലെങ്കിൽ സ്കെയിലബിൾ ബിസിനസ് മാതൃകയോ വേണം. അംഗീകാരം ഉറപ്പല്ല. നിങ്ങളുടെ ബിസിനസിൽ എന്താണ് പുതിയത്?",
 cap_en="DPIIT eligibility needs innovation or improvement of products or services, or a scalable business model. Approval is never guaranteed. What is new in your business?",
 cap_mg="DPIIT yogyathakku innovation allenkil scalable business model venam. Angeekaaram urappalla. Ningalude business-il enthaanu puthiyathu?")

duo("ud022", "tech_founder", "A", "home", "ടേൺഓവർ 200 കോടി\nകടന്നാൽ DPIIT\nപോകുമോ?", [
 ("A","wide","അരുണേ, നമ്മുടെ സ്റ്റാർട്ടപ്പ് വളരുന്നു. ടേൺഓവർ പരിധി എന്താണ്?"),
 ("V","V","സ്നേഹേ, ഫെബ്രുവരി 2026-ലെ വിജ്ഞാപനപ്രകാരം ഓരോ വർഷവും 200 കോടിക്ക് താഴെയായിരിക്കണം."),
 ("A","A","ഡീപ്-ടെക്കിന് 300 കോടി. ഒരു വർഷം കടന്നാൽ DPIIT നഷ്ടമാകും."),
 ("V","V","അപ്പോ വളർച്ചയ്ക്ക് മുമ്പ് ഇക്കാര്യം അറിഞ്ഞിരിക്കണം."),
 ("A","wide","അതെ. മുമ്പ് ഇത് 100 കോടിയായിരുന്നു, പുതിയ നിയമം അറിഞ്ഞ് തീരുമാനിക്കൂ."),
 ("V","wide","വളർച്ച നല്ലതാണ്, പക്ഷേ പരിധി അറിഞ്ഞിരിക്കണം.")],
 "വളർച്ചയ്ക്ക് മുമ്പ്\nപരിധി അറിഞ്ഞിരിക്കൂ", CTA_DPIIT, theme="faq",
 cap_ml="DPIIT അംഗീകാരത്തിന് ഓരോ വർഷത്തെയും ടേൺഓവർ 200 കോടിക്ക് താഴെയായിരിക്കണം. ഡീപ്-ടെക്കിന് 300 കോടി. 2026 ഫെബ്രുവരിയിലെ വിജ്ഞാപനം പ്രകാരമാണിത്. നിങ്ങളുടെ ടേൺഓവർ എത്രയാണ്?",
 cap_en="Turnover must stay below 200 crore rupees in every year for DPIIT recognition, or 300 crore for deep tech, under the February 2026 notification. What is your current turnover?",
 cap_mg="DPIIT angeekaarathinu oro varshathe turnover 200 kodikku thaazhe venam. Deep tech-nu 300 kodi. 2026 February vijnjaapanam prakaaram. Ningalude turnover ethra?")

duo("ud023", "traditional_innovator", "B", "gym", "പത്ത് വർഷം\nകഴിഞ്ഞാൽ DPIIT\nഇല്ല", [
 ("A","wide","ജസ്റ്റിനേ, ഞങ്ങളുടെ കമ്പനി പത്ത് വർഷം മുമ്പ് തുടങ്ങിയതാണ്. ഇപ്പോഴും DPIIT പറ്റുമോ?"),
 ("V","V","റിയാ, പത്ത് വർഷത്തിനുള്ളിൽ മാത്രം. ഡീപ്-ടെക്കിന് ഇരുപത് വർഷം വരെ."),
 ("A","A","അപ്പോ നമ്മൾ സാധാരണ വിഭാഗമാണ്. ഇനി പുതിയ അപേക്ഷ വേണ്ടേ?"),
 ("V","V","ഇൻകോർപ്പറേഷൻ തീയതി മുതലാണ് കണക്ക്. അതിന് മുമ്പുള്ള തീയതി നോക്കൂ."),
 ("A","wide","അതെ. തീയതി വ്യക്തമാക്കി മാത്രം അപേക്ഷിക്കൂ."),
 ("V","wide","പ്രായം നോക്കി തീരുമാനിക്കൂ, അവസാന തീയതിക്ക് മുമ്പേ.")],
 "ഇൻകോർപ്പറേഷൻ തീയതി\nമുതലാണ് പത്ത് വർഷം", CTA_DPIIT, theme="faq",
 cap_ml="DPIIT അംഗീകാരത്തിന് കമ്പനി ഇൻകോർപ്പറേറ്റ് ചെയ്ത തീയതി മുതൽ പത്ത് വർഷത്തിനുള്ളിലായിരിക്കണം. ഡീപ്-ടെക്കിന് ഇരുപത് വർഷം. നിങ്ങളുടെ കമ്പനി എപ്പോൾ തുടങ്ങി?",
 cap_en="For DPIIT, a company must be under 10 years old counted from incorporation, or 20 years for deep tech. When was your company incorporated?",
 cap_mg="DPIIT-nu company incorporate cheytha theeyathi muthal 10 varsham. Deep tech-nu 20 varsham. Ningalude company eppozhaanu thudangiyathu?")

duo("ud024", "student_founder", "A", "classroom", "പേറ്റന്റ് ഫയലിംഗിൽ\n80 ശതമാനം ഇളവ്.\nആർക്ക്?", [
 ("A","wide","ആദർശേ, DPIIT കിട്ടിയാൽ പേറ്റന്റിൽ ഇളവ് കിട്ടുമെന്ന് കേട്ടു."),
 ("V","V","നിമ്മീ, അതെ. പേറ്റന്റ് ഫയലിംഗിൽ 80 ശതമാനം ഇളവുണ്ട്."),
 ("A","A","ട്രേഡ്മാർക്കിന് 50 ശതമാനം. IP പരിശോധനയും വേഗത്തിലാകും."),
 ("V","V","പക്ഷേ അത് അംഗീകാരം കിട്ടിയ ശേഷം മാത്രം."),
 ("A","wide","അതെ. അപേക്ഷയ്ക്ക് മുമ്പ് ഇളവ് കിട്ടില്ല."),
 ("V","wide","ഇളവ് ഉറപ്പല്ല, നിയമം അറിഞ്ഞ് ആസൂത്രണം ചെയ്യൂ.")],
 "പേറ്റന്റിൽ 80 ശതമാനം,\nട്രേഡ്മാർക്കിൽ 50 ശതമാനം", CTA_BENEFITS, theme="faq",
 cap_ml="DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പുകൾക്ക് പേറ്റന്റ് ഫയലിംഗിൽ 80 ശതമാനവും ട്രേഡ്മാർക്കിൽ 50 ശതമാനവും ഇളവ് കിട്ടും. അംഗീകാരം കിട്ടിയ ശേഷം മാത്രം. നിങ്ങൾ പേറ്റന്റ് ഫയൽ ചെയ്യുന്നുണ്ടോ?",
 cap_en="DPIIT-recognised startups get an 80 percent rebate on patent filing and 50 percent on trademark filing, only after recognition. Are you planning to file a patent?",
 cap_mg="DPIIT angeekaaramulla startups-nu patent filing-il 80 percent, trademark-il 50 percent ilavu. Angeekaaram kittiya sesham maathram. Ningal patent file cheyyunnundo?")

duo("ud025", "traditional_innovator", "B", "library", "തൊഴിൽ, പരിസ്ഥിതി\nനിയമങ്ങൾ സ്വയം\nസാക്ഷ്യപ്പെടുത്തൽ", [
 ("A","wide","അനൂപേ, DPIIT കിട്ടിയാൽ ഇൻസ്പെക്ഷൻ കുറയുമെന്ന് കേട്ടു."),
 ("V","V","ഗ്രീഷ്മേ, അതെ. തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങൾക്ക് സ്വയം സാക്ഷ്യപ്പെടുത്തൽ ഓപ്ഷൻ കിട്ടും."),
 ("A","A","എല്ലാ നിയമങ്ങളും ബാധകമല്ലാതാകുമോ?"),
 ("V","V","ഇല്ല. പക്ഷേ ചില നിയമങ്ങളിൽ ഇളവ് മാത്രം."),
 ("A","wide","അതുകൊണ്ട് ഏത് നിയമമെന്ന് വ്യക്തമാക്കി ചെക്ക് ചെയ്യണം."),
 ("V","wide","എല്ലാ നിയമവും ഒഴിവാകുമെന്ന് കരുതരുത്.")],
 "എല്ലാ നിയമവും ഒഴിവല്ല,\nചിലതിൽ മാത്രം ഇളവ്", CTA_BENEFITS, theme="faq",
 cap_ml="DPIIT അംഗീകാരമുള്ള സ്റ്റാർട്ടപ്പുകൾക്ക് ചില തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ സ്വയം സാക്ഷ്യപ്പെടുത്തൽ സൗകര്യം കിട്ടും. എല്ലാ നിയമത്തിനും ബാധകമല്ല. നിങ്ങളുടെ ബിസിനസിന് ഏതൊക്കെ നിയമങ്ങളുണ്ട്?",
 cap_en="DPIIT-recognised startups may self-certify under some labour and environment laws, not all of them. Which laws apply to your business?",
 cap_mg="DPIIT angeekaaramulla startups-nu chila labour, environment niyamangalil self-certification kittum. Ellaa niyamavum allaa. Ningalude businessinu etha niyamangal baadhakam?")

duo("ud026", "tech_founder", "A", "rooftop", "DPIIT കിട്ടി.\nടാക്സ് ഹോളിഡേ\nഓട്ടോമാറ്റിക്കല്ല", [
 ("A","wide","ശ്യാമേ, DPIIT കിട്ടിയാൽ ടാക്സ് ഒഴിവ് കിട്ടുമെന്ന് ഒരാൾ പറഞ്ഞു."),
 ("V","V","ആര്യേ, ഇതൊന്നും ഓട്ടോമാറ്റിക് അല്ല. 80-IAC പ്രത്യേക അപേക്ഷയാണ്."),
 ("A","A","അപ്പോ DPIIT കൊണ്ട് മാത്രം ടാക്സ് ഒഴിവില്ലേ?"),
 ("V","V","ഇല്ല. ആദ്യ പത്തിൽ മൂന്ന് വർഷം ലാഭത്തിന് ഒഴിവ്, പക്ഷേ അത് വേറെ അംഗീകാരം."),
 ("A","wide","അതെ. ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കണം."),
 ("V","wide","DPIIT ഉണ്ടെന്ന് കരുതി ടാക്സ് പ്ലാൻ ഇടരുത്.")],
 "ടാക്സ് ഒഴിവ് വേറെ\nഅപേക്ഷ, സ്വയമേവയല്ല", CTA_BENEFITS, theme="new",
 cap_ml="DPIIT അംഗീകാരം ഉണ്ടെങ്കിലും 80-IAC ടാക്സ് ഒഴിവ് സ്വയമേവ കിട്ടില്ല. ഇത് പ്രത്യേക അപേക്ഷയാണ്, ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കണം. നിങ്ങൾ ടാക്സ് ഒഴിവ് പ്ലാൻ ചെയ്യുന്നുണ്ടോ?",
 cap_en="Even with DPIIT recognition, the section 80-IAC tax holiday is a separate application approved by an inter-ministerial board, not automatic. Are you planning around a tax holiday?",
 cap_mg="DPIIT undaayaalum 80-IAC tax ilavu swamedhayaa kittilla. Ithu verae apekshayaanu, inter-ministerial board angeekarikkanam. Ningal tax ilavu plan cheyyunnundo?")

duo("ud027", "traditional_innovator", "B", "beach", "സർക്കാർ സ്കീമും\nടെൻഡറും കിട്ടാൻ\nഒരു അംഗീകാരം", [
 ("A","wide","നിഖിലേ, ടെൻഡറിന് വേണ്ടി നമ്മുടെ കമ്പനിക്ക് എന്ത് വേണം?"),
 ("V","V","ദിവ്യേ, DPIIT അംഗീകാരമുണ്ടെങ്കിൽ പല സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും യോഗ്യത."),
 ("A","A","അപ്പോ അതൊരു വാതിൽ മാത്രമാണ്."),
 ("V","V","അതെ. ഓരോ സ്കീമിനും വെവ്വേറെ നിബന്ധനയുണ്ട്."),
 ("A","wide","ഓരോന്നിന്റെയും നിബന്ധന പരിശോധിക്കണം."),
 ("V","wide","അംഗീകാരം തുടക്കം, ഉറപ്പല്ല.")],
 "അംഗീകാരം ഒരു വാതിൽ,\nഓരോ സ്കീമിനും നിബന്ധന", CTA_BENEFITS, theme="new",
 cap_ml="DPIIT അംഗീകാരം പല സർക്കാർ സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും യോഗ്യത നൽകാം, പക്ഷേ ഓരോന്നിനും വ്യത്യസ്ത നിബന്ധനയുണ്ട്. ഉറപ്പല്ല. നിങ്ങൾ ഏത് സ്കീമാണ് നോക്കുന്നത്?",
 cap_en="DPIIT recognition can open the door to many government schemes and tenders, each with its own conditions. It is not a guarantee. Which scheme are you looking at?",
 cap_mg="DPIIT angeekaaram pala government schemes-um tenders-um yogyatha tharaam, pakshe oro-kkum niyamangal undu. Urappalla. Ningal etha scheme-aanu nokkunnathu?")

duo("ud028", "tech_founder", "B", "hospital", "LLP-ക്കും DPIIT\nകിട്ടും.\nപക്ഷേ ഒരു നിബന്ധന", [
 ("A","wide","ജോസഫേ, ഞങ്ങളുടേത് LLP ആണ്. DPIIT-ന് അപേക്ഷിക്കാമോ?"),
 ("V","V","ലക്ഷ്മീ, അതെ. LLP യോഗ്യമാണ്. പ്രൈവറ്റ് ലിമിറ്റഡ് മാത്രമല്ല."),
 ("A","A","എന്നാൽ മറ്റ് നിബന്ധനകൾ ബാധകമല്ലേ?"),
 ("V","V","ബാധകമാണ്. പത്ത് വർഷം, ടേൺഓവർ, ഇന്നൊവേഷൻ എല്ലാം."),
 ("A","wide","അപ്പോ LLP ആണെന്ന് മാത്രം പോരാ."),
 ("V","wide","എല്ലാ നിബന്ധനയും ഒരുമിച്ച് പരിശോധിക്കൂ.")],
 "LLP യോഗ്യം, പക്ഷേ\nമറ്റ് നിബന്ധനകളും ബാധകം", CTA_DPIIT, theme="faq",
 cap_ml="LLP ആയാലും DPIIT അംഗീകാരത്തിന് യോഗ്യതയുണ്ട്. പക്ഷേ പത്ത് വർഷം, ടേൺഓവർ പരിധി, ഇന്നൊവേഷൻ അല്ലെങ്കിൽ സ്കെയിലബിൾ മാതൃക എന്നിവ എല്ലാം ബാധകമാണ്. നിങ്ങളുടെ LLP എന്ന് തുടങ്ങി?",
 cap_en="An LLP can apply for DPIIT recognition, but the 10-year age limit, turnover cap and innovation or scalability test all still apply. When was your LLP formed?",
 cap_mg="LLP-kkum DPIIT-nu apekshikkaam, pakshe 10 varsham, turnover paridhi, innovation enniva baadhakam. Ningalude LLP eppozhaanu thudangiyathu?")

duo("ud029", "tech_founder", "A", "salon", "പുതിയ സ്റ്റുഡിയോയ്ക്ക്\nDPIIT അപേക്ഷ.\nഎന്ത് തെളിയിക്കണം?", [
 ("A","wide","വിനീതേ, പുതിയ സ്റ്റുഡിയോയ്ക്ക് DPIIT അപേക്ഷ കൊടുക്കണോ?"),
 ("V","V","സോണിയാ, യോഗ്യതയ്ക്ക് ഇന്നൊവേഷൻ അല്ലെങ്കിൽ സ്കെയിലബിൾ മാതൃക വേണം."),
 ("A","A","ഞങ്ങളുടെ മാതൃക വളരാൻ പറ്റുന്നതാണെന്ന് എങ്ങനെ തെളിയിക്കും?"),
 ("V","V","ഓരോ ശാഖയും ഒരേ രീതിയിൽ നീങ്ങുന്ന മാതൃക, അതിന്റെ രേഖ വേണം."),
 ("A","wide","അതെ. കണക്കും പ്ലാനും ചേർത്ത് വെക്കണം."),
 ("V","wide","അംഗീകാരം ഉറപ്പല്ല, രേഖ നല്ലതാക്കൂ.")],
 "സ്കെയിലബിൾ മാതൃക\nരേഖയായി തെളിയിക്കൂ", CTA_DPIIT, theme="new",
 cap_ml="DPIIT അപേക്ഷയ്ക്ക് സ്കെയിലബിൾ ബിസിനസ് മാതൃക തെളിയിക്കാൻ രേഖയും പ്ലാനും വേണം. അംഗീകാരം ഉറപ്പല്ല. നിങ്ങളുടെ ബിസിനസ് മാതൃക എഴുതി വെച്ചിട്ടുണ്ടോ?",
 cap_en="A DPIIT application needs a written scalable business model, supported by numbers and a plan. Recognition is never guaranteed. Have you written your business model down?",
 cap_mg="DPIIT apekshakku scalable business model thelikkaan rekhayum planum venam. Angeekaaram urappalla. Ningalude business model ezhuthi vecchittundo?")
