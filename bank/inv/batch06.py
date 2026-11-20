# Investor batch 06 (21 Nov, month backlog). Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented).
# Facts only from topics.FACTS_INV. No amounts beyond statutory ones, no company values, no promises, no investment advice.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

# CRM #1 (asked investors before registering anything): tree-house builder, investor's first question "which company?" -> only a Pvt Ltd can issue shares
duo("vd038", "founder_raising", "A", "munnar", "\"ഏത് കമ്പനി?\"\nഇൻവെസ്റ്റർ ചോദിച്ചു.\nഉത്തരം: \"ഞാൻ\"", [
 ("A","wide","ബേസിലേ, നിന്റെ മരവീട് പ്രോജക്റ്റ് കൊള്ളാം. ഞാൻ ഷെയർ എടുക്കാം. ഏത് കമ്പനിയിലാ?"),
 ("V","V","സെലിനേ, കമ്പനി ഒന്നുമില്ല. പണിയും ഞാൻ, പേരും ഞാൻ, കണക്കും ഞാൻ."),
 ("A","A","അപ്പോ എനിക്ക് ഷെയർ എവിടുന്ന് തരും? നിന്റെ ഷർട്ടിന്റെ പോക്കറ്റിൽ നിന്നോ?"),
 ("A","wide","ഷെയർ ഇറക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്ററിനോ LLP-ക്കോ പാർട്ണർഷിപ്പിനോ ഷെയർ ഇല്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി, പിന്നെ പിച്ച്."),
 ("A","wide","മരത്തിന് മുകളിൽ വീട്, കമ്പനിക്ക് മുകളിൽ ഷെയർ.")],
 "മരത്തിന് മുകളിൽ വീട്,\nകമ്പനിക്ക് മുകളിൽ ഷെയർ", CTA_FUNDING, theme="crm",
 cap_ml="മലയോരത്ത് മരവീടുകൾ പണിയുന്ന ഒരാൾ ഇൻവെസ്റ്ററെ കണ്ടു, പക്ഷേ ആദ്യ ചോദ്യം 'ഏത് കമ്പനി?' ആയിരുന്നു. ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം; പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും ഷെയർ ഇറക്കാൻ പറ്റില്ല. നിങ്ങളുടെ ബിസിനസ് ഇപ്പോൾ ഏത് ഘടനയിലാ?",
 cap_en="A tree-house builder in the hills met an investor, and the first question was 'which company?'. Only a private limited company can take equity investment; a proprietorship, partnership or LLP cannot issue shares. What structure is your business in today?",
 cap_mg="Malayorathu maraveedukal paniyunna oraal investor-e kandu, pakshe aadya chodyam 'ethu company?' aayirunnu. Equity investment edukkaan private limited company venam; proprietorship-inum LLP-kkum share irakkaan pattilla. Ningalude business ippol ethu roopathila?")

# CRM #16 (Gulf Malayali investing in a Kerala startup): wants to send it from his sister's Kerala account -> money must come from the investor's own account
duo("vd039", "nri_investor", "A", "gulf", "\"പെങ്ങളുടെ അക്കൗണ്ടിൽ\nനിന്ന് അയച്ചാൽ\nപോരേ?\"", [
 ("A","wide","ഫൈസലേ, നാട്ടിലെ ആ മത്സ്യത്തീറ്റ സ്റ്റാർട്ടപ്പിൽ ഞാൻ ഇടുന്നുണ്ട്. പെങ്ങളുടെ അക്കൗണ്ടിൽ നിന്ന് അയക്കാൻ പറഞ്ഞു."),
 ("V","V","ഷിജൂ, ഷെയർ ആരുടെ പേരിലാ?"),
 ("A","A","എന്റെ പേരിൽ തന്നെ. പൈസ എന്റേതല്ലേ, ഏത് അക്കൗണ്ടായാലെന്താ?"),
 ("V","wide","പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ പണം ഇൻവെസ്റ്ററുടെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന്, കമ്പനിയുടെ വേറൊരു അക്കൗണ്ടിലേക്ക് വരണം."),
 ("A","A","അപ്പോ പെങ്ങളുടെ സ്നേഹം മതി, അക്കൗണ്ട് വേണ്ട."),
 ("V","wide","ഷെയർ നിന്റേതെങ്കിൽ, അക്കൗണ്ടും നിന്റേത്.")],
 "ഷെയർ നിന്റേതെങ്കിൽ,\nഅക്കൗണ്ടും നിന്റേത്", CTA_INVEST, theme="crm",
 cap_ml="ഗൾഫിലുള്ള ഒരാൾ നാട്ടിലെ സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കാൻ പെങ്ങളുടെ അക്കൗണ്ടിൽ നിന്ന് പണം അയക്കാൻ നോക്കി. ഷെയർ ആരുടെ പേരിലാണോ, പണം അയാളുടെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന് കമ്പനിയുടെ വേറൊരു അക്കൗണ്ടിലേക്ക് വരണം. നിങ്ങളുടെ നിക്ഷേപം ഏത് അക്കൗണ്ടിൽ നിന്നായിരുന്നു?",
 cap_en="A Gulf Malayali investing in a Kerala startup planned to send the money from his sister's account at home. In a private placement the money must come from the investor's own bank account into a separate company bank account, in the same name as the shares. Which account did your investment come from?",
 cap_mg="Gulf-il ulla oraal naattile startup-il invest cheyyaan pengalude account-il ninnu paisa ayakkaan nokki. Share aarude perilaano, paisa ayaalude swantham bank account-il ninnu company-yude veroru account-ilekku varanam. Ningalude investment ethu account-il ninnaayirunnu?")

