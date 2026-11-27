# nri batch 02 (27 Nov evening refill): 3D duo reel. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns. Facts only from topics.FACTS_NRI. Never promise a loan or subsidy, never say when a subsidy is released, never our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA

# faq: a returnee counts 15% of a 30 lakh loan as his subsidy; the capital subsidy has a ceiling of 3 lakh
duo("pvd006", "returnee_loan", "B", "airport", "30 ലക്ഷത്തിന്റെ 15%\nസബ്സിഡി എന്ന്\nകണക്ക് കൂട്ടി", [
 ("A","wide","റഫീഖേ, 30 ലക്ഷം ലോൺ എടുത്താൽ 15% സബ്സിഡി. അപ്പോ നാലര ലക്ഷം തിരിച്ചു കിട്ടും എന്നാ എന്റെ കണക്ക്."),
 ("V","V","ഷമീറേ, NORKA NDPREM-ൽ ക്യാപിറ്റൽ സബ്സിഡി 15% ആണ്. പക്ഷേ പരമാവധി 3 ലക്ഷം."),
 ("A","A","അപ്പോ നാലര അല്ല. അതും ബാങ്ക് ലോൺ അനുവദിച്ചാൽ മാത്രം, അല്ലേ?"),
 ("V","V","അതെ. ലോൺ ബാങ്കാണ് തീരുമാനിക്കുന്നത്. സബ്സിഡി കണക്കിൽ കൂട്ടി പ്ലാൻ ചെയ്യരുത്."),
 ("A","wide","15% ആയാലും, മുകളിൽ ഒരു പരിധിയുണ്ട്.")],
 "15% സബ്സിഡി,\nപരമാവധി 3 ലക്ഷം", CTA_NORKA, theme="faq",
 cap_ml="NORKA NDPREM-ൽ ക്യാപിറ്റൽ സബ്സിഡി 15% ആണ്, പക്ഷേ പരമാവധി 3 ലക്ഷം. ലോൺ അനുവദിക്കുന്നത് ബാങ്കാണ്; സബ്സിഡി ഉറപ്പായി കണക്കിൽ കൂട്ടി പ്ലാൻ ചെയ്യരുത്. നിങ്ങളുടെ പ്രോജക്റ്റ് പ്ലാനിൽ സബ്സിഡി എങ്ങനെയാണ് എഴുതിയത്?",
 cap_en="A Gulf returnee counts 15% of a 30 lakh loan as his subsidy. Under NORKA NDPREM the capital subsidy is 15%, but capped at 3 lakh, and only once the bank sanctions the loan; the bank decides. Don't build your plan on the subsidy. How did your project plan count it?",
 cap_mg="NORKA NDPREM-il capital subsidy 15% aanu, pakshe paramaavadhi 3 lakh. Loan anuvadikkunnathu bank aanu; subsidy urappaayi kanakkil kootti plan cheyyaruthu. Ningalude project plan-il subsidy engane aanu ezhuthiyathu?")
