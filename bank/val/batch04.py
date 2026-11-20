# Company valuation batch 04 (20 Nov, month backlog). Facts only from topics.FACTS_VAL. Never state a value or a fee. People, firms and towns invented.
# crm scripts are built on STORY_THEMES C25 and #13 / #15 / #19 with changed sector, people and numbers.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

# FAQ: the "sales x 10" rule people repeat
duo("qv024", "raising_round", "A", "metro", "\"വിറ്റുവരവ് ഗുണം 10.\nഅതാണ് വാല്യുവേഷൻ\"\nആരു പറഞ്ഞു?", [
 ("A","wide","കിരണേ, നമ്മുടെ വാല്യുവേഷൻ കണ്ടുപിടിച്ചു. വർഷത്തെ വിൽപ്പന ഗുണം 10. ഒരു വീഡിയോയിൽ കണ്ടതാ."),
 ("V","V","അഞ്ജലീ, അത് ഒരു നിയമമല്ല. ഒരു ഇൻവെസ്റ്ററും ആ ഗുണനം ചോദിക്കില്ല."),
 ("A","A","പിന്നെ എങ്ങനെയാ കണക്ക്?"),
 ("V","V","രീതികൾ: ഭാവിയിലെ ക്യാഷ് ഫ്ലോ, സമാന കമ്പനികൾ, ആസ്തി മൂല്യം. തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പിന് സമാന കമ്പനികളും പ്രൊജക്ഷനും."),
 ("A","wide","അപ്പോ വീഡിയോ കണക്ക് ഡിലീറ്റ്."),
 ("V","wide","ഗുണിക്കാൻ എളുപ്പം, ന്യായീകരിക്കാൻ പാട്.")],
 "വാല്യുവേഷൻ ഒരു\nഗുണനപ്പട്ടികയല്ല", CTA_WORTH, theme="faq",
 cap_ml="വിറ്റുവരവിനെ ഒരു സംഖ്യ കൊണ്ട് ഗുണിച്ചാൽ വാല്യുവേഷൻ ആകില്ല. ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, സമാന കമ്പനികളുടെ താരതമ്യം, ആസ്തി മൂല്യം എന്നിവയാണ് രീതികൾ; തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും പ്രൊജക്ഷനും. ഈ ഗുണം 10 കേട്ടിട്ടുണ്ടോ?",
 cap_en="Multiplying your sales by a magic number is not a valuation. Accepted methods are discounted cash flow, comparable companies or deals, and net asset value; early startups lean on comparables and projections. Ever heard the 'sales times 10' rule?",
 cap_mg="Sales-ine oru number kondu gunichaal valuation aakilla. Discounted cash flow, comparable companies, net asset value - ithaanu methods; early startups-nu comparables-um projection-um. Ee 'times 10' rule kettittundo?")

# FAQ: who may certify fair value for money from abroad
duo("qv025", "nri_share_issue", "A", "mall", "\"എഞ്ചിനീയർ മച്ചാൻ\nഒപ്പിട്ട് തരും\"\nഫെയർ വാല്യു അങ്ങനെയല്ല", [
 ("A","wide","ജാഫറേ, ഖത്തറിലെ ഇക്ക ഷെയർ വാങ്ങുന്നു. ഫെയർ വാല്യു എന്റെ മച്ചാൻ എഴുതിത്തരും. അവൻ എഞ്ചിനീയറാ."),
 ("V","V","സുമയ്യാ, എഞ്ചിനീയർക്ക് കണക്ക് അറിയാം. പക്ഷേ ഒപ്പിടാൻ അധികാരം ഇല്ല."),
 ("A","A","പിന്നെ ആര് ഒപ്പിടണം?"),
 ("V","V","ഫെയർ വാല്യു CA, SEBI രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സർട്ടിഫൈ ചെയ്യണം. അതിന് താഴെ ഷെയർ പാടില്ല."),
 ("A","wide","മച്ചാൻ പാലം പണിയട്ടെ. കണക്ക് ശരിയായ ആളെക്കൊണ്ട്."),
 ("V","wide","ബന്ധം വേറെ, ഒപ്പ് വേറെ.")],
 "ഫെയർ വാല്യു\nആർക്കും എഴുതാനാകില്ല", CTA_VALUATION, theme="faq",
 cap_ml="റീപാട്രിയേഷൻ ബേസിസിൽ NRI അല്ലെങ്കിൽ വിദേശ നിക്ഷേപം വരുമ്പോൾ ഷെയർ ഫെയർ വാല്യുവിന് താഴെ ഇറക്കാൻ പാടില്ല. അത് CA, SEBI രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് അംഗീകരിച്ച രീതിയിൽ സർട്ടിഫൈ ചെയ്യണം. നിങ്ങളുടെ നിക്ഷേപകൻ ഏത് രാജ്യത്താണ്?",
 cap_en="When an NRI invests on a repatriation basis or foreign money comes in, shares cannot be issued below fair value, and that fair value must be certified by a CA, a SEBI-registered merchant banker or a cost accountant using an accepted method. A relative's signature won't do. Which country is your investor in?",
 cap_mg="Repatriation basis-il NRI allenkil foreign investment varumpol share fair value-nu thaazhe irakkaan paadilla. Athu CA, SEBI registered merchant banker allenkil cost accountant certify cheyyanam. Ningalude investor etha raajyathaanu?")

