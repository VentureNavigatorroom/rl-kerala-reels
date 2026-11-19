# Financial projections batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FP. Never mention our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

duo("fp002", "investor_pitch", "A", "mall", "പിച്ച് റിജക്റ്റ്.\nകാരണം: \"വാലിഡേഷൻ\nഇല്ല, സെയിൽസ് ഇല്ല\"", [
 ("A","wide","ജാഫർ, ഇൻവെസ്റ്റർ മെയിൽ: 'മാർക്കറ്റ് വാലിഡേഷൻ ഇല്ല, സെയിൽസ് ഡാറ്റ ഇല്ല.' നമുക്ക് 300 കസ്റ്റമേഴ്സ് ഉണ്ടല്ലോ!"),
 ("V","V","സുമയ്യാ, ആ 300 നമ്മുടെ ഡെക്കിൽ എവിടെ? നമ്മൾ കാണിച്ചത് 5 വർഷത്തെ സ്വപ്നം മാത്രം."),
 ("A","A","അപ്പോ ഇനി എന്ത് കാണിക്കണം?"),
 ("V","wide","ഇന്നത്തെ കസ്റ്റമേഴ്സിൽ നിന്ന് തുടങ്ങണം. എത്ര പേർ, ഒരാളിൽ നിന്ന് എത്ര വരുമാനം, മാസം എത്ര വളർച്ച. ട്രാക്ഷനോട് ചേർന്ന നമ്പർ."),
 ("A","A","സ്വപ്നം അവസാനം, കസ്റ്റമർ ആദ്യം."),
 ("V","wide","300 കസ്റ്റമർ ഒളിപ്പിച്ച്, 3 കോടി കാണിച്ചു.")],
 "സ്വപ്നം അവസാനം,\nകസ്റ്റമർ ആദ്യം", CTA_PROJECTION, theme="crm",
 cap_ml="\"മാർക്കറ്റ് വാലിഡേഷൻ ഇല്ല\" എന്ന് പറഞ്ഞ് പിച്ച് റിജക്റ്റ്, പക്ഷേ 300 കസ്റ്റമേഴ്സ് ഉണ്ടായിരുന്നു. പ്രൊജക്ഷൻ ഇന്നത്തെ ട്രാക്ഷനിൽ നിന്ന് തുടങ്ങണം: കസ്റ്റമേഴ്സ്, ഒരാളിൽ നിന്നുള്ള വരുമാനം, വളർച്ച. നിങ്ങൾക്ക് ഇപ്പോൾ എത്ര കസ്റ്റമേഴ്സ്?",
 cap_en="A modest-fashion brand's pitch is rejected for 'no market validation, no sales data', though it had 300 paying customers. Projections should start from today's traction: customers, revenue per customer and growth. How many customers do you have today?",
 cap_mg="'Market validation illa' ennu paranju pitch reject, pakshe 300 customers undaayirunnu. Projection innathe traction-il ninnu thudanganam: customers, oraalil ninnulla varumaanam, valarcha. Ningalkku ippol ethra customers?")

