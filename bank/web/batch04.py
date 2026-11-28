# web batch 04 (28 Nov night): tech development (apps, MVPs, team software, automations, websites). Business-first angle.
# OUR service: never a price, instalment amount, timeline or delivery date; never promise users, sales, rankings or funding. Facts only from topics.FACTS_WEB.
# Names, sectors and towns invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_WEBSITE, CTA_WEBPLAN = topics.CTA_WEBSITE, topics.CTA_WEBPLAN

# faq: ready-made apps have too much of what a tuition centre doesn't need and none of what it does
duo("wbd105", "ops_software", "B", "classroom", "200 കുട്ടികൾ.\nഹാജർ ബുക്കിൽ,\nബാച്ച് ഓർമയിൽ", [
 ("A","wide","ആദർശേ, ഇരുന്നൂറ് കുട്ടികൾ, ആറ് ബാച്ച്. ഹാജർ ബുക്കിൽ, ടൈംടേബിൾ ബോർഡിൽ. ദിവസവും പേരന്റ്സിന്റെ കോൾ."),
 ("V","V","നിമ്മീ, നിന്റെ ട്യൂഷൻ സെന്ററിന് ചേരുന്ന ഒരു സോഫ്റ്റ്‌വെയർ ആലോചിച്ചോ?"),
 ("A","A","റെഡിമെയ്ഡ് ആപ്പുകൾ നോക്കി. വേണ്ടാത്തത് ഒരുപാട്, വേണ്ടത് ഇല്ല."),
 ("V","V","ആദ്യം സെന്റർ എങ്ങനെ നടക്കുന്നു എന്ന് മനസ്സിലാക്കണം. ഹാജരും പേരന്റ്സിനുള്ള മെസ്സേജുമാണ് സമയം തിന്നുന്നതെങ്കിൽ അത് ആദ്യം."),
 ("A","wide","അപ്പോ എല്ലാം ഒന്നിച്ച് വേണ്ട. ഏറ്റവും വേദനിക്കുന്നത് ആദ്യം."),
 ("V","wide","നിന്റെ രീതിക്ക് നിന്റെ സോഫ്റ്റ്‌വെയർ.")],
 "നിങ്ങളുടെ രീതിക്ക്\nനിങ്ങളുടെ സോഫ്റ്റ്‌വെയർ", CTA_WEBPLAN, theme="faq",
 cap_ml="റെഡിമെയ്ഡ് ആപ്പിൽ വേണ്ടാത്തത് ഒരുപാട്, വേണ്ടത് ഇല്ലേ? ആദ്യം നിങ്ങളുടെ സ്ഥാപനം എങ്ങനെ നടക്കുന്നു എന്ന് മനസ്സിലാക്കി, ഏറ്റവും സമയം കളയുന്ന പണി ആദ്യം ശരിയാക്കുന്ന സോഫ്റ്റ്‌വെയർ. മാസ തവണയായി അടയ്ക്കാം. നിങ്ങളുടെ സമയം തിന്നുന്ന പണി ഏത്?",
 cap_en="Two hundred students, six batches, attendance in a book and parents calling every day. Ready-made apps had plenty she didn't need and nothing she did. Good team software starts from how your centre runs and fixes the biggest time-waster first, paid in monthly parts. What eats your time?",
 cap_mg="Readymade app-il vendaathathu orupaadu, vendathu ille? Aadyam ningalude sthaapanam engane nadakkunnu ennu manassilaakki, ettavum samayam kalayunna pani aadyam shariyaakkunna software. Maasa thavanayaayi adaykkaam. Ningalude samayam thinnunna pani ethu?")

# crm (#8 style, invented): a catering unit's wedding order sank in a WhatsApp chat; the kitchen never saw it
duo("wbd106", "ops_software", "A", "weddinghall", "കല്യാണ ഓർഡർ\nവാട്സാപ്പിൽ വന്നു.\nഅടുക്കള അറിഞ്ഞില്ല", [
 ("A","wide","ശരത്തേട്ടാ, ഞായറാഴ്ചത്തെ കല്യാണത്തിന് മുന്നൂറ് പേരുടെ ഓർഡർ. അടുക്കളയിൽ ആരും അറിഞ്ഞില്ല!"),
 ("V","V","കാവ്യേ, ഓർഡർ എന്റെ വാട്സാപ്പിൽ ആയിരുന്നു. നൂറ് ചാറ്റിനിടയിൽ മുങ്ങിപ്പോയി."),
 ("A","A","ഇത് മൂന്നാം തവണയാ. ഇനി എന്ത് ചെയ്യും?"),
 ("V","V","ഓർഡർ ഒരിടത്ത് കയറ്റുന്ന ഒരു ലളിതമായ സോഫ്റ്റ്‌വെയർ. കയറ്റിയാൽ അടുക്കളയ്ക്കും ഡെലിവറിക്കും ഒരുമിച്ച് കാണാം."),
 ("A","wide","ഒറ്റയടിക്ക് വലിയ തുക വേണ്ട, മാസ തവണയായി ചെയ്യാം എന്നല്ലേ ആ ടീം പറഞ്ഞത്? ഇന്ന് തന്നെ വിളിക്കാം."),
 ("V","wide","ചാറ്റ് സംസാരത്തിന്, ഓർഡർ സിസ്റ്റത്തിൽ.")],
 "ചാറ്റ് സംസാരത്തിന്,\nഓർഡർ സിസ്റ്റത്തിൽ", CTA_WEBPLAN, theme="crm",
 cap_ml="ഓർഡർ വാട്സാപ്പ് ചാറ്റിൽ മുങ്ങിപ്പോയോ? ഓർഡർ ഒരിടത്ത് കയറ്റി അടുക്കളയ്ക്കും ഡെലിവറിക്കും ഒരുമിച്ച് കാണിക്കുന്ന ലളിതമായ സോഫ്റ്റ്‌വെയർ നിങ്ങളുടെ രീതിക്ക് ഉണ്ടാക്കാം, മാസ തവണയായി. നിങ്ങളുടെ ഓർഡറുകൾ ഇപ്പോൾ എവിടെ വരുന്നു?",
 cap_en="A 300-guest wedding order sat in a WhatsApp chat and the kitchen never saw it, for the third time. Simple order software built around how your unit works puts every order in one place for the kitchen and delivery, paid in monthly parts. Where do your orders land today?",
 cap_mg="Order WhatsApp chat-il mungippoyo? Order oridathu kayatti adukkalaykkum delivery-kkum orumichu kaanikkunna laalithamaaya software ningalude reethikku undaakkaam, maasa thavanayaayi. Ningalude orders ippol evide varunnu?")