# NEW, d904 pattern: a fishing-boat company, assets vs income
duo("qv026", "raising_round", "B", "fishmarket", "3 ബോട്ട്, 2 വല.\n\"ബോട്ട് പഴയതാ,\nമൂല്യം വരുമാനം മാത്രം\"", [
 ("A","wide","ആന്റണീ, ഇൻവെസ്റ്റർ പറയുന്നു ബോട്ടുകൾ പഴയതാ, കമ്പനിയുടെ മൂല്യം മീൻ വിൽപ്പന മാത്രം നോക്കി മതിയെന്ന്."),
 ("V","V","സുമേ, മൂന്ന് ബോട്ടും വലയും കോൾഡ് റൂമും വെറുതെ കടലിൽ ഒഴുകുകയാണോ?"),
 ("A","A","അപ്പോ ആസ്തിയും കണക്കിൽ വരുമോ?"),
 ("V","V","ആസ്തി കൂടുതലുള്ള ബിസിനസിന് നെറ്റ് അസറ്റ് വാല്യു രീതി. വരുമാനത്തിന് ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ. ബിസിനസ് നോക്കി രീതി."),
 ("A","wide","അപ്പോ ബോട്ടിന്റെ രേഖയും മീനിന്റെ കണക്കും ഒരുമിച്ച് റെഡിയാക്കാം."),
 ("V","wide","ബോട്ട് പഴയതാകും, ആസ്തി കാണാതാകില്ല.")],
 "ആസ്തിക്കും വരുമാനത്തിനും\nവേറെ രീതി", CTA_WORTH, theme="new",
 cap_ml="ബോട്ട്, വല, കോൾഡ് റൂം പോലെ ആസ്തി കൂടുതലുള്ള ബിസിനസിന് നെറ്റ് അസറ്റ് വാല്യു രീതി നോക്കാം; വരുമാനം നോക്കാൻ ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ. ബിസിനസിന്റെ സ്വഭാവം നോക്കിയാണ് രീതി. നിങ്ങളുടെ ബിസിനസിന്റെ ബലം: ആസ്തിയോ വരുമാനമോ?",
 cap_en="For an asset-heavy business like boats, nets and a cold room, net asset value is one method; discounted cash flow looks at income. The business decides which method fits. Your business's strength: assets or income?",
 cap_mg="Boat, vala, cold room pole aasthi kooduthal ulla business-nu net asset value method nokkaam; varumaanam nokkaan discounted cash flow. Ningalude business-inte balam: aasthiyo varumaanamo?")

