# ROC annual compliance batch 06 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_ROC. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING


duo("rc028", "new_company_roc", "A", "textile", "\"എല്ലാ മാസവും GST\nഫയൽ ചെയ്യുന്നുണ്ട്.\nപിന്നെന്ത് ROC?\"", [
 ("A","wide","പ്രകാശേ, സാരി ഷോപ്പ് കമ്പനിയാക്കിയിട്ട് ഒരു വർഷം. ROC-യിൽ നിന്ന് ഈ വർഷത്തെ ഫയലിംഗ് ചെയ്തോ?"),
 ("V","V","രമ്യേ, എല്ലാ മാസവും GST റിട്ടേൺ ഫയൽ ചെയ്യുന്നുണ്ടല്ലോ. പ്രൊപ്രൈറ്റർഷിപ്പിൽ അത് മതിയായിരുന്നു."),
 ("A","A","GST നികുതി വകുപ്പിനാ. കമ്പനിക്ക് ROC-യിൽ വേറെ കണക്കുണ്ട്."),
 ("V","wide","അതെന്താ?"),
 ("A","wide","സെപ്റ്റംബർ 30-നുള്ളിൽ AGM. പിന്നെ 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7. വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ."),
 ("V","V","GST ടാക്സിന്റെ കണക്ക്. ROC കമ്പനിയുടെ കണക്ക്.")],
 "GST ടാക്സിന്റെ കണക്ക്,\nROC കമ്പനിയുടെ കണക്ക്", CTA_ROC, theme="crm",
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പിൽ നിന്ന് കമ്പനിയായ സാരി ഷോപ്പ്, GST റിട്ടേൺ കൊണ്ട് എല്ലാം കഴിഞ്ഞെന്ന് കരുതി. കമ്പനിക്ക് ROC-യിൽ വേറെ ഫയലിംഗ്: സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7. നിങ്ങളുടെ ബിസിനസ് പ്രൊപ്രൈറ്റർഷിപ്പോ കമ്പനിയോ?",
 cap_en="A saree shop became a private limited company and the owner thought monthly GST returns covered everything. A company has separate ROC filings: AGM by 30 September, AOC-4 within 30 days of it, MGT-7 within 60 days. Proprietorship or company?",
 cap_mg="Proprietorship-il ninnu company aaya saree shop, GST return kondu ellaam kazhinjennu karuthi. Company-kku ROC-il vere filing: September 30-nullil AGM, 30 divasathil AOC-4, 60 divasathil MGT-7. Ningalude business proprietorship-o company-o?")

duo("rc029", "dormant_company", "B", "rooftop", "സുഹൃത്ത് 10% ഷെയർ\nവാങ്ങാൻ റെഡി.\n2 വർഷം ഫയലിംഗ് ഇല്ല", [
 ("A","wide","ശ്യാമേ, റൂഫ്‌ടോപ്പ് കഫേ വീണ്ടും തുറക്കാൻ ഗോകുൽ പൈസ ഇടാമെന്ന്. 10% ഷെയർ മതിയെന്ന്."),
 ("V","V","ആര്യേ, നല്ല വാർത്ത. പക്ഷേ കഫേ അടച്ച രണ്ട് വർഷം കമ്പനി ഒന്നും ഫയൽ ചെയ്തില്ല."),
 ("A","A","അടച്ച കടയ്ക്ക് എന്ത് ഫയലിംഗ്?"),
 ("V","wide","ബിസിനസ് ഇല്ലെങ്കിലും വേണം. മൂന്നാം വർഷവും മുടങ്ങിയാൽ കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം, നമുക്ക് 5 വർഷം ഡയറക്ടർ അയോഗ്യതയും."),
 ("A","A","അപ്പോ ഷെയർ കൊടുക്കും മുമ്പ് കണക്ക് തീർക്കണം."),
 ("V","wide","ഇൻവെസ്റ്റർ ആദ്യം കാണുന്നത് മെനു അല്ല, ഫയലിംഗാ.")],
 "ഇൻവെസ്റ്റർ ആദ്യം\nനോക്കുന്നത് ഫയലിംഗ്", CTA_FILING, theme="crm",
 cap_ml="രണ്ട് വർഷം അടച്ചിട്ട റൂഫ്‌ടോപ്പ് കഫേ, ഇപ്പോൾ ഒരു സുഹൃത്ത് 10% ഷെയർ എടുക്കാൻ റെഡി. പക്ഷേ ആ രണ്ട് വർഷം കമ്പനി ഒന്നും ഫയൽ ചെയ്തില്ല. ബിസിനസ് ഇല്ലെങ്കിലും ഫയലിംഗ് വേണം; 3 വർഷം മുടങ്ങിയാൽ സ്ട്രൈക്ക് ഓഫും 5 വർഷം ഡയറക്ടർ അയോഗ്യതയും വരാം. നിങ്ങളുടെ കമ്പനി ഇപ്പോൾ ഓടുന്നുണ്ടോ?",
 cap_en="A rooftop cafe shut for two years, and now a friend wants 10% of the shares. But the company filed nothing in those two years. Filings are due even with zero business; a third year missed can mean strike-off and a 5-year director disqualification. Is your company active right now?",
 cap_mg="Randu varsham adachitta rooftop cafe, ippol oru friend 10% share edukkaan ready. Pakshe aa randu varsham company onnum file cheythilla. Business illenkilum filing venam; 3 varsham mudangiyaal strike off-um 5 varsham director ayogyathayum varaam. Ningalude company ippol odunnundo?")

