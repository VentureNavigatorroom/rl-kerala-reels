# Company valuation batch 05 (20 Nov, month backlog). Facts only from topics.FACTS_VAL. Never state a value or a fee. People, firms and towns invented.
# crm scripts are built on STORY_THEMES #14 / #16 / #17 / #20 with changed sector, people and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

# CRM #16 (Gulf relative investing in a cousin's startup): money sent before any report
duo("qv034", "nri_share_issue", "A", "petrolpump", "ഒമാനിലെ മാമൻ\nപണം അയച്ചു.\n\"പേപ്പർ പിന്നെ മതി\"", [
 ("A","wide","ഷിബൂ, പമ്പിന്റെ അടുത്ത് EV ചാർജിംഗ് കമ്പനി. നിന്റെ ഒമാനിലെ മാമൻ ഷെയറിന് പണം അയക്കാം, പേപ്പർ പിന്നെ എന്ന്."),
 ("V","V","സന്തോഷേട്ടാ, മാമൻ NRI ആണ്. തിരികെ കൊണ്ടുപോകാവുന്ന റിപാട്രിയേഷൻ നിക്ഷേപമാണോ?"),
 ("A","A","അതേ. എത്ര ഷെയർ കൊടുക്കണം എന്ന് നമ്മൾ തീരുമാനിച്ചാൽ പോരേ?"),
 ("V","wide","പോരാ. ഫെയർ വാല്യുവിൽ താഴെ ഷെയർ പാടില്ല. CA, സെബി മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തണം."),
 ("A","A","അപ്പോ റിപ്പോർട്ട് ആദ്യം."),
 ("V","wide","മാമന്റെ സ്നേഹം പേപ്പറില്ലാതെ, ഷെയർ പേപ്പറോടെ.")],
 "സ്നേഹം പേപ്പറില്ലാതെ,\nഷെയർ പേപ്പറോടെ", CTA_VALUATION, theme="crm",
 cap_ml="ഗൾഫിലെ ബന്ധു റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ നാട്ടിലെ കമ്പനിയിൽ ഷെയർ എടുക്കുമ്പോൾ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാൻ പറ്റില്ല. CA, സെബി രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് അംഗീകൃത രീതിയിൽ സാക്ഷ്യപ്പെടുത്തണം. നിങ്ങളുടെ കുടുംബത്തിൽ ഗൾഫ് നിക്ഷേപകർ ഉണ്ടോ?",
 cap_en="When a Gulf relative invests in a Kerala company on a repatriation basis, shares cannot be issued below fair value, certified by a CA, SEBI-registered merchant banker or cost accountant using an accepted method. Get the report before the shares. Any Gulf investors in your family?",
 cap_mg="Gulf-ile relative repatriation basis-il naattile company-il share edukkumbol fair value-il thaazhe kodukkaan pattilla. CA, SEBI merchant banker, allenkil cost accountant certify cheyyanam. Ningalude family-il Gulf investors undo?")

