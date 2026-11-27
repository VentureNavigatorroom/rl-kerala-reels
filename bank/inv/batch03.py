# Investor seed batch 03 (19 Nov, backlog). Situations from bank/STORY_THEMES.md (anonymised; names and details invented).
# Facts only from topics.FACTS_INV. No amounts beyond statutory ones, no company values, no promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

duo("vd009", "family_money", "B", "home", "സുഹൃത്തിന്റെ പണം\nഒരു പേപ്പറും ഇല്ലാതെ\nവാങ്ങി", [
 ("A","wide","അരുണേ, ചങ്ങാതി 5 ലക്ഷം തന്നു. കമ്പനിയിൽ ഓഹരി വേണ്ടെന്ന് പറഞ്ഞു."),
 ("V","V","സ്നേഹേ, വെറുതെ വാങ്ങിയതല്ലേ? പേപ്പർ വേണ്ടല്ലോ."),
 ("A","A","സുഹൃത്തായാലും ഇത് നിക്ഷേപമാണ്. ഓഹരി, കരാർ, ഫയലിംഗ് എല്ലാം വേണം."),
 ("V","V","അപ്പോ ഓഹരി എങ്ങനെ കൊടുക്കും?"),
 ("A","wide","കമ്പനി പ്രൈവറ്റ് ലിമിറ്റഡ് ആണെങ്കിൽ പ്രൈവറ്റ് പ്ലേസ്മെന്റ് വഴി."),
 ("V","wide","പണം വന്നതിന് ശേഷം മാത്രമല്ല, രേഖ ആദ്യം.")],
 "സുഹൃത്തിന്റെ പണവും\nനിക്ഷേപം തന്നെ", CTA_INVEST, theme="faq",
 cap_ml="സുഹൃത്തുക്കളിൽ നിന്നുള്ള പണവും നിക്ഷേപമാണ്. ഓഹരി, കരാർ, ഫയലിംഗ് എന്നിവ ഒരുപോലെ വേണം. നിങ്ങൾ ഇതുവരെ ഒരു പേപ്പറും ഒപ്പിട്ടിട്ടുണ്ടോ?",
 cap_en="Money from a friend is still an investment. Shares, an agreement and filings are needed the same way. Have you signed any paper for money you already received?",
 cap_mg="Friends-inte kaasum investment thanne. Shares, agreement, filing ellam venam. Ningal oru paperum ozhippittundo?")

duo("vd010", "founder_raising", "A", "office", "LLP ആണ്.\nഇൻവെസ്റ്റർ ഓഹരി\nചോദിച്ചു", [
 ("A","wide","രാഹുലേ, ഇൻവെസ്റ്റർ ഓഹരി ചോദിക്കുന്നു. നമ്മുടേത് LLP ആണ്."),
 ("V","V","നേഹ, എല്ലാ കമ്പനിക്കും ഓഹരി കിട്ടില്ലേ?"),
 ("A","A","LLP-ക്ക് ഓഹരി ഇറക്കാൻ പറ്റില്ല. ഇക്വിറ്റി നിക്ഷേപത്തിന് പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം."),
 ("V","V","അപ്പോ മാറ്റം എങ്ങനെ?"),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡ് ആയി മാറുന്നതിന് മുമ്പ് ഇൻവെസ്റ്ററെ ഒപ്പിടുവിക്കരുത്."),
 ("V","wide","ഘടന ആദ്യം ശരിയാക്കൂ.")],
 "ഇക്വിറ്റിക്ക് വേണ്ടത്\nപ്രൈവറ്റ് ലിമിറ്റഡ്", CTA_FUNDING, theme="faq",
 cap_ml="ഇക്വിറ്റി നിക്ഷേപം സ്വീകരിക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. LLP-ക്ക് ഓഹരി ഇറക്കാൻ കഴിയില്ല. നിങ്ങളുടേത് ഏത് ഘടനയാണ്?",
 cap_en="Only a private limited company can take equity investment; an LLP cannot issue shares. Which structure is your business in right now?",
 cap_mg="Equity investment-nu private limited company venam. LLP-kku shares illa. Ningalude business etha structure?")

