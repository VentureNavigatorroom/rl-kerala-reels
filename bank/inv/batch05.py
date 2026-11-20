# Investor batch 05 (20 Nov evening, month backlog). Situations from bank/STORY_THEMES.md (anonymised; names, sectors, towns and numbers invented).
# Facts only from topics.FACTS_INV. No amounts beyond statutory ones, no company values, no promises.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

# CRM #16 (Gulf Malayali investor asks what protects him): founder could sell to a stranger -> right of first refusal, in the articles
duo("vd028", "nri_investor", "A", "gulfoffice", "\"അവൻ ഷെയർ ആർക്കെങ്കിലും\nവിറ്റാലോ?\"\nദുബായിൽ ഒരു ചോദ്യം", [
 ("A","wide","ആസിഫേ, അനിയത്തിയുടെ ഫ്രണ്ടിന്റെ ബേക്കറി സ്റ്റാർട്ടപ്പിൽ ഇടുകയാ. നാളെ അവൻ ഷെയർ ഏതോ ഒരാൾക്ക് വിറ്റാൽ ഞാൻ എന്ത് ചെയ്യും?"),
 ("V","V","ഷഹാനാ, SHA-യിൽ റൈറ്റ് ഓഫ് ഫസ്റ്റ് റിഫ്യൂസൽ ചോദിക്കൂ. വിൽക്കും മുമ്പ് ആദ്യം നിനക്ക് ഓഫർ ചെയ്യണം."),
 ("A","A","SHA-യിൽ എഴുതിയാൽ തീർന്നല്ലോ."),
 ("V","wide","തീർന്നില്ല. ആ അവകാശം കമ്പനിയെ കെട്ടണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിലും എഴുതണം. ആർട്ടിക്കിൾസ് ഭേദഗതി ചെയ്യണം."),
 ("A","A","അപ്പോ രണ്ട് പേപ്പറും ഒരേ കാര്യം പറയണം."),
 ("V","wide","ആദ്യ അവസരം നിനക്ക്, ആദ്യ പേജിൽ മാത്രമല്ല.")],
 "ആദ്യ അവസരം\nനിനക്ക്, കരാറിൽ\nമാത്രമല്ല", CTA_INVEST, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് ഒരു സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കുമ്പോൾ ഫൗണ്ടർ ഷെയർ മറ്റൊരാൾക്ക് വിറ്റാലോ? SHA-യിലെ റൈറ്റ് ഓഫ് ഫസ്റ്റ് റിഫ്യൂസൽ: വിൽക്കും മുമ്പ് ആദ്യം നിങ്ങൾക്ക് ഓഫർ. പക്ഷേ ഇത് കമ്പനിയെ കെട്ടാൻ ആർട്ടിക്കിൾസിലും എഴുതണം. നിങ്ങളുടെ SHA ആർട്ടിക്കിൾസുമായി ഒത്തുനോക്കിയോ?",
 cap_en="Investing from the Gulf and worried the founder may sell to a stranger? A right of first refusal in the SHA means the shares must be offered to you first, but it binds the company only once it is written into the Articles of Association. Has your SHA been matched with the articles: yes or no?",
 cap_mg="Gulf-il ninnu oru startup-il invest cheyyumbol founder share mattoraalkku vittaalo? SHA-yile right of first refusal: vilkkum mumpu aadyam ningalkku offer. Pakshe ithu company-ye kettaan Articles-ilum ezhuthanam. Ningalude SHA Articles-umaayi othunokkiyo?")