duo("fp003", "early_revenue", "B", "munnar", "12 വർഷത്തെ ഏലത്തോട്ടം.\nഇൻവെസ്റ്റർ: \"നമ്പർ\nകാണിക്കൂ\" കയ്യിൽ ഡയറി", [
 ("A","wide","ബേസിലേ, ഇൻവെസ്റ്റർ 3 വർഷത്തെ പ്രൊജക്ഷൻ ചോദിച്ചു. എന്റെ കയ്യിൽ അപ്പന്റെ ഡയറി മാത്രം."),
 ("V","V","സെലിനേ, ആ ഡയറി ചെറിയ കാര്യമല്ല. 12 വർഷത്തെ വിളവും വിൽപ്പനയും അതിലില്ലേ?"),
 ("A","A","ഉണ്ട്. പക്ഷേ അത് ഭാവിയല്ലല്ലോ."),
 ("V","wide","ഭാവിയുടെ അടിത്തറ അതാണ്. കഴിഞ്ഞ വിൽപ്പനയിൽ നിന്ന് വിളവ്, ചെലവ്, ക്യാഷ് ഫ്ലോ. ഓരോ അനുമാനവും എഴുതി വെക്കണം."),
 ("A","A","അപ്പന്റെ ഡയറി ഇനി ഡാറ്റ."),
 ("V","wide","പഴയ കണക്കാണ് പുതിയ കണക്കിന്റെ വേര്.")],
 "പഴയ കണക്കാണ്\nപുതിയ കണക്കിന്റെ വേര്", CTA_FORECAST, theme="crm",
 cap_ml="വർഷങ്ങളായി നടക്കുന്ന ഫാം ബിസിനസ്, പക്ഷേ ഇൻവെസ്റ്റർക്ക് കാണിക്കാൻ നമ്പർ അടുക്കി വെച്ചിട്ടില്ല. കഴിഞ്ഞ വിൽപ്പനയാണ് 3 വർഷ പ്രൊജക്ഷന്റെ അടിത്തറ: വരുമാനം, ചെലവ്, ക്യാഷ് ഫ്ലോ, എഴുതിയ അനുമാനങ്ങൾ. നിങ്ങളുടെ കണക്ക് എവിടെയാണ്: ഡയറിയിലോ ഷീറ്റിലോ?",
 cap_en="A 12-year-old cardamom farm has an investor asking for projections and only a father's handwritten diary of sales. Past numbers are the base: revenue drivers, costs and cash flow for 3 years, with every assumption written down. Where are your numbers: diary or spreadsheet?",
 cap_mg="Varshangalaayi nadakkunna farm business, pakshe investor-kku kaanikkaan number adukki vechittilla. Kazhinja vilpanayaanu 3 varsha projection-nte adithara: varumaanam, chelavu, cash flow, ezhuthiya anumaanangal. Ningalude kanakku evideyaanu: diary-ilo sheet-ilo?")

duo("fp004", "investor_pitch", "C", "classroom", "\"ഇൻവെസ്റ്റർ ഏത്\nനമ്പറാണ് ആദ്യം\nനോക്കുന്നത്?\"", [
 ("A","wide","ആദർശേ, മെന്ററിംഗിന് വന്ന കുട്ടി ചോദിച്ചു, ഇൻവെസ്റ്റർ ഏത് നമ്പറാ ആദ്യം നോക്കുന്നതെന്ന്. നീ എന്ത് പറയും?"),
 ("V","V","നിമ്മീ, ലാഭം ആയിരിക്കും, അല്ലേ?"),
 ("A","A","അതിന് മുമ്പ് ലാഭം എവിടെ നിന്ന് വരും എന്ന്."),
 ("V","wide","അതായത് റെവന്യൂ ഡ്രൈവേഴ്സ്: എത്ര കസ്റ്റമേഴ്സ്, ഒരാളിൽ നിന്ന് എത്ര, മാസം എത്ര വളർച്ച. പിന്നെ ബ്രേക്ക്-ഈവൻ."),
 ("A","A","ഉത്തരം ഒരു സംഖ്യയല്ല, ഒരു കാരണം."),
 ("V","wide","ലാഭം റിസൾട്ട്. ഡ്രൈവേഴ്സ് സിലബസ്.")],
 "ലാഭം റിസൾട്ട്,\nഡ്രൈവേഴ്സ് സിലബസ്", CTA_PROJECTION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ആദ്യം നോക്കുന്നത് ലാഭമല്ല, ലാഭം എവിടെ നിന്ന് വരും എന്നതാണ്: കസ്റ്റമേഴ്സ്, ഒരാളിൽ നിന്നുള്ള വരുമാനം, വളർച്ച, പിന്നെ ബ്രേക്ക്-ഈവൻ. നിങ്ങളുടെ ബ്രേക്ക്-ഈവൻ മാസം അറിയാമോ?",
 cap_en="What do investors check first in your financials? Not profit, but where it comes from: revenue drivers (customers, revenue per customer, growth), then break-even. Do you know your break-even month: yes or no?",
 cap_mg="Investor aadyam nokkunnathu laabhamalla, laabham evide ninnu varum ennathaanu: customers, oraalil ninnulla varumaanam, valarcha, pinne break-even. Ningalude break-even maasam ariyaamo?")