duo("rc030", "late_filer", "C", "hospital", "\"മോന്റെ പേരിൽ ഒരു\nകമ്പനിയുണ്ട്\" ഇന്നാ\nഅറിഞ്ഞത്", [
 ("A","wide","ജോസഫേ, നമ്മുടെ ആൽബിൻ കോളേജിൽ വെച്ച് ഒരു കമ്പനി തുടങ്ങിയിരുന്നെന്ന്. ഇന്നാ പറഞ്ഞത്."),
 ("V","V","ലക്ഷ്മീ, ആ ഹാക്കത്തോണിന് വേണ്ടി? അത് ജയിച്ചു, പിന്നെ എല്ലാരും മറന്നു."),
 ("A","A","അവൻ ഇപ്പോഴും അതിൽ ഡയറക്ടറാ. രണ്ട് വർഷമായി ഒന്നും ഫയൽ ചെയ്തിട്ടില്ല."),
 ("V","wide","എന്നാൽ ഇക്കൊല്ലം തന്നെ തീർക്കണം. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത വരാം."),
 ("A","A","അപ്പോ അവന്റെ അടുത്ത സ്റ്റാർട്ടപ്പിൽ ഡയറക്ടറാകാൻ പറ്റില്ല."),
 ("V","wide","പഴയ പ്രോജക്റ്റിന് മാർക്ക് കിട്ടി. കമ്പനിക്ക് ഇനി ഫയലിംഗ് വേണം.")],
 "പ്രോജക്റ്റ് തീർന്നു,\nകമ്പനി തീർന്നില്ല", CTA_FILING, theme="crm",
 cap_ml="കോളേജ് ഹാക്കത്തോണിന് തുടങ്ങിയ കമ്പനി, ജയിച്ച ശേഷം എല്ലാരും മറന്നു; മകൻ ഇപ്പോഴും ഡയറക്ടർ. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത വരാം, അടുത്ത സ്റ്റാർട്ടപ്പിലും. നിങ്ങളുടെ വീട്ടിൽ ആരുടെയെങ്കിലും പേരിൽ മറന്ന കമ്പനി ഉണ്ടോ?",
 cap_en="A son registered a company for a college hackathon, won, and everyone forgot it; he is still a director. Three years without filings can disqualify a director for 5 years, which also blocks his next startup. Is there a forgotten company in someone's name at home?",
 cap_mg="College hackathon-nu thudangiya company, jayicha shesham ellaarum marannu; makan ippozhum director. 3 varsham file cheythillenkil director-kku 5 varsham ayogyatha varaam, adutha startup-ilum. Ningalude veettil aarudeyenkilum peril maranna company undo?")

