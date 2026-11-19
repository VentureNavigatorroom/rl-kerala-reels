# Financial projections batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FP. Never mention our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

duo("fp010", "investor_pitch", "A", "handloom", "ഡെക്കിൽ 30 ഫോട്ടോ,\n2 അവാർഡ്. ഇൻവെസ്റ്റർ:\n\"നമ്പർ എവിടെ?\"", [
 ("A","wide","കുമാറേ, ഇൻവെസ്റ്റർ മറുപടി അയച്ചു: 'ഫിനാൻഷ്യൽ മെട്രിക്സ് ഇല്ല.' നമ്മുടെ ഡെക്കിൽ മുപ്പത് ഫോട്ടോ ഉണ്ടായിരുന്നല്ലോ!"),
 ("V","V","ലീലേ, ഫോട്ടോയിൽ തറി ഭംഗിയാ. പക്ഷേ തറി എത്ര സമ്പാദിക്കും എന്ന് ഒരു പേജിലും ഇല്ല."),
 ("A","A","അപ്പോ അവർക്ക് എന്താ കാണേണ്ടത്?"),
 ("V","wide","മൂന്ന് വർഷത്തെ ലാഭനഷ്ട കണക്ക്, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ എന്ന് എന്ന്. ഓരോ നമ്പറിനും എഴുതിയ അനുമാനം."),
 ("A","A","ഭംഗി കണ്ട് കയ്യടിക്കും. കണക്ക് കണ്ടാലേ കൈ നീട്ടൂ."),
 ("V","wide","ഫോട്ടോ ഹൃദയത്തിന്. നമ്പർ ചെക്കിന്.")],
 "ഫോട്ടോ ഹൃദയത്തിന്,\nനമ്പർ ചെക്കിന്", CTA_PROJECTION, theme="crm",
 cap_ml="മനോഹരമായ ഡെക്ക്, പക്ഷേ ഇൻവെസ്റ്റർ മറുപടി: 'ഫിനാൻഷ്യൽ മെട്രിക്സ് ഇല്ല.' പിച്ചിൽ 3 വർഷത്തെ ലാഭനഷ്ട കണക്ക്, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ, എഴുതിയ അനുമാനങ്ങൾ വേണം. നിങ്ങളുടെ ഡെക്കിൽ നമ്പർ പേജ് ഉണ്ടോ?",
 cap_en="A handloom brand's beautiful pitch deck gets 'no financial metrics' back from the investor. Investors want a 3-year P&L, cash flow, the break-even point and written assumptions. Does your deck have a numbers page?",
 cap_mg="Manoharamaaya deck, pakshe investor marupadi: 'financial metrics illa.' Pitch-il 3 varshathe P&L, cash flow, break-even, ezhuthiya anumaanangal venam. Ningalude deck-il number page undo?")

duo("fp011", "pre_revenue", "A", "pharmacy", "6 മാസത്തെ പണം\nചോദിച്ചു. ലാഭം\nവരുന്നത് 14-ാം മാസം", [
 ("A","wide","പ്രവീണേ, നമ്മുടെ മരുന്ന് ഡെലിവറി ആപ്പിന് ആറ് മാസത്തെ ചെലവ് മാത്രം ഇൻവെസ്റ്ററോട് ചോദിച്ചാൽ മതിയല്ലോ?"),
 ("V","V","സിനീ, നമ്മുടെ ഷീറ്റിൽ ബ്രേക്ക്-ഈവൻ എത്രാം മാസമാ?"),
 ("A","A","പതിനാലാം മാസം. ഓ..."),
 ("V","wide","അതെ. ക്യാഷ് ഫ്ലോ മാസം തോറും നോക്കൂ. പണം ഏറ്റവും താഴുന്ന മാസം വരെ പിടിച്ചുനിൽക്കാനുള്ളതാണ് ശരിയായ ആവശ്യം."),
 ("A","A","അപ്പോ ആറാം മാസം നമ്മൾ വീണ്ടും പാത്രവുമായി ഇറങ്ങേണ്ടി വന്നേനെ."),
 ("V","wide","തുക ബില്ലിൽ നിന്നല്ല, ക്യാഷ് ഫ്ലോയിൽ നിന്ന്.")],
 "തുക ബില്ലിൽ നിന്നല്ല,\nക്യാഷ് ഫ്ലോയിൽ നിന്ന്", CTA_FORECAST, theme="crm",
 cap_ml="ഇൻവെസ്റ്ററോട് 6 മാസത്തെ ചെലവ് മാത്രം ചോദിച്ചു, പക്ഷേ ബ്രേക്ക്-ഈവൻ 14-ാം മാസം. എത്ര ചോദിക്കണം എന്ന് മാസ ക്യാഷ് ഫ്ലോ പറയും: പണം ഏറ്റവും താഴുന്ന മാസം വരെ. നിങ്ങളുടെ ബ്രേക്ക്-ഈവൻ എത്രാം മാസം?",
 cap_en="A medicine-delivery app asks investors for 6 months of costs, but its break-even is in month 14. The monthly cash flow tells you how much to ask: enough to reach the lowest cash month. Which month is your break-even?",
 cap_mg="Investor-odu 6 maasathe chelavu maathram chodichu, pakshe break-even 14-aam maasam. Ethra chodikkanam ennu monthly cash flow parayum: paisa ettavum thaazhunna maasam vare. Ningalude break-even ethraam maasam?")

