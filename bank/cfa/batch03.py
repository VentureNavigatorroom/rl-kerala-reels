# Co-founder agreements batch 03 (19 Nov evening, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_CFA. Never decide a split. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

duo("cf002", "tech_nontech", "A", "office", "70/30 വാക്കാൽ.\nഇപ്പോ രണ്ടുപേരും\nപറയുന്നു: \"ഞാനാണ് CEO\"", [
 ("A","wide","രാഹുൽ, ഇൻവെസ്റ്റർക്ക് അയച്ച ഡെക്കിൽ നീ CEO എന്ന് എഴുതിയോ? നമ്മുടെ നോട്ടിൽ ഞാനാണ് CEO."),
 ("V","V","നേഹ, 70 എന്റെ കയ്യിലല്ലേ. അപ്പോ ഞാൻ CEO, നീ COO എന്ന് കരുതി."),
 ("A","A","70/30 പറഞ്ഞു, റോൾ ആരും എഴുതിയില്ല."),
 ("V","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ ഷെയർ മാത്രമല്ല, ആര് എന്ത് ചെയ്യും, ആര് തീരുമാനിക്കും എന്നും എഴുതണം."),
 ("A","A","ഇൻവെസ്റ്റർ കാണും മുമ്പ് നമ്മൾ ഒരേ പേജിൽ വരണം."),
 ("V","wide","ബോസ് ആരെന്ന് ബോസിനും അറിയില്ല.")],
 "ഷെയർ മാത്രമല്ല,\nറോളും എഴുതണം", CTA_COFOUNDER, theme="crm",
 cap_ml="70/30 വാക്കാൽ പറഞ്ഞു, പക്ഷേ CEO ആര്, COO ആര് എന്ന് രണ്ടുപേർക്കും രണ്ട് ഉത്തരം. കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ ഷെയറിനൊപ്പം റോളും തീരുമാനങ്ങൾ ആര് എടുക്കും എന്നതും എഴുതണം. നിങ്ങളുടെ ടീമിൽ റോൾ എഴുതിയിട്ടുണ്ടോ?",
 cap_en="A 70/30 split agreed verbally, and now both founders think they are the CEO. A co-founder agreement covers roles and who decides what, not just the equity split. Are your roles written down: yes or no?",
 cap_mg="70/30 vaakkaal paranju, pakshe CEO aaru, COO aaru ennu randuperkkum randu utharam. Co-founder agreement-il share-inoppam role-um theerumaanangal aaru edukkum ennathum ezhuthanam. Ningalude team-il role ezhuthiyittundo?")

duo("cf003", "family_cofounders", "B", "kitchen", "ആങ്ങള \"കോ-ഫൗണ്ടർ\".\nഎഴുതിയിരിക്കുന്നത്\nഫോൺ കോൺടാക്റ്റിൽ മാത്രം", [
 ("A","wide","രാജേഷേ, നിന്റെ ഫോണിൽ എന്റെ പേര് 'ബിന്ദു കോ-ഫൗണ്ടർ' എന്നാ. വേറെ എവിടെയെങ്കിലും എഴുതിയിട്ടുണ്ടോ?"),
 ("V","V","ബിന്ദൂ, ആങ്ങളയും പെങ്ങളുമല്ലേ. ഇതിനൊക്കെ പേപ്പർ എന്തിനാ?"),
 ("A","A","മസാല യൂണിറ്റിൽ ഞാൻ 4 വർഷമായി പണിയെടുക്കുന്നു. എനിക്ക് എത്ര ഷെയർ എന്ന് ആർക്കും അറിയില്ല."),
 ("V","wide","ശരിയാ. കുടുംബമാണെങ്കിലും ഷെയർ, റോൾ, തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും എന്നത് എഴുതണം."),
 ("A","A","അല്ലെങ്കിൽ അടുത്ത തർക്കം ഊണുമേശയിൽ."),
 ("V","wide","കോൺടാക്റ്റ് നെയിം എഗ്രിമെന്റ് അല്ല.")],
 "കോൺടാക്റ്റ് നെയിം\nഎഗ്രിമെന്റ് അല്ല", CTA_COFOUNDER, theme="crm",
 cap_ml="സഹോദരി \"കോ-ഫൗണ്ടർ\" ആണ്, പക്ഷേ അത് എഴുതിയിരിക്കുന്നത് ഫോൺ കോൺടാക്റ്റിൽ മാത്രം. കുടുംബ ബിസിനസിലും ഷെയർ, റോൾ, തർക്കം തീർക്കുന്ന രീതി എഴുതി വെക്കണം. നിങ്ങളുടെ കോ-ഫൗണ്ടർ കുടുംബത്തിലുള്ള ആളാണോ?",
 cap_en="A sister has worked in her brother's spice unit for 4 years as a 'co-founder', but the only place that is written is his phone contacts. Family co-founders need a written agreement too: equity, roles and how disputes are settled. Is your co-founder family: yes or no?",
 cap_mg="Sahodari 'co-founder' aanu, pakshe athu ezhuthiyirikkunnathu phone contact-il maathram. Kudumba business-ilum share, role, tharkkam theerkkunna reethi ezhuthi vekkanam. Ningalude co-founder kudumbathil ulla aalaano?")

