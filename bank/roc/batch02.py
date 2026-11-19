# ROC annual compliance batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_ROC. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rc002", "late_filer", "B", "hostel", "കോളേജ് പ്രൊജക്റ്റിന്\nതുടങ്ങിയ കമ്പനി.\n3 വർഷം മറന്നു", [
 ("A","wide","സഞ്ജു, ഫൈനൽ ഇയറിൽ ഡ്രോൺ പ്രൊജക്റ്റിന് നമ്മൾ ഒരു കമ്പനി തുടങ്ങിയില്ലേ? അത് ഓർമ്മയുണ്ടോ?"),
 ("V","V","ഓ, അത്! പ്രൊജക്റ്റ് കഴിഞ്ഞു, എല്ലാരും ജോലിക്ക് പോയി. എന്താ ഇപ്പോ?"),
 ("A","A","പുതിയ സ്റ്റാർട്ടപ്പിന് ഒരു ഇൻവെസ്റ്റർ ചോദിച്ചു, പഴയ കമ്പനിയുടെ ഫയലിംഗ് എന്തായി എന്ന്. 3 വർഷമായി ഒന്നുമില്ല."),
 ("V","wide","3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യത വരാം. കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം."),
 ("A","A","അപ്പോ പുതിയത് തുടങ്ങും മുമ്പ് പഴയത് ശരിയാക്കണം."),
 ("V","wide","അതെ. പ്രൊജക്റ്റ് തീർന്നാലും കമ്പനി ജീവനോടെയുണ്ട്.")],
 "മറന്ന കമ്പനിക്കും\nഫയലിംഗ് ഉണ്ട്", CTA_ROC, theme="crm",
 cap_ml="കോളേജ് പ്രൊജക്റ്റിന് തുടങ്ങിയ കമ്പനി 3 വർഷം മറന്നുപോയി. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യതയും കമ്പനി സ്ട്രൈക്ക് ഓഫും വരാം.",
 cap_en="Students registered a company for a final-year drone project, then forgot it for 3 years. Three years without ROC filings can disqualify the directors for 5 years and get the company struck off. Fix the old company before starting the next one.",
 cap_mg="College project-nu thudangiya company 3 varsham marannupoyi. 3 varsham file cheythillenkil directors-nu 5 varsham ayogyathayum company strike off-um varaam.")