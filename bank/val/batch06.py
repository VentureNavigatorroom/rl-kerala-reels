# Company valuation batch 06 (21 Nov, month backlog). Facts only from topics.FACTS_VAL (and FACTS_INV where it touches shares). Never state a value or a fee. People, firms and towns invented.
# crm scripts are built on STORY_THEMES #2 / #4 / #21 / #30 with changed sector, people and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

# CRM #4 (NRI founder planning to move back): his own extra money still needs fair value
duo("qv044", "nri_share_issue", "A", "gulf", "\"എന്റെ കമ്പനിയിൽ\nഎന്റെ പണം.\nഅതിനും റിപ്പോർട്ടോ?\"", [
 ("A","wide","ഫൈസലേ, നാട്ടിലെ എന്റെ മറൈൻ സ്പെയർ പാർട്സ് കമ്പനിയിൽ ഞാൻ തന്നെ കൂടുതൽ പണം ഇടുന്നു. പുതിയ ഷെയർ എടുക്കും."),
 ("V","V","ഷിജൂ, നീ ഇവിടെ NRI ആണ്. ആ പണം പിന്നീട് തിരികെ കൊണ്ടുപോകാവുന്ന റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിലാണോ?"),
 ("A","A","അതേ. പക്ഷേ കമ്പനി എന്റേതല്ലേ? എനിക്ക് ഇഷ്ടമുള്ള നിരക്കിൽ എടുക്കാമല്ലോ."),
 ("V","wide","ഇല്ല. NRI ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല. CA, സെബി മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തണം."),
 ("A","A","സ്വന്തം വീട്ടിൽ കയറാനും ഗേറ്റ് പാസോ?"),
 ("V","wide","ഉടമ ആയാലും ഫെയർ വാല്യുവിന് ഇളവില്ല.")],
 "സ്വന്തം കമ്പനി ആണെങ്കിലും\nഫെയർ വാല്യു ആദ്യം", CTA_VALUATION, theme="crm",
 cap_ml="ഗൾഫിലിരുന്ന് സ്വന്തം നാട്ടിലെ കമ്പനിയിൽ റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ പുതിയ ഷെയർ എടുക്കുന്ന NRI ഫൗണ്ടർക്കും ഫെയർ വാല്യുവിൽ താഴെ ഷെയർ പാടില്ല. CA, സെബി രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തണം. നിങ്ങൾ ഗൾഫിലിരുന്ന് നാട്ടിൽ കമ്പനി നടത്തുന്നുണ്ടോ?",
 cap_en="An NRI founder putting more of his own money into his Kerala company on a repatriation basis still cannot take new shares below fair value, even though he owns the company. Fair value must be certified by a CA, SEBI-registered merchant banker or cost accountant using an accepted method. Running a Kerala company from the Gulf?",
 cap_mg="Gulf-il irunnu swantham naattile company-il repatriation basis-il puthiya share edukkunna NRI founder-kkum fair value-il thaazhe share paadilla. CA, SEBI merchant banker, allenkil cost accountant certify cheyyanam. Ningal Gulf-il irunnu naattil company nadathunnundo?")

