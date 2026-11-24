# FSSAI batch 04 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# d904 pattern: seasonal festival stall

# d904 pattern: gym-made protein laddoos
duo("fs011", "packaged_food", "B", "gym", "\"ജിമ്മിലെ പിള്ളേർക്ക്\nമാത്രമല്ലേ വിൽക്കുന്നത്?\"\nമാസം 200 പാക്കറ്റ്", [
 ("A","wide","ജസ്റ്റിൻ, കൗണ്ടറിൽ വെച്ച ആ പ്രോട്ടീൻ ലഡ്ഡു പാക്കറ്റിൽ FSSAI നമ്പർ കാണുന്നില്ലല്ലോ."),
 ("V","V","റിയാ, ജിമ്മിലെ മെമ്പർമാർക്ക് മാത്രമല്ലേ. മാസം 200 പാക്കറ്റ്. കടയിൽ വെക്കുന്നില്ലല്ലോ."),
 ("A","A","ആർക്ക് വിൽക്കുന്നു എന്നല്ല, പാക്കറ്റിലാക്കി വിൽക്കുന്നു എന്നതാണ് കാര്യം."),
 ("V","wide","അപ്പോ എന്താ ചെയ്യേണ്ടത്?"),
 ("A","wide","ബേസിക് രജിസ്ട്രേഷൻ എടുക്കണം. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക FSSAI നമ്പർ പ്രിന്റ് ചെയ്യണം."),
 ("V","V","മസിലിന് പ്രോട്ടീൻ, പാക്കറ്റിന് നമ്പർ.")],
 "പാക്കറ്റിൽ വിറ്റാൽ\n14 അക്ക നമ്പർ", CTA_FSSAI, theme="new",
 cap_ml="ജിമ്മിലെ അംഗങ്ങൾക്ക് മാത്രം വിൽക്കുന്ന വീട്ടിലുണ്ടാക്കിയ പ്രോട്ടീൻ ലഡ്ഡുവിനും FSSAI വേണം. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം. നിങ്ങളുടെ ജിമ്മിൽ ഇങ്ങനെ വിൽക്കുന്നുണ്ടോ?",
 cap_en="Homemade protein laddoos sold only to gym members still need FSSAI. Packaged food must carry the 14-digit FSSAI number. Does your gym sell snacks like this?",
 cap_mg="Gym members-nu maathram vilkkunna protein laddu-vinum FSSAI venam. Pack cheytha food-il 14 akka number print cheyyanam. Ningalude gym-il ingane vilkkunnundo?")

# CRM #4 / #26 (returnee starting a food business), changed sector and numbers

# CRM #29 (woman founder, health food, incubation), changed product and numbers
duo("fs013", "packaged_food", "B", "rooftop", "ഡെമോ ഡേയിൽ ബയർ\n500 പാക്കറ്റ് ചോദിച്ചു.\nലേബലിൽ നമ്പർ ഇല്ല", [
 ("A","wide","ശ്യാം, ഡെമോ ഡേയിൽ ഒരു സൂപ്പർമാർക്കറ്റ് ബയർ നമ്മുടെ റാഗി മിക്സ് 500 പാക്കറ്റ് ചോദിച്ചു!"),
 ("V","V","ആര്യേ, സൂപ്പർ! ഡെലിവറി എന്നാ?"),
 ("A","A","ആദ്യം ലേബലിലെ FSSAI നമ്പർ അയക്കാൻ പറഞ്ഞു. നമ്മുടെ പാക്കറ്റിൽ അതില്ല."),
 ("V","wide","പാക്ക് ചെയ്ത ഭക്ഷണത്തിന് 14 അക്ക നമ്പർ ലേബലിൽ നിർബന്ധം. ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ പ്രിന്റ്."),
 ("A","wide","അപ്പോ 500 ലേബലും വീണ്ടും അടിക്കണം."),
 ("V","V","നമ്പർ ആദ്യം, പാക്കറ്റ് പിന്നെ.")],
 "ലേബൽ അടിക്കും മുമ്പ്\nFSSAI നമ്പർ", CTA_FOOD, theme="crm",
 cap_ml="ഇൻകുബേറ്റർ ഡെമോ ഡേയിൽ സൂപ്പർമാർക്കറ്റ് 500 പാക്കറ്റ് റാഗി മിക്സ് ചോദിച്ചു, പക്ഷേ ലേബലിൽ FSSAI നമ്പർ ഇല്ല. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ നിർബന്ധം. നിങ്ങളുടെ ലേബലിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="At an incubator demo day a supermarket asked for 500 packs of a ragi mix, but the label had no FSSAI number. Packaged food must carry the 14-digit number. Is it on your label?",
 cap_mg="Incubator demo day-il supermarket 500 packet ragi mix chodichu, pakshe label-il FSSAI number illa. Pack cheytha food-il 14 akka number nirbandham. Ningalude label-il number undo?")

