# deck batch 01 (28 Nov night): seed 3D reels. Facts only from topics.FACTS_DECK. No prices, no promised results.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PITCHDECK, CTA_DECK = topics.CTA_PITCHDECK, topics.CTA_DECK

duo('dkd001', 'first_raise_deck', 'A', 'rooftop', '40 സ്ലൈഡ്.\nഇൻവെസ്റ്റർ\nമറുപടി തന്നില്ല', [('A', 'wide', 'ശ്യാമേ, നാൽപ്പത് സ്ലൈഡുള്ള ഡെക്ക് അയച്ചു. ഇൻവെസ്റ്റർ മറുപടി തന്നില്ല.'), ('V', 'V', 'ആര്യേ, മീറ്റിംഗിന് മുമ്പ് ഇൻവെസ്റ്റർ ഡെക്ക് വായിക്കും. കഥ കുറച്ച് സ്ലൈഡിൽ വ്യക്തമാകണം.'), ('A', 'A', 'എന്തൊക്കെ വേണം?'), ('V', 'V', 'പ്രശ്നം, പരിഹാരം, മാർക്കറ്റ്, ട്രാക്ഷൻ, ബിസിനസ് മോഡൽ, ടീം, എത്ര വേണം, എന്തിന്.'), ('A', 'wide', 'ബാക്കി വിശദാംശം ഡാറ്റ റൂമിൽ.'), ('V', 'wide', 'കൂടുതൽ സ്ലൈഡ് അല്ല, വ്യക്തമായ കഥ.')],
 'കൂടുതൽ സ്ലൈഡ് അല്ല,\nവ്യക്തമായ കഥ', CTA_PITCHDECK, theme='crm',
 cap_ml='ഇൻവെസ്റ്റർ പിച്ച് ഡെക്ക് നീളം കൂടിയാൽ വായിക്കില്ല. പ്രശ്നം, പരിഹാരം, മാർക്കറ്റ്, ട്രാക്ഷൻ, ബിസിനസ് മോഡൽ, ടീം, ആവശ്യപ്പെടുന്നതും അതിന്റെ ഉപയോഗവും. നിങ്ങളുടെ ഡെക്കിൽ എത്ര സ്ലൈഡ്?',
 cap_en='He sent a forty-slide deck and the investor never replied. Investors often read the deck before meeting you, so tell the story in a few slides: problem, solution, market, traction, model, team and the ask. How many slides is yours?',
 cap_mg='Investor pitch deck neelam koodiyaal vaayikkilla. Problem, solution, market, traction, business model, team, the ask. Ningalude deck-il ethra slide?')

duo('dkd002', 'demo_day', 'B', 'classroom', 'ഡെമോ ഡേയിൽ\nഇൻവെസ്റ്റർ ഡെക്ക്\nകൊണ്ടുപോയി', [('A', 'wide', 'ആദർശേ, ഡെമോ ഡേയിൽ മുഴുവൻ ഇൻവെസ്റ്റർ ഡെക്കും കാണിച്ചു. സമയം തീർന്നു, പകുതി പോലും എത്തിയില്ല.'), ('V', 'V', 'നിമ്മീ, ഓരോ മുറിക്കും വേറെ ഡെക്ക്. ഡെമോ ഡേയ്ക്ക് കുറച്ച് സ്ലൈഡ് മാത്രം.'), ('A', 'A', 'ഗ്രാന്റ് അപേക്ഷയ്ക്ക്?'), ('V', 'V', 'ഐഡിയ, ഘട്ടം, ടീം, പണം എങ്ങനെ ഉപയോഗിക്കും. ബാങ്കിന് തിരിച്ചടവ്.'), ('A', 'wide', 'ക്ലയന്റിന് അവരുടെ പ്രശ്നവും നിങ്ങളുടെ തെളിവും.'), ('V', 'wide', 'മുറി നോക്കി ഡെക്ക്.')],
 'മുറി നോക്കി\nഡെക്ക്', CTA_DECK, theme='faq',
 cap_ml='എല്ലാ ആവശ്യത്തിനും ഒരേ പിച്ച് ഡെക്ക് പോരാ: ഇൻവെസ്റ്റർ ഡെക്ക്, ഡെമോ ഡേ ഡെക്ക്, ഗ്രാന്റ് ഡെക്ക്, ബാങ്ക് ഡെക്ക്, സെയിൽസ് ഡെക്ക്, വൺ പേജർ. നിങ്ങൾ ഏതാണ് തയ്യാറാക്കുന്നത്?',
 cap_en='She used her full investor deck at a timed demo day and ran out of time halfway. Each room needs its own deck: investor, demo day, grant, bank, sales, plus a one-pager. Which one are you preparing?',
 cap_mg='Ella aavashyathinum ore pitch deck poraa: investor deck, demo day deck, grant deck, bank deck, sales deck, one-pager. Ningal ethaanu ready aakkunnathu?')

duo('dkd003', 'first_raise_deck', 'A', 'beach', 'ഡെക്കിൽ ഒരു നമ്പർ.\nപ്രൊജക്ഷനിൽ\nവേറൊന്ന്', [('A', 'wide', 'നിഖിലേ, ഡെക്കിൽ ഒരു വരുമാന നമ്പർ, പ്രൊജക്ഷനിൽ വേറൊന്ന്. ഇൻവെസ്റ്റർ അത് കണ്ടുപിടിച്ചു.'), ('V', 'V', 'ദിവ്യേ, ഡെക്ക്, പ്രൊജക്ഷൻ, ഡാറ്റ റൂം. മൂന്നിലും ഒരേ നമ്പർ വേണം.'), ('A', 'A', 'ട്രാക്ഷൻ കുറച്ച് കൂട്ടിക്കാണിച്ചാലോ?'), ('V', 'V', 'കൂട്ടിക്കാണിച്ച ട്രാക്ഷൻ വിശ്വാസം കളയും. ചെറുതാണെങ്കിലും സത്യം പറയുക.'), ('A', 'wide', 'ഡ്യൂ ഡിലിജൻസിൽ എല്ലാം പരിശോധിക്കും.'), ('V', 'wide', 'ഒരു കമ്പനി, ഒരു നമ്പർ.')],
 'ഒരു കമ്പനി,\nഒരു നമ്പർ', CTA_PITCHDECK, theme='new',
 cap_ml='പിച്ച് ഡെക്കിലെ നമ്പറുകൾ പ്രൊജക്ഷനുമായും ഡാറ്റ റൂമുമായും ഒത്തുപോകണം. കൂട്ടിക്കാണിച്ച ട്രാക്ഷൻ വിശ്വാസം കളയും. നിങ്ങളുടെ നമ്പറുകൾ ഒത്തുപോകുന്നുണ്ടോ?',
 cap_en="The revenue in his deck didn't match his projections, and the investor noticed. Deck, projections and data room must show the same numbers; inflated traction loses trust. Do yours match?",
 cap_mg='Pitch deck-ile numbers projection-umaayum data room-umaayum otthupokanam. Koottikkaanicha traction vishwaasam kalayum. Ningalude numbers otthupokunnundo?')