duo("fp012", "early_revenue", "B", "rubber", "15 വർഷത്തെ കണക്ക്.\nബന്ധു: \"ചെറിയ നമ്പർ,\nഒന്ന് കൂട്ടി എഴുതൂ\"", [
 ("A","wide","തോമസേ, ലാറ്റക്സ് മാറ്റ് യൂണിറ്റിന്റെ പ്രൊജക്ഷൻ കണ്ട് അമ്മാവൻ പറഞ്ഞു, നമ്പർ ചെറുതാ, ഇരട്ടിയാക്കി എഴുതാൻ."),
 ("V","V","ജോയീ, പതിനഞ്ച് വർഷം ഒരു മാസം പോലും മുടങ്ങാത്ത വിൽപ്പന. അതിനേക്കാൾ വലിയ നമ്പർ എന്തിനാ?"),
 ("A","A","ഇൻവെസ്റ്റർക്ക് വലിയ നമ്പർ അല്ലേ ഇഷ്ടം?"),
 ("V","wide","ഇഷ്ടം വിശ്വസിക്കാവുന്ന നമ്പറാ. ഇന്നത്തെ വിൽപ്പനയിൽ നിന്ന് തുടങ്ങി, ഓരോ വളർച്ചയ്ക്കും കാരണം എഴുതണം. ഊതിവീർപ്പിച്ചാൽ വിശ്വാസം പോകും."),
 ("A","A","അപ്പോ പഴക്കം തന്നെ നമ്മുടെ ബലം."),
 ("V","wide","ഇരട്ടിയാക്കിയ നമ്പർ, പകുതിയായ വിശ്വാസം.")],
 "ഇരട്ടിയാക്കിയ നമ്പർ,\nപകുതിയായ വിശ്വാസം", CTA_PROJECTION, theme="crm",
 cap_ml="വർഷങ്ങളുടെ സ്ഥിരമായ ചെറിയ വിൽപ്പന ഒരു ബലഹീനതയല്ല. പ്രൊജക്ഷൻ ഇന്നത്തെ വിൽപ്പനയിൽ നിന്ന് തുടങ്ങണം, ഓരോ വളർച്ചയ്ക്കും എഴുതിയ കാരണം വേണം; ഊതിവീർപ്പിച്ച നമ്പർ വിശ്വാസം കളയും. നിങ്ങളുടെ ബിസിനസ് എത്ര വർഷമായി?",
 cap_en="Years of steady, modest sales are not a weakness. A projection should start from today's sales with a written reason for every bit of growth; inflated numbers lose trust. How many years old is your business?",
 cap_mg="Varshangalude sthiramaaya cheriya vilppana oru balaheenathayalla. Projection innathe vilppanayil ninnu thudanganam, oro valarchakkum ezhuthiya kaaranam venam; oothiveerppicha number vishwaasam kalayum. Ningalude business ethra varshamaayi?")

