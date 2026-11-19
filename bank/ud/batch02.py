# Udyam batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_UD. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

duo("yd005", "manufacturer", "A", "fishmarket", "\"പണ്ട് ഉദ്യോഗ് ആധാർ\nഎടുത്തതാ\"\nടെൻഡറിൽ റിജക്റ്റ്", [
 ("A","wide","ആന്റണി, ഉണക്കമീൻ യൂണിറ്റിന്റെ ടെൻഡർ റിജക്റ്റ് ആയി. ഉദ്യം സർട്ടിഫിക്കറ്റ് ഇല്ലെന്ന്. പഴയ ഉദ്യോഗ് ആധാർ ഉണ്ടല്ലോ!"),
 ("V","V","ചേച്ചീ, 2020 ജൂലൈ 1 മുതൽ MSME രജിസ്ട്രേഷൻ ഉദ്യം ആണ്. പഴയത് ഉദ്യമിലേക്ക് മാറ്റണം."),
 ("A","A","അതിന് എന്തൊക്കെ വേണം?"),
 ("V","wide","ഓൺലൈൻ, ആധാർ വെച്ച്. പാൻ, GST ഉണ്ടെങ്കിൽ അതും, സെൽഫ് ഡിക്ലറേഷൻ. പുതുക്കേണ്ട, വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്താൽ മതി."),
 ("A","A","അടുത്ത ടെൻഡറിന് മുമ്പ് ചെയ്യും."),
 ("V","wide","പഴയ മീൻ ഉണക്കി വിൽക്കാം. പഴയ രജിസ്ട്രേഷൻ പറ്റില്ല.")],
 "ഉദ്യോഗ് ആധാർ\nഉദ്യമിലേക്ക് മാറ്റൂ", CTA_UDYAM, theme="faq",
 cap_ml="പഴയ ഉദ്യോഗ് ആധാർ മാത്രമുള്ള യൂണിറ്റ് ടെൻഡറിൽ പുറത്തായി. 2020 ജൂലൈ 1 മുതൽ MSME രജിസ്ട്രേഷൻ ഉദ്യം: ഓൺലൈൻ, ആധാർ, പാൻ, സെൽഫ് ഡിക്ലറേഷൻ. നിങ്ങളുടേത് ഇപ്പോഴും ഉദ്യോഗ് ആധാറാണോ?",
 cap_en="A dried-fish unit lost a tender because it only had an old Udyog Aadhaar. Since 1 July 2020 MSME registration is Udyam: online, Aadhaar-based, with PAN (and GSTIN if any) and a self-declaration. No renewal, but keep the details updated. Still on Udyog Aadhaar?",
 cap_mg="Pazhaya Udyog Aadhaar maathramulla unit tender-il purathaayi. 2020 July 1 muthal MSME registration Udyam: online, Aadhaar, PAN, self declaration.")