# CRM #14 (many small investors): one rice mill, 25 neighbours
duo("qv035", "raising_round", "A", "akshaya", "25 അയൽക്കാർ.\nഓരോരുത്തർക്കും\nഷെയർ. കണക്ക് ആര്?", [
 ("A","wide","രമേശേ, നിന്റെ അരിമില്ലിന് 25 അയൽക്കാർ ചെറിയ തുക ഇടാൻ റെഡി എന്ന് കേട്ടു. ഷെയർ കൊടുക്കാനാ പ്ലാൻ?"),
 ("V","V","അതേ സുധേച്ചീ. ഓരോരുത്തർക്കും ഞാൻ തോന്നുന്ന ഒരു നിരക്കിൽ കൊടുക്കും."),
 ("A","A","തോന്നുന്ന നിരക്കോ? അങ്ങനെ പുതിയ ഷെയർ ഇറക്കാൻ പറ്റുമോ?"),
 ("V","V","അത് പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റ് ആണെന്ന് CA പറഞ്ഞു. രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം."),
 ("A","wide","അപ്പോ ഒരു റിപ്പോർട്ട്, എല്ലാവർക്കും ഒരേ അടിസ്ഥാനം."),
 ("V","wide","അയൽപക്കം നല്ലതാവാൻ കണക്ക് ഒന്നാവണം.")],
 "അയൽപക്കം നന്നാവാൻ\nകണക്ക് ഒന്നാവണം", CTA_VALUATION, theme="crm",
 cap_ml="അയൽക്കാരിൽ നിന്നും കൂട്ടുകാരിൽ നിന്നും ചെറിയ തുകകൾ വാങ്ങി പുതിയ ഷെയർ ഇറക്കുന്നത് പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റ് ആണെങ്കിൽ രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം. ഓരോരുത്തർക്കും തോന്നിയ നിരക്കല്ല. നിങ്ങളുടെ ബിസിനസിൽ ആരൊക്കെ നിക്ഷേപിക്കാൻ റെഡി?",
 cap_en="Taking small amounts from many neighbours or friends for new shares? A preferential allotment needs a registered valuer's report, not a rate that feels right for each person. Who wants to invest in your business?",
 cap_mg="Ayalkkaaril ninnum friends-il ninnum cheriya thuka vaangi puthiya share irakkunnathu preferential allotment aanenkil registered valuer report venam. Thonniya rate alla. Ningalude business-il aarokke invest cheyyaan ready?")

# CRM #17 (loan instead of equity): which one needs a valuation
duo("qv036", "raising_round", "A", "homestay", "ബാങ്ക് ലോണോ\nഇൻവെസ്റ്ററോ?\nഒന്നിന് മാത്രം കണക്ക്", [
 ("A","wide","ജോമോനേ, മൂന്ന് മുറി കൂടി പണിയാൻ ബാങ്ക് ലോൺ എടുക്കണോ, ആ ജർമ്മൻ ഗസ്റ്റ് പറഞ്ഞ നിക്ഷേപം എടുക്കണോ?"),
 ("V","V","ടീനേ, ലോൺ തിരിച്ചടയ്ക്കണം. നിക്ഷേപം എടുത്താൽ കമ്പനിയുടെ ഒരു ഭാഗം അവർക്ക്."),
 ("A","A","ഭാഗം എത്ര എന്ന് എങ്ങനെ അറിയും?"),
 ("V","wide","അതിനാണ് വാല്യുവേഷൻ. നിക്ഷേപം എടുക്കുമ്പോൾ വേണം. വിദേശ നിക്ഷേപമാണെങ്കിൽ ഫെയർ വാല്യുവിൽ താഴെ ഷെയർ പാടില്ല."),
 ("A","A","അപ്പോ ആദ്യം കണക്ക്, പിന്നെ തീരുമാനം."),
 ("V","wide","ലോൺ പലിശ ചോദിക്കും, ഇൻവെസ്റ്റർ ശതമാനം ചോദിക്കും.")],
 "ലോൺ പലിശ ചോദിക്കും,\nഇൻവെസ്റ്റർ ശതമാനം", CTA_WORTH, theme="crm",
 cap_ml="ലോൺ തിരിച്ചടയ്ക്കണം; ഇക്വിറ്റി നിക്ഷേപം എടുത്താൽ കമ്പനിയുടെ ഒരു ഭാഗം കൊടുക്കണം. എത്ര ഭാഗം എന്ന് അറിയാൻ വാല്യുവേഷൻ വേണം, വിദേശ നിക്ഷേപത്തിന് ഫെയർ വാല്യുവിൽ താഴെ ഷെയർ പാടില്ല. നിങ്ങൾ ഏതിലേക്ക്: ലോൺ അല്ലെങ്കിൽ ഇക്വിറ്റി?",
 cap_en="A loan is repaid; equity means giving up part of the company, and a valuation tells you how much. For foreign investment, shares cannot go below fair value. Which way are you leaning: loan or equity?",
 cap_mg="Loan thirichadaykkanam; equity eduthaal company-yude oru bhaagam kodukkanam. Ethra ennu ariyaan valuation venam, foreign investment-nu fair value-il thaazhe share paadilla. Ningal ethilekku: loan or equity?")

