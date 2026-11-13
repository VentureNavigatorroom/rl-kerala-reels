# Script bank, batch 15. New situations: a tapioca farmer offered a three-year buy-back by a Salem starch factory, a bakery whose
# egg puffs a multiplex wants at every interval, a tea-shop masala-chai premix a Gulf importer wants 20% of, a saree shop dressing a
# film song from a building owned by an uncle in Mumbai, a dosa counter for five malls whose legal team asks about INC-20A, a fish-
# pickle maker supplying a cruise line under a "Kerala Pickles" name; a Jeddah couple who both want to be the only directors, a Dubai
# interior designer with 12 Kochi villas from January, a Dubai kids'-store manager naming her Kerala brand after her employer's, a man
# flying to Muscat for the first time who thinks he must resign as director, a mother whose Kuwait son "cannot hold shares", a Doha
# sister whose brother's fish ponds earn nothing yet; a nail artist three bridal showrooms want, a tailor with 120 carol costumes and
# an OPC 12 days old, a Braille printer who wants "Braille Bank", a crochet maker building stock for a year with no sales, an abacus
# teacher called "Smart Kids", a bridal make-up artist at day 168 in wedding season, an astrophotographer in a rented rooftop room.
# Same fact list and no-price rule as batch01. Segments proprietor 7, nri 6, solo 7; 16 duo3d in 16 different locations (none used in
# batch14), default names. Proprietor scripts again open on money waiting on the table (the d401 pattern); share kept at 7/40.
# Every script carries cap_ml / cap_en / cap_mg (captions.py adds hook, CTA and hashtags).
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS

S = []
def duo(id, segment, bucket, scene, hook, lines, end, cta, names=None, sound=None, **kw):
    d = dict(id=id, kind="duo3d", scene=scene, names=names, segment=segment, bucket=bucket, hook=hook, lines=lines, end=end, cta=cta, **kw)
    if sound: d["sound"] = sound
    S.append(d)
def chat(id, segment, bucket, hook, names, lines, end, cta, **kw): S.append(dict(id=id, kind="chat", segment=segment, bucket=bucket, hook=hook, names=names, lines=lines, end=end, cta=cta, **kw))
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))

# ---------------- proprietor ----------------
# farm: Vasu + Gopi. A Salem starch factory will buy all of Gopi's tapioca for three years, but signs only with a company next month.
duo("d1701", "proprietor", "A", "farm", "തമിഴ്നാട്ടിലെ സ്റ്റാർച്ച് ഫാക്ടറി:\n\"മൂന്ന് വർഷം നിങ്ങളുടെ\nകപ്പ മുഴുവൻ ഞങ്ങൾക്ക്\"", [
 ("V","wide","വാസുവേട്ടാ, സേലത്ത് നിന്ന് ആ സ്റ്റാർച്ച് ഫാക്ടറിക്കാർ വീണ്ടും വന്നു."),
 ("A","A","ഗോപീ, കഴിഞ്ഞ തവണ വെറുതെ വന്ന് ചായ കുടിച്ച് പോയവരല്ലേ?"),
 ("V","V","ഇത്തവണ അങ്ങനെ അല്ല. മൂന്ന് വർഷം നമ്മുടെ പത്തേക്കറിലെ കപ്പ മുഴുവൻ അവർ എടുക്കും. എഴുതിയ കരാർ."),
 ("A","wide","ദൈവമേ! ഇനി ചന്തയിൽ കപ്പയുമായി കാത്തിരിക്കണ്ട!"),
 ("V","V","പക്ഷേ ഒരു കണ്ടീഷൻ. കരാർ കമ്പനിയുമായി മാത്രം. അടുത്ത മാസം ഒന്നാം തീയതി ഒപ്പിടാൻ വരും."),
 ("A","A","കമ്പനിക്ക് രണ്ട് ഡയറക്ടർ വേണം. നീയും ഞാനും. ചേട്ടനും അനിയനും."),
 ("V","V","എത്ര ദിവസം എടുക്കും?"),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. നാളെ തന്നെ ഡോക്യുമെന്റ്സ് എടുക്ക്."),
 ("V","wide","ശരി. കപ്പ പറിക്കും മുമ്പ് പേപ്പർ റെഡി!")],
 "വലിയ കരാറിന് മുമ്പ്\nകമ്പനി റെഡി", CTA_DOCS,
 cap_ml="പത്തേക്കർ കപ്പ കൃഷി ചെയ്യുന്ന സഹോദരന്മാർക്ക് സേലത്തെ സ്റ്റാർച്ച് ഫാക്ടറിയുടെ മൂന്ന് വർഷത്തെ ബൈ-ബാക്ക് കരാർ, കമ്പനിയുമായി മാത്രം. രണ്ടുപേരും ഡയറക്ടർമാരായി Pvt Ltd; രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="Two farmer brothers in Kerala are offered a three-year buy-back for their tapioca by a starch factory, which signs only with a company next month. They can be the two directors of a private limited company; registration usually takes 7-15 working days.",
 cap_mg="10 acre kappa krishi cheyyunna brothers-nu Salem starch factory-yude 3 varsha buy-back contract, company-yumaayi maathram. Randuperum director aayi Pvt Ltd; register cheyyan saadharana 7-15 working days.")

# bakery: Jisha + Sabu. A multiplex wants Sabu's egg puffs at every interval on four screens; he thinks a company needs 10 lakh first.
duo("d1702", "proprietor", "A", "bakery", "മൾട്ടിപ്ലക്സിലെ നാല് സ്ക്രീനിലും\nഇന്റർവെല്ലിന് നമ്മുടെ പഫ്സ്!", [
 ("V","wide","ജിഷേ, ആ മൾട്ടിപ്ലക്സിന്റെ മാനേജർ വന്നിരുന്നു. ഇന്റർവെല്ലിന് നമ്മുടെ മുട്ട പഫ്സ് വേണമെന്ന്!"),
 ("A","A","സാബുച്ചേട്ടാ, നാല് സ്ക്രീൻ, ദിവസം പതിനാറ് ഷോ. ഓവൻ ഇനി ഉറങ്ങില്ല!"),
 ("V","V","പക്ഷേ വെണ്ടർ ആകാൻ കമ്പനി വേണം. കമ്പനിക്ക് പത്ത് ലക്ഷം ക്യാപിറ്റൽ ബാങ്കിൽ കാണിക്കണ്ടേ?"),
 ("A","wide","വേണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇപ്പോൾ ഇല്ല."),
 ("V","V","അപ്പോ പിന്നെ എന്താ വേണ്ടത്?"),
 ("A","A","രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും. ചേട്ടനും ഞാനും. പിന്നെ ബേക്കറിയുടെ അഡ്രസ്സിന്റെ പേപ്പറും."),
 ("V","V","പത്ത് ലക്ഷം കൂട്ടാൻ ഒരു വർഷം കാത്തിരിക്കാൻ ആയിരുന്നു എന്റെ പ്ലാൻ."),
 ("A","wide","ഒരു വർഷം കാത്തിരുന്നാൽ സിനിമ മാത്രമല്ല, ഇന്റർവെല്ലും തീരും!")],
 "വലിയ ഓർഡറിന്\nവലിയ ക്യാപിറ്റൽ വേണ്ട", CTA_START,
 cap_ml="ബേക്കറിയിലെ മുട്ട പഫ്സ് മൾട്ടിപ്ലക്സിലെ നാല് സ്ക്രീനിലും വേണം, വെണ്ടർ കമ്പനി ആയിരിക്കണം. പത്ത് ലക്ഷം ക്യാപിറ്റൽ കാണിക്കണം എന്ന് കരുതി കാത്തിരിക്കണ്ട; പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല.",
 cap_en="A Kerala bakery is asked to supply egg puffs to a four-screen multiplex, which only works with company vendors. The owner thought he needed 10 lakh in the bank first, but a private limited company has no minimum paid-up capital.",
 cap_mg="Bakery-yile mutta puffs multiplex-ile 4 screen-ilum venam, vendor company aayirikkanam. 10 lakh capital kaanikkanam ennu karuthi kaathirikkanda; Pvt Ltd-nu minimum paid-up capital illa.")

