# Idea validation toon 01 (28 Nov): series "വിഷ്ണുവിന്റെ ഗിഫ്റ്റ് ബോക്സ്", eps 1-4. Situation changed from the anonymised call (C29). Facts only from topics.FACTS_IDEA.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, toon, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.toon, _h.S, _h.C, _h.T, _h.topics
CTA_VALIDATE, CTA_IDEA = topics.CTA_VALIDATE, topics.CTA_IDEA
SER = "വിഷ്ണുവിന്റെ ഗിഫ്റ്റ് ബോക്സ്"

toon('ivx01', 'build_first', "B", {'A': 'വിഷ്ണു', 'B': 'അപ്പൂപ്പൻ', 'C': 'മീര'}, 'ജോലി വിട്ടു.\nആദ്യം ആപ്പ്\nഉണ്ടാക്കാം!', [('A', 'അപ്പൂപ്പാ, ജോലി വിട്ടു. ഹോം ബേക്കർമാരുടെ ഫെസ്റ്റിവൽ ഗിഫ്റ്റ് ബോക്സിന് ഒരു ആപ്പ് ഉണ്ടാക്കാൻ പോകുന്നു!'), ('C', 'ആപ്പ് ഉണ്ടാക്കിയാൽ ആളുകൾ വാങ്ങുമെന്ന് ഉറപ്പുണ്ടോ?'), ('B', 'മോനേ, ആദ്യം ആപ്പ് അല്ല. ആദ്യം പത്ത് യഥാർത്ഥ ഓർഡർ. അത് കൈകൊണ്ട് ചെയ്ത് നോക്ക്.')],
 {'title': 'ആദ്യം എന്ത്?', 'rows': [('ആപ്പ്', 'പിന്നീട്'), ('കമ്പനി', 'പിന്നീട്'), ('യഥാർത്ഥ ഓർഡർ', 'ഇപ്പോൾ')], 'total': ('ടെസ്റ്റ്', 'ആദ്യം')},
 ['പണം ചെലവാക്കും മുമ്പ് ആവശ്യക്കാർ ഉണ്ടോ എന്ന് നോക്കുക.', 'ആദ്യ ഓർഡറുകൾ കൈകൊണ്ട് ചെയ്യുക.'],
 'ആപ്പിന് മുമ്പ്\nഓർഡർ', CTA_VALIDATE, mentor="B", series=SER, ep=1, next='ഏത് ഒരൊറ്റ കാര്യത്തിൽ തുടങ്ങും?', scene='home', theme='new',
 cap_ml='പുതിയ ബിസിനസ് ഐഡിയയ്ക്ക് ആദ്യം ആപ്പല്ല, യഥാർത്ഥ ഓർഡറുകളാണ് വേണ്ടത്. ആദ്യ ഓർഡറുകൾ കൈകൊണ്ട് ചെയ്ത് ഡിമാൻഡ് ടെസ്റ്റ് ചെയ്യൂ. നിങ്ങളുടെ ഐഡിയ എന്താണ്?',
 cap_en="Vishnu quits his job to build an app for festival gift boxes from home bakers. His grandfather's advice: no app yet, get ten real orders first and handle them by hand. What's your idea?",
 cap_mg='Puthiya business idea-kku aadyam app alla, real orders aanu venddathu. Aadya orders kai kondu cheythu demand test cheyyu. Ningalude idea enthaanu?')

toon('ivx02', 'marketplace_idea', "B", {'A': 'വിഷ്ണു', 'B': 'അപ്പൂപ്പൻ', 'C': 'മീര'}, 'എല്ലാ ഉൽപ്പന്നവും\nവിൽക്കാം.\nഅവിടെയാണ് തെറ്റ്', [('A', 'കേക്ക്, ചോക്ലേറ്റ്, അച്ചാർ, കരകൗശലം. എല്ലാം ഒന്നിച്ച് തുടങ്ങിയാലോ?'), ('B', 'എല്ലാവർക്കും വേണ്ടത് ആർക്കും വേണ്ടാതാകും. ഒരു ഉൽപ്പന്നം, ഒരു കൂട്ടം കസ്റ്റമർ. അതിൽ തുടങ്ങ്.')],
 {'title': 'ഒരു നിഷ്', 'rows': [('ഉൽപ്പന്നം', 'ഒന്ന്'), ('കസ്റ്റമർ', 'ഒരു കൂട്ടം'), ('ചാനൽ', 'ഇൻസ്റ്റഗ്രാം')], 'total': ('ടെസ്റ്റ്', 'വ്യക്തം')},
 ['ആദ്യം ഒരു ഉൽപ്പന്നത്തിൽ ആവശ്യം തെളിയിക്കുക.', 'പിന്നെ മാത്രം കൂടുതൽ ചേർക്കുക.'],
 'ഒന്നിൽ ജയിച്ചിട്ട്\nപലതിലേക്ക്', CTA_VALIDATE, mentor="B", series=SER, ep=2, next='ഒരു കസ്റ്റമറെ കിട്ടാൻ എത്ര ചെലവ്?', scene='shop', theme='faq',
 cap_ml='പുതിയ മാർക്കറ്റ്പ്ലേസ് ഐഡിയ എല്ലാ ഉൽപ്പന്നവുമായി തുടങ്ങരുത്. ഒരു ഉൽപ്പന്നം, ഒരു കൂട്ടം കസ്റ്റമർ, ഒരു ചാനൽ. നിങ്ങളുടെ ആദ്യ നിഷ് ഏതാണ്?',
 cap_en="Vishnu wants to sell cakes, chocolates, pickles and crafts all at once. Start with one product, one customer group and one channel, and prove demand there first. What's your first niche?",
 cap_mg='Puthiya marketplace idea ella product-um aayi thudangaruthu. Oru product, oru koottam customer, oru channel. Ningalude aadya niche ethaanu?')

