# GST seed batch 01 (20 Nov). Short scripts (6 lines) that open on the painful moment: 19 Nov data shows viewers leave after 3-12 s.
# Situations from bank/STORY_THEMES.md (anonymised; names and details invented). Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd001", "trader", "A", "bakery", "ഹോട്ടൽ ഓർഡർ റെഡി.\nഒറ്റ ചോദ്യം:\n\"GST ബില്ല് ഉണ്ടോ?\"", [
 ("A","wide","സാബുച്ചേട്ടാ, ആ വലിയ ഹോട്ടലിലെ മാനേജർ വിളിച്ചു. എല്ലാ ദിവസവും നമ്മുടെ ബ്രെഡും കേക്കും വേണമെന്ന്!"),
 ("V","V","കൊള്ളാമല്ലോ. പക്ഷേ അവർ ചോദിച്ചത് GST ബില്ലാ. നമുക്ക് GST നമ്പർ ഇല്ലല്ലോ."),
 ("A","A","നമ്മുടെ ടേൺഓവർ 40 ലക്ഷം ആയിട്ടില്ലല്ലോ. അപ്പോ വേണ്ടല്ലോ?"),
 ("V","wide","നിർബന്ധം അല്ല. പക്ഷേ ആർക്കും സ്വമേധയാ രജിസ്റ്റർ ചെയ്യാം. വലിയ ബയർമാർ GST ബില്ലേ എടുക്കൂ."),
 ("A","A","പാൻ, ആധാർ, ഫോട്ടോ, കടയുടെ അഡ്രസ്സ് പ്രൂഫ്, ബാങ്ക് ഡീറ്റെയിൽസ്. അത്ര മതി."),
 ("V","wide","എങ്കിൽ നാളെ തന്നെ. ഓർഡർ പോകരുത്!")],
 "ലിമിറ്റ് ആയില്ലെങ്കിലും\nGST എടുക്കാം", CTA_GST,
 cap_ml="ബേക്കറിക്ക് ഹോട്ടലിന്റെ ദിവസ ഓർഡർ, പക്ഷേ അവർക്ക് GST ബില്ല് വേണം. ടേൺഓവർ ലിമിറ്റ് ആയില്ലെങ്കിലും GST രജിസ്ട്രേഷൻ സ്വമേധയാ എടുക്കാം; വലിയ ബയർമാർ GSTIN ചോദിക്കും.",
 cap_en="A Kerala bakery wins a hotel's daily order, but the hotel wants a GST bill. Even below the turnover limit you can take GST registration voluntarily, and big buyers usually insist on a GSTIN.",
 cap_mg="Bakery-kku hotel-nte daily order, pakshe avarkku GST bill venam. Turnover limit aayillenkilum GST registration swamedhaya edukkaam; valiya buyers GSTIN chodikkum.")

duo("gd002", "online_seller", "A", "mobileshop", "തമിഴ്നാട്ടിൽ നിന്ന്\nആദ്യ ഓൺലൈൻ ഓർഡർ.\nപക്ഷേ GST ഇല്ല", [
 ("A","wide","ഫഹദ്, എന്റെ ഹാൻഡ്‌മേഡ് സോപ്പിന് ചെന്നൈയിൽ നിന്ന് ഓർഡർ! പക്ഷേ സൈറ്റ് GSTIN ചോദിക്കുന്നു."),
 ("V","V","മറ്റൊരു സംസ്ഥാനത്തേക്കാണോ? എങ്കിൽ ടേൺഓവർ എത്ര ചെറുതായാലും ആദ്യ വിൽപ്പന മുതൽ GST വേണം."),
 ("A","A","കേരളത്തിനുള്ളിൽ മാത്രം വിറ്റാലോ?"),
 ("V","wide","ലിമിറ്റിൽ താഴെ, കേരളത്തിൽ മാത്രം ആണെങ്കിൽ ചില സൈറ്റുകളിൽ പാൻ വെച്ചുള്ള എൻറോൾമെന്റ് മതിയാകും. പുറത്തേക്ക് വിൽക്കാൻ GST തന്നെ."),
 ("A","A","എനിക്ക് ഇന്ത്യ മുഴുവൻ വിൽക്കണം."),
 ("V","wide","എങ്കിൽ ആദ്യം GSTIN. പിന്നെ ലിസ്റ്റിംഗ്.")],
 "മറ്റ് സംസ്ഥാനത്തേക്ക്\nവിൽക്കാൻ ആദ്യം GST", CTA_GST,
 cap_ml="ഹാൻഡ്‌മേഡ് സോപ്പിന് മറ്റൊരു സംസ്ഥാനത്ത് നിന്ന് ഓൺലൈൻ ഓർഡർ. മറ്റ് സംസ്ഥാനങ്ങളിലേക്ക് സാധനം വിൽക്കാൻ ടേൺഓവർ നോക്കാതെ ആദ്യ വിൽപ്പന മുതൽ GST വേണം.",
 cap_en="A handmade soap maker gets her first online order from another state. Selling goods to other states needs GST registration from the first sale, whatever the turnover. GST for online sellers in Kerala.",
 cap_mg="Handmade soap-nu vere state-il ninnu online order. Other state-ilekku saadhanam vilkkaan turnover nokkaathe first sale muthal GST venam.")

