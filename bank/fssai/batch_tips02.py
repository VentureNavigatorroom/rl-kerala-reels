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

lst('fst005', 'cloud_kitchen', "B", 'ഡെലിവറി ആപ്പിൽ\nലിസ്റ്റ് ചെയ്യും മുമ്പ്\n3 ചെക്ക്', [('നമ്പർ', 'ആപ്പ് ആദ്യം ചോദിക്കുന്നത് FSSAI നമ്പർ.'), ('ലെവൽ', 'വർഷം പന്ത്രണ്ട് ലക്ഷം കടക്കുമെങ്കിൽ സ്റ്റേറ്റ് ലൈസൻസ്.'), ('തീയതി', 'കാലാവധി കഴിഞ്ഞിട്ടില്ലെന്ന് ഉറപ്പാക്കൂ.')],
 'മെനു റെഡി,\nനമ്പറും റെഡിയാക്കൂ', CTA_FSSAI, theme="tip",
 cap_ml='ക്ലൗഡ് കിച്ചൺ ഡെലിവറി ആപ്പിൽ ലിസ്റ്റ് ചെയ്യും മുമ്പ്: FSSAI നമ്പർ, ശരിയായ ലെവൽ, കാലാവധി. ആപ്പ് ആദ്യം ചോദിക്കുന്നത് നമ്പർ തന്നെ. ഇതിൽ ഏതാണ് ബാക്കി?',
 cap_en='Before listing your cloud kitchen on a delivery app, check three things: the FSSAI number, the right level for your turnover, and the validity date. The app asks for the number first. Which one is pending?',
 cap_mg='Cloud kitchen delivery app-il list cheyyum mumpu: FSSAI number, sheriyaaya level, validity. App aadyam chodikkunnathu number aanu. Ithil ethaanu baakki?')

lst('fst006', 'spice_exporter', "B", 'ചെറിയ ഇറക്കുമതി.\nബേസിക് മതിയോ?\nഒരു "എന്താവും" ഉത്തരം', [('ഇറക്കുമതിക്കാർ', 'ടേൺഓവർ ചെറുതായാലും സെൻട്രൽ ലൈസൻസ്.'), ('ഇരുപത് കോടിക്ക് മുകളിൽ', 'അവിടെയും സെൻട്രൽ ലൈസൻസ്.'), ('ട്രിക്ക്', 'ആദ്യ ഷിപ്പ്മെന്റിന് മുമ്പ് ലൈസൻസ് റെഡിയാക്കൂ.')],
 'ചെറിയ കണ്ടെയ്നർ,\nസെൻട്രൽ ലൈസൻസ്', CTA_FSSAI, theme="tip",
 cap_ml='ഭക്ഷണം ഇറക്കുമതി ചെയ്യുന്നവർക്ക് ടേൺഓവർ ചെറുതായാലും FSSAI സെൻട്രൽ ലൈസൻസ് വേണം. 20 കോടിക്ക് മുകളിലുള്ളവർക്കും സെൻട്രൽ. നിങ്ങൾ ഇറക്കുമതി ചെയ്യുന്നുണ്ടോ?',
 cap_en='Food importers need an FSSAI central licence even when their turnover is small. Businesses above 20 crore need central too. Do you import any food?',
 cap_mg='Food import cheyyunnavarkku turnover cheruthaayaalum FSSAI central licence venam. 20 kodikku mukalil ullavarkkum central. Ningal import cheyyunnundo?')

lst('fst007', 'cafe_owner', "B", 'മാസ വിൽപ്പന\nഒരു ലക്ഷം കടന്നോ?\n5 സെക്കൻഡ് ചെക്ക്', [('മാസം ഒരു ലക്ഷം', 'വർഷം ഏകദേശം പന്ത്രണ്ട് ലക്ഷം: ബേസിക്കിന്റെ അതിര്.'), ('സ്ഥിരമായി കടന്നാൽ', 'സ്റ്റേറ്റ് ലൈസൻസിലേക്ക് മാറാൻ സമയമായി.'), ('ട്രിക്ക്', 'ഓരോ മാസവും ആകെ വിൽപ്പന കുറിച്ചുവെക്കൂ.')],
 'കച്ചവടം വളരുമ്പോൾ\nലൈസൻസും വളരണം', CTA_FSSAI, theme="tip",
 cap_ml='FSSAI ബേസിക് രജിസ്ട്രേഷൻ വർഷം 12 ലക്ഷം വരെ. അതായത് മാസം ഏകദേശം ഒരു ലക്ഷം. സ്ഥിരമായി അതിന് മുകളിലാണെങ്കിൽ സ്റ്റേറ്റ് ലൈസൻസ് നോക്കൂ. നിങ്ങളുടെ മാസ വിൽപ്പന എത്ര?',
 cap_en='FSSAI basic registration covers up to 12 lakh a year, roughly 1 lakh a month. If you are steadily above that, it is time for a state licence. What are your monthly sales?',
 cap_mg='FSSAI basic registration varsham 12 lakh vare, athaayathu maasam oru lakh. Sthiramaayi athinu mukalil aanel state licence nokku. Ningalude maasa vilppana ethra?')

