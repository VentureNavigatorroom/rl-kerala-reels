# Co-founder agreements batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_CFA. Never decide a split. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

# CRM #20 (investor asks for a data room): no founders' agreement after 3 years
duo("cf020", "tech_nontech", "A", "bank", "ഡാറ്റാ റൂമിൽ\nഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"ഫൗണ്ടർ എഗ്രിമെന്റ് എവിടെ?\"", [
 ("A","wide","മനോജേ, ഇൻവെസ്റ്റർ ഡാറ്റാ റൂമിൽ ഫൗണ്ടർ എഗ്രിമെന്റ് ചോദിച്ചു. മൂന്ന് വർഷമായിട്ടും നമ്മൾ ഒപ്പിട്ടിട്ടില്ല."),
 ("V","V","ശ്രുതീ, നമ്മൾ രണ്ടുപേരും എങ്ങും പോകുന്നില്ലല്ലോ. പിന്നെ അവർക്കെന്തിനാ അത്?"),
 ("A","A","നാളെ ഒരാൾ പോയാൽ ഷെയർ എന്താകും, ആപ്പ് ആരുടേത്? അതാ അവർ നോക്കുന്നത്."),
 ("V","V","അപ്പോ എഗ്രിമെന്റിൽ എന്തൊക്കെ വേണം?"),
 ("A","wide","ഷെയർ വിഭജനം, വെസ്റ്റിംഗ്, റോളുകൾ, എല്ലാ ഐപിയും കമ്പനിക്ക്, പോകുന്നവരുടെ ഷെയർ തിരിച്ചുവാങ്ങൽ."),
 ("V","wide","ഫോൾഡർ ഒഴിഞ്ഞാൽ, ഡീലും ഒഴിയും.")],
 "ഡാറ്റാ റൂമിലെ\nആദ്യ ഫയൽ", CTA_COFOUNDER, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റാ റൂം ചോദിക്കുമ്പോൾ ഫൗണ്ടർ എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ പ്രശ്നമാണ്. ഷെയർ വിഭജനം, വെസ്റ്റിംഗ്, റോളുകൾ, ഐപി കമ്പനിക്ക്, പോകുന്നവരുടെ ഷെയർ തിരിച്ചുവാങ്ങൽ എല്ലാം എഴുതണം. നിങ്ങളുടേത് ഒപ്പിട്ടോ? അതെ / ഇല്ല?",
 cap_en="When an investor opens the data room, a missing founders' agreement stands out. It should cover the equity split, vesting, roles, all IP assigned to the company and buy-back of a leaver's unvested shares. Have you signed yours? Yes or no?",
 cap_mg="Investor data room chodikkumpol founder agreement illenkil prashnamaanu. Share split, vesting, roles, IP company-kku, pokunnavarude share thirichu vaangal ellam ezhuthanam. Ningaludethu ozhippitto? Athe / illa?")

# CRM #26 (Gulf returnee building in Kerala) + remote co-founder: who decides what
duo("cf021", "remote_cofounder", "B", "gulfroom", "\"ഞാൻ അറിയാതെ\nഒരാളെയും എടുക്കരുത്\"\nദുബായിൽ നിന്ന് കോ-ഫൗണ്ടർ", [
 ("A","wide","ഷംസൂ, അടുത്ത മാസം ഞാൻ നാട്ടിലേക്ക്. പ്രൊഡക്റ്റ് ഇനി അവിടെ ഇരുന്ന് ഞാൻ നോക്കും."),
 ("V","V","നസീറേ, ശരി. പക്ഷേ ഞാൻ അറിയാതെ ഒരാളെയും ജോലിക്കെടുക്കരുത്, ഒരു ബില്ലും പാസാക്കരുത്."),
 ("A","A","ഓരോ ചെറിയ കാര്യത്തിനും നിന്റെ ഷിഫ്റ്റ് കഴിയും വരെ ഞാൻ കാത്തിരിക്കണോ?"),
 ("V","V","അപ്പോ ആര് എന്ത് തീരുമാനിക്കും?"),
 ("A","wide","അത് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതാം. ദിവസേനയുള്ളത് എനിക്ക്, വലിയ തീരുമാനങ്ങൾ രണ്ടുപേരും ചേർന്ന്."),
 ("V","wide","റിമോട്ട് ടിവിക്ക് മതി, കമ്പനിക്ക് എഗ്രിമെന്റ്.")],
 "ആര് എന്ത് തീരുമാനിക്കും:\nഎഴുതി വെക്കൂ", CTA_COFOUNDER, theme="crm",
 cap_ml="ഒരു കോ-ഫൗണ്ടർ ഗൾഫിൽ, മറ്റേയാൾ നാട്ടിൽ. ദിവസേനയുള്ള തീരുമാനം ആരുടേത്, വലിയ തീരുമാനങ്ങൾ എങ്ങനെ എന്നത് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതിയാൽ ഓരോ കാര്യത്തിനും കാത്തിരിക്കേണ്ട. നിങ്ങളുടെ കോ-ഫൗണ്ടർ ഏത് നാട്ടിൽ?",
 cap_en="One co-founder in the Gulf, the other running things in Kerala. Write down in the co-founder agreement who makes day-to-day calls and which decisions need both of you, so nobody waits on every small thing. Where is your co-founder?",
 cap_mg="Oru co-founder Gulf-il, mattethu naattil. Daily theerumaanam aarudethu, valiya theerumaanangal engane ennathu co-founder agreement-il ezhuthiyaal ororo kaaryathinum kaathirikkenda. Ningalude co-founder ethu naattil?")

