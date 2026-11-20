# Trademark batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_TM. Never promise registration or mention fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

# CRM #20 (investor asks for a data room) + F5: the brand behind the company name
duo("tm022", "d2c_brand", "A", "hotellobby", "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"ബ്രാൻഡ് ട്രേഡ്മാർക്ക്\nകോപ്പി എവിടെ?\"", [
 ("A","wide","ജെയ്സാ, ഇൻവെസ്റ്റർ ഡാറ്റാ റൂമിൽ നമ്മുടെ മില്ലറ്റ് ബാർ ബ്രാൻഡിന്റെ ട്രേഡ്മാർക്ക് കോപ്പി ചോദിച്ചു."),
 ("V","V","നീതൂ, കമ്പനി പേര് അപ്രൂവൽ ലെറ്റർ ഇട്ടാൽ പോരേ? അതേ പേര് തന്നെയല്ലേ?"),
 ("A","A","ഞാനും അങ്ങനെയാ കരുതിയത്. പക്ഷേ അവർ ചോദിച്ചത് ബ്രാൻഡിന്റെ രേഖയാ."),
 ("V","wide","കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. ബ്രാൻഡിന് ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ വേറെ ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ ആദ്യം ഫയലിംഗ്, പിന്നെ ഡാറ്റാ റൂം."),
 ("V","V","പേര് കമ്പനിക്ക്, ബ്രാൻഡ് ഇനിയും ആർക്കുമല്ല.")],
 "കമ്പനി പേര് കിട്ടിയാലും\nബ്രാൻഡ് സുരക്ഷിതമല്ല", CTA_TRADEMARK, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റാ റൂമിൽ ബ്രാൻഡിന്റെ ട്രേഡ്മാർക്ക് രേഖ ചോദിച്ചപ്പോൾ ഫൗണ്ടർ കൊടുത്തത് കമ്പനി പേര് അപ്രൂവൽ. അത് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല; ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ വേറെ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ ബ്രാൻഡ് ഫയൽ ചെയ്തോ?",
 cap_en="An investor's data room asked for the brand's trademark papers, and the founder only had the company name approval. A company name approval does not protect a brand: the trademark is filed separately with the Trade Marks Registry. Is your brand filed: yes or no?",
 cap_mg="Investor data room-il brand-inte trademark rekha chodichappol founder koduthathu company name approval. Athu brand-ine samrakshikkilla; Trade Marks Registry-il vere file cheyyanam. Ningalude brand file cheytho?")

# CRM C13 (founders abroad bringing something to Kerala): a Gulf restaurant name
duo("tm023", "food_brand", "B", "gulfroom", "\"ദുബായിൽ 3 ഷോപ്പ്.\nകൊച്ചിയിലും അതേ പേര്.\nപ്രശ്നമില്ലല്ലോ?\"", [
 ("A","wide","ഷംസൂ, നമ്മുടെ കുഴിമന്തി ഷോപ്പിന്റെ പേര് ദുബായിൽ എല്ലാർക്കും അറിയാം. കൊച്ചിയിലും അതേ പേരിൽ തുറക്കാം."),
 ("V","V","നസീറേ, കൊച്ചിയിൽ ആ പേര് ആരെങ്കിലും ഫയൽ ചെയ്തിട്ടുണ്ടോ എന്ന് നോക്കിയോ?"),
 ("A","A","ദുബായിലെ പേപ്പർ എല്ലാം നമ്മുടെ കയ്യിലുണ്ടല്ലോ."),
 ("V","wide","നാട്ടിൽ ബ്രാൻഡ് സംരക്ഷിക്കാൻ ഇന്ത്യയിലെ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യണം, റെസ്റ്റോറന്റ് സർവീസിന്റെ ക്ലാസിൽ."),
 ("A","A","അപ്പോ ബോർഡ് പണിയുന്നതിന് മുമ്പ് ഫയലിംഗ്."),
 ("V","V","മന്തി ദുബായിൽ നിന്ന് വരും, പേര് ഇവിടെ ഫയൽ ചെയ്യണം.")],
 "നാട്ടിലെ ബ്രാൻഡിന്\nനാട്ടിൽ ഫയലിംഗ്", CTA_BRAND, theme="crm",
 cap_ml="ഗൾഫിൽ അറിയപ്പെടുന്ന റെസ്റ്റോറന്റ് പേര് കേരളത്തിലേക്ക് കൊണ്ടുവരുമ്പോൾ, ഇന്ത്യയിലെ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ റെസ്റ്റോറന്റ് സർവീസിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യണം. ഗൾഫിൽ നിന്ന് നാട്ടിലേക്ക് എന്ത് ബിസിനസ്?",
 cap_en="Bringing a restaurant name that is known in the Gulf to Kerala? To protect it here, file with India's Trade Marks Registry in the class for restaurant services. What business are you bringing home?",
 cap_mg="Gulf-il ariyappedunna restaurant peru Kerala-yilekku konduvarumpol, India-yile Trade Marks Registry-il restaurant service class-il file cheyyanam. Gulf-il ninnu naattilekku enthu business?")

