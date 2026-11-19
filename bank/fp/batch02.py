# Financial projections batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FP. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

duo("fp001", "pre_revenue", "A", "metro", "\"എത്ര വേണം?\"\n\"ആപ്പ് ചെലവ് + 6 മാസം\nശമ്പളം\"", [
 ("A","wide","കിരൺ, ഇൻവെസ്റ്റർ ചോദിച്ചു എത്ര വേണം എന്ന്. ഞാൻ ആപ്പ് ഡെവലപ്മെന്റും 6 മാസത്തെ ചെലവും കൂട്ടി പറഞ്ഞു."),
 ("V","V","എന്നിട്ട്?"),
 ("A","A","അയാൾ ചോദിച്ചു, മാസം തോറുമുള്ള പ്രൊജക്ഷൻ എവിടെ എന്ന്."),
 ("V","wide","അതാ വേണ്ടത്. 3 വർഷം, ആദ്യ വർഷം മാസം തോറും. എത്ര കസ്റ്റമർ, ഓരോരുത്തരും എത്ര തരും, ചെലവ്, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക് ഈവൻ."),
 ("A","A","അപ്പോ ചോദിക്കുന്ന തുക കണക്കിൽ നിന്ന് വരണം."),
 ("V","wide","അതെ. ബില്ല് കൂട്ടിയാൽ ബജറ്റ്. ഭാവി കണക്കാക്കിയാൽ പ്രൊജക്ഷൻ.")],
 "ചോദിക്കുന്ന തുക\nകണക്കിൽ നിന്ന് വരണം", CTA_PROJECTION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റ്മെന്റ് തുക ആപ്പ് ചെലവും ശമ്പളവും കൂട്ടി പറഞ്ഞപ്പോൾ ഇൻവെസ്റ്റർ പ്രൊജക്ഷൻ ചോദിച്ചു. 3 വർഷം, ആദ്യ വർഷം മാസം തോറും: കസ്റ്റമർ, വരുമാനം, ചെലവ്, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക് ഈവൻ.",
 cap_en="A founder worked out her ask by adding app development to six months of costs, and the investor asked for monthly projections instead. Investors expect 3 years, month by month for year 1: customers, revenue per customer, costs, cash flow and break-even.",
 cap_mg="Investment thuka app chelavum shambalavum kootti paranjappol investor projection chodichu. 3 varsham, aadya varsham maasam thorum: customer, varumaanam, chelavu, cash flow, break-even.")