# Investor agreements seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
car("vk001", "founder_raising", "പേപ്പർ", "ഇൻവെസ്റ്റർ യെസ്\nപറഞ്ഞു. ഇനി\nഈ 4 പേപ്പർ", [
 ("ടേം ഷീറ്റ്", "പ്രധാന നിബന്ധനകൾ. മിക്കതും ബൈൻഡിംഗ് അല്ല, എക്സ്ക്ലൂസിവിറ്റിയും കോൺഫിഡൻഷ്യാലിറ്റിയും ബൈൻഡിംഗ്."),
 ("ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്", "എത്ര പൈസ, എത്ര ഷെയർ, എന്ത് വ്യവസ്ഥ."),
 ("ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്", "ബോർഡ് സീറ്റ്, ഷെയർ ട്രാൻസ്ഫർ നിയന്ത്രണം, എക്സിറ്റ്."),
 ("ആർട്ടിക്കിൾസ് മാറ്റം", "ഈ അവകാശങ്ങൾ കമ്പനിയെ ബാധിക്കാൻ ആർട്ടിക്കിൾസിലും വേണം.")],
 "പൈസയ്ക്ക് മുമ്പ്\nപേപ്പർ", topics.CTA_INVEST,
 cap_ml="ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞാൽ വേണ്ട നാല് പേപ്പർ: ടേം ഷീറ്റ്, ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്, ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്, ആർട്ടിക്കിൾസ് മാറ്റം.",
 cap_en="After an investor says yes, four documents: term sheet, share subscription agreement, shareholders' agreement and amended articles of association. Investor agreements for Kerala startups.",
 cap_mg="Investor yes paranjaal venda 4 paper: term sheet, share subscription agreement, shareholders agreement, articles maattam.")
car("vk002", "nri_investor", "NRI", "ഗൾഫിൽ നിന്ന്\nനാട്ടിലെ കമ്പനിയിൽ\nനിക്ഷേപിക്കുമ്പോൾ", [
 ("കമ്പനി", "പ്രൈവറ്റ് ലിമിറ്റഡ് ആണെന്ന് ഉറപ്പാക്കൂ."),
 ("മൂല്യം", "റീപാട്രിയേഷൻ ബേസിസിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ ആകരുത്. വാല്യുവേഷൻ റിപ്പോർട്ട്."),
 ("റിപ്പോർട്ട്", "അലോട്ട്മെന്റ് കഴിഞ്ഞ് 30 ദിവസത്തിൽ RBI-ക്ക് FC-GPR."),
 ("സുരക്ഷ", "ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിൽ നിങ്ങളുടെ അവകാശങ്ങൾ.")],
 "ദൂരെയിരുന്നും\nസുരക്ഷിതമായി", topics.CTA_FUNDING,
 cap_ml="ഗൾഫിലുള്ള മലയാളി നാട്ടിലെ കമ്പനിയിൽ നിക്ഷേപിക്കുമ്പോൾ: പ്രൈവറ്റ് ലിമിറ്റഡ്, വാല്യുവേഷൻ, 30 ദിവസത്തിൽ FC-GPR, ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്.",
 cap_en="Investing from the Gulf in a Kerala company: check it is a Pvt Ltd, shares issued at or above fair value with a valuation report, FC-GPR within 30 days of allotment, and your rights in a shareholders' agreement.",
 cap_mg="Gulf-il ulla Malayali naattile company-il invest cheyyumbol: Pvt Ltd, valuation, 30 divasathil FC-GPR, shareholders agreement.")
