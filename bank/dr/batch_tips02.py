# Data room tips 02 (28 Nov night): tip reels as duo scenes, theme="tip". Facts only from topics.FACTS_DR. No fees, no promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE

# tip: the five red flags to check yourself before an investor does
duo('drt004', 'raising_first', 'A', 'akshaya', 'ഇൻവെസ്റ്റർ കാണും മുമ്പ്\n5 റെഡ് ഫ്ലാഗ്\nനിങ്ങൾ തന്നെ നോക്കൂ', [
 ('A', 'wide', 'രമേശേ, ഇൻവെസ്റ്ററെ കാണും മുമ്പ് അഞ്ച് ചോദ്യം സ്വയം ചോദിക്കൂ.'),
 ('A', 'A', 'ഒന്ന്: ROC, GST ഫയലിംഗ് എന്തെങ്കിലും പെൻഡിംഗ് ഉണ്ടോ? രണ്ട്: കോ-ഫൗണ്ടർ കരാർ ഒപ്പിട്ടോ?'),
 ('V', 'V', 'മൂന്ന്: ക്യാപ് ടേബിളും ഷെയർ രേഖയും ചേരുന്നുണ്ടോ? നാല്: പ്രൊജക്ഷൻ എഴുതിയോ?'),
 ('A', 'A', 'അഞ്ച്: ബ്രാൻഡ് ട്രേഡ്മാർക്ക് ചെയ്ത് സംരക്ഷിച്ചോ? ഒന്നിന് ഇല്ല എന്നാണെങ്കിൽ അത് ആദ്യം ശരിയാക്കൂ.'),
 ('V', 'wide', 'അവർ കണ്ടുപിടിക്കും മുമ്പ്, നമ്മൾ തിരുത്തണം.')],
 'അവർ കണ്ടുപിടിക്കും മുമ്പ്\nനിങ്ങൾ തിരുത്തൂ', CTA_DILIGENCE, theme='tip',
 cap_ml='ഡ്യൂ ഡിലിജൻസിലെ 5 റെഡ് ഫ്ലാഗ്: പെൻഡിംഗ് ROC, GST ഫയലിംഗ്; ഒപ്പിടാത്ത കോ-ഫൗണ്ടർ കരാർ; ഷെയർ രേഖയുമായി ചേരാത്ത ക്യാപ് ടേബിൾ; പ്രൊജക്ഷൻ ഇല്ല; ബ്രാൻഡ് സംരക്ഷിച്ചിട്ടില്ല. നിങ്ങൾക്ക് എത്ര എണ്ണം ടിക്ക് ചെയ്യാം?',
 cap_en="Five due diligence red flags to check yourself before an investor does: pending ROC or GST filings, no signed co-founder agreement, a cap table that doesn't match share records, no projections, and an unprotected brand. How many can you tick?",
 cap_mg='Due diligence-ile 5 red flag: pending ROC, GST filing; oppidaatha co-founder agreement; share rekhayumaayi cheraatha cap table; projection illa; brand samrakshichittilla. Ningalkku ethra ennam tick cheyyaam?')

# tip: the first file in the data room is an index of folders, with what is in and what is pending
duo('drt005', 'messy_docs', 'B', 'railway', 'ഡാറ്റ റൂമിലെ\nആദ്യ ഫയൽ:\nഒരു ലിസ്റ്റ്', [
 ('A', 'wide', 'ദിനേശേ, ഡാറ്റ റൂം തുറക്കുന്ന ഇൻവെസ്റ്റർ ആദ്യം എന്ത് കാണണം എന്ന് അറിയാമോ?'),
 ('V', 'V', 'ഷീബേ, പിച്ച് ഡെക്ക് അല്ലേ?'),
 ('A', 'A', 'അതിനും മുമ്പ് ഒരു ലിസ്റ്റ്. ഏതൊക്കെ ഫോൾഡർ, ഓരോന്നിലും എന്ത്, എന്ത് പെൻഡിംഗ്.'),
 ('V', 'V', 'പെൻഡിംഗ് എന്ന് എഴുതിയാൽ മോശമല്ലേ?'),
 ('A', 'wide', 'ഒളിച്ചുവെച്ചത് അവർ കണ്ടുപിടിച്ചാൽ സംശയം. നേരത്തെ നമ്മൾ പറഞ്ഞാൽ വിശ്വാസം.'),
 ('V', 'wide', 'ആദ്യം ലിസ്റ്റ്, പിന്നെ ഫോൾഡർ.')],
 'ആദ്യം ലിസ്റ്റ്,\nപിന്നെ ഫോൾഡർ', CTA_DATAROOM, theme='tip',
 cap_ml='ഡാറ്റ റൂമിലെ ആദ്യ ഫയൽ ഒരു ലിസ്റ്റ് ആകട്ടെ: ഏതൊക്കെ ഫോൾഡർ, ഓരോന്നിലും എന്ത്, എന്ത് പെൻഡിംഗ്. ഇൻവെസ്റ്റർ തിരഞ്ഞ് സമയം കളയില്ല. നിങ്ങളുടെ ഫോൾഡറിന് ഒരു ലിസ്റ്റുണ്ടോ?',
 cap_en="Make the first file in your data room an index: which folders exist, what is inside each and what is still pending. Investors stop hunting, and a pending item said openly beats one they find. Does your folder have an index?",
 cap_mg="Data room-ile aadya file oru list aakatte: ethokke folder, oronnilum enthu, enthu pending. Investor thiranju samayam kalayilla. Ningalude folder-inu oru list undo?")

# tip: add each month's GST returns and bank statements so the data room never goes stale
duo('drt006', 'investor_asked', 'A', 'kitchen', 'ഡാറ്റ റൂം ഒരിക്കൽ\nഉണ്ടാക്കി. ആറ് മാസം\nതൊട്ടിട്ടില്ല', [
 ('A', 'wide', 'രാജേഷേ, ആറ് മാസം മുമ്പ് ഉണ്ടാക്കിയ ഡാറ്റ റൂം ലിങ്ക് ഇന്ന് ഒരു ഇൻവെസ്റ്റർക്ക് അയക്കാൻ പോകുവാ.'),
 ('V', 'V', 'ബിന്ദൂ, നിൽക്ക്. അതിലെ ബാങ്ക് സ്റ്റേറ്റ്മെന്റും GST റിട്ടേണും ആറ് മാസം പഴയതല്ലേ?'),
 ('A', 'A', 'ശരിയാ. ക്യാപ് ടേബിളും പിന്നെ മാറിയിട്ടുണ്ട്.'),
 ('V', 'V', 'എല്ലാ മാസവും ഒരു പത്ത് മിനിറ്റ്: പുതിയ റിട്ടേൺ, സ്റ്റേറ്റ്മെന്റ്, പുതിയ കരാർ ഫോൾഡറിൽ ഇടുക.'),
 ('A', 'wide', 'പഴയ ഫോൾഡർ പഴയ കഥ പറയും.'),
 ('V', 'wide', 'മാസം ഒരിക്കൽ, ഫോൾഡർ പുതുക്കണം.')],
 'മാസം ഒരിക്കൽ\nഫോൾഡർ പുതുക്കൂ', CTA_DATAROOM, theme='tip',
 cap_ml='ഡാറ്റ റൂം ഒരിക്കൽ ഉണ്ടാക്കിയാൽ പോരാ. എല്ലാ മാസവും പുതിയ GST റിട്ടേൺ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, കരാറുകൾ, ക്യാപ് ടേബിൾ മാറ്റം ഫോൾഡറിൽ ഇടൂ. നിങ്ങളുടെ ഫോൾഡർ അവസാനം പുതുക്കിയത് എപ്പോൾ?',
 cap_en="A data room built once and left alone goes stale: old bank statements, old GST returns, an outdated cap table. Give it ten minutes a month to add the new returns, statements and agreements. When did you last update yours?",
 cap_mg='Data room orikkal undaakkiyaal poraa. Ella maasavum puthiya GST return, bank statement, karaarukal, cap table maattam folder-il idu. Ningalude folder avasaanam puthukkiyathu eppol?')

# tip: open the link the way the investor will, before sending it
duo('drt007', 'investor_asked', 'B', 'autostand', 'ലിങ്ക് അയച്ചു.\nഇൻവെസ്റ്റർ പറഞ്ഞു:\n"ഒന്നും തുറക്കുന്നില്ല"', [
 ('A', 'wide', 'ഷാജീ, ഇന്നലെ ഡാറ്റ റൂം ലിങ്ക് അയച്ചു. ഇൻവെസ്റ്റർ പറയുന്നു, ഒന്നും തുറക്കുന്നില്ല എന്ന്!'),
 ('V', 'V', 'സജീ, അയക്കും മുമ്പ് വേറൊരു ഫോണിൽ, ലോഗിൻ ചെയ്യാതെ, ഒന്ന് തുറന്നു നോക്കിയോ?'),
 ('A', 'A', 'ഇല്ല. എന്റെ ഫോണിൽ എല്ലാം തുറക്കുന്നുണ്ടായിരുന്നു.'),
 ('V', 'V', 'അതാണ് കാര്യം. അവർ കാണുന്നതുപോലെ നോക്കണം: ഫോൾഡർ തുറക്കുന്നുണ്ടോ, ഫയൽ വായിക്കാമോ, അവർക്ക് കാണേണ്ടത് മാത്രം കാണുന്നുണ്ടോ.'),
 ('A', 'wide', 'നമുക്ക് തുറന്നാൽ പോരാ, അവർക്ക് തുറക്കണം.')],
 'അയക്കും മുമ്പ്\nഅവരുടെ കണ്ണിൽ നോക്കൂ', CTA_DATAROOM, theme='tip',
 cap_ml='ഡാറ്റ റൂം ലിങ്ക് അയക്കും മുമ്പ് വേറൊരു ഫോണിൽ, ലോഗിൻ ചെയ്യാതെ തുറന്നു നോക്കൂ: ഫോൾഡർ തുറക്കുന്നുണ്ടോ, ഫയൽ വായിക്കാമോ, കാണേണ്ടത് മാത്രം കാണുന്നുണ്ടോ. നിങ്ങൾ അവസാനം ഇങ്ങനെ ടെസ്റ്റ് ചെയ്തത് എപ്പോൾ?',
 cap_en="The data room link went out and the investor says nothing opens. Before you send it, open it on another phone, logged out: do the folders open, can the files be read, and does the viewer see only what they should? Have you tested yours?",
 cap_mg='Data room link ayakkum mumbu veroru phone-il, login cheyyaathe thurannu nokku: folder thurakkunnundo, file vaayikkaamo, kaanendathu maathram kaanunnundo. Ningal avasaanam ingane test cheythathu eppol?')
