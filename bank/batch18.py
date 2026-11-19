# Script bank, batch 18. New situations: a freelance technical writer whose German client signs from 1 January (Christmas in the
# middle of the 7-15 working days), a Shopify developer whose landlady downstairs must sign the NOC, a 3D furniture-render artist
# who wants a famous furniture brand's name, a LinkedIn ghostwriter whose US client wants equity, a pet photographer with an idle
# monsoon year, a medical coder in a hostel who thinks he needs lakhs first, an online Carnatic teacher moving to Sydney;
# pharmacists whose delivery-app name is one letter from an existing company, campus EV-scooter cofounders whose investor's cheque
# meets an LLP, millet-snack cofounders who think each must put in lakhs, a mobile puncture-van pair at day 150, a home-salon app
# founder who wants 100% of the shares, robotics-kit cofounders who think the auditor comes at year end, saree-rental sisters whose
# Dubai brother-in-law wants shares; a lab assistant's 3D-printed sewing-machine parts, an airline ground-staff's balcony-garden
# setups for a builder, a mall HR executive's joining kits with her husband in Oman, a mobile-shop employee's refurbished laptops
# named like a phone giant, a night-shift nurse at day 29, a "keep your job, start a company" myths list.
# Same fact list and no-price rule as batch01. Segments freelancer 7, cofounders 7, salaried 6; 16 duo3d in 16 different locations,
# all among the least used so far (none used in batch16/17), default names. Audience data: 8 posting days, so no audience-led shift
# (see INSIGHTS.md run 8). Every script carries cap_ml / cap_en / cap_mg (captions.py adds hook, CTA and hashtags).
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
# office: Neha + Rahul. Rahul writes manuals for a German pump maker; a 3-year contract from 1 January, only with a company; he plans to start mid-December.
duo("d2001", "freelancer", "A", "office", "ജർമ്മൻ ക്ലയന്റ്:\n\"ജനുവരി 1 മുതൽ കരാർ.\nകമ്പനിയുമായി മാത്രം\"", [
 ("V","wide","നേഹാ, ആ ജർമ്മൻ പമ്പ് കമ്പനിക്ക് എന്റെ മാന്വലുകൾ ഇഷ്ടപ്പെട്ടു! മൂന്ന് വർഷത്തെ കരാർ തരാമെന്ന്."),
 ("A","A","സൂപ്പർ രാഹുൽ! ഇനി ട്രീറ്റ് ജർമ്മൻ സ്റ്റൈലിൽ വേണം."),
 ("V","V","ഒരു കണ്ടീഷൻ. ജനുവരി ഒന്ന് മുതൽ കരാർ, അതും കമ്പനിയുമായി മാത്രം. ഫ്രീലാൻസറുമായി ഒപ്പിടില്ലെന്ന്."),
 ("A","A","ജനുവരിക്ക് ഇനി ആറാഴ്ച. രജിസ്ട്രേഷൻ എന്ന് തുടങ്ങാനാ പ്ലാൻ?"),
 ("V","V","ഡിസംബർ പകുതിക്ക്. സമയം ഇഷ്ടം പോലെ ഉണ്ടല്ലോ."),
 ("A","wide","ഇല്ല! പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. ഇടയ്ക്ക് ക്രിസ്മസ് അവധിയും വരും."),
 ("V","V","അയ്യോ, ഡിസംബറിലെ കലണ്ടർ മുഴുവൻ ചുവന്ന അക്കങ്ങളാണല്ലോ!"),
 ("A","A","അതുകൊണ്ട് ഡോക്യുമെന്റ്സ് ഈ ആഴ്ച തന്നെ. ട്രീറ്റ് ജനുവരിയിൽ മതി.")],
 "കരാർ തീയതിയിൽ നിന്ന്\nപിന്നോട്ട് എണ്ണൂ", CTA_DOCS,
 cap_ml="ജർമ്മൻ കമ്പനിക്ക് മാന്വലുകൾ എഴുതുന്ന ഫ്രീലാൻസർക്ക് ജനുവരി 1 മുതൽ മൂന്ന് വർഷത്തെ കരാർ, കമ്പനിയുമായി മാത്രം. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; ഡിസംബറിലെ അവധികൾ കൂടി കണക്കാക്കി ഇപ്പോൾ തുടങ്ങണം.",
 cap_en="A Kochi freelance technical writer lands a three-year contract with a German manufacturer from 1 January, but only with a company. Private limited company registration in Kerala usually takes 7-15 working days, and the Christmas holidays fall in between, so the documents go in this week.",
 cap_mg="German company-kku manual ezhuthunna freelancer-nu January 1 muthal 3 varshathe contract, company-yumaayi maathram. Pvt Ltd company register cheyyan saadharana 7-15 working days; December-ile leave koodi kanakkaakki ippo thanne thudanganam.")

# home: Sneha + Arun. Arun builds Shopify stores for Gulf shops from a rented flat; a Muscat client wants a company invoice; the landlady lives downstairs.
duo("d2002", "freelancer", "C", "home", "വാടക ഫ്ലാറ്റിൽ ഇരുന്ന്\nഗൾഫ് ഷോപ്പുകൾക്ക്\nവെബ്സൈറ്റ്. ഓഫീസ്?", [
 ("V","wide","സ്നേഹേ, മസ്കറ്റിലെ ആ പെർഫ്യൂം കടക്കാർ ഇനി കമ്പനി ബില്ല് മാത്രമേ എടുക്കൂ എന്ന്."),
 ("A","A","നല്ലതല്ലേ? അരുണേട്ടന്റെ ഫ്രീലാൻസ് പരിപാടി ഇനി കമ്പനി ആകട്ടെ."),
 ("V","V","പക്ഷേ കമ്പനിക്ക് ഓഫീസ് വേണ്ടേ? നമ്മൾ ഈ വാടക ഫ്ലാറ്റിൽ, എന്റെ ലാപ്ടോപ്പ് ഡൈനിംഗ് ടേബിളിൽ."),
 ("A","wide","ഈ ഫ്ലാറ്റിന്റെ അഡ്രസ്സ് തന്നെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും മതി."),
 ("V","V","ഉടമ താഴത്തെ നിലയിലെ ടീച്ചറാണ്. വാടക ഒരു ദിവസം വൈകിയാൽ പോലും ചോദിക്കുന്ന ആൾ."),
 ("A","A","അതുകൊണ്ടാ ടീച്ചർക്ക് ചേട്ടനെ വിശ്വാസം. ഇന്ന് വൈകിട്ട് ഒരു പാക്കറ്റ് ലഡ്ഡുവുമായി താഴേക്ക് പോ."),
 ("V","wide","ലഡ്ഡുവും NOC പേപ്പറും. ഡൈനിംഗ് ടേബിൾ ഇനി ഹെഡ് ഓഫീസ്!")],
 "വാടക വീടും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="വാടക ഫ്ലാറ്റിൽ ഇരുന്ന് ഗൾഫ് കടകൾക്ക് വെബ്സൈറ്റ് ഉണ്ടാക്കുന്ന ഫ്രീലാൻസർക്ക് മസ്കറ്റിലെ ക്ലയന്റ് കമ്പനി ബില്ല് ചോദിക്കുന്നു. കമ്പനി രജിസ്ട്രേഷന് പ്രത്യേക ഓഫീസ് വേണ്ട; വീട്ടുടമയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ വാടക വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A Kerala freelancer building online stores for Gulf shops works from a rented flat, and a Muscat client now wants a company invoice. You do not need a separate office to register a company: with the landlord's NOC and a recent electricity bill, the rented home can be the registered office.",
 cap_mg="Vaadaka flat-il irunnu Gulf kadakalkku website undaakkunna freelancer-nodu Muscat client company bill chodikkunnu. Company register cheyyan separate office venda; veettudamayude NOC-um puthiya current bill-um undenkil vaadaka veedu registered office aakkaam.")

