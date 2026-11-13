# Script bank, batch 11. New situations: an airport lounge wanting a bakery's unniyappam, a football club's season-long juice counters,
# a hospital canteen tender for five years, a home tiffin cook feeding a 400-worker construction site, a Varkala kayak man who wants
# "Bank" in his company name, a sound-and-light rental's two-year event contract, a crane operator in Abu Dhabi who thinks he must buy
# a crane first, Saudi dates for a Ramadan supermarket deal, an insurance clerk in Dubai who wants "Insurance" in her Kerala name,
# a Dubai phone-accessories brand run from a sister's rented flat, three Gulf colleagues' investment letters for an LLP, a nurse in
# Germany who wants shares but no director post, a Munnar trekking guide in a rented room, a cruise line's cooking classes, a retired
# teacher's audiobook OPC, a solo food truck at an IT park, a solo goat farmer past six months, a wedding drone photographer.
# Same fact list and no-price rule as batch01. Segments proprietor 7, nri 7, solo 6; 15 duo3d in 15 different locations, default names.
# Every script carries cap_ml / cap_en / cap_mg (search captions); factory/captions.py adds the hook, CTA and hashtags.
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
# bakery: Jisha + Sabu. The airport lounge wants Sabu's unniyappam every morning from opening day, three weeks away; vendors must be a Pvt Ltd.
duo("d1301", "proprietor", "A", "bakery", "എയർപോർട്ട് ലൗഞ്ച് പറഞ്ഞു:\n\"എല്ലാ രാവിലെയും\nനിങ്ങളുടെ ഉണ്ണിയപ്പം വേണം\"", [
 ("A","wide","സാബുച്ചേട്ടാ, ഇന്ന് ഉണ്ണിയപ്പം എണ്ണിയിട്ട് മൂന്നാമത്തെ തവണയാ എണ്ണുന്നത്. എന്ത് പറ്റി?"),
 ("V","V","ജിഷേ, എയർപോർട്ടിലെ പുതിയ ലൗഞ്ച്. ദിവസവും രാവിലെ അഞ്ഞൂറ് ഉണ്ണിയപ്പം നമ്മുടേത് വേണമെന്ന്."),
 ("A","A","ഫ്ലൈറ്റ് പിടിക്കാൻ ഓടുന്നവർ നമ്മുടെ ഉണ്ണിയപ്പം തിന്നുമോ! എന്നാ തുടങ്ങുന്നത്?"),
 ("V","V","ലൗഞ്ച് തുറക്കുന്നത് മൂന്നാഴ്ച കഴിഞ്ഞ്. പക്ഷേ വെണ്ടർ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി ആയിരിക്കണം."),
 ("V","V","നമുക്ക് GST ഒക്കെ ഉണ്ടല്ലോ. ബേക്കറി ബോർഡിൽ 'കമ്പനി' എന്ന് എഴുതിയാൽ പോരേ?"),
 ("A","wide","ചേട്ടാ, ബോർഡിൽ എഴുതിയാൽ കമ്പനി ആകില്ല. രജിസ്റ്റർ ചെയ്യണം. സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ. ചേട്ടനും ഞാനും. ഡോക്യുമെന്റ്സ് ഈ ആഴ്ച തന്നെ."),
 ("V","V","മൂന്നാഴ്ചയിൽ നിന്ന് പതിനഞ്ച് ദിവസം പോയാൽ… കഷ്ടിച്ച്!"),
 ("A","wide","അതുകൊണ്ട് ഇന്ന് അപ്പം ചുടുന്നതിനൊപ്പം ഫോമും ചുടാം!")],
 "ലൗഞ്ച് തുറക്കും മുമ്പ്\nകമ്പനി റെഡിയാകണം", CTA_START,
 cap_ml="എയർപോർട്ട് ലൗഞ്ചിലേക്ക് ദിവസവും ഉണ്ണിയപ്പം സപ്ലൈ ചെയ്യാൻ ബേക്കറിക്ക് ഓഫർ, പക്ഷേ വെണ്ടർ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി ആയിരിക്കണം. GST ഉണ്ടെന്ന് കരുതി ബേക്കറി കമ്പനി ആകില്ല. കേരളത്തിൽ Pvt Ltd കമ്പനി രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം എടുക്കും.",
 cap_en="A Kerala bakery gets a daily supply order from an airport lounge, but vendors must be a private limited company. Having GST does not make a shop a company. Private limited company registration usually takes 7 to 15 working days, so start well before the contract date.",
 cap_mg="Bakery-kku airport lounge-il ninnu daily order, pakshe vendor Pvt Ltd company aayirikkanam. GST undennu vechu shop company aakilla. Pvt Ltd company register cheyyan saadharana 7-15 working days edukkum, athukondu nerathe thudanguka.")

# juiceshop: Raziya + Naushad. A football club gives Naushad all stadium juice counters for the season; his company is 25 days old, no auditor yet.
duo("d1302", "proprietor", "B", "juiceshop", "സ്റ്റേഡിയത്തിലെ എല്ലാ\nജ്യൂസ് കൗണ്ടറും ഈ സീസൺ\nനമുക്ക്!", [
 ("V","wide","റസിയാ, ഫുട്ബോൾ ക്ലബ്ബിന്റെ മെയിൽ വന്നു! സ്റ്റേഡിയത്തിലെ എല്ലാ ജ്യൂസ് കൗണ്ടറും ഈ സീസൺ നമുക്ക്!"),
 ("A","A","ഗോൾ! അതിനല്ലേ കഴിഞ്ഞ മാസം കമ്പനി ആക്കിയത്. ഇനി എന്താ അവർക്ക് വേണ്ടത്?"),
 ("V","V","ഒരു വെണ്ടർ ഫോം. അതിൽ ഒരു കോളം: കമ്പനിയുടെ ഓഡിറ്റർ ആര്?"),
 ("V","V","ഓഡിറ്റർ ഒക്കെ വർഷാവസാനം കണക്ക് നോക്കാൻ വരുന്നവരല്ലേ? ഇപ്പോ എന്തിനാ?"),
 ("A","wide","അല്ല. കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം. അത് നിയമമാണ്."),
 ("A","A","സർട്ടിഫിക്കറ്റ് വന്നിട്ട് ഇരുപത്തഞ്ച് ദിവസം. ഇനി അഞ്ച് ദിവസം മാത്രം."),
 ("V","V","അയ്യോ. ഫസ്റ്റ് ഹാഫ് കഴിയും മുമ്പ് ഗോൾ അടിക്കണം!"),
 ("A","A","പിന്നെ നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A-യും ഉണ്ട്. അതും കലണ്ടറിൽ ഇട്."),
 ("V","wide","ശരി ക്യാപ്റ്റൻ! ഇന്ന് ജ്യൂസ് അടിക്കുന്നതിന് മുമ്പ് ഓഡിറ്ററെ വിളിക്കാം.")],
 "30 ദിവസത്തിനുള്ളിൽ\nആദ്യ ഓഡിറ്റർ", CTA_AFTER,
 cap_ml="ഫുട്ബോൾ സ്റ്റേഡിയത്തിലെ ജ്യൂസ് കൗണ്ടർ കോൺട്രാക്ട് കിട്ടി, പക്ഷേ വെണ്ടർ ഫോമിൽ ഓഡിറ്ററുടെ പേര് ചോദിക്കുന്നു. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം, 180 ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം.",
 cap_en="A Kochi juice shop owner turned his business into a private limited company and won a stadium contract, then the vendor form asked for his auditor. Every new company must appoint its first auditor within 30 days of incorporation and file INC-20A within 180 days.",
 cap_mg="Juice shop company aakki, stadium contract kitti, pakshe vendor form-il auditor aaru ennu chodikkunnu. Company register cheythu 30 days-inullil first auditor-ne vekkanam, 180 days-inullil INC-20A file cheyyanam. Calendar-il ittekku.")

