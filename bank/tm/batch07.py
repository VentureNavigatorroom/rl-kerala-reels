# Trademark batch 07 (21 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_TM. Never promise registration or mention fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

# CRM (small business wants to expand): franchise enquiries, but only a company name approval
duo("tm042", "food_brand", "A", "bank", "3 പേർ ഫ്രാഞ്ചൈസി\nചോദിച്ചു. ആദ്യ ചോദ്യം:\n\"ട്രേഡ്മാർക്ക് ഉണ്ടോ?\"", [
 ("A","wide","മനോജേ, നിങ്ങളുടെ പുട്ടുകടയ്ക്ക് മൂന്ന് പേർ ഫ്രാഞ്ചൈസി ചോദിച്ചെന്ന് കേട്ടു. ലോൺ അതിനാണോ?"),
 ("V","V","അതെ ശ്രുതീ. പക്ഷേ അവരുടെ വക്കീൽ ആദ്യം ചോദിച്ചത് ട്രേഡ്മാർക്ക് സർട്ടിഫിക്കറ്റ്. എന്റെ കയ്യിൽ കമ്പനി പേരിന്റെ അപ്രൂവൽ മാത്രം."),
 ("A","A","കമ്പനി പേര് കിട്ടിയാൽ ബ്രാൻഡ് സംരക്ഷിക്കപ്പെടില്ല."),
 ("A","wide","റെസ്റ്റോറന്റ് സർവീസിന്റെ ക്ലാസിൽ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യണം. ഫയൽ ചെയ്ത ശേഷം ബോർഡിൽ TM ഇടാം."),
 ("V","V","അപ്പോ ആദ്യം പേര് എന്റേതാക്കണം, പിന്നെ മറ്റുള്ളവർക്ക് കൊടുക്കാം."),
 ("A","wide","സ്വന്തമല്ലാത്ത പേര് വാടകയ്ക്ക് കൊടുക്കാൻ പറ്റില്ല.")],
 "സ്വന്തമല്ലാത്ത പേര്\nവാടകയ്ക്ക് കൊടുക്കാനാവില്ല", CTA_BRAND, theme="crm",
 cap_ml="പുട്ടുകടയ്ക്ക് ഫ്രാഞ്ചൈസി ചോദിച്ചവരുടെ വക്കീൽ ആദ്യം ചോദിച്ചത് ട്രേഡ്മാർക്ക്. കമ്പനി പേരിന്റെ അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല; റെസ്റ്റോറന്റ് സർവീസിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യണം. നിങ്ങൾ ഫ്രാഞ്ചൈസി ആലോചിക്കുന്നുണ്ടോ?",
 cap_en="Three people asked a puttu shop for a franchise, and their lawyer's first question was the trademark. A company name approval does not protect a brand: file in the class for restaurant services before you franchise it. Are you planning to franchise: yes or no?",
 cap_mg="Puttu kadaykku franchise chodichavarude vakkeel aadyam chodichathu trademark. Company name approval brand-ine samrakshikkilla; restaurant service class-il file cheyyanam. Ningal franchise aalochikkunnundo?")

