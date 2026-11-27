# GST batch 07 (27 Nov night): "fix-it" reels on a query / rejection of a GST application (HANDOVER 5b).
# Facts only from topics.FACTS_GST (CGST rule 9 line added 27 Nov from taxinformation.cbic.gov.in). Never promise approval. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

# faq, fix-it: a courier franchise ignored a REG-03 notice for days, thinking it was spam
duo("gd045", "trader", "B", "courier", "GST അപേക്ഷയ്ക്ക്\nഒരു നോട്ടീസ്.\n\"സ്പാം ആയിരിക്കും\"", [
 ("A","wide","അരവിന്ദേ, GST പോർട്ടലിൽ നിന്ന് REG-03 എന്ന് ഒരു മെയിൽ. അഞ്ച് ദിവസമായി നോക്കിയിട്ടില്ല."),
 ("V","V","ജയേ, അത് സ്പാം അല്ല. ഓഫീസർ അപേക്ഷയിൽ ഒരു ചോദ്യം ചോദിച്ചതാ. മറുപടി REG-04-ൽ, 7 പ്രവൃത്തി ദിവസത്തിനകം."),
 ("A","A","മറുപടി കൊടുത്തില്ലെങ്കിലോ?"),
 ("V","V","അപേക്ഷ റിജക്ട് ചെയ്യാം. ഇന്ന് തന്നെ ചോദിച്ച രേഖ കൊടുക്കാം."),
 ("A","wide","GST നോട്ടീസ് വന്നാൽ, ആദ്യം വായിക്കൂ.")],
 "REG-03 വന്നാൽ\n7 പ്രവൃത്തി ദിവസം", CTA_GST, theme="faq",
 cap_ml="GST അപേക്ഷയ്ക്ക് REG-03 നോട്ടീസ് വന്നോ? ഓഫീസർ ഒരു വിശദീകരണമോ രേഖയോ ചോദിക്കുന്നതാണ്. മറുപടി REG-04-ൽ, നോട്ടീസ് കിട്ടി 7 പ്രവൃത്തി ദിവസത്തിനകം. മറുപടി ഇല്ലെങ്കിൽ അപേക്ഷ റിജക്ട് ചെയ്യാം. നിങ്ങളുടെ GST മെയിൽ അവസാനം നോക്കിയത് എപ്പോൾ?",
 cap_en="A courier franchise owner leaves a GST portal mail called REG-03 unopened for five days. It is the officer's query on the application: the reply goes in REG-04 within 7 working days of the notice, and with no reply the application may be rejected. When did you last check your GST mail?",
 cap_mg="GST apekshaykku REG-03 notice vanno? Officer oru vishadeekaranamo rekhayo chodikkunnathaanu. Marupadi REG-04-il, notice kitti 7 working days-inakam. Marupadi illenkil apeksha reject cheyyaam. Ningalude GST mail avasaanam nokkiyathu eppol?")

