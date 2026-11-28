# contract tips 01 (28 Nov night), theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_CONTRACT, CTA_VENDOR = topics.CTA_CONTRACT, topics.CTA_VENDOR

duo('kct001', 'freelance_service', 'B', 'metro', 'ഏത് ബിസിനസ്\nകരാറിലും\n7 കാര്യം', [('A', 'wide', 'കിരണേ, ഏത് കരാറിലും നിർബന്ധമായും എന്തൊക്കെ വേണം?'), ('V', 'V', 'അഞ്ജലീ, ആരൊക്കെ കക്ഷികൾ, കൃത്യമായ സ്കോപ്പ്, വിലയും പേയ്മെന്റും.'), ('A', 'A', 'പിന്നെ?'), ('V', 'V', 'ഡെലിവറി, ജോലിയുടെ ഉടമസ്ഥത, രഹസ്യസ്വഭാവം, ടെർമിനേഷനും തർക്കപരിഹാരവും.'), ('A', 'wide', 'അവസാനം ശരിയായ സ്റ്റാമ്പും ഒപ്പും.'), ('V', 'wide', 'ഏഴ് കാര്യം, ഒരു സുരക്ഷ.')],
 'ഏഴ് കാര്യം,\nഒരു സുരക്ഷ', CTA_CONTRACT, theme='tip',
 cap_ml='ഏത് ബിസിനസ് കരാറിലും 7 കാര്യം: കക്ഷികൾ, സ്കോപ്പ്, വിലയും പേയ്മെന്റും, ഡെലിവറി, ജോലിയുടെ ഉടമസ്ഥത, രഹസ്യസ്വഭാവം, ടെർമിനേഷനും തർക്കപരിഹാരവും. പിന്നെ ശരിയായ സ്റ്റാമ്പ്. നിങ്ങളുടെ കരാറിൽ എത്ര ഉണ്ട്?',
 cap_en='Every business contract needs seven things: the parties, scope, payment terms, delivery, who owns the work, confidentiality, and termination with dispute terms, plus proper stamping. How many does yours have?',
 cap_mg='Ethu business karaarilum 7 kaaryam: parties, scope, vilayum payment-um, delivery, jolliyude udamastatha, confidentiality, termination-um dispute-um. Pinne shariyaaya stamp. Ningalude karaaril ethra undu?')

