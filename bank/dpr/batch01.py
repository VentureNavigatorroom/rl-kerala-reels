# dpr batch 01 (28 Nov night): seed 3D reels. Facts only from topics.FACTS_DPR. No prices, no promised results.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTREPORT, CTA_DPR = topics.CTA_PROJECTREPORT, topics.CTA_DPR

duo('dpd001', 'term_loan', 'A', 'office', 'ലോൺ ചോദിച്ചു.\nബാങ്ക് പറഞ്ഞു:\nപ്രോജക്ട് റിപ്പോർട്ട്?', [('A', 'wide', 'രാഹുലേ, ബാങ്കിൽ ലോൺ ചോദിച്ചപ്പോൾ ആദ്യം പ്രോജക്ട് റിപ്പോർട്ട് കൊണ്ടുവരാൻ പറഞ്ഞു. അതെന്താ?'), ('V', 'V', 'നേഹ, നിങ്ങളുടെ ബിസിനസിന്റെ മുഴുവൻ കണക്ക് ഒരു രേഖയിൽ. ചെലവ്, ഫണ്ടിംഗ്, പ്രൊജക്ഷൻ.'), ('A', 'A', 'ബാങ്ക് പിന്നെ എന്ത് നോക്കും?'), ('V', 'V', 'പ്രധാനമായും ഒന്ന്: ഈ ബിസിനസിന് ലോൺ തിരിച്ചടയ്ക്കാൻ പറ്റുമോ എന്ന്.'), ('A', 'wide', 'ബാങ്കിന്റെ ഫോർമാറ്റ് ഉണ്ടെങ്കിൽ അത് തന്നെ ഉപയോഗിക്കണം.'), ('V', 'wide', 'ഐഡിയ അല്ല, തിരിച്ചടവ്.')],
 'ഐഡിയ അല്ല,\nതിരിച്ചടവ്', CTA_PROJECTREPORT, theme='faq',
 cap_ml='ബാങ്ക് ലോണിന് പ്രോജക്ട് റിപ്പോർട്ടിൽ പ്രോജക്ട് ചെലവ്, ഫണ്ടിംഗ്, പ്രൊജക്ഷൻ, തിരിച്ചടവ് ശേഷി എന്നിവ വേണം. ബാങ്കിന്റെയോ സ്കീമിന്റെയോ ഫോർമാറ്റ് ആദ്യം. നിങ്ങൾ ഏത് ലോണിനാണ്?',
 cap_en="The bank asked for a project report before the loan. It brings together project cost, funding, projections and, above all, whether the business can repay; the bank's or scheme's format comes first. Which loan are you applying for?",
 cap_mg='Bank loan-inu project report-il project chelavu, funding, projection, thiricchadavu sheshi venam. Bank-inte format aadyam. Ningal ethu loan-inaanu?')

duo('dpd002', 'pmegp_dpr', 'B', 'library', 'വിൽപ്പന ഇരട്ടിയാക്കി\nഎഴുതി. ബാങ്ക്\nചോദ്യം ചോദിച്ചു', [('A', 'wide', 'അനൂപേ, ലോൺ കിട്ടാൻ റിപ്പോർട്ടിൽ വിൽപ്പന കൂട്ടി എഴുതി. ബാങ്ക് ഒരുപാട് ചോദ്യം ചോദിച്ചു.'), ('V', 'V', 'ഗ്രീഷ്മേ, അമിത പ്രൊജക്ഷൻ ആണ് സാധാരണ പ്രശ്നം. ബാങ്ക് അത് പെട്ടെന്ന് കണ്ടുപിടിക്കും.'), ('A', 'A', 'പിന്നെ എങ്ങനെ എഴുതണം?'), ('V', 'V', 'മാർക്കറ്റ് പിന്തുണയ്ക്കുന്ന നമ്പർ. എല്ലാ ഭാഗത്തും ഒരേ നമ്പർ.'), ('A', 'wide', 'വർക്കിംഗ് ക്യാപിറ്റൽ വിട്ടുപോകരുത്.'), ('V', 'wide', 'വലിയ നമ്പർ അല്ല, ശരിയായ നമ്പർ.')],
 'വലിയ നമ്പർ അല്ല,\nശരിയായ നമ്പർ', CTA_DPR, theme='crm',
 cap_ml='പ്രോജക്ട് റിപ്പോർട്ടിൽ വിൽപ്പന കൂട്ടി എഴുതിയാൽ ബാങ്ക് ചോദ്യങ്ങൾ ചോദിക്കും. മാർക്കറ്റ് പിന്തുണയ്ക്കുന്ന, എല്ലാ ഭാഗത്തും ഒത്തുപോകുന്ന നമ്പറുകൾ എഴുതൂ. നിങ്ങളുടെ റിപ്പോർട്ട് ഒന്നു കൂടി നോക്കിയോ?',
 cap_en="She inflated the sales in her project report and the bank came back with questions. Use numbers the market supports, keep them consistent across every section and don't leave out working capital. Have you rechecked yours?",
 cap_mg='Project report-il vilppana koottiyezhuthiyaal bank chodyangal chodikkum. Market pinthunaykkunna, ella bhaagathum otthupokunna numbers ezhuthu. Ningalude report onnu koodi nokkiyo?')

duo('dpd003', 'expansion', 'A', 'home', 'ലോണിന്റെ\nതുക മാത്രം\nചോദിച്ചാൽ പോരാ', [('A', 'wide', 'അരുണേ, കട വലുതാക്കാൻ ലോൺ വേണം. തുക പറഞ്ഞാൽ മതിയോ?'), ('V', 'V', 'സ്നേഹേ, പോരാ. ആ പണം എന്തിനൊക്കെ എന്ന് പ്രോജക്ട് ചെലവിൽ കാണിക്കണം.'), ('A', 'A', 'പിന്നെ?'), ('V', 'V', 'എത്ര സ്വന്തം പണം, എത്ര ലോൺ എന്ന് ഫണ്ടിംഗ് പ്ലാൻ. സ്റ്റോക്കിനുള്ള വർക്കിംഗ് ക്യാപിറ്റലും.'), ('A', 'wide', 'ഇതെല്ലാം ഒത്തുവന്നാലേ ബാങ്കിന് വ്യക്തമാകൂ.'), ('V', 'wide', 'തുക അല്ല, പ്ലാൻ.')],
 'തുക അല്ല,\nപ്ലാൻ', CTA_PROJECTREPORT, theme='new',
 cap_ml='ബിസിനസ് വലുതാക്കാൻ ലോൺ ചോദിക്കുമ്പോൾ തുക മാത്രം പോരാ: പ്രോജക്ട് ചെലവ്, സ്വന്തം പങ്കും ലോണും, വർക്കിംഗ് ക്യാപിറ്റൽ എന്നിവ റിപ്പോർട്ടിൽ വേണം. നിങ്ങൾ എന്തിനാണ് ലോൺ എടുക്കുന്നത്?',
 cap_en="Asking for an expansion loan? The amount alone isn't enough: show the project cost, how much is your own money and how much is loan, and the working capital. What is the loan for?",
 cap_mg='Business valuthaakkaan loan chodikkumbol thuka maathram poraa: project chelavu, swantham pankum loan-um, working capital report-il venam. Ningal enthinaanu loan edukkunnathu?')

