# Co-founder agreements batch 06 (20 Nov night, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_CFA. Never decide a split. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

# CRM #16 twist (roles never written, mislabelled): both founders signed a bank form as MD
duo("cf029", "friends_cofounders", "A", "hotellobby", "ബാങ്ക് ഫോമിൽ\nരണ്ടുപേരും ഒപ്പിട്ടു:\n\"MD\"", [
 ("A","wide","ജെയ്സണേ, ബാങ്കിൽ നിന്ന് വിളിച്ചു. ലോൺ ഫോമിൽ നമ്മൾ രണ്ടുപേരും MD എന്നാ എഴുതിയത്."),
 ("V","V","നീതൂ, കയാക്ക് ടൂറുകൾ മുഴുവൻ നടത്തുന്നത് ഞാനല്ലേ. അപ്പോ MD ഞാൻ തന്നെ."),
 ("A","A","ബുക്കിംഗും കണക്കും ഞാനാ നോക്കുന്നത്. ആര് എന്ത് തീരുമാനിക്കും എന്ന് നമ്മൾ എവിടെയും എഴുതിയില്ല."),
 ("V","V","അപ്പോ ഇത് എവിടെയാ എഴുതേണ്ടത്?"),
 ("A","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ: ഓരോരുത്തരുടെ റോൾ, ആര് എന്ത് തീരുമാനിക്കും. അതേ അവകാശങ്ങൾ SHA-യിലും ആർട്ടിക്കിൾസിലും."),
 ("V","wide","കായലിൽ രണ്ട് തുഴ ശരി. കമ്പനിയിൽ രണ്ട് ദിശ വേണ്ട.")],
 "രണ്ട് തുഴ ശരി,\nരണ്ട് ദിശ വേണ്ട", CTA_COFOUNDER, theme="crm",
 cap_ml="കായൽ കയാക്ക് ടൂർ കമ്പനിയുടെ രണ്ട് ഫൗണ്ടർമാരും ബാങ്ക് ഫോമിൽ MD എന്ന് എഴുതി, കാരണം റോൾ എവിടെയും എഴുതിയിരുന്നില്ല. കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ റോളും ആര് എന്ത് തീരുമാനിക്കും എന്നതും എഴുതണം, അതേ അവകാശങ്ങൾ SHA-യിലും ആർട്ടിക്കിൾസിലും. നിങ്ങളുടെ കമ്പനിയിൽ MD ആര്?",
 cap_en="Both founders of a backwater kayak-tour company signed a bank form as MD, because their roles were never written down. A co-founder agreement sets each founder's role and who decides what, and the same rights go into the SHA and the articles. Who is the MD in your company?",
 cap_mg="Kaayal kayak tour company-yude randu founders-um bank form-il MD ennu ezhuthi, kaaranam role evideyum ezhuthiyirunnilla. Co-founder agreement-il role-um aaru enthu theerumaanikkum ennathum ezhuthanam, athe avakaashangal SHA-yilum articles-ilum. Ningalude company-il MD aaru?")

