# IEC batch 07 (27 Nov night): service exports after FTP 2023 (SEIS gone; IEC on the date of service for FTP benefits). Facts only from topics.FACTS_IEC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo('ied060', 'service_export', 'A', 'office', '"വിദേശ ക്ലയന്റിന്\nസർവീസ് ചെയ്താൽ\n7% കിട്ടും!" ഇപ്പോഴോ?', [('A', 'wide', 'രാഹുലേ, ഒരു വീഡിയോയിൽ കണ്ടു. വിദേശത്തേക്ക് സർവീസ് ചെയ്താൽ സർക്കാർ 7% തരുമെന്ന്!'), ('V', 'V', 'നേഹ, അത് പഴയ SEIS സ്കീമാണ്. 2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ അത് നിർത്തി.'), ('A', 'A', 'അപ്പോ സർവീസിന് IEC വേണ്ടേ?'), ('V', 'V', 'നയത്തിലെ ആനുകൂല്യം വേണമെങ്കിൽ മാത്രം. പക്ഷേ സർവീസ് ചെയ്യുന്ന ദിവസം തന്നെ IEC കയ്യിൽ വേണം.'), ('A', 'wide', 'പിന്നെ എടുത്താൽ പഴയ ബില്ലുകൾക്ക് ഉപകാരപ്പെടില്ല.'), ('V', 'wide', 'ബിൽ അയക്കും മുമ്പ് കോഡ്.')],
 '7% പോയി.\nIEC ഇപ്പോഴും നേരത്തെ', CTA_IEC, theme='faq',
 cap_ml='വിദേശ ക്ലയന്റിന് സർവീസ് ചെയ്താൽ 7% കിട്ടുമെന്ന് പറയുന്നത് പഴയ SEIS സ്കീമാണ്; 2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ അത് നിർത്തി. നയത്തിലെ ആനുകൂല്യം വേണമെങ്കിൽ സർവീസ് ചെയ്യുന്ന ദിവസം തന്നെ IEC വേണം. നിങ്ങൾ വിദേശ ക്ലയന്റിന് ബിൽ ചെയ്യുന്നുണ്ടോ?',
 cap_en='A viral video says service exporters get 7% from the government. That was the old SEIS scheme, discontinued under the Foreign Trade Policy 2023. An IEC is still needed to take FTP benefits, and it must be held on the date you render the service. Do you bill foreign clients?',
 cap_mg='Videsha client-inu service cheythaal 7% kittum ennu parayunnathu pazhaya SEIS scheme aanu; 2023-le FTP-yil athu nirthi. FTP benefit venamenkil service cheyyunna divasam thanne IEC venam. Ningal videsha client-inu bill cheyyunnundo?')

duo('ied061', 'service_export', 'B', 'library', 'IEC എടുത്തത്\nആറ് മാസം\nകഴിഞ്ഞിട്ട്', [('A', 'wide', 'അനൂപേ, ആറ് മാസമായി ഗൾഫിലെ ക്ലയന്റിന് ഡിസൈൻ ചെയ്യുന്നു. ഇന്നലെ IEC എടുത്തു. പഴയ ജോലിക്കും ആനുകൂല്യം കിട്ടുമോ?'), ('V', 'V', 'ഗ്രീഷ്മേ, വിദേശ വ്യാപാര നയം പറയുന്നത് സർവീസ് ചെയ്യുന്ന ദിവസം IEC ഉണ്ടായിരിക്കണം എന്നാണ്.'), ('A', 'A', 'അപ്പോ കഴിഞ്ഞ ആറ് മാസം?'), ('V', 'V', 'ആ ദിവസങ്ങളിൽ IEC ഇല്ലായിരുന്നെങ്കിൽ ആ സേവനങ്ങൾക്ക് നയത്തിലെ ആനുകൂല്യം ചോദിക്കാൻ ബുദ്ധിമുട്ടാകും.'), ('A', 'wide', 'ഇനി മുതൽ എല്ലാം ശരിയാകും.'), ('V', 'wide', 'ആദ്യ ബില്ലിന് മുമ്പ് IEC.')],
 'ആദ്യ ബില്ലിന് മുമ്പ്\nIEC', CTA_EXPORT, theme='crm',
 cap_ml='വിദേശ ക്ലയന്റിന് സർവീസ് ചെയ്യുന്നവർക്ക് വിദേശ വ്യാപാര നയത്തിലെ ആനുകൂല്യം വേണമെങ്കിൽ സർവീസ് ചെയ്യുന്ന ദിവസം IEC ഉണ്ടായിരിക്കണം. ആദ്യ ബില്ലിന് മുമ്പ് എടുക്കൂ. നിങ്ങളുടെ ആദ്യ വിദേശ ക്ലയന്റ് എപ്പോൾ?',
 cap_en='She has designed for a Gulf client for six months and took her IEC yesterday. Under the Foreign Trade Policy 2023 the IEC must be held on the date the service is rendered to claim FTP benefits, so get it before your first foreign invoice. When did your first foreign client start?',
 cap_mg='Videsha client-inu service cheyyunnavarkku FTP benefit venamenkil service cheyyunna divasam IEC undaayirikkanam. Aadya bill-inu mumpu edukku. Ningalude aadya videsha client eppol?')

