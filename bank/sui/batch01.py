# Startup India (DPIIT) seed batch 01 (20 Nov). Short, conflict-first; situations from bank/STORY_THEMES.md (anonymised).
# Facts only from topics.FACTS_SUI. Never promise approval or a benefit. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

duo("ud001", "traditional_innovator", "A", "farm", "മുട്ടക്കോഴി ഫാം\nകൂൺ കൃഷിയായി.\n\"ഇതും സ്റ്റാർട്ടപ്പ് ആണോ?\"", [
 ("A","wide","ഗോപീ, നിന്റെ പുതിയ കൂൺ ഷെഡ് കണ്ടു. എന്ത് രീതിയാ അത്?"),
 ("V","V","വാസുവേട്ടാ, കുറഞ്ഞ വെള്ളത്തിൽ കൂടുതൽ വിളവ്. ഞാൻ തന്നെ ഉണ്ടാക്കിയ രീതി."),
 ("A","A","എങ്കിൽ നിന്റെ ബിസിനസും സ്റ്റാർട്ടപ്പ് ആകും. ആപ്പ് മാത്രമല്ല സ്റ്റാർട്ടപ്പ്."),
 ("V","V","സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷൻ കിട്ടുമോ?"),
 ("A","wide","പുതുമയുള്ള രീതി, 10 വർഷത്തിൽ താഴെ പഴക്കം, കമ്പനിയോ LLP-യോ. നിന്റേത് ഇപ്പോൾ പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ? ആദ്യം അത് മാറ്റണം."),
 ("V","wide","ആദ്യം LLP, പിന്നെ DPIIT.")],
 "കൃഷിയിലും പുതുമ\nഉണ്ടെങ്കിൽ സ്റ്റാർട്ടപ്പ്", CTA_DPIIT,
 cap_ml="മുട്ടക്കോഴി ഫാമിൽ നിന്ന് പുതിയ രീതിയിലുള്ള കൂൺ കൃഷിയിലേക്ക്. പുതുമയുള്ള പ്രോസസ് ഉള്ള കൃഷി, ഫുഡ്, ആയുർവേദ ബിസിനസുകൾക്കും DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷന് അപേക്ഷിക്കാം; പക്ഷേ കമ്പനി, LLP അല്ലെങ്കിൽ പാർട്ണർഷിപ്പ് ആയിരിക്കണം.",
 cap_en="From an egg farm to mushrooms grown with a new low-water method. Startups are not only apps: agri, food and ayurveda businesses with a genuinely new process can apply for Startup India DPIIT recognition, but only as a company, LLP or registered partnership.",
 cap_mg="Egg farm-il ninnu puthiya reethiyilulla koon krishiyilekku. Puthumayulla process ulla agri, food, ayurveda business-um DPIIT recognition-nu apply cheyyaam; pakshe company, LLP allenkil partnership aayirikkanam.")

duo("ud002", "grant_seeker", "A", "library", "ഗ്രാന്റ് അപേക്ഷ\nറിജക്റ്റ്. കാരണം:\n\"DPIIT ഇല്ല\"", [
 ("A","wide","അനൂപ്, ആ ഗ്രാന്റിന്റെ റിസൾട്ട് വന്നോ?"),
 ("V","V","വന്നു, ഗ്രീഷ്മേ. റിജക്റ്റ്. DPIIT റെക്കഗ്നിഷൻ ഇല്ലെന്ന് പറഞ്ഞ്."),
 ("A","A","ആശയം നല്ലതായിട്ടും?"),
 ("V","V","പല സർക്കാർ സ്കീമുകളും ആദ്യം നോക്കുന്നത് അതാണ്. KSUM ഗ്രാന്റുകളും സാധാരണ ചോദിക്കും."),
 ("A","wide","അടുത്ത കോളിന് മുമ്പ് റെക്കഗ്നിഷൻ എടുത്ത് വെക്ക്."),
 ("V","wide","ഇത്തവണ പേപ്പർ ആദ്യം.")],
 "ഗ്രാന്റിന് മുമ്പ്\nDPIIT", CTA_DPIIT,
 cap_ml="നല്ല ആശയം ഉണ്ടായിട്ടും ഗ്രാന്റ് അപേക്ഷ റിജക്റ്റ്, കാരണം DPIIT റെക്കഗ്നിഷൻ ഇല്ല. പല സർക്കാർ സ്കീമുകളും KSUM ഗ്രാന്റുകളും ഇത് ചോദിക്കും; അടുത്ത കോളിന് മുമ്പ് എടുത്ത് വെക്കൂ.",
 cap_en="A good idea, but the grant application was rejected for one reason: no DPIIT recognition. Many government schemes and Kerala Startup Mission grants ask for Startup India recognition, so get it before the next call.",
 cap_mg="Nalla idea undaayittum grant application reject, kaaranam DPIIT recognition illa. Pala government schemes-um KSUM grants-um ithu chodikkum; adutha call-nu mumbu eduthu vekkoo.")

duo("ud003", "tech_founder", "B", "rooftop", "\"DPIIT കിട്ടിയാൽ\nടാക്സ് ഇല്ല\"\nഇത് പകുതി ശരി", [
 ("A","wide","ശ്യാം, നിന്റെ കമ്പനിക്ക് സ്റ്റാർട്ടപ്പ് ഇന്ത്യ കിട്ടിയല്ലോ. ഇനി ടാക്സ് വേണ്ടല്ലോ?"),
 ("V","V","എല്ലാവരും അങ്ങനെയാ കരുതുന്നത്, ആര്യേ. പക്ഷേ അത് ഓട്ടോമാറ്റിക് അല്ല."),
 ("A","A","പിന്നെ?"),
 ("V","V","3 വർഷത്തെ ടാക്സ് ഹോളിഡേയ്ക്ക് വേറെ അപേക്ഷ കൊടുക്കണം. ഒരു സർക്കാർ ബോർഡ് അംഗീകരിക്കണം."),
 ("A","wide","അപ്പോ റെക്കഗ്നിഷൻ ആദ്യ പടി മാത്രം."),
 ("V","wide","അതേ. ഇനി രണ്ടാമത്തെ പടി.")],
 "റെക്കഗ്നിഷൻ ഒന്ന്,\nടാക്സ് ഹോളിഡേ വേറെ", CTA_BENEFITS,
 cap_ml="DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷൻ കിട്ടിയാൽ ടാക്സ് ഓട്ടോമാറ്റിക്കായി ഒഴിവാകില്ല. 3 വർഷത്തെ ടാക്സ് ഹോളിഡേയ്ക്ക് (80-IAC) വേറെ അപേക്ഷ വേണം, ഇന്റർ മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കണം.",
 cap_en="Myth: DPIIT recognition means no income tax. The 3-year tax holiday under section 80-IAC is a separate application that the Inter-Ministerial Board must approve. Startup India benefits, explained for Kerala founders.",
 cap_mg="DPIIT recognition kittiyaal tax automatic aayi ozhivaakilla. 3 varshathe tax holiday-kku (80-IAC) vere application venam, Inter Ministerial Board angeekarikkanam.")

duo("ud004", "student_founder", "A", "classroom", "ഫൈനൽ ഇയർ പ്രൊജക്റ്റ്\nഇൻവെസ്റ്റർ കണ്ടു.\n\"കമ്പനി ഏതാ?\"", [
 ("A","wide","ആദർശ്, നിന്റെ കുട്ടികൾക്കുള്ള ഫുട്ബോൾ ആപ്പ് ഇൻവെസ്റ്റർ കണ്ടെന്ന് കേട്ടു!"),
 ("V","V","കണ്ടു, നിമ്മി ടീച്ചർ. ആദ്യ ചോദ്യം: കമ്പനി ഏതാ? DPIIT ഉണ്ടോ?"),
 ("A","A","നീ ഇതുവരെ രജിസ്റ്റർ ചെയ്തില്ലേ?"),
 ("V","V","ഇല്ല. പ്രൊജക്റ്റ് മാത്രം."),
 ("A","wide","ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്. പിന്നെ സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷൻ. ഇൻവെസ്റ്റർക്ക് വിശ്വാസം കൂടും."),
 ("V","wide","അടുത്ത മീറ്റിംഗിന് സർട്ടിഫിക്കറ്റുമായി.")],
 "പ്രൊജക്റ്റിൽ നിന്ന്\nസ്റ്റാർട്ടപ്പിലേക്ക്", CTA_DPIIT,
 cap_ml="കോളേജ് പ്രൊജക്റ്റ് ആയി തുടങ്ങിയ ആപ്പ് ഇൻവെസ്റ്റർ കണ്ടു, ആദ്യ ചോദ്യം കമ്പനിയും DPIIT-യും. ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷൻ, പിന്നെ സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷൻ.",
 cap_en="A student founder's app gets an investor meeting, and the first questions are: which company, and is it DPIIT recognised? Register a private limited company first, then apply for Startup India recognition. Student startups in Kerala.",
 cap_mg="College project aayi thudangiya app investor kandu, aadya chodyam company-um DPIIT-um. Aadyam Pvt Ltd registration, pinne Startup India recognition.")

chat("uc001", "investor_ready", "A", "പ്രൊപ്രൈറ്റർഷിപ്പിന്\nDPIIT? റിജക്റ്റ്.\nകാരണം ഇതാ", ("ദിവ്യ", "നിഖിൽ"), [
 (1,"ദിവ്യേ, എന്റെ DPIIT അപേക്ഷ തള്ളി. എന്റെ ബിസിനസ് നന്നായി പോകുന്നുണ്ടല്ലോ."),
 (0,"നിന്റെ ബിസിനസ് പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ?"),
 (1,"അതേ. എന്റെ പേരിൽ മാത്രം."),
 (0,"അതാ കാരണം. കമ്പനി, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് ഇവയ്ക്കേ റെക്കഗ്നിഷൻ കിട്ടൂ."),
 (1,"അപ്പോ ആദ്യം കമ്പനി."),
 (0,"അതേ. ഇൻവെസ്റ്റ്മെന്റും നോക്കുന്നുണ്ടെങ്കിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് തന്നെ നല്ലത്.")],
 "പ്രൊപ്രൈറ്റർഷിപ്പിന്\nറെക്കഗ്നിഷൻ ഇല്ല", CTA_DPIIT,
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പിന് DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷൻ കിട്ടില്ല. പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് എന്നിവയ്ക്കാണ് അപേക്ഷിക്കാൻ പറ്റുക; ഇൻവെസ്റ്റ്മെന്റ് നോക്കുന്നെങ്കിൽ Pvt Ltd.",
 cap_en="A proprietorship cannot get Startup India DPIIT recognition. Only a private limited company, LLP or registered partnership can apply, and if you also want investors, a Pvt Ltd is the right choice.",
 cap_mg="Proprietorship-nu DPIIT recognition kittilla. Pvt Ltd, LLP, registered partnership ivaykku maathram apply cheyyaam; investment nokkunnenkil Pvt Ltd.")

lst("ul001", "grant_seeker", "B", "DPIIT റെക്കഗ്നിഷൻ\nകിട്ടാൻ വേണ്ട\n3 കാര്യം", [
 ("കമ്പനി അല്ലെങ്കിൽ LLP", "രജിസ്റ്റർ ചെയ്ത് 10 വർഷത്തിൽ താഴെ. പ്രൊപ്രൈറ്റർഷിപ്പിന് പറ്റില്ല."),
 ("ടേൺഓവർ", "ഒരു വർഷവും 200 കോടി കടന്നിട്ടില്ല."),
 ("പുതുമ", "പുതിയ പ്രോഡക്റ്റ്, പ്രോസസ് അല്ലെങ്കിൽ വളരാൻ പറ്റുന്ന ബിസിനസ് മോഡൽ.")],
 "3-ഉം ഉണ്ടോ?", CTA_DPIIT,
 cap_ml="DPIIT സ്റ്റാർട്ടപ്പ് ഇന്ത്യ റെക്കഗ്നിഷന് വേണ്ടത്: പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP അല്ലെങ്കിൽ രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്; 10 വർഷത്തിൽ താഴെ പഴക്കം; ഒരു വർഷവും 200 കോടി കടക്കാത്ത ടേൺഓവർ; പുതുമ.",
 cap_en="Startup India DPIIT recognition checklist: a Pvt Ltd, LLP or registered partnership; under 10 years old; turnover never above Rs 200 crore in any year; and an innovative product, process or scalable model.",
 cap_mg="DPIIT Startup India recognition-nu venda 4 kaaryam: Pvt Ltd, LLP allenkil registered partnership; 10 varshathil thaazhe; 200 crore kadakkatha turnover; puthuma.")
