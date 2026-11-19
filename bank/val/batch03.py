# Company valuation batch 03 (20 Nov, month backlog). Facts only from topics.FACTS_VAL. Never state a value or a fee. People, firms and towns invented.
# crm scripts are built on STORY_THEMES C25-C28 with changed sector, people and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

duo("qv014", "raising_round", "A", "textile", "2 വർഷം പണിതു.\nവാല്യുവേഷനിൽ\nകണ്ടത് 6 മാസം", [
 ("A","wide","പ്രകാശേ, രണ്ട് വർഷം നമ്മൾ കർട്ടൻ ഡിസൈൻ ചെയ്തു. റിപ്പോർട്ടിൽ കമ്പനിയുടെ ആറ് മാസം മാത്രം!"),
 ("V","V","രമ്യേ, ആ രണ്ട് വർഷത്തെ ബില്ലുകൾ ആരുടെ പേരിലായിരുന്നു?"),
 ("A","A","നമ്മുടെ സ്വന്തം പേരിൽ. കമ്പനി വന്നത് പിന്നെയാ."),
 ("V","V","വാല്യുവേഷൻ കമ്പനിയുടേതാണ്. അതിന്റെ കണക്ക്, ആസ്തി, പ്രൊജക്ഷൻ, സമാന കമ്പനികൾ. പുറത്ത് ചെയ്ത പണി അതിൽ വരില്ല."),
 ("A","wide","അപ്പോ ഇനി എല്ലാ ഓർഡറും കമ്പനിയുടെ പേരിൽ."),
 ("V","wide","പേരിൽ ഇല്ലാത്തത് കണക്കിലും ഇല്ല.")],
 "കമ്പനിയുടെ പേരിൽ\nഇല്ലാത്തത് കണക്കിലില്ല", CTA_WORTH, theme="crm",
 cap_ml="കമ്പനി തുടങ്ങും മുമ്പ് സ്വന്തം പേരിൽ ചെയ്ത പ്രോജക്ടുകൾ കമ്പനിയുടെ വാല്യുവേഷനിൽ സാധാരണ കാണില്ല. വാല്യുവേഷൻ കമ്പനിയുടെ കണക്കും ആസ്തിയും പ്രൊജക്ഷനും നോക്കിയാണ്. നിങ്ങളുടെ ഓർഡറുകൾ ആരുടെ പേരിലാണ്?",
 cap_en="Projects you billed in your own name before forming the company usually don't show up in the company's valuation. A valuation looks at the company's own numbers, assets and projections. Whose name are your orders in?",
 cap_mg="Company thudangum mumpu swantham perilu cheytha project-ukal company valuation-il saadharana kaanilla. Valuation company-yude kanakkum aasthiyum projection-um nokki aanu. Ningalude order-ukal aarude perilaanu?")

duo("qv015", "share_transfer", "A", "handloom", "\"30 വർഷത്തെ കട\nഎത്ര വരും?\"\n\"അറിയില്ല\"", [
 ("A","wide","കുമാരേട്ടാ, അച്ഛന്റെ സാരിക്കട പുതിയ ഓൺലൈൻ കമ്പനിയിലേക്ക് ചേർക്കണം. അതിന് എത്ര ഷെയർ കിട്ടും?"),
 ("V","V","ലീലേ, കട തുടങ്ങിയിട്ട് മുപ്പത് വർഷം. പക്ഷേ ഇതുവരെ ആരും അതിന്റെ മൂല്യം കണക്കാക്കിയിട്ടില്ല."),
 ("A","A","അപ്പോ ഒരു തുക ഊഹിച്ച് ഇട്ടാലോ?"),
 ("V","V","പറ്റില്ല. വാല്യുവേഷൻ വേണം. സ്റ്റോക്കും കെട്ടിടവും നോക്കുന്ന നെറ്റ് അസറ്റ്, വരുമാനം നോക്കുന്ന ക്യാഷ് ഫ്ലോ."),
 ("A","wide","അപ്പോ പഴക്കം മാത്രം പോരാ, കണക്കും വേണം."),
 ("V","wide","മുപ്പത് വർഷം ഓർമ്മയിൽ, മൂല്യം റിപ്പോർട്ടിൽ.")],
 "പഴയ ബിസിനസ്സിന്റെ\nമൂല്യം ഊഹിക്കരുത്", CTA_WORTH, theme="crm",
 cap_ml="കുടുംബ ബിസിനസ് പുതിയ കമ്പനിയിലേക്ക് ചേർക്കുമ്പോൾ അതിന്റെ മൂല്യം ഊഹിക്കരുത്. നെറ്റ് അസറ്റ്, ക്യാഷ് ഫ്ലോ പോലുള്ള രീതികളിൽ വാല്യുവേഷൻ ചെയ്യൂ. നിങ്ങളുടെ കുടുംബ ബിസിനസ്സിന് എത്ര വർഷമായി?",
 cap_en="Moving a family business into a new company? Don't guess what it is worth: get a valuation using methods like net asset value and cash flows. How old is your family business?",
 cap_mg="Kudumba business puthiya company-ilekku cherkkumbol athinte moolyam oohikkaruthu. Net asset, cash flow pole ulla reethiyil valuation cheyyu. Ningalude kudumba business-nu ethra varshamaayi?")

