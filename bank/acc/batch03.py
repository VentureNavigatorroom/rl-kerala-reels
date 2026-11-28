# acc batch 03 (28 Nov night): 3D duo reels. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns. Facts only from topics.FACTS_ACC. No fixed due dates, no tax amounts, no fees of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

# crm: a returnee shut his spice shop and went back to the Gulf; the GST registration is still alive, so nil returns keep falling due
duo("acd007", "nil_filer", "B", "gulfroom", "കട പൂട്ടി ദുബായിലേക്ക്.\nGST നമ്പർ\nനാട്ടിൽ തന്നെ ബാക്കി", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ സ്പൈസസ് കട പൂട്ടിയിട്ട് എട്ട് മാസം. GST നമ്പർ പക്ഷേ ഇപ്പോഴും ഉണ്ട്. അത് അവിടെ കിടന്നോട്ടെ, അല്ലേ?"),
 ("V","V","നസീറേ, കട പൂട്ടിയാലും രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം റിട്ടേൺ വേണം. വിൽപ്പന ഇല്ലാത്ത മാസത്തിന് നിൽ റിട്ടേൺ."),
 ("A","A","എട്ട് മാസത്തെ നിൽ റിട്ടേണോ? അടുത്ത ലീവിന് നാട്ടിൽ പോയിട്ട് നോക്കാം."),
 ("V","V","ലീവ് വരെ കാക്കണ്ട. ഏറ്റവും പഴയ മാസം ആദ്യം. രജിസ്ട്രേഷൻ ഇനി എന്ത് ചെയ്യണം എന്ന് ടീമിനോട് ചോദിക്ക്."),
 ("A","wide","കട പൂട്ടി, പക്ഷേ റിട്ടേണിന്റെ വാതിൽ തുറന്നുകിടക്കുന്നു.")],
 "കട പൂട്ടിയാലും\nനമ്പർ ഉണ്ടെങ്കിൽ റിട്ടേൺ", CTA_ITR, theme="crm",
 cap_ml="നാട്ടിലെ കട പൂട്ടി ഗൾഫിലേക്ക് തിരിച്ചുപോയോ? GST രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ വേണം. ഏറ്റവും പഴയ മാസം ആദ്യം തീർക്കൂ, രജിസ്ട്രേഷന്റെ കാര്യം ടീമിനോട് ചോദിക്കൂ. നിങ്ങളുടെ GST നമ്പർ ഇപ്പോഴും ആക്ടീവ് ആണോ?",
 cap_en="Shut your Kerala shop and went back to the Gulf? As long as the GST registration exists, nil returns are due for months with no sales. Clear the oldest month first and ask the team what to do with the registration. Is your GST number still active?",
 cap_mg="Naattile kada pootti Gulf-ilekku thirichu poyo? GST registration ullidatholam vilpana illaatha maasavum nil return venam. Ettavum pazhaya maasam aadyam theerkku, registration-nte kaaryam team-inodu chodikku. Ningalude GST number ippozhum active aano?")