# teashop: Anu + Vishnu. A Gulf food importer wants Vishnu's masala-chai premix for supermarkets and 20% for funding a packing unit.
duo("d1703", "proprietor", "B", "teashop", "ചായക്കടയിലെ മസാല ചായപ്പൊടി.\nഗൾഫിലെ ഇംപോർട്ടർ:\n\"20% ഷെയർ തരാമോ?\"", [
 ("A","wide","വിഷ്ണൂ, ആ സൂട്ടിട്ട ആൾ ഇന്ന് മൂന്നാമത്തെ ചായയാ കുടിക്കുന്നത്."),
 ("V","V","അനു, പുള്ളി ഗൾഫിലെ ഫുഡ് ഇംപോർട്ടർ. നമ്മുടെ മസാല ചായപ്പൊടി അവിടത്തെ സൂപ്പർമാർക്കറ്റുകളിൽ വേണമെന്ന്."),
 ("A","A","നമ്മുടെ ഏലക്കയും ഇഞ്ചിയും ഇനി വിമാനത്തിൽ!"),
 ("V","V","പാക്കിംഗ് യൂണിറ്റിന് പുള്ളി പൈസ ഇടും. പകരം ഇരുപത് ശതമാനം ഷെയർ. നമ്മൾ ഇപ്പോഴും വെറും ചായക്കടയാണല്ലോ."),
 ("A","wide","ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിന് അത് പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി. പിന്നെ ഷെയർ."),
 ("A","A","അതേ. കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ. നീയും ഞാനും. ഇംപോർട്ടർ ഷെയർഹോൾഡർ."),
 ("V","wide","എന്നാ ആദ്യത്തെ ബോർഡ് മീറ്റിംഗ് ഈ ബെഞ്ചിൽ. മിനിറ്റ്സിനൊപ്പം പരിപ്പുവടയും!")],
 "ഷെയർ ചോദിച്ച് ആള് വന്നോ?\nആദ്യം കമ്പനി", CTA_START,
 cap_ml="ചായക്കടയിലെ മസാല ചായപ്പൊടി ഗൾഫിലെ സൂപ്പർമാർക്കറ്റുകളിൽ എത്തിക്കാൻ ഒരു ഇംപോർട്ടർ പൈസ ഇടാം, പകരം 20% ഷെയർ. പ്രൊപ്രൈറ്റർഷിപ്പിന് ഷെയർ കൊടുക്കാൻ പറ്റില്ല; ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി, 2 ഡയറക്ടർ.",
 cap_en="A Kerala tea shop's masala-chai premix catches a Gulf importer's eye, and he offers to fund a packing unit for 20% of the business. A proprietorship cannot issue shares; register a private limited company with two directors first.",
 cap_mg="Chaayakkadayile masala chaayappodi Gulf supermarket-il ethikkan oru importer paisa idaam, pakaram 20% share. Proprietorship-nu share kodukkan pattilla; aadyam Pvt Ltd company, 2 director.")

# textile: Ramya + Prakash. A film's costume team wants 300 kasavu sets for a song; the shop, the planned office, is in an uncle's building.
duo("d1704", "proprietor", "C", "textile", "സിനിമയിലെ പാട്ടിന് 300 കസവ്.\nകമ്പനി ഓഫീസ് ആകേണ്ട കട\nമാമന്റെ ബിൽഡിംഗിൽ", [
 ("A","wide","പ്രകാശേട്ടാ, ആ സിനിമയുടെ കോസ്റ്റ്യൂം ടീം പോയോ? എന്ത് പറഞ്ഞു?"),
 ("V","V","രമ്യേ, ഒരു പാട്ടിന് മുന്നൂറ് കസവ് സെറ്റ്. പിന്നെ അവരുടെ അടുത്ത പടങ്ങൾക്കും നമ്മൾ തന്നെ സപ്ലൈ."),
 ("A","A","നമ്മുടെ കസവ് സ്ക്രീനിൽ! പക്ഷേ ബില്ല് കമ്പനി പേരിൽ വേണമെന്നല്ലേ പറഞ്ഞത്?"),
 ("V","V","അതേ. കമ്പനി ഓഫീസ് നമ്മുടെ കട തന്നെ. പതിനഞ്ച് വർഷമായി ഇവിടെ അല്ലേ."),
 ("A","wide","കട മാമന്റെ ബിൽഡിംഗിലാണ്. ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC വേണം. പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും."),
 ("V","V","മാമൻ മുംബൈയിൽ. ഫോൺ എടുക്കുന്നത് ഞായറാഴ്ച മാത്രം."),
 ("A","A","എങ്കിൽ ഈ ഞായറാഴ്ച തന്നെ വിളിക്ക്. NOC ഒപ്പിട്ട് അയക്കാൻ പറ."),
 ("V","wide","ശരി. മാമന് സിനിമ ഇഷ്ടമാ. പാട്ടിന്റെ കാര്യം പറഞ്ഞാൽ ഉടൻ ഒപ്പിടും!")],
 "കട വാടകയ്ക്കാണോ?\nഉടമയുടെ NOC റെഡിയാക്കൂ", CTA_DOCS,
 cap_ml="സാരിക്കടയ്ക്ക് സിനിമയിലെ പാട്ടിന് 300 കസവ് സെറ്റിന്റെ ഓർഡർ, ബില്ല് കമ്പനി പേരിൽ വേണം. കട മാമന്റെ ബിൽഡിംഗിൽ ആയതുകൊണ്ട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം.",
 cap_en="A Kerala saree shop wins an order for 300 kasavu sets for a film song, and the producers want company invoices. The shop sits in an uncle's building, so registering it as the company's office needs the owner's NOC and a recent utility bill.",
 cap_mg="Saree kadaykku cinema paattinu 300 kasavu set order, bill company peril venam. Kada maamante building-il aayathukondu registered office aakkan owner-nte NOC-um puthiya utility bill-um venam.")

