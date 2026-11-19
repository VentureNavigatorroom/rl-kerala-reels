# Co-founder agreement batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_CFA. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

duo("cf001", "late_joiner", "A", "salon", "55% എന്റെ കയ്യിൽ.\nരണ്ട് പുതിയ പാർട്ണർ.\nകൺട്രോൾ ആർക്ക്?", [
 ("A","wide","വിനീത്, എന്റെ ബ്രൈഡൽ മേക്കപ്പ് ബിസിനസിൽ രണ്ട് പേർ പാർട്ണർ ആകാൻ റെഡി. എനിക്ക് ഇപ്പോ 55%."),
 ("V","V","അവർക്ക് ഷെയർ കൊടുത്താൽ 55% കുറയും. തീരുമാനങ്ങൾ ആര് എടുക്കും എന്ന് എഴുതിയിട്ടുണ്ടോ?"),
 ("A","A","ഇല്ല. എല്ലാം വാക്കാലെ ആണ്."),
 ("V","wide","കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ റോളുകൾ, തീരുമാനങ്ങൾ, വെസ്റ്റിംഗ് എല്ലാം വേണം. അതേ റൈറ്റ്സ് SHA-യിലും ആർട്ടിക്കിൾസിലും."),
 ("A","A","ഷെയർ കുറഞ്ഞാലും ശബ്ദം കുറയരുത്."),
 ("V","wide","അതെ. മേക്കപ്പ് പോലെ, ആദ്യം ബേസ് ഇടണം.")],
 "പാർട്ണർ വരും മുമ്പ്\nഎഗ്രിമെന്റ്", CTA_COFOUNDER, theme="crm",
 cap_ml="55% ഉള്ള ഫൗണ്ടർ പുതിയ പാർട്ണർമാരെ എടുക്കുമ്പോൾ കൺട്രോൾ എങ്ങനെ കാക്കും? കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ റോളുകളും തീരുമാന അധികാരവും വെസ്റ്റിംഗും എഴുതി, അതേ റൈറ്റ്സ് SHA-യിലും ആർട്ടിക്കിൾസിലും ചേർക്കണം.",
 cap_en="A bridal makeup founder holding 55% is bringing in two partners, with nothing in writing. A co-founder agreement sets roles, decisions and vesting, and the same rights must be mirrored in the SHA and the articles. Who decides in your business?",
 cap_mg="55% ulla founder puthiya partners-ine edukkumbol control engane kaakkum? Co-founder agreement-il roles-um decision power-um vesting-um ezhuthi, athe rights SHA-yilum articles-ilum cherkkanam.")