# Co-founder agreements batch 08 (28 Nov night). Partner-dispute reels: general information only, "a lawyer must see the documents",
# LLP First Schedule rules only for LLPs, always "may" for courts. New angles: an LLP's hit product moved to a partner's new company
# (para 12), a new partner brought in without consent (para 7), a change in the nature of business (para 8), a frozen firm account
# (s.9 interim measures); plus two founder stories (a co-founder leaving for a government job; a split asked for on payment day).
# Invented names, sectors and towns. Facts only from topics.FACTS_CFA. Never decide the split, never a fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

# FAQ (F23): 50/50 LLP, one hit product, the other partner wants to move it into his own new company
duo('cfd006', 'friends_cofounders', 'A', 'mobileshop', 'ഹിറ്റ് ഉൽപ്പന്നം\nഎൽഎൽപിയുടേത്. പാർട്ണർ\nഅത് പുതിയ കമ്പനിയിലേക്ക്', [
 ('A', 'wide', 'ഫഹദേ, നമ്മുടെ എൽഎൽപിയുടെ കഥകളി ഫോൺ കവറാണ് ഹിറ്റ്. പാർട്ണർ സ്വന്തം കമ്പനി തുടങ്ങി അത് അങ്ങോട്ട് മാറ്റാൻ പോകുന്നു.'),
 ('V', 'V', 'ഹന്നാ, എല്ലാം ഇമെയിലിലാണല്ലോ സമ്മതിച്ചത്. എൽഎൽപി എഗ്രിമെന്റ് ഇതിനെക്കുറിച്ച് എന്ത് പറയുന്നു?'),
 ('A', 'A', 'ലാഭം പകുതി എന്ന് മാത്രം. ഡിസൈനോ ബ്രാൻഡോ ഒന്നും എഴുതിയിട്ടില്ല.'),
 ('V', 'V', 'എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് ഫസ്റ്റ് ഷെഡ്യൂൾ: എൽഎൽപിയുടെ സ്വത്തോ പേരോ ഉപയോഗിച്ച് കിട്ടിയ നേട്ടത്തിന് പാർട്ണർ കണക്ക് പറയണം.'),
 ('A', 'wide', 'അപ്പോ ഇമെയിലും വിൽപ്പന കണക്കും ഡിസൈൻ ഫയലുകളും ഒരുമിച്ച് വെച്ച് വക്കീലിനെ കാണാം.'),
 ('V', 'wide', 'ഹിറ്റ് ആരുടേത് എന്ന് രേഖ പറയും.')],
 'ഹിറ്റ് ആരുടേത്\nഎന്ന് രേഖ പറയും', CTA_COFOUNDER, theme='faq',
 cap_ml='50/50 എൽഎൽപിയുടെ ഹിറ്റ് ഉൽപ്പന്നം ഒരു പാർട്ണർ സ്വന്തം പുതിയ കമ്പനിയിലേക്ക് മാറ്റാൻ നോക്കുന്നു. ആദ്യം എൽഎൽപി എഗ്രിമെന്റ് നോക്കണം; അത് മിണ്ടാത്തിടത്ത് എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പ്രകാരം എൽഎൽപിയുടെ സ്വത്തോ പേരോ ബിസിനസ് ബന്ധമോ ഉപയോഗിച്ചുള്ള നേട്ടത്തിന് പാർട്ണർ കണക്ക് പറയണം. ഇത് പൊതുവായ വിവരം മാത്രം; നിങ്ങളുടെ രേഖകൾ ഒരു വക്കീൽ കാണണം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ഉൽപ്പന്നം ആരുടേത് എന്ന് എഴുതിയിട്ടുണ്ടോ?',
 cap_en='In a 50/50 LLP, one partner plans to move the hit product into a new company of his own. The LLP agreement comes first; where it is silent, the First Schedule of the LLP Act says a partner must account for any benefit from using the LLP\'s property, name or business connection. General information only: a lawyer must see your documents. Does your agreement say who owns the product?',
 cap_mg='50/50 LLP-yude hit product oru partner swantham puthiya company-ilekku maattaan nokkunnu. Aadyam LLP agreement nokkanam; athu mindaathidathu LLP Act-ile First Schedule prakaaram LLP-yude swatho pero business bandhamo upayogichulla nettathinu partner kanakku parayanam. Ithu general information maathram; ningalude rekhakal oru vakeel kaananam. Ningalude agreement-il product aarudethu ennu ezhuthiyittundo?')

