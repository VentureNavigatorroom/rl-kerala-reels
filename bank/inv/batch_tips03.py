# Tips and tricks 03 (20 Nov, writer run 17: keep 10 unposted). theme="tip". Facts only from topics.FACTS_INV. Never investment advice or returns.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

lst('vt011', 'nri_investor', "B", 'NRI-ക്ക് ഷെയർ\nഅലോട്ട് ചെയ്തു.\nഇനി 2 ഫയലിംഗ്', [('PAS-3', 'അലോട്ട്മെന്റ് കഴിഞ്ഞ് പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ, കമ്പനി രജിസ്ട്രാർക്ക്.'), ('FC-GPR', 'റിപാട്രിയേഷൻ നിക്ഷേപമാണെങ്കിൽ മുപ്പത് ദിവസത്തിനുള്ളിൽ RBI-ക്ക്.'), ('ട്രിക്ക്', 'അലോട്ട്മെന്റ് ദിവസം തന്നെ രണ്ട് തീയതിയും കലണ്ടറിൽ ഇടൂ.')],
 'ഒരു അലോട്ട്മെന്റ്,\nരണ്ട് ഡെഡ്‌ലൈൻ', CTA_FUNDING, theme="tip",
 cap_ml='ഗൾഫിലെ ബന്ധു റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ നിക്ഷേപിച്ചാൽ ഷെയർ അലോട്ട് ചെയ്ത ദിവസം മുതൽ രണ്ട് ക്ലോക്ക് ഓടും: PAS-3 പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ, FC-GPR മുപ്പത് ദിവസത്തിനുള്ളിൽ RBI-ക്ക്. നിങ്ങളുടെ കമ്പനിയിൽ NRI നിക്ഷേപകർ ഉണ്ടോ?',
 cap_en='When an NRI invests on a repatriation basis, two clocks start on the allotment date: PAS-3 to the registrar within 15 days and the FC-GPR report to RBI within 30 days. Put both dates in the calendar the day you allot. Any NRI investors in your company?',
 cap_mg='Gulf-ile bandhu repatriation basis-il invest cheythaal share allot cheytha divasam muthal randu clock odum: PAS-3 15 divasathinullil, FC-GPR 30 divasathinullil RBI-kku. Ningalude company-il NRI investors undo?')
