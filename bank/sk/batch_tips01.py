# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

lst('mt001', 'idea_stage', "B", 'ഗ്രാന്റ് പണം\nകിട്ടാൻ വേണ്ട\nമൂന്ന് രേഖ', [('കമ്പനി', 'പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP, കേരളത്തിൽ.'), ('യുണീക്ക് ID', 'KSUM പോർട്ടലിൽ.'), ('DPIIT', 'പല കോളുകളും ചോദിക്കും.')],
 'പണം വരും മുമ്പ്\nഇവ വേണം', CTA_GRANT, theme="tip",
 cap_ml='KSUM ഗ്രാന്റിന് പലപ്പോഴും വേണ്ടത്: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP, യുണീക്ക് ID, DPIIT അംഗീകാരം. ഓരോ കോളും നോക്കൂ. ഇതിൽ എന്ത് ബാക്കി?',
 cap_en='KSUM grants often need a Kerala-registered private limited or LLP, the Unique ID and DPIIT recognition. Check each live call. Which is still pending for you?',
 cap_mg='KSUM grant-nu: Kerala-il register cheytha private limited allenkil LLP, Unique ID, DPIIT. Oro call-um nokku. Ethaanu baakki?')

lst('mt002', 'kerala_registered', "B", 'യുണീക്ക് ID:\nഒരു മിനിറ്റിൽ\nഅറിയേണ്ടത്', [('എന്താണ്', 'KSUM-ലെ സ്റ്റാർട്ടപ്പിന്റെ തിരിച്ചറിയൽ.'), ('എവിടെ', 'KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ.'), ('എന്തിന്', 'KSUM സ്കീമുകൾക്കും ഗ്രാന്റുകൾക്കും.')],
 'ID ആദ്യ പടി,\nതിരഞ്ഞെടുപ്പ് വേറെ', CTA_KSUM, theme="tip",
 cap_ml='KSUM യുണീക്ക് ID സ്റ്റാർട്ടപ്പിന്റെ തിരിച്ചറിയലാണ്. KSUM സ്കീമുകൾക്കും ഗ്രാന്റുകൾക്കും ഇത് വേണം. ഗ്രാന്റ് തിരഞ്ഞെടുപ്പ് വേറെയാണ്. നിങ്ങൾക്ക് ID ഉണ്ടോ?',
 cap_en="The KSUM Unique ID is your startup's identity for KSUM schemes and grants, applied for on the KSUM startup portal. Selection is separate. Do you have one?",
 cap_mg='KSUM Unique ID startup-nte thiricharivu. Schemes-num grants-num venam. Selection verae. Ningalkku ID undo?')

lst('mt003', 'campus', "B", 'ഐഡിയ ഗ്രാന്റ്:\nക്രമം തെറ്റിക്കരുത്', [('ഒന്ന്', 'കമ്പനിക്ക് മുമ്പും അപേക്ഷിക്കാം.'), ('രണ്ട്', 'പണത്തിന് മുമ്പ് കമ്പനി രജിസ്റ്റർ ചെയ്യണം.'), ('മൂന്ന്', 'യുണീക്ക് ID-യും എടുക്കണം.')],
 'അപേക്ഷ നേരത്തെ,\nകമ്പനി പണത്തിന് മുമ്പ്', CTA_GRANT, theme="tip",
 cap_ml='ഐഡിയ ഗ്രാന്റിന് കമ്പനിക്ക് മുമ്പും അപേക്ഷിക്കാം. പക്ഷേ പണം വിട്ടുകിട്ടാൻ കമ്പനിയും യുണീക്ക് ID-യും വേണം. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='You can apply for the idea grant before incorporating, but the company and the Unique ID are needed before money is released. Which step are you at?',
 cap_mg='Idea grant-nu company-kku mumpum apply cheyyaam, pakshe panam kittaan company-yum Unique ID-yum venam. Ningal etha step-il?')