# hospital: Lakshmi + Joseph. Joseph has run the hospital canteen alone for nine years; the new tender is for five years and only for a Pvt Ltd.
duo("d1303", "proprietor", "A", "hospital", "ഒൻപത് വർഷമായി\nആശുപത്രി ക്യാന്റീൻ.\nപുതിയ ടെൻഡർ 5 വർഷത്തേക്ക്", [
 ("A","wide","ജോസഫ് ചേട്ടാ, നോട്ടീസ് ബോർഡിൽ ക്യാന്റീൻ ടെൻഡർ. അഞ്ച് വർഷത്തേക്ക്!"),
 ("V","V","കണ്ടു ലക്ഷ്മീ. ഒൻപത് വർഷമായി ഈ ക്യാന്റീൻ ഞാനാ നടത്തുന്നത്. ഇത്തവണ ഒരു പുതിയ നിബന്ധന."),
 ("V","V","അപേക്ഷിക്കുന്നത് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി ആയിരിക്കണം. ഞാൻ ഒറ്റയ്ക്ക് ഒരു പ്രൈവറ്റ് ലിമിറ്റഡ് തുടങ്ങാം."),
 ("A","A","ഒറ്റയ്ക്ക് പറ്റില്ല ചേട്ടാ. പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ വേണം."),
 ("V","V","ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി ഇല്ലേ?"),
 ("A","A","ഉണ്ട്. പക്ഷേ ടെൻഡറിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് എന്നല്ലേ എഴുതിയിരിക്കുന്നത്?"),
 ("V","V","ശരിയാ. അപ്പോ രണ്ടാമത്തെ ആൾ… അടുക്കളയിൽ മോൻ ഉണ്ട്. ഒൻപത് വർഷമായി ദോശ ചുടുന്നത് അവനാ."),
 ("A","wide","അത് മതി. ദോശ ചുടുന്നവൻ ഇനി ഡയറക്ടർ. പക്ഷേ ടെൻഡർ തീയതിക്ക് മുമ്പ് കമ്പനി ഉണ്ടാകണം."),
 ("V","wide","എന്നാൽ ഇന്ന് തന്നെ തുടങ്ങാം. ടെൻഡർ ജയിച്ചാൽ ആദ്യ ചായ സിസ്റ്റർക്ക്!")],
 "ടെൻഡർ Pvt Ltd ചോദിച്ചാൽ\nരണ്ടുപേർ വേണം", CTA_START,
 cap_ml="ഒൻപത് വർഷമായി ആശുപത്രി ക്യാന്റീൻ നടത്തുന്ന പ്രൊപ്രൈറ്റർക്ക് പുതിയ ടെൻഡറിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി നിർബന്ധം. Pvt Ltd കമ്പനിക്ക് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം. ഒറ്റയ്ക്കാണെങ്കിൽ OPC ആണ് വഴി.",
 cap_en="A canteen owner who has run a hospital canteen in Kerala for nine years finds the new five-year tender is open only to private limited companies. A Pvt Ltd needs at least two directors and two shareholders; a single owner would look at a One Person Company (OPC) instead.",
 cap_mg="9 varshamaayi hospital canteen nadathunna proprietor-nu puthiya tender-il Pvt Ltd company venam. Pvt Ltd-nu minimum 2 directors, 2 shareholders venam. Ottaykku aanenkil one person company (OPC) aanu option.")

# home: Sneha + Arun. Sneha's home tiffin service is asked for 400 site lunches a day; she thinks she must first rent a commercial room as the office.
duo("d1304", "proprietor", "B", "home", "40 പേർക്ക് ഊണ്.\nഇപ്പോ ഒരു സൈറ്റിൽ നിന്ന്\n\"ദിവസം 400 ഊണ് വേണം\"", [
 ("V","wide","സ്നേഹേ, അടുക്കളയിൽ നിന്ന് ഫോണിൽ ആരോടാ ഇത്ര ഉറക്കെ?"),
 ("A","A","അരുണേട്ടാ, ആ ഫ്ലാറ്റ് പണിയുന്ന കൺസ്ട്രക്ഷൻ കമ്പനി. സൈറ്റിലെ പണിക്കാർക്ക് ദിവസം നാനൂറ് ഊണ് നമ്മുടെ വക വേണമെന്ന്!"),
 ("V","V","നാൽപ്പതിൽ നിന്ന് നാനൂറ്! പക്ഷേ അവർ പൈസ കൊടുക്കുന്നത് കമ്പനികൾക്ക് മാത്രമല്ലേ?"),
 ("A","A","അതാ. കമ്പനി തുടങ്ങണം. അതിന് ടൗണിൽ ഒരു കൊമേഴ്സ്യൽ മുറി വാടകയ്ക്ക് എടുക്കണം. അഡ്വാൻസ് എവിടുന്ന്?"),
 ("V","wide","വേണ്ട. വീടിന്റെ അഡ്രസ്സും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം."),
 ("V","V","വീട് എന്റെ പേരിലല്ലേ. ഉടമ എന്ന നിലയിൽ ഞാൻ NOC ഒപ്പിട്ട് തരാം. കൂടെ പുതിയ ഒരു കറന്റ് ബില്ല്."),
 ("A","A","അപ്പോ ഓഫീസും അടുക്കളയും ഒരേ വീട്ടിൽ!"),
 ("V","V","അതേ. മുറിക്ക് കൊടുക്കേണ്ട പൈസയ്ക്ക് ഒരു വലിയ ചെമ്പ് വാങ്ങ്. നാനൂറ് പേർക്ക് ചോറ് വെക്കണ്ടേ!"),
 ("A","wide","NOC തരുന്നതിന് ചേട്ടന് ഇന്ന് സ്പെഷ്യൽ മീൻ കറി. ബാക്കി നാനൂറ് പേർക്ക് നാളെ മുതൽ!")],
 "ഓഫീസ് മുറി വേണ്ട.\nവീട് മതി", CTA_DOCS,
 cap_ml="വീട്ടിലെ ടിഫിൻ സർവീസിന് കൺസ്ട്രക്ഷൻ സൈറ്റിൽ നിന്ന് ദിവസം 400 ഊണിന്റെ ഓർഡർ, പക്ഷേ കമ്പനി വേണം. കമ്പനി രജിസ്ട്രേഷന് കൊമേഴ്സ്യൽ മുറി നിർബന്ധമില്ല. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ വീടിന്റെ അഡ്രസ്സ് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A home tiffin cook in Kerala gets an order for 400 site lunches a day, but the builder pays only companies. You don't need to rent a commercial room to register a company: your home can be the registered office with the owner's NOC and a recent utility bill.",
 cap_mg="Veettile tiffin service-nu construction site-il ninnu daily 400 oonu order, pakshe company venam. Company register cheyyan commercial room venda. Owner-nte NOC-um puthiya current bill-um undenkil veedinte address registered office aakkam.")