duo("rc031", "late_filer", "B", "cafe", "പരീക്ഷയ്ക്ക് പഠിക്കാൻ\nപോയ കോ-ഫൗണ്ടർ.\nKYC ആര് ചെയ്യും?", [
 ("A","wide","റോഷാ, ശ്രീനാഥ് PSC പരീക്ഷയ്ക്ക് പഠിക്കാൻ ആറ് മാസം ബ്രേക്ക് എടുത്തു. ഫോൺ ഓഫാ."),
 ("V","V","ആൽവിനേ, അവൻ ഇപ്പോഴും നമ്മുടെ ഡ്രോൺ ക്ലീനിംഗ് കമ്പനിയിൽ ഡയറക്ടറല്ലേ? സെപ്റ്റംബർ അടുത്തു."),
 ("A","A","കമ്പനിക്ക് വേണ്ടി നമ്മൾ രണ്ടുപേർ ചെയ്താൽ പോരേ?"),
 ("V","wide","പോരാ. DIR-3 KYC എല്ലാ ഡയറക്ടർക്കും, ഓരോരുത്തരും സെപ്റ്റംബർ 30-നുള്ളിൽ. ബ്രേക്കിലുള്ളയാൾക്കും."),
 ("A","A","എങ്കിൽ ഇന്ന് തന്നെ അവന്റെ വീട്ടിൽ പോകാം."),
 ("V","wide","പരീക്ഷയ്ക്ക് ബ്രേക്ക് ഉണ്ട്. KYC-ക്ക് ബ്രേക്ക് ഇല്ല.")],
 "പരീക്ഷയ്ക്ക് ബ്രേക്ക്,\nKYC-ക്ക് ബ്രേക്കില്ല", CTA_ROC, theme="crm",
 cap_ml="ഒരു കോ-ഫൗണ്ടർ PSC പരീക്ഷയ്ക്ക് പഠിക്കാൻ ആറ് മാസം ബ്രേക്ക് എടുത്തു, പക്ഷേ ഇപ്പോഴും ഡയറക്ടർ. DIR-3 KYC എല്ലാ ഡയറക്ടർക്കും സെപ്റ്റംബർ 30-നുള്ളിൽ, ബ്രേക്കിലുള്ളയാൾക്കും. നിങ്ങളുടെ കമ്പനിയിൽ എത്ര ഡയറക്ടർമാർ?",
 cap_en="One co-founder took six months off to study for an exam, but he is still a director of the company. DIR-3 KYC is due from every director by 30 September, including the one on a break. How many directors does your company have?",
 cap_mg="Oru co-founder PSC exam-nu padikkaan aaru maasam break eduthu, pakshe ippozhum director. DIR-3 KYC ella director-kkum September 30-nullil, break-il ullayaalkkum. Ningalude company-il ethra director?")

duo("rc032", "new_company_roc", "A", "weddinghall", "ജൂലൈയിൽ AGM.\n\"AOC-4 ഒക്ടോബറിൽ\nചെയ്താൽ മതി\"", [
 ("A","wide","ശരത്തേ, കല്യാണ സീസണിന് മുമ്പ് ഫോട്ടോഗ്രഫി കമ്പനിയുടെ AGM ജൂലൈ 10-ന് തന്നെ നടത്തി."),
 ("V","V","കാവ്യേ, സൂപ്പർ. ഇനി AOC-4 എല്ലാരും ചെയ്യുന്ന പോലെ ഒക്ടോബറിൽ ചെയ്യാം."),
 ("A","A","പലരുടെയും AGM സെപ്റ്റംബറിലാ. നമ്മുടേത് ജൂലൈയിൽ കഴിഞ്ഞു."),
 ("V","wide","അതിനെന്താ?"),
 ("A","wide","AOC-4 AGM കഴിഞ്ഞ് 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ. ജൂലൈ 10-ന് AGM എങ്കിൽ AOC-4 ഓഗസ്റ്റിൽ തന്നെ."),
 ("V","V","നേരത്തെ AGM, നേരത്തെ ഡെഡ്‌ലൈൻ.")],
 "നേരത്തെ AGM,\nനേരത്തെ ഡെഡ്‌ലൈൻ", CTA_ROC, theme="faq",
 cap_ml="AOC-4 എല്ലാവർക്കും ഒക്ടോബറിൽ ആണോ? അല്ല. AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ AOC-4, 60 ദിവസത്തിനുള്ളിൽ MGT-7. ജൂലൈയിൽ AGM നടത്തിയ വെഡ്ഡിംഗ് ഫോട്ടോഗ്രഫി കമ്പനിക്ക് AOC-4 ഓഗസ്റ്റിൽ തന്നെ. നിങ്ങളുടെ AGM ഏത് മാസം?",
 cap_en="Is AOC-4 due in October for everyone? No. It is due within 30 days of your own AGM, and MGT-7 within 60 days. A wedding photography company that held its AGM on 10 July has AOC-4 due in August. Which month was your AGM?",
 cap_mg="AOC-4 ellaavarkkum October-il aano? Alla. AGM kazhinju 30 divasathinullil AOC-4, 60 divasathinullil MGT-7. July-il AGM nadathiya wedding photography company-kku AOC-4 August-il thanne. Ningalude AGM ethu maasam?")