duo("fp013", "investor_pitch", "B", "bakery", "\"ആദ്യ വർഷം\n80 ലക്ഷം വിൽപ്പന\"\nഇൻവെസ്റ്റർ: \"ഏത് മാസം?\"", [
 ("A","wide","സാബൂ, ഇൻവെസ്റ്റർക്ക് ഞാൻ ഒറ്റ വരി അയച്ചു: ആദ്യ വർഷം എൺപത് ലക്ഷം. തിരിച്ച് ചോദ്യം, ഏത് മാസം എത്ര?"),
 ("V","V","ജിഷേ, രണ്ടാമത്തെ ഔട്ട്‌ലെറ്റ് തുറക്കുന്ന മാസം ഓർത്തോ? അന്ന് ചെലവ് കൂടും, വരുമാനം പതുക്കെയേ വരൂ."),
 ("A","A","ഒറ്റ വരിയിൽ അത് കാണില്ലല്ലോ."),
 ("V","wide","അതുകൊണ്ടാ ആദ്യ വർഷം മാസം തോറും വേണ്ടത്. പന്ത്രണ്ട് കോളം. എവിടെയാ പണം കുറയുന്നത് എന്ന് അപ്പോഴേ കാണൂ."),
 ("A","A","വർഷത്തെ ആകെ സംഖ്യ ഒരു കുഴി മൂടിവെക്കും."),
 ("V","wide","കേക്ക് മുഴുവനല്ല, ഓരോ കഷണവും കാണിക്കണം.")],
 "കേക്ക് മുഴുവനല്ല,\nഓരോ കഷണവും", CTA_FORECAST, theme="crm",
 cap_ml="ആദ്യ വർഷത്തെ ആകെ വിൽപ്പന മാത്രം കാണിച്ചാൽ പണം കുറയുന്ന മാസങ്ങൾ മറഞ്ഞുപോകും. 3 വർഷ പ്രൊജക്ഷനിൽ ആദ്യ വർഷം മാസം തോറും വേണം. നിങ്ങളുടെ ഷീറ്റ്: വർഷമോ മാസമോ?",
 cap_en="A bakery founder sends the investor one line: year-one sales total. A yearly total hides the months when cash dips, like the month a new outlet opens. Year one should be month by month. Is your sheet yearly or monthly?",
 cap_mg="Aadya varshathe aake vilppana maathram kaanichaal paisa kurayunna maasangal maranju pokum. 3 varsha projection-il aadya varsham maasam thorum venam. Ningalude sheet: varshamo maasamo?")

duo("fp014", "early_revenue", "A", "salon", "\"എനിക്ക് ശമ്പളം\nവേണ്ട, ഷീറ്റിൽ\nഇടേണ്ട\" ശരിയോ?", [
 ("A","wide","വിനീതേ, നമ്മുടെ ബ്രൈഡൽ മേക്കപ്പ് സ്റ്റുഡിയോയുടെ ചെലവ് ഷീറ്റിൽ എന്റെ ശമ്പളം പൂജ്യം. ഞാൻ എടുക്കില്ലല്ലോ."),
 ("V","V","സോണിയേ, ഇന്ന് എടുക്കില്ല. രണ്ട് വർഷം കഴിഞ്ഞും എടുക്കില്ലേ?"),
 ("A","A","അപ്പോഴേക്കും ഒരു മാനേജരെ വെക്കണം."),
 ("V","wide","അതാ. ചെലവിൽ ടീമും ഹയറിംഗും സത്യമായി വേണം. ഇല്ലെങ്കിൽ ലാഭം കടലാസിൽ മാത്രം വലുതാകും, ഇൻവെസ്റ്റർ അത് കണ്ടുപിടിക്കും."),
 ("A","A","എന്റെ ത്യാഗം ഷീറ്റിൽ ലാഭമായി അഭിനയിക്കുന്നു."),
 ("V","wide","ഫ്രീ ആയി ജോലി ചെയ്യാം. ഫ്രീ ആയി കണക്ക് എഴുതരുത്.")],
 "ഫ്രീ ജോലി ശരി,\nഫ്രീ കണക്ക് വേണ്ട", CTA_PROJECTION, theme="faq",
 cap_ml="ഫൗണ്ടറുടെ ശമ്പളവും ഭാവിയിലെ ഹയറിംഗും ഇല്ലാത്ത ചെലവ് ഷീറ്റ് ലാഭം കൃത്രിമമായി കൂട്ടും. പ്രൊജക്ഷനിലെ ചെലവുകൾ യാഥാർത്ഥ്യമുള്ളതാകണം. നിങ്ങളുടെ ഷീറ്റിൽ നിങ്ങളുടെ ശമ്പളം ഉണ്ടോ?",
 cap_en="A cost sheet with zero founder salary and no future hires makes profit look bigger than it is. Costs and hiring in a projection must be realistic, and investors notice when they aren't. Is your own salary in your sheet?",
 cap_mg="Founder-nte salary-um bhaaviyile hiring-um illaatha cost sheet laabham krithrimamaayi koottum. Projection-ile chelavukal yaathaarthyamullathaakanam. Ningalude sheet-il ningalude salary undo?")