# NEW: Gulf-based partners find out a new partner is being added to their Kerala LLP without asking them (para 7)
duo('cfd007', 'remote_cofounder', 'B', 'gulf', '"അളിയനെ പാർട്ണർ\nആക്കുന്നു" ഞങ്ങളോട്\nഒരു വാക്ക് ചോദിക്കാതെ', [
 ('A', 'wide', 'ഫൈസലേ, നാട്ടിലെ നമ്മുടെ ട്രാവൽ എൽഎൽപിയിൽ സിബി അവന്റെ അളിയനെ പുതിയ പാർട്ണർ ആക്കാൻ പോകുന്നു. നമ്മളോട് ചോദിച്ചിട്ടില്ല.'),
 ('V', 'V', 'ഷിജൂ, നമ്മുടെ എൽഎൽപി എഗ്രിമെന്റിൽ പുതിയ പാർട്ണറെക്കുറിച്ച് എന്തെങ്കിലും ഉണ്ടോ?'),
 ('A', 'A', 'ഒന്നുമില്ല. അന്ന് ലീവിന് പോയപ്പോൾ തിരക്കിൽ ഒപ്പിട്ടതാ.'),
 ('V', 'V', 'എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് ഫസ്റ്റ് ഷെഡ്യൂൾ: എല്ലാ പാർട്ണർമാരുടെയും സമ്മതമില്ലാതെ പുതിയ പാർട്ണറെ ചേർക്കാനാവില്ല.'),
 ('A', 'wide', 'അപ്പോ എഗ്രിമെന്റ് കോപ്പിയും അവന്റെ മെസേജും എടുത്ത് നാട്ടിലെ ഒരു വക്കീലിനോട് സംസാരിക്കാം.'),
 ('V', 'wide', 'ദൂരെയാണെങ്കിലും സമ്മതം നമ്മുടേതാ.')],
 'ദൂരെയാണെങ്കിലും\nസമ്മതം നിങ്ങളുടേത്', CTA_COFOUNDER, theme='new',
 cap_ml='ഗൾഫിലുള്ള പാർട്ണർമാരോട് ചോദിക്കാതെ നാട്ടിലെ എൽഎൽപിയിൽ പുതിയ പാർട്ണറെ ചേർക്കാൻ നോക്കുന്നു. എൽഎൽപി എഗ്രിമെന്റ് ഇതിനെക്കുറിച്ച് മിണ്ടുന്നില്ലെങ്കിൽ, എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പ്രകാരം എല്ലാ പാർട്ണർമാരുടെയും സമ്മതമില്ലാതെ പുതിയ പാർട്ണർ വരില്ല. പൊതുവായ വിവരം മാത്രം; രേഖകൾ ഒരു വക്കീൽ കാണണം. നിങ്ങൾ വിദേശത്തിരുന്ന് നാട്ടിലെ ബിസിനസിൽ പാർട്ണറാണോ?',
 cap_en='Two partners working in the Gulf learn that a partner back home is adding his brother-in-law to their LLP without asking them. If the LLP agreement says nothing on this, the First Schedule of the LLP Act says no new partner comes in without the consent of all partners. General information only: a lawyer must see your documents. Are you a partner in a Kerala business from abroad?',
 cap_mg='Gulf-il ulla partners-inodu chodikkaathe naattile LLP-yil puthiya partner-e cherkkaan nokkunnu. LLP agreement ithine kurichu mindunnillenkil, LLP Act-ile First Schedule prakaaram ella partners-ntem sammathamillaathe puthiya partner varilla. General information maathram; rekhakal oru vakeel kaananam. Ningal videshathirunnu naattile business-il partner aano?',
 names=('ഷിജു', 'ഫൈസൽ'))