duo("rc033", "new_company_roc", "C", "akshaya", "\"ബിസിനസ് തുടങ്ങിയിട്ടില്ല,\nINC-20A പിന്നെ\"", [
 ("A","wide","രമേശേ, കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ട് അഞ്ച് മാസം. ഇനി എന്തെങ്കിലും ഫോം ബാക്കിയുണ്ടോ?"),
 ("V","V","സുധേ, ഫിഷ് ഫീഡ് യൂണിറ്റ് ഇതുവരെ തുടങ്ങിയില്ലല്ലോ. തുടങ്ങുമ്പോൾ INC-20A ഫയൽ ചെയ്യാം."),
 ("A","A","അത് ബിസിനസ് തുടങ്ങുന്ന ദിവസം നോക്കിയല്ല."),
 ("V","wide","പിന്നെ?"),
 ("A","wide","INC-20A കമ്പനി രജിസ്റ്റർ ചെയ്ത് 180 ദിവസത്തിനുള്ളിൽ. നമുക്ക് ഇനി ഒരു മാസം കൂടിയേ ഉള്ളൂ."),
 ("V","V","മെഷീൻ വന്നില്ലെങ്കിലും ഡെഡ്‌ലൈൻ വരും.")],
 "മെഷീൻ വന്നില്ലെങ്കിലും\nഡെഡ്‌ലൈൻ വരും", CTA_ROC, theme="faq",
 cap_ml="ബിസിനസ് തുടങ്ങിയിട്ട് INC-20A ഫയൽ ചെയ്താൽ മതിയോ? ഇല്ല. INC-20A കമ്പനി രജിസ്റ്റർ ചെയ്ത് 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം, യൂണിറ്റ് തുടങ്ങിയാലും ഇല്ലെങ്കിലും. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര മാസമായി?",
 cap_en="Can INC-20A wait until the business actually starts? No. It is due within 180 days of incorporation, whether the fish-feed unit is running or not. How many months old is your company?",
 cap_mg="Business thudangiyittu INC-20A file cheythaal mathiyo? Illa. INC-20A company register cheythu 180 divasathinullil file cheyyanam, unit thudangiyaalum illenkilum. Ningalude company-kku ethra maasamaayi?")

duo("rc034", "dormant_company", "B", "salon", "\"ഷെയർ ഒന്നുമില്ല,\nഞാൻ ഡയറക്ടർ മാത്രം.\nഎനിക്കെന്ത്?\"", [
 ("A","wide","വിനീതേ, മെഹന്ദി ആർട്ടിസ്റ്റുകളുടെ ആ കമ്പനിയിൽ നീ ഡയറക്ടറല്ലേ? 3 വർഷമായി ഒന്നും ഫയൽ ചെയ്തില്ലെന്ന് കേട്ടു."),
 ("V","V","സോണിയേ, എനിക്ക് ഒരു ഷെയറും ഇല്ല. ഒപ്പിടാൻ വേണ്ടി ഡയറക്ടറാക്കിയതാ. ഉടമസ്ഥർ നോക്കും."),
 ("A","A","നിയമം ഷെയർ നോക്കിയല്ല, പേര് നോക്കിയാ."),
 ("V","wide","എന്ന് വെച്ചാൽ?"),
 ("A","wide","3 വർഷം ഫയൽ ചെയ്യാത്ത കമ്പനിയുടെ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത വരാം. ഷെയർ ഇല്ലാത്തവർക്കും."),
 ("V","V","ഷെയർ ഇല്ലെങ്കിലും ഷെയർ ഉണ്ട്, പ്രശ്നത്തിൽ.")],
 "ഷെയർ ഇല്ലെങ്കിലും\nപ്രശ്നത്തിൽ ഷെയർ", CTA_FILING, theme="faq",
 cap_ml="ഷെയർ ഒന്നുമില്ലാതെ ഒപ്പിടാൻ മാത്രം ഡയറക്ടറായാൽ ഫയലിംഗ് മുടങ്ങിയാൽ പ്രശ്നമുണ്ടോ? ഉണ്ട്. 3 വർഷം ഫയൽ ചെയ്യാത്ത കമ്പനിയുടെ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത വരാം, ഷെയർ ഇല്ലാത്തവർക്കും. നിങ്ങൾ ഏതെങ്കിലും കമ്പനിയിൽ ഡയറക്ടറാണോ?",
 cap_en="Made a director just to sign, with no shares at all: does a missed filing still affect you? Yes. If the company does not file for 3 years, its directors can be disqualified for 5 years, shareholders or not. Are you a director anywhere?",
 cap_mg="Share onnumillaathe oppidaan maathram director aayaal filing mudangiyaal prashnamundo? Undu. 3 varsham file cheyyaatha company-yude director-kku 5 varsham ayogyatha varaam, share illaathavarkkum. Ningal ethenkilum company-il director aano?")