# FAQ (investor side): paid, 75 days later still no shares -> allot within 60 days or refund within the next 15 days, else 12% interest
duo("vd040", "angel", "B", "tailor", "പണം കൊടുത്തിട്ട്\n75 ദിവസം.\nഷെയർ എവിടെ?", [
 ("A","wide","മോഹനേട്ടാ, ആ ഡ്രൈവിംഗ് സ്കൂൾ ആപ്പിൽ ഇട്ട പൈസയുടെ ഷെയർ കിട്ടിയോ?"),
 ("V","V","ഉഷേ, 75 ദിവസമായി. ചോദിക്കുമ്പോൾ 'അടുത്ത ആഴ്ച' എന്ന് മാത്രം."),
 ("A","A","അവർക്ക് സമയപരിധി ഉണ്ട്, മോഹനേട്ടാ."),
 ("A","wide","പണം കിട്ടി 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്യണം. ഇല്ലെങ്കിൽ അടുത്ത 15 ദിവസത്തിൽ തിരിച്ചുതരണം, വൈകിയാൽ 12% പലിശയോടെ."),
 ("V","V","അപ്പോ 'അടുത്ത ആഴ്ച'ക്കും നിയമത്തിൽ ഒരു തീയതി ഉണ്ട്."),
 ("A","wide","ഷെയറോ പണമോ, രണ്ടിലൊന്ന് തിരിച്ചുവരണം.")],
 "ഷെയറോ പണമോ,\nരണ്ടിലൊന്ന്\nതിരിച്ചുവരണം", CTA_FUNDING, theme="faq",
 cap_ml="ഒരു സ്റ്റാർട്ടപ്പിൽ പണം ഇട്ടിട്ട് 75 ദിവസമായിട്ടും ഷെയർ കിട്ടിയില്ലേ? പണം കിട്ടി 60 ദിവസത്തിനുള്ളിൽ കമ്പനി ഷെയർ അലോട്ട് ചെയ്യണം, അല്ലെങ്കിൽ അടുത്ത 15 ദിവസത്തിൽ തിരികെ നൽകണം, വൈകിയാൽ 12% പലിശ. നിങ്ങൾക്ക് ഷെയർ കിട്ടാൻ എത്ര ദിവസം എടുത്തു?",
 cap_en="Put money into a startup and still no shares after 75 days? The company must allot shares within 60 days of receiving the money, or refund it within the next 15 days, else with 12% interest. How many days did your allotment take?",
 cap_mg="Oru startup-il paisa ittittu 75 divasamaayittum share kittiyille? Paisa kitti 60 divasathinullil company share allot cheyyanam, allenkil aduttha 15 divasathil thirike nalkanam, vaikiyaal 12% palisha. Ningalkku share kittaan ethra divasam eduthu?")