# CRM C4 (two related businesses, only one protected): car service vs car-care bottles
duo("tm024", "d2c_brand", "C", "garage", "സർവീസ് സെന്ററിന്\nട്രേഡ്മാർക്ക് ഉണ്ട്.\nഷാംപൂ കുപ്പിക്ക് ഇല്ല", [
 ("A","wide","ജിതിനേ, നമ്മുടെ കാർ ഷാംപൂ 2,000 കുപ്പി റെഡി. ഗാരേജിന്റെ അതേ പേര്, ട്രേഡ്മാർക്ക് ഉള്ള പേര്."),
 ("V","V","ഐശ്വര്യേ, ആ ട്രേഡ്മാർക്ക് ഏത് ക്ലാസിലാ? കാർ റിപ്പയർ സർവീസിന് അല്ലേ?"),
 ("A","A","അതെ. ഷാംപൂവും നമ്മുടെ തന്നെയല്ലേ, അതും അതിൽ പെടില്ലേ?"),
 ("V","wide","ഇല്ല. 45 ക്ലാസുണ്ട്. സർവീസ് ഒരു ക്ലാസ്, കുപ്പിയിലെ ഉൽപ്പന്നം വേറെ ക്ലാസ്. ഓരോന്നിലും ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ ഷാംപൂവിന്റെ ക്ലാസിൽ കൂടി ഫയൽ ചെയ്യാം."),
 ("V","V","കാർ കഴുകാം, ക്ലാസ് കഴുകിക്കളയരുത്.")],
 "സർവീസ് ഒരു ക്ലാസ്\nഉൽപ്പന്നം വേറെ ക്ലാസ്", CTA_TRADEMARK, theme="crm",
 cap_ml="കാർ സർവീസ് സെന്ററിന്റെ ട്രേഡ്മാർക്ക് സർവീസ് ക്ലാസിൽ മാത്രം. അതേ പേരിലെ കാർ ഷാംപൂ കുപ്പികൾ വേറെ ക്ലാസാണ്. 45 ക്ലാസിൽ നിന്ന് നിങ്ങൾ കച്ചവടം ചെയ്യുന്ന ഓരോന്നിലും ഫയൽ ചെയ്യണം. സർവീസോ ഉൽപ്പന്നമോ?",
 cap_en="A car service centre's trademark covers the repair service class only; car shampoo bottles under the same name fall in another class. Out of 45 classes, file in each one you trade in. Service or product?",
 cap_mg="Car service centre-inte trademark service class-il maathram. Athe perile car shampoo kuppikal vere class aanu. 45 class-il ningal kachavadam cheyyunna oronnilum file cheyyanam. Service-o product-o?")

