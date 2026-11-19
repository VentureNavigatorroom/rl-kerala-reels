# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

lst('vt001', 'founder_raising', "B", 'ഇൻവെസ്റ്റർ പണം:\n3 തീയതികൾ\nഓർക്കൂ', [('അറുപത് ദിവസം', 'പണം കിട്ടിയാൽ അതിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്യണം.'), ('പതിനഞ്ച് ദിവസം', 'അലോട്ട്മെന്റ് കഴിഞ്ഞ് PAS-3 ഫയൽ ചെയ്യണം.'), ('അതുവരെ', 'ആ പണം ഉപയോഗിക്കരുത്.')],
 'തീയതി തെറ്റിയാൽ\nപണം തിരികെ', CTA_FUNDING, theme="tip",
 cap_ml='ഇൻവെസ്റ്റർ പണം കിട്ടി 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്യണം, അല്ലെങ്കിൽ തിരികെ നൽകണം. അലോട്ട്മെന്റ് കഴിഞ്ഞ് 15 ദിവസത്തിനുള്ളിൽ PAS-3. ഈ തീയതികൾ നിങ്ങൾ കലണ്ടറിൽ ഇട്ടോ?',
 cap_en="Allot shares within 60 days of receiving investor money or refund it; file PAS-3 within 15 days of allotment, and don't use the money until then. Are these dates in your calendar?",
 cap_mg='Investor panam kittiyaal 60 divasathinullil share allot cheyyanam, allenkil thirike kodukkanam. 15 divasathinullil PAS-3. Ee dates calendar-il ittoo?')

lst('vt002', 'family_money', "B", 'ബന്ധുവിന്റെ പണം\nസ്വീകരിക്കും മുമ്പ്\nഒരു ട്രിക്ക്', [('സ്വന്തം അക്കൗണ്ട്', 'നിക്ഷേപകന്റെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന് മാത്രം.'), ('പ്രത്യേക അക്കൗണ്ട്', 'കമ്പനിയുടെ വേറെ അക്കൗണ്ടിലേക്ക്.'), ('രേഖ', 'ഷെയറും കരാറും ഫയലിംഗും.')],
 'ബന്ധുവായാലും\nരേഖ നിർബന്ധം', CTA_INVEST, theme="tip",
 cap_ml='സ്വകാര്യ പ്ലേസ്മെന്റിൽ പണം നിക്ഷേപകന്റെ സ്വന്തം അക്കൗണ്ടിൽ നിന്ന് കമ്പനിയുടെ പ്രത്യേക അക്കൗണ്ടിലേക്ക് മാത്രം. ബന്ധുവിന്റെ പണത്തിനും ഇത് ബാധകം. നിങ്ങൾ ഇങ്ങനെയാണോ സ്വീകരിച്ചത്?',
 cap_en="In a private placement, money must come from the investor's own bank account into a separate company account, even from family. Is that how you received it?",
 cap_mg='Private placement-il panam investor-nte swantham account-il ninnu company-yude separate account-ilekku maathram. Bandhuvinte panathinum ithu baadhakam. Ningal angane aano sweekarichathu?')

lst('vt003', 'angel', "B", 'ടേം ഷീറ്റ്:\nഒപ്പിട്ടാൽ ഉടനെ\nബാധകമാകുന്നവ', [('രഹസ്യാത്മകത', 'ഒപ്പിട്ട ദിവസം മുതൽ.'), ('നോ-ഷോപ്പ്', 'മറ്റൊരാളെ തേടാൻ പറ്റില്ല.'), ('ചെലവും നിയമവും', 'ആര് വഹിക്കും, ഏത് നിയമം.')],
 'ബാക്കി ബൈൻഡിംഗ് അല്ലെങ്കിലും\nഇവ ബാധകം', CTA_TERMSHEET, theme="tip",
 cap_ml='ടേം ഷീറ്റ് പൊതുവെ ബൈൻഡിംഗ് അല്ല, പക്ഷേ രഹസ്യാത്മകത, എക്സ്ക്ലൂസിവിറ്റി, ചെലവ്, ഗവേണിംഗ് നിയമം എന്നിവ ഒപ്പിടുമ്പോൾ തന്നെ ബാധകം. നിങ്ങളുടെ ടേം ഷീറ്റിൽ നോ-ഷോപ്പ് ഉണ്ടോ?',
 cap_en='A term sheet is mostly non-binding, but confidentiality, exclusivity, costs and governing law usually bind from signing. Does yours have a no-shop clause?',
 cap_mg='Term sheet mostly binding alla, pakshe confidentiality, exclusivity, cost, governing law sign cheyyumbol thanne baadhakam. Ningalude term sheet-il no-shop undo?')