# FAQ (investor side): small angel finds a drag-along clause and panics -> lets the majority require others to sell along; binds only via the articles
duo("vd041", "angel", "C", "garage", "SHA-യിൽ ഒരു വാക്ക്:\n\"ഡ്രാഗ്-അലോങ്\".\nഎന്നെ വലിച്ചിഴക്കുമോ?", [
 ("A","wide","ജിതിനേ, എന്റെ ഇ-സ്കൂട്ടർ കൺവേർഷൻ കമ്പനിയുടെ SHA വായിച്ചോ? ഒപ്പിടാൻ എന്താ ഇത്ര പേടി?"),
 ("V","V","ഐശ്വര്യേ, ഇതിൽ 'ഡ്രാഗ്-അലോങ്' എന്ന് കാണുന്നു. എന്റെ ഷെയർ നിർബന്ധിച്ച് വിൽപ്പിക്കുമോ?"),
 ("A","A","ഭൂരിഭാഗം ഷെയർഹോൾഡർമാർ കമ്പനി വിൽക്കാൻ തീരുമാനിച്ചാൽ, ബാക്കിയുള്ളവരും കൂടെ വിൽക്കണം എന്ന് ആവശ്യപ്പെടാം."),
 ("A","wide","അത് കമ്പനിയെ കെട്ടണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിലും എഴുതണം. അതുകൊണ്ട് ഒപ്പിടും മുമ്പ് രണ്ടും വായിക്കണം."),
 ("V","V","അപ്പോ പേടിക്കേണ്ടത് ക്ലോസിനെയല്ല, വായിക്കാത്തതിനെയാ."),
 ("A","wide","വായിക്കാത്ത ക്ലോസാ ശരിക്കും വലിക്കുന്നത്.")],
 "വായിക്കാത്ത ക്ലോസാ\nശരിക്കും വലിക്കുന്നത്", CTA_INVEST, theme="faq",
 cap_ml="ചെറിയ ഇൻവെസ്റ്റർ SHA-യിൽ 'ഡ്രാഗ്-അലോങ്' കണ്ട് പേടിച്ചു. ഭൂരിപക്ഷം കമ്പനി വിൽക്കാൻ തീരുമാനിച്ചാൽ ബാക്കിയുള്ളവരും കൂടെ വിൽക്കണം എന്ന് ആവശ്യപ്പെടാൻ പറ്റുന്ന ക്ലോസ്; ആർട്ടിക്കിൾസിൽ എഴുതിയാലേ കമ്പനിയെ കെട്ടൂ. നിങ്ങൾ ഒപ്പിട്ട SHA മുഴുവൻ വായിച്ചോ?",
 cap_en="A small investor saw 'drag-along' in the SHA and panicked. It lets the majority require the other shareholders to sell along when the company is sold, and it binds the company only once written into the Articles of Association. Did you read every clause of the SHA you signed?",
 cap_mg="Cheriya investor SHA-yil 'drag-along' kandu pedichu. Bhooripaksham company vilkkaan theerumaanichaal baakkiyullavarum koode vilkkanam ennu aavashyappedaan pattunna clause; Articles-il ezhuthiyaale company-ye kettoo. Ningal oppitta SHA muzhuvan vaayicho?")

