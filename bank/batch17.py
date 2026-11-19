# Script bank, batch 17. New situations: a night porotta stall a film unit wants for 40 days of shooting, two tempo travellers a
# Bengaluru travel startup wants 25% of, home catering a hospital wants for two years of patient meals (house in his mother's name),
# a boat-repair yard naming itself "Alappuzha Boat Yard", hotel-linen laundry for five hotels at month four, a spice mill an exporter
# wants five tonnes a month from, a "big order, first week" checklist; a Kuwait driver funding his brother's phone-repair shops for
# shares, a Bahrain worker who thinks the government sends the auditor, a Qatar engineer's CCTV company run from his mother's house,
# a Dubai couple who want the company done inside three weeks of leave, a man back from Oman who wants an airline's name on his spice
# packs, a New Zealand nurse home for his wife's delivery, a Saudi nurse's 30-day leave and her son's cycle-rental; a video-CV maker
# told she needs a partner, an LED-wall renter at day 160, a bridal fitness trainer with two weeks to a contract, a banana-chips
# shipper working from his father-in-law's house, a children's storyteller named like an existing company, a calligrapher at day 28.
# Same fact list and no-price rule as batch01. Segments proprietor 7, nri 7, solo 6; 16 duo3d in 16 different locations (none used
# in batch16). Proprietor scripts again open on money waiting on the table (the d401 pattern); share kept at 7/40, no shift.
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
# thattukada: Sijo + Biju. A film unit wants Biju's porotta and beef for 120 crew every night for 40 days; invoices only from a company; shoot starts in 3 weeks.
duo("d1901", "proprietor", "A", "thattukada", "സിനിമ ഷൂട്ടിംഗ് ടീം:\n\"40 ദിവസം, 120 പേർക്ക്\nരാത്രി പൊറോട്ട\"", [
 ("A","wide","ബിജൂ, ആ കാറിൽ വന്ന താടിക്കാരൻ ആരാ? മൂന്ന് പ്ലേറ്റ് ബീഫ് തീർത്തല്ലോ."),
 ("V","V","സിജോ, സിനിമയുടെ പ്രൊഡക്ഷൻ മാനേജർ! അടുത്ത മാസം ഇവിടെ ഷൂട്ടിംഗ്. നാൽപ്പത് ദിവസം നൂറ്റിയിരുപത് പേർക്ക് രാത്രി ഭക്ഷണം."),
 ("A","A","നമ്മുടെ തട്ടുകടയിൽ നിന്ന്? ഹീറോയും നമ്മുടെ പൊറോട്ട തിന്നും!"),
 ("V","V","പക്ഷേ ബില്ല് കമ്പനി പേരിൽ വേണം. ഷൂട്ടിംഗ് തുടങ്ങാൻ മൂന്ന് ആഴ്ച മാത്രം."),
 ("A","wide","എങ്കിൽ ഇന്ന് തന്നെ തുടങ്ങണം. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("V","V","ഡോക്യുമെന്റ്സ് എന്തൊക്കെ വേണം?"),
 ("A","A","രണ്ട് ഡയറക്ടർമാരുടെ ഡോക്യുമെന്റ്സും ഓഫീസ് അഡ്രസ്സിന്റെ പേപ്പറും. ലിസ്റ്റ് നാളെ രാവിലെ ചോദിക്കാം."),
 ("V","wide","ശരി. ആദ്യ ദിവസത്തെ ഷോട്ട്: ബിജു ആൻഡ് കമ്പനി, പൊറോട്ട അടിക്കുന്നു!")],
 "ഷൂട്ടിംഗിന് മുമ്പ്\nകമ്പനി റെഡി", CTA_DOCS,
 cap_ml="രാത്രി പൊറോട്ടയും ബീഫും വിൽക്കുന്ന തട്ടുകടയ്ക്ക് സിനിമ ഷൂട്ടിംഗ് ടീമിന്റെ 40 ദിവസത്തെ ഓർഡർ, 120 പേർക്ക്; ബില്ല് കമ്പനി പേരിൽ വേണം. ഷൂട്ടിംഗിന് മൂന്ന് ആഴ്ച; പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="A night food stall in Kerala gets a film unit's order: dinner for 120 crew for 40 days, invoiced by a company, starting in three weeks. Private limited company registration usually takes 7-15 working days, so the documents start today.",
 cap_mg="Raathri porottayum beef-um vilkkunna thattukadaykku cinema shooting team-nte 40 divasathe order, 120 perkku; bill company peril venam. Shooting-nu 3 aazhcha; Pvt Ltd register cheyyan saadharana 7-15 working days.")

# autostand: Saji + Shaji. Shaji owns two tempo travellers; a Bengaluru travel startup will fund three more for 25% of his business. He is a proprietor.
duo("d1902", "proprietor", "A", "autostand", "രണ്ട് ടെമ്പോ ട്രാവലർ.\nബാംഗ്ലൂർ സ്റ്റാർട്ടപ്പ്:\n\"3 എണ്ണം കൂടി, 25% തരൂ\"", [
 ("A","wide","ഷാജീ, നിന്റെ വണ്ടി ഇന്നും മൂന്നാറിൽ നിന്ന് വന്നതേ ഉള്ളോ?"),
 ("V","V","സജിയേട്ടാ, ഈ മാസം ഇരുപത്തിരണ്ട് ട്രിപ്പ്! ഒരു ബാംഗ്ലൂർ ട്രാവൽ സ്റ്റാർട്ടപ്പ് വിളിച്ചിരുന്നു."),
 ("V","V","മൂന്ന് വണ്ടി കൂടി വാങ്ങാൻ അവർ പൈസ ഇടും. പകരം ഇരുപത്തിയഞ്ച് ശതമാനം ഷെയർ."),
 ("A","A","ഷെയറോ? നിന്റെ ബിസിനസ് നിന്റെ പേരിൽ മാത്രം അല്ലേ? അതിൽ ഷെയർ എങ്ങനെ കൊടുക്കും?"),
 ("A","wide","ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിനും പാർട്ണർഷിപ്പിനും പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി. രണ്ട് ഡയറക്ടർ വേണ്ടേ?"),
 ("A","A","വേണം. നിന്റെ അനിയൻ രണ്ടാമത്തെ വണ്ടി ഓടിക്കുന്നില്ലേ? അവൻ തന്നെ."),
 ("V","wide","ശരി. അഞ്ച് വണ്ടി, ഒരു കമ്പനി. സ്റ്റാൻഡിൽ ഇനി എന്നെ മുതലാളീ എന്ന് വിളിക്കണം!")],
 "ഇൻവെസ്റ്റർ ഷെയർ ചോദിച്ചോ?\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="രണ്ട് ടെമ്പോ ട്രാവലർ ഓടിക്കുന്ന ഉടമയ്ക്ക് ബാംഗ്ലൂരിലെ ട്രാവൽ സ്റ്റാർട്ടപ്പ് മൂന്ന് വണ്ടിക്ക് കൂടി പൈസ ഇടാം, പകരം 25% ഷെയർ. പ്രൊപ്രൈറ്റർഷിപ്പിന് ഷെയർ കൊടുക്കാൻ പറ്റില്ല; ആദ്യം 2 ഡയറക്ടറുള്ള Pvt Ltd കമ്പനി.",
 cap_en="A Kerala tempo-traveller owner with two vans is offered funding for three more by a Bengaluru travel startup in exchange for 25%. A proprietorship cannot issue shares; only a private limited company with two directors can take this equity investment.",
 cap_mg="2 tempo traveller odikkunna owner-nu Bangalore travel startup 3 vandikku koodi paisa idaam, pakaram 25% share. Proprietorship-nu share kodukkan pattilla; aadyam 2 director ulla Pvt Ltd company.")

# kitchen: Bindu + Rajesh. A hospital wants Rajesh's home catering for two years of patient meals, from a company; the house is in his mother's name.
duo("d1903", "proprietor", "C", "kitchen", "ആശുപത്രിയിലെ രോഗികൾക്ക്\nരണ്ട് വർഷം ഭക്ഷണം.\nവീട് അമ്മയുടെ പേരിൽ", [
 ("V","wide","ബിന്ദൂ, ആ ആശുപത്രിയുടെ ഡയറ്റീഷ്യൻ ഓക്കെ പറഞ്ഞു! രോഗികൾക്കുള്ള ഭക്ഷണം രണ്ട് വർഷം നമ്മൾ."),
 ("A","A","ഉപ്പ് കുറച്ച്, എണ്ണ കുറച്ച്. ഒരു ദിവസം മുന്നൂറ് പ്ലേറ്റ്! പക്ഷേ കരാർ കമ്പനിയുമായി അല്ലേ?"),
 ("V","V","അതേ. പക്ഷേ നമ്മുടെ അടുക്കള വീട്ടിലല്ലേ? ടൗണിൽ ഓഫീസ് മുറി എടുക്കേണ്ടി വരും."),
 ("A","wide","വേണ്ട. വീട്ടിലെ അഡ്രസ്സ് കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം."),
 ("V","V","വീട് അമ്മയുടെ പേരിലാ."),
 ("A","A","അപ്പോ അമ്മയുടെ NOC വേണം. പിന്നെ വീടിന്റെ പുതിയ കറന്റ് ബില്ലും. അത്രയേ ഉള്ളൂ."),
 ("V","V","അമ്മ ഒപ്പിടും. പക്ഷേ ആദ്യം ചോദിക്കും, ഉപ്പ് എന്തിനാ കുറച്ചതെന്ന്!"),
 ("A","wide","അത് ആശുപത്രിയുടെ റൂൾ. NOC നമ്മുടെ റൂൾ!")],
 "വീട് മറ്റൊരാളുടെ പേരിലോ?\nNOC മതി", CTA_DOCS,
 cap_ml="വീട്ടിലെ അടുക്കളയിൽ നിന്ന് കാറ്ററിംഗ് ചെയ്യുന്നയാൾക്ക് ആശുപത്രിയിലെ രോഗികളുടെ ഭക്ഷണത്തിന് രണ്ട് വർഷത്തെ കരാർ, കമ്പനിയുമായി മാത്രം. വീട് അമ്മയുടെ പേരിൽ ആണെങ്കിലും അമ്മയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A Kerala home caterer wins a two-year contract for a hospital's patient meals, signed only with a company. The house is in his mother's name; with her NOC and a recent electricity bill, home can be the company's registered office, no town office needed.",
 cap_mg="Veettile adukkalayil ninnu catering cheyyunna aalkku hospital-ile rogikalude food-nu 2 varshathe contract, company-yumaayi maathram. Veedu ammayude peril aanenkilum ammayude NOC-um puthiya current bill-um undenkil registered office aakkaam.")

# ferry: Meera + Tony. A houseboat owners' group gives Tony's boat-repair yard yearly maintenance of 40 boats; he wants the company called "Alappuzha Boat Yard".
duo("d1904", "proprietor", "B", "ferry", "40 ഹൗസ്ബോട്ടിന്റെ\nവർഷ മെയിന്റനൻസ്. പേര്:\n\"ആലപ്പുഴ ബോട്ട് യാർഡ്\"", [
 ("A","wide","ടോണീ, ആ ഹൗസ്ബോട്ട് ഉടമകളുടെ മീറ്റിംഗ് എന്തായി?"),
 ("V","V","മീരേ, നാൽപ്പത് ബോട്ടിന്റെ ഒരു വർഷത്തെ മെയിന്റനൻസ് എന്റെ യാർഡിന്! പക്ഷേ കരാർ കമ്പനിയുമായി മാത്രം."),
 ("A","A","കൊള്ളാം! കമ്പനിക്ക് എന്ത് പേര്?"),
 ("V","V","ആലപ്പുഴ ബോട്ട് യാർഡ് പ്രൈവറ്റ് ലിമിറ്റഡ്. സിമ്പിൾ. എല്ലാവർക്കും മനസ്സിലാകും."),
 ("A","wide","എല്ലാവർക്കും മനസ്സിലാകും. പക്ഷേ ഇതുപോലെ ഒരു പേര് ഇതിനകം ആരെങ്കിലും എടുത്തിട്ടുണ്ടാകും."),
 ("A","A","നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("V","V","എങ്കിൽ എന്റെ അപ്പന്റെ വള്ളത്തിന്റെ പേര്. ആ പഴയ ചുണ്ടൻ."),
 ("A","wide","അതാ വേറിട്ടത്. ബാക്കപ്പിന് രണ്ട് പേര് കൂടി എഴുത്!")],
 "സ്ഥലപ്പേര് + ബിസിനസ്.\nഅത് മാത്രം പോരാ", CTA_NAME,
 cap_ml="ബോട്ട് റിപ്പയർ യാർഡ് നടത്തുന്നയാൾക്ക് 40 ഹൗസ്ബോട്ടുകളുടെ ഒരു വർഷത്തെ മെയിന്റനൻസ് കരാർ, കമ്പനിയുമായി മാത്രം. സ്ഥലപ്പേരും ബിസിനസും മാത്രം ചേർത്ത പേര് നിലവിലുള്ള കമ്പനികളോട് സാമ്യം വന്ന് റിജക്ട് ആകാം; വേറിട്ട പേരുകൾ കരുതൂ.",
 cap_en="An Alappuzha boat-repair yard wins yearly maintenance for 40 houseboats, contract only with a company, and the owner wants a place-plus-trade name. Names like that are often similar to existing companies or LLPs and get rejected, so keep distinctive options ready.",
 cap_mg="Boat repair yard nadathunna aalkku 40 houseboat-nte oru varshathe maintenance contract, company-yumaayi maathram. Sthalapperum business-um maathram chertha peru existing company-kalodu saamyam vannu reject aakaam; vere names karuthu.")

# hotellobby: Neethu + Jaison. Jaison's laundry signed for the linen of five hotels; his company is four months old and INC-20A is not filed.
duo("d1905", "proprietor", "B", "hotellobby", "അഞ്ച് ഹോട്ടലിന്റെ ബെഡ്ഷീറ്റ്.\nകമ്പനിക്ക് നാല് മാസം.\nഒരു ഫോം ബാക്കി", [
 ("A","wide","ജെയ്സണേ, ഇന്നും വാനിൽ ബെഡ്ഷീറ്റ് മല! ഈ ഹോട്ടലിലെ മാത്രമാണോ?"),
 ("V","V","നീതൂ, ഇപ്പോ അഞ്ച് ഹോട്ടൽ. അതിന് വേണ്ടിയാ നാല് മാസം മുമ്പ് ലോൺഡ്രി കമ്പനി ആക്കിയത്."),
 ("A","A","നാല് മാസമോ? INC-20A ഫയൽ ചെയ്തോ?"),
 ("V","V","അതെന്താ? പുതിയ ഡിറ്റർജന്റിന്റെ പേരാണോ?"),
 ("A","wide","ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ഫോം. കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("V","V","നാല് മാസം. അപ്പോ ഇനിയും രണ്ട് മാസം ഉണ്ട്. സമാധാനം."),
 ("A","A","സമാധാനിക്കണ്ട. മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഓരോ ഡയറക്ടർക്കും ദിവസം ആയിരം രൂപ വേറെ."),
 ("V","wide","എങ്കിൽ ഈ ആഴ്ച തന്നെ. ബെഡ്ഷീറ്റ് പോലെ ഫയലും വെളുപ്പിക്കാം!")],
 "കമ്പനിക്ക് മാസങ്ങളായോ?\nINC-20A ചെക്ക് ചെയ്യൂ", CTA_AFTER,
 cap_ml="അഞ്ച് ഹോട്ടലുകളുടെ ബെഡ്ഷീറ്റും ടവലും കഴുകുന്ന ലോൺഡ്രിയുടെ കമ്പനിക്ക് നാല് മാസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. 180 ദിവസത്തിനുള്ളിൽ ചെയ്യണം; വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപ.",
 cap_en="A Kerala laundry that washes linen for five hotels became a company four months ago, and INC-20A is still not filed. It is due within 180 days of incorporation; missing it means 50,000 on the company and 1,000 a day for each director in default.",
 cap_mg="5 hotel-nte bedsheet-um towel-um kazhukunna laundry-yude company-kku 4 maasam, INC-20A file cheythittilla. 180 days-inullil cheyyanam; vaikiyal company-kku 50,000 pizha, oro director-kkum divasam 1,000.")

# chat: Saleem + his daughter Shabna. An export house wants five tonnes of Saleem's ground spices a month, contract only with a Pvt Ltd; he wants it "just me".
chat("c1011", "proprietor", "A", "മുളകുപൊടി മില്ലിന്\nമാസം 5 ടൺ എക്സ്പോർട്ട് ഓർഡർ", ("സലീം", "ഷബ്ന"), [
 (0,"മോളേ, ആ എക്സ്പോർട്ട് ഹൗസ് വീണ്ടും വിളിച്ചു. മാസം അഞ്ച് ടൺ മുളകും മല്ലിയും!"),
 (1,"ഉപ്പാ! നമ്മുടെ മില്ലിന്റെ മണം ഇനി കപ്പലിൽ!"),
 (0,"പക്ഷേ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയുമായി മാത്രം കരാർ. ഞാൻ ഒറ്റയ്ക്ക് ഒരു കമ്പനി തുടങ്ങാം."),
 (1,"ഉപ്പാ, പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം."),
 (0,"രണ്ടാമത്തെ ആൾ ആര്? നിന്റെ ഇക്ക ഷാർജയിലാണ്."),
 (1,"ഞാൻ ഉണ്ടല്ലോ. നാട്ടിൽ തന്നെ. കണക്കും ഞാൻ തന്നെ നോക്കുന്നു."),
 (0,"അത് ശരിയാ. എന്നെക്കാൾ നന്നായി നീ ബില്ല് എഴുതും."),
 (1,"അപ്പോ ഉറപ്പിച്ചു. ഡയറക്ടർ ഉപ്പയും മോളും. ആദ്യ മീറ്റിംഗ് ഇന്ന് രാത്രി ചായയ്ക്ക്!")],
 "വലിയ ഓർഡറിന്\nരണ്ട് ഡയറക്ടർ", CTA_START,
 cap_ml="മുളകുപൊടി മിൽ നടത്തുന്ന ഉപ്പയ്ക്ക് മാസം 5 ടൺ എക്സ്പോർട്ട് ഓർഡർ, പ്രൈവറ്റ് ലിമിറ്റഡുമായി മാത്രം കരാർ. Pvt Ltd-ന് കുറഞ്ഞത് 2 ഡയറക്ടറും 2 ഷെയർഹോൾഡറും വേണം; നാട്ടിലുള്ള മകൾ രണ്ടാമത്തെ ഡയറക്ടർ.",
 cap_en="A Kerala spice-mill owner is offered a five-tonne monthly export order, contract only with a private limited company, and plans to form it alone. A Pvt Ltd needs at least two directors and two shareholders, so his daughter at home joins the board.",
 cap_mg="Mulakupodi mill nadathunna uppaykku maasam 5 ton export order, Pvt Ltd-umaayi maathram contract. Pvt Ltd-nu kuranjathu 2 director-um 2 shareholder-um venam; naattilulla makal randaamathe director.")

lst("l1011", "proprietor", "C", "വലിയ ഓർഡർ ഫോണിൽ വന്നു.\nആദ്യ ആഴ്ച ചെയ്യേണ്ട\n3 കാര്യം", [
 ("ഇന്ന് തന്നെ തുടങ്ങൂ", "Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം. കരാർ തീയതിയിൽ നിന്ന് പിന്നോട്ട് എണ്ണൂ."),
 ("ഓഫീസ് മുറി വേണ്ട", "വീടോ കടയോ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും."),
 ("ലക്ഷങ്ങൾ കാണിക്കേണ്ട", "പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല.")],
 "ഓർഡർ റെഡി.\nകമ്പനിയും റെഡിയാക്കൂ", CTA_DOCS,
 cap_ml="കടയ്ക്കോ ചെറിയ യൂണിറ്റിനോ കമ്പനിയുമായി മാത്രം കരാർ ഒപ്പിടുന്ന വലിയ ഓർഡർ വന്നോ? Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; വീടോ കടയോ NOC-യും ബില്ലും വെച്ച് ഓഫീസ് ആക്കാം; മിനിമം ക്യാപിറ്റൽ ഇല്ല.",
 cap_en="A big order just came in, but the buyer signs only with a company? Pvt Ltd registration usually takes 7-15 working days, your home or shop can be the registered office with the owner's NOC and a recent bill, and there is no minimum capital.",
 cap_mg="Kadaykko cheriya unit-ino company-yumaayi maathram contract oppidunna valiya order vanno? Pvt Ltd register cheyyan saadharana 7-15 working days; veedo kadayo NOC-um bill-um vechu office aakkaam; minimum capital illa.")

# ---------------- nri ----------------
# gulfroom: Naseer + Shamsu. Shamsu, a driver in Kuwait, wants to fund his brother's three phone-repair shops in Kerala and hold shares; the brother is a proprietor.
duo("d1906", "nri", "A", "gulfroom", "കുവൈറ്റിൽ ഡ്രൈവർ.\nനാട്ടിൽ അനിയന്റെ മൊബൈൽ\nറിപ്പയർ ഷോപ്പിൽ ഷെയർ?", [
 ("A","wide","ഷംസൂ, ഡ്യൂട്ടി കഴിഞ്ഞിട്ടും ഫോണിൽ തന്നെ. ആരാ?"),
 ("V","V","നസീറിക്കാ, അനിയൻ. അവന്റെ മൊബൈൽ റിപ്പയർ ഷോപ്പ് ഇപ്പോ മൂന്നെണ്ണം. നാലാമത്തേതിന് ഞാൻ പൈസ ഇടാമെന്ന് പറഞ്ഞു."),
 ("A","A","നല്ലത്. പക്ഷേ നിന്റെ പൈസയ്ക്ക് എന്ത് ഉറപ്പ്?"),
 ("V","V","ഷെയർ തരാമെന്ന് അവൻ പറഞ്ഞു. പക്ഷേ കട അവന്റെ പേരിൽ മാത്രം ആണ്."),
 ("A","wide","അതാ പ്രശ്നം. ഒരാളുടെ പേരിലുള്ള കടയിൽ ഷെയർ ഇല്ല. ഷെയർ എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം."),
 ("V","V","ഞാൻ കുവൈറ്റിൽ അല്ലേ? എനിക്ക് ഷെയർഹോൾഡർ ആകാൻ പറ്റുമോ?"),
 ("A","A","പറ്റും. NRI-ക്കും ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം. അനിയൻ നാട്ടിലുള്ള ഡയറക്ടർ."),
 ("V","wide","എങ്കിൽ ആദ്യം കമ്പനി, പിന്നെ പൈസ. ഇത്തവണ എല്ലാം പേപ്പറിൽ!")],
 "ഗൾഫിലെ പൈസ നാട്ടിലേക്ക്?\nഷെയർ പേപ്പറിൽ വേണം", CTA_START,
 cap_ml="കുവൈറ്റിൽ ഡ്രൈവറായ പ്രവാസി നാട്ടിലെ അനിയന്റെ മൊബൈൽ റിപ്പയർ ഷോപ്പുകളിൽ പൈസ ഇട്ട് ഷെയർ എടുക്കാൻ നോക്കുന്നു, പക്ഷേ കട അനിയന്റെ പേരിൽ മാത്രം. ഷെയർ എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം; NRI-ക്ക് ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം.",
 cap_en="An NRI driver in Kuwait wants to fund his brother's fourth phone-repair shop in Kerala and hold shares, but the business is a proprietorship. Shares need a private limited company, and an NRI can be its shareholder and director while the brother is the resident director.",
 cap_mg="Kuwait-il driver aaya pravaasi naattile aniyante mobile repair shop-il paisa ittu share edukkan nokkunnu, pakshe kada aniyante peril maathram. Share edukkan Pvt Ltd company venam; NRI-kku shareholder-um director-um aakaam.")

# gulf: Shiju + Faisal. Faisal works in Bahrain; his Kerala water-purifier company with his wife got its certificate; he thinks the government sends an auditor.
duo("d1907", "nri", "B", "gulf", "ബഹ്റൈനിൽ നിന്ന് കമ്പനി.\n\"ഓഡിറ്ററെ ഗവൺമെന്റ്\nഅയച്ചുതരും\"", [
 ("V","wide","ഷിജുവേട്ടാ, നാട്ടിലെ വാട്ടർ പ്യൂരിഫയർ കമ്പനിയുടെ സർട്ടിഫിക്കറ്റ് വന്നു! ഭാര്യ ഫോട്ടോ അയച്ചു."),
 ("A","A","ഫൈസലേ, കൊള്ളാം. ഓഡിറ്ററെ വെച്ചോ?"),
 ("V","V","അത് ഗവൺമെന്റ് അയച്ചുതരില്ലേ? സർട്ടിഫിക്കറ്റിനൊപ്പം വരുമെന്നാ ഞാൻ കരുതിയത്."),
 ("A","wide","ഇല്ല. ആദ്യത്തെ ഓഡിറ്ററെ കമ്പനി തന്നെ നിയമിക്കണം. കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ."),
 ("V","V","സർട്ടിഫിക്കറ്റ് വന്നിട്ട് പന്ത്രണ്ട് ദിവസം ആയി."),
 ("A","A","അപ്പോ പതിനെട്ട് ദിവസം ബാക്കി. നാട്ടിൽ ഭാര്യയുണ്ടല്ലോ. അവൾ ഡയറക്ടർ അല്ലേ?"),
 ("V","V","അതേ. ഇന്ന് രാത്രി വിളിച്ച് പറയാം. ഈ ആഴ്ച തന്നെ ഓഡിറ്റർ."),
 ("A","wide","വെള്ളം ശുദ്ധമാക്കുന്ന കമ്പനി. കണക്കും ശുദ്ധമാകട്ടെ!")],
 "ഓഡിറ്റർ തനിയെ വരില്ല.\n30 ദിവസം", CTA_AFTER,
 cap_ml="ബഹ്റൈനിൽ ജോലി ചെയ്യുന്ന പ്രവാസിയുടെയും നാട്ടിലുള്ള ഭാര്യയുടെയും വാട്ടർ പ്യൂരിഫയർ കമ്പനിക്ക് സർട്ടിഫിക്കറ്റ് വന്നു; ഓഡിറ്ററെ ഗവൺമെന്റ് അയയ്ക്കുമെന്നാണ് അദ്ദേഹം കരുതിയത്. ആദ്യത്തെ ഓഡിറ്ററെ കമ്പനി തന്നെ 30 ദിവസത്തിനുള്ളിൽ നിയമിക്കണം.",
 cap_en="An NRI in Bahrain and his wife in Kerala just got their water-purifier company's certificate, and he thought the government would send an auditor. The company itself must appoint its first auditor within 30 days of incorporation.",
 cap_mg="Bahrain-il joli cheyyunna pravaasiyudeyum naattilulla bhaaryayudeyum water purifier company-kku certificate vannu; auditor-e government ayakkum ennu karuthi. First auditor-e company thanne 30 days-inullil appoint cheyyanam.")

# gulfoffice: Shahana + Asif. Asif, an engineer in Qatar, sets up a CCTV-installation company in Kannur run by his brother; office is the family house in his mother's name.
duo("d1908", "nri", "C", "gulfoffice", "ഖത്തറിൽ എഞ്ചിനീയർ.\nകണ്ണൂരിൽ CCTV കമ്പനി.\nഓഫീസ് ഉമ്മയുടെ വീട്", [
 ("A","wide","ആസിഫേ, ലഞ്ച് ബ്രേക്കിലും ക്യാമറ ആംഗിളോ?"),
 ("V","V","ഷഹാനാ, കണ്ണൂരിലെ CCTV കമ്പനിയുടെ പ്ലാൻ. അനിയൻ നാട്ടിൽ ഇൻസ്റ്റലേഷൻ നോക്കും. ഞാനും അവനും ഡയറക്ടർമാർ."),
 ("A","A","കൊള്ളാം. ഓഫീസ് എവിടെ?"),
 ("V","V","തറവാട് വീട്. പക്ഷേ അത് ഉമ്മയുടെ പേരിലാ. ഞാൻ ഇവിടെ ഇരുന്ന് അത് എങ്ങനെ ശരിയാക്കും?"),
 ("A","wide","എളുപ്പമാ. ഉമ്മയുടെ NOC. പിന്നെ ആ വീടിന്റെ പുതിയ കറന്റ് ബില്ലോ വെള്ളക്കരം ബില്ലോ."),
 ("A","A","അനിയൻ നാട്ടിൽ ഉണ്ടല്ലോ. ഉമ്മയെക്കൊണ്ട് ഒപ്പിടീക്കാൻ അവനോട് പറ."),
 ("V","V","ഉമ്മ ഒപ്പിടും. പക്ഷേ ആദ്യം ചോദിക്കും, വീട്ടിൽ ക്യാമറ വെക്കുമോ എന്ന്!"),
 ("A","wide","വെക്ക്. ആദ്യ ക്ലയന്റ് ഉമ്മ!")],
 "വീട് ഉമ്മയുടെ പേരിലോ?\nNOC മതി", CTA_DOCS,
 cap_ml="ഖത്തറിൽ എഞ്ചിനീയറായ പ്രവാസി അനിയനോടൊപ്പം കണ്ണൂരിൽ CCTV ഇൻസ്റ്റലേഷൻ കമ്പനി തുടങ്ങുന്നു; ഓഫീസ് ഉമ്മയുടെ പേരിലുള്ള തറവാട്. ഉമ്മയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ ആ വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="An NRI engineer in Qatar starts a CCTV-installation company in Kannur with his brother, who lives in Kerala. The family house is in their mother's name; with her NOC and a recent utility bill, it can be the company's registered office.",
 cap_mg="Qatar-il engineer aaya pravaasi aniyanodoppam Kannur-il CCTV installation company thudangunnu; office ummayude peril ulla tharavaad. Ummayude NOC-um puthiya utility bill-um undenkil aa veedu registered office aakkaam.")

# mall: Sumayya + Jafar. The Dubai couple fly home for three weeks in December and want their Kerala gift-hamper company done within the leave.
duo("d1909", "nri", "A", "mall", "ഡിസംബറിൽ 3 ആഴ്ച ലീവ്.\nനാട്ടിൽ ചെന്ന് കമ്പനി\nതുടങ്ങിയാൽ മതിയോ?", [
 ("V","wide","സുമയ്യാ, ടിക്കറ്റ് കിട്ടി! ഡിസംബർ പത്ത് മുതൽ മൂന്ന് ആഴ്ച നാട്ടിൽ."),
 ("A","A","ജാഫറിക്കാ, അപ്പോ ആ ഗിഫ്റ്റ് ഹാമ്പർ കമ്പനി ലീവിൽ തന്നെ തുടങ്ങാം. കല്യാണ സീസൺ ഓർഡറുകൾ കാത്തിരിക്കുന്നു."),
 ("V","V","അതാ പ്ലാൻ. നാട്ടിൽ ചെന്നിട്ട് ഡോക്യുമെന്റ്സ് നോക്കാം."),
 ("A","wide","അങ്ങനെ ചെയ്താൽ ലീവ് തീരും. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","ഇപ്പോ ദുബായിൽ ഇരുന്ന് തന്നെ പേപ്പറുകൾ റെഡിയാക്കാം. നമ്മൾ NRI ആയാലും ഡയറക്ടർ ആകാം."),
 ("V","V","നാട്ടിലുള്ള ഒരു ഡയറക്ടർ കൂടി വേണ്ടേ?"),
 ("A","A","എന്റെ അനിയത്തി. ഹാമ്പർ പാക്ക് ചെയ്യുന്നത് അവളല്ലേ."),
 ("V","wide","ശരി. ലീവിൽ കമ്പനി ഉദ്ഘാടനം, ഷോപ്പിംഗ് അല്ല!")],
 "ലീവിന് മുമ്പേ\nപേപ്പർ റെഡി", CTA_DOCS,
 cap_ml="ദുബായിലുള്ള ദമ്പതികൾ ഡിസംബറിലെ മൂന്ന് ആഴ്ച ലീവിൽ നാട്ടിൽ ഗിഫ്റ്റ് ഹാമ്പർ കമ്പനി തുടങ്ങാൻ നോക്കുന്നു. Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; ദുബായിൽ ഇരുന്ന് തന്നെ ഡോക്യുമെന്റ്സ് തുടങ്ങാം, NRI-ക്കും ഡയറക്ടർ ആകാം.",
 cap_en="A Dubai NRI couple want their Kerala gift-hamper company running during three weeks of leave in December. Pvt Ltd registration usually takes 7-15 working days, NRIs can be directors, and the documents can start from Dubai now, with a sister at home as the resident director.",
 cap_mg="Dubai-yil ulla couple December-ile 3 aazhcha leave-il naattil gift hamper company thudangan nokkunnu. Pvt Ltd register cheyyan saadharana 7-15 working days; Dubai-yil irunnu thanne documents thudangaam, NRI-kkum director aakaam.")

# airport: Shameer + Rafeeq. Rafeeq is back from Oman after 20 years to pack spices for Gulf shops and wants the name of a famous Gulf airline on his company.
duo("d1910", "nri", "B", "airport", "20 വർഷം ഒമാനിൽ.\nസ്പൈസസ് കമ്പനിക്ക്\nഒരു എയർലൈനിന്റെ പേര്", [
 ("A","wide","റഫീഖേ, ഇരുപത് വർഷത്തിന് ശേഷം ഫൈനൽ എക്സിറ്റ്! ഇനി എന്താ പ്ലാൻ?"),
 ("V","V","ഷമീറേ, സ്പൈസസ് പാക്ക് ചെയ്ത് ഗൾഫിലെ കടകളിലേക്ക്. അവിടത്തെ കടക്കാരെ എനിക്ക് എല്ലാവരെയും അറിയാം."),
 ("A","A","കൊള്ളാം. കമ്പനിക്ക് പേര്?"),
 ("V","V","എനിക്ക് എന്നും പ്രിയപ്പെട്ട ആ ഗൾഫ് എയർലൈനിന്റെ പേര്. പിന്നിൽ സ്പൈസസ്. ഗൾഫുകാർക്ക് പെട്ടെന്ന് പിടികിട്ടും."),
 ("A","wide","പിടികിട്ടും. എയർലൈൻ കമ്പനിക്കും പിടികിട്ടും! അത് അവരുടെ ട്രേഡ്മാർക്കാണ്."),
 ("A","A","വേറൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് റിജക്ട് ആകാം."),
 ("V","V","എങ്കിൽ ഒമാനിലെ എന്റെ ആദ്യത്തെ കടയുടെ തെരുവിന്റെ പേര്? അതാർക്കും ഇല്ല."),
 ("A","wide","അതാ നല്ലത്. നിന്റെ കഥ ഉള്ള പേര്. ബാക്കപ്പിന് രണ്ടെണ്ണം കൂടി!")],
 "ഫേമസ് ബ്രാൻഡിന്റെ പേര്\nനിങ്ങളുടെ കമ്പനിക്ക് വേണ്ട", CTA_NAME,
 cap_ml="ഇരുപത് വർഷം ഒമാനിൽ ജോലി ചെയ്ത് തിരിച്ചെത്തിയ പ്രവാസി ഗൾഫിലെ കടകൾക്ക് സ്പൈസസ് പാക്ക് ചെയ്യുന്ന കമ്പനിക്ക് ഒരു എയർലൈനിന്റെ പേര് ഇടാൻ നോക്കുന്നു. മറ്റൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന കമ്പനി പേര് റിജക്ട് ആകാം.",
 cap_en="A returning NRI back in Kerala after 20 years in Oman wants to name his spice-export company after a famous Gulf airline. A company name that clashes with someone else's trademark can be rejected, so build a name from your own story instead.",
 cap_mg="20 varsham Oman-il joli cheythu thirichethiya pravaasi Gulf kadakalkku spices pack cheyyunna company-kku oru airline-nte peru idaan nokkunnu. Vere aalude trademark-umaayi clash aakunna company name reject aakaam.")

# munnar: Celine + Basil. Basil, a nurse in New Zealand, is home for his wife's delivery and wants a cardamom-estate homestay company with his sister Celine.
duo("d1911", "nri", "A", "munnar", "ന്യൂസിലൻഡിൽ നഴ്സ്.\nഭാര്യയുടെ പ്രസവത്തിന്\nലീവിൽ. ഒപ്പം ഒരു പ്ലാൻ", [
 ("A","wide","ബേസിലേ, കുഞ്ഞിന്റെ ഉറക്കം കഴിഞ്ഞോ? അതോ നീ ഇപ്പോഴും ഏലത്തോട്ടത്തിൽ കറങ്ങുവാണോ?"),
 ("V","V","സെലിൻ ചേച്ചീ, ഒരു പ്ലാൻ ഉണ്ട്. അപ്പന്റെ ഏലത്തോട്ടത്തിലെ പഴയ ബംഗ്ലാവ് ഹോംസ്റ്റേ ആക്കാം. ചേച്ചിയും ഞാനും."),
 ("A","A","കൊള്ളാം. പക്ഷേ നീ അടുത്ത മാസം ന്യൂസിലൻഡിലേക്ക് തിരിച്ചു പോകില്ലേ?"),
 ("V","V","അതാ. ഞാൻ വിദേശത്ത് ആയതുകൊണ്ട് പൈസ മാത്രം ഇടാം, ഡയറക്ടർ ആകാൻ പറ്റില്ലെന്ന് ഒരാൾ പറഞ്ഞു."),
 ("A","wide","അത് തെറ്റാ. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("A","A","ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. അത് ഞാൻ. തോട്ടത്തിന് അടുത്ത് തന്നെ ഉണ്ടല്ലോ."),
 ("V","V","എങ്കിൽ ലീവ് തീരും മുമ്പ് ഡോക്യുമെന്റ്സ് തുടങ്ങാം."),
 ("A","wide","ഡീൽ. ഹോംസ്റ്റേയുടെ ആദ്യ ഗസ്റ്റ് നിന്റെ കുഞ്ഞ്!")],
 "വിദേശത്താണോ?\nഡയറക്ടർ ആകാം", CTA_START,
 cap_ml="ന്യൂസിലൻഡിൽ നഴ്സായ പ്രവാസി ഭാര്യയുടെ പ്രസവത്തിന് ലീവിൽ വന്നപ്പോൾ ഇടുക്കിയിലെ ഏലത്തോട്ട ബംഗ്ലാവ് ഹോംസ്റ്റേ കമ്പനി ആക്കാൻ നോക്കുന്നു. NRI-ക്ക് Pvt Ltd-ൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം; നാട്ടിലുള്ള ചേച്ചി റസിഡന്റ് ഡയറക്ടർ.",
 cap_en="An NRI nurse from New Zealand, home in Idukki for his wife's delivery, wants to turn the family cardamom-estate bungalow into a homestay company with his sister. NRIs can be directors and shareholders of an Indian Pvt Ltd; the sister at home is the resident director.",
 cap_mg="New Zealand-il nurse aaya pravaasi bhaaryayude prasavathinu leave-il vannappol Idukki-yile elathotta bungalow homestay company aakkan nokkunnu. NRI-kku Pvt Ltd-il director-um shareholder-um aakaam; naattilulla chechi resident director.")

# chat: Daisy + her son Tomy. Daisy, a nurse in Saudi, has 30 days of leave from next week; Tomy's Fort Kochi cycle-rental needs a company and she wants to be a director.
chat("c1012", "nri", "A", "സൗദിയിൽ നിന്ന് 30 ദിവസം\nലീവ്. മകന്റെ സൈക്കിൾ\nറെന്റൽ കമ്പനി", ("ഡെയ്സി", "ടോമി"), [
 (0,"ടോമീ, അടുത്ത വെള്ളിയാഴ്ച ഞാൻ ലാൻഡ് ചെയ്യും. മുപ്പത് ദിവസം ലീവ്!"),
 (1,"മമ്മീ! ഫോർട്ട് കൊച്ചിയിലെ സൈക്കിൾ റെന്റലിന് ഒരു റിസോർട്ട് കരാർ തരാമെന്ന്. കമ്പനി ആയാൽ മാത്രം."),
 (0,"ഞാനും ഡയറക്ടർ ആകും. പൈസ ഇടുന്നത് ഞാനല്ലേ. ലീവിൽ വന്നിട്ട് എല്ലാം തുടങ്ങാം."),
 (1,"മമ്മി സൗദിയിൽ ആയാലും ഡയറക്ടർ ആകാം. NRI-ക്കും പറ്റും. ഞാൻ നാട്ടിലുള്ള ഡയറക്ടർ."),
 (1,"പക്ഷേ വന്നിട്ട് തുടങ്ങിയാൽ ലീവ് തീരും. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം."),
 (0,"അപ്പോ ഇന്ന് തന്നെ എന്റെ ഡോക്യുമെന്റ്സ് സ്കാൻ ചെയ്ത് അയക്കാം."),
 (1,"സൂപ്പർ. മമ്മി വരുമ്പോൾ സർട്ടിഫിക്കറ്റ് റെഡി!"),
 (0,"എങ്കിൽ എയർപോർട്ടിൽ നിന്ന് നേരെ സൈക്കിളിൽ വീട്ടിലേക്ക്!")],
 "ലീവിന് മുമ്പ് തുടങ്ങൂ.\nലീവിൽ ആഘോഷിക്കൂ", CTA_DOCS,
 cap_ml="സൗദിയിൽ നഴ്സായ അമ്മയ്ക്ക് 30 ദിവസം ലീവ്; ഫോർട്ട് കൊച്ചിയിലെ മകന്റെ സൈക്കിൾ റെന്റലിന് റിസോർട്ട് കരാർ, കമ്പനി ആയാൽ മാത്രം. NRI-ക്ക് ഡയറക്ടർ ആകാം; Pvt Ltd-ന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം, ലീവിന് മുമ്പേ തുടങ്ങൂ.",
 cap_en="An NRI nurse in Saudi has 30 days of leave coming, and her son's Fort Kochi cycle-rental has a resort contract waiting, company only. She can be a director while abroad; Pvt Ltd registration usually takes 7-15 working days, so start before she lands.",
 cap_mg="Saudi-yil nurse aaya ammaykku 30 divasam leave; Fort Kochi-yile makante cycle rental-nu resort contract, company aayaal maathram. NRI-kku director aakaam; Pvt Ltd-nu saadharana 7-15 working days, leave-nu munpe thudangu.")

# ---------------- solo ----------------
# metro: Anjali + Kiran. Anjali makes video CVs alone for job seekers; a placement agency wants a company contract; Kiran says she needs a partner first.
duo("d1912", "solo", "A", "metro", "വീഡിയോ CV ഉണ്ടാക്കുന്നത്\nഞാൻ ഒറ്റയ്ക്ക്. കിരൺ:\n\"ആദ്യം ഒരു പാർട്ണർ വേണം\"", [
 ("V","wide","അഞ്ജലീ, ഇന്നും മെട്രോയിൽ ലാപ്ടോപ്പ്. ആരുടെ വീഡിയോ?"),
 ("A","A","കിരണേ, ഒരു ഫ്രഷറുടെ വീഡിയോ CV. ഈ മാസം അറുപതാമത്തേത്!"),
 ("A","A","ഒരു പ്ലേസ്മെന്റ് ഏജൻസി എല്ലാ ക്യാൻഡിഡേറ്റ്സിനും എന്നോട് ചെയ്യാൻ പറഞ്ഞു. പക്ഷേ കമ്പനിയുമായി മാത്രം കരാർ."),
 ("V","V","കമ്പനിക്ക് കുറഞ്ഞത് രണ്ടുപേർ വേണം. ആദ്യം ഒരു പാർട്ണറെ കണ്ടുപിടിക്ക്."),
 ("A","wide","വേണ്ട. ഒറ്റയ്ക്ക് തുടങ്ങാൻ വൺ പേഴ്സൺ കമ്പനി ഉണ്ട്. OPC."),
 ("V","V","ഒറ്റയ്ക്ക് കമ്പനിയോ? എനിക്കറിയില്ലായിരുന്നു."),
 ("A","A","ഞാനും കഴിഞ്ഞ ആഴ്ചയാ അറിഞ്ഞത്. എഡിറ്റിംഗും ഞാൻ, ഡയറക്ടറും ഞാൻ."),
 ("V","wide","എങ്കിൽ നിന്റെ വീഡിയോ CV-യിൽ ഒരു വരി കൂടി: ഫൗണ്ടർ!")],
 "പാർട്ണറെ കാത്തിരിക്കണ്ട.\nOPC ഉണ്ട്", CTA_START,
 cap_ml="ജോലി അന്വേഷിക്കുന്നവർക്ക് ഒറ്റയ്ക്ക് വീഡിയോ CV ഉണ്ടാക്കുന്ന യുവതിക്ക് പ്ലേസ്മെന്റ് ഏജൻസിയുടെ കരാർ, കമ്പനിയുമായി മാത്രം; കമ്പനിക്ക് പാർട്ണർ വേണമെന്ന് കൂട്ടുകാരൻ. ഒറ്റയ്ക്കുള്ള ഫൗണ്ടർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം.",
 cap_en="A solo video-CV maker in Kochi is offered a placement agency's contract, company only, and a friend says she needs a partner first. A solo founder can register a One Person Company (OPC) without waiting for a cofounder.",
 cap_mg="Joli anweshikkunnavarkku ottaykku video CV undaakkunna aalkku placement agency-yude contract, company-yumaayi maathram; company-kku partner venam ennu friend. Ottaykkulla founder-nu One Person Company (OPC) thudangaam.")

# weddinghall: Kavya + Sarath. Sarath rents LED video walls to weddings alone through his OPC; day 160, INC-20A not filed, twelve weddings booked this month.
duo("d1913", "solo", "B", "weddinghall", "കല്യാണ ഹാളിൽ LED വാൾ.\nOPC-ക്ക് 160 ദിവസം.\nഈ മാസം 12 കല്യാണം", [
 ("A","wide","ശരത്തേ, സ്ക്രീനിൽ വധുവിന്റെ മുഖം മൂന്നാമതും ഫ്രീസ് ആയി!"),
 ("V","V","കാവ്യേ, കേബിൾ മാറ്റി. ഇപ്പോ ഓക്കെ. ഈ മാസം പന്ത്രണ്ട് കല്യാണം. LED വാൾ ഞാൻ ഒറ്റയ്ക്ക്."),
 ("A","A","ഒറ്റയ്ക്ക് കമ്പനി ആക്കിയതല്ലേ? OPC എന്നല്ലേ പറഞ്ഞത്. എത്ര ദിവസമായി?"),
 ("V","V","ഏകദേശം അഞ്ചേകാൽ മാസം. നൂറ്റിയറുപത് ദിവസം കാണും."),
 ("A","wide","INC-20A ഫയൽ ചെയ്തോ? ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ഫോം. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ വേണം."),
 ("V","V","അത് വലിയ കമ്പനികൾക്കല്ലേ? ഞാൻ ഒരാൾ മാത്രം."),
 ("A","A","OPC-ക്കും ബാധകം. മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടറായ നിനക്ക് ദിവസം ആയിരം രൂപ വേറെ."),
 ("V","wide","എങ്കിൽ ഇന്ന് രാത്രി ഫോം. സ്ക്രീൻ ഫ്രീസ് ആകാം, ഡെഡ്‌ലൈൻ ഫ്രീസ് ആകില്ല!")],
 "OPC ആണോ?\nINC-20A നിങ്ങൾക്കും", CTA_AFTER,
 cap_ml="കല്യാണങ്ങൾക്ക് LED വീഡിയോ വാൾ വാടകയ്ക്ക് കൊടുക്കുന്ന യുവാവിന്റെ OPC-ക്ക് 160 ദിവസം, ഈ മാസം 12 കല്യാണം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. വൺ പേഴ്സൺ കമ്പനിക്കും 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം; വൈകിയാൽ 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ.",
 cap_en="A solo LED video-wall renter for Kerala weddings has 12 bookings this month, and his One Person Company is at day 160 with INC-20A not filed. An OPC must file it within 180 days too: 50,000 on the company and 1,000 a day for the director if missed.",
 cap_mg="Kalyanangalkku LED video wall vaadakaykku kodukkunna aalude OPC-kku 160 divasam, ee maasam 12 kalyanam, INC-20A file cheythittilla. OPC-kkum 180 days-inullil file cheyyanam; vaikiyal 50,000 pizha, director-kku divasam 1,000.")

# gym: Riya + Justin. Riya trains brides-to-be alone; a wedding-planner chain wants her for all its brides, contract with a company in two weeks.
duo("d1914", "solo", "A", "gym", "കല്യാണപ്പെണ്ണുങ്ങളുടെ\nഫിറ്റ്നസ് ട്രെയിനർ.\nകരാർ രണ്ടാഴ്ചയിൽ", [
 ("V","wide","റിയാ, ഇന്ന് രാവിലെ അഞ്ച് മണിക്ക് തന്നെ മൂന്ന് കല്യാണപ്പെണ്ണുങ്ങൾ!"),
 ("A","A","ജസ്റ്റിനേ, ഇത് തുടക്കം മാത്രം. ഒരു വെഡ്ഡിംഗ് പ്ലാനർ ചെയിൻ അവരുടെ എല്ലാ വധുക്കളെയും എനിക്ക് തരാമെന്ന്."),
 ("V","V","സൂപ്പർ! എന്നാണ് തുടങ്ങുന്നത്?"),
 ("A","A","രണ്ടാഴ്ചയിൽ കരാർ ഒപ്പിടണം. എന്റെ കമ്പനിയുമായി. ഞാൻ ആണെങ്കിൽ ഇതുവരെ ഒന്നും തുടങ്ങിയില്ല."),
 ("V","wide","എങ്കിൽ ഇന്ന് തന്നെ തുടങ്ങ്. ഒറ്റയ്ക്കാണെങ്കിൽ OPC. ഒരു പ്രൈവറ്റ് ലിമിറ്റഡ് പോലെ, ഒരാൾക്ക്."),
 ("V","V","രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും. രണ്ടാഴ്ച ടൈറ്റാ."),
 ("A","A","അപ്പോ ഇന്ന് ട്രെയിനിംഗ് കഴിഞ്ഞ് നേരെ ഡോക്യുമെന്റ്സ്."),
 ("V","wide","ഗുഡ്. വധുക്കൾക്ക് സ്ക്വാറ്റ്, നിനക്ക് പേപ്പർ വർക്ക്!")],
 "കരാർ അടുത്താണോ?\nഇന്ന് തന്നെ തുടങ്ങൂ", CTA_START,
 cap_ml="കല്യാണത്തിന് മുമ്പ് വധുക്കളെ ഒറ്റയ്ക്ക് ട്രെയിൻ ചെയ്യുന്ന ഫിറ്റ്നസ് ട്രെയിനർക്ക് ഒരു വെഡ്ഡിംഗ് പ്ലാനർ ചെയിനിന്റെ കരാർ, രണ്ടാഴ്ചയിൽ, കമ്പനിയുമായി മാത്രം. ഒറ്റയ്ക്കാണെങ്കിൽ OPC; രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="A solo bridal fitness trainer in Kerala is offered a wedding-planner chain's contract, to be signed with her company in two weeks. A solo founder can register a One Person Company (OPC), and registration usually takes 7-15 working days, so start today.",
 cap_mg="Kalyanathinu munpu vadhukkale ottaykku train cheyyunna fitness trainer-nu oru wedding planner chain-nte contract, 2 aazhchayil, company-yumaayi maathram. Ottaykkaanenkil OPC; register cheyyan saadharana 7-15 working days.")

# courier: Jaya + Aravind. Aravind ships banana chips alone to Malayalis in the US; he lives in his father-in-law's house and wants it as the office.
duo("d1915", "solo", "C", "courier", "അമേരിക്കയിലെ മലയാളികൾക്ക്\nകായ വറുത്തത്. ഓഫീസ്\nഭാര്യയുടെ അപ്പന്റെ വീട്", [
 ("A","wide","അരവിന്ദേ, ഇന്നും പതിനെട്ട് പാഴ്സൽ! എല്ലാം ന്യൂജേഴ്സിയിലേക്കോ?"),
 ("V","V","ജയേച്ചീ, ന്യൂജേഴ്സി, ടെക്സസ്, ഷിക്കാഗോ. അവിടത്തെ മലയാളി കടകൾക്ക് ഇനി കമ്പനി ഇൻവോയ്സ് വേണമെന്ന്."),
 ("A","A","കമ്പനി ആക്ക്. ഒറ്റയ്ക്കല്ലേ? OPC മതി."),
 ("V","V","അതേ. പക്ഷേ ഓഫീസ് അഡ്രസ്സ്? ഞങ്ങൾ താമസിക്കുന്നത് ഭാര്യയുടെ അപ്പന്റെ വീട്ടിലാ."),
 ("A","wide","ആ വീട് തന്നെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. അപ്പന്റെ NOC വേണം. പിന്നെ പുതിയ ഒരു കറന്റ് ബില്ലും."),
 ("V","V","അമ്മായിയപ്പനോട് ഒപ്പ് ചോദിക്കാൻ ഒരു മടി."),
 ("A","A","ഒരു പാക്കറ്റ് കായ വറുത്തത് കൂടെ കൊടുത്താൽ മതി. ഒപ്പ് ഉറപ്പ്."),
 ("V","wide","ഡബിൾ പാക്കറ്റ്. ഒന്ന് ഒപ്പിന്, ഒന്ന് അനുഗ്രഹത്തിന്!")],
 "ഭാര്യവീട്ടിലും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="അമേരിക്കയിലെ മലയാളി കടകൾക്ക് ഒറ്റയ്ക്ക് കായ വറുത്തത് അയക്കുന്നയാൾക്ക് കമ്പനി ഇൻവോയ്സ് വേണം; താമസം ഭാര്യയുടെ അപ്പന്റെ വീട്ടിൽ. ഉടമയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ ആ വീട് OPC-യുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A solo founder in Kerala ships banana chips to Malayali stores in the US, which now want company invoices. He lives in his father-in-law's house: with the owner's NOC and a recent electricity bill, it can be his One Person Company's registered office.",
 cap_mg="America-yile Malayali kadakalkku ottaykku kaaya varuthathu ayakkunna aalkku company invoice venam; thaamasam bhaaryayude appante veettil. Owner-nte NOC-um puthiya current bill-um undenkil aa veedu OPC-yude registered office aakkaam.")

# park: Gayathri + Ananthu. Gayathri tells stories to children in parks alone; a daycare chain wants monthly sessions from a company; she picked "Story Time India".
duo("d1916", "solo", "B", "park", "പാർക്കിലെ കഥപറച്ചിൽ.\nഡേകെയർ ചെയിൻ വിളിച്ചു.\nപേര്: \"സ്റ്റോറി ടൈം ഇന്ത്യ\"", [
 ("V","wide","ഗായത്രീ, ഇന്ന് മുപ്പത് കുട്ടികൾ! ആ കടുവയുടെ കഥ കഴിഞ്ഞപ്പോൾ എല്ലാവരും കയ്യടിച്ചു."),
 ("A","A","അനന്തൂ, ഒരു ഡേകെയർ ചെയിനിന്റെ മാനേജർ ഉണ്ടായിരുന്നു. എല്ലാ മാസവും അവരുടെ പത്ത് ബ്രാഞ്ചിലും കഥ!"),
 ("V","V","കൊള്ളാം! കമ്പനി വേണ്ടി വരും. പേര് ആലോചിച്ചോ?"),
 ("A","A","സ്റ്റോറി ടൈം ഇന്ത്യ. എളുപ്പം. എല്ലാവരും ഓർക്കും."),
 ("V","wide","എല്ലാവരും ഓർക്കും, കാരണം ഇതുപോലെ ഒരുപാട് പേരുകൾ ഇപ്പോഴേ ഉണ്ട്."),
 ("V","V","നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("A","A","എങ്കിൽ എന്റെ അമ്മൂമ്മയുടെ കഥപ്പെട്ടി. അമ്മൂമ്മയാ എനിക്ക് ആദ്യം കഥ പറഞ്ഞത്."),
 ("V","wide","അതാ പേര്! വേറിട്ടതും നിന്റേതും. രണ്ട് ബാക്കപ്പ് കൂടി എഴുത്!")],
 "എളുപ്പമുള്ള പേര്\nഎല്ലാവർക്കും എളുപ്പം", CTA_NAME,
 cap_ml="പാർക്കുകളിൽ കുട്ടികൾക്ക് ഒറ്റയ്ക്ക് കഥ പറയുന്ന യുവതിക്ക് ഡേകെയർ ചെയിനിന്റെ മാസ കരാർ; കമ്പനി പേരായി 'സ്റ്റോറി ടൈം ഇന്ത്യ' പോലുള്ള പൊതു പേര്. നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം ഉള്ള പേര് റിജക്ട് ആകാം.",
 cap_en="A solo children's storyteller in Kerala is offered monthly sessions at a daycare chain's ten branches and picks a common name like 'Story Time India'. Names similar to an existing company or LLP can be rejected, so choose something distinctive and keep backups.",
 cap_mg="Park-kalil kuttikalkku ottaykku katha parayunna aalkku daycare chain-nte maasa contract; company name aayi 'Story Time India' pole common peru. Existing company-yudeyo LLP-yudeyo perinodu saamyam ulla peru reject aakaam.")

# chat: Muhsin + Irfan. Muhsin paints Arabic calligraphy for homes alone through his OPC, 28 days old; a builder wants panels for 40 villas; no auditor yet.
chat("c1013", "solo", "B", "അറബിക് കാലിഗ്രഫി.\n40 വില്ലയുടെ ഓർഡർ.\nOPC-ക്ക് 28 ദിവസം", ("മുഹ്സിൻ", "ഇർഫാൻ"), [
 (0,"ഇർഫാനേ, ആ ബിൽഡർ ഓക്കെ പറഞ്ഞു! നാൽപ്പത് വില്ലയിലും എന്റെ കാലിഗ്രഫി പാനൽ!"),
 (1,"മാഷാ അല്ലാഹ്! OPC ആക്കിയത് നന്നായി. എന്നാ സർട്ടിഫിക്കറ്റ് വന്നത്?"),
 (0,"ഇരുപത്തിയെട്ട് ദിവസം മുമ്പ്. ഇപ്പോ ബ്രഷ് മാത്രം. പേപ്പർ ഒക്കെ പിന്നെ."),
 (1,"ഒന്ന് നിൽക്ക്. ആദ്യത്തെ ഓഡിറ്ററെ മുപ്പത് ദിവസത്തിനുള്ളിൽ വെക്കണം. OPC ആയാലും."),
 (0,"രണ്ട് ദിവസമോ?! ഒറ്റയ്ക്കുള്ള കമ്പനിക്ക് ഇതൊന്നും വേണ്ടെന്ന് ഞാൻ കരുതി."),
 (1,"വേണം. ഇന്ന് തന്നെ ഒരു ഓഡിറ്ററെ വിളിക്ക്. എന്റെ കസിൻ ഉണ്ട്, നമ്പർ അയക്കാം."),
 (0,"അയക്ക്. ഇന്ന് വൈകിട്ട് തന്നെ സംസാരിക്കാം."),
 (1,"ഗുഡ്. ആദ്യത്തെ പാനൽ എന്റെ വീട്ടിൽ, ഓർമ്മയ്ക്ക്!")],
 "ഒറ്റയ്ക്കുള്ള കമ്പനിക്കും\n30 ദിവസം ബാധകം", CTA_AFTER,
 cap_ml="വീടുകൾക്ക് അറബിക് കാലിഗ്രഫി ചെയ്യുന്ന യുവാവിന്റെ OPC-ക്ക് 28 ദിവസം; 40 വില്ലയുടെ ഓർഡർ വന്നു, ഓഡിറ്റർ ഇല്ല. വൺ പേഴ്സൺ കമ്പനിയും ഉണ്ടായി 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A solo Arabic-calligraphy artist in Kerala wins panels for 40 villas, and his One Person Company is 28 days old with no auditor. An OPC must also appoint its first auditor within 30 days of incorporation.",
 cap_mg="Veedukalkku Arabic calligraphy cheyyunna aalude OPC-kku 28 divasam; 40 villa-yude order vannu, auditor illa. One Person Company-um undaayi 30 days-inullil first auditor-e appoint cheyyanam.")