# faq: "an app like the taxi apps" is an idea, not a plan; a business-first team asks the questions before code
duo("wbd107", "app_idea", "B", "foodcourt", "\"ഒരു ആപ്പ് വേണം,\nടാക്സി ആപ്പ് പോലെ\"\nഅത്രയേ ഉള്ളൂ പ്ലാൻ", [
 ("A","wide","ഡെന്നിസേ, പ്ലംബറെയും ഇലക്ട്രീഷ്യനെയും വിളിക്കാൻ ഒരു ആപ്പ് വേണം. ടാക്സി ആപ്പ് പോലെ."),
 ("V","V","മരിയേ, ആര് ബുക്ക് ചെയ്യും? പണിക്കാർ എങ്ങനെ ചേരും? പൈസ ആർക്ക്, എപ്പോൾ? ക്യാൻസൽ ആയാൽ എന്ത്?"),
 ("A","A","അതൊന്നും ആലോചിച്ചില്ല. ആപ്പ് ഉണ്ടാക്കുന്നവർ നോക്കില്ലേ?"),
 ("V","V","ബിസിനസ് അറിയുന്ന ടീം ഈ ചോദ്യങ്ങൾ ആദ്യം ചോദിക്കും. ഉത്തരങ്ങൾ ഒരു ഫ്ലോ ആക്കിയിട്ടേ കോഡ് തുടങ്ങൂ."),
 ("A","wide","അപ്പോ ആ ഒറ്റ വരി ഒരു പ്ലാൻ അല്ല, ഒരു തുടക്കം മാത്രം."),
 ("V","wide","ഐഡിയ ഒരു വരി, പ്ലാൻ ഒരു പേജ്.")],
 "ഐഡിയ ഒരു വരി,\nപ്ലാൻ ഒരു പേജ്", CTA_WEBPLAN, theme="faq",
 cap_ml="\"ആ ആപ്പ് പോലെ ഒന്ന്\" എന്നത് പ്ലാൻ അല്ല. ആര് ഉപയോഗിക്കും, പൈസ എങ്ങനെ വരും, ക്യാൻസൽ ആയാൽ എന്ത്: ബിസിനസ് അറിയുന്ന ടീം ഇത് ആദ്യം ചോദിക്കും, പിന്നെയാണ് കോഡ്. നിങ്ങളുടെ ആപ്പ് ഐഡിയ ഒരു വരിയാണോ ഒരു പേജാണോ?",
 cap_en="\"An app like the taxi apps, but for plumbers\" is an idea, not a plan. Who books, how workers join, who gets paid and when, what happens on a cancellation: a business-first team asks these before any code. Is your app idea one line or one page?",
 cap_mg="'Aa app pole onnu' ennathu plan alla. Aaru upayogikkum, paisa engane varum, cancel aayaal enthu: business ariyunna team ithu aadyam chodikkum, pinneyaanu code. Ningalude app idea oru variyaano oru pejaano?")