# CRM #2 (business run as a trust / proprietorship): the investor cannot get shares in it
duo("qv045", "raising_round", "A", "pharmacy", "\"20% തരാം\"\nഇൻവെസ്റ്റർ റെഡി.\nപക്ഷേ ഷെയറേ ഇല്ല", [
 ("A","wide","പ്രവീണേ, നമ്മുടെ ഹെർബൽ ഹെയർ ഓയിൽ യൂണിറ്റിന് ഇൻവെസ്റ്റർ റെഡി. ഇരുപത് ശതമാനം ഷെയർ ചോദിക്കുന്നു. വാല്യുവേഷൻ ചെയ്യാം?"),
 ("V","V","സിനിച്ചേച്ചീ, യൂണിറ്റ് ഇപ്പോഴും ചേച്ചിയുടെ പേരിലെ പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ?"),
 ("A","A","അതേ. അതിന് എന്താ?"),
 ("V","wide","ഷെയർ ഇറക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. ആദ്യം കമ്പനി, പിന്നെ അതിന്റെ വാല്യുവേഷൻ, അതിൽ നിന്നാ ഷെയറിന്റെ കണക്ക്."),
 ("A","wide","ഇല്ലാത്ത ഷെയറിന്റെ ശതമാനം പറഞ്ഞ് ഞാൻ ചിരിച്ചു."),
 ("V","wide","എണ്ണ തേക്കും മുമ്പ് തല വേണം.")],
 "എണ്ണ തേക്കും മുമ്പ്\nതല വേണം", CTA_VALUATION, theme="crm",
 cap_ml="ഹെർബൽ ഹെയർ ഓയിൽ യൂണിറ്റിൽ ഇൻവെസ്റ്റർ ഇരുപത് ശതമാനം ഷെയർ ചോദിച്ചു, പക്ഷേ ബിസിനസ് ഒരു പ്രൊപ്രൈറ്റർഷിപ്പ്. ഷെയർ ഇറക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം; അതിനുശേഷം ആ കമ്പനിയുടെ വാല്യുവേഷൻ. നിങ്ങളുടെ ബിസിനസ് ഇപ്പോൾ ഏത് ഘടനയിലാണ്?",
 cap_en="An investor asked for 20% of a herbal hair-oil unit, but the business is a proprietorship, and only a private limited company can issue shares to an investor. Form the company first, then value that company to know how many shares the money buys. What structure is your business in today?",
 cap_mg="Herbal hair oil unit-il investor 20% share chodichu, pakshe business oru proprietorship. Share irakkaan private limited company venam; athinu shesham aa company-yude valuation. Ningalude business ippol ethu roopathilaanu?")

# CRM #21 (egg farm switched to mushrooms with a new process): old numbers, new business
duo("qv046", "raising_round", "A", "teashop", "മുട്ട ഫാം\nകൂൺ ഫാം ആയി.\nകണക്ക് ഇപ്പോഴും മുട്ടയുടേത്", [
 ("A","wide","വിഷ്ണൂ, ഇൻവെസ്റ്റർക്ക് വാല്യുവേഷന് അയച്ചത് പഴയ മുട്ട ഫാമിന്റെ മൂന്ന് വർഷത്തെ കണക്കാ?"),
 ("V","V","അനൂ, അതല്ലേ കൈയിലുള്ളത്? കൂൺ തുടങ്ങിയിട്ട് എട്ട് മാസമേ ആയുള്ളൂ."),
 ("A","A","പക്ഷേ ഇൻവെസ്റ്റർ പണം ഇടുന്നത് കൂണിന്റെ പുതിയ പ്രോസസിനല്ലേ?"),
 ("V","wide","ശരിയാ. വാല്യുവേഷൻ ഒരു ആവശ്യത്തിനും തീയതിക്കും. ഭാവി വരുമാനം കൂണിന്റെ പ്രൊജക്ഷനിൽ നിന്ന്, പഴയ ഷെഡ് ആസ്തിയായി."),
 ("A","wide","അപ്പോ കോഴി പോയി, കണക്ക് ഇപ്പോഴും കൂട്ടിൽ."),
 ("V","wide","കൂൺ വളർത്തുമ്പോൾ മുട്ടക്കണക്ക് അടയിരിക്കട്ടെ.")],
 "കോഴി പോയി,\nകണക്ക് കൂട്ടിൽ തന്നെ", CTA_WORTH, theme="crm",
 cap_ml="മുട്ട ഫാം പുതിയ പ്രോസസോടെ കൂൺ ഫാം ആയി, പക്ഷേ ഇൻവെസ്റ്റർക്ക് അയച്ചത് പഴയ മുട്ടക്കണക്ക്. വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും തീയതിക്കും: ഭാവി വരുമാനം പുതിയ ബിസിനസിന്റെ പ്രൊജക്ഷനിൽ നിന്ന്, ഷെഡും ഉപകരണങ്ങളും ആസ്തിയായി. നിങ്ങളുടെ ബിസിനസ് വഴി മാറിയിട്ടുണ്ടോ?",
 cap_en="An egg farm switched to mushrooms with a new process, yet the founders sent investors three years of egg numbers. A valuation is for a specific purpose and date: discounted cash flow looks at the new business's projections, while sheds and equipment count under net asset value. Has your business ever pivoted?",
 cap_mg="Mutta farm puthiya process-ode koon farm aayi, pakshe investor-kku ayachathu pazhaya mutta-kkanakku. Valuation oru prathyeka aavashyathinum theeyathikkum: bhaavi varumaanam puthiya business-inte projection-il ninnu, shed-um upakaranangalum asset aayi. Ningalude business vazhi maariyittundo?")