# rooftop: Arya + Shyam. Shyam makes 3D renders for online furniture sellers and wants his company named after a famous furniture brand.
duo("d2003", "freelancer", "B", "rooftop", "3D ഫർണിച്ചർ റെൻഡർ.\nകമ്പനിക്ക് പേര്:\nലോകത്തെ വലിയ ബ്രാൻഡിന്റേത്", [
 ("A","wide","ശ്യാം, ടെറസിൽ ഇരുന്ന് എന്താ ഇത്ര ആലോചന?"),
 ("V","V","ആര്യേ, കമ്പനിക്ക് പേര് ഇട്ടു! ആ വലിയ സ്വീഡിഷ് ഫർണിച്ചർ ബ്രാൻഡിന്റെ പേര്, പിന്നെ കേരള."),
 ("A","A","എന്തിന്? നീ ഉണ്ടാക്കുന്നത് ഓൺലൈൻ കടക്കാർക്കുള്ള ത്രീഡി ചിത്രങ്ങൾ അല്ലേ?"),
 ("V","V","അതുകൊണ്ടാ. ആ പേര് കേട്ടാൽ ക്ലയന്റ്സ് ക്യൂ നിൽക്കും."),
 ("A","wide","ക്യൂ നിൽക്കുന്നതിന് മുമ്പ് പേര് തന്നെ റിജക്ട് ആകും. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് കിട്ടില്ല."),
 ("A","A","നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉള്ളതും കിട്ടില്ല."),
 ("V","V","എങ്കിൽ എന്റെ ഒരു സ്വന്തം വാക്ക്. സോഫയും കസേരയും ചേർത്ത്, സോഫക്കസേര!"),
 ("A","wide","അത് ആർക്കും ഇല്ല. പക്ഷേ ബാക്കപ്പിന് രണ്ട് പേര് കൂടി എഴുതിക്കോ.")],
 "വലിയ ബ്രാൻഡിന്റെ പേര്\nനിങ്ങൾക്ക് കിട്ടില്ല", CTA_NAME,
 cap_ml="ഓൺലൈൻ ഫർണിച്ചർ കടകൾക്ക് 3D റെൻഡർ ചെയ്യുന്ന ഫ്രീലാൻസർക്ക് കമ്പനിക്ക് ലോകപ്രശസ്ത ഫർണിച്ചർ ബ്രാൻഡിന്റെ പേര് വേണം. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്നതോ നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യമുള്ളതോ ആയ കമ്പനി പേര് റിജക്ട് ആകും.",
 cap_en="A Kerala 3D artist who renders furniture for online stores wants to name his private limited company after a world-famous furniture brand. A company name that clashes with a trademark or looks like an existing company's name gets rejected, so pick your own word and keep two backups.",
 cap_mg="Online furniture kadakalkku 3D render cheyyunna freelancer-nu company-kku world famous furniture brand-nte peru venam. Trademark-umaayi clash aakunnatho ippozhulla company-yude perinodu saamyam ullatho aaya company name reject aakum.")

# cafe: Alvin + Roshan. Roshan ghostwrites LinkedIn posts for founders; a US client wants to put money into his business for a stake.
duo("d2004", "freelancer", "A", "cafe", "അമേരിക്കൻ ക്ലയന്റ്:\n\"നിന്റെ ബിസിനസിൽ\nഎനിക്കൊരു സ്റ്റേക്ക് വേണം\"", [
 ("V","wide","ആൽവിൻ, ഞാൻ പോസ്റ്റ് എഴുതിക്കൊടുക്കുന്ന ആ അമേരിക്കൻ ഫൗണ്ടർ ഇന്നലെ ഒരു ഓഫർ തന്നു."),
 ("A","A","ലിങ്ക്ഡ്ഇനിൽ ഒരു ലൈക്ക് കൂടി ആണോ?"),
 ("V","V","പോടാ. എന്റെ ബിസിനസിൽ പൈസ ഇടാം, പകരം പത്ത് ശതമാനം ഷെയർ. നാല് എഴുത്തുകാരെ കൂടി എടുക്കാം."),
 ("A","A","നിന്റെ ബിസിനസ് എന്ന് പറഞ്ഞാൽ നീയും നിന്റെ ലാപ്ടോപ്പും. അതിന് ഷെയർ ഇല്ലല്ലോ."),
 ("A","wide","ഷെയർ കൊടുത്ത് ഇൻവെസ്റ്റ്മെന്റ് വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. ഫ്രീലാൻസിനോ പാർട്ണർഷിപ്പിനോ പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി. രണ്ടാമത്തെ ഡയറക്ടർ ആര്?"),
 ("A","A","ഞാൻ തന്നെ. നിന്റെ എല്ലാ പോസ്റ്റും ആദ്യം വായിക്കുന്നത് ഞാനല്ലേ?"),
 ("V","wide","ശരി. പക്ഷേ ഡയറക്ടർക്കും കോഫി സ്വന്തം കാശിനാണ്!")],
 "ഷെയർ ചോദിച്ചാൽ\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="സ്റ്റാർട്ടപ്പ് ഫൗണ്ടർമാർക്ക് ലിങ്ക്ഡ്ഇൻ പോസ്റ്റുകൾ എഴുതുന്ന ഫ്രീലാൻസറുടെ ബിസിനസിൽ അമേരിക്കൻ ക്ലയന്റ് പൈസ ഇട്ട് 10% ഷെയർ ചോദിക്കുന്നു. ഷെയർ കൊടുത്ത് ഇൻവെസ്റ്റ്മെന്റ് വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി മാത്രം; ഫ്രീലാൻസിനോ പാർട്ണർഷിപ്പിനോ LLP-ക്കോ പറ്റില്ല.",
 cap_en="A Kerala freelance ghostwriter is offered money for a 10% stake by his American client so he can hire four more writers. Only a private limited company can take equity investment; a freelancer, a partnership or an LLP cannot, so the Pvt Ltd comes first.",
 cap_mg="Founders-nu LinkedIn post ezhuthunna freelancer-nte business-il American client paisa ittu 10% share chodikkunnu. Share koduthu investment vaangaan Pvt Ltd company maathram; freelance-ino partnership-ino LLP-kko pattilla.")