# crm (#20 / #25 style, invented): an investor tired of slides wants to see the product work - an MVP (no funding promised)
duo("wbd108", "mvp_founder", "A", "metro", "ഇൻവെസ്റ്റർ പറഞ്ഞു:\n\"സ്ലൈഡ് വേണ്ട,\nവർക്ക് ചെയ്യുന്നത് കാണിക്ക്\"", [
 ("A","wide","കിരണേ, മീറ്റിംഗിൽ ഇൻവെസ്റ്റർ പറഞ്ഞു, സ്ലൈഡ് കണ്ട് മടുത്തു, ആപ്പ് ശരിക്കും വർക്ക് ചെയ്യുന്നത് കാണിക്ക് എന്ന്."),
 ("V","V","അഞ്ജലീ, അപ്പോ ആദ്യം ഒരു MVP. പ്രധാന പ്രശ്നം തീർക്കുന്ന ഏറ്റവും ചെറിയ വേർഷൻ."),
 ("A","A","പക്ഷേ ഏത് ഫീച്ചർ ആദ്യം വേണം എന്ന് എനിക്ക് ഉറപ്പില്ല."),
 ("V","V","അതിന് ബിസിനസ് അറിയുന്ന ടീം വേണം. കസ്റ്റമർ ആര്, പൈസ എങ്ങനെ വരും, ഇൻവെസ്റ്റർ എന്ത് നോക്കും. അത് നോക്കി MVP തീരുമാനിക്കും."),
 ("A","wide","ഫണ്ടിംഗ് ആർക്കും ഉറപ്പില്ല. പക്ഷേ അടുത്ത മീറ്റിംഗിൽ കാണിക്കാൻ ഒന്ന് ഉണ്ടാകും."),
 ("V","wide","പറഞ്ഞാൽ സ്ലൈഡ്, കാണിച്ചാൽ തെളിവ്.")],
 "പറഞ്ഞാൽ സ്ലൈഡ്,\nകാണിച്ചാൽ തെളിവ്", CTA_WEBPLAN, theme="crm",
 cap_ml="സ്ലൈഡ് അല്ല, വർക്ക് ചെയ്യുന്ന ഒന്ന് കാണണം എന്ന് ഇൻവെസ്റ്റർ പറഞ്ഞോ? പ്രധാന പ്രശ്നം തീർക്കുന്ന ഏറ്റവും ചെറിയ വേർഷനാണ് MVP. ഫണ്ടിംഗ് ആർക്കും ഉറപ്പ് പറയാനാവില്ല, പക്ഷേ കാണിക്കാൻ ഒന്ന് ഉണ്ടാകും. നിങ്ങളുടെ MVP-യിൽ ആദ്യം എന്ത്?",
 cap_en="The investor was tired of slides and asked to see the product work. An MVP is the smallest version that solves the main problem, chosen by a team that knows who the customer is, how money comes in and what investors look at. Nobody can promise funding, but you'll have something to show. What goes in your MVP first?",
 cap_mg="Slide alla, work cheyyunna onnu kaananam ennu investor paranjo? Pradhaana prashnam theerkkunna ettavum cheriya version aanu MVP. Funding aarkkum urappu parayaanaavilla, pakshe kaanikkaan onnu undaakum. Ningalude MVP-yil aadyam enthu?")

# crm (invented): a friend builds the app "on weekends"; a year later it is still half done
duo("wbd109", "mvp_founder", "B", "garage", "\"ശനിയും ഞായറും ചെയ്യാം\"\nകൂട്ടുകാരൻ പറഞ്ഞു.\nഒരു വർഷം, ആപ്പ് ഇല്ല", [
 ("A","wide","ജിതിനേ, നീ ശനിയും ഞായറും ചെയ്യാം എന്ന് പറഞ്ഞിട്ട് ഒരു വർഷമായി. ആപ്പ് ഇപ്പോഴും പകുതി."),
 ("V","V","ഐശ്വര്യേ, ഓഫീസ് പണി കഴിഞ്ഞ് സമയം കിട്ടുന്നില്ല. ക്ഷമിക്ക്."),
 ("A","A","നിന്നെ കുറ്റം പറയുന്നില്ല. പക്ഷേ ബിസിനസ് കാത്തിരിക്കില്ലല്ലോ."),
 ("V","V","ശരിയാ. ബിസിനസ് മനസ്സിലാക്കി ശരിയായി ഉണ്ടാക്കുന്ന ടീമിന് കൊടുക്ക്. ഒറ്റയടിക്ക് വലിയ തുക ഇല്ലെങ്കിൽ മാസ തവണയായി അടയ്ക്കാം."),
 ("A","wide","എത്ര, എങ്ങനെ എന്ന് അവർ കോളിൽ പറയും. ഞാൻ ഇന്ന് വിളിക്കാം."),
 ("V","wide","സൗഹൃദം നിലനിർത്ത്, പ്രോജക്റ്റ് ടീമിന് കൊടുക്ക്.")],
 "സൗഹൃദം കൂട്ടുകാരന്,\nപ്രോജക്റ്റ് ടീമിന്", CTA_WEBPLAN, theme="crm",
 cap_ml="കൂട്ടുകാരൻ ഒഴിവുസമയത്ത് ഉണ്ടാക്കുന്ന ആപ്പ് ഒരു വർഷമായിട്ടും പകുതിയാണോ? ബിസിനസ് മനസ്സിലാക്കി ഉണ്ടാക്കുന്ന ടീമിന് കൊടുക്കൂ, മാസ തവണയായി അടയ്ക്കാം; കൃത്യം ടീം കോളിൽ പറയും. ഈ റീൽ ആർക്ക് അയക്കും?",
 cap_en="A friend offered to build the app on weekends, and a year later it is still half done. Keep the friendship and give the project to a team that understands the business, paid in monthly parts; the team quotes on a call. Who needs to see this?",
 cap_mg="Koottukaaran ozhivusamayathu undaakkunna app oru varshamaayittum pakuthiyaano? Business manassilaakki undaakkunna team-inu kodukku, maasa thavanayaayi adaykkaam; krithyam team call-il parayum. Ee reel aarkku ayakkum?")