# CRM #18 twist (co-founder only in name): "co-founder" on the website for 3 years, zero shares
duo("cf030", "late_joiner", "B", "shop", "3 വർഷം വെബ്സൈറ്റിൽ\n\"കോ-ഫൗണ്ടർ\".\nഷെയർ: പൂജ്യം", [
 ("A","wide","സുരേഷേ, ഇൻവെസ്റ്റർ മീറ്റിംഗിന് മുമ്പ് ഒരു ചോദ്യം. വെബ്സൈറ്റിൽ മൂന്ന് വർഷമായി ഞാൻ കോ-ഫൗണ്ടറാ. എന്റെ ഷെയർ എവിടെ?"),
 ("V","V","ബിനൂ, ഉത്സവ ലൈറ്റ് ബുക്കിംഗ് മുഴുവൻ നീയാ നോക്കിയത്, സത്യം. പക്ഷേ ഷെയർ മുഴുവൻ എന്റെ പേരിലാ."),
 ("A","A","അപ്പോ ആ കോ-ഫൗണ്ടർ എന്നത് വെറും ഒരു വാക്കാണോ?"),
 ("V","wide","ശതമാനം നമ്മൾ രണ്ടുപേരും ചേർന്ന് തീരുമാനിക്കണം. എന്നിട്ട് അത്, വെസ്റ്റിംഗും റോളും സഹിതം, എഗ്രിമെന്റിൽ എഴുതണം."),
 ("A","A","അപ്പോ ഇൻവെസ്റ്റർ വരും മുമ്പ് ഇത് ഒപ്പിടണം."),
 ("V","wide","പദവി വെബ്സൈറ്റിൽ മതി. ഷെയർ എഗ്രിമെന്റിൽ വേണം.")],
 "പദവി വെബ്സൈറ്റിൽ,\nഷെയർ എഗ്രിമെന്റിൽ", CTA_COFOUNDER, theme="crm",
 cap_ml="ഉത്സവ ലൈറ്റ് റെന്റൽ ബിസിനസിന്റെ വെബ്സൈറ്റിൽ മൂന്ന് വർഷമായി കോ-ഫൗണ്ടർ, പക്ഷേ ഒരു ഷെയറും ഇല്ല. ശതമാനം ഫൗണ്ടർമാർ തന്നെ തീരുമാനിക്കണം; അത് വെസ്റ്റിംഗും റോളും സഹിതം കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ പദവി എവിടെ എഴുതിയിട്ടുണ്ട്?",
 cap_en="Called a co-founder on the website of a festival-lights rental business for 3 years, but holding zero shares. Only the founders can decide the percentage, and it belongs in a written co-founder agreement with vesting and roles. Where is your co-founder title written down?",
 cap_mg="Ulsava light rental business-nte website-il moonnu varshamaayi co-founder, pakshe oru share-um illa. Shathamaanam founders thanne theerumaanikkanam; athu vesting-um role-um sahitham co-founder agreement-il ezhuthanam. Ningalude padavi evide ezhuthiyittundu?")

# CRM #20 twist (one team member stops showing up): equal shares already issued at incorporation
duo("cf031", "friends_cofounders", "C", "teashop", "മൂന്ന് പേർക്കും 33%.\nഒരാൾ 8 മാസമായി\nവരുന്നേയില്ല", [
 ("A","wide","വിഷ്ണൂ, ലോൺഡ്രി ആപ്പ് കമ്പനി തുടങ്ങിയപ്പോൾ മൂന്ന് പേർക്കും തുല്യ ഷെയർ. മൂന്നാമൻ എട്ട് മാസമായി വരുന്നേയില്ല."),
 ("V","V","അനൂ, ഷെയർ അന്നേ കൊടുത്തുപോയി. കമ്പനി തുടങ്ങിയ ശേഷം ഇനി ഒന്നും ചെയ്യാനില്ല."),
 ("A","A","അങ്ങനെയല്ല. കമ്പനി തുടങ്ങിയ ശേഷവും വഴിയുണ്ട്."),
 ("V","V","എന്ത് വഴി?"),
 ("A","wide","എഗ്രിമെന്റിൽ വെസ്റ്റിംഗും അൺവെസ്റ്റഡ് ഷെയർ തിരിച്ചുവാങ്ങലും എഴുതാം. SHA-യിലും ആർട്ടിക്കിൾസിലും അതേ വേണം."),
 ("V","wide","ഷെയർ ഇന്നലെ കൊടുത്തു. നിബന്ധന ഇന്ന് എഴുതാം.")],
 "ഷെയർ ഇന്നലെ,\nനിബന്ധന ഇന്ന്", CTA_VESTING, theme="crm",
 cap_ml="കോളേജ് ലോൺഡ്രി ആപ്പ് കമ്പനിയിൽ മൂന്ന് പേർക്കും തുല്യ ഷെയർ, ഒരാൾ എട്ട് മാസമായി വരുന്നില്ല. കമ്പനി തുടങ്ങിയ ശേഷവും വെസ്റ്റിംഗും അൺവെസ്റ്റഡ് ഷെയർ തിരിച്ചുവാങ്ങലും എഗ്രിമെന്റിൽ എഴുതാം, SHA-യിലും ആർട്ടിക്കിൾസിലും അതേ വേണം. നിങ്ങളുടെ ടീമിൽ വെസ്റ്റിംഗ് ഉണ്ടോ?",
 cap_en="Three college friends got equal shares when the laundry-app company was registered, and one has not shown up for 8 months. Even after incorporation you can sign an agreement with vesting and buy-back of unvested shares, mirrored in the SHA and articles. Does your team have vesting?",
 cap_mg="College laundry app company-il moonnu perkkum thulya share, oraal ettu maasamaayi varunnilla. Company thudangiya sheshavum vesting-um unvested share thirichuvaangalum agreement-il ezhuthaam, SHA-yilum articles-ilum athe venam. Ningalude team-il vesting undo?")