# CRM #20 (investor asks for a data room and the valuation basis): only an idea in the head
duo("qv037", "raising_round", "B", "hotellobby", "\"ഡാറ്റ റൂമും\nവാല്യുവേഷൻ അടിസ്ഥാനവും\nഅയക്കൂ\" കൈയിൽ ഐഡിയ", [
 ("A","wide","ജെയ്സണേ, വെഡ്ഡിംഗ് പ്ലാനിംഗ് ആപ്പിന് ഒരു ഇൻവെസ്റ്റർ മെയിൽ: ഡാറ്റ റൂം, പിന്നെ വാല്യുവേഷന്റെ അടിസ്ഥാനം."),
 ("V","V","നീതൂ, നമുക്ക് 6 മാസമായി. ലാഭം ഇല്ല. എന്ത് അടിസ്ഥാനം കാണിക്കും?"),
 ("A","A","ഒരു നമ്പർ പറഞ്ഞാൽ പോരേ?"),
 ("V","wide","പോരാ. തുടക്കത്തിലെ കമ്പനിക്ക് സമാന കമ്പനികളും സമാന ഇടപാടുകളും, പിന്നെ പ്രൊജക്ഷനും ആണ് അടിസ്ഥാനം."),
 ("A","A","അപ്പോ ആദ്യം നമ്മുടെ നമ്പറുകൾ എഴുതണം."),
 ("V","wide","ഐഡിയ തലയിൽ മതി, കണക്ക് ഫോൾഡറിൽ വേണം.")],
 "ഐഡിയ തലയിൽ മതി,\nകണക്ക് ഫോൾഡറിൽ", CTA_VALUATION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റ റൂമും വാല്യുവേഷന്റെ അടിസ്ഥാനവും ചോദിച്ചാൽ ഒരു നമ്പർ മാത്രം പോരാ. തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പുകൾക്ക് സമാന കമ്പനികളുമായുള്ള താരതമ്യവും പ്രൊജക്ഷനുമാണ് ആശ്രയം. നിങ്ങളുടെ നമ്പറുകൾ ഫോൾഡറിലാണോ തലയിലാണോ?",
 cap_en="When an investor asks for a data room and the basis of your valuation, a single number is not enough. Early startups lean on comparable companies and deals plus projections. Are your numbers in a folder or only in your head?",
 cap_mg="Investor data room-um valuation basis-um chodichaal oru number maathram poraa. Early startups-nu comparables-um projection-um aanu aashrayam. Ningalude numbers folder-ilaano thalayilaano?")