duo("cf004", "friends_cofounders", "C", "textile", "പാർട്ണർഷിപ്പ് ഫേം\n12 വർഷം. ഇൻവെസ്റ്റർ:\n\"കമ്പനി ആക്കൂ\"", [
 ("A","wide","പ്രകാശേട്ടാ, ഇൻവെസ്റ്റർ പറഞ്ഞു, നമ്മുടെ സാരി ഫേം കമ്പനി ആക്കണം എന്ന്. പഴയ പാർട്ണർഷിപ്പ് ഡീഡ് പോരേ?"),
 ("V","V","രമ്യേ, ആ ഡീഡ് ഫേമിന് വേണ്ടി എഴുതിയതാ. കമ്പനിയിൽ നമ്മൾ ഷെയർഹോൾഡർമാരാണ്."),
 ("A","A","അപ്പോ പുതിയ എഗ്രിമെന്റ് വേണോ?"),
 ("V","wide","വേണം. ഷെയർ, റോൾ, ആരെങ്കിലും പോയാൽ എന്ത്. അതേ അവകാശങ്ങൾ SHA-യിലും ആർട്ടിക്കിൾസിലും വരണം."),
 ("A","A","കട പഴയത്, പേപ്പർ പുതിയത്."),
 ("V","wide","തറി അതുതന്നെ, നൂല് മാറ്റണം.")],
 "ഫേം കമ്പനിയായാൽ\nപുതിയ എഗ്രിമെന്റ്", CTA_COFOUNDER, theme="crm",
 cap_ml="12 വർഷം പഴയ പാർട്ണർഷിപ്പ് ഫേം ഇൻവെസ്റ്റ്മെന്റിന് വേണ്ടി കമ്പനിയാകുന്നു. പഴയ ഡീഡ് പോരാ: ഷെയർ, റോൾ, ലീവർ ക്ലോസ് ഉള്ള പുതിയ ഫൗണ്ടേഴ്സ് എഗ്രിമെന്റ്, അത് SHA-യിലും ആർട്ടിക്കിൾസിലും. നിങ്ങളുടെ ബിസിനസ് ഇപ്പോൾ ഫേമാണോ?",
 cap_en="A 12-year-old saree partnership firm is converting to a company because an investor asked. The old partnership deed won't carry over: the founders need a fresh agreement on equity, roles and leavers, mirrored in the SHA and the articles. Is your business a firm today: yes or no?",
 cap_mg="12 varsham pazhaya partnership firm investment-inu vendi company aakunnu. Pazhaya deed poraa: share, role, leaver clause ulla puthiya founders agreement, athu SHA-yilum articles-ilum. Ningalude business ippol firm aano?")

