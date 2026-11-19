# KSUM batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_SK. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

duo("md005", "kerala_registered", "A", "munnar", "\"LLP ആണ്, അതുകൊണ്ട്\nKSUM കിട്ടില്ല\"\nആര് പറഞ്ഞു?", [
 ("A","wide","ബേസിൽ, നമ്മുടെ ടീ-ടൂറിസം ആപ്പ് LLP ആയാ രജിസ്റ്റർ ചെയ്തത്. KSUM യുണീക്ക് ഐഡി കമ്പനികൾക്ക് മാത്രമല്ലേ?"),
 ("V","V","അല്ല. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ ആകാം. MCA-യിൽ സ്റ്റാറ്റസ് ആക്ടീവ് ആയിരിക്കണം."),
 ("A","A","ഗ്രാന്റിന് വേറെ എന്തെങ്കിലും വേണോ?"),
 ("V","wide","മിക്ക ഗ്രാന്റുകൾക്കും DPIIT റെക്കഗ്നിഷനും ചോദിക്കും. KSUM-ന്റെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ അപേക്ഷിക്കാം."),
 ("A","A","എങ്കിൽ ഇന്ന് തന്നെ പോർട്ടൽ തുറക്കാം."),
 ("V","wide","ചായ തണുക്കും മുമ്പ് യുണീക്ക് ഐഡി.")],
 "LLP-ക്കും\nKSUM യുണീക്ക് ഐഡി", CTA_KSUM, theme="faq",
 cap_ml="LLP-ക്ക് KSUM യുണീക്ക് ഐഡി കിട്ടുമോ? കിട്ടും: കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ, MCA-യിൽ ആക്ടീവ് സ്റ്റാറ്റസ്. മിക്ക ഗ്രാന്റുകൾക്കും DPIIT-ഉം വേണം. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ് LLP ആണോ?",
 cap_en="Can an LLP get the KSUM Unique ID? Yes: a private limited company or LLP registered in Kerala with Active status at MCA. Most KSUM grants also ask for DPIIT recognition. Apply on KSUM's startup portal. Is your startup an LLP?",
 cap_mg="LLP-kku KSUM Unique ID kittumo? Kittum: Kerala-yil register cheytha private limited-o LLP-yo, MCA-yil active status. Mikka grants-num DPIIT-um venam.")

duo("md006", "campus", "B", "classroom", "ഐഡിയ ഗ്രാന്റ്\nഷോർട്ട്‌ലിസ്റ്റ്.\nപൈസ? \"കമ്പനി എവിടെ?\"", [
 ("A","wide","ആദർശ്, നമ്മുടെ കാർഷിക സെൻസർ ഐഡിയ ഷോർട്ട്‌ലിസ്റ്റ് ആയി! പക്ഷേ ഫണ്ട് റിലീസിന് കമ്പനി ചോദിക്കുന്നു."),
 ("V","V","ഐഡിയ ഗ്രാന്റിന് കമ്പനി ഇല്ലാതെ അപേക്ഷിക്കാം. പക്ഷേ പൈസ കിട്ടും മുമ്പ് കമ്പനിയും യുണീക്ക് ഐഡിയും വേണം."),
 ("A","A","അപ്പോ ഇപ്പോ തന്നെ കമ്പനി തുടങ്ങണോ?"),
 ("V","wide","അതെ, കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത്. പിന്നെ KSUM പോർട്ടലിൽ യുണീക്ക് ഐഡി."),
 ("A","A","സെമസ്റ്റർ എക്സാമിന് മുമ്പ് ഇതും പാസ്സാകണം."),
 ("V","wide","ഐഡിയ ജയിച്ചു. ഇനി പേപ്പർ ജയിക്കണം.")],
 "ഗ്രാന്റ് റിലീസിന്\nകമ്പനി വേണം", CTA_GRANT, theme="crm",
 cap_ml="കോളേജ് ടീമിന്റെ ഐഡിയ KSUM ഐഡിയ ഗ്രാന്റിൽ ഷോർട്ട്‌ലിസ്റ്റ് ആയി, പക്ഷേ കമ്പനി ഇല്ല. കമ്പനിക്ക് മുമ്പ് അപേക്ഷിക്കാം; പണം റിലീസ് ചെയ്യും മുമ്പ് കമ്പനിയും യുണീക്ക് ഐഡിയും വേണം.",
 cap_en="A campus team's farm sensor idea is shortlisted for the KSUM idea grant, but they never formed a company. You may apply before incorporating, but the company, registered in Kerala, and the KSUM Unique ID are needed before any money is released.",
 cap_mg="College team-inte idea KSUM idea grant-il shortlist aayi, pakshe company illa. Company-kku munpu apekshikkaam; panam release cheyyum munpu company-um Unique ID-um venam.")

duo("md007", "returnee", "A", "railway", "കമ്പനി ബാംഗ്ലൂരിൽ.\nഡ്രോൺ കേരളത്തിലെ പാടത്ത്.\nKSUM: \"ഇല്ല\"", [
 ("A","wide","ദിനേശേട്ടാ, മസ്കറ്റിൽ നിന്ന് വന്ന് ഞാൻ തുടങ്ങിയ ഡ്രോൺ സ്പ്രേ കമ്പനി ബാംഗ്ലൂരിലാ രജിസ്റ്റർ ചെയ്തത്. KSUM-ൽ പ്രശ്നമുണ്ടോ?"),
 ("V","V","KSUM സ്കീമുകൾക്ക് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതാകണം. യുണീക്ക് ഐഡി ഉള്ളവർക്കാ ഗ്രാന്റും ഇൻക്യുബേഷനും."),
 ("A","A","പാടം ഇവിടെ, ജോലിക്കാരും ഇവിടെ. എന്നിട്ടും?"),
 ("V","wide","അതെ, രജിസ്ട്രേഷൻ എവിടെ എന്നാ നോക്കുന്നത്. മിക്ക ഗ്രാന്റുകൾക്കും DPIIT-ഉം ചോദിക്കും."),
 ("A","A","അപ്പോ ആദ്യം ഇത് ശരിയാക്കണം."),
 ("V","wide","ഡ്രോൺ പറക്കുന്നത് കേരളത്തിൽ. പേപ്പറും ഇവിടെ ഇറങ്ങണം.")],
 "KSUM-ന് കേരള\nരജിസ്ട്രേഷൻ വേണം", CTA_KSUM, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തി തുടങ്ങിയ ഡ്രോൺ സ്റ്റാർട്ടപ്പ് മറ്റൊരു സംസ്ഥാനത്ത് രജിസ്റ്റർ ചെയ്തു. KSUM സ്കീമുകൾക്ക് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പും യുണീക്ക് ഐഡിയും വേണം. നിങ്ങളുടെ കമ്പനി എവിടെ രജിസ്റ്റർ ചെയ്തു?",
 cap_en="A Gulf returnee's paddy-spraying drone startup works in Kerala but was registered in Bengaluru. KSUM schemes, grants and incubation are for startups registered in Kerala that hold the KSUM Unique ID; most grants also ask for DPIIT recognition.",
 cap_mg="Gulf-il ninnu thirichethi thudangiya drone startup vere state-il register cheythu. KSUM schemes-nu Kerala-yil register cheytha startup-um Unique ID-um venam.")
