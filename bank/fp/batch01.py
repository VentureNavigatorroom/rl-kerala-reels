# Financial projections seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_FP. NEVER mention a fee. fpd001 built on STORY_THEMES #12 with changed sector and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

duo("fpd001", "investor_pitch", "A", "weddinghall", "മൂന്നാം വർഷം 500 കോടി.\nഇൻവെസ്റ്റർ ചിരിച്ചു.\nപിച്ച് തീർന്നു", [
 ("A","wide","ശരത്തേ, വെഡ്ഡിംഗ് പ്ലാനിംഗ് ആപ്പിന്റെ പിച്ചിൽ ഇൻവെസ്റ്റർ ചിരിച്ചു. മൂന്നാം വർഷം 500 കോടി എന്ന് ഞാൻ കാണിച്ചു."),
 ("V","V","കാവ്യേ, ഇതുവരെ എത്ര കല്യാണം ബുക്ക് ചെയ്തു?"),
 ("A","A","പന്ത്രണ്ട്."),
 ("V","V","പന്ത്രണ്ടിൽ നിന്ന് അവിടേക്കുള്ള വഴി കാണിക്കണം. എത്ര ക്ലയന്റ്, ഒരാളിൽ നിന്ന് എത്ര, എത്ര വളർച്ച."),
 ("A","wide","പെരുപ്പിച്ച നമ്പർ വിശ്വാസം കളയും. ട്രാക്ഷനോട് ചേർന്ന നമ്പർ മതി."),
 ("V","wide","സ്വപ്നം വലുതാകട്ടെ, സ്പ്രെഡ്ഷീറ്റ് സത്യമാകട്ടെ.")],
 "നമ്പർ വലുതല്ല,\nവിശ്വസനീയം", CTA_PROJECTION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ നോക്കുന്നത് വലിയ നമ്പർ അല്ല, ട്രാക്ഷനോട് ചേർന്ന വിശ്വസനീയമായ പ്രോജക്ഷൻ: എത്ര ക്ലയന്റ്, ഒരാളിൽ നിന്ന് എത്ര, എത്ര വളർച്ച. പെരുപ്പിച്ച നമ്പർ വിശ്വാസം കളയും.",
 cap_en="A founder shows Rs 500 crore in year three with 12 customers today, and the investor laughs. Projections should be realistic and tied to traction: customers, revenue per customer, growth. Inflated numbers lose trust.",
 cap_mg="Investor nokkunnathu valiya number alla, traction-nodu chernna vishvasaneeyamaaya projection: ethra client, oraalil ninnu ethra, ethra valarcha. Peruppicha number vishvaasam kalayum.")

duo("fpd002", "bank_loan", "B", "akshaya", "ലോൺ ഫയൽ മടങ്ങി.\nമാനേജർ: \"പ്രോജക്റ്റ്\nറിപ്പോർട്ട് എവിടെ?\"", [
 ("A","wide","രമേശേട്ടാ, പപ്പടം യൂണിറ്റ് വലുതാക്കാനുള്ള ലോൺ ഫയൽ ബാങ്ക് തിരിച്ചുതന്നു."),
 ("V","V","സുധേ, എന്താ കാരണം പറഞ്ഞത്?"),
 ("A","A","പ്രോജക്റ്റ് റിപ്പോർട്ട് വേണമെന്ന്. അടുത്ത മൂന്ന് വർഷത്തെ കണക്ക്."),
 ("V","V","എത്ര ഉൽപ്പാദനം, എത്ര ചെലവ്, ലോൺ തിരിച്ചടയ്ക്കാനുള്ള ക്യാഷ് ഫ്ലോ. ബാങ്ക് നോക്കുന്നത് അതാണ്."),
 ("A","wide","ആദ്യ വർഷം മാസം തോറും, പിന്നെ വർഷം തോറും. എല്ലാം എഴുതി വെക്കാം."),
 ("V","wide","പപ്പടം പൊള്ളുന്നത് എണ്ണയിൽ, ലോൺ പൊള്ളുന്നത് കണക്കില്ലാതെ.")],
 "ലോണിന് മുമ്പ്\nകണക്ക്", CTA_FORECAST, theme="new",
 cap_ml="ബിസിനസ് ലോണിന് ബാങ്ക് പ്രോജക്റ്റ് റിപ്പോർട്ട് ചോദിക്കാം: 3 വർഷത്തെ ഉൽപ്പാദനം, ചെലവ്, തിരിച്ചടവിനുള്ള ക്യാഷ് ഫ്ലോ. ആദ്യ വർഷം മാസം തോറും. നിങ്ങൾ ലോണിന് അപേക്ഷിക്കാൻ പോകുന്നുണ്ടോ?",
 cap_en="A small papad unit's loan file comes back: the bank wants a project report. Three years of output, costs and the cash flow to repay, month by month for the first year. Are you planning a business loan?",
 cap_mg="Business loan-nu bank project report chodikkaam: 3 varshathe ulpaadanam, chelavu, thirichadavinulla cash flow. Aadya varsham maasam thorum. Ningal loan-nu apekshikkaan pokunnundo?")