# CRM #18 (money in, compliance skipped): private placement taken on a board meeting alone; a special resolution is needed
duo("vd029", "founder_raising", "B", "photocopy", "\"ബോർഡ് മീറ്റിംഗിൽ\nതീരുമാനിച്ചു,\nപോരേ?\" പോരാ", [
 ("A","wide","ഉണ്ണീ, PAS-4 ഓഫർ ലെറ്ററിന്റെ 4 കോപ്പി എടുക്കണം. ഇൻവെസ്റ്റർക്ക് ഷെയർ കൊടുക്കാൻ ബോർഡ് മീറ്റിംഗിൽ തീരുമാനിച്ചു."),
 ("V","V","അശ്വതീ, കഴിഞ്ഞ ആഴ്ച ഇതേ ലെറ്ററിന് ഒരു CA വന്നിരുന്നു. ഷെയർഹോൾഡർമാരുടെ സ്പെഷ്യൽ റെസല്യൂഷൻ എവിടെ എന്ന് ചോദിച്ചു."),
 ("A","A","ഷെയർഹോൾഡർമാർ ഞങ്ങൾ രണ്ട് പേരല്ലേ ഉള്ളൂ."),
 ("V","wide","രണ്ടായാലും പ്രൈവറ്റ് പ്ലേസ്മെന്റിന് സ്പെഷ്യൽ റെസല്യൂഷൻ വേണം, പിന്നെ ഓഫർ ലെറ്റർ, പിന്നെ പണം."),
 ("A","A","അപ്പോ ആദ്യം ആ ഒരു പേജ്."),
 ("V","wide","കോപ്പി പിന്നെ, റെസല്യൂഷൻ ആദ്യം.")],
 "കോപ്പി പിന്നെ,\nറെസല്യൂഷൻ ആദ്യം", CTA_FUNDING, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർക്ക് പുതിയ ഷെയർ കൊടുക്കാൻ ബോർഡ് മീറ്റിംഗ് മാത്രം പോരാ. പ്രൈവറ്റ് പ്ലേസ്മെന്റിന് ഷെയർഹോൾഡർമാരുടെ സ്പെഷ്യൽ റെസല്യൂഷൻ, പിന്നെ PAS-4 ഓഫർ ലെറ്റർ, പിന്നെ ഇൻവെസ്റ്ററുടെ സ്വന്തം അക്കൗണ്ടിൽ നിന്ന് പണം. ഈ ക്രമം നിങ്ങൾക്ക് അറിയാമായിരുന്നോ?",
 cap_en="A board meeting alone is not enough to issue new shares to an investor. A private placement needs a special resolution of the shareholders, then the PAS-4 offer letter, then the money from the investor's own bank account. Did you know this order: yes or no?",
 cap_mg="Investor-kku puthiya share kodukkaan board meeting maathram poraa. Private placement-inu shareholders-inte special resolution, pinne PAS-4 offer letter, pinne investor-inte swantham account-il ninnu panam. Ee kramam ningalkku ariyaamaayirunno?")

# CRM #16 (investor side): the "costs" clause binds from signing even if the deal falls through
duo("vd030", "angel", "B", "railway", "ഡീൽ നടന്നില്ല.\nഎന്നിട്ടും വക്കീലിന്റെ\nബിൽ എനിക്ക്?", [
 ("A","wide","ദിനേശേ, ടേം ഷീറ്റ് മാത്രമേ ഒപ്പിട്ടുള്ളൂ, ഡീൽ നടന്നില്ല. എന്നിട്ടും ഇൻവെസ്റ്ററുടെ വക്കീലിന്റെ ബിൽ ഞങ്ങൾ കൊടുക്കണമെന്ന്."),
 ("V","V","ഷീബേ, ടേം ഷീറ്റിൽ കോസ്റ്റ്സ് എന്നൊരു ഭാഗം ഉണ്ടായിരുന്നോ?"),
 ("A","A","ഉണ്ടായിരുന്നു. പക്ഷേ ടേം ഷീറ്റ് ബൈൻഡിംഗ് അല്ലല്ലോ."),
 ("V","wide","മിക്കതും ബൈൻഡിംഗ് അല്ല. പക്ഷേ രഹസ്യാത്മകത, എക്സ്ക്ലൂസിവിറ്റി, ചെലവ്, ഏത് നിയമം എന്നിവ ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം."),
 ("A","A","അപ്പോ ആ ഒരു വരി ഞാൻ വായിച്ചില്ല."),
 ("V","wide","ഡീൽ ട്രെയിൻ പോയാലും, ടിക്കറ്റ് കയ്യിൽ.")],
 "ഡീൽ ട്രെയിൻ പോയാലും,\nടിക്കറ്റ് കയ്യിൽ", CTA_TERMSHEET, theme="crm",
 cap_ml="ടേം ഷീറ്റ് മിക്കവാറും ബൈൻഡിംഗ് അല്ല. പക്ഷേ രഹസ്യാത്മകത, എക്സ്ക്ലൂസിവിറ്റി (നോ-ഷോപ്പ്), ചെലവുകൾ, ഏത് നിയമം എന്നീ ഭാഗങ്ങൾ ഒപ്പിട്ട ദിവസം മുതൽ ബാധകമാണ്. ഡീൽ നടന്നില്ലെങ്കിലും. നിങ്ങളുടെ ടേം ഷീറ്റിൽ ചെലവ് ആര് വഹിക്കും?",
 cap_en="A term sheet is mostly non-binding, but confidentiality, exclusivity (no-shop), costs and governing law usually bind from the day you sign, even if the deal falls through. In your term sheet, who bears the costs?",
 cap_mg="Term sheet mikkavaarum binding alla. Pakshe confidentiality, exclusivity (no-shop), costs, governing law ennee bhaagangal oppitta divasam muthal baadhakam. Deal nadannillenkilum. Ningalude term sheet-il chelavu aaru vahikkum?")