# NEW: three-partner bakery LLP, two want to turn it into an event company (para 8: majority for decisions, all partners for a change in the nature of business)
duo('cfd008', 'friends_cofounders', 'A', 'bakery', 'ബേക്കറി എൽഎൽപി\nഇനി ഇവന്റ് കമ്പനി?\n2 പേർ യെസ്, ഞാൻ നോ', [
 ('A', 'wide', 'ബിജോയ്, ബേക്കറി നിർത്തി നമ്മുടെ എൽഎൽപി ഇവന്റ് മാനേജ്മെന്റ് ആക്കാമെന്ന് മറ്റ് രണ്ടുപേരും. ഭൂരിപക്ഷം അവർക്കാണെന്ന്.'),
 ('V', 'V', 'ഷൈനീ, എഗ്രിമെന്റിൽ വോട്ടിനെക്കുറിച്ചോ ബിസിനസ് മാറ്റുന്നതിനെക്കുറിച്ചോ എന്താ ഉള്ളത്?'),
 ('A', 'A', 'ഒരു വരി പോലുമില്ല. ലാഭം മൂന്നായി പങ്കിടും എന്ന് മാത്രം.'),
 ('V', 'V', 'എങ്കിൽ ഫസ്റ്റ് ഷെഡ്യൂൾ: സാധാരണ തീരുമാനം ഭൂരിപക്ഷത്തിന്. പക്ഷേ ബിസിനസിന്റെ സ്വഭാവം മാറ്റാൻ എല്ലാ പാർട്ണർമാരുടെയും സമ്മതം വേണം.'),
 ('A', 'wide', 'പുതിയ ഓവൻ വാങ്ങാൻ വോട്ട് മതി. ബേക്കറി തന്നെ മാറ്റാൻ എന്റെ സമ്മതവും വേണം.'),
 ('V', 'wide', 'എന്നാലും നിങ്ങളുടെ രേഖ ഒരു വക്കീൽ നോക്കട്ടെ.')],
 'ഓവന് വോട്ട് മതി,\nബിസിനസ് മാറ്റാൻ എല്ലാവരും', CTA_COFOUNDER, theme='new',
 cap_ml='മൂന്ന് പാർട്ണർമാരുള്ള ബേക്കറി എൽഎൽപി ഇവന്റ് കമ്പനി ആക്കാൻ രണ്ടുപേർക്ക് താൽപര്യം, ഒരാൾക്ക് ഇല്ല. എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ: സാധാരണ തീരുമാനങ്ങൾ ഭൂരിപക്ഷത്തിന്, ഒരാൾക്ക് ഒരു വോട്ട്; പക്ഷേ ബിസിനസിന്റെ സ്വഭാവം മാറ്റാൻ എല്ലാവരുടെയും സമ്മതം. ഇത് എൽഎൽപിക്ക് മാത്രം, പൊതുവായ വിവരം; രേഖകൾ ഒരു വക്കീൽ കാണണം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ വോട്ടിംഗ് എഴുതിയിട്ടുണ്ടോ?',
 cap_en='Two of three partners want to turn their bakery LLP into an event company. Where the LLP agreement is silent, the LLP Act\'s First Schedule says ordinary decisions go by a majority of partners, one vote each, but the nature of the business cannot change without every partner\'s consent. LLP rule only, general information: a lawyer must see your documents. Does your agreement say how you vote?',
 cap_mg='Moonnu partners ulla bakery LLP event company aakkaan randu perkku thaalparyam, oraalkku illa. Agreement mindaathidathu LLP Act-ile First Schedule: saadhaarana theerumaanangal bhooripakshathinu, oraalkku oru vote; pakshe business-inte swabhaavam maattaan ellaavarudeyum sammatham. Ithu LLP-kku maathram, general information; rekhakal oru vakeel kaananam. Ningalude agreement-il voting ezhuthiyittundo?',
 names=('ഷൈനി', 'ബിജോയ്'))

