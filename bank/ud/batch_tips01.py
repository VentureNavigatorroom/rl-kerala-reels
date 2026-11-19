# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

lst('yt001', 'supplier_unpaid', "B", 'വലിയ ബയർ\nപണം വൈകിച്ചാൽ:\n45 ദിവസ നിയമം', [('പതിനഞ്ച് ദിവസം', 'കരാർ ഇല്ലെങ്കിൽ അതിനുള്ളിൽ പണം.'), ('നാല്പത്തിയഞ്ച് ദിവസം', 'കരാറുണ്ടെങ്കിലും പരമാവധി.'), ('വൈകിയാൽ', 'ബാങ്ക് നിരക്കിന്റെ മൂന്നിരട്ടി കൂട്ടുപലിശ.')],
 'ഉദ്യം ഉണ്ടെങ്കിൽ\nഈ സംരക്ഷണം', CTA_UDYAM, theme="tip",
 cap_ml='ഉദ്യം രജിസ്റ്റർ ചെയ്ത മൈക്രോ, സ്മോൾ നിർമ്മാണ, സർവീസ് യൂണിറ്റുകൾക്ക് ബയർ 15 ദിവസത്തിനുള്ളിൽ, കരാറുണ്ടെങ്കിൽ 45 ദിവസത്തിനുള്ളിൽ പണം നൽകണം. നിങ്ങളുടെ ബയർ എത്ര ദിവസം എടുക്കുന്നു?',
 cap_en='For Udyam-registered micro and small manufacturers and service units, buyers must pay within 15 days, or the agreed time up to 45 days, or owe compound interest. How long does your buyer take?',
 cap_mg='Udyam ulla micro, small units-nu buyer 15 divasathinullil, karaar undel 45 divasathinullil panam kodukkanam. Ningalude buyer ethra divasam edukkunnu?')

lst('yt002', 'manufacturer', "B", 'മൈക്രോയോ\nസ്മോളോ? രണ്ട്\nലിമിറ്റും നോക്കൂ', [('മൈക്രോ', 'നിക്ഷേപം രണ്ടര കോടി, ടേൺഓവർ പത്ത് കോടി വരെ.'), ('സ്മോൾ', 'നിക്ഷേപം ഇരുപത്തഞ്ച് കോടി, ടേൺഓവർ നൂറ് കോടി വരെ.'), ('ട്രിക്ക്', 'ഏതെങ്കിലും ഒന്ന് കടന്നാൽ അടുത്ത വിഭാഗം.')],
 'രണ്ടും ഒരുമിച്ച്\nനോക്കണം', CTA_MSME, theme="tip",
 cap_ml='2025 ഏപ്രിൽ മുതൽ മൈക്രോ: നിക്ഷേപം 2.5 കോടി, ടേൺഓവർ 10 കോടി വരെ. സ്മോൾ: 25 കോടി, 100 കോടി. ഒന്ന് കടന്നാൽ അടുത്ത വിഭാഗം. നിങ്ങൾ ഏതിൽ?',
 cap_en='Since April 2025, micro means investment up to 2.5 crore and turnover up to 10 crore; small means 25 crore and 100 crore. Crossing either moves you up. Which are you?',
 cap_mg='2025 April muthal micro: nikshepam 2.5 kodi, turnover 10 kodi vare. Small: 25 kodi, 100 kodi. Onnu kadannaal adutha vibhaagam. Ningal ethil?')

lst('yt003', 'trader_ud', "B", 'കച്ചവടക്കാർക്ക്\nഉദ്യം: ഒരു\nവ്യത്യാസം', [('കിട്ടും', 'റീട്ടെയിൽ, ഹോൾസെയിൽ കച്ചവടക്കാർക്കും രജിസ്റ്റർ ചെയ്യാം.'), ('ഉപയോഗം', 'മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം.'), ('ഇല്ലാത്തത്', 'നാല്പത്തിയഞ്ച് ദിവസ പേമെന്റ് സംരക്ഷണം.')],
 'കട ഉടമകൾ\nഇത് അറിയണം', CTA_UDYAM, theme="tip",
 cap_ml='റീട്ടെയിൽ, ഹോൾസെയിൽ കച്ചവടക്കാർക്ക് ഉദ്യം രജിസ്ട്രേഷൻ എടുക്കാം, പക്ഷേ മുൻഗണനാ വായ്പയ്ക്ക് മാത്രം. 45 ദിവസ പേമെന്റ് സംരക്ഷണം ഇല്ല. നിങ്ങൾ കച്ചവടക്കാരനാണോ?',
 cap_en='Retail and wholesale traders can register on Udyam, but only for priority sector lending. The 45-day payment protection does not apply. Are you a trader?',
 cap_mg='Retail, wholesale kachavadakkarkkum Udyam edukkaam, pakshe priority lending-nu maathram. 45 divasa payment samrakshanam illa. Ningal trader aano?')