# FAQ: "ESOP is for big IT companies"
duo("qv038", "esop_plan", "A", "foodcourt", "8 പേരുള്ള കിച്ചൺ.\n\"ഇസോപ്പ് ഒക്കെ\nഇൻഫോപാർക്കിലല്ലേ?\"", [
 ("A","wide","ഡെന്നിസേ, നമ്മുടെ ക്ലൗഡ് കിച്ചണിലെ ഹെഡ് ഷെഫിന് ഷെയർ കൊടുത്ത് പിടിച്ചുനിർത്തണം."),
 ("V","V","മരിയേ, ഇസോപ്പ് ഒക്കെ വലിയ ഐടി കമ്പനികൾക്കല്ലേ? നമ്മൾ 8 പേരല്ലേ ഉള്ളൂ."),
 ("A","A","കമ്പനി ചെറുതാണ്. പക്ഷേ ഷെഫ് പോയാൽ ബിസിനസ് തീർന്നു."),
 ("V","wide","എങ്കിൽ ചെറിയ കമ്പനിക്കും ഇസോപ്പ് ആകാം. പക്ഷേ ഇസോപ്പ് ഇറക്കുമ്പോൾ വാല്യുവേഷൻ വേണം, ആ തീയതിയിലേക്ക്."),
 ("A","A","അപ്പോ ആദ്യം കണക്ക്, പിന്നെ ഷെഫിന് ഓഫർ."),
 ("V","wide","ഇസോപ്പിന് കമ്പനിയുടെ വലിപ്പമല്ല, കണക്കാണ് വേണ്ടത്.")],
 "ഇസോപ്പിന് വലിപ്പമല്ല,\nകണക്കാണ് വേണ്ടത്", CTA_VALUATION, theme="faq",
 cap_ml="ഇസോപ്പ് വലിയ ഐടി കമ്പനികൾക്ക് മാത്രമല്ല. 8 പേരുള്ള കിച്ചണിലും പ്രധാന ആളെ പിടിച്ചുനിർത്താൻ ഷെയർ നൽകാം; പക്ഷേ ഇസോപ്പ് ഇറക്കുമ്പോൾ ആ തീയതിയിലേക്കുള്ള വാല്യുവേഷൻ വേണം. നിങ്ങളുടെ ടീമിൽ പിടിച്ചുനിർത്തേണ്ട ഒരാൾ ഉണ്ടോ?",
 cap_en="ESOPs are not only for big IT companies. Even an 8-person cloud kitchen can offer shares to keep a key chef, but issuing ESOPs needs a valuation for that purpose and date. Is there one person your team cannot lose?",
 cap_mg="ESOP valiya IT company-kalkku maathramalla. 8 per ulla kitchen-ilum key chef-ine pidichunirthaan share kodukkaam; pakshe ESOP irakkumbol aa date-ilekkulla valuation venam. Ningalude team-il angane oraal undo?")

# FAQ: "the balance sheet says minus, so we are worth nothing"
duo("qv039", "raising_round", "B", "thattukada", "ബാലൻസ് ഷീറ്റിൽ\nമൈനസ്. \"കമ്പനിക്ക്\nമൂല്യം പൂജ്യം\"", [
 ("A","wide","ബിജൂ, നമ്മുടെ ബസ് ട്രാക്കിംഗ് ആപ്പിന്റെ ബാലൻസ് ഷീറ്റ് മൈനസ്. ആസ്തി രണ്ട് ലാപ്ടോപ്പ് മാത്രം."),
 ("V","V","സിജോ, അപ്പോ ഇൻവെസ്റ്ററോട് എന്ത് മൂല്യം പറയും? പൂജ്യം അല്ലേ?"),
 ("A","A","ആസ്തി മാത്രം നോക്കിയാൽ അങ്ങനെ തോന്നും."),
 ("V","wide","ആസ്തി മൂല്യം ഒരു രീതി മാത്രം. തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പിന് സമാന കമ്പനികളും പ്രൊജക്ഷനും ആണ് പ്രധാനം."),
 ("A","A","അപ്പോ ലാപ്ടോപ്പ് എണ്ണിയാൽ ആപ്പിന്റെ കണക്ക് ആകില്ല."),
 ("V","wide","ലാപ്ടോപ്പ് രണ്ട്, യൂസർമാർ ആയിരം. ഏത് എണ്ണും?")],
 "ലാപ്ടോപ്പ് എണ്ണിയാൽ\nആപ്പിന്റെ കണക്കാകില്ല", CTA_WORTH, theme="faq",
 cap_ml="ബാലൻസ് ഷീറ്റിൽ ആസ്തി കുറവായതുകൊണ്ട് സ്റ്റാർട്ടപ്പിന്റെ മൂല്യം പൂജ്യം ആകണമെന്നില്ല. നെറ്റ് അസറ്റ് വാല്യു ഒരു രീതി മാത്രം; തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പുകൾക്ക് സമാന കമ്പനികളും പ്രൊജക്ഷനും ആണ് ആശ്രയം. നിങ്ങളുടെ ബിസിനസ്: ആസ്തി കൂടുതലോ ആശയം കൂടുതലോ?",
 cap_en="A thin balance sheet does not mean a startup is worth nothing. Net asset value is only one method; early startups lean on comparable companies and projections. Your business: asset-heavy or idea-heavy?",
 cap_mg="Balance sheet-il asset kuravaayathukondu startup-inte value poojyam aakanamennilla. Net asset value oru method maathram; early startups-nu comparables-um projection-um. Ningalude business: asset koodutho idea koodutho?")