duo("fp015", "grant_application", "B", "veranda", "തെയ്യം ചമയം\nഉണ്ടാക്കുന്നവന്\nപ്രൊജക്ഷൻ എന്തിന്?", [
 ("A","wide","ബാലേട്ടാ, ചമയ യൂണിറ്റിന് ഗ്രാന്റ് അപേക്ഷയിൽ മൂന്ന് വർഷത്തെ കണക്ക് ചോദിക്കുന്നു."),
 ("V","V","ശാന്തേ, നമുക്ക് ഇൻവെസ്റ്റർ ഇല്ലല്ലോ. പ്രൊജക്ഷൻ ആപ്പുകാർക്കല്ലേ?"),
 ("A","A","ബാങ്ക് ലോണിനും ചോദിച്ചല്ലോ കഴിഞ്ഞ കൊല്ലം."),
 ("V","wide","ശരിയാ. ഇൻവെസ്റ്റർ മാത്രമല്ല, ബാങ്കും ഗ്രാന്റ് പാനലും ചോദിക്കും. ഉത്സവ മാസത്തെ ഓർഡറും ബാക്കി മാസത്തെ ചെലവും എഴുതണം."),
 ("A","A","അപ്പോ കിരീടത്തിനും കണക്കുണ്ട്."),
 ("V","wide","ദൈവത്തിന് ചമയം, ബാങ്കിന് കണക്ക്.")],
 "ദൈവത്തിന് ചമയം,\nബാങ്കിന് കണക്ക്", CTA_FORECAST, theme="faq",
 cap_ml="ഇൻവെസ്റ്റർ ഇല്ലാത്ത പരമ്പരാഗത ബിസിനസിനും ഫിനാൻഷ്യൽ പ്രൊജക്ഷൻ വേണ്ടിവരും: ബാങ്കുകളും ഗ്രാന്റ് പാനലുകളും ചോദിക്കും. സീസൺ മാസങ്ങളും ബാക്കി മാസങ്ങളും വേറെ എഴുതൂ. നിങ്ങളുടെ ബിസിനസ്: സീസണലോ വർഷം മുഴുവനോ?",
 cap_en="A theyyam costume workshop thinks projections are only for app startups. Banks and grant panels ask for them too, not just investors. Write festival months and quiet months separately. Is your business seasonal or year-round?",
 cap_mg="Investor illaatha paramparaagatha business-inum financial projection vendivarum: bank-um grant panel-um chodikkum. Season maasangalum baakki maasangalum vere ezhuthu. Ningalude business: seasonal-o varsham muzhuvano?")

duo("fp016", "investor_pitch", "B", "tailor", "നെറ്റിപ്പട്ടം\nസ്റ്റാർട്ടപ്പ്: \"10 വർഷ\nപ്രൊജക്ഷൻ ഇംപ്രസ് ചെയ്യും\"", [
 ("A","wide","മോഹനേട്ടാ, നമ്മുടെ നെറ്റിപ്പട്ടം ഓൺലൈൻ സ്റ്റോറിന് പത്ത് വർഷത്തെ പ്രൊജക്ഷൻ ഉണ്ടാക്കി. ഇൻവെസ്റ്റർ ഞെട്ടും."),
 ("V","V","ഉഷേ, പത്താം വർഷം എത്ര ഓർഡർ എന്ന് നിനക്ക് ഉറപ്പുണ്ടോ?"),
 ("A","A","അത്... ഒരു ഊഹം."),
 ("V","wide","അതാ പ്രശ്നം. സാധാരണ മൂന്ന് വർഷം മതി, ആദ്യ വർഷം മാസം തോറും. അതിനപ്പുറം കണക്കല്ല, ജാതകമാ."),
 ("A","A","അപ്പോ ഏഴ് വർഷം വെട്ടാം."),
 ("V","wide","മൂന്ന് വർഷം കണക്ക്. പത്ത് വർഷം ജാതകം.")],
 "മൂന്ന് വർഷം കണക്ക്,\nപത്ത് വർഷം ജാതകം", CTA_FORECAST, theme="faq",
 cap_ml="കൂടുതൽ വർഷം കാണിച്ചാൽ ഇൻവെസ്റ്റർ ഇംപ്രസ് ആകില്ല. സാധാരണ മൂന്ന് വർഷത്തെ പ്രൊജക്ഷൻ, ആദ്യ വർഷം മാസം തോറും; അതിനപ്പുറം ഊഹമാണ്. നിങ്ങളുടെ പ്രൊജക്ഷൻ എത്ര വർഷത്തേക്ക്?",
 cap_en="A nettipattam online store builds a 10-year projection to impress investors. The usual ask is 3 years, month by month for the first; beyond that it's guesswork. How many years does yours cover?",
 cap_mg="Kooduthal varsham kaanichaal investor impress aakilla. Saadhaarana moonnu varshathe projection, aadya varsham maasam thorum; athinappuram oohamaanu. Ningalude projection ethra varshathekku?")

