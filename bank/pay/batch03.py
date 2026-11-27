# pay batch 03 (27 Nov night): ESIC reels from the verified esic.gov.in line added to topics.FACTS_PAY (27 Nov).
# Never promise an incentive or state our fee; disputes / inspections go to a labour-law professional. Invented names and places.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ESIC, CTA_PAYROLL = topics.CTA_ESIC, topics.CTA_PAYROLL

# faq: a catering kitchen cuts the employer's 3.25% from the staff's pay
duo("pyd008", "ten_staff", "B", "kitchen", "ESI മുഴുവൻ\nസ്റ്റാഫിന്റെ\nശമ്പളത്തിൽ നിന്ന്!", [
 ("A","wide","രാജേഷേ, കാറ്ററിംഗ് സ്റ്റാഫിന്റെ സ്ലിപ്പ് നോക്കി. ESI-ക്ക് നാല് ശതമാനം മുഴുവൻ അവരുടെ ശമ്പളത്തിൽ നിന്നാണല്ലോ പിടിച്ചത്."),
 ("V","V","ബിന്ദൂ, ESI അവരുടെ ഗുണത്തിനല്ലേ? അപ്പോ അവർ തന്നെ അടയ്ക്കട്ടെ."),
 ("A","A","അങ്ങനെയല്ല. ജീവനക്കാരന്റെ പങ്ക് ശമ്പളത്തിന്റെ 0.75% മാത്രം. 3.25% തൊഴിലുടമ സ്വന്തമായി അടയ്ക്കണം."),
 ("V","V","അപ്പോ ഈ മാസം മുതൽ സ്ലിപ്പ് ശരിയാക്കാം."),
 ("A","wide","അവരുടെ പങ്ക് 0.75%. ബാക്കി നമ്മുടേത്.")],
 "ജീവനക്കാരൻ 0.75%,\nതൊഴിലുടമ 3.25%", CTA_ESIC, theme="faq",
 cap_ml="ESI കോൺട്രിബ്യൂഷൻ: ജീവനക്കാരന്റെ പങ്ക് ശമ്പളത്തിന്റെ 0.75%, തൊഴിലുടമയുടേത് 3.25%. തൊഴിലുടമയുടെ പങ്ക് സ്റ്റാഫിന്റെ ശമ്പളത്തിൽ നിന്ന് പിടിക്കരുത്. നിങ്ങളുടെ സ്ലിപ്പിൽ ESI എത്ര ശതമാനമാണ്?",
 cap_en="A catering kitchen deducts the whole ESI amount from its staff's pay. The employee's share is 0.75% of wages; the employer pays its own 3.25% and must not cut it from salaries. What percentage does your slip show for ESI?",
 cap_mg="ESI contribution: jeevanakkaarante panku shambalathinte 0.75%, thozhiludamayudethu 3.25%. Thozhiludamayude panku staff-inte shambalathil ninnu pidikkaruthu. Ningalude slip-il ESI ethra shathamaanamaanu?")

# new: a plant nursery's trainee on a low daily wage: no employee share, the employer still pays
duo("pyd009", "ten_staff", "B", "farm", "ട്രെയിനിയുടെ\nകൂലി കുറവ്.\nESI-യേ വേണ്ട?", [
 ("A","wide","ഗോപീ, നഴ്സറിയിലെ പുതിയ ട്രെയിനിക്ക് ദിവസക്കൂലി ശരാശരി 176 രൂപയിൽ താഴെയാണ്. അപ്പോ ESI ഒന്നും വേണ്ടല്ലോ?"),
 ("V","V","വാസുവേട്ടാ, ആ ട്രെയിനി സ്വന്തം പങ്ക് അടയ്ക്കേണ്ട. പക്ഷേ തൊഴിലുടമയുടെ പങ്ക് നമ്മൾ അടയ്ക്കണം."),
 ("A","A","അപ്പോ ഒഴിവ് അവന് മാത്രം, നമുക്കില്ല."),
 ("V","V","അതെ. മാസം കഴിഞ്ഞ് 15 ദിവസത്തിനകം അടയ്ക്കുകയും വേണം."),
 ("A","wide","കൂലി കുറഞ്ഞാലും, നമ്മുടെ പങ്ക് ബാക്കി.")],
 "ജീവനക്കാരന് ഒഴിവ്,\nതൊഴിലുടമയ്ക്ക് ഇല്ല", CTA_ESIC, theme="new",
 cap_ml="ദിവസക്കൂലി ശരാശരി 176 രൂപ വരെ ഉള്ള ജീവനക്കാർ ESI-യിൽ സ്വന്തം പങ്ക് അടയ്ക്കേണ്ട. പക്ഷേ തൊഴിലുടമ അവരുടെ പങ്ക് അടയ്ക്കണം, മാസം കഴിഞ്ഞ് 15 ദിവസത്തിനകം. നിങ്ങളുടെ സ്ഥാപനത്തിൽ ട്രെയിനികൾ ഉണ്ടോ?",
 cap_en="A plant nursery has a trainee on an average daily wage under 176 rupees and assumes no ESI is due. Employees with an average daily wage up to 176 rupees pay no employee share, but the employer still pays its share, within 15 days of the end of the month. Do you have trainees?",
 cap_mg="Divasakkooli sharaashari 176 rupees vare ulla jeevanakkaar ESI-yil swantham panku adaykkenda. Pakshe thozhiludama avarude panku adaykkanam, maasam kazhinju 15 divasathinakam. Ningalude sthaapanathil trainees undo?")
