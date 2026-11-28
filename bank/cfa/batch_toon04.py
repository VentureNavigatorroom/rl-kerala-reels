# Toon batch 04 for cfa (28 Nov night), episodes 9-11 of "അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്" (ep 8 teased "ഓർഡർ കിട്ടി, ഇനി?").
# Hari's LLP dispute continues: ep 9 an interim order (keep the copy, follow it, the court decides on a breach: always "may");
# ep 10 a partner who never paid his capital (First Schedule para 2, LLP only); ep 11 court or tribunal once the tribunal exists
# (s.9(3), s.17). General information only, a lawyer must see the documents. Facts only from topics.FACTS_CFA. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
SER = "അഖിലിന്റെ സ്റ്റാർട്ടപ്പ്"

toon("cfx09", "friends_cofounders", "B", {"A": "അഖിൽ", "B": "അപ്പൂപ്പൻ", "C": "ഹരി"}, "ഹരിക്ക് കോടതിയുടെ\nഇടക്കാല ഓർഡർ കിട്ടി.\nഇനി എന്ത്?", [
 ("C", "അഖിലേ, ഗോഡൗണിലെ സ്റ്റോക്ക് ആർബിട്രേഷൻ തീരും വരെ ആരും തൊടരുതെന്ന് കോടതിയുടെ ഇടക്കാല ഓർഡർ കിട്ടി. ഞാൻ ജയിച്ചില്ലേ?"),
 ("A", "അപ്പൂപ്പാ, ഓർഡർ കിട്ടിയാൽ കേസ് തീർന്നോ?"),
 ("B", "ഇല്ല. ഇത് ഇടക്കാല സംരക്ഷണം മാത്രം, കേസ് ഇനിയും നടക്കും. ഓർഡറിന്റെ കോപ്പി സൂക്ഷിക്കുക. ഹരിയും അത് പാലിക്കണം."),
 ("C", "മറുവശം അത് ലംഘിച്ചാലോ?"),
 ("B", "തീയതിയും ഫോട്ടോയും മെസേജും കുറിച്ച് വക്കീലിനെ അറിയിക്കുക. ലംഘിച്ചയാളുടെ സ്വത്ത് ജപ്തിക്കോ സിവിൽ ജയിലിനോ കോടതിക്ക് ഉത്തരവിടാം."),
 ("B", "പക്ഷേ എന്ത് ചെയ്യണം എന്ന് കോടതിയാണ് തീരുമാനിക്കുക. നമ്മളല്ല.")],
 dict(title="ഓർഡർ കിട്ടിയ ശേഷം", rows=[("ഓർഡർ കോപ്പി", "സൂക്ഷിക്കുക"), ("സ്വന്തം ഭാഗം", "പാലിക്കുക"), ("ലംഘനം കണ്ടാൽ", "തീയതി സഹിതം കുറിക്കുക")], total=("അടുത്ത പടി", "വക്കീൽ പറയും")),
 ["ഇടക്കാല ഓർഡർ അവസാന വിധിയല്ല.", "ഓർഡർ ലംഘിക്കപ്പെട്ടാൽ സ്വയം ഒന്നും ചെയ്യാതെ, തെളിവുമായി വക്കീലിനെ കാണുക."],
 "ഓർഡർ കയ്യിൽ,\nതെളിവ് ഫയലിൽ", topics.CTA_COFOUNDER, mentor="B", series=SER, ep=9, next="പണം ഇടാത്ത പാർട്ണർ", scene="teashop", theme="faq",
 cap_ml="പാർട്ണർ തർക്കത്തിൽ കോടതിയുടെ ഇടക്കാല ഓർഡർ കിട്ടിയാൽ കേസ് തീർന്നു എന്നല്ല. ഓർഡറിന്റെ കോപ്പി സൂക്ഷിക്കുക, സ്വന്തം ഭാഗം പാലിക്കുക, മറുവശം ലംഘിച്ചാൽ തീയതിയും തെളിവും കുറിച്ച് വക്കീലിനെ അറിയിക്കുക. ലംഘിച്ചവരുടെ സ്വത്ത് ജപ്തിയോ സിവിൽ ജയിലോ കോടതിക്ക് ഉത്തരവിടാം; തീരുമാനം കോടതിയുടേത്. പൊതുവായ വിവരം മാത്രം. നിങ്ങളുടെ കയ്യിൽ എല്ലാ ഓർഡറുകളുടെയും കോപ്പി ഉണ്ടോ?",
 cap_en="Hari got an interim court order to keep the godown stock untouched until the arbitration ends. That is protection, not the final result. Keep the order copy, follow it yourself, and if the other side breaks it, note dates and evidence and tell your lawyer. A court may order attachment of the property of a person who disobeys, or civil prison; the court decides. General information only. Do you keep copies of every order?",
 cap_mg="Partner tharkkathil kodathiyude idakkaala order kittiyaal case theernnu ennalla. Order copy sookshikkuka, swantham bhaagam paalikkuka, maruvasham langhichaal theeyathiyum thelivum kurichu vakeeline ariyikkuka. Langhichavarude swathu japthiyo civil jailo kodathikku uthharavidaam; theerumaanam kodathiyudethu. General information maathram. Ningalude kayyil ella order-ukaludeyum copy undo?")

toon("cfx10", "friends_cofounders", "B", {"A": "അഖിൽ", "B": "അപ്പൂപ്പൻ", "C": "അനഘ"}, "\"പണം മുഴുവൻ ഞാൻ.\nഅവൻ ഒന്നും ഇട്ടില്ല.\nഇപ്പോ പകുതി വേണം\"", [
 ("C", "അഖിലേ, കേക്ക് സ്റ്റുഡിയോ എൽഎൽപിയിലെ പണം മുഴുവൻ ഞാൻ ഇട്ടു. പാർട്ണർ പറഞ്ഞ തുക ഇതുവരെ ഇട്ടില്ല. ഇപ്പോ ലാഭത്തിന്റെ പകുതി വേണമെന്ന്."),
 ("A", "അപ്പൂപ്പാ, ആര് എത്ര ഇടണം എന്ന് എഗ്രിമെന്റിൽ എഴുതിയില്ലെങ്കിലോ?"),
 ("B", "എൽഎൽപി എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് ഫസ്റ്റ് ഷെഡ്യൂൾ വരും. അതിൽ മൂലധനവും ലാഭവും നഷ്ടവും പാർട്ണർമാർ തുല്യമായി പങ്കിടും എന്നാണ്."),
 ("C", "അപ്പോ അവനെ പുറത്താക്കി ബിസിനസ് ഞാൻ എടുക്കാമോ?"),
 ("B", "അത് രേഖകളും സാഹചര്യവും നോക്കി ഒരു വക്കീൽ പറയേണ്ടതാണ്. നീ ഇട്ട പണത്തിന്റെ ബാങ്ക് രേഖയും അവന്റെ വാഗ്ദാന മെസേജുകളും എടുത്ത് വെക്കുക."),
 ("A", "എന്റെ എഗ്രിമെന്റിൽ ആര് എത്ര, എപ്പോൾ, ഇട്ടില്ലെങ്കിൽ എന്ത് എന്ന് ഇന്ന് തന്നെ എഴുതും.")],
 dict(title="എഗ്രിമെന്റ് മിണ്ടിയില്ലെങ്കിൽ", rows=[("മൂലധനം", "തുല്യമായി"), ("ലാഭവും നഷ്ടവും", "തുല്യമായി"), ("ഇട്ട പണത്തിന്റെ രേഖ", "സൂക്ഷിക്കുക")], total=("ആദ്യം നോക്കുന്നത്", "എഗ്രിമെന്റ്")),
 ["ആര് എത്ര പണം ഇടും, എപ്പോൾ, ഇട്ടില്ലെങ്കിൽ എന്ത് എന്ന് എഗ്രിമെന്റിൽ എഴുതുക.", "ഫസ്റ്റ് ഷെഡ്യൂൾ എൽഎൽപിക്ക് മാത്രം. തർക്കമായാൽ രേഖകളുമായി വക്കീലിനെ കാണുക."],
 "വാഗ്ദാനം വാക്കിൽ,\nമൂലധനം എഴുത്തിൽ", topics.CTA_COFOUNDER, mentor="B", series=SER, ep=10, next="ട്രിബ്യൂണൽ വന്ന ശേഷം", scene="home", theme="faq",
 cap_ml="എൽഎൽപിയിൽ ഒരാൾ പണം മുഴുവൻ ഇട്ടു, മറ്റേയാൾ വാഗ്ദാനം ചെയ്ത തുക ഇട്ടില്ല, ഇപ്പോൾ ലാഭത്തിന്റെ പകുതി ചോദിക്കുന്നു. എഗ്രിമെന്റ് മിണ്ടാത്തിടത്ത് എൽഎൽപി നിയമത്തിലെ ഫസ്റ്റ് ഷെഡ്യൂൾ പ്രകാരം മൂലധനവും ലാഭവും നഷ്ടവും തുല്യമായി പങ്കിടും. അതുകൊണ്ട് ആര് എത്ര, എപ്പോൾ, ഇട്ടില്ലെങ്കിൽ എന്ത് എന്ന് എഴുതുക. പൊതുവായ വിവരം മാത്രം; രേഖകൾ ഒരു വക്കീൽ കാണണം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ മൂലധനം എഴുതിയിട്ടുണ്ടോ?",
 cap_en="One partner put in all the money; the other never paid what he promised and now wants half the profit. Where the LLP agreement is silent, the LLP Act's First Schedule says partners share capital, profits and losses equally. So write who puts in how much, by when, and what happens if they don't. General information only: a lawyer must see your documents. Is capital written in your agreement?",
 cap_mg="LLP-yil oraal panam muzhuvan ittu, mattethaal vaagdaanam cheytha thuka ittilla, ippol laabhathinte pakuthi chodikkunnu. Agreement mindaathidathu LLP Act-ile First Schedule prakaaram capital-um laabhavum nashtavum thulyamaayi pankidum. Athukondu aaru ethra, eppol, ittillenkil enthu ennu ezhuthuka. General information maathram; rekhakal oru vakeel kaananam. Ningalude agreement-il capital ezhuthiyittundo?")

toon("cfx11", "friends_cofounders", "B", {"A": "അഖിൽ", "B": "അപ്പൂപ്പൻ", "C": "ഹരി"}, "ട്രിബ്യൂണൽ വന്നു.\nഎന്നിട്ടും പാർട്ണർ\nവീണ്ടും കോടതിയിൽ", [
 ("C", "അഖിലേ, ആർബിട്രൽ ട്രിബ്യൂണൽ ഇപ്പോൾ നിലവിൽ വന്നു. എന്നിട്ടും പാർട്ണർ പുതിയ ഇടക്കാല ഓർഡറിന് വീണ്ടും കോടതിയിൽ പോകുന്നു."),
 ("A", "അപ്പൂപ്പാ, ഇനി ഇടക്കാല കാര്യങ്ങൾ ആര് നോക്കും? കോടതിയോ ട്രിബ്യൂണലോ?"),
 ("B", "ആർബിട്രേഷന് മുമ്പും ഇടയിലും കോടതിയോട് ഇടക്കാല സംരക്ഷണം ചോദിക്കാം. പക്ഷേ ട്രിബ്യൂണൽ വന്നാൽ കോടതി സാധാരണ അത് ട്രിബ്യൂണലിന് വിടും."),
 ("C", "ട്രിബ്യൂണലിന്റെ ഓർഡറിന് കോടതി ഓർഡറിന്റെ ബലമുണ്ടോ?"),
 ("B", "ഉണ്ട്. ട്രിബ്യൂണലിന്റെ ഇടക്കാല ഓർഡർ കോടതി ഓർഡർ പോലെ നടപ്പാക്കാം. നിന്റെ കാര്യത്തിൽ ഏത് വഴി എന്ന് വക്കീൽ രേഖ നോക്കി പറയും.")],
 dict(title="ഇടക്കാല സംരക്ഷണം ആരോട്", rows=[("ആർബിട്രേഷന് മുമ്പ്", "കോടതി"), ("ട്രിബ്യൂണൽ വന്ന ശേഷം", "സാധാരണ ട്രിബ്യൂണൽ"), ("ട്രിബ്യൂണലിന്റെ ഓർഡർ", "കോടതി ഓർഡർ പോലെ")], total=("ഏത് വഴി", "വക്കീലുമായി ആലോചിച്ച്")),
 ["ഓരോ ഘട്ടത്തിലും എവിടെ പോകണം എന്ന് വക്കീലിനോട് ചോദിക്കുക.", "എല്ലാ ഓർഡറുകളുടെയും കോപ്പി തീയതി ക്രമത്തിൽ ഒരു ഫയലിൽ വെക്കുക."],
 "ട്രിബ്യൂണൽ വന്നാൽ\nആദ്യ വാതിൽ അതാണ്", topics.CTA_COFOUNDER, mentor="B", series=SER, ep=11, next="അടുത്ത സീസൺ", scene="office", theme="faq",
 cap_ml="ആർബിട്രേഷന് മുമ്പും ഇടയിലും ഇടക്കാല സംരക്ഷണത്തിന് കോടതിയെ സമീപിക്കാം; പക്ഷേ ആർബിട്രൽ ട്രിബ്യൂണൽ നിലവിൽ വന്നാൽ കോടതി സാധാരണ അത് ട്രിബ്യൂണലിന് വിടും. ട്രിബ്യൂണലിന്റെ ഇടക്കാല ഓർഡർ കോടതി ഓർഡർ പോലെ നടപ്പാക്കാം. പൊതുവായ വിവരം മാത്രം; നിങ്ങളുടെ കാര്യം ഒരു വക്കീൽ രേഖ നോക്കി പറയണം. നിങ്ങളുടെ എഗ്രിമെന്റിൽ ആർബിട്രേഷൻ ക്ലോസ് ഉണ്ടോ?",
 cap_en="Before or during arbitration, a party may ask a court for interim measures, but once the arbitral tribunal is formed the court normally leaves it to the tribunal. The tribunal's interim order is enforceable as if it were a court order. General information only: a lawyer must look at your documents. Does your agreement have an arbitration clause?",
 cap_mg="Arbitration-inu mumpum idayilum idakkaala samrakshanathinu kodathiye sameepikkaam; pakshe arbitral tribunal roopeekarichaal kodathi saadhaarana athu tribunal-inu vidum. Tribunal-inte idakkaala order court order pole nadappaakkaam. General information maathram; ningalude kaaryam oru vakeel rekha nokki parayanam. Ningalude agreement-il arbitration clause undo?")