# beach: Divya + Nikhil. A resort chain wants Nikhil's kayak trips for all its guests; he wants to call the company "Varkala Kayak Bank".
duo("d1305", "proprietor", "A", "beach", "റിസോർട്ട് ചെയിൻ പറഞ്ഞു:\n\"എല്ലാ ഗസ്റ്റിനും\nനിങ്ങളുടെ കയാക്ക് ട്രിപ്പ്\"", [
 ("A","wide","നിഖിലേ, കയാക്ക് ഒക്കെ വെള്ളത്തിലിറക്കാതെ കരയിൽ ഇരുന്ന് എന്താ എഴുതുന്നത്?"),
 ("V","V","ദിവ്യേച്ചീ, ആ റിസോർട്ട് ചെയിൻ. അവരുടെ എല്ലാ ഗസ്റ്റിനും നമ്മുടെ കയാക്ക് ട്രിപ്പ്. കോൺട്രാക്ട് കമ്പനിയുമായി മാത്രം."),
 ("A","A","അടിപൊളി! കമ്പനിക്ക് പേര് ആലോചിച്ചോ?"),
 ("V","V","ഉറപ്പിച്ചു. വർക്കല കയാക്ക് ബാങ്ക്! കയാക്കുകൾ ഡിപ്പോസിറ്റ് ചെയ്ത് വെച്ചിരിക്കുന്ന സ്ഥലം. എങ്ങനെയുണ്ട്?"),
 ("A","wide","പേര് കൊള്ളാം. പക്ഷേ Bank, Insurance പോലുള്ള വാക്കുകൾ കമ്പനി പേരിൽ വന്നാൽ പ്രത്യേക അനുമതി വേണം."),
 ("A","A","ഇല്ലെങ്കിൽ പേര് റിജക്ട് ആകാം. അപ്പോ കോൺട്രാക്ടും വൈകും."),
 ("V","V","അയ്യോ. ലോൺ ചോദിച്ച് ആൾക്കാർ കടപ്പുറത്ത് ക്യൂ നിൽക്കുകയും ചെയ്യും!"),
 ("A","A","അതുകൊണ്ട് ബാങ്ക് വേണ്ട. കടലും തിരയും കയാക്കും ഒക്കെ ചേർത്ത് മൂന്ന് പേര് കൂടി എഴുത്."),
 ("V","wide","ശരി. ബാങ്ക് ഞാൻ കടലിൽ ഒഴുക്കി. ഇനി പുതിയ പേര്, പുതിയ തിര!")],
 "Bank എന്ന വാക്ക്\nപേരിൽ ഇടും മുമ്പ്", CTA_NAME,
 cap_ml="വർക്കലയിലെ കയാക്ക് ബിസിനസിന് റിസോർട്ട് ചെയിനിന്റെ കോൺട്രാക്ട്, കമ്പനി പേരിൽ 'Bank' വേണമെന്ന് ആഗ്രഹം. Bank, Insurance പോലുള്ള വാക്കുകൾക്ക് പ്രത്യേക അനുമതി വേണം, ഇല്ലെങ്കിൽ കമ്പനി പേര് റിജക്ട് ആകാം. രജിസ്ട്രേഷന് മുമ്പ് ബാക്കപ്പ് പേരുകൾ കരുതൂ.",
 cap_en="A kayak operator in Varkala lands a resort-chain contract and wants 'Bank' in his company name. Words like Bank or Insurance need special approval, so a name like that can get rejected at company registration. Keep two or three backup company names ready.",
 cap_mg="Varkala-yile kayak business-nu resort chain contract, company name-il 'Bank' venam ennu aagraham. Bank, Insurance pole ulla words-nu special approval venam, illenkil company name reject aakaam. Register cheyyunnathinu munpu backup names ready aakku.")