duo("fpd003", "grant_application", "A", "farm", "ഗ്രാന്റ് ഫോമിൽ ഒരു കോളം:\n\"ബ്രേക്ക്-ഈവൻ എപ്പോൾ?\"\nഉത്തരമില്ല", [
 ("A","wide","ഗോപീ, ഹൈഡ്രോപോണിക്സ് ഫാമിന്റെ ഗ്രാന്റ് ഫോമിൽ ഒരു ചോദ്യം: ബ്രേക്ക്-ഈവൻ എപ്പോൾ?"),
 ("V","V","വാസുവേട്ടാ, ലാഭം വരുമ്പോൾ വരും. അതല്ലേ ഉത്തരം?"),
 ("A","A","അത് പാനലിന് പോരാ."),
 ("V","V","ചെലവ് എത്ര, ഓരോ മാസവും എത്ര വിൽക്കും, വരവും ചെലവും എപ്പോൾ ഒപ്പമെത്തും. അതാണ് ബ്രേക്ക്-ഈവൻ."),
 ("A","wide","എന്തുകൊണ്ട് ഈ നമ്പർ എന്ന അനുമാനങ്ങളും എഴുതി വെക്കണം."),
 ("V","wide","വിളവ് എപ്പോൾ എന്ന് കർഷകന് അറിയാം. കമ്പനിക്കും അറിയണം.")],
 "ബ്രേക്ക്-ഈവൻ\nഎപ്പോൾ?", CTA_PROJECTION, theme="new",
 cap_ml="ഗ്രാന്റ് പാനലുകൾ ഫിനാൻഷ്യൽ പ്രോജക്ഷൻ ചോദിക്കും: ചെലവ്, മാസവിൽപ്പന, ബ്രേക്ക്-ഈവൻ എപ്പോൾ, ഓരോ നമ്പറിന്റെയും അനുമാനം. നിങ്ങളുടെ ബിസിനസിന്റെ ബ്രേക്ക്-ഈവൻ എപ്പോൾ എന്ന് അറിയാമോ?",
 cap_en="A hydroponics farm's grant form asks: when do you break even? Grant panels expect projections with costs, monthly sales, break-even and written assumptions. Do you know your break-even month?",
 cap_mg="Grant panels financial projection chodikkum: chelavu, maasavilpana, break-even eppol, oro number-nteyum anumaanam. Ningalude business-nte break-even eppol ennu ariyaamo?")

duo("fpd004", "pre_revenue", "B", "park", "ഒരു രൂപ പോലും\nവരുമാനമില്ല.\nപിന്നെന്ത് ഫോർകാസ്റ്റ്?", [
 ("A","wide","അനന്തൂ, ഇൻവെസ്റ്റർ മൂന്ന് വർഷത്തെ ഫോർകാസ്റ്റ് ചോദിച്ചു. നമുക്ക് ഇതുവരെ ഒരു സെയിൽ പോലും ഇല്ലല്ലോ."),
 ("V","V","ഗായത്രീ, സെയിൽ ഇല്ലാത്തപ്പോഴാ അത് കൂടുതൽ വേണ്ടത്."),
 ("A","A","പിന്നെ എന്ത് വെച്ച് എഴുതും?"),
 ("V","V","എത്ര ഉപഭോക്താക്കൾ, ഒരാളിൽ നിന്ന് എത്ര, എത്ര വളർച്ച, എത്ര പേരെ ജോലിക്കെടുക്കും. ഓരോ അനുമാനവും എഴുതണം."),
 ("A","wide","ആദ്യ വർഷം മാസം തോറും, പിന്നെ രണ്ട് വർഷം."),
 ("V","wide","വരുമാനം പൂജ്യം ആകാം, പ്ലാൻ പൂജ്യമാകരുത്.")],
 "വരുമാനമില്ലെങ്കിലും\nഫോർകാസ്റ്റ് വേണം", CTA_FORECAST, theme="faq",
 cap_ml="വരുമാനം ഇല്ലാത്ത സ്റ്റാർട്ടപ്പിനും ഇൻവെസ്റ്റർ 3 വർഷത്തെ ഫോർകാസ്റ്റ് ചോദിക്കും: ഉപഭോക്താക്കൾ, വളർച്ച, ജോലിക്കാർ, എഴുതിയ അനുമാനങ്ങൾ. ആദ്യ വർഷം മാസം തോറും. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പിന് വരുമാനം തുടങ്ങിയോ?",
 cap_en="No revenue yet, so no forecast? Investors still ask for 3 years: customers, revenue per customer, growth and hiring, with written assumptions, month by month for year one. Has your startup started earning?",
 cap_mg="Varumaanam illaatha startup-num investor 3 varshathe forecast chodikkum: customers, valarcha, jolikkaar, ezhuthiya anumaanangal. Aadya varsham maasam thorum. Ningalude startup-nu varumaanam thudangiyo?")