# new: three shops' sales typed into a sheet every night - an automation
duo("wbd110", "ops_software", "A", "shop", "മൂന്ന് കട.\nരാത്രി 11 മണിക്ക്\nകണക്ക് ടൈപ്പിംഗ്", [
 ("A","wide","സുരേഷേ, എന്നും രാത്രി പതിനൊന്ന് മണിക്ക് മൂന്ന് കടയിലെയും വിൽപ്പന ഞാൻ ഷീറ്റിൽ ടൈപ്പ് ചെയ്യുന്നു."),
 ("V","V","ബിനൂ, ബില്ലിംഗിൽ ഉള്ള അതേ കണക്ക് അല്ലേ നീ വീണ്ടും ടൈപ്പ് ചെയ്യുന്നത്?"),
 ("A","A","അതെ. ചിലപ്പോൾ തെറ്റും. പിന്നെ പിറ്റേന്നത്തെ സ്റ്റോക്ക് ഓർഡറും തെറ്റും."),
 ("V","V","എല്ലാ ദിവസവും ഒരേ രീതിയിൽ ചെയ്യുന്ന പണി ഒരു ഓട്ടോമേഷന് കൊടുക്കാം. മൂന്ന് കടയുടെയും കണക്ക് ഒരിടത്ത് സ്വയം വരുന്ന രീതിയിൽ."),
 ("A","wide","അപ്പോ രാത്രി ഞാൻ ഉറങ്ങും, കണക്ക് സിസ്റ്റം നോക്കും."),
 ("V","wide","ദിവസവും ഒരേ പണിയാണെങ്കിൽ, അത് മെഷീന്റെ പണി.")],
 "ദിവസവും ഒരേ പണി?\nഅത് ഓട്ടോമേഷന്", CTA_WEBPLAN, theme="new",
 cap_ml="എല്ലാ ദിവസവും ഒരേ രീതിയിൽ ചെയ്യുന്ന പണി, ഉദാഹരണത്തിന് ബില്ലിലെ കണക്ക് വീണ്ടും ഷീറ്റിൽ ടൈപ്പ് ചെയ്യുന്നത്, ഒരു ഓട്ടോമേഷന് കൊടുക്കാം. നിങ്ങൾ ദിവസവും ആവർത്തിക്കുന്ന പണി ഏത്?",
 cap_en="Every night at 11, the owner retypes the day's sales from three shops into a sheet, and the mistakes flow into the next day's stock order. Work done the same way every day is a job for an automation, built around how your shops run. What do you repeat every day?",
 cap_mg="Ella divasavum ore reethiyil cheyyunna pani, udaaharanathinu bill-ile kanakku veendum sheet-il type cheyyunnathu, oru automation-inu kodukkaam. Ningal divasavum aavarthikkunna pani ethu?")

# faq: the app is ready but payments aren't live - payments and KYC are part of building it (FACTS_WEB: gateways ask app details)
duo("wbd111", "app_idea", "B", "mobileshop", "ആപ്പ് റെഡി.\nപേയ്മെന്റ് ബട്ടൺ\nലൈവ് അല്ല", [
 ("A","wide","വരുണേ, ബൈക്ക് റെന്റൽ ആപ്പ് റെഡി. പക്ഷേ പേയ്മെന്റ് ലൈവ് ആയിട്ടില്ല. ഡെവലപ്പർ പറയുന്നു, അത് അവന്റെ പണിയല്ല എന്ന്."),
 ("V","V","ഹന്നേ, ഗേറ്റ്‌വേ KYC-യിൽ സാധാരണ ആപ്പിന്റെ വിവരവും ബിസിനസ് രേഖകളും ചോദിക്കും. അത് തുടക്കത്തിലേ ആലോചിക്കണമായിരുന്നു."),
 ("A","A","കോഡ് മാത്രമല്ല, പേയ്മെന്റും രേഖയും ഒക്കെ ആപ്പിന്റെ ഭാഗമാണോ?"),
 ("V","V","ബിസിനസ് അറിയുന്ന ടീം ആദ്യമേ ചോദിക്കും: പൈസ എങ്ങനെ വരും, ഏത് പേരിൽ, എന്ത് രേഖ. എന്നിട്ടാണ് ബട്ടൺ ഉണ്ടാക്കുന്നത്."),
 ("A","wide","ബട്ടൺ ഉണ്ടാക്കാൻ എളുപ്പം. പൈസ വരുന്ന വഴിയാണ് ആലോചിക്കേണ്ടത്.")],
 "ആപ്പിന് മുമ്പ്\nപൈസയുടെ വഴി", CTA_WEBPLAN, theme="faq",
 cap_ml="ആപ്പ് റെഡി, പക്ഷേ പേയ്മെന്റ് ലൈവ് അല്ലേ? ഗേറ്റ്‌വേ KYC-യിൽ സാധാരണ ആപ്പ് വിവരവും ബിസിനസ് രേഖകളും ചോദിക്കും. ബിസിനസ് അറിയുന്ന ടീം അത് തുടക്കത്തിലേ ആലോചിക്കും. നിങ്ങളുടെ ആപ്പിൽ പൈസ എങ്ങനെ വരും?",
 cap_en="The bike rental app is ready, but payments aren't live and the developer says that's not his job. Payment gateways commonly ask for app details and business documents during KYC, so a business-first team plans how money comes in, in whose name, before building the button. How will money come into your app?",
 cap_mg="App ready, pakshe payment live alle? Gateway KYC-yil saadhaarana app vivaravum business rekhakalum chodikkum. Business ariyunna team athu thudakkathile aalochikkum. Ningalude app-il paisa engane varum?", names=("ഹന്ന", "വരുൺ"))

