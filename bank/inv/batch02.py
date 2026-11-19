# Investor agreements batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_INV. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

duo("vd005", "founder_raising", "A", "hotellobby", "ടേം ഷീറ്റ് ഒപ്പിട്ടു.\nപാർട്ടി നടത്തി.\nപൈസ വന്നില്ല", [
 ("A","wide","ജെയ്സൺ, ടേം ഷീറ്റ് ഒപ്പിട്ട രാത്രി ഞങ്ങൾ ടീം പാർട്ടി നടത്തി. 2 മാസമായി, പൈസ വന്നിട്ടില്ല!"),
 ("V","V","ടേം ഷീറ്റ് മിക്കവാറും നോൺ-ബൈൻഡിംഗ് ആണ്. രഹസ്യസ്വഭാവം, എക്സ്ക്ലൂസിവിറ്റി, ചെലവ്, ഗവേണിംഗ് ലോ, ഇവയേ സാധാരണ ബൈൻഡ് ചെയ്യൂ."),
 ("A","A","അപ്പോ ഡീൽ എപ്പോ ഉറപ്പാകും?"),
 ("V","wide","ടേം ഷീറ്റ് കഴിഞ്ഞ് ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്, പിന്നെ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്. അത് ഒപ്പിടുമ്പോഴാ കാര്യം."),
 ("A","A","അടുത്ത തവണ പാർട്ടി അലോട്ട്മെന്റിന് ശേഷം."),
 ("V","wide","അതെ. കേക്ക് മുറിക്കാൻ SSA വരെ കാത്തിരിക്കൂ.")],
 "ടേം ഷീറ്റ് ഡീൽ അല്ല,\nതുടക്കം മാത്രം", CTA_TERMSHEET, theme="faq",
 cap_ml="ടേം ഷീറ്റ് ഒപ്പിട്ടാൽ ഡീൽ ഉറപ്പായി എന്ന് കരുതരുത്. ടേം ഷീറ്റ് മിക്കവാറും നോൺ-ബൈൻഡിംഗ്; രഹസ്യസ്വഭാവം, എക്സ്ക്ലൂസിവിറ്റി, ചെലവ്, ഗവേണിംഗ് ലോ മാത്രം സാധാരണ ബൈൻഡിംഗ്. പിന്നെ SSA, SHA. നിങ്ങൾ ടേം ഷീറ്റ് കഴിഞ്ഞ് ആഘോഷിച്ചോ?",
 cap_en="A startup team celebrated the night they signed a term sheet, and two months later the money still hasn't come. A term sheet is mostly non-binding: only confidentiality, exclusivity, costs and governing law usually bind. The deal is done through the SSA and SHA.",
 cap_mg="Term sheet oppittaal deal urappaayi ennu karutharuthu. Term sheet mikkavaarum non-binding; confidentiality, exclusivity, costs, governing law maathram binding. Pinne SSA, SHA.")

duo("vd006", "family_money", "B", "balcony", "\"നാട്ടിലെ 60 പേരിൽ\nനിന്ന് 1 ലക്ഷം വീതം\"\nപ്ലാൻ കേട്ട് CA ഞെട്ടി", [
 ("A","wide","വിവേക്, ഞാൻ ഒരു പ്ലാൻ ഇട്ടു. നാട്ടിലെ 60 പേരിൽ നിന്ന് 1 ലക്ഷം വീതം, എല്ലാവർക്കും കുറച്ച് ഷെയർ."),
 ("V","V","അമ്മൂ, അത് സൂക്ഷിച്ച് വേണം. പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ ഒരു വർഷം പരമാവധി 200 പേർ."),
 ("A","A","60 അല്ലേ ഉള്ളൂ, അപ്പോ കുഴപ്പമില്ലല്ലോ?"),
 ("V","wide","എണ്ണം മാത്രമല്ല. സ്പെഷ്യൽ റെസല്യൂഷൻ, PAS-4 ഓഫർ ലെറ്റർ, ഓരോരുത്തരുടെ സ്വന്തം അക്കൗണ്ടിൽ നിന്ന് പൈസ, പിന്നെ PAS-3."),
 ("A","A","അപ്പോ ആളെണ്ണം കൂട്ടുന്നതല്ല, ഘടന ശരിയാക്കുന്നതാ കാര്യം."),
 ("V","wide","അതെ. ചിട്ടി പിടിക്കുന്ന പോലെ അല്ല ഷെയർ കൊടുക്കുന്നത്.")],
 "ഒരു വർഷം\nപരമാവധി 200 പേർ", CTA_INVEST, theme="crm",
 cap_ml="നാട്ടിലെ 60 പേരിൽ നിന്ന് ചെറിയ തുകകൾ വാങ്ങി ഷെയർ കൊടുക്കാൻ പ്ലാൻ. പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ വർഷം പരമാവധി 200 പേർ; സ്പെഷ്യൽ റെസല്യൂഷൻ, PAS-4, ഇൻവെസ്റ്ററുടെ സ്വന്തം അക്കൗണ്ടിൽ നിന്ന് പണം, PAS-3 ഫയലിംഗ് വേണം.",
 cap_en="A founder plans to raise 1 lakh each from 60 people back home, all getting a few shares. A private placement is limited to 200 people a year, and it still needs a special resolution, a PAS-4 offer letter, money from each investor's own account and a PAS-3 filing.",
 cap_mg="Naattile 60 peril ninnu cheriya thukakal vaangi share kodukkaan plan. Private placement-il varsham paramaavadhi 200 per; special resolution, PAS-4, investor-ude swantham account-il ninnu panam, PAS-3 venam.")