duo("fp005", "investor_pitch", "A", "gulf", "ദുബായ് ഇൻവെസ്റ്റർ:\n\"നമ്പർ അയക്കൂ\"\n\"അടുത്ത ആഴ്ച ഇക്കാ\"", [
 ("A","wide","ഫൈസലേ, നിന്റെ മീൻ ഡെലിവറി സ്റ്റാർട്ടപ്പിന് ആ ഇൻവെസ്റ്റർ നമ്പർ ചോദിച്ചിട്ട് എത്ര ദിവസമായി?"),
 ("V","V","ഷിജുക്കാ, 3 ആഴ്ച. ഓരോ തവണയും 'അടുത്ത ആഴ്ച' എന്ന് പറഞ്ഞു."),
 ("A","A","ഇൻവെസ്റ്റർ കാത്തിരിക്കില്ല. ഡീൽ തണുക്കും."),
 ("V","wide","എന്താ റെഡിയാക്കി വെക്കേണ്ടത്?"),
 ("A","A","3 വർഷത്തെ പ്രൊജക്ഷൻ, ആദ്യ വർഷം മാസം തോറും. ലാഭനഷ്ടം, ക്യാഷ് ഫ്ലോ, അനുമാനങ്ങൾ. മീറ്റിംഗിന് മുമ്പ്."),
 ("V","wide","മീൻ ഫ്രഷ് ആകണം. നമ്പറും.")],
 "മീനും നമ്പറും\nഫ്രഷ് ആകണം", CTA_FORECAST, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ നമ്പർ ചോദിച്ചു, \"അടുത്ത ആഴ്ച\" പറഞ്ഞ് 3 ആഴ്ച പോയി. മീറ്റിംഗിന് മുമ്പ് തന്നെ 3 വർഷ പ്രൊജക്ഷൻ റെഡിയാക്കുക: ആദ്യ വർഷം മാസം തോറും, ലാഭനഷ്ടം, ക്യാഷ് ഫ്ലോ, അനുമാനങ്ങൾ. നിങ്ങളുടെ നമ്പർ ഇന്ന് അയക്കാൻ റെഡിയാണോ?",
 cap_en="An investor in Dubai asked a fish-delivery founder for numbers three weeks ago, and every answer was 'next week'. Deals cool down in the delay. Have 3-year projections ready before the meeting: monthly for year one, P&L, cash flow and assumptions. Could you send yours today: yes or no?",
 cap_mg="Investor number chodichu, 'adutha aazhcha' paranju 3 aazhcha poyi. Meeting-inu mumbu thanne 3 varsha projection ready aakkuka: aadya varsham maasam thorum, P&L, cash flow, anumaanangal. Ningalude number innu ayakkaan ready aano?")

duo("fp006", "pre_revenue", "B", "rooftop", "\"എല്ലാ മാസവും\nഡബിൾ\" ഇൻവെസ്റ്റർ\nചോദിച്ചു: എങ്ങനെ?", [
 ("A","wide","ശ്യാമേ, പെറ്റ് ഗ്രൂമിംഗ് വാനിന്റെ ഷീറ്റിൽ എല്ലാ മാസവും വരുമാനം ഡബിൾ ആക്കിയോ?"),
 ("V","V","ആര്യേ, ഗ്രാഫ് നല്ല ഭംഗിയുണ്ട്. മുകളിലേക്ക് മാത്രം."),
 ("A","A","ഒരു വാൻ, ഒരു ഗ്രൂമർ. ഡിസംബറിൽ 4,000 പട്ടികളെ എങ്ങനെ കുളിപ്പിക്കും?"),
 ("V","wide","ശരിയാ. ഓരോ വളർച്ചയ്ക്കും കാരണം എഴുതണം. പുതിയ വാൻ, പുതിയ ആളുകൾ, അതിന്റെ ചെലവ്."),
 ("A","A","വിശ്വസിക്കാവുന്ന നമ്പർ, വലിയ നമ്പറിനേക്കാൾ നല്ലത്."),
 ("V","wide","ഗ്രാഫ് മുകളിലേക്ക്, വിശ്വാസം താഴേക്ക്.")],
 "ഗ്രാഫ് മുകളിലേക്ക്,\nവിശ്വാസം താഴേക്ക്", CTA_PROJECTION, theme="faq",
 cap_ml="എല്ലാ മാസവും വരുമാനം ഡബിൾ എന്ന് പ്രൊജക്ഷനിൽ എഴുതിയോ? ഓരോ വളർച്ചയ്ക്കും കാരണവും ചെലവും (പുതിയ ആളുകൾ, ഉപകരണം) എഴുതണം. വിശ്വസിക്കാൻ പറ്റാത്ത നമ്പർ ഇൻവെസ്റ്ററുടെ വിശ്വാസം കളയും. നിങ്ങളുടെ വളർച്ചാ നിരക്ക് എത്ര?",
 cap_en="A pet-grooming van startup shows revenue doubling every month, with one van and one groomer. Every growth assumption needs a reason and the costs behind it (vans, hires). Inflated numbers lose investor trust. What growth rate did you assume?",
 cap_mg="Ellaa maasavum varumaanam double ennu projection-il ezhuthiyo? Oro valarchaykkum kaaranavum chelavum (puthiya aalukal, upakaranam) ezhuthanam. Viswasikkaan pattaatha number investor-ude viswaasam kalayum. Ningalude valarcha nirakku ethra?")

