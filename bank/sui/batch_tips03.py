# Tips and tricks 03 (20 Nov, writer run): keeps sui at 10+ unposted tips. theme="tip". Facts only from topics.FACTS_SUI. Never promise approval or a benefit.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

lst('ut011', 'investor_ready', "C", 'DPIIT-ന് 4 ഘടന.\nടാക്സ് ഹോളിഡേയ്ക്ക്\n2 മാത്രം', [('റെക്കഗ്നിഷൻ', 'പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, സഹകരണ സംഘം.'), ('80-IAC ടാക്സ് ഹോളിഡേ', 'പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കും മാത്രം, അതും വേറെ അപേക്ഷ.'), ('ഘടന തിരഞ്ഞെടുക്കും മുമ്പ്', 'രണ്ടും വേണോ എന്ന് ഇപ്പോഴേ തീരുമാനിക്കൂ.')],
 'ഘടന ആദ്യം,\nഹോളിഡേ പിന്നെ', CTA_BENEFITS, theme="tip",
 cap_ml='DPIIT റെക്കഗ്നിഷന് പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്, സഹകരണ സംഘം എന്നിവയ്ക്ക് അപേക്ഷിക്കാം. പക്ഷേ 80-IAC ടാക്സ് ഹോളിഡേ പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കും മാത്രം, അതും ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡിന് വേറെ അപേക്ഷ. നിങ്ങളുടെ ഘടന ഏതാ?',
 cap_en='Four structures can apply for DPIIT recognition: private limited company, LLP, registered partnership and cooperative society. The section 80-IAC tax holiday is only for a private limited company or LLP, and it is a separate application to the Inter-Ministerial Board. Which structure is yours?',
 cap_mg='DPIIT recognition-nu private limited, LLP, registered partnership, cooperative society ennivaykku apekshikkaam. Pakshe 80-IAC tax holiday private limited-inum LLP-kkum maathram, athum Inter-Ministerial Board-nu vere apeksha. Ningalude ghadana ethaa?')