duo("fpd005", "early_revenue", "A", "ferry", "കണക്കിൽ ലാഭം.\nഎന്നിട്ടും ശമ്പളം\nകൊടുക്കാൻ പൈസയില്ല", [
 ("A","wide","ടോണീ, കണക്ക് പ്രകാരം നമ്മുടെ ബോട്ട് ടൂർ കമ്പനി ലാഭത്തിലാ. പക്ഷേ ഈ മാസം ശമ്പളം കൊടുക്കാൻ അക്കൗണ്ടിൽ പൈസയില്ല."),
 ("V","V","മീരേ, ട്രാവൽ ഏജന്റുമാർ എപ്പോഴാ പണം തരുന്നത്?"),
 ("A","A","മൂന്ന് മാസം കഴിഞ്ഞ്."),
 ("V","V","അതാ കാര്യം. ലാഭം കടലാസിൽ, ക്യാഷ് അക്കൗണ്ടിൽ. പ്രോജക്ഷനിൽ ലാഭനഷ്ട കണക്ക് മാത്രമല്ല, ക്യാഷ് ഫ്ലോയും വേണം."),
 ("A","wide","ഇനി ഓരോ മാസവും പണം എപ്പോൾ വരും, എപ്പോൾ പോകും എന്ന് എഴുതാം."),
 ("V","wide","ഡീസൽ ഇല്ലെങ്കിൽ ലാഭം കരയിൽ നിൽക്കും.")],
 "ലാഭമുണ്ട്,\nക്യാഷ് ഇല്ല?", CTA_PROJECTION, theme="new",
 cap_ml="ലാഭവും ക്യാഷും രണ്ടാണ്. ക്ലയന്റുകൾ വൈകി പണം തന്നാൽ ലാഭത്തിലുള്ള കമ്പനിക്കും ശമ്പളം മുടങ്ങാം. പ്രോജക്ഷനിൽ ക്യാഷ് ഫ്ലോ മാസം തോറും വേണം. നിങ്ങളുടെ ക്ലയന്റുകൾ എത്ര ദിവസം കഴിഞ്ഞ് പണം തരും?",
 cap_en="Profitable on paper, but no cash for salaries because agents pay after three months. Profit and cash are different: projections need a monthly cash flow, not only a P&L. How long do your clients take to pay?",
 cap_mg="Laabhavum cash-um randaanu. Clients vaiki panam thannaal laabhathilulla company-kkum shambalam mudangaam. Projection-il cash flow maasam thorum venam. Ningalude clients ethra divasam kazhinju panam tharum?")

lst("fpl001", "investor_pitch", "B", "ഇൻവെസ്റ്റർ ആദ്യം\nനോക്കുന്ന 3 ഷീറ്റ്", [
 ("ലാഭനഷ്ട കണക്ക്", "3 വർഷം. ആദ്യ വർഷം മാസം തോറും."),
 ("ക്യാഷ് ഫ്ലോ", "പണം എപ്പോൾ വരും, എപ്പോൾ തീരും. ലാഭവും ക്യാഷും രണ്ടാണ്."),
 ("അനുമാനങ്ങൾ", "ഉപഭോക്താക്കൾ, വളർച്ച, ജോലിക്കാർ. ഓരോ നമ്പറിനും ഒരു കാരണം.")],
 "നിങ്ങളുടെ ഡെക്കിൽ\nഏതാണ് ഇല്ലാത്തത്?", CTA_PROJECTION, theme="faq",
 cap_ml="ഇൻവെസ്റ്റർ നോക്കുന്ന 3 ഷീറ്റ്: 3 വർഷത്തെ ലാഭനഷ്ട കണക്ക്, മാസം തോറുമുള്ള ക്യാഷ് ഫ്ലോ, എഴുതിയ അനുമാനങ്ങൾ. നിങ്ങളുടെ പിച്ച് ഡെക്കിൽ ഏതാണ് ഇല്ലാത്തത്: 1, 2, 3?",
 cap_en="Three sheets investors look at first: a 3-year P&L (monthly for year one), cash flow, and written assumptions behind every number. Which one is missing from your deck: 1, 2 or 3?",
 cap_mg="Investor nokkunna 3 sheet: 3 varshathe P&L, maasam thorumulla cash flow, ezhuthiya anumaanangal. Ningalude pitch deck-il ethaanu illaathathu: 1, 2, 3?")