# CRM #13 (friends-and-family money): cash in an envelope; money must come from the investor's own bank account
duo("vd031", "family_money", "A", "thattukada", "തട്ടുകടയിൽ ഒരു\nകവർ: \"3 ലക്ഷം, ക്യാഷ്.\nഷെയർ പിന്നെ മതി\"", [
 ("A","wide","ബിജുവേ, ഇതാ കവർ. നിന്റെ കോക്കനട്ട് മിൽക്ക് സ്റ്റാർട്ടപ്പിൽ എന്റെ പങ്ക്. ക്യാഷാ, ബാങ്ക് ഒന്നും വേണ്ട."),
 ("V","V","സിജോ, സ്നേഹം മനസ്സിലായി. പക്ഷേ ഇത് ഷെയറിനുള്ള പണമല്ലേ?"),
 ("A","A","അതെ, ഷെയർ നീ പിന്നെ എപ്പോഴെങ്കിലും എഴുതിത്തന്നാൽ മതി."),
 ("V","wide","ഷെയറിനുള്ള പണം നിന്റെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന് കമ്പനിയുടെ വേറിട്ട അക്കൗണ്ടിലേക്ക് വരണം. 60 ദിവസത്തിൽ അലോട്ട് ചെയ്യണം."),
 ("A","A","അപ്പോ കവർ തിരിച്ച്, ട്രാൻസ്ഫർ നാളെ."),
 ("V","wide","കവറിലെ പണം സമ്മാനം, ട്രാൻസ്ഫറിലേത് ഷെയർ.")],
 "കവറിലെ പണം സമ്മാനം,\nട്രാൻസ്ഫറിലേത് ഷെയർ", CTA_INVEST, theme="crm",
 cap_ml="സുഹൃത്ത് ഷെയറിനായി ക്യാഷ് കവർ നീട്ടിയാൽ? സുഹൃത്തിന്റെ പണവും നിക്ഷേപം തന്നെ. പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ പണം ഇൻവെസ്റ്ററുടെ സ്വന്തം ബാങ്ക് അക്കൗണ്ടിൽ നിന്ന് കമ്പനിയുടെ വേറിട്ട അക്കൗണ്ടിലേക്ക് വരണം, 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്യണം. നിങ്ങളുടെ ആദ്യ ഇൻവെസ്റ്റർ ആരായിരുന്നു: കൂട്ടുകാരനോ കുടുംബമോ?",
 cap_en="A friend offers cash in an envelope for shares? Money from friends is still an investment. In a private placement it must come from the investor's own bank account into a separate company bank account, and shares must be allotted within 60 days. Your first investor: friend or family?",
 cap_mg="Suhruthu share-inaayi cash cover neettiyaal? Suhruthinte panavum investment thanne. Private placement-il panam investor-inte swantham bank account-il ninnu company-yude separate account-ilekku varanam, 60 divasathinullil share allot cheyyanam. Ningalude aadya investor aaraayirunnu: koottukaarano kudumbamo?")