# CRM C1 (brand used for ~20 years, never registered), d904 pattern: station snack stall
duo("tm025", "food_brand", "A", "railway", "19 വർഷം സ്റ്റേഷനിലെ\nഉണ്ണിയപ്പം ബ്രാൻഡ്.\nട്രേഡ്മാർക്ക്? ഇല്ല", [
 ("A","wide","ദിനേശേട്ടാ, ഒരു ചെയിൻ നമ്മുടെ ഉണ്ണിയപ്പം ബ്രാൻഡ് ഏറ്റെടുക്കാൻ വരുന്നു. ആദ്യം ചോദിച്ചത് ട്രേഡ്മാർക്ക് സർട്ടിഫിക്കറ്റ്."),
 ("V","V","ഷീബേ, 19 വർഷമായി എല്ലാ ട്രെയിനിലും ആളുകൾക്ക് നമ്മുടെ പേര് അറിയാം. അത് പോരേ?"),
 ("A","A","അവർക്ക് വേണ്ടത് പേപ്പറാ. നമ്മുടെ കയ്യിൽ ഉള്ളത് കടയുടെ ലൈസൻസ് മാത്രം."),
 ("V","wide","എങ്കിൽ ഇന്ന് തന്നെ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യാം. ഫയൽ ചെയ്താൽ TM ഇടാം, രജിസ്റ്റർ ആയാൽ R."),
 ("A","A","പേര് എല്ലാ കംപാർട്ട്മെന്റിലും ഉണ്ട്, പക്ഷേ ഒരു ഫയലിലും ഇല്ല."),
 ("V","V","പേരിന് 19 വയസ്സ്, രേഖയ്ക്ക് പൂജ്യം.")],
 "പ്രശസ്തി രേഖയല്ല\nആദ്യം ഫയലിംഗ്", CTA_BRAND, theme="crm",
 cap_ml="റെയിൽവേ സ്റ്റേഷനിലെ 19 വർഷം പഴയ ഉണ്ണിയപ്പം ബ്രാൻഡ് ഒരു ചെയിൻ ഏറ്റെടുക്കാൻ വന്നപ്പോൾ ട്രേഡ്മാർക്ക് ഇല്ല. പ്രശസ്തി രേഖയല്ല: ഫയൽ ചെയ്താൽ TM, രജിസ്റ്റർ ആയാൽ മാത്രം R. നിങ്ങളുടെ ബ്രാൻഡിന് എത്ര വയസ്സ്?",
 cap_en="A 19-year-old railway-station snack brand had no trademark when a chain came to take it over. Fame is not a paper: you can use TM once you file, and R only after registration. How old is your brand?",
 cap_mg="Railway station-ile 19 varsham pazhaya unniyappam brand oru chain etteduthan vannappol trademark illa. Prasasthi rekhayalla: file cheythaal TM, register aayaal maathram R. Ningalude brand-inu ethra vayassu?")

# F: "do I have to wait for registration before I launch with my brand?"
duo("tm026", "d2c_brand", "B", "balcony", "\"രജിസ്ട്രേഷൻ കിട്ടും വരെ\nലോഞ്ച് ഇല്ല\"\n8 മാസം കാത്തിരുന്നു", [
 ("A","wide","വിവേകേ, മെഴുകുതിരി ബ്രാൻഡ് ഫയൽ ചെയ്തിട്ട് 8 മാസമായി. രജിസ്ട്രേഷൻ വരാതെ ലോഞ്ച് ചെയ്യാൻ പേടി."),
 ("V","V","അമ്മൂ, ഫയൽ ചെയ്ത ദിവസം മുതൽ ലേബലിൽ TM ഇടാമല്ലോ."),
 ("A","A","അപ്പോ R ചിഹ്നത്തിന് വേണ്ടിയാണോ ഞാൻ ഇത്രയും കാത്തത്?"),
 ("V","wide","അതെ. R രജിസ്ട്രേഷന് ശേഷം മാത്രം. TM ഇട്ട് വിൽക്കാൻ ഫയലിംഗ് മതി."),
 ("A","A","അപ്പോ ദീപാവലിക്ക് മുമ്പ് ലോഞ്ച്."),
 ("V","V","തിരി കത്തിക്കാൻ R നോക്കേണ്ട, TM മതി.")],
 "ഫയൽ ചെയ്താൽ TM\nകാത്തിരിക്കേണ്ടത് R-ന്", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തിട്ട് രജിസ്ട്രേഷൻ വരും വരെ ലോഞ്ച് നീട്ടേണ്ടതില്ല. ഫയൽ ചെയ്താൽ TM ഇടാം; R ചിഹ്നം മാത്രമാണ് രജിസ്ട്രേഷൻ വരെ കാത്തിരിക്കേണ്ടത്. നിങ്ങളുടെ ലോഞ്ച് എന്തിന് വേണ്ടി കാത്തിരിക്കുന്നു?",
 cap_en="A candle brand delayed its launch for 8 months waiting for trademark registration. Once you have filed, you can use TM on the label; only the R symbol waits for registration. What is holding your launch back?",
 cap_mg="Trademark file cheythittu registration varum vare launch neettendathilla. File cheythaal TM idaam; R symbol maathramaanu registration vare kaathirikkendathu. Ningalude launch enthinu vendi kaathirikkunnu?")