duo("yd006", "service_unit", "B", "office", "എഗ്രിമെന്റിൽ ഒപ്പിട്ടു:\n\"പേമെന്റ് 90 ദിവസം\"\nനിയമം 45 ആണ്", [
 ("A","wide","രാഹുൽ, ഐടി പാർക്കിലെ കമ്പനിക്ക് ഹൗസ്കീപ്പിംഗ് സർവീസ് കൊടുക്കാൻ കരാർ ഒപ്പിട്ടു. പേമെന്റ് 90 ദിവസത്തിൽ എന്ന്."),
 ("V","V","നമുക്ക് ഉദ്യം ഉണ്ടല്ലോ, മൈക്രോ സർവീസ് യൂണിറ്റ്. എഗ്രിമെന്റിൽ എഴുതിയാലും പരമാവധി 45 ദിവസം."),
 ("A","A","എഗ്രിമെന്റ് ഇല്ലായിരുന്നെങ്കിലോ?"),
 ("V","wide","15 ദിവസം. അത് കഴിഞ്ഞാൽ RBI ബാങ്ക് റേറ്റിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ. പരാതി MSME സമാധാൻ പോർട്ടലിൽ."),
 ("A","A","അപ്പോ 90 എന്ന് എഴുതിയാലും നിയമം 45."),
 ("V","wide","അതെ. ചൂല് നമ്മുടേത്. കലണ്ടർ നിയമത്തിന്റേത്.")],
 "എഴുതിയത് 90 ആയാലും\nപരമാവധി 45 ദിവസം", CTA_UDYAM, theme="new",
 cap_ml="കരാറിൽ 90 ദിവസം എന്ന് എഴുതിയാലും ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക് പേമെന്റ് പരമാവധി 45 ദിവസം; കരാർ ഇല്ലെങ്കിൽ 15. വൈകിയാൽ RBI ബാങ്ക് റേറ്റിന്റെ 3 ഇരട്ടി കൂട്ടുപലിശ. നിങ്ങളുടെ ക്ലയന്റ് എത്ര ദിവസത്തിൽ പേ ചെയ്യുന്നു?",
 cap_en="A housekeeping services unit signed a contract saying payment in 90 days. For Udyam-registered micro and small manufacturing and service units, buyers must pay within 15 days, or the agreed time up to 45 days; after that they owe compound interest at 3x the RBI bank rate.",
 cap_mg="Karaaril 90 divasam ennu ezhuthiyaalum Udyam ulla micro, small units-nu payment paramaavadhi 45 divasam; karaar illenkil 15. Vaikiyaal RBI bank rate-inte 3 iratti koottupalisha.")

duo("yd007", "loan_seeker", "A", "autostand", "\"ഉദ്യം എടുത്തു,\nഇനി ലോൺ ഉറപ്പ്\"\nബാങ്ക് പറഞ്ഞത് വേറെ", [
 ("A","wide","ഷാജി, ഇലക്ട്രിക് ഓട്ടോ സർവീസ് സെന്ററിന് ഉദ്യം എടുത്തു. ഇനി ലോൺ ഉറപ്പല്ലേ?"),
 ("V","V","ഉറപ്പ് ആരും തരില്ല. ഉദ്യം കൊണ്ട് പ്രയോറിറ്റി സെക്ടർ ലെൻഡിംഗിൽ പെടും."),
 ("A","A","പിന്നെ എന്താ ഗുണം?"),
 ("V","wide","CGTMSE പോലുള്ള കൊളാറ്ററൽ ഇല്ലാത്ത ലോൺ സ്കീമുകൾക്ക് സഹായം, സർക്കാർ ടെൻഡറുകളിൽ മുൻഗണന. ബാക്കി ബിസിനസിന്റെ കണക്ക്."),
 ("A","A","ശരി, ആദ്യം കണക്ക് റെഡിയാക്കാം."),
 ("V","wide","ഓട്ടോ ഓടാൻ ബാറ്ററി വേണം. ലോൺ ഓടാൻ കണക്കും.")],
 "ഉദ്യം ലോൺ ഉറപ്പല്ല,\nവാതിൽ തുറക്കും", CTA_UDYAM, theme="faq",
 cap_ml="ഉദ്യം എടുത്താൽ ലോൺ ഉറപ്പാണോ? അല്ല. പ്രയോറിറ്റി സെക്ടർ ലെൻഡിംഗ്, CGTMSE പോലുള്ള കൊളാറ്ററൽ ഇല്ലാത്ത ലോൺ സ്കീമുകൾ, സർക്കാർ ടെൻഡറിൽ മുൻഗണന എന്നിവയ്ക്ക് സഹായിക്കും. നിങ്ങൾ ബിസിനസ് ലോൺ നോക്കുന്നുണ്ടോ?",
 cap_en="An EV auto service centre took Udyam registration and assumes the loan is now guaranteed. It isn't: Udyam helps with priority sector lending, collateral-free loan schemes such as CGTMSE and preferences in government tenders, but nobody can promise a loan.",
 cap_mg="Udyam eduthaal loan urappaano? Alla. Priority sector lending, CGTMSE pole collateral illaatha loan schemes, sarkkar tender-il munganana ennivaykku sahaayikkum.")
