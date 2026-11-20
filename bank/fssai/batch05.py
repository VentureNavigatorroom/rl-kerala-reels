# FSSAI batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# crm: small cold-press mill, a supermarket chain's buyer checks the label
duo("fs020", "packaged_food", "A", "shop", "സൂപ്പർമാർക്കറ്റ് ബയർ\nകുപ്പി തിരിച്ചു വെച്ചു:\n\"നമ്പർ എവിടെ?\"", [
 ("A","wide","സുരേഷേ, നമ്മുടെ മരച്ചക്ക് വെളിച്ചെണ്ണയ്ക്ക് സൂപ്പർമാർക്കറ്റിൽ നിന്ന് ഓർഡർ വന്നതാ. ബയർ കുപ്പി തിരിച്ചു വെച്ചു."),
 ("V","V","ബിനൂ, എണ്ണ നല്ലതല്ലേ? അയാൾക്ക് എന്താ പ്രശ്നം?"),
 ("A","A","എണ്ണയല്ല, ലേബൽ. ലേബലിൽ FSSAI നമ്പർ ഇല്ലെന്ന്."),
 ("V","wide","ശരിയാ. പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഫുഡിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ നിർബന്ധം. എണ്ണയും ഫുഡ് തന്നെ."),
 ("A","A","അപ്പോ കുപ്പി നന്നായാൽ പോരാ."),
 ("V","wide","എണ്ണ ചക്കിൽ, വിശ്വാസം ലേബലിൽ.")],
 "എണ്ണ ചക്കിൽ,\nവിശ്വാസം ലേബലിൽ", CTA_FSSAI, theme="crm",
 cap_ml="മരച്ചക്കിൽ ആട്ടിയ വെളിച്ചെണ്ണയ്ക്ക് സൂപ്പർമാർക്കറ്റ് ഓർഡർ വന്നു, പക്ഷേ ലേബലിൽ FSSAI നമ്പർ ഇല്ലാത്തതുകൊണ്ട് ബയർ കുപ്പി തിരിച്ചു വെച്ചു. പാക്ക് ചെയ്ത ഫുഡിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ നിർബന്ധം. നിങ്ങളുടെ ലേബലിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="A small cold-press coconut oil mill got its first supermarket order, and the buyer handed the bottle back: no FSSAI number on the label. Packaged food, oil included, must carry the 14-digit FSSAI number. Is the number on your label?",
 cap_mg="Marachakkil aattiya velichennakku supermarket order vannu, pakshe label-il FSSAI number illaathathukondu buyer kuppi thirichu vechu. Pack cheytha food-inte label-il 14 akka FSSAI number nirbandham. Ningalude label-il number undo?")

# d904 pattern: wild honey collector, myth as question
duo("fs021", "packaged_food", "B", "rubber", "\"കാട്ടുതേൻ\nപ്രകൃതിയുടേതല്ലേ?\nഅതിന് ലൈസൻസോ?\"", [
 ("A","wide","തോമസേ, കാട്ടിലെ തേൻ ഞാൻ ഉണ്ടാക്കുന്നതല്ലല്ലോ. തേനീച്ചയുടേതാ. അതിന് എന്തിനാ FSSAI?"),
 ("V","V","ജോയീ, തേനീച്ച കുപ്പിയിൽ ആക്കി ലേബൽ ഒട്ടിക്കുന്നില്ലല്ലോ. അത് നീയല്ലേ ചെയ്യുന്നത്?"),
 ("A","A","മാസം 300 കുപ്പി. ടൗണിലെ മൂന്ന് കടകളിൽ."),
 ("V","wide","പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഫുഡിന് 14 അക്ക FSSAI നമ്പർ വേണം. വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി."),
 ("A","A","തേൻ കാട്ടിലേത്, കുപ്പി എന്റേത്."),
 ("V","wide","തേനീച്ചയ്ക്ക് ലൈസൻസ് വേണ്ട, കുപ്പിക്ക് വേണം.")],
 "തേനീച്ചയ്ക്ക് വേണ്ട,\nകുപ്പിക്ക് വേണം", CTA_FOOD, theme="faq",
 cap_ml="കാട്ടുതേൻ പ്രകൃതിയുടേതാണ്, പക്ഷേ കുപ്പിയിലാക്കി ലേബൽ ഒട്ടിച്ച് വിൽക്കുമ്പോൾ അത് പാക്ക് ചെയ്ത ഫുഡ് ആണ്: 14 അക്ക FSSAI നമ്പർ വേണം. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങൾ വാങ്ങുന്ന തേനിന്റെ കുപ്പിയിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="Wild honey comes from the forest, but once you bottle it, label it and sell it, it is packaged food and needs the 14-digit FSSAI number. Basic registration covers turnover up to 12 lakh a year. Does the honey you buy show the number: yes or no?",
 cap_mg="Kaattuthen prakruthiyudethaanu, pakshe kuppiyilaakki label ottichu vilkkumbol athu pack cheytha food aanu: 14 akka FSSAI number venam. Varsham 12 lakh vare turnover-inu basic registration mathi. Ningal vaangunna then-inte kuppiyil number undo?")