# F: "I bought the domain, so the name is mine?"
duo("tm027", "app_founder", "A", "metro", "ഡൊമെയ്ൻ വാങ്ങി.\nഹാൻഡിലും കിട്ടി.\nപേര് നമ്മുടേതായോ?", [
 ("A","wide","കിരണേ, ആപ്പിന്റെ ഡൊമെയ്നും ഇൻസ്റ്റാഗ്രാം ഹാൻഡിലും കിട്ടി. പേര് ഇനി നമ്മുടേതാ!"),
 ("V","V","അഞ്ജലീ, ആ പേര് ട്രേഡ്മാർക്കായി ആരെങ്കിലും ഫയൽ ചെയ്തിട്ടുണ്ടോ എന്ന് നോക്കിയോ?"),
 ("A","A","ഡൊമെയ്ൻ ഫ്രീ ആയിരുന്നല്ലോ, അപ്പോ ആരും എടുത്തിട്ടില്ലല്ലോ."),
 ("V","wide","ഡൊമെയ്നോ കമ്പനി പേരോ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. ആപ്പിന്റെ ക്ലാസിൽ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ അടുത്ത സ്റ്റേഷന് മുമ്പ് സെർച്ച് ചെയ്യാം."),
 ("V","V","ഡൊമെയ്ൻ വാടകയ്ക്ക്, ബ്രാൻഡ് സ്വന്തമാക്കണം.")],
 "ഡൊമെയ്ൻ ബ്രാൻഡ് അല്ല\nട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യൂ", CTA_BRAND, theme="faq",
 cap_ml="ഡൊമെയ്നും ഇൻസ്റ്റാഗ്രാം ഹാൻഡിലും കിട്ടിയാൽ പേര് നിങ്ങളുടേതാകില്ല. ആപ്പ് പ്രവർത്തിക്കുന്ന ക്ലാസിൽ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യണം. ആദ്യം വാങ്ങിയത് ഡൊമെയ്നോ ട്രേഡ്മാർക്കോ?",
 cap_en="Getting the domain and the Instagram handle does not make a name yours. A domain or a company name does not protect a brand: file the trademark with the Trade Marks Registry in the class your app works in. What did you get first: domain or trademark?",
 cap_mg="Domain-um Instagram handle-um kittiyaal peru ningaludethaakilla. App pravarthikkunna class-il Trade Marks Registry-il file cheyyanam. Aadyam vaangiyathu domain-o trademark-o?")

# F: "registered, so R goes on everything I sell?"
duo("tm028", "d2c_brand", "C", "rooftop", "വിത്തിന് R കിട്ടി.\nചെടിച്ചട്ടിയിലും\nR അടിച്ചാലോ?", [
 ("A","wide","ശ്യാമേ, നമ്മുടെ ടെറസ് ഗാർഡൻ വിത്ത് ബ്രാൻഡ് രജിസ്റ്റർ ആയി! പുതിയ ചെടിച്ചട്ടിയിലും R അടിക്കാം."),
 ("V","V","ആര്യേ, രജിസ്ട്രേഷൻ ഏത് ക്ലാസിലാ? വിത്തിന്റെ ക്ലാസിൽ മാത്രമല്ലേ?"),
 ("A","A","പേര് ഒന്നല്ലേ. ചട്ടിക്കും അത് മതിയാകില്ലേ?"),
 ("V","wide","R രജിസ്റ്റർ ആയ ക്ലാസിലെ ഉൽപ്പന്നത്തിന് മാത്രം. ചട്ടി വേറെ ക്ലാസ്; അവിടെ ഫയൽ ചെയ്താൽ TM ഇടാം."),
 ("A","A","അപ്പോ ചട്ടിക്ക് പുതിയ ഫയലിംഗ്, അതുവരെ TM."),
 ("V","V","വിത്തിന് R, ചട്ടിക്ക് ക്ഷമ.")],
 "R രജിസ്റ്റർ ആയ\nക്ലാസിൽ മാത്രം", CTA_TRADEMARK, theme="faq",
 cap_ml="വിത്തിന്റെ ക്ലാസിൽ രജിസ്റ്റർ ആയ ബ്രാൻഡിന്റെ R ചിഹ്നം ചെടിച്ചട്ടിയിൽ ഇടാൻ പറ്റില്ല. ചട്ടി വേറെ ക്ലാസ്: അവിടെ ഫയൽ ചെയ്താൽ TM, രജിസ്റ്റർ ആയാൽ R. നിങ്ങളുടെ അടുത്ത ഉൽപ്പന്നം ഏത്?",
 cap_en="A seed brand registered in its class cannot put R on its new flower pots: pots are a different class. File there to use TM, and R comes only after that registration. What is your next product?",
 cap_mg="Vithinte class-il register aaya brand-inte R symbol chedichattiyil idaan pattilla. Chatti vere class: avide file cheythaal TM, register aayaal R. Ningalude adutha product etha?")