# FAQ: a partner leaves for Canada; "value it next year"
duo("qv040", "partner_exit", "A", "munnar", "പാർട്ണർ കാനഡയിലേക്ക്.\n\"കണക്ക് അടുത്ത വർഷം\nനോക്കാം\"", [
 ("A","wide","ബേസിലേ, ജീപ്പ് സഫാരി കമ്പനിയിലെ ജിതിൻ അടുത്ത മാസം കാനഡയിലേക്ക്. അവന്റെ ഷെയർ നമ്മൾ എടുക്കും."),
 ("V","V","സെലിനേ, അവൻ പോയിട്ട് അടുത്ത വർഷം കണക്ക് നോക്കാം. തിരക്കില്ലല്ലോ."),
 ("A","A","അടുത്ത വർഷം സീസൺ കഴിഞ്ഞാൽ കണക്ക് മാറില്ലേ?"),
 ("V","wide","മാറും. വാല്യുവേഷൻ ഒരു ആവശ്യത്തിനും ഒരു തീയതിക്കും ആണ്. പാർട്ണർ പോകുന്ന ദിവസത്തേക്ക് ചെയ്യണം."),
 ("A","A","അപ്പോ പോകും മുമ്പ് റിപ്പോർട്ട്."),
 ("V","wide","വിമാനം കയറും മുമ്പ് കണക്ക് ഇറങ്ങണം.")],
 "വിമാനം കയറും മുമ്പ്\nകണക്ക് ഇറങ്ങണം", CTA_VALUATION, theme="faq",
 cap_ml="പാർട്ണർ പോകുമ്പോൾ ഷെയറിന്റെ കണക്ക് പിന്നീട് നോക്കാം എന്ന് കരുതരുത്. വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും ഒരു പ്രത്യേക തീയതിക്കും ആണ്; പാർട്ണർ ഇറങ്ങുന്ന ദിവസത്തേക്ക് ചെയ്യണം. നിങ്ങളുടെ ടീമിൽ ആരെങ്കിലും വിദേശത്തേക്ക് പോകാൻ പ്ലാനുണ്ടോ?",
 cap_en="When a partner exits, do not leave the share valuation for later. A valuation is for a specific purpose and date, so it should be done for the day the partner leaves. Is anyone in your team planning to move abroad?",
 cap_mg="Partner pokumbol share-inte kanakku pinneedu nokkaam ennu karutharuthu. Valuation oru purpose-num oru date-num aanu; partner irangunna divasathekku cheyyanam. Ningalude team-il aarenkilum abroad pokaan plan undo?")