lst('fst008', 'home_baker', "B", 'ക്രിസ്മസ് കേക്ക്\nഓർഡർ തുടങ്ങും മുമ്പ്\nഈ 3 കാര്യം', [('രജിസ്ട്രേഷൻ', 'വീട്ടിലെ ബേക്കർക്കും FSSAI ബേസിക് വേണം.'), ('കാലാവധി', 'ഡിസംബർ കഴിയും വരെ സാധുവാണോ എന്ന് നോക്കൂ.'), ('ബോക്സ്', 'പാക്ക് ചെയ്ത കേക്കിൽ പതിനാല് അക്ക നമ്പർ.')],
 'സീസൺ വരും മുമ്പ്\nപേപ്പർ റെഡി', CTA_FOOD, theme="tip",
 cap_ml='ക്രിസ്മസ് കേക്ക് ഓർഡറുകൾക്ക് മുമ്പ്: വീട്ടിലെ ബേക്കർക്കും FSSAI ബേസിക് രജിസ്ട്രേഷൻ വേണം, കാലാവധി നോക്കണം, പാക്ക് ചെയ്ത ബോക്സിൽ 14 അക്ക നമ്പർ വേണം. ഈ വർഷം എത്ര കേക്ക്?',
 cap_en='Before the Christmas cake orders start: home bakers need FSSAI basic registration too, check that it stays valid through December, and print the 14-digit number on packed boxes. How many cakes this year?',
 cap_mg='Christmas cake order-nu mumpu: veettile baker-num FSSAI basic registration venam, validity nokkanam, pack cheytha box-il 14 akka number venam. Ee varsham ethra cake?')

lst('fst009', 'packaged_food', "B", 'വലിയ ഓർഡർ\nവരുന്നു: ഒപ്പിടും\nമുമ്പ് 3 ചെക്ക്', [('ഈ ഓർഡറോടെ', 'വർഷ വിൽപ്പന പന്ത്രണ്ട് ലക്ഷം കടക്കുമോ? എങ്കിൽ സ്റ്റേറ്റ്.'), ('ലേബൽ', 'ഓരോ പാക്കറ്റിലും പതിനാല് അക്ക നമ്പർ.'), ('സമയം', 'ഡെലിവറി തീരും വരെ ലൈസൻസ് കാലാവധി ഉണ്ടോ?')],
 'ഓർഡർ വലുത്,\nതയ്യാറെടുപ്പും വലുത്', CTA_FOOD, theme="tip",
 cap_ml='ഹോട്ടലിൽ നിന്നോ സൂപ്പർമാർക്കറ്റിൽ നിന്നോ വലിയ ഓർഡർ വന്നാൽ: വിൽപ്പന 12 ലക്ഷം കടക്കുമോ, ലേബലിൽ നമ്പർ ഉണ്ടോ, ഡെലിവറി തീരും വരെ ലൈസൻസ് സാധുവാണോ എന്ന് നോക്കൂ. നിങ്ങളുടെ ഏറ്റവും വലിയ ഓർഡർ ഏത്?',
 cap_en='When a big hotel or supermarket order arrives, check three things: will it push yearly sales past 12 lakh, does every pack carry the 14-digit number, and is the licence valid until the last delivery. What is your biggest order so far?',
 cap_mg='Valiya order vannaal: vilppana 12 lakh kadakkumo, label-il number undo, delivery theerum vare licence valid aano ennu nokku. Ningalude ettavum valiya order ethu?')

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