# CRM #30 (college founder after demo day): two angels, two numbers
duo("qv047", "raising_round", "A", "photocopy", "ഡെമോ ഡേ കഴിഞ്ഞു.\nരണ്ട് എയ്ഞ്ചൽ.\nരണ്ട് നമ്പർ", [
 ("A","wide","ഉണ്ണീ, ഡെമോ ഡേയിൽ രണ്ട് എയ്ഞ്ചൽ വന്നു. ഒരാൾ ഇരുപത് ശതമാനം ചോദിക്കുന്നു, മറ്റേയാൾ അതേ പണത്തിന് മുപ്പത്."),
 ("V","V","അശ്വതീ, നിന്റെ ലാബ് റോബോട്ട് കിറ്റിന് ശരിക്കും എത്ര മൂല്യമുണ്ടെന്ന് നിനക്ക് അറിയാമോ?"),
 ("A","A","ഇല്ല. ആര് കുറവ് ചോദിക്കുന്നോ അവരെ എടുക്കാമെന്ന് വിചാരിച്ചു."),
 ("V","wide","ആദ്യം സ്വന്തം അടിസ്ഥാനം. തുടക്കത്തിൽ താരതമ്യ കമ്പനികളും ഡീലുകളും നിന്റെ പ്രൊജക്ഷനും. അതുണ്ടെങ്കിൽ രണ്ട് ഓഫറും അളക്കാം."),
 ("A","wide","അവരുടെ നമ്പർ അവരുടേത്. എന്റെ നമ്പർ എന്റേത്.")],
 "അവരുടെ നമ്പർ അവരുടേത്,\nനിന്റെ നമ്പർ നിന്റേത്", CTA_VALUATION, theme="crm",
 cap_ml="കോളേജ് ഡെമോ ഡേയിൽ രണ്ട് എയ്ഞ്ചൽ നിക്ഷേപകർ ഒരേ തുകയ്ക്ക് വ്യത്യസ്ത ശതമാനം ചോദിച്ചു. സ്വന്തം വാല്യുവേഷൻ അടിസ്ഥാനം ഇല്ലെങ്കിൽ ഏത് ഓഫർ നല്ലതെന്ന് അളക്കാൻ പറ്റില്ല; തുടക്കത്തിൽ താരതമ്യ കമ്പനികളും ഡീലുകളും പ്രൊജക്ഷനും ആണ് അടിസ്ഥാനം. നിങ്ങൾക്ക് ഒന്നിലധികം ഓഫർ കിട്ടിയിട്ടുണ്ടോ?",
 cap_en="After a college demo day, two angels offered the same money for very different percentages. Without your own valuation basis you cannot compare offers; for an early startup that basis is comparable companies and deals plus your own projections. Ever had two offers on the table?",
 cap_mg="College demo day-il randu angel investors ore thukaykku vyathyastha shathamaanam chodichu. Swantham valuation adisthaanam illenkil ethu offer nallathennu alakkaan pattilla; thudakkathil comparable companies-um deals-um projection-um aanu adisthaanam. Ningalkku onniladhikam offer kittiyittundo?")