# FAQ (founder side): investor asks for anti-dilution, co-founder takes it as an insult -> protects early money if a later round comes at a lower share rate
duo("vd042", "founder_raising", "A", "salon", "\"ആന്റി-ഡൈല്യൂഷൻ\nചോദിച്ചു. നമ്മളെ\nവിശ്വാസമില്ലേ?\"", [
 ("A","wide","വിനീതേ, നമ്മുടെ സലൂൺ ബുക്കിംഗ് ആപ്പിന്റെ ടേം ഷീറ്റിൽ ഇൻവെസ്റ്റർ ആന്റി-ഡൈല്യൂഷൻ ചോദിച്ചിട്ടുണ്ട്."),
 ("V","V","സോണിയേ, അതിനർത്ഥം നമ്മളെ വിശ്വാസമില്ലെന്നല്ലേ? ഞാൻ പറ്റില്ലെന്ന് പറയാൻ പോകുവാ."),
 ("A","A","അത് അപമാനമല്ല. അടുത്ത റൗണ്ട് കുറഞ്ഞ ഷെയർ നിരക്കിൽ വന്നാൽ ആദ്യം വന്നയാളെ കാക്കുന്ന ക്ലോസാ."),
 ("A","wide","SHA-യിൽ എഴുതിയാലും ആർട്ടിക്കിൾസിലും ചേർത്താലേ കമ്പനിയെ കെട്ടൂ. എത്ര, എങ്ങനെ എന്നത് ചർച്ച ചെയ്യാം."),
 ("V","V","അപ്പോ ചൂടാകേണ്ട, ക്ലോസ് വായിച്ച് ചർച്ച ചെയ്താൽ മതി."),
 ("A","wide","കുട ചോദിക്കുന്നത് മഴ വരുമെന്ന് ശപിച്ചിട്ടല്ല.")],
 "കുട ചോദിക്കുന്നത്\nമഴയെ ശപിച്ചിട്ടല്ല", CTA_TERMSHEET, theme="faq",
 cap_ml="ടേം ഷീറ്റിൽ ഇൻവെസ്റ്റർ ആന്റി-ഡൈല്യൂഷൻ ചോദിച്ചപ്പോൾ കോ-ഫൗണ്ടർക്ക് അത് അവിശ്വാസമായി തോന്നി. അടുത്ത റൗണ്ട് കുറഞ്ഞ ഷെയർ നിരക്കിൽ വന്നാൽ നേരത്തെ വന്ന ഇൻവെസ്റ്ററെ കാക്കുന്ന ക്ലോസാണ് അത്; ആർട്ടിക്കിൾസിൽ ചേർത്താലേ കമ്പനിയെ കെട്ടൂ. നിങ്ങളുടെ ടേം ഷീറ്റിൽ ഈ ക്ലോസ് ഉണ്ടോ?",
 cap_en="An investor asked for anti-dilution in the term sheet and a co-founder took it as distrust. It is a common clause that protects an early investor if a later round is raised at a lower share rate, and it binds the company only once written into the Articles. Is there an anti-dilution clause in your term sheet?",
 cap_mg="Term sheet-il investor anti-dilution chodichappol co-founder-kku athu aviswaasamaayi thonni. Aduttha round kuranja share nirakkil vannaal nerathe vanna investor-e kaakkunna clause aanu athu; Articles-il cherthaale company-ye kettoo. Ningalude term sheet-il ee clause undo?")

# NEW (d904: myth + vivid job): jackfruit-seed flour unit puts angel money into the daily sales account -> separate bank account; no use until PAS-3
duo("vd043", "founder_raising", "B", "kitchen", "\"പൈസ പൈസ തന്നെ.\nഒരു അക്കൗണ്ട്\nപോരേ?\"", [
 ("A","wide","രാജേഷേ, ഏഞ്ചലിന്റെ പൈസ നമ്മുടെ ചക്കക്കുരു പൊടിയുടെ ദിവസവരവ് വരുന്ന അക്കൗണ്ടിലേക്ക് തന്നെ ഇടാൻ പറഞ്ഞു."),
 ("V","V","ബിന്ദു, അത് പറ്റില്ല. ഇൻവെസ്റ്റ്മെന്റ് പണം വരേണ്ടത് കമ്പനിയുടെ വേറൊരു ബാങ്ക് അക്കൗണ്ടിലേക്കാ."),
 ("A","A","അതിൽ എന്താ വ്യത്യാസം? പൈസ പൈസ തന്നെയല്ലേ?"),
 ("V","wide","ഷെയർ അലോട്ട് ചെയ്ത് PAS-3 ഫയൽ ചെയ്യും വരെ ആ പണം ഉപയോഗിക്കാൻ പാടില്ല. കൂട്ടിക്കലർത്തിയാൽ ആര് പറയും ഏതാ ഏതെന്ന്?"),
 ("A","A","അപ്പോ ചാക്ക് വേറെ, അക്കൗണ്ടും വേറെ."),
 ("V","wide","ചക്കക്കുരുവും നിക്ഷേപവും ഒരേ ചാക്കിൽ വേണ്ട.")],
 "ചക്കക്കുരുവും നിക്ഷേപവും\nഒരേ ചാക്കിൽ വേണ്ട", CTA_FUNDING, theme="new",
 cap_ml="ചക്കക്കുരു പൊടി യൂണിറ്റ് ഏഞ്ചൽ ഇൻവെസ്റ്റ്മെന്റ് ദിവസവരവ് വരുന്ന അക്കൗണ്ടിൽ തന്നെ ഇടാൻ നോക്കി. പ്രൈവറ്റ് പ്ലേസ്മെന്റ് പണം കമ്പനിയുടെ വേറൊരു ബാങ്ക് അക്കൗണ്ടിൽ വരണം, PAS-3 ഫയൽ ചെയ്യും വരെ ഉപയോഗിക്കാനും പാടില്ല. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ബാങ്ക് അക്കൗണ്ട് ഉണ്ട്?",
 cap_en="A jackfruit-seed flour unit nearly put its angel money into the same account as daily sales. Private placement money must come into a separate company bank account and cannot be used until PAS-3 is filed after allotment. How many bank accounts does your company have?",
 cap_mg="Chakkakkuru podi unit angel investment divasavaravu varunna account-il thanne idaan nokki. Private placement paisa company-yude veroru bank account-il varanam, PAS-3 file cheyyum vare upayogikkaanum paadilla. Ningalude company-kku ethra bank account undu?")

