# IEC batch 08 (28 Nov night): fresh situations only (topic facts are nearly used up, so 3 scripts, not 8).
# Personal use vs selling to friends, the "IEC pays you" myth, a bank asking for the IEC before an import advance. Facts only from topics.FACTS_IEC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

# FAQ: one keyboard for himself, nine sold to gamer friends with a small margin
duo('ied062', 'importer', 'B', 'cafe', 'ഒന്ന് എനിക്ക്,\nഒമ്പത് ഫ്രണ്ട്സിന്.\n"ഇത് കച്ചവടമല്ലല്ലോ"', [
 ('A', 'wide', 'റോഷനേ, ജപ്പാനിൽ നിന്ന് 10 ഗെയിമിംഗ് കീബോർഡ് വരുത്തുന്നു. ഒന്ന് എനിക്ക്, ഒമ്പത് ഫ്രണ്ട്സിന്. IEC വേണ്ടല്ലോ?'),
 ('V', 'V', 'ആൽവിനേ, ഫ്രണ്ട്സ് അതിന് പണം തരുമോ?'),
 ('A', 'A', 'പിന്നല്ലാതെ. ചെറിയൊരു ലാഭവും വെക്കും.'),
 ('V', 'V', 'എങ്കിൽ ആ ഒമ്പതെണ്ണം കച്ചവടമാ. സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്കേ IEC വേണ്ടാത്തതുള്ളൂ. വിൽക്കാനുള്ളതിന് കസ്റ്റംസ് IEC ചോദിക്കും.'),
 ('A', 'wide', 'അപ്പോ ഫ്രണ്ട്സ് ആണെങ്കിലും കച്ചവടം കച്ചവടം തന്നെ.'),
 ('V', 'wide', 'ലാഭം വെച്ചാൽ ഫ്രണ്ടും കസ്റ്റമർ.')],
 'ലാഭം വെച്ചാൽ\nഫ്രണ്ടും കസ്റ്റമർ', CTA_IEC, theme='faq',
 cap_ml='സ്വന്തം ഉപയോഗത്തിനുള്ള ഇറക്കുമതിക്ക് IEC വേണ്ട. പക്ഷേ കൂട്ടുകാർക്ക് ലാഭം വെച്ച് വിൽക്കാനാണ് വരുത്തുന്നതെങ്കിൽ അത് കച്ചവടത്തിനുള്ള ഇറക്കുമതിയാണ്; കസ്റ്റംസ് IEC ചോദിക്കും. നിങ്ങൾ വിദേശത്ത് നിന്ന് എന്താണ് വരുത്തുന്നത്?',
 cap_en='No IEC is needed for an import meant for your own use. But if you bring in ten gaming keyboards and sell nine to friends at a small margin, that part is a trade import and customs will ask for the IEC. What do you import from abroad?',
 cap_mg='Swantham upayogathinulla import-inu IEC venda. Pakshe friends-inu laabham vechu vilkkaan aanu varuthunnathenkil athu kachavadathinulla import aanu; customs IEC chodikkum. Ningal videshathu ninnu enthaanu varuthunnathu?')