# CRM #17 twist (majority founder bringing in a partner): who owns the boutique's designs
duo("cf032", "late_joiner", "A", "tailor", "പുതിയ പാർട്ണർ\nവരുന്നു. എന്റെ 200\nഡിസൈൻ ആരുടേത്?", [
 ("A","wide","മോഹനേട്ടാ, ബുട്ടീക്കിൽ നിങ്ങളെ കോ-ഫൗണ്ടറാക്കാൻ തീരുമാനിച്ചു. പക്ഷേ എനിക്ക് ഒരു പേടിയുണ്ട്."),
 ("V","V","ഉഷേ, എന്തിനാ പേടി? ഞാൻ വെട്ടുന്ന പാറ്റേണുകൾ നമ്മുടെ ബ്രൈഡൽ ലൈനിന് വേണ്ടിയല്ലേ."),
 ("A","A","നാളെ നിങ്ങൾ പോയാൽ ആ പാറ്റേണുകളും എന്റെ ഡിസൈനുകളും കൂടെ പോകുമോ?"),
 ("V","wide","അതിനാ കോ-ഫൗണ്ടർ എഗ്രിമെന്റ്. ബിസിനസിന് വേണ്ടി നമ്മൾ ഉണ്ടാക്കുന്ന എല്ലാ ഐപിയും കമ്പനിക്ക്."),
 ("A","A","ശരി. എന്റെ പഴയ ഡിസൈൻ ഫയലുകളും കമ്പനിയുടെ പേരിലേക്ക്."),
 ("V","wide","ഷെയർ നമ്മൾ തീരുമാനിക്കും. ഡിസൈൻ ആരുടേത് എന്ന് പേപ്പർ തീരുമാനിക്കും.")],
 "ഷെയർ നമ്മൾ,\nഡിസൈൻ പേപ്പർ", CTA_COFOUNDER, theme="crm",
 cap_ml="ബ്രൈഡൽ ബുട്ടീക്ക് ഉടമ ഒരു പാറ്റേൺ മാസ്റ്ററെ കോ-ഫൗണ്ടറാക്കുന്നു, പേടി ഡിസൈനുകൾ ആരുടേത് എന്നതിൽ. ബിസിനസിന് വേണ്ടി ഉണ്ടാക്കുന്ന എല്ലാ ഐപിയും, ഡിസൈനും പാറ്റേണും, കമ്പനിക്ക് എന്ന് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ ഡിസൈനുകൾ ആരുടെ പേരിലാ?",
 cap_en="A bridal boutique owner is making her pattern master a co-founder, and worries about who will own the designs. The co-founder agreement should assign all IP created for the business, designs and patterns included, to the company. Whose name are your designs in?",
 cap_mg="Bridal boutique udama oru pattern master-e co-founder aakkunnu, pedi design-ukal aarudethu ennathil. Business-nu vendi undaakkunna ella IP-yum, design-um pattern-um, company-kku ennu co-founder agreement-il ezhuthanam. Ningalude design-ukal aarude peril aa?")

