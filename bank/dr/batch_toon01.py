# Data room toon 01 (28 Nov): 2D story series "നിഖിലിന്റെ ആദ്യ ഫണ്ടിംഗ്", eps 1-4. Facts only from topics.FACTS_DR. Never promise funding, an investor, a valuation or a timeline; no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, toon, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.toon, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE
SER = "നിഖിലിന്റെ ആദ്യ ഫണ്ടിംഗ്"

toon("drx01", "investor_asked", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "ഇൻവെസ്റ്റർ പറഞ്ഞു:\n\"ഡാറ്റ റൂം\nഅയക്കൂ\"", [
 ("A", "അമ്മൂമ്മേ, ഇൻവെസ്റ്റർ മീറ്റിംഗ് നന്നായി. ഇപ്പോൾ അവർ ഡാറ്റ റൂം ലിങ്ക് ചോദിക്കുന്നു!"),
 ("C", "ഡാറ്റ റൂം എന്നാൽ എന്താ? വല്ല മുറിയും ആണോ?"),
 ("B", "മുറി അല്ല മോളേ. കമ്പനിയുടെ എല്ലാ രേഖകളും ഒരുക്കി വെച്ച ഒരു സുരക്ഷിത ഓൺലൈൻ ഫോൾഡർ.")],
 dict(title="ഡാറ്റ റൂമിൽ", rows=[("രജിസ്ട്രേഷൻ രേഖകൾ", "വേണം"), ("കണക്കുകൾ, പ്രൊജക്ഷൻ", "വേണം"), ("കരാറുകൾ", "വേണം")], total=("ഇൻവെസ്റ്റർ നോക്കുന്നത്", "എല്ലാം")),
 ["ഇൻവെസ്റ്റർ ചോദിക്കും മുമ്പേ രേഖകൾ ഒരിടത്ത് ഒരുക്കുക.", "ഓരോ ഫോൾഡറിനും വ്യക്തമായ പേര് നൽകുക."],
 "ലിങ്ക് ചോദിക്കും മുമ്പ്\nഫോൾഡർ റെഡി", CTA_DATAROOM, mentor="B", series=SER, ep=1, next="കമ്പനി രജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ?", scene="home", theme="faq",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റ റൂം ചോദിച്ചാൽ എന്ത് ചെയ്യും? കമ്പനിയുടെ എല്ലാ രേഖകളും ഒരുക്കിയ സുരക്ഷിത ഓൺലൈൻ ഫോൾഡറാണ് ഡാറ്റ റൂം. നിങ്ങളുടെ രേഖകൾ ഒരിടത്താണോ?",
 cap_en="Nikhil's investor meeting went well, and now they want a data room link. A data room is a secure online folder with all your company's documents: registration, accounts, projections and agreements. Are your documents in one place?",
 cap_mg="Investor data room chodichaal enthu cheyyum? Company-yude ella rekhakalum orukkiya secure online folder aanu data room. Ningalude rekhakal oridathaano?")

toon("drx02", "unregistered_dr", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ"}, "ഡാറ്റ റൂം ഉണ്ടാക്കാൻ\nനോക്കി. കമ്പനി\nതന്നെ ഇല്ല!", [
 ("A", "അമ്മൂമ്മേ, ഫോൾഡർ തുടങ്ങി. പക്ഷേ ഇൻകോർപ്പറേഷൻ സർട്ടിഫിക്കറ്റ് എവിടെ? ഞാൻ കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ടില്ല!"),
 ("B", "ഇക്വിറ്റി നിക്ഷേപത്തിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം മോനേ. ഡാറ്റ റൂമിന്റെ ആദ്യ ഫോൾഡർ അതാണ്.")],
 dict(title="ആദ്യ ഫോൾഡർ", rows=[("ഇൻകോർപ്പറേഷൻ സർട്ടിഫിക്കറ്റ്", "വേണം"), ("MOA, AOA", "വേണം"), ("കമ്പനി PAN", "വേണം")], total=("കമ്പനി ഇല്ലെങ്കിൽ", "ആദ്യം രജിസ്ട്രേഷൻ")),
 ["ഇൻവെസ്റ്റർ സംസാരം തുടങ്ങും മുമ്പ് കമ്പനി രജിസ്റ്റർ ചെയ്യുക.", "ഷെയർ ആർക്ക് എത്ര എന്ന് രേഖയിൽ ആക്കുക."],
 "ഡാറ്റ റൂമിന്റെ\nതുടക്കം രജിസ്ട്രേഷൻ", CTA_DATAROOM, mentor="B", series=SER, ep=2, next="പ്രൊജക്ഷൻ ഇല്ലെങ്കിൽ?", scene="office", theme="crm",
 cap_ml="ഡാറ്റ റൂമിന്റെ ആദ്യ ഫോൾഡർ കമ്പനി രജിസ്ട്രേഷൻ രേഖകളാണ്: ഇൻകോർപ്പറേഷൻ സർട്ടിഫിക്കറ്റ്, MOA, AOA, PAN. കമ്പനി ഇല്ലെങ്കിൽ ആദ്യം രജിസ്ട്രേഷൻ. നിങ്ങളുടെ കമ്പനി രജിസ്റ്റർ ചെയ്തോ?",
 cap_en="Nikhil starts his data room and realises he never registered a company. Equity investment needs a private limited company, and its incorporation certificate, MOA, AOA and PAN are the first folder. Is your company registered?",
 cap_mg="Data room-inte aadya folder company registration rekhakal aanu: incorporation certificate, MOA, AOA, PAN. Company illenkil aadyam registration. Ningalude company register cheytho?")

toon("drx03", "raising_first", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "\"അടുത്ത 3 വർഷം\nഎന്താകും?\"\nഉത്തരമില്ല", [
 ("C", "നിഖിലേ, ഇൻവെസ്റ്റർ മൂന്ന് വർഷത്തെ പ്രൊജക്ഷൻ ചോദിച്ചല്ലോ. റെഡി ആണോ?"),
 ("A", "എന്റെ മനസ്സിലുണ്ട്. എഴുതിയിട്ടില്ല."),
 ("B", "മനസ്സിലുള്ളത് ഇൻവെസ്റ്റർക്ക് വായിക്കാനാവില്ല. ആദ്യ വർഷം മാസം തോറും, കാരണം എഴുതിയ കണക്ക് വേണം.")],
 dict(title="പ്രൊജക്ഷനിൽ", rows=[("മൂന്ന് വർഷം", "വേണം"), ("ആദ്യ വർഷം മാസം തോറും", "വേണം"), ("ഓരോ നമ്പറിനും കാരണം", "വേണം")], total=("ഊഹ നമ്പറുകൾ", "റെഡ് ഫ്ലാഗ്")),
 ["ഓരോ നമ്പറിനും ഒരു കാരണം എഴുതുക.", "ഇപ്പോഴത്തെ വരുമാനവുമായി പ്രൊജക്ഷൻ ചേരണം."],
 "മനസ്സിലെ കണക്ക്\nപേപ്പറിലാക്കൂ", CTA_DILIGENCE, mentor="B", series=SER, ep=3, next="കോ-ഫൗണ്ടർ കരാർ ഇല്ലെങ്കിൽ?", scene="office", theme="faq",
 cap_ml="ഡാറ്റ റൂമിൽ ഇൻവെസ്റ്റർ മൂന്ന് വർഷത്തെ ഫിനാൻഷ്യൽ പ്രൊജക്ഷൻ നോക്കും. ആദ്യ വർഷം മാസം തോറും, ഓരോ നമ്പറിനും കാരണം വേണം. നിങ്ങളുടെ പ്രൊജക്ഷൻ എഴുതിയോ?",
 cap_en="The investor asks Nikhil for three-year projections, and they only exist in his head. A data room needs written projections, month by month for year one, with a reason behind every number. Have you written yours down?",
 cap_mg="Data room-il investor moonnu varshathe financial projection nokkum. Aadya varsham maasam thorum, oro number-inum kaaranam venam. Ningalude projection ezhuthiyo?")

toon("drx04", "messy_docs", "B", {"A": "നിഖിൽ", "B": "അമ്മൂമ്മ", "C": "ദിവ്യ"}, "ഫൗണ്ടർമാർ രണ്ട്.\nഒപ്പിട്ട കരാർ\nഒന്നുമില്ല", [
 ("C", "നിഖിലേ, നീയും ദിവ്യയും ആണോ ഫൗണ്ടർമാർ? ഷെയർ എങ്ങനെ?"),
 ("A", "വാക്കാലുള്ള ധാരണ ഉണ്ട്. പേപ്പർ ഒന്നുമില്ല."),
 ("B", "ഇൻവെസ്റ്റർക്ക് വാക്കല്ല, ഒപ്പിട്ട കോ-ഫൗണ്ടർ കരാറും ക്യാപ് ടേബിളും വേണം. ഇല്ലെങ്കിൽ ഡ്യൂ ഡിലിജൻസിൽ റെഡ് ഫ്ലാഗ്.")],
 dict(title="ഡ്യൂ ഡിലിജൻസ്", rows=[("കോ-ഫൗണ്ടർ കരാർ", "ഒപ്പിട്ടത്"), ("ക്യാപ് ടേബിൾ", "രേഖയുമായി ചേരണം"), ("വെസ്റ്റിംഗ്", "എഴുതിയത്")], total=("വാക്കാലുള്ള ധാരണ", "പോരാ")),
 ["ഫണ്ടിംഗിന് മുമ്പ് കോ-ഫൗണ്ടർ കരാർ ഒപ്പിടുക.", "ക്യാപ് ടേബിൾ ഷെയർ രേഖകളുമായി ഒത്തുനോക്കുക."],
 "വാക്ക് പോരാ,\nഒപ്പ് വേണം", CTA_DILIGENCE, mentor="B", series=SER, ep=4, next="GST, ROC ഫയലിംഗ് പെൻഡിംഗ്", scene="teashop", theme="crm",
 cap_ml="രണ്ട് ഫൗണ്ടർമാർ, ഒപ്പിട്ട കരാർ ഇല്ല: ഡ്യൂ ഡിലിജൻസിൽ ഇത് റെഡ് ഫ്ലാഗ് ആണ്. ഒപ്പിട്ട കോ-ഫൗണ്ടർ കരാറും ശരിയായ ക്യാപ് ടേബിളും ഡാറ്റ റൂമിൽ വേണം. നിങ്ങളുടെ കരാർ ഒപ്പിട്ടോ?",
 cap_en="Two founders, a verbal deal and no signed agreement: in due diligence that's a red flag. A data room needs a signed co-founder agreement and a cap table that matches the share records. Is yours signed?",
 cap_mg="Randu founders, oppitta karaar illa: due diligence-il ithu red flag aanu. Oppitta co-founder agreement-um shariyaaya cap table-um data room-il venam. Ningalude karaar oppitto?")