# d904 pattern: houseboat cook, new angle
duo("fs022", "cafe_owner", "C", "ferry", "\"കായലിലാ അടുക്കള.\nനിയമം കരയിലല്ലേ?\"", [
 ("A","wide","ടോണീ, നിന്റെ ഹൗസ്ബോട്ടിലെ കരിമീൻ പൊള്ളിച്ചതിന് ടൂറിസ്റ്റുകൾ വേറെ പൈസ തരുന്നുണ്ടല്ലോ. FSSAI ഉണ്ടോ?"),
 ("V","V","മീരേ, അടുക്കള വെള്ളത്തിലാ. ഫുഡ് സേഫ്റ്റി ഓഫീസർ നീന്തി വരുമോ?"),
 ("A","A","ടൂറിസ്റ്റ് റിവ്യൂവിൽ നിന്റെ ബോട്ടിന്റെ പേരും ഫോട്ടോയും ഉണ്ട്. നീന്തേണ്ട കാര്യമില്ല."),
 ("V","wide","ബോട്ടിൽ വിൽക്കുന്നതും ഫുഡ് ബിസിനസ് തന്നെ. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി."),
 ("A","A","ബോട്ട് ഒഴുകും. പിഴ ഒഴുകിപ്പോകില്ല."),
 ("V","wide","കായലിൽ ഒഴുകാം, നിയമത്തിൽ നിന്ന് പറ്റില്ല.")],
 "കായലിൽ ഒഴുകാം,\nനിയമത്തിൽ നിന്നല്ല", CTA_FSSAI, theme="new",
 cap_ml="ഹൗസ്ബോട്ടിൽ ടൂറിസ്റ്റുകൾക്ക് കരിമീൻ പൊള്ളിച്ചത് വിൽക്കുന്നത് വെള്ളത്തിലാണെങ്കിലും ഫുഡ് ബിസിനസ് തന്നെ. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് FSSAI ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങൾ ഹൗസ്ബോട്ടിൽ കഴിച്ചിട്ടുണ്ടോ?",
 cap_en="Selling karimeen fry to tourists on a houseboat is still a food business, even if the kitchen floats. FSSAI basic registration covers turnover up to 12 lakh a year. Ever eaten on a houseboat: yes or no?",
 cap_mg="Houseboat-il tourists-nu karimeen pollichathu vilkkunnathu vellathil aanengilum food business thanne. Varsham 12 lakh vare turnover-inu FSSAI basic registration mathi. Ningal houseboat-il kazhichittundo?")