# chat: Sanal runs a sound-and-light rental; a Bengaluru event company offers two years of shows if he becomes a company. His father thinks a company needs ten lakh in the bank.
chat("c951", "proprietor", "B", "ബെംഗളൂരു ഇവന്റ് കമ്പനി:\n\"2 വർഷത്തെ ഷോകൾ.\nകമ്പനി ആണെങ്കിൽ മാത്രം\"", ("സനൽ", "അച്ഛൻ"), [
 (0,"അച്ഛാ, ആ ബെംഗളൂരു ഇവന്റ് കമ്പനി വിളിച്ചു. രണ്ട് വർഷത്തെ ഷോകൾക്ക് സൗണ്ടും ലൈറ്റും നമ്മുടേത്."),
 (1,"ദൈവമേ. നമ്മുടെ കല്യാണ ആംപ്ലിഫയർ ബെംഗളൂരു വരെ പോകുമോ?"),
 (0,"പോകും. പക്ഷേ ഒരു നിബന്ധന. നമ്മൾ രജിസ്റ്റേർഡ് കമ്പനി ആയിരിക്കണം."),
 (1,"കമ്പനി എന്നൊക്കെ പറഞ്ഞാൽ ബാങ്കിൽ പത്ത് ലക്ഷം കാണിക്കണ്ടേ മോനേ? നമ്മുടെ പൈസ മുഴുവൻ സ്പീക്കറിലാ."),
 (0,"വേണ്ട അച്ഛാ. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 (1,"അപ്പോ ആര് ആരൊക്കെ വേണം?"),
 (0,"കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ. ഞാനും അച്ഛനും."),
 (1,"മുപ്പത് കൊല്ലം മൈക്ക് ടെസ്റ്റ് ചെയ്ത എന്നെ ഡയറക്ടർ ആക്കുമോ?"),
 (0,"ആക്കും. ഹലോ ഹലോ മൈക്ക് ടെസ്റ്റിംഗ്… ഡയറക്ടർ അച്ഛൻ!")],
 "ലക്ഷങ്ങൾ കാണിക്കേണ്ട.\nരണ്ടുപേർ മതി", CTA_START,
 cap_ml="സൗണ്ട് ആൻഡ് ലൈറ്റ് റെന്റൽ നടത്തുന്ന അച്ഛനും മകനും ബെംഗളൂരുവിലെ ഇവന്റ് കമ്പനിയുടെ രണ്ട് വർഷത്തെ കോൺട്രാക്ട്. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല. രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും മതി.",
 cap_en="A father-and-son sound and light rental in Kerala is offered two years of event work, if they register a company. There is no minimum paid-up capital for a private limited company; two directors and two shareholders are enough to start.",
 cap_mg="Sound and light rental nadathunna achanum makanum Bengaluru event company-yude 2 varsha contract. Pvt Ltd thudangan bank-il lakhs kaanikkanda, minimum paid-up capital nirbandham illa. 2 directors, 2 shareholders mathi.")

lst("l951", "proprietor", "C", "വലിയ ഓർഡർ വന്നു.\nബയർ ചോദിച്ചു: \"കമ്പനിയാണോ?\"\nയെസ് പറയും മുമ്പ് 3 കാര്യം", [
 ("ആരൊക്കെ: രണ്ടുപേരോ ഒരാളോ?", "പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC."),
 ("എത്ര ദിവസം: ഒപ്പിടൽ തീയതി നോക്കൂ", "Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം. പേര് റിജക്ട് ആയാൽ വൈകും."),
 ("എവിടെ: ഓഫീസ് അഡ്രസ്സ്", "വീടും ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC, പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ല്.")],
 "ഓർഡർ കാത്തിരിക്കില്ല.\nഡോക്യുമെന്റ്സ് ഇന്ന്", CTA_DOCS,
 cap_ml="കടയ്ക്കോ ചെറിയ ബിസിനസിനോ വലിയ ഓർഡർ വരുമ്പോൾ ബയർ ആദ്യം ചോദിക്കുന്നത്: കമ്പനിയാണോ? Pvt Ltd-ഓ OPC-യോ, രജിസ്ട്രേഷന് എത്ര ദിവസം, ഓഫീസ് അഡ്രസ്സിന് എന്ത് ഡോക്യുമെന്റ്സ് എന്ന് ആദ്യമേ അറിഞ്ഞിരിക്കൂ.",
 cap_en="Got a big order and the buyer asks if you are a registered company? Three things to check first: Pvt Ltd or OPC, how many working days company registration takes, and which documents you need to use your home as the registered office.",
 cap_mg="Valiya order vannu, buyer chodichu 'company aano?' Yes parayum munpu 3 kaaryam: Pvt Ltd aano OPC aano, company register cheyyan ethra working days, office address-nu enthokke documents venam.")

# ---------------- nri ----------------
# gulf: Shiju + Faisal. Faisal, a crane operator in Abu Dhabi, has a port-road contractor in Kerala who will hire a crane, but only from a company; he thinks he must buy the crane first to "show capital".
duo("d1306", "nri", "A", "gulf", "നാട്ടിലെ റോഡ് പണിക്ക്\nക്രെയിൻ വാടകയ്ക്ക്.\n\"ആദ്യം ക്രെയിൻ വാങ്ങണം\"", [
 ("A","wide","ഫൈസലേ, ഡ്യൂട്ടി കഴിഞ്ഞിട്ടും ക്രെയിനിന്റെ ഫോട്ടോ തന്നെ നോക്കി ഇരിക്കുവാണോ?"),
 ("V","V","ഷിജുവേട്ടാ, നാട്ടിൽ ഒരു റോഡ് കോൺട്രാക്ടർ. അവരുടെ പണിക്ക് ക്രെയിൻ വാടകയ്ക്ക് വേണം. പക്ഷേ ബിൽ കമ്പനിയുടേത് ആകണം."),
 ("A","A","ഇരുപത് കൊല്ലം അബുദാബിയിൽ ക്രെയിൻ ഓടിച്ചവൻ നാട്ടിൽ ക്രെയിൻ കമ്പനി. കൊള്ളാം!"),
 ("V","V","പക്ഷേ ആദ്യം ഒരു ക്രെയിൻ വാങ്ങണം. എന്നാലല്ലേ കമ്പനിക്ക് ക്യാപിറ്റൽ കാണിക്കാൻ പറ്റൂ?"),
 ("A","wide","വേണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡ് തുടങ്ങാൻ മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 ("A","A","NRI-ക്കും ഡയറക്ടർ ആകാം. നാട്ടിലുള്ള ഒരാൾ കൂടി ഡയറക്ടർ ആയാൽ മതി."),
 ("V","V","നാട്ടിൽ അനിയൻ ഉണ്ട്. അവന് ക്രെയിൻ അറിയില്ല, പക്ഷേ ഒപ്പിടാൻ അറിയാം."),
 ("A","A","അത് മതി. ആദ്യം കമ്പനി, പിന്നെ കോൺട്രാക്ട്, പിന്നെ ക്രെയിൻ."),
 ("V","wide","ശരി. ക്രെയിൻ കൊണ്ട് പൊക്കാൻ പറ്റാത്തത് ഒന്നേയുള്ളൂ. മടി!")],
 "ആദ്യം ക്രെയിൻ അല്ല,\nആദ്യം കമ്പനി", CTA_START,
 cap_ml="അബുദാബിയിലെ ക്രെയിൻ ഓപ്പറേറ്റർക്ക് നാട്ടിൽ ക്രെയിൻ റെന്റൽ കമ്പനി തുടങ്ങണം, പക്ഷേ ആദ്യം മെഷീൻ വാങ്ങണമെന്ന് കരുതുന്നു. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം ക്യാപിറ്റൽ നിർബന്ധമില്ല. NRI-ക്ക് ഡയറക്ടർ ആകാം, ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.",
 cap_en="An NRI crane operator in Abu Dhabi wants to start an equipment rental company in Kerala and thinks he must buy a crane first. A private limited company has no minimum paid-up capital. NRIs can be directors, with at least one director resident in India.",
 cap_mg="Abu Dhabi-yile crane operator-nu naattil crane rental company thudanganam, pakshe aadyam machine vaanganam ennu vicharikkunnu. Pvt Ltd thudangan minimum capital venda. NRI-kkum director aakaam, oru director India-yil thamasikkunna aal aakanam.")

# gulfroom: Naseer + Shamsu. Shamsu sends Saudi dates to his brother's shop in Kerala; a supermarket chain wants exclusive Ramadan supply from a company, six weeks out.
duo("d1307", "nri", "B", "gulfroom", "സൂപ്പർമാർക്കറ്റ് ചെയിൻ:\n\"റമദാന് നിങ്ങളുടെ ഈന്തപ്പഴം\nമാത്രം മതി\"", [
 ("V","wide","നസീറേ, നാട്ടിൽ നിന്ന് അനിയൻ വിളിച്ചു. ഒരു സൂപ്പർമാർക്കറ്റ് ചെയിൻ!"),
 ("A","A","നമ്മൾ അയക്കുന്ന ഈന്തപ്പഴത്തിനോ?"),
 ("V","V","അതേ. റമദാന് അവരുടെ എല്ലാ ഷോപ്പിലും നമ്മുടെ ഈന്തപ്പഴം മാത്രം. പക്ഷേ സപ്ലയർ കമ്പനി ആയിരിക്കണം."),
 ("A","A","റമദാന് ആറാഴ്ചയേ ഉള്ളൂ ഷംസൂ. നീ ഇവിടെ, അനിയൻ അവിടെ. കമ്പനി എങ്ങനെ?"),
 ("V","V","അതാ ചോദ്യം. ഞാൻ NRI അല്ലേ. എനിക്ക് ഡയറക്ടർ ആകാൻ പറ്റുമോ?"),
 ("A","wide","പറ്റും. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. നാട്ടിലുള്ള അനിയൻ രണ്ടാമത്തെ ഡയറക്ടർ."),
 ("A","A","രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. ആറാഴ്ച ഉണ്ടല്ലോ, ഇന്ന് തുടങ്ങിയാൽ."),
 ("V","V","ഇന്ന് തന്നെ. നോമ്പ് തുടങ്ങും മുമ്പ് കമ്പനി നോമ്പ് തുറക്കണം!"),
 ("A","wide","ആദ്യത്തെ പെട്ടി ഈന്തപ്പഴം എനിക്ക്. ഐഡിയ തന്നതിന്റെ സ്നേഹം!")],
 "നിങ്ങൾ ഗൾഫിൽ,\nഅനിയൻ നാട്ടിൽ.\nകമ്പനി റെഡി", CTA_START,
 cap_ml="സൗദിയിൽ നിന്ന് ഈന്തപ്പഴം അയക്കുന്ന NRI-ക്ക് കേരളത്തിലെ സൂപ്പർമാർക്കറ്റ് ചെയിനിന്റെ റമദാൻ ഓർഡർ, സപ്ലയർ കമ്പനി ആയിരിക്കണം. NRI-ക്ക് ഗൾഫിലിരുന്ന് ഡയറക്ടർ ആകാം, നാട്ടിലുള്ള സഹോദരൻ രണ്ടാമത്തെ ഡയറക്ടർ. രജിസ്ട്രേഷന് 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="An NRI in Saudi Arabia ships dates to his brother's shop in Kerala, and a supermarket chain wants exclusive Ramadan supply from a company. NRIs can be directors of an Indian private limited company while the brother at home is the resident director; registration usually takes 7 to 15 working days.",
 cap_mg="Saudi-yil ninnu dates ayakkunna NRI-kku Kerala supermarket chain-inte Ramadan order, supplier company aayirikkanam. NRI-kku Gulf-il irunnu thanne director aakaam, naattilulla aniyan resident director. NRI business in Kerala thudangan 7-15 working days.")

# gulfoffice: Shahana + Asif. Shahana, an insurance-office clerk in Dubai, wants her Kerala travel-help agency named "... Insurance Hub".
duo("d1308", "nri", "A", "gulfoffice", "ദുബായിൽ ഇൻഷുറൻസ് ഓഫീസ്.\nനാട്ടിലെ കമ്പനിക്കും\n\"ഇൻഷുറൻസ്\" എന്ന് പേര്?", [
 ("V","wide","ഷഹാന, ലഞ്ച് ബ്രേക്കിൽ ലോഗോ ഡിസൈനോ? ഇത് ഏത് കമ്പനിയുടെ?"),
 ("A","A","എന്റേത് ആസിഫേ. നാട്ടിൽ ഗൾഫിലേക്ക് പോകുന്നവർക്ക് യാത്ര, വിസ കാര്യങ്ങൾ ഒക്കെ സഹായിക്കുന്ന ഒരു ഏജൻസി."),
 ("V","V","പേര് എന്താ?"),
 ("A","A","മലബാർ ഇൻഷുറൻസ് ഹബ്. പത്ത് കൊല്ലമായി ഞാൻ ഇൻഷുറൻസ് ഓഫീസിലല്ലേ. ആ വാക്ക് കേട്ടാൽ ആൾക്കാർക്ക് വിശ്വാസം വരും."),
 ("V","wide","പക്ഷേ Insurance, Bank പോലുള്ള വാക്കുകൾ കമ്പനി പേരിൽ ഇടാൻ പ്രത്യേക അനുമതി വേണം."),
 ("V","V","അനുമതി ഇല്ലാതെ ഇട്ടാൽ പേര് റിജക്ട് ആകാം. അപ്പോ സമയം പോകും."),
 ("A","A","ഇൻഷുറൻസ് ഓഫീസിൽ ഇരുന്ന് പേരിന് ഇൻഷുറൻസ് എടുക്കാൻ മറന്നു!"),
 ("V","V","ഹബ് നിർത്ത്. വേറെ മൂന്ന് പേര് കൂടി എഴുത്. സ്വന്തം ഒരു വാക്ക്."),
 ("A","wide","ശരി. ആദ്യം പേര്, പിന്നെ ലോഗോ. ഈ ലോഗോ ഇപ്പോ തൽക്കാലം വാൾപേപ്പർ!")],
 "Insurance, Bank\nപേരിൽ വേണോ?\nആദ്യം ഇത് കേൾക്കൂ", CTA_NAME,
 cap_ml="ദുബായിലെ ഇൻഷുറൻസ് ഓഫീസിൽ ജോലി ചെയ്യുന്ന NRI-ക്ക് നാട്ടിലെ ഏജൻസിക്ക് 'Insurance' ഉള്ള കമ്പനി പേര് വേണം. Insurance, Bank പോലുള്ള വാക്കുകൾക്ക് പ്രത്യേക അനുമതി വേണം, ഇല്ലെങ്കിൽ പേര് റിജക്ട് ആകാം. ലോഗോയ്ക്ക് മുമ്പ് പേര് ഉറപ്പിക്കൂ.",
 cap_en="An NRI working in a Dubai insurance office wants 'Insurance' in the company name of her new agency in Kerala. Restricted words like Insurance or Bank need special approval and can get a company name rejected. Settle the name before you design the logo.",
 cap_mg="Dubai insurance office-il work cheyyunna NRI-kku naattile agency-kku 'Insurance' ulla company name venam. Insurance, Bank pole ulla words-nu special approval venam, illenkil name reject aakum. Logo cheyyunnathinu munpu company name urappikku.")

# mall: Sumayya + Jafar. Jafar sells phones in a Dubai mall and starts a phone-accessories brand with his sister in Kerala; she lives in a rented flat.
duo("d1309", "nri", "B", "mall", "ദുബായ് മാളിൽ ഫോൺ വിൽപ്പന.\nനാട്ടിൽ അനിയത്തിയുമായി\nസ്വന്തം ബ്രാൻഡ്", [
 ("V","wide","സുമയ്യ, ഈ ചാർജർ കവർ കണ്ടോ? നാട്ടിൽ ഇത് നമ്മുടെ ബ്രാൻഡിൽ ഇറക്കാൻ പോകുന്നു."),
 ("A","A","ജാഫറേ, നീയും അനിയത്തിയും കൂടിയല്ലേ? കമ്പനി ആക്കിയോ?"),
 ("V","V","ആക്കണം. ഓൺലൈൻ സ്റ്റോറുകൾ രജിസ്റ്റേർഡ് കമ്പനിയിൽ നിന്നേ എടുക്കൂ. പ്രശ്നം ഓഫീസ് അഡ്രസ്സ്."),
 ("V","V","അനിയത്തി താമസിക്കുന്നത് വാടക ഫ്ലാറ്റിലാ. അത് ഓഫീസ് ആക്കാൻ പറ്റില്ലല്ലോ."),
 ("A","wide","പറ്റും. ഫ്ലാറ്റിന്റെ ഉടമയുടെ NOC വേണം. കൂടെ പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും."),
 ("A","A","കറന്റ് ബില്ല് ഉടമയുടെ പേരിലാണെങ്കിലും കുഴപ്പമില്ല. പുതിയതായിരിക്കണം എന്ന് മാത്രം."),
 ("V","V","ഉടമ ഒരു റിട്ടയേർഡ് മാഷാ. സമ്മതിക്കുമോ ആവോ?"),
 ("A","A","ഒരു നല്ല ഫോൺ കവർ സമ്മാനം കൊടുത്ത് ചോദിക്ക്. മാഷുമാർക്ക് ഫോൺ താഴെ വീഴും!"),
 ("V","wide","ഐഡിയ കൊള്ളാം. NOC-ക്ക് ആദ്യത്തെ കവർ മാഷിന്!")],
 "വാടക ഫ്ലാറ്റും\nഓഫീസ് ആക്കാം", CTA_DOCS,
 cap_ml="ദുബായ് മാളിൽ ജോലി ചെയ്യുന്ന NRI-യും നാട്ടിലെ അനിയത്തിയും ചേർന്ന് ഫോൺ ആക്സസറി ബ്രാൻഡ്. അനിയത്തിയുടെ വാടക ഫ്ലാറ്റും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം: ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും മതി. NRI-ക്ക് ഡയറക്ടർ ആകാം.",
 cap_en="An NRI who sells phones in a Dubai mall starts a phone-accessories brand in Kerala with his sister. Her rented flat can be the company's registered office with the owner's NOC and a recent utility bill, and NRIs can be directors and shareholders.",
 cap_mg="Dubai mall-il work cheyyunna NRI-yum naattile aniyathiyum chernnu phone accessories brand. Aniyathiyude rented flat-um registered office aakkam, owner-nte NOC-um puthiya utility bill-um mathi. Company registration documents ready aakku.")

# airport: Shameer + Rafeeq. Rafeeq lands from Muscat with letters from three Gulf colleagues who want 10% each of his cold-storage business, registered last month as an LLP.
duo("d1310", "nri", "A", "airport", "മസ്കറ്റിൽ നിന്ന് വന്നത്\nമൂന്ന് ഇൻവെസ്റ്റർ കത്തുമായി.\nകമ്പനി LLP", [
 ("A","wide","റഫീഖേ, ബാഗിനേക്കാൾ ശ്രദ്ധിച്ച് ആ ഫയൽ പിടിച്ചിരിക്കുന്നത് എന്താ?"),
 ("V","V","ഷമീർക്കാ, ഇത് സ്വർണമാ. മസ്കറ്റിലെ മൂന്ന് കൂട്ടുകാരുടെ കത്ത്. കോൾഡ് സ്റ്റോറേജിൽ ഓരോരുത്തർക്കും പത്ത് ശതമാനം വേണം."),
 ("A","A","അടിപൊളി! കമ്പനി കഴിഞ്ഞ മാസം രജിസ്റ്റർ ചെയ്തില്ലേ?"),
 ("V","V","ചെയ്തു. LLP ആയിട്ട്. കൂട്ടുകാരൻ പറഞ്ഞു അതാ എളുപ്പമെന്ന്."),
 ("A","wide","അതാ പ്രശ്നം. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡിനേ പറ്റൂ. LLP-ക്കും പാർട്ണർഷിപ്പിനും പറ്റില്ല."),
 ("V","V","അപ്പോ ഈ മൂന്ന് കത്ത്?"),
 ("A","A","കത്ത് കളയണ്ട. ഇൻവെസ്റ്റ്മെന്റ് വേണമെങ്കിൽ സ്ട്രക്ചർ പ്രൈവറ്റ് ലിമിറ്റഡ് ആകണം. ആദ്യം അത് ഉറപ്പിക്ക്."),
 ("V","V","പ്ലെയിനിൽ ഇരുന്ന് ഞാൻ അവർക്ക് ഷെയർ സർട്ടിഫിക്കറ്റ് വരെ ഡിസൈൻ ചെയ്തു!"),
 ("A","wide","ഡിസൈൻ സൂക്ഷിച്ച് വെക്ക്. ശരിയായ കമ്പനി വരുമ്പോൾ ഉപയോഗിക്കാം!")],
 "നിക്ഷേപം വേണോ?\nLLP പോരാ", CTA_START,
 cap_ml="മസ്കറ്റിലെ കൂട്ടുകാർ നാട്ടിലെ കോൾഡ് സ്റ്റോറേജ് ബിസിനസിൽ ഷെയർ ചോദിച്ചു, പക്ഷേ കമ്പനി LLP ആയിട്ടാണ് രജിസ്റ്റർ ചെയ്തത്. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ. LLP-ക്കും പാർട്ണർഷിപ്പിനും പറ്റില്ല.",
 cap_en="An NRI back from Muscat brings investment letters from three Gulf colleagues, but his Kerala cold-storage business was registered as an LLP. Only a private limited company can take equity investment; an LLP or partnership cannot issue shares to investors.",
 cap_mg="Muscat-ile friends cold storage business-il share chodichu, pakshe company LLP aayittaanu register cheythathu. Share koduthu investment edukkan Pvt Ltd-nu maathrame pattu. LLP vs Pvt Ltd: investors undenkil Pvt Ltd thanne.")

# chat: Ancy, a nurse in Germany, wants shares in her brother's bakery company but no director post; she asks who signs then.
chat("c952", "nri", "B", "ജർമനിയിലെ നഴ്സ്:\n\"ഷെയർ മതി.\nഡയറക്ടർ ഒന്നും ആക്കണ്ട\"", ("ആൻസി", "അനിയൻ"), [
 (0,"ഡാ, നിന്റെ ബേക്കറി കമ്പനിയിൽ ഞാൻ പൈസ ഇടാം. പക്ഷേ ഒരു കണ്ടീഷൻ."),
 (1,"ചേച്ചി എന്ത് പറഞ്ഞാലും സമ്മതം. കണ്ടീഷൻ പറ."),
 (0,"ഷെയർ മതി. ഡയറക്ടർ ഒന്നും ആക്കണ്ട. ഇവിടെ നൈറ്റ് ഷിഫ്റ്റിന് ഇടയിൽ ഒപ്പിടാൻ എനിക്ക് പറ്റില്ല."),
 (1,"NRI-ക്ക് ഷെയർഹോൾഡർ മാത്രമായി നിൽക്കാം. പക്ഷേ ഒരു പ്രശ്നം."),
 (1,"പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ വേണം. ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ. അത് ഞാൻ."),
 (0,"അപ്പോ രണ്ടാമത്തെ ഡയറക്ടർ?"),
 (1,"ചേച്ചി അല്ലെങ്കിൽ നാട്ടിലുള്ള വേറെ ഒരാൾ. അമ്മ ഓക്കേ ആണോന്ന് ചോദിക്കാം."),
 (0,"അമ്മ ഡയറക്ടർ! ഇനി ബേക്കറിയിലെ കേക്കിന് മധുരം കൂടും, കണക്കിന് കൃത്യതയും."),
 (1,"അപ്പോ ചേച്ചി ഷെയർ, ഞാനും അമ്മയും ഡയറക്ടർ. ഡീൽ!")],
 "ഷെയർ മാത്രം മതിയോ?\nഡയറക്ടർ രണ്ടുപേർ\nവേറെ വേണം", CTA_START,
 cap_ml="ജർമനിയിൽ നഴ്സായ ചേച്ചിക്ക് അനിയന്റെ ബേക്കറി കമ്പനിയിൽ ഷെയർ മാത്രം മതി, ഡയറക്ടർ ആകണ്ട. NRI-ക്ക് ഷെയർഹോൾഡർ ആകാം. പക്ഷേ Pvt Ltd കമ്പനിക്ക് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ വേണം, അതിൽ ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ.",
 cap_en="A Malayali nurse in Germany wants to invest in her brother's bakery company in Kerala as a shareholder only, not a director. NRIs can hold shares, but a private limited company still needs at least two directors, one of them resident in India.",
 cap_mg="Germany-yil nurse aaya chechikku aniyante bakery company-il share mathi, director aakanda. NRI-kku shareholder aakaam. Pakshe Pvt Ltd company-kku minimum 2 directors venam, athil oraal India-yil thamasikkunna aal.")

lst("l952", "nri", "C", "ലീവ് 30 ദിവസം.\nനാട്ടിൽ കമ്പനി തുടങ്ങണം.\nലീവ് പ്ലാൻ 3 സ്റ്റെപ്പിൽ", [
 ("ലാൻഡ് ചെയ്യുന്ന ആഴ്ച: പേരും ഡോക്യുമെന്റ്സും", "മൂന്ന് പേര് കരുതൂ. സാമ്യമുള്ള പേര് റിജക്ട് ആകാം."),
 ("അടുത്ത 2-3 ആഴ്ച: രജിസ്ട്രേഷൻ", "Pvt Ltd-ന് സാധാരണ 7-15 പ്രവൃത്തി ദിവസം. നാട്ടിലുള്ള ഒരു ഡയറക്ടർ നിർബന്ധം."),
 ("ഫ്ലൈറ്റിന് മുമ്പ്: തീയതികൾ കൈമാറുക", "30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A. നാട്ടിലെ ഡയറക്ടറുടെ കലണ്ടറിൽ.")],
 "ലീവ് തീരും മുമ്പ്\nകമ്പനി റെഡി", CTA_AFTER,
 cap_ml="30 ദിവസത്തെ ലീവിൽ നാട്ടിൽ വന്ന് കമ്പനി തുടങ്ങാൻ പ്ലാൻ ഉള്ള NRI-കൾക്ക്: ആദ്യ ആഴ്ച കമ്പനി പേരും ഡോക്യുമെന്റ്സും, പിന്നെ 7-15 പ്രവൃത്തി ദിവസത്തെ രജിസ്ട്രേഷൻ, പോകും മുമ്പ് ഓഡിറ്ററും INC-20A തീയതികളും നാട്ടിലെ ഡയറക്ടറെ ഏൽപ്പിക്കുക.",
 cap_en="Coming home on a 30-day leave to start a company in Kerala? Week one: company name and documents. Next two to three weeks: Pvt Ltd registration with a resident director. Before you fly back: hand over the 30-day auditor and 180-day INC-20A dates.",
 cap_mg="30 days leave-il naattil vannu company register cheyyan plan undo? First week company name-um documents-um, pinne 7-15 working days registration, flight-nu munpu auditor-um INC-20A dates-um naattile director-ne elpikkuka.")

# ---------------- solo ----------------
# munnar: Celine + Basil. Celine guides treks alone; a Bengaluru offsite company books monthly treks with company invoices; she lives in a rented room above a spice shop.
duo("d1311", "solo", "A", "munnar", "ഒറ്റയ്ക്ക് ട്രെക്കിംഗ് ഗൈഡ്.\nബെംഗളൂരു കമ്പനി പറഞ്ഞു:\n\"എല്ലാ മാസവും ഒരു ബാച്ച്\"", [
 ("V","wide","സെലിൻ, ഇന്ന് ട്രെക്കിംഗ് ഇല്ലേ? മലയുടെ മുകളിൽ ഇരുന്ന് ഫോണിലാണല്ലോ."),
 ("A","A","ബേസിലേ, ബെംഗളൂരുവിലെ ഒരു ഓഫ്സൈറ്റ് കമ്പനി. എല്ലാ മാസവും ഒരു ബാച്ച് ട്രെക്കിംഗിന് എന്റെ കൂടെ വിടുമെന്ന്."),
 ("V","V","ഒറ്റയ്ക്ക് ഗൈഡ് ചെയ്യുന്നവൾക്ക് സ്ഥിരം കസ്റ്റമർ! പിന്നെന്താ മുഖത്ത് മൂടൽമഞ്ഞ്?"),
 ("A","A","ഇൻവോയ്സ് കമ്പനിയുടേത് ആകണം. ഒറ്റയ്ക്ക് OPC തുടങ്ങാം. പക്ഷേ ഓഫീസ്? ഞാൻ താമസിക്കുന്നത് ആ സ്പൈസ് കടയുടെ മുകളിലെ വാടക മുറിയിലാ."),
 ("V","wide","അത് മതി. വാടക മുറിയും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. കെട്ടിട ഉടമയുടെ NOC വേണം."),
 ("V","V","കൂടെ പുതിയ ഒരു കറന്റ് ബില്ല്. പഴയത് പോരാ."),
 ("A","A","ഉടമ താഴെ ഏലക്ക തൂക്കുന്ന അച്ചായനാ. NOC-ക്ക് എന്ത് കൊടുക്കും?"),
 ("V","V","അടുത്ത ട്രെക്കിംഗിന് അച്ചായനെ ഫ്രീ ആയി കൊണ്ടുപോ. മല കയറി ക്ഷീണിക്കുമ്പോൾ ഒപ്പിടും!"),
 ("A","wide","ശരി! ഇന്ന് വൈകിട്ട് ഇറങ്ങുമ്പോൾ NOC-യും ബില്ലും എടുക്കാം.")],
 "വാടക മുറിയിൽ നിന്നും\nകമ്പനി തുടങ്ങാം", CTA_DOCS,
 cap_ml="മൂന്നാറിൽ ഒറ്റയ്ക്ക് ട്രെക്കിംഗ് ഗൈഡ് ചെയ്യുന്നയാൾക്ക് ബെംഗളൂരു കമ്പനിയുടെ സ്ഥിരം ബുക്കിംഗ്, പക്ഷേ ഇൻവോയ്സ് കമ്പനിയുടേത് വേണം. ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം. വാടക മുറിയും ഓഫീസ് ആക്കാം, ഉടമയുടെ NOC-യും പുതിയ ബില്ലും മതി.",
 cap_en="A solo trekking guide in Munnar gets monthly bookings from a Bengaluru company that needs company invoices. A solo founder can form a One Person Company (OPC), and even a rented room can be the registered office with the owner's NOC and a recent utility bill.",
 cap_mg="Munnar-il ottaykku trekking guide cheyyunna aalkku Bengaluru company-yude monthly booking, pakshe invoice company-yudethu venam. Ottaykku aanenkil one person company (OPC) thudangaam. Rent room-um office aakkam, owner NOC-um puthiya bill-um mathi.")

# homestay: Teena + Jomon. Teena teaches Kerala cooking alone at her homestay; a cruise line wants weekly classes for passengers and she picked "Teena's Kitchen".
duo("d1312", "solo", "B", "homestay", "ക്രൂയിസ് കപ്പലിലെ\nയാത്രക്കാർക്ക് എല്ലാ ആഴ്ചയും\nനമ്മുടെ കുക്കിംഗ് ക്ലാസ്", [
 ("V","wide","ടീനേച്ചീ, ഇന്ന് അടുക്കളയിൽ പത്ത് വിദേശികൾ അവിയൽ ഇളക്കുന്നു!"),
 ("A","A","ജോമോനേ, അത് സാമ്പിൾ ക്ലാസ്. ഒരു ക്രൂയിസ് കമ്പനി എല്ലാ ആഴ്ചയും അവരുടെ യാത്രക്കാരെ ഇവിടെ കൊണ്ടുവരാം എന്ന്."),
 ("V","V","ചേച്ചി ഒറ്റയ്ക്ക് തുടങ്ങിയ കുക്കിംഗ് ക്ലാസ് ഇനി കപ്പലിൽ കയറി!"),
 ("A","A","പക്ഷേ കോൺട്രാക്ട് കമ്പനിയുമായി മാത്രം. ഞാൻ OPC ആക്കുന്നു. പേര് റെഡി: ടീനാസ് കിച്ചൻ."),
 ("V","V","ചേച്ചീ, ഗൂഗിളിൽ ടീനാസ് കിച്ചൻ എന്ന് അടിച്ചാൽ എത്ര എണ്ണം വരും എന്ന് നോക്കിയോ?"),
 ("V","wide","നിലവിലുള്ള കമ്പനിയോടോ LLP-യോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യമുള്ള പേര് റിജക്ട് ആകാം."),
 ("A","A","അയ്യോ. ഞാൻ ഏപ്രൺ വരെ പ്രിന്റ് ചെയ്യാൻ കൊടുത്തു!"),
 ("V","V","ഏപ്രൺ അടുക്കളയിൽ ഇട്ടോ. കമ്പനിക്ക് നാടിന്റെയോ തറവാടിന്റെയോ പേര് ചേർത്ത് മൂന്ന് ഓപ്ഷൻ ആലോചിക്ക്."),
 ("A","wide","ശരി. അവിയലിൽ എല്ലാം ഇടാം. പേരിൽ സാമ്യം മാത്രം ഇടില്ല!")],
 "ഏപ്രൺ പ്രിന്റ് ചെയ്യും മുമ്പ്\nപേര് ചെക്ക് ചെയ്യൂ", CTA_NAME,
 cap_ml="ഹോംസ്റ്റേയിൽ ഒറ്റയ്ക്ക് കേരള കുക്കിംഗ് ക്ലാസ് നടത്തുന്നവർക്ക് ക്രൂയിസ് കമ്പനിയുടെ ആഴ്ചതോറുമുള്ള ബുക്കിംഗ്. OPC-ക്ക് ഇട്ട പേര് പലരും ഉപയോഗിക്കുന്നത്. നിലവിലുള്ള കമ്പനിയോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകാം.",
 cap_en="A solo homestay host who teaches Kerala cooking gets weekly cruise bookings and picks a very common name for her One Person Company. A company name similar to an existing company, LLP or trademark can be rejected, so check before printing anything.",
 cap_mg="Homestay-il ottaykku cooking class nadathunna chechikku cruise company booking. OPC-kku itta peru common aanu. Existing company, LLP allenkil trademark-umaayi saamyam ulla company name reject aakaam, print cheyyum munpu check cheyyu.")

# veranda: Shantha + Balan. Shantha, a retired Malayalam teacher, records children's audiobooks alone as an OPC; the publisher pays only next year, so she plans no filing this year.
duo("d1313", "solo", "A", "veranda", "62-ാം വയസ്സിൽ OPC.\nകുട്ടികളുടെ ഓഡിയോബുക്ക്.\nപൈസ വരുന്നത് അടുത്ത വർഷം", [
 ("V","wide","ശാന്ത ടീച്ചറേ, വരാന്തയിൽ മൈക്ക് ഒക്കെ വെച്ച് റേഡിയോ നിലയമാണോ?"),
 ("A","A","ബാലേട്ടാ, കുട്ടികൾക്കുള്ള കഥകൾ. ഒരു പബ്ലിഷർ എന്റെ ശബ്ദത്തിൽ ഓഡിയോബുക്ക് സീരീസ് ഇറക്കുന്നു. ഒറ്റയ്ക്ക് OPC ആക്കി."),
 ("V","V","റിട്ടയർ ചെയ്തിട്ട് കമ്പനി! ഇനി ടീച്ചർ അല്ല, എംഡി!"),
 ("A","A","പക്ഷേ ആദ്യത്തെ പൈസ അടുത്ത വർഷമേ വരൂ. അതുകൊണ്ട് ഈ വർഷം കണക്കും ഫയലിംഗും ഒന്നും വേണ്ടല്ലോ."),
 ("V","wide","അത് വേണം ടീച്ചറേ. വരുമാനം ഇല്ലെങ്കിലും ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്."),
 ("V","V","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ വെച്ച് ലേറ്റ് ഫീ കയറും."),
 ("A","A","ദിവസം നൂറ്! ഹോംവർക്ക് വൈകിയാൽ ഞാൻ പോലും ഇത്ര ശിക്ഷ കൊടുത്തിട്ടില്ല."),
 ("V","V","അതുകൊണ്ട് ഡ്യൂ ഡേറ്റ് ബോർഡിൽ എഴുതി വെക്ക്. ക്ലാസിൽ ചെയ്തതുപോലെ."),
 ("A","wide","ശരി. ഇത്തവണ ഹോംവർക്ക് ടീച്ചർക്ക് തന്നെ!")],
 "വരുമാനം പൂജ്യമായാലും\nഫയലിംഗ് വേണം", CTA_AFTER,
 cap_ml="റിട്ടയർ ചെയ്ത മലയാളം ടീച്ചർ ഒറ്റയ്ക്ക് OPC തുടങ്ങി കുട്ടികളുടെ ഓഡിയോബുക്ക് ചെയ്യുന്നു, വരുമാനം അടുത്ത വർഷം. വരുമാനം ഇല്ലാത്ത വർഷവും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസക്കണക്കിന് ലേറ്റ് ഫീ.",
 cap_en="A retired Malayalam teacher starts a One Person Company for children's audiobooks, with the first income due next year. Annual ROC filings are due even with zero revenue, and late filing adds a daily penalty for every form.",
 cap_mg="Retire cheytha Malayalam teacher ottaykku OPC thudangi, audiobook income adutha varsham. Revenue illatha varshavum annual filing nirbandham aanu. Late aayaal oro form-inum daily late penalty kerum.")

# thattukada: Sijo + Biju. Sijo runs a biriyani food truck alone; an IT park wants it inside the campus on a vendor contract. Biju volunteers as "partner" for free biriyani.
duo("d1314", "solo", "B", "thattukada", "ഫുഡ് ട്രക്ക് ഇനി\nIT പാർക്കിനുള്ളിൽ.\n\"പാർട്ണർ ആയി ഞാനുണ്ട്\"", [
 ("V","wide","സിജോ, ഇന്ന് ട്രക്കിന് മുന്നിൽ ലാപ്ടോപ്പ് ബാഗുകളുടെ ക്യൂ ആണല്ലോ!"),
 ("A","A","ബിജുവേട്ടാ, IT പാർക്കിലെ അഡ്മിൻ ടീം. ആഴ്ചയിൽ അഞ്ച് ദിവസം ട്രക്ക് കാമ്പസിനുള്ളിൽ ഇടാം എന്ന്."),
 ("V","V","അടിപൊളി! പിന്നെന്താ മുഖം വാടിയ ബിരിയാണി പോലെ?"),
 ("A","A","വെണ്ടർ കോൺട്രാക്ട് കമ്പനിയുമായി മാത്രം. ഞാൻ ഒറ്റയ്ക്കാ. കമ്പനിക്ക് പാർട്ണർ വേണ്ടേ?"),
 ("V","V","ഞാനുണ്ടല്ലോ! പാർട്ണർ ഞാൻ. ദിവസവും ഒരു ബിരിയാണി ഫ്രീ, അത്രേ വേണ്ടൂ."),
 ("A","wide","ചേട്ടാ, ഒറ്റയ്ക്ക് തുടങ്ങുന്നവർക്ക് വൺ പേഴ്സൺ കമ്പനി, OPC ഉണ്ട്. പാർട്ണർ വേണ്ട."),
 ("V","V","അപ്പോ എന്റെ ഫ്രീ ബിരിയാണി?"),
 ("A","A","അത് പാർട്ണർഷിപ്പ് ഇല്ലാതെയും തരാം. ഷെയർ ചോദിക്കരുത് എന്ന് മാത്രം!"),
 ("V","wide","ഡീൽ! ഇന്ന് മുതൽ ഞാൻ വെറും കസ്റ്റമർ. ലെഗ് പീസ് ഉള്ളത്!")],
 "ഒറ്റയ്ക്കാണോ?\nപാർട്ണറെ തേടണ്ട", CTA_START,
 cap_ml="ഒറ്റയ്ക്ക് ബിരിയാണി ഫുഡ് ട്രക്ക് നടത്തുന്നയാൾക്ക് IT പാർക്കിനുള്ളിൽ വെണ്ടർ കോൺട്രാക്ട്, പക്ഷേ കമ്പനി വേണം. കമ്പനി തുടങ്ങാൻ പാർട്ണർ നിർബന്ധമില്ല. ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) രജിസ്റ്റർ ചെയ്യാം.",
 cap_en="A solo food truck owner in Kochi gets an IT park vendor contract that needs a company, and a friend offers to be his partner. You don't need a partner: a solo founder can register a One Person Company (OPC).",
 cap_mg="Ottaykku biriyani food truck nadathunna aalkku IT park vendor contract, pakshe company venam. Company thudangan partner venda. Ottaykku aanenkil one person company (OPC) register cheyyaam.")

# farm: Vasu + Gopi. Vasu's goat farm became an OPC six and a half months ago for an exporter's yearly contract; no INC-20A filed.
duo("d1315", "solo", "A", "farm", "ആട് ഫാം OPC ആക്കിയിട്ട്\nആറര മാസം.\nഒരു ഫോം മറന്നു", [
 ("V","wide","വാസുവേട്ടാ, ആടുകൾക്ക് പുതിയ ഷെഡ്! കയറ്റുമതിക്കാരന്റെ കോൺട്രാക്ട് കൊണ്ട് കാര്യം നടന്നല്ലോ."),
 ("A","A","ഗോപീ, അതിന് വേണ്ടിയല്ലേ ആറര മാസം മുമ്പ് OPC ആക്കിയത്. ഒറ്റയ്ക്ക് നോക്കുന്ന ഫാമിന് കമ്പനി പേര്!"),
 ("V","V","എന്നിട്ട് ബിസിനസ് തുടങ്ങിയെന്ന ഡിക്ലറേഷൻ, INC-20A, കൊടുത്തോ?"),
 ("A","A","അതെന്താ? ആട് വളർത്താൻ വേറെ ഡിക്ലറേഷനോ?"),
 ("V","wide","കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യേണ്ട ഫോമാ. ആറ് മാസം കഴിഞ്ഞു."),
 ("V","V","വൈകിയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ, പരമാവധി ഒരു ലക്ഷം."),
 ("A","A","അയ്യോ! ഒരു ആടിനെ വിറ്റാലും തീരില്ലല്ലോ."),
 ("V","V","അതുകൊണ്ട് ഇന്ന് തന്നെ ആരെയെങ്കിലും കൊണ്ട് നോക്കിക്ക്. ഇനി വൈകിക്കരുത്."),
 ("A","wide","ഇനി ആടിന് തീറ്റ കൊടുക്കുന്ന ദിവസം പോലെ ഫോമിന്റെ ദിവസവും ഞാൻ മറക്കില്ല!")],
 "180 ദിവസം\nകടന്നുപോയോ?\nഇന്ന് തന്നെ നോക്കൂ", CTA_AFTER,
 cap_ml="ഒറ്റയ്ക്ക് നടത്തുന്ന ആട് ഫാം OPC ആക്കിയിട്ട് ആറര മാസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 180 ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം. വൈകിയാൽ കമ്പനിക്കും ഡയറക്ടർക്കും പിഴയുണ്ട്.",
 cap_en="A solo goat farmer in Kerala turned his farm into a One Person Company for an export contract, and six and a half months later INC-20A is still not filed. INC-20A is due within 180 days of incorporation; missing it brings penalties on the company and the director.",
 cap_mg="Ottaykku nadathunna aadu farm OPC aakkiyittu aarara maasam, INC-20A file cheythilla. Company register cheythu 180 days-inullil INC-20A file cheyyanam. Late aayaal company-kkum director-kkum penalty undu.")

# chat: Haris shoots wedding drone videos alone; a real-estate developer wants monthly site drone surveys from a company; he is saving for a second drone first.
chat("c953", "solo", "B", "കല്യാണത്തിന് ഡ്രോൺ.\nബിൽഡർ ചോദിച്ചു:\n\"എല്ലാ മാസവും സൈറ്റ് ഷൂട്ട്?\"", ("ഹാരിസ്", "ശരണ്യ"), [
 (0,"ശരണ്യേ, ആ ഫ്ലാറ്റ് ബിൽഡർ വിളിച്ചു. അവരുടെ എല്ലാ സൈറ്റും മാസത്തിൽ ഒരിക്കൽ ഡ്രോണിൽ ഷൂട്ട് ചെയ്യണം."),
 (1,"കല്യാണ സീസൺ കഴിഞ്ഞാലും പണി! എന്നാ തുടങ്ങുന്നത്?"),
 (0,"അവർക്ക് കമ്പനി ഇൻവോയ്സ് വേണം. കമ്പനി ആക്കാൻ ആദ്യം രണ്ടാമത്തെ ഡ്രോൺ വാങ്ങി ക്യാപിറ്റൽ കാണിക്കണം. അതിന് പൈസ സേവ് ചെയ്യുന്നു."),
 (1,"ആര് പറഞ്ഞു? കമ്പനി തുടങ്ങാൻ മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 (0,"ശരിക്കും? പക്ഷേ ഞാൻ ഒറ്റയ്ക്കാ. ക്യാമറയും ഡ്രോണും ഞാനും."),
 (1,"ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി, OPC. ഡ്രോൺ ഡയറക്ടർ ആകണ്ട."),
 (0,"അപ്പോ രണ്ടാമത്തെ ഡ്രോൺ?"),
 (1,"ബിൽഡറുടെ ആദ്യ രണ്ട് മാസത്തെ പണി കഴിയുമ്പോൾ അത് തന്നെ വരും. ആദ്യം കമ്പനി."),
 (0,"ശരി. ഇന്ന് ഡ്രോൺ താഴെ ഇറക്കി ഡോക്യുമെന്റ്സ് എടുക്കാം.")],
 "രണ്ടാം ഡ്രോണിന്\nകാത്തിരിക്കണ്ട", CTA_START,
 cap_ml="കല്യാണങ്ങൾക്ക് ഒറ്റയ്ക്ക് ഡ്രോൺ ഷൂട്ട് ചെയ്യുന്നയാൾക്ക് ബിൽഡറുടെ മാസം തോറുമുള്ള സൈറ്റ് ഷൂട്ട് ഓഫർ, ഇൻവോയ്സ് കമ്പനിയുടേത് വേണം. ക്യാപിറ്റൽ കാണിക്കാൻ പുതിയ ഉപകരണം വാങ്ങേണ്ട, മിനിമം ക്യാപിറ്റൽ നിർബന്ധമില്ല. ഒറ്റയ്ക്കാണെങ്കിൽ OPC.",
 cap_en="A solo wedding drone photographer is offered monthly site shoots by a real-estate developer who needs company invoices. He thought he had to buy a second drone to show capital, but there is no minimum paid-up capital, and a solo founder can start a One Person Company.",
 cap_mg="Kalyanathinu ottaykku drone shoot cheyyunna aalkku builder-inte monthly site shoot offer, invoice company-yudethu venam. Capital kaanikkan puthiya drone vaanganda, minimum capital nirbandham illa. Ottaykku aanenkil OPC thudangaam.")