duo("qv016", "raising_round", "A", "bakery", "\"ചെറിയ തുകയല്ലേ,\nകണക്ക് എന്തിന്?\"\nമാമന്റെ ഒറ്റ ചോദ്യം", [
 ("A","wide","സാബുവേ, പെറ്റ് ഫുഡ് ബ്രാൻഡിന്റെ ആദ്യ ഘട്ടത്തിന് മാമനോട് ഒരു ചെറിയ തുക ചോദിച്ചു. മൂന്ന് വർഷത്തിൽ ലാഭം തരാമെന്നും."),
 ("V","V","ജിഷേ, മാമൻ തിരിച്ച് എന്ത് ചോദിച്ചു?"),
 ("A","A","പണത്തിന് പകരം എത്ര ശതമാനം ഷെയർ എന്ന്. ഞാൻ ഞെട്ടിപ്പോയി."),
 ("V","V","തുക ചെറുതായാലും ഷെയർ കൊടുക്കുന്നെങ്കിൽ മൂല്യം അറിയണം. തുടക്കക്കാർക്ക് സമാന കമ്പനികളും പ്രൊജക്ഷനും നോക്കും."),
 ("A","wide","അപ്പോ ആദ്യം പ്രൊജക്ഷൻ, പിന്നെ മാമനെ കാണാം."),
 ("V","wide","തുക ചെറുതാകാം. ശതമാനം അങ്ങനെയല്ല.")],
 "ചെറിയ നിക്ഷേപത്തിനും\nശതമാനം കണക്കിൽ നിന്ന്", CTA_VALUATION, theme="crm",
 cap_ml="ചെറിയ തുകയുടെ നിക്ഷേപമായാലും ഷെയർ നൽകുന്നെങ്കിൽ കമ്പനിയുടെ മൂല്യം അറിയണം. ആദ്യഘട്ട സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും പ്രൊജക്ഷനുമാണ് അടിസ്ഥാനം. നിങ്ങളോട് ആരെങ്കിലും ശതമാനം ചോദിച്ചിട്ടുണ്ടോ?",
 cap_en="Even a small investment in exchange for shares needs to know what the company is worth. For early startups, comparables and projections carry the weight. Has anyone asked you for a percentage yet?",
 cap_mg="Cheriya thuka aayaalum share kodukkunnenkil company-yude moolyam ariyanam. Early startup-nu comparables-um projection-um aanu adisthaanam. Ningalodu aarenkilum percentage chodichittundo?")