# FAQ: "the law says vesting must be 4 years"
duo("cf033", "tech_nontech", "B", "pharmacy", "\"വെസ്റ്റിംഗ് 4 വർഷം\nവേണമെന്ന് നിയമം\nഉണ്ടല്ലോ\" ശരിയോ?", [
 ("A","wide","പ്രവീൺ, കൂൺ കിറ്റ് കമ്പനിയിൽ കോ-ഫൗണ്ടറാകാൻ നീ എന്താ മടിക്കുന്നത്?"),
 ("V","V","സിനീ, ഞാൻ രണ്ട് വർഷമേ ഫുൾടൈം ഉണ്ടാകൂ. വെസ്റ്റിംഗ് 4 വർഷം വേണമെന്ന് നിയമമില്ലേ?"),
 ("A","A","നാല് വർഷം, ഒരു വർഷ ക്ലിഫ്. അത് ഒരു സാധാരണ രീതിയാണ്, നിയമമല്ല."),
 ("V","V","അപ്പോ നമ്മുടെ സ്ഥിതിക്ക് പറ്റിയത് എഴുതാമോ?"),
 ("A","wide","എഴുതാം. ഫുൾടൈം എത്ര കാലം, റോൾ എന്ത്, പോയാൽ അൺവെസ്റ്റഡ് ഷെയർ കമ്പനി തിരിച്ചുവാങ്ങും: എല്ലാം എഗ്രിമെന്റിൽ."),
 ("V","wide","പതിവ് കോപ്പി ചെയ്യണ്ട. നമ്മുടേത് എഴുതാം.")],
 "പതിവ് കോപ്പി ചെയ്യണ്ട,\nനിങ്ങളുടേത് എഴുതൂ", CTA_VESTING, theme="faq",
 cap_ml="വെസ്റ്റിംഗ് 4 വർഷം വേണമെന്ന് നിയമമുണ്ടോ? ഇല്ല. 4 വർഷം, ഒരു വർഷ ക്ലിഫ് എന്നത് സാധാരണ രീതി മാത്രം. ടീമിന് പറ്റിയ കാലാവധി, റോൾ, അൺവെസ്റ്റഡ് ഷെയർ തിരിച്ചുവാങ്ങൽ എഗ്രിമെന്റിൽ എഴുതാം. നിങ്ങളുടെ വെസ്റ്റിംഗ് എത്ര വർഷം?",
 cap_en="Does the law say founder vesting must be 4 years? No. Four years with a 1-year cliff is a common practice, not a rule. Write the period, roles and buy-back of unvested shares that fit your team into the co-founder agreement. How many years is your vesting?",
 cap_mg="Vesting 4 varsham venamennu niyamam undo? Illa. 4 varsham, oru varsha cliff ennathu saadhaarana reethi maathram. Team-nu pattiya kaalaavadhi, role, unvested share thirichuvaangal agreement-il ezhuthaam. Ningalude vesting ethra varsham?")

# FAQ: "if I leave, the company takes all my shares"
duo("cf034", "family_cofounders", "C", "autostand", "\"പോയാൽ ഷെയർ\nമുഴുവൻ പോകും\"\nഅനിയൻ പേടിച്ചു", [
 ("A","wide","ഷാജീ, ഇലക്ട്രിക് ഓട്ടോ ഫ്ലീറ്റ് കമ്പനിയുടെ എഗ്രിമെന്റ് റെഡി. നീ ഒപ്പിട്ടാൽ മതി."),
 ("V","V","സജിച്ചേട്ടാ, കേട്ടത് ഇങ്ങനെയാ: ഇത് ഒപ്പിട്ടാൽ എപ്പോ പോയാലും ഷെയർ മുഴുവൻ കമ്പനി എടുക്കും."),
 ("A","A","അങ്ങനെയല്ല. ഷെയർ കാലം കൊണ്ടാ സ്വന്തമാകുന്നത്. അതാ വെസ്റ്റിംഗ്."),
 ("V","V","അപ്പോ മൂന്ന് വർഷം കഴിഞ്ഞ് ഞാൻ പോയാലോ?"),
 ("A","wide","അതുവരെ വെസ്റ്റ് ചെയ്തത് നിനക്ക്. ബാക്കി അൺവെസ്റ്റഡ് ഷെയർ മാത്രം കമ്പനി തിരിച്ചുവാങ്ങും, എഗ്രിമെന്റ് പറയുന്ന പോലെ."),
 ("V","wide","ഓടിയ ദൂരം എനിക്ക്. ബാക്കി വഴി കമ്പനിക്ക്.")],
 "ഓടിയ ദൂരം നിനക്ക്,\nബാക്കി കമ്പനിക്ക്", CTA_VESTING, theme="faq",
 cap_ml="വെസ്റ്റിംഗ് ഉള്ള എഗ്രിമെന്റ് ഒപ്പിട്ടാൽ, പോകുമ്പോൾ ഷെയർ മുഴുവൻ പോകുമോ? ഇല്ല. അതുവരെ വെസ്റ്റ് ചെയ്ത ഷെയർ നിങ്ങളുടേത്; അൺവെസ്റ്റഡ് ഭാഗം മാത്രം, എഗ്രിമെന്റിലെ ലീവർ ക്ലോസ് പ്രകാരം, കമ്പനി തിരിച്ചുവാങ്ങും. നിങ്ങൾ ഇത് അറിഞ്ഞിരുന്നോ?",
 cap_en="Two brothers running an electric-auto fleet: does signing a vesting agreement mean losing all your shares when you leave? No. Shares vested so far stay yours; only the unvested part can be bought back by the company, as the leaver clause says. Did you know this?",
 cap_mg="Vesting ulla agreement oppittaal, pokumpol share muzhuvan pokumo? Illa. Athuvare vest cheytha share ningaludethu; unvested bhaagam maathram, agreement-ile leaver clause prakaaram, company thirichuvaangum. Ningal ithu arinjirunno?")