# crm: a son takes over his father's hardware shop and finds unfiled returns; each return locks 3 years after its own due date
duo("acd008", "small_trader_acc", "B", "shop", "അച്ഛന്റെ കട ഏറ്റെടുത്തു.\nഅലമാരയിൽ കിട്ടിയത്:\nഫയൽ ചെയ്യാത്ത റിട്ടേൺ", [
 ("A","wide","സുരേഷേട്ടാ, അച്ഛന്റെ ഹാർഡ്‌വെയർ കട ഏറ്റെടുത്തപ്പോൾ കണ്ടു: 2025-ലെ കുറേ മാസത്തെ GST റിട്ടേൺ ഫയൽ ചെയ്തിട്ടില്ല."),
 ("V","V","ശ്രീനാഥേ, ഇനി 'പിന്നെ നോക്കാം' വേണ്ട. 2025 ജൂലൈ മുതലുള്ള റിട്ടേൺ, ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയാൽ പോർട്ടൽ എടുക്കില്ല."),
 ("A","A","മൂന്ന് വർഷം ഉണ്ടല്ലോ. പതുക്കെ മതി."),
 ("V","V","ഓരോ റിട്ടേണിനും സ്വന്തം കണക്കാണ്. ആദ്യത്തേത് ആദ്യം പൂട്ടും. ഏറ്റവും പഴയതിൽ നിന്ന് ഈ ആഴ്ച തന്നെ തുടങ്ങ്."),
 ("A","wide","അച്ഛന്റെ കട മാത്രമല്ല, അച്ഛന്റെ ബാക്കിയും എനിക്ക് കിട്ടി.")],
 "പഴയ ബാക്കി\nപൂട്ടും മുമ്പ് തീർക്കൂ", CTA_ACCOUNTS, names=("ശ്രീനാഥ്", "സുരേഷ്"), theme="crm",
 cap_ml="കുടുംബത്തിന്റെ കട ഏറ്റെടുത്തപ്പോൾ ഫയൽ ചെയ്യാത്ത GST റിട്ടേണുകൾ കണ്ടോ? 2025 ജൂലൈ മുതലുള്ള ഓരോ റിട്ടേണും ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയാൽ പോർട്ടൽ എടുക്കില്ല. ഏറ്റവും പഴയതിൽ നിന്ന് ഇപ്പോൾ തന്നെ തുടങ്ങൂ. നിങ്ങളുടെ കടയിൽ പഴയ ബാക്കി ഉണ്ടോ?",
 cap_en="Took over the family shop and found unfiled GST returns? From the July 2025 tax period, the portal blocks each return once 3 years have passed from its due date, so the oldest locks first. Start from the oldest one now. Any old returns pending at your shop?",
 cap_mg="Kudumbathinte kada ettedutthappol file cheyyaatha GST returns kando? 2025 July muthalulla oro returnum due date kazhinju 3 varsham aayaal portal edukkilla. Ettavum pazhayathil ninnu ippol thanne thudangu. Ningalude kadayil pazhaya baakki undo?")

# faq: a wedding caterer forgot one big invoice in GSTR-1 and wants to add it straight into 3B
duo("acd009", "small_trader_acc", "B", "weddinghall", "ഒരു കല്യാണ ബിൽ\nGSTR-1-ൽ വിട്ടുപോയി.\n\"3B-ൽ കൂട്ടിയാൽ പോരേ?\"", [
 ("A","wide","ശരത്തേ, കഴിഞ്ഞ മാസത്തെ ഏറ്റവും വലിയ കല്യാണ ഓർഡറിന്റെ ബിൽ GSTR-1-ൽ കയറ്റാൻ മറന്നു."),
 ("V","V","കാവ്യേ, അതിനെന്താ? 3B ഫയൽ ചെയ്യുമ്പോൾ ആ തുക കൂടി ചേർത്ത് അടിച്ചാൽ മതി."),
 ("A","A","ഇപ്പോൾ അങ്ങനെ പറ്റില്ല. 3B-ലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരും. വിട്ടുപോയ ബിൽ GSTR-1A-യിൽ ചേർക്കണം, 3B-ക്ക് മുമ്പ്."),
 ("V","V","അപ്പോ ബിൽ ബുക്ക് മുഴുവൻ ഒന്ന് ഒത്തുനോക്കിയിട്ട് ആദ്യം 1A, പിന്നെ 3B."),
 ("A","wide","പായസം വിട്ടുപോയാൽ അടുത്ത പന്തിയിലല്ല, ഇപ്പോൾ തന്നെ വിളമ്പണം.")],
 "വിട്ടുപോയ ബിൽ\n3B-ക്ക് മുമ്പ് 1A-യിൽ", CTA_ACCOUNTS, theme="faq",
 cap_ml="GSTR-1-ൽ ഒരു ബിൽ ചേർക്കാൻ മറന്നോ? 3B-ലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരുന്നതുകൊണ്ട് 3B-ൽ നേരിട്ട് കൂട്ടാൻ പറ്റില്ല. 3B-ക്ക് മുമ്പ് GSTR-1A-യിൽ ചേർക്കൂ. നിങ്ങൾ 3B-ക്ക് മുമ്പ് GSTR-1 ഒത്തുനോക്കാറുണ്ടോ?",
 cap_en="Forgot an invoice in GSTR-1? GSTR-3B sales figures now come locked from GSTR-1, so you can't simply add it in 3B. Add it in GSTR-1A before filing 3B. Do you check GSTR-1 before 3B?",
 cap_mg="GSTR-1-il oru bill cherkkaan maranno? 3B-yile vilpana kanakku GSTR-1-il ninnu lock aayi varunnathukondu 3B-il nerittu koottaan pattilla. 3B-kku munpu GSTR-1A-yil cherkku. Ningal 3B-kku munpu GSTR-1 othunokkaarundo?")