# d904 pattern: saree shop that also sells jackfruit jam jars
duo("fs023", "home_baker", "A", "textile", "\"സാരിക്കടയിൽ\nചക്കവരട്ടി വിറ്റാൽ\nഅത് ഫുഡ് കടയാകുമോ?\"", [
 ("A","wide","പ്രകാശേ, കല്യാണ സീസണിൽ സാരിക്കൊപ്പം എന്റെ അമ്മയുടെ ചക്കവരട്ടി ജാറും വിൽക്കുന്നില്ലേ? ഇതുവരെ 400 ജാർ പോയി."),
 ("V","V","രമ്യേ, ഇത് സാരിക്കടയാ. ഫുഡ് ലൈസൻസ് ഹോട്ടലുകാർക്കല്ലേ?"),
 ("A","A","കട സാരിയുടേതാകാം. ജാറിനുള്ളിലുള്ളത് ഫുഡ് ആണ്."),
 ("V","wide","വീട്ടിൽ ഉണ്ടാക്കുന്നവർക്കും FSSAI വേണം. വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി, ജാറിൽ 14 അക്ക നമ്പറും."),
 ("A","A","അപ്പോ അമ്മയുടെ പേരിൽ ബേസിക് എടുക്കാം."),
 ("V","wide","സാരി മടക്കി വെക്കാം, നിയമം മടക്കി വെക്കരുത്.")],
 "സാരി മടക്കാം,\nനിയമം മടക്കരുത്", CTA_FOOD, theme="faq",
 cap_ml="സാരിക്കടയുടെ കൗണ്ടറിൽ വീട്ടിലുണ്ടാക്കിയ ചക്കവരട്ടി ജാർ വിൽക്കുന്നുണ്ടോ? വീട്ടിൽ ഉണ്ടാക്കുന്നവർക്കും FSSAI വേണം: വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ, ജാറിൽ 14 അക്ക നമ്പർ. നിങ്ങളുടെ കടയിൽ ഫുഡ് കൂടി വിൽക്കുന്നുണ്ടോ?",
 cap_en="A saree shop sells a mother's homemade jackfruit jam jars at the counter in wedding season. Home makers need FSSAI too: basic registration up to 12 lakh a year, and the 14-digit number on every jar. Does your shop sell food on the side: yes or no?",
 cap_mg="Saree kadayude counter-il veettil undaakkiya chakkavaratti jar vilkkunnundo? Veettil undaakkunnavarkkum FSSAI venam: varsham 12 lakh vare basic registration, jar-il 14 akka number. Ningalude kadayil food koodi vilkkunnundo?")

# crm: campus founders, delivery app asks for the number
duo("fs024", "home_baker", "B", "classroom", "മില്ലറ്റ് കുക്കീസ്\nആപ്പിൽ ലിസ്റ്റ്\nചെയ്യാൻ നോക്കി. നിന്നു", [
 ("A","wide","ആദർശേ, നമ്മുടെ മില്ലറ്റ് കുക്കീസ് ഡെലിവറി ആപ്പിൽ ഇടാൻ നോക്കി. ഫോം പാതിയിൽ നിന്നു."),
 ("V","V","നിമ്മീ, ഹോസ്റ്റലിൽ എല്ലാവർക്കും ഇഷ്ടമായതല്ലേ. ആപ്പ് എന്താ ചോദിച്ചത്?"),
 ("A","A","ഒരു ബോക്സ്: FSSAI നമ്പർ. നമുക്ക് അതില്ല."),
 ("V","wide","ഡെലിവറി ആപ്പുകൾ FSSAI നമ്പർ ചോദിക്കും. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി."),
 ("A","A","റെസിപ്പി റെഡി, നമ്പർ ആയിട്ടില്ല."),
 ("V","wide","ഹോസ്റ്റലിൽ ഹിറ്റ്, ആപ്പിൽ ഹിറ്റാകാൻ നമ്പർ വേണം.")],
 "ഹോസ്റ്റലിൽ ഹിറ്റ്,\nആപ്പിൽ നമ്പർ വേണം", CTA_FSSAI, theme="crm",
 cap_ml="കോളേജ് ടീമിന്റെ മില്ലറ്റ് കുക്കീസ് ഹോസ്റ്റലിൽ ഹിറ്റായി, പക്ഷേ ഡെലിവറി ആപ്പ് FSSAI നമ്പർ ചോദിച്ചപ്പോൾ ലിസ്റ്റിംഗ് നിന്നു. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങളുടെ കോളേജിൽ ഫുഡ് സ്റ്റാർട്ടപ്പ് ഉണ്ടോ?",
 cap_en="A college team's millet cookies were a hit in the hostel, but the delivery app listing stopped at one box: FSSAI number. Basic registration covers turnover up to 12 lakh a year. Is there a food startup in your college: yes or no?",
 cap_mg="College team-inte millet cookies hostel-il hit aayi, pakshe delivery app FSSAI number chodichappol listing ninnu. Varsham 12 lakh vare turnover-inu basic registration mathi. Ningalude college-il food startup undo?")