# FAQ (F27): one partner has the bank block the other's signature; suppliers and staff wait (s.9 interim measures, general)
duo('cfd009', 'friends_cofounders', 'B', 'bank', 'ഒപ്പ് ബ്ലോക്ക്.\nസപ്ലയർ ബില്ലും ശമ്പളവും\nരണ്ടും മുടങ്ങി', [
 ('A', 'wide', 'സനലേ, പാർട്ണർ ബാങ്കിൽ കത്ത് കൊടുത്തു. ഇപ്പോ എന്റെ ഒപ്പിന് ചെക്ക് പാസാകില്ല. കാറ്ററിംഗ് സപ്ലയർമാരും ജോലിക്കാരും കാത്തിരിക്കുന്നു.'),
 ('V', 'V', 'ദീപ്തീ, നിങ്ങളുടെ പാർട്ണർഷിപ്പ് ഡീഡിൽ ആര് ഒപ്പിടും, തർക്കം വന്നാൽ എന്ത് എന്ന് എഴുതിയിട്ടുണ്ടോ?'),
 ('A', 'A', 'തർക്കം ആർബിട്രേഷനിലേക്ക് എന്നൊരു വരി ഉണ്ട്. പക്ഷേ അത് തുടങ്ങാൻ തന്നെ സമയം എടുക്കില്ലേ?'),
 ('V', 'V', 'ആർബിട്രേഷന് മുമ്പും ഇടക്കാല സംരക്ഷണം കോടതിയോട് ചോദിക്കാം, തുക സുരക്ഷിതമാക്കാനോ റിസീവറിനോ പോലുള്ളത്. തീരുമാനം കോടതിയുടേത്.'),
 ('A', 'wide', 'അപ്പോ സ്റ്റേറ്റ്മെന്റ്, ബാങ്കിലെ കത്തിന്റെ കോപ്പി, കൊടുക്കാനുള്ള ബില്ലുകളുടെ ലിസ്റ്റ്. ഇന്ന് തന്നെ വക്കീലിനെ കാണാം.'),
 ('V', 'wide', 'വഴക്ക് പാർട്ണർമാർക്ക്, നഷ്ടം ജോലിക്കാർക്ക്.')],
 'വഴക്ക് പാർട്ണർമാർക്ക്,\nനഷ്ടം ജോലിക്കാർക്ക്', CTA_COFOUNDER, theme='faq',
 cap_ml='പാർട്ണർമാർ തമ്മിലുള്ള വഴക്കിൽ ഒരാളുടെ ഒപ്പ് ബാങ്കിൽ ബ്ലോക്ക് ആയി, സപ്ലയർമാരും ജോലിക്കാരും കാത്തിരിക്കുന്നു. എഗ്രിമെന്റിൽ ആർബിട്രേഷൻ ഉണ്ടെങ്കിൽ, ആർബിട്രേഷന് മുമ്പും ഇടയിലും തുക സുരക്ഷിതമാക്കൽ, റിസീവർ പോലുള്ള ഇടക്കാല നടപടികൾ കോടതിയോട് ചോദിക്കാം; തീരുമാനം കോടതിയുടേത്. പൊതുവായ വിവരം മാത്രം; രേഖകൾ ഒരു വക്കീൽ കാണണം. നിങ്ങളുടെ ഡീഡിൽ ആര് ഒപ്പിടും എന്ന് എഴുതിയിട്ടുണ്ടോ?',
 cap_en='In a partners\' fight, one partner asked the bank to block the other\'s signature, and suppliers and staff are left unpaid. If the agreement has an arbitration clause, a party may ask a court for interim measures, such as securing an amount or appointing a receiver, even before the arbitration starts; the court decides. General information only: a lawyer must see your documents. Does your deed say who signs?',
 cap_mg='Partners thammilulla vazhakkil oraalude oppu bank-il block aayi, suppliers-um joliikkaarum kaathirikkunnu. Agreement-il arbitration undenkil, arbitration-inu mumpum idayilum thuka surakshithamaakkal, receiver pole idakkaala nadapadikal kodathiyodu chodikkaam; theerumaanam kodathiyudethu. General information maathram; rekhakal oru vakeel kaananam. Ningalude deed-il aaru oppidum ennu ezhuthiyittundo?',
 names=('ദീപ്തി', 'സനൽ'))

