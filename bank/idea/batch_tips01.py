# Idea validation tips 01 (28 Nov), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALIDATE, CTA_IDEA = topics.CTA_VALIDATE, topics.CTA_IDEA

duo('ivt001', 'build_first', 'A', 'metro', 'ഐഡിയ ടെസ്റ്റ്:\n5 നമ്പർ\nമാത്രം എഴുതൂ', [('A', 'wide', 'കിരണേ, ഐഡിയ ടെസ്റ്റ് ചെയ്യുമ്പോൾ എന്തൊക്കെ എഴുതണം?'), ('V', 'V', 'അഞ്ജലീ, അഞ്ച് നമ്പർ മതി. ഓർഡർ, ഓർഡറിലെ വരുമാനം, പരസ്യ ചെലവ്.'), ('A', 'A', 'ബാക്കി രണ്ട്?'), ('V', 'V', 'ഒരു കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ്, വീണ്ടും വാങ്ങിയവർ.'), ('A', 'wide', 'ഈ അഞ്ചും എല്ലാ ആഴ്ചയും നോക്കിയാൽ തീരുമാനം എളുപ്പം.'), ('V', 'wide', 'അഞ്ച് നമ്പർ, ഒരു തീരുമാനം.')],
 'അഞ്ച് നമ്പർ,\nഒരു തീരുമാനം', CTA_VALIDATE, theme='tip',
 cap_ml='ഐഡിയ ടെസ്റ്റ് ചെയ്യുമ്പോൾ അഞ്ച് നമ്പർ എഴുതൂ: ഓർഡറുകൾ, ഓർഡറിലെ വരുമാനം, പരസ്യ ചെലവ്, ഒരു കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ്, വീണ്ടും വാങ്ങിയവർ. നിങ്ങൾ ഏതൊക്കെ എഴുതുന്നുണ്ട്?',
 cap_en='Testing an idea? Track five numbers every week: orders, earnings per order, ad spend, cost to win each customer, and repeat buyers. Which of these are you tracking?',
 cap_mg='Idea test cheyyumbol anchu number ezhuthu: orders, order-ile varumaanam, ad chelavu, oru customer-e kittaanulla chelavu, veendum vaangiyavar. Ningal ethokke ezhuthunnundu?')

duo('ivt002', 'side_project', 'B', 'home', 'ആദ്യം എന്ത്,\nപിന്നെ എന്ത്:\nപുതിയ ഐഡിയ', [('A', 'wide', 'അരുണേ, പുതിയ ഐഡിയയ്ക്ക് ആദ്യം എന്താണ് ചെയ്യേണ്ടത്?'), ('V', 'V', 'സ്നേഹേ, ആദ്യം ഡിമാൻഡ് ടെസ്റ്റ്. പിന്നെ പ്രൊപ്രൈറ്റർഷിപ്പും ഉദ്യമും.'), ('A', 'A', 'ആപ്പ് എപ്പോൾ?'), ('V', 'V', 'ഡിമാൻഡ് തെളിഞ്ഞ ശേഷം. ഇൻവെസ്റ്റർ വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡും വാല്യുവേഷനും.'), ('A', 'wide', 'ക്രമം തെറ്റിയാൽ പണം പോകും.'), ('V', 'wide', 'ക്രമം ശരിയാക്കൂ.')],
 'ക്രമം\nശരിയാക്കൂ', CTA_IDEA, theme='tip',
 cap_ml='പുതിയ ഐഡിയയ്ക്ക് ശരിയായ ക്രമം: ഡിമാൻഡ് ടെസ്റ്റ്, പ്രൊപ്രൈറ്റർഷിപ്പും ഉദ്യമും, ഡിമാൻഡ് തെളിഞ്ഞ ശേഷം ആപ്പ്, ഇൻവെസ്റ്റർ വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡും വാല്യുവേഷനും. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='The money-saving order for a new idea: test demand, start as a proprietorship with Udyam, build the app after demand is proven, then a private limited company and a valuation when investors come in. Which step are you on?',
 cap_mg='Puthiya idea-kku shariyaaya kramam: demand test, proprietorship-um Udyam-um, demand theliyunna sesham app, investor varumbol private limited-um valuation-um. Ningal ethu ghattathilaanu?')

duo('ivt003', 'marketplace_idea', 'A', 'hospital', 'മാർക്കറ്റ്പ്ലേസ്\nഐഡിയ? ആദ്യം\nകൈകൊണ്ട്', [('A', 'wide', 'ജോസഫേ, വാങ്ങുന്നവരെയും ഉണ്ടാക്കുന്നവരെയും ബന്ധിപ്പിക്കുന്ന ഒരു പ്ലാറ്റ്ഫോം ആണ് ഐഡിയ.'), ('V', 'V', 'ലക്ഷ്മീ, ആദ്യം പ്ലാറ്റ്ഫോം വേണ്ട. ഇൻസ്റ്റഗ്രാമിൽ കാണിച്ച് ഓർഡർ കിട്ടിയാൽ നിങ്ങൾ തന്നെ ബന്ധിപ്പിക്കുക.'), ('A', 'A', 'അത് വലിയ ജോലിയല്ലേ?'), ('V', 'V', 'അതാണ് പഠനം. ഏത് വശത്താണ് പ്രശ്നം എന്ന് കൃത്യമായി മനസ്സിലാകും.'), ('A', 'wide', 'പിന്നെ ഉണ്ടാക്കുന്ന പ്ലാറ്റ്ഫോം ശരിയായിരിക്കും.'), ('V', 'wide', 'പ്ലാറ്റ്ഫോമിന് മുമ്പ് പ്രക്രിയ.')],
 'പ്ലാറ്റ്ഫോമിന് മുമ്പ്\nപ്രക്രിയ', CTA_VALIDATE, theme='tip',
 cap_ml='മാർക്കറ്റ്പ്ലേസ് ഐഡിയയ്ക്ക് ആദ്യം പ്ലാറ്റ്ഫോം വേണ്ട. ഇൻസ്റ്റഗ്രാമിൽ കാണിച്ച് ആദ്യ ഓർഡറുകൾ കൈകൊണ്ട് ബന്ധിപ്പിക്കൂ. അങ്ങനെ എന്ത് ഉണ്ടാക്കണം എന്ന് കൃത്യമായി അറിയാം. നിങ്ങളുടെ ആദ്യ ഓർഡർ എപ്പോൾ?',
 cap_en="Planning a marketplace? Skip the platform at first: show products on Instagram and connect the first buyers and makers by hand. You'll learn exactly what the platform needs to do. When is your first order?",
 cap_mg='Marketplace idea-kku aadyam platform venda. Instagram-il kaanichu aadya orders kai kondu bandhippikku. Angane enthu undaakkanam ennu krithyamaayi ariyaam. Ningalude aadya order eppol?')

