# Data room toon 02 (28 Nov night): "നിഖിലിന്റെ ആദ്യ ഫണ്ടിംഗ്", eps 5-8. Facts only from topics.FACTS_DR. Never promise funding, an investor, a valuation or a timeline; no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, toon, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.toon, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE
SER = "നിഖിലിന്റെ ആദ്യ ഫണ്ടിംഗ്"

# ep 5 (teased by drx04: "GST, ROC ഫയലിംഗ് പെൻഡിംഗ്"); crm C6 style: the company sat idle and nobody filed
toon("drx05", "messy_docs", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "കമ്പനി രണ്ട് വർഷം\nഉറങ്ങി. ഫയലിംഗും\nഉറങ്ങി", [
 ("C", "നിഖിലേ, കമ്പനി കുറച്ച് കാലം ഒന്നും ചെയ്യാതെ ഇരുന്നതല്ലേ. അപ്പോ ഫയലിംഗ് ഒന്നും വേണ്ടല്ലോ?"),
 ("A", "ഞാനും അങ്ങനെയാ കരുതിയത്. പക്ഷേ ഇൻവെസ്റ്ററുടെ ലിസ്റ്റിൽ GST റിട്ടേണും ROC ഫയലിംഗും ഉണ്ട്, അമ്മൂമ്മേ."),
 ("B", "ബിസിനസ് ഉറങ്ങിയാലും ഫയലിംഗ് ഉറങ്ങില്ല മോനേ. പെൻഡിംഗ് ഫയലിംഗ് ഡ്യൂ ഡിലിജൻസിൽ ആദ്യം കാണുന്ന റെഡ് ഫ്ലാഗുകളിൽ ഒന്നാണ്."),
 ("A", "അപ്പോ ഡാറ്റ റൂമിന് മുമ്പ് പെൻഡിംഗ് ഉള്ളത് തീർക്കണം.")],
 dict(title="കംപ്ലയൻസ് ഫോൾഡർ", rows=[("ROC ഫയലിംഗ്", "പെൻഡിംഗ് തീർക്കുക"), ("GST റിട്ടേൺ", "ഒത്തുനോക്കുക"), ("ഇൻകം ടാക്സ്", "ഫോൾഡറിൽ")], total=("പെൻഡിംഗ് ഉണ്ടെങ്കിൽ", "റെഡ് ഫ്ലാഗ്")),
 ["ഇൻവെസ്റ്ററെ കാണും മുമ്പ് പെൻഡിംഗ് ഫയലിംഗുകൾ ലിസ്റ്റ് ചെയ്ത് തീർക്കുക.", "ഫയൽ ചെയ്ത ഓരോ രേഖയും കംപ്ലയൻസ് ഫോൾഡറിൽ ഇടുക."],
 "ബിസിനസ് ഉറങ്ങിയാലും\nഫയലിംഗ് ഉറങ്ങില്ല", CTA_DILIGENCE, mentor="B", series=SER, ep=5, next="\"എത്ര ഷെയറിന് എത്ര പൈസ?\"", scene="office", theme="crm",
 cap_ml="കമ്പനി കുറച്ച് കാലം ഒന്നും ചെയ്യാതെ ഇരുന്നാലും ഫയലിംഗ് പെൻഡിംഗ് ആയാൽ ഡ്യൂ ഡിലിജൻസിൽ റെഡ് ഫ്ലാഗ്. GST, ഇൻകം ടാക്സ്, ROC ഫയലിംഗുകൾ ഡാറ്റ റൂമിൽ വേണം. നിങ്ങളുടെ ഏതെങ്കിലും ഫയലിംഗ് ഉറങ്ങിക്കിടക്കുന്നുണ്ടോ?",
 cap_en="Nikhil's company sat idle for two years and nobody filed. Pending filings are among the first red flags in due diligence: the data room needs GST returns, income tax and ROC filings. Is any of your filing asleep?",
 cap_mg="Company kurachu kaalam onnum cheyyaathe irunnaalum filing pending aayaal due diligence-il red flag. GST, income tax, ROC filings data room-il venam. Ningalude ethenkilum filing urangikkidakkunnundo?")