duo("gd003", "service_pro", "A", "office", "പണി കഴിഞ്ഞു.\nക്ലയന്റ്: \"GSTIN ഇല്ലാതെ\nപേമെന്റ് ഇല്ല\"", [
 ("A","wide","രാഹുൽ, ആ കമ്പനിയുടെ വെബ്സൈറ്റ് പണി തീർന്നില്ലേ? പേമെന്റ് എവിടെ?"),
 ("V","V","അവരുടെ അക്കൗണ്ട്സ് പറയുന്നു, GSTIN ഉള്ള ഇൻവോയ്സ് ഇല്ലാതെ പേമെന്റ് പ്രോസസ് ചെയ്യില്ലെന്ന്."),
 ("A","A","നിന്റെ വരുമാനം 20 ലക്ഷം കടന്നോ?"),
 ("V","V","ഈ വർഷം അടുത്തെത്തി. സർവീസിന് 20 ലക്ഷം കടന്നാൽ GST നിർബന്ധം."),
 ("A","wide","എങ്കിൽ ഇപ്പോഴേ എടുക്ക്. ലിമിറ്റ് കടന്ന ശേഷം ഓടുന്നതിലും നല്ലത്."),
 ("V","V","ശരി. അടുത്ത ഇൻവോയ്സ് GSTIN-ഓടെ.")],
 "സർവീസിന് ലിമിറ്റ്\n20 ലക്ഷം", CTA_LIMIT,
 cap_ml="വെബ്സൈറ്റ് പണി കഴിഞ്ഞു, പക്ഷേ കോർപ്പറേറ്റ് ക്ലയന്റ് GSTIN ഇല്ലാതെ പേമെന്റ് തരില്ല. കേരളത്തിൽ സർവീസ് ബിസിനസിന് വർഷം 20 ലക്ഷം കടന്നാൽ GST രജിസ്ട്രേഷൻ നിർബന്ധം.",
 cap_en="A freelance web developer finishes the job, but the corporate client won't pay without an invoice carrying a GSTIN. In Kerala, service businesses must register for GST above Rs 20 lakh turnover a year.",
 cap_mg="Website pani kazhinju, pakshe corporate client GSTIN illaathe payment tharilla. Kerala-yil service business-nu varsham 20 lakh kadannaal GST registration nirbandham.")

duo("gd004", "trader", "B", "shop", "\"തിരക്കിനിടയിൽ\nടേൺഓവർ നോക്കിയില്ല\"\n45 ലക്ഷം ആയി", [
 ("A","wide","സുരേഷേ, ഈ വർഷം ഹോൾസെയിൽ നന്നായി പോയല്ലോ. കണക്ക് നോക്കിയോ?"),
 ("V","V","ഇന്നലെ നോക്കി. 45 ലക്ഷം! തിരക്കിനിടയിൽ ശ്രദ്ധിച്ചില്ല."),
 ("A","A","സാധനങ്ങൾക്ക് 40 ലക്ഷം കടന്നാൽ GST വേണം. നീ രജിസ്റ്റർ ചെയ്തിട്ടില്ലല്ലോ."),
 ("V","V","ഇനി എന്ത് പറ്റും?"),
 ("A","wide","വൈകിയാൽ ടാക്സും 18% പലിശയും പിഴയും. പിഴ 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ."),
 ("V","wide","ഇനി ഒരു ദിവസം പോലും വൈകില്ല.")],
 "40 ലക്ഷം കടന്നോ?\nഇന്ന് തന്നെ നോക്കൂ", CTA_PENALTY,
 cap_ml="ഹോൾസെയിൽ കച്ചവടക്കാരന്റെ ടേൺഓവർ 45 ലക്ഷം ആയത് അറിഞ്ഞില്ല. സാധനങ്ങൾക്ക് 40 ലക്ഷം കടന്നാൽ GST നിർബന്ധം; വൈകിയാൽ ടാക്സ്, 18% പലിശ, 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10% പിഴ.",
 cap_en="A Kerala wholesaler realises his turnover crossed Rs 45 lakh without GST registration. For goods the limit is Rs 40 lakh; registering late means the tax, 18% interest and a penalty of Rs 10,000 or 10% of the tax, whichever is higher.",
 cap_mg="Wholesale kachavadakkarante turnover 45 lakh aayathu arinjilla. Goods-nu 40 lakh kadannaal GST nirbandham; vaikiyaal tax, 18% interest, 10,000 allenkil tax-inte 10% penalty.")