# FAQ: a franchise partner buys 10% at the founding-day rate
duo("qv041", "share_transfer", "A", "salon", "ഫ്രാഞ്ചൈസി പാർട്ണർക്ക്\n10% ഷെയർ. \"തുടങ്ങിയ\nഅന്നത്തെ നിരക്കിൽ\"", [
 ("A","wide","വിനീതേ, തൃശൂർ ഫ്രാഞ്ചൈസി എടുത്ത ലിജിക്ക് എന്റെ സലൂൺ കമ്പനിയിൽ 10% ഷെയർ വേണം. ഞാൻ തുടങ്ങിയ അന്നത്തെ നിരക്കിൽ കൊടുക്കാം."),
 ("V","V","സോണിയേ, അന്ന് ഒരു കസേര. ഇന്ന് ആറ് ബ്രാഞ്ച്. അതേ നിരക്കോ?"),
 ("A","A","പരിചയക്കാരിയല്ലേ, കണക്ക് വേണോ?"),
 ("V","wide","ഷെയർ കൈമാറ്റത്തിന് വാല്യുവേഷൻ വേണം. അതും ഇന്നത്തെ തീയതിക്ക്, അംഗീകൃത രീതിയിൽ."),
 ("A","A","അപ്പോ അന്നത്തെ കണക്ക് അന്നത്തേക്ക്."),
 ("V","wide","കസേര ഒന്നിൽ നിന്ന് ആറിലെത്തി, കണക്കും എത്തണം.")],
 "ബ്രാഞ്ച് ആറായി,\nകണക്കും പുതുതാകണം", CTA_WORTH, theme="faq",
 cap_ml="ഷെയർ കൈമാറുമ്പോൾ കമ്പനി തുടങ്ങിയ ദിവസത്തെ നിരക്കല്ല നോക്കേണ്ടത്. ഷെയർ കൈമാറ്റത്തിന് വാല്യുവേഷൻ വേണം, അതും ഒരു പ്രത്യേക തീയതിക്ക്, അംഗീകൃത രീതിയിൽ. നിങ്ങളുടെ ബിസിനസ് തുടങ്ങിയതിൽ നിന്ന് എത്ര വളർന്നു?",
 cap_en="Selling shares to a franchise partner at the rate from the founding day? A share transfer needs a valuation for a specific date, by an accepted method. How much has your business grown since day one?",
 cap_mg="Share kaimaarumbol company thudangiya divasathe rate alla nokkendathu. Share transfer-nu valuation venam, oru specific date-nu, accepted method-il. Ningalude business thudangiyathil ninnu ethra valarnnu?")

# New, d904 pattern: two houseboat owners merging; "50:50 because we both have 3 boats"
duo("qv042", "share_transfer", "B", "ferry", "മൂന്ന് ബോട്ട് അവന്,\nമൂന്ന് എനിക്ക്.\n\"അപ്പോ 50:50 അല്ലേ?\"", [
 ("A","wide","ടോണീ, ജോസിന്റെ ഹൗസ്ബോട്ട് കമ്പനിയും എന്റേതും ഒന്നാക്കുകയാ. രണ്ടിനും മൂന്ന് ബോട്ട്. അപ്പോ 50:50."),
 ("V","V","മീരേ, നിന്റെ ബോട്ടുകൾക്ക് വിദേശ ബുക്കിംഗ് വർഷം മുഴുവൻ. ജോസിന്റേത് ഓണത്തിന് മാത്രം. എണ്ണം ഒന്നാണെങ്കിലും മൂല്യം ഒന്നാണോ?"),
 ("A","A","ബോട്ട് എണ്ണിയാൽ പോരേ?"),
 ("V","wide","പോരാ. മെർജറിന് രണ്ട് കമ്പനിക്കും വാല്യുവേഷൻ വേണം. ആസ്തി, വരുമാനം, സമാന ഇടപാടുകൾ: അംഗീകൃത രീതികൾ."),
 ("A","A","അപ്പോ ബോട്ട് എണ്ണമല്ല, കണക്കാണ് ശതമാനം പറയുക."),
 ("V","wide","കായലിൽ ഒരേ നീളം, കണക്കിൽ ഒരേ മൂല്യം വേണമെന്നില്ല.")],
 "കായലിൽ ഒരേ നീളം,\nകണക്കിൽ ഒരേ മൂല്യമല്ല", CTA_VALUATION, theme="new",
 cap_ml="രണ്ട് കമ്പനികൾ ഒന്നാകുമ്പോൾ ബോട്ടിന്റെയോ കടയുടെയോ എണ്ണം നോക്കി 50:50 എന്ന് തീരുമാനിക്കരുത്. മെർജറിന് രണ്ട് കമ്പനിക്കും വാല്യുവേഷൻ വേണം: ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, സമാന ഇടപാടുകൾ, നെറ്റ് അസറ്റ് വാല്യു പോലുള്ള അംഗീകൃത രീതികൾ. നിങ്ങൾ മറ്റൊരു ബിസിനസുമായി ചേരാൻ ആലോചിക്കുന്നുണ്ടോ?",
 cap_en="Two houseboat companies merging cannot split 50:50 just because each has three boats. A merger needs a valuation of both companies by accepted methods such as discounted cash flow, comparable deals and net asset value. Thinking of joining hands with another business?",
 cap_mg="Randu company onnaakumbol boat-inteyo kadayudeyo ennam nokki 50:50 ennu theerumaanikkaruthu. Merger-nu randu company-kkum valuation venam: DCF, comparable deals, net asset value. Ningal vere business-umaayi cheraan aalochikkunnundo?")

