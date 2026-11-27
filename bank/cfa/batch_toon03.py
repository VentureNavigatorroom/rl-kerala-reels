# Toon batch 03 for cfa (27 Nov, owner's idea: partner disputes), episodes 7-8 of "അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്" (ep 6 teased "ഇൻവെസ്റ്റർ").
# Facts only from topics.FACTS_CFA "Partner disputes" (LLP First Schedule rules are LLP-only). General information, never advice on a
# case: a lawyer must see the documents. Never promise an outcome, never criticise police or lawyers. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("cfx07", "tech_nontech", "B", {"A": "അഖിൽ", "B": "അപ്പൂപ്പൻ", "C": "ശ്രുതി"}, "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n'നിങ്ങൾ രണ്ടുപേരും\nതെറ്റിയാൽ?'", [
 ("C", "അഖിലേ, ഇൻവെസ്റ്റർ ചോദിച്ചു: നമ്മൾ രണ്ടുപേരും ഒരു കാര്യത്തിൽ തെറ്റിയാൽ കമ്പനി നിന്നുപോകുമോ എന്ന്."),
 ("A", "അപ്പൂപ്പാ, ഞങ്ങൾ തമ്മിൽ വഴക്കൊന്നും ഇല്ലല്ലോ. എന്തിനാ ഈ ചോദ്യം?"),
 ("B", "തുല്യ ഷെയർ ഉള്ളിടത്ത് ഒരു ഉടക്ക് മതി എല്ലാം നിൽക്കാൻ. അതാ ഇൻവെസ്റ്റർ എഗ്രിമെന്റിൽ ആദ്യം നോക്കുന്നത്."),
 ("C", "അപ്പോ നമ്മൾ എന്ത് എഴുതണം, അപ്പൂപ്പാ?"),
 ("B", "ഏത് തീരുമാനത്തിന് രണ്ടുപേരും വേണം, ടൈ ആയാൽ എന്ത്, തർക്കം ആദ്യം എങ്ങനെ സംസാരിച്ച് തീർക്കും, തീർന്നില്ലെങ്കിൽ ഏത് വഴി.")],
 dict(title="തർക്കം വരും മുമ്പ് എഴുതാൻ", rows=[("ഏത് തീരുമാനം", "ആര് എടുക്കും"), ("ടൈ ആയാൽ", "എന്ത് ചെയ്യും"), ("തീരാത്ത തർക്കം", "ഏത് വഴി")], total=("എഴുതിയില്ലെങ്കിൽ", "കമ്പനി നിൽക്കും")),
 ["തുല്യ ഷെയർ ആണെങ്കിൽ ടൈ വന്നാൽ എന്ത് എന്ന് എഴുതുക.", "തർക്കം തീർക്കാനുള്ള വഴി സ്നേഹമുള്ളപ്പോൾ തന്നെ എഗ്രിമെന്റിൽ ചേർക്കുക."],
 "ടൈ വന്നാൽ എന്ത്?\nഇന്നുതന്നെ എഴുതൂ", topics.CTA_COFOUNDER, mentor="B", series="അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്", ep=7, next="ഹരിയുടെ എൽഎൽപി തർക്കം", scene="office", theme="new",
 cap_ml="അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്, എപ്പിസോഡ് 7. ഇൻവെസ്റ്റർ ചോദിച്ചു: 'നിങ്ങൾ രണ്ടുപേരും തെറ്റിയാൽ?' തുല്യ ഷെയർ ഉള്ള ഫൗണ്ടർമാർ ഏത് തീരുമാനത്തിന് രണ്ടുപേരും വേണം, ടൈ ആയാൽ എന്ത്, തർക്കം എങ്ങനെ തീർക്കും എന്നത് കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ എഴുതണം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ഇത് ഉണ്ടോ?",
 cap_en="Akhil's startup, episode 7. The investor asks: \"What if the two of you disagree?\" Founders with equal shares should write into the co-founder agreement which decisions need both of them, what happens in a tie, and how a dispute will be resolved. Does yours say this?",
 cap_mg="Akhil-nte startup, episode 7. Investor chodichu: 'Ningal randuperum thettiyaal?' Thulya share ulla founders ethu theerumaanathinu randuperum venam, tie aayaal enthu, tharkkam engane theerkkum ennathu co-founder agreement-il ezhuthanam. Ningalude agreement-il ithu undo?")

