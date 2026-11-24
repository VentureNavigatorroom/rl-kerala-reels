# FSSAI batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# crm: small cold-press mill, a supermarket chain's buyer checks the label
duo("fs020", "packaged_food", "A", "shop", "സൂപ്പർമാർക്കറ്റ് ബയർ\nകുപ്പി തിരിച്ചു വെച്ചു:\n\"നമ്പർ എവിടെ?\"", [
 ("A","wide","സുരേഷേ, നമ്മുടെ മരച്ചക്ക് വെളിച്ചെണ്ണയ്ക്ക് സൂപ്പർമാർക്കറ്റിൽ നിന്ന് ഓർഡർ വന്നതാ. ബയർ കുപ്പി തിരിച്ചു വെച്ചു."),
 ("V","V","ബിനൂ, എണ്ണ നല്ലതല്ലേ? അയാൾക്ക് എന്താ പ്രശ്നം?"),
 ("A","A","എണ്ണയല്ല, ലേബൽ. ലേബലിൽ FSSAI നമ്പർ ഇല്ലെന്ന്."),
 ("V","wide","ശരിയാ. പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഫുഡിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ നിർബന്ധം. എണ്ണയും ഫുഡ് തന്നെ."),
 ("A","A","അപ്പോ കുപ്പി നന്നായാൽ പോരാ."),
 ("V","wide","എണ്ണ ചക്കിൽ, വിശ്വാസം ലേബലിൽ.")],
 "എണ്ണ ചക്കിൽ,\nവിശ്വാസം ലേബലിൽ", CTA_FSSAI, theme="crm",
 cap_ml="മരച്ചക്കിൽ ആട്ടിയ വെളിച്ചെണ്ണയ്ക്ക് സൂപ്പർമാർക്കറ്റ് ഓർഡർ വന്നു, പക്ഷേ ലേബലിൽ FSSAI നമ്പർ ഇല്ലാത്തതുകൊണ്ട് ബയർ കുപ്പി തിരിച്ചു വെച്ചു. പാക്ക് ചെയ്ത ഫുഡിന്റെ ലേബലിൽ 14 അക്ക FSSAI നമ്പർ നിർബന്ധം. നിങ്ങളുടെ ലേബലിൽ നമ്പർ ഉണ്ടോ?",
 cap_en="A small cold-press coconut oil mill got its first supermarket order, and the buyer handed the bottle back: no FSSAI number on the label. Packaged food, oil included, must carry the 14-digit FSSAI number. Is the number on your label?",
 cap_mg="Marachakkil aattiya velichennakku supermarket order vannu, pakshe label-il FSSAI number illaathathukondu buyer kuppi thirichu vechu. Pack cheytha food-inte label-il 14 akka FSSAI number nirbandham. Ningalude label-il number undo?")

# d904 pattern: wild honey collector, myth as question

# d904 pattern: houseboat cook, new angle

# d904 pattern: saree shop that also sells jackfruit jam jars

# crm: campus founders, delivery app asks for the number

# crm: small dairy's ghee wins a hotel buffet contract, outgrows basic registration

# faq: one-year registration taken last Onam

# faq: profit vs turnover

# crm: canteen contractor "starting soon", licence later
duo("fs027", "cloud_kitchen", "C", "canteen", "\"ടെൻഡർ കിട്ടിയിട്ട്\nലൈസൻസ് എടുക്കാം\"", [
 ("A","wide","അമലേ, ഐടി പാർക്കിലെ കാന്റീൻ ടെൻഡർ കിട്ടിയാൽ തിങ്കളാഴ്ച മുതൽ 600 ഊണ് ദിവസം."),
 ("V","V","ആതിരേ, FSSAI ടെൻഡർ കിട്ടിയിട്ട് എടുക്കാം. ആദ്യം പാചകം തുടങ്ങട്ടെ."),
 ("A","A","അപ്പോ ലൈസൻസ് വരുന്നത് വരെ വിൽക്കുന്ന ഊണോ?"),
 ("V","wide","ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 ("A","A","ആദ്യത്തെ ഊണിന് മുമ്പ് നമ്പർ."),
 ("V","wide","അടുപ്പ് കത്തും മുമ്പ് ലൈസൻസ് കയ്യിൽ വേണം.")],
 "അടുപ്പിന് മുമ്പ്\nലൈസൻസ്", CTA_FOOD, theme="crm",
 cap_ml="കാന്റീൻ ടെൻഡർ കിട്ടിയ ശേഷം FSSAI എടുക്കാം എന്നാണോ പ്ലാൻ? ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. ആദ്യത്തെ ഊണിന് മുമ്പ് നമ്പർ വേണം. നിങ്ങളുടെ ഓഫീസ് കാന്റീനിൽ നമ്പർ കണ്ടിട്ടുണ്ടോ?",
 cap_en="Planning to get FSSAI only after the canteen tender is won? Selling food without it can mean a penalty up to 5 lakh and up to 6 months in prison, so the number comes before the first meal is served. Seen an FSSAI number in your office canteen: yes or no?",
 cap_mg="Canteen tender kittiya shesham FSSAI edukkaam ennaano plan? Licence illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Aadyathe oonu-nu mumpu number venam. Ningalude office canteen-il number kandittundo?")

# d904 pattern: ice-candy cart, myth as question