# NEW, d904 pattern: coconut-shell craft, "nobody like us"
duo("qv027", "raising_round", "B", "beach", "\"ചിരട്ട കൊണ്ട്\nലാമ്പ്. ഞങ്ങളെപ്പോലെ\nആരുമില്ല\"", [
 ("A","wide","നിഖിലേ, ഞങ്ങൾ ചിരട്ട കൊണ്ട് ലാമ്പ് ഉണ്ടാക്കുന്നു. ലോകത്ത് വേറെ ആരുമില്ല. അപ്പോ വാല്യുവേഷൻ എങ്ങനെ?"),
 ("V","V","ദിവ്യേ, ചിരട്ട പുതിയതാകാം. പക്ഷേ ഹാൻഡ്മെയ്ഡ് ഡെക്കർ വിൽക്കുന്നവർ ധാരാളം ഉണ്ട്."),
 ("A","A","അവരെ എന്തിനാ നോക്കുന്നത്?"),
 ("V","V","തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പിന്റെ വാല്യുവേഷൻ സമാന കമ്പനികളും ഡീലുകളും പിന്നെ സ്വന്തം പ്രൊജക്ഷനും നോക്കിയാണ്."),
 ("A","wide","അപ്പോ അടുത്തുള്ള അഞ്ച് ബ്രാൻഡുകളുടെ ലിസ്റ്റ് ഇന്ന് തന്നെ."),
 ("V","wide","ഉൽപ്പന്നം ഒന്നേയുള്ളൂ, താരതമ്യം പലതുണ്ട്.")],
 "പുതിയ ഉൽപ്പന്നത്തിനും\nതാരതമ്യം ഉണ്ട്", CTA_VALUATION, theme="new",
 cap_ml="നിങ്ങളെപ്പോലെ ആരുമില്ല എന്ന് തോന്നിയാലും വാല്യുവേഷന് സമാന കമ്പനികളും ഡീലുകളും നോക്കും. തുടക്കത്തിലെ സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും സ്വന്തം പ്രൊജക്ഷനുമാണ് പ്രധാനം. നിങ്ങളുടെ ഉൽപ്പന്നം ഒറ്റ വാക്കിൽ?",
 cap_en="Even if nobody makes exactly what you make, a valuation still looks at comparable companies and deals. For early startups, comparables and your own projections carry the weight. Your product in one word?",
 cap_mg="Ningale pole aarumilla ennu thonniyaalum valuation-nu comparable companies-um deals-um nokkum. Early startups-nu comparables-um swantham projection-um aanu pradhaanam. Ningalude product oru vaakkil?")

# FAQ: "the valuer will write what we ask"
duo("qv028", "raising_round", "A", "bank", "\"നമുക്ക് വേണ്ട\nനമ്പർ പറഞ്ഞാൽ\nറിപ്പോർട്ടിൽ വരും\"", [
 ("A","wide","മനോജേ, വാല്യുവറോട് നമുക്ക് വേണ്ട സംഖ്യ പറയാം. അത് റിപ്പോർട്ടിൽ എഴുതിയാൽ മതി."),
 ("V","V","ശ്രുതീ, റിപ്പോർട്ട് ഓർഡർ ചെയ്യുന്ന മെനു അല്ല."),
 ("A","A","പിന്നെ അതിൽ എന്താ വരുന്നത്?"),
 ("V","V","അംഗീകരിച്ച രീതിയിൽ, ഒരു പ്രത്യേക ആവശ്യത്തിനും ഒരു പ്രത്യേക തീയതിക്കും. കണക്കും പ്രൊജക്ഷനും പിന്തുണയ്ക്കുന്ന സംഖ്യ മാത്രം."),
 ("A","wide","അപ്പോ ആഗ്രഹമല്ല, പ്രൊജക്ഷൻ ശക്തമാക്കണം."),
 ("V","wide","റിപ്പോർട്ട് കണക്ക് പറയും, കൊതി പറയില്ല.")],
 "ആഗ്രഹിച്ച സംഖ്യ\nറിപ്പോർട്ടിൽ വരില്ല", CTA_WORTH, theme="faq",
 cap_ml="വാല്യുവേഷൻ റിപ്പോർട്ടിൽ നമുക്ക് ഇഷ്ടമുള്ള സംഖ്യ എഴുതിക്കാനാകില്ല. അംഗീകരിച്ച രീതിയിൽ, ഒരു പ്രത്യേക ആവശ്യത്തിനും തീയതിക്കും വേണ്ടിയാണ് അത്. നിങ്ങളുടെ പ്രൊജക്ഷൻ എഴുതി വച്ചിട്ടുണ്ടോ?",
 cap_en="You can't order the number you want in a valuation report. It is prepared by an accepted method, for a specific purpose and date, and the numbers have to back it. Are your projections written down?",
 cap_mg="Valuation report-il namukku ishtamulla number ezhuthikkaan pattilla. Accepted method-il, oru purpose-num date-num vendi aanu athu. Ningalude projection ezhuthi vechittundo?")