# new, fix-it: replying to a query, a textile shop wants to change the mobile number too
duo("gd046", "trader", "B", "textile", "GST ചോദ്യത്തിന് മറുപടി.\nകൂട്ടത്തിൽ മൊബൈൽ\nനമ്പറും മാറ്റാം?", [
 ("A","wide","പ്രകാശേ, ഓഫീസർ വാടക കരാറിലെ അഡ്രസ് തിരുത്താൻ പറഞ്ഞു. കൂട്ടത്തിൽ പുതിയ മൊബൈൽ നമ്പറും REG-04-ൽ കൊടുക്കാം."),
 ("V","V","രമ്യേ, REG-04-ൽ രേഖകളും തിരുത്തലുകളും കൊടുക്കാം. പക്ഷേ PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ ഈ വഴി മാറ്റാൻ പറ്റില്ല."),
 ("A","A","അപ്പോ ചോദിച്ച തിരുത്തൽ മാത്രം, കൃത്യമായി."),
 ("V","V","അതെ. മറുപടി കിട്ടിയാൽ ഓഫീസർ 7 പ്രവൃത്തി ദിവസത്തിനകം തീരുമാനിക്കും."),
 ("A","wide","ചോദിച്ചതിന് മാത്രം, കൃത്യമായ മറുപടി.")],
 "ചോദിച്ച തിരുത്തൽ,\nകൃത്യമായി", CTA_GST, theme="new",
 cap_ml="GST അപേക്ഷയിലെ ചോദ്യത്തിന് REG-04-ൽ രേഖകളും തിരുത്തലുകളും കൊടുക്കാം. പക്ഷേ PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ ഈ വഴി മാറ്റാനാവില്ല. മറുപടി കിട്ടി 7 പ്രവൃത്തി ദിവസത്തിനകം ഓഫീസർ തീരുമാനിക്കും. നിങ്ങൾക്ക് GST ഓഫീസറിൽ നിന്ന് ചോദ്യം വന്നിട്ടുണ്ടോ?",
 cap_en="Replying to a GST query about her rent agreement, a textile shop owner wants to change her mobile number too. A REG-04 reply can carry documents and corrections, but not changes to PAN, State, mobile or e-mail. After the reply the officer decides within 7 working days. Have you had a GST query?",
 cap_mg="GST apekshayile chodyathinu REG-04-il rekhakalum thiruthalukalum kodukkaam. Pakshe PAN, State, mobile, email ee vazhi maattaanaavilla. Marupadi kitti 7 working days-inakam officer theerumaanikkum. Ningalkku GST officer-il ninnu chodyam vannittundo?")

# tip (fix-it): a GST application query in 3 steps
duo("gt101", "new_company", "B", "akshaya", "GST അപേക്ഷയ്ക്ക്\nചോദ്യം വന്നോ?\n3 സ്റ്റെപ്പ്", [
 ("A","wide","രമേശേട്ടാ, GST അപേക്ഷയിൽ ഓഫീസർ ചോദ്യം ചോദിച്ചാൽ മൂന്ന് സ്റ്റെപ്പ്."),
 ("A","A","ഒന്ന്: REG-03 നോട്ടീസ് മുഴുവൻ വായിക്കുക. എന്ത് രേഖ, എന്ത് തിരുത്തൽ എന്ന്."),
 ("V","V","രണ്ട്: REG-04-ൽ മറുപടി, 7 പ്രവൃത്തി ദിവസത്തിനകം. ചോദിച്ച രേഖ തന്നെ."),
 ("A","A","മൂന്ന്: മറുപടിക്ക് ശേഷം ഓഫീസർ 7 പ്രവൃത്തി ദിവസത്തിനകം തീരുമാനിക്കും. മറുപടി ഇല്ലെങ്കിൽ റിജക്ട് ആകാം."),
 ("V","wide","വായിക്കുക, മറുപടി, കാത്തിരിക്കുക.")],
 "വായിക്കൂ, 7 ദിവസത്തിനകം\nമറുപടി കൊടുക്കൂ", CTA_GST, theme="tip",
 cap_ml="GST അപേക്ഷയ്ക്ക് ചോദ്യം വന്നാൽ 3 സ്റ്റെപ്പ്: REG-03 നോട്ടീസ് മുഴുവൻ വായിക്കുക; REG-04-ൽ ചോദിച്ച രേഖയോടെ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി; മറുപടിക്ക് ശേഷം ഓഫീസർ 7 പ്രവൃത്തി ദിവസത്തിനകം തീരുമാനിക്കും. മറുപടി ഇല്ലെങ്കിൽ REG-05 വഴി റിജക്ട് ചെയ്യാം. ഈ ഫോം നമ്പറുകൾ നിങ്ങൾ കേട്ടിട്ടുണ്ടോ?",
 cap_en="A query on your GST application, in 3 steps: read the REG-03 notice in full; reply in REG-04 with exactly what was asked within 7 working days; after the reply the officer decides within 7 working days. With no reply the application may be rejected in REG-05. Had you heard of these forms?",
 cap_mg="GST apekshaykku chodyam vannaal 3 step: REG-03 notice muzhuvan vaayikkuka; REG-04-il chodicha rekhayode 7 working days-inakam marupadi; marupadikku shesham officer 7 working days-inakam theerumaanikkum. Marupadi illenkil REG-05 vazhi reject cheyyaam. Ee form numbers ningal kettittundo?")