duo("vd007", "angel", "A", "hospital", "SHA-യിൽ ബോർഡ് സീറ്റ്.\nമീറ്റിംഗിന്\nവിളിച്ചില്ല", [
 ("A","wide","ജോസഫ്, ഞാൻ ഇൻവെസ്റ്റ് ചെയ്ത സ്റ്റാർട്ടപ്പ് ബോർഡ് മീറ്റിംഗിന് എന്നെ വിളിച്ചില്ല. SHA-യിൽ എനിക്ക് ബോർഡ് സീറ്റ് ഉണ്ടല്ലോ!"),
 ("V","V","SHA-യിലെ റൈറ്റ്സ് കമ്പനിയെ ബൈൻഡ് ചെയ്യാൻ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിലും എഴുതണം. അത് ചെയ്തോ?"),
 ("A","A","അത്... അറിയില്ല."),
 ("V","wide","ബോർഡ് സീറ്റ്, റൈറ്റ് ഓഫ് ഫസ്റ്റ് റിഫ്യൂസൽ, ടാഗ്-അലോങ്. എല്ലാം ആർട്ടിക്കിൾസ് ഭേദഗതി ചെയ്ത് ചേർക്കണം."),
 ("A","A","പല്ല് നോക്കുന്ന പോലെ ഇനി പേപ്പറും നോക്കും."),
 ("V","wide","അതെ. പല്ലിന് ക്രൗൺ പോലെ, SHA-ക്ക് ആർട്ടിക്കിൾസ്.")],
 "SHA റൈറ്റ്സ്\nആർട്ടിക്കിൾസിലും വേണം", CTA_INVEST, theme="new",
 cap_ml="SHA-യിൽ ബോർഡ് സീറ്റ് ഉണ്ടായിട്ടും ഏഞ്ചൽ ഇൻവെസ്റ്ററെ മീറ്റിംഗിന് വിളിച്ചില്ല. SHA റൈറ്റ്സ് കമ്പനിയെ ബൈൻഡ് ചെയ്യാൻ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷൻ ഭേദഗതി ചെയ്യണം. നിങ്ങൾ സ്റ്റാർട്ടപ്പിൽ ഇൻവെസ്റ്റ് ചെയ്തിട്ടുണ്ടോ?",
 cap_en="A dentist who invested in a startup was left out of the board meeting despite a board seat in the SHA. SHA rights such as a board seat, first refusal and tag-along bind the company only once they are written into the Articles of Association.",
 cap_mg="SHA-yil board seat undaayittum angel investor-e meeting-nu vilichilla. SHA rights company-ye bind cheyyaan Articles of Association amend cheyyanam.")

duo("vd008", "founder_raising", "B", "handloom", "\"ഇൻവെസ്റ്റ്മെന്റ് എടുത്താൽ\nഏഞ്ചൽ ടാക്സ്\"\nപേടിച്ച് 1 വർഷം", [
 ("A","wide","കുമാർ, കൈത്തറി ബാഗ് ബ്രാൻഡിന് ഒരു ഏഞ്ചൽ ഇൻവെസ്റ്റർ റെഡി. പക്ഷേ ഏഞ്ചൽ ടാക്സ് പേടിച്ച് ഞാൻ ഒരു വർഷമായി നീട്ടുന്നു."),
 ("V","V","ഏഞ്ചൽ ടാക്സ് 2024-25 സാമ്പത്തിക വർഷം മുതൽ എല്ലാ ഇൻവെസ്റ്റർമാർക്കും എടുത്തുകളഞ്ഞു."),
 ("A","A","ശരിക്കും? അപ്പോ നേരെ പൈസ വാങ്ങാമല്ലേ?"),
 ("V","wide","നേരെ അല്ല. ഷെയർ കൊടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പിന്നെ എഗ്രിമെന്റുകളും ഫയലിംഗും."),
 ("A","A","പേടിച്ച് ഒരു വർഷം വെറുതെ പോയി."),
 ("V","wide","നൂല് പുതിയത്, നിയമവും പുതിയത്. പേടി മാത്രം പഴയത്.")],
 "ഏഞ്ചൽ ടാക്സ്\nഇപ്പോൾ ഇല്ല", CTA_FUNDING, theme="faq",
 cap_ml="ഏഞ്ചൽ ടാക്സ് പേടിച്ച് ഒരു വർഷം ഇൻവെസ്റ്റ്മെന്റ് നീട്ടി. 2024-25 മുതൽ എല്ലാ ഇൻവെസ്റ്റർമാർക്കും ഏഞ്ചൽ ടാക്സ് ഇല്ല; പക്ഷേ ഷെയർ കൊടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയും എഗ്രിമെന്റുകളും ഫയലിംഗും വേണം.",
 cap_en="A handloom bag founder delayed an angel's money for a year out of fear of angel tax. Angel tax was abolished for all investors from FY 2024-25. You still need a private limited company to issue shares, plus the agreements and filings.",
 cap_mg="Angel tax pedichu oru varsham investment neetti. 2024-25 muthal ella investors-num angel tax illa; pakshe share kodukkaan private limited company-um agreements-um filing-um venam.")