# FAQ (myth: followers = company value). d904 pattern: viral kappa-biryani kitchen
duo("qv048", "raising_round", "A", "home", "രണ്ട് ലക്ഷം\nഫോളോവേഴ്സ്.\n\"അതാണ് നമ്മുടെ മൂല്യം\"", [
 ("A","wide","അരുണേ, നമ്മുടെ കപ്പ ബിരിയാണി റീൽ വൈറലായി. രണ്ട് ലക്ഷം ഫോളോവേഴ്സ്. ഇൻവെസ്റ്ററോട് ഫോളോവേഴ്സ് വെച്ച് മൂല്യം പറയാം."),
 ("V","V","സ്നേഹേ, വാല്യുവർ ഫോളോവേഴ്സിനെ എണ്ണില്ല."),
 ("A","A","പിന്നെ എന്തിനെ?"),
 ("V","wide","ഭാവി ക്യാഷ് ഫ്ലോ, താരതമ്യ കമ്പനികളും ഡീലുകളും, അല്ലെങ്കിൽ ആസ്തി. ഫോളോവേഴ്സ് ഓർഡറായി, ഓർഡർ വരുമാനമായി മാറിയാലേ കണക്കിൽ കയറൂ."),
 ("A","wide","അപ്പോ ലൈക്ക് ബാലൻസ് ഷീറ്റിൽ ഇല്ല."),
 ("V","wide","ലൈക്ക് വയറ് നിറയ്ക്കും, കണക്ക് നിറയ്ക്കില്ല.")],
 "ലൈക്ക് ബാലൻസ് ഷീറ്റിൽ\nകയറില്ല", CTA_WORTH, theme="faq",
 cap_ml="വൈറലായ കപ്പ ബിരിയാണി കിച്ചൺ ഫോളോവേഴ്സിന്റെ എണ്ണം വെച്ച് കമ്പനിയുടെ മൂല്യം പറയാൻ നോക്കി. വാല്യുവേഷന്റെ അംഗീകൃത രീതികൾ ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, താരതമ്യ കമ്പനികളും ഡീലുകളും, നെറ്റ് അസറ്റ് വാല്യു എന്നിവയാണ്. ഫോളോവേഴ്സ് വരുമാനമായാലേ കണക്കിൽ വരൂ. നിങ്ങളുടെ ഫോളോവേഴ്സ്: ഓർഡറോ ലൈക്കോ?",
 cap_en="A viral kappa-biryani kitchen wanted to quote its company value from its follower count. Valuers use discounted cash flow, comparable companies and deals, or net asset value; followers count only once they turn into orders and income. Your followers: orders or likes?",
 cap_mg="Viral aaya kappa biryani kitchen followers-inte ennam vechu company-yude moolyam parayaan nokki. Valuation-inte methods discounted cash flow, comparable companies and deals, net asset value. Followers varumaanam aayaale kanakkil varoo. Ningalude followers: order-o like-o?")

# New: foreign guest wants to invest. d904 pattern: Ayurveda retreat with a yoga regular from Germany
duo("qv049", "nri_share_issue", "A", "hospital", "ജർമൻ യോഗ ഗസ്റ്റ്\nചോദിച്ചു: \"ഞാനും\nഷെയർ എടുക്കട്ടെ?\"", [
 ("A","wide","ജോസഫേ, എല്ലാ വർഷവും വരുന്ന ആ ജർമൻ യോഗ ഗസ്റ്റ് നമ്മുടെ ആയുർവേദ റിട്രീറ്റ് കമ്പനിയിൽ ഷെയർ എടുക്കണം എന്ന്."),
 ("V","V","ലക്ഷ്മീ, നല്ല കാര്യം. സ്ഥിരം ഗസ്റ്റ് അല്ലേ, കുറഞ്ഞ നിരക്കിൽ ഷെയർ കൊടുത്താലോ?"),
 ("A","A","അങ്ങനെ പറ്റില്ല ജോസഫേ. വിദേശ നിക്ഷേപത്തിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാനാവില്ല."),
 ("A","wide","അംഗീകൃത രീതിയിൽ CA, സെബി മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തിയ റിപ്പോർട്ട് ആദ്യം."),
 ("V","wide","അപ്പോ ഉഴിച്ചിൽ സ്നേഹത്തോടെ, ഷെയർ കണക്കോടെ.")],
 "ഉഴിച്ചിൽ സ്നേഹത്തോടെ,\nഷെയർ കണക്കോടെ", CTA_VALUATION, theme="new",
 cap_ml="എല്ലാ വർഷവും വരുന്ന ഒരു ജർമൻ യോഗ ഗസ്റ്റ് ആയുർവേദ റിട്രീറ്റ് കമ്പനിയിൽ ഷെയർ എടുക്കാൻ ആഗ്രഹിക്കുന്നു. വിദേശ നിക്ഷേപത്തിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല; അംഗീകൃത രീതിയിൽ CA, സെബി രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തണം. നിങ്ങളുടെ ബിസിനസിൽ വിദേശ ഗസ്റ്റുകൾ വരാറുണ്ടോ?",
 cap_en="A yoga guest from Germany who comes every year wants shares in an Ayurveda retreat company. In foreign investment, shares cannot be issued below fair value, certified by a CA, SEBI-registered merchant banker or cost accountant using an accepted method, so a loyal guest gets no special rate. Do foreign guests visit your business?",
 cap_mg="Ella varshavum varunna oru German yoga guest Ayurveda retreat company-il share edukkaan aagrahikkunnu. Videsha nikshepathil share fair value-il thaazhe paadilla; CA, SEBI merchant banker, allenkil cost accountant certify cheyyanam. Ningalude business-il videsha guests varaarundo?")

