# nri tips 02 (27 Nov evening): tip reel as a duo3d scene. theme="tip". Facts only from topics.FACTS_NRI.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA

duo("pvt003", "gulf_returnee", "B", "gulfoffice", "NORKA NDPREM:\n4 നമ്പർ\nഓർത്തുവെക്കൂ", [
 ("A","wide","ആസിഫേ, NORKA NDPREM-നെ കുറിച്ച് നാല് നമ്പർ ഓർത്താൽ മതി."),
 ("A","A","ഒന്ന്: വിദേശത്ത് കുറഞ്ഞത് 2 വർഷം, പിന്നെ സ്ഥിരമായി തിരിച്ചെത്തിയവർ. രണ്ട്: ലോൺ 1 ലക്ഷം മുതൽ 30 ലക്ഷം വരെ."),
 ("V","V","മൂന്ന്: ക്യാപിറ്റൽ സബ്സിഡി 15%, പരമാവധി 3 ലക്ഷം. നാല്: ആദ്യ 4 വർഷം 3% പലിശ സബ്സിഡി, കൃത്യമായി തിരിച്ചടച്ചാൽ."),
 ("A","A","ലോൺ തീരുമാനിക്കുന്നത് പാർട്ണർ ബാങ്കാണ്. അത് മറക്കരുത്."),
 ("V","wide","2 വർഷം, 30 ലക്ഷം, 15%, 3%.")],
 "2 വർഷം, 30 ലക്ഷം,\n15%, 3%", CTA_NORKA, theme="tip",
 cap_ml="NORKA NDPREM, 4 നമ്പറിൽ: വിദേശത്ത് കുറഞ്ഞത് 2 വർഷം കഴിഞ്ഞ് സ്ഥിരമായി തിരിച്ചെത്തിയവർക്ക്; ലോൺ 1 ലക്ഷം മുതൽ 30 ലക്ഷം വരെ; ക്യാപിറ്റൽ സബ്സിഡി 15% (പരമാവധി 3 ലക്ഷം); ആദ്യ 4 വർഷം 3% പലിശ സബ്സിഡി, കൃത്യമായി തിരിച്ചടയ്ക്കുന്നവർക്ക്. ലോൺ തീരുമാനിക്കുന്നത് ബാങ്കാണ്. ഇതിൽ ഏത് നമ്പറാണ് നിങ്ങൾക്ക് പുതിയത്?",
 cap_en="NORKA NDPREM in 4 numbers: for Keralites who returned for good after at least 2 years abroad; bank loans from 1 lakh to 30 lakh; a 15% capital subsidy (up to 3 lakh); a 3% interest subsidy for the first 4 years for those who repay on time. The partner bank decides the loan. Which number was new to you?",
 cap_mg="NORKA NDPREM, 4 number-il: videshathu kuranjathu 2 varsham kazhinju sthiramaayi thiricchethiyavarkku; loan 1 lakh muthal 30 lakh vare; capital subsidy 15% (paramaavadhi 3 lakh); aadya 4 varsham 3% palisha subsidy, kruthyamaayi thiricchadaykkunnavarkku. Loan theerumaanikkunnathu bank aanu. Ithil ethu number aanu ningalkku puthiyathu?")