duo("cf005", "friends_cofounders", "A", "canteen", "ഒരാൾ പരീക്ഷയ്ക്ക്\nപോയി. തിരിച്ചു വന്നപ്പോൾ\n\"എന്റെ 25% എവിടെ?\"", [
 ("A","wide","അമലേ, നമ്മുടെ ഡ്രോൺ ടീമിൽ നിന്ന് കിരൺ ഒരു വർഷം പരീക്ഷയ്ക്ക് പോയി. ഇപ്പോ 25% ചോദിക്കുന്നു."),
 ("V","V","ആതിരേ, തുടങ്ങിയ ദിവസം 4 പേർക്കും 25% എന്ന് പറഞ്ഞതാ. പേപ്പറൊന്നുമില്ല."),
 ("A","A","ഒരു വർഷം പണി ചെയ്തവർക്കും ചെയ്യാത്തവർക്കും ഒരേ ഷെയർ?"),
 ("V","wide","അതിനാണ് വെസ്റ്റിംഗ്. പണിയെടുക്കുന്നതിനനുസരിച്ച് ഷെയർ കിട്ടും. പോയാൽ വെസ്റ്റ് ആകാത്ത ഷെയർ തിരിച്ചെടുക്കാം."),
 ("A","A","ഇനി എല്ലാർക്കും പുതിയ എഗ്രിമെന്റ്."),
 ("V","wide","അറ്റൻഡൻസ് ഇല്ലാതെ മാർക്ക് ഇല്ല.")],
 "അറ്റൻഡൻസ് ഇല്ലാതെ\nമാർക്ക് ഇല്ല", CTA_VESTING, theme="crm",
 cap_ml="കോളേജ് സ്റ്റാർട്ടപ്പിൽ ഒരാൾ ഒരു വർഷം പരീക്ഷയ്ക്ക് പോയി, തിരിച്ചു വന്ന് മുഴുവൻ ഷെയർ ചോദിക്കുന്നു. വെസ്റ്റിംഗ് ഉണ്ടെങ്കിൽ പണിയെടുക്കുന്നതിനനുസരിച്ച് ഷെയർ, പോയാൽ വെസ്റ്റ് ആകാത്തത് തിരിച്ചെടുക്കാം. നിങ്ങളുടെ ടീമിൽ എത്ര പേർ?",
 cap_en="One member of a college drone team paused for a year of exams and now claims his full 25%. Vesting earns shares over time, and a leaver clause lets the company buy back unvested shares. How many founders are on your team?",
 cap_mg="College startup-il oraal oru varsham pareekshaykku poyi, thirichu vannu muzhuvan share chodikkunnu. Vesting undenkil paniyedukkunnathinanusarichu share, poyaal vest aakaathathu thirichedukkaam. Ningalude team-il ethra per?")

duo("cf006", "friends_cofounders", "B", "cafe", "50/50 ആണ്, ഫെയർ ആണ്.\nപിന്നെ എഗ്രിമെന്റ്\nഎന്തിന്?", [
 ("A","wide","റോഷാ, നമ്മൾ 50/50 അല്ലേ? അത്ര ഫെയർ ആകുമ്പോൾ എഗ്രിമെന്റ് എന്തിനാ?"),
 ("V","V","ആൽവിനേ, കാപ്പിക്കുരു വറുക്കാൻ പുതിയ മെഷീൻ വേണം എന്ന് നീ. വേണ്ട എന്ന് ഞാൻ. ഇനി ആര് തീരുമാനിക്കും?"),
 ("A","A","അത്... രണ്ടുപേരും തുല്യരല്ലേ."),
 ("V","wide","അതാണ് പ്രശ്നം. 50/50-ൽ ആര് തീരുമാനിക്കും, തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും എന്നത് എഴുതണം."),
 ("A","A","തുല്യ ഷെയർ, തുല്യ കുരുക്ക്."),
 ("V","wide","ടൈ ആയാൽ ടൈ ബ്രേക്കർ ആര്?")],
 "50/50 ആയാൽ\nടൈ ബ്രേക്കർ ആര്?", CTA_COFOUNDER, theme="faq",
 cap_ml="50/50 ഷെയർ ഫെയർ ആണ്, പക്ഷേ രണ്ടുപേരും വിയോജിച്ചാൽ ആര് തീരുമാനിക്കും? കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തീരുമാനങ്ങൾ എടുക്കുന്ന രീതിയും തർക്കം തീർക്കുന്ന വഴിയും എഴുതണം. നിങ്ങളുടെ ടീം 50/50 ആണോ?",
 cap_en="Two coffee roasters split 50/50, so they skipped the agreement. Then they disagree on a new machine and nobody can decide. Equal shares still need written rules on decisions and dispute resolution. Is your team 50/50: yes or no?",
 cap_mg="50/50 share fair aanu, pakshe randuperum viyojichaal aaru theerumaanikkum? Co-founder agreement-il theerumaanangal edukkunna reethiyum tharkkam theerkkunna vazhiyum ezhuthanam. Ningalude team 50/50 aano?")

