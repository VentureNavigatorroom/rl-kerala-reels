# Trademark batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_TM. Never promise registration or mention fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

duo("tm012", "copied_brand", "A", "textile", "കുടുംബം പിരിഞ്ഞു.\nകസിൻ കടയുടെ പേരിൽ\nകമ്പനി തുടങ്ങി", [
 ("A","wide","പ്രകാശേട്ടാ, അപ്പൂപ്പന്റെ കാലത്തെ നമ്മുടെ സാരിക്കടയുടെ പേരിൽ കസിൻ ഒരു കമ്പനി രജിസ്റ്റർ ചെയ്തു."),
 ("V","V","രമ്യേ, അപ്പോ ആ പേര് ഇനി അവന്റേതായോ?"),
 ("A","A","അവൻ പറയുന്നത് അങ്ങനെയാ. കമ്പനി പേര് കിട്ടിയാൽ ബ്രാൻഡും കിട്ടുമെന്ന്."),
 ("V","wide","കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല, അവന്റേതായാലും. ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ നമ്മുടെ തുണിയുടെ ക്ലാസിൽ ഇന്ന് തന്നെ ഫയൽ ചെയ്യാം."),
 ("V","wide","നൂൽ പഴയതാകാം, ഫയലിംഗ് വൈകരുത്.")],
 "കമ്പനി പേര്\nബ്രാൻഡ് അല്ല", CTA_TRADEMARK, theme="crm",
 cap_ml="മൂന്ന് തലമുറ പഴയ സാരിക്കടയുടെ പേരിൽ കസിൻ കമ്പനി രജിസ്റ്റർ ചെയ്തു. കമ്പനി പേര് അപ്രൂവൽ ആരുടെയും ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല, കച്ചവടം ചെയ്യുന്ന ക്ലാസിൽ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യണം. നിങ്ങളുടെ കടയുടെ പേര് ഫയൽ ചെയ്തോ?",
 cap_en="After a family split, a cousin registered a company using the old saree shop's name and now claims the brand. A company name approval protects nobody's brand, his or yours: the trademark has to be filed in the class you trade in. Is your shop's name filed: yes or no?",
 cap_mg="Moonnu thalamura pazhaya saree kadayude peril cousin company register cheythu. Company name approval aarudeyum brand-ine samrakshikkilla, kachavadam cheyyunna class-il trademark file cheyyanam. Ningalude kadayude peru file cheytho?")

duo("tm013", "food_brand", "B", "cafe", "ഏജന്റ് ട്രേഡ്മാർക്ക്\nഫയൽ ചെയ്തു.\nകഫേ മാത്രം പുറത്ത്", [
 ("A","wide","റോഷനേ, നമ്മുടെ കഫേയുടെ ട്രേഡ്മാർക്ക് പേപ്പർ ഏജന്റ് അയച്ചു. ഒന്ന് വായിച്ചു നോക്ക്."),
 ("V","V","ആൽവിനേ, ഇതിൽ കാപ്പിപ്പൊടിയുടെ ക്ലാസ് മാത്രമേ ഉള്ളൂ. കഫേ നടത്തുന്ന സർവീസ് ഇല്ല."),
 ("A","A","നമ്മൾ പൊടി വിൽക്കുന്നത് ചെറിയ സൈഡ് ബിസിനസ് അല്ലേ. പ്രധാനം കഫേ ആണ്."),
 ("V","wide","45 ക്ലാസുണ്ട്. കച്ചവടം ചെയ്യുന്ന ഓരോ ക്ലാസിലും ഫയൽ ചെയ്യണം. കഫേ സർവീസിന് വേറെ ക്ലാസ്."),
 ("A","A","അപ്പോ പൊടി സേഫ്, കഫേ സേഫ് അല്ല."),
 ("V","wide","കാപ്പി ഒരു ക്ലാസിൽ, കഫേ വേറൊരു ക്ലാസിൽ.")],
 "കാപ്പി ഒരു ക്ലാസിൽ,\nകഫേ വേറൊരു ക്ലാസിൽ", CTA_BRAND, theme="crm",
 cap_ml="ഏജന്റ് കഫേയുടെ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തു, പക്ഷേ കാപ്പിപ്പൊടിയുടെ ക്ലാസിൽ മാത്രം. 45 ക്ലാസുണ്ട്, കഫേ സർവീസിന് വേറെ ക്ലാസ്. നിങ്ങളുടെ ഫയലിംഗിൽ ഏത് ക്ലാസാണെന്ന് നോക്കിയിട്ടുണ്ടോ?",
 cap_en="An agent filed the cafe's trademark, but only in the class for packaged coffee powder, not for running the cafe itself. There are 45 classes, and you file in each class you actually trade in. Have you checked which class your filing covers: yes or no?",
 cap_mg="Agent cafe-yude trademark file cheythu, pakshe kaappippodiyude class-il maathram. 45 class undu, cafe service-inu vere class. Ningalude filing-il ethu class aanennu nokkiyittundo?")

duo("tm014", "app_founder", "A", "courier", "6 വണ്ടിയിൽ പേര്\nപെയിന്റ് ചെയ്തു.\nസെർച്ച് ചെയ്തത് പിന്നെ", [
 ("A","wide","അരവിന്ദേ, മീൻ ഡെലിവറി ആപ്പിന്റെ പേര് 6 വാനിലും പെയിന്റ് ചെയ്തു. നല്ല നീല കളർ."),
 ("V","V","ജയേ, ആ പേര് ട്രേഡ്മാർക്ക് സെർച്ച് ചെയ്തിരുന്നോ? ഞാൻ ഇന്നലെ നോക്കി."),
 ("A","A","എന്നിട്ട്?"),
 ("V","wide","അതേ ക്ലാസിൽ വേറൊരാൾ മുമ്പേ ഫയൽ ചെയ്തിട്ടുണ്ട്. ആദ്യം സെർച്ച്, പിന്നെ ഫയലിംഗ്, അതിന് ശേഷം TM."),
 ("A","A","ബ്രഷ് ആദ്യം എടുത്തു, പേപ്പർ അവസാനം."),
 ("V","wide","ആറ് വണ്ടിയിൽ പേരുണ്ട്, ഒരു പേപ്പറിലും ഇല്ല.")],
 "ആറ് വണ്ടിയിൽ പേര്,\nഒരു പേപ്പറിലും ഇല്ല", CTA_BRAND, theme="crm",
 cap_ml="മീൻ ഡെലിവറി സ്റ്റാർട്ടപ്പ് 6 വാനിൽ പേര് പെയിന്റ് ചെയ്തു, പിന്നെയാണ് സെർച്ച് ചെയ്തത്: അതേ ക്ലാസിൽ വേറൊരാൾ മുമ്പേ ഫയൽ ചെയ്തിരുന്നു. ആദ്യം സെർച്ച്, പിന്നെ ട്രേഡ്മാർക്ക് ഫയലിംഗ്, അതിന് ശേഷം TM. നിങ്ങൾ ആദ്യം ചെയ്തത്: ലോഗോയോ ഫയലിംഗോ?",
 cap_en="A fish-delivery startup painted its name on 6 vans and only then searched the trademark records: someone had already filed the same name in the same class. Search first, then file, and only after filing use TM. What came first for you: logo or filing?",
 cap_mg="Meen delivery startup 6 van-il peru paint cheythu, pinneyaanu search cheythathu: athe class-il veroraal munpe file cheythirunnu. Aadyam search, pinne trademark filing, athinu shesham TM. Ningal aadyam cheythathu: logo-o filing-o?")

duo("tm015", "food_brand", "C", "kitchen", "അമ്മയുടെ അച്ചാറിന്\nട്രേഡ്മാർക്ക്. മകന്റെ\nക്ലൗഡ് കിച്ചന്?", [
 ("A","wide","രാജേഷേ, നമ്മുടെ അച്ചാർ ബ്രാൻഡിന്റെ അതേ പേരിൽ നീ ക്ലൗഡ് കിച്ചൻ തുടങ്ങുന്നു എന്ന് കേട്ടു."),
 ("V","V","അതേ ബിന്ദുവമ്മേ, പേര് ട്രേഡ്മാർക്ക് ചെയ്തതല്ലേ. എനിക്കും അതിന്റെ സംരക്ഷണം കിട്ടുമല്ലോ."),
 ("A","A","ഞാൻ ഫയൽ ചെയ്തത് അച്ചാർ കുപ്പിക്കാ. നീ വിൽക്കുന്നത് ഊണാണ്."),
 ("V","wide","ശരിയാ. അച്ചാർ ഒരു സാധനം, ഭക്ഷണം വിളമ്പുന്നത് ഒരു സർവീസ്. ആ ക്ലാസിലും ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ അടുക്കള ഒന്ന്, ക്ലാസ് രണ്ട്."),
 ("V","wide","അമ്മയുടെ രുചി കിട്ടും, അമ്മയുടെ ക്ലാസ് കിട്ടില്ല.")],
 "അമ്മയുടെ രുചി കിട്ടും,\nഅമ്മയുടെ ക്ലാസ് കിട്ടില്ല", CTA_TRADEMARK, theme="crm",
 cap_ml="അമ്മയുടെ അച്ചാർ ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഉണ്ട്, മകൻ അതേ പേരിൽ ക്ലൗഡ് കിച്ചൻ തുടങ്ങുന്നു. അച്ചാർ ഒരു ഉൽപ്പന്നം, ഭക്ഷണം വിളമ്പുന്നത് വേറെ ക്ലാസിലെ സർവീസ്. കുടുംബത്തിലെ രണ്ടാമത്തെ ബിസിനസിനും ഒരേ പേരാണോ?",
 cap_en="A mother's pickle brand is a filed trademark, and her son is opening a cloud kitchen under the same name. Pickle jars are goods; serving meals is a service in a different class, so it needs its own filing. Does your family's second business use the same name: yes or no?",
 cap_mg="Ammayude achaar brand-inu trademark undu, makan athe peril cloud kitchen thudangunnu. Achaar oru ulpannam, bhakshanam vilampunnathu vere class-ile service. Kudumbathile randaamathe business-inum ore peraano?")

duo("tm016", "d2c_brand", "A", "mobileshop", "2 വർഷമായി ലോഗോയിൽ\nTM. ഫയൽ ചെയ്തിട്ടേ\nഇല്ല", [
 ("A","wide","ഫഹദേ, നിന്റെ ഫോൺ കവർ ബ്രാൻഡിന്റെ ലോഗോയിൽ TM കണ്ടു. എന്ന് ഫയൽ ചെയ്തു?"),
 ("V","V","ഹന്നാ, ഫയൽ ഒന്നും ചെയ്തിട്ടില്ല. TM ഇട്ടാൽ തന്നെ ആളുകൾ പേടിക്കും."),
 ("A","wide","TM ഇടേണ്ടത് ട്രേഡ് മാർക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്ത ശേഷമാണ്. ചിഹ്നം ഫയലിംഗ് അല്ല."),
 ("V","V","അപ്പോ രണ്ട് വർഷം ഞാൻ ഇട്ടത് വെറും രണ്ട് അക്ഷരം?"),
 ("A","A","അതേ. ആദ്യം ഫയലിംഗ്, പിന്നെ TM."),
 ("V","wide","ഫോണിന് കവർ ഉണ്ട്, ബ്രാൻഡിന് ഇല്ല.")],
 "ഫോണിന് കവർ ഉണ്ട്,\nബ്രാൻഡിന് ഇല്ല", CTA_BRAND, theme="faq",
 cap_ml="ലോഗോയിൽ TM ഇട്ടാൽ ബ്രാൻഡ് സുരക്ഷിതമാകുമോ? ഇല്ല. TM ഉപയോഗിക്കേണ്ടത് ട്രേഡ് മാർക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്ത ശേഷമാണ്, ചിഹ്നം മാത്രം ഫയലിംഗ് അല്ല. നിങ്ങളുടെ ലോഗോയിൽ TM ഉണ്ടോ?",
 cap_en="A phone-cover brand has shown TM on its logo for two years without ever filing. The symbol is not a filing: TM is used after you file with the Trade Marks Registry, and R only after registration. Is there a TM on your logo: yes or no?",
 cap_mg="Logo-il TM ittaal brand surakshithamaakumo? Illa. TM upayogikkendathu Trade Marks Registry-il file cheytha shesham, chihnam maathram filing alla. Ningalude logo-il TM undo?")

duo("tm017", "d2c_brand", "B", "fishmarket", "അലങ്കാര മീൻ ബ്രാൻഡിന്\nഒബ്ജക്ഷൻ. \"ബ്രാൻഡ്\nപോയോ?\"", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, നമ്മുടെ ഗപ്പി ഫാമിന്റെ ട്രേഡ്മാർക്കിന് ഒബ്ജക്ഷൻ വന്നു. എല്ലാം പോയി."),
 ("V","V","സുമേ, ഒബ്ജക്ഷൻ എന്ന് കേട്ടാൽ റിജക്ഷൻ എന്നാണോ അർത്ഥം?"),
 ("A","A","അല്ലേ? ഞാൻ ടാങ്കിലെ ബോർഡ് മാറ്റാൻ പോകുകയായിരുന്നു."),
 ("V","wide","ഒബ്ജക്ഷൻ ഒരു ചോദ്യമാണ്. 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. മിണ്ടാതിരുന്നാലാണ് അപകടം."),
 ("A","A","അപ്പോ ബോർഡ് അവിടെ നിൽക്കട്ടെ, മറുപടി ഇന്ന് തുടങ്ങാം."),
 ("V","wide","മീൻ മിണ്ടില്ല, നമ്മൾ മിണ്ടണം.")],
 "ഒബ്ജക്ഷൻ ഒരു ചോദ്യം,\nമറുപടി 30 ദിവസത്തിൽ", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്കിന് ഒബ്ജക്ഷൻ വന്നാൽ ബ്രാൻഡ് പോയോ? ഇല്ല. ഒബ്ജക്ഷൻ ഒരു ചോദ്യമാണ്, 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. മിണ്ടാതിരുന്നാലാണ് അപകടം. ഇത് അറിയാമായിരുന്നോ?",
 cap_en="An ornamental fish farm's trademark got an objection, and the owner thought the brand was gone. An objection is a question, not a rejection: the reply is due within 30 days. Staying silent is the real risk. Did you know this: yes or no?",
 cap_mg="Trademark-inu objection vannaal brand poyo? Illa. Objection oru chodyamaanu, 30 divasathinullil marupadi kodukkanam. Mindaathirunnaalaanu apakadam. Ithu ariyaamaayirunno?")

duo("tm018", "d2c_brand", "C", "pharmacy", "\"ജേണലിൽ പേര് വന്നു!\nനാളെ മുതൽ R\nഇടാം\"", [
 ("A","wide","പ്രവീണേ, നമ്മുടെ കാച്ചിയ എണ്ണയുടെ ബ്രാൻഡ് ട്രേഡ്മാർക്ക് ജേണലിൽ വന്നു! ലേബലിൽ R ഇടട്ടെ?"),
 ("V","V","സിനീ, ജേണലിൽ വന്നത് രജിസ്ട്രേഷൻ അല്ല. ഇനിയാണ് മറ്റുള്ളവർ കാണുന്നത്."),
 ("A","A","കണ്ടിട്ട് അവർ എന്ത് ചെയ്യും?"),
 ("V","wide","ജേണലിൽ വന്ന് 4 മാസത്തിനുള്ളിൽ ആർക്കും ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം. R രജിസ്ട്രേഷന് ശേഷം മാത്രം. അതുവരെ TM."),
 ("A","A","അപ്പോ എണ്ണ കാച്ചി, ഇനി തണുക്കാൻ കാത്തിരിക്കണം."),
 ("V","wide","ജേണൽ ഷോക്കേസ് ആണ്, സർട്ടിഫിക്കറ്റ് അല്ല.")],
 "ജേണൽ ഷോക്കേസ്,\nസർട്ടിഫിക്കറ്റ് അല്ല", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് ജേണലിൽ പേര് വന്നാൽ R ഇടാമോ? ഇല്ല. ജേണലിൽ വന്ന് 4 മാസം ആർക്കും ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം, R രജിസ്ട്രേഷന് ശേഷം മാത്രം. അതുവരെ TM. നിങ്ങളുടെ ബ്രാൻഡ് ഏത് ഘട്ടത്തിലാണ്?",
 cap_en="A herbal hair-oil brand appeared in the Trade Marks Journal and the founder wanted R on the label the next day. Publication is not registration: for 4 months after it anyone can file an opposition, and R comes only after registration. Until then it's TM. Which stage is your brand at?",
 cap_mg="Trademark journal-il peru vannaal R idaamo? Illa. Journal-il vannu 4 maasam aarkkum opposition file cheyyaam, R registration-inu shesham maathram. Athuvare TM. Ningalude brand ethu ghattathilaanu?")

duo("tm019", "d2c_brand", "A", "beach", "സർഫ് സ്കൂൾ ചോദിക്കുന്നു:\n\"45 ക്ലാസിലും\nഫയൽ ചെയ്താലോ?\"", [
 ("A","wide","നിഖിലേ, നമ്മുടെ സർഫ് സ്കൂളിന്റെ പേര് 45 ക്ലാസിലും ഫയൽ ചെയ്താലോ? പിന്നെ ആരും തൊടില്ല."),
 ("V","V","ദിവ്യേ, നമ്മൾ സോപ്പും സിമന്റും വിൽക്കുന്നുണ്ടോ?"),
 ("A","A","ഇല്ല. സർഫിംഗ് ക്ലാസും പിന്നെ കുറച്ച് ടീ-ഷർട്ടും."),
 ("V","wide","അപ്പോ ആ രണ്ടിന്റെയും ക്ലാസിൽ. 45 ക്ലാസുണ്ടെങ്കിലും ഫയൽ ചെയ്യേണ്ടത് നമ്മൾ കച്ചവടം ചെയ്യുന്ന ക്ലാസുകളിൽ."),
 ("A","A","എല്ലാ തിരയിലും കയറാൻ പറ്റില്ല, അല്ലേ?"),
 ("V","wide","കടലിൽ തിര 45, നമ്മൾ കയറുന്നത് രണ്ടിൽ.")],
 "കടലിൽ തിര 45,\nനമ്മൾ കയറുന്നത് രണ്ടിൽ", CTA_BRAND, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് 45 ക്ലാസിലും ഫയൽ ചെയ്യണോ? വേണ്ട. ഫയൽ ചെയ്യേണ്ടത് നിങ്ങൾ കച്ചവടം ചെയ്യുന്ന ക്ലാസുകളിലാണ്: സർഫ് സ്കൂളിന് കോച്ചിംഗ് സർവീസും വിൽക്കുന്ന ടീ-ഷർട്ടും. നിങ്ങളുടെ ബിസിനസ് എത്ര ക്ലാസിൽ?",
 cap_en="A beach surf school wanted to file its name in all 45 trademark classes so nobody could touch it. You file in the classes you actually trade in: here, the coaching service and the T-shirts they sell. How many classes does your business trade in: one, two or more?",
 cap_mg="Trademark 45 class-ilum file cheyyano? Venda. File cheyyendathu ningal kachavadam cheyyunna class-ukalil: surf school-inu coaching service-um vilkkunna T-shirt-um. Ningalude business ethra class-il?")

duo("tm020", "food_brand", "B", "farm", "റിട്ടയർ ആകുന്ന\nകർഷകന്റെ തേൻ ബ്രാൻഡ്\nവാങ്ങുന്നു", [
 ("A","wide","ഗോപീ, മലയോരത്തെ ആ പഴയ തേൻ ബ്രാൻഡ് നമ്മൾക്ക് തരാമെന്ന് മത്തായിച്ചേട്ടൻ പറഞ്ഞു. സർട്ടിഫിക്കറ്റ് ഉണ്ട്."),
 ("V","V","വാസുവേട്ടാ, ആ സർട്ടിഫിക്കറ്റിലെ തീയതി നോക്കിയോ?"),
 ("A","A","2014. ട്രേഡ്മാർക്ക് ഒരിക്കൽ കിട്ടിയാൽ എന്നും ഉണ്ടല്ലോ."),
 ("V","wide","ഇല്ല. രജിസ്ട്രേഷൻ 10 വർഷത്തേക്കാണ്, പിന്നെ പുതുക്കണം. പുതുക്കിയോ എന്ന് ആദ്യം നോക്കണം."),
 ("A","A","തേൻ പഴകിയാലും കേടാകില്ല, പേപ്പർ അങ്ങനെയല്ല."),
 ("V","wide","തേൻ വാങ്ങും മുമ്പ് തീയതി നോക്കണം.")],
 "തേൻ കേടാകില്ല,\nപേപ്പറിന് കാലാവധിയുണ്ട്", CTA_TRADEMARK, theme="new",
 cap_ml="റിട്ടയർ ആകുന്ന കർഷകന്റെ പഴയ തേൻ ബ്രാൻഡ് വാങ്ങുകയാണോ? ട്രേഡ്മാർക്ക് രജിസ്ട്രേഷൻ 10 വർഷത്തേക്കാണ്, പിന്നെ പുതുക്കണം. വാങ്ങും മുമ്പ് പുതുക്കിയോ എന്ന് നോക്കൂ. നിങ്ങളുടെ ബ്രാൻഡിന് എത്ര വയസ്സായി?",
 cap_en="Two farmers are about to take over a retiring beekeeper's honey brand, and its trademark certificate is from 2014. Registration lasts 10 years and then has to be renewed, so check the renewal before you take over a brand. How old is your brand's registration?",
 cap_mg="Retire aakunna karshakante pazhaya then brand vaangukayaano? Trademark registration 10 varshathekkaanu, pinne puthukkanam. Vaangum munpu puthukkiyo ennu nokku. Ningalude brand-inu ethra vayassaayi?")

chat("tm021", "copied_brand", "C", "കളരി പഠിച്ച ശിഷ്യൻ\nഅതേ പേരിൽ അക്കാദമി.\nജേണലിൽ 3 മാസം മുമ്പ്", ("ഗായത്രി", "അനന്തു"), [
 (0,"അനന്തൂ, നമ്മുടെ കളരി സംഘത്തിന്റെ അതേ പേരിൽ നമ്മുടെ പഴയ ശിഷ്യൻ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തു. ജേണലിൽ കണ്ടു."),
 (1,"ഗായത്രിച്ചേച്ചീ, എന്നാ ജേണലിൽ വന്നത്?"),
 (0,"മൂന്ന് മാസം മുമ്പ്. ഇനി ഒന്നും ചെയ്യാൻ പറ്റില്ലല്ലോ."),
 (1,"പറ്റും. ജേണലിൽ വന്ന് 4 മാസത്തിനുള്ളിൽ ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം. ഒരു മാസം ബാക്കിയുണ്ട്."),
 (0,"അപ്പോ ഇന്ന് തന്നെ തുടങ്ങാം. നമ്മുടെ പേരും ഫയൽ ചെയ്യാം."),
 (1,"അടവ് പഠിപ്പിക്കാം, സമയം പഠിപ്പിക്കാൻ പറ്റില്ല.")],
 "ജേണലിൽ വന്നാൽ\n4 മാസം മാത്രം", CTA_BRAND, theme="new",
 cap_ml="പഴയ ശിഷ്യൻ കളരി സംഘത്തിന്റെ അതേ പേരിൽ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തു, ജേണലിൽ വന്നിട്ട് 3 മാസം. ജേണലിൽ വന്ന് 4 മാസത്തിനുള്ളിൽ ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം. നിങ്ങളുടെ പേരിന് സമാനമായ അപേക്ഷകൾ നോക്കാറുണ്ടോ?",
 cap_en="A former student filed a trademark for the same name as the Kalaripayattu academy he trained at, and it was published in the journal 3 months ago. An opposition can be filed within 4 months of journal publication, so there is one month left. Do you check the journal for names like yours: yes or no?",
 cap_mg="Pazhaya shishyan kalari sanghathinte athe peril trademark file cheythu, journal-il vannittu 3 maasam. Journal-il vannu 4 maasathinullil opposition file cheyyaam. Ningalude perinu samaanamaaya apekshakal nokkaarundo?")