# FAQ: next round at a lower price shrinks the first angel's stake -> anti-dilution in the SHA and the articles
duo("vd032", "angel", "B", "bank", "ആദ്യം ഇട്ടത് ഞാൻ.\nപുതിയ റൗണ്ട് കുറഞ്ഞ\nനിരക്കിൽ. എന്റെ ഷെയർ?", [
 ("A","wide","മനോജേ, നീ ഇൻവെസ്റ്റ് ചെയ്ത ടൂറിസം ആപ്പ് പുതിയ റൗണ്ട് എടുക്കുന്നു, കഴിഞ്ഞ തവണത്തേക്കാൾ കുറഞ്ഞ നിരക്കിൽ എന്ന് കേട്ടു."),
 ("V","V","അതാ ശ്രുതീ പേടി. ഞാൻ കൊടുത്ത നിരക്ക് കൂടുതലായിരുന്നു, ഇനി എന്റെ പങ്ക് ചുരുങ്ങുമോ?"),
 ("A","A","നിന്റെ SHA-യിൽ ആന്റി-ഡൈല്യൂഷൻ എഴുതിയിട്ടുണ്ടോ?"),
 ("V","wide","ഉണ്ട്. പക്ഷേ ആർട്ടിക്കിൾസിൽ ഉണ്ടോ എന്ന് നോക്കിയിട്ടില്ല."),
 ("A","A","അതാ കാര്യം. SHA-യിലെ അവകാശം കമ്പനിയെ കെട്ടുന്നത് ആർട്ടിക്കിൾസിൽ എഴുതിയാൽ മാത്രം."),
 ("V","wide","അപ്പോ ആദ്യം ഒപ്പല്ല, ആർട്ടിക്കിൾസ് നോക്കണം.")],
 "നിരക്ക് താഴാം,\nനിന്റെ അവകാശം\nതാഴരുത്", CTA_TERMSHEET, theme="faq",
 cap_ml="അടുത്ത റൗണ്ട് കുറഞ്ഞ നിരക്കിൽ വന്നാൽ ആദ്യ ഇൻവെസ്റ്ററുടെ പങ്ക് എന്താകും? അതിനാണ് SHA-യിലെ ആന്റി-ഡൈല്യൂഷൻ അവകാശം. പക്ഷേ അത് കമ്പനിയെ കെട്ടണമെങ്കിൽ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിലും എഴുതണം. നിങ്ങളുടെ SHA-യിൽ ഇതുണ്ടോ?",
 cap_en="What happens to an early investor if the next round is raised at a lower share rate? That is what an anti-dilution right in the SHA is for, but it binds the company only when written into the Articles of Association. Does your SHA have one: yes or no?",
 cap_mg="Adutha round kuranja nirakkil vannaal aadya investor-inte panku enthaakum? Athinaanu SHA-yile anti-dilution right. Pakshe athu company-ye kettanamenkil Articles of Association-ilum ezhuthanam. Ningalude SHA-yil ithundo?")

# FAQ: founder posts the term sheet online to celebrate; confidentiality binds from signing
duo("vd033", "founder_raising", "A", "metro", "ടേം ഷീറ്റിന്റെ ഫോട്ടോ\nലിങ്ക്ഡ്ഇനിൽ.\n200 ലൈക്ക്. ഒരു മെയിൽ", [
 ("A","wide","കിരണേ, ടേം ഷീറ്റ് ഒപ്പിട്ടതിന്റെ ഫോട്ടോ ലിങ്ക്ഡ്ഇനിൽ ഇട്ടു. ഇപ്പോൾ ഇൻവെസ്റ്ററുടെ മെയിൽ: രഹസ്യം ലംഘിച്ചു എന്ന്."),
 ("V","V","അഞ്ജലീ, ഫോട്ടോയിൽ തുകയും നിബന്ധനകളും കാണാമായിരുന്നോ?"),
 ("A","A","കാണാം. പക്ഷേ ടേം ഷീറ്റ് ബൈൻഡിംഗ് അല്ലല്ലോ എന്ന് കരുതി."),
 ("V","wide","മിക്കതും അല്ല. പക്ഷേ രഹസ്യാത്മകത ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം. അതിനൊപ്പം നോ-ഷോപ്പും."),
 ("A","A","അപ്പോ പോസ്റ്റ് ഇപ്പോൾ തന്നെ മാറ്റാം."),
 ("V","wide","ആഘോഷം പണം വന്നിട്ട്, പോസ്റ്റ് ഡീൽ കഴിഞ്ഞിട്ട്.")],
 "ആഘോഷം പണം വന്നിട്ട്,\nപോസ്റ്റ് ഡീൽ\nകഴിഞ്ഞിട്ട്", CTA_TERMSHEET, theme="faq",
 cap_ml="ടേം ഷീറ്റ് ഒപ്പിട്ട സന്തോഷത്തിൽ അത് സോഷ്യൽ മീഡിയയിൽ ഇടാമോ? ടേം ഷീറ്റ് മിക്കവാറും ബൈൻഡിംഗ് അല്ലെങ്കിലും രഹസ്യാത്മകത, നോ-ഷോപ്പ്, ചെലവ്, ഏത് നിയമം എന്നീ ഭാഗങ്ങൾ ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം. നിങ്ങൾ ആദ്യം ആരോടാണ് പറഞ്ഞത്?",
 cap_en="Can you post your signed term sheet online to celebrate? A term sheet is mostly non-binding, but confidentiality, no-shop, costs and governing law usually bind from signing. Who did you tell first?",
 cap_mg="Term sheet oppitta santhoshathil athu social media-yil idaamo? Term sheet mikkavaarum binding allenkilum confidentiality, no-shop, costs, governing law ennee bhaagangal oppitta divasam muthal baadhakam. Ningal aadyam aarodaanu paranjathu?")