duo("vd012", "founder_raising", "A", "balcony", "SHA ഒപ്പിട്ടു.\nപക്ഷേ ആർട്ടിക്കിൾസിൽ\nഒന്നും ഇല്ല", [
 ("A","wide","വിവേകേ, SHA-യിൽ റൈറ്റ് ഓഫ് ഫസ്റ്റ് റിഫ്യൂസൽ എഴുതിയല്ലോ. കമ്പനിക്ക് ബാധകമല്ലേ?"),
 ("V","V","അമ്മൂ, SHA എല്ലാവരും ഒപ്പിട്ടതല്ലേ? അതുകൊണ്ട് ബാധകമല്ലേ?"),
 ("A","A","ഇല്ല. ഓഹരി കൈമാറ്റ നിയന്ത്രണങ്ങൾ കമ്പനിയെ ബാധിക്കണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിൽ എഴുതണം."),
 ("V","V","അപ്പോ ആർട്ടിക്കിൾസ് മാറ്റണം."),
 ("A","wide","അതെ. ടാഗ്-എലോംഗ്, ഡ്രാഗ്-എലോംഗ്, ബോർഡ് സീറ്റ് എല്ലാം അവിടെ വേണം."),
 ("V","wide","SHA മാത്രം കൊണ്ട് കാര്യം നടക്കില്ല.")],
 "SHA-യിലെ അവകാശം\nആർട്ടിക്കിൾസിലും വേണം", CTA_FUNDING, theme="new",
 cap_ml="ഷെയർഹോൾഡേഴ്സ് അഗ്രിമെന്റിലെ ഓഹരി കൈമാറ്റ നിയന്ത്രണങ്ങൾ കമ്പനിയെ ബാധിക്കണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിൽ എഴുതണം. നിങ്ങളുടെ ആർട്ടിക്കിൾസ് അപ്ഡേറ്റ് ചെയ്തോ?",
 cap_en="Share transfer limits in a shareholders' agreement bind the company only when they are written into the Articles of Association. Have you updated your Articles yet?",
 cap_mg="SHA-yile share transfer nianthranakal company-ye baadhikkanamenkil Articles of Association-il ezhuthanam. Ningalude Articles update cheytho?")

