# acc tips 01 (27 Nov): tip reels as duo3d scenes (not lists, per the 26 Nov review). theme="tip". Facts only from topics.FACTS_ACC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

duo("act001", "small_trader_acc", "B", "akshaya", "GST റിട്ടേൺ\nഫയൽ ചെയ്യും മുമ്പ്\n3 ചെക്ക്", [
 ("A","wide","രമേശേട്ടാ, ഈ മാസത്തെ GST റിട്ടേൺ ഫയൽ ചെയ്യും മുമ്പ് മൂന്ന് കാര്യം നോക്കാം."),
 ("A","A","ഒന്ന്: GSTR-1-ലെ ബില്ലുകൾ ശരിയാണോ. 3B-ലെ കണക്ക് അതിൽ നിന്നാണ് വരുന്നത്."),
 ("V","V","രണ്ട്: വിൽപ്പന ഇല്ലാത്ത മാസമാണെങ്കിലും നിൽ റിട്ടേൺ."),
 ("A","A","മൂന്ന്: പഴയ റിട്ടേൺ ബാക്കിയുണ്ടോ എന്ന്. 3 വർഷം കഴിഞ്ഞാൽ പോർട്ടൽ എടുക്കില്ല."),
 ("V","wide","മൂന്ന് ചെക്ക്, ഒരു ടെൻഷനും ഇല്ല.")],
 "ബില്ല്, നിൽ റിട്ടേൺ,\nപഴയ ബാക്കി", CTA_ITR, theme="tip",
 cap_ml="GST റിട്ടേൺ ഫയൽ ചെയ്യും മുമ്പ് 3 ചെക്ക്: GSTR-1-ലെ ബില്ലുകൾ ശരിയാണോ (3B-യിലെ കണക്ക് അതിൽ നിന്ന്), വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ, പഴയ റിട്ടേൺ ബാക്കിയുണ്ടോ (3 വർഷം കഴിഞ്ഞാൽ പോർട്ടൽ ബ്ലോക്ക് ചെയ്യും). ഇതിൽ ഏതാണ് നിങ്ങൾ മറക്കാറുള്ളത്?",
 cap_en="Three checks before filing a GST return: are the bills in GSTR-1 right (3B takes its sales figures from it), is a nil return filed for months with no sales, and is any old return pending (the portal blocks it 3 years after its due date). Which one do you usually forget?",
 cap_mg="GST return file cheyyum mumbu 3 check: GSTR-1-ile billukal sheriyaano (3B-yile kanakku athil ninnu), vilpana illaatha maasavum nil return, pazhaya return baakkiyundo (3 varsham kazhinjaal portal block cheyyum). Ithil ethaanu ningal marakkaarullathu?")

duo("act002", "freelancer_itr", "B", "library", "പുതിയ ഇൻകം ടാക്സ് ആക്ട്:\nITR-ന് മുമ്പ്\n3 കാര്യം", [
 ("A","wide","അനൂപേ, കഴിഞ്ഞ വർഷത്തെ ITR നോക്കി ഈ വർഷവും അതേപോലെ ഫയൽ ചെയ്യാനാണോ പ്ലാൻ?"),
 ("A","A","2026 ഏപ്രിൽ മുതൽ പുതിയ ഇൻകം ടാക്സ് ആക്ട്, 2025 ആണ്. ഇനി 'ടാക്സ് ഇയർ' എന്നാണ് പറയുന്നത്."),
 ("V","V","സെക്ഷൻ നമ്പറുകളും മാറിയില്ലേ? പഴയ നമ്പർ നോക്കി ക്ലെയിം ചെയ്യരുതല്ലോ."),
 ("A","A","അതെ. പിന്നെ ഈ വർഷത്തെ ഡ്യൂ ഡേറ്റ് ടീമിനോട് ചോദിച്ച് ഉറപ്പാക്കുക."),
 ("V","wide","പുതിയ നിയമം, പഴയ കോപ്പി വേണ്ട.")],
 "പുതിയ ആക്ട്,\nപഴയ കോപ്പി വേണ്ട", CTA_ITR, theme="tip",
 cap_ml="ITR-ന് മുമ്പ് 3 കാര്യം: 2026 ഏപ്രിൽ 1 മുതൽ പുതിയ ഇൻകം ടാക്സ് ആക്ട്, 2025 ആണ്; ഇനി 'ടാക്സ് ഇയർ'; സെക്ഷൻ നമ്പറുകൾ മാറി, പഴയ നമ്പർ നോക്കി ക്ലെയിം ചെയ്യരുത്. ഡ്യൂ ഡേറ്റ് ടീമിനോട് ഉറപ്പാക്കൂ. നിങ്ങൾ കഴിഞ്ഞ വർഷത്തെ ഫോം കോപ്പി ചെയ്യാറുണ്ടോ?",
 cap_en="Three things before your ITR: the Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026; it speaks of a 'Tax Year'; and section numbers changed, so don't claim by last year's numbers. Confirm the due date with the team. Do you usually copy last year's return?",
 cap_mg="ITR-nu mumbu 3 kaaryam: 2026 April 1 muthal puthiya Income-tax Act, 2025 aanu; ini 'Tax Year'; section numbers maari, pazhaya number nokki claim cheyyaruthu. Due date team-inodu urappaakku. Ningal kazhinja varshathe form copy cheyyaarundo?")