# CRM (co-founder pauses / leaves, written vesting): a co-founder gets a government job after a year and a half
duo('cfd010', 'friends_cofounders', 'A', 'library', 'PSC ജോലി കിട്ടി.\nകോ-ഫൗണ്ടർ പോകുന്നു.\nഅവന്റെ 30%?', [
 ('A', 'wide', 'ഗോകുലേ, PSC ജോലി കിട്ടിയതിൽ സന്തോഷം. പക്ഷേ നമ്മുടെ കാർഷിക ഡ്രോൺ സ്റ്റാർട്ടപ്പിലെ നിന്റെ 30% എന്ത് ചെയ്യും?'),
 ('V', 'V', 'ആരതീ, അത് എന്റെ കൂടെ പോരില്ലേ? ഒന്നര വർഷം ഞാനും പണിതതല്ലേ?'),
 ('A', 'A', 'നമ്മുടെ കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ നാല് വർഷത്തെ വെസ്റ്റിംഗും ഒരു വർഷ ക്ലിഫും ഉണ്ട്. നീയും ഒപ്പിട്ടതാ.'),
 ('V', 'V', 'അപ്പോ ഒന്നര വർഷം കൊണ്ട് വെസ്റ്റ് ആയത് എനിക്ക്. ബാക്കി?'),
 ('A', 'wide', 'വെസ്റ്റ് ആകാത്ത ഷെയർ ലീവർ ക്ലോസ് പ്രകാരം കമ്പനി തിരികെ വാങ്ങും. പുതിയ ആളെ എടുക്കാൻ അത് വേണം.'),
 ('V', 'wide', 'പണിതത് എനിക്ക്, ബാക്കി കമ്പനിക്ക്.')],
 'പണിതത് നിനക്ക്,\nബാക്കി കമ്പനിക്ക്', CTA_VESTING, theme='crm',
 cap_ml='കോ-ഫൗണ്ടർക്ക് സർക്കാർ ജോലി കിട്ടി, ഒന്നര വർഷം കഴിഞ്ഞ് പോകുന്നു. എഗ്രിമെന്റിൽ വെസ്റ്റിംഗ് (സാധാരണ രീതി: നാല് വർഷം, ഒരു വർഷ ക്ലിഫ്) ഉണ്ടെങ്കിൽ വെസ്റ്റ് ആയത് അവന്, വെസ്റ്റ് ആകാത്തത് ലീവർ ക്ലോസ് പ്രകാരം കമ്പനി തിരികെ വാങ്ങും. ആർക്ക് എത്ര എന്ന് നിങ്ങളാണ് തീരുമാനിക്കേണ്ടത്. നിങ്ങളുടെ ടീമിൽ ആരെങ്കിലും ജോലിക്ക് പോകാൻ ആലോചിക്കുന്നുണ്ടോ?',
 cap_en='A co-founder of an agri-drone startup got a government job after a year and a half. Because their co-founder agreement had vesting (a common practice is 4 years with a 1-year cliff) and a leaver clause, he keeps what has vested and the company buys back the unvested shares. Is anyone on your team thinking of leaving for a job?',
 cap_mg='Co-founder-inu sarkkar joli kitti, onnara varsham kazhinju pokunnu. Agreement-il vesting (common practice: 4 varsham, 1 varsham cliff) undenkil vest aayathu avanu, vest aakaathathu leaver clause prakaaram company thirike vaangum. Aarkku ethra ennu ningalaanu theerumaanikkendathu. Ningalude team-il aarenkilum joliykku pokaan aalochikkunnundo?',
 names=('ആരതി', 'ഗോകുൽ'))