# FAQ: a retired couple heard that taking an IEC brings government money
duo('ied063', 'handicraft_export', 'A', 'veranda', '"IEC എടുത്താൽ\nസർക്കാർ കാശ്\nതരും"', [
 ('A', 'wide', 'ബാലേട്ടാ, നമ്മുടെ ചകിരി കരകൗശലത്തിന് IEC എടുക്കാമെന്ന് പറഞ്ഞത് സർക്കാർ കാശ് തരുമെന്ന് കേട്ടിട്ടാണോ?'),
 ('V', 'V', 'അതേ ശാന്തേ. പഞ്ചായത്തിലെ ഒരാൾ പറഞ്ഞു, IEC കിട്ടിയാൽ എന്തെങ്കിലും വരുമെന്ന്.'),
 ('A', 'A', 'IEC ഒരു സ്കീമല്ല. DGFT തരുന്ന 10 അക്ക കോഡാണ്, നമ്മുടെ ബിസിനസിന്റെ PAN-മായി ബന്ധിപ്പിച്ചത്.'),
 ('V', 'V', 'പിന്നെ അതുകൊണ്ട് എന്താ ഗുണം?'),
 ('A', 'wide', 'സാധനം കയറ്റി അയക്കുമ്പോൾ കസ്റ്റംസും ബാങ്കും അത് ചോദിക്കും. കോഡ് ഇല്ലെങ്കിൽ കയറ്റുമതി അവിടെ നിൽക്കും.'),
 ('V', 'wide', 'കാശ് തരുന്ന പെട്ടിയല്ല, വാതിൽ തുറക്കുന്ന താക്കോൽ.')],
 'IEC കാശല്ല,\nവാതിലിന്റെ താക്കോൽ', CTA_IEC, theme='faq',
 cap_ml='IEC എടുത്താൽ സർക്കാർ പണം തരുമെന്ന് പലരും കരുതുന്നു. IEC ഒരു സ്കീമല്ല; DGFT തരുന്ന, ബിസിനസിന്റെ PAN-മായി ബന്ധിപ്പിച്ച 10 അക്ക കോഡാണ്. സാധനം കയറ്റി അയക്കുമ്പോൾ കസ്റ്റംസും ബാങ്കും അത് ചോദിക്കും. ഈ മിഥ്യ നിങ്ങളും കേട്ടിട്ടുണ്ടോ?',
 cap_en='Many people think the government pays you once you take an IEC. It does not: the IEC is a 10-digit code from DGFT linked to the business PAN, and customs and banks ask for it when you ship goods. Without it, the export stops. Have you heard this myth too?',
 cap_mg='IEC eduthaal sarkkar panam tharum ennu palarum karuthunnu. IEC oru scheme alla; DGFT tharunna, business PAN-umaayi bandhippicha 10 akka code aanu. Saadhanam kayatti ayakkumbol customs-um bank-um athu chodikkum. Ee mithya ningalum kettittundo?')

# NEW: the bank asks for the IEC before an advance to a Belgian chocolate supplier
duo('ied064', 'importer', 'B', 'foodcourt', 'ബെൽജിയം സപ്ലയർക്ക്\nഅഡ്വാൻസ് അയക്കാൻ\nബാങ്ക്: "IEC?"', [
 ('A', 'wide', 'ഡെന്നിസേ, ചോക്ലേറ്റ് സപ്ലയർക്ക് അഡ്വാൻസ് അയച്ചോ? അടുത്ത മാസമാ ഡെസേർട്ട് മേള.'),
 ('V', 'V', 'മരിയാ, ബാങ്ക് ഫോം തിരിച്ചു തന്നു. ഒരു കോളം കാലി: IEC നമ്പർ.'),
 ('A', 'A', 'സാധനം തുറമുഖത്ത് എത്തുമ്പോഴല്ലേ കോഡ് ഒക്കെ ചോദിക്കുന്നത്?'),
 ('V', 'V', 'അല്ല. കച്ചവടത്തിനുള്ള ഇറക്കുമതിക്ക് കസ്റ്റംസ് മാത്രമല്ല, ബാങ്കും IEC ചോദിക്കും. പണം അയക്കുന്നിടത്ത് തന്നെ.'),
 ('A', 'wide', 'അപ്പോ ആദ്യം കോഡ്, പിന്നെ അഡ്വാൻസ്, പിന്നെ ചോക്ലേറ്റ്.'),
 ('V', 'wide', 'പണം പോകും മുമ്പ് കോഡ് വേണം.')],
 'പണം പോകും മുമ്പ്\nകോഡ് വേണം', CTA_IEC, theme='new',
 cap_ml='വിദേശ സപ്ലയർക്ക് അഡ്വാൻസ് അയക്കാൻ പോലും ബാങ്ക് IEC ചോദിക്കാം. കച്ചവടത്തിനുള്ള ഇറക്കുമതിക്ക് കസ്റ്റംസും ബാങ്കും IEC ചോദിക്കും; സാധനം എത്തും വരെ കാത്തിരിക്കേണ്ട. നിങ്ങളുടെ ആദ്യ ഇറക്കുമതി ഏതാണ്?',
 cap_en='A dessert counter wanted to pay a Belgian chocolate supplier in advance, and the bank form came back with one empty box: the IEC number. For imports made for trade, both customs and banks ask for the IEC, so get it before the money leaves. What is your first import?',
 cap_mg='Videsha supplier-inu advance ayakkaan polum bank IEC chodikkaam. Kachavadathinulla import-inu customs-um bank-um IEC chodikkum; saadhanam ethum vare kaathirikkenda. Ningalude aadya import ethaanu?')