# CRM #2 (business run as a proprietorship) + #3 (trust, nothing written): promised "half" in a juice shop
duo("cf022", "friends_cofounders", "C", "juiceshop", "\"പകുതി നിനക്ക്\"\n3 വർഷം മുമ്പ് പറഞ്ഞു.\nകടയ്ക്ക് ഷെയറേ ഇല്ല", [
 ("A","wide","നൗഷാദേ, ജ്യൂസ് കട കമ്പനി ആക്കുകയാ. നാല് ബ്രാഞ്ച് കൂടി തുടങ്ങാൻ."),
 ("V","V","റസിയാ, 3 വർഷം മുമ്പ് പകുതി എനിക്കെന്ന് പറഞ്ഞതോ? കടലാസിൽ എവിടെയുമില്ലല്ലോ."),
 ("A","A","പ്രൊപ്രൈറ്റർഷിപ്പിൽ ഷെയർ എന്നൊന്നില്ല. ലൈസൻസ് എല്ലാം എന്റെ പേരിലാ."),
 ("V","V","അപ്പോ ഞാൻ വെറും ജോലിക്കാരനോ?"),
 ("A","wide","അല്ല. കമ്പനി വരുമ്പോൾ ഷെയർ എത്ര എന്ന് നമ്മൾ തീരുമാനിച്ച് എഗ്രിമെന്റിൽ എഴുതാം. വെസ്റ്റിംഗും റോളും സഹിതം."),
 ("V","wide","വാക്ക് ജ്യൂസ് പോലെയാ, വേഗം പുളിക്കും.")],
 "പറഞ്ഞ ഷെയർ\nഎഴുതിയാലേ ഷെയർ", CTA_COFOUNDER, theme="crm",
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പിൽ ഷെയർ ഇല്ല, അതുകൊണ്ട് വാക്കാൽ പറഞ്ഞ \"പകുതി\" കമ്പനി ആക്കുമ്പോൾ എഴുതി ഉറപ്പിക്കണം: ഷെയർ വിഭജനം, വെസ്റ്റിംഗ്, റോൾ. ശതമാനം നിങ്ങൾ തീരുമാനിക്കും. വാക്ക് കൊടുത്ത ഷെയർ ഉണ്ടോ?",
 cap_en="A proprietorship has no shares, so a spoken promise of \"half\" must be written down when the business becomes a company: equity split, vesting and roles. You decide the percentage. Ever promised someone a share by word?",
 cap_mg="Proprietorship-il share illa, athukondu vaakkaal paranja \"pakuthi\" company aakkumpol ezhuthi urappikkanam: share split, vesting, role. Percentage ningal theerumaanikkum. Vaakku koduttha share undo?")

