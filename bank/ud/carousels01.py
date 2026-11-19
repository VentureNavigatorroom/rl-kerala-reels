# Udyam carousels seed (19 Nov). Facts only from topics.FACTS_UD; no fees; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
car("yk001", "supplier_unpaid", "45 ദിവസം", "ബയർ പണം\nവൈകിക്കുന്നോ?\nഉദ്യം ഉണ്ടെങ്കിൽ", [
 ("ആർക്ക്", "മാനുഫാക്ചറിംഗ്, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക്."),
 ("എത്ര ദിവസം", "എഗ്രിമെന്റ് ഇല്ലെങ്കിൽ 15 ദിവസം. ഉണ്ടെങ്കിലും 45 ദിവസത്തിൽ കൂടരുത്."),
 ("വൈകിയാൽ", "ബയർ RBI ബാങ്ക് റേറ്റിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ കൊടുക്കണം."),
 ("പരാതി", "MSME സമാധാൻ പോർട്ടലിൽ.")],
 "ആദ്യം ഉദ്യം,\nപിന്നെ ബിൽ", topics.CTA_UDYAM, theme="faq",
 cap_ml="ഉദ്യം ഉള്ള മാനുഫാക്ചറിംഗ്, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക് ബയർ 45 ദിവസത്തിനുള്ളിൽ പണം തരണം; വൈകിയാൽ കൂട്ടുപലിശ, പരാതി MSME സമാധാൻ പോർട്ടലിൽ.",
 cap_en="Buyer delaying payment? Udyam-registered manufacturing and service micro and small units must be paid within 15 days, or up to 45 days by agreement; after that the buyer owes compound interest at 3x the RBI bank rate. Complaints go to MSME Samadhaan.",
 cap_mg="Udyam ulla manufacturing, service micro small units-nu buyer 45 divasathinullil paisa tharanam; vaikiyaal koottupalisha, complaint MSME Samadhaan portal-il.")
car("yk002", "manufacturer", "ലിമിറ്റ്", "2025 മുതൽ\nMSME ലിമിറ്റ്\nമാറി", [
 ("മൈക്രോ", "നിക്ഷേപം 2.5 കോടി, ടേൺഓവർ 10 കോടി വരെ."),
 ("സ്മോൾ", "നിക്ഷേപം 25 കോടി, ടേൺഓവർ 100 കോടി വരെ."),
 ("മീഡിയം", "നിക്ഷേപം 125 കോടി, ടേൺഓവർ 500 കോടി വരെ."),
 ("ശ്രദ്ധിക്കൂ", "രണ്ട് ലിമിറ്റും പാലിക്കണം. ഒന്ന് കടന്നാൽ അടുത്ത കാറ്റഗറി.")],
 "നിങ്ങൾ ഏതിൽ?", topics.CTA_MSME, theme="faq",
 cap_ml="2025 ഏപ്രിൽ മുതൽ പുതിയ MSME ലിമിറ്റ്: മൈക്രോ 2.5 കോടി / 10 കോടി, സ്മോൾ 25 / 100 കോടി, മീഡിയം 125 / 500 കോടി. രണ്ടും പാലിക്കണം.",
 cap_en="New MSME limits since April 2025: micro Rs 2.5 crore investment / Rs 10 crore turnover, small Rs 25 / 100 crore, medium Rs 125 / 500 crore. Both limits must be met.",
 cap_mg="2025 April muthal puthiya MSME limit: micro 2.5 / 10 crore, small 25 / 100 crore, medium 125 / 500 crore. Randum paalikkanam.")