chat("fp017", "pre_revenue", "A", "ടെംപ്ലേറ്റ് ഡൗൺലോഡ്\nചെയ്തു, നമ്പർ മാറ്റി.\nപ്രൊജക്ഷൻ റെഡി?", ("റസിയ", "നൗഷാദ്"), [
 (0, "നൗഷാദ്, ഇന്റർനെറ്റിൽ നിന്ന് ഒരു ഫിനാൻഷ്യൽ മോഡൽ ടെംപ്ലേറ്റ് കിട്ടി. നമ്മുടെ പേര് ഇട്ടു, നമ്പർ മാറ്റി. റെഡി!"),
 (1, "റസിയാ, അതിലെ വളർച്ച ആരുടേതാ? ആ ടെംപ്ലേറ്റ് ഉണ്ടാക്കിയ കമ്പനിയുടേതോ നമ്മുടേതോ?"),
 (0, "അത്... അതിൽ ഉണ്ടായിരുന്നത് തന്നെ."),
 (1, "അപ്പോ അത് നമ്മുടെ പ്രൊജക്ഷനല്ല. നമ്മുടെ കസ്റ്റമർ, നമ്മുടെ ചെലവ്, നമ്മുടെ അനുമാനങ്ങൾ എഴുതി വെക്കണം. ട്രാക്ഷനോട് ചേരണം."),
 (0, "ടെംപ്ലേറ്റ് കുപ്പി മാത്രം, അകത്തെ വെള്ളം നമ്മുടേതാകണം."),
 (1, "കടം വാങ്ങിയ ഷീറ്റ്, കടം വാങ്ങിയ സ്വപ്നം.")],
 "കടം വാങ്ങിയ ഷീറ്റ്,\nകടം വാങ്ങിയ സ്വപ്നം", CTA_PROJECTION, theme="faq",
 cap_ml="ടെംപ്ലേറ്റ് ഉപയോഗിക്കാം, പക്ഷേ അതിലെ അനുമാനങ്ങൾ നിങ്ങളുടേതാകണം: നിങ്ങളുടെ കസ്റ്റമേഴ്സ്, ചെലവ്, വളർച്ച, എഴുതി വെച്ച്. ഇൻവെസ്റ്റർ ആദ്യം ചോദിക്കുന്നത് 'ഈ നമ്പർ എവിടെ നിന്ന്?' എന്നാണ്. നിങ്ങൾ ടെംപ്ലേറ്റ് ഉപയോഗിക്കാറുണ്ടോ?",
 cap_en="A downloaded template with your name on it isn't your projection. Use your own customers, costs and growth, write the assumptions down, and tie them to your traction. Do you use templates?",
 cap_mg="Template upayogikkaam, pakshe athile anumaanangal ningaludethaakanam: ningalude customers, chelavu, valarcha, ezhuthi vechu. Investor aadyam chodikkunnathu 'ee number evide ninnu?' ennaanu. Ningal template upayogikkaarundo?")

duo("fp018", "pre_revenue", "B", "autostand", "തെങ്ങുകയറ്റ ആപ്പ്:\n\"കേരളത്തിലെ എല്ലാ\nതെങ്ങും നമ്മുടെ കസ്റ്റമർ\"", [
 ("A","wide","ഷാജീ, നമ്മുടെ തെങ്ങുകയറ്റ ബുക്കിംഗ് ആപ്പിന്റെ ഷീറ്റിൽ ഞാൻ എഴുതി: കേരളത്തിലെ എല്ലാ തെങ്ങും കസ്റ്റമർ!"),
 ("V","V","സജീ, തെങ്ങ് ബുക്ക് ചെയ്യില്ല. വീട്ടുകാരാ ബുക്ക് ചെയ്യുന്നത്. നമ്മുടെ നാട്ടിൽ ഈ മാസം എത്ര പേർ ബുക്ക് ചെയ്തു?"),
 ("A","A","നാല്പത്തിരണ്ട്."),
 ("V","wide","അവിടന്ന് തുടങ്ങ്. മാസം എത്ര വീട്, ഒരു കയറ്റത്തിന് നമുക്ക് എത്ര കിട്ടും, മാസം എത്ര വളർച്ച. അതാണ് വരുമാനത്തിന്റെ ഡ്രൈവറുകൾ."),
 ("A","A","അപ്പോ ആകാശം വരെ അല്ല, തെങ്ങിന്റെ മണ്ട വരെ."),
 ("V","wide","തെങ്ങ് എണ്ണിയാൽ സ്വപ്നം. വീട് എണ്ണിയാൽ ബിസിനസ്.")],
 "തെങ്ങ് എണ്ണിയാൽ സ്വപ്നം,\nവീട് എണ്ണിയാൽ ബിസിനസ്", CTA_PROJECTION, theme="new",
 cap_ml="'കേരളം മുഴുവൻ നമ്മുടെ മാർക്കറ്റ്' എന്നത് പ്രൊജക്ഷനല്ല. ഇന്നത്തെ ബുക്കിംഗിൽ നിന്ന് തുടങ്ങൂ: എത്ര കസ്റ്റമേഴ്സ്, ഒരാളിൽ നിന്ന് എത്ര, മാസം എത്ര വളർച്ച. നിങ്ങൾ എണ്ണുന്നത് മാർക്കറ്റോ കസ്റ്റമേഴ്സിനെയോ?",
 cap_en="A coconut-climber booking app counts every coconut tree in Kerala as a customer. A projection starts from real bookings: how many households, how much per climb, monthly growth. Are you counting the market or your customers?",
 cap_mg="'Kerala muzhuvan nammude market' ennathu projection-alla. Innathe booking-il ninnu thudangu: ethra customers, oraalil ninnu ethra, maasam ethra valarcha. Ningal ennunnathu market-o customers-ineyo?")

duo("fp019", "bank_loan", "A", "gulfroom", "ഗൾഫിൽ 11 വർഷം.\nനാട്ടിൽ ജ്യൂസ് കട.\n\"പ്രൊജക്ഷൻ? ഞാൻ ചെറിയ ആളാ\"", [
 ("A","wide","ഷംസൂ, നാട്ടിൽ ജ്യൂസ് കടയ്ക്ക് ലോൺ എടുക്കാൻ ബാങ്ക് കണക്ക് ചോദിച്ചു. അതൊക്കെ വലിയ കമ്പനിക്കല്ലേ?"),
 ("V","V","നസീറേ, ലോൺ വലുതായാലും ചെറുതായാലും തിരിച്ചടവ് എവിടെ നിന്ന് എന്ന് ബാങ്കിന് അറിയണം."),
 ("A","A","അത് കട നടന്നാൽ വരുമല്ലോ."),
 ("V","wide","അത് കടലാസിൽ കാണിക്കണം. ലോണിന് ബാങ്ക് പ്രോജക്റ്റ് റിപ്പോർട്ട് ചോദിക്കാം: വരുമാനം, ചെലവ്, മാസ ക്യാഷ് ഫ്ലോ, എന്ന് മുതൽ ലാഭം."),
 ("A","A","അപ്പോ ജ്യൂസിന് മുമ്പ് കണക്ക് പിഴിയണം."),
 ("V","wide","കണക്ക് പിഴിഞ്ഞാലേ ലോൺ ഇറങ്ങൂ.")],
 "ജ്യൂസിന് മുമ്പ്\nകണക്ക് പിഴിയണം", CTA_FORECAST, theme="new",
 cap_ml="ചെറിയ കടയ്ക്കുള്ള ലോണിനും ബാങ്ക് പ്രോജക്റ്റ് റിപ്പോർട്ടും പ്രൊജക്ഷനും ചോദിക്കാം: വരുമാനം, ചെലവ്, മാസ ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ. ഗൾഫിൽ നിന്ന് മടങ്ങി ബിസിനസ് തുടങ്ങുന്നവർ ഇത് ആദ്യം റെഡിയാക്കൂ. നിങ്ങൾ എന്ന് നാട്ടിൽ വരും?",
 cap_en="A Gulf returnee planning a juice shop thinks projections are only for big companies. For a business loan of any size, the bank may ask for a project report: revenue, costs, monthly cash flow and break-even. When are you coming home?",
 cap_mg="Cheriya kadaykkulla loan-inum bank project report-um projection-um chodikkaam: varumaanam, chelavu, maasa cash flow, break-even. Gulf-il ninnu madangi business thudangunnavar ithu aadyam ready aakku. Ningal ennu naattil varum?")
