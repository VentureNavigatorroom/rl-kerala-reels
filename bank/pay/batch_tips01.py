# Pay tips 01 (27 Nov): tip reels as duo3d scenes (not lists), theme="tip". Facts only from topics.FACTS_PAY. No fees, no promised incentive.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ESIC, CTA_PAYROLL = topics.CTA_ESIC, topics.CTA_PAYROLL

duo("pyt001", "ten_staff", "B", "bakery", "ശമ്പളം കൊടുക്കും മുമ്പ്\nഒരു മിനിറ്റ്:\n2 എണ്ണം നോക്കൂ", [
 ("A","wide","സാബുച്ചേട്ടാ, ഓരോ മാസവും ശമ്പളം കൊടുക്കും മുമ്പ് ഞാൻ രണ്ട് എണ്ണം നോക്കും."),
 ("V","V","ഏതൊക്കെ, ജിഷേ?"),
 ("A","A","ഒന്ന്, സ്റ്റാഫ് എത്ര. 10 ആയാൽ ESIC, 20 ആയാൽ EPF."),
 ("A","wide","രണ്ട്, ശമ്പള പരിധി. ESIC-ന് മാസം 21,000 രൂപ വരെ, EPF-ന് 2026 സെപ്റ്റംബർ 17 മുതൽ 25,000 രൂപ."),
 ("V","wide","എണ്ണം നോക്കുന്നവന് പിഴ എണ്ണേണ്ട.")],
 "എണ്ണം 10, 20.\nപരിധി 21,000, 25,000", CTA_ESIC, theme="tip",
 cap_ml="ശമ്പളം കൊടുക്കും മുമ്പുള്ള മാസ ചെക്ക്: സ്റ്റാഫ് 10 ആയാൽ ESIC, 20 ആയാൽ EPF. ESIC ശമ്പള പരിധി മാസം 21,000 രൂപ; EPF പരിധി 2026 സെപ്റ്റംബർ 17 മുതൽ 25,000 രൂപ. ഈ മാസം നിങ്ങളുടെ സ്റ്റാഫ് എണ്ണം മാറിയോ?",
 cap_en="A one-minute check before every payday: 10 staff means ESIC, 20 means EPF. The ESIC wage ceiling is 21,000 a month, and the EPF ceiling is 25,000 a month from 17 September 2026. Did your staff count change this month?",
 cap_mg="Shambalam kodukkum mumpulla maasa check: staff 10 aayaal ESIC, 20 aayaal EPF. ESIC wage limit maasam 21,000 roopa; EPF limit 2026 September 17 muthal 25,000 roopa. Ee maasam ningalude staff ennam maariyo?")

duo("pyt002", "new_hires_incentive", "B", "kitchen", "പുതിയ സ്റ്റാഫിന്\nസഹായം കണക്കിൽ\nകൂട്ടും മുമ്പ്", [
 ("V","wide","ബിന്ദൂ, കാറ്ററിംഗിന് നാല് പേരെ കൂടി എടുക്കുന്നു. PM-VBRY സഹായം കണക്കിൽ കൂട്ടിയാലോ?"),
 ("A","A","രാജേഷേട്ടാ, ആദ്യം ഉറപ്പിക്കരുത്. EPFO രജിസ്ട്രേഷൻ ഉള്ളവർക്കാണ്, ഓരോ പുതിയ സ്റ്റാഫിനും മാസം 3,000 രൂപ വരെ."),
 ("V","V","എല്ലാവർക്കും കിട്ടുമോ?"),
 ("A","wide","നിബന്ധനകൾ ഉണ്ട്. സ്റ്റാഫ് 6 മാസമെങ്കിലും തുടരണം, ശമ്പള നിരക്ക് അനുസരിച്ച് തുക മാറും, വേറെയും നിബന്ധനകൾ."),
 ("A","A","സഹായം ബോണസ് ആയി കാണൂ, ബജറ്റ് ആയിട്ടല്ല.")],
 "\"വരെ\" എന്ന വാക്ക്\nശ്രദ്ധിക്കൂ", CTA_PAYROLL, theme="tip",
 cap_ml="PM-VBRY പദ്ധതിയിൽ EPFO രജിസ്ട്രേഷൻ ഉള്ള തൊഴിലുടമയ്ക്ക് ഓരോ അധിക സ്റ്റാഫിനും മാസം 3,000 രൂപ വരെ കിട്ടാം. പക്ഷേ നിബന്ധനകൾ ഉണ്ട്: സ്റ്റാഫ് 6 മാസമെങ്കിലും തുടരണം, തുക ശമ്പള നിരക്ക് അനുസരിച്ച് മാറും, വേറെയും നിബന്ധനകൾ. ഉറപ്പായി ബജറ്റിൽ കൂട്ടരുത്. നിങ്ങൾ ഈ വർഷം എത്ര പേരെ എടുക്കും?",
 cap_en="Under PM-VBRY, EPFO-registered employers can get up to 3,000 a month for each additional employee, subject to conditions: the employee stays at least 6 months, the amount depends on the wage slab, and other conditions apply. Don't build it into your budget as a sure thing. How many people are you hiring this year?",
 cap_mg="PM-VBRY padhathiyil EPFO registration ulla employer-kku oro adhika staff-inum maasam 3,000 roopa vare kittaam. Pakshe conditions undu: staff 6 maasamenkilum thudaranam, thuka wage slab anusarichu maarum, vereyum conditions. Urappaayi budget-il koottaruthu. Ningal ee varsham ethra pere edukkum?")