# crm (#8 style, invented): a home pickle seller loses orders inside Instagram messages
duo("wbd112", "online_shop", "A", "courier", "ഇൻസ്റ്റഗ്രാമിൽ 40 ഓർഡർ.\nപാക്ക് ചെയ്തത് 36.\nനാലെണ്ണം എവിടെ?", [
 ("A","wide","അരവിന്ദേ, അച്ചാർ ഓർഡർ നാല്പതെണ്ണം ഇൻസ്റ്റഗ്രാം മെസ്സേജിൽ വന്നു. പാക്ക് ചെയ്തത് മുപ്പത്താറ്. നാലെണ്ണം വിട്ടുപോയി!"),
 ("V","V","ജയേച്ചീ, മെസ്സേജിൽ ഓർഡർ എടുക്കുമ്പോൾ ഇത് പതിവാ. ആര്, എന്ത്, എവിടെ എന്ന് ഒരിടത്ത് ഇല്ല."),
 ("A","A","അപ്പോ ഇൻസ്റ്റഗ്രാം വിടണോ?"),
 ("V","V","വേണ്ട. ഇൻസ്റ്റഗ്രാമിൽ കാണിക്കാം, ഓർഡർ സ്വന്തം സൈറ്റിൽ എടുക്കാം. ഓരോ ഓർഡറും പേരും അഡ്രസും സഹിതം ഒരു ലിസ്റ്റിൽ വരും."),
 ("A","wide","പേജിന് എന്ത് പറ്റിയാലും ഓർഡർ ലിസ്റ്റ് നമ്മുടേത്."),
 ("V","wide","ഇൻസ്റ്റഗ്രാം ഷോറൂം, സൈറ്റ് ഓർഡർ കൗണ്ടർ.")],
 "ഇൻസ്റ്റഗ്രാം ഷോറൂം,\nസൈറ്റ് ഓർഡർ കൗണ്ടർ", CTA_WEBSITE, theme="crm",
 cap_ml="ഇൻസ്റ്റഗ്രാം മെസ്സേജിൽ ഓർഡർ വിട്ടുപോകുന്നുണ്ടോ? ഇൻസ്റ്റഗ്രാമിൽ കാണിക്കൂ, ഓർഡർ സ്വന്തം സൈറ്റിൽ എടുക്കൂ: ഓരോ ഓർഡറും പേരും അഡ്രസും സഹിതം ഒരു ലിസ്റ്റിൽ. നിങ്ങൾക്ക് കഴിഞ്ഞ മാസം എത്ര ഓർഡർ വിട്ടുപോയി?",
 cap_en="Forty pickle orders came in through Instagram messages; thirty-six were packed. Keep Instagram as the showroom and take orders on your own site, so every order lands in one list with name and address, and the list stays yours whatever happens to the page. How many orders slipped last month?",
 cap_mg="Instagram message-il order vittupokunnundo? Instagram-il kaanikku, order swantham site-il edukku: oro order-um perum addressum sahitham oru list-il. Ningalkku kazhinja maasam ethra order vittupoyi?")

# new: a photographer couple double-booked a wedding date - a small booking calendar system
duo("wbd113", "service_business", "B", "balcony", "ഒരേ ദിവസം\nരണ്ട് കല്യാണം ബുക്ക്.\nക്യാമറ ഒന്ന്", [
 ("A","wide","വിവേകേ, ഡിസംബർ പതിനാലിന് നമ്മൾ രണ്ട് കല്യാണം ബുക്ക് ചെയ്തു എന്ന് ഇപ്പോഴാ കണ്ടത്!"),
 ("V","V","അമ്മൂ, ഒന്ന് നീ ഫോണിൽ എടുത്തു, മറ്റേത് ഞാൻ ഇൻസ്റ്റഗ്രാമിൽ. രണ്ടും ഡയറിയിൽ കയറിയില്ല."),
 ("A","A","ഇനി ഒരു കുടുംബത്തോട് സോറി പറയണം. അഡ്വാൻസും തിരിച്ച് കൊടുക്കണം."),
 ("V","V","ബുക്കിംഗ് എവിടെ നിന്ന് വന്നാലും ഒരു കലണ്ടറിൽ കയറുന്ന ചെറിയ സിസ്റ്റം വേണം. ബുക്ക് ആയ ദിവസം വീണ്ടും കൊടുക്കാൻ പറ്റാത്ത രീതിയിൽ."),
 ("A","wide","നമ്മുടെ പണി ഫോട്ടോ എടുക്കൽ. ഓർമ സിസ്റ്റം നോക്കട്ടെ."),
 ("V","wide","ഒരു ദിവസം, ഒരു ബുക്കിംഗ്, ഒരു കലണ്ടർ.")],
 "എല്ലാ ബുക്കിംഗും\nഒരു കലണ്ടറിൽ", CTA_WEBPLAN, theme="new",
 cap_ml="ഫോണിലും ഇൻസ്റ്റഗ്രാമിലും ഡയറിയിലും ബുക്കിംഗ് ചിതറിയാൽ ഒരേ ദിവസം രണ്ട് ബുക്കിംഗ് വരും. എവിടെ നിന്ന് വന്നാലും ഒരു കലണ്ടറിൽ കയറുന്ന ചെറിയ സിസ്റ്റം നിങ്ങളുടെ രീതിക്ക് ഉണ്ടാക്കാം. നിങ്ങൾക്ക് എപ്പോഴെങ്കിലും ഡബിൾ ബുക്കിംഗ് പറ്റിയോ?",
 cap_en="One booking came by phone, the other on Instagram, neither reached the diary, and now two weddings share one date. A small system that puts every booking, wherever it comes from, into one calendar and blocks a date once taken fixes that. Ever been double-booked?",
 cap_mg="Phone-ilum Instagram-ilum diary-yilum booking chithariyaal ore divasam randu booking varum. Evide ninnu vannaalum oru calendar-il kayarunna cheriya system ningalude reethikku undaakkaam. Ningalkku eppozhenkilum double booking pattiyo?")