# FAQ: allotment missed; founder wants to "keep it as a loan" -> refund within 15 days or 12% interest
duo("vd034", "founder_raising", "C", "courier", "60 ദിവസം കഴിഞ്ഞു,\nഷെയർ ഇല്ല. \"അത്\nലോൺ ആക്കിയാലോ?\"", [
 ("A","wide","അരവിന്ദേ, ഇൻവെസ്റ്ററുടെ പണം വന്നിട്ട് 64 ദിവസം. ഷെയർ അലോട്ട് ചെയ്തില്ല. തൽക്കാലം അത് ലോൺ ആയി കാണിച്ചാലോ?"),
 ("V","V","ജയേ, പേര് മാറ്റിയാൽ നിയമം മാറില്ല. 60 ദിവസത്തിൽ അലോട്ട്മെന്റ് നടന്നില്ലെങ്കിൽ എന്ത് ചെയ്യണം എന്ന് നിയമം പറയുന്നുണ്ട്."),
 ("A","A","എന്താ പറയുന്നത്?"),
 ("V","wide","അടുത്ത 15 ദിവസത്തിനുള്ളിൽ പണം തിരികെ നൽകണം. വൈകിയാൽ 12% പലിശ."),
 ("A","A","അപ്പോ ഇനി ആഴ്ചകളേ ബാക്കിയുള്ളൂ."),
 ("V","wide","ഷെയർ അല്ലെങ്കിൽ തിരിച്ചടവ്. മൂന്നാമത്തെ വഴിയില്ല.")],
 "ഷെയർ അല്ലെങ്കിൽ\nതിരിച്ചടവ്. മൂന്നാം\nവഴിയില്ല", CTA_FUNDING, theme="faq",
 cap_ml="ഇൻവെസ്റ്ററുടെ പണം വന്ന് 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്തില്ലെങ്കിൽ അത് ലോൺ ആക്കി മാറ്റാമോ? ഇല്ല. അടുത്ത 15 ദിവസത്തിനുള്ളിൽ പണം തിരികെ നൽകണം, അല്ലെങ്കിൽ 12% പലിശ. നിങ്ങളുടെ അലോട്ട്മെന്റ് തീയതി കുറിച്ചിട്ടുണ്ടോ?",
 cap_en="Missed the 60-day allotment and thinking of calling the money a loan? Not allowed: if shares are not allotted within 60 days of receiving the money, it must be refunded within the next 15 days, or 12% interest applies. Have you noted your allotment date: yes or no?",
 cap_mg="Investor-inte panam vannu 60 divasathinullil share allot cheythillenkil athu loan aakki maattaamo? Illa. Adutha 15 divasathinullil panam thirike nalkanam, allenkil 12% palisha. Ningalude allotment date kurichittundo?")