# CRM #2 (runs it as a trust, investor can't get shares): palliative-care equipment rental run as a charitable trust -> only a Pvt Ltd can issue shares
duo("vd044", "founder_raising", "C", "pharmacy", "\"ട്രസ്റ്റിൽ ഷെയർ\nതരാം\" എന്ന്\nപറഞ്ഞുപോയി", [
 ("A","wide","പ്രവീണേ, നിന്റെ വീൽചെയർ, ഓക്സിജൻ വാടക സർവീസിൽ ഇൻവെസ്റ്റ് ചെയ്യാൻ ഒരു ഡോക്ടർ റെഡിയാണല്ലോ."),
 ("V","V","സിനീ, ഞാൻ 'ട്രസ്റ്റിൽ 10% ഷെയർ തരാം' എന്ന് പറഞ്ഞുപോയി. അത് ചാരിറ്റബിൾ ട്രസ്റ്റാ."),
 ("A","A","ട്രസ്റ്റിന് ഷെയർ ഇല്ലല്ലോ. പിന്നെ എന്ത് കൊടുക്കും?"),
 ("A","wide","ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി തന്നെ വേണം. ട്രസ്റ്റോ പാർട്ണർഷിപ്പോ LLP-യോ ഷെയർ ഇറക്കില്ല."),
 ("V","V","അപ്പോ സേവനം ട്രസ്റ്റിൽ, ബിസിനസ് കമ്പനിയിൽ. വേറെ വേറെ."),
 ("A","wide","ട്രസ്റ്റിൽ വിശ്വാസം ഉണ്ട്, ഷെയർ ഇല്ല.")],
 "ട്രസ്റ്റിൽ വിശ്വാസം ഉണ്ട്,\nഷെയർ ഇല്ല", CTA_FUNDING, theme="crm",
 cap_ml="വീൽചെയറും ഓക്സിജനും വാടകയ്ക്ക് നൽകുന്ന സേവനം ചാരിറ്റബിൾ ട്രസ്റ്റായി നടത്തുന്ന ഒരാൾ ഇൻവെസ്റ്റർക്ക് ഷെയർ വാഗ്ദാനം ചെയ്തു. ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം; ട്രസ്റ്റിനും LLP-ക്കും ഷെയർ ഇറക്കാൻ പറ്റില്ല. നിങ്ങളുടെ സംരംഭം ട്രസ്റ്റോ കമ്പനിയോ?",
 cap_en="A founder running a wheelchair and oxygen rental service as a charitable trust promised an investor shares. Only a private limited company can take equity investment; a trust, partnership or LLP cannot issue shares. Is your venture a trust or a company?",
 cap_mg="Wheelchair-um oxygen-um vaadakaykku nalkunna sevanam charitable trust aayi nadathunna oraal investor-kku share vaagdaanam cheythu. Equity investment edukkaan private limited company venam; trust-inum LLP-kkum share irakkaan pattilla. Ningalude samrambham trust-o company-o?")

