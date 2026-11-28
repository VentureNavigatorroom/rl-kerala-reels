# IEC tips 05 (28 Nov night): one tip as a duo3d scene, theme="tip" (the topic's other tip angles are already used by iet001-iet020).
# Status Holders under FTP 2023. Facts only from topics.FACTS_IEC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo('iet021', 'first_exporter', 'A', 'airport', '"സ്റ്റാറ്റസ് ഹോൾഡർ"\nഎന്ന് കേട്ടോ?\n20 സെക്കൻഡിൽ', [
 ('A', 'wide', 'റഫീഖേ, ഇന്നലത്തെ എക്സ്പോർട്ടർ മീറ്റിൽ ഒരാൾ പറഞ്ഞു, അയാൾ സ്റ്റാറ്റസ് ഹോൾഡർ ആണെന്ന്. അതെന്താ?'),
 ('V', 'V', 'ഷമീറേ, 2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ ഉയർന്ന കയറ്റുമതി നടത്തുന്നവർക്ക് കിട്ടുന്ന അംഗീകാരം. ചില പ്രത്യേക സൗകര്യങ്ങളും ഉണ്ട്.'),
 ('A', 'A', 'IEC എടുത്ത ഉടനെ അത് കിട്ടുമോ?'),
 ('V', 'V', 'ഇല്ല. IEC തുടക്കം മാത്രം, പദവി കയറ്റുമതി വളരുമ്പോൾ. അതുവരെ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂണിൽ IEC അപ്ഡേറ്റ് ചെയ്യുക.'),
 ('A', 'wide', 'ആദ്യം കോഡ്, പിന്നെ കയറ്റുമതി, പിന്നെ പദവി.'),
 ('V', 'wide', 'കോഡ് തുടക്കം, പദവി സമ്പാദ്യം.')],
 'കോഡ് തുടക്കം,\nപദവി സമ്പാദ്യം', CTA_EXPORT, theme='tip',
 cap_ml='2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ ഉയർന്ന കയറ്റുമതി നടത്തുന്നവരെ സ്റ്റാറ്റസ് ഹോൾഡർ ആയി അംഗീകരിക്കും, ചില പ്രത്യേക സൗകര്യങ്ങളോടെ. IEC എടുത്താൽ ഉടൻ കിട്ടുന്നതല്ല; അതുവരെ IEC വർഷം തോറും ഏപ്രിൽ-ജൂണിൽ അപ്ഡേറ്റ് ചെയ്ത് ആക്ടീവ് ആക്കി വെക്കൂ. നിങ്ങളുടെ കയറ്റുമതി ഏത് ഘട്ടത്തിൽ?',
 cap_en='Under the Foreign Trade Policy 2023, high export performers can be recognised as Status Holders, with certain privileges. It does not come with the IEC itself: the IEC is only the start, so keep it active by updating it every year between April and June. What stage is your export business at?',
 cap_mg='2023-le FTP-yil uyarnna export nadathunnavare Status Holder aayi angeekarikkum, chila prathyeka saukaryangalodu koode. IEC eduthaal udan kittunnathalla; athuvare IEC varsham thorum April-June-il update cheythu active aakki vekkoo. Ningalude export ethu ghattathil?')