# FAQ: "we are the majority, we can throw him out and take his shares"
duo("cf035", "friends_cofounders", "A", "bakery", "\"അവനെ പുറത്താക്കി\nഷെയർ എടുക്കാം\"\nഅത്ര എളുപ്പമോ?", [
 ("A","wide","സാബൂ, മില്ലറ്റ് കുക്കി കമ്പനിയിൽ മൂന്നാമത്തെ പാർട്ണർ ഒരു ഓർഡറും നോക്കുന്നില്ല. നമ്മൾ രണ്ടുപേർ ചേർന്ന് പുറത്താക്കാം."),
 ("V","V","ജിഷേ, പുറത്താക്കിയാൽ അവന്റെ ഷെയർ നമുക്ക് തിരിച്ചു കിട്ടുമോ?"),
 ("A","A","നമ്മൾ രണ്ടുപേരും ഭൂരിപക്ഷമല്ലേ. അത് മതിയാകില്ലേ?"),
 ("V","wide","എഗ്രിമെന്റിൽ വെസ്റ്റിംഗും അൺവെസ്റ്റഡ് ഷെയർ തിരിച്ചുവാങ്ങലും ഇല്ലെങ്കിൽ, അവൻ പോയാലും ഷെയർ അവന്റെ പേരിൽ തന്നെ."),
 ("A","A","അപ്പോ തുടക്കത്തിൽ വേണ്ടിയിരുന്നത് വഴക്കല്ല, എഗ്രിമെന്റ്."),
 ("V","wide","ഷെയർ തിരിച്ചെടുക്കാൻ ഭൂരിപക്ഷം പോരാ. എഴുതിയ കരാർ വേണം.")],
 "ഭൂരിപക്ഷം പോരാ,\nഎഴുതിയ കരാർ വേണം", CTA_COFOUNDER, theme="faq",
 cap_ml="ഒന്നും ചെയ്യാത്ത കോ-ഫൗണ്ടറെ ബാക്കി രണ്ടുപേർ ചേർന്ന് ഒഴിവാക്കിയാൽ ഷെയർ തിരിച്ചു കിട്ടുമോ? വെസ്റ്റിംഗും അൺവെസ്റ്റഡ് ഷെയർ തിരിച്ചുവാങ്ങലും എഗ്രിമെന്റിൽ ഇല്ലെങ്കിൽ, ഷെയർ അയാളുടെ പേരിൽ തന്നെ ഇരിക്കും. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ലീവർ ക്ലോസ് ഉണ്ടോ?",
 cap_en="Two of three millet-cookie founders want to push out the partner who does nothing. Can the majority take his shares back? Without vesting and a buy-back clause for unvested shares in the agreement, his shares stay in his name. Does your agreement have a leaver clause?",
 cap_mg="Onnum cheyyaattha co-founder-e baakki randuper chernnu ozhivaakkiyaal share thirichu kittumo? Vesting-um unvested share thirichuvaangalum agreement-il illenkil, share ayaalude peril thanne irikkum. Ningalude agreement-il leaver clause undo?")