# CRM #5 / C5 (two businesses under one name): catering + drone photography in one proprietorship, investor wants only the drone side -> shares need its own Pvt Ltd
duo("vd045", "founder_raising", "A", "canteen", "ഇൻവെസ്റ്റർക്ക് ഡ്രോൺ\nമതി. സദ്യ വേണ്ട.\nരണ്ടും ഒരു പേരിൽ", [
 ("A","wide","അമലേ, ഇൻവെസ്റ്റർ എന്ത് പറഞ്ഞു? നിന്റെ ഡ്രോൺ ഫോട്ടോഗ്രഫി ഇഷ്ടപ്പെട്ടോ?"),
 ("V","V","ആതിരേ, ഡ്രോൺ ഇഷ്ടപ്പെട്ടു. പക്ഷേ എന്റെ കാറ്ററിംഗും ഡ്രോണും ഒരേ പ്രൊപ്രൈറ്റർഷിപ്പ് പേരിലാ."),
 ("A","A","അയാൾക്ക് സദ്യയുടെ ഷെയർ വേണ്ടല്ലോ."),
 ("A","wide","പ്രൊപ്രൈറ്റർഷിപ്പിന് ഷെയർ ഇറക്കാൻ പറ്റില്ല. ഷെയർ കൊടുക്കാൻ ഡ്രോൺ ബിസിനസ് ഒരു പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയായി മാറണം."),
 ("V","V","അപ്പോ സദ്യ എന്റേത്, ഡ്രോൺ കമ്പനിയുടേത്."),
 ("A","wide","ഇലയും ഡ്രോണും ഒരു പന്തിയിൽ വിളമ്പരുത്.")],
 "ഇലയും ഡ്രോണും\nഒരു പന്തിയിൽ\nവിളമ്പരുത്", CTA_FUNDING, theme="crm",
 cap_ml="കാറ്ററിംഗും ഡ്രോൺ ഫോട്ടോഗ്രഫിയും ഒരേ പ്രൊപ്രൈറ്റർഷിപ്പ് പേരിൽ നടത്തുന്ന ഒരാൾക്ക് ഡ്രോൺ ഭാഗത്ത് മാത്രം ഇൻവെസ്റ്റർ താൽപര്യം കാണിച്ചു. ഷെയർ നൽകാൻ ആ ബിസിനസ് സ്വന്തം പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയിൽ വേണം. നിങ്ങൾ ഒരു പേരിൽ എത്ര ബിസിനസ് നടത്തുന്നു?",
 cap_en="A man running catering and drone photography under one proprietorship found an investor interested only in the drone side. A proprietorship cannot issue shares, so the business that takes investment has to sit in its own private limited company. How many businesses are you running under one name?",
 cap_mg="Catering-um drone photography-um ore proprietorship peril nadathunna oraalkku drone bhaagathu maathram investor thaalparyam kaanichu. Share nalkaan aa business swantham private limited company-il venam. Ningal oru peril ethra business nadathunnu?")

# NEW (d904: myth + vivid job): father puts his gratuity into his daughter's backwater boat-ambulance startup -> family money still needs shares, agreement, filings
duo("vd046", "family_money", "B", "akshaya", "\"അച്ഛന്റെ പൈസയ്ക്ക്\nഎന്തിനാ പേപ്പർ?\"", [
 ("A","wide","രമേശേ, അച്ഛൻ ഗ്രാറ്റുവിറ്റി മുഴുവൻ എന്റെ ബോട്ട് ആംബുലൻസ് കമ്പനിക്ക് തന്നു. അച്ഛനല്ലേ, പേപ്പർ വേണ്ടല്ലോ."),
 ("V","V","സുധേ, അച്ഛൻ ആയാലും അത് ഇൻവെസ്റ്റ്മെന്റാ. നാളെ അനിയൻ ചോദിച്ചാൽ എന്ത് കാണിക്കും?"),
 ("A","A","വീട്ടുകാര്യത്തിന് എഴുത്തുകുത്ത് വേണോ?"),
 ("V","wide","വീട്ടുകാരുടെ പണവും നിക്ഷേപം തന്നെ. ഷെയർ, എഗ്രിമെന്റ്, ഫയലിംഗ്: പുറത്തുള്ളവർക്ക് ചെയ്യുന്നതെല്ലാം ഇവിടെയും വേണം."),
 ("A","A","അപ്പോ അച്ഛനും ഷെയർഹോൾഡർ."),
 ("V","wide","അച്ഛന്റെ സ്നേഹത്തിന് പേപ്പർ വേണ്ട, ഷെയറിന് വേണം.")],
 "സ്നേഹത്തിന് പേപ്പർ\nവേണ്ട, ഷെയറിന്\nവേണം", CTA_INVEST, theme="new",
 cap_ml="കായലിൽ ബോട്ട് ആംബുലൻസ് തുടങ്ങിയ മകൾക്ക് അച്ഛൻ ഗ്രാറ്റുവിറ്റി മുഴുവൻ നൽകി, 'അച്ഛനല്ലേ, പേപ്പർ വേണ്ട' എന്നായിരുന്നു വിചാരം. വീട്ടുകാരുടെ പണവും നിക്ഷേപം തന്നെ: ഷെയർ, എഗ്രിമെന്റ്, ഫയലിംഗ് എല്ലാം വേണം. നിങ്ങളുടെ ബിസിനസിൽ വീട്ടുകാരുടെ പണം ഉണ്ടോ?",
 cap_en="A father gave his whole gratuity to his daughter's backwater boat-ambulance company, and she thought family money needs no papers. Money from family is still an investment: shares, an agreement and the filings are needed the same way as for an outsider. Is there family money in your business?",
 cap_mg="Kaayalil boat ambulance thudangiya makalkku achan gratuity muzhuvan nalki, 'achanalle, paper venda' ennaayirunnu vichaaram. Veettukaarude paisayum nikshepam thanne: share, agreement, filing ellaam venam. Ningalude business-il veettukaarude paisa undo?")