# New: senior drummer leaves a chenda troupe company. d904 pattern: the drums are not the whole value
duo("qv050", "partner_exit", "A", "autostand", "\"അവന്റെ ചെണ്ട\nഅവന് കൊടുത്താൽ\nകണക്ക് തീർന്നു\"", [
 ("A","wide","ഷാജീ, നമ്മുടെ ചെണ്ടമേള കമ്പനിയിൽ നിന്ന് ആശാൻ ഇറങ്ങുന്നു. അദ്ദേഹത്തിന്റെ മൂന്ന് ചെണ്ട തിരികെ കൊടുത്താൽ തീർന്നില്ലേ?"),
 ("V","V","സജീ, ആശാന് കമ്പനിയിൽ ഷെയർ ഉണ്ട്. അടുത്ത രണ്ട് സീസണിലെ ഉത്സവ ബുക്കിംഗും കമ്പനിയുടേതല്ലേ?"),
 ("A","A","അത് ശരിയാ. ബുക്കിംഗ് ഡയറി നിറഞ്ഞിരിക്കുകയാ."),
 ("V","wide","പാർട്ണർ ഇറങ്ങുമ്പോൾ ആ തീയതിക്ക് വാല്യുവേഷൻ വേണം. ചെണ്ട ആസ്തി മാത്രം. ബുക്കിംഗിലെ ഭാവി വരുമാനവും കണക്കിൽ വരും."),
 ("A","wide","ചെണ്ട തിരികെ കൊടുത്താൽ താളം തീരില്ല.")],
 "ചെണ്ട കൊടുത്താൽ\nതാളം തീരില്ല", CTA_WORTH, theme="new",
 cap_ml="ചെണ്ടമേള കമ്പനിയിൽ നിന്ന് മുതിർന്ന പാർട്ണർ ഇറങ്ങുമ്പോൾ അദ്ദേഹത്തിന്റെ ചെണ്ടകൾ തിരികെ കൊടുത്താൽ കണക്ക് തീരില്ല. പാർട്ണർ എക്സിറ്റിന് ആ തീയതിയിലെ വാല്യുവേഷൻ വേണം: ആസ്തി ഒരു രീതി, ബുക്കിംഗിൽ നിന്നുള്ള ഭാവി ക്യാഷ് ഫ്ലോ മറ്റൊന്ന്. നിങ്ങളുടെ ബിസിനസിന്റെ ശക്തി: ആസ്തിയോ ബുക്കിംഗോ?",
 cap_en="When a senior partner leaves a chenda troupe company, handing back his drums does not settle his shares. A partner exit needs a valuation as of the exit date: net asset value is one method, discounted cash flow from the festival bookings is another. Your business's strength: assets or bookings?",
 cap_mg="Chendamela company-il ninnu muthirnna partner irangumbol addehathinte chendakal thirike koduthaal kanakku theerilla. Partner exit-inu aa theeyathiyile valuation venam: asset oru method, booking-il ninnulla bhaavi cash flow mattonnu. Ningalude business-inte shakthi: asset-o booking-o?")