# CRM #3 (two friends on trust, nothing written), d904 pattern: dried-fish brand frozen by a fight
duo("cf023", "friends_cofounders", "B", "fishmarket", "ഉണക്കമീൻ ബ്രാൻഡ്.\nരണ്ട് പാർട്ണർ, ഒരു വഴക്ക്.\n6 മാസമായി ഓർഡർ ഇല്ല", [
 ("A","wide","ആന്റണീ, പാക്കിംഗിന്റെ കാര്യത്തിൽ തുടങ്ങിയ വഴക്കാ. 6 മാസമായി ഒരു ഓർഡറും എടുക്കുന്നില്ല."),
 ("V","V","സുമേ, രണ്ടുപേരും കോടതിയിൽ പോകുമെന്നാ പറയുന്നത്. അത് വർഷങ്ങൾ എടുക്കും."),
 ("A","A","തുടങ്ങുമ്പോൾ വിശ്വാസം മാത്രം. തർക്കം വന്നാൽ എന്ത് എന്ന് ഒരു വരി പോലും എഴുതിയില്ല."),
 ("V","V","ഇനി തുടങ്ങുന്നവർ എന്ത് ചെയ്യണം?"),
 ("A","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തർക്കം എങ്ങനെ തീർക്കും എന്ന് ആദ്യമേ എഴുതണം. ആദ്യം എന്ത് ചെയ്യും, ആരെ സമീപിക്കും."),
 ("V","wide","മീൻ ഉണങ്ങിയാൽ ലാഭം, ബന്ധം ഉണങ്ങിയാൽ നഷ്ടം.")],
 "തർക്കം തീർക്കുന്ന വഴി\nആദ്യമേ എഴുതൂ", CTA_COFOUNDER, theme="crm",
 cap_ml="രണ്ട് പാർട്ണർമാരുടെ വഴക്കിൽ ഒരു ബിസിനസ് മാസങ്ങളോളം നിന്നുപോകാം. തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും എന്ന് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തുടക്കത്തിലേ എഴുതൂ, സ്നേഹമുള്ളപ്പോൾ. നിങ്ങളുടേതിൽ ആ വരി ഉണ്ടോ?",
 cap_en="A fight between two partners can freeze a business for months. Write the dispute-resolution route into the co-founder agreement at the start, while you still get along. Does yours have that clause?",
 cap_mg="Randu partner-marude vazhakkil oru business maasangalolam ninnupokaam. Tharkkam vannaal engane theerkkum ennu co-founder agreement-il thudakkathile ezhuthu, snehamullappol. Ningaludethil aa vari undo?")

# FAQ: "we'll write the agreement after funding"
duo("cf024", "tech_nontech", "A", "busstop", "\"ഫണ്ടിംഗ് കിട്ടിയിട്ട്\nഎഗ്രിമെന്റ് എഴുതാം\"\nഅപ്പോഴേക്കും വൈകും", [
 ("A","wide","അഖിലേ, എഗ്രിമെന്റ് ഇപ്പോ എന്തിനാ? ഫണ്ടിംഗ് കിട്ടിയിട്ട് വക്കീലിനെ കാണാം."),
 ("V","V","ജിബിനേ, ഫണ്ടിംഗിന് മുമ്പ് നമ്മളിൽ ഒരാൾ പോയാലോ? ഷെയർ മുഴുവൻ കൂടെ പോകും."),
 ("A","A","അതിന് ആരും പോകുന്നില്ലല്ലോ."),
 ("V","V","ആരും പ്ലാൻ ചെയ്ത് പോകാറില്ല. വെസ്റ്റിംഗും ലീവർ ക്ലോസും ഇപ്പോ എഴുതിയാലേ വെസ്റ്റ് ആകാത്ത ഷെയർ തിരിച്ചുവാങ്ങാൻ പറ്റൂ."),
 ("A","wide","എങ്കിൽ ബസ് വരും മുമ്പ് ടിക്കറ്റ് എടുക്കാം."),
 ("V","wide","കുട മഴയ്ക്ക് മുമ്പ്, കരാർ പണത്തിന് മുമ്പ്.")],
 "എഗ്രിമെന്റ്\nഫണ്ടിംഗിന് മുമ്പ്", CTA_VESTING, theme="faq",
 cap_ml="\"ഫണ്ടിംഗ് കിട്ടിയിട്ട് എഗ്രിമെന്റ്\" എന്നത് സാധാരണ തെറ്റാണ്. അതിന് മുമ്പ് ഒരാൾ പോയാൽ ഷെയർ മുഴുവൻ കൂടെ പോകും. വെസ്റ്റിംഗും ലീവർ ക്ലോസും ആദ്യം എഴുതൂ. നിങ്ങൾ എഴുതിയോ? അതെ / ഇല്ല?",
 cap_en="\"We'll sign the agreement after funding\" is a common mistake: if a co-founder leaves before that, all their shares leave too. Write vesting and the leaver clause in first. Have you? Yes or no?",
 cap_mg="\"Funding kittiyittu agreement\" ennathu saadhaarana thettaanu. Athinu munpu oraal poyaal share muzhuvan koode pokum. Vesting-um leaver clause-um aadyam ezhuthu. Ningal ezhuthiyo? Athe / illa?")

# FAQ: part-time tech co-founder asking for an equal share
duo("cf025", "tech_nontech", "B", "metro", "\"ഞാൻ വീക്കെൻഡിൽ\nകോഡ് ചെയ്യാം.\n50% തരണം\"", [
 ("A","wide","കിരണേ, നീ ഐടി ജോലി വിടില്ല, ആഴ്ചയിൽ രണ്ട് ദിവസം മാത്രം. എന്നിട്ടും 50%?"),
 ("V","V","അഞ്ജലീ, ആപ്പ് മുഴുവൻ ഞാനല്ലേ ഉണ്ടാക്കുന്നത്. അത് ചെറിയ കാര്യമാണോ?"),
 ("A","A","എത്ര ശതമാനം എന്ന് നമ്മൾ രണ്ടുപേരും തീരുമാനിക്കും. പക്ഷേ എത്ര സമയം, എന്ത് ചുമതല എന്നത് എഴുതണം."),
 ("V","V","പിന്നീട് ഞാൻ ഫുൾ ടൈം വന്നാലോ?"),
 ("A","wide","അതും എഗ്രിമെന്റിൽ. ഷെയർ വെസ്റ്റിംഗോടെ, സാധാരണ 4 വർഷം. കോഡ് കമ്പനിയുടെ പേരിൽ."),
 ("V","wide","പാർട്ട് ടൈം ആകാം, എഴുത്ത് ഫുൾ ടൈം വേണം.")],
 "സമയവും ചുമതലയും\nഎഴുതി വെക്കൂ", CTA_COFOUNDER, theme="faq",
 cap_ml="ജോലി വിടാതെ വീക്കെൻഡിൽ മാത്രം വരുന്ന ടെക് കോ-ഫൗണ്ടർ? ശതമാനം നിങ്ങൾ തീരുമാനിക്കും, പക്ഷേ സമയം, ചുമതല, വെസ്റ്റിംഗ്, കോഡ് കമ്പനിക്ക് എന്നത് എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ കോ-ഫൗണ്ടർ ഫുൾ ടൈമോ പാർട്ട് ടൈമോ?",
 cap_en="A tech co-founder who keeps the day job and codes only on weekends? You decide the percentage, but write down the time commitment, the role, vesting and that the code belongs to the company. Is your co-founder full-time or part-time?",
 cap_mg="Joli vidaathe weekend-il maathram varunna tech co-founder? Percentage ningal theerumaanikkum, pakshe samayam, chumathala, vesting, code company-kku ennathu agreement-il ezhuthanam. Ningalude co-founder full time-o part time-o?")

# FAQ: "who owns the page?", d904 pattern: night food-tour brand on a personal account
duo("cf026", "friends_cofounders", "C", "thattukada", "40,000 ഫോളോവേഴ്സ്.\nപേജ് അവന്റെ ഫോണിൽ.\nബ്രാൻഡ് ആരുടേത്?", [
 ("A","wide","ബിജുവേട്ടാ, നമ്മുടെ നൈറ്റ് ഫുഡ് ടൂർ പേജിന് 40,000 ഫോളോവേഴ്സ് ആയി!"),
 ("V","V","സിജോ, അത് നിന്റെ പേഴ്സണൽ അക്കൗണ്ട് അല്ലേ? നാളെ നീ പിണങ്ങിയാൽ പേജും പോകില്ലേ?"),
 ("A","A","ഞാൻ പിണങ്ങാനോ? നമ്മൾ കോ-ഫൗണ്ടേഴ്സ് അല്ലേ."),
 ("V","V","അതുകൊണ്ടാ. എഗ്രിമെന്റിൽ ബ്രാൻഡ്, ലോഗോ, വീഡിയോ എല്ലാം കമ്പനിക്ക് അസൈൻ ചെയ്യണം."),
 ("A","wide","എങ്കിൽ പേജും കമ്പനിയുടെ പേരിലേക്ക് മാറ്റാം."),
 ("V","wide","ദോശ നിന്റെ കല്ലിൽ, ബ്രാൻഡ് കമ്പനിയുടെ പേരിൽ.")],
 "ബ്രാൻഡ് കമ്പനിയുടേത്\nഎന്ന് എഴുതൂ", CTA_COFOUNDER, theme="faq",
 cap_ml="ബ്രാൻഡിന്റെ പേജ് ഒരു കോ-ഫൗണ്ടറുടെ പേഴ്സണൽ അക്കൗണ്ടിലാണോ? ബ്രാൻഡ്, ലോഗോ, വീഡിയോ ഉൾപ്പെടെ എല്ലാ ഐപിയും കമ്പനിക്ക് അസൈൻ ചെയ്യുന്നത് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ പേജ് ആരുടെ പേരിൽ?",
 cap_en="Is your brand's page sitting in one co-founder's personal account? The co-founder agreement should assign all IP to the company, including the brand, logo and videos. Whose name is your page in?",
 cap_mg="Brand-inte page oru co-founder-ude personal account-ilaano? Brand, logo, video ulppede ella IP-um company-kku assign cheyyunnathu co-founder agreement-il ezhuthanam. Ningalude page aarude peril?")

# FAQ: "the idea was mine, so no vesting for me"
chat("cfc002", "friends_cofounders", "A", "\"ഐഡിയ എന്റേതാ.\nഎനിക്ക് വെസ്റ്റിംഗ്\nവേണ്ട\"", ("ദേവിക", "അർജുൻ"), [
 (0,"അർജുൻ, ഐഡിയ എന്റേതാണ്. അതുകൊണ്ട് എന്റെ ഷെയറിന് വെസ്റ്റിംഗ് വേണ്ടല്ലോ?"),
 (1,"ദേവികേ, ഐഡിയയ്ക്ക് കൂടുതൽ ശതമാനം വേണമെങ്കിൽ അത് നമുക്ക് സംസാരിച്ച് തീരുമാനിക്കാം."),
 (0,"പക്ഷേ വെസ്റ്റിംഗ് അർജുന് മാത്രം പോരേ?"),
 (1,"വെസ്റ്റിംഗ് സാധാരണ എല്ലാ ഫൗണ്ടർമാർക്കും: 4 വർഷം, ഒരു വർഷം ക്ലിഫ്. ആര് നേരത്തെ പോയാലും കമ്പനി സുരക്ഷിതം."),
 (0,"ശരി, ഐഡിയ ജീവിക്കേണ്ടത് കമ്പനിയിലാണല്ലോ."),
 (1,"ഐഡിയ ഒരു ദിവസം, കമ്പനി നാല് വർഷം.")],
 "ഐഡിയ കൊണ്ടുവന്നവർക്കും\nവെസ്റ്റിംഗ്", CTA_VESTING, theme="faq",
 cap_ml="ഐഡിയ കൊണ്ടുവന്ന ഫൗണ്ടർക്ക് വെസ്റ്റിംഗ് വേണ്ടേ? സാധാരണ രീതി എല്ലാ ഫൗണ്ടർമാർക്കും വെസ്റ്റിംഗ്: 4 വർഷം, ഒരു വർഷം ക്ലിഫ്. ശതമാനം വേറെ ചർച്ച. നിങ്ങളുടെ ടീമിൽ ഐഡിയ ആരുടേത്?",
 cap_en="Does the founder who brought the idea skip vesting? Common practice is vesting for every founder: 4 years with a 1-year cliff. The percentage is a separate conversation. Whose idea was it in your team?",
 cap_mg="Idea konduvanna founder-kku vesting vende? Saadhaarana reethi ella founder-markkum vesting: 4 varsham, oru varsham cliff. Percentage vere charcha. Ningalude team-il idea aarudethu?")

# NEW, d904 pattern: bridal make-up duo after a 40-wedding season
duo("cf027", "friends_cofounders", "B", "weddinghall", "40 കല്യാണം ഒരു സീസണിൽ.\nഇപ്പോ ചോദ്യം:\n\"ക്ലയന്റ് കൊണ്ടുവന്നത് ആര്?\"", [
 ("A","wide","ശരത്തേ, ഈ സീസണിൽ 40 കല്യാണം. മേക്കപ്പ് ഞാൻ, ബുക്കിംഗ് നീ. ഇനി കമ്പനി ആക്കാം."),
 ("V","V","കാവ്യേ, ക്ലയന്റ്സിൽ പകുതിയും എന്റെ പരിചയം വഴി. ഷെയർ അതനുസരിച്ച് വേണം."),
 ("A","A","ഞാൻ ഇല്ലെങ്കിൽ ഒരു മണവാട്ടിയും ഒരുങ്ങില്ല!"),
 ("V","V","എങ്കിൽ ആര് എത്ര എന്ന് ആര് തീരുമാനിക്കും?"),
 ("A","wide","നമ്മൾ തന്നെ, ഇപ്പോൾ. ശതമാനം, ആരുടെ ചുമതല എന്ത്, പോയാൽ ഷെയർ എന്ത്. എല്ലാം കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ."),
 ("V","wide","മേക്കപ്പ് ഒരു രാത്രി, എഗ്രിമെന്റ് എന്നും.")],
 "സീസൺ തീരും മുമ്പ്\nഷെയർ എഴുതൂ", CTA_COFOUNDER, theme="new",
 cap_ml="തിരക്കുള്ള ഒരു കല്യാണ സീസൺ കഴിയുമ്പോഴാണ് \"ആരാ കൂടുതൽ ചെയ്തത്\" എന്ന തർക്കം. ശതമാനം, ചുമതല, പോയാൽ ഷെയർ എന്ത് എന്നത് നിങ്ങൾ തന്നെ തീരുമാനിച്ച് ആദ്യമേ എഴുതൂ. നിങ്ങളുടെ ബിസിനസ് സീസണലോ?",
 cap_en="After a packed wedding season comes the fight over who did more. Decide the percentage, the roles and what happens to a leaver's shares yourselves, and write it down early. Is your business seasonal?",
 cap_mg="Thirakkulla oru kalyaana season kazhiyumpozhaanu \"aaraa kooduthal cheythathu\" enna tharkkam. Percentage, chumathala, poyaal share enthu ennathu ningal thanne theerumaanichu aadyame ezhuthu. Ningalude business seasonal-o?")

# NEW: a founder's spouse "just helping" for months asks for a share
duo("cf028", "late_joiner", "C", "library", "ആറ് മാസം\n\"വെറുതെ സഹായിച്ചു\".\nഇപ്പോ: \"എന്റെ ഷെയർ?\"", [
 ("A","wide","അനൂപേ, രേഷ്മ ആറ് മാസമായി നമ്മുടെ ആപ്പിന് ചോദ്യങ്ങൾ എഴുതുന്നു. ഇന്നലെ ചോദിച്ചു, ഞാനും കോ-ഫൗണ്ടർ അല്ലേ എന്ന്."),
 ("V","V","ഗ്രീഷ്മേ, അവൾ വെറുതെ സഹായിക്കുന്നതാണെന്നാ ഞാൻ വിചാരിച്ചത്."),
 ("A","A","ആയിരക്കണക്കിന് ചോദ്യങ്ങൾ. അവ ആരുടേത് എന്ന് ഒരു കടലാസ് പോലുമില്ല."),
 ("V","V","ഇനി എന്ത് ചെയ്യും?"),
 ("A","wide","കോ-ഫൗണ്ടർ ആകുന്നെങ്കിൽ ഷെയർ മൂന്നുപേരും ചേർന്ന് തീരുമാനിക്കും, വെസ്റ്റിംഗോടെ. ചോദ്യങ്ങൾ കമ്പനിയുടേത് എന്ന് എഴുതണം."),
 ("V","wide","വെറുതെ സഹായം വെറുതെ തീരില്ല.")],
 "പുതിയ ആൾ വന്നാൽ\nഅന്നേ എഴുതൂ", CTA_COFOUNDER, theme="new",
 cap_ml="\"വെറുതെ സഹായിക്കുന്ന\" ഒരാൾ മാസങ്ങൾ കഴിഞ്ഞ് ഷെയർ ചോദിക്കാം. പുതിയ ആൾ ചേരുന്ന ദിവസം തന്നെ റോൾ, വെസ്റ്റിംഗ്, ഉണ്ടാക്കുന്നത് കമ്പനിക്ക് എന്നിവ എഴുതൂ. നിങ്ങളുടെ ടീമിൽ \"വെറുതെ സഹായിക്കുന്ന\" ആരെങ്കിലും ഉണ്ടോ?",
 cap_en="Someone \"just helping out\" can ask for a share months later. The day a new person joins, write down their role, vesting and that what they create belongs to the company. Is anyone \"just helping\" in your team?",
 cap_mg="\"Veruthe sahaayikkunna\" oraal maasangal kazhinju share chodikkaam. Puthiya aal cherunna divasam thanne role, vesting, undaakkunnathu company-kku enniva ezhuthu. Ningalude team-il \"veruthe sahaayikkunna\" aarenkilum undo?")