# FAQ (NRI investor): sister abroad wants shares at a 'family rate' below fair value -> repatriation basis needs not below fair value + FC-GPR; non-repat is domestic
chat("vc003", "nri_investor", "C", "\"ചേച്ചിയല്ലേ,\nകുടുംബ നിരക്കിൽ\nഷെയർ തന്നാൽ മതി\"", ("ടീന", "ജോബി"), [
 (0,"ജോബീ, കാനഡയിൽ നിന്ന് ഞാൻ നിന്റെ കമ്പനിയിൽ ഇടാം. ചേച്ചിയല്ലേ, കുടുംബ നിരക്കിൽ ഷെയർ തന്നാൽ മതി."),
 (1,"ടീനേച്ചീ, പൈസ പിന്നീട് കാനഡയിലേക്ക് തിരിച്ചുകൊണ്ടുപോകണോ?"),
 (0,"വേണം. അതിന് എന്താ?"),
 (1,"റീപാട്രിയേഷൻ ബേസിസിൽ ആണെങ്കിൽ ന്യായമായ മൂല്യത്തിൽ താഴെ ഷെയർ കൊടുക്കാൻ പറ്റില്ല. വാല്യുവേഷൻ റിപ്പോർട്ട് വേണം."),
 (1,"അലോട്ട് ചെയ്ത് 30 ദിവസത്തിനുള്ളിൽ RBI-ക്ക് FC-GPR. നോൺ-റീപാട്രിയേഷൻ ആണെങ്കിൽ നാട്ടിലെ നിക്ഷേപം പോലെ."),
 (0,"അപ്പോ സ്നേഹം അനിയന്, ന്യായമൂല്യം നിയമത്തിന്.")],
 "സ്നേഹം അനിയന്,\nന്യായമൂല്യം നിയമത്തിന്", CTA_INVEST, theme="faq",
 cap_ml="വിദേശത്തുള്ള ചേച്ചി അനിയന്റെ കമ്പനിയിൽ 'കുടുംബ നിരക്കിൽ' ഷെയർ ചോദിച്ചു. പണം തിരിച്ചുകൊണ്ടുപോകാവുന്ന റീപാട്രിയേഷൻ ബേസിസിൽ ന്യായമായ മൂല്യത്തിൽ താഴെ പറ്റില്ല, വാല്യുവേഷൻ റിപ്പോർട്ടും 30 ദിവസത്തിൽ FC-GPR-ഉം വേണം. നിങ്ങളുടെ വീട്ടിൽ ആരെങ്കിലും വിദേശത്ത് നിന്ന് നിക്ഷേപിക്കാൻ ആലോചിക്കുന്നുണ്ടോ?",
 cap_en="A sister abroad asked for shares in her brother's company at a 'family rate'. On a repatriation basis shares cannot be issued below fair value: a valuation report is needed and FC-GPR goes to RBI within 30 days of allotment. On a non-repatriation basis it is treated as domestic investment. Is anyone in your family planning to invest from abroad?",
 cap_mg="Videshathulla chechi aniyante company-il 'kudumba nirakkil' share chodichu. Paisa thirichu kondupokaavunna repatriation basis-il nyaayamaaya moolyathil thaazhe pattilla, valuation report-um 30 divasathil FC-GPR-um venam. Ningalude veettil aarenkilum videshathu ninnu invest cheyyaan aalochikkunnundo?")