# New, d904 pattern: latex elephant masks for festivals; "the buyer's offer is our valuation"
duo("qv043", "share_transfer", "B", "rubber", "പൂരത്തിന് റബ്ബർ\nആനമുഖം. \"ബയർ പറഞ്ഞ\nനമ്പറാണ് മൂല്യം\"", [
 ("A","wide","തോമസേ, നമ്മുടെ ആനമുഖം കമ്പനിയിൽ 10% ഷെയർ വാങ്ങാൻ ബാംഗ്ലൂരിലെ ഒരാൾ ഒരു നമ്പർ പറഞ്ഞു. അതാണ് നമ്മുടെ വാല്യുവേഷൻ."),
 ("V","V","ജോയിച്ചേട്ടാ, അവൻ പറഞ്ഞ നമ്പർ അവന്റെ ആഗ്രഹമാ. കണക്ക് അല്ല."),
 ("A","A","വാങ്ങുന്നവൻ സമ്മതിച്ചാൽ പിന്നെ എന്ത് കണക്ക്?"),
 ("V","wide","ഷെയർ കൈമാറ്റത്തിന് വാല്യുവേഷൻ വേണം. അംഗീകൃത രീതിയിൽ, ഈ ആവശ്യത്തിനും ഈ തീയതിക്കും."),
 ("A","A","അപ്പോ ഓഫർ കേൾക്കാം, കണക്ക് വേറെ ചെയ്യണം."),
 ("V","wide","ഓഫർ ഒരു നമ്പർ, വാല്യുവേഷൻ ഒരു കണക്ക്.")],
 "ഓഫർ ഒരു നമ്പർ,\nവാല്യുവേഷൻ ഒരു കണക്ക്", CTA_WORTH, theme="new",
 cap_ml="വാങ്ങാൻ വരുന്നയാൾ പറയുന്ന നമ്പർ തന്നെ കമ്പനിയുടെ വാല്യുവേഷൻ ആകില്ല. ഷെയർ കൈമാറ്റത്തിന് അംഗീകൃത രീതിയിൽ, ആ ആവശ്യത്തിനും തീയതിക്കും ചെയ്ത വാല്യുവേഷൻ വേണം. ഓഫർ കിട്ടിയാൽ നിങ്ങൾ ആദ്യം എന്ത് ചെയ്യും?",
 cap_en="A buyer's offer is not your company's valuation. A share transfer needs a valuation by an accepted method, for that purpose and date. Got an offer? What would you check first?",
 cap_mg="Vaangaan varunnayaal parayunna number thanne company-yude valuation aakilla. Share transfer-nu accepted method-il, aa purpose-num date-num cheytha valuation venam. Offer kittiyaal ningal aadyam enthu cheyyum?")