# FAQ (co-founder joining later gets new shares): preferential allotment needs a registered valuer
duo("qv051", "raising_round", "A", "balcony", "രണ്ടാം വർഷം\nപുതിയ കോ-ഫൗണ്ടർ.\n\"ഷെയർ അങ്ങ് കൊടുക്കാം\"", [
 ("A","wide","വിവേകേ, നമ്മുടെ ടൂർ ബുക്കിംഗ് ആപ്പിൽ രണ്ടാം വർഷം ഒരു ടെക് കോ-ഫൗണ്ടർ വരുന്നു. പുതിയ ഷെയർ ഇറക്കി കൊടുക്കാം, അത്രയല്ലേ ഉള്ളൂ?"),
 ("V","V","അമ്മൂ, അയാൾ നമ്മുടെ കൂട്ടുകാരനാ. ഒരു മീറ്റിംഗ്, ഒരു ഒപ്പ്, തീർന്നു."),
 ("A","A","ഇല്ല വിവേകേ. ഒരാൾക്ക് മാത്രമായി പുതിയ ഷെയർ ഇറക്കുന്നതിന് നിയമം വേറെയാ."),
 ("A","wide","തിരഞ്ഞെടുത്ത ആൾക്ക് പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റ് ആയി ഷെയർ ഇറക്കാൻ രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം."),
 ("V","wide","സൗഹൃദം ഒപ്പിൽ, ഷെയർ റിപ്പോർട്ടിൽ.")],
 "സൗഹൃദം ഒപ്പിൽ,\nഷെയർ റിപ്പോർട്ടിൽ", CTA_VALUATION, theme="faq",
 cap_ml="രണ്ടാം വർഷം ചേരുന്ന ടെക് കോ-ഫൗണ്ടർക്ക് പുതിയ ഷെയർ ഇറക്കുമ്പോൾ ഒരു മീറ്റിംഗും ഒപ്പും മാത്രം പോരാ. തിരഞ്ഞെടുത്ത ആൾക്ക് പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റ് ആയി ഷെയർ ഇറക്കാൻ രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം. നിങ്ങളുടെ ടീമിൽ ആരെങ്കിലും പിന്നീട് ചേർന്നോ?",
 cap_en="A tech co-founder joins a tour-booking app in its second year, and the founders plan to issue new shares with one meeting and a signature. Issuing new shares to selected people is a preferential allotment, and it needs a registered valuer's report. Did someone join your founding team later?",
 cap_mg="Randaam varsham cherunna tech co-founder-kku puthiya share irakkumbol oru meeting-um oppum maathram pora. Thiranjedutha aalkku preferential allotment aayi share irakkaan registered valuer-ude report venam. Ningalude team-il aarenkilum pinneedu chernno?")

# FAQ (three methods, three numbers: which one is right?)
duo("qv052", "raising_round", "A", "bank", "റിപ്പോർട്ടിൽ\nമൂന്ന് രീതി.\nമൂന്ന് നമ്പർ. ഏതാ ശരി?", [
 ("A","wide","കിരണേ, നമ്മുടെ മൺപാത്ര സ്റ്റുഡിയോയുടെ വാല്യുവേഷൻ റിപ്പോർട്ടിൽ മൂന്ന് രീതി, മൂന്ന് നമ്പർ. ഇതിൽ ഏതാ സത്യം?"),
 ("V","V","ദിവ്യേ, ഏറ്റവും വലുത് എടുത്ത് ഇൻവെസ്റ്ററെ കാണിക്കാം."),
 ("A","A","അങ്ങനെ പറ്റില്ല കിരണേ. ഭാവി വരുമാനം, താരതമ്യ കമ്പനികൾ, ആസ്തി: മൂന്നും മൂന്ന് വഴിക്ക് നോക്കുന്നു."),
 ("A","wide","തുടക്കത്തിൽ താരതമ്യവും പ്രൊജക്ഷനുമാ ഭാരം. റിപ്പോർട്ടിന്റെ ആവശ്യവും തീയതിയും നോക്കി വാല്യുവർ തീരുമാനിക്കും."),
 ("V","wide","വലിയ നമ്പർ ഇഷ്ടം, പക്ഷേ ശരിയായ നമ്പറേ നിൽക്കൂ.")],
 "വലിയ നമ്പർ ഇഷ്ടം,\nശരിയായ നമ്പർ നിൽക്കും", CTA_WORTH, theme="faq",
 cap_ml="മൺപാത്ര സ്റ്റുഡിയോയുടെ വാല്യുവേഷൻ റിപ്പോർട്ടിൽ മൂന്ന് രീതികൾ മൂന്ന് നമ്പർ കാണിച്ചു: ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, താരതമ്യ കമ്പനികളും ഡീലുകളും, നെറ്റ് അസറ്റ് വാല്യു. തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പിന് താരതമ്യവും പ്രൊജക്ഷനുമാണ് കൂടുതൽ ഭാരം, ഓരോ റിപ്പോർട്ടും ഒരു ആവശ്യത്തിനും തീയതിക്കും. നിങ്ങൾ ആദ്യം നോക്കുക: വരുമാനമോ ആസ്തിയോ?",
 cap_en="A pottery studio's valuation report showed three methods and three numbers: discounted cash flow, comparable companies and deals, and net asset value. You don't just pick the biggest; for early startups comparables and projections carry more weight, and every report is for a specific purpose and date. What do you look at first: income or assets?",
 cap_mg="Manpaathra studio-yude valuation report-il moonnu methods moonnu number kaanichu: discounted cash flow, comparable companies and deals, net asset value. Thudakkathile startup-inu comparables-um projection-um aanu kooduthal bhaaram, oro report-um oru aavashyathinum theeyathikkum. Ningal aadyam nokkuka: varumaanamo asset-o?",
 names=("ദിവ്യ", "കിരൺ"))