duo("qv017", "raising_round", "A", "hostel", "ഇൻവെസ്റ്റർ മീറ്റിംഗ്\nഅടുത്ത മാസം.\nകൈയിൽ ഒരു സ്ലൈഡ്", [
 ("A","wide","സഞ്ജൂ, അടുത്ത മാസം ഇൻവെസ്റ്റർ മീറ്റിംഗ്. വാല്യുവേഷൻ സ്ലൈഡിൽ ഒരു വലിയ നമ്പർ ഇട്ടാലോ?"),
 ("V","V","അലീനേ, ആ നമ്പർ എവിടെ നിന്ന് വരും?"),
 ("A","A","മറ്റ് ആപ്പുകൾക്ക് കിട്ടിയത് നോക്കി. അത്ര മതിയല്ലോ."),
 ("V","V","നമ്മളെപ്പോലെ തുടക്കത്തിലുള്ളവർക്ക് താരതമ്യവും നമ്മുടെ സ്വന്തം പ്രൊജക്ഷനും ചേർന്നാണ് കണക്ക്. പ്രൊജക്ഷൻ ഇല്ലെങ്കിൽ പകുതിയേ ഉള്ളൂ."),
 ("A","wide","അപ്പോ ഈ ആഴ്ച പ്രൊജക്ഷൻ, അടുത്ത ആഴ്ച വാല്യുവേഷൻ."),
 ("V","wide","സ്ലൈഡിലെ നമ്പറിന് പിന്നിൽ ഒരു ഷീറ്റ് വേണം.")],
 "നമ്പറിന് മുമ്പ്\nപ്രൊജക്ഷൻ", CTA_VALUATION, theme="crm",
 cap_ml="ഫണ്ട് റെയ്സിന് മുമ്പ് വാല്യുവേഷനും പ്രൊജക്ഷനും ഒരുമിച്ചാണ് തയ്യാറാക്കേണ്ടത്. ആദ്യഘട്ട സ്റ്റാർട്ടപ്പിന്റെ വാല്യുവേഷൻ താരതമ്യത്തെയും പ്രൊജക്ഷനെയും ആശ്രയിക്കുന്നു. നിങ്ങളുടെ പ്രൊജക്ഷൻ റെഡിയാണോ?",
 cap_en="Before you raise, build the projections and the valuation together. An early startup's valuation leans on comparables and its own projections. Are your projections ready?",
 cap_mg="Fund raise-nu mumpu valuation-um projection-um orumichaanu thayyaaraakkendathu. Early startup valuation comparables-um projection-um aashrayikkunnu. Ningalude projection ready aano?")

duo("qv018", "partner_exit", "B", "gym", "\"അന്ന് ഇട്ട തുക\nതിരികെ തരാം\"\nബൈബാക്ക് അങ്ങനെയല്ല", [
 ("A","wide","ജസ്റ്റിനേ, തുടക്കത്തിൽ പണം ഇട്ട ഡോക്ടർ ഷെയർ തിരികെ തരാമെന്ന്. അന്ന് ഇട്ട തുക അങ്ങ് മടക്കി കൊടുത്താൽ പോരേ?"),
 ("V","V","റിയേ, അന്ന് നമുക്ക് ഒരു ജിം. ഇന്ന് നാല് ബ്രാഞ്ച്. കമ്പനി അതേപോലെയാണോ?"),
 ("A","A","അല്ല. പക്ഷേ അതല്ലേ എളുപ്പം?"),
 ("V","V","കമ്പനി സ്വന്തം ഷെയർ തിരികെ വാങ്ങുന്ന ബൈബാക്കിന് വാല്യുവേഷൻ വേണം. ഇന്നത്തെ തീയതിയിലെ മൂല്യം, അംഗീകൃത രീതിയിൽ."),
 ("A","wide","അപ്പോ പഴയ തുകയല്ല, ഇന്നത്തെ കണക്ക്."),
 ("V","wide","മസിൽ മാത്രമല്ല, ഷെയറും വളരും.")],
 "ബൈബാക്കിന്\nഇന്നത്തെ വാല്യുവേഷൻ", CTA_VALUATION, theme="faq",
 cap_ml="കമ്പനി സ്വന്തം ഷെയർ തിരികെ വാങ്ങുന്ന ബൈബാക്കിന് വാല്യുവേഷൻ വേണം. പഴയ നിക്ഷേപ തുകയല്ല, ആ തീയതിയിലെ കണക്കാണ് നോക്കുന്നത്. നിങ്ങളുടെ കമ്പനി ഷെയർ തിരികെ വാങ്ങാൻ ആലോചിക്കുന്നുണ്ടോ?",
 cap_en="A share buy-back needs a valuation as of that date, not the amount the investor put in years ago. Is your company planning to buy back shares?",
 cap_mg="Company swantham share thirike vaangunna buyback-nu valuation venam. Pazhaya thuka alla, aa theeyathiyile kanakku aanu nokkunnathu. Ningalude company buyback aalochikkunnundo?")