duo("rc035", "new_company_roc", "A", "gym", "\"AGM മാർച്ച് 31-നുള്ളിൽ\nനടത്തിയാൽ മതി\"", [
 ("A","wide","ജസ്റ്റിനേ, സെൽഫ് ഡിഫൻസ് സ്റ്റുഡിയോയുടെ AGM മാർച്ചിൽ വെക്കാം. സാമ്പത്തിക വർഷം തീരുന്നതിന് മുമ്പ്."),
 ("V","V","റിയേ, ഇപ്പോ നവംബറാ. മാർച്ച് വരെ കാത്തിരുന്നാൽ പണി കിട്ടും."),
 ("A","A","അതെന്താ, വർഷം തീരാൻ ഇനിയും നാല് മാസമില്ലേ?"),
 ("V","wide","ഇല്ല. AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. അത് കഴിഞ്ഞു. AOC-4, MGT-7 വൈകുന്ന ഓരോ ദിവസവും ഫോം ഒന്നിന് 100 രൂപ."),
 ("A","A","അപ്പോ മാർച്ച് അല്ല, ഇന്ന് തന്നെ തുടങ്ങണം."),
 ("V","wide","കലണ്ടർ മാർച്ചിൽ തീരും. AGM സെപ്റ്റംബറിൽ.")],
 "കലണ്ടർ മാർച്ചിൽ,\nAGM സെപ്റ്റംബറിൽ", CTA_ROC, theme="faq",
 cap_ml="AGM സാമ്പത്തിക വർഷം തീരുന്ന മാർച്ച് 31-നുള്ളിൽ മതിയോ? ഇല്ല. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയുടെ AGM സെപ്റ്റംബർ 30-നുള്ളിൽ; AOC-4, MGT-7 വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ, പരിധിയില്ല. നിങ്ങളുടെ AGM നടന്നോ?",
 cap_en="Can the AGM wait until 31 March, the end of the financial year? No. A private limited company holds its AGM by 30 September; late AOC-4 and MGT-7 cost Rs 100 a day per form, with no cap. Has your AGM happened?",
 cap_mg="AGM financial year theerunna March 31-nullil mathiyo? Illa. Pvt Ltd company-yude AGM September 30-nullil; AOC-4, MGT-7 vaikiyaal form onninu divasam 100 roopa, limit illa. Ningalude AGM nadanno?")