# FAQ: "the GST certificate shows my trade name, so the brand is mine"
duo("tm043", "d2c_brand", "B", "office", "\"GST സർട്ടിഫിക്കറ്റിൽ\nട്രേഡ് നെയിം ഉണ്ടല്ലോ.\nബ്രാൻഡ് സേഫ്!\"", [
 ("A","wide","രാഹുലേ, നിന്റെ മുളകുപൊടി ബ്രാൻഡിന്റെ അതേ പേരിൽ ഒരു ഓൺലൈൻ സെല്ലർ ഇറങ്ങിയല്ലോ."),
 ("V","V","നേഹേ, പേടിക്കേണ്ട. GST സർട്ടിഫിക്കറ്റിൽ ട്രേഡ് നെയിം ആയി ആ പേര് കൊടുത്തിട്ടുണ്ട്."),
 ("A","A","GST-യിലെ പേര് നികുതി കണക്കിനാ. കമ്പനി പേരും അതുപോലെ, ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല."),
 ("A","wide","ബ്രാൻഡിന് ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ മുളകുപൊടിയുടെ ക്ലാസിൽ ഫയൽ ചെയ്യണം."),
 ("V","V","അപ്പോ ഇത്രയും കാലം പേപ്പർ ഉണ്ടെന്ന് കരുതിയത് വേറെ പേപ്പർ."),
 ("A","wide","GST നികുതിക്ക്, ട്രേഡ്മാർക്ക് പേരിന്.")],
 "GST നികുതിക്ക്,\nട്രേഡ്മാർക്ക് പേരിന്", CTA_TRADEMARK, theme="faq",
 cap_ml="GST സർട്ടിഫിക്കറ്റിലെ ട്രേഡ് നെയിം ബ്രാൻഡിനെ സംരക്ഷിക്കുമെന്ന് പലരും കരുതുന്നു. കമ്പനി പേരുപോലെ അതും ട്രേഡ്മാർക്ക് അല്ല; ബ്രാൻഡ് നിങ്ങളുടെ പ്രോഡക്റ്റിന്റെ ക്ലാസിൽ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യണം. നിങ്ങളും ഇങ്ങനെ കരുതിയിരുന്നോ?",
 cap_en="Many sellers think the trade name on their GST certificate protects their brand. Like a company name approval, it is not a trademark: file the brand with the Trade Marks Registry in your product's class. Did you think so too: yes or no?",
 cap_mg="GST certificate-ile trade name brand-ine samrakshikkum ennu palarum karuthunnu. Company name pole athum trademark alla; brand ningalude product-inte class-il Trade Marks Registry-il file cheyyanam. Ningalum ingane karuthiyirunno?")

# NEW (d904 pattern): bridal mehendi artist, objection arrives in peak wedding season
duo("tm044", "salon_clinic", "C", "weddinghall", "40 കല്യാണം.\nഅതിനിടയിൽ ട്രേഡ്മാർക്ക്\nഒബ്ജക്ഷൻ", [
 ("A","wide","ശരത്തേ, ഈ സീസണിൽ നാല്പത് കല്യാണത്തിന് മൈലാഞ്ചി. അതിനിടയ്ക്ക് ബ്രാൻഡിന് ഒബ്ജക്ഷൻ മെയിൽ."),
 ("V","V","കാവ്യേ, സീസൺ കഴിഞ്ഞ് സമാധാനത്തോടെ മറുപടി കൊടുത്താൽ പോരേ?"),
 ("A","A","സീസൺ തീരാൻ രണ്ട് മാസം ഉണ്ട്."),
 ("V","wide","എങ്കിൽ പറ്റില്ല. ഒബ്ജക്ഷന് മുപ്പത് ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. ഈ ആഴ്ച തന്നെ തുടങ്ങണം."),
 ("A","A","കല്യാണം ഒന്ന് മാറ്റിവെക്കാം, മറുപടി പറ്റില്ല."),
 ("V","V","മൈലാഞ്ചി ഉണങ്ങാൻ അര മണിക്കൂർ, മറുപടിക്ക് മുപ്പത് ദിവസം.")],
 "മൈലാഞ്ചി ഉണങ്ങാൻ അര മണിക്കൂർ,\nമറുപടിക്ക് 30 ദിവസം", CTA_TRADEMARK, theme="new",
 cap_ml="കല്യാണ സീസണിന്റെ തിരക്കിനിടയിൽ മൈലാഞ്ചി ആർട്ടിസ്റ്റിന്റെ ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ വന്നു. സീസൺ കഴിയും വരെ കാത്തിരിക്കാൻ പറ്റില്ല: മറുപടി 30 ദിവസത്തിനുള്ളിൽ. നിങ്ങളുടെ തിരക്കുള്ള മാസം ഏതാ?",
 cap_en="A bridal mehendi artist got a trademark objection in the middle of wedding season and planned to reply after it. The reply to an objection is due within 30 days, season or not. Which is your busiest month?",
 cap_mg="Kalyana season-inte thirakkinidayil mylanchi artist-inte brand-inu trademark objection vannu. Season kazhiyum vare kaathirikkaan pattilla: marupadi 30 divasathinullil. Ningalude thirakkulla maasam ethaa?")