duo("qv019", "share_transfer", "B", "weddinghall", "രണ്ട് കമ്പനിയും\nനമ്മുടേത്. ഒന്നാക്കാൻ\nകണക്ക് വേണോ?", [
 ("A","wide","ശരത്തേ, നമ്മുടെ ഡെക്കറേഷൻ കമ്പനിയും കാറ്ററിംഗ് കമ്പനിയും ഒന്നാക്കിയാലോ? രണ്ടും നമ്മുടേതല്ലേ."),
 ("V","V","കാവ്യേ, രണ്ടിലും ഷെയർഹോൾഡർമാർ ഒരേ ആളുകളാണോ?"),
 ("A","A","ഡെക്കറേഷനിൽ എന്റെ അനിയത്തിക്കും ഷെയറുണ്ട്."),
 ("V","V","മെർജറിന് വാല്യുവേഷൻ വേണം. ഓരോ കമ്പനിക്കും എത്ര മൂല്യം എന്ന് നോക്കിയാണ് ആർക്ക് എത്ര ഷെയർ എന്ന് തീരുമാനിക്കുന്നത്."),
 ("A","wide","അപ്പോ സ്വന്തം കമ്പനികളായാലും റിപ്പോർട്ട് വേണം."),
 ("V","wide","കല്യാണം രണ്ട് കുടുംബത്തിന്റേത്. മെർജർ രണ്ട് കണക്കിന്റേത്.")],
 "മെർജറിന് മുമ്പ്\nരണ്ട് വാല്യുവേഷൻ", CTA_VALUATION, theme="faq",
 cap_ml="രണ്ട് കമ്പനികൾ ഒന്നാക്കുന്ന മെർജറിന് വാല്യുവേഷൻ വേണം, ഉടമകൾ ഒരേ കുടുംബമായാലും. ഓരോ കമ്പനിയുടെയും മൂല്യം നോക്കിയാണ് ഷെയർ തീരുമാനിക്കുന്നത്. നിങ്ങൾക്ക് ഒന്നിലധികം കമ്പനികളുണ്ടോ?",
 cap_en="Merging two companies needs a valuation, even when the same family owns both: each company's value decides who gets how many shares. Do you run more than one company?",
 cap_mg="Randu company onnaakkunna merger-nu valuation venam, udamakal ore kudumbam aayaalum. Oro company-yudeyum moolyam nokki aanu share theerumaanikkunnathu. Ningalkku onniladhikam company undo?")

duo("qv020", "raising_round", "B", "park", "ലാഭം പൂജ്യം.\nഅപ്പോ കമ്പനിയുടെ\nമൂല്യവും പൂജ്യമോ?", [
 ("A","wide","അനന്തൂ, നിന്റെ തെയ്യം മുടി റെപ്ലിക്കകൾക്ക് പുറംനാട്ടിൽ നിന്ന് ഓർഡർ. ഇൻവെസ്റ്റർ വാല്യുവേഷൻ ചോദിച്ചു."),
 ("V","V","ഗായത്രീ, ഈ വർഷം ലാഭം ഇല്ല. അപ്പോ മൂല്യവും പൂജ്യമല്ലേ?"),
 ("A","A","അല്ല. ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ ഭാവി വരുമാനം നോക്കും. തുടക്കക്കാർക്ക് സമാന കമ്പനികളും പ്രൊജക്ഷനും."),
 ("V","V","അപ്പോ ഇന്നത്തെ ലാഭമല്ല, വരാനിരിക്കുന്ന ഓർഡറുകൾ എഴുതി കാണിക്കണം."),
 ("A","wide","അതെ. ഓരോ നമ്പറിനും ഒരു കാരണവും."),
 ("V","wide","ലാഭം ഇന്നില്ല. ഭാവി കണക്കിലുണ്ട്.")],
 "ലാഭം ഇല്ലെന്നത്\nമൂല്യം ഇല്ലെന്നല്ല", CTA_WORTH, theme="faq",
 cap_ml="ലാഭമില്ലാത്ത കമ്പനിക്ക് മൂല്യം പൂജ്യമല്ല. ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ ഭാവി വരുമാനം നോക്കുന്നു; ആദ്യഘട്ട സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും പ്രൊജക്ഷനും. നിങ്ങളുടെ ബിസിനസ് ഏത് കലാരൂപവുമായി ബന്ധപ്പെട്ടതാണ്?",
 cap_en="No profit does not mean zero value. Discounted cash flow looks at future income, and early startups lean on comparables and projections. Is your business built on a traditional art?",
 cap_mg="Laabham illaatha company-kku moolyam poojyam alla. DCF bhaavi varumaanam nokkum; early startup-nu comparables-um projection-um. Ningalude business ethu kalaaroopavumaayi bandhappettathaanu?")