duo("fp007", "early_revenue", "C", "courier", "പ്രൊജക്ഷനിൽ 40 സിറ്റി.\nജോലിക്കാർ: 2 പേർ\nമാത്രം", [
 ("A","wide","അരവിന്ദേ, ഡെലിവറി സ്റ്റാർട്ടപ്പിന്റെ ഷീറ്റിൽ രണ്ടാം വർഷം 40 സിറ്റി. ശമ്പളം കൊടുക്കുന്നത് 2 പേർക്ക് മാത്രം."),
 ("V","V","ജയേ, ആദ്യം വരുമാനം കാണിക്കാം എന്ന് കരുതി. ആളുകളെ പിന്നെ നോക്കാം."),
 ("A","A","40 സിറ്റിയിൽ ആര് പാക്കറ്റ് എടുക്കും? നമ്മൾ രണ്ടുപേരും ബൈക്കിലോ?"),
 ("V","wide","ശരി. വരുമാനം വളരുമ്പോൾ ആര്, എപ്പോൾ, എത്ര ശമ്പളം എന്ന ഹയറിംഗ് പ്ലാനും ചെലവിൽ വരണം."),
 ("A","A","അല്ലെങ്കിൽ ലാഭം കാണുന്നത് ഷീറ്റിൽ മാത്രം."),
 ("V","wide","വരുമാനം 40 സിറ്റി, ടീം 2 ബൈക്ക്.")],
 "വരുമാനം വളരുമ്പോൾ\nടീമും ചെലവിൽ", CTA_PROJECTION, theme="faq",
 cap_ml="പ്രൊജക്ഷനിൽ വരുമാനം 40 സിറ്റിയിലേക്ക്, പക്ഷേ ജോലിക്കാർ 2 പേർ മാത്രം? വളർച്ചയ്ക്ക് വേണ്ട ഹയറിംഗും ശമ്പളവും ചെലവിൽ കാണിക്കണം. നിങ്ങളുടെ അടുത്ത ഹയർ എപ്പോൾ?",
 cap_en="A delivery startup projects 40 cities in year two but budgets salaries for just two people. Projections need a hiring plan in the costs: who, when and what it costs as revenue grows. When is your next hire?",
 cap_mg="Projection-il varumaanam 40 city-ilekku, pakshe jolikkaar 2 per maathram? Valarchaykku venda hiring-um shambalavum chelavil kaanikkanam. Ningalude adutha hire eppol?")