# NEW (d904 pattern): a Theyyam-mask miniature carver thinks only big companies can oppose
duo("tm045", "copied_brand", "A", "park", "\"അവർ വലിയ കമ്പനി.\nനമ്മൾ എതിർത്താൽ\nആര് കേൾക്കാൻ?\"", [
 ("A","wide","അനന്തൂ, നിന്റെ തെയ്യം മുഖംമൂടി മിനിയേച്ചറിന്റെ പേരിനോട് സാമ്യമുള്ള ഒരു പേര് ട്രേഡ് മാർക്ക്സ് ജേണലിൽ വന്നിട്ടുണ്ട്."),
 ("V","V","ഗായത്രീ, അത് വലിയ സുവനീർ കമ്പനിയാ. ഞാൻ ഒറ്റയ്ക്ക് കൊത്തുന്ന ആളാ. എതിർത്തിട്ട് എന്ത് കാര്യം?"),
 ("A","A","ജേണലിൽ വന്നാൽ ആർക്കും എതിർക്കാം. ചെറുതോ വലുതോ എന്നില്ല."),
 ("A","wide","പക്ഷേ പ്രസിദ്ധീകരിച്ച് നാല് മാസത്തിനുള്ളിൽ ഓപ്പോസിഷൻ ഫയൽ ചെയ്യണം. അത് കഴിഞ്ഞാൽ ആ വഴി അടയും."),
 ("V","V","അപ്പോ ഉളി താഴെ വെച്ച് ആദ്യം തീയതി നോക്കാം."),
 ("A","wide","എതിർക്കാൻ വലിപ്പം വേണ്ട, സമയം വേണം.")],
 "എതിർക്കാൻ വലിപ്പം വേണ്ട,\nസമയം വേണം", CTA_BRAND, theme="new",
 cap_ml="തെയ്യം മുഖംമൂടി മിനിയേച്ചർ ഉണ്ടാക്കുന്ന ഒറ്റയാൾ കരകൗശലക്കാരന്റെ പേരിനോട് സാമ്യമുള്ള പേര് ഒരു വലിയ കമ്പനി ഫയൽ ചെയ്തു. ട്രേഡ് മാർക്ക്സ് ജേണലിൽ വന്ന് 4 മാസത്തിനുള്ളിൽ ആർക്കും ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം. നിങ്ങൾ ജേണൽ നോക്കാറുണ്ടോ?",
 cap_en="A one-man Theyyam-mask miniature carver found a big souvenir company's look-alike name in the Trade Marks Journal and thought he was too small to object. Anyone can file an opposition, within 4 months of publication. Do you ever check the journal?",
 cap_mg="Theyyam mukhammoodi miniature undaakkunna ottayaal karakaushalakkaarante perinodu saamyamulla peru oru valiya company file cheythu. Trade Marks Journal-il vannu 4 maasathinullil aarkkum opposition file cheyyaam. Ningal journal nokkaarundo?")