# ep 6: the investor asks "how much for how many shares?" - a valuation is one of the missing pieces we prepare (never a figure)
toon("drx06", "investor_asked", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "\"എത്ര ഷെയറിന്\nഎത്ര പൈസ?\"\nനിഖിൽ ഒരു നമ്പർ പറഞ്ഞു", [
 ("C", "നിഖിലേ, ഇൻവെസ്റ്റർ ചോദിച്ചപ്പോൾ നീ എന്ത് നമ്പർ ആണ് പറഞ്ഞത്?"),
 ("A", "മനസ്സിൽ തോന്നിയ ഒന്ന്. അവർ ചോദിച്ചു, ഇത് എങ്ങനെ കണക്കാക്കി എന്ന്. ഉത്തരം ഇല്ലായിരുന്നു, അമ്മൂമ്മേ."),
 ("B", "തോന്നിയ നമ്പർ ഡാറ്റ റൂമിൽ നിൽക്കില്ല മോനേ. പ്രൊജക്ഷനും ബിസിനസ് മോഡലും വെച്ച് ഒരു വാല്യുവേഷൻ ആദ്യം ഒരുക്കണം."),
 ("A", "ഇല്ലാത്തതാണെങ്കിൽ അതും ഒരുക്കാം അല്ലേ? എത്ര വരും എന്ന് ഇപ്പോൾ ഊഹിക്കേണ്ട.")],
 dict(title="ഷെയർ ചർച്ചയ്ക്ക് മുമ്പ്", rows=[("പ്രൊജക്ഷൻ", "എഴുതിയത്"), ("ബിസിനസ് മോഡൽ", "വ്യക്തം"), ("വാല്യുവേഷൻ", "കാരണങ്ങളോടെ")], total=("തോന്നിയ നമ്പർ", "ചോദ്യം മാത്രം")),
 ["വാല്യുവേഷൻ ഒരു ഊഹമല്ല, കാരണങ്ങളോടെ ഒരുക്കുന്ന രേഖയാണ്.", "ഷെയർ ചർച്ചയ്ക്ക് മുമ്പ് അത് ഡാറ്റ റൂമിൽ വെക്കുക."],
 "തോന്നിയ നമ്പർ അല്ല,\nകാരണമുള്ള കണക്ക്", CTA_DATAROOM, mentor="B", series=SER, ep=6, next="വലിയ ക്ലയന്റ്, കരാർ ഇല്ല", scene="home", theme="faq",
 cap_ml="ഇൻവെസ്റ്റർ \"എത്ര ഷെയറിന് എത്ര പൈസ\" എന്ന് ചോദിച്ചാൽ തോന്നിയ നമ്പർ പറയരുത്. പ്രൊജക്ഷനും ബിസിനസ് മോഡലും വെച്ചുള്ള വാല്യുവേഷൻ ഡാറ്റ റൂമിൽ വേണം. ഇല്ലെങ്കിൽ ഞങ്ങളുടെ ടീം അതും ഒരുക്കും. നിങ്ങളുടെ നമ്പറിന് കാരണമുണ്ടോ?",
 cap_en="The investor asked how much for how many shares, and Nikhil said a number from his head. A valuation should be prepared with reasons, from projections and the business model, and sit in the data room; if it's missing, our team prepares it too. Can you explain your number?",
 cap_mg="Investor 'ethra share-inu ethra paisa' ennu chodichaal thonniya number parayaruthu. Projection-um business model-um vechulla valuation data room-il venam. Illenkil njangalude team athum orukkum. Ningalude number-inu kaaranamundo?")

# ep 7: half the revenue comes from one client, with nothing signed
toon("drx07", "investor_asked", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "വരുമാനത്തിന്റെ പകുതി\nഒരു ക്ലയന്റ്.\nകരാർ? ഇല്ല", [
 ("C", "നിഖിലേ, ഇൻവെസ്റ്റർ നമ്മുടെ ഏറ്റവും വലിയ ക്ലയന്റിന്റെ കരാർ ചോദിച്ചു. എല്ലാം വാട്സാപ്പിൽ അല്ലേ?"),
 ("A", "അമ്മൂമ്മേ, അവർ മൂന്ന് വർഷമായി ഓർഡർ തരുന്നു. ഒരിക്കലും മുടങ്ങിയിട്ടില്ല. അത് പോരേ?"),
 ("B", "നിനക്ക് വിശ്വാസം ഉണ്ട്, ഇൻവെസ്റ്റർക്ക് രേഖ വേണം. പ്രധാന കസ്റ്റമർ, വെണ്ടർ കരാറുകൾ ഡാറ്റ റൂമിൽ വേണം മോനേ."),
 ("C", "കരാർ ഇല്ലെങ്കിൽ ആ വരുമാനം എത്ര ഉറപ്പാണ് എന്ന് അവർ സംശയിക്കും, അല്ലേ?")],
 dict(title="കരാർ ഫോൾഡർ", rows=[("പ്രധാന കസ്റ്റമർ കരാർ", "ഒപ്പിട്ടത്"), ("പ്രധാന വെണ്ടർ കരാർ", "ഒപ്പിട്ടത്"), ("വാട്സാപ്പ് ധാരണ", "പോരാ")], total=("വലിയ വരുമാനം", "എഴുതിയ കരാർ")),
 ["വരുമാനത്തിന്റെ വലിയ പങ്ക് തരുന്ന ക്ലയന്റുമായി എഴുതിയ കരാർ വെക്കുക.", "ഒപ്പിട്ട കോപ്പി ഡാറ്റ റൂമിന്റെ കരാർ ഫോൾഡറിൽ ഇടുക."],
 "വിശ്വാസം നിങ്ങൾക്ക്,\nരേഖ ഇൻവെസ്റ്റർക്ക്", CTA_DILIGENCE, mentor="B", series=SER, ep=7, next="ഡാറ്റ റൂം റെഡി. ഇനി ഫണ്ട് ഉറപ്പാണോ?", scene="office", theme="crm",
 cap_ml="വരുമാനത്തിന്റെ പകുതി ഒരു ക്ലയന്റിൽ നിന്ന്, പക്ഷേ ഒപ്പിട്ട കരാർ ഇല്ല. പ്രധാന കസ്റ്റമർ, വെണ്ടർ കരാറുകൾ ഡാറ്റ റൂമിൽ ഇൻവെസ്റ്റർ നോക്കും. നിങ്ങളുടെ വലിയ ക്ലയന്റുമായി കരാറുണ്ടോ?",
 cap_en="Half of Nikhil's revenue comes from one client, and everything is on WhatsApp. Investors look for signed key customer and vendor contracts in the data room. Is your biggest client on paper?",
 cap_mg="Varumaanathinte pakuthi oru client-il ninnu, pakshe oppitta karaar illa. Pradhaana customer, vendor karaarukal data room-il investor nokkum. Ningalude valiya client-umaayi karaarundo?")