duo("cf007", "late_joiner", "C", "gym", "10 മാസം കഴിഞ്ഞ്\nകോ-ഫൗണ്ടർ പോയി.\n\"എന്റെ ഷെയർ?\"", [
 ("A","wide","ജസ്റ്റിൻ, ഫിറ്റ്നസ് ആപ്പിൽ നിന്ന് വരുൺ 10 മാസം കഴിഞ്ഞ് പോയി. 20% ചോദിക്കുന്നു."),
 ("V","V","റിയാ, എഗ്രിമെന്റിൽ എന്താ എഴുതിയിരിക്കുന്നത്?"),
 ("A","A","4 വർഷം വെസ്റ്റിംഗ്, 1 വർഷം ക്ലിഫ്. അതിന്റെ അർത്ഥം എനിക്ക് മുഴുവൻ മനസ്സിലായില്ല."),
 ("V","wide","ക്ലിഫ് എന്നാൽ ആദ്യ ഒരു വർഷം തികയും മുമ്പ് പോയാൽ ഒരു ഷെയറും വെസ്റ്റ് ആകില്ല."),
 ("A","A","10 മാസം. ക്ലിഫിന് 2 മാസം മുമ്പ്."),
 ("V","wide","ക്ലിഫിന് മുമ്പ് ചാടിയാൽ കയ്യിൽ ഒന്നുമില്ല.")],
 "ക്ലിഫിന് മുമ്പ് പോയാൽ\nഷെയർ ഇല്ല", CTA_VESTING, theme="faq",
 cap_ml="വെസ്റ്റിംഗിലെ ക്ലിഫ് എന്താണ്? സാധാരണ രീതി 4 വർഷം വെസ്റ്റിംഗ്, 1 വർഷം ക്ലിഫ്: ഒരു വർഷം തികയും മുമ്പ് പോയാൽ ഷെയർ വെസ്റ്റ് ആകില്ല. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ക്ലിഫ് ഉണ്ടോ?",
 cap_en="A co-founder of a fitness app leaves after 10 months and asks for his 20%. With the common 4-year vesting and 1-year cliff, nothing vests if you leave before the first year is up. Does your agreement have a cliff: yes or no?",
 cap_mg="Vesting-ile cliff enthaanu? Saadhaarana reethi 4 varsham vesting, 1 varsham cliff: oru varsham thikayum mumbu poyaal share vest aakilla. Ningalude agreement-il cliff undo?")

duo("cf008", "tech_nontech", "A", "garage", "കോ-ഫൗണ്ടർ പോയി.\nകൂടെ 3 മെക്കാനിക്കുകളും", [
 ("A","wide","ജിതിനേ, EV സർവീസ് സെന്റർ വിട്ട് പോയ ഷിബിൻ നമ്മുടെ 3 മെക്കാനിക്കുകളെയും കൊണ്ടുപോയി."),
 ("V","V","ഐശ്വര്യേ, അവൻ സ്വന്തം ഗ്യാരേജ് തുടങ്ങുന്നത് തടയാൻ പറ്റുമോ?"),
 ("A","A","അത് തടയാൻ എളുപ്പമല്ല. പോയ ശേഷമുള്ള നോൺ-കോംപീറ്റ് ഇന്ത്യയിൽ സാധാരണ നടക്കില്ല."),
 ("V","wide","പക്ഷേ നമ്മുടെ ആളുകളെ വിളിച്ചുകൊണ്ടുപോകരുത് എന്ന നോൺ-സോളിസിറ്റും രഹസ്യം സൂക്ഷിക്കാനുള്ള ക്ലോസും നടപ്പാക്കാം."),
 ("A","A","നമ്മുടെ എഗ്രിമെന്റിൽ അത് ഉണ്ടായിരുന്നില്ല."),
 ("V","wide","ഗ്യാരേജ് തടയാൻ പറ്റില്ല, ടീമിനെ കാക്കാം.")],
 "ഗ്യാരേജ് തടയാൻ പറ്റില്ല,\nടീമിനെ കാക്കാം", CTA_COFOUNDER, theme="new",
 cap_ml="കോ-ഫൗണ്ടർ പോയപ്പോൾ ടീമിനെയും കൊണ്ടുപോയി. ഇന്ത്യയിൽ പോയ ശേഷമുള്ള നോൺ-കോംപീറ്റ് സാധാരണ നടപ്പാകില്ല, പക്ഷേ നോൺ-സോളിസിറ്റും കോൺഫിഡൻഷ്യാലിറ്റി ക്ലോസും നടപ്പാക്കാം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ഇതുണ്ടോ?",
 cap_en="A co-founder leaves an EV service centre and takes three mechanics with him. A post-exit non-compete is generally not enforceable in India, but non-solicit and confidentiality clauses can be. Does your co-founder agreement have them: yes or no?",
 cap_mg="Co-founder poyappol team-ineyum kondupoyi. India-yil poya shesham ulla non-compete saadhaarana nadappaakilla, pakshe non-solicit-um confidentiality clause-um nadappaakkaam. Ningalude agreement-il ithundo?")

