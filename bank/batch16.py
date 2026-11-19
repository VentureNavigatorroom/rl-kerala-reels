# Script bank, batch 16. New situations: a freelance game tester who names his company after an app store, a food photographer
# for a seafood exporter living in her brother's house, a Flutter developer whose certificate came during a hackathon (day 26, no
# auditor), a packaging designer for Ayurveda brands who wants a Pvt Ltd "just me", a GPS installer for truck fleets at day 175, a
# web developer for weavers whom a Delhi crafts marketplace wants 20% of, a UX researcher whose Singapore client starts in 3 weeks;
# milk-subscription cofounders naming themselves like the big dairy brand, podcast-network cofounders who want a partnership "for
# now" a month before an investor meeting, two physios opening a clinic for football academies in a rented room, rubber-seed oil
# cofounders at day 27, siblings installing tender-coconut machines with no sales yet, app cofounders mid-launch at day 160;
# a salaried hotel chef's chutney powder for a supermarket whose vendor window closes in 3 weeks, a car surveyor's weekend used-car
# inspection a dealer wants 10% of, a college librarian alone with an audiobook app, a pharma rep's diabetic snacks at day 21,
# a call-centre lead's train snack boxes named almost like an existing company, a Technopark engineer's smart-home installs at day 172.
# Same fact list and no-price rule as batch01. Segments freelancer 7, cofounders 7, salaried 6; 16 duo3d in 16 different locations,
# all among the least used so far, default names. Audience data: 7 posting days, so no audience-led shift (see INSIGHTS.md run 7).
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

# ---------------- freelancer ----------------
# canteen: Athira + Amal. Amal tests mobile games freelance for studios abroad and wants to call his company "Play Store Testers".
duo("d1801", "freelancer", "B", "canteen", "ഗെയിം ടെസ്റ്റർ.\nകമ്പനിയുടെ പേര്:\n\"പ്ലേ സ്റ്റോർ ടെസ്റ്റേഴ്സ്\"", [
 ("A","wide","അമലേ, ഊണ് തണുത്തു. ഫോണിൽ ഇപ്പോഴും ആ ഡ്രാഗണിനെ കൊല്ലുവാണോ?"),
 ("V","V","ആതിരേ, ഇത് കളിയല്ല, ജോലിയാ. ഫിൻലൻഡിലെ ഒരു സ്റ്റുഡിയോയുടെ പുതിയ ഗെയിം. ബഗ് കണ്ടുപിടിക്കണം."),
 ("A","A","അത് കൊള്ളാം. അവർ കമ്പനി ഇൻവോയ്സ് ചോദിച്ചെന്നല്ലേ പറഞ്ഞത്?"),
 ("V","V","അതേ. പേരും തീരുമാനിച്ചു. പ്ലേ സ്റ്റോർ ടെസ്റ്റേഴ്സ് പ്രൈവറ്റ് ലിമിറ്റഡ്. കേട്ടാൽ തന്നെ ആളുകൾക്ക് മനസ്സിലാകും."),
 ("A","wide","മനസ്സിലാകും. ആ ബ്രാൻഡിന്റെ ഉടമകൾക്കും മനസ്സിലാകും!"),
 ("A","A","വേറൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് റിജക്ട് ആകാം."),
 ("V","V","അയ്യോ. എങ്കിൽ എന്റെ സ്വന്തം വാക്ക് വേണം."),
 ("A","A","നിന്റെ നാട്ടിലെ ഒരു വാക്ക്, ഒരു ഗെയിം പദം. വേറിട്ട മൂന്ന് പേര് എഴുതി വെക്ക്."),
 ("V","wide","എങ്കിൽ ബഗ് പിടുത്തം ആദ്യം പേരിൽ നിന്ന് തുടങ്ങാം!")],
 "വലിയ ബ്രാൻഡിന്റെ പേര്\nനിങ്ങളുടെ കമ്പനിക്ക് വേണ്ട", CTA_NAME,
 cap_ml="വിദേശ സ്റ്റുഡിയോകൾക്ക് മൊബൈൽ ഗെയിം ടെസ്റ്റ് ചെയ്യുന്ന ഫ്രീലാൻസർ കമ്പനിക്ക് ഒരു ആപ്പ് സ്റ്റോറിന്റെ പേര് ഇടാൻ നോക്കുന്നു. മറ്റൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന കമ്പനി പേര് റിജക്ട് ആകാം; സ്വന്തമായ വേറിട്ട പേരുകൾ കരുതൂ.",
 cap_en="A freelance game tester in Kerala working for studios abroad wants his company named after a famous app store. A company name that clashes with someone else's trademark can be rejected, so shortlist distinctive names of your own before you register.",
 cap_mg="Videsha studio-kalkku mobile game test cheyyunna freelancer company-kku oru app store-nte peru idaan nokkunnu. Vere aalude trademark-umaayi clash aakunna company name reject aakaam; swanthamaaya vere names karuthu.")

# fishmarket: Suma + Antony. Suma shoots food photos freelance; a seafood exporter wants a year of catalogue shoots, billed by a company. She lives in her brother's house.
duo("d1802", "freelancer", "C", "fishmarket", "സീഫുഡ് എക്സ്പോർട്ടറുടെ\nഒരു വർഷത്തെ ഫോട്ടോഷൂട്ട്.\nവീട് ആങ്ങളയുടേത്", [
 ("V","wide","സുമേ, ഈ ചെമ്മീൻ മൂന്നാമത്തെ തവണയാ ലൈറ്റിന് മുന്നിൽ പോസ് ചെയ്യുന്നത്!"),
 ("A","A","ആന്റണിച്ചേട്ടാ, ഇത് സാധാരണ ഫോട്ടോ അല്ല. ആ എക്സ്പോർട്ട് കമ്പനിയുടെ കാറ്റലോഗിനാ. ഒരു വർഷത്തെ കരാർ."),
 ("V","V","ആഹാ! അപ്പോ ബില്ല് ഒക്കെ എങ്ങനെ?"),
 ("A","A","കമ്പനി പേരിൽ വേണം. പക്ഷേ ഓഫീസ് അഡ്രസ്സ് എന്ത് കൊടുക്കും? ഞാൻ താമസിക്കുന്നത് ആങ്ങളയുടെ വീട്ടിലാ."),
 ("V","wide","അത് മതി. വീട്ടിലെ അഡ്രസ്സ് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം."),
 ("V","V","ആങ്ങളയുടെ NOC വേണം. പിന്നെ ആ വീടിന്റെ പുതിയ കറന്റ് ബില്ലോ വെള്ളക്കരം ബില്ലോ."),
 ("A","A","അത്രയേ ഉള്ളോ? ഞാൻ കരുതി ടൗണിൽ മുറി എടുക്കണമെന്ന്."),
 ("V","V","മുറി വേണ്ട. ആങ്ങളയ്ക്ക് ഒരു കിലോ ചെമ്മീൻ കൊടുത്താൽ NOC റെഡി!"),
 ("A","wide","ചെമ്മീൻ ഫോട്ടോയ്ക്കുള്ളതാ. ആങ്ങളയ്ക്ക് ചായ മതി!")],
 "വീട്ടിലെ അഡ്രസ്സും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="ഫ്രീലാൻസ് ഫുഡ് ഫോട്ടോഗ്രാഫർക്ക് സീഫുഡ് എക്സ്പോർട്ടറുടെ ഒരു വർഷത്തെ കാറ്റലോഗ് ഷൂട്ട്, ബില്ല് കമ്പനി പേരിൽ വേണം. താമസിക്കുന്നത് ആങ്ങളയുടെ വീട്ടിൽ; അദ്ദേഹത്തിന്റെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ ആ വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A freelance food photographer in Kerala lands a year of catalogue shoots for a seafood exporter, billed by a company. She lives in her brother's house: with his NOC and a recent utility bill, that home can be the company's registered office.",
 cap_mg="Freelance food photographer-kku seafood exporter-nte oru varshathe catalogue shoot, bill company peril venam. Thaamasikkunnathu aangalayude veettil; adheham NOC-um puthiya utility bill-um thannaal aa veedu registered office aakkaam.")

# hostel: Alina + Sanju. Sanju builds Flutter apps freelance; the certificate came 26 days ago, in the middle of a 48-hour hackathon. No auditor yet.
duo("d1803", "freelancer", "B", "hostel", "48 മണിക്കൂർ ഹാക്കത്തോൺ.\nകമ്പനിക്ക് 26 ദിവസം.\nഓഡിറ്റർ? ആര്?", [
 ("A","wide","സഞ്ജൂ, രണ്ട് ദിവസമായി ഉറങ്ങിയില്ലല്ലോ. ഹാക്കത്തോൺ എങ്ങനെ?"),
 ("V","V","അലീനേ, രണ്ടാം സ്ഥാനം! ഇനി ഒരാഴ്ച ഉറക്കം മാത്രം."),
 ("A","A","ഉറങ്ങും മുമ്പ് ഒന്ന് ചോദിക്കട്ടെ. നിന്റെ കമ്പനിയുടെ സർട്ടിഫിക്കറ്റ് വന്നിട്ട് എത്ര ദിവസമായി?"),
 ("V","V","ഹാക്കത്തോണിന്റെ തലേന്ന് വന്നു. ഏകദേശം ഇരുപത്തിയാറ് ദിവസം."),
 ("A","wide","ആദ്യത്തെ ഓഡിറ്ററെ കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ വെക്കണം. നിനക്ക് ഇനി നാല് ദിവസം."),
 ("V","V","നാല് ദിവസമോ? ഞാൻ കരുതി ഓഡിറ്റർ വർഷാവസാനം മതിയെന്ന്."),
 ("A","A","വർഷാവസാനം അല്ല. ഇപ്പോൾ. ഉറക്കം രണ്ട് ദിവസം കൂടി നീട്ടി വെക്ക്."),
 ("V","wide","ശരി. ആദ്യം ഓഡിറ്റർ, പിന്നെ ഉറക്കം. ബഗ് ഫിക്സ് പോലെ!")],
 "സർട്ടിഫിക്കറ്റ് വന്നോ?\n30 ദിവസം എണ്ണിത്തുടങ്ങൂ", CTA_AFTER,
 cap_ml="ഫ്രീലാൻസ് ഫ്ലട്ടർ ഡെവലപ്പറുടെ കമ്പനി സർട്ടിഫിക്കറ്റ് വന്നത് ഹാക്കത്തോണിന്റെ തലേന്ന്; ഇപ്പോൾ 26 ദിവസം, ഓഡിറ്റർ ഇല്ല. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി ഉണ്ടായി 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A freelance Flutter developer in Kerala got his company certificate the day before a hackathon and is now at day 26 with no auditor. A private limited company must appoint its first auditor within 30 days of incorporation, not at year end.",
 cap_mg="Freelance Flutter developer-nte company certificate vannathu hackathon-nte thalennu; ippol 26 divasam, auditor illa. Pvt Ltd company undaayi 30 days-inullil first auditor-e appoint cheyyanam, varshaavasaanam alla.")

# pharmacy: Sini + Praveen. Praveen designs packaging for Ayurveda brands freelance and wants a Pvt Ltd with himself as the only director and shareholder.
duo("d1804", "freelancer", "A", "pharmacy", "ആയുർവേദ ബ്രാൻഡുകളുടെ\nപാക്കിംഗ് ഡിസൈനർ:\n\"Pvt Ltd, ഞാൻ മാത്രം\"", [
 ("V","wide","സിനീ, ഈ എണ്ണക്കുപ്പിയുടെ ലേബൽ നോക്ക്. എന്റെ ഡിസൈൻ!"),
 ("A","A","പ്രവീണേ, കൊള്ളാം. ഇത് ഇപ്പോ എത്രാമത്തെ ബ്രാൻഡാ?"),
 ("V","V","ഏഴാമത്തെ. രണ്ട് വലിയ കമ്പനികൾ ഇനി ഒരു വർഷത്തെ കരാർ തരും. പക്ഷേ എന്റെ കമ്പനിയുമായി മാത്രം."),
 ("V","V","അതുകൊണ്ട് പ്രൈവറ്റ് ലിമിറ്റഡ്. ഡയറക്ടറും ഷെയർഹോൾഡറും ഞാൻ മാത്രം."),
 ("A","wide","അത് പറ്റില്ല. പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം."),
 ("V","V","എന്റെ കൂടെ ആരുമില്ല. ഭാര്യക്ക് ഡിസൈൻ എന്ന് കേട്ടാൽ തലവേദന."),
 ("A","A","എങ്കിൽ വൺ പേഴ്സൺ കമ്പനി. OPC. ഒറ്റയ്ക്ക് തുടങ്ങാൻ വേണ്ടി തന്നെ ഉള്ളതാ."),
 ("V","wide","ഒറ്റയ്ക്ക് കമ്പനി! എന്റെ ലേബൽ പോലെ. ചെറുത്, പക്ഷേ ഒഫീഷ്യൽ!")],
 "ഒറ്റയ്ക്കാണോ?\nOPC നോക്കൂ", CTA_START,
 cap_ml="ആയുർവേദ ബ്രാൻഡുകൾക്ക് പാക്കിംഗ് ഡിസൈൻ ചെയ്യുന്ന ഫ്രീലാൻസർക്ക് രണ്ട് കമ്പനികളുടെ ഒരു വർഷത്തെ കരാർ, കമ്പനിയുമായി മാത്രം. പ്രൈവറ്റ് ലിമിറ്റഡിന് 2 ഡയറക്ടറും 2 ഷെയർഹോൾഡറും വേണം; ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC) നോക്കാം.",
 cap_en="A freelance packaging designer for Ayurveda brands wants a private limited company with himself as the only director. A Pvt Ltd needs at least two directors and two shareholders; a solo founder can register a One Person Company (OPC) instead.",
 cap_mg="Ayurveda brands-nu packaging design cheyyunna freelancer-kku 2 company-yude contract, company-yumaayi maathram. Pvt Ltd-nu 2 director-um 2 shareholder-um venam; ottaykkaanenkil One Person Company (OPC) nokkaam.")

# petrolpump: Santhosh + Shibu. Shibu fits GPS trackers in trucks freelance; his company was formed for a logistics firm's yearly contract and is 175 days old. No INC-20A.
duo("d1805", "freelancer", "B", "petrolpump", "ലോറികളിൽ GPS ഫിറ്റ്.\nകമ്പനിക്ക് 175 ദിവസം.\nഅഞ്ച് ദിവസം ബാക്കി", [
 ("A","wide","ഷിബൂ, ഇന്ന് എത്ര ലോറിയിൽ GPS വെച്ചു?"),
 ("V","V","സന്തോഷേട്ടാ, പതിനാല്. ആ ലോജിസ്റ്റിക്സ് കമ്പനിയുടെ നൂറ്റിയിരുപത് ലോറിയും ഈ വർഷം എന്റെ കയ്യിൽ!"),
 ("A","A","അതിനല്ലേ ആറ് മാസം മുമ്പ് കമ്പനി ആക്കിയത്. INC-20A ഫയൽ ചെയ്തോ?"),
 ("V","V","അതെന്താ? പുതിയ GPS മോഡലോ?"),
 ("A","wide","ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ഫോം. കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ."),
 ("V","V","ഇന്ന് നൂറ്റിയെഴുപത്തഞ്ചാം ദിവസം. ലോറി എവിടെ എന്ന് എനിക്കറിയാം. എന്റെ ഡെഡ്‌ലൈൻ എവിടെ എന്ന് അറിഞ്ഞില്ല!"),
 ("A","A","മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർമാർക്ക് ദിവസം ആയിരം രൂപ വേറെ."),
 ("V","wide","നാളെ ലോറി വേണ്ട. ആദ്യം ഫോം!")],
 "ലോറി ട്രാക്ക് ചെയ്യുന്നുണ്ടോ?\nഡെഡ്‌ലൈനും ട്രാക്ക് ചെയ്യൂ", CTA_AFTER,
 cap_ml="ലോറികളിൽ GPS ഫിറ്റ് ചെയ്യുന്ന ഫ്രീലാൻസർ ലോജിസ്റ്റിക്സ് കരാറിന് വേണ്ടി കമ്പനി ആക്കി; ഇപ്പോൾ 175 ദിവസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. 180 ദിവസത്തിനുള്ളിൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ.",
 cap_en="A freelance GPS installer formed his company for a logistics firm's 120-truck contract; it is now day 175 and INC-20A is not filed. The commencement form is due within 180 days of incorporation: 50,000 on the company and 1,000 a day per director in default.",
 cap_mg="Lorry-kalil GPS fit cheyyunna freelancer logistics contract-nu vendi company aakki; ippol 175 divasam, INC-20A file cheythittilla. 180 days-inullil cheythillenkil company-kku 50,000 pizha, director-kku divasam 1,000.")

# handloom: Leela + Kumar. Kumar builds online stores for weavers freelance; a Delhi crafts marketplace offers money for 20% of his platform. He bills as a proprietor.
duo("d1806", "freelancer", "A", "handloom", "നെയ്ത്തുകാരുടെ വെബ്സൈറ്റ്\nഉണ്ടാക്കുന്നവൻ. ഡൽഹി:\n\"20% ഷെയർ തരാമോ?\"", [
 ("A","wide","കുമാറേ, എന്റെ സാരി ഇപ്പോ ഓൺലൈനിൽ ബാംഗ്ലൂരിലേക്ക് പോകുന്നു. നിന്റെ വെബ്സൈറ്റ് കൊള്ളാം!"),
 ("V","V","ലീലച്ചേച്ചീ, ഇപ്പോ പതിനെട്ട് നെയ്ത്തുകാർക്ക് ഞാൻ സൈറ്റ് ഉണ്ടാക്കി. ഒരു ഡൽഹി ക്രാഫ്റ്റ് മാർക്കറ്റ്പ്ലേസ് വിളിച്ചു."),
 ("A","A","എന്തിന്? ഓർഡർ തരാനോ?"),
 ("V","V","എന്റെ പ്ലാറ്റ്ഫോമിൽ പൈസ ഇടാൻ. പകരം ഇരുപത് ശതമാനം ഷെയർ. ഞാനാണെങ്കിൽ ഇപ്പോഴും ഒറ്റയ്ക്ക് ബില്ല് അടിക്കുന്ന ഫ്രീലാൻസർ."),
 ("A","wide","ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിലും LLP-യിലും അത് പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി. അതിന് രണ്ട് ഡയറക്ടർ."),
 ("A","A","നിന്റെ കൂടെ കോഡ് എഴുതുന്ന ആ കൂട്ടുകാരി ഇല്ലേ? അവളോട് ചോദിക്ക്."),
 ("V","wide","ചോദിക്കാം. ആദ്യത്തെ ബോർഡ് മീറ്റിംഗ് ചേച്ചിയുടെ തറിയുടെ അടുത്ത്!")],
 "ഷെയർ ചോദിച്ച് ഇൻവെസ്റ്റർ?\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="നെയ്ത്തുകാർക്ക് ഓൺലൈൻ സ്റ്റോർ ഉണ്ടാക്കുന്ന ഫ്രീലാൻസ് വെബ് ഡെവലപ്പറുടെ പ്ലാറ്റ്ഫോമിൽ ഒരു ഡൽഹി മാർക്കറ്റ്പ്ലേസ് പൈസ ഇടാം, പകരം 20% ഷെയർ. പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും ഇക്വിറ്റി എടുക്കാൻ പറ്റില്ല; പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം.",
 cap_en="A freelance web developer who builds online stores for Kerala weavers is offered funding by a Delhi crafts marketplace for 20% of his platform. Only a private limited company can take equity investment; a proprietorship or LLP cannot, so register the Pvt Ltd first.",
 cap_mg="Neythukaarkku online store undaakkunna freelance web developer-nte platform-il oru Delhi marketplace paisa idaam, pakaram 20% share. Proprietorship-inum LLP-kkum equity edukkan pattilla; Pvt Ltd company venam.")

# chat: Nila + Varun. Nila does UX research freelance; a Singapore client's contract starts in three weeks and must be signed with an Indian company.
chat("c1001", "freelancer", "A", "സിംഗപ്പൂർ ക്ലയന്റ്.\n3 ആഴ്ചയിൽ കരാർ.\nകമ്പനി? ഇനിയും ഇല്ല", ("നിള", "വരുൺ"), [
 (0,"വരുൺ, സിംഗപ്പൂരിലെ ആ ഫിൻടെക് ഓക്കെ പറഞ്ഞു! ആറ് മാസത്തെ യൂസർ റിസർച്ച്!"),
 (1,"സൂപ്പർ നിള! എപ്പോ തുടങ്ങും?"),
 (0,"മൂന്ന് ആഴ്ച കഴിഞ്ഞ്. പക്ഷേ കരാർ ഇന്ത്യയിലെ ഒരു രജിസ്റ്റേർഡ് കമ്പനിയുമായി മാത്രം."),
 (0,"അടുത്ത ആഴ്ച ഡോക്യുമെന്റ്സ് നോക്കാമെന്ന് വിചാരിച്ചു."),
 (1,"അടുത്ത ആഴ്ച അല്ല, ഇന്ന്. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 (1,"ഒരാഴ്ച കളഞ്ഞാൽ ആദ്യ മീറ്റിംഗിൽ നീ ഫ്രീലാൻസർ ആയി തന്നെ ഇരിക്കും."),
 (0,"ശരി. ഇന്ന് രാത്രി തന്നെ ഡോക്യുമെന്റ്സ് ലിസ്റ്റ് റെഡിയാക്കാം."),
 (1,"ഗുഡ്. എന്നിട്ട് എന്നെ നിന്റെ ആദ്യത്തെ ടെസ്റ്റ് യൂസർ ആക്കിക്കോ!")],
 "ക്ലയന്റ് റെഡി.\nകമ്പനി റെഡിയാണോ?", CTA_DOCS,
 cap_ml="ഫ്രീലാൻസ് UX റിസർച്ചർക്ക് സിംഗപ്പൂരിലെ ഫിൻടെക്കിന്റെ ആറ് മാസത്തെ കരാർ, മൂന്ന് ആഴ്ചയിൽ തുടങ്ങും, ഇന്ത്യൻ കമ്പനിയുമായി മാത്രം. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; ഡോക്യുമെന്റ്സ് ഇന്ന് തന്നെ തുടങ്ങൂ.",
 cap_en="A freelance UX researcher in Kerala wins a six-month project from a Singapore fintech that will only sign with a registered Indian company, starting in three weeks. Pvt Ltd registration usually takes 7-15 working days, so start the documents today.",
 cap_mg="Freelance UX researcher-kku Singapore fintech-nte 6 maasathe contract, 3 aazhchayil thudangum, Indian company-yumaayi maathram. Pvt Ltd register cheyyan saadharana 7-15 working days; documents innu thanne thudangu.")

# ---------------- cofounders ----------------
# bank: Shruthi + Manoj. Two cofounders of a morning milk-subscription app want a name that sounds just like the state's best-known dairy brand.
duo("d1807", "cofounders", "B", "bank", "പാൽ സബ്സ്ക്രിപ്ഷൻ ആപ്പ്.\nപേര് നാട്ടിലെ വലിയ\nപാൽ ബ്രാൻഡ് പോലെ", [
 ("V","wide","ശ്രുതീ, ലോഗോ റെഡി! നീല പശു, വെള്ള അക്ഷരം."),
 ("A","A","മനോജേ, ഇത് കണ്ടാൽ എല്ലാവരും വിചാരിക്കും ആ വലിയ പാൽ ബ്രാൻഡിന്റെ ആപ്പ് ആണെന്ന്."),
 ("V","V","അതാ ഐഡിയ. പേരും അതുപോലെ. ഒരക്ഷരം മാത്രം മാറ്റി. ആളുകൾ പെട്ടെന്ന് വിശ്വസിക്കും."),
 ("A","wide","വിശ്വസിക്കും. പക്ഷേ നിലവിലുള്ള കമ്പനിയുടെ പേരിനോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("V","V","ഒരക്ഷരം മാറ്റിയാലും?"),
 ("A","A","ഒരക്ഷരം മാറ്റിയാലും കേൾക്കുമ്പോൾ ഒരുപോലെ ആണെങ്കിൽ പ്രശ്നമാ."),
 ("V","V","എങ്കിൽ നമ്മുടെ സ്വന്തം പേര് വേണം. രാവിലെ അഞ്ചരയ്ക്ക് പാൽ എത്തിക്കുന്നവർ."),
 ("A","wide","അഞ്ചര! അതൊരു നല്ല പേരാ. ബാക്കപ്പിന് രണ്ട് പേര് കൂടി എഴുത്!")],
 "കോപ്പി പേര് വേണ്ട.\nസ്വന്തം പേര് മതി", CTA_NAME,
 cap_ml="രാവിലത്തെ പാൽ സബ്സ്ക്രിപ്ഷൻ ആപ്പ് തുടങ്ങുന്ന രണ്ട് കോ-ഫൗണ്ടർമാർ നാട്ടിലെ വലിയ പാൽ ബ്രാൻഡിനോട് സാമ്യമുള്ള പേര് ഇടാൻ നോക്കുന്നു. നിലവിലുള്ള കമ്പനി പേരിനോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യം ഉള്ള പേര് റിജക്ട് ആകാം.",
 cap_en="Two cofounders starting a morning milk-subscription app in Kerala want a name one letter away from the state's best-known dairy brand. A company name similar to an existing company or a trademark can be rejected, so pick something of your own.",
 cap_mg="Raavilathe paal subscription app thudangunna 2 co-founders naattile valiya paal brand-inodu saamyam ulla peru idaan nokkunnu. Existing company name-inodo trademark-inodo saamyam ulla peru reject aakaam.")

# busstop: Jibin + Akhil. Two friends running a Malayalam podcast network meet an investor next month; Jibin wants a partnership "for now".
duo("d1808", "cofounders", "A", "busstop", "മലയാളം പോഡ്കാസ്റ്റ് നെറ്റ്‌വർക്ക്.\nഇൻവെസ്റ്റർ മീറ്റിംഗ്\nഅടുത്ത മാസം", [
 ("A","wide","അഖിലേ, ബസ് വരുന്നത് വരെ ഒന്ന് കേൾക്ക്. ഇൻവെസ്റ്റർ അടുത്ത മാസം പത്താം തീയതി കാണാമെന്ന്!"),
 ("V","V","ജിബിനേ, നമ്മുടെ പന്ത്രണ്ട് പോഡ്കാസ്റ്റിനും കൂടി ഒരു കമ്പനി വേണ്ടേ?"),
 ("A","A","അതിനാ പ്ലാൻ. ഇപ്പോ ഒരു പാർട്ണർഷിപ്പ് ഡീഡ്. പൈസ വന്നിട്ട് കമ്പനി ആക്കാം."),
 ("V","wide","ഇൻവെസ്റ്റർ ഷെയർ ചോദിക്കും. പാർട്ണർഷിപ്പിൽ ഷെയർ കൊടുക്കാൻ പറ്റില്ല. അതിന് പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം."),
 ("A","A","അപ്പോ മീറ്റിംഗിന് മുമ്പ് തന്നെ കമ്പനി വേണം."),
 ("V","V","അതേ. സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. ഒരു മാസം ഉണ്ട്. ഇപ്പോ തുടങ്ങിയാൽ മതി."),
 ("A","A","രണ്ട് ഡീഡ് ഉണ്ടാക്കി സമയം കളയണ്ട, അല്ലേ?"),
 ("V","wide","ഇല്ല. ഈ ബസ് സ്റ്റോപ്പിൽ നിന്ന് നേരെ ഡോക്യുമെന്റ്സിലേക്ക്!")],
 "ഇൻവെസ്റ്റർ വരും മുമ്പ്\nശരിയായ കമ്പനി", CTA_START,
 cap_ml="മലയാളം പോഡ്കാസ്റ്റ് നെറ്റ്‌വർക്ക് നടത്തുന്ന രണ്ട് കൂട്ടുകാർക്ക് അടുത്ത മാസം ഇൻവെസ്റ്റർ മീറ്റിംഗ്; ഒരാൾക്ക് ഇപ്പോൾ പാർട്ണർഷിപ്പ് മതി. ഷെയർ കൊടുത്ത് ഫണ്ട് വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം; രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="Two cofounders of a Malayalam podcast network meet an investor next month, and one wants a partnership deed for now. An investor will want shares, which only a private limited company can issue; registration usually takes 7-15 working days, so start now.",
 cap_mg="Malayalam podcast network nadathunna 2 friends-nu adutha maasam investor meeting; oraalkku ippol partnership mathi. Share koduthu fund vaangan Pvt Ltd venam; register cheyyan saadharana 7-15 working days.")

# hospital: Lakshmi + Joseph. Two physiotherapists open a sports-injury clinic for football academies in a rented room; the landlord lives next door.
duo("d1809", "cofounders", "C", "hospital", "ഫുട്ബോൾ അക്കാദമികൾക്ക്\nഫിസിയോ ക്ലിനിക്.\nമുറി വാടകയ്ക്ക്", [
 ("A","wide","ജോസഫേ, മൂന്ന് ഫുട്ബോൾ അക്കാദമികൾ ഒപ്പിട്ടു! എല്ലാ കളിക്കാരുടെയും ഫിസിയോ നമ്മൾ."),
 ("V","V","ലക്ഷ്മീ, അപ്പോ ക്ലിനിക്ക് കമ്പനി ആക്കണം. ഓഫീസ് അഡ്രസ്സ് ഈ വാടകമുറി തന്നെ."),
 ("A","A","മുറി വാടകയ്ക്കല്ലേ? അത് കമ്പനി ഓഫീസ് ആക്കാൻ പറ്റുമോ?"),
 ("V","wide","പറ്റും. ഉടമയുടെ NOC വേണം. പിന്നെ ഈ മുറിയുടെ പുതിയ ഒരു കറന്റ് ബില്ലും."),
 ("A","A","ഉടമ തൊട്ടടുത്ത വീട്ടിലല്ലേ? മുട്ടുവേദനയ്ക്ക് നമ്മുടെ അടുത്ത് വരുന്ന ആ ചേട്ടൻ?"),
 ("V","V","അതേ. ഇന്ന് വൈകിട്ട് അദ്ദേഹത്തിന്റെ സെഷൻ ഉണ്ട്."),
 ("A","wide","എങ്കിൽ സെഷൻ കഴിഞ്ഞ് NOC. മുട്ടും ശരി, പേപ്പറും ശരി!")],
 "വാടകമുറിയും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="ഫുട്ബോൾ അക്കാദമികൾക്കായി സ്പോർട്സ് ഫിസിയോ ക്ലിനിക് തുടങ്ങുന്ന രണ്ട് ഫിസിയോതെറാപ്പിസ്റ്റുകൾ. വാടകമുറി കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം; ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഡോക്യുമെന്റ്സിൽ വേണം.",
 cap_en="Two physiotherapist cofounders open a sports-injury clinic for football academies in a rented room in Kerala. A rented space can be the company's registered office, with the owner's NOC and a recent utility bill among the documents.",
 cap_mg="Football academy-kalkku sports physio clinic thudangunna 2 physiotherapists. Vaadaka muri company-yude registered office aakkaam; owner-nte NOC-um puthiya utility bill-um documents-il venam.")

# rubber: Joy + Thomas. Two cofounders press rubber-seed oil for soap makers; the company is 27 days old and each thinks the other appointed the auditor.
duo("d1810", "cofounders", "B", "rubber", "റബ്ബർക്കുരു എണ്ണ കമ്പനി.\n27 ദിവസം.\n\"ഓഡിറ്റർ നീ വെച്ചില്ലേ?\"", [
 ("V","wide","ജോയിച്ചാ, ആ സോപ്പ് കമ്പനിക്ക് ആദ്യത്തെ ഇരുനൂറ് ലിറ്റർ എണ്ണ പോയി!"),
 ("A","A","തോമസേ, നന്നായി. പിന്നെ, ഓഡിറ്ററുടെ കാര്യം നീ ശരിയാക്കിയല്ലോ?"),
 ("V","V","ഞാനോ? അത് ജോയിച്ചൻ നോക്കുമെന്നല്ലേ പറഞ്ഞത്?"),
 ("A","wide","ഞാൻ കരുതി നീ നോക്കുമെന്ന്. രണ്ട് ഡയറക്ടർമാരും മറ്റേ ആളെ നോക്കി ഇരുന്നു!"),
 ("V","V","കമ്പനി ഉണ്ടായിട്ട് എത്ര ദിവസമായി?"),
 ("A","A","ഇരുപത്തിയേഴ്. ആദ്യത്തെ ഓഡിറ്ററെ മുപ്പത് ദിവസത്തിനുള്ളിൽ വെക്കണം."),
 ("V","V","മൂന്ന് ദിവസം! എണ്ണ ആട്ടുന്നതിനേക്കാൾ വേഗം വേണം."),
 ("A","wide","ഇനി മുതൽ ഒരു ലിസ്റ്റ്. ഓരോ ജോലിക്കും ഒരു പേര്. ഊഹം വേണ്ട!")],
 "രണ്ട് ഡയറക്ടർ.\nഓഡിറ്റർ ആരുടെ ജോലി?", CTA_AFTER,
 cap_ml="റബ്ബർക്കുരുവിൽ നിന്ന് സോപ്പ് കമ്പനികൾക്കുള്ള എണ്ണ ഉണ്ടാക്കുന്ന രണ്ട് കോ-ഫൗണ്ടർമാർ; കമ്പനിക്ക് 27 ദിവസം, ഓഡിറ്ററെ മറ്റേ ആൾ വെച്ചു എന്ന് രണ്ടുപേരും കരുതി. ആദ്യത്തെ ഓഡിറ്ററെ 30 ദിവസത്തിനുള്ളിൽ നിയമിക്കണം.",
 cap_en="Two cofounders pressing rubber-seed oil for soap makers in Kerala are at day 27, and each thought the other had appointed the auditor. A private limited company must appoint its first auditor within 30 days of incorporation; give every task one owner.",
 cap_mg="Rubber kuruvil ninnu soap company-kalkkulla enna undaakkunna 2 co-founders; company-kku 27 divasam, auditor-e mattethaal vechu ennu randuperum karuthi. First auditor-e 30 days-inullil appoint cheyyanam.")

# juiceshop: Raziya + Naushad. Siblings are installing tender-coconut vending machines at stations; the company is a year old, machines not running, no sales.
duo("d1811", "cofounders", "B", "juiceshop", "കരിക്ക് വെൻഡിംഗ് മെഷീൻ.\nഒരു വർഷം. ഒരു കരിക്ക്\nപോലും വിറ്റില്ല", [
 ("V","wide","റസിയാ, മൂന്നാമത്തെ സ്റ്റേഷനിലും മെഷീൻ ഫിറ്റ് ചെയ്തു. കറന്റ് കണക്ഷൻ മാത്രം ബാക്കി."),
 ("A","A","നൗഷാദേ, കമ്പനി തുടങ്ങിയിട്ട് ഒരു വർഷമായി. ആനുവൽ ഫയലിംഗ് ആയില്ലേ?"),
 ("V","V","എന്ത് ഫയലിംഗ്? ഒരു കരിക്ക് പോലും വിറ്റില്ല. വരുമാനം പൂജ്യം."),
 ("A","wide","വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("A","A","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. ദിവസം കൂടുന്തോറും കൂടും."),
 ("V","V","മെഷീൻ ഓടിയില്ലെങ്കിലും പിഴ ഓടും, അല്ലേ?"),
 ("A","A","അതേ. ഈ ആഴ്ച ഓഡിറ്ററെ കാണാം. ബാലൻസ് ഷീറ്റ് പൂജ്യം ആണെങ്കിലും."),
 ("V","wide","ശരി. ആദ്യത്തെ കരിക്ക് ഓഡിറ്റർക്ക്, ഫ്രീ!")],
 "വിൽപ്പന തുടങ്ങിയില്ല.\nഫയലിംഗ് തുടങ്ങണം", CTA_AFTER,
 cap_ml="റെയിൽവേ സ്റ്റേഷനുകളിൽ കരിക്ക് വെൻഡിംഗ് മെഷീൻ വെക്കുന്ന സഹോദരങ്ങളുടെ കമ്പനിക്ക് ഒരു വർഷം, ഇതുവരെ വിൽപ്പന ഇല്ല. വരുമാനം പൂജ്യം ആയാലും ആനുവൽ ROC ഫയലിംഗ് ചെയ്യണം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="Sibling cofounders installing tender-coconut vending machines at Kerala railway stations reach their company's first year with no sales yet. Annual ROC filing is due even with zero revenue, and each late form costs 100 a day.",
 cap_mg="Railway station-kalil karikku vending machine vekkunna siblings-nte company-kku oru varsham, ithuvare sales illa. Varumanam zero aayaalum annual ROC filing cheyyanam; vaikiyal oro form-inum divasam 100 pizha.")

# chat: Febin + Anagha. Their bus-stop ad-screen startup launches next week; Anagha notices the company is 160 days old and INC-20A is pending.
chat("c1002", "cofounders", "B", "ലോഞ്ച് അടുത്ത ആഴ്ച.\nകമ്പനിക്ക് 160 ദിവസം.\nഒരു ഫോം മറന്നു", ("ഫെബിൻ", "അനഘ"), [
 (0,"അനഘേ, ആദ്യത്തെ പത്ത് ബസ് സ്റ്റോപ്പ് സ്ക്രീനും റെഡി! ലോഞ്ച് വ്യാഴാഴ്ച."),
 (1,"സൂപ്പർ ഫെബിൻ. ഒരു ചെറിയ കാര്യം. നമ്മുടെ കമ്പനിക്ക് ഇന്ന് നൂറ്റിയറുപത് ദിവസം."),
 (0,"അതിന്? കേക്ക് മുറിക്കണോ?"),
 (1,"INC-20A ഫയൽ ചെയ്തിട്ടില്ല. ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ഫോം. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ വേണം."),
 (0,"ഇരുപത് ദിവസം ഉണ്ടല്ലോ. ലോഞ്ച് കഴിഞ്ഞ് നോക്കാം."),
 (1,"ലോഞ്ച് കഴിഞ്ഞാൽ നമ്മൾ ഉറങ്ങും. മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. നമുക്ക് രണ്ടുപേർക്കും ദിവസം ആയിരം രൂപ വേറെ."),
 (0,"ശരി ശരി. നാളെ രാവിലെ ആദ്യം ഫോം. പിന്നെ സ്ക്രീൻ."),
 (1,"ഡീൽ. ലോഞ്ചിന്റെ ആദ്യ സ്ലൈഡിൽ എഴുതാം: ഫയൽ ചെയ്ത കമ്പനി!")],
 "ലോഞ്ചിന്റെ തിരക്കിൽ\nINC-20A മറക്കരുത്", CTA_AFTER,
 cap_ml="ബസ് സ്റ്റോപ്പുകളിൽ പരസ്യ സ്ക്രീൻ വെക്കുന്ന സ്റ്റാർട്ടപ്പിന്റെ കോ-ഫൗണ്ടർമാർ ലോഞ്ചിന്റെ തിരക്കിൽ; കമ്പനിക്ക് 160 ദിവസം, INC-20A ബാക്കി. 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപ.",
 cap_en="Startup cofounders putting ad screens at Kerala bus stops are a week from launch, and their company is at day 160 with INC-20A pending. Miss the 180-day deadline and it is 50,000 on the company plus 1,000 a day for each director in default.",
 cap_mg="Bus stop-il ad screen vekkunna startup co-founders launch-nte thirakkil; company-kku 160 divasam, INC-20A baakki. 180 days-inullil file cheythillenkil company-kku 50,000 pizha, oro director-kkum divasam 1,000.")

lst("l1001", "cofounders", "C", "കോ-ഫൗണ്ടർ അടുത്ത വർഷം\nവിദേശത്തേക്ക് പോകുന്നോ?\n3 കാര്യം അറിയണം", [
 ("വിദേശത്ത് പോയാലും തുടരാം", "NRI-ക്കും ഇന്ത്യൻ Pvt Ltd-ൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. ഷെയർ വിൽക്കേണ്ട."),
 ("ഒരാൾ നാട്ടിൽ വേണം", "കുറഞ്ഞത് ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളായിരിക്കണം."),
 ("ഫയലിംഗ് ദൂരം നോക്കില്ല", "ആനുവൽ ഫയലിംഗ് എല്ലാ വർഷവും. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.")],
 "പോകുന്നതിന് മുമ്പ്\nറോളുകൾ ഉറപ്പിക്കൂ", CTA_START,
 cap_ml="കോ-ഫൗണ്ടർ ഗൾഫിലേക്കോ യൂറോപ്പിലേക്കോ ജോലിക്ക് പോകുന്നുണ്ടോ? NRI-ക്ക് പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആയി തുടരാം, പക്ഷേ ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കണം; ആനുവൽ ഫയലിംഗ് മുടക്കരുത്.",
 cap_en="Is your cofounder moving abroad next year? An NRI can stay on as a director and shareholder of your Indian private limited company, but at least one director must live in India, and annual filings stay due every year.",
 cap_mg="Co-founder Gulf-ilekko Europe-ilekko joli-kku pokunnundo? NRI-kku Pvt Ltd-il director-um shareholder-um aayi thudaraam, pakshe oru director India-yil thaamasikkanam; annual filing mudakkaruthu.")

# ---------------- salaried ----------------
# shop: Binu + Suresh. Suresh, a hotel chef, sells his chutney powder on weekends; a supermarket chain's vendor window closes in three weeks, companies only.
duo("d1812", "salaried", "A", "shop", "ഹോട്ടൽ ഷെഫിന്റെ\nചമ്മന്തിപ്പൊടി. സൂപ്പർമാർക്കറ്റ്:\n\"3 ആഴ്ചയിൽ വെണ്ടർ ലിസ്റ്റ്\"", [
 ("A","wide","സുരേഷേ, ഈ ആഴ്ചയും നിന്റെ ചമ്മന്തിപ്പൊടി മുഴുവൻ തീർന്നു."),
 ("V","V","ബിനുച്ചേട്ടാ, അതിനേക്കാൾ വലിയ കാര്യം. ആ സൂപ്പർമാർക്കറ്റ് ചെയിനിന്റെ പർച്ചേസ് മാനേജർ ഹോട്ടലിൽ ഊണ് കഴിക്കാൻ വന്നു."),
 ("V","V","അവരുടെ പതിനാറ് ഷോപ്പിലും വെക്കാമെന്ന്. പക്ഷേ വെണ്ടർ ലിസ്റ്റ് മൂന്ന് ആഴ്ചയിൽ ക്ലോസ് ചെയ്യും. കമ്പനികൾ മാത്രം."),
 ("A","A","നീ ഹോട്ടലിലെ ജോലി വിടുമോ?"),
 ("V","V","ഇല്ല. ജോലി അവിടെ. ചമ്മന്തി ഇവിടെ. ഞായറാഴ്ച ഓഫിന് നോക്കാമെന്ന് കരുതി."),
 ("A","wide","ഞായറാഴ്ച വരെ കാക്കണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","ഇന്ന് രാത്രി ഡോക്യുമെന്റ്സ് എടുത്ത് വെക്ക്. രണ്ടാമത്തെ ഡയറക്ടർ ആര്?"),
 ("V","wide","ഭാര്യ. ചമ്മന്തിയുടെ രഹസ്യ റെസിപ്പി അവളുടേതാ!")],
 "വെണ്ടർ ലിസ്റ്റ് അടയും മുമ്പ്\nകമ്പനി റെഡി", CTA_DOCS,
 cap_ml="ഹോട്ടലിൽ ഷെഫ് ആയി ജോലി ചെയ്യുന്നയാളുടെ ചമ്മന്തിപ്പൊടി 16 സൂപ്പർമാർക്കറ്റുകളിൽ വെക്കാം, പക്ഷേ വെണ്ടർ ലിസ്റ്റ് മൂന്ന് ആഴ്ചയിൽ അടയും, കമ്പനികൾ മാത്രം. ജോലി വിടാതെ Pvt Ltd തുടങ്ങാം; രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം.",
 cap_en="A salaried hotel chef's weekend chutney powder gets a chance at 16 supermarket outlets, but the vendor list closes in three weeks and takes only companies. Pvt Ltd registration usually takes 7-15 working days, so start the documents tonight.",
 cap_mg="Hotel-il chef aayi joli cheyyunna aalude chammanthippodi 16 supermarket-il vekkaam, pakshe vendor list 3 aazhchayil adayum, company maathram. Joli vidaathe Pvt Ltd thudangaam; register cheyyan saadharana 7-15 working days.")

# garage: Aishwarya + Jithin. Aishwarya, a salaried car-insurance surveyor, inspects used cars for buyers on weekends; a used-car dealer wants 10% for funding.
duo("d1813", "salaried", "A", "garage", "ഇൻഷുറൻസ് സർവേയർ.\nവീക്കെൻഡിൽ യൂസ്ഡ് കാർ ചെക്ക്.\nഡീലർ: \"10% തരാമോ?\"", [
 ("V","wide","ഐശ്വര്യേ, ഈ കാറിന്റെ അടിയിൽ നിന്ന് ഇറങ്ങി വാ. ആ യൂസ്ഡ് കാർ ഡീലർ വീണ്ടും വിളിച്ചു."),
 ("A","A","ജിതിനേ, ഇന്ന് ഞായർ. എന്റെ വീക്കെൻഡ് ഇൻസ്പെക്ഷൻ ദിവസം. എന്താ പറഞ്ഞത്?"),
 ("V","V","നിന്റെ കാർ ചെക്കിംഗ് സർവീസ് മൂന്ന് ജില്ലയിലേക്ക് വളർത്താൻ പൈസ ഇടാമെന്ന്. പകരം പത്ത് ശതമാനം ഷെയർ."),
 ("A","A","ഷെയറോ? ഞാൻ ഇപ്പോ എന്റെ പേരിൽ ബില്ല് കൊടുക്കുന്നതേ ഉള്ളൂ."),
 ("V","wide","അതാ കാര്യം. ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. ഒറ്റയ്ക്കുള്ള ബിസിനസിൽ അത് പറ്റില്ല."),
 ("A","A","ഓഫീസിലെ ജോലി തുടരാമല്ലോ, അല്ലേ?"),
 ("V","V","ജോലി ജോലിയുടെ വഴിക്ക്. കമ്പനി കമ്പനിയുടെ വഴിക്ക്. രണ്ട് ഡയറക്ടർ വേണം, അത്രേ ഉള്ളൂ."),
 ("A","wide","എങ്കിൽ രണ്ടാമത്തെ ഡയറക്ടർ നീ. ടയർ പ്രഷർ ചെക്കിംഗ് നിന്റെ ഡിപ്പാർട്ട്മെന്റ്!")],
 "ഡീലർ ഷെയർ ചോദിച്ചോ?\nആദ്യം കമ്പനി", CTA_START,
 cap_ml="കാർ ഇൻഷുറൻസ് സർവേയർ ആയി ജോലി ചെയ്യുന്ന യുവതി വീക്കെൻഡിൽ യൂസ്ഡ് കാർ ഇൻസ്പെക്ഷൻ നടത്തുന്നു; ഒരു ഡീലർ പൈസ ഇടാം, പകരം 10% ഷെയർ. ഇക്വിറ്റി എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം, ജോലി വിടേണ്ട.",
 cap_en="A salaried car-insurance surveyor in Kerala runs a weekend used-car inspection service, and a dealer offers to fund it for 10%. Only a private limited company can take equity investment, so register a Pvt Ltd with two directors before you take the money.",
 cap_mg="Car insurance surveyor aayi joli cheyyunna aal weekend-il used car inspection nadathunnu; oru dealer paisa idaam, pakaram 10% share. Equity edukkan Pvt Ltd company venam, joli videnda.")

# library: Greeshma + Anoop. Anoop, a college librarian, makes a Malayalam book-summary audio app alone; his wife will not be a director.
duo("d1814", "salaried", "C", "library", "കോളേജ് ലൈബ്രേറിയന്റെ\nഓഡിയോ ആപ്പ്. ഭാര്യ:\n\"ഡയറക്ടർ ഞാനില്ല\"", [
 ("A","wide","അനൂപേ, ലൈബ്രറിയിൽ ഹെഡ്ഫോൺ വെച്ച് ആരോടാ സംസാരിക്കുന്നത്?"),
 ("V","V","ഗ്രീഷ്മേ, ആരോടുമല്ല. എന്റെ ആപ്പിന് പുസ്തകങ്ങളുടെ മലയാളം സംഗ്രഹം റെക്കോർഡ് ചെയ്യുവാ. അഞ്ഞൂറ് പുസ്തകം കഴിഞ്ഞു."),
 ("A","A","കൊള്ളാം! ഒരു പബ്ലിഷർ ലൈസൻസ് തരാമെന്ന് പറഞ്ഞില്ലേ? കമ്പനി ആയോ?"),
 ("V","V","അതാ പ്രശ്നം. കമ്പനിക്ക് രണ്ട് പേര് വേണമെന്ന് കേട്ടു. ഭാര്യയോട് ചോദിച്ചു. ഡയറക്ടർ ആകില്ലെന്ന്."),
 ("A","wide","ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി. OPC. ഒരാൾക്ക് മാത്രമായി തുടങ്ങാം."),
 ("V","V","ജോലി ചെയ്തുകൊണ്ട് തന്നെ?"),
 ("A","A","അതേ. ശമ്പളം ലൈബ്രറിയിൽ നിന്ന്. ആപ്പ് നിന്റെ കമ്പനിയുടേത്."),
 ("V","wide","എങ്കിൽ ആദ്യത്തെ ഓഡിയോ സംഗ്രഹം: ഒറ്റയ്ക്ക് കമ്പനി തുടങ്ങിയ ലൈബ്രേറിയൻ!")],
 "പാർട്ണർ ഇല്ലേ?\nOPC ഉണ്ട്", CTA_START,
 cap_ml="കോളേജ് ലൈബ്രേറിയൻ ജോലിക്കൊപ്പം പുസ്തകങ്ങളുടെ മലയാളം ഓഡിയോ സംഗ്രഹ ആപ്പ് ഉണ്ടാക്കുന്നു; ഭാര്യക്ക് ഡയറക്ടർ ആകാൻ താൽപ്പര്യമില്ല. ഒറ്റയ്ക്കുള്ള ഫൗണ്ടർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) രജിസ്റ്റർ ചെയ്യാം.",
 cap_en="A salaried college librarian in Kerala builds a Malayalam book-summary audio app, and his wife does not want to be a director. A solo founder can register a One Person Company (OPC) and keep the day job.",
 cap_mg="College librarian joli-kkoppam pusthakangalude Malayalam audio summary app undaakkunnu; bhaarya-kku director aakaan thaalparyam illa. Ottaykkulla founder-nu One Person Company (OPC) register cheyyaam.")

# akshaya: Sudha + Ramesh. Ramesh, a pharma sales rep, delivers sugar-free snacks to diabetic patients; his company is 21 days old, no auditor yet.
duo("d1815", "salaried", "B", "akshaya", "മെഡിക്കൽ റെപ്പിന്റെ\nഷുഗർ ഫ്രീ സ്നാക്സ്.\nകമ്പനിക്ക് 21 ദിവസം", [
 ("A","wide","രമേശേ, ഇന്നും ബാഗിൽ മരുന്ന് സാമ്പിളിനൊപ്പം ഷുഗർ ഫ്രീ ലഡ്ഡുവോ?"),
 ("V","V","സുധേച്ചീ, ഡോക്ടർമാർ തന്നെ ചോദിക്കുന്നു. നൂറ്റിനാൽപ്പത് പ്രമേഹ രോഗികൾക്ക് ഇപ്പോ മാസം ഡെലിവറി."),
 ("A","A","കമ്പനി ആയെന്ന് പറഞ്ഞല്ലോ. എന്ന് വന്നു സർട്ടിഫിക്കറ്റ്?"),
 ("V","V","മൂന്നാഴ്ച മുമ്പ്. ഇരുപത്തിയൊന്ന് ദിവസം. ബാക്കി കാര്യങ്ങൾ മാർച്ചിൽ നോക്കാം."),
 ("A","wide","മാർച്ച് വരെ കാക്കാൻ പറ്റില്ല. ആദ്യത്തെ ഓഡിറ്ററെ മുപ്പത് ദിവസത്തിനുള്ളിൽ വെക്കണം."),
 ("V","V","ഒമ്പത് ദിവസം മാത്രം! ഈ മാസം ടാർഗറ്റും ഉണ്ട്."),
 ("A","A","ടാർഗറ്റ് കമ്പനിയുടേത്. ഓഡിറ്റർ നിന്റെ കമ്പനിയുടേത്. രണ്ടും വേണം."),
 ("V","wide","ശരി. നാളത്തെ ആദ്യ കോൾ ഓഡിറ്റർക്ക്. സാമ്പിൾ ലഡ്ഡുവും കൊണ്ടുപോകാം!")],
 "ജോലിയുടെ ടാർഗറ്റിനിടയിൽ\n30 ദിവസം മറക്കരുത്", CTA_AFTER,
 cap_ml="മെഡിക്കൽ റെപ്പ് ആയി ജോലി ചെയ്യുന്നയാൾ പ്രമേഹ രോഗികൾക്ക് ഷുഗർ ഫ്രീ സ്നാക്സ് എത്തിക്കുന്ന കമ്പനി തുടങ്ങി; 21 ദിവസം, ഓഡിറ്റർ ഇല്ല. കമ്പനി ഉണ്ടായി 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A salaried pharma sales rep in Kerala delivers sugar-free snacks to diabetic patients through his new company, now 21 days old with no auditor. The first auditor must be appointed within 30 days of incorporation, whatever the day job's targets.",
 cap_mg="Medical rep aayi joli cheyyunna aal diabetic patients-nu sugar free snacks ethikkunna company thudangi; 21 divasam, auditor illa. Company undaayi 30 days-inullil first auditor-e appoint cheyyanam.")

# railway: Sheeba + Dinesh. Sheeba, a call-centre team lead, sells train-journey snack boxes from Shoranur; her name "Rail Bites" is close to an existing company's.
duo("d1816", "salaried", "B", "railway", "ട്രെയിൻ യാത്രക്കാർക്ക്\nസ്നാക്ക് ബോക്സ്.\nപേര് വേറൊരു കമ്പനിയുടേത്?", [
 ("V","wide","ഷീബേ, ഈ ബോക്സിൽ എന്തൊക്കെയാ? ഉണ്ണിയപ്പം, കായ വറുത്തത്, ഒരു കുഞ്ഞ് കുപ്പി സംഭാരം!"),
 ("A","A","ദിനേശേ, ട്രെയിൻ യാത്രക്കാർക്കുള്ള സ്നാക്ക് ബോക്സ്. ഷിഫ്റ്റ് കഴിഞ്ഞ് രാത്രി പാക്ക് ചെയ്യുന്നതാ."),
 ("A","A","ഒരു ട്രാവൽ ആപ്പ് ലിസ്റ്റ് ചെയ്യാമെന്ന്. കമ്പനി പേര് റെയിൽ ബൈറ്റ്സ്."),
 ("V","V","ആ പേരിൽ ഇപ്പോ തന്നെ ഒരു കമ്പനി ഇല്ലേ? ബാംഗ്ലൂരിൽ കണ്ടതായി ഓർമ്മ."),
 ("A","wide","ഉണ്ടോ? ഞാൻ നോക്കിയില്ല."),
 ("V","V","നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം. ആദ്യം സെർച്ച് ചെയ്യ്."),
 ("A","A","എങ്കിൽ ഷൊർണൂരിന്റെ ഒരു വാക്ക് ചേർക്കാം. നമ്മുടെ ജംഗ്ഷന്റെ മണം വേണം."),
 ("V","wide","മൂന്ന് പേര് എഴുത്. ആദ്യത്തെ ബോക്സ് എനിക്ക്, ടിക്കറ്റ് ഇല്ലാതെ!")],
 "പേര് ഇടും മുമ്പ്\nസെർച്ച് ചെയ്യൂ", CTA_NAME,
 cap_ml="കോൾ സെന്ററിൽ ജോലി ചെയ്യുന്ന യുവതി ഷൊർണൂരിൽ ട്രെയിൻ യാത്രക്കാർക്ക് സ്നാക്ക് ബോക്സ് ഉണ്ടാക്കുന്നു; ഇഷ്ടപ്പെട്ട പേര് നിലവിലുള്ള ഒരു കമ്പനിയുടേതിനോട് സാമ്യമുള്ളത്. കമ്പനി പേര് റിജക്ട് ആകാതിരിക്കാൻ ആദ്യം സെർച്ച് ചെയ്ത് വേറിട്ട പേരുകൾ കരുതൂ.",
 cap_en="A salaried call-centre team lead packs snack boxes for train passengers at Shoranur after her shift, and her chosen company name is close to an existing company's. A name similar to an existing company or LLP can be rejected, so search first and keep backups.",
 cap_mg="Call centre-il joli cheyyunna aal Shoranur-il train yaathrakkaarkku snack box undaakkunnu; ishtapetta peru existing company-yudethinodu saamyam ullathu. Company name reject aakaathirikkan aadyam search cheythu vere names karuthu.")

# chat: Hari + Deepthi. Hari, a Technopark engineer, installs smart-home kits on weekends; his company is 172 days old and INC-20A is pending.
chat("c1003", "salaried", "B", "ഓഫീസിൽ കോഡ്.\nവീക്കെൻഡിൽ സ്മാർട്ട് ഹോം.\n172-ാം ദിവസം", ("ഹരി", "ദീപ്തി"), [
 (1,"ഹരീ, ഈ ശനിയാഴ്ചയും മൂന്ന് വീട്ടിൽ സ്മാർട്ട് ലൈറ്റ് ഫിറ്റിംഗ് ആണോ?"),
 (0,"ദീപ്തീ, നാല്. ഒരു ബിൽഡർ പുതിയ ഫ്ലാറ്റുകൾ മുഴുവൻ തരാമെന്ന് പറഞ്ഞു."),
 (1,"സൂപ്പർ. പിന്നെ, നിന്റെ കമ്പനി തുടങ്ങിയിട്ട് ഏകദേശം ആറ് മാസം ആയില്ലേ? ആ ഫോം?"),
 (0,"ഏത് ഫോം? ഓഫീസിലെ അപ്രൈസൽ ഫോമോ?"),
 (1,"അല്ല. INC-20A. ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്നത്. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 (0,"നോക്കട്ടെ... ഇന്ന് നൂറ്റിയെഴുപത്തിരണ്ടാം ദിവസം! എട്ട് ദിവസം."),
 (1,"മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ വേറെ."),
 (0,"ശനിയാഴ്ചത്തെ ആദ്യ ഫിറ്റിംഗ് ഈ ഫോം. ലൈറ്റ് പിന്നെ!")],
 "ശമ്പള ജോലിക്കിടയിലും\nINC-20A ഓർക്കണം", CTA_AFTER,
 cap_ml="ടെക്നോപാർക്കിലെ എഞ്ചിനീയർ വീക്കെൻഡിൽ സ്മാർട്ട് ഹോം ഇൻസ്റ്റലേഷൻ ചെയ്യുന്നു; സൈഡ് കമ്പനിക്ക് 172 ദിവസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. 180 ദിവസത്തിനുള്ളിൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ.",
 cap_en="A salaried Technopark engineer installs smart-home kits on weekends, and his side company is at day 172 with INC-20A not filed. It is due within 180 days of incorporation: 50,000 on the company and 1,000 a day for each director in default.",
 cap_mg="Technopark-ile engineer weekend-il smart home installation cheyyunnu; side company-kku 172 divasam, INC-20A file cheythittilla. 180 days-inullil cheythillenkil company-kku 50,000 pizha, director-kku divasam 1,000.")