# crm: small dairy's ghee wins a hotel buffet contract, outgrows basic registration
duo("fs025", "packaged_food", "C", "hotellobby", "ഹോട്ടൽ കോൺട്രാക്ട്.\nനെയ്യ് വിൽപ്പന 7-ൽ\nനിന്ന് 19 ലക്ഷം", [
 ("A","wide","ജെയ്സൺ, ഹോട്ടലിന്റെ ബുഫേയ്ക്ക് വർഷം മുഴുവൻ എന്റെ നാടൻ നെയ്യ്. ഒപ്പിടാൻ റെഡി."),
 ("V","V","നീതൂ, കൺഗ്രാറ്റ്സ്. പക്ഷേ ഇപ്പോ വിൽപ്പന 7 ലക്ഷം, ഇതോടെ 19 ലക്ഷം ആകില്ലേ?"),
 ("A","A","അതെ. എന്റെ കയ്യിൽ ബേസിക് രജിസ്ട്രേഷൻ ഉണ്ടല്ലോ."),
 ("V","wide","ബേസിക് വർഷം 12 ലക്ഷം വരെ മാത്രം. അതിന് മുകളിൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ് വേണം."),
 ("A","A","അപ്പോ കോൺട്രാക്ടിന് മുമ്പ് ലൈസൻസ് മാറ്റണം."),
 ("V","wide","ഓർഡർ വളർന്നാൽ ലൈസൻസും വളരണം.")],
 "ഓർഡർ വളർന്നാൽ\nലൈസൻസും വളരണം", CTA_FSSAI, theme="crm",
 cap_ml="ചെറിയ ഡെയറിയുടെ നാടൻ നെയ്യിന് ഹോട്ടൽ ബുഫേ കോൺട്രാക്ട് കിട്ടി, വിൽപ്പന 7 ലക്ഷത്തിൽ നിന്ന് 19 ലക്ഷം ആകും. FSSAI ബേസിക് രജിസ്ട്രേഷൻ വർഷം 12 ലക്ഷം വരെ മാത്രം; അതിന് മുകളിൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്. നിങ്ങളുടെ അടുത്ത വലിയ ഓർഡർ ഏതാ?",
 cap_en="A small dairy's ghee won a year-round hotel buffet contract that will take sales from 7 lakh to 19 lakh. FSSAI basic registration only covers up to 12 lakh a year; above that, up to 20 crore, you need a state licence. What's your next big order?",
 cap_mg="Cheriya dairy-yude naadan neyyinu hotel buffet contract kitti, vilppana 7 lakhathil ninnu 19 lakh aakum. FSSAI basic registration varsham 12 lakh vare maathram; athinu mukalil 20 kodi vare state licence. Ningalude adutha valiya order ethaa?")

