# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

lst('iet001', 'first_exporter', "B", 'IEC: ഏപ്രിൽ മുതൽ\nജൂൺ വരെ\nഒരു ജോലി', [('എന്ത്', 'IEC ഓൺലൈനിൽ അപ്ഡേറ്റ് ചെയ്യുക.'), ('എപ്പോൾ', 'എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ.'), ('ഇല്ലെങ്കിൽ', 'ഡീആക്ടിവേറ്റ് ആകും.')],
 'കലണ്ടറിൽ ഇടൂ,\nഷിപ്പ്മെന്റ് രക്ഷിക്കൂ', CTA_IEC, theme="tip",
 cap_ml='IEC കാലഹരണപ്പെടില്ല, പക്ഷേ എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെ ഓൺലൈനിൽ അപ്ഡേറ്റ് ചെയ്യണം. ഇല്ലെങ്കിൽ ഡീആക്ടിവേറ്റ് ആകും. ഈ വർഷം ചെയ്തോ?',
 cap_en='Your IEC never expires, but update it online every year between April and June or it is deactivated. Did you do it this year?',
 cap_mg='IEC expire aakilla, pakshe ella varshavum April-June online update venam. Illenkil deactivate. Ee varsham cheytho?')

lst('iet002', 'importer', "B", 'IEC വേണോ\nവേണ്ടയോ? 3\nസാഹചര്യം', [('വിൽക്കാൻ ഇറക്കുമതി', 'വേണം.'), ('സ്വന്തം ഉപയോഗത്തിന്', 'വേണ്ട.'), ('സർവീസ് കയറ്റുമതി', 'ആനുകൂല്യം ക്ലെയിം ചെയ്യാൻ വേണം.')],
 'ആവശ്യം നോക്കി\nതീരുമാനിക്കൂ', CTA_IEC, theme="tip",
 cap_ml='ബിസിനസ് ആവശ്യത്തിന് ഇറക്കുമതിയും കയറ്റുമതിയും ചെയ്യാൻ IEC വേണം. സ്വന്തം ഉപയോഗത്തിന് വേണ്ട. സർവീസ് കയറ്റുമതിക്കാർക്ക് ആനുകൂല്യം ക്ലെയിം ചെയ്യാൻ വേണം. നിങ്ങൾ ഏതിൽ?',
 cap_en='IEC is needed to import or export goods for business, not for personal use, and service exporters need it to claim export benefits. Which case is yours?',
 cap_mg='Business-nu import, export cheyyaan IEC venam. Swantham upayogathinu venda. Service exporters-nu benefits claim cheyyaan venam. Ningal ethil?')

lst('iet003', 'spice_trade', "B", 'ഒരു PAN,\nഒരു IEC,\nപല ഉൽപ്പന്നം', [('ഒരു PAN', 'ഒരു IEC മാത്രം.'), ('പത്ത് അക്കം', 'DGFT നൽകുന്ന കോഡ്.'), ('ട്രിക്ക്', 'ബിസിനസ് PAN-ൽ എടുക്കൂ, സ്വന്തം PAN-ൽ അല്ല.')],
 'ഒരു കോഡ് മതി\nഎല്ലാത്തിനും', CTA_EXPORT, theme="tip",
 cap_ml='ഒരു PAN-ന് ഒരു IEC മാത്രം, DGFT നൽകുന്ന 10 അക്ക കോഡ്. കയറ്റുമതി ചെയ്യുന്ന ബിസിനസിന്റെ PAN-ൽ എടുക്കൂ. നിങ്ങളുടെ IEC ആരുടെ PAN-ലാണ്?',
 cap_en="One PAN gets one IEC, a 10-digit code from DGFT. Take it on the exporting business's PAN. Whose PAN is your IEC on?",
 cap_mg='Oru PAN-nu oru IEC, DGFT kodukkunna 10 digit code. Export cheyyunna business-nte PAN-il edukku. Ningalude IEC aarude PAN-il?')