duo("fp008", "bank_loan", "A", "beach", "ഹൗസ്ബോട്ട് ലോൺ.\nപ്രൊജക്ഷനിൽ 12 മാസവും\nഒരേ വരുമാനം", [
 ("A","wide","നിഖിലേ, പുതിയ ഹൗസ്ബോട്ടിന്റെ ലോൺ ഫയലിൽ ജൂണിലും ജൂലൈയിലും ഡിസംബറിന്റെ അതേ ബുക്കിംഗ്?"),
 ("V","V","ദിവ്യേ, ആവറേജ് എടുത്തു. 12 കൊണ്ട് ഹരിച്ചു."),
 ("A","A","കർക്കിടകത്തിൽ ബോട്ടിൽ ടൂറിസ്റ്റുകളല്ല, മഴയാ."),
 ("V","wide","അതിനാണ് ആദ്യ വർഷം മാസം തോറും കാണിക്കുന്നത്. ഏത് മാസം പണം വരും, ഏത് മാസം EMI-ക്ക് ക്യാഷ് വേണം."),
 ("A","A","ആവറേജ് കൊണ്ട് മഴക്കാലം കടക്കില്ല."),
 ("V","wide","മഴയ്ക്ക് കണക്ക് അറിയില്ല, കണക്കിന് മഴ അറിയണം.")],
 "മഴയ്ക്ക് കണക്ക് അറിയില്ല,\nകണക്കിന് മഴ അറിയണം", CTA_FORECAST, theme="new",
 cap_ml="സീസണൽ ബിസിനസിന്റെ പ്രൊജക്ഷനിൽ 12 മാസവും ഒരേ വരുമാനം കാണിച്ചാൽ ബാങ്കിന് വിശ്വാസം വരില്ല. ആദ്യ വർഷം മാസം തോറുമുള്ള ക്യാഷ് ഫ്ലോ ഓഫ് സീസണും കാണിക്കണം. നിങ്ങളുടെ ബിസിനസിന് ഓഫ് സീസൺ ഉണ്ടോ?",
 cap_en="A houseboat loan file shows the same bookings in the monsoon as in December. A seasonal business needs month-by-month projections for the first year, so the bank sees when cash comes in and when the EMI needs covering. Does your business have an off-season: yes or no?",
 cap_mg="Seasonal business-nte projection-il 12 maasavum ore varumaanam kaanichaal bank-inu viswaasam varilla. Aadya varsham maasam thorumulla cash flow off season-um kaanikkanam. Ningalude business-inu off season undo?")

duo("fp009", "pre_revenue", "B", "home", "ഭാര്യ ചോദിച്ചു:\n\"എന്ന് മുതൽ ശമ്പളം?\"\nഉത്തരമില്ല", [
 ("A","wide","അരുണേ, ജോലി വിട്ട് സ്റ്റാർട്ടപ്പ് തുടങ്ങിയിട്ട് 8 മാസം. എന്ന് മുതലാ വീട്ടിൽ ശമ്പളം വരുന്നത്?"),
 ("V","V","സ്നേഹേ, ബിസിനസ് പിക്ക് ആകുമ്പോൾ."),
 ("A","A","അത് ഒരു തീയതിയല്ല. ഒരു മാസം പറ."),
 ("V","wide","ശരിയാ. ബ്രേക്ക്-ഈവൻ മാസം കണക്കാക്കണം. എത്ര കസ്റ്റമേഴ്സ് വന്നാൽ ചെലവ് തീരും, എത്ര മാസം എടുക്കും."),
 ("A","A","ഇൻവെസ്റ്റർ ചോദിക്കുന്നതും ഇതുതന്നെ."),
 ("V","wide","ഇൻവെസ്റ്ററെക്കാൾ കടുത്ത പാനൽ വീട്ടിലാണ്.")],
 "ഇൻവെസ്റ്ററെക്കാൾ\nകടുത്ത പാനൽ വീട്ടിൽ", CTA_FORECAST, theme="new",
 cap_ml="\"ബിസിനസ് പിക്ക് ആകുമ്പോൾ\" ഒരു തീയതിയല്ല. എത്ര കസ്റ്റമേഴ്സ് വന്നാൽ ചെലവ് തീരും, അത് ഏത് മാസം എന്ന ബ്രേക്ക്-ഈവൻ കണക്ക് ഇൻവെസ്റ്ററും വീട്ടുകാരും ചോദിക്കും. നിങ്ങളുടെ ബ്രേക്ക്-ഈവൻ ഏത് മാസം?",
 cap_en="Eight months after quitting his job, a founder's wife asks when a salary will come home, and 'when business picks up' is not a date. Work out your break-even month: how many customers cover your costs, and how long that takes. Investors ask the same. Which month is your break-even?",
 cap_mg="'Business pick aakumpol' oru theeyathiyalla. Ethra customers vannaal chelavu theerum, athu ethu maasam enna break-even kanakku investor-um veettukaarum chodikkum. Ningalude break-even ethu maasam?")