chat("gc001", "nri_business", "A", "ദുബായിലിരുന്ന് നാട്ടിലെ\nകടയ്ക്ക് GST?\n\"ഞാൻ ഇല്ലാതെ പറ്റുമോ?\"", ("ഷഹാന", "ആസിഫ്"), [
 (1,"ഇത്താ, നാട്ടിലെ ഫർണിച്ചർ കട നന്നായി പോകുന്നു. അനിയൻ പറയുന്നു GST എടുക്കണമെന്ന്."),
 (0,"നീ ദുബായിൽ അല്ലേ? ഉടമ നീ ആണോ?"),
 (1,"അതേ, കട എന്റെ പേരിൽ. ഞാൻ നാട്ടിൽ വരണോ?"),
 (0,"ആധാറിലെ മൊബൈലിൽ OTP വരും. ആ നമ്പർ ആക്ടീവ് ആണെങ്കിൽ വരാതെ ചെയ്യാം. കടയുടെ അഡ്രസ്സ് പ്രൂഫും ബാങ്ക് ഡീറ്റെയിൽസും വേണം."),
 (1,"നാട്ടിലെ നമ്പർ ഇപ്പോഴും ഉണ്ട്!"),
 (0,"എങ്കിൽ പ്രശ്നമില്ല. ഇവിടെ ഇരുന്ന് ചെയ്യാം.")],
 "ആധാർ മൊബൈൽ\nആക്ടീവ് ആക്കി വെക്കൂ", CTA_GST,
 cap_ml="ദുബായിലുള്ള ആളുടെ പേരിലുള്ള നാട്ടിലെ ഫർണിച്ചർ കടയ്ക്ക് GST വേണം. ആധാറുമായി ബന്ധിപ്പിച്ച മൊബൈലിൽ OTP വരും; കടയുടെ അഡ്രസ്സ് പ്രൂഫും ബാങ്ക് ഡീറ്റെയിൽസും വേണം.",
 cap_en="A Gulf Malayali owns a furniture shop in Kerala that now needs GST registration. Aadhaar OTP goes to the linked mobile, so keep that number active; you also need the shop's address proof and bank details.",
 cap_mg="Dubai-il ulla aalude perilulla naattile furniture kadakku GST venam. Aadhaar-umaayi link cheytha mobile-il OTP varum; kadayude address proof-um bank details-um venam.")

lst("gl001", "online_seller", "B", "GST ഇല്ലാതെ\nവിൽക്കാൻ പറ്റാത്ത\n3 സാഹചര്യം", [
 ("മറ്റൊരു സംസ്ഥാനത്തേക്ക്", "സാധനം കേരളത്തിന് പുറത്ത് വിൽക്കുന്നെങ്കിൽ ആദ്യ വിൽപ്പന മുതൽ GST."),
 ("ലിമിറ്റ് കടന്നാൽ", "സാധനങ്ങൾക്ക് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം."),
 ("വലിയ ബയർ ചോദിച്ചാൽ", "നിർബന്ധമല്ലെങ്കിലും ബിസിനസ് നഷ്ടപ്പെടാതിരിക്കാൻ സ്വമേധയാ എടുക്കാം.")],
 "ഏതിലാണ് നിങ്ങൾ?", CTA_LIMIT,
 cap_ml="GST ഇല്ലാതെ മുന്നോട്ട് പോകാൻ പറ്റാത്ത മൂന്ന് സാഹചര്യങ്ങൾ: മറ്റ് സംസ്ഥാനത്തേക്ക് സാധന വിൽപ്പന, സാധനങ്ങൾക്ക് 40 ലക്ഷം അല്ലെങ്കിൽ സർവീസിന് 20 ലക്ഷം ടേൺഓവർ, വലിയ ബയർ GSTIN ചോദിക്കുമ്പോൾ.",
 cap_en="Three situations where you can't keep selling without GST in Kerala: selling goods to other states, turnover above Rs 40 lakh for goods or Rs 20 lakh for services, and big buyers who ask for a GSTIN.",
 cap_mg="GST illaathe munnottu pokaan pattatha 3 saahacharyam: other state-ilekku goods, goods-nu 40 lakh allenkil service-nu 20 lakh turnover, valiya buyer GSTIN chodikkumbol.")