toon('ivx03', 'occasion_products', "B", {'A': 'വിഷ്ണു', 'B': 'അപ്പൂപ്പൻ', 'C': 'മീര'}, 'ഓർഡർ 20.\nലാഭമോ? കണക്ക്\nനോക്കിയില്ല', [('C', 'ഇരുപത് ഓർഡർ കിട്ടി! വിജയിച്ചില്ലേ?'), ('A', 'പരസ്യത്തിന് ചെലവാക്കിയതും ഓരോ ഓർഡറിലെ കമ്മീഷനും നോക്കിയില്ല.'), ('B', 'ഒരു കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ്, ഒരു ഓർഡറിലെ വരുമാനം, വീണ്ടും വാങ്ങുന്നവർ. ഈ മൂന്നാണ് കണക്ക്.')],
 {'title': 'ഓരോ ഓർഡറും', 'rows': [('കസ്റ്റമറെ കിട്ടാൻ ചെലവ്', 'എഴുതുക'), ('ഓർഡറിലെ വരുമാനം', 'എഴുതുക'), ('വീണ്ടും വാങ്ങിയവർ', 'എണ്ണുക')], 'total': ('ലാഭമോ നഷ്ടമോ', 'വ്യക്തം')},
 ['ഓർഡർ എണ്ണം അല്ല, ഓർഡറിലെ കണക്ക് നോക്കുക.', 'ഗിഫ്റ്റ് പോലുള്ളവയിൽ വീണ്ടും വാങ്ങുന്നവരെ ആദ്യമേ നോക്കുക.'],
 'എണ്ണം അല്ല,\nകണക്ക്', CTA_IDEA, mentor="B", series=SER, ep=3, next='കസ്റ്റമറോ സപ്ലയറോ, ഏതാണ് പ്രയാസം?', scene='teashop', theme='new',
 cap_ml='ഓർഡറുകളുടെ എണ്ണം വിജയമല്ല. ഒരു കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവും ഒരു ഓർഡറിലെ വരുമാനവും വീണ്ടും വാങ്ങുന്നവരും നോക്കണം. നിങ്ങൾ ഈ കണക്ക് എഴുതുന്നുണ്ടോ?',
 cap_en='Twenty orders feels like success, but Vishnu never compared his ad spend with the commission per order. Track what each customer costs to win, what each order earns and who buys again. Do you write these numbers down?',
 cap_mg='Orders-inte ennam vijayam alla. Oru customer-e kittaanulla chelavum oru order-ile varumaanavum veendum vaangunnavarum nokkanam. Ningal ee kanakku ezhuthunnundo?')

toon('ivx04', 'career_switch', "B", {'A': 'വിഷ്ണു', 'B': 'അപ്പൂപ്പൻ', 'C': 'മീര'}, 'ഓർഡർ കൂടി.\nഇനി കമ്പനി\nവേണോ?', [('A', 'അപ്പൂപ്പാ, ഓർഡർ കൂടി. ഇപ്പോൾ ഒരു കമ്പനി രജിസ്റ്റർ ചെയ്യണോ?'), ('B', 'ടെസ്റ്റ് ചെയ്യാൻ പ്രൊപ്രൈറ്റർഷിപ്പും ഉദ്യമും മതി. ഉദ്യം സർക്കാർ പോർട്ടലിൽ സൗജന്യമാണ്.'), ('C', 'പക്ഷേ ഇൻവെസ്റ്റർ വന്നാൽ?'), ('B', 'അപ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡ്. ബാധ്യത പരിമിതം, ഷെയർ നൽകാം.')],
 {'title': 'ഘടന ഘട്ടം ഘട്ടമായി', 'rows': [('ടെസ്റ്റ്', 'പ്രൊപ്രൈറ്റർഷിപ്പ്'), ('രജിസ്ട്രേഷൻ', 'ഉദ്യം, സൗജന്യം'), ('ഇൻവെസ്റ്റർ', 'പ്രൈവറ്റ് ലിമിറ്റഡ്')], 'total': ('ശരിയായ സമയം', 'ശരിയായ ഘടന')},
 ['പ്രൊപ്രൈറ്റർഷിപ്പിൽ വ്യക്തിയും ബിസിനസും ഒന്നാണെന്ന് ഓർക്കുക.', 'ഷെയർ നൽകും മുമ്പ് പ്രൈവറ്റ് ലിമിറ്റഡ് ആക്കുക.'],
 'ഘട്ടം അറിഞ്ഞ്\nഘടന', CTA_IDEA, mentor="B", series=SER, ep=4, next='ഇൻവെസ്റ്റർക്ക് വാല്യുവേഷൻ എങ്ങനെ?', scene='office', theme='faq',
 cap_ml='പുതിയ ബിസിനസ് ടെസ്റ്റ് ചെയ്യാൻ പ്രൊപ്രൈറ്റർഷിപ്പും സൗജന്യ ഉദ്യം രജിസ്ട്രേഷനും മതി. ഇൻവെസ്റ്റർ വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡ്. നിങ്ങൾ ഇപ്പോൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='Orders are growing and Vishnu wonders if he needs a company now. To test, a proprietorship with free Udyam registration is enough, though personal and business liability are linked; when investors come in, a private limited company gives limited liability and can issue shares. Which stage are you at?',
 cap_mg='Puthiya business test cheyyaan proprietorship-um free Udyam registration-um mathi. Investor varumbol private limited. Ningal ippol ethu ghattathilaanu?')

