# Valuation (28 Nov, from the anonymised call C29): early-stage valuation routes and refresh.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

duo('qv054', 'raising_round', 'A', 'library', 'ഇൻവെസ്റ്റർ ചർച്ചയ്ക്ക്\nഏത് വാല്യുവേഷൻ?\nരണ്ട് വഴി', [('A', 'wide', 'അനൂപേ, വരുമാനം ഇല്ലാത്ത സ്റ്റാർട്ടപ്പിന് വാല്യുവേഷൻ എങ്ങനെ?'), ('V', 'V', 'ഗ്രീഷ്മേ, പ്രൊജക്ഷൻ, മാർക്കറ്റ്, ബിസിനസ് മോഡൽ ഇവ വെച്ചാണ് ആദ്യ ഘട്ടത്തിൽ.'), ('A', 'A', 'ആര് ചെയ്യണം?'), ('V', 'V', 'ആദ്യ ചർച്ചയ്ക്ക് CA. ഷെയർ നൽകുമ്പോൾ രജിസ്റ്റേർഡ് വാല്യുവറോ മർച്ചന്റ് ബാങ്കറോ വേണ്ടിവരാം.'), ('A', 'wide', 'റിപ്പോർട്ട് കുറച്ച് മാസം കഴിഞ്ഞാൽ പുതുക്കേണ്ടിവരും.'), ('V', 'wide', 'ആവശ്യം നോക്കി വാല്യുവർ.')],
 'ആവശ്യം നോക്കി\nവാല്യുവർ', CTA_VALUATION, theme='crm',
 cap_ml='വരുമാനം ഇല്ലാത്ത സ്റ്റാർട്ടപ്പിന് പ്രൊജക്ഷനും മാർക്കറ്റും ബിസിനസ് മോഡലും വെച്ചാണ് വാല്യുവേഷൻ. ആദ്യ ചർച്ചയ്ക്ക് CA-യുടെ റിപ്പോർട്ട്, ഔദ്യോഗിക ഷെയർ നൽകലിന് രജിസ്റ്റേർഡ് വാല്യുവറോ മർച്ചന്റ് ബാങ്കറോ വേണ്ടിവരാം. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en="A startup with no revenue is valued on projections, market potential and its business model. A CA's valuation can support early investor talks, while a formal share issue may need a registered valuer or merchant banker, and reports need refreshing after a few months. Which stage are you at?",
 cap_mg='Varumaanam illaatha startup-inu projection-um market-um business model-um vechaanu valuation. Aadya charchaykku CA report, official share issue-inu registered valuer-o merchant banker-o venddi varaam. Ningal ethu ghattathilaanu?')

