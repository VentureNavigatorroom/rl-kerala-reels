# IEC tips 04 (27 Nov night): service export rule, theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

duo('iet020', 'service_export', 'A', 'rooftop', 'സർവീസ് കയറ്റുമതി:\nIEC എപ്പോൾ വേണം,\nഎപ്പോൾ വേണ്ട', [('A', 'wide', 'ശ്യാമേ, വിദേശ ക്ലയന്റിന് ജോലി ചെയ്യാൻ മാത്രം IEC വേണോ?'), ('V', 'V', 'ആര്യേ, വേണ്ട. പണം വാങ്ങാനും ജോലി ചെയ്യാനും IEC നിർബന്ധമല്ല.'), ('A', 'A', 'പിന്നെ എപ്പോൾ?'), ('V', 'V', 'വിദേശ വ്യാപാര നയത്തിലെ ആനുകൂല്യം എടുക്കുമ്പോൾ. അതിന് സർവീസ് ചെയ്യുന്ന ദിവസം IEC വേണം.'), ('A', 'wide', 'പഴയ 7% സ്കീം ഇപ്പോൾ ഇല്ല എന്നും ഓർക്കണം.'), ('V', 'wide', 'ആനുകൂല്യത്തിന് IEC, ജോലിക്ക് വേണ്ട.')],
 'ആനുകൂല്യത്തിന് IEC,\nജോലിക്ക് വേണ്ട', CTA_IEC, theme='tip',
 cap_ml='സർവീസ് കയറ്റുമതിക്ക് IEC നിർബന്ധം വിദേശ വ്യാപാര നയത്തിലെ ആനുകൂല്യം എടുക്കുമ്പോൾ മാത്രം; അതിന് സർവീസ് ചെയ്യുന്ന ദിവസം IEC വേണം. പഴയ 7% SEIS ഇപ്പോൾ ഇല്ല. നിങ്ങൾ ഏത് സർവീസാണ് വിദേശത്തേക്ക് ചെയ്യുന്നത്?',
 cap_en='For service exports, an IEC is required only when you take benefits under the Foreign Trade Policy, and then it must be held on the date the service is rendered. The old 7% SEIS incentive no longer exists. What service do you provide abroad?',
 cap_mg='Service export-inu IEC nirbandham FTP benefit edukkumbol maathram; athinu service cheyyunna divasam IEC venam. Pazhaya 7% SEIS ippol illa. Ningal ethu service aanu videshathekku cheyyunnathu?')