# CRM (two friends on trust, nothing written; who owns what comes up when money arrives)
duo('cfd011', 'friends_cofounders', 'B', 'hostel', 'ആദ്യ വലിയ പേയ്മെന്റ്\nവന്ന ദിവസം അവൻ:\n"എനിക്ക് പകുതി"', [
 ('A', 'wide', 'ആൽബിനേ, ടർഫ് ബുക്കിംഗ് ആപ്പിന് ആദ്യ കോർപ്പറേറ്റ് ലീഗിന്റെ പേയ്മെന്റ് വന്നു. അന്ന് തന്നെ വരുൺ പറയുന്നു, അവന് പകുതി ഷെയർ വേണമെന്ന്.'),
 ('V', 'V', 'ഡെൽനേ, തുടങ്ങിയപ്പോൾ ആർക്ക് എത്ര എന്ന് നിങ്ങൾ മൂന്നുപേരും പറഞ്ഞിരുന്നോ?'),
 ('A', 'A', 'ഇല്ല. "നമ്മൾ ഒന്നല്ലേ" എന്ന് മാത്രം. ഒന്നും എഴുതിയിട്ടില്ല.'),
 ('V', 'V', 'എത്ര ശതമാനം എന്ന് ഞാൻ പറയില്ല, അത് നിങ്ങൾ തീരുമാനിക്കണം. പക്ഷേ തീരുമാനിക്കുന്നത് റോളും വെസ്റ്റിംഗും ചേർത്ത് എഗ്രിമെന്റിൽ എഴുതണം.'),
 ('A', 'wide', 'അടുത്ത പേയ്മെന്റിന് മുമ്പ് മൂന്നുപേരും ഇരുന്ന് എഴുതാം.'),
 ('V', 'wide', 'പണത്തിന് മുമ്പ് എഴുതിയാൽ കരാർ. ശേഷമായാൽ കലഹം.')],
 'പണത്തിന് മുമ്പ് കരാർ,\nശേഷമായാൽ കലഹം', CTA_COFOUNDER, theme='crm',
 cap_ml='ഒന്നും എഴുതാതെ തുടങ്ങിയ ആപ്പ് സ്റ്റാർട്ടപ്പിന് ആദ്യ വലിയ പേയ്മെന്റ് വന്ന ദിവസം ഒരു കോ-ഫൗണ്ടർ പകുതി ഷെയർ ചോദിക്കുന്നു. ശതമാനം നിങ്ങൾ തന്നെ തീരുമാനിക്കണം; പക്ഷേ അത് റോളും വെസ്റ്റിംഗും ചേർത്ത് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം, പണം വരുന്നതിന് മുമ്പ്. ഈ റീൽ ആ കൂട്ടുകാർക്ക് അയക്കൂ. നിങ്ങളുടെ ഷെയർ എഴുതിയിട്ടുണ്ടോ?',
 cap_en='Three friends built a turf-booking app on trust, with nothing written. The day the first big corporate payment arrives, one asks for half the shares. Nobody can decide the split for you, but whatever you agree must go into a co-founder agreement with roles and vesting, before the money comes in. Is your split written down?',
 cap_mg='Onnum ezhuthaathe thudangiya app startup-inu aadya valiya payment vanna divasam oru co-founder pakuthi share chodikkunnu. Shathamaanam ningal thanne theerumaanikkanam; pakshe athu role-um vesting-um cherthu co-founder agreement-il ezhuthanam, panam varunnathinu mumpu. Ningalude share ezhuthiyittundo?',
 names=('ഡെൽന', 'ആൽബിൻ'))