# FAQ: drag-along: a buyer wants the whole company, one small shareholder refuses
duo("vd035", "cofounder_split", "C", "mall", "വാങ്ങാൻ ആളുണ്ട്,\n100% വേണം.\nഒരാൾ: \"ഞാൻ വിൽക്കില്ല\"", [
 ("A","wide","ജാഫറിക്കാ, നമ്മുടെ ഹോം ഡെക്കോർ ബ്രാൻഡ് മുഴുവനായി വാങ്ങാൻ ഒരു കമ്പനി വന്നു. പക്ഷേ 4% ഉള്ള നമ്മുടെ പഴയ ഡിസൈനർ വിൽക്കില്ലെന്ന്."),
 ("V","V","സുമയ്യാ, ഇൻവെസ്റ്റർ വന്നപ്പോൾ ഒപ്പിട്ട SHA-യിൽ ഡ്രാഗ്-അലോങ് ഉണ്ടായിരുന്നോ?"),
 ("A","A","അതെന്താ? ഞാൻ ഓർക്കുന്നില്ല."),
 ("V","wide","ഭൂരിപക്ഷം വിൽക്കുമ്പോൾ ചെറിയ ഷെയർഹോൾഡർമാരെയും കൂടെ വിൽക്കാൻ ബാധ്യസ്ഥരാക്കുന്ന ക്ലോസ്. ആർട്ടിക്കിൾസിലുണ്ടെങ്കിലേ കമ്പനിയെ കെട്ടൂ."),
 ("A","A","അപ്പോ ആദ്യം SHA-യും ആർട്ടിക്കിൾസും എടുക്കട്ടെ."),
 ("V","wide","ഡീൽ വരുമ്പോഴല്ല, ഷെയർ കൊടുക്കുമ്പോഴാ ഇത് എഴുതേണ്ടത്.")],
 "ഡീൽ വരുമ്പോഴല്ല,\nഷെയർ കൊടുക്കുമ്പോൾ\nഎഴുതണം", CTA_INVEST, theme="faq",
 cap_ml="കമ്പനി മുഴുവനായി വാങ്ങാൻ ആളുവന്നാൽ ഒരു ചെറിയ ഷെയർഹോൾഡർക്ക് ഡീൽ തടയാമോ? SHA-യിലെ ഡ്രാഗ്-അലോങ് ക്ലോസ് ഭൂരിപക്ഷം വിൽക്കുമ്പോൾ മറ്റുള്ളവരെയും കൂടെ വിൽക്കാൻ ബാധ്യസ്ഥരാക്കും; അത് ആർട്ടിക്കിൾസിലും എഴുതണം. നിങ്ങളുടെ SHA-യിൽ ഡ്രാഗ്-അലോങ് ഉണ്ടോ?",
 cap_en="A buyer wants 100% of the company and one small shareholder refuses: can they block it? A drag-along clause in the SHA lets the majority require the others to sell along, and it binds the company only when written into the articles too. Does your SHA have a drag-along: yes or no?",
 cap_mg="Company muzhuvanaayi vaangaan aalu vannaal oru cheriya shareholder-kku deal thadayaamo? SHA-yile drag-along clause bhooripaksham vilkkumbol mattullavareyum koode vilkkaan baadhyastharaakkum; athu Articles-ilum ezhuthanam. Ningalude SHA-yil drag-along undo?")

# NEW (d904 pattern, unusual Kerala job): banana-fibre pad startup; Gulf angel's term sheet picks a foreign law
duo("vd036", "founder_raising", "A", "farm", "വാഴനാരിൽ നിന്ന്\nപാഡ്. ടേം ഷീറ്റിൽ\nഖത്തറിലെ നിയമം", [
 ("A","wide","ഗോപിയേട്ടാ, വാഴനാര് പാഡ് സ്റ്റാർട്ടപ്പിന് ദോഹയിലെ ഒരാൾ പണം ഇടാമെന്ന്. ടേം ഷീറ്റിൽ ഏത് നിയമം എന്നിടത്ത് അവരുടെ രാജ്യം."),
 ("V","V","വാസൂ, ടേം ഷീറ്റല്ലേ, ബൈൻഡിംഗ് അല്ലെന്നല്ലേ എല്ലാരും പറയുന്നത്?"),
 ("A","A","ഞാനും അങ്ങനെ കരുതി ഒപ്പിടാൻ പോകുകയായിരുന്നു."),
 ("V","wide","പക്ഷേ ഏത് നിയമം, രഹസ്യാത്മകത, നോ-ഷോപ്പ്, ചെലവ്: ഇവ ഒപ്പിട്ട ദിവസം മുതൽ ബാധകമാണ് എന്ന് നമ്മുടെ CA പറഞ്ഞു."),
 ("A","A","അപ്പോ ആ വരി ഒന്ന് ചോദിച്ചിട്ട് ഒപ്പിടാം."),
 ("V","wide","വാഴ നാട്ടിൽ, നിയമം ദോഹയിൽ? ഒപ്പിന് മുമ്പ് ചോദിക്ക്.")],
 "വാഴ നാട്ടിൽ, നിയമം\nദോഹയിൽ? ഒപ്പിന്\nമുമ്പ് ചോദിക്കൂ", CTA_TERMSHEET, theme="new",
 cap_ml="ടേം ഷീറ്റ് ബൈൻഡിംഗ് അല്ലെന്ന് കരുതി ഒപ്പിടുമ്പോൾ ശ്രദ്ധിക്കേണ്ട വരി: ഏത് നിയമം (ഗവേണിംഗ് ലോ). അതും രഹസ്യാത്മകത, നോ-ഷോപ്പ്, ചെലവ് എന്നിവയും ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം. വാഴനാര് പാഡ് പോലെ നാടൻ ഐഡിയയ്ക്കും ഗൾഫ് ഇൻവെസ്റ്റർ വരാം. നിങ്ങളുടെ ടേം ഷീറ്റിൽ ഏത് നിയമമാണ്?",
 cap_en="Signing a term sheet because it is 'non-binding'? Check the governing law line: governing law, confidentiality, no-shop and costs usually bind from signing. Even a banana-fibre pad idea from a Kerala farm can draw a Gulf investor. Which law does your term sheet name?",
 cap_mg="Term sheet binding alla ennu karuthi oppidumbol shraddhikkenda vari: ethu niyamam (governing law). Athum confidentiality, no-shop, costs-um oppitta divasam muthal baadhakam. Vaazhanaaru pad pole naadan idea-kkum Gulf investor varaam. Ningalude term sheet-il ethu niyamamaanu?")