# FAQ, d904 pattern: a pottery studio that "will never raise"
duo("qv029", "share_transfer", "B", "shop", "\"ഇൻവെസ്റ്റർ വേണ്ട.\nഅപ്പോ വാല്യുവേഷനും\nവേണ്ട\"", [
 ("A","wide","സുരേഷേ, നമ്മുടെ മൺകല സ്റ്റുഡിയോയ്ക്ക് ഇൻവെസ്റ്റർ വേണ്ട. അപ്പോ വാല്യുവേഷനും ഒരിക്കലും വേണ്ടല്ലോ."),
 ("V","V","ബിനൂ, നിന്റെ പെങ്ങൾ എന്റെ കുറച്ച് ഷെയർ വാങ്ങാൻ നോക്കുന്നത് മറന്നോ?"),
 ("A","A","അത് വീട്ടുകാര്യമല്ലേ?"),
 ("V","V","ഷെയർ കൈമാറ്റം, പാർട്ണർ ഇറങ്ങൽ, ഇസോപ്പ്, ബൈബാക്ക്, മെർജർ: ഇവയ്ക്കെല്ലാം വാല്യുവേഷൻ വേണ്ടിവരാം. നിക്ഷേപം ഒരു കാരണം മാത്രം."),
 ("A","wide","അപ്പോ കളിമണ്ണിനൊപ്പം കണക്കും കുഴയ്ക്കണം."),
 ("V","wide","പണം വരുമ്പോൾ മാത്രമല്ല, ഷെയർ നീങ്ങുമ്പോഴും.")],
 "ഷെയർ നീങ്ങിയാൽ\nവാല്യുവേഷൻ", CTA_VALUATION, theme="faq",
 cap_ml="നിക്ഷേപകരെ എടുക്കുന്നില്ലെങ്കിലും വാല്യുവേഷൻ വേണ്ടിവരാം: ഷെയർ കൈമാറ്റം, പാർട്ണർ ഇറങ്ങൽ, ഇസോപ്പ്, ബൈബാക്ക്, മെർജർ എന്നിവയ്ക്ക്. നിങ്ങളുടെ കമ്പനിയിൽ ഷെയർ ഉടമകൾ എത്ര പേർ?",
 cap_en="Not taking investors doesn't mean you'll never need a valuation: share transfers, a partner's exit, ESOPs, buy-backs and mergers can all need one. How many shareholders does your company have?",
 cap_mg="Investors-ine edukkunnillenkilum valuation venditharaam: share transfer, partner exit, ESOP, buyback, merger. Ningalude company-yil shareholders ethra per?")

# CRM C25 (small ask with a promised return), mobile repair academy
duo("qv030", "raising_round", "A", "mobileshop", "\"മൂന്ന് വർഷത്തിൽ\nഇരട്ടി തരാം\"\nഇൻവെസ്റ്റർ ചിരിച്ചു", [
 ("A","wide","ഫഹദേ, ഞാൻ ഇൻവെസ്റ്ററോട് പറഞ്ഞു, ഫേസ് ഒന്നിന് പണം തന്നാൽ മൂന്ന് വർഷത്തിൽ ഇരട്ടി. അയാൾ ചിരിച്ചു."),
 ("V","V","ഹന്നാ, അയാൾ ചോദിച്ചത് റിട്ടേൺ വാഗ്ദാനമല്ല. ഷെയർ ആണ്."),
 ("A","A","അപ്പോ എത്ര ശതമാനം കൊടുക്കും എന്ന് എങ്ങനെ അറിയും?"),
 ("V","V","നിക്ഷേപം എടുക്കുമ്പോൾ ആദ്യം കമ്പനിയുടെ വാല്യുവേഷൻ. സമാന കമ്പനികളും പ്രൊജക്ഷനും നോക്കി, ആ തീയതിക്ക്."),
 ("A","wide","അപ്പോ വാഗ്ദാനം വെട്ടി, പ്രൊജക്ഷൻ എഴുതാം."),
 ("V","wide","വാഗ്ദാനം കേട്ട് ചിരിക്കും, കണക്ക് കണ്ട് ഇരിക്കും.")],
 "റിട്ടേൺ വാഗ്ദാനമല്ല,\nവാല്യുവേഷൻ", CTA_VALUATION, theme="crm",
 cap_ml="നിക്ഷേപകന് ഇരട്ടി റിട്ടേൺ വാഗ്ദാനം ചെയ്യുന്നതിന് പകരം, എത്ര ഷെയർ കൊടുക്കണം എന്ന് അറിയാൻ കമ്പനിയുടെ വാല്യുവേഷൻ വേണം. തുടക്കത്തിൽ അത് സമാന കമ്പനികളും പ്രൊജക്ഷനും നോക്കിയാണ്. നിങ്ങൾ ഇൻവെസ്റ്ററോട് എന്താണ് പറഞ്ഞത്: ശതമാനമോ റിട്ടേണോ?",
 cap_en="Instead of promising an investor double their money, know what your company is worth so you know how many shares to offer. Early on, that rests on comparables and projections, as of a specific date. What did you pitch: a percentage or a return?",
 cap_mg="Investor-nu irattu return vaagdaanam cheyyunnathinu pakaram, ethra share kodukkanam ennariyaan company valuation venam. Thudakkathil athu comparables-um projection-um nokki aanu. Ningal pitch cheythathu: percentage-o return-o?")