# FAQ (NRI: repatriation or non-repatriation basis changes the paperwork)
duo("qv053", "nri_share_issue", "A", "mall", "\"റിപാട്രിയേഷനോ\nനോൺ-റിപാട്രിയേഷനോ?\"\nഒരു ടിക്ക്, വലിയ വ്യത്യാസം", [
 ("A","wide","ആസിഫേ, അനിയത്തിയുടെ ടെക്സ്റ്റൈൽ കമ്പനിയിൽ ഞാൻ ഷെയർ എടുക്കും. ഫോമിൽ ഒരു ടിക്ക്: റിപാട്രിയേഷനോ നോൺ-റിപാട്രിയേഷനോ. രണ്ടും ഒന്നല്ലേ?"),
 ("V","V","ഫാത്തിമാ, അല്ല. പണം പിന്നീട് പുറത്തേക്ക് കൊണ്ടുപോകാവുന്ന റിപാട്രിയേഷൻ ആണെങ്കിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല."),
 ("A","A","അപ്പോ സാക്ഷ്യപ്പെടുത്തിയ വാല്യുവേഷൻ റിപ്പോർട്ട് വേണം. പിന്നെ?"),
 ("V","wide","മുപ്പത് ദിവസത്തിനുള്ളിൽ RBI-ക്ക് റിപ്പോർട്ടിംഗും. നോൺ-റിപാട്രിയേഷൻ ആണെങ്കിൽ ആഭ്യന്തര നിക്ഷേപം പോലെ കണക്കാക്കും."),
 ("A","wide","ഒരു ടിക്ക് ചെറുത്, അതിന്റെ പിന്നാലെ വരുന്ന പേപ്പർ വലുത്.")],
 "ടിക്ക് ചെറുത്,\nപിന്നാലെ വരുന്ന പേപ്പർ വലുത്", CTA_VALUATION, theme="faq",
 cap_ml="ഗൾഫിലെ ചേച്ചി അനിയത്തിയുടെ കമ്പനിയിൽ ഷെയർ എടുക്കുമ്പോൾ ഫോമിലെ ഒരു ടിക്ക് പ്രധാനം. റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല, വാല്യുവേഷൻ റിപ്പോർട്ടും മുപ്പത് ദിവസത്തിനുള്ളിൽ RBI റിപ്പോർട്ടിംഗും വേണം; നോൺ-റിപാട്രിയേഷൻ ആഭ്യന്തര നിക്ഷേപം പോലെ. നിങ്ങളുടെ NRI നിക്ഷേപം ഏത് അടിസ്ഥാനത്തിൽ?",
 cap_en="A Gulf-based sister taking shares in her sibling's home-textile company must tick one box: repatriation or non-repatriation. On a repatriation basis, shares cannot go below fair value, so a certified valuation report is needed and the allotment is reported to RBI within 30 days; non-repatriation NRI money is treated as domestic. Which basis is your NRI investment on?",
 cap_mg="Gulf-ile chechi aniyathiyude company-il share edukkumbol form-ile oru tick pradhaanam. Repatriation basis-il share fair value-il thaazhe paadilla, valuation report-um 30 divasathinullil RBI reporting-um venam; non-repatriation domestic nikshepam pole. Ningalude NRI nikshepam ethu basis-il?",
 names=("ഫാത്തിമ", "ആസിഫ്"))