duo("qv021", "nri_share_issue", "B", "gulfroom", "\"കൂട്ടുകാരനല്ലേ,\nപഴയ നിരക്കിൽ\nഷെയർ തരാം\"", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ തെങ്ങുകയറ്റ യന്ത്രക്കമ്പനിയിൽ കൂട്ടുകാരൻ എനിക്ക് പഴയ നിരക്കിൽ ഷെയർ തരാമെന്ന്."),
 ("V","V","നസീറിക്കാ, ഇങ്ങള് ഇവിടെ ജോലി ചെയ്യുന്ന NRI അല്ലേ? അപ്പോ നിയമം വേറെയാ."),
 ("A","A","സൗഹൃദത്തിനും നിയമമോ?"),
 ("V","V","റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിലുള്ള NRI നിക്ഷേപത്തിന് ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാൻ പാടില്ല. അംഗീകൃത രീതിയിലുള്ള വാല്യുവേഷൻ വേണം."),
 ("A","wide","അപ്പോ കൂട്ടുകാരന്റെ വാക്കല്ല, റിപ്പോർട്ടിലെ കണക്ക്."),
 ("V","wide","തെങ്ങിൽ യന്ത്രം കയറും. ഷെയറിൽ ഫെയർ വാല്യു.")],
 "NRI-ക്ക് ഫെയർ വാല്യുവിൽ\nതാഴെ ഷെയർ ഇല്ല", CTA_WORTH, theme="faq",
 cap_ml="ഗൾഫിലുള്ള NRI നാട്ടിലെ കമ്പനിയിൽ റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ നിക്ഷേപിക്കുമ്പോൾ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാൻ പാടില്ല, കൂട്ടുകാരനായാലും. അംഗീകൃത രീതിയിലുള്ള വാല്യുവേഷൻ വേണം. നിങ്ങൾ ഗൾഫിലാണോ?",
 cap_en="When an NRI invests in a Kerala company on a repatriation basis, shares cannot be issued below fair value, even between friends. A valuation by an accepted method is needed. Are you working in the Gulf?",
 cap_mg="Gulf-ile NRI repatriation basis-il naattile company-il nikshepikkumbol share fair value-il thaazhe kodukkaan paadilla, koottukaaran aayaalum. Valuation venam. Ningal Gulf-il aano?")