# ep 8: the data room is ready - does that mean the money is sure? (honest answer: no one can promise that)
toon("drx08", "raising_first", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "ഡാറ്റ റൂം റെഡി.\n\"ഇനി ഫണ്ട്\nഉറപ്പല്ലേ?\"", [
 ("A", "അമ്മൂമ്മേ, എല്ലാ ഫോൾഡറും നിറഞ്ഞു. ഫയലിംഗ് തീർന്നു, കരാർ ഒപ്പിട്ടു. ഇനി ഫണ്ടിംഗ് ഉറപ്പല്ലേ?"),
 ("B", "ആർക്കും അത് ഉറപ്പ് പറയാൻ പറ്റില്ല മോനേ. ഇൻവെസ്റ്റർ തീരുമാനിക്കുന്നത് ബിസിനസ് നോക്കിയാണ്."),
 ("C", "പിന്നെ ഇത്രയും പണി എന്തിനായിരുന്നു?"),
 ("B", "രേഖ കുഴഞ്ഞതുകൊണ്ടുള്ള വൈകലും റെഡ് ഫ്ലാഗും നേരത്തെ ഒഴിവാക്കാം. ലോൺ ആയാലും പാർട്ണർ ആയാലും ഇതേ ഫോൾഡർ ഉപകാരപ്പെടും.")],
 dict(title="ഡാറ്റ റൂം കൊണ്ട്", rows=[("ഫണ്ട് ഉറപ്പ്", "ഇല്ല"), ("റെഡ് ഫ്ലാഗ്", "നേരത്തെ ശരിയാക്കാം"), ("ലോൺ, പാർട്ണർ, വിൽപ്പന", "അതേ ഫോൾഡർ")], total=("ഉറപ്പുള്ളത്", "നിങ്ങളുടെ ഒരുക്കം")),
 ["ഫണ്ട് ഉറപ്പ് തരുന്ന ആരെയും വിശ്വസിക്കരുത്.", "ഡാറ്റ റൂം ഓരോ മാസവും പുതുക്കി വെക്കുക."],
 "ഫണ്ട് ഉറപ്പില്ല,\nഒരുക്കം ഉറപ്പാക്കാം", CTA_DATAROOM, mentor="B", series=SER, ep=8, next="ഇൻവെസ്റ്ററുടെ ചോദ്യ ലിസ്റ്റ് വന്നു", scene="home", theme="faq",
 cap_ml="ഡാറ്റ റൂം റെഡിയായാൽ ഫണ്ട് ഉറപ്പാണോ? ഇല്ല, ആർക്കും അത് ഉറപ്പ് പറയാൻ പറ്റില്ല. പക്ഷേ രേഖ കുഴഞ്ഞതുകൊണ്ടുള്ള വൈകലും റെഡ് ഫ്ലാഗും ഒഴിവാക്കാം. ഫണ്ട് ഉറപ്പ് തന്ന ആരെയെങ്കിലും നിങ്ങൾ കണ്ടിട്ടുണ്ടോ?",
 cap_en="Nikhil's data room is complete. Does that make funding certain? No one can promise that; investors decide on the business. What a data room does is stop messy documents and red flags from slowing or stalling due diligence, and the same folder serves a loan, a partner or a sale. Has anyone ever 'guaranteed' you funding?",
 cap_mg="Data room ready aayaal fund urappaano? Illa, aarkkum athu urappu parayaan pattilla. Pakshe rekha kuzhanjathukondulla vaikalum red flag-um ozhivaakkaam. Fund urappu thanna aareyenkilum ningal kandittundo?")