# foodcourt: Maria + Dennis. A mall group wants their dosa counter in five malls; its legal team asks whether INC-20A is filed (company is five months old).
duo("d1705", "proprietor", "B", "foodcourt", "അഞ്ച് മാളിലും നമ്മുടെ\nദോശ കൗണ്ടർ. ലീഗൽ ടീം\nചോദിച്ചു: \"INC-20A?\"", [
 ("A","wide","ഡെന്നിസേ, മാൾ ഗ്രൂപ്പിന്റെ മെയിൽ വന്നു! അഞ്ച് മാളിലും നമ്മുടെ ദോശ കൗണ്ടർ!"),
 ("V","V","മരിയാ, അതിനാണല്ലോ അഞ്ച് മാസം മുമ്പ് കമ്പനി ആക്കിയത്. ഇനി ഒപ്പിട്ടാൽ മതി."),
 ("A","A","മെയിലിൽ ഒരു ചോദ്യം കൂടി. കമ്പനിയുടെ INC-20A ഫയൽ ചെയ്തോ എന്ന്."),
 ("V","V","അതെന്താ? ദോശയുടെ പുതിയ മാവോ?"),
 ("A","wide","ബിസിനസ് തുടങ്ങി എന്ന് കാണിക്കുന്ന ഫോം. കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("V","V","അഞ്ച് മാസം. അപ്പോ ഏകദേശം നൂറ്റമ്പത് ദിവസം. ഇനി മുപ്പത് ദിവസം മാത്രം!"),
 ("A","A","മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. നമുക്ക് രണ്ടുപേർക്കും ദിവസം ആയിരം രൂപ വേറെ."),
 ("V","wide","ഈ ആഴ്ച തന്നെ ഫയൽ ചെയ്യാം. എന്നിട്ട് അഞ്ച് മാളിലും ദോശ ചുടാം!")],
 "വലിയ കരാറിന് മുമ്പ്\nINC-20A ചെക്ക്", CTA_AFTER,
 cap_ml="അഞ്ച് മാളുകളിൽ ദോശ കൗണ്ടർ തുടങ്ങാൻ കരാർ റെഡി, പക്ഷേ മാൾ ഗ്രൂപ്പിന്റെ ലീഗൽ ടീം INC-20A ചോദിച്ചു. കമ്പനി രജിസ്റ്റർ ചെയ്ത് 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം; വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപ.",
 cap_en="A couple's dosa counter is about to sign with a mall group for five malls, and the group's legal team asks if INC-20A is filed. The commencement of business form is due within 180 days of incorporation; missing it means 50,000 on the company and 1,000 a day per director in default.",
 cap_mg="5 mall-il dosa counter thudangan contract ready, pakshe mall group-nte legal team INC-20A chodichu. Company register cheythu 180 days-inullil file cheyyanam; vaikiyal company-kku 50,000 pizha, oro director-kkum divasam 1,000.")

# chat: Shiny + her son Albin. A cruise-line supplier wants 2,000 jars of fish pickle a month, contract only with a company; she picks "Kerala Pickles".
chat("c991", "proprietor", "A", "ക്രൂയിസ് കപ്പലിലേക്ക്\nമാസം 2,000 ജാർ മീൻ അച്ചാർ", ("ഷൈനി", "ആൽബിൻ"), [
 (0,"ആൽബിനേ, ആ ക്രൂയിസ് കപ്പലിന്റെ സപ്ലയർ വിളിച്ചു. മാസം രണ്ടായിരം ജാർ മീൻ അച്ചാർ വേണം!"),
 (1,"മമ്മീ! നമ്മുടെ അടുക്കളയിലെ അച്ചാർ ഇനി കടലിന് നടുവിൽ!"),
 (0,"പക്ഷേ കമ്പനിയുമായി മാത്രം കരാർ. പേര് ഞാൻ തീരുമാനിച്ചു: കേരള പിക്കിൾസ്."),
 (1,"മമ്മീ, അത് ഇതിനകം പലരും ഇട്ടിട്ടുണ്ടാകും. നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 (0,"എങ്കിൽ എന്റെ പേര് ചേർത്താലോ?"),
 (1,"അതാ നല്ലത്. മമ്മിയുടെ പേരോ നമ്മുടെ വീട്ടുപേരോ ചേർത്ത് വേറിട്ട മൂന്ന് പേര് എഴുതാം."),
 (0,"വീട്ടുപേര് കടവിൽ. കടവിൽ ഫിഷ് പിക്കിൾസ്. കടലിനും ചേരും!"),
 (1,"സൂപ്പർ. ബാക്കപ്പിന് രണ്ട് പേര് കൂടി. പിന്നെ ആദ്യത്തെ ജാർ എനിക്ക്!")],
 "എല്ലാവരും ഇട്ട പേര്\nനിങ്ങൾക്ക് വേണ്ട", CTA_NAME,
 cap_ml="വീട്ടിൽ മീൻ അച്ചാർ ഉണ്ടാക്കുന്ന അമ്മയ്ക്ക് ക്രൂയിസ് കപ്പലിലേക്ക് മാസം 2,000 ജാറിന്റെ ഓർഡർ, കരാർ കമ്പനിയുമായി മാത്രം. 'കേരള പിക്കിൾസ്' പോലുള്ള പേര് നിലവിലുള്ള കമ്പനികളോട് സാമ്യം വന്ന് റിജക്ട് ആകാം; വീട്ടുപേര് ചേർത്ത് വേറിട്ട പേരുകൾ കരുതൂ.",
 cap_en="A home fish-pickle maker in Kerala is offered a 2,000-jar monthly order for a cruise line, contract only with a company. Common names like 'Kerala Pickles' may be similar to existing companies and get rejected, so build a distinctive company name, maybe from your family name.",
 cap_mg="Veettil meen achaar undaakkunna ammaykku cruise kappalilekku maasam 2,000 jar order, contract company-yumaayi maathram. 'Kerala Pickles' pole common name reject aakaam; veettuperu cherthu vere company names karuthu.")

lst("l991", "proprietor", "B", "കടയിൽ ഷെയർ ചോദിച്ച്\nആരെങ്കിലും വന്നാൽ\nആദ്യം 3 കാര്യം", [
 ("ഷെയർ കൊടുക്കാൻ കമ്പനി വേണം", "പ്രൊപ്രൈറ്റർഷിപ്പ്, പാർട്ണർഷിപ്പ്, LLP: ഇവയിൽ ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പറ്റില്ല."),
 ("കുറഞ്ഞത് രണ്ടുപേർ", "Pvt Ltd-ന് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ."),
 ("പൈസ വരും മുമ്പേ തുടങ്ങാം", "മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല. ഇൻവെസ്റ്റർ വരും മുമ്പ് കമ്പനി റെഡിയാക്കാം.")],
 "ഷെയർ ചോദിച്ചാൽ\nസ്ട്രക്ചർ ആദ്യം", CTA_START,
 cap_ml="നിങ്ങളുടെ കടയിലോ ചെറിയ ബിസിനസിലോ ആരെങ്കിലും പൈസ ഇട്ട് ഷെയർ ചോദിക്കുന്നുണ്ടോ? പ്രൊപ്രൈറ്റർഷിപ്പിനും പാർട്ണർഷിപ്പിനും LLP-ക്കും ഷെയർ കൊടുക്കാൻ പറ്റില്ല; 2 ഡയറക്ടറുള്ള Pvt Ltd കമ്പനി വേണം, മിനിമം ക്യാപിറ്റൽ ഇല്ല.",
 cap_en="Someone wants to invest in your shop in exchange for shares? A proprietorship, partnership or LLP cannot take equity investment. You need a private limited company with two directors and two shareholders, and there is no minimum capital to wait for.",
 cap_mg="Ningalude kadayilo business-ilo aarenkilum paisa ittu share chodikkunnundo? Proprietorship-inum partnership-inum LLP-kkum share kodukkan pattilla; 2 director ulla Pvt Ltd company venam, minimum capital illa.")

# ---------------- nri ----------------
# gulf: Shiju + Faisal. Faisal and his wife, both in Jeddah, plan an AC-service company in Malappuram with themselves as the only directors.
duo("d1706", "nri", "A", "gulf", "ഭാര്യയും ഞാനും ജിദ്ദയിൽ.\nരണ്ടുപേരും ഡയറക്ടർ.\nനാട്ടിൽ ആരുമില്ല", [
 ("V","wide","ഷിജുവേട്ടാ, മലപ്പുറത്ത് എസി സർവീസ് കമ്പനി. ഫോമെല്ലാം റെഡി. ഞാനും ഭാര്യയും ഡയറക്ടർമാർ."),
 ("A","A","ഫൈസലേ, നിങ്ങൾ രണ്ടുപേരും ജിദ്ദയിൽ അല്ലേ?"),
 ("V","V","അതേ. NRI-ക്ക് ഡയറക്ടർ ആകാമെന്ന് കഴിഞ്ഞ മാസം നിങ്ങൾ തന്നെ പറഞ്ഞില്ലേ."),
 ("A","wide","ആകാം. പക്ഷേ ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. രണ്ടുപേരും ഇവിടെ ആയാൽ പോരാ."),
 ("V","V","അയ്യോ. ആ വരി ഞാൻ വായിച്ചില്ല."),
 ("A","A","നാട്ടിൽ ആരുണ്ട്? ബിസിനസ് നോക്കാൻ പറ്റുന്ന ഒരാൾ."),
 ("V","V","ഉപ്പ. റിട്ടയർ ആയിട്ട് ദിവസവും എസി മെക്കാനിക്കുകളോട് തർക്കിക്കുന്ന ആളാ."),
 ("A","wide","എങ്കിൽ ഉപ്പ തന്നെ നാട്ടിലെ ഡയറക്ടർ. തർക്കം ഇനി ഒഫീഷ്യൽ!")],
 "എല്ലാ ഡയറക്ടറും വിദേശത്തോ?\nഒരാൾ നാട്ടിൽ വേണം", CTA_START,
 cap_ml="ജിദ്ദയിലുള്ള ദമ്പതികൾ മലപ്പുറത്ത് എസി സർവീസ് കമ്പനി തുടങ്ങുന്നു, രണ്ടുപേരും മാത്രം ഡയറക്ടർമാർ. NRI-ക്ക് ഡയറക്ടർ ആകാം, പക്ഷേ ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം; നാട്ടിലുള്ള ഉപ്പ മൂന്നാമത്തെ ഡയറക്ടർ.",
 cap_en="An NRI couple in Jeddah plans an AC-service company in Malappuram with only the two of them as directors. NRIs can be directors of an Indian Pvt Ltd, but at least one director must be resident in India, so a parent at home can join the board.",
 cap_mg="Jeddah-yil ulla couple Malappuram-il AC service company thudangunnu, randuperum maathram director. NRI-kku director aakaam, pakshe oru director enkilum India-yil thaamasikkunna aal aakanam; naattilulla uppa director.")

# gulfoffice: Shahana + Asif. Shahana, a Dubai interior designer, has a Kochi builder's 12 villas from January but no company yet.
duo("d1707", "nri", "B", "gulfoffice", "ദുബായിൽ ഇന്റീരിയർ ഡിസൈനർ.\nകൊച്ചിയിലെ ബിൽഡർ:\n\"ജനുവരി മുതൽ 12 വില്ല\"", [
 ("V","wide","ഷഹാനാ, മൂഡ്ബോർഡ് മാറ്റി വെക്ക്. കൊച്ചിയിലെ ആ ബിൽഡറുടെ മെയിൽ വായിച്ചോ?"),
 ("A","A","ആസിഫേ, വായിച്ചു. ജനുവരി മുതൽ പന്ത്രണ്ട് വില്ലയുടെ ഇന്റീരിയർ. നാട്ടിലെ എന്റെ കമ്പനിയുമായി കരാർ."),
 ("V","V","നാട്ടിൽ കമ്പനി എവിടെ? ഇതുവരെ ഇൻസ്റ്റ പേജ് മാത്രം അല്ലേ?"),
 ("A","A","അതാ. ഡിസംബറിൽ ലീവിന് നാട്ടിൽ ചെന്നിട്ട് രജിസ്റ്റർ ചെയ്യാം എന്ന് കരുതി."),
 ("V","wide","ലീവ് വരെ കാക്കണ്ട. NRI-ക്കും ഡയറക്ടർ ആകാം. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം."),
 ("V","V","നാട്ടിൽ താമസിക്കുന്ന ഒരു ഡയറക്ടർ കൂടി വേണം. നിന്റെ ആങ്ങള?"),
 ("A","A","ആങ്ങള ആർക്കിടെക്റ്റ് ആണ്. ബിൽഡർക്കും അവനെ അറിയാം. ഇന്ന് തന്നെ ഡോക്യുമെന്റ്സ് ലിസ്റ്റ് അയക്കാം."),
 ("V","wide","ജനുവരിയിൽ വില്ല. ഡിസംബറിൽ കമ്പനി റെഡി!")],
 "ലീവ് വരെ കാക്കണ്ട.\nകമ്പനി ഇപ്പോൾ", CTA_DOCS,
 cap_ml="ദുബായിലെ ഇന്റീരിയർ ഡിസൈനർക്ക് കൊച്ചിയിലെ ബിൽഡറുടെ 12 വില്ലകളുടെ ഓർഡർ, നാട്ടിലെ കമ്പനിയുമായി കരാർ. ലീവിന് വരും വരെ കാക്കണ്ട; NRI-ക്കും ഡയറക്ടർ ആകാം, നാട്ടിലുള്ള സഹോദരൻ രണ്ടാമത്തെ ഡയറക്ടർ, Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7-15 പ്രവൃത്തി ദിവസം.",
 cap_en="A Dubai-based interior designer has a Kochi builder's order for 12 villas from January, contract with her Kerala company, which doesn't exist yet. NRIs can be directors; with her brother at home as the resident director, a Pvt Ltd usually takes 7-15 working days, no need to wait for leave.",
 cap_mg="Dubai-yile interior designer-nu Kochi builder-nte 12 villa order, naattile company-yumaayi contract. Leave-nu varum vare kaakkanda; NRI-kkum director aakaam, naattilulla aangala randamathe director, Pvt Ltd register cheyyan 7-15 working days.")

# mall: Sumayya + Jafar. Sumayya manages a kids'-clothing store in a Dubai mall and wants her Kerala brand named almost like that store.
duo("d1708", "nri", "C", "mall", "ദുബായ് മാളിൽ കിഡ്സ് സ്റ്റോർ മാനേജർ.\nനാട്ടിലെ ബ്രാൻഡിന്\nഅതേ സ്റ്റോറിന്റെ ഛായ", [
 ("V","wide","സുമയ്യാ, ഷിഫ്റ്റ് കഴിഞ്ഞിട്ടും ഈ കുട്ടിയുടുപ്പിന്റെ റാക്കിന്റെ മുന്നിൽ?"),
 ("A","A","ജാഫറിക്കാ, കോഴിക്കോട് അനിയത്തിയുമായി കുട്ടികളുടെ ഉടുപ്പിന് സ്വന്തം ബ്രാൻഡ് തുടങ്ങുന്നു."),
 ("V","V","ആഹാ! പേര് ഇട്ടോ?"),
 ("A","A","ഈ സ്റ്റോറിന്റെ പേരിനോട് ഏതാണ്ട് സാമ്യമുള്ള പേര്. അമ്മമാർക്ക് പെട്ടെന്ന് പരിചയം തോന്നും."),
 ("V","wide","പരിചയം തോന്നുന്നതാ പ്രശ്നം. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്നതോ നിലവിലുള്ള പേരിനോട് സാമ്യമുള്ളതോ ആയ പേര് റിജക്ട് ആകാം."),
 ("V","V","പിന്നെ നിന്റെ മാനേജ്മെന്റ് ഇത് കണ്ടാൽ അടുത്ത അപ്രൈസൽ എന്താകും?"),
 ("A","A","അയ്യോ. അത് ഞാൻ ഓർത്തില്ല."),
 ("V","wide","സ്വന്തം പേര് ഉണ്ടാക്ക്. മൂന്നെണ്ണം. ആരുടെയും നിഴൽ ഇല്ലാതെ."),
 ("A","wide","ശരി. കുഞ്ഞുടുപ്പ്. മലയാളം, ക്യൂട്ട്, ആരുടേതുമല്ല!")],
 "അറിയാവുന്ന പേരിന്റെ\nഛായ വേണ്ട", CTA_NAME,
 cap_ml="ദുബായ് മാളിലെ കിഡ്സ് സ്റ്റോർ മാനേജർ കോഴിക്കോട് സ്വന്തം ബ്രാൻഡ് തുടങ്ങുന്നു, പേര് ജോലി ചെയ്യുന്ന സ്റ്റോറിന്റേത് പോലെ. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്നതോ നിലവിലുള്ള പേരിനോട് സാമ്യമുള്ളതോ ആയ കമ്പനി പേര് റിജക്ട് ആകാം.",
 cap_en="An NRI store manager in a Dubai mall launches her own kids'-clothing brand in Kozhikode with a name close to her employer's store. Company names that clash with a trademark or resemble an existing company can be rejected; build a name of your own.",
 cap_mg="Dubai mall-ile kids store manager Kozhikode swantham brand thudangunnu, peru joli cheyyunna store-nte pole. Trademark clash aakunnatho existing perinodu saamyam ullatho aaya company name reject aakaam.")

# airport: Shameer + Rafeeq. Rafeeq flies to Muscat for his first Gulf job and thinks he must resign as director of his fish-drying company.
duo("d1709", "nri", "A", "airport", "ആദ്യമായി ഗൾഫിലേക്ക്.\n\"കമ്പനിയിൽ നിന്ന്\nഡയറക്ടർ സ്ഥാനം ഒഴിയണം\"", [
 ("A","wide","റഫീഖേ, ബോർഡിംഗ് പാസ് കയ്യിൽ ഉണ്ടല്ലോ. എന്താ ഇത്ര ടെൻഷൻ?"),
 ("V","V","ഷമീറിക്കാ, മസ്കറ്റിൽ ജോലി കിട്ടി പോകുവാ. പക്ഷേ നാട്ടിലെ മീൻ ഉണക്കൽ കമ്പനിയിൽ നിന്ന് ഡയറക്ടർ സ്ഥാനം ഒഴിയണം."),
 ("A","A","ആര് പറഞ്ഞു ഒഴിയണം എന്ന്?"),
 ("V","V","നാട്ടുകാർ. ഗൾഫിൽ പോയാൽ ഇന്ത്യൻ കമ്പനിയിൽ ഡയറക്ടർ ആകാൻ പറ്റില്ലെന്ന്."),
 ("A","wide","തെറ്റാണ്. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("A","A","ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. നിന്റെ ഭാര്യ നാട്ടിൽ ഉണ്ടല്ലോ."),
 ("V","V","അവളാ ശരിക്കും കമ്പനി നടത്തുന്നത്. ഞാൻ പേരിന് മാത്രം ബോസ്."),
 ("A","wide","എങ്കിൽ ഒന്നും മാറുന്നില്ല. നീ മസ്കറ്റിൽ, ബോസ് നാട്ടിൽ!")],
 "ഗൾഫിലേക്ക് പോകുന്നോ?\nഡയറക്ടർ ആയി തുടരാം", CTA_START,
 cap_ml="ആദ്യമായി മസ്കറ്റിലേക്ക് ജോലിക്ക് പോകുന്ന റഫീഖ് കരുതി, നാട്ടിലെ കമ്പനിയിൽ നിന്ന് ഡയറക്ടർ സ്ഥാനം ഒഴിയണമെന്ന്. NRI-ക്കും ഇന്ത്യൻ Pvt Ltd കമ്പനിയിൽ ഡയറക്ടർ ആയി തുടരാം; നാട്ടിലുള്ള ഭാര്യ ഇന്ത്യയിൽ താമസിക്കുന്ന ഡയറക്ടർ.",
 cap_en="Leaving Kerala for his first Gulf job in Muscat, a young founder thinks he must resign as director of his fish-drying company. NRIs can stay directors of an Indian private limited company, as long as one director, here his wife, lives in India.",
 cap_mg="Aadyamaayi Muscat-ilekku jolikku pokunna aal karuthi, naattile company-yil ninnu director sthaanam ozhiyanam ennu. NRI-kkum Indian Pvt Ltd-il director aayi thudaraam; naattilulla bharya resident director.")

# veranda: Shantha + Balan. Shantha, sixty, registers her coconut-oil mill; Balan says their son in Kuwait cannot hold shares.
duo("d1710", "nri", "B", "veranda", "അമ്മയുടെ വെളിച്ചെണ്ണ മിൽ.\nകുവൈത്തിലെ മകന്\nഷെയർ കൊടുക്കാമോ?", [
 ("A","wide","ബാലേട്ടാ, പത്രം മാറ്റി വെക്ക്. എന്റെ വെളിച്ചെണ്ണ മില്ലിന് കമ്പനി രജിസ്റ്റർ ചെയ്യാൻ പോകുവാ."),
 ("V","V","ശാന്തേ, അറുപതാം വയസ്സിൽ കമ്പനി! ആരൊക്കെയാ കൂടെ?"),
 ("A","A","ഞാനും ഏട്ടനും ഡയറക്ടർ. പിന്നെ കുവൈത്തിലുള്ള നമ്മുടെ മോന് ഷെയർ. അവനാണല്ലോ മെഷീന് പൈസ അയക്കുന്നത്."),
 ("V","wide","മോന് ഷെയർ പറ്റില്ല. അവൻ NRI അല്ലേ. ബാങ്കിലെ മാനേജർ അങ്ങനെ എന്തോ പറഞ്ഞിരുന്നു."),
 ("A","A","മാനേജർ എന്തോ പറഞ്ഞു, ഏട്ടൻ ബാക്കി ഊഹിച്ചു. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡർ ആകാം. ഡയറക്ടറും ആകാം."),
 ("V","V","എങ്കിൽ എന്റെ ഊഹം പിൻവലിച്ചു."),
 ("A","wide","നമ്മൾ രണ്ടുപേരും നാട്ടിൽ ഉണ്ടല്ലോ. ഇന്ത്യയിൽ താമസിക്കുന്ന ഡയറക്ടർ വേണം എന്നതും ശരിയായി."),
 ("V","wide","ശരി. ആദ്യത്തെ കുപ്പി എണ്ണ കുവൈത്തിലേക്ക്. ഷെയർഹോൾഡർക്ക് സാമ്പിൾ!")],
 "മക്കൾ വിദേശത്താണോ?\nഷെയർഹോൾഡർ ആകാം", CTA_START,
 cap_ml="അറുപതാം വയസ്സിൽ വെളിച്ചെണ്ണ മില്ല് കമ്പനി ആക്കുന്ന അമ്മ, മെഷീന് പൈസ അയക്കുന്നത് കുവൈത്തിലുള്ള മകൻ. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം; നാട്ടിലുള്ള അച്ഛനും അമ്മയും ഡയറക്ടർമാർ.",
 cap_en="A 60-year-old mother in Kerala registers her coconut-oil mill as a company, funded by her son in Kuwait. Her husband thought an NRI can't hold shares, but NRIs can be shareholders and directors of an Indian private limited company.",
 cap_mg="60-aam vayassil velichenna mill company aakkunna amma, machine-nu paisa ayakkunnathu Kuwait-il ulla makan. NRI-kkum Indian Pvt Ltd-il shareholder-um director-um aakaam; naattilulla achanum ammayum director.")

# chat: Shabna (Doha) + her brother Irfan. Their fish-farm company is a year old; ponds are dug, no fish sold, so Irfan thinks no filing.
chat("c992", "nri", "C", "ദോഹയിൽ നിന്ന് പൈസ.\nനാട്ടിൽ മീൻ കുളം.\nമീനില്ല, ഫയലിംഗും വേണ്ട?", ("ഷബ്ന", "ഇർഫാൻ"), [
 (1,"ഇത്താ, കുളം കുഴിക്കൽ കഴിഞ്ഞു! മീൻ കുഞ്ഞുങ്ങൾ മാർച്ചിൽ വരും."),
 (0,"സൂപ്പർ! കമ്പനി ആയിട്ട് ഇപ്പോ ഒരു വർഷം ആകുന്നു. ആനുവൽ ഫയലിംഗ് നോക്കിയോ?"),
 (1,"ഫയലിംഗോ? ഒരു മീൻ പോലും വിറ്റില്ല. വരുമാനം പൂജ്യം. അപ്പോ ഒന്നും ചെയ്യണ്ടല്ലോ."),
 (0,"അങ്ങനെ അല്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 (0,"വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. ഞാൻ അയക്കുന്ന പൈസ കുളത്തിലേക്കാ, പിഴയിലേക്കല്ല."),
 (1,"ശരി ഇത്താ. നാളെ തന്നെ ഓഡിറ്ററെ കാണാം."),
 (0,"ഗുഡ്. മീൻ വരും മുമ്പ് പേപ്പർ ശരിയാകട്ടെ."),
 (1,"ആദ്യത്തെ കരിമീൻ ദോഹയിലേക്ക്. പാഴ്സൽ ആയി!")],
 "വരുമാനം പൂജ്യം.\nഫയലിംഗ് നിർബന്ധം", CTA_AFTER,
 cap_ml="ദോഹയിലുള്ള സഹോദരി പൈസ അയക്കുന്നു, നാട്ടിലെ മീൻ വളർത്തൽ കമ്പനിക്ക് ഒരു വർഷമായി, ഇതുവരെ വിൽപ്പന ഇല്ല. വരുമാനം പൂജ്യം ആയാലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="An NRI sister in Doha funds her brother's fish-farm company in Kerala; a year in, the ponds are dug but nothing is sold. Annual ROC filing is still due with zero revenue, and each late form costs 100 a day.",
 cap_mg="Doha-yil ulla sister paisa ayakkunnu, naattile fish farm company-kku oru varsham, ithuvare sales illa. Varumanam zero aayaalum annual filing cheyyanam; vaikiyal oro form-inum divasam 100 pizha.")

# ---------------- solo ----------------
# salon: Sonia + Vineeth. A bridal-store chain wants Sonia's nail bar in three showrooms, contract with a company; she has no partner.
duo("d1711", "solo", "A", "salon", "ബ്രൈഡൽ സ്റ്റോർ ചെയിൻ:\n\"മൂന്ന് ഷോറൂമിലും\nനിങ്ങളുടെ നെയിൽ ബാർ\"", [
 ("V","wide","സോണിയ ചേച്ചീ, ആ ബ്രൈഡൽ ഷോറൂമിലെ മാഡം എന്ത് പറഞ്ഞു?"),
 ("A","A","വിനീതേ, അവരുടെ മൂന്ന് ഷോറൂമിലും കല്യാണപ്പെണ്ണുങ്ങൾക്ക് എന്റെ നെയിൽ ബാർ വേണമെന്ന്!"),
 ("V","V","സൂപ്പർ! പിന്നെന്താ മുഖം വാടിയത്?"),
 ("A","A","കരാർ കമ്പനിയുമായി മാത്രം. കമ്പനി തുടങ്ങാൻ രണ്ടുപേർ വേണം. എനിക്ക് പാർട്ണർ ഇല്ല."),
 ("V","wide","ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി, OPC തുടങ്ങാം. പാർട്ണറെ തേടി നടക്കണ്ട."),
 ("A","A","ഞാൻ തന്നെ ഡയറക്ടർ, ഞാൻ തന്നെ നെയിൽ ആർട്ടിസ്റ്റ്?"),
 ("V","V","അതെ. പിന്നെ ആദ്യത്തെ ഓഡിറ്റർ മുപ്പത് ദിവസത്തിനുള്ളിൽ. അതും ഓർത്തോ."),
 ("A","wide","ശരി. ഇനി എന്റെ നഖം പോലും ഒഫീഷ്യൽ!")],
 "പാർട്ണർ ഇല്ലേ?\nOPC തുടങ്ങാം", CTA_START,
 cap_ml="ഒറ്റയ്ക്ക് ജോലി ചെയ്യുന്ന നെയിൽ ആർട്ടിസ്റ്റിനെ മൂന്ന് ബ്രൈഡൽ ഷോറൂമുകൾ വിളിക്കുന്നു, കരാർ കമ്പനിയുമായി മാത്രം. പാർട്ണർ ഇല്ലെങ്കിലും വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം; ആദ്യ ഓഡിറ്റർ 30 ദിവസത്തിനുള്ളിൽ.",
 cap_en="A solo nail artist in Kerala is invited to run nail bars in three bridal showrooms, but they contract only with companies. You don't need a partner: a One Person Company (OPC) works, with the first auditor appointed within 30 days.",
 cap_mg="Ottaykku joli cheyyunna nail artist-ne 3 bridal showroom vilikkunnu, contract company-yumaayi maathram. Partner illenkilum One Person Company (OPC) thudangaam; first auditor 30 days-inullil.")

# tailor: Usha + Mohanan. Mohanan's OPC is 12 days old; four schools want 120 carol costumes and he plans the auditor "after Christmas".
duo("d1712", "solo", "B", "tailor", "നാല് സ്കൂളിന് കരോൾ കോസ്റ്റ്യൂം.\nOPC ആയിട്ട് 12 ദിവസം", [
 ("A","wide","മോഹനേട്ടാ, ഈ ചുവന്ന തുണി മുഴുവൻ സാന്താക്ലോസിനാണോ?"),
 ("V","V","ഉഷേ, നാല് സ്കൂളിന്റെ കരോളിന് നൂറ്റിയിരുപത് സാന്താ കോസ്റ്റ്യൂം. OPC ആയതിന്റെ ആദ്യ ഓർഡർ!"),
 ("A","A","കൊള്ളാം. കമ്പനി ആയിട്ട് എത്ര ദിവസമായി? ഓഡിറ്ററെ വെച്ചോ?"),
 ("V","V","പന്ത്രണ്ട് ദിവസം. ഓഡിറ്റർ ക്രിസ്മസ് കഴിഞ്ഞ് നോക്കാം. ഇപ്പോ സൂചിയും നൂലും മാത്രം."),
 ("A","wide","ക്രിസ്മസ് കഴിഞ്ഞാൽ വൈകും. കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ വെക്കണം."),
 ("V","V","പന്ത്രണ്ട് പോയി. ഇനി പതിനെട്ട് ദിവസം. സാന്തയുടെ താടിയേക്കാൾ വേഗം പോകും."),
 ("A","A","നാളെ ഉച്ചയ്ക്ക് കട അടച്ച് ടൗണിലെ ഓഡിറ്ററെ കാണ്. ബാക്കി തയ്യൽ ഞാൻ നോക്കാം."),
 ("V","wide","ശരി. ഇത്തവണ സാന്തയുടെ സമ്മാനം എനിക്ക് തന്നെ. സമാധാനം!")],
 "ഓർഡർ തിരക്കിലും\nഓഡിറ്റർ 30 ദിവസത്തിൽ", CTA_AFTER,
 cap_ml="തയ്യൽക്കടക്കാരന്റെ OPC-ക്ക് 12 ദിവസം, നാല് സ്കൂളുകളുടെ ക്രിസ്മസ് കരോൾ കോസ്റ്റ്യൂം ഓർഡർ. ഓഡിറ്റർ ക്രിസ്മസ് കഴിഞ്ഞ് പോരാ; കമ്പനി രജിസ്റ്റർ ചെയ്ത് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A tailor's One Person Company is 12 days old and swamped with carol costumes for four schools. The first auditor can't wait for Christmas: it must be appointed within 30 days of incorporation.",
 cap_mg="Thayyal kadakkaarante OPC-kku 12 divasam, 4 school-nte Christmas carol costume order. Auditor Christmas kazhinju pora; company register cheythu 30 days-inullil first auditor-ne niyamikkanam.")

# photocopy: Aswathy + Unni. Aswathy prints Braille notes alone; a trust wants them for 15 schools a year; she wants "Braille Bank".
duo("d1713", "solo", "C", "photocopy", "അന്ധരായ കുട്ടികൾക്ക് ബ്രെയിൽ നോട്ട്സ്.\nകമ്പനി പേര്: \"ബ്രെയിൽ ബാങ്ക്\"", [
 ("V","wide","അശ്വതീ, ഈ കുത്തുകൾ മാത്രമുള്ള പേജുകൾ എല്ലാം ആർക്കാ?"),
 ("A","A","ഉണ്ണീ, കാഴ്ചയില്ലാത്ത കുട്ടികൾക്ക് ബ്രെയിൽ നോട്ട്സ്. ഒരു ട്രസ്റ്റ് പറഞ്ഞു, എല്ലാ വർഷവും പതിനഞ്ച് സ്കൂളിന് വേണം."),
 ("V","V","അടിപൊളി! ഒറ്റയ്ക്കാണല്ലോ, OPC ആക്കാം. പേര്?"),
 ("A","A","ബ്രെയിൽ ബാങ്ക്. ബുക്ക് ബാങ്ക് പോലെ. എല്ലാവർക്കും പെട്ടെന്ന് മനസ്സിലാകും."),
 ("V","wide","മനസ്സിലാകും. പക്ഷേ ബാങ്ക്, ഇൻഷുറൻസ് പോലുള്ള വാക്കുകൾ കമ്പനി പേരിൽ നിയന്ത്രിതമാണ്. അതുകൊണ്ട് റിജക്ട് ആകാം."),
 ("A","A","അയ്യോ. ഈ ബാങ്കിൽ പൈസ ഇല്ല, പുസ്തകം മാത്രമേ ഉള്ളൂ!"),
 ("V","V","അത് പേര് നോക്കുന്നവർക്ക് അറിയില്ലല്ലോ. ബാങ്ക് ഇല്ലാത്ത മൂന്ന് പേര് എഴുത്."),
 ("A","wide","എങ്കിൽ തൊട്ടറിവ്. തൊട്ടു വായിക്കുന്ന അറിവ്!")],
 "ചില വാക്കുകൾ\nപേരിൽ പാടില്ല", CTA_NAME,
 cap_ml="കാഴ്ചയില്ലാത്ത കുട്ടികൾക്ക് ബ്രെയിൽ നോട്ട്സ് പ്രിന്റ് ചെയ്യുന്ന അശ്വതിക്ക് OPC-ക്ക് 'ബ്രെയിൽ ബാങ്ക്' എന്ന് പേര് വേണം. ബാങ്ക്, ഇൻഷുറൻസ് പോലുള്ള നിയന്ത്രിത വാക്കുകളുള്ള കമ്പനി പേര് റിജക്ട് ആകാം; വേറെ മൂന്ന് പേര് കരുതൂ.",
 cap_en="A solo Braille printer gets a yearly order for 15 schools and wants to name her One Person Company 'Braille Bank'. Restricted words like Bank or Insurance can get a company name rejected, so keep three other names ready.",
 cap_mg="Kaazhchayillatha kuttikalkku Braille notes print cheyyunna aalkku OPC-kku 'Braille Bank' ennu peru venam. Bank, Insurance pole restricted words ulla company name reject aakaam; vere 3 names karuthu.")

# balcony: Ammu + Vivek. Ammu spent the year making 300 crochet toys for a January launch; zero sales, so she thinks no annual filing.
duo("d1714", "solo", "A", "balcony", "ഒരു വർഷം മുഴുവൻ ക്രോഷെ\nബൊമ്മകൾ ഉണ്ടാക്കി.\nവിൽപ്പന ഇതുവരെ പൂജ്യം", [
 ("V","wide","അമ്മൂ, ബാൽക്കണി മുഴുവൻ ആനയും പൂച്ചയും മുയലും! ഇതൊരു മൃഗശാലയാണോ?"),
 ("A","A","വിവേകേ, ലോഞ്ചിന് മുന്നൂറ് ക്രോഷെ ബൊമ്മ. ജനുവരിയിൽ വെബ്സൈറ്റ് തുറക്കും."),
 ("V","V","OPC ആയിട്ട് ഒരു വർഷം ആയില്ലേ? ആനുവൽ ഫയലിംഗ് ചെയ്തോ?"),
 ("A","A","ഒരു ബൊമ്മ പോലും വിറ്റില്ല. വിൽപ്പന ഇല്ലാത്ത കമ്പനിക്ക് എന്ത് ഫയലിംഗ്?"),
 ("V","wide","വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം. ഒറ്റയാൾ കമ്പനി ആണെങ്കിലും."),
 ("V","V","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ."),
 ("A","A","എന്റെ ആനക്കുട്ടിയെക്കാൾ വേഗം വളരുമല്ലോ ആ പിഴ."),
 ("V","wide","അതുകൊണ്ട് ലോഞ്ചിന് മുമ്പ് ഫയലിംഗ്. പിന്നെ സന്തോഷത്തോടെ ലോഞ്ച്!")],
 "ലോഞ്ചിന് മുമ്പും\nഫയലിംഗ് മുടക്കരുത്", CTA_AFTER,
 cap_ml="ഒരു വർഷം മുഴുവൻ ക്രോഷെ ബൊമ്മകൾ ഉണ്ടാക്കി സ്റ്റോക്ക് ആക്കിയ അമ്മുവിന്റെ OPC-ക്ക് ഇതുവരെ വിൽപ്പന ഇല്ല. വരുമാനം പൂജ്യം ആയാലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A solo crochet-toy maker spent her One Person Company's first year building stock for a January launch, with zero sales. Annual filing is still due with zero revenue, and late forms cost 100 a day each.",
 cap_mg="Oru varsham muzhuvan crochet bommakal undaakki stock aakkiya aalude OPC-kku ithuvare sales illa. Varumanam zero aayaalum annual filing cheyyanam; vaikiyal oro form-inum divasam 100 pizha.")

# classroom: Nimmi + Adarsh. Nimmi teaches abacus alone; eight schools want a company contract; she picks "Smart Kids Abacus".
duo("d1715", "solo", "B", "classroom", "എട്ട് സ്കൂളിൽ അബാക്കസ്.\nപേര്: \"സ്മാർട്ട് കിഡ്സ്\".\nഅതിൽ എന്താ പ്രശ്നം?", [
 ("V","wide","നിമ്മി ടീച്ചറേ, ഇന്ന് പിള്ളേർ എന്നെക്കാൾ വേഗം കണക്ക് കൂട്ടി. ഞാൻ നാണം കെട്ടു."),
 ("A","A","ആദർശേ, അതാണ് അബാക്കസ്. ഇപ്പോ എട്ട് സ്കൂൾ വിളിച്ചു. അവർ കമ്പനിയുമായി മാത്രമേ കരാർ ഒപ്പിടൂ."),
 ("V","V","ഒറ്റയ്ക്കല്ലേ, OPC ആക്കാം. പേര് ആലോചിച്ചോ?"),
 ("A","A","സ്മാർട്ട് കിഡ്സ് അബാക്കസ്. നല്ല പേരല്ലേ?"),
 ("V","wide","നല്ലതാ. പക്ഷേ ആ പേരിനോട് സാമ്യമുള്ള എത്ര കമ്പനിയും LLP-യും ഉണ്ടാകും? സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("A","A","സ്മാർട്ട് എന്ന വാക്ക് ഇല്ലാത്ത ഒരു ട്യൂഷൻ സെന്ററും നാട്ടിൽ ഇല്ലല്ലോ."),
 ("V","V","അതുകൊണ്ട് ടീച്ചറുടെ സ്വന്തം ടച്ച് വേണം. ഒപ്പം രണ്ട് ബാക്കപ്പ് പേരും."),
 ("A","wide","എങ്കിൽ മണിമുത്ത് അബാക്കസ്. മുത്ത് എണ്ണി കണക്ക് പഠിക്കാം!")],
 "സ്മാർട്ട് പേര് അല്ല,\nവേറിട്ട പേര്", CTA_NAME,
 cap_ml="ഒറ്റയ്ക്ക് അബാക്കസ് പഠിപ്പിക്കുന്ന ടീച്ചറെ എട്ട് സ്കൂളുകൾ വിളിക്കുന്നു, കരാർ കമ്പനിയുമായി മാത്രം. 'സ്മാർട്ട് കിഡ്സ്' പോലുള്ള പേരുകൾ നിലവിലുള്ള കമ്പനികളോടോ LLP-കളോടോ സാമ്യം വന്ന് റിജക്ട് ആകാം; വേറിട്ട OPC പേര് കണ്ടെത്തൂ.",
 cap_en="A solo abacus teacher in Kerala is wanted by eight schools that sign only with companies, and she picks 'Smart Kids Abacus'. Names similar to existing companies or LLPs get rejected, so give your One Person Company a distinctive name with backups.",
 cap_mg="Ottaykku abacus padippikkunna teacher-ne 8 school vilikkunnu, contract company-yumaayi maathram. 'Smart Kids' pole names existing company-kalodo LLP-kalodo saamyam vannu reject aakaam; vere OPC name kandethu.")

# chat: Delna + her mother. Delna, a solo bridal make-up artist in Thrissur, is at day 168 of her OPC with 14 weddings this month.
chat("c993", "solo", "A", "ഈ മാസം 14 കല്യാണം.\nOPC-ക്ക് 168 ദിവസം.\nഅമ്മയുടെ ഒരു മെസ്സേജ്", ("ഡെൽന", "അമ്മ"), [
 (1,"മോളേ, ഇന്ന് എത്രാമത്തെ കല്യാണപ്പെണ്ണ്?"),
 (0,"അമ്മേ, ഇന്ന് മൂന്ന്. ഇരിങ്ങാലക്കുടയിൽ ഒന്ന്, തൃശ്ശൂരിൽ രണ്ട്. ഇപ്പോ ഐലൈനർ വരയ്ക്കുവാ."),
 (1,"ഒന്ന് ചോദിക്കട്ടെ. നിന്റെ കമ്പനി തുടങ്ങിയിട്ട് ആറ് മാസം ആകാറായില്ലേ? ആ ഫോമിന്റെ കാര്യം?"),
 (0,"ഏത് ഫോം? കല്യാണ സീസൺ കഴിഞ്ഞിട്ട് നോക്കാം അമ്മേ."),
 (1,"കസിൻ പറഞ്ഞു. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം. ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കാൻ."),
 (0,"ഇന്ന് നൂറ്റി അറുപത്തെട്ടാം ദിവസം! പന്ത്രണ്ട് ദിവസം മാത്രം."),
 (1,"മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. നിനക്ക് ദിവസം ആയിരം രൂപ വേറെ."),
 (0,"അമ്മേ, നാളെ രാവിലെ ആദ്യം ഇത്. അമ്മയാണ് എന്റെ ഏറ്റവും നല്ല മാനേജർ!")],
 "കല്യാണ സീസണിലും\nINC-20A മറക്കരുത്", CTA_AFTER,
 cap_ml="തൃശ്ശൂരിലെ ബ്രൈഡൽ മേക്കപ്പ് ആർട്ടിസ്റ്റിന്റെ OPC-ക്ക് 168 ദിവസം, ഈ മാസം 14 കല്യാണം, INC-20A ഓർമ്മിപ്പിച്ചത് അമ്മ. 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ.",
 cap_en="A solo bridal make-up artist in Thrissur has 14 weddings this month and her One Person Company is at day 168; her mother remembers INC-20A. It is due within 180 days of incorporation: 50,000 on the company and 1,000 a day for the director if missed.",
 cap_mg="Thrissur-ile bridal makeup artist-nte OPC-kku 168 divasam, ee maasam 14 kalyanam, INC-20A ormippichathu amma. 180 days-inullil file cheythillenkil company-kku 50,000 pizha, director-kku divasam 1,000.")

# rooftop: Arya + Shyam. Shyam photographs the night sky alone; a hotel chain wants his prints in every room; office is his rented rooftop room.
duo("d1716", "solo", "C", "rooftop", "നക്ഷത്രങ്ങളുടെ ഫോട്ടോ\nഹോട്ടൽ മുറികളിലേക്ക്.\nഓഫീസ്: വാടക ടെറസ് മുറി", [
 ("A","wide","ശ്യാമേ, രാത്രി രണ്ട് മണിക്ക് ടെറസിൽ ക്യാമറയും കൊണ്ട്. വീണ്ടും ആകാശഗംഗ?"),
 ("V","V","ആര്യേ, നല്ല വാർത്ത. ഒരു ഹോട്ടൽ ചെയിൻ അവരുടെ എല്ലാ മുറിയിലും എന്റെ നക്ഷത്ര ഫോട്ടോ ഫ്രെയിം ചെയ്ത് വെക്കും."),
 ("A","A","വൗ! പക്ഷേ ഹോട്ടലുകാർ കമ്പനി ഇൻവോയ്സ് അല്ലേ ചോദിക്കുക?"),
 ("V","V","അതേ. ഒറ്റയ്ക്കാണ്, OPC ആക്കാം. പക്ഷേ ഓഫീസ്? ഈ വാടക ടെറസ് മുറി മാത്രമേ ഉള്ളൂ."),
 ("A","wide","താമസിക്കുന്ന ഈ മുറി രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC-യും പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും വേണം."),
 ("V","V","ഉടമ താഴത്തെ നിലയിൽ ഉണ്ട്. പക്ഷേ എട്ട് മണി കഴിഞ്ഞാൽ വാതിൽ തുറക്കില്ല."),
 ("A","A","എങ്കിൽ നാളെ രാവിലെ. ഉറങ്ങാതെ നക്ഷത്രം നോക്കുന്ന ആൾക്ക് സൂര്യോദയവും കാണാമല്ലോ."),
 ("V","wide","ശരി. ആദ്യത്തെ ഫ്രെയിം ഉടമയ്ക്ക്. NOC-യുടെ നന്ദി!")],
 "ഓഫീസ് ചെറുതാകാം.\nപേപ്പർ ശരിയാകണം", CTA_DOCS,
 cap_ml="രാത്രി ആകാശം ഫോട്ടോ എടുക്കുന്ന ശ്യാമിന്റെ ചിത്രങ്ങൾ ഒരു ഹോട്ടൽ ചെയിൻ എല്ലാ മുറിയിലും വെക്കും, ഇൻവോയ്സ് കമ്പനിയിൽ നിന്ന്. വാടകയ്ക്ക് താമസിക്കുന്ന ടെറസ് മുറി OPC-യുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം, ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ.",
 cap_en="A solo astrophotographer's night-sky prints will hang in every room of a hotel chain, invoiced by a company. His rented rooftop room can be his One Person Company's registered office with the owner's NOC and a recent utility bill.",
 cap_mg="Raathri aakaasham photo edukkunna aalude chithrangal oru hotel chain ella muriyilum vekkum, invoice company-yil ninnu. Vaadakaykku thaamasikkunna terrace room OPC registered office aakkam, owner-nte NOC-um puthiya utility bill-um undenkil.")
