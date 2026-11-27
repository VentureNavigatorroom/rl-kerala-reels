# acc tips 02 (27 Nov evening): tip reel as a duo3d scene. theme="tip". Facts only from topics.FACTS_ACC + GSTR-3B late fees in topics.FACTS_GST.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

duo("act003", "small_trader_acc", "B", "bank", "വൈകിയാൽ എത്ര പോകും?\n3 ലേറ്റ് ഫീ\nഒറ്റ നോട്ടത്തിൽ", [
 ("A","wide","മനോജേ, റിട്ടേൺ വൈകിയാൽ എത്ര പോകും എന്ന് ഒറ്റ നോട്ടത്തിൽ പറയാം."),
 ("A","A","നിൽ GSTR-3B: ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 രൂപ വരെ."),
 ("V","V","വിൽപ്പന ഉള്ള 3B: ദിവസം 50 രൂപ. ടേൺഓവർ ഒന്നര കോടി വരെ 2,000 രൂപ വരെ."),
 ("A","A","ITR: വരുമാനം 5 ലക്ഷം വരെ 1,000 രൂപ. അതിന് മുകളിൽ 5,000 രൂപ."),
 ("V","wide","സമയത്ത് ഫയൽ ചെയ്താൽ ഇതൊന്നും വേണ്ട.")],
 "സമയത്ത് ഫയൽ ചെയ്താൽ\nലേറ്റ് ഫീ ഇല്ല", CTA_ITR, theme="tip",
 cap_ml="വൈകിയാൽ എത്ര പോകും? നിൽ GSTR-3B: ദിവസം 20 രൂപ (ഒരു റിട്ടേണിന് 500 രൂപ വരെ). വിൽപ്പന ഉള്ള 3B: ദിവസം 50 രൂപ (ടേൺഓവർ 1.5 കോടി വരെ 2,000 രൂപ വരെ). ITR: വരുമാനം 5 ലക്ഷം വരെ 1,000 രൂപ, അതിന് മുകളിൽ 5,000 രൂപ. ഡ്യൂ ഡേറ്റ് ടീമിനോട് ഉറപ്പാക്കൂ. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് പുതിയ അറിവ്?",
 cap_en="What a late filing costs: a nil GSTR-3B, 20 rupees a day (up to 500 rupees per return); a 3B with sales, 50 rupees a day (up to 2,000 rupees for turnover up to 1.5 crore); a late ITR, 1,000 rupees for income up to 5 lakh, 5,000 rupees above that. Confirm due dates with the team. Which one was new to you?",
 cap_mg="Vaikiyaal ethra pokum? Nil GSTR-3B: divasam 20 rupees (oru return-inu 500 rupees vare). Vilpana ulla 3B: divasam 50 rupees (turnover 1.5 crore vare 2,000 rupees vare). ITR: varumaanam 5 lakh vare 1,000 rupees, athinu mukalil 5,000 rupees. Due date team-inodu urappaakku. Ithil ethaanu ningalkku puthiya arivu?")