# CRM #21 (farm switching to a new product), d904 pattern: mushroom pickle

# CRM #20 (investor asks for a data room), cloud kitchen with an expired licence

# FAQ: "only on Instagram, so no FSSAI"

# FAQ: small importer assumes basic is enough

# d904 pattern: railway platform snack packets
duo("fs018", "home_baker", "B", "railway", "\"ട്രെയിനിൽ ആര്\nലേബൽ വായിക്കാനാ?\"\nദിവസം 100 പാക്കറ്റ്", [
 ("A","wide","ദിനേശേട്ടാ, പ്ലാറ്റ്ഫോമിലെ സ്റ്റാളിൽ നമ്മുടെ ഇലയട പാക്കറ്റ് ദിവസം 100 എണ്ണം പോകുന്നുണ്ട്."),
 ("V","V","ഷീബേ, നല്ലത്. പാക്കറ്റിൽ FSSAI നമ്പർ ഉണ്ടോ?"),
 ("A","A","ട്രെയിൻ പിടിക്കാൻ ഓടുന്നവർ ലേബൽ വായിക്കുമോ? ആരും നോക്കില്ല."),
 ("V","wide","യാത്രക്കാരൻ നോക്കിയില്ലെങ്കിലും നിയമം നോക്കും. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ വേണം. ഇല്ലെങ്കിൽ 5 ലക്ഷം വരെ പിഴ."),
 ("A","wide","അപ്പോ ആദ്യം രജിസ്ട്രേഷൻ, പിന്നെ പുതിയ ലേബൽ."),
 ("V","V","ട്രെയിൻ ഓടും, പിഴ കാത്തുനിൽക്കും.")],
 "ആരും വായിച്ചില്ലെങ്കിലും\nനമ്പർ വേണം", CTA_FOOD, theme="faq",
 cap_ml="റെയിൽവേ സ്റ്റാളിൽ ദിവസം 100 ഇലയട പാക്കറ്റ് വിൽക്കുന്നു, ലേബലിൽ FSSAI നമ്പർ ഇല്ല. പാക്ക് ചെയ്ത ഭക്ഷണത്തിൽ 14 അക്ക നമ്പർ നിർബന്ധം; ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ. നിങ്ങൾ ലേബൽ വായിക്കാറുണ്ടോ?",
 cap_en="A home cook sells 100 packets of ela ada a day at a railway stall, with no FSSAI number on the label. Packaged food must carry the 14-digit number; selling without registration can mean a penalty of up to 5 lakh. Do you read food labels?",
 cap_mg="Railway stall-il divasam 100 elayada packet vilkkunnu, label-il FSSAI number illa. Pack cheytha food-il 14 akka number nirbandham; illaathe vittaal 5 lakh vare pizha. Ningal label vaayikkaarundo?")

# FAQ: "first time it's only a warning"
chat("fs019", "cloud_kitchen", "C", "\"ആദ്യം പിടിച്ചാൽ\nവാണിംഗ് മാത്രം\"\nശരിക്കും?", ("ഹന്ന", "ഫഹദ്"), [
 (1,"ഹന്നാ, ക്ലൗഡ് കിച്ചൺ തുടങ്ങി 3 മാസമായി. FSSAI ഇപ്പോഴും ആയിട്ടില്ല."),
 (0,"ഫഹദേ, ഇതുവരെ അപേക്ഷിച്ചില്ലേ?"),
 (1,"ആദ്യം പിടിച്ചാൽ വാണിംഗ് മാത്രം എന്നാ എല്ലാരും പറയുന്നേ."),
 (0,"എല്ലാരും പറയുന്നത് നിയമമല്ല. ലൈസൻസ് ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 (1,"ശരി. ഇന്ന് തന്നെ അപേക്ഷിക്കാം."),
 (0,"വാണിംഗ് കേട്ടുകേൾവി, പിഴ നിയമം.")],
 "കേട്ടുകേൾവി വിട്ട്\nരജിസ്ട്രേഷൻ എടുക്കൂ", CTA_FSSAI, theme="faq",
 cap_ml="\"ആദ്യം പിടിച്ചാൽ വാണിംഗ് മാത്രം\" എന്ന് കരുതി FSSAI ഇല്ലാതെ ക്ലൗഡ് കിച്ചൺ നടത്തരുത്. ലൈസൻസ് ഇല്ലാതെ ഭക്ഷണം വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. ഈ കേട്ടുകേൾവി നിങ്ങൾ കേട്ടിട്ടുണ്ടോ?",
 cap_en="Don't run a cloud kitchen without FSSAI on the belief that the first time is only a warning. Selling food without a licence can mean a penalty of up to 5 lakh and up to 6 months in prison. Have you heard this myth?",
 cap_mg="\"Aadyam pidichaal warning maathram\" ennu karuthi FSSAI illaathe cloud kitchen nadatharuthu. Licence illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Ee kettukelvi ningal kettittundo?")