duo("qv022", "share_transfer", "B", "classroom", "ഇസോപ്പിന് എടുത്ത\nറിപ്പോർട്ട് ഷെയർ\nകൈമാറ്റത്തിനും?", [
 ("A","wide","ആദർശേ, കളരി അക്കാദമിയിൽ ഗുരുക്കളുടെ കുറച്ച് ഷെയർ ഒരു ശിഷ്യൻ വാങ്ങുന്നു. ഇസോപ്പിന് എടുത്ത റിപ്പോർട്ട് ഉണ്ടല്ലോ."),
 ("V","V","നിമ്മി ടീച്ചറേ, ആ റിപ്പോർട്ട് എന്തിന് വേണ്ടി എഴുതിയതാ?"),
 ("A","A","ജീവനക്കാർക്ക് ഷെയർ കൊടുക്കാൻ. കമ്പനി ഒന്നല്ലേ?"),
 ("V","V","വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും ഒരു തീയതിക്കുമാണ്. ഷെയർ കൈമാറ്റത്തിന് ആ ആവശ്യം പറഞ്ഞുള്ള റിപ്പോർട്ട് വേണം."),
 ("A","wide","അപ്പോ ഒരു റിപ്പോർട്ട് എല്ലാ അടവിനും പറ്റില്ല."),
 ("V","wide","ഓരോ അടവിനും ഓരോ ചുവട്. ഓരോ ആവശ്യത്തിനും ഓരോ റിപ്പോർട്ട്.")],
 "ഒരു ആവശ്യം,\nഒരു റിപ്പോർട്ട്", CTA_VALUATION, theme="new",
 cap_ml="ഇസോപ്പിന് വേണ്ടി ചെയ്ത വാല്യുവേഷൻ റിപ്പോർട്ട് ഷെയർ കൈമാറ്റത്തിന് അതേപടി ഉപയോഗിക്കാൻ പറ്റണമെന്നില്ല. ഓരോ റിപ്പോർട്ടും ഒരു ആവശ്യത്തിനും ഒരു തീയതിക്കുമാണ്. നിങ്ങളുടെ കൈയിലെ റിപ്പോർട്ട് ഏത് ആവശ്യത്തിനുള്ളതാണ്?",
 cap_en="A valuation done for ESOPs may not fit a share transfer: every report is for a specific purpose and date. What purpose was your last report written for?",
 cap_mg="ESOP-nu cheytha valuation report share transfer-nu athepadi upayogikkaan pattanamennilla. Oro report-um oru aavashyathinum oru theeyathikkum aanu. Ningalude report ethu aavashyathinullathaanu?")

chat("qv023", "esop_plan", "C", "\"ഇസോപ്പ് തരാം\"\nഎന്ന് ഓഫർ ലെറ്റർ.\nഎത്ര എന്ന് ചോദിച്ചാൽ?", ("ഫാത്തിമ", "മുനീർ"), [
 (0,"മുനീർ സാർ, ഓഫർ ലെറ്ററിൽ ഇസോപ്പ് എന്ന് മാത്രം. അതിന് എത്ര മൂല്യം എന്ന് എങ്ങനെ അറിയും?"),
 (1,"ഫാത്തിമ, ഗ്രാന്റ് ചെയ്യുന്ന ദിവസത്തെ കമ്പനി വാല്യുവേഷൻ നോക്കിയാണ് അത് കണക്കാക്കുന്നത്."),
 (0,"അപ്പോ ഇപ്പോൾ ആരെങ്കിലും പറയുന്ന ഒരു നമ്പർ അല്ലേ?"),
 (1,"അല്ല. അംഗീകൃത രീതിയിൽ, ആ തീയതിക്ക് വേണ്ടി ചെയ്യുന്ന റിപ്പോർട്ട്. ഊഹമല്ല."),
 (0,"എങ്കിൽ ഗ്രാന്റിന്റെ തീയതി എഴുതി തരുമോ?"),
 (1,"തരാം. വാക്ക് ഓഫറിൽ, മൂല്യം റിപ്പോർട്ടിൽ.")],
 "ഇസോപ്പിന്റെ മൂല്യം\nഗ്രാന്റ് ദിവസത്തെ കണക്കിൽ", CTA_VALUATION, theme="new",
 cap_ml="ഇസോപ്പ് ലഭിക്കുന്ന ജീവനക്കാർ അറിയേണ്ടത്: അതിന്റെ കണക്ക് ഗ്രാന്റ് ചെയ്യുന്ന ദിവസത്തെ കമ്പനി വാല്യുവേഷനിൽ നിന്നാണ്. ഗ്രാന്റ് തീയതി എഴുതി വാങ്ങൂ. നിങ്ങളുടെ ഓഫറിൽ ഇസോപ്പ് ഉണ്ടോ?",
 cap_en="Got ESOPs in your offer letter? Their worth is based on the company's valuation on the grant date, by an accepted method, not a number someone says. Get the grant date in writing. Does your offer include ESOPs?",
 cap_mg="ESOP kittunna employee ariyendathu: athinte kanakku grant cheyyunna divasathe company valuation-il ninnaanu. Grant date ezhuthi vaangu. Ningalude offer-il ESOP undo?")