# CRM (Gulf returnees, idea stage): filed = done forever?
duo("tm046", "food_brand", "B", "home", "ഗൾഫിൽ നിന്ന് വന്നു.\nകേക്ക് ബ്രാൻഡ് ഫയൽ ചെയ്തു.\n\"ഇനി ആരും തൊടില്ല\"", [
 ("A","wide","അരുണേ, ഷാർജയിലെ ഗ്രൂപ്പിൽ ഹിറ്റായ എന്റെ കേക്ക് ബ്രാൻഡ് ഇവിടെ ട്രേഡ്മാർക്കിന് ഫയൽ ചെയ്തു."),
 ("V","V","സ്നേഹേ, സൂപ്പർ! എങ്കിൽ ഇനി ആരും തൊടില്ല. ബോക്സിൽ R അടിച്ച് ലോഞ്ച് ചെയ്യാം."),
 ("A","A","ഫയൽ ചെയ്തതേ ഉള്ളൂ. ഇപ്പോൾ TM മാത്രം."),
 ("A","wide","ജേണലിൽ വന്ന ശേഷം നാല് മാസം ആർക്കും എതിർക്കാം. R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം."),
 ("V","V","അപ്പോ ഫയലിംഗ് അടുപ്പിൽ വെച്ചതേ ഉള്ളൂ, കേക്ക് ആയിട്ടില്ല."),
 ("A","wide","ഓവനിൽ വെച്ചാൽ കേക്ക് ആകില്ല, ഫയൽ ചെയ്താൽ R-ഉം.")],
 "ഫയൽ ചെയ്താൽ TM,\nരജിസ്റ്റർ ആയാലേ R", CTA_TRADEMARK, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തിയ ദമ്പതികൾ കേക്ക് ബ്രാൻഡ് ഫയൽ ചെയ്ത ഉടൻ ബോക്സിൽ R അടിക്കാൻ ഒരുങ്ങി. ഫയൽ ചെയ്താൽ TM മാത്രം; ജേണലിൽ വന്ന ശേഷം 4 മാസം ആർക്കും എതിർക്കാം, R രജിസ്ട്രേഷന് ശേഷം. നിങ്ങളുടെ അപേക്ഷ ഏത് ഘട്ടത്തിലാ?",
 cap_en="A couple back from the Gulf filed their cake brand and wanted R on the boxes at launch. Filing lets you use TM; after journal publication anyone can oppose for 4 months, and R comes only after registration. What stage is your application at?",
 cap_mg="Gulf-il ninnu thirichethiya dampathikal cake brand file cheytha udan box-il R adikkaan orungi. File cheythaal TM maathram; journal-il vanna shesham 4 maasam aarkkum ethirkkaam, R registration-inu shesham. Ningalude apeksha ethu ghattathilaa?")

# CRM (NRI investor checking before putting money in)
duo("tm047", "d2c_brand", "C", "gulf", "ഡെക്കിൽ \"രജിസ്റ്റേർഡ്\nബ്രാൻഡ്\". ചോദിച്ചപ്പോൾ:\n\"ഫയൽ ചെയ്തിട്ടുണ്ട്\"", [
 ("A","wide","ഫൈസലേ, നാട്ടിലെ കസിന്റെ ബാംബൂ ടൂത്ത്ബ്രഷ് ബ്രാൻഡിൽ ഞാൻ പൈസ ഇടാൻ നോക്കുകയാ. ഡെക്കിൽ രജിസ്റ്റേർഡ് ബ്രാൻഡ് എന്നുണ്ട്."),
 ("V","V","ഷിജൂ, നമ്പർ ചോദിച്ചപ്പോൾ അവൻ എന്താ പറഞ്ഞത്?"),
 ("A","A","ഫയൽ ചെയ്തിട്ടുണ്ട്, ഉടനെ ശരിയാകും എന്ന്."),
 ("V","wide","ഫയൽ ചെയ്തതും രജിസ്റ്റർ ആയതും രണ്ടാ. ഫയൽ ചെയ്താൽ TM, രജിസ്ട്രേഷൻ കിട്ടിയാലേ R. ഡെക്കിൽ സത്യം വേണം."),
 ("A","A","പൈസ ഇടുന്നതിന് മുമ്പ് സ്റ്റാറ്റസ് ഞാൻ തന്നെ നോക്കും."),
 ("V","V","ഡെക്കിലെ ഒരു വാക്ക് തെറ്റിയാൽ മുഴുവൻ ഡെക്കും സംശയത്തിലാ.")],
 "ഫയൽ ചെയ്തത് TM,\nരജിസ്റ്റർ ആയത് R", CTA_BRAND, theme="crm",
 cap_ml="ഗൾഫിലെ NRI കസിന്റെ ബ്രാൻഡിൽ നിക്ഷേപിക്കാൻ നോക്കിയപ്പോൾ ഡെക്കിൽ രജിസ്റ്റേർഡ് ബ്രാൻഡ്, സത്യത്തിൽ ഫയൽ ചെയ്തതേ ഉള്ളൂ. ഫയൽ ചെയ്താൽ TM, രജിസ്ട്രേഷൻ കിട്ടിയാലേ R. നിങ്ങളുടെ ഡെക്കിൽ എന്താ എഴുതിയിരിക്കുന്നത്?",
 cap_en="An NRI about to invest in his cousin's bamboo toothbrush brand found the deck said registered brand, but the trademark was only filed. Filing lets you use TM; R and the word registered only after registration. What does your deck say?",
 cap_mg="Gulf-ile NRI cousin-inte brand-il nikshepikkaan nokkiyappol deck-il registered brand, sathyathil file cheythathe ulloo. File cheythaal TM, registration kittiyaale R. Ningalude deck-il enthaa ezhuthiyirikkunnathu?")

