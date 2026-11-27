# nri tips 01 (27 Nov): tip reels as 3D scenes (not lists), theme="tip". Facts only from topics.FACTS_NRI. Never promise a loan or subsidy.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, toon, S, C, T, topics = _h.duo, _h.toon, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA


duo("pvt001", "nri_investing", "B", "bank", "NRI ഷെയർ ഉടമ ഉണ്ടോ?\nഈ 3 തീയതി\nഓർത്തുവെക്കൂ", [
 ("A","wide","മനോജ്, കമ്പനിയിൽ NRI ഷെയർ ഉടമ ഉണ്ടെങ്കിൽ മൂന്ന് തീയതി ഓർക്കണം."),
 ("V","V","പറ, ഞാൻ എഴുതാം."),
 ("A","A","പുതിയ ഷെയർ കൊടുത്താൽ 30 ദിവസത്തിനകം FC-GPR. ഷെയർ കൈമാറിയാൽ 60 ദിവസത്തിനകം FC-TRS."),
 ("V","V","മൂന്നാമത്തേത്?"),
 ("A","wide","എല്ലാ വർഷവും ജൂലൈ 15-നകം FLA റിട്ടേൺ. മൂന്നും RBI-ക്ക്.")],
 "30, 60, ജൂലൈ 15", CTA_PRAVASI, theme="tip",
 cap_ml="കമ്പനിയിൽ NRI ഷെയർ ഉടമ ഉണ്ടെങ്കിൽ: പുതിയ ഷെയർ കൊടുത്താൽ 30 ദിവസത്തിനകം FC-GPR, ഷെയർ കൈമാറിയാൽ 60 ദിവസത്തിനകം FC-TRS, എല്ലാ വർഷവും ജൂലൈ 15-നകം FLA റിട്ടേൺ. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് പുതിയത്?",
 cap_en="A non-resident shareholder in your company? Three dates: FC-GPR within 30 days of issuing shares, FC-TRS within 60 days of a share transfer, and the FLA return by 15 July every year. Which one was new to you?",
 cap_mg="Company-il NRI share udama undenkil: puthiya share koduthaal 30 divasathinakam FC-GPR, share kaimaariyaal 60 divasathinakam FC-TRS, ella varshavum July 15-nakam FLA return. Ithil ethaanu ningalkku puthiyathu?")

duo("pvt002", "gulf_returnee", "B", "ferry", "NORKA ലോണിന്\nമുമ്പ് ഈ\n3 ചോദ്യം", [
 ("V","wide","മീരേ, ചേട്ടൻ ഗൾഫിൽ നിന്ന് വരുന്നു. NORKA ലോണിന് മുമ്പ് എന്ത് നോക്കണം?"),
 ("A","A","ഒന്ന്: 2 വർഷമെങ്കിലും വിദേശത്ത് ജോലി ചെയ്തോ? രണ്ട്: സ്ഥിരമായി തിരിച്ചു വന്നതാണോ?"),
 ("V","V","മൂന്ന്?"),
 ("A","wide","തവണ കൃത്യമായി അടയ്ക്കാൻ പറ്റുമോ? 3% പലിശ സബ്സിഡി കൃത്യമായി അടയ്ക്കുന്നവർക്കാണ്. ലോൺ തീരുമാനം ബാങ്കിന്റേത്.")],
 "മൂന്നിനും അതെ\nആണോ?", CTA_NORKA, theme="tip",
 cap_ml="NORKA NDPREM-ന് മുമ്പ് 3 ചോദ്യം: 2 വർഷമെങ്കിലും വിദേശത്ത് ജോലി ചെയ്തോ? സ്ഥിരമായി തിരിച്ചു വന്നതാണോ? തവണ കൃത്യമായി അടയ്ക്കാൻ പറ്റുമോ? 3% പലിശ സബ്സിഡി കൃത്യമായി അടയ്ക്കുന്നവർക്ക് മാത്രം. ലോൺ ബാങ്കാണ് തീരുമാനിക്കുന്നത്. നിങ്ങൾക്ക് മൂന്നിനും അതെ ആണോ?",
 cap_en="Three questions before a NORKA NDPREM loan: did you work abroad for at least 2 years, have you returned for good, and can you repay every instalment on time? The 3% interest subsidy is only for on-time repayers, and the bank decides the loan. Is it yes to all three?",
 cap_mg="NORKA NDPREM-nu mumpu 3 chodyam: 2 varshamenkilum videshathu joli cheytho? Sthiramaayi thirichu vannathaano? Thavana krithyamaayi adakkaan pattumo? 3% palisha subsidy krithyamaayi adakkunnavarkku maathram. Loan bank aanu theerumaanikkunnathu. Ningalkku moonninum athe aano?")