# faq: one-year registration taken last Onam
chat("fsc002", "home_baker", "A", "ഓണം പായസം കിറ്റ്.\nഓർഡർ 200.\nരജിസ്ട്രേഷൻ തീരുന്നു", ("അശ്വതി", "ഉണ്ണി"), [
 (0,"ഉണ്ണീ, ഈ ഓണത്തിന് പായസം കിറ്റിന് 200 ഓർഡർ ആയി!"),
 (1,"അശ്വതീ, സൂപ്പർ. FSSAI സർട്ടിഫിക്കറ്റിൽ തീയതി ഒന്ന് നോക്ക്."),
 (0,"കഴിഞ്ഞ ഓണത്തിന് എടുത്തതാ. ഒരിക്കൽ എടുത്താൽ മതിയല്ലോ?"),
 (1,"അല്ല. 1 മുതൽ 5 വർഷം വരെയാണ് കാലാവധി. നീ എടുത്തത് ഒരു വർഷത്തേക്ക്. തീരും മുമ്പ് പുതുക്കണം."),
 (0,"നോക്കി... അടുത്ത ആഴ്ച തീരും!"),
 (1,"പായസം തിളയ്ക്കും മുമ്പ് പുതുക്കൽ.")],
 "പായസം തിളയ്ക്കും\nമുമ്പ് പുതുക്കൽ", CTA_FOOD, theme="faq",
 cap_ml="കഴിഞ്ഞ ഓണത്തിന് എടുത്ത FSSAI രജിസ്ട്രേഷൻ ഒരു വർഷത്തേക്ക് ആയിരുന്നു, ഈ ഓണത്തിന്റെ 200 ഓർഡറിന് ഒരാഴ്ച മുമ്പ് തീരുന്നു. FSSAI 1 മുതൽ 5 വർഷം വരെ സാധുവാണ്; തീരും മുമ്പ് പുതുക്കണം. നിങ്ങളുടേത് എത്ര വർഷത്തേക്കാ?",
 cap_en="A home cook's FSSAI registration, taken last Onam for one year, expires a week before this Onam's 200 payasam-kit orders. FSSAI registration is valid for 1 to 5 years and must be renewed before expiry. How many years did you take yours for?",
 cap_mg="Kazhinja Onathinu eduttha FSSAI registration oru varshathekku aayirunnu, ee Onathinte 200 order-inu oraazhcha mumpu theerunnu. FSSAI 1 muthal 5 varsham vare saadhuvaanu; theerum mumpu puthukkanam. Ningaludethu ethra varshathekkaa?")

# faq: profit vs turnover
duo("fs026", "cafe_owner", "B", "bakery", "\"ലാഭം 9 ലക്ഷമേ ഉള്ളൂ.\nബേസിക് മതിയല്ലോ?\"", [
 ("A","wide","സാബൂ, ഈ വർഷം ലാഭം 9 ലക്ഷമേ ഉള്ളൂ. 12 ലക്ഷത്തിന് താഴെ, അപ്പോ ബേസിക് രജിസ്ട്രേഷൻ മതിയല്ലോ?"),
 ("V","V","ജിഷേ, ലാഭമല്ല നോക്കുന്നത്. ബേക്കറിയുടെ മൊത്തം വിൽപ്പന എത്രയാ?"),
 ("A","A","ബില്ലെല്ലാം കൂട്ടിയാൽ... 26 ലക്ഷം."),
 ("V","wide","12 ലക്ഷം പരിധി ടേൺഓവറിനാ, ലാഭത്തിനല്ല. 12 ലക്ഷം കടന്നാൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്."),
 ("A","A","അപ്പോ പോക്കറ്റിൽ വന്നതല്ല, കൗണ്ടറിൽ വന്നതാ കണക്ക്."),
 ("V","wide","ലാഭം നിങ്ങളുടേത്, ടേൺഓവർ നിയമത്തിന്റേത്.")],
 "ലാഭം നിങ്ങളുടേത്,\nടേൺഓവർ നിയമത്തിന്റേത്", CTA_FSSAI, theme="faq",
 cap_ml="FSSAI ബേസിക് രജിസ്ട്രേഷന്റെ 12 ലക്ഷം പരിധി ലാഭത്തിനല്ല, വർഷത്തെ മൊത്തം ടേൺഓവറിനാണ്. ലാഭം 9 ലക്ഷമായാലും വിൽപ്പന 26 ലക്ഷമെങ്കിൽ 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ് വേണം. നിങ്ങൾ നോക്കിയത് ലാഭമോ ടേൺഓവറോ?",
 cap_en="The 12 lakh limit for FSSAI basic registration is about yearly turnover, not profit. A bakery with 9 lakh profit but 26 lakh in sales needs a state licence (up to 20 crore). Which did you check: profit or turnover?",
 cap_mg="FSSAI basic registration-nte 12 lakh paridhi laabhathinalla, varshathe mottham turnover-inaanu. Laabham 9 lakh aayaalum vilppana 26 lakh engil 20 kodi vare state licence venam. Ningal nokkiyathu laabhamo turnover-o?")