# FAQ: one filing for an app also covers printed workbooks?
duo("tm048", "app_founder", "A", "gulfoffice", "ആപ്പിന് ട്രേഡ്മാർക്ക്.\nഅതേ പേരിൽ\nപുസ്തകം? സംരക്ഷണം ഇല്ല", [
 ("A","wide","ആസിഫേ, നമ്മുടെ അറബി പഠന ആപ്പിന്റെ പേരിൽ തന്നെ വർക്ക്ബുക്ക് അച്ചടിച്ച് ഇറക്കാൻ ഓർഡർ കൊടുത്തു."),
 ("V","V","ഷഹാനാ, ആപ്പിന്റെ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തതല്ലേ. പുസ്തകവും അതിൽ പെടില്ലേ?"),
 ("A","A","അത് ആപ്പിന്റെ ക്ലാസിൽ മാത്രം."),
 ("V","wide","നാല്പത്തഞ്ച് ക്ലാസുണ്ട്. അച്ചടിച്ച പുസ്തകം വേറെ ക്ലാസാ. കച്ചവടം ചെയ്യുന്ന ഓരോ ക്ലാസിലും ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പോ പ്രസ്സിൽ പോകും മുമ്പ് ഒരു ഫയലിംഗ് കൂടി."),
 ("V","V","സ്ക്രീനിലെ പേര് പേപ്പറിൽ ഇറങ്ങുമ്പോൾ ക്ലാസും മാറും.")],
 "സ്ക്രീനിൽ നിന്ന് പേപ്പറിലേക്ക്,\nക്ലാസും മാറും", CTA_TRADEMARK, theme="faq",
 cap_ml="അറബി പഠന ആപ്പിന്റെ ട്രേഡ്മാർക്ക് അതേ പേരിലുള്ള അച്ചടിച്ച വർക്ക്ബുക്കിനെ സംരക്ഷിക്കില്ല. 45 ക്ലാസുകളിൽ ആപ്പും പുസ്തകവും വേറെ വേറെ; കച്ചവടം ചെയ്യുന്ന ഓരോ ക്ലാസിലും ഫയൽ ചെയ്യണം. നിങ്ങളുടെ ബ്രാൻഡ് എത്ര ക്ലാസിൽ കച്ചവടം ചെയ്യുന്നു?",
 cap_en="A language-learning app's trademark does not cover printed workbooks sold under the same name. Of the 45 classes, apps and printed books fall in different ones: file in each class you trade in. In how many forms does your brand go out?",
 cap_mg="Arabi padana app-inte trademark athe perilulla achadicha workbook-ine samrakshikkilla. 45 class-ukalil app-um pusthakavum vere vere; kachavadam cheyyunna oro class-ilum file cheyyanam. Ningalude brand ethokke roopathil irangunnu?")