# CRM #13 (friend's money with no paper), now turning into shares
duo("qv031", "raising_round", "B", "kitchen", "4 വർഷം മുമ്പത്തെ\nകടം. ഇപ്പോ\n\"ഷെയർ ആക്കിത്തരൂ\"", [
 ("A","wide","രാജേഷേ, നാല് വർഷം മുമ്പ് നിന്റെ കൂട്ടുകാരൻ തന്ന പണം. ഇപ്പോ അവൻ പറയുന്നു, തിരികെ വേണ്ട, ഷെയർ മതി."),
 ("V","V","ബിന്ദൂ, നല്ലതല്ലേ. അന്ന് തന്ന തുകയ്ക്ക് അന്നത്തെ കണക്കിൽ ഷെയർ കൊടുക്കാം."),
 ("A","A","അന്നത്തെ കണക്കോ? ഇന്ന് കമ്പനി പഴയതല്ലല്ലോ."),
 ("V","V","ശരിയാണ്. ഇന്ന് പുതിയ ഷെയർ ഇറക്കുമ്പോൾ പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന് രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം, ഇന്നത്തെ തീയതിക്ക്."),
 ("A","wide","അപ്പോ സൗഹൃദം പഴയത്, കണക്ക് പുതിയത്."),
 ("V","wide","കടം പഴയതാകും, ഷെയർ ഇന്നത്തേതാണ്.")],
 "കടം ഷെയറാകുമ്പോൾ\nഇന്നത്തെ വാല്യുവേഷൻ", CTA_VALUATION, theme="crm",
 cap_ml="പഴയ കടം ഷെയറായി മാറ്റുമ്പോൾ, ഇന്ന് ഷെയർ ഇറക്കുന്ന തീയതിക്കുള്ള വാല്യുവേഷൻ വേണം. പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന് രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് നിർബന്ധം. കൂട്ടുകാരിൽ നിന്ന് പേപ്പർ ഇല്ലാതെ പണം വാങ്ങിയിട്ടുണ്ടോ?",
 cap_en="Turning an old friendly loan into shares? The shares are issued today, so the valuation must be as of today, and a preferential allotment needs a registered valuer's report. Ever taken money from a friend without paperwork?",
 cap_mg="Pazhaya kadam share aakki maattumpol innathe date-nulla valuation venam. Preferential allotment-nu registered valuer-ude report nirbandham. Friends-il ninnu paper illaathe paisa vaangiyittundo?")