chat("fpc001", "investor_pitch", "C", "\"5 വർഷം, 20 ടാബ്,\nഎല്ലാം കൃത്യം\"\nഇൻവെസ്റ്റർ തുറന്നില്ല", ("അഞ്ജലി", "കിരൺ"), [
 (0,"കിരൺ, ഫിനാൻഷ്യൽ മോഡൽ റെഡി. 5 വർഷം, 20 ടാബ്. ദിവസം തോറുമുള്ള കണക്ക്."),
 (1,"അഞ്ജലീ, ഇൻവെസ്റ്റർ അത് തുറക്കാൻ പോലും സമയം എടുക്കില്ല."),
 (0,"അപ്പോ എത്ര വർഷം വേണം?"),
 (1,"3 വർഷം. ആദ്യ വർഷം മാസം തോറും. ലാഭനഷ്ടം, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ, എഴുതിയ അനുമാനങ്ങൾ."),
 (0,"20 ടാബിൽ നിന്ന് 4 ആയി."),
 (1,"കട്ടി കുറഞ്ഞാൽ കാര്യം തെളിയും.")],
 "3 വർഷം, ആദ്യ വർഷം\nമാസം തോറും", CTA_FORECAST, theme="faq",
 cap_ml="ഫിനാൻഷ്യൽ പ്രൊജക്ഷൻ എത്ര വർഷത്തേക്ക് വേണം? സാധാരണ 3 വർഷം, ആദ്യ വർഷം മാസം തോറും: ലാഭനഷ്ടം, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ, എഴുതിയ അനുമാനങ്ങൾ. നിങ്ങളുടെ മോഡലിൽ എത്ര ടാബ്?",
 cap_en="How many years should financial projections cover? Typically 3 years, month by month for year one: P&L, cash flow, break-even and written assumptions. A 20-tab, 5-year model with daily numbers often goes unread. How many tabs does your model have?",
 cap_mg="Financial projection ethra varshathekku venam? Saadhaarana 3 varsham, aadya varsham maasam thorum: P&L, cash flow, break-even, ezhuthiya anumaanangal. Ningalude model-il ethra tab?")

lst("fpl002", "grant_application", "A", "ഓരോ പ്രൊജക്ഷനിലും\nഎഴുതേണ്ട 3 അനുമാനം", [
 ("കസ്റ്റമേഴ്സ്", "മാസം എത്ര പേർ വരും, എവിടെ നിന്ന്."),
 ("ഒരാളിൽ നിന്നുള്ള വരുമാനം", "ഒരു കസ്റ്റമർ ഒരു മാസം എത്ര തരും."),
 ("വളർച്ചയും ടീമും", "എത്ര ശതമാനം വളർച്ച, അതിന് എത്ര പുതിയ ആളുകൾ.")],
 "നിങ്ങളുടെ ഷീറ്റിൽ\nഏതാണ് ഇല്ലാത്തത്?", CTA_PROJECTION, theme="faq",
 cap_ml="ഇൻവെസ്റ്റർ, ബാങ്ക്, ഗ്രാന്റ് പാനൽ: എല്ലാവരും നോക്കുന്ന 3 അനുമാനം. മാസം എത്ര കസ്റ്റമേഴ്സ്, ഒരാളിൽ നിന്ന് എത്ര വരുമാനം, വളർച്ചയും അതിന് വേണ്ട ടീമും. നിങ്ങളുടെ ഷീറ്റിൽ ഏതാണ് ഇല്ലാത്തത്: 1, 2, 3?",
 cap_en="Three assumptions every projection should spell out, for investors, banks and grant panels alike: customers per month, revenue per customer, and growth with the team it needs. Which is missing from your sheet: 1, 2 or 3?",
 cap_mg="Investor, bank, grant panel: ellaavarum nokkunna 3 anumaanam. Maasam ethra customers, oraalil ninnu ethra varumaanam, valarchayum athinu venda team-um. Ningalude sheet-il ethaanu illaathathu: 1, 2, 3?")
