# Investor-agreement seed batch 01 (20 Nov). Both sides: founders raising and people investing. Short, conflict-first.
# Situations from bank/STORY_THEMES.md (anonymised; invented names/details). Facts only from topics.FACTS_INV. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

duo("vd001", "cofounder_split", "A", "cafe", "70/30 വാട്സ്ആപ്പിൽ\nഉറപ്പിച്ചു. 6 മാസം\nകഴിഞ്ഞ് അവൻ പോയി", [
 ("A","wide","റോഷൻ, നിന്റെ കോ-ഫൗണ്ടർ ഇപ്പോൾ എവിടെ? ആപ്പ് ലോഞ്ച് അടുത്തല്ലോ."),
 ("V","V","ആറ് മാസം കഴിഞ്ഞ് അവൻ വേറെ ജോലിക്ക് പോയി. പക്ഷേ മുപ്പത് ശതമാനം ഷെയർ ഇപ്പോഴും അവന്റെ കയ്യിൽ."),
 ("A","A","അതെങ്ങനെ? പണി ചെയ്യാത്ത ആൾക്ക് ഷെയർ?"),
 ("V","V","ഞങ്ങൾ വാട്സ്ആപ്പിൽ എഴുപത്-മുപ്പത് എന്ന് പറഞ്ഞു. വേറൊന്നും എഴുതിയില്ല."),
 ("A","wide","ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിൽ വെസ്റ്റിംഗ് വേണമായിരുന്നു. നിന്നാലേ ഷെയർ മുഴുവൻ കിട്ടൂ എന്ന്. ആർട്ടിക്കിൾസിലും അത് വേണം."),
 ("V","wide","അടുത്ത കോ-ഫൗണ്ടർക്ക് ആദ്യം എഗ്രിമെന്റ്.")],
 "ഷെയർ വീതിക്കും മുമ്പ്\nഎഗ്രിമെന്റ്", CTA_INVEST,
 cap_ml="കോ-ഫൗണ്ടർമാർ ഷെയർ 70/30 എന്ന് വാട്സ്ആപ്പിൽ മാത്രം ഉറപ്പിച്ചു; ഒരാൾ ആറ് മാസം കഴിഞ്ഞ് പോയിട്ടും 30% കയ്യിൽ. ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിൽ വെസ്റ്റിംഗ് എഴുതുക, ആർട്ടിക്കിൾസിലും ചേർക്കുക.",
 cap_en="Two co-founders agreed a 70/30 split on WhatsApp; one left after six months still holding 30%. Put founder vesting in a shareholders' agreement and the articles before you split equity. Co-founder agreement in Kerala.",
 cap_mg="Co-founders share 70/30 ennu WhatsApp-il maathram urappichu; oraal 6 maasam kazhinju poyittum 30% kayyil. Shareholders agreement-il vesting ezhuthuka, articles-ilum cherkkuka.")

duo("vd002", "family_money", "A", "home", "അമ്മാവൻ തന്ന 10 ലക്ഷം.\nഒരു പേപ്പറുമില്ല.\nഇപ്പോൾ തിരിച്ച് ചോദിക്കുന്നു", [
 ("A","wide","അരുൺ, എന്താ മുഖം വാടിയിരിക്കുന്നത്?"),
 ("V","V","സ്നേഹേ, ബിസിനസ് തുടങ്ങാൻ അമ്മാവൻ പത്ത് ലക്ഷം തന്നില്ലേ. ഇപ്പോൾ പലിശ സഹിതം തിരിച്ച് വേണമെന്ന്."),
 ("A","A","അത് കടമോ, ഷെയറോ? അന്ന് എന്താ പറഞ്ഞത്?"),
 ("V","V","ഒന്നും എഴുതിയില്ല. വീട്ടുകാരല്ലേ എന്ന് കരുതി."),
 ("A","wide","വീട്ടുകാരുടെ പൈസയും ഇൻവെസ്റ്റ്മെന്റ് ആണ്. ഷെയർ ആണെങ്കിൽ എഗ്രിമെന്റും അലോട്ട്മെന്റും ഫയലിംഗും വേണം."),
 ("V","wide","ഇനി ആരുടെ പൈസ ആയാലും ആദ്യം പേപ്പർ.")],
 "വീട്ടുകാരുടെ പൈസയ്ക്കും\nഎഗ്രിമെന്റ്", CTA_INVEST,
 cap_ml="ബിസിനസ് തുടങ്ങാൻ ബന്ധു തന്ന പൈസ, ഒരു എഗ്രിമെന്റും ഇല്ല; ഇപ്പോൾ പലിശ സഹിതം തിരിച്ച് ചോദിക്കുന്നു. വീട്ടുകാരുടെ പൈസയും ഇൻവെസ്റ്റ്മെന്റ് ആണ്: ഷെയർ ആണെങ്കിൽ എഗ്രിമെന്റ്, അലോട്ട്മെന്റ്, ഫയലിംഗ് വേണം.",
 cap_en="A relative put money into a Kerala founder's business with nothing in writing and now wants it back with interest. Friends-and-family money is still an investment: if it is for shares, you need an agreement, allotment and filings.",
 cap_mg="Business thudangaan bandhu thanna paisa, oru agreement-um illa; ippol interest sahitham thirichu chodikkunnu. Family paisayum investment aanu: share aanenkil agreement, allotment, filing venam.")

duo("vd003", "nri_investor", "A", "gulfroom", "ദുബായിൽ നിന്ന് കസിന്റെ\nസ്റ്റാർട്ടപ്പിൽ 25 ലക്ഷം.\n\"എന്റെ പൈസ സേഫ് ആണോ?\"", [
 ("A","wide","ഷംസു, നാട്ടിലെ കസിന്റെ ഫുഡ് ഡെലിവറി ആപ്പിൽ ഇടുന്നുണ്ടോ?"),
 ("V","V","ഇടാം എന്ന് വിചാരിക്കുന്നു. പക്ഷേ ഞാൻ ഇവിടെ, അവൻ അവിടെ. എനിക്ക് എന്ത് സുരക്ഷ?"),
 ("A","A","ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്. ബോർഡ് സീറ്റ്, നിന്റെ അറിവില്ലാതെ ഷെയർ വിൽക്കാൻ പറ്റാത്ത ക്ലോസ്, എക്സിറ്റ്."),
 ("V","V","ഞാൻ NRI അല്ലേ. വേറെ എന്തെങ്കിലും?"),
 ("A","wide","തിരികെ കൊണ്ടുപോകാവുന്ന രീതിയിൽ ആണെങ്കിൽ അലോട്ട്മെന്റ് കഴിഞ്ഞ് 30 ദിവസത്തിൽ RBI-ക്ക് റിപ്പോർട്ട്. വാല്യുവേഷൻ റിപ്പോർട്ടും വേണം."),
 ("V","wide","എങ്കിൽ ആദ്യം എഗ്രിമെന്റ്, പിന്നെ ട്രാൻസ്ഫർ.")],
 "നിക്ഷേപിക്കും മുമ്പ്\nനിങ്ങളുടെ സുരക്ഷ എഴുതൂ", CTA_INVEST,
 cap_ml="ദുബായിലുള്ള മലയാളി നാട്ടിലെ കസിന്റെ സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കാൻ: ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിൽ ബോർഡ് സീറ്റ്, ഷെയർ ട്രാൻസ്ഫർ നിയന്ത്രണം, എക്സിറ്റ്. റീപാട്രിയേഷൻ ബേസിസ് ആണെങ്കിൽ 30 ദിവസത്തിൽ FC-GPR.",
 cap_en="A Gulf Malayali wants to invest in his cousin's Kerala startup. Protect yourself with a shareholders' agreement (board seat, share transfer limits, exit). NRI investment on repatriation basis needs a valuation and FC-GPR reporting within 30 days of allotment.",
 cap_mg="Dubai-il ulla Malayali naattile cousin-nte startup-il invest cheyyaan: shareholders agreement-il board seat, share transfer limit, exit. Repatriation basis aanenkil 30 divasathil FC-GPR.")

duo("vd004", "founder_raising", "A", "office", "ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞു.\nപൈസ വന്നു. അടുത്ത ദിവസം\nഅത് ചെലവാക്കി. തെറ്റ്!", [
 ("A","wide","രാഹുൽ, ഫണ്ടിംഗ് കിട്ടിയല്ലോ! പാർട്ടി എപ്പോൾ?"),
 ("V","V","പാർട്ടി പോട്ടെ. പൈസ വന്ന അടുത്ത ദിവസം ഞാൻ ലാപ്ടോപ്പും ഓഫീസ് വാടകയും കൊടുത്തു."),
 ("A","A","ഷെയർ അലോട്ട് ചെയ്തോ? PAS-3 ഫയൽ ചെയ്തോ?"),
 ("V","V","അതൊക്കെ വേണോ?"),
 ("A","wide","വേണം. പൈസ പ്രത്യേക അക്കൗണ്ടിൽ. 60 ദിവസത്തിൽ അലോട്ട്മെന്റ്, 15 ദിവസത്തിൽ PAS-3. അത് കഴിഞ്ഞേ ആ പൈസ ഉപയോഗിക്കാവൂ."),
 ("V","wide","ഇനി ഓരോ സ്റ്റെപ്പും കലണ്ടറിൽ.")],
 "ഫണ്ടിംഗ് കിട്ടിയാൽ\nആദ്യം ഫയലിംഗ്", CTA_FUNDING,
 cap_ml="ഇൻവെസ്റ്റർ പൈസ വന്ന ഉടനെ ചെലവാക്കരുത്. പ്രത്യേക ബാങ്ക് അക്കൗണ്ട്, 60 ദിവസത്തിൽ ഷെയർ അലോട്ട്മെന്റ്, 15 ദിവസത്തിൽ PAS-3; PAS-3 ഫയൽ ചെയ്ത ശേഷമേ പൈസ ഉപയോഗിക്കാവൂ.",
 cap_en="Got investor money? Don't spend it yet. It sits in a separate bank account, shares are allotted within 60 days, PAS-3 is filed within 15 days of allotment, and only then can the company use the money. Startup funding compliance in India.",
 cap_mg="Investor paisa vanna udane chelavaakkaruthu. Separate bank account, 60 divasathil share allotment, 15 divasathil PAS-3; PAS-3 file cheytha sheshame paisa upayogikkaavu.")

chat("vc001", "founder_raising", "A", "\"പിച്ച് റിജക്റ്റ്.\nകാരണം ഒറ്റ വാക്ക്:\nവാലിഡേഷൻ\"", ("ആര്യ", "ശ്യാം"), [
 (1,"ചേച്ചി, ഇൻവെസ്റ്റർ എന്റെ പിച്ച് റിജക്റ്റ് ചെയ്തു. മാർക്കറ്റ് വാലിഡേഷൻ ഇല്ലെന്ന്."),
 (0,"എത്ര കസ്റ്റമർ ഇപ്പോൾ ഉണ്ട്?"),
 (1,"ഇതുവരെ ആരുമില്ല. ആപ്പ് റെഡി ആകുന്നതേയുള്ളൂ."),
 (0,"ആദ്യം പത്ത് പേർക്ക് വിൽക്ക്. അവരുടെ കണക്ക് കാണിക്ക്. അതാണ് വാലിഡേഷൻ."),
 (1,"അതിനിടയിൽ വേറെ എന്തെങ്കിലും?"),
 (0,"കമ്പനി രജിസ്ട്രേഷനും ഫൗണ്ടർ എഗ്രിമെന്റും റെഡിയാക്ക്. അടുത്ത യെസിന് പേപ്പർ വൈകരുത്.")],
 "ആദ്യം കസ്റ്റമർ,\nപിന്നെ ഇൻവെസ്റ്റർ", CTA_TERMSHEET,
 cap_ml="ഇൻവെസ്റ്റർ പിച്ച് റിജക്റ്റ് ചെയ്യാൻ സാധാരണ കാരണം: മാർക്കറ്റ് വാലിഡേഷൻ ഇല്ല. ആദ്യ കസ്റ്റമർമാരെ നേടൂ, അതിനിടയിൽ കമ്പനിയും ഫൗണ്ടർ എഗ്രിമെന്റും റെഡിയാക്കൂ.",
 cap_en="The most common reason an investor rejects a pitch: no market validation. Get your first paying customers, and meanwhile get the company and founder agreements ready so the next yes is not delayed by paperwork. Startup fundraising tips for Kerala founders.",
 cap_mg="Investor pitch reject cheyyaan saadharana kaaranam: market validation illa. Aadya customers-ne nedoo, athinidayil company-um founder agreement-um ready aakkoo.")

lst("vl001", "angel", "B", "സ്റ്റാർട്ടപ്പിൽ പൈസ\nഇടും മുമ്പ് ഇൻവെസ്റ്റർ\nചോദിക്കേണ്ട 3 ചോദ്യം", [
 ("ഇത് പ്രൈവറ്റ് ലിമിറ്റഡ് ആണോ?", "ഷെയർ കിട്ടാൻ കമ്പനി Pvt Ltd ആയിരിക്കണം."),
 ("എന്റെ അവകാശങ്ങൾ എവിടെ എഴുതും?", "ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിൽ, പിന്നെ ആർട്ടിക്കിൾസിലും."),
 ("ഷെയർ എപ്പോൾ കിട്ടും?", "പൈസ കിട്ടി 60 ദിവസത്തിനുള്ളിൽ അലോട്ട്മെന്റ്.")],
 "ചോദിച്ചിട്ട് മാത്രം\nട്രാൻസ്ഫർ", CTA_INVEST,
 cap_ml="സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കും മുമ്പ് ഇൻവെസ്റ്റർ ചോദിക്കേണ്ട മൂന്ന് ചോദ്യം: കമ്പനി പ്രൈവറ്റ് ലിമിറ്റഡ് ആണോ, അവകാശങ്ങൾ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിലും ആർട്ടിക്കിൾസിലും ഉണ്ടോ, 60 ദിവസത്തിൽ ഷെയർ അലോട്ട് ചെയ്യുമോ.",
 cap_en="Three questions to ask before you invest in a startup: is it a private limited company, where are your rights written (shareholders' agreement and articles), and will your shares be allotted within 60 days. Angel investing in Kerala.",
 cap_mg="Startup-il invest cheyyum mumbu investor chodikkenda 3 chodyam: company Pvt Ltd aano, rights shareholders agreement-ilum articles-ilum undo, 60 divasathil share allot cheyyumo.")

for _x in S: _x.setdefault("theme", "crm")   # built on bank/STORY_THEMES.md (anonymised CRM situations)