# F14-style myth "small businesses don't need a trademark", d904 pattern: a famous night food stall
duo("tm029", "food_brand", "A", "thattukada", "\"തട്ടുകടയ്ക്ക് എന്ത്\nട്രേഡ്മാർക്ക്?\"\nഅടുത്ത ടൗണിൽ അതേ പേര്", [
 ("A","wide","ബിജൂ, നമ്മുടെ തട്ടുകടയുടെ പേരിൽ അടുത്ത ടൗണിൽ ഒരു റെസ്റ്റോറന്റ് തുടങ്ങി. ബോർഡ് പോലും കോപ്പി."),
 ("V","V","സിജോ, തട്ടുകടയ്ക്ക് ട്രേഡ്മാർക്ക് ഒന്നും വേണ്ടെന്നല്ലേ നീ പറഞ്ഞത്?"),
 ("A","A","അത് വലിയ കമ്പനികൾക്ക് മാത്രമാണെന്നാ ഞാൻ കരുതിയത്."),
 ("V","wide","ഭക്ഷണം വിളമ്പുന്ന സർവീസിനും ക്ലാസുണ്ട്. ആ ക്ലാസിൽ ഫയൽ ചെയ്താൽ മാത്രമേ പേരിന് സംരക്ഷണമുള്ളൂ."),
 ("A","A","ഇന്ന് രാത്രി ദോശ ചുടുന്നതിന് മുമ്പ് ഫയലിംഗ്."),
 ("V","V","കട ചെറുതാകാം, പേര് ചെറുതല്ല.")],
 "ചെറിയ കടയ്ക്കും\nവലിയ പേര് കാക്കണം", CTA_BRAND, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് വലിയ കമ്പനികൾക്ക് മാത്രമല്ല. ഭക്ഷണം വിളമ്പുന്ന സർവീസിനും ക്ലാസുണ്ട്; അവിടെ ഫയൽ ചെയ്താലേ പേരിന് സംരക്ഷണമുള്ളൂ. നിങ്ങളുടെ നാട്ടിലെ ഫേമസ് തട്ടുകട ഏത്?",
 cap_en="Trademarks are not only for big companies. Serving food is a service with its own class, and a night food stall's famous name is protected only once it is filed there. Which night food stall is famous in your town?",
 cap_mg="Trademark valiya company-kalkku maathramalla. Bhakshanam vilampunna service-inum class undu; avide file cheythaale perinu samrakshanam ullu. Ningalude naattile famous thattukada etha?")

# new, d904 pattern: hill-estate chocolate brand, objection while out of network
duo("tm030", "food_brand", "B", "munnar", "മലയിൽ റേഞ്ച് ഇല്ല.\nട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ\nമെയിലിൽ 3 ആഴ്ച", [
 ("A","wide","ബേസിലേ, താഴെ ടൗണിൽ വന്നപ്പോഴാ മെയിൽ കണ്ടത്. ചോക്ലേറ്റ് ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ."),
 ("V","V","സെലിനേ, എസ്റ്റേറ്റിൽ റേഞ്ച് ഇല്ലെന്ന് രജിസ്ട്രിക്ക് അറിയില്ലല്ലോ. എത്ര ദിവസമായി?"),
 ("A","A","മൂന്ന് ആഴ്ച. ബ്രാൻഡ് പോയോ?"),
 ("V","wide","ഒബ്ജക്ഷൻ ഒരു ചോദ്യമാണ്. 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. ഇനി ഒരാഴ്ചയേ ഉള്ളൂ."),
 ("A","A","ഇന്ന് മല കയറുന്നതിന് മുമ്പ് മറുപടി."),
 ("V","V","റേഞ്ച് ഇല്ലെങ്കിലും ഡെഡ്‌ലൈൻ ഉണ്ട്.")],
 "ഒബ്ജക്ഷന് മറുപടി\n30 ദിവസത്തിൽ", CTA_TRADEMARK, theme="new",
 cap_ml="മലയിലെ എസ്റ്റേറ്റിൽ റേഞ്ച് ഇല്ലാതെ ചോക്ലേറ്റ് ബ്രാൻഡിന്റെ ട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ മെയിൽ 3 ആഴ്ച കാണാതെ കിടന്നു. ഒബ്ജക്ഷന് 30 ദിവസത്തിനുള്ളിൽ മറുപടി വേണം. നിങ്ങളുടെ ട്രേഡ്മാർക്ക് മെയിൽ ആരാ നോക്കുന്നത്?",
 cap_en="A hill-estate chocolate brand had no network and missed a trademark objection email for 3 weeks. An objection must be answered within 30 days. Who checks your trademark emails?",
 cap_mg="Malayile estate-il range illaathe chocolate brand-inte trademark objection mail 3 aazhcha kaanaathe kidannu. Objection-inu 30 divasathinullil marupadi venam. Ningalude trademark mail aara nokkunnathu?")

