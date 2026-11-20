# Tips and tricks 03 (20 Nov evening): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_FP. Never a fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

lst('fpt011', 'early_revenue', "B", 'പ്രൊജക്ഷൻ\nഉണ്ടാക്കി മറന്നോ?\nമാസാവസാനം 3 വരി', [('പ്ലാൻ', 'ഈ മാസം പ്രതീക്ഷിച്ച വരുമാനവും ചെലവും.'), ('യഥാർത്ഥം', 'ശരിക്കും വന്നതും പോയതും.'), ('വ്യത്യാസം വലുതെങ്കിൽ', 'ആ അനുമാനം തിരുത്തൂ, ബാക്കി മാസങ്ങളും.')],
 'പ്ലാനും കണക്കും\nഒത്തുനോക്കിയാലേ\nവിശ്വാസം', CTA_FORECAST, theme="tip",
 cap_ml='ഇൻവെസ്റ്റർക്കും ബാങ്കിനും വേണ്ടത് ട്രാക്ഷനോട് ചേർന്ന പ്രൊജക്ഷൻ. എല്ലാ മാസാവസാനവും പ്ലാൻ ചെയ്ത നമ്പറും യഥാർത്ഥ നമ്പറും ഒത്തുനോക്കി, എഴുതിയ അനുമാനങ്ങൾ തിരുത്തൂ. നിങ്ങൾ ഇത് മാസം തോറും നോക്കാറുണ്ടോ?',
 cap_en='Investors and banks want projections tied to real traction. At every month end, compare planned numbers with actuals and fix the written assumptions behind any big gap. Do you check this every month?',
 cap_mg='Investor-kkum bank-inum vendathu traction-odu chernna projection. Ella maasaavasaanavum plan cheytha number-um real number-um othunokki, ezhuthiya assumptions thiruthoo. Ningal ithu maasam thorum nokkaarundo?')