duo("cf009", "friends_cofounders", "B", "foodcourt", "ഷെഫ് കോ-ഫൗണ്ടർ\nപോയി. പോകുമ്പോൾ\n\"റെസിപ്പി എന്റേതാ\"", [
 ("A","wide","ഡെന്നിസേ, നമ്മുടെ ക്ലൗഡ് കിച്ചന്റെ ഹിറ്റ് ബീഫ് റോസ്റ്റ് റെസിപ്പി അവൻ പുതിയ ഹോട്ടലിൽ വിൽക്കുന്നു."),
 ("V","V","മരിയാ, അവൻ പറയുന്നത് റെസിപ്പി അവന്റെ അമ്മയുടേതാണെന്ന്."),
 ("A","A","പക്ഷേ മെനു, ബ്രാൻഡ്, ടെസ്റ്റ് ചെയ്തത് എല്ലാം കമ്പനിയുടെ പണം കൊണ്ടാ."),
 ("V","wide","അതിനാണ് എഗ്രിമെന്റിൽ IP ക്ലോസ്. കമ്പനിക്ക് വേണ്ടി ഉണ്ടാക്കുന്നതെല്ലാം കമ്പനിയുടേത്, ആദ്യ ദിവസം മുതൽ."),
 ("A","A","നമ്മൾ എഴുതിയിരുന്നെങ്കിൽ..."),
 ("V","wide","റെസിപ്പി അടുക്കളയിൽ, ഉടമസ്ഥത എഗ്രിമെന്റിൽ.")],
 "റെസിപ്പി അടുക്കളയിൽ,\nഉടമസ്ഥത എഗ്രിമെന്റിൽ", CTA_COFOUNDER, theme="new",
 cap_ml="ഷെഫ് കോ-ഫൗണ്ടർ പോയപ്പോൾ ഹിറ്റ് റെസിപ്പിയും കൊണ്ടുപോയി. കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ കമ്പനിക്ക് വേണ്ടി ഉണ്ടാക്കുന്ന എല്ലാ IP-യും (റെസിപ്പി, ബ്രാൻഡ്, ഡിസൈൻ) കമ്പനിയുടേതാണെന്ന് എഴുതണം. നിങ്ങളുടെ ബിസിനസിന്റെ രഹസ്യം എന്താണ്?",
 cap_en="A chef co-founder leaves a cloud kitchen and starts selling its best-selling recipe elsewhere. A co-founder agreement should assign everything created for the business (recipes, brand, designs) to the company from day one. What is your business's secret ingredient?",
 cap_mg="Chef co-founder poyappol hit recipe-um kondupoyi. Co-founder agreement-il company-kku vendi undaakkunna ellaa IP-yum (recipe, brand, design) company-yudethaanennu ezhuthanam. Ningalude business-nte rahasyam enthaanu?")

chat("cfc001", "remote_cofounder", "C", "കാനഡയിലെ കോ-ഫൗണ്ടർ\n3 മാസമായി മിണ്ടുന്നില്ല.\nഷെയർ 40%", ("ഹന്ന", "ഫഹദ്"), [
 (0,"ഫഹദ്, കാനഡയിലുള്ള ബിബിൻ 3 മാസമായി കോളും മെയിലും എടുക്കുന്നില്ല. അവന്റെ കയ്യിൽ 40%."),
 (1,"ഹന്നാ, എഗ്രിമെന്റിൽ ലീവർ ക്ലോസ് ഉണ്ടോ?"),
 (0,"എഗ്രിമെന്റ് ഉണ്ട്, വെസ്റ്റിംഗും ഉണ്ട്. ഒന്നര വർഷമേ ആയുള്ളൂ."),
 (1,"അപ്പോ വെസ്റ്റ് ആകാത്ത ഷെയർ ലീവർ ക്ലോസ് വഴി കമ്പനിക്ക് തിരിച്ചു വാങ്ങാം."),
 (0,"ഭാഗ്യം, അന്ന് എഴുതി വെച്ചത്."),
 (1,"ടൈം സോൺ മാറാം, ക്ലോസ് മാറില്ല.")],
 "വെസ്റ്റ് ആകാത്ത ഷെയർ\nതിരിച്ചു വാങ്ങാം", CTA_VESTING, theme="faq",
 cap_ml="വിദേശത്തുള്ള കോ-ഫൗണ്ടർ മാസങ്ങളായി മിണ്ടുന്നില്ല, പക്ഷേ ഷെയർ കയ്യിലുണ്ട്. വെസ്റ്റിംഗും ലീവർ ക്ലോസും ഉണ്ടെങ്കിൽ വെസ്റ്റ് ആകാത്ത ഷെയർ കമ്പനിക്ക് തിരിച്ചു വാങ്ങാം. നിങ്ങളുടെ കോ-ഫൗണ്ടർ ഏത് നാട്ടിലാണ്?",
 cap_en="A co-founder in Canada has gone silent for 3 months while holding 40%. With vesting and a leaver clause in the co-founder agreement, the company can buy back the unvested shares. Where is your co-founder based?",
 cap_mg="Videshathulla co-founder maasangalaayi mindunnilla, pakshe share kayyilundu. Vesting-um leaver clause-um undenkil vest aakaatha share company-kku thirichu vaangaam. Ningalude co-founder ethu naattilaanu?")

lst("cfl002", "friends_cofounders", "A", "കോ-ഫൗണ്ടർ പോകുമ്പോൾ\nഎഗ്രിമെന്റ് ഉത്തരം\nതരേണ്ട 3 ചോദ്യം", [
 ("ഷെയർ എത്ര കൊണ്ടുപോകും?", "വെസ്റ്റ് ആയത് മാത്രം. ബാക്കി കമ്പനിക്ക് തിരിച്ചു വാങ്ങാം."),
 ("കോഡും ബ്രാൻഡും ആരുടേത്?", "കമ്പനിക്ക് വേണ്ടി ഉണ്ടാക്കിയതെല്ലാം കമ്പനിയുടേത്."),
 ("ടീമിനെ കൊണ്ടുപോകുമോ?", "നോൺ-സോളിസിറ്റും രഹസ്യം സൂക്ഷിക്കാനുള്ള ക്ലോസും നടപ്പാക്കാം.")],
 "നിങ്ങളുടെ എഗ്രിമെന്റ്\nഎത്രയ്ക്ക് ഉത്തരം തരും?", CTA_COFOUNDER, theme="faq",
 cap_ml="കോ-ഫൗണ്ടർ പോകുമ്പോൾ 3 ചോദ്യം: എത്ര ഷെയർ കൊണ്ടുപോകും (വെസ്റ്റ് ആയത് മാത്രം), കോഡും ബ്രാൻഡും ആരുടേത് (കമ്പനിയുടേത്), ടീമിനെ കൊണ്ടുപോകുമോ (നോൺ-സോളിസിറ്റ്). നിങ്ങളുടെ എഗ്രിമെന്റ് എത്രയ്ക്ക് ഉത്തരം തരും: 0, 1, 2, 3?",
 cap_en="When a co-founder leaves, your agreement should answer three questions: how many shares go with them (only vested ones; the company can buy back the rest), who owns the code and brand (the company), and can they take the team (non-solicit and confidentiality). How many does yours answer: 0, 1, 2 or 3?",
 cap_mg="Co-founder pokumpol 3 chodyam: ethra share kondupokum (vest aayathu maathram), code-um brand-um aarudethu (company-yudethu), team-ine kondupokumo (non-solicit). Ningalude agreement ethrakku utharam tharum: 0, 1, 2, 3?")