# beach: Divya + Nikhil. Nikhil's pet-photography company was registered in May; the monsoon brought no shoots; he thinks nothing is due.
duo("d2005", "freelancer", "B", "beach", "പെറ്റ് ഫോട്ടോഗ്രഫി കമ്പനി.\nമഴക്കാലത്ത് ഒരു\nഷൂട്ടും ഇല്ല", [
 ("A","wide","നിഖിൽ, ആ ലാബ്രഡോറിന്റെ ഫോട്ടോ സൂപ്പർ! പുതിയ ക്ലയന്റ് ആണോ?"),
 ("V","V","ദിവ്യേ, ഈ സീസണിലെ ആദ്യത്തെ ഷൂട്ട്. മേയിൽ കമ്പനി തുടങ്ങി, പിന്നെ മഴ. നായകളും വീട്ടിൽ, ഞാനും വീട്ടിൽ."),
 ("A","A","അപ്പോ കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ആലോചിച്ചോ?"),
 ("V","V","വരുമാനം ഇല്ലാത്ത വർഷത്തിന് എന്ത് ഫയലിംഗ്? പൂജ്യത്തിന് ആരും കണക്ക് ചോദിക്കില്ല."),
 ("A","wide","ചോദിക്കും. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("A","A","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ."),
 ("V","V","ദിവസം നൂറ്? അത് ഒരു നായയുടെ ബിസ്കറ്റ് ബജറ്റ് ആണല്ലോ!"),
 ("A","wide","അതുകൊണ്ട് കലണ്ടറിൽ ഡേറ്റ് മാർക്ക് ചെയ്യ്. ഷൂട്ട് പോലെ തന്നെ.")],
 "വരുമാനം പൂജ്യം.\nഫയലിംഗ് നിർബന്ധം", CTA_AFTER,
 cap_ml="മേയിൽ കമ്പനി തുടങ്ങിയ പെറ്റ് ഫോട്ടോഗ്രാഫർക്ക് മഴക്കാലം മുഴുവൻ ഒരു ഷൂട്ടും കിട്ടിയില്ല; വരുമാനം ഇല്ലാത്തതിനാൽ ഫയലിംഗ് വേണ്ടെന്ന് കരുതി. വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് നിർബന്ധം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A Kerala pet photographer registered his company in May, then the monsoon brought zero shoots, so he assumed there was nothing to file. Annual filing with the ROC is due even with zero revenue, and filing late costs 100 rupees per day for each form.",
 cap_mg="May-il company thudangiya pet photographer-nu mazhakkaalam muzhuvan oru shoot-um kittiyilla; varumaanam illaathathinaal filing venda ennu karuthi. Varumaanam poojyam aanenkilum company annual filing nirbandham; vaikiyaal oro form-inum divasam 100 roopa late penalty.")

# hostel: Aleena + Sanju. Sanju does medical coding for US hospitals from a hostel room; an outsourcing firm wants a company; he thinks he needs lakhs first.
duo("d2006", "freelancer", "A", "hostel", "മെഡിക്കൽ കോഡിംഗ്\nഹോസ്റ്റൽ മുറിയിൽ.\n\"ആദ്യം ലക്ഷങ്ങൾ വേണം\"", [
 ("A","wide","സഞ്ജൂ, രാത്രി മുഴുവൻ ലാപ്ടോപ്പിൽ എന്താ? ഇപ്പോഴും അമേരിക്കൻ ആശുപത്രികളുടെ കോഡിംഗ് ആണോ?"),
 ("V","V","അതേ അലീനേ. ഒരു ഔട്ട്സോഴ്സിംഗ് കമ്പനി എനിക്ക് മാസം ആയിരം ഫയൽ തരാമെന്ന്. പക്ഷേ കമ്പനിയുമായി മാത്രം."),
 ("A","A","എങ്കിൽ കമ്പനി തുടങ്ങ്. എന്താ പ്രശ്നം?"),
 ("V","V","കമ്പനി തുടങ്ങാൻ ബാങ്കിൽ ലക്ഷങ്ങൾ കാണിക്കണ്ടേ? എന്റെ അക്കൗണ്ടിൽ ഈ മാസത്തെ മെസ്സ് ബില്ല് മാത്രം."),
 ("A","wide","വേണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല."),
 ("V","V","ശരിക്കും? ഞാൻ രണ്ട് വർഷം കൂടി സേവ് ചെയ്യാമെന്ന് വിചാരിച്ചിരിക്കുവായിരുന്നു."),
 ("A","A","രണ്ട് വർഷം കാത്തിരുന്നാൽ ആ ആയിരം ഫയൽ വേറെ ആരെങ്കിലും എടുക്കും."),
 ("V","wide","എങ്കിൽ ഇന്ന് തന്നെ ഡോക്യുമെന്റ്സ്. മെസ്സ് ബില്ല് പിന്നെ അടയ്ക്കാം!")],
 "കമ്പനി തുടങ്ങാൻ\nലക്ഷങ്ങൾ വേണ്ട", CTA_START,
 cap_ml="ഹോസ്റ്റൽ മുറിയിൽ ഇരുന്ന് അമേരിക്കൻ ആശുപത്രികൾക്ക് മെഡിക്കൽ കോഡിംഗ് ചെയ്യുന്ന ഫ്രീലാൻസർക്ക് മാസം 1,000 ഫയലിന്റെ ഓർഡർ, കമ്പനിയുമായി മാത്രം. ബാങ്കിൽ ലക്ഷങ്ങൾ കാണിക്കണമെന്ന് കരുതി; പക്ഷേ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല.",
 cap_en="A freelance medical coder working from a Kerala hostel room is offered a thousand files a month, but only as a company, and believes he must show lakhs in the bank first. A private limited company has no minimum paid-up capital, so he does not need to wait two more years.",
 cap_mg="Hostel muriyil irunnu American hospital-ukalkku medical coding cheyyunna freelancer-nu maasam 1000 file-nte order, company-yumaayi maathram. Bank-il lakhs kaanikkanam ennu karuthi; pakshe Pvt Ltd company-kku minimum paid-up capital illa.")

chat("c1021", "freelancer", "C", "ഓൺലൈനിൽ സംഗീത ക്ലാസ്.\nഅടുത്ത മാസം സിഡ്നിയിലേക്ക്.\nകമ്പനി ഇവിടെ നിൽക്കുമോ?", ("അഞ്ജന", "ഗോകുൽ"), [
 (0,"ഗോകുലേ, വിസ വന്നു! അടുത്ത മാസം ഞാനും കിച്ചുവും സിഡ്നിയിലേക്ക്."),
 (1,"ഹാ! അപ്പോ നിന്റെ ഓൺലൈൻ കർണാടക സംഗീത ക്ലാസുകൾ? നൂറ്റിയിരുപത് കുട്ടികൾ ഇല്ലേ?"),
 (0,"അതാ ടെൻഷൻ. കമ്പനി ആക്കാൻ ഇരിക്കുവായിരുന്നു. ഞാൻ പോയാൽ ഇന്ത്യൻ കമ്പനി പറ്റില്ലല്ലോ."),
 (1,"പറ്റും. പക്ഷേ ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളായിരിക്കണം."),
 (0,"അച്ഛൻ തൃശ്ശൂരിൽ ഉണ്ട്. കുട്ടികളുടെ കണക്ക് ഒക്കെ ഇപ്പോഴും അച്ഛനാ നോക്കുന്നത്."),
 (1,"ബെസ്റ്റ്. അച്ഛനും നീയും ഡയറക്ടർ. ക്ലാസ് സിഡ്നിയിൽ നിന്ന്, കമ്പനി തൃശ്ശൂരിൽ."),
 (0,"സമയവ്യത്യാസം മാത്രം പ്രശ്നം. എന്റെ വൈകിട്ട് അഞ്ച് അവിടെ രാവിലെ."),
 (1,"അത് നന്നായി. രാവിലെ സാധകം, കുട്ടികൾക്കും നല്ലതാ!")],
 "വിദേശത്ത് പോയാലും\nകമ്പനി നാട്ടിൽ", CTA_START,
 cap_ml="നൂറ്റിയിരുപത് കുട്ടികളെ ഓൺലൈനായി കർണാടക സംഗീതം പഠിപ്പിക്കുന്ന ടീച്ചർ അടുത്ത മാസം സിഡ്നിയിലേക്ക്. ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയിൽ ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളായിരിക്കണം; തൃശ്ശൂരിലുള്ള അച്ഛൻ ആ ഡയറക്ടർ.",
 cap_en="An online Carnatic music teacher with 120 students is moving to Sydney and fears her Kerala company plan is over. A private limited company needs at least one director resident in India, so her father in Thrissur joins as director and the classes continue from Australia.",
 cap_mg="120 kuttikale online aayi Carnatic music padippikkunna teacher adutha maasam Sydney-ilekku. Indian Pvt Ltd company-yil oru director enkilum India-yil thaamasikkunna aal aayirikkanam; Thrissur-ulla achan aa director.")

# ---------------- cofounders ----------------
# pharmacy: Sini + Praveen. Two pharmacists building a medicine-delivery app; their chosen name is one letter away from an existing company.
duo("d2007", "cofounders", "B", "pharmacy", "മരുന്ന് ഡെലിവറി ആപ്പ്.\nപേര് ഒരു അക്ഷരം\nമാത്രം വ്യത്യാസം", [
 ("A","wide","പ്രവീൺ, ആപ്പിന്റെ ലോഗോ റെഡി! പച്ച കുരിശും ഒരു ചെറിയ സ്കൂട്ടറും."),
 ("V","V","സിനീ, പേര് ഞാൻ ഫിക്സ് ചെയ്തു. ആ വലിയ മെഡിക്കൽ കമ്പനിയുടെ പേരിൽ ഒരു അക്ഷരം മാറ്റി."),
 ("A","A","ഒരു അക്ഷരം മാത്രമോ? ആളുകൾ കൺഫ്യൂസ് ആകില്ലേ?"),
 ("V","V","അതാണ് ഐഡിയ. അവരാണെന്ന് വിചാരിച്ച് ഓർഡർ ചെയ്യും."),
 ("A","wide","ആളുകൾക്ക് മുമ്പ് രജിസ്ട്രാർ കൺഫ്യൂസ് ആകില്ല. നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകും."),
 ("V","V","റിജക്ട് ആയാൽ ലോഗോയും മാറ്റണ്ടേ?"),
 ("A","A","അതുകൊണ്ടാ പറഞ്ഞത്. ആദ്യം പേര്, പിന്നെ ലോഗോ. നമ്മുടെ സ്വന്തം വാക്ക് വേണം."),
 ("V","wide","ശരി. ഇന്ന് രാത്രി ഷിഫ്റ്റിൽ ഇരുന്ന് പത്ത് പുതിയ പേര് എഴുതാം.")],
 "ഒരക്ഷരം മാറ്റിയാൽ\nപുതിയ പേര് ആകില്ല", CTA_NAME,
 cap_ml="മരുന്ന് ഡെലിവറി ആപ്പ് തുടങ്ങുന്ന രണ്ട് ഫാർമസിസ്റ്റുകൾ ഒരു വലിയ മെഡിക്കൽ കമ്പനിയുടെ പേരിൽ ഒരു അക്ഷരം മാത്രം മാറ്റി കമ്പനി പേര് ആക്കാൻ നോക്കുന്നു. നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യമുള്ള പേര് രജിസ്ട്രേഷനിൽ റിജക്ട് ആകും.",
 cap_en="Two pharmacist cofounders in Kerala name their medicine-delivery startup by changing one letter in a big healthcare company's name. A company name similar to an existing company or LLP is rejected at registration, so fix the name before you print the logo.",
 cap_mg="Marunnu delivery app thudangunna 2 pharmacist-ukal oru valiya medical company-yude perile oru aksharam maathram maatti company name aakkaan nokkunnu. Ippozhulla company-yudeyo LLP-yudeyo perinodu saamyam ulla peru registration-il reject aakum.")

# bank: Sruthi + Manoj. Campus EV-scooter rental cofounders registered an LLP; an alumnus investor brings a cheque for 15%.
duo("d2008", "cofounders", "A", "bank", "ഇൻവെസ്റ്ററുടെ ചെക്ക്\nകൈയിൽ. പക്ഷേ നമ്മൾ\nLLP ആണ്", [
 ("A","wide","മനോജ്, ആ ചെക്ക് ഇങ്ങ് താ. ബാങ്ക് അടയ്ക്കുന്നതിന് മുമ്പ് ഡെപ്പോസിറ്റ് ചെയ്യാം."),
 ("V","V","ശ്രുതീ, ഒന്ന് നിൽക്ക്. കോളേജിലെ ആ സീനിയർ ഈ പൈസ തന്നത് പതിനഞ്ച് ശതമാനം ഷെയറിനാണ്."),
 ("A","A","അതെ, ക്യാമ്പസിൽ ഇരുപത് ഇലക്ട്രിക് സ്കൂട്ടർ കൂടി. അതിനെന്താ?"),
 ("V","V","നമ്മൾ രജിസ്റ്റർ ചെയ്തത് LLP ആണ്. LLP-യിൽ ഷെയർ എന്ന ഒന്നില്ലല്ലോ."),
 ("A","wide","ശരിയാ. ഷെയർ കൊടുത്ത് ഇക്വിറ്റി ഇൻവെസ്റ്റ്മെന്റ് എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ."),
 ("V","V","അപ്പോ ചെക്ക് തിരിച്ചു കൊടുക്കണോ?"),
 ("A","A","വേണ്ട. സീനിയറെ വിളിച്ച് പറ. സ്ട്രക്ചർ ശരിയാക്കിയിട്ട് ഡെപ്പോസിറ്റ്. അതുവരെ ചെക്ക് എന്റെ ബാഗിൽ."),
 ("V","wide","നിന്റെ ബാഗിൽ ആണെങ്കിൽ സേഫ്. ലോക്കറിനെക്കാൾ സേഫ്!")],
 "LLP-ക്ക് ഷെയർ ഇല്ല.\nഇൻവെസ്റ്റർക്ക് Pvt Ltd", CTA_START,
 cap_ml="ക്യാമ്പസിൽ ഇലക്ട്രിക് സ്കൂട്ടർ വാടകയ്ക്ക് കൊടുക്കുന്ന രണ്ട് കോഫൗണ്ടർമാർക്ക് സീനിയർ 15% ഷെയറിന് ചെക്ക് കൊടുത്തു, പക്ഷേ അവർ LLP ആണ്. ഷെയർ കൊടുത്ത് ഇക്വിറ്റി ഇൻവെസ്റ്റ്മെന്റ് എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ; LLP-ക്കും പാർട്ണർഷിപ്പിനും പറ്റില്ല.",
 cap_en="Two cofounders running an electric-scooter rental on a Kerala campus get an alumnus's cheque for 15%, then realise they registered an LLP. Only a private limited company can take equity investment for shares; an LLP or partnership cannot, so the structure comes before the deposit.",
 cap_mg="Campus-il electric scooter vaadakaykku kodukkunna 2 cofounders-nu senior 15% share-nu cheque koduthu, pakshe avar LLP aanu. Share koduthu equity investment edukkaan Pvt Ltd company-kku maathrame pattoo; LLP-kkum partnership-num pattilla.")

# canteen: Athira + Amal. Millet-snack cofounders; Amal thinks each founder must first put in five lakh before a company can exist.
duo("d2009", "cofounders", "C", "canteen", "മില്ലറ്റ് സ്നാക്സ്.\n\"കമ്പനിക്ക് ആദ്യം\nഅഞ്ച് ലക്ഷം വീതം\"", [
 ("A","wide","അമൽ, ഈ റാഗി ചിപ്സ് കാന്റീനിൽ അര മണിക്കൂർ കൊണ്ട് തീർന്നു!"),
 ("V","V","ആതിരേ, മൂന്ന് സൂപ്പർമാർക്കറ്റ് ചോദിച്ചു കഴിഞ്ഞു. പക്ഷേ കമ്പനി ആകാൻ കുറച്ച് കാത്തിരിക്കണം."),
 ("A","A","എന്തിന് കാത്തിരിക്കണം?"),
 ("V","V","കമ്പനി തുടങ്ങാൻ നമ്മൾ ഓരോരുത്തരും അഞ്ച് ലക്ഷം വീതം ഇടണം എന്ന് അളിയൻ പറഞ്ഞു."),
 ("A","wide","അളിയൻ ചായ ഉണ്ടാക്കിയാൽ മതി. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല."),
 ("V","V","ഇല്ലേ? ഞാൻ ബൈക്ക് വിൽക്കാൻ ഫോട്ടോ വരെ എടുത്തു!"),
 ("A","A","ബൈക്ക് വിൽക്കണ്ട. ഡെലിവറിക്ക് അത് വേണം. നമുക്ക് ആവശ്യമുള്ളത് മാത്രം ഇട്ട് തുടങ്ങാം."),
 ("V","wide","എങ്കിൽ ആദ്യത്തെ ഡയറക്ടർ മീറ്റിംഗ് ഇവിടെ. കാന്റീനിലെ ലാസ്റ്റ് ബെഞ്ചിൽ!")],
 "കമ്പനിക്ക്\nമിനിമം ക്യാപിറ്റൽ ഇല്ല", CTA_START,
 cap_ml="റാഗി ചിപ്സും മില്ലറ്റ് സ്നാക്സും ഉണ്ടാക്കുന്ന രണ്ട് കോഫൗണ്ടർമാർ കരുതി കമ്പനി തുടങ്ങാൻ ഓരോരുത്തരും അഞ്ച് ലക്ഷം വീതം ഇടണമെന്ന്. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല; ബിസിനസിന് ആവശ്യമുള്ളത് മാത്രം ഇട്ട് തുടങ്ങാം.",
 cap_en="Two Kerala cofounders whose millet chips sell out in the canteen are told each must put in five lakh before they can form a company. A private limited company has no minimum paid-up capital, so they can start the Pvt Ltd with only what the business needs.",
 cap_mg="Ragi chips-um millet snacks-um undaakkunna 2 cofounders karuthi company thudangaan ororuthharum 5 lakh veetham idanam ennu. Pvt Ltd company-kku minimum paid-up capital illa; business-nu aavashyam ullathu maathram ittu thudangaam.")

# busstop: Jibin + Akhil. Mobile puncture-repair van cofounders, company registered 150 days ago; share money never deposited, no commencement filing.
duo("d2010", "cofounders", "B", "busstop", "പഞ്ചർ റിപ്പയർ വാൻ.\nകമ്പനിക്ക് 150 ദിവസം.\nഒരു ഫോം ബാക്കി", [
 ("A","wide","അഖിലേ, ഇന്ന് രാവിലെ മൂന്ന് പഞ്ചർ. ഒന്ന് ഹൈവേയിൽ ഒരു ബസ്സിന്റേത്!"),
 ("V","V","ജിബിനേ, നമ്മുടെ വാനിന്റെ നമ്പർ ഇപ്പോ എല്ലാ ഡ്രൈവർമാരുടെയും ഫോണിൽ ഉണ്ട്."),
 ("A","A","കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ട് എത്ര ദിവസമായി?"),
 ("V","V","നൂറ്റിയമ്പത്. ഷെയർ പൈസ അക്കൗണ്ടിൽ ഇടാൻ ഇതുവരെ സമയം കിട്ടിയില്ല."),
 ("A","wide","എങ്കിൽ ഈ ആഴ്ച തന്നെ ഇടണം. ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന INC-20A നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("V","V","മിസ്സ് ആയാൽ?"),
 ("A","A","കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഓരോ ഡയറക്ടർക്കും ദിവസം ആയിരം രൂപ, ഒരു ലക്ഷം വരെ."),
 ("V","wide","ഇത് ഹൈവേയിലെ പഞ്ചറിനെക്കാൾ വലിയ പഞ്ചർ ആണല്ലോ. ഇന്ന് തന്നെ ബാങ്കിൽ പോകാം!")],
 "180 ദിവസം തീരും മുമ്പ്\nINC-20A", CTA_AFTER,
 cap_ml="ഹൈവേയിൽ പഞ്ചർ റിപ്പയർ വാൻ ഓടിക്കുന്ന രണ്ട് കോഫൗണ്ടർമാരുടെ കമ്പനിക്ക് 150 ദിവസം; ഷെയർ പൈസ ഇട്ടിട്ടില്ല, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. 180 ദിവസത്തിനുള്ളിൽ INC-20A വേണം; ഇല്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴയും ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപ (പരമാവധി 1 ലക്ഷം).",
 cap_en="Two cofounders running a roadside puncture-repair van in Kerala are 150 days past incorporation, with no share money deposited and no INC-20A filed. The commencement-of-business filing is due within 180 days; missing it means a 50,000 rupee penalty on the company and 1,000 rupees a day per officer, up to 1 lakh.",
 cap_mg="Highway-il puncture repair van odikkunna 2 cofounders-nte company-kku 150 divasam; share paisa ittittilla, INC-20A file cheythittilla. 180 divasathinullil INC-20A venam; illenkil company-kku 50,000 roopa pizhayum oro director-num divasam 1,000 roopa (max 1 lakh).")

# salon: Sonia + Vineeth. Home-salon booking app; Vineeth wants Sonia as director but all the shares in his own name.
duo("d2011", "cofounders", "C", "salon", "\"നീ ഡയറക്ടർ.\nപക്ഷേ ഷെയർ മുഴുവൻ\nഎന്റെ പേരിൽ\"", [
 ("V","wide","സോണിയേ, ഹോം സലൂൺ ആപ്പിന്റെ കമ്പനി പേപ്പർ ഞാൻ റെഡിയാക്കി. നീ ഡയറക്ടർ, ഷെയർ മുഴുവൻ എന്റെ പേരിൽ."),
 ("A","A","മുഴുവനോ? ബ്യൂട്ടീഷ്യന്മാരെ മുഴുവൻ കൊണ്ടുവന്നത് ഞാനല്ലേ?"),
 ("V","V","അത് ശരി. പക്ഷേ പിന്നെ ഒരു ഇൻവെസ്റ്റർ വരുമ്പോൾ ഒരാളോട് സംസാരിച്ചാൽ മതിയല്ലോ."),
 ("A","wide","അതൊന്നും നടക്കില്ല. പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം."),
 ("V","V","അപ്പോ ഷെയർ രണ്ട് പേർക്കും വേണം?"),
 ("A","A","വേണം. ഞാൻ എത്ര ശതമാനം എന്ന് ഇന്ന് തന്നെ എഴുതി ഒപ്പിടാം. പിന്നീട് വഴക്ക് വേണ്ട."),
 ("V","wide","ശരി. പക്ഷേ ആപ്പിൽ ആദ്യത്തെ ഹെയർകട്ട് ബുക്കിംഗ് എന്റേത്!")],
 "രണ്ട് ഡയറക്ടർ,\nരണ്ട് ഷെയർഹോൾഡർ", CTA_START,
 cap_ml="ഹോം സലൂൺ ബുക്കിംഗ് ആപ്പ് തുടങ്ങുന്ന കോഫൗണ്ടർ പങ്കാളിയെ ഡയറക്ടർ ആക്കി ഷെയർ മുഴുവൻ സ്വന്തം പേരിൽ വെക്കാൻ നോക്കുന്നു. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് കുറഞ്ഞത് 2 ഡയറക്ടറും 2 ഷെയർഹോൾഡറും വേണം; ഷെയർ എത്ര എന്ന് തുടക്കത്തിലേ എഴുതി വെക്കുക.",
 cap_en="A Kerala home-salon app founder wants his cofounder as director but every share in his own name. A private limited company needs at least two directors and two shareholders, so agree the split in writing on day one and avoid the fight later.",
 cap_mg="Home salon booking app thudangunna cofounder partner-ine director aakki share muzhuvan swantham peril vekkaan nokkunnu. Pvt Ltd company-kku kuranjathu 2 director-um 2 shareholder-um venam; share ethra ennu thudakkathil thanne ezhuthi vekkuka.")

# classroom: Nimmi + Adarsh. Robotics-kit cofounders for schools; company 22 days old; Adarsh thinks the auditor comes at year end.
duo("d2012", "cofounders", "A", "classroom", "സ്കൂളുകൾക്ക് റോബോട്ടിക്സ്\nകിറ്റ്. കമ്പനിക്ക്\n22 ദിവസം", [
 ("A","wide","ആദർശ്, ആ റോബോട്ട് കുട്ടികളുടെ ടേബിളിൽ നിന്ന് താഴെ വീഴാതെ നോക്കിക്കോ."),
 ("V","V","നിമ്മീ, പ്രിൻസിപ്പൽ ഓക്കെ പറഞ്ഞു! അടുത്ത വർഷം നാല് സ്കൂളിൽ നമ്മുടെ കിറ്റ്."),
 ("A","A","കൊള്ളാം. കമ്പനിക്ക് ഇപ്പോ ഇരുപത്തിരണ്ട് ദിവസം. ഓഡിറ്ററെ വെച്ചോ?"),
 ("V","V","ഓഡിറ്റർ മാർച്ചിൽ അല്ലേ? കണക്ക് നോക്കുമ്പോൾ മാത്രം വിളിച്ചാൽ മതി."),
 ("A","wide","അല്ല. ആദ്യത്തെ ഓഡിറ്ററെ കമ്പനി തുടങ്ങി മുപ്പത് ദിവസത്തിനുള്ളിൽ നിയമിക്കണം."),
 ("V","V","മുപ്പതോ? അപ്പോ ഇനി എട്ട് ദിവസം മാത്രം!"),
 ("A","A","അതേ. ഇന്ന് തന്നെ രണ്ട് പേരോട് സംസാരിക്ക്. റോബോട്ടിനെ ഞാൻ നോക്കാം."),
 ("V","wide","ഈ റോബോട്ടിന് ഒരു ടൈമർ വെക്കാം. മുപ്പത് ദിവസം, ബീപ് ബീപ്!")],
 "ആദ്യ ഓഡിറ്റർ\n30 ദിവസത്തിനുള്ളിൽ", CTA_AFTER,
 cap_ml="സ്കൂളുകൾക്ക് റോബോട്ടിക്സ് കിറ്റ് ഉണ്ടാക്കുന്ന കോഫൗണ്ടർമാരുടെ കമ്പനിക്ക് 22 ദിവസം; ഓഡിറ്റർ മാർച്ചിൽ മതിയെന്ന് കരുതി. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="Two cofounders selling robotics kits to Kerala schools are 22 days past incorporation and think the auditor is only needed in March. A new private limited company must appoint its first auditor within 30 days of incorporation, so they have eight days left.",
 cap_mg="Schools-nu robotics kit undaakkunna cofounders-nte company-kku 22 divasam; auditor March-il mathi ennu karuthi. Company registration kazhinju 30 divasathinullil first auditor-e appoint cheyyanam.")

chat("c1022", "cofounders", "A", "സാരി റെന്റൽ സൈറ്റ്.\nദുബായിലെ അളിയൻ:\n\"എനിക്കും ഷെയർ വേണം\"", ("ശ്വേത", "ദേവിക"), [
 (0,"ദേവൂ, ദുബായിൽ നിന്ന് ചേട്ടൻ വിളിച്ചിരുന്നു. നമ്മുടെ സാരി റെന്റൽ സൈറ്റിൽ പൈസ ഇടാമെന്ന്."),
 (1,"ചേച്ചീ സത്യമാണോ? ഈ കല്യാണ സീസണിൽ നൂറ് സാരി കൂടി വാങ്ങാം!"),
 (0,"പക്ഷേ ചേട്ടന് ലോൺ ആയിട്ടല്ല, ഷെയർ ആയിട്ട് വേണം. നമ്മൾ ഇപ്പോ രണ്ട് പേരുടെ പാർട്ണർഷിപ്പ് ആണല്ലോ."),
 (1,"പാർട്ണർഷിപ്പിൽ ഷെയർ കൊടുക്കാൻ പറ്റില്ല. അതിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം."),
 (0,"ചേട്ടൻ NRI ആണ്. NRI-ക്ക് ഇന്ത്യൻ കമ്പനിയിൽ ഷെയർ എടുക്കാൻ പറ്റുമോ?"),
 (1,"പറ്റും. NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം."),
 (0,"അപ്പോ ആദ്യം കമ്പനി. നമ്മൾ രണ്ട് പേരും ഇവിടെ ഡയറക്ടർ, ചേട്ടൻ ഷെയർഹോൾഡർ."),
 (1,"ഡീൽ. പക്ഷേ ചേട്ടന്റെ ഭാര്യക്ക് ഫ്രീ സാരി ഇല്ലെന്ന് ആദ്യമേ പറയണം!")],
 "ദുബായിൽ നിന്ന് ഷെയർ?\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="കല്യാണ സാരികൾ വാടകയ്ക്ക് കൊടുക്കുന്ന സഹോദരിമാരുടെ സൈറ്റിൽ ദുബായിലുള്ള അളിയൻ പൈസ ഇട്ട് ഷെയർ ചോദിക്കുന്നു. പാർട്ണർഷിപ്പിന് ഷെയർ കൊടുക്കാൻ പറ്റില്ല; പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം, NRI-ക്ക് അതിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം.",
 cap_en="Two sisters renting out wedding sarees from Kerala get an offer from their brother-in-law in Dubai, who wants shares, not a loan. A partnership cannot issue shares; they need a private limited company, and an NRI can be a shareholder and director of an Indian Pvt Ltd.",
 cap_mg="Kalyaana saree vaadakaykku kodukkunna sisters-nte site-il Dubai-ulla aliyan paisa ittu share chodikkunnu. Partnership-nu share kodukkan pattilla; Pvt Ltd company venam, NRI-kku athil shareholder-um director-um aakaam.")

# ---------------- salaried ----------------
# photocopy: Aswathy + Unni. Unni, a college lab assistant, 3D-prints spare parts for old sewing machines; a garment unit wants 200 a month; his wife wants no part in it.
duo("d2013", "salaried", "A", "photocopy", "കോളേജിൽ ലാബ് അസിസ്റ്റന്റ്.\nരാത്രി 3D പ്രിന്റ്.\nകൂടെ ആരുമില്ല", [
 ("A","wide","ഉണ്ണീ, ഇത് എന്ത് പാർട്ടാ? പ്ലാസ്റ്റിക്കിന്റെ ഒരു ചെറിയ ചക്രം?"),
 ("V","V","അശ്വതീ, പഴയ തയ്യൽ മെഷീന്റെ സ്പെയർ പാർട്ട്. കടയിൽ കിട്ടാനില്ല. ഞാൻ രാത്രി ത്രീഡി പ്രിന്റ് ചെയ്യും."),
 ("V","V","ഒരു ഗാർമെന്റ് യൂണിറ്റിന് മാസം ഇരുനൂറ് എണ്ണം വേണം. ബില്ല് കമ്പനിയുടെ പേരിൽ."),
 ("A","A","അപ്പോ കമ്പനി തുടങ്ങ്. ലാബിലെ ജോലി കഴിഞ്ഞ് വരുമ്പോൾ നീ തന്നെ മുതലാളി."),
 ("V","V","കമ്പനിക്ക് രണ്ട് പേര് വേണ്ടേ? ഭാര്യ പറഞ്ഞു, ഈ പ്ലാസ്റ്റിക് കളിയിൽ എന്നെ കൂട്ടണ്ടെന്ന്."),
 ("A","wide","വേണ്ട. ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി, OPC. ഒരാൾക്ക് മാത്രമായി ഒരു കമ്പനി."),
 ("V","V","അപ്പോ ഭാര്യയെ നിർബന്ധിക്കണ്ട. വീട്ടിൽ സമാധാനം, കമ്പനിയിൽ ഞാൻ."),
 ("A","A","പേപ്പറുകൾ എല്ലാം ഇവിടെ കൊണ്ടുവാ. ഫോട്ടോകോപ്പി എന്റെ വക!")],
 "ഒറ്റയ്ക്കാണോ?\nOPC ഉണ്ട്", CTA_START,
 cap_ml="കോളേജിൽ ലാബ് അസിസ്റ്റന്റ് ആയി ജോലി ചെയ്യുന്നയാൾ രാത്രി പഴയ തയ്യൽ മെഷീനുകളുടെ സ്പെയർ പാർട്ടുകൾ 3D പ്രിന്റ് ചെയ്യുന്നു; ഗാർമെന്റ് യൂണിറ്റിന് മാസം 200 എണ്ണം, ബില്ല് കമ്പനി പേരിൽ. കൂടെ ആരും ഇല്ലെങ്കിൽ ഒറ്റയ്ക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം.",
 cap_en="A salaried college lab assistant in Kerala 3D-prints spare parts for old sewing machines at night, and a garment unit wants 200 a month billed to a company. His wife wants no part in it, and that is fine: a solo founder can form a One Person Company (OPC).",
 cap_mg="College-il lab assistant aayi joli cheyyunna aal raathri pazhaya thayyal machine-nte spare parts 3D print cheyyunnu; garment unit-nu maasam 200 ennam, bill company peril. Koode aarum illenkil ottaykku One Person Company (OPC) thudangaam.")

# balcony: Ammu + Vivek. Vivek, airline ground staff, sets up balcony gardens on weekends; a builder wants all 80 balconies done; he thinks he must show capital first.
duo("d2014", "salaried", "B", "balcony", "80 ബാൽക്കണിയിൽ\nപൂന്തോട്ടം. ബിൽഡർ:\n\"കമ്പനി ആയിട്ട് വാ\"", [
 ("A","wide","വിവേക്, ഈ തക്കാളിച്ചെടി ഇത്ര വേഗം വളർന്നോ? നീ ഇതിന് എയർപോർട്ട് പരിശീലനം കൊടുത്തോ?"),
 ("V","V","അമ്മൂ, നമ്മുടെ ഫ്ലാറ്റിന്റെ ബിൽഡർ ഇത് കണ്ടു. പുതിയ ടവറിലെ എൺപത് ബാൽക്കണിയിലും ഇതുപോലെ വേണമെന്ന്."),
 ("A","A","വാവ്! വീക്കെൻഡ് ഹോബി ഇനി ബിസിനസ്."),
 ("V","V","പക്ഷേ കമ്പനി ആയിട്ട് വരാൻ പറഞ്ഞു. ബാങ്കിൽ കാണിക്കാൻ എനിക്ക് വലിയ തുക ഇല്ല. ഇപ്പോഴും ലോൺ അടയ്ക്കുവാ."),
 ("A","wide","അതിന് വലിയ തുക വേണ്ട. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല."),
 ("V","V","അപ്പോ ജോലി ഉള്ളപ്പോൾ തന്നെ കമ്പനി തുടങ്ങാം. ഷിഫ്റ്റ് കഴിഞ്ഞ് ചെടി, വീക്കെൻഡിൽ ബാൽക്കണി."),
 ("A","A","രണ്ടാമത്തെ ഡയറക്ടർ ഞാൻ. ചെടികൾക്ക് വെള്ളം ഒഴിക്കുന്നത് ഞാനല്ലേ?"),
 ("V","wide","ഡീൽ. എൺപത് ബാൽക്കണി, രണ്ട് ഡയറക്ടർ, ഒരു തക്കാളിച്ചെടി!")],
 "വലിയ ഓർഡറിന്\nവലിയ ക്യാപിറ്റൽ വേണ്ട", CTA_START,
 cap_ml="എയർപോർട്ടിൽ ജോലി ചെയ്യുന്നയാൾ വീക്കെൻഡിൽ ചെയ്യുന്ന ബാൽക്കണി ഗാർഡൻ ബിൽഡർ കണ്ടു; പുതിയ ടവറിലെ 80 ബാൽക്കണിക്കും വേണം, കമ്പനിയുമായി മാത്രം. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല; ജോലി വിടാതെ തന്നെ തുടങ്ങാം.",
 cap_en="A salaried airport employee in Kerala sets up balcony gardens on weekends, and his builder wants all 80 balconies of a new tower done by a company. He thought he needed a big bank balance, but a private limited company has no minimum paid-up capital.",
 cap_mg="Airport-il joli cheyyunna aal weekend-il cheyyunna balcony garden builder kandu; puthiya tower-ile 80 balcony-kkum venam, company-yumaayi maathram. Pvt Ltd company-kku minimum paid-up capital illa; joli vidaathe thanne thudangaam.")

# foodcourt: Maria + Dennis. Maria, an HR executive at a mall, makes joining kits for IT companies; her husband in Oman would be the other director; Dennis worries.
duo("d2015", "salaried", "C", "foodcourt", "ഐടി കമ്പനികൾക്ക്\nജോയിനിംഗ് കിറ്റ്.\nഭർത്താവ് ഒമാനിൽ", [
 ("V","wide","മരിയേ, ഈ ബോക്സിൽ എന്താ? നോട്ട്ബുക്ക്, ബോട്ടിൽ, ഒരു ചെറിയ ചെടി?"),
 ("A","A","പുതിയതായി ജോയിൻ ചെയ്യുന്നവർക്കുള്ള വെൽക്കം കിറ്റ്. മൂന്ന് ഐടി കമ്പനികൾ മാസം തോറും ചോദിക്കുന്നു."),
 ("V","V","എച്ച്ആർ ജോലിക്കിടയിൽ ഇതും? അപ്പോ കമ്പനി ആക്കണ്ടേ?"),
 ("A","A","ആലോചിക്കുന്നു. രണ്ടാമത്തെ ഡയറക്ടർ ടോം ആണ്. പക്ഷേ ടോം ഒമാനിൽ അല്ലേ?"),
 ("V","V","അത് പ്രശ്നം ആകുമോ? രണ്ട് ഡയറക്ടറും നാട്ടിൽ വേണ്ടേ?"),
 ("A","wide","വേണ്ട. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളായാൽ മതി. അത് ഞാൻ."),
 ("A","A","NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. ടോമിന് അവിടെ ഇരുന്ന് തന്നെ."),
 ("V","wide","എങ്കിൽ ആദ്യത്തെ കിറ്റ് എനിക്ക്. ഞാനും ഇന്ന് ഈ ഫുഡ്കോർട്ടിൽ പുതിയ ജോലിക്കാരനാ!")],
 "ഭർത്താവ് ഗൾഫിൽ?\nഡയറക്ടർ ആകാം", CTA_START,
 cap_ml="മാളിൽ എച്ച്ആർ ആയി ജോലി ചെയ്യുന്ന യുവതി ഐടി കമ്പനികൾക്ക് ജോയിനിംഗ് കിറ്റ് ഉണ്ടാക്കുന്നു; രണ്ടാമത്തെ ഡയറക്ടർ ഒമാനിലുള്ള ഭർത്താവ്. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി; NRI-ക്ക് ഇന്ത്യൻ Pvt Ltd കമ്പനിയിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം.",
 cap_en="A salaried HR executive in Kochi builds welcome kits for new joiners at three IT companies, and her husband in Oman would be the second director. Only one director needs to be resident in India, and an NRI can be a director and shareholder of an Indian private limited company.",
 cap_mg="Mall-il HR aayi joli cheyyunna yuvathi IT company-kalkku joining kit undaakkunnu; randaamathe director Oman-ilulla bharthaavu. Oru director enkilum India-yil thaamasikkunna aal aayaal mathi; NRI-kku Indian Pvt Ltd-il director-um shareholder-um aakaam.")

# mobileshop: Hanna + Fahad. Fahad, salaried at a phone shop, refurbishes laptops for students on Sundays; he wants a name that sounds like a phone giant's.
duo("d2016", "salaried", "B", "mobileshop", "ഞായറാഴ്ച ലാപ്ടോപ്പ്\nറിഫർബിഷ്. പേരിൽ ഒരു\nഫോൺ ഭീമന്റെ ഛായ", [
 ("A","wide","ഫഹദേ, ഷോപ്പിലെ ജോലി കഴിഞ്ഞിട്ടും ഈ പഴയ ലാപ്ടോപ്പുകൾ എന്തിനാ?"),
 ("V","V","ഹന്നേ, ഞായറാഴ്ച ഞാൻ ഇത് നന്നാക്കി കോളേജ് കുട്ടികൾക്ക് കൊടുക്കും. രണ്ട് കോളേജ് ബൾക്ക് ആയി ചോദിച്ചു."),
 ("A","A","കമ്പനി ആക്കാൻ പ്ലാൻ ഉണ്ടോ?"),
 ("V","V","ഉണ്ട്. പേരും റെഡി. ആ വലിയ ഫോൺ കമ്പനിയുടെ പേരിന്റെ കൂടെ റിന്യൂ എന്ന് ചേർത്ത്."),
 ("A","wide","അത് കിട്ടില്ല. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് റിജക്ട് ആകും."),
 ("A","A","അത് പോലെ, നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉള്ളതും."),
 ("V","V","അപ്പോ എന്റെ സ്വന്തം പേര് വേണം. ഞായറാഴ്ച ടെക് എങ്ങനെ?"),
 ("A","wide","അതാ നിന്റെ കഥ. ബാക്കപ്പിന് രണ്ട് പേര് കൂടി എഴുതിക്കോ.")],
 "കടം വാങ്ങിയ പേര്\nറിജക്ട് ആകും", CTA_NAME,
 cap_ml="മൊബൈൽ ഷോപ്പിൽ ശമ്പളത്തിന് ജോലി ചെയ്യുന്ന യുവാവ് ഞായറാഴ്ചകളിൽ പഴയ ലാപ്ടോപ്പുകൾ നന്നാക്കി കോളേജ് കുട്ടികൾക്ക് കൊടുക്കുന്നു; കമ്പനിക്ക് വലിയ ഫോൺ ബ്രാൻഡിന്റെ പേര് ചേർക്കാൻ നോക്കുന്നു. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്നതോ നിലവിലുള്ള കമ്പനിയോട് സാമ്യമുള്ളതോ ആയ പേര് റിജക്ട് ആകും.",
 cap_en="A salaried phone-shop employee in Kerala refurbishes laptops for college students on Sundays and wants a company name built on a big phone brand. Names that clash with a trademark or resemble an existing company are rejected at registration, so choose your own story for the name.",
 cap_mg="Mobile shop-il shambalathinu joli cheyyunna yuvaavu Sunday-kalil pazhaya laptop nannaakki college kuttikalkku kodukkunnu; company-kku valiya phone brand-nte peru cherkkaan nokkunnu. Trademark-umaayi clash aakunnatho ippozhulla company-yodu saamyam ullatho aaya peru reject aakum.")

chat("c1023", "salaried", "A", "നൈറ്റ് ഷിഫ്റ്റ് നഴ്സ്.\nസൈഡ് കമ്പനിക്ക്\nഇന്ന് 29-ാം ദിവസം", ("ഷൈനി", "ദീപ്തി"), [
 (0,"ദീപ്തീ, ഷിഫ്റ്റ് കഴിഞ്ഞോ? എന്റെ ലാക്ടേഷൻ കൺസൾട്ടേഷൻ കമ്പനിക്ക് ആദ്യത്തെ ക്ലയന്റ്!"),
 (1,"സൂപ്പർ ഷൈനി! കമ്പനി സർട്ടിഫിക്കറ്റ് വന്നിട്ട് എത്ര ദിവസമായി?"),
 (0,"ഇന്ന് ഇരുപത്തിയൊമ്പത്. നൈറ്റ് ഷിഫ്റ്റ് കാരണം ബാക്കി ഒന്നും നോക്കിയില്ല."),
 (1,"ഷൈനീ! ആദ്യത്തെ ഓഡിറ്ററെ മുപ്പത് ദിവസത്തിനുള്ളിൽ വെക്കണം. അതായത് നാളെ!"),
 (0,"നാളെയോ?! ഞാൻ വിചാരിച്ചു ഓഡിറ്റർ ഒക്കെ വർഷം കഴിയുമ്പോൾ മതിയെന്ന്."),
 (1,"അല്ല. എന്റെ അനിയന്റെ കമ്പനിക്ക് ഓഡിറ്റ് ചെയ്യുന്ന ആളുടെ നമ്പർ അയക്കാം. രാവിലെ തന്നെ വിളിക്ക്."),
 (0,"ഉറങ്ങുന്നതിന് മുമ്പ് വിളിക്കാം. അലാറം വെച്ചു."),
 (1,"നല്ല കുട്ടി. ഡ്യൂട്ടി കഴിഞ്ഞ് ഒരു ഡ്യൂട്ടി കൂടി!")],
 "ആദ്യ ഓഡിറ്റർ:\n30 ദിവസം മാത്രം", CTA_AFTER,
 cap_ml="ആശുപത്രിയിൽ നൈറ്റ് ഷിഫ്റ്റ് ചെയ്യുന്ന നഴ്സിന്റെ ലാക്ടേഷൻ കൺസൾട്ടേഷൻ കമ്പനിക്ക് ഇന്ന് 29-ാം ദിവസം; ഓഡിറ്ററെ ഇതുവരെ വെച്ചിട്ടില്ല. പുതിയ കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A salaried night-shift nurse in Kerala started a lactation-consultation company on the side, and today is day 29 with no auditor. A new company must appoint its first auditor within 30 days of incorporation, so the call happens before she sleeps.",
 cap_mg="Hospital-il night shift cheyyunna nurse-nte lactation consultation company-kku innu 29-aam divasam; auditor-e ithuvare vechittilla. Puthiya company registration kazhinju 30 divasathinullil first auditor-e appoint cheyyanam.")

lst("l1021", "salaried", "C", "ജോലി വിടാതെ കമ്പനി.\nആദ്യം മാറ്റേണ്ട\n3 തെറ്റിദ്ധാരണ", [
 ("\"ഓഫീസ് മുറി എടുക്കണം\"", "വേണ്ട. വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും."),
 ("\"ബാങ്കിൽ ലക്ഷങ്ങൾ വേണം\"", "പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല."),
 ("\"ഒരു പാർട്ണർ നിർബന്ധം\"", "ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം.")],
 "ശമ്പളം വരുമ്പോഴും\nസ്വന്തം കമ്പനി", CTA_START,
 cap_ml="ശമ്പള ജോലി വിടാതെ സൈഡ് ബിസിനസ് കമ്പനി ആക്കാൻ ആലോചിക്കുന്നവർ ആദ്യം മാറ്റേണ്ട മൂന്ന് തെറ്റിദ്ധാരണകൾ. വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം, പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം ക്യാപിറ്റൽ ഇല്ല, ഒറ്റയ്ക്കാണെങ്കിൽ OPC.",
 cap_en="Three myths that stop salaried people in Kerala from turning a side business into a company. Your home can be the registered office with an NOC and utility bill, a private limited company has no minimum capital, and a solo founder can form a One Person Company.",
 cap_mg="Shambala joli vidaathe side business company aakkaan aalochikkunnavar aadyam maattenda 3 thettidhaaranakal. Veedu registered office aakkaam, Pvt Ltd-nu minimum capital illa, ottaykku aanenkil OPC.")