toon("cfx08", "friends_cofounders", "B", {"A": "അഖിൽ", "B": "അപ്പൂപ്പൻ", "C": "ഹരി"}, "ഹരിയുടെ എൽഎൽപി.\nഎഗ്രിമെന്റിൽ\nതർക്ക ക്ലോസ് ഇല്ല", [
 ("C", "അഖിലേ, പാർട്ണറുമായി തർക്കം. ഞങ്ങളുടെ എൽഎൽപി എഗ്രിമെന്റിൽ തർക്കം എങ്ങനെ തീർക്കും എന്ന് ഒരു വരി പോലുമില്ല."),
 ("A", "അപ്പൂപ്പാ, അപ്പോ ഹരിക്ക് ഇനി ഒരു വഴിയുമില്ലേ?"),
 ("B", "എൽഎൽപി നിയമത്തിൽ ഒരു ഫസ്റ്റ് ഷെഡ്യൂൾ ഉണ്ട്. എഗ്രിമെന്റ് മിണ്ടാത്ത കാര്യങ്ങളിൽ അതിലെ നിയമങ്ങൾ വരും."),
 ("C", "അതിൽ തർക്കത്തെക്കുറിച്ച് എന്താ പറയുന്നത്?"),
 ("B", "എഗ്രിമെന്റിൽ നിന്നുള്ള തർക്കം അതുകൊണ്ട് തീർന്നില്ലെങ്കിൽ ആർബിട്രേഷന് വിടണം. ഇടക്കാല സംരക്ഷണത്തിന് കോടതിയെയും സമീപിക്കാം."),
 ("B", "പക്ഷേ ഓരോ കേസും വേറെയാ. രേഖകൾ ഒരു വക്കീൽ നോക്കട്ടെ.")],
 dict(title="ഹരി ഇപ്പോൾ കയ്യിൽ വെക്കേണ്ടത്", rows=[("എൽഎൽപി എഗ്രിമെന്റ്", "കോപ്പി"), ("മെസേജ്, മിനിറ്റ്സ്", "തീയതി സഹിതം"), ("ബാങ്ക്, സ്റ്റോക്ക്", "ലിസ്റ്റ്")], total=("ഇതുമായി", "വക്കീലിനെ കാണുക")),
 ["ഓരോ കേസും വ്യത്യസ്തം. വഴി തീരുമാനിക്കും മുമ്പ് ഒരു വക്കീൽ രേഖകൾ കാണണം.", "അടുത്ത എഗ്രിമെന്റിൽ തർക്കം തീർക്കുന്ന വഴി ആദ്യമേ എഴുതുക."],
 "രേഖകൾ കയ്യിൽ,\nവക്കീൽ കൂടെ", topics.CTA_COFOUNDER, mentor="B", series="അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്", ep=8, next="ഓർഡർ കിട്ടി, ഇനി?", scene="teashop", theme="faq",
 cap_ml="അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്, എപ്പിസോഡ് 8. സുഹൃത്ത് ഹരിയുടെ എൽഎൽപി എഗ്രിമെന്റിൽ തർക്കം തീർക്കുന്ന വഴി എഴുതിയിട്ടില്ല. എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പറയുന്നത്: എഗ്രിമെന്റിൽ നിന്നുള്ള തർക്കം അതുകൊണ്ട് തീർന്നില്ലെങ്കിൽ ആർബിട്രേഷന് വിടണം. ഇടക്കാല സംരക്ഷണത്തിന് ആർബിട്രേഷൻ നിയമത്തിലെ സെക്ഷൻ 9 പ്രകാരം കോടതിയെ സമീപിക്കാം. ഇത് പൊതുവായ വിവരം മാത്രം; നിങ്ങളുടെ കേസ് ഒരു വക്കീൽ രേഖകൾ നോക്കി പറയണം. ഞങ്ങളുടെ ടീമിന് വക്കീലുമായി ബന്ധിപ്പിക്കാം.",
 cap_en="Akhil's startup, episode 8. His friend Hari's LLP agreement has no dispute clause. The LLP Act's First Schedule says disputes between partners arising out of the LLP agreement that can't be resolved under it are referred to arbitration, and section 9 of the Arbitration and Conciliation Act lets a party ask a court for interim protection. General information only, not legal advice: a lawyer must look at your documents. Our team can connect you with one.",
 cap_mg="Akhil-nte startup, episode 8. Friend Hari-yude LLP agreement-il tharkkam theerkkunna vazhi ezhuthiyittilla. LLP niyamathile First Schedule parayunnathu: agreement-il ninnulla tharkkam athukondu theernnillenkil arbitration-nu vidanam. Idakkaala samrakshanathinu arbitration niyamathile section 9 prakaaram court-ne sameepikkaam. Ithu pothuvaaya vivaram maathram; ningalude case oru vakeel rekhakal nokki parayanam. Njangalude team-nu vakeelumaayi bandhippikkaam.")