# crm: canteen contractor "starting soon", licence later
duo("fs027", "cloud_kitchen", "C", "canteen", "\"ടെൻഡർ കിട്ടിയിട്ട്\nലൈസൻസ് എടുക്കാം\"", [
 ("A","wide","അമലേ, ഐടി പാർക്കിലെ കാന്റീൻ ടെൻഡർ കിട്ടിയാൽ തിങ്കളാഴ്ച മുതൽ 600 ഊണ് ദിവസം."),
 ("V","V","ആതിരേ, FSSAI ടെൻഡർ കിട്ടിയിട്ട് എടുക്കാം. ആദ്യം പാചകം തുടങ്ങട്ടെ."),
 ("A","A","അപ്പോ ലൈസൻസ് വരുന്നത് വരെ വിൽക്കുന്ന ഊണോ?"),
 ("V","wide","ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 ("A","A","ആദ്യത്തെ ഊണിന് മുമ്പ് നമ്പർ."),
 ("V","wide","അടുപ്പ് കത്തും മുമ്പ് ലൈസൻസ് കയ്യിൽ വേണം.")],
 "അടുപ്പിന് മുമ്പ്\nലൈസൻസ്", CTA_FOOD, theme="crm",
 cap_ml="കാന്റീൻ ടെൻഡർ കിട്ടിയ ശേഷം FSSAI എടുക്കാം എന്നാണോ പ്ലാൻ? ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. ആദ്യത്തെ ഊണിന് മുമ്പ് നമ്പർ വേണം. നിങ്ങളുടെ ഓഫീസ് കാന്റീനിൽ നമ്പർ കണ്ടിട്ടുണ്ടോ?",
 cap_en="Planning to get FSSAI only after the canteen tender is won? Selling food without it can mean a penalty up to 5 lakh and up to 6 months in prison, so the number comes before the first meal is served. Seen an FSSAI number in your office canteen: yes or no?",
 cap_mg="Canteen tender kittiya shesham FSSAI edukkaam ennaano plan? Licence illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Aadyathe oonu-nu mumpu number venam. Ningalude office canteen-il number kandittundo?")

# d904 pattern: ice-candy cart, myth as question
duo("fs028", "cafe_owner", "A", "beach", "\"കോലൈസ് വെറും\nഐസും സിറപ്പും.\nഅത് ഫുഡ് ആണോ?\"", [
 ("A","wide","നിഖിലേ, ബീച്ചിൽ നിന്റെ കോലൈസ് വണ്ടിക്ക് മുന്നിൽ എന്നും ക്യൂ ആണല്ലോ. FSSAI എടുത്തോ?"),
 ("V","V","ദിവ്യേ, ഐസും സിറപ്പും മാത്രം. അത് ഫുഡ് ആണോ?"),
 ("A","A","കുട്ടികൾ വായിൽ ഇടുന്നതെല്ലാം ഫുഡ് ആണ്, നിഖിലേ."),
 ("V","wide","ശരിയാ. വർഷം 12 ലക്ഷം വരെ ബേസിക് രജിസ്ട്രേഷൻ മതി. ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ."),
 ("A","A","ഐസ് ഉരുകും. പിഴ ഉരുകില്ല."),
 ("V","wide","കോലൈസ് തണുത്തതാവാം, നിയമം ചൂടാ.")],
 "കോലൈസ് തണുപ്പ്,\nനിയമം ചൂട്", CTA_FSSAI, theme="new",
 cap_ml="ബീച്ചിലെ കോലൈസ് വണ്ടി 'ഐസും സിറപ്പും മാത്രം' എന്ന് കരുതി FSSAI എടുത്തില്ല. വർഷം 12 ലക്ഷം വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി; ഇല്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങളുടെ ഇഷ്ട കോലൈസ് ഫ്ലേവർ ഏതാ?",
 cap_en="A beach ice-candy cart thought 'it's just ice and syrup' and never took FSSAI. Basic registration covers turnover up to 12 lakh a year; selling food without it can mean a penalty up to 5 lakh. Your favourite ice-candy flavour?",
 cap_mg="Beach-ile kolice vandi 'ice-um syrup-um maathram' ennu karuthi FSSAI eduthilla. Varsham 12 lakh vare turnover-inu basic registration mathi; illaathe food vittaal 5 lakh vare pizha. Ningalude ishta kolice flavour ethaa?")
