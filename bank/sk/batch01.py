# Kerala Startup Mission seed batch 01 (20 Nov). Short, conflict-first; situations from bank/STORY_THEMES.md (anonymised).
# Facts only from topics.FACTS_SK. Never state grant amounts or promise selection. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

duo("md001", "returnee", "A", "airport", "14 വർഷം ഗൾഫിൽ\nസോഫ്റ്റ്‌വെയർ. നാട്ടിൽ\nസ്റ്റാർട്ടപ്പ്. KSUM അറിയില്ല", [
 ("A","wide","റഫീഖ്, ഇത്തവണ ലീവിനല്ലല്ലോ വരവ്?"),
 ("V","V","ഷമീർ, ഇനി നാട്ടിൽ തന്നെ. ഞാൻ ഉണ്ടാക്കിയ സോഫ്റ്റ്‌വെയർ പ്രോഡക്റ്റ് ഇവിടെ നിന്ന് വിൽക്കണം."),
 ("A","A","കേരള സ്റ്റാർട്ടപ്പ് മിഷനിൽ രജിസ്റ്റർ ചെയ്തോ?"),
 ("V","V","അതെന്താ? ഞാൻ കേട്ടിട്ടില്ല."),
 ("A","wide","KSUM-ന്റെ ഗ്രാന്റുകൾ, ഇൻക്യുബേഷൻ, പ്രോഗ്രാമുകൾ എല്ലാം യുണീക്ക് ഐഡി ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. ആദ്യം കേരളത്തിൽ കമ്പനി."),
 ("V","wide","എയർപോർട്ടിൽ നിന്ന് നേരെ പ്ലാനിംഗിലേക്ക്!")],
 "തിരിച്ചു വരുമ്പോൾ\nKSUM ഐഡിയുമായി", CTA_KSUM,
 cap_ml="ഗൾഫിൽ വർഷങ്ങൾ സോഫ്റ്റ്‌വെയർ രംഗത്ത്, ഇനി നാട്ടിൽ സ്റ്റാർട്ടപ്പ്. കേരള സ്റ്റാർട്ടപ്പ് മിഷന്റെ ഗ്രാന്റുകളും ഇൻക്യുബേഷനും പ്രോഗ്രാമുകളും KSUM യുണീക്ക് ഐഡി ഉള്ള, കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പുകൾക്കാണ്.",
 cap_en="Coming back from the Gulf to build your startup in Kerala? Kerala Startup Mission's grants, incubation and programmes are for startups registered in Kerala that hold a KSUM Unique ID. KSUM registration for NRI returnees.",
 cap_mg="Gulf-il varshangal software rangathu, ini naattil startup. Kerala Startup Mission-nte grants-um incubation-um programs-um KSUM unique ID ulla, Kerala-yil register cheytha startups-nu aanu.")

duo("md002", "idea_stage", "A", "park", "ഐഡിയ റെഡി. പ്രോട്ടോടൈപ്പ്\nറെഡി. ഗ്രാന്റ് പോർട്ടലിൽ:\n\"യുണീക്ക് ഐഡി?\"", [
 ("A","wide","അനന്തു, നിന്റെ വാട്ടർ സെൻസർ പ്രോട്ടോടൈപ്പ് ഗംഭീരം! ഗ്രാന്റിന് അപേക്ഷിച്ചോ?"),
 ("V","V","ഗായത്രി, ഐഡിയ ഗ്രാന്റിന് നോക്കി. കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം എന്ന് കണ്ടു."),
 ("A","A","അപേക്ഷിക്കാം. പക്ഷേ പൈസ കിട്ടും മുമ്പ് കമ്പനിയും KSUM യുണീക്ക് ഐഡിയും വേണം."),
 ("V","V","അപ്പോ സെലക്ട് ആയാൽ ഓടണം?"),
 ("A","wide","ഓടാതിരിക്കാൻ ഇപ്പോഴേ തുടങ്ങ്. കമ്പനി, പിന്നെ ഐഡി."),
 ("V","wide","ഗ്രാന്റിന് മുമ്പ് പേപ്പർ റെഡി.")],
 "സെലക്ഷന് മുമ്പേ\nകമ്പനിയും ഐഡിയും", CTA_GRANT,
 cap_ml="KSUM ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം; പക്ഷേ പൈസ കിട്ടും മുമ്പ് പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP-യും KSUM യുണീക്ക് ഐഡിയും വേണം. സെലക്ഷന് മുമ്പേ തുടങ്ങൂ.",
 cap_en="You can apply for the KSUM idea grant before you have a company, but the company and the KSUM Unique ID are needed before any money is released. Start the paperwork before selection, not after. Kerala startup grants.",
 cap_mg="KSUM idea grant-nu company illaathe apply cheyyaam; pakshe paisa kittum mumbu Pvt Ltd allenkil LLP-um KSUM unique ID-um venam. Selection-nu mumbe thudangoo.")

duo("md003", "kerala_registered", "A", "office", "കമ്പനി 2 വർഷമായി.\nKSUM ഗ്രാന്റ് കോൾ\nവന്നു, പോയി", [
 ("A","wide","രാഹുൽ, KSUM-ന്റെ ആ ഗ്രാന്റ് കോൾ കണ്ടോ? ഇന്നലെ ആയിരുന്നു ലാസ്റ്റ് ഡേറ്റ്."),
 ("V","V","കണ്ടു, നേഹേ. പക്ഷേ നമുക്ക് യുണീക്ക് ഐഡി ഇല്ലായിരുന്നു. അപേക്ഷിക്കാൻ പറ്റിയില്ല."),
 ("A","A","കമ്പനി രണ്ട് വർഷമായില്ലേ? ഇതുവരെ എടുത്തില്ലേ?"),
 ("V","V","ആവശ്യം വരുമ്പോൾ എടുക്കാം എന്ന് വിചാരിച്ചു."),
 ("A","wide","ആവശ്യം വരുമ്പോൾ സമയം കാണില്ല. DPIIT-യും യുണീക്ക് ഐഡിയും ഇപ്പോഴേ എടുത്ത് വെക്ക്."),
 ("V","wide","അടുത്ത കോൾ നമ്മൾ മിസ്സ് ചെയ്യില്ല.")],
 "കോൾ വരും മുമ്പ്\nഐഡി എടുക്കൂ", CTA_KSUM,
 cap_ml="രണ്ട് വർഷമായ കേരള കമ്പനിക്ക് KSUM യുണീക്ക് ഐഡി ഇല്ലാത്തതുകൊണ്ട് ഗ്രാന്റ് കോൾ നഷ്ടമായി. DPIIT റെക്കഗ്നിഷനും KSUM ഐഡിയും ആവശ്യം വരും മുമ്പേ എടുത്ത് വെക്കൂ.",
 cap_en="A two-year-old Kerala company missed a KSUM grant call because it never took the Unique ID. Get DPIIT recognition and the KSUM Unique ID before the next call opens, not during it.",
 cap_mg="Randu varshamaaya Kerala company-kku KSUM unique ID illaathathu kondu grant call nashtamaayi. DPIIT recognition-um KSUM ID-um aavashyam varum mumbe eduthu vekkoo.")

duo("md004", "women_founder", "A", "kitchen", "വീട്ടിലെ ഹെൽത്ത് ഫുഡ്\nബ്രാൻഡ്. ഇൻക്യുബേഷൻ\nവേണം. എവിടെ തുടങ്ങും?", [
 ("A","wide","രാജേഷേ, എന്റെ മില്ലറ്റ് ബ്രാൻഡിന് ഒരു വലിയ കിച്ചണും ഒരു മെന്ററും വേണം."),
 ("V","V","ബിന്ദു, കേരള സ്റ്റാർട്ടപ്പ് മിഷന്റെ ഇൻക്യുബേഷൻ നോക്കിയോ?"),
 ("A","A","അതൊക്കെ ആപ്പുകാർക്ക് അല്ലേ?"),
 ("V","V","പുതുമയുള്ള ഫുഡ് പ്രോഡക്റ്റിനും സാധ്യതയുണ്ട്. പക്ഷേ ആദ്യം കമ്പനി, പിന്നെ KSUM യുണീക്ക് ഐഡി."),
 ("A","wide","എങ്കിൽ അടുക്കളയിൽ നിന്ന് കമ്പനിയിലേക്ക്."),
 ("V","wide","ആദ്യത്തെ പായ്ക്കറ്റ് എനിക്ക്!")],
 "അടുക്കളയിൽ നിന്ന്\nസ്റ്റാർട്ടപ്പിലേക്ക്", CTA_KSUM,
 cap_ml="വീട്ടിൽ തുടങ്ങിയ മില്ലറ്റ് ഹെൽത്ത് ഫുഡ് ബ്രാൻഡിന് ഇൻക്യുബേഷനും മെന്റർഷിപ്പും വേണം. KSUM പ്രോഗ്രാമുകൾക്ക് ആദ്യം കമ്പനിയും KSUM യുണീക്ക് ഐഡിയും.",
 cap_en="A woman founder's home-made millet health-food brand needs a bigger kitchen and a mentor. Kerala Startup Mission programmes are open to innovative food startups too: register the company, then get the KSUM Unique ID.",
 cap_mg="Veettil thudangiya millet health food brand-nu incubation-um mentorship-um venam. KSUM programs-nu aadyam company-um KSUM unique ID-um.")

chat("mc001", "campus", "A", "ഡെമോ ഡേ കഴിഞ്ഞു.\n\"ഇനി എന്ത്?\"", ("അലീന", "സഞ്ജു"), [
 (1,"അലീന, ഡെമോ ഡേയിൽ നമ്മുടെ റോബോട്ട് ആം എല്ലാവർക്കും ഇഷ്ടപ്പെട്ടു! ഇനി എന്ത്?"),
 (0,"ഇനി കമ്പനി. പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP, കേരളത്തിൽ."),
 (1,"പിന്നെ?"),
 (0,"സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷൻ, പിന്നെ KSUM യുണീക്ക് ഐഡി. മിക്ക ഗ്രാന്റുകളും ഈ രണ്ടും ചോദിക്കും."),
 (1,"പരീക്ഷ കഴിഞ്ഞ് തുടങ്ങിയാലോ?"),
 (0,"പേപ്പർ ഇപ്പോൾ തുടങ്ങാം. പഠിത്തം ഒപ്പം പോകും.")],
 "ഡെമോ ഡേ കഴിഞ്ഞ്\nഈ 3 പടി", CTA_GRANT,
 cap_ml="കോളേജ് ഡെമോ ഡേ കഴിഞ്ഞ സ്റ്റുഡന്റ് ഫൗണ്ടർമാരുടെ അടുത്ത മൂന്ന് പടി: കേരളത്തിൽ കമ്പനി അല്ലെങ്കിൽ LLP, DPIIT റെക്കഗ്നിഷൻ, KSUM യുണീക്ക് ഐഡി. മിക്ക ഗ്രാന്റുകളും ഇത് ചോദിക്കും.",
 cap_en="Student founders after the campus demo day: register a company or LLP in Kerala, get DPIIT recognition, then the KSUM Unique ID. Most Kerala startup grants ask for these.",
 cap_mg="College demo day kazhinja student founders-nte adutha 3 padi: Kerala-yil company allenkil LLP, DPIIT recognition, KSUM unique ID. Mikka grants-um ithu chodikkum.")

lst("ml001", "idea_stage", "B", "KSUM ഗ്രാന്റിന്\nമുമ്പ് ചെയ്യേണ്ട\n3 കാര്യം", [
 ("കേരളത്തിൽ കമ്പനി", "പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP."),
 ("DPIIT റെക്കഗ്നിഷൻ", "മിക്ക KSUM ഗ്രാന്റുകളും ചോദിക്കും."),
 ("KSUM യുണീക്ക് ഐഡി", "KSUM സ്കീമുകളുടെ വാതിൽ.")],
 "ഏതാണ് ബാക്കി?", CTA_GRANT,
 cap_ml="KSUM ഗ്രാന്റിന് മുമ്പ്: കേരളത്തിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് അല്ലെങ്കിൽ LLP, DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷൻ, KSUM യുണീക്ക് ഐഡി.",
 cap_en="Before applying for a Kerala Startup Mission grant: a Pvt Ltd or LLP registered in Kerala, DPIIT Startup India recognition, and the KSUM Unique ID.",
 cap_mg="KSUM grant-nu mumbu: Kerala-yil Pvt Ltd allenkil LLP, DPIIT recognition, KSUM unique ID.")