# FAQ: "once I resign, nothing stays confidential"
duo("cf036", "remote_cofounder", "B", "gulfoffice", "\"രാജി വെച്ചാൽ\nരഹസ്യം ഒന്നും\nബാക്കിയില്ല\"", [
 ("A","wide","ആസിഫ്, നീ എതിരാളി കമ്പനിയിൽ ചേരുന്നു എന്ന് കേട്ടു. നമ്മുടെ നഴ്സ് റിക്രൂട്ട്മെന്റ് ക്ലയന്റ് ലിസ്റ്റ് നിനക്ക് മുഴുവൻ അറിയാമല്ലോ."),
 ("V","V","ഷഹാനാ, രാജി വെച്ചാൽ ഞാൻ ഫ്രീയാ. ഇന്ത്യയിൽ നോൺ-കോമ്പീറ്റ് നടക്കില്ലെന്ന് എല്ലാർക്കും അറിയാം."),
 ("A","A","ജോലി മാറുന്നത് തടയാൻ പറ്റില്ലായിരിക്കും. പക്ഷേ എല്ലാം അങ്ങനെയല്ല."),
 ("V","V","പിന്നെ എന്താ ബാക്കി?"),
 ("A","wide","പോയ ശേഷമുള്ള നോൺ-കോമ്പീറ്റ് പൊതുവെ നടക്കില്ല. പക്ഷേ എഗ്രിമെന്റിലെ കോൺഫിഡൻഷ്യാലിറ്റിയും നോൺ-സോളിസിറ്റും നടപ്പാക്കാം."),
 ("V","wide","കസേര മാറാം. രഹസ്യം കൂടെ പോരില്ല.")],
 "കസേര മാറാം,\nരഹസ്യം കൂടെ പോരില്ല", CTA_COFOUNDER, theme="faq",
 cap_ml="കോ-ഫൗണ്ടർ രാജി വെച്ച് എതിരാളി കമ്പനിയിൽ ചേർന്നാൽ ക്ലയന്റ് ലിസ്റ്റും കൊണ്ടുപോകാമോ? പോയ ശേഷമുള്ള നോൺ-കോമ്പീറ്റ് ഇന്ത്യയിൽ പൊതുവെ നടക്കില്ല, പക്ഷേ കോൺഫിഡൻഷ്യാലിറ്റിയും നോൺ-സോളിസിറ്റും നടപ്പാക്കാം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ഇവ ഉണ്ടോ?",
 cap_en="A co-founder of a nurse-recruitment startup resigns to join a rival and says nothing is confidential any more. A post-exit non-compete is generally not enforceable in India, but confidentiality and non-solicit clauses can be. Does your agreement have them?",
 cap_mg="Co-founder raaji vechu ethiraali company-il chernnaal client list-um kondupokaamo? Poya sheshamulla non-compete India-yil pothuve nadakkilla, pakshe confidentiality-um non-solicit-um nadappaakkaam. Ningalude agreement-il ivaa undo?")

# New: a rubber-sheet solar dryer startup; the dispute clause written on day one saves the friendship
duo("cf037", "friends_cofounders", "C", "rubber", "തർക്കം പഞ്ചായത്ത്\nമെമ്പർക്ക് മുന്നിൽ\nഎത്തും മുമ്പ്", [
 ("A","wide","തോമസേ, തമിഴ്നാട് ഡീലർക്ക് ഡ്രയർ കൊടുക്കില്ലെന്ന് നീ വാശി പിടിച്ചാൽ, ഞാൻ പഞ്ചായത്ത് മെമ്പറെ വിളിക്കും."),
 ("V","V","ജോയീ, മെമ്പറെ വിളിക്കണ്ട. നമ്മൾ ഒപ്പിട്ട എഗ്രിമെന്റ് ഒന്ന് എടുക്ക്."),
 ("A","A","റബ്ബർ ഷീറ്റ് ഡ്രയറിന്റെ ഡീലറെക്കുറിച്ച് അതിൽ എന്തുണ്ട്?"),
 ("V","wide","ഡീലറെക്കുറിച്ചല്ല. തർക്കം വന്നാൽ എങ്ങനെ തീർക്കും എന്ന് നമ്മൾ തുടക്കത്തിലേ എഴുതി. ആ വഴിയേ പോകാം."),
 ("A","A","കൂട്ടുകാരായിരുന്നപ്പോൾ എഴുതിയത് ഇന്ന് നമ്മളെ രക്ഷിച്ചു."),
 ("V","wide","വഴക്ക് വരും മുമ്പ് വഴി എഴുതണം.")],
 "വഴക്കിന് മുമ്പ്\nവഴി എഴുതണം", CTA_COFOUNDER, theme="new",
 cap_ml="റബ്ബർ ഷീറ്റ് സോളാർ ഡ്രയർ കമ്പനിയിലെ രണ്ട് ഫൗണ്ടർമാർ ഒരു ഡീലറെച്ചൊല്ലി വഴക്കിട്ടു, പക്ഷേ തർക്കം എങ്ങനെ തീർക്കും എന്ന് അവർ തുടക്കത്തിലേ എഗ്രിമെന്റിൽ എഴുതിയിരുന്നു. ഡിസ്പ്യൂട്ട് റെസല്യൂഷൻ ക്ലോസ് സൗഹൃദം ഉള്ളപ്പോൾ എഴുതൂ. നിങ്ങളുടേതിൽ ഇത് ഉണ്ടോ?",
 cap_en="Two founders of a rubber-sheet solar dryer company clash over a dealer, but they wrote down how disputes would be settled on day one. Put a dispute-resolution clause in your co-founder agreement while you still get along. Does yours have one?",
 cap_mg="Rubber sheet solar dryer company-ile randu founders oru dealer-e cholli vazhakkittu, pakshe tharkkam engane theerkkum ennu avar thudakkathile agreement-il ezhuthiyirunnu. Dispute resolution clause souhrudam ullappol ezhuthoo. Ningaludethil ithu undo?")

