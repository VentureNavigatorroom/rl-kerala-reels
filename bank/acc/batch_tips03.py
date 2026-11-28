# acc tips 03 (28 Nov night): tip reel as a duo3d scene. theme="tip". Facts only from topics.FACTS_ACC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

# tip: the three GST changes since mid-2025 that small traders still miss, side by side
duo("act004", "small_trader_acc", "B", "courier", "2025-ന് ശേഷം GST-യിൽ\nമാറിയ 3 കാര്യം.\nനിങ്ങൾ അറിഞ്ഞോ?", [
 ("A","wide","അരവിന്ദേ, 2025 മുതൽ GST-യിൽ മാറിയ മൂന്ന് കാര്യം ഒറ്റ ശ്വാസത്തിൽ."),
 ("A","A","ഒന്ന്: 3B-ലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരും. തെറ്റ് കണ്ടാൽ 3B-ക്ക് മുമ്പ് GSTR-1A-യിൽ തിരുത്ത്."),
 ("V","V","രണ്ട്: 2025 ജൂലൈ മുതലുള്ള റിട്ടേൺ, ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയാൽ പോർട്ടൽ എടുക്കില്ല."),
 ("A","A","മൂന്ന്: 2025 സെപ്റ്റംബർ 22-ന് റേറ്റുകൾ മാറി. മിക്കതും 5% അല്ലെങ്കിൽ 18%, കുറച്ച് സാധനങ്ങൾക്ക് 40%."),
 ("V","wide","ലോക്ക്, 3 വർഷം, പുതിയ റേറ്റ്. പഴയ ശീലം ഇനി പോരാ.")],
 "ലോക്ക്, 3 വർഷം,\nപുതിയ റേറ്റ്", CTA_ACCOUNTS, theme="tip",
 cap_ml="2025-ന് ശേഷം GST-യിൽ മാറിയ 3 കാര്യം: 3B-ലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരും (തിരുത്ത് GSTR-1A-യിൽ, 3B-ക്ക് മുമ്പ്). 2025 ജൂലൈ മുതലുള്ള റിട്ടേൺ ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയാൽ പോർട്ടൽ എടുക്കില്ല. 2025 സെപ്റ്റംബർ 22-ന് റേറ്റുകൾ 5% / 18% ആയി, കുറച്ച് സാധനങ്ങൾക്ക് 40%. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് പുതിയത്?",
 cap_en="Three GST changes since 2025: GSTR-3B sales figures come locked from GSTR-1 (fix in GSTR-1A before 3B); from the July 2025 tax period the portal blocks a return 3 years after its due date; rates reset on 22 Sep 2025 to mostly 5% or 18%, with 40% for a few goods. Which one is new to you?",
 cap_mg="2025-nu shesham GST-yil maariya 3 kaaryam: 3B-yile vilpana kanakku GSTR-1-il ninnu lock aayi varum (thiruthu GSTR-1A-yil, 3B-kku munpu). 2025 July muthalulla return due date kazhinju 3 varsham aayaal portal edukkilla. 2025 September 22-nu rates 5% / 18% aayi, kurachu saadhanangalkku 40%. Ithil ethaanu ningalkku puthiyathu?")