# faq: a site made years ago for computers, unreadable on phones
duo("wbd114", "old_website", "A", "veranda", "സൈറ്റ് തുറന്നാൽ\nഫോണിൽ അക്ഷരം\nഉറുമ്പിനെപ്പോലെ", [
 ("A","wide","ബാലേട്ടാ, നമ്മുടെ എണ്ണയുടെ സൈറ്റ് ഫോണിൽ തുറന്നപ്പോൾ അക്ഷരം ഉറുമ്പിനെപ്പോലെ. വിരൽ വെച്ച് വലുതാക്കണം."),
 ("V","V","ശാന്തേ, കൊല്ലങ്ങൾക്ക് മുമ്പ് കമ്പ്യൂട്ടറിൽ നോക്കാൻ ഉണ്ടാക്കിയതാ. അന്ന് ആര് ഫോണിൽ നോക്കി?"),
 ("A","A","ഇപ്പോൾ എല്ലാവരും ഫോണിലാ. നമ്മുടെ പഴയ കസ്റ്റമേഴ്സ് പോലും."),
 ("V","V","എങ്കിൽ സൈറ്റ് ഫോണിന് ചേരുന്നതാകണം. അക്ഷരം വായിക്കാം, ബട്ടൺ തൊടാം, പെട്ടെന്ന് തുറക്കണം. പഴയത് പുതുക്കാം."),
 ("A","wide","എണ്ണ പഴയ രീതിയിൽ, സൈറ്റ് പുതിയ രീതിയിൽ.")],
 "എണ്ണ പഴയ രീതി,\nസൈറ്റ് പുതിയ രീതി", CTA_WEBSITE, theme="faq",
 cap_ml="പഴയ സൈറ്റ് ഫോണിൽ തുറക്കുമ്പോൾ അക്ഷരം വലുതാക്കി നോക്കണോ? ഇന്ന് കസ്റ്റമർ ഫോണിലാണ്: വായിക്കാവുന്ന അക്ഷരം, തൊടാവുന്ന ബട്ടൺ, പെട്ടെന്ന് തുറക്കുന്ന പേജ്. നിങ്ങളുടെ സൈറ്റ് ഫോണിൽ അവസാനം നോക്കിയത് എപ്പോൾ?",
 cap_en="An ayurvedic oil maker's site was built years ago for computers, and on a phone you have to pinch to read it. Customers are on phones now: readable text, tappable buttons, fast-loading pages. When did you last open your site on a phone?",
 cap_mg="Pazhaya site phone-il thurakkumbol aksharam valuthaakki nokkano? Innu customer phone-ilaanu: vaayikkaavunna aksharam, thodaavunna button, pettennu thurakkunna page. Ningalude site phone-il avasaanam nokkiyathu eppol?")

# crm (#26 style, invented): a Gulf returnee wants a big travel app on day one; start with a site that matches how his customers book
duo("wbd115", "no_website", "B", "airport", "ദുബായിൽ നിന്ന് വന്നു.\nആദ്യ ദിവസം തന്നെ\nവലിയ ആപ്പ് വേണം", [
 ("A","wide","റഫീഖേ, നാട്ടിൽ ടൂർ ബിസിനസ് തുടങ്ങുവാ. വലിയ ട്രാവൽ ആപ്പുകൾ പോലെ ഒരെണ്ണം ആദ്യം തന്നെ വേണം."),
 ("V","V","ഷമീറേ, ആദ്യ മാസം നിന്റെ കസ്റ്റമർ ആരായിരിക്കും? അവർ എങ്ങനെ ബുക്ക് ചെയ്യാനാണ് ഇഷ്ടപ്പെടുന്നത്?"),
 ("A","A","ഗൾഫിലെ കൂട്ടുകാരും അവരുടെ ഫാമിലിയും. അവർ വാട്സാപ്പിൽ ചോദിക്കും."),
 ("V","V","എങ്കിൽ ആദ്യം പാക്കേജും ഫോട്ടോയും വാട്സാപ്പ് ബട്ടണും ഉള്ള നല്ല സൈറ്റ്, ബിസിനസ് പേരിൽ ഡൊമെയ്ൻ. ആപ്പ് ആവശ്യം വരുമ്പോൾ."),
 ("A","wide","അപ്പോ ആദ്യ പടി സൈറ്റ്, ആപ്പ് അടുത്ത പടി."),
 ("V","wide","ബിസിനസ് വളരുമ്പോൾ ടെക്കും വളരട്ടെ.")],
 "ബിസിനസ് വളരുമ്പോൾ\nടെക്കും വളരട്ടെ", CTA_WEBSITE, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് വന്ന് ബിസിനസ് തുടങ്ങുമ്പോൾ ആദ്യ ദിവസം തന്നെ വലിയ ആപ്പ് വേണോ? നിങ്ങളുടെ കസ്റ്റമർ എങ്ങനെ ബുക്ക് ചെയ്യുന്നു എന്ന് നോക്കി തുടങ്ങൂ: ബിസിനസ് പേരിൽ ഡൊമെയ്നും വാട്സാപ്പ് ബട്ടണും ഉള്ള സൈറ്റ്. ആപ്പ് ആവശ്യം വരുമ്പോൾ. ഈ റീൽ ഏത് പ്രവാസിക്ക് അയക്കും?",
 cap_en="Back from Dubai to start a tour business, he wants an app like the big travel apps on day one. Start from how your first customers actually book: a good site with packages, photos, a WhatsApp button and a domain in the business's name, and an app when the business needs one. Which returnee friend needs this?",
 cap_mg="Gulf-il ninnu vannu business thudangumbol aadya divasam thanne valiya app veno? Ningalude customer engane book cheyyunnu ennu nokki thudangu: business peril domain-um WhatsApp button-um ulla site. App aavashyam varumbol. Ee reel ethu pravaasikku ayakkum?")

# new: a workshop's customers forget the next service; an automatic reminder (no promised result)
duo("wbd116", "ops_software", "A", "petrolpump", "ബുക്കിൽ 800 നമ്പർ.\nആരെയും വിളിച്ചില്ല.\nവണ്ടി വന്നില്ല", [
 ("A","wide","ഷിബൂ, കഴിഞ്ഞ വർഷം നമ്മുടെ വർക്ക്ഷോപ്പിൽ സർവീസ് ചെയ്ത വണ്ടികളിൽ പലതും പിന്നെ വന്നിട്ടില്ല."),
 ("V","V","സന്തോഷേ, അടുത്ത സർവീസ് സമയമായി എന്ന് ആരെങ്കിലും അവരെ ഓർമിപ്പിച്ചോ?"),
 ("A","A","നമ്പർ ബുക്കിൽ ഉണ്ട്. പക്ഷേ ഓരോരുത്തരെയും വിളിക്കാൻ സമയം എവിടെ?"),
 ("V","V","അതിനാണ് ഓട്ടോമേഷൻ. സർവീസ് തീയതി ഒരിക്കൽ കയറ്റിയാൽ, സമയമാകുമ്പോൾ കസ്റ്റമർക്ക് സ്വയം ഒരു മെസ്സേജ് പോകുന്ന രീതി."),
 ("A","wide","വരണോ വേണ്ടയോ എന്ന് അവർ തീരുമാനിക്കട്ടെ. ഓർമിപ്പിക്കൽ നമ്മുടെ ഭാഗം."),
 ("V","wide","നമ്മൾ മറന്നാലും, സിസ്റ്റം മറക്കില്ല.")],
 "നമ്മൾ മറന്നാലും\nസിസ്റ്റം മറക്കില്ല", CTA_WEBPLAN, theme="new",
 cap_ml="ബുക്കിൽ നൂറുകണക്കിന് കസ്റ്റമർ നമ്പർ, പക്ഷേ ആരെയും ഓർമിപ്പിക്കാൻ സമയമില്ലേ? സർവീസ് തീയതി കയറ്റിയാൽ സമയമാകുമ്പോൾ സ്വയം മെസ്സേജ് പോകുന്ന ഓട്ടോമേഷൻ നിങ്ങളുടെ രീതിക്ക് ഉണ്ടാക്കാം. നിങ്ങളുടെ കസ്റ്റമർ നമ്പറുകൾ ഇപ്പോൾ എവിടെ?",
 cap_en="Eight hundred numbers in the workshop book, and nobody reminded them about the next service. An automation can send each customer a message when their service date comes up, once the date is entered, built around how your workshop runs. Where do your customer numbers sit today?",
 cap_mg="Book-il noorukanakkinu customer number, pakshe aareyum ormippikkaan samayamille? Service theeyathi kayattiyaal samayamaakumbol swayam message pokunna automation ningalude reethikku undaakkaam. Ningalude customer numbers ippol evide?")

# new: an expired box of medicine behind the shelf - start with the one problem that hurts most
duo("wbd117", "ops_software", "B", "pharmacy", "അലമാരയുടെ പിന്നിൽ\nകാലാവധി കഴിഞ്ഞ\nഒരു പെട്ടി മരുന്ന്", [
 ("A","wide","പ്രവീണേ, സ്റ്റോക്ക് എടുത്തപ്പോൾ പിന്നിലെ അലമാരയിൽ കാലാവധി കഴിഞ്ഞ ഒരു പെട്ടി മരുന്ന്!"),
 ("V","V","സിനീ, ഓരോ ബാച്ചിന്റെയും തീയതി ആർക്കും ഓർത്തുവെക്കാൻ പറ്റില്ല. ബുക്കിൽ എഴുതിയത് ആരും നോക്കുന്നുമില്ല."),
 ("A","A","വലിയ ഫാർമസി സോഫ്റ്റ്‌വെയർ നമുക്ക് വേണോ?"),
 ("V","V","വലുത് വേണ്ട. നമ്മുടെ ഏറ്റവും വലിയ പ്രശ്നം തീർക്കുന്നത് മതി: തീയതി അടുക്കുമ്പോൾ ഒരു മുന്നറിയിപ്പ്. പിന്നെ ആവശ്യം പോലെ കൂട്ടാം."),
 ("A","wide","ഒറ്റയടിക്ക് വലിയ തുക വേണ്ട, മാസ തവണയായും ചെയ്യാം എന്ന് കേട്ടു."),
 ("V","wide","ആദ്യം ഏറ്റവും വേദനിക്കുന്ന പ്രശ്നം.")],
 "ആദ്യം ഏറ്റവും\nവേദനിക്കുന്ന പ്രശ്നം", CTA_WEBPLAN, theme="new",
 cap_ml="വലിയ സോഫ്റ്റ്‌വെയർ അല്ല, നിങ്ങളുടെ ഏറ്റവും വലിയ പ്രശ്നം തീർക്കുന്ന ചെറിയ ഒന്ന് ആദ്യം: ഉദാഹരണത്തിന് കാലാവധി അടുക്കുമ്പോൾ മുന്നറിയിപ്പ്. പിന്നെ ആവശ്യം പോലെ കൂട്ടാം, മാസ തവണയായി. നിങ്ങളുടെ കടയിലെ ഏറ്റവും വലിയ തലവേദന ഏത്?",
 cap_en="A whole box of expired medicine turned up behind the shelf. You don't need a huge system first: start with the one thing that hurts most, like an alert as expiry dates come close, then add as you need, paid in monthly parts. What's the biggest headache in your shop?",
 cap_mg="Valiya software alla, ningalude ettavum valiya prashnam theerkkunna cheriya onnu aadyam: udaaharanathinu kaalaavadhi adukkumbol munnariyippu. Pinne aavashyam pole koottaam, maasa thavanayaayi. Ningalude kadayile ettavum valiya thalavedana ethu?")

# faq myth: "MVP means a half-built, buggy app" - it means small, not broken
duo("wbd118", "mvp_founder", "A", "gym", "MVP എന്നാൽ\nപകുതി ഉണ്ടാക്കിയ\nആപ്പ്? അല്ല", [
 ("A","wide","ജസ്റ്റിനേ, MVP എന്ന് പറഞ്ഞാൽ പകുതി പണി ചെയ്ത, ബഗ് നിറഞ്ഞ ആപ്പ് അല്ലേ?"),
 ("V","V","അഞ്ജനേ, അല്ല. ഒരു പ്രധാന പ്രശ്നം മാത്രം, പക്ഷേ അത് നന്നായി തീർക്കുന്ന ഏറ്റവും ചെറിയ വേർഷൻ."),
 ("A","A","അപ്പോ എന്റെ യോഗ ക്ലാസ് ആപ്പിൽ ആദ്യം എന്ത്?"),
 ("V","V","നിന്റെ ആളുകൾ ഏറ്റവും കൂടുതൽ ചോദിക്കുന്നത്. ക്ലാസ് ബുക്കിംഗ് ആണെങ്കിൽ അത് മാത്രം. ഫോണിൽ നന്നായി, വേഗത്തിൽ."),
 ("A","wide","ചെറുത്, പക്ഷേ പൊട്ടിയതല്ല."),
 ("V","wide","ചെറുതായി തുടങ്ങാം, പക്ഷേ മുഴുവനായി.")],
 "ചെറുത്,\nപക്ഷേ മുഴുവൻ", CTA_WEBPLAN, theme="faq",
 cap_ml="MVP എന്നാൽ പകുതി പണി ചെയ്ത ആപ്പ് അല്ല: ഒരു പ്രധാന പ്രശ്നം നന്നായി തീർക്കുന്ന ഏറ്റവും ചെറിയ വേർഷൻ, ഫോണിൽ നന്നായി, വേഗത്തിൽ. നിങ്ങളുടെ ആപ്പിലെ ആ ഒരു കാര്യം ഏത്?",
 cap_en="Myth: an MVP is a half-built, buggy app. It is the smallest version that solves one main problem properly, mobile-friendly and fast. For a yoga class app that might be class booking alone. What is the one thing in yours?",
 cap_mg="MVP ennaal pakuthi pani cheytha app alla: oru pradhaana prashnam nannaayi theerkkunna ettavum cheriya version, phone-il nannaayi, vegathil. Ningalude app-ile aa oru kaaryam ethu?", names=("അഞ്ജന", "ജസ്റ്റിൻ"))