# New: a surf school where one co-founder coaches abroad for half the year
duo("cf038", "remote_cofounder", "A", "beach", "\"ആറ് മാസം ബാലിയിൽ.\nതീരുമാനം ഞാൻ\nവന്നിട്ട്\"", [
 ("A","wide","നിഖിലേ, മൺസൂണിൽ നീ ബാലിയിൽ കോച്ചിംഗിന് പോകുമ്പോൾ ഇവിടെ സർഫ് സ്കൂളിൽ ആര് തീരുമാനിക്കും?"),
 ("V","V","ദിവ്യേ, വലിയ കാര്യങ്ങൾ ഞാൻ വന്നിട്ട് നോക്കാം. പുതിയ ബോർഡ് വാങ്ങുന്നത് ഒക്കെ ഒക്ടോബറിൽ."),
 ("A","A","കഴിഞ്ഞ വർഷം അങ്ങനെ കാത്തിരുന്ന് സീസണിലെ ആദ്യ ബാച്ച് മുഴുവൻ പോയി."),
 ("V","V","അപ്പോ ഇനി എന്ത് ചെയ്യണം?"),
 ("A","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതാം: ഓരോരുത്തരുടെ റോൾ, ഒരാൾ ഇല്ലാത്തപ്പോൾ ആര് തീരുമാനിക്കും, ഏതിന് രണ്ടുപേരും വേണം."),
 ("V","wide","തിര കാത്തുനിൽക്കും. ബിസിനസ് കാത്തുനിൽക്കില്ല.")],
 "തിര കാത്തുനിൽക്കും,\nബിസിനസ് നിൽക്കില്ല", CTA_COFOUNDER, theme="new",
 cap_ml="വർക്കലയിലെ സർഫ് സ്കൂളിന്റെ ഒരു കോ-ഫൗണ്ടർ വർഷത്തിൽ ആറ് മാസം വിദേശത്ത്, തീരുമാനങ്ങൾ എല്ലാം അയാൾ വരുന്നത് വരെ കാത്തിരിക്കുന്നു. റോളുകളും, ഒരാൾ ഇല്ലാത്തപ്പോൾ ആര് തീരുമാനിക്കും എന്നതും, ഏതിന് രണ്ടുപേരും വേണം എന്നതും എഗ്രിമെന്റിൽ എഴുതൂ. നിങ്ങളുടെ കോ-ഫൗണ്ടർ എവിടെയാ?",
 cap_en="One co-founder of a surf school spends half the year coaching abroad, and every decision waits for him to come back. Write roles into the co-founder agreement, plus who decides when one founder is away and which calls need both. Where is your co-founder right now?",
 cap_mg="Varkala-yile surf school-nte oru co-founder varshathil aaru maasam videshathu, theerumaanangal ellam ayaal varunnathu vare kaathirikkunnu. Role-kalum, oraal illaathappol aaru theerumaanikkum ennathum, ethinu randuperum venam ennathum agreement-il ezhuthoo. Ningalude co-founder evideyaa?")