# CRM #15 (co-founder leaves after 6 months with his shares)
duo("qv032", "partner_exit", "A", "garage", "6 മാസം കഴിഞ്ഞ്\nഅവൻ പോയി.\n25% കൂടെ പോയി", [
 ("A","wide","ജിതിനേ, ആറ് മാസം കഴിഞ്ഞ് വിഷ്ണു പോയി. പക്ഷേ അവന്റെ 25% ഷെയർ ഇപ്പോഴും അവന്റെ പേരിൽ."),
 ("V","V","ഐശ്വര്യേ, ആറ് മാസമല്ലേ ഉണ്ടായുള്ളൂ. ഷെയർ വെറുതെ തിരികെ എടുക്കാം."),
 ("A","A","എഴുതിയ കരാർ ഒന്നുമില്ല. അവൻ സമ്മതിക്കില്ല."),
 ("V","V","എങ്കിൽ ഷെയർ വാങ്ങണം. പാർട്ണർ ഇറങ്ങുമ്പോൾ ആ തീയതിക്ക് അംഗീകരിച്ച രീതിയിലുള്ള വാല്യുവേഷൻ ആണ് തർക്കം തീർക്കുന്നത്."),
 ("A","wide","അടുത്ത പാർട്ണർ വരുമ്പോൾ ആദ്യം കരാർ."),
 ("V","wide","ആള് പോയാലും ഷെയർ പോകില്ല.")],
 "ഇറങ്ങിയ പാർട്ണറുടെ\nഷെയറിനും കണക്ക്", CTA_WORTH, theme="crm",
 cap_ml="കോ-ഫൗണ്ടർ ആറ് മാസത്തിൽ ഇറങ്ങിയാലും, എഴുതിയ കരാർ ഇല്ലെങ്കിൽ ഷെയർ അയാളുടേത് തന്നെ. തിരികെ വാങ്ങാൻ ആ തീയതിക്കുള്ള വാല്യുവേഷൻ ആണ് ന്യായമായ വഴി. നിങ്ങളുടെ ഫൗണ്ടർ കരാർ എഴുതിയതാണോ?",
 cap_en="A co-founder who walks out after six months still owns their shares if nothing was written down. Buying them back fairly needs a valuation as of that date, by an accepted method. Is your founders' agreement in writing?",
 cap_mg="Co-founder aaru maasathil irangiyaalum, ezhuthiya agreement illenkil share avarudethu thanne. Thirike vaangaan aa date-nulla valuation aanu nyaayamaaya vazhi. Ningalude founder agreement ezhuthiyathaano?")

# CRM #19 ("I'll talk to my partner and call back"), the report date runs out
duo("qv033", "raising_round", "B", "railway", "\"പാർട്ണറോട് ചോദിച്ച്\nവിളിക്കാം\"\n8 മാസം കഴിഞ്ഞു", [
 ("A","wide","ദിനേശേ, ഇൻവെസ്റ്റർ വീണ്ടും വിളിച്ചു. ഞാൻ പാർട്ണറോട് ചോദിക്കാമെന്ന് പറഞ്ഞിട്ട് എട്ട് മാസമായി."),
 ("V","V","ഷീബേ, സാരമില്ല. അന്നത്തെ വാല്യുവേഷൻ റിപ്പോർട്ട് കൈയിൽ ഉണ്ടല്ലോ."),
 ("A","A","അതിന് ശേഷം നമ്മൾ രണ്ട് ഷോപ്പ് കൂടി തുറന്നു."),
 ("V","V","എങ്കിൽ ആ റിപ്പോർട്ട് പഴയ കമ്പനിയുടേതാണ്. വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും തീയതിക്കും മാത്രം."),
 ("A","wide","ഇനി കോൾ തീർക്കാൻ ഡേറ്റ് ഇടാം. എട്ട് മാസമല്ല, എട്ട് ദിവസം."),
 ("V","wide","തീരുമാനം വൈകിയാൽ, റിപ്പോർട്ട് പഴകും.")],
 "വൈകിയാൽ റിപ്പോർട്ടും\nപഴകും", CTA_VALUATION, theme="crm",
 cap_ml="തീരുമാനം മാസങ്ങൾ നീണ്ടാൽ, അതിനിടെ കമ്പനി മാറിയാൽ പഴയ വാല്യുവേഷൻ റിപ്പോർട്ട് മതിയാകില്ല. വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും തീയതിക്കും വേണ്ടിയാണ്. നിങ്ങൾ എത്ര കാലമായി 'തിരിച്ചു വിളിക്കാം' എന്ന് പറയുന്നു?",
 cap_en="If a deal drags on for months and the company changes meanwhile, the old valuation report won't fit: a valuation is for a specific purpose and date. How long have you been saying 'I'll call back'?",
 cap_mg="Theerumaanam maasangal neendaal, athinidayil company maariyaal pazhaya valuation report mathiyaakilla. Valuation oru purpose-num date-num vendi aanu. Ningal ethra kaalamaayi 'thirichu vilikkaam' ennu parayunnu?")
