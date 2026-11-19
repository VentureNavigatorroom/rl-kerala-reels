# Tips and tricks 02 (20 Nov, refill to 10 tips). theme="tip". Facts only from topics.FACTS_NDA. No fees, no court promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

lst('ndt004', 'agency_client', "B", 'NDA ലംഘിച്ചാൽ?\nആദ്യം ഈ 3 സ്റ്റെപ്പ്', [('കരാർ എടുക്കൂ', 'ലംഘിച്ചാൽ എന്ത് പരിഹാരം എന്ന് എഴുതിയിട്ടുണ്ടോ എന്ന് നോക്കൂ.'), ('തെളിവ് സൂക്ഷിക്കൂ', 'എന്ത് പങ്കുവെച്ചു, എപ്പോൾ എന്നതിന്റെ രേഖ.'), ('വേഗം നീങ്ങൂ', 'ഉപയോഗം തടയാൻ ഇൻജങ്ഷൻ ചോദിക്കാം, വക്കീലിനോട് ഉടൻ.')],
 'വൈകിയാൽ രഹസ്യം\nപരക്കും', CTA_NDA, theme="tip",
 cap_ml='NDA ലംഘിച്ചാൽ ആദ്യം കരാറിലെ പരിഹാരം നോക്കൂ, തെളിവ് സൂക്ഷിക്കൂ. ഉപയോഗം തടയാൻ ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം ചോദിക്കാം. നിങ്ങളുടെ NDA-യിൽ പരിഹാരം എഴുതിയിട്ടുണ്ടോ?',
 cap_en='If someone breaks your NDA: check the remedy clause, keep proof of what you shared and when, and move fast; an injunction can be sought to stop the use. Does your NDA name a remedy?',
 cap_mg='NDA lamghichaal aadyam karaarile remedy nokku, theliv sookshikku. Upayogam thadayaan injunction chodikkaam. Ningalude NDA-yil remedy undo?')

lst('ndt005', 'freelancer_nda', "B", 'NDA ഒപ്പിട്ടോ?\nകലണ്ടറിൽ ഇടേണ്ട\n3 കാര്യം', [('ഒപ്പിട്ട തീയതി', 'എന്ന് മുതൽ രഹസ്യം സൂക്ഷിക്കണം.'), ('അവസാന തീയതി', 'NDA-യിൽ എഴുതിയ കാലാവധി എന്ന് തീരും.'), ('പുതിയ വിവരം', 'കാലാവധി തീരാറായാൽ പുതിയത് പങ്കുവെക്കും മുമ്പ് പുതുക്കൂ.')],
 'രഹസ്യത്തിനും\nഒരു തീയതി ഉണ്ട്', CTA_NDA, theme="tip",
 cap_ml='ഓരോ NDA-യ്ക്കും കാലാവധി ഉണ്ട്. ഒപ്പിട്ട തീയതിയും അവസാന തീയതിയും കലണ്ടറിൽ ഇടൂ. നിങ്ങളുടെ NDA എത്ര കാലത്തേക്കാണ്?',
 cap_en='Every NDA has a duration. Put the signing date and the end date in your calendar, and renew before sharing anything new near the end. How long is your NDA?',
 cap_mg='Oro NDA-kkum kaalavadhi und. Oppitta date-um avasaana date-um calendar-il idu. Ningalude NDA ethra kaalathekkaanu?')