duo("vd013", "founder_raising", "B", "hospital", "പൈസ അക്കൗണ്ടിൽ വന്നു.\nPAS-3 ഫയൽ\nചെയ്തിട്ടില്ല", [
 ("A","wide","ജോസഫേ, ഇൻവെസ്റ്ററുടെ പൈസ അക്കൗണ്ടിൽ വന്നു. ഇനി ഉപയോഗിക്കാമല്ലോ?"),
 ("V","V","ലക്ഷ്മീ, അലോട്ട്മെന്റ് കഴിഞ്ഞോ? PAS-3 ഫയൽ ചെയ്തോ?"),
 ("A","A","അലോട്ട്മെന്റ് ചെയ്തു. പക്ഷേ PAS-3 ഇതുവരെ ഇല്ല."),
 ("V","V","അപ്പോ പൈസ ഇപ്പോഴും ഉപയോഗിക്കാൻ പറ്റില്ല."),
 ("A","wide","അതെ. അലോട്ട്മെന്റിന് ശേഷം പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("V","wide","പൈസ എവിടെയും ചെലവാക്കുന്നതിന് മുമ്പ് ഫയൽ ചെയ്യൂ.")],
 "PAS-3 ഫയൽ ചെയ്യാതെ\nപണം ഉപയോഗിക്കരുത്", CTA_FUNDING, theme="faq",
 cap_ml="പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ ഓഹരി അനുവദിച്ച ശേഷം പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ PAS-3 ഫയൽ ചെയ്യണം. അതുവരെ പണം ഉപയോഗിക്കാൻ പാടില്ല. നിങ്ങളുടെ അലോട്ട്മെന്റ് തീയതി എപ്പോഴായിരുന്നു?",
 cap_en="In a private placement, file PAS-3 within 15 days of allotment. The money cannot be used until then. When was your last allotment date?",
 cap_mg="Private placement-il shares allot cheytha sesham 15 divasathinullil PAS-3 file cheyyanam. Athuvare panam upayogikkaan pattilla. Ningalude allotment date eppozhaayirunnu?")

duo("vd014", "angel", "A", "library", "\"ഏഞ്ചൽ ടാക്സ്\nഉണ്ട്, അതുകൊണ്ട്\nവേണ്ട\"", [
 ("A","wide","അനൂപേ, ഏഞ്ചൽ ടാക്സ് ഉള്ളതുകൊണ്ട് ഇൻവെസ്റ്റർ വരില്ലെന്ന് ആരോ പറഞ്ഞു."),
 ("V","V","ഗ്രീഷ്മേ, അത് പഴയ കാര്യമാണ്. ഫിനാൻസ് വർഷം 2024-25 മുതൽ ഏഞ്ചൽ ടാക്സ് നിർത്തി."),
 ("A","A","എല്ലാ നിക്ഷേപകർക്കും ബാധകമല്ലെന്നാണോ?"),
 ("V","V","അതേ. ഇപ്പോൾ ആ വാദം ഉപയോഗിക്കേണ്ട."),
 ("A","wide","പക്ഷേ ഓഹരി നിബന്ധന, രേഖകൾ എന്നിവ ഇപ്പോഴും ശരിയാകണം."),
 ("V","wide","പഴയ നിയമം അല്ല, പുതിയ നിയമം നോക്കൂ.")],
 "ഏഞ്ചൽ ടാക്സ് 2024-25\nമുതൽ ഇല്ല", CTA_INVEST, theme="faq",
 cap_ml="ഏഞ്ചൽ ടാക്സ് 2024-25 സാമ്പത്തിക വർഷം മുതൽ എല്ലാ നിക്ഷേപകർക്കും നിർത്തലാക്കി. നിക്ഷേപകരെ തേടുമ്പോൾ പഴയ വാദം ഒഴിവാക്കൂ. നിങ്ങൾ എവിടെയാണ് ഇത് കേട്ടത്?",
 cap_en="Angel tax was abolished for all investors from financial year 2024-25. Drop the old argument when you pitch investors. Where did you first hear about angel tax?",
 cap_mg="Angel tax 2024-25 muthal ella investor-kkum nirthalakki. Pazhaya vaadam ozhivaakku. Ningal angel tax-nte kaaryam evide ninnu kettu?")

duo("vd015", "nri_investor", "B", "rooftop", "ദുബായിൽ നിന്ന് പണം.\nFC-GPR വേണോ?\nഎപ്പോൾ?", [
 ("A","wide","ശ്യാമേ, ദുബായിലെ കസിൻ തിരിച്ചു കൊണ്ടുപോകാവുന്ന രീതിയിൽ നിക്ഷേപിക്കുന്നു."),
 ("V","V","ആര്യേ, അപ്പോ റിപ്പാട്രിയേഷൻ ഉണ്ടെങ്കിൽ FC-GPR വേണം അല്ലേ?"),
 ("A","A","അതെ. ഓഹരി അനുവദിച്ച് മുപ്പത് ദിവസത്തിനുള്ളിൽ RBI-യെ അറിയിക്കണം."),
 ("V","V","നിബന്ധന ന്യായമായതായിരിക്കണമെന്ന് വേറെ നിയമമില്ലേ?"),
 ("A","wide","ഉണ്ട്. റിപ്പാട്രിയേഷൻ ആണെങ്കിൽ വാല്യുവേഷൻ റിപ്പോർട്ട് വേണം."),
 ("V","wide","തിരിച്ചുപോകാത്ത നിക്ഷേപമാണെങ്കിൽ ആഭ്യന്തരമായി കണക്കാക്കും.")],
 "തിരിച്ചു കൊണ്ടുപോകുന്ന\nNRI നിക്ഷേപം = FC-GPR", CTA_INVEST, theme="new",
 cap_ml="പ്രവാസി നിക്ഷേപകൻ തിരിച്ചു കൊണ്ടുപോകാവുന്ന രീതിയിൽ നിക്ഷേപിച്ചാൽ ഓഹരി അനുവദിച്ച് മുപ്പത് ദിവസത്തിനുള്ളിൽ FC-GPR റിപ്പോർട്ട് ചെയ്യണം. നിങ്ങളുടെ നിക്ഷേപകൻ ഏത് രീതിയിലാണ് പണം അയക്കുന്നത്?",
 cap_en="An NRI investment on a repatriation basis needs FC-GPR reporting to RBI within 30 days of allotment, on a fair value basis. How is your overseas investor sending the money?",
 cap_mg="NRI investment repatriation basis-il aanel allotment kazhinju 30 divasathinullil FC-GPR report cheyyanam. Ningalude overseas investor panam ethu reethiyil ayakkunnu?")

duo("vd016", "founder_raising", "A", "classroom", "ടേം ഷീറ്റ് ഒപ്പിട്ടാൽ\nഅടുത്തത് എന്ത്?\nക്രമം തെറ്റിയാൽ", [
 ("A","wide","ആദർശേ, ടേം ഷീറ്റ് ഒപ്പിട്ടു. ഇനി എന്ത് രേഖ വേണം?"),
 ("V","V","നിമ്മീ, ആദ്യം ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്. പിന്നെ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്."),
 ("A","A","അപ്പോ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ് പേടിക്കാതെ ആദ്യം പണം വാങ്ങാമോ?"),
 ("V","V","പണം വാങ്ങുന്നതിന് മുമ്പ് ക്രമം ശരിയാക്കണം."),
 ("A","wide","അതെ. ക്രമം തെറ്റിയാൽ അവകാശങ്ങൾ ദുർബലമാകും."),
 ("V","wide","ടേം ഷീറ്റ്, SSA, SHA. ഈ ക്രമം മനസ്സിൽ വെക്കൂ.")],
 "ടേം ഷീറ്റ്, SSA, SHA\nഈ ക്രമം മാറ്റരുത്", CTA_TERMSHEET, theme="faq",
 cap_ml="ടേം ഷീറ്റ്, ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ് (SSA), ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ് (SHA) എന്നീ ക്രമത്തിൽ രേഖകൾ വരുന്നു. ക്രമം തെറ്റിയാൽ അവകാശങ്ങൾ ദുർബലമാകും. നിങ്ങൾ ഇപ്പോൾ ഏത് ഘട്ടത്തിലാണ്?",
 cap_en="Investor documents come in order: term sheet, then share subscription agreement (SSA), then shareholders' agreement (SHA). Out of order weakens your rights. Which stage are you at now?",
 cap_mg="Term sheet, SSA, SHA enna kramathil documents varum. Kramam thettiyaal avakaashangal dhurbalamaakum. Ningal ippol etha ghattathilaanu?")

duo("vd017", "founder_raising", "B", "gym", "ബോർഡ് സീറ്റ്\nഎഴുതിയിട്ടും കിട്ടിയില്ല.\nകാരണം?", [
 ("A","wide","ജസ്റ്റിനേ, ഇൻവെസ്റ്റർക്ക് ബോർഡ് സീറ്റ് എഴുതിയ കരാർ ഉണ്ട്. പക്ഷേ മീറ്റിംഗിൽ വിളിച്ചില്ല."),
 ("V","V","റിയാ, കരാർ ഒപ്പിട്ടോ? ആർട്ടിക്കിൾസിൽ അത് ഉണ്ടോ?"),
 ("A","A","ഇല്ല. കരാറിലുണ്ട്, ആർട്ടിക്കിൾസിൽ ഇല്ല."),
 ("V","V","അപ്പോ കമ്പനി അത് ബാധകമാക്കാൻ ബാധ്യസ്ഥമല്ല."),
 ("A","wide","അതെ. ആർട്ടിക്കിൾസ് മാറ്റിയ ശേഷം മാത്രം ബോർഡ് സീറ്റ്."),
 ("V","wide","കരാർ മതി എന്ന് കരുതരുത്.")],
 "കരാറിൽ മാത്രം ബോർഡ് സീറ്റ്\nആർട്ടിക്കിൾസിൽ വേണം", CTA_FUNDING, theme="faq",
 cap_ml="ബോർഡ് സീറ്റ് പോലുള്ള അവകാശങ്ങൾ കമ്പനിയെ ബാധിക്കണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിൽ എഴുതണം. കരാറിൽ മാത്രം മതിയാകില്ല. നിങ്ങളുടെ ആർട്ടിക്കിൾസിൽ എന്തൊക്കെയുണ്ട്?",
 cap_en="Rights such as a board seat bind the company only when written in the Articles of Association, not in the agreement alone. What does your Articles currently say?",
 cap_mg="Board seat pole-ulla avakaashangal Articles of Association-il ezhuthanam. Karaarilmaathram mathiyaakilla. Ningalude Articles-il enthokkeyundu?")

duo("vd018", "founder_raising", "A", "beach", "വിദേശ നിക്ഷേപം\nന്യായമായ നിബന്ധന വേണം.\nഎന്ത് റിപ്പോർട്ട്?", [
 ("A","wide","നിഖിലേ, വിദേശ ഇൻവെസ്റ്റർ ഓഹരി വാങ്ങുന്നു. നിബന്ധന എങ്ങനെ തീരുമാനിക്കും?"),
 ("V","V","ദിവ്യേ, വാല്യുവേഷൻ റിപ്പോർട്ട് വേണം. നിബന്ധന ന്യായമായതായിരിക്കണം."),
 ("A","A","അപ്പോ പറയുന്ന നിബന്ധനയല്ല, റിപ്പോർട്ട് തീരുമാനിക്കും."),
 ("V","V","അതേ. നിബന്ധനയുടെ അടിസ്ഥാനം എഴുതി വെക്കണം."),
 ("A","wide","രേഖ ഇല്ലെങ്കിൽ റിസർവ് ബാങ്ക് ഫയലിംഗ് തടസ്സപ്പെടും."),
 ("V","wide","വാല്യുവേഷൻ ആദ്യം, ഒപ്പിടൽ പിന്നീട്.")],
 "വാല്യുവേഷൻ റിപ്പോർട്ട്\nഇല്ലെങ്കിൽ വിദേശ നിക്ഷേപം തടസ്സം", CTA_INVEST, theme="new",
 cap_ml="തിരിച്ചു കൊണ്ടുപോകാവുന്ന വിദേശ നിക്ഷേപത്തിന് ന്യായമായ നിബന്ധനയ്ക്കുള്ള വാല്യുവേഷൻ റിപ്പോർട്ട് വേണം. നിബന്ധന പറയുന്നതിന് മുമ്പ് റിപ്പോർട്ട് തയ്യാറാക്കൂ. നിങ്ങളുടെ ഇൻവെസ്റ്റർ വിദേശത്താണോ?",
 cap_en="A repatriable foreign investment needs a valuation report that supports fair terms. Prepare the report before you agree the terms. Is your investor based overseas?",
 cap_mg="Repatriation-yulla videshi nikshepathinu nyaya vilakku valuation report venam. Vila parayunnathinu mumpu report thayyaarakkoo. Ningalude investor videshathaano?")