# FAQ: the designer adds an R to the logo file "for the look"
chat("tm049", "d2c_brand", "B", "ഡിസൈനർ അയച്ച ലോഗോ.\nമൂലയിൽ ഒരു R.\nഫയലിംഗ് കഴിഞ്ഞിട്ടില്ല", ("ഡെൽന", "ശ്രീനാഥ്"), [
 (0,"ശ്രീനാഥ്, ആയുർവേദ സോപ്പിന്റെ ലോഗോ കിട്ടി. മൂലയിൽ ഒരു R ചിഹ്നം. നീ ഇട്ടതാണോ?"),
 (1,"അതെ ഡെൽന, ബ്രാൻഡുകൾക്കെല്ലാം അതുണ്ടല്ലോ. ഒരു റിച്ച് ലുക്ക്."),
 (0,"നമ്മൾ ട്രേഡ്മാർക്ക് ഫയൽ പോലും ചെയ്തിട്ടില്ല."),
 (1,"എങ്കിൽ മാറ്റാം. ഫയൽ ചെയ്ത ശേഷം TM. R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം."),
 (0,"അപ്പോ ഇപ്പോൾ ചിഹ്നം ഒന്നും വേണ്ട, ആദ്യം ഫയലിംഗ്."),
 (1,"ശരി. ലുക്കിന് നിറം മതി, R വേണ്ട.")],
 "ലുക്കിന് നിറം മതി,\nR വേണ്ട", CTA_TRADEMARK, theme="faq",
 cap_ml="ഡിസൈനർ ഭംഗിക്ക് വേണ്ടി ലോഗോയിൽ R ചേർത്തു, പക്ഷേ ട്രേഡ്മാർക്ക് ഫയൽ പോലും ചെയ്തിരുന്നില്ല. ഫയൽ ചെയ്ത ശേഷം TM, രജിസ്ട്രേഷന് ശേഷം മാത്രം R. നിങ്ങളുടെ ലോഗോ ഫയലിൽ ഏത് ചിഹ്നമാ?",
 cap_en="A designer added an R to a soap brand's logo for the look, before the trademark was even filed. TM once you file, R only after registration. Check the final logo file before it goes to print. Which symbol is in your logo file?",
 cap_mg="Designer bhangikku vendi logo-yil R cherthu, pakshe trademark file polum cheythirunnilla. File cheytha shesham TM, registration-inu shesham maathram R. Ningalude logo file-il ethu chihnamaa?")

# CRM (idea stage: two friends, no company yet, plan to sort the name "later")
duo("tm050", "d2c_brand", "C", "teashop", "\"ആദ്യം കമ്പനി,\nപിന്നെ ലോഗോ,\nട്രേഡ്മാർക്ക് പിന്നീട്\"", [
 ("A","wide","വിഷ്ണൂ, നമ്മുടെ കോൾഡ് ബ്രൂ കാപ്പിക്ക് ഇട്ട പേര് ഇൻസ്റ്റയിൽ ടീസർ ആയി ഇട്ടിട്ട് ഒരാഴ്ച."),
 ("V","V","അനൂ, ആദ്യം കമ്പനി രജിസ്റ്റർ ചെയ്യാം. കമ്പനി പേര് കിട്ടിയാൽ ബ്രാൻഡും നമ്മുടേതാകില്ലേ?"),
 ("A","A","ഇല്ല. കമ്പനി പേരിന്റെ അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല."),
 ("A","wide","കാപ്പിയുടെ ക്ലാസിൽ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ പേര് ഫയൽ ചെയ്യണം. ടീസർ കണ്ടവരിൽ ആരെങ്കിലും ആദ്യം ഫയൽ ചെയ്യാം."),
 ("V","V","ടീസർ ഇട്ടത് നമ്മൾ, ഫയൽ ചെയ്യുന്നത് വേറെ ആൾ. അത് വേണ്ട."),
 ("A","wide","ടീസറിന് മുമ്പ് ഫയലിംഗ്.")],
 "ടീസറിന് മുമ്പ്\nഫയലിംഗ്", CTA_BRAND, theme="crm",
 cap_ml="കോൾഡ് ബ്രൂ ബ്രാൻഡിന്റെ പേര് ടീസർ ആയി ഇട്ട ശേഷം കമ്പനി ആദ്യം, ട്രേഡ്മാർക്ക് പിന്നീട് എന്ന് രണ്ട് സുഹൃത്തുക്കൾ കരുതി. കമ്പനി പേര് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല; പ്രോഡക്റ്റിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ ബ്രാൻഡ് പേര് പുറത്ത് പറഞ്ഞോ?",
 cap_en="Two friends teased their cold brew brand name on Instagram and planned to register the company first and the trademark later. A company name approval does not protect a brand: file the name in your product's class before the teaser. Have you announced your brand name yet?",
 cap_mg="Cold brew brand-inte peru teaser aayi itta shesham company aadyam, trademark pinneedu ennu randu suhruthukkal karuthi. Company name brand-ine samrakshikkilla; product-inte class-il file cheyyanam. Ningalude brand peru purathu paranjo?")