duo("rc036", "late_filer", "B", "park", "ഓലപ്പന്ത് കമ്പനി.\n\"ROC റിമൈൻഡർ\nഅയക്കുമല്ലോ\"", [
 ("A","wide","അനന്തൂ, ഓലപ്പന്തും ഓലപ്പീപ്പിയും വിൽക്കുന്ന നമ്മുടെ കമ്പനിക്ക് ഇത്തവണ ഫയലിംഗ് ചെയ്തോ?"),
 ("V","V","ഗായത്രീ, സമയമാകുമ്പോൾ ROC ഒരു റിമൈൻഡർ അയക്കുമല്ലോ. ഒന്നും വന്നില്ല."),
 ("A","A","റിമൈൻഡറിന് കാത്തിരിക്കാം. പക്ഷേ ഡെഡ്‌ലൈൻ കാത്തിരിക്കില്ല."),
 ("V","wide","അപ്പോ തീയതി?"),
 ("A","wide","AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ. വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ, പരിധിയില്ല."),
 ("V","V","റിമൈൻഡർ വരില്ല. ലേറ്റ് ഫീ വരും.")],
 "റിമൈൻഡർ വരില്ല,\nലേറ്റ് ഫീ വരും", CTA_ROC, theme="new",
 cap_ml="ഓലപ്പന്തും ഓലപ്പീപ്പിയും ഉണ്ടാക്കുന്ന ചെറിയ കമ്പനി, ROC റിമൈൻഡറിന് കാത്തിരുന്നു. പക്ഷേ തീയതികൾ റിമൈൻഡർ നോക്കിയല്ല: AGM സെപ്റ്റംബർ 30-നുള്ളിൽ, AOC-4 30 ദിവസത്തിൽ, MGT-7 60 ദിവസത്തിൽ; വൈകിയാൽ ഫോം ഒന്നിന് ദിവസം 100 രൂപ. നിങ്ങളുടെ കമ്പനിയിൽ തീയതി ആര് ഓർക്കും?",
 cap_en="A small company making palm-leaf balls and whistles waited for a reminder from the ROC. The dates do not wait for one: AGM by 30 September, AOC-4 within 30 days, MGT-7 within 60 days; late fee Rs 100 a day per form, no cap. Who tracks the dates in your company?",
 cap_mg="Olappanthum olappeeppiyum undaakkunna cheriya company, ROC reminder-nu kaathirunnu. Pakshe theeyathikal reminder nokkiyalla: AGM September 30-nullil, AOC-4 30 divasathil, MGT-7 60 divasathil; vaikiyaal form onninu divasam 100 roopa. Ningalude company-il theeyathi aaru orkkum?")

duo("rc037", "dormant_company", "C", "beach", "ചീനവല റൈഡ് കമ്പനി.\n\"AGM അഞ്ച് വർഷത്തിൽ\nഒരിക്കലല്ലേ?\"", [
 ("A","wide","നിഖിലേ, ടൂറിസ്റ്റുകൾക്കുള്ള ചീനവല റൈഡ് കമ്പനിയുടെ AGM ഈ വർഷം നടത്തിയോ?"),
 ("V","V","ദിവ്യേ, കഴിഞ്ഞ വർഷം നടത്തിയല്ലോ. ക്ലബ്ബിന്റെ ഇലക്ഷൻ പോലെ അഞ്ച് വർഷം കൂടുമ്പോൾ മതി."),
 ("A","A","ക്ലബ്ബ് വേറെ, കമ്പനി വേറെ."),
 ("V","wide","എന്താ വ്യത്യാസം?"),
 ("A","wide","കമ്പനിക്ക് എല്ലാ വർഷവും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM. പിന്നെ AOC-4, MGT-7. ബിസിനസ് ഇല്ലാത്ത വർഷവും."),
 ("V","V","വല എല്ലാ ദിവസവും താഴും. AGM എല്ലാ വർഷവും.")],
 "വല എല്ലാ ദിവസവും,\nAGM എല്ലാ വർഷവും", CTA_ROC, theme="new",
 cap_ml="ടൂറിസ്റ്റുകൾക്ക് ചീനവല റൈഡ് നടത്തുന്ന കമ്പനി, ക്ലബ്ബ് ഇലക്ഷൻ പോലെ AGM അഞ്ച് വർഷത്തിൽ ഒരിക്കൽ മതിയെന്ന് കരുതി. പ്രൈവറ്റ് ലിമിറ്റഡിന് എല്ലാ വർഷവും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM, പിന്നെ AOC-4, MGT-7. നിങ്ങളുടെ അവസാന AGM എന്നായിരുന്നു?",
 cap_en="A company running Chinese-fishing-net rides for tourists thought the AGM, like a club election, was needed only every five years. A private limited company holds an AGM every year by 30 September, then files AOC-4 and MGT-7. When was your last AGM?",
 cap_mg="Tourists-nu cheenavala ride nadathunna company, club election pole AGM anchu varshathil orikkal mathiyennu karuthi. Pvt Ltd-nu ella varshavum September 30-nullil AGM, pinne AOC-4, MGT-7. Ningalude avasaana AGM ennaayirunnu?")