lst('ndt006', 'founder_pitching', "B", 'ആദ്യ പിച്ച് ഡെക്കിൽ\nഇടരുതാത്ത 3 കാര്യം', [('സോഴ്സ് കോഡ്', 'പ്രശ്നവും പരിഹാരവും പറയാം, കോഡ് വേണ്ട.'), ('ഫോർമുല, റെസിപ്പി', 'എന്ത് ചെയ്യുന്നു എന്ന് പറയൂ, എങ്ങനെ എന്ന് പിന്നീട്.'), ('കസ്റ്റമർ ലിസ്റ്റ്', 'എണ്ണം കാണിക്കാം, പേരുകൾ വേണ്ട.')],
 'ഡെക്കിൽ കഥ,\nരഹസ്യം പിന്നീട്', CTA_SECRET, theme="tip",
 cap_ml='പല ഇൻവെസ്റ്റർമാരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. അതുകൊണ്ട് ആദ്യ ഡെക്കിൽ കോഡും ഫോർമുലയും കസ്റ്റമർ പേരുകളും വേണ്ട. നിങ്ങളുടെ ഡെക്കിൽ ഇതിൽ ഏതുണ്ട്?',
 cap_en="Many investors won't sign an NDA at pitch stage, so keep source code, formulas and customer names out of your first deck. Show the problem, the solution and the numbers. Which of these is in your deck?",
 cap_mg='Pala investors-um pitch stage-il NDA oppidaarilla. Aadya deck-il code-um formula-um customer perukalum venda. Ningalude deck-il ithil ethundu?')

lst('ndt007', 'vendor_supplier', "B", 'വാട്സ്ആപ്പ് വാക്കോ\nഒപ്പിട്ട NDA-യോ?\nഒരു താരതമ്യം', [('"ആരോടും പറയില്ല"', 'ഒരു വാക്ക് മാത്രം. എന്താണ് രഹസ്യം എന്ന് പോലും ഇല്ല.'), ('ശരിയായ NDA', 'രഹസ്യം, കാലാവധി, പരിഹാരം എഴുതിയ കരാർ.'), ('സ്റ്റാമ്പ്', 'സംസ്ഥാന സ്റ്റാമ്പ് നിയമപ്രകാരം ചെയ്താൽ ഇന്ത്യയിൽ നടപ്പാക്കാം.')],
 'വാക്ക് പറക്കും,\nകരാർ നിൽക്കും', CTA_NDA, theme="tip",
 cap_ml='"ആരോടും പറയില്ല" എന്ന വാട്സ്ആപ്പ് മെസേജ് NDA അല്ല. ശരിയായി എഴുതി സ്റ്റാമ്പ് ചെയ്ത NDA ഇന്ത്യയിൽ നടപ്പാക്കാവുന്ന കരാറാണ്. നിങ്ങളുടെ രഹസ്യം ഏതിലാണ്: വാക്കോ കരാറോ?',
 cap_en='"I won\'t tell anyone" on WhatsApp is not an NDA. A properly drafted NDA, stamped under the state\'s stamp law, is an enforceable contract in India. Which protects your secret: a promise or a contract?',
 cap_mg='"Aarodum parayilla" enna WhatsApp message NDA alla. Shariyaayi ezhuthi stamp cheytha NDA India-yil nadappaakkaavunna karaar aanu. Vaakko karaaro?')

lst('ndt008', 'employee_nda', "B", 'പുതിയ ജീവനക്കാരൻ:\nജോയിൻ ദിവസം\nNDA ചെക്ക്ലിസ്റ്റ്', [('ആക്സസിന് മുമ്പ്', 'ഡാറ്റ കാണും മുമ്പ് ഒപ്പിടണം.'), ('എന്താണ് രഹസ്യം', 'കസ്റ്റമർ ലിസ്റ്റ്, കോഡ്, പ്രോസസ്: പേരെടുത്ത് എഴുതൂ.'), ('എത്ര കാലം', 'ജോലി വിട്ട ശേഷവും എത്ര കാലം എന്ന് എഴുതൂ.')],
 'ഒന്നാം ദിവസം ഒപ്പ്,\nപിന്നെ പാസ്‌വേഡ്', CTA_NDA, theme="tip",
 cap_ml='പുതിയ ജീവനക്കാരന് ഡാറ്റ ആക്സസ് കൊടുക്കും മുമ്പ് NDA ഒപ്പിടുവിക്കൂ. എന്താണ് രഹസ്യം, ജോലി വിട്ട ശേഷം എത്ര കാലം എന്ന് വ്യക്തമായി എഴുതൂ. നിങ്ങളുടെ ടീമിൽ എല്ലാവരും ഒപ്പിട്ടോ?',
 cap_en='Get the NDA signed before a new employee gets data access. Name what is confidential and how long it lasts after they leave. Has everyone on your team signed?',
 cap_mg='Puthiya jeevanakkaaranu data access kodukkum mumpu NDA oppiduvikku. Enthaanu rahasyam, joli vitta shesham ethra kaalam ennu ezhuthu. Team-il ellaarum oppitto?')

lst('ndt009', 'freelancer_nda', "B", 'ക്ലയന്റ് NDA\nഅയച്ചോ? ഒപ്പിടും\nമുമ്പ് 3 ചോദ്യം', [('ആരുടെ രഹസ്യം?', 'അവരുടേത് മാത്രമോ, നിങ്ങളുടെ ടൂളുകളും ഉൾപ്പെടുമോ?'), ('ഒഴിവാക്കലുണ്ടോ?', 'പൊതുവായതും സ്വയം ഉണ്ടാക്കിയതും പുറത്താണോ?'), ('എത്ര കാലം?', 'കാലാവധി ഇല്ലെങ്കിൽ ചോദിച്ച് എഴുതിക്കൂ.')],
 'വായിച്ചിട്ട് ഒപ്പ്,\nഒപ്പിട്ടിട്ട് ദുഃഖം വേണ്ട', CTA_SECRET, theme="tip",
 cap_ml='ക്ലയന്റിന്റെ NDA ഒപ്പിടും മുമ്പ് മൂന്ന് ചോദ്യം: ആരുടെ രഹസ്യം, ഒഴിവാക്കലുകൾ ഉണ്ടോ, എത്ര കാലം. ഫ്രീലാൻസർമാർക്ക് ഇത് പ്രധാനം. നിങ്ങൾ അവസാനം ഒപ്പിട്ട NDA വായിച്ചിരുന്നോ?',
 cap_en="Freelancers, before signing a client's NDA ask three things: whose information is covered, are public and independently developed things excluded, and for how long. Did you read the last NDA you signed?",
 cap_mg='Client-nte NDA oppidum mumpu moonnu chodyam: aarude rahasyam, exclusions undo, ethra kaalam. Freelancers-nu ithu pradhaanam. Avasaanam oppitta NDA vaayichirunno?')

lst('ndt010', 'vendor_supplier', "B", 'സപ്ലയർക്ക്\nഡ്രോയിംഗ് അയക്കണോ?\nആദ്യം ഇത്', [('NDA ആദ്യം', 'ഫയൽ അയക്കും മുമ്പ് ഒപ്പിട്ട് സ്റ്റാമ്പ് ചെയ്യണം.'), ('പേരെടുത്ത് എഴുതൂ', 'ഏത് ഡ്രോയിംഗ്, ഏത് പ്രോസസ് രഹസ്യം എന്ന് NDA-യിൽ.'), ('ആവശ്യത്തിന് മാത്രം', 'ജോലിക്ക് വേണ്ട ഭാഗം മാത്രം അയക്കൂ.')],
 'അയച്ചത് തിരികെ\nവരില്ല', CTA_SECRET, theme="tip",
 cap_ml='സപ്ലയർക്ക് ഡിസൈനോ ഡ്രോയിംഗോ അയക്കും മുമ്പ് NDA ഒപ്പിടുവിക്കൂ, ഏതാണ് രഹസ്യം എന്ന് പേരെടുത്ത് എഴുതൂ. ആവശ്യമുള്ള ഭാഗം മാത്രം അയക്കൂ. നിങ്ങൾ എന്താണ് നിർമ്മിക്കുന്നത്?',
 cap_en='Before sending designs or drawings to a supplier, get an NDA signed that names exactly what is confidential, and send only the part the job needs. What do you manufacture?',
 cap_mg='Supplier-nu design-o drawing-o ayakkum mumpu NDA oppiduvikku. Ethaanu rahasyam ennu perueduthu ezhuthu. Aavashyamulla bhaagam maathram ayakku. Ningal enthaanu nirmikkunnathu?')
