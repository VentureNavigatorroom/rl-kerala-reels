# GST batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

duo("gd005", "trader", "A", "veranda", "\"ഈ മാസം ഒരു വിൽപ്പനയും\nഇല്ല, റിട്ടേൺ വേണ്ട\"\nപിഴ വന്നു", [
 ("A","wide","ബാലേട്ടാ, ഓണം കഴിഞ്ഞ് പായസം മിക്സിന് ഓർഡർ ഒന്നുമില്ല. ഈ മാസം GST റിട്ടേൺ വേണ്ടല്ലോ?"),
 ("V","V","വേണം ശാന്തേ. വിൽപ്പന ഇല്ലെങ്കിലും നിൽ റിട്ടേൺ ഫയൽ ചെയ്യണം."),
 ("A","A","ഒന്നും വിറ്റില്ലെങ്കിൽ എന്ത് ഫയൽ ചെയ്യാനാ?"),
 ("V","wide","നിൽ റിട്ടേൺ വൈകിയാൽ ദിവസം 20 രൂപ ലേറ്റ് ഫീ, 500 വരെ. രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം റിട്ടേൺ ഉണ്ട്."),
 ("A","A","കച്ചവടം ഉറങ്ങിയാലും GST ഉണർന്നിരിക്കും."),
 ("V","wide","അതെ. പായസം തണുക്കും, റിട്ടേൺ തണുക്കില്ല.")],
 "വിൽപ്പന ഇല്ലെങ്കിലും\nനിൽ റിട്ടേൺ", CTA_PENALTY, theme="faq",
 cap_ml="ഓണം കഴിഞ്ഞ് വിൽപ്പന ഇല്ലാത്ത മാസവും GST റിട്ടേൺ വേണം. നിൽ റിട്ടേൺ വൈകിയാൽ ദിവസം 20 രൂപ ലേറ്റ് ഫീ, പരമാവധി 500. നിങ്ങളുടെ ബിസിനസ് സീസണലാണോ?",
 cap_en="A payasam-mix seller has no orders after Onam and thinks no GST return is due. Wrong: returns are due even in months with no sales. A late nil GSTR-3B costs Rs 20 a day, capped at Rs 500. Is your business seasonal?",
 cap_mg="Onam kazhinju vilppana illaatha maasavum GST return venam. Nil return vaikiyaal divasam 20 roopa late fee, paramaavadhi 500. Ningalude business seasonal aano?")

duo("gd006", "trader", "B", "akshaya", "\"GST കിട്ടാൻ\nമാസങ്ങൾ എടുക്കും\"\nഅതുകൊണ്ട് ഓർഡർ വിട്ടു", [
 ("A","wide","രമേശ്, ആ കാറ്ററിംഗ് കമ്പനിയുടെ വാഴയില ഓർഡർ ഞാൻ വേണ്ടെന്ന് വെച്ചു. GST കിട്ടാൻ മാസങ്ങൾ എടുക്കുമല്ലോ."),
 ("V","V","ആര് പറഞ്ഞു? 2025 നവംബർ 1 മുതൽ ലോ-റിസ്ക് അപേക്ഷകൾക്ക് 3 പ്രവൃത്തി ദിവസത്തിനുള്ളിൽ ഓട്ടോ അപ്രൂവൽ."),
 ("A","A","എല്ലാവർക്കും അങ്ങനെയാണോ?"),
 ("V","wide","അല്ലെങ്കിൽ 7 പ്രവൃത്തി ദിവസം. ഫിസിക്കൽ വെരിഫിക്കേഷൻ വേണ്ടിവന്നാൽ 30 ദിവസം വരെ."),
 ("A","A","മാസങ്ങൾ അല്ല, ദിവസങ്ങൾ!"),
 ("V","wide","അതെ. ഇല വാടും മുമ്പ് GST വരും.")],
 "GST: ദിവസങ്ങൾ,\nമാസങ്ങൾ അല്ല", CTA_GST, theme="new",
 cap_ml="GST കിട്ടാൻ മാസങ്ങൾ എടുക്കും എന്ന് കരുതി വലിയ ഓർഡർ വിട്ടു. 2025 നവംബർ 1 മുതൽ ലോ-റിസ്ക് അപേക്ഷകൾക്ക് 3 പ്രവൃത്തി ദിവസത്തിൽ ഓട്ടോ അപ്രൂവൽ; അല്ലെങ്കിൽ 7, വെരിഫിക്കേഷൻ ഉണ്ടെങ്കിൽ 30 ദിവസം വരെ.",
 cap_en="A banana-leaf supplier turned down a catering company's order, thinking GST takes months. Since 1 Nov 2025 low-risk GST applications are auto-approved within 3 working days; otherwise 7 working days, up to 30 if physical verification is needed.",
 cap_mg="GST kittaan maasangal edukkum ennu karuthi valiya order vittu. 2025 November 1 muthal low-risk applications-nu 3 working days-il auto approval; allenkil 7, verification undenkil 30 divasam vare.")

duo("gd007", "new_company", "A", "garage", "പുതിയ മെഷീനുകൾക്ക്\nGST അടച്ചു.\nക്രെഡിറ്റ്? ഒന്നുമില്ല", [
 ("A","wide","ജിതിൻ, പുതിയ കാർ ഡീറ്റെയിലിംഗ് സ്റ്റുഡിയോയ്ക്ക് മെഷീനുകൾ വാങ്ങിയപ്പോൾ നല്ലൊരു തുക GST ആയി പോയി."),
 ("V","V","നമുക്ക് GST രജിസ്ട്രേഷൻ ഇല്ലല്ലോ. അപ്പോ ആ ടാക്സ് ഇൻപുട്ട് ക്രെഡിറ്റ് ആയി എടുക്കാൻ പറ്റില്ല."),
 ("A","A","ടേൺഓവർ 20 ലക്ഷം ആയിട്ടില്ല. എന്നാലും എടുക്കാമോ?"),
 ("V","wide","സ്വമേധയാ ആർക്കും എടുക്കാം. ഇൻപുട്ട് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം. കമ്പനി ക്ലയന്റ്സും GSTIN ചോദിക്കും."),
 ("A","A","അപ്പോ അടുത്ത മെഷീന് മുമ്പ് GSTIN."),
 ("V","wide","അതെ. കാർ മിനുക്കും മുമ്പ് കണക്ക് മിനുക്കണം.")],
 "ഇൻപുട്ട് ക്രെഡിറ്റ്\nരജിസ്റ്റർ ചെയ്തവർക്ക്", CTA_GST, theme="faq",
 cap_ml="GST രജിസ്ട്രേഷൻ ഇല്ലാത്തതുകൊണ്ട് മെഷീനുകൾക്ക് അടച്ച GST ക്രെഡിറ്റ് ആയി കിട്ടിയില്ല. ലിമിറ്റിന് താഴെയും സ്വമേധയാ GST എടുക്കാം; ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം. വോളണ്ടറി GST നിങ്ങൾക്ക് ഗുണമാകുമോ?",
 cap_en="A new car detailing studio paid GST on its machines but can't claim it back because it isn't registered. Anyone may register voluntarily, even below the Rs 20 lakh service limit; input tax credit is only for registered persons, and business clients often ask for a GSTIN.",
 cap_mg="GST registration illaathathukondu machines-nu adacha GST credit aayi kittiyilla. Limit-nu thaazheyum swamedhaya GST edukkaam; input tax credit register cheythavarkku maathram.")
