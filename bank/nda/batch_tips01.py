# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

lst('ndt001', 'agency_client', "B", 'നല്ല NDA-യിൽ\nവേണ്ട 3\nകാര്യം', [('രഹസ്യം എന്ത്', 'വ്യക്തമായി നിർവചിക്കണം.'), ('എത്ര കാലം', 'കാലാവധി എഴുതണം.'), ('ലംഘിച്ചാൽ', 'ഇൻജങ്ഷൻ പോലുള്ള പരിഹാരം.')],
 'ഒപ്പിടും മുമ്പ്\nമൂന്നും നോക്കൂ', CTA_NDA, theme="tip",
 cap_ml='നല്ല NDA-യിൽ രഹസ്യ വിവരം എന്ത്, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത് പരിഹാരം എന്നിവ വ്യക്തമാകണം. നിങ്ങളുടെ NDA-യിൽ ഇവ മൂന്നും ഉണ്ടോ?',
 cap_en='A good NDA defines what is confidential, for how long, and the remedy, such as an injunction, if it is breached. Does yours have all three?',
 cap_mg='Nalla NDA-yil rahasyam enthu, ethra kaalam, lamghichaal enthu ennivavyaktham venam. Ningalude NDA-yil moonnum undo?')

lst('ndt002', 'founder_pitching', "B", 'NDA സംരക്ഷിക്കാത്ത\n3 കാര്യം', [('ഇതിനകം പൊതുവായത്', 'സംരക്ഷണം ഇല്ല.'), ('സ്വതന്ത്രമായി ഉണ്ടാക്കിയത്', 'ഒഴിവാക്കലാണ്.'), ('പിച്ച് ഘട്ടം', 'പല ഇൻവെസ്റ്റർമാരും ഒപ്പിടില്ല.')],
 'അറിഞ്ഞിരുന്നാൽ\nനിരാശ ഇല്ല', CTA_SECRET, theme="tip",
 cap_ml='ഇതിനകം പൊതുവായ വിവരവും സ്വതന്ത്രമായി വികസിപ്പിച്ചതും NDA കൊണ്ട് സംരക്ഷിക്കാനാവില്ല. പല ഇൻവെസ്റ്റർമാരും പിച്ച് ഘട്ടത്തിൽ NDA ഒപ്പിടാറില്ല. നിങ്ങൾ എന്താണ് സംരക്ഷിക്കാൻ ശ്രമിക്കുന്നത്?',
 cap_en="An NDA cannot protect what is already public or independently developed, and many investors won't sign one at pitch stage. What are you trying to protect?",
 cap_mg='Public aaya vivaravum swathanthramaayi undaakkiyathum NDA kondu samrakshikkaan pattilla. Pala investors-um pitch stage-il NDA oppidilla. Ningal enthaanu samrakshikkaan nokkunnathu?')

lst('ndt003', 'vendor_supplier', "B", 'വൺ-വേയോ\nമ്യൂച്വലോ?\n5 സെക്കൻഡ് ടെസ്റ്റ്', [('നിങ്ങൾ മാത്രം പങ്കുവെക്കുന്നു', 'വൺ-വേ NDA.'), ('രണ്ടുപേരും', 'മ്യൂച്വൽ NDA.'), ('ട്രിക്ക്', 'സംസ്ഥാന നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്യൂ.')],
 'ശരിയായ തരം,\nശരിയായ സ്റ്റാമ്പ്', CTA_NDA, theme="tip",
 cap_ml='ഒരു വശം മാത്രം രഹസ്യം പങ്കുവെക്കുമ്പോൾ വൺ-വേ NDA, രണ്ടുപേരും പങ്കുവെക്കുമ്പോൾ മ്യൂച്വൽ. സംസ്ഥാനത്തിന്റെ സ്റ്റാമ്പ് നിയമപ്രകാരം സ്റ്റാമ്പ് ചെയ്യണം. നിങ്ങളുടേത് ഏതാണ്?',
 cap_en="One side sharing secrets: one-way NDA. Both sides: mutual. Either way, stamp it under the state's stamp law. Which do you need?",
 cap_mg='Oru vasham maathram share cheyyumbol one-way NDA, randuperum aanel mutual. State stamp niyamam prakaaram stamp cheyyanam. Ningalkku ethu venam?')

