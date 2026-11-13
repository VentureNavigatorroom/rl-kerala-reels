# Script bank, batch 12. New situations: a car photographer whose dealership group wants a yearly contract, a fashion stylist who
# wants a magazine's name, a medical writer paid only after 14 months, a sign-language interpreter whose channel wants a stake in her
# captioning tool, a tattoo artist 40 days past incorporation with no auditor, a violin accompanist signing with a Dubai dance-school
# chain from a rented flat, a home elder-care app where one founder "only invests", a rooftop film club at day 150, a Malayalam
# keyboard app registered as a partnership, a campus laundry pickup by two final-year students, jar meals named after a supermarket's
# brand, a paddy-spraying drone pair racing the season, a bank cashier's leather wallets for a hotel gift shop, a radiographer's
# Saturday CPR classes with no revenue yet, a mill supervisor and a tailor who think registration means a month of leave, a
# Technopark employee whose US cousin wants shares in his aunt's handloom, cabin crew with a travel-pillow brand, an office admin
# whose side-company name is one letter from an existing company.
# Same fact list and no-price rule as batch01. Segments freelancer 7, cofounders 7, salaried 6; 15 duo3d in 15 different locations
# (the least used so far), default names. Every script carries cap_ml / cap_en / cap_mg (captions.py adds hook, CTA and hashtags).
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS

S = []
def duo(id, segment, bucket, scene, hook, lines, end, cta, names=None, sound=None, **kw):
    d = dict(id=id, kind="duo3d", scene=scene, names=names, segment=segment, bucket=bucket, hook=hook, lines=lines, end=end, cta=cta, **kw)
    if sound: d["sound"] = sound
    S.append(d)
def chat(id, segment, bucket, hook, names, lines, end, cta, **kw): S.append(dict(id=id, kind="chat", segment=segment, bucket=bucket, hook=hook, names=names, lines=lines, end=end, cta=cta, **kw))
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))

# ---------------- freelancer ----------------
# busstop: Jibin + Akhil. Akhil shoots cars for dealerships; a dealership group wants a yearly contract with a company; he thinks that means taking a job.
duo("d1401", "freelancer", "A", "busstop", "കാർ ഫോട്ടോഗ്രാഫർ.\nഡീലർഷിപ്പ് ഗ്രൂപ്പ്:\n\"ഒരു വർഷത്തെ കോൺട്രാക്ട്\"", [
 ("A","wide","അഖിലേ, ബസ് മൂന്നെണ്ണം പോയി. നീ ഫോണിൽ നിന്ന് തല പൊക്കുന്നില്ലല്ലോ."),
 ("V","V","ജിബിനേ, ആ കാർ ഡീലർഷിപ്പ് ഗ്രൂപ്പ്. അവരുടെ ആറ് ഷോറൂമിലെയും ഫോട്ടോ ഒരു വർഷത്തേക്ക് എനിക്ക്."),
 ("A","A","ഒരു വർഷം! പിന്നെന്താ മുഖം ബ്രേക്ക് ഡൗൺ ആയ ബസ് പോലെ?"),
 ("V","V","കോൺട്രാക്ട് കമ്പനിയുമായി മാത്രം. ഞാൻ ഒറ്റയ്ക്കല്ലേ. ഫ്രീലാൻസ് നിർത്തി ഏതെങ്കിലും കമ്പനിയിൽ ജോലിക്ക് കയറണോ?"),
 ("A","wide","എന്തിന്! ഒറ്റയ്ക്കുള്ളവർക്ക് സ്വന്തം കമ്പനി തുടങ്ങാം. വൺ പേഴ്സൺ കമ്പനി. OPC."),
 ("A","A","നീ തന്നെ ഉടമ. നീ തന്നെ ഡയറക്ടർ. പാർട്ണറെ തേടി നടക്കണ്ട."),
 ("V","V","അപ്പോ ഞാൻ ജോലി തേടണ്ട, എന്റെ കമ്പനി ജോലി തരും!"),
 ("A","A","അതെ. ആദ്യം കമ്പനി, പിന്നെ കോൺട്രാക്ട്. ഡീലർ കാത്തിരിക്കില്ല."),
 ("V","wide","ശരി. അടുത്ത ബസിൽ കയറുന്നത് ഡയറക്ടർ ആയിട്ട്!")],
 "ഒറ്റയ്ക്കാണോ?\nOPC ഉണ്ട്", CTA_START,
 cap_ml="കാർ ഡീലർഷിപ്പുകൾക്ക് ഫോട്ടോ എടുക്കുന്ന ഫ്രീലാൻസർക്ക് ഒരു വർഷത്തെ കോൺട്രാക്ട്, പക്ഷേ കമ്പനിയുമായി മാത്രം. ഒറ്റയ്ക്കാണെങ്കിൽ ജോലിക്ക് കയറണ്ട, വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം. ഉടമയും ഡയറക്ടറും നിങ്ങൾ തന്നെ.",
 cap_en="A freelance car photographer in Kerala is offered a year-long contract by a dealership group that signs only with companies. He thinks he must take a job, but a solo founder can register a One Person Company (OPC) and stay his own boss.",
 cap_mg="Car dealership-nu photo edukkunna freelancer-nu 1 varsha contract, pakshe company-yumaayi maathram. Ottaykku aanenkil job-nu keranda, one person company (OPC) register cheyyaam. Owner-um director-um ningal thanne.")

# textile: Remya + Prakash. Remya styles ad shoots freelance and wants to call her company after a famous fashion magazine.
duo("d1402", "freelancer", "B", "textile", "ഫ്രീലാൻസ് സ്റ്റൈലിസ്റ്റ്.\nകമ്പനിക്ക് പേര്:\nഒരു ഫാഷൻ മാസികയുടേത്", [
 ("V","wide","രമ്യേ, സാരി നോക്കാൻ വന്നിട്ട് ബില്ലിന്റെ പുറകിൽ എന്താ എഴുതുന്നത്?"),
 ("A","A","പ്രകാശേട്ടാ, എന്റെ കമ്പനിയുടെ പേര്. ആഡ് ഷൂട്ടുകൾക്ക് ഇനി ഇൻവോയ്സ് കമ്പനിയുടെ പേരിൽ വേണമെന്ന് ഏജൻസി."),
 ("V","V","എന്നിട്ട് പേര് കിട്ടിയോ?"),
 ("A","A","കിട്ടി. ആ ഫേമസ് ഫാഷൻ മാസികയുടെ പേര്, പിന്നെ കേരള. കേട്ടാൽ തന്നെ ക്ലാസ്സ്!"),
 ("V","wide","ക്ലാസ്സ് ഒക്കെ ശരി. പക്ഷേ ട്രേഡ്മാർക്ക് ഉള്ള ഒരു ബ്രാൻഡിന്റെ പേരുമായി സാമ്യം ഉണ്ടെങ്കിൽ കമ്പനി പേര് റിജക്ട് ആകാം."),
 ("V","V","റിജക്ട് ആയാൽ വീണ്ടും പേര് കൊടുക്കണം. അപ്പോ ഏജൻസിയുടെ ഡേറ്റും പോകും."),
 ("A","A","അയ്യോ. എന്റെ സ്വന്തം സ്റ്റൈലിന് മറ്റൊരാളുടെ പേര്. അത് തന്നെ സ്റ്റൈൽ അല്ലല്ലോ."),
 ("V","V","അതാ. നിന്റെ സ്വന്തം വാക്ക് വെച്ച് മൂന്ന് പേര് എഴുത്. ആരുടെയും കോപ്പി വേണ്ട."),
 ("A","wide","ശരി. പേരിനും ഇനി ഞാൻ തന്നെ സ്റ്റൈലിംഗ്!")],
 "വലിയ ബ്രാൻഡിന്റെ പേര്\nകടം എടുക്കല്ലേ", CTA_NAME,
 cap_ml="ആഡ് ഷൂട്ടുകൾക്ക് സ്റ്റൈലിംഗ് ചെയ്യുന്ന ഫ്രീലാൻസർക്ക് ഒരു ഫാഷൻ മാസികയുടെ പേരിൽ കമ്പനി വേണം. ട്രേഡ്മാർക്ക് ഉള്ള ബ്രാൻഡിനോട് സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകാം. സ്വന്തം വാക്കുകൾ വെച്ച് രണ്ടുമൂന്ന് പേര് കരുതൂ.",
 cap_en="A freelance fashion stylist in Kochi wants to name her company after a famous fashion magazine. A company name that clashes with a trademark can be rejected at registration, so build two or three names from your own words before you apply.",
 cap_mg="Ad shoot-nu styling cheyyunna freelancer-nu oru fashion magazine-nte perilu company venam. Trademark ulla brand-inodu saamyam ulla company name reject aakaam. Swantham words vechu 2-3 names ready aakku.")

