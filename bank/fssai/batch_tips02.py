# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

lst('fst004', 'cafe_owner', "B", 'FSSAI ഇല്ലാതെ\nവിറ്റാൽ എന്ത്\nസംഭവിക്കും?', [('പിഴ', 'അഞ്ച് ലക്ഷം വരെ.'), ('തടവ്', 'ആറ് മാസം വരെ.'), ('ട്രിക്ക്', 'ആദ്യ വിൽപ്പനയ്ക്ക് മുമ്പ് നമ്പർ കയ്യിൽ വേണം.')],
 'ആദ്യം നമ്പർ,\nപിന്നെ കച്ചവടം', CTA_FOOD, theme="tip",
 cap_ml='FSSAI ഇല്ലാതെ ഭക്ഷണം വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. കട തുറക്കും മുമ്പ് തന്നെ രജിസ്ട്രേഷനോ ലൈസൻസോ എടുക്കൂ. നിങ്ങളുടെ കടയ്ക്ക് നമ്പർ ഉണ്ടോ?',
 cap_en='Selling food without FSSAI can mean a penalty of up to 5 lakh and up to 6 months in prison. Get your registration or licence before the first sale. Does your shop have its number?',
 cap_mg='FSSAI illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Kada thurakkum mumpu thanne registration edukku. Ningalude kadaykku number undo?')






lst('fst010', 'spice_exporter', "B", 'കടകൾക്ക് മാത്രം\nവിൽക്കുന്നു. FSSAI\nവേണോ?', [('കടകൾക്കും ഹോട്ടലുകൾക്കും', 'വിറ്റാലും അത് ഫുഡ് ബിസിനസ് തന്നെ.'), ('ലെവൽ', 'ആകെ വർഷ വിൽപ്പന നോക്കി: ബേസിക്, സ്റ്റേറ്റ്, സെൻട്രൽ.'), ('ട്രിക്ക്', 'ബയർ ചോദിക്കും മുമ്പ് നമ്പർ റെഡിയാക്കൂ.')],
 'നേരിട്ടല്ലെങ്കിലും\nഫുഡ് ഫുഡ് തന്നെ', CTA_FSSAI, theme="tip",
 cap_ml='മസാലയോ അരിപ്പൊടിയോ കടകൾക്കും ഹോട്ടലുകൾക്കും മാത്രം വിറ്റാലും FSSAI വേണം. ആകെ വർഷ വിൽപ്പന നോക്കി ബേസിക്, സ്റ്റേറ്റ് അല്ലെങ്കിൽ സെൻട്രൽ. നിങ്ങൾ ആർക്കാണ് വിൽക്കുന്നത്?',
 cap_en='Selling spices or flour only to shops and hotels still needs FSSAI. Your total yearly sales decide basic, state or central. Who do you sell to?',
 cap_mg='Masala-yo ari-podiyo kadakalkkum hotel-ukalkkum maathram vittaalum FSSAI venam. Aake varsha vilppana nokki basic, state allel central. Ningal aarkkaanu vilkkunnathu?')

lst('fst011', 'cafe_owner', "B", 'കഫേയിൽ വാങ്ങി\nവിൽക്കുന്ന പാക്കറ്റ്:\nഒരു ചെക്ക്', [('പാക്കറ്റിൽ', 'സപ്ലയറുടെ പതിനാല് അക്ക FSSAI നമ്പർ ഉണ്ടോ?'), ('ഇല്ലെങ്കിൽ', 'ആ പാക്കറ്റ് ഷെൽഫിൽ വെക്കല്ലേ.'), ('നിങ്ങളുടേത്', 'കഫേയ്ക്കും സ്വന്തം FSSAI നമ്പർ വേണം.')],
 'സപ്ലയറുടെ നമ്പർ\nആദ്യം നോക്കൂ', CTA_FOOD, theme="tip",
 cap_ml='കഫേയിൽ വാങ്ങി വിൽക്കുന്ന പാക്കറ്റ് സ്നാക്സിൽ സപ്ലയറുടെ 14 അക്ക FSSAI നമ്പർ ഉണ്ടോ എന്ന് നോക്കൂ. കഫേയ്ക്കും സ്വന്തം FSSAI വേണം. നിങ്ങളുടെ ഷെൽഫിൽ നമ്പർ ഇല്ലാത്ത പാക്കറ്റ് ഉണ്ടോ?',
 cap_en="Selling packaged snacks in your cafe? Check that every packet carries the maker's 14-digit FSSAI number, and keep your own FSSAI for the cafe too. Any packet on your shelf without one?",
 cap_mg='Cafe-il vaangi vilkkunna packet snacks-il supplier-nte 14 akka FSSAI number undo ennu nokku. Cafe-kkum swantham FSSAI venam. Number illaatha packet undo?')