# faq: a physiotherapist wants presumptive taxation because her dentist friend uses it
duo("acd010", "freelancer_itr", "B", "hospital", "\"ഡോക്ടർ ഫ്രണ്ട്\nചെയ്യുന്നത് തന്നെ\nഞാനും ചെയ്യും\"", [
 ("A","wide","ജോസഫേ, എന്റെ ഫിസിയോ ക്ലിനിക്കിനും ഡെന്റിസ്റ്റ് ഫ്രണ്ട് ചെയ്യുന്ന പോലെ പ്രിസംപ്റ്റീവ് ടാക്സേഷൻ എടുക്കാം എന്ന് കരുതി."),
 ("V","V","ലക്ഷ്മീ, പ്രൊഫഷണലുകൾക്ക് ആ രീതി ഉണ്ട്. പക്ഷേ നിബന്ധനകൾ ഉണ്ട്. ഫ്രണ്ടിന് ചേർന്നത് നിനക്കും ചേരണമെന്നില്ല."),
 ("A","A","അവളുടെ വരുമാനവും എന്റേതും വേറെ ആണല്ലോ. അപ്പോ ഞാൻ എന്ത് നോക്കണം?"),
 ("V","V","ഈ വർഷത്തെ വരവും ചെലവും ബാങ്ക് കണക്കും എടുത്ത് ടീമിനോട് ചോദിക്ക്, നിനക്ക് ബാധകമാണോ എന്ന്. എന്നിട്ട് തീരുമാനിക്ക്."),
 ("A","wide","ഫ്രണ്ടിന്റെ കുറിപ്പടി എന്റെ അസുഖത്തിന് ചേരില്ല, അല്ലേ?")],
 "ഫ്രണ്ടിന്റെ രീതിയല്ല,\nനിങ്ങളുടെ നിബന്ധന", CTA_ITR, theme="faq",
 cap_ml="ഫ്രണ്ട് പ്രിസംപ്റ്റീവ് ടാക്സേഷൻ എടുക്കുന്നു, അതുകൊണ്ട് ഞാനും? പ്രൊഫഷണലുകൾക്ക് ആ രീതി ഉണ്ട്, പക്ഷേ നിബന്ധനകൾ ഉണ്ട്. വരവും ചെലവും ബാങ്ക് കണക്കും വെച്ച് നിങ്ങൾക്ക് ബാധകമാണോ എന്ന് ആദ്യം ഉറപ്പാക്കൂ. നിങ്ങൾ ഏത് പ്രൊഫഷനിലാണ്?",
 cap_en="Your friend uses presumptive taxation, so you will too? The scheme exists for professionals, but under conditions. Check with your income, expenses and bank records whether it applies to you first. What is your profession?",
 cap_mg="Friend presumptive taxation edukkunnu, athukondu njaanum? Professionals-nu aa reethi undu, pakshe nibandhanakal undu. Varavum chelavum bank kanakkum vechu ningalkku baadhakamaano ennu aadyam urappaakku. Ningal ethu profession-ilaanu?")