# pharmacy: Sini + Praveen. Sini writes medical content for a Hyderabad pharma firm that pays only after 14 months; her company has no revenue this year.
duo("d1403", "freelancer", "C", "pharmacy", "ക്ലയന്റ് പൈസ തരുന്നത്\n14 മാസം കഴിഞ്ഞ്.\n\"അതുവരെ ഫയലിംഗ് വേണ്ടല്ലോ\"", [
 ("V","wide","സിനിചേച്ചീ, ഗുളികയുടെ പേര് പോലും ചേച്ചിക്ക് മനഃപാഠമാണല്ലോ. എഴുത്ത് എങ്ങനെ പോകുന്നു?"),
 ("A","A","പ്രവീണേ, ഹൈദരാബാദിലെ ഫാർമ കമ്പനിക്ക് വേണ്ടി ഒരു വലിയ പ്രോജക്ട്. പക്ഷേ പൈസ പതിനാല് മാസം കഴിഞ്ഞേ വരൂ."),
 ("V","V","അപ്പോ ഈ വർഷം ചേച്ചിയുടെ കമ്പനിക്ക് വരുമാനം പൂജ്യം?"),
 ("A","A","പൂജ്യം. അതുകൊണ്ട് ഈ വർഷം ഫയലിംഗ് ഒന്നും വേണ്ടല്ലോ. സമാധാനം."),
 ("V","wide","അത് മരുന്നിന്റെ സൈഡ് ഇഫക്ട് പോലെയാ ചേച്ചീ. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("V","V","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ വെച്ച് ലേറ്റ് ഫീ."),
 ("A","A","പതിനാല് മാസം ദിവസം നൂറ് വെച്ച്… പ്രോജക്ട് പൈസ വരും മുമ്പ് പിഴ വരും!"),
 ("V","V","അതാ. ഡ്യൂ ഡേറ്റ് ഇപ്പോ തന്നെ കലണ്ടറിൽ ഇട്. ഒരു റിമൈൻഡറും."),
 ("A","wide","ശരി ഡോക്ടർ. ഡോസ് മുടക്കില്ല!")],
 "വരുമാനം പൂജ്യം.\nഫയലിംഗ് പൂജ്യം അല്ല", CTA_AFTER,
 cap_ml="ഫാർമ കമ്പനിക്ക് മെഡിക്കൽ കണ്ടന്റ് എഴുതുന്ന ഫ്രീലാൻസർക്ക് പേയ്മെന്റ് 14 മാസം കഴിഞ്ഞ്, ഈ വർഷം കമ്പനിക്ക് വരുമാനമില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A freelance medical writer in Kerala will be paid by her pharma client only after 14 months, so her company has zero revenue this year. Annual filings are still due with zero revenue, and late filing costs Rs 100 per day per form.",
 cap_mg="Pharma company-kku medical content ezhuthunna freelancer-nu payment 14 maasam kazhinju, ee varsham company-kku revenue illa. Zero revenue aanenkilum annual filing cheyyanam. Vaikiyal oro form-inum divasam 100 roopa penalty.")

# classroom: Nimmi + Adarsh. Nimmi interprets the news in sign language; the channel's parent group wants 20% of the captioning tool she built.
duo("d1404", "freelancer", "A", "classroom", "ആംഗ്യഭാഷയിൽ വാർത്ത.\nചാനൽ ചോദിച്ചു:\n\"നിന്റെ ടൂളിൽ 20% തരുമോ?\"", [
 ("V","wide","നിമ്മി ടീച്ചറേ, ക്ലാസ് കഴിഞ്ഞിട്ടും കൈ കൊണ്ട് എന്തോ പറഞ്ഞ് ചിരിക്കുന്നല്ലോ."),
 ("A","A","ആദർശേ, വാർത്ത ആംഗ്യഭാഷയിൽ ചെയ്യുന്ന ആ ചാനൽ ഇല്ലേ. അവരുടെ ഗ്രൂപ്പ് ഒരു ഓഫർ തന്നു."),
 ("A","A","ഞാൻ ഉണ്ടാക്കിയ ക്യാപ്ഷനിംഗ് ടൂളിൽ ഇരുപത് ശതമാനം. പകരം നല്ലൊരു നിക്ഷേപം."),
 ("V","V","സൂപ്പർ! ടൂൾ ഏത് കമ്പനിയുടെ പേരിലാ?"),
 ("A","A","കമ്പനി ഒന്നുമില്ല. ഞാൻ ഫ്രീലാൻസ്. എന്റെ പേരിൽ ഒരു പ്രൊപ്രൈറ്റർഷിപ്പ്."),
 ("V","wide","അപ്പോ ഇരുപത് ശതമാനം എന്തിൽ കൊടുക്കും? ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം."),
 ("V","V","പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും പാർട്ണർഷിപ്പിനും ഷെയർ ഇല്ല."),
 ("A","A","അപ്പോ ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്. എന്നിട്ട് ഇരുപത് ശതമാനം."),
 ("V","wide","അതെ. ഇത് ആംഗ്യഭാഷയിൽ ഒന്ന് പറഞ്ഞ് താ, എനിക്കും പഠിക്കണം!")],
 "ഷെയർ ചോദിച്ചാൽ\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="ആംഗ്യഭാഷയിൽ വാർത്ത ചെയ്യുന്ന ഫ്രീലാൻസ് ഇന്റർപ്രെറ്റർ ഉണ്ടാക്കിയ ക്യാപ്ഷനിംഗ് ടൂളിൽ ഒരു മീഡിയ ഗ്രൂപ്പ് 20% ഷെയർ ചോദിക്കുന്നു. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി തന്നെ വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും പറ്റില്ല.",
 cap_en="A freelance sign-language news interpreter in Kerala built a captioning tool, and a media group wants 20% of it for an investment. Only a private limited company can take equity investment; a proprietorship, partnership or LLP cannot issue shares.",
 cap_mg="Sign language news interpreter aaya freelancer-nte captioning tool-il oru media group 20% share chodikkunnu. Share koduthu investment edukkan Pvt Ltd company venam. Proprietorship-num LLP-kkum pattilla. Startup funding-nu munpu structure sheriyaakku.")

# salon: Sonia + Vineeth. Vineeth's tattoo studio became a company 40 days ago for a hotel chain's guest offer; nobody appointed the first auditor.
duo("d1405", "freelancer", "B", "salon", "ടാറ്റൂ ആർട്ടിസ്റ്റ്.\nകമ്പനി ആയിട്ട് 40 ദിവസം.\nഓഡിറ്റർ? \"പിന്നെ നോക്കാം\"", [
 ("A","wide","വിനീതേ, ടാറ്റൂ മെഷീൻ മാറ്റി വെച്ച് ഇത്ര സീരിയസ് ആയി എന്താ വായിക്കുന്നത്?"),
 ("V","V","സോണിയചേച്ചീ, ആ ഹോട്ടൽ ചെയിനിന്റെ അഗ്രിമെന്റ്. അവരുടെ ഗസ്റ്റുകൾക്ക് എന്റെ ടാറ്റൂ. അതിനാ കമ്പനി ആക്കിയത്."),
 ("A","A","കമ്പനി ആയിട്ട് എത്ര ദിവസമായി?"),
 ("V","V","നാൽപ്പത് ദിവസം. ബാക്കി ഒക്കെ സമയം പോലെ. ഓഡിറ്റർ ഒക്കെ പിന്നെ നോക്കാം."),
 ("A","wide","പിന്നെ എന്നല്ല. കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം. ആ സമയം കഴിഞ്ഞു."),
 ("V","V","അയ്യോ. ടാറ്റൂ മായ്ക്കാൻ പറ്റില്ല, ഡേറ്റും മായ്ക്കാൻ പറ്റില്ല."),
 ("A","A","അതാ. ഇന്ന് തന്നെ ഓഡിറ്ററെ കാണ്. പിന്നെ നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A. അത് മറക്കല്ലേ."),
 ("V","V","ശരി. ഈ രണ്ട് ഡേറ്റും ഞാൻ എന്റെ കൈയിൽ ടാറ്റൂ ചെയ്യാം!"),
 ("A","wide","വേണ്ട. ഫോണിലെ കലണ്ടർ മതി!")],
 "ഓഡിറ്റർ:\nആദ്യ 30 ദിവസത്തിൽ", CTA_AFTER,
 cap_ml="ഹോട്ടൽ ചെയിനിന്റെ അഗ്രിമെന്റിന് വേണ്ടി കമ്പനി തുടങ്ങിയ ടാറ്റൂ ആർട്ടിസ്റ്റ് 40 ദിവസമായിട്ടും ഓഡിറ്ററെ വെച്ചില്ല. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം. 180 ദിവസത്തിനുള്ളിൽ INC-20A-യും ഫയൽ ചെയ്യണം.",
 cap_en="A freelance tattoo artist in Kochi turned his studio into a company for a hotel-chain deal, and 40 days later still has no auditor. Every new company must appoint its first auditor within 30 days of incorporation and file INC-20A within 180 days.",
 cap_mg="Hotel chain agreement-nu vendi company thudangiya tattoo artist 40 days aayittum auditor-ne vechilla. Company register cheythu 30 days-inullil first auditor venam. 180 days-inullil INC-20A file cheyyanam. Rendum calendar-il idu.")

# chat: Hari, a Carnatic violin accompanist, signs with a Dubai dance-school chain for two years; they need a company address and he rents his flat.
chat("c961", "freelancer", "B", "വയലിൻ വായിക്കുന്നത്\nദുബായ് ഡാൻസ് സ്കൂളുകൾക്ക്.\nഓഫീസ്? വാടക ഫ്ലാറ്റ്", ("ഹരി", "അമ്മ"), [
 (0,"അമ്മേ, ദുബായിലെ ആ ഡാൻസ് സ്കൂൾ ചെയിൻ രണ്ട് വർഷത്തേക്ക് സൈൻ ചെയ്യാമെന്ന്. ഓൺലൈൻ ക്ലാസ്സിന് എന്റെ വയലിൻ."),
 (1,"ഗുരുവായൂരപ്പാ! അപ്പോ ഇനി രാത്രി മുഴുവൻ വയലിൻ കേൾക്കാം."),
 (0,"പക്ഷേ അവർക്ക് കമ്പനി വേണം. കമ്പനിക്ക് ഒരു ഓഫീസ് അഡ്രസ്സും. നമ്മുടെ ഫ്ലാറ്റ് വാടകയ്ക്കല്ലേ."),
 (1,"വാടക വീട് ഓഫീസ് ആക്കാൻ പറ്റില്ലേ മോനേ?"),
 (0,"പറ്റും. ഫ്ലാറ്റിന്റെ ഉടമയുടെ NOC വേണം. കൂടെ പുതിയ ഒരു കറന്റ് ബില്ലും."),
 (1,"ഉടമ ആ കുര്യൻ സാറല്ലേ. അദ്ദേഹത്തിന്റെ മോളുടെ കല്യാണത്തിന് നീയല്ലേ വായിച്ചത്."),
 (0,"അതെ! അപ്പോ NOC ചോദിക്കാൻ ഒരു രാഗം കൂടി വായിക്കാം."),
 (1,"ബില്ല് ഞാൻ എടുത്ത് വെക്കാം. ഈ മാസത്തേത് തന്നെ."),
 (0,"അമ്മയാണ് എന്റെ ആദ്യത്തെ മാനേജർ!")],
 "വാടക വീടും\nകമ്പനി ഓഫീസ് ആക്കാം", CTA_DOCS,
 cap_ml="ദുബായിലെ ഡാൻസ് സ്കൂൾ ചെയിനിന് ഓൺലൈനായി വയലിൻ വായിക്കുന്ന ഫ്രീലാൻസർക്ക് രണ്ട് വർഷത്തെ കോൺട്രാക്ട്, കമ്പനി വേണം. വാടക ഫ്ലാറ്റും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം: ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം.",
 cap_en="A freelance Carnatic violinist in Kerala gets a two-year contract with a Dubai dance-school chain that works only with companies. His rented flat can be the registered office if he has the owner's NOC and a recent utility bill.",
 cap_mg="Dubai dance school chain-nu online violin vaayikkunna freelancer-nu 2 varsha contract, company venam. Rented flat-um registered office aakkam: owner-nte NOC-um puthiya current bill-um mathi. Company register cheyyan documents ithokke.")

lst("l961", "freelancer", "C", "ഫ്രീലാൻസിംഗ് വളർന്നോ?\nകമ്പനി ആകാൻ സമയമായി\nഎന്നതിന്റെ 3 സൂചന", [
 ("ക്ലയന്റ് \"കമ്പനി ഡീറ്റെയിൽസ്\" ചോദിക്കുന്നു", "വലിയ ക്ലയന്റുകൾ പലരും കമ്പനിയുമായി മാത്രം കോൺട്രാക്ട്. ഒറ്റയ്ക്കാണെങ്കിൽ OPC."),
 ("ആരോ നിങ്ങളുടെ ജോലിയിൽ ഷെയർ ചോദിക്കുന്നു", "ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് മാത്രം."),
 ("ഒരു വലിയ ഡേറ്റ് വരുന്നു", "Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7-15 പ്രവൃത്തി ദിവസം. ഡേറ്റിന് മുമ്പ് തുടങ്ങൂ.")],
 "സൂചന കണ്ടാൽ\nവൈകിക്കല്ലേ", CTA_START,
 cap_ml="ഫ്രീലാൻസർ കമ്പനി രജിസ്റ്റർ ചെയ്യേണ്ട സമയം എപ്പോൾ? ക്ലയന്റ് കമ്പനി ഡീറ്റെയിൽസ് ചോദിക്കുമ്പോൾ, ആരെങ്കിലും ഷെയർ ചോദിക്കുമ്പോൾ, വലിയ ഡെഡ്‌ലൈൻ വരുമ്പോൾ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC, നിക്ഷേപം വേണമെങ്കിൽ Pvt Ltd.",
 cap_en="When should a freelancer in Kerala register a company? When clients ask for company details, when someone wants a share of your work, or when a big date is coming. A solo freelancer can start a One Person Company; equity investment needs a Pvt Ltd.",
 cap_mg="Freelancer eppol company register cheyyanam? Client company details chodikkumbol, aarenkilum share chodikkumbol, valiya deadline varumbol. Ottaykku aanenkil OPC, investment venamenkil Pvt Ltd.")

# ---------------- cofounders ----------------
# canteen: Athira + Amal. Two founders of a home elder-care booking app; Amal says the money-only cofounder need not be a director, so one director is enough.
duo("d1406", "cofounders", "A", "canteen", "ഒരാൾ ആപ്പ് നടത്തും.\nമറ്റേയാൾ പൈസ ഇടും.\n\"ഡയറക്ടർ ഒരാൾ മതി\"", [
 ("A","wide","അമലേ, നമ്മുടെ വയോജന കെയർ ആപ്പിന്റെ കമ്പനി ഫോം റെഡി. ഡയറക്ടർ കോളം ആരുടെ പേര്?"),
 ("V","V","ആതിരയുടെ മാത്രം. നീയല്ലേ ആപ്പ് നടത്തുന്നത്. ഞാൻ പൈസ ഇടുന്നു, അത്രയേ ഉള്ളൂ."),
 ("A","A","അപ്പോ ഒരു ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും?"),
 ("V","V","അതെ. ഡയറക്ടർ ഒരാൾ മതിയല്ലോ. എനിക്ക് മീറ്റിംഗ് ഒന്നും ഇഷ്ടമല്ല."),
 ("A","wide","ഇല്ല അമലേ. പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം."),
 ("A","A","നീയോ, അല്ലെങ്കിൽ വിശ്വാസമുള്ള വേറെ ഒരാളോ രണ്ടാമത്തെ ഡയറക്ടർ ആകണം."),
 ("V","V","വേറെ ആളെ കയറ്റിയാൽ പിന്നെ തീരുമാനം മൂന്നുപേരുടെ. അത് വേണ്ട. ഞാൻ തന്നെ ആകാം."),
 ("A","A","അപ്പോ ഇനി മീറ്റിംഗിന് നീയും വരണം. ക്യാന്റീനിൽ ആണെങ്കിലും."),
 ("V","wide","എങ്കിൽ എല്ലാ മീറ്റിംഗും ഈ ക്യാന്റീനിൽ. പരിപ്പുവട ബോർഡിന്റെ ചെലവിൽ!")],
 "Pvt Ltd:\nകുറഞ്ഞത് 2 ഡയറക്ടർ", CTA_START,
 cap_ml="വയോജനങ്ങൾക്ക് ഹോം കെയർ ബുക്ക് ചെയ്യുന്ന ആപ്പിന്റെ കോഫൗണ്ടർമാർ: ഒരാൾ നടത്തും, മറ്റേയാൾ പൈസ മാത്രം ഇടും. പക്ഷേ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം. ഫോം പൂരിപ്പിക്കും മുമ്പ് ഉറപ്പിക്കൂ.",
 cap_en="Two cofounders of an elder-care app in Kerala plan to make only one of them a director because the other just invests. A private limited company needs at least two directors and two shareholders, so decide who the second director is before you file.",
 cap_mg="Elder care app-inte cofounders: oraal nadathum, mattoraal paisa maathram idum. Pakshe Pvt Ltd company-kku minimum 2 directors-um 2 shareholders-um venam. Form fill cheyyunnathinu munpu second director aaru ennu urappikku.")

# rooftop: Arya + Shyam. Their rooftop film-screening club became a company 150 days ago; INC-20A is still not filed.
duo("d1407", "cofounders", "B", "rooftop", "ടെറസിൽ സിനിമ ക്ലബ്.\nകമ്പനി ആയിട്ട് 150 ദിവസം.\nINC-20A? \"അതെന്ത്?\"", [
 ("A","wide","ശ്യാമേ, ഇന്നത്തെ സിനിമയ്ക്ക് നാൽപ്പത് ടിക്കറ്റ്. പ്രൊജക്ടർ റെഡിയാണോ?"),
 ("V","V","റെഡി ആര്യേ. പിന്നെ ഒരു സന്തോഷം. നമ്മുടെ കമ്പനിക്ക് നൂറ്റമ്പത് ദിവസം തികഞ്ഞു."),
 ("A","A","നൂറ്റമ്പതോ! INC-20A ഫയൽ ചെയ്തോ?"),
 ("V","V","അതെന്ത്? പുതിയ സിനിമയുടെ പേരാണോ?"),
 ("A","wide","തമാശ അല്ല. ബിസിനസ് തുടങ്ങി എന്ന് കാണിക്കുന്ന ഫോം. കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("A","A","മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. നമ്മൾ രണ്ടുപേർക്കും ദിവസം ആയിരം രൂപ വെച്ച്, ഒരു ലക്ഷം വരെ."),
 ("V","V","ഇനി മുപ്പത് ദിവസം മാത്രം. ഇത് ഹൊറർ സിനിമയാണല്ലോ!"),
 ("A","A","ഇന്റർവെൽ വരെ സമയം ഉണ്ട്. നാളെ രാവിലെ തന്നെ ഫയൽ ചെയ്യാം."),
 ("V","wide","ശരി. ഇന്നത്തെ ഷോ കഴിഞ്ഞ് സ്ക്രീനിൽ ഒരു റിമൈൻഡർ ഇടാം. INC-20A!")],
 "180 ദിവസം.\nINC-20A മറക്കല്ലേ", CTA_AFTER,
 cap_ml="ടെറസിൽ സിനിമ പ്രദർശിപ്പിക്കുന്ന ക്ലബ് കമ്പനി ആയിട്ട് 150 ദിവസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം. വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപയും ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപയും (പരമാവധി 1 ലക്ഷം) പിഴ.",
 cap_en="Two cofounders run a rooftop film club in Kochi as a company, now 150 days old with INC-20A still pending. The commencement-of-business form is due within 180 days; missing it means a Rs 50,000 penalty on the company and Rs 1,000 a day per officer in default, up to Rs 1 lakh.",
 cap_mg="Terrace-il cinema club nadathunna cofounders-nte company-kku 150 days, INC-20A file cheythilla. Company register cheythu 180 days-inullil file cheyyanam. Vaikiyal company-kku 50,000 roopa penalty, oro director-kkum divasam 1,000 roopa (max 1 lakh).")

# balcony: Ammu + Vivek. Their Malayalam keyboard app was registered last year as a partnership firm; a college senior's angel group wants to invest for shares.
duo("d1408", "cofounders", "A", "balcony", "മലയാളം കീബോർഡ് ആപ്പ്.\nഏഞ്ചൽ ഇൻവെസ്റ്റർ റെഡി.\nകമ്പനി? പാർട്ണർഷിപ്പ്", [
 ("A","wide","വിവേകേ, ആ സീനിയറിന്റെ ഏഞ്ചൽ ഗ്രൂപ്പ് മെയിൽ അയച്ചു! നമ്മുടെ കീബോർഡ് ആപ്പിൽ നിക്ഷേപിക്കാമെന്ന്."),
 ("V","V","ആഹാ! അവസാനം നമ്മുടെ 'ൻ' ബട്ടണിന് ഒരു ആരാധകനെ കിട്ടി."),
 ("A","A","പക്ഷേ ഒരു ചോദ്യം. എത്ര ഷെയർ തരും, കമ്പനി ഏത് ടൈപ്പ് എന്ന്."),
 ("V","V","കഴിഞ്ഞ കൊല്ലം രജിസ്റ്റർ ചെയ്തില്ലേ. പാർട്ണർഷിപ്പ് ഫേം. അന്ന് അതായിരുന്നു എളുപ്പം."),
 ("A","wide","അതാ പ്രശ്നം വിവേകേ. പാർട്ണർഷിപ്പിന് ഷെയർ ഇല്ല. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം."),
 ("V","V","LLP ആക്കിയാലോ? അതും ലിമിറ്റഡ് അല്ലേ?"),
 ("A","A","LLP-ക്കും പറ്റില്ല. ഇൻവെസ്റ്റർക്ക് ഷെയർ വേണമെങ്കിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് തന്നെ."),
 ("V","V","എളുപ്പം നോക്കി എടുത്തത് ഇപ്പോ ഏറ്റവും കഠിനമായി."),
 ("A","wide","കീബോർഡിൽ ബാക്ക്‌സ്പേസ് ഉണ്ടല്ലോ. ഇതിലും ഒന്ന് അമർത്താം!")],
 "പാർട്ണർഷിപ്പിന്\nഷെയർ ഇല്ല", CTA_START,
 cap_ml="മലയാളം കീബോർഡ് ആപ്പ് ഉണ്ടാക്കിയ രണ്ട് കോഫൗണ്ടർമാർക്ക് ഏഞ്ചൽ ഇൻവെസ്റ്റ്മെന്റ് ഓഫർ, പക്ഷേ ബിസിനസ് പാർട്ണർഷിപ്പ് ഫേം ആയാണ് രജിസ്റ്റർ ചെയ്തത്. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ.",
 cap_en="Two cofounders built a Malayalam keyboard app and an angel group wants to invest, but they registered as a partnership firm last year. Only a private limited company can take equity investment; a partnership or LLP cannot issue shares.",
 cap_mg="Malayalam keyboard app-inte cofounders-nu angel investment offer, pakshe partnership firm aayittaanu register cheythathu. Share koduthu investment edukkan Pvt Ltd company-kku maathrame pattu. Startup funding plan undenkil aadyame Pvt Ltd.")

# hostel: Alina + Sanju. Two final-year students run a laundry pickup for four hostels; they think they need a degree and lakhs before forming a company.
duo("d1409", "cofounders", "C", "hostel", "നാല് ഹോസ്റ്റലിലെ\nതുണി അലക്കൽ പിക്കപ്പ്.\n\"കോഴ്സ് കഴിഞ്ഞ് കമ്പനി\"", [
 ("A","wide","സഞ്ജു, ഇന്ന് മാത്രം അറുപത് ബാഗ് തുണി! നമ്മുടെ ലോൺഡ്രി പിക്കപ്പ് ഹിറ്റ് ആയി."),
 ("V","V","അലീനേ, അപ്പുറത്തെ കോളേജും ചോദിച്ചു. പക്ഷേ അവരുടെ ഹോസ്റ്റൽ വാർഡൻ കമ്പനിയുമായേ കരാർ ഒപ്പിടൂ."),
 ("A","A","കമ്പനി ഒക്കെ കോഴ്സ് കഴിഞ്ഞ്. ഡിഗ്രി കിട്ടി, കുറച്ച് ലക്ഷം കൈയിൽ വന്നിട്ട്."),
 ("V","wide","ലക്ഷം വേണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 ("V","V","നമ്മൾ രണ്ടുപേർ. രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ. അത് മതി."),
 ("A","A","ഓഫീസ്? ഈ ഹോസ്റ്റൽ റൂം പറ്റില്ലല്ലോ."),
 ("V","V","എന്റെ വീട് മതി. അച്ഛന്റെ പേരിലാ. അച്ഛന്റെ NOC, പിന്നെ പുതിയ ഒരു കറന്റ് ബില്ല്."),
 ("A","A","അപ്പോ ഡിഗ്രി സർട്ടിഫിക്കറ്റിന് മുമ്പ് കമ്പനി സർട്ടിഫിക്കറ്റ്!"),
 ("V","wide","അതെ. വൈവയ്ക്ക് ചോദിച്ചാൽ പറയാം, ഞങ്ങൾ ഡയറക്ടർമാരാ!")],
 "കമ്പനിക്ക് ലക്ഷങ്ങൾ\nവേണ്ട", CTA_START,
 cap_ml="നാല് ഹോസ്റ്റലുകളിൽ ലോൺഡ്രി പിക്കപ്പ് നടത്തുന്ന രണ്ട് വിദ്യാർത്ഥികൾക്ക് പുതിയ കോളേജിന്റെ കരാർ, കമ്പനി വേണം. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം ക്യാപിറ്റൽ നിർബന്ധമില്ല. രണ്ട് ഡയറക്ടർമാരും വീട്ടിലെ അഡ്രസ്സും (ഉടമയുടെ NOC, പുതിയ ബില്ല്) മതി.",
 cap_en="Two final-year students run a laundry pickup for four hostels and a new college will sign only with a company. A private limited company has no minimum paid-up capital; two directors and a home address with the owner's NOC and a recent utility bill are enough to start.",
 cap_mg="4 hostel-il laundry pickup nadathunna 2 students-nu puthiya college contract, company venam. Pvt Ltd thudangan lakhs venda, minimum capital nirbandham illa. 2 directors-um veedinte address-um (owner NOC, puthiya bill) mathi. Student startup Kerala.")

# foodcourt: Maria + Dennis. Their Kerala meals-in-a-jar brand is named almost exactly like a supermarket chain's own label.
duo("d1410", "cofounders", "B", "foodcourt", "ജാറിൽ കേരള ഊണ്.\nപേര് ഒരു സൂപ്പർമാർക്കറ്റ്\nബ്രാൻഡ് പോലെ", [
 ("V","wide","മരിയാ, നമ്മുടെ ജാർ ലേബൽ പ്രിന്റിന് കൊടുക്കട്ടെ? അയ്യായിരം സ്റ്റിക്കർ."),
 ("A","A","ഒരു മിനിറ്റ് ഡെന്നിസേ. ഈ പേര് എവിടെയോ കണ്ടിട്ടുണ്ട്."),
 ("V","V","എവിടെ? ഞാൻ രാത്രി മുഴുവൻ ഇരുന്ന് ഉണ്ടാക്കിയ പേരാ."),
 ("A","A","ആ വലിയ സൂപ്പർമാർക്കറ്റിന്റെ സ്വന്തം ബ്രാൻഡ്. അവരുടെ അച്ചാറിന്റെ പേരും ഏകദേശം ഇത് തന്നെ."),
 ("A","wide","ട്രേഡ്മാർക്ക് ഉള്ള ഒരു പേരുമായി സാമ്യം ഉണ്ടെങ്കിൽ കമ്പനി പേര് റിജക്ട് ആകാം."),
 ("V","V","ഒരു അക്ഷരം മാറ്റിയാലോ?"),
 ("A","A","കേൾക്കുമ്പോൾ ഒരുപോലെ ആണെങ്കിൽ ഒരു അക്ഷരം പോരാ. രണ്ടുപേരും ഇരുന്ന് പുതിയ മൂന്ന് പേര്."),
 ("V","V","സ്റ്റിക്കർ അടിച്ചിരുന്നെങ്കിൽ അയ്യായിരം സ്റ്റിക്കർ ചവറ്റുകൊട്ടയിൽ!"),
 ("A","wide","ആദ്യം പേര് ഉറപ്പിക്ക്. പിന്നെ സ്റ്റിക്കർ. പിന്നെ ഊണ്!")],
 "ലേബൽ അടിക്കും മുമ്പ്\nപേര് ചെക്ക് ചെയ്യൂ", CTA_NAME,
 cap_ml="ജാറിൽ കേരള ഊണ് വിൽക്കുന്ന കോഫൗണ്ടർമാരുടെ ബ്രാൻഡ് പേര് ഒരു സൂപ്പർമാർക്കറ്റിന്റെ സ്വന്തം ബ്രാൻഡ് പോലെ. ട്രേഡ്മാർക്കുമായി സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകാം. ലേബലും സ്റ്റിക്കറും അടിക്കും മുമ്പ് കമ്പനി പേര് ഉറപ്പിക്കൂ.",
 cap_en="Two cofounders selling Kerala meals in jars almost printed 5,000 labels with a name that sounds like a supermarket's own brand. A company name that clashes with a trademark can be rejected, so check and confirm the company name before printing anything.",
 cap_mg="Jar-il Kerala meals vilkkunna cofounders-nte brand name oru supermarket brand pole. Trademark-umaayi saamyam ulla company name reject aakaam. Label print cheyyunnathinu munpu company name check cheythu urappikku.")

# chat: Vipin + Arjun, ex-colleagues, plan a drone paddy-spraying service; the Kuttanad season starts in three weeks and they have not started registering.
chat("c962", "cofounders", "A", "ഡ്രോൺ കൊണ്ട്\nപാടത്ത് മരുന്നടി.\nസീസൺ 3 ആഴ്ചയിൽ", ("വിപിൻ", "അർജുൻ"), [
 (0,"അളിയാ, കുട്ടനാട്ടിലെ മൂന്ന് പാടശേഖര സമിതി വിളിച്ചു. ഈ സീസണിൽ നമ്മുടെ ഡ്രോൺ വേണമെന്ന്."),
 (1,"സൂപ്പർ! എപ്പോ തുടങ്ങണം?"),
 (0,"മൂന്നാഴ്ച കഴിഞ്ഞ്. പക്ഷേ ബിൽ കമ്പനിയുടേത് ആകണം. നമ്മൾ ഇതുവരെ കമ്പനി ആക്കിയില്ലല്ലോ."),
 (1,"ഒരു ദിവസം കൊണ്ട് ആക്കാം. പേരും ഒപ്പും, തീർന്നു."),
 (0,"ഒരു ദിവസം അല്ല. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം."),
 (1,"അപ്പോ മൂന്നാഴ്ച കഷ്ടിച്ച്. പേര് റിജക്ട് ആയാൽ പിന്നെയും വൈകും."),
 (0,"അതുകൊണ്ട് ഇന്ന് രാത്രി തന്നെ മൂന്ന് പേര്, രണ്ടുപേരുടെയും ഡോക്യുമെന്റ്സ്."),
 (1,"ശരി. ഡ്രോൺ പറക്കും മുമ്പ് കമ്പനി പറക്കണം!")],
 "സീസൺ കാത്തിരിക്കില്ല.\n7-15 പ്രവൃത്തി ദിവസം", CTA_START,
 cap_ml="കുട്ടനാട്ടിൽ ഡ്രോൺ ഉപയോഗിച്ച് പാടത്ത് മരുന്ന് തളിക്കുന്ന സ്റ്റാർട്ടപ്പിന് സീസൺ മൂന്നാഴ്ചയിൽ, ബിൽ കമ്പനിയുടേത് വേണം. Pvt Ltd കമ്പനി രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം. പേര് റിജക്ട് ആയാൽ വൈകും, ബാക്കപ്പ് പേരുകൾ കരുതൂ.",
 cap_en="Two ex-colleagues run a drone paddy-spraying service in Kuttanad and the season starts in three weeks, but farmers' committees need company bills. Private limited company registration usually takes 7 to 15 working days, longer if the name is rejected, so start today.",
 cap_mg="Kuttanad-il drone vechu paadathu marunnu thalikkunna startup-nu season 3 aazhchayil, bill company-yude venam. Pvt Ltd register cheyyan saadharana 7-15 working days. Name reject aayaal vaikum, backup names ready aakku.")

lst("l962", "cofounders", "C", "കൂട്ടുകാരനുമായി\nകമ്പനി തുടങ്ങും മുമ്പ്\nമേശപ്പുറത്ത് 3 ചോദ്യം", [
 ("ആരൊക്കെ ഡയറക്ടർ?", "Pvt Ltd-ന് കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ."),
 ("നാളെ ഇൻവെസ്റ്റർ വന്നാലോ?", "ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ Pvt Ltd മാത്രം. LLP-ക്കും പാർട്ണർഷിപ്പിനും പറ്റില്ല."),
 ("ആര് ഡേറ്റുകൾ നോക്കും?", "30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A. ഒരാളെ ചുമതല ഏൽപ്പിക്കൂ.")],
 "ഇപ്പോ ചോദിച്ചാൽ\nപിന്നെ വഴക്കില്ല", CTA_START,
 cap_ml="കൂട്ടുകാരനുമായി സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്നവർ ആദ്യം സംസാരിക്കേണ്ട 3 കാര്യം: ആരൊക്കെ ഡയറക്ടർ (Pvt Ltd-ന് കുറഞ്ഞത് 2), ഇൻവെസ്റ്റർ വന്നാൽ ഷെയർ കൊടുക്കാൻ Pvt Ltd തന്നെ വേണം, ഓഡിറ്ററും INC-20A ഡേറ്റുകളും ആര് നോക്കും.",
 cap_en="Starting a company with a friend in Kerala? Settle three questions first: who the two directors are, whether you will want investors (only a Pvt Ltd can issue shares to them), and who tracks the 30-day auditor and 180-day INC-20A dates.",
 cap_mg="Friend-umaayi company thudangunnathinu munpu 3 chodyam: aarokke director (Pvt Ltd-nu minimum 2), investor vannaal share kodukkan Pvt Ltd thanne venam, auditor-um INC-20A dates-um aaru nokkum.")

# ---------------- salaried ----------------
# bank: Shruthi + Manoj. Manoj, a bank cashier, makes leather wallets at night; a hotel gift shop wants a steady supply from a company; the house is in his mother's name.
duo("d1411", "salaried", "A", "bank", "ബാങ്കിൽ ക്യാഷ്യർ.\nരാത്രി ലെതർ വാലറ്റ്.\nഹോട്ടൽ ഗിഫ്റ്റ് ഷോപ്പ് റെഡി", [
 ("A","wide","മനോജേ, നോട്ട് എണ്ണുന്നതിനിടയിൽ എന്താ ആ ലെതർ വാലറ്റിൽ നോക്കുന്നത്?"),
 ("V","V","ശ്രുതീ, ഇത് ഞാൻ രാത്രി ഉണ്ടാക്കുന്നതാ. ആ സ്റ്റാർ ഹോട്ടലിലെ ഗിഫ്റ്റ് ഷോപ്പ് എല്ലാ മാസവും വേണമെന്ന്."),
 ("A","A","അത് കലക്കി! അവർക്ക് ബിൽ വേണ്ടേ?"),
 ("V","V","കമ്പനിയുടെ ബിൽ വേണം. പക്ഷേ ഓഫീസ് ഇല്ല. വാലറ്റ് ഉണ്ടാക്കുന്നത് വീട്ടിലെ വരാന്തയിലാ."),
 ("A","wide","വീടും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. വീട് ആരുടെ പേരിലാ?"),
 ("V","V","അമ്മയുടെ പേരിൽ."),
 ("A","A","എങ്കിൽ അമ്മയുടെ NOC. കൂടെ പുതിയ ഒരു കറന്റ് ബില്ലോ വാട്ടർ ബില്ലോ. ഓഫീസ് റെഡി."),
 ("V","V","അമ്മയ്ക്ക് ഒരു സ്പെഷ്യൽ വാലറ്റ് ഉണ്ടാക്കി കൊടുക്കാം. NOC-ക്ക് ഒരു സ്നേഹസമ്മാനം!"),
 ("A","wide","അതിനകത്ത് ഈ മാസത്തെ കറന്റ് ബില്ലും വെച്ചോ!")],
 "വീട്ടിലെ വരാന്തയും\nഓഫീസ് ആകും", CTA_DOCS,
 cap_ml="ബാങ്കിൽ ക്യാഷ്യറായ ആൾ രാത്രി ഉണ്ടാക്കുന്ന ലെതർ വാലറ്റിന് ഹോട്ടൽ ഗിഫ്റ്റ് ഷോപ്പിന്റെ മാസ ഓർഡർ, കമ്പനി ബിൽ വേണം. വീടിന്റെ അഡ്രസ്സ് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം: വീട്ടുടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും മതി.",
 cap_en="A bank cashier in Kerala makes leather wallets at night, and a hotel gift shop wants a monthly supply billed by a company. His home can be the registered office with the owner's NOC (his mother's) and a recent utility bill.",
 cap_mg="Bank cashier raathri undaakkunna leather wallet-nu hotel gift shop-inte monthly order, company bill venam. Veedinte address registered office aakkam: owner-nte NOC-um puthiya utility bill-um mathi. Side business company register cheyyan documents ithaanu.")

# photocopy: Aswathy + Unni. Aswathy, a hospital radiographer, teaches CPR to office teams on Saturdays; her company has had no revenue for eight months.
duo("d1412", "salaried", "C", "photocopy", "ശനിയാഴ്ച CPR ക്ലാസ്.\nകമ്പനി ആയിട്ട് 8 മാസം.\nവരുമാനം ഇതുവരെ ഇല്ല", [
 ("V","wide","അശ്വതിചേച്ചീ, ഈ CPR പോസ്റ്റർ നൂറ് കോപ്പി ആണോ?"),
 ("A","A","അതെ ഉണ്ണീ. ഓഫീസുകളിൽ ശനിയാഴ്ച CPR ക്ലാസ്. ഇതുവരെ ഒരു ഓഫീസും പൈസ തന്നിട്ടില്ല, അതാ പോസ്റ്റർ."),
 ("V","V","കമ്പനി ആക്കിയിട്ട് കുറേ ആയില്ലേ?"),
 ("A","A","എട്ട് മാസം. വരുമാനം ഒന്നുമില്ലാത്തതുകൊണ്ട് കണക്ക് ഒന്നും കൊടുക്കണ്ടല്ലോ. ആശുപത്രിയിലെ ജോലി തന്നെ ധാരാളം."),
 ("V","wide","അത് തെറ്റാ ചേച്ചീ. വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("V","V","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. അത് ദിവസവും കൂടും."),
 ("A","A","അപ്പോ ഹൃദയം നിലയ്ക്കാതിരിക്കാൻ ഞാൻ പഠിപ്പിക്കുന്നു, കമ്പനി നിലയ്ക്കാതിരിക്കാൻ ആര്?"),
 ("V","V","ഡ്യൂ ഡേറ്റ് ഓർക്കുന്ന ഒരു ഓഡിറ്റർ. പിന്നെ ചേച്ചിയുടെ കലണ്ടർ."),
 ("A","wide","ശരി. കമ്പനിക്കും ഒരു CPR. ഇന്ന് തന്നെ!")],
 "വരുമാനം ഇല്ലെങ്കിലും\nഫയലിംഗ് ഉണ്ട്", CTA_AFTER,
 cap_ml="ആശുപത്രിയിൽ ജോലി ചെയ്യുന്ന റേഡിയോഗ്രാഫറുടെ സൈഡ് കമ്പനി ഓഫീസുകളിൽ CPR ക്ലാസ് എടുക്കുന്നു, 8 മാസമായി വരുമാനമില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് നിർബന്ധം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A hospital radiographer in Kerala runs a side company teaching CPR to office teams on Saturdays, with no revenue in eight months. A company with zero revenue still has to do its annual filings with the ROC, and late filing costs Rs 100 per day per form.",
 cap_mg="Hospital-il job cheyyunna radiographer-nte side company office-ukalil CPR class edukkunnu, 8 maasamaayi revenue illa. Zero revenue aanenkilum annual filing (ROC) nirbandham. Vaikiyal oro form-inum divasam 100 roopa penalty.")

# tailor: Usha + Mohanan. Mohanan, a textile-mill supervisor, and Usha plan a school-uniform company; he thinks registering means a month of leave.
duo("d1413", "salaried", "B", "tailor", "യൂണിഫോം കമ്പനി തുടങ്ങാൻ\n\"ഒരു മാസം ലീവ് വേണം\"", [
 ("A","wide","മോഹനേട്ടാ, മൂന്ന് സ്കൂളുകൾ യൂണിഫോം ഓർഡർ തരാമെന്ന്. പക്ഷേ ബിൽ കമ്പനിയുടേത് ആകണം."),
 ("V","V","അറിയാം ഉഷേ. പക്ഷേ കമ്പനി തുടങ്ങാൻ ഒരു മാസം ലീവ് എടുക്കണം. മില്ലിൽ ലീവ് ചോദിച്ചാൽ സൂപ്പർവൈസറെ തന്നെ മാറ്റും."),
 ("A","A","ഒരു മാസമോ? ആര് പറഞ്ഞു?"),
 ("V","V","ഓഫീസുകൾ കയറി ഇറങ്ങണ്ടേ? ഫോം, ഒപ്പ്, ക്യൂ…"),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. അതിനിടയിൽ ദിവസവും ഓടേണ്ട കാര്യമില്ല."),
 ("A","A","നമ്മുടെ രണ്ടുപേരുടെയും ഡോക്യുമെന്റ്സ്, ഈ കടയുടെ അഡ്രസ്സ് പ്രൂഫ്. അത് ശരിയാക്കി വെച്ചാൽ മതി."),
 ("V","V","അപ്പോ ലീവ് വേണ്ട? മില്ലിലെ ഡ്യൂട്ടിയും കമ്പനിയും ഒരുമിച്ച്?"),
 ("A","A","അതെ. ഞാൻ തയ്ക്കും, ചേട്ടൻ ഒപ്പിടും. സ്കൂൾ തുറക്കും മുമ്പ് യൂണിഫോം റെഡി."),
 ("V","wide","എങ്കിൽ ഈ ലീവ് ലെറ്റർ കീറി കളയാം!")],
 "ലീവ് വേണ്ട.\nഡോക്യുമെന്റ്സ് മതി", CTA_DOCS,
 cap_ml="ടെക്സ്റ്റൈൽ മില്ലിലെ സൂപ്പർവൈസറും ടെയ്ലറും ചേർന്ന് സ്കൂൾ യൂണിഫോം കമ്പനി തുടങ്ങാൻ ഒരു മാസം ലീവ് വേണമെന്ന് കരുതി. Pvt Ltd കമ്പനി രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം. ഡോക്യുമെന്റ്സ് റെഡി ആക്കിയാൽ ജോലിക്കൊപ്പം നടക്കും.",
 cap_en="A textile-mill supervisor and his wife, a tailor, want to start a school-uniform company in Kerala and think it needs a month of leave. Private limited company registration usually takes 7 to 15 working days; with the documents ready, it runs alongside your job.",
 cap_mg="Mill supervisor-um tailor aaya bharyayum school uniform company thudangan 1 maasam leave venam ennu vicharichu. Pvt Ltd company register cheyyan saadharana 7-15 working days. Documents ready aakkiyaal job-inte koode nadakkum.")

# handloom: Leela + Kumar. Kumar works at Technopark and sells his aunt Leela's handloom sarees online; his cousin in the US wants shares.
duo("d1414", "salaried", "A", "handloom", "ടെക്നോപാർക്കിൽ ജോലി.\nവൈകുന്നേരം അമ്മായിയുടെ\nകൈത്തറി ഓൺലൈനിൽ", [
 ("A","wide","കുമാറേ, ലാപ്ടോപ്പും കൊണ്ട് തറിയുടെ അടുത്ത് ഇരിക്കല്ലേ. നൂല് കുരുങ്ങും."),
 ("V","V","ലീലമ്മായീ, ഒരു സന്തോഷം. അമേരിക്കയിലുള്ള വിനുച്ചേട്ടന് നമ്മുടെ കൈത്തറി ബിസിനസിൽ ഷെയർ വേണമെന്ന്."),
 ("A","A","അവൻ അവിടെ ഇരുന്ന് ഇവിടത്തെ ഷെയറോ? അതൊക്കെ നടക്കുമോ?"),
 ("V","wide","നടക്കും. NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം."),
 ("V","V","പക്ഷേ ഇപ്പോ ഇത് അമ്മായിയുടെ പേരിലുള്ള കടയല്ലേ. ഷെയർ കൊടുക്കാൻ ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ് ആക്കണം."),
 ("A","A","ഡയറക്ടർ ആരൊക്കെ?"),
 ("V","V","അമ്മായിയും ഞാനും. ഒരാൾ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ വേണം. നമ്മൾ രണ്ടുപേരും ഇവിടെ തന്നെ."),
 ("A","A","എഴുപത് വയസ്സിൽ ഡയറക്ടർ! തറി പോലും ഞെട്ടും."),
 ("V","wide","തറിയുടെ ഡയറക്ടർ പണ്ടേ അമ്മായി ആണല്ലോ!")],
 "വിദേശത്തുള്ളവർക്കും\nഷെയർ എടുക്കാം", CTA_START,
 cap_ml="ടെക്നോപാർക്കിൽ ജോലി ചെയ്യുന്ന ആൾ വൈകുന്നേരം അമ്മായിയുടെ കൈത്തറി ഓൺലൈനിൽ വിൽക്കുന്നു, അമേരിക്കയിലുള്ള കസിന് ഷെയർ വേണം. NRI-ക്ക് പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡർ ആകാം. ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.",
 cap_en="A Technopark employee sells his aunt's handloom sarees online after work, and a cousin in the US wants a share. An NRI can be a shareholder or director of an Indian private limited company, as long as at least one director is resident in India.",
 cap_mg="Technopark-il job cheyyunna aal vaikunneram ammaayiyude handloom online-il vilkkunnu, America-yilulla cousin-nu share venam. NRI-kku Pvt Ltd-il shareholder aakaam. Oru director India-yil thamasikkunna aal aakanam.")

# chat: Reshma, cabin crew based in Kochi, has a travel-pillow brand; she flies 20 days a month and asks her friend Anjana what dates she must not miss.
chat("c963", "salaried", "B", "മാസത്തിൽ 20 ദിവസം\nആകാശത്ത്.\nകമ്പനി ഡേറ്റുകൾ ആര് നോക്കും?", ("രേഷ്മ", "അഞ്ജന"), [
 (0,"അഞ്ജനേ, ട്രാവൽ പില്ലോ ബ്രാൻഡ് കമ്പനി ആയി! ഇന്നലെ സർട്ടിഫിക്കറ്റ് വന്നു."),
 (1,"കൺഗ്രാറ്റ്സ്! ഇനി ഫ്ലൈറ്റിലും നിന്റെ തലയണ."),
 (0,"പക്ഷേ ഞാൻ മാസത്തിൽ ഇരുപത് ദിവസം പറക്കുവാ. ഏതൊക്കെ ഡേറ്റാ മിസ്സ് ആകാൻ പാടില്ലാത്തത്?"),
 (1,"ആദ്യം മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്റർ."),
 (1,"പിന്നെ നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A. ബിസിനസ് തുടങ്ങി എന്ന് അറിയിക്കുന്ന ഫോം."),
 (0,"അത് മിസ്സ് ആയാൽ?"),
 (1,"കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർമാർക്ക് ദിവസം ആയിരം രൂപ വെച്ച് വേറെയും."),
 (0,"ഇനി ലാൻഡ് ചെയ്യുമ്പോൾ ആദ്യം നോക്കുന്നത് കലണ്ടർ. പിന്നെ ലഗേജ്!")],
 "30 ദിവസം, 180 ദിവസം.\nരണ്ട് ഡേറ്റ് മാത്രം", CTA_AFTER,
 cap_ml="കൊച്ചിയിലെ ക്യാബിൻ ക്രൂ ജീവനക്കാരിയുടെ ട്രാവൽ പില്ലോ ബ്രാൻഡ് കമ്പനി ആയി, പക്ഷേ മാസത്തിൽ 20 ദിവസം യാത്ര. 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ, 180 ദിവസത്തിനുള്ളിൽ INC-20A. ഇത് മിസ്സ് ആയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ.",
 cap_en="A Kochi-based cabin crew member just registered her travel-pillow brand as a company but flies 20 days a month. The two dates to protect: first auditor within 30 days and INC-20A within 180 days; missing INC-20A means a Rs 50,000 penalty on the company.",
 cap_mg="Kochi-yile cabin crew-nte travel pillow brand company aayi, pakshe maasathil 20 divasam flight-il. 30 days-inullil first auditor, 180 days-inullil INC-20A. Miss aayaal company-kku 50,000 roopa penalty.")

# office: Neha + Rahul. Rahul, an office admin, picked a side-company name one letter away from an existing company's.
duo("d1415", "salaried", "C", "office", "ഓഫീസ് അഡ്മിൻ.\nസൈഡ് കമ്പനിക്ക് പേര്:\nഒരു അക്ഷരം മാത്രം വ്യത്യാസം", [
 ("A","wide","രാഹുലേ, പ്രിന്റർ ടോണർ ഓർഡർ ചെയ്യാൻ പറഞ്ഞിട്ട് എന്താ ഗൂഗിളിൽ നോക്കുന്നത്?"),
 ("V","V","നേഹേ, എന്റെ സൈഡ് കമ്പനിയുടെ പേര്. ഓഫീസുകൾക്ക് ഇവന്റ് ഡെക്കറേഷൻ. പേര് ഉറപ്പിച്ചു."),
 ("A","A","നോക്കട്ടെ… ഇതേ പേര് ഇവിടെ ഒരു കമ്പനിക്ക് ഉണ്ടല്ലോ."),
 ("V","V","ഉണ്ട്. പക്ഷേ ഞാൻ ഒരു അക്ഷരം മാറ്റി. അവരുടേതിൽ 'ഐ', എന്റേതിൽ 'വൈ'."),
 ("A","wide","വായിക്കുമ്പോൾ ഒരേ പോലെ ആണെങ്കിൽ അത് പോരാ. നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("V","V","റിജക്ട് ആയാൽ എന്താ?"),
 ("A","A","വീണ്ടും പേര് കൊടുക്കണം. സമയം പോകും. ആദ്യമേ ഒട്ടും സാമ്യം ഇല്ലാത്ത രണ്ടുമൂന്ന് പേര് കരുതിക്കോ."),
 ("V","V","ഓഫീസിലെ ടോണർ പോലും ഞാൻ ബാക്കപ്പ് വെക്കും. പേരിന് ബാക്കപ്പ് വെച്ചില്ല!"),
 ("A","wide","ഇനി രണ്ടും വെക്ക്. ടോണർ ആദ്യം!")],
 "ഒരു അക്ഷരം മാറ്റിയാൽ\nപുതിയ പേര് ആകില്ല", CTA_NAME,
 cap_ml="ഓഫീസ് അഡ്മിൻ ആയ ആളുടെ സൈഡ് കമ്പനിക്ക് നിലവിലുള്ള ഒരു കമ്പനിയുടെ പേരിൽ നിന്ന് ഒരു അക്ഷരം മാത്രം മാറ്റിയ പേര്. നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യമുള്ള പേര് റിജക്ട് ആകാം. ഒട്ടും സാമ്യമില്ലാത്ത ബാക്കപ്പ് പേരുകൾ കരുതൂ.",
 cap_en="An office admin in Kochi picked a side-company name that differs from an existing company's by one letter. A company name similar to an existing company or LLP can be rejected, so keep two or three clearly different backup names ready.",
 cap_mg="Office admin-nte side company-kku oru existing company-yude perilninnu oru aksharam maathram maattiya peru. Existing company-yudeyo LLP-yudeyo perinodu saamyam undenkil company name reject aakum. Backup names ready aakku.")