# NEW (d904 pattern): chenda-melam booking app; founder wants to sell 2% to his guru, the SHA limits transfers
duo("vd037", "cofounder_split", "B", "foodcourt", "\"എന്റെ ഷെയർ,\nഎന്റെ ഗുരുവിന്\nകൊടുക്കും\" പറ്റുമോ?", [
 ("A","wide","ഡെന്നിസേ, ചെണ്ടമേളം ബുക്കിംഗ് ആപ്പിലെ എന്റെ 2% ആശാന് കൊടുക്കണം. ഇൻവെസ്റ്റർ പറയുന്നു അവരുടെ സമ്മതം വേണമെന്ന്."),
 ("V","V","മരിയാ, ഷെയർ നിന്റേതാണ്. പക്ഷേ SHA-യിൽ ഷെയർ കൈമാറ്റത്തിന് നിയന്ത്രണം ഒപ്പിട്ടിട്ടില്ലേ?"),
 ("A","A","ഒപ്പിട്ടു. പക്ഷേ അത് സ്വന്തം ഷെയറിനും ബാധകമോ?"),
 ("V","wide","SHA-യിലെ കൈമാറ്റ നിയന്ത്രണം ആർട്ടിക്കിൾസിൽ എഴുതിയിട്ടുണ്ടെങ്കിൽ കമ്പനിയും അത് പാലിക്കും. ആദ്യം സമ്മതം, പിന്നെ കൈമാറ്റം."),
 ("A","A","ആശാന് താളം, ഇൻവെസ്റ്റർക്ക് സമ്മതം."),
 ("V","wide","താളം തെറ്റാതെ കൊട്ടണമെങ്കിൽ ആദ്യം പേപ്പർ നോക്ക്.")],
 "ഗുരുദക്ഷിണയും\nSHA വായിച്ചിട്ട്", CTA_INVEST, theme="new",
 cap_ml="ഫൗണ്ടർക്ക് സ്വന്തം ഷെയർ ആർക്കും കൊടുക്കാമോ? ഇൻവെസ്റ്റർ വന്ന ശേഷം SHA-യിൽ ഷെയർ കൈമാറ്റത്തിന് നിയന്ത്രണങ്ങൾ ഉണ്ടാകാം, ആർട്ടിക്കിൾസിൽ എഴുതിയാൽ അത് കമ്പനിയെയും കെട്ടും. ചെണ്ടമേളം ബുക്ക് ചെയ്യുന്ന ആപ്പിന്റെ ഫൗണ്ടർക്ക് പോലും. ഷെയർ കൊടുക്കും മുമ്പ് നിങ്ങൾ SHA വായിക്കുമോ?",
 cap_en="Can a founder give his own shares to anyone? After an investor comes in, the SHA may limit share transfers, and once written into the Articles of Association it binds the company too, even for the founder of a chenda-melam booking app. Would you read the SHA before gifting shares: yes or no?",
 cap_mg="Founder-kku swantham share aarkkum kodukkaamo? Investor vanna shesham SHA-yil share transfer-inu niyanthranangal undaakaam, Articles-il ezhuthiyaal athu company-yeyum kettum. Chenda melam book cheyyunna app-inte founder-kku polum. Share kodukkum mumpu ningal SHA vaayikkumo?")
