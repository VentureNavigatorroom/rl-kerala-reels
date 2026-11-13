# Script bank, batch 13. New situations: a hardware store chosen as sole supplier for a 200-villa township, a rubber-sheet dealer
# racing a tyre maker's vendor window, a car-wash man whose idle company never filed while a cab fleet checks his record, a prawn
# processor offered money for 30% by a Japanese buyer's agent, a home snack-maker for 12 school canteens whose husband wants no part,
# a printing press with a three-year exam-booklet contract and a son in Canada; a Doha electrician waiting two years to "go home
# first", Riyadh roommates whose Kerala building is not ready so there is no revenue, an Abu Dhabi HR manager setting up an
# interview-coaching centre with her mother, an attar brand named like a famous perfume house, a Kuwait returnee who thinks a
# used-car showroom company needs 25 lakh shown, an Irish nurse funding her sister's Hindi-tuition centre, a Saudi engineer's wife
# counting the auditor's 30 days; a solo backwater fishing guide, a bridal-jewellery rental OPC at day 165, a beekeeper whose name
# copies a big honey brand, a spice parcel seller to Europe from her husband's house, a crossword app with no revenue.
# Same fact list and no-price rule as batch01. Segments proprietor 7, nri 7, solo 6; 15 duo3d in 15 different locations, default names.
# Proprietor scripts again open on money waiting on the table (the d401 pattern), with new situations; share kept at 7/40.
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
# shop: Binu + Suresh. A builder wants Suresh's hardware store as sole supplier for a 200-villa township, contract with a company only; he wants "Kerala Hardware".
duo("d1501", "proprietor", "A", "shop", "200 വില്ലകളുടെ ടൗൺഷിപ്പ്.\nഎല്ലാ സാധനവും\nനമ്മുടെ കടയിൽ നിന്ന്!", [
 ("A","wide","സുരേഷേ, ആ ബിൽഡറുടെ കാർ കടയുടെ മുന്നിൽ അര മണിക്കൂർ നിന്നല്ലോ. എന്ത് പറഞ്ഞു?"),
 ("V","V","ബിനുച്ചേട്ടാ, ഇരുന്നൂറ് വില്ലയുടെ ടൗൺഷിപ്പ്. പൈപ്പ് മുതൽ പെയിന്റ് വരെ എല്ലാം നമ്മുടെ കടയിൽ നിന്ന്."),
 ("A","A","ഇരുന്നൂറ് വില്ല! അപ്പോ ഇനി നമ്മുടെ ആണിക്ക് പോലും ഡിമാൻഡ്."),
 ("V","V","പക്ഷേ കരാർ കമ്പനിയുമായി മാത്രം. പേര് ഞാൻ ഉറപ്പിച്ചു. കേരള ഹാർഡ്‌വെയർ."),
 ("A","wide","കേരള ഹാർഡ്‌വെയർ എന്ന പേരിൽ ഇപ്പോ തന്നെ എത്ര കമ്പനി ഉണ്ടാകും? നിലവിലുള്ള പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം."),
 ("A","A","റിജക്ട് ആയാൽ വീണ്ടും അപേക്ഷ. ബിൽഡർ അത്രയും കാത്തിരിക്കുമോ?"),
 ("V","V","അയ്യോ. എല്ലാ കടയുടെ ബോർഡിലും ഇതേ പേരാണല്ലോ, ഞാൻ ഓർത്തില്ല."),
 ("A","A","നിന്റെ അച്ഛന്റെ പേരോ, നമ്മുടെ സ്ഥലത്തിന്റെ പേരോ ചേർത്ത് വേറിട്ട മൂന്ന് പേര് എഴുത്."),
 ("V","wide","ശരി. ആണി പോലെ ഉറച്ച ഒരു പേര്!")],
 "എല്ലാവരുടെയും പേര്\nനിങ്ങളുടേത് ആകില്ല", CTA_NAME,
 cap_ml="200 വില്ലകളുടെ ടൗൺഷിപ്പിന് ഹാർഡ്‌വെയർ കടയെ സോൾ സപ്ലയർ ആക്കാൻ ബിൽഡർ റെഡി, പക്ഷേ കരാർ കമ്പനിയുമായി മാത്രം. 'കേരള ഹാർഡ്‌വെയർ' പോലുള്ള സാധാരണ പേരുകൾ നിലവിലുള്ള കമ്പനികളോട് സാമ്യം വന്ന് റിജക്ട് ആകാം. വേറിട്ട കമ്പനി പേര് കരുതൂ.",
 cap_en="A builder wants a Kerala hardware store as sole supplier for a 200-villa township, but will sign only with a company. Common names like 'Kerala Hardware' are often similar to existing companies and get rejected, so pick a distinctive company name with backups.",
 cap_mg="200 villa township-nu hardware kadaye sole supplier aakkan builder ready, pakshe contract company-yumaayi maathram. 'Kerala Hardware' pole common names existing company-yodu saamyam vannu reject aakaam. Vere oru company name urappikku.")

# rubber: Joy + Thomas. A tyre maker will buy Thomas's rubber sheets directly, but its vendor window closes in 20 days and only takes companies.
duo("d1502", "proprietor", "B", "rubber", "ടയർ കമ്പനി പറഞ്ഞു:\n\"നേരിട്ട് വാങ്ങാം.\nവെണ്ടർ ലിസ്റ്റ് 20 ദിവസം\"", [
 ("A","wide","തോമാച്ചാ, ഷീറ്റ് ഉണക്കുന്നതിനിടയിൽ ഫോണിൽ ആരാ?"),
 ("V","V","ജോയിച്ചായാ, ആ ടയർ കമ്പനിയുടെ പർച്ചേസ് മാനേജർ. ഇടനിലക്കാരൻ ഇല്ലാതെ നമ്മുടെ ഷീറ്റ് നേരിട്ട് എടുക്കാമെന്ന്."),
 ("A","A","ദൈവം കാത്തു! ഇനി ഏജന്റിന് കമ്മീഷൻ ഇല്ല."),
 ("V","V","പക്ഷേ വെണ്ടർ ലിസ്റ്റ് ഇരുപത് ദിവസം കൂടിയേ തുറന്നിരിക്കൂ. കമ്പനികളെ മാത്രം എടുക്കും."),
 ("A","wide","ഇരുപത് ദിവസം. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. നാളെ അല്ല, ഇന്ന് തുടങ്ങണം."),
 ("A","A","നീയും ഞാനും ഡയറക്ടർ. രണ്ടുപേരുടെയും ഡോക്യുമെന്റ്സ്, ഓഫീസ് അഡ്രസ്സിന്റെ പേപ്പർ."),
 ("V","V","റബ്ബർ വെട്ടാൻ രാവിലെ നാല് മണിക്ക് എഴുന്നേൽക്കുന്നവർക്ക് ഇത് എളുപ്പം."),
 ("A","A","പക്ഷേ പേര് റിജക്ട് ആയാൽ ദിവസം പോകും. രണ്ടുമൂന്ന് പേരും കരുതിക്കോ."),
 ("V","wide","ശരി. ഷീറ്റ് ഉണങ്ങും മുമ്പ് ഡോക്യുമെന്റ്സ് റെഡി!")],
 "വെണ്ടർ ലിസ്റ്റ്\nകാത്തിരിക്കില്ല", CTA_DOCS,
 cap_ml="റബ്ബർ ഷീറ്റ് ഡീലർക്ക് ടയർ കമ്പനിയിൽ നേരിട്ട് സപ്ലൈ ചെയ്യാൻ അവസരം, പക്ഷേ വെണ്ടർ ലിസ്റ്റ് 20 ദിവസം മാത്രം, കമ്പനികൾക്ക് മാത്രം. Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം. ഡോക്യുമെന്റ്സും ബാക്കപ്പ് പേരുകളും ഇന്ന് തന്നെ.",
 cap_en="A rubber-sheet dealer in Kerala can sell directly to a tyre maker, but its vendor list closes in 20 days and takes only companies. Private limited company registration usually takes 7 to 15 working days, so get documents and backup names ready today.",
 cap_mg="Rubber sheet dealer-nu tyre company-kku nerittu supply cheyyan chance, pakshe vendor list 20 days maathram, company-kalkku maathram. Pvt Ltd register cheyyan saadharana 7-15 working days. Documents-um backup names-um innu thanne.")

# petrolpump: Santhosh + Shibu. Shibu's car-wash company was formed last year for a contract that fell through, never filed; now a cab fleet checks his record.
duo("d1503", "proprietor", "C", "petrolpump", "300 ടാക്സിയുടെ കാർ വാഷ്.\nപക്ഷേ കഴിഞ്ഞ വർഷത്തെ\nഫയലിംഗ്?", [
 ("A","wide","ഷിബൂ, ആ ടാക്സി കമ്പനിയുടെ ആളുകൾ എന്താ കാർ വാഷിന്റെ ഫോട്ടോ എടുക്കുന്നത്?"),
 ("V","V","സന്തോഷേട്ടാ, മുന്നൂറ് ടാക്സി എല്ലാ ആഴ്ചയും ഇവിടെ കഴുകാനുള്ള കരാർ. പക്ഷേ അവർ കമ്പനിയുടെ ഫയലിംഗ് ഒക്കെ ചെക്ക് ചെയ്യുമെന്ന്."),
 ("A","A","നിനക്ക് കഴിഞ്ഞ കൊല്ലം തന്നെ കമ്പനി ഉണ്ടല്ലോ."),
 ("V","V","ഉണ്ട്. അന്നത്തെ കരാർ നടന്നില്ല. ഒരു രൂപ പോലും വരുമാനം വന്നില്ല. അതുകൊണ്ട് ഫയലിംഗ് ഒന്നും ചെയ്തില്ല."),
 ("A","wide","അതാ കുഴപ്പം. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("A","A","വൈകുന്ന ഓരോ ദിവസവും ഓരോ ഫോമിനും നൂറ് രൂപ ലേറ്റ് ഫീ. അത് കൂടിക്കൊണ്ടിരിക്കും."),
 ("V","V","അപ്പോ കാർ കഴുകും മുമ്പ് കമ്പനിയെ കഴുകണം!"),
 ("A","A","അതെ. ഇന്ന് തന്നെ ഓഡിറ്ററെ കണ്ട് പഴയ ഫയലിംഗ് തീർക്ക്. എന്നിട്ട് കരാർ."),
 ("V","wide","ശരി. ഇനി എല്ലാ വർഷവും കാർ വാഷിനൊപ്പം കമ്പനി വാഷും!")],
 "വരുമാനം ഇല്ലാത്ത വർഷവും\nഫയലിംഗ് വേണം", CTA_AFTER,
 cap_ml="കഴിഞ്ഞ വർഷം തുടങ്ങിയ കമ്പനിക്ക് വരുമാനമില്ലാത്തതുകൊണ്ട് ഫയലിംഗ് ചെയ്തില്ല, ഇപ്പോൾ 300 ടാക്സികളുടെ കാർ വാഷ് കരാറിന് മുമ്പ് ടാക്സി കമ്പനി റെക്കോർഡ് ചെക്ക് ചെയ്യുന്നു. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം, വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.",
 cap_en="A car-wash owner in Kerala formed a company last year for a deal that fell through and never filed because there was no revenue. Now a cab fleet wants to check his record. Annual filings are due even with zero revenue, and late filing costs Rs 100 per day per form.",
 cap_mg="Kazhinja varsham thudangiya company-kku revenue illaathathukondu filing cheythilla, ippol 300 taxi car wash contract-nu munpu record check. Zero revenue aanenkilum annual filing (ROC) cheyyanam, vaikiyal oro form-inum divasam 100 roopa.")

# fishmarket: Suma + Antony. A Japanese buyer's agent offers money for 30% of Antony's prawn-processing unit, a proprietorship.
duo("d1504", "proprietor", "A", "fishmarket", "ചെമ്മീൻ യൂണിറ്റ്.\nജപ്പാൻ ബയറുടെ ഏജന്റ്:\n\"30% തരൂ, പൈസ ഇടാം\"", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, ആ സൂട്ടിട്ട ആൾ മീൻ മണം സഹിച്ച് ഇത്ര നേരം എന്താ സംസാരിച്ചത്?"),
 ("V","V","സുമേ, ജപ്പാനിലെ ബയറുടെ ഏജന്റ്. നമ്മുടെ ചെമ്മീൻ യൂണിറ്റിൽ മുപ്പത് ശതമാനം വേണം. പകരം പുതിയ ഫ്രീസർ ലൈനിനുള്ള നിക്ഷേപം."),
 ("A","A","മുപ്പത് ശതമാനം എന്തിൽ? യൂണിറ്റ് ചേട്ടന്റെ ഒറ്റ പേരിലുള്ള പ്രൊപ്രൈറ്റർഷിപ്പ് അല്ലേ?"),
 ("V","V","അതെ. ഒരു പേപ്പറിൽ മുപ്പത് ശതമാനം എന്ന് എഴുതി ഒപ്പിട്ടാൽ പോരേ?"),
 ("A","wide","പോരാ. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിന് ഷെയർ ഇല്ല."),
 ("A","A","പാർട്ണർഷിപ്പിനും LLP-ക്കും പറ്റില്ല. ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്, കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ."),
 ("V","V","അപ്പോ ഡയറക്ടർ ഞാനും… മകൾ ഫുഡ് ടെക്നോളജി പഠിച്ചതല്ലേ, അവളും."),
 ("A","A","അതാ നല്ലത്. ജപ്പാൻകാർ ക്വാളിറ്റി ചോദിക്കുമ്പോൾ ഉത്തരം അവൾ പറയും."),
 ("V","wide","ശരി. ചെമ്മീൻ ഫ്രീസ് ചെയ്യാം, ഡീൽ ഫ്രീസ് ആകരുത്!")],
 "ബയർ ഷെയർ ചോദിച്ചാൽ\nആദ്യം Pvt Ltd", CTA_START,
 cap_ml="ചെമ്മീൻ പ്രോസസിംഗ് യൂണിറ്റിൽ 30% ഷെയറിന് പകരം നിക്ഷേപം നൽകാൻ ജപ്പാൻ ബയറുടെ ഏജന്റ്, പക്ഷേ ബിസിനസ് പ്രൊപ്രൈറ്റർഷിപ്പ്. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും പറ്റില്ല.",
 cap_en="A Japanese buyer's agent offers to fund a new freezer line at a Kerala prawn-processing unit in return for 30%, but the unit is a proprietorship. Only a private limited company can take equity investment, with at least two directors.",
 cap_mg="Chemmeen processing unit-il 30% share-nu pakaram investment tharaan Japan buyer-inte agent, pakshe business proprietorship. Share koduthu investment edukkan Pvt Ltd company venam. Proprietorship-num LLP-kkum pattilla.")

# kitchen: Bindu + Rajesh. Twelve school canteens want Bindu's home snacks, billed by a company; Rajesh wants no part, so she will be alone.
duo("d1505", "proprietor", "B", "kitchen", "12 സ്കൂൾ ക്യാന്റീനിൽ\nനമ്മുടെ ഉന്നക്കായ.\n\"കമ്പനിയിൽ ഞാനില്ല\"", [
 ("A","wide","രാജേഷേട്ടാ, ഉന്നക്കായ എണ്ണയിൽ ഇട്ടോ? ഇല്ലെങ്കിൽ ഇങ്ങോട്ട് വാ, ഒരു വാർത്ത."),
 ("V","V","എന്താ ബിന്ദൂ? എണ്ണ ചൂടായി."),
 ("A","A","പന്ത്രണ്ട് സ്കൂൾ ക്യാന്റീനിൽ നമ്മുടെ പലഹാരം വേണമെന്ന് മാനേജ്മെന്റ്. പക്ഷേ ബിൽ കമ്പനിയുടേത് ആകണം."),
 ("V","V","കമ്പനി നീ തുടങ്ങിക്കോ. എന്നെ ഡയറക്ടർ ഒന്നും ആക്കണ്ട. എനിക്ക് ബാങ്കിലെ ജോലി തന്നെ ധാരാളം."),
 ("A","A","അപ്പോ രണ്ടാമത്തെ ആൾ ഇല്ലാതെ എങ്ങനെ? പ്രൈവറ്റ് ലിമിറ്റഡിന് രണ്ടുപേർ വേണ്ടേ?"),
 ("V","wide","ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി ഉണ്ട്. OPC. നീ ഒറ്റയ്ക്ക് ഉടമ, ഒറ്റയ്ക്ക് ഡയറക്ടർ."),
 ("A","A","അപ്പോ പലഹാരവും ഞാൻ, കമ്പനിയും ഞാൻ."),
 ("V","V","ഞാൻ ടേസ്റ്റ് ടെസ്റ്റർ. ശമ്പളം ദിവസം രണ്ട് ഉന്നക്കായ."),
 ("A","wide","അത് ഡീൽ. പക്ഷേ ഇന്നത്തേത് സ്കൂളിനുള്ളതാ, തൊടല്ലേ!")],
 "പാർട്ണർ ഇല്ലെങ്കിലും\nകമ്പനി തുടങ്ങാം", CTA_START,
 cap_ml="വീട്ടിൽ പലഹാരം ഉണ്ടാക്കുന്ന സംരംഭകയ്ക്ക് 12 സ്കൂൾ ക്യാന്റീനുകളുടെ ഓർഡർ, ബിൽ കമ്പനിയുടേത് വേണം, പക്ഷേ ഭർത്താവ് ഡയറക്ടർ ആകാനില്ല. ഒറ്റയ്ക്ക് തുടങ്ങാൻ വൺ പേഴ്സൺ കമ്പനി (OPC) ഉണ്ട്. ഉടമയും ഡയറക്ടറും ഒരാൾ തന്നെ.",
 cap_en="A home snack-maker in Kerala is asked to supply 12 school canteens with company bills, but her husband doesn't want to be a director. A solo owner can register a One Person Company (OPC) and be its only director and shareholder.",
 cap_mg="Veettil palahaaram undaakkunna aalkku 12 school canteen order, bill company-yude venam, pakshe bharthavu director aakaan illa. Ottaykku thudangan one person company (OPC) undu. Owner-um director-um ningal thanne.")

# chat: Rasheed's printing press wins a three-year exam-booklet contract; he thinks his son in Canada cannot be the second director.
chat("c971", "proprietor", "A", "പ്രസ്സിന് 3 വർഷത്തെ\nപരീക്ഷാ ബുക്ക്‌ലെറ്റ് ഓർഡർ.\nമകൻ കാനഡയിൽ", ("റഷീദ്", "മകൻ"), [
 (0,"മോനേ, യൂണിവേഴ്സിറ്റിയുടെ പരീക്ഷാ ബുക്ക്‌ലെറ്റ് മൂന്ന് വർഷം നമ്മുടെ പ്രസ്സിൽ. പക്ഷേ കമ്പനി ആയിരിക്കണം."),
 (1,"ഉപ്പാ, സൂപ്പർ! നാൽപ്പത് കൊല്ലത്തെ മഷിയുടെ മണത്തിന് കിട്ടിയ സമ്മാനം."),
 (0,"രണ്ട് ഡയറക്ടർ വേണം. ഉമ്മയ്ക്ക് താൽപ്പര്യമില്ല. നീയാണെങ്കിൽ കാനഡയിൽ. അത് നടക്കില്ലല്ലോ."),
 (1,"നടക്കും ഉപ്പാ. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടർ ആകാം."),
 (1,"ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം. അത് ഉപ്പ തന്നെ."),
 (0,"അപ്പോ ഞാൻ ഇവിടെ, നീ അവിടെ. രണ്ടുപേരും ഡയറക്ടർ."),
 (1,"അതെ. ഡോക്യുമെന്റ്സ് ഞാൻ ഇവിടുന്ന് അയക്കാം. ഉപ്പ ഓഫീസ് അഡ്രസ്സിന്റെ പേപ്പർ റെഡിയാക്കിക്കോ."),
 (0,"ശരി. ആദ്യത്തെ ബുക്ക്‌ലെറ്റിന്റെ കവറിൽ നിന്റെ പേരും അച്ചടിക്കാം!")],
 "മകൻ വിദേശത്താണോ?\nഡയറക്ടർ ആകാം", CTA_START,
 cap_ml="നാൽപ്പത് വർഷമായി പ്രിന്റിംഗ് പ്രസ്സ് നടത്തുന്ന ഉപ്പയ്ക്ക് യൂണിവേഴ്സിറ്റിയുടെ മൂന്ന് വർഷത്തെ ഓർഡർ, കമ്പനി വേണം, മകൻ കാനഡയിൽ. NRI-ക്കും Pvt Ltd കമ്പനിയിൽ ഡയറക്ടർ ആകാം. നാട്ടിലുള്ള ഒരു ഡയറക്ടർ മതി.",
 cap_en="A printing-press owner in Kerala wins a three-year exam-booklet order that needs a company, and his only willing co-director is his son in Canada. NRIs can be directors of an Indian private limited company; the father at home is the resident director.",
 cap_mg="40 varshamaayi printing press nadathunna uppaykku university-yude 3 varsha order, company venam, makan Canada-yil. NRI-kkum Pvt Ltd company-il director aakaam. Naattilulla oru director mathi.")

lst("l971", "proprietor", "C", "കട കമ്പനി ആക്കും മുമ്പ്\nഈ 3 പേപ്പർ\nറെഡി ആക്കി വെക്കൂ", [
 ("ഓഫീസ് അഡ്രസ്സിന്റെ പേപ്പർ", "കടയോ വീടോ ആകാം. ഉടമയുടെ NOC, പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ല്."),
 ("ആരൊക്കെ ഡയറക്ടർ", "Pvt Ltd-ന് കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC."),
 ("മൂന്ന് പേരുകൾ", "നിലവിലുള്ള കമ്പനിയോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യമുള്ള പേര് റിജക്ട് ആകാം.")],
 "പേപ്പർ റെഡി എങ്കിൽ\nകമ്പനി വേഗം", CTA_DOCS,
 cap_ml="കടയോ ചെറിയ ബിസിനസോ കമ്പനി ആക്കാൻ ആദ്യം റെഡിയാക്കേണ്ടത്: ഓഫീസ് അഡ്രസ്സിന് ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും, ആരൊക്കെ ഡയറക്ടർ എന്ന തീരുമാനം, സാമ്യമില്ലാത്ത മൂന്ന് കമ്പനി പേരുകൾ.",
 cap_en="Turning your shop into a company in Kerala? Get three things ready first: the office address papers (owner's NOC and a recent utility bill), who the directors are (two for a Pvt Ltd, or an OPC if you are alone), and three company names that don't copy anyone.",
 cap_mg="Kada company aakkan aadyam ready aakkendathu: office address-nu owner-nte NOC-um puthiya utility bill-um, aarokke director ennu theerumanam, saamyam illaatha 3 company names. Company registration documents checklist.")

# ---------------- nri ----------------
# gulf: Shiju + Faisal. Shiju, an electrician in Doha, plans a rooftop-solar firm in Palakkad with his cousin but wants to wait two years until he goes home for good.
duo("d1506", "nri", "A", "gulf", "ദോഹയിൽ ഇലക്ട്രീഷ്യൻ.\nനാട്ടിൽ സോളാർ കമ്പനി.\n\"നാട്ടിൽ സെറ്റിൽ ആയിട്ട്\"", [
 ("V","wide","ഷിജുവേട്ടാ, ഈ സോളാർ പാനലിന്റെ വീഡിയോ ഇന്ന് പത്താമത്തെ തവണയാ കാണുന്നത്."),
 ("A","A","ഫൈസലേ, പാലക്കാട്ട് കസിൻ ഒരു സോളാർ ഇൻസ്റ്റലേഷൻ കമ്പനി തുടങ്ങാമെന്ന്. നാട്ടിൽ വെയിലിന് കുറവില്ലല്ലോ."),
 ("V","V","അടിപൊളി. എന്നാ തുടങ്ങുന്നത്?"),
 ("A","A","രണ്ട് കൊല്ലം കഴിഞ്ഞ്. ഞാൻ നാട്ടിൽ സെറ്റിൽ ആയിട്ട്. ഗൾഫിൽ ഇരുന്ന് ഡയറക്ടർ ആകാൻ പറ്റില്ലല്ലോ."),
 ("V","wide","പറ്റും ചേട്ടാ. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("V","V","ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി. അത് കസിൻ."),
 ("A","A","അപ്പോ രണ്ട് കൊല്ലം കാത്തിരിക്കണ്ട. ഇപ്പോ തുടങ്ങിയാൽ ഞാൻ വരുമ്പോഴേക്കും കമ്പനിക്ക് രണ്ട് വയസ്സ്."),
 ("V","V","ഇവിടെ ചേട്ടൻ വയറിംഗ്, അവിടെ കസിൻ പാനൽ. നല്ല കണക്ഷൻ!"),
 ("A","wide","ഷോർട്ട് സർക്യൂട്ട് ഇല്ലാതെ നോക്കിയാൽ മതി!")],
 "ഗൾഫിൽ ഇരുന്നും\nനാട്ടിൽ ഡയറക്ടർ", CTA_START,
 cap_ml="ദോഹയിൽ ഇലക്ട്രീഷ്യനായ NRI-ക്ക് പാലക്കാട്ട് കസിനുമായി സോളാർ ഇൻസ്റ്റലേഷൻ കമ്പനി, പക്ഷേ നാട്ടിൽ സെറ്റിൽ ആയിട്ട് മതിയെന്ന് കരുതി. NRI-ക്ക് ഗൾഫിലിരുന്ന് തന്നെ Pvt Ltd കമ്പനിയിൽ ഡയറക്ടർ ആകാം. ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ മതി.",
 cap_en="An NRI electrician in Doha plans a solar installation company in Palakkad with his cousin, but wants to wait two years until he moves home. NRIs can be directors of an Indian private limited company now, as long as one director, here the cousin, lives in India.",
 cap_mg="Doha-yil electrician aaya NRI-kku Palakkad-il cousin-umaayi solar company, pakshe naattil settle aayittu mathi ennu vicharichu. NRI-kku Gulf-il irunnu thanne Pvt Ltd-il director aakaam. NRI business in Kerala ippol thudangaam.")

# gulfroom: Naseer + Shamsu. Their Kerala company was formed to run a rented warehouse, but the building is not ready; no revenue this year, so they plan no filing.
duo("d1507", "nri", "C", "gulfroom", "റിയാദിൽ ഇരുന്ന് നാട്ടിൽ\nകമ്പനി തുടങ്ങി.\nഗോഡൗൺ ഇതുവരെ റെഡി ആയില്ല", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ ഗോഡൗണിന്റെ ഫോട്ടോ വന്നോ? പണി കഴിഞ്ഞോ?"),
 ("V","V","എവിടെ നസീർക്കാ. ഇനിയും ആറ് മാസം. മേൽക്കൂര പോലും ആയില്ല."),
 ("A","A","അപ്പോ ഈ വർഷം കമ്പനിക്ക് ഒരു രൂപ പോലും വരുമാനം ഇല്ല."),
 ("V","V","ഇല്ല. അതുകൊണ്ട് ഈ വർഷം കമ്പനിയുടെ കണക്ക്, ഫയലിംഗ് ഒന്നും വേണ്ടല്ലോ. ഒരു ടെൻഷൻ കുറഞ്ഞു."),
 ("A","wide","അത് ശരിയല്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("A","A","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. നമ്മൾ ഇവിടെ ഇരിക്കുമ്പോഴും അത് കൂടും."),
 ("V","V","ഗോഡൗൺ പണിയും മുമ്പ് പിഴയുടെ ഗോഡൗൺ പണിയണ്ട."),
 ("A","A","നാട്ടിലെ ഡയറക്ടറോട് പറ. ഓഡിറ്ററെ കണ്ട് ഡ്യൂ ഡേറ്റ് എഴുതി വെക്കാൻ."),
 ("V","wide","ഇന്ന് തന്നെ വിളിക്കാം. ഗോഡൗൺ വൈകിയാലും ഫയലിംഗ് വൈകില്ല!")],
 "ഗോഡൗൺ റെഡി അല്ലെങ്കിലും\nഫയലിംഗ് ഉണ്ട്", CTA_AFTER,
 cap_ml="റിയാദിലെ രണ്ട് NRI-കൾ നാട്ടിൽ തുടങ്ങിയ കമ്പനിയുടെ ഗോഡൗൺ പണി തീർന്നിട്ടില്ല, ഈ വർഷം വരുമാനമില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="Two NRIs in Riyadh formed a company in Kerala for a warehouse that is still under construction, so there is no revenue this year. Annual filings are still due with zero revenue, and late filing costs Rs 100 per day per form even while you are abroad.",
 cap_mg="Riyadh-ile 2 NRI-kal naattil thudangiya company-yude godown pani theernnilla, ee varsham revenue illa. Zero revenue aanenkilum annual filing (ROC) cheyyanam. Vaikiyal oro form-inum divasam 100 roopa.")

# gulfoffice: Shahana + Asif. Shahana, an HR manager in Abu Dhabi, wants an interview-coaching centre in Kottayam run by her mother; she thinks NRIs can only invest, not direct.
duo("d1508", "nri", "B", "gulfoffice", "അബുദാബിയിൽ HR മാനേജർ.\nകോട്ടയത്ത് ഇന്റർവ്യൂ\nകോച്ചിംഗ് സെന്റർ", [
 ("V","wide","ഷഹാന, ഇന്റർവ്യൂ എടുക്കുന്ന ആൾ ഇന്ന് ഇന്റർവ്യൂ ടിപ്സ് എഴുതുന്നോ?"),
 ("A","A","ആസിഫേ, കോട്ടയത്ത് ഒരു ഇന്റർവ്യൂ കോച്ചിംഗ് സെന്റർ. ഉമ്മ നടത്തും. ഞാൻ ഇവിടുന്ന് ഓൺലൈനിൽ ക്ലാസ് എടുക്കും."),
 ("V","V","കൊള്ളാം. കമ്പനി ആരുടെ പേരിൽ?"),
 ("A","A","ഉമ്മയും അമ്മാവനും ഡയറക്ടർ. ഞാൻ പൈസ മാത്രം ഇടും. NRI-ക്ക് ഡയറക്ടർ ആകാൻ പറ്റില്ലല്ലോ."),
 ("V","wide","പറ്റും. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("V","V","ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ വേണം. ഉമ്മ അവിടെ ഉണ്ടല്ലോ. നീയും ഉമ്മയും മതി."),
 ("A","A","അപ്പോ അമ്മാവനെ ബുദ്ധിമുട്ടിക്കണ്ട. ഐഡിയ എന്റേത്, തീരുമാനവും എന്റേത്."),
 ("V","V","കറക്റ്റ്. സ്വന്തം കമ്പനിയിൽ നീ വെറും പൈസ ആകണ്ട."),
 ("A","wide","ഇന്റർവ്യൂ ടിപ് നമ്പർ ഒന്ന്: സ്വന്തം കസേര വിട്ടുകൊടുക്കരുത്!")],
 "NRI-ക്ക് പൈസ മാത്രമല്ല,\nഡയറക്ടർ കസേരയും", CTA_START,
 cap_ml="അബുദാബിയിൽ HR മാനേജറായ NRI-ക്ക് കോട്ടയത്ത് ഉമ്മയുമായി ഇന്റർവ്യൂ കോച്ചിംഗ് സെന്റർ, പക്ഷേ NRI-ക്ക് ഡയറക്ടർ ആകാൻ പറ്റില്ലെന്ന് കരുതി. NRI-ക്ക് Pvt Ltd കമ്പനിയിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം, ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.",
 cap_en="An NRI HR manager in Abu Dhabi is starting an interview-coaching centre in Kottayam with her mother and thought NRIs could only invest. NRIs can be both directors and shareholders of an Indian private limited company; her mother at home is the resident director.",
 cap_mg="Abu Dhabi-yil HR manager aaya NRI-kku Kottayam-il ummayumaayi interview coaching centre, pakshe NRI-kku director aakaan pattilla ennu vicharichu. NRI-kku Pvt Ltd-il director-um shareholder-um aakaam, oru director India-yil thamasikkunna aal.")

# mall: Sumayya + Jafar. Their Kerala-made attar brand, sold in Dubai, is named almost like a famous perfume house.
duo("d1509", "nri", "A", "mall", "നാട്ടിൽ ഉണ്ടാക്കുന്ന അത്തർ.\nദുബായിൽ വിൽപ്പന.\nപേര് ഒരു വലിയ പെർഫ്യൂം ഹൗസ് പോലെ", [
 ("A","wide","ജാഫറേ, ആ കടയിലെ ഷോകേസ് നോക്കി എന്താ ഇങ്ങനെ നിൽക്കുന്നത്?"),
 ("V","V","സുമയ്യ, നമ്മുടെ അത്തർ ബ്രാൻഡിന് ഇട്ട പേര്. ഈ കടയുടെ ബോർഡിലും ഏകദേശം അതേ പേര്!"),
 ("A","A","അത് ഒരു വലിയ പെർഫ്യൂം ഹൗസ് അല്ലേ? അവരുടെ പേര് എല്ലാ മാളിലും ഉണ്ടല്ലോ."),
 ("V","V","എനിക്ക് അത് ഓർമ്മ വന്നില്ല. നാട്ടിലെ കമ്പനി രജിസ്ട്രേഷന് അതേ പേരാ കൊടുക്കാൻ ഇരുന്നത്."),
 ("A","wide","കൊടുക്കല്ലേ. ട്രേഡ്മാർക്ക് ഉള്ള ബ്രാൻഡിനോട് സാമ്യം ഉണ്ടെങ്കിൽ കമ്പനി പേര് റിജക്ട് ആകാം."),
 ("A","A","പിന്നെ ലേബൽ, കുപ്പി, എല്ലാം മാറ്റേണ്ടി വരും. ആദ്യമേ നമ്മുടേതായ ഒരു പേര്."),
 ("V","V","നമ്മുടെ നാട്ടിലെ മുല്ലപ്പൂവിന്റെ പേര് വെച്ചാലോ?"),
 ("A","A","അത് കൊള്ളാം. അതുപോലെ മൂന്ന് പേര് കൂടി. ഒന്ന് പോയാലും ബാക്കി ഉണ്ട്."),
 ("V","wide","ശരി. പേരിനും ഇനി നാടിന്റെ മണം!")],
 "മറ്റൊരാളുടെ പേരിന്\nനിങ്ങളുടെ മണം ഉണ്ടാകില്ല", CTA_NAME,
 cap_ml="നാട്ടിൽ ഉണ്ടാക്കി ദുബായിൽ വിൽക്കുന്ന അത്തർ ബ്രാൻഡിന് ഒരു വലിയ പെർഫ്യൂം ബ്രാൻഡിന്റെ പോലുള്ള പേര്. ട്രേഡ്മാർക്ക് ഉള്ള ബ്രാൻഡിനോട് സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകാം. ലേബൽ ചെയ്യും മുമ്പ് സ്വന്തം പേരും ബാക്കപ്പ് പേരുകളും ഉറപ്പിക്കൂ.",
 cap_en="An NRI couple in Dubai sells a Kerala-made attar brand whose name sounds like a famous perfume house. A company name that clashes with a trademark can be rejected, so settle an original name, with backups, before labels and bottles are printed.",
 cap_mg="Naattil undaakki Dubai-il vilkkunna attar brand-nu oru famous perfume brand pole ulla peru. Trademark ulla brand-inodu saamyam ulla company name reject aakaam. Label cheyyunnathinu munpu swantham company name urappikku.")

# airport: Shameer + Rafeeq. Shameer is back from Kuwait for good to open a used-car showroom and thinks a company needs 25 lakh shown in the bank.
duo("d1510", "nri", "B", "airport", "കുവൈത്തിൽ നിന്ന്\nഎന്നെന്നേക്കുമായി തിരികെ.\nയൂസ്ഡ് കാർ ഷോറൂം", [
 ("V","wide","ഷമീർക്കാ, ഇത്തവണ ലഗേജ് കൂടുതലാണല്ലോ. തിരിച്ച് പോകുന്നില്ലേ?"),
 ("A","A","ഇല്ല റഫീഖേ. ഇരുപത് കൊല്ലം കുവൈത്തിൽ കാർ വിറ്റു. ഇനി നാട്ടിൽ സ്വന്തം യൂസ്ഡ് കാർ ഷോറൂം."),
 ("V","V","സൂപ്പർ! കമ്പനി ആക്കുന്നില്ലേ?"),
 ("A","A","ആക്കണം. പക്ഷേ കമ്പനിക്ക് ബാങ്കിൽ ഇരുപത്തഞ്ച് ലക്ഷം കാണിക്കണമെന്ന് കേട്ടു. സെറ്റിൽമെന്റ് പൈസ ഇനിയും വന്നിട്ടില്ല."),
 ("V","wide","അത് തെറ്റാ ഇക്കാ. പ്രൈവറ്റ് ലിമിറ്റഡ് തുടങ്ങാൻ മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 ("V","V","രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ. ഇക്കയും ഇത്തയും മതി."),
 ("A","A","അപ്പോ സെറ്റിൽമെന്റ് വരുന്നത് വരെ കാത്തിരിക്കണ്ട?"),
 ("V","V","വേണ്ട. പൈസ വരുമ്പോൾ അത് കാറിന്. കമ്പനി ഇപ്പോ തന്നെ."),
 ("A","wide","ശരി. ആദ്യ കാർ വിൽക്കുമ്പോൾ നിനക്ക് ഒരു ടെസ്റ്റ് ഡ്രൈവ് ഫ്രീ!")],
 "കമ്പനിക്ക്\nലക്ഷങ്ങൾ കാണിക്കേണ്ട", CTA_START,
 cap_ml="കുവൈത്തിൽ നിന്ന് എന്നെന്നേക്കുമായി തിരിച്ചെത്തിയ NRI-ക്ക് നാട്ടിൽ യൂസ്ഡ് കാർ ഷോറൂം കമ്പനി, പക്ഷേ ബാങ്കിൽ 25 ലക്ഷം കാണിക്കണമെന്ന് കരുതി. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല.",
 cap_en="An NRI back from Kuwait for good wants to open a used-car showroom in Kerala and believes a company must show 25 lakh in the bank. A private limited company has no minimum paid-up capital; two directors and two shareholders are enough to register.",
 cap_mg="Kuwait-il ninnu thirichu vanna NRI-kku naattil used car showroom company, pakshe bank-il 25 lakh kaanikkanam ennu vicharichu. Pvt Ltd company-kku minimum paid-up capital nirbandham illa. Returning NRI business Kerala.")

# railway: Sheeba + Dinesh. Sheeba, a nurse in Ireland, funds her sister's Hindi-tuition centre and wants shares; the sister plans a partnership with a friend.
duo("d1511", "nri", "C", "railway", "അയർലണ്ടിൽ നഴ്സ്.\nഅനിയത്തിയുടെ ട്യൂഷൻ\nസെന്ററിൽ ഷെയർ വേണം", [
 ("V","wide","ഷീബേച്ചീ, ട്രെയിൻ വരാൻ ഇനിയും അര മണിക്കൂർ. ലീവ് എങ്ങനെ പോകുന്നു?"),
 ("A","A","ദിനേശേ, ലീവ് മുഴുവൻ അനിയത്തിയുടെ ഹിന്ദി ട്യൂഷൻ സെന്ററിന്റെ കാര്യമാ. ഞാനാ പൈസ ഇടുന്നത്."),
 ("V","V","അപ്പോ ചേച്ചിക്ക് ഷെയർ ഉണ്ടല്ലോ?"),
 ("A","A","അതാ സംശയം. അവൾ കൂട്ടുകാരിയുമായി പാർട്ണർഷിപ്പ് ആക്കാൻ ഇരിക്കുവാ. ഞാൻ അയർലണ്ടിൽ. എനിക്ക് ഷെയർ എങ്ങനെ?"),
 ("V","wide","പാർട്ണർഷിപ്പിൽ ഷെയർ ഇല്ല ചേച്ചീ. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം."),
 ("V","V","NRI-ക്കും പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡർ ആകാം. അനിയത്തിയും കൂട്ടുകാരിയും ഡയറക്ടർ."),
 ("A","A","അപ്പോ എന്റെ പൈസയ്ക്ക് എന്റെ പേരിൽ ഷെയർ. അയർലണ്ടിൽ ഇരുന്നാലും."),
 ("V","V","അതെ. പാർട്ണർഷിപ്പ് ഡീഡ് എഴുതും മുമ്പ് ഇത് അവളോട് പറ."),
 ("A","wide","ശരി. ഹിന്ദിയിൽ പറയാം, അവൾക്ക് എളുപ്പം മനസ്സിലാകും!")],
 "പൈസ ഇടുന്നത് നിങ്ങൾ.\nഷെയർ നിങ്ങളുടെ പേരിൽ", CTA_START,
 cap_ml="അയർലണ്ടിൽ നഴ്സായ ചേച്ചി അനിയത്തിയുടെ ഹിന്ദി ട്യൂഷൻ സെന്ററിന് പൈസ ഇടുന്നു, പക്ഷേ അനിയത്തി പാർട്ണർഷിപ്പ് ആക്കാൻ ഇരിക്കുന്നു. പാർട്ണർഷിപ്പിൽ ഷെയർ ഇല്ല. NRI-ക്ക് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയിൽ ഷെയർഹോൾഡർ ആകാം.",
 cap_en="A Malayali nurse in Ireland is funding her sister's Hindi-tuition centre in Kerala, but the sister plans a partnership with a friend. A partnership cannot issue shares; in a private limited company the NRI sister can hold shares while the two at home are directors.",
 cap_mg="Ireland-il nurse aaya chechi aniyathiyude Hindi tuition centre-nu paisa idunnu, pakshe aniyathi partnership aakkan irikkunnu. Partnership-il share illa. NRI-kku Pvt Ltd company-il shareholder aakaam.")

# chat: Muneer, an engineer in Saudi, and his wife Fathima, who runs their new Kerala company; day 20 of the auditor's 30 days.
chat("c972", "nri", "B", "ഭർത്താവ് സൗദിയിൽ.\nകമ്പനി ആയിട്ട് 20 ദിവസം.\nഓഡിറ്റർ ഇതുവരെ ഇല്ല", ("ഫാത്തിമ", "മുനീർ"), [
 (0,"ഇക്കാ, കമ്പനി സർട്ടിഫിക്കറ്റ് വന്നിട്ട് ഇന്ന് ഇരുപത് ദിവസം. ആരോ ചോദിച്ചു, ഓഡിറ്റർ ആരാന്ന്."),
 (1,"ഓഡിറ്റർ ഒക്കെ മാർച്ചിൽ അല്ലേ? ഞാൻ ലീവിന് വരുമ്പോൾ നോക്കാം."),
 (0,"അല്ല ഇക്കാ. കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ വെക്കണം."),
 (1,"മുപ്പതോ? അപ്പോ ഇനി പത്ത് ദിവസം മാത്രം. എന്റെ ലീവ് മൂന്ന് മാസം കഴിഞ്ഞാ."),
 (0,"അതുകൊണ്ട് ഞാൻ നാളെ ടൗണിലെ ഓഡിറ്ററെ കാണാം. ഡയറക്ടർ ഞാനും ആണല്ലോ."),
 (1,"ശരി. പിന്നെ വേറെ എന്തെങ്കിലും?"),
 (0,"നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A. അതും കലണ്ടറിൽ ഇട്ടു."),
 (1,"ഞാൻ സൗദിയിൽ എഞ്ചിനീയർ. നാട്ടിലെ കമ്പനിയുടെ ചീഫ് എഞ്ചിനീയർ നീ!")],
 "മുപ്പത് ദിവസത്തിൽ\nആദ്യ ഓഡിറ്റർ", CTA_AFTER,
 cap_ml="ഭർത്താവ് സൗദിയിൽ, ഭാര്യ നാട്ടിൽ കമ്പനി നോക്കുന്നു. കമ്പനി ആയിട്ട് 20 ദിവസം, ഓഡിറ്ററെ വെച്ചിട്ടില്ല. രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം, 180 ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം.",
 cap_en="An NRI engineer in Saudi Arabia thinks the auditor is a March job, while his wife runs their new company in Kerala. The first auditor must be appointed within 30 days of incorporation, and INC-20A filed within 180 days, leave or no leave.",
 cap_mg="Bharthavu Saudi-yil, bharya naattil company nokkunnu. Company aayittu 20 divasam, auditor-ne vechilla. Register cheythu 30 days-inullil first auditor venam, 180 days-inullil INC-20A file cheyyanam.")

# ---------------- solo ----------------
# ferry: Meera + Tony. Tony guides backwater fishing trips alone; a travel app will list only companies; he thinks he needs a partner first.
duo("d1512", "solo", "A", "ferry", "കായലിൽ ചൂണ്ടയിടൽ ട്രിപ്പ്.\nട്രാവൽ ആപ്പ്:\n\"കമ്പനികളെ മാത്രം ലിസ്റ്റ് ചെയ്യും\"", [
 ("A","wide","ടോണീ, ഇന്ന് ഒരു മീൻ പോലും കിട്ടിയില്ലേ? മുഖം അങ്ങനെ."),
 ("V","V","മീൻ കിട്ടി മീരേ. കിട്ടാത്തത് ഒരു പാർട്ണറെയാ."),
 ("A","A","പാർട്ണറോ? ചൂണ്ടയിടാൻ രണ്ടുപേർ വേണോ?"),
 ("V","V","ആ വലിയ ട്രാവൽ ആപ്പ് എന്റെ ട്രിപ്പ് ലിസ്റ്റ് ചെയ്യാമെന്ന്. പക്ഷേ കമ്പനി ആയിരിക്കണം. കമ്പനിക്ക് രണ്ടുപേർ വേണ്ടേ?"),
 ("A","wide","വേണ്ട. ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി ഉണ്ട്. OPC. ഉടമയും ഡയറക്ടറും നീ തന്നെ."),
 ("A","A","ഓഫീസ് അഡ്രസ്സിന് വീട് മതി. വീട് ആരുടെ പേരിലാണോ അവരുടെ NOC, ഒരു പുതിയ കറന്റ് ബില്ല്."),
 ("V","V","അപ്പോ ഈ വള്ളവും ഞാനും, ഒരു കമ്പനി!"),
 ("A","A","അതെ. പാർട്ണറെ തേടി സമയം കളയണ്ട. സീസൺ തുടങ്ങാറായി."),
 ("V","wide","ശരി. ഇന്ന് മുതൽ ഞാൻ കായലിലെ ഏക ഡയറക്ടർ!")],
 "പാർട്ണറെ കാത്തിരിക്കേണ്ട.\nOPC ഉണ്ട്", CTA_START,
 cap_ml="കായലിൽ ചൂണ്ടയിടൽ ട്രിപ്പ് ഒറ്റയ്ക്ക് നടത്തുന്ന ഗൈഡിന് ട്രാവൽ ആപ്പിൽ ലിസ്റ്റ് ചെയ്യാൻ കമ്പനി വേണം, പാർട്ണർ ഇല്ലെന്ന് വിഷമം. ഒറ്റയ്ക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം. വീട് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ ബില്ലും മതി.",
 cap_en="A solo backwater fishing guide in Kerala can get listed on a big travel app only as a company, and thinks he needs a partner first. A solo founder can register a One Person Company (OPC), with his home as the office using the owner's NOC and a recent utility bill.",
 cap_mg="Kaayalil choondayidal trip ottaykku nadathunna guide-nu travel app-il list cheyyan company venam, partner illa ennu vishamam. Ottaykku one person company (OPC) thudangaam. Veedu office aakkan owner NOC-um puthiya bill-um mathi.")

# weddinghall: Kavya + Sarath. Kavya rents bridal jewellery alone through her OPC; it is day 165 and INC-20A is not filed.
duo("d1513", "solo", "B", "weddinghall", "ബ്രൈഡൽ ആഭരണ റെന്റൽ.\nOPC ആയിട്ട് 165 ദിവസം.\nINC-20A ബാക്കി", [
 ("V","wide","കാവ്യേ, ഇന്നത്തെ കല്യാണപ്പെണ്ണിന്റെ മാല നിന്റേതാണല്ലേ? സ്റ്റേജ് മൊത്തം തിളങ്ങുന്നു."),
 ("A","A","ശരത്തേ, എന്റെ റെന്റൽ കളക്ഷൻ. ഈ സീസണിൽ പതിനെട്ട് കല്യാണം. കമ്പനി ആക്കിയത് നന്നായി."),
 ("V","V","കമ്പനി ആയിട്ട് എത്ര നാളായി?"),
 ("A","A","നൂറ്റിയറുപത്തഞ്ച് ദിവസം. ഞാൻ ഒറ്റയ്ക്കല്ലേ. OPC. അതിന് പ്രത്യേകിച്ച് ഫോം ഒന്നും ഇല്ലല്ലോ."),
 ("V","wide","ഉണ്ട്. INC-20A. കമ്പനി ഉണ്ടായി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം. ഇനി പതിനഞ്ച് ദിവസം."),
 ("V","V","മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ വെച്ച്, ഒരു ലക്ഷം വരെ."),
 ("A","A","അയ്യോ! മാല തിരിച്ച് വാങ്ങാൻ മറന്നാലും ഇത് മറക്കരുതായിരുന്നു."),
 ("V","V","ഈ ആഴ്ച തന്നെ ചെയ്യ്. കല്യാണ സീസൺ ആണെന്ന് പിഴയ്ക്ക് അറിയില്ല."),
 ("A","wide","നാളെ രാവിലെ ആദ്യത്തെ ജോലി അത്. മാല പിന്നെ!")],
 "OPC ആണെങ്കിലും\nINC-20A ഉണ്ട്", CTA_AFTER,
 cap_ml="ബ്രൈഡൽ ആഭരണങ്ങൾ വാടകയ്ക്ക് കൊടുക്കുന്ന സംരംഭകയുടെ വൺ പേഴ്സൺ കമ്പനിക്ക് 165 ദിവസം, INC-20A ഫയൽ ചെയ്തിട്ടില്ല. OPC ആണെങ്കിലും 180 ദിവസത്തിനുള്ളിൽ INC-20A വേണം. വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ (പരമാവധി 1 ലക്ഷം).",
 cap_en="A solo bridal-jewellery rental founder in Kerala runs her business as a One Person Company that is 165 days old, with INC-20A not filed. An OPC must also file INC-20A within 180 days; missing it means Rs 50,000 on the company and Rs 1,000 a day per officer, up to Rs 1 lakh.",
 cap_mg="Bridal jewellery rental nadathunna aalude one person company-kku 165 divasam, INC-20A file cheythilla. OPC aanenkilum 180 days-inullil INC-20A venam. Vaikiyal company-kku 50,000 roopa, director-kku divasam 1,000 roopa (max 1 lakh).")

# akshaya: Sudha + Ramesh. Ramesh keeps bees alone and wants his company named like the biggest honey brand in the shops.
duo("d1514", "solo", "C", "akshaya", "തേനീച്ച കർഷകൻ.\nകമ്പനിക്ക് പേര്:\nകടയിലെ വലിയ തേൻ ബ്രാൻഡ് പോലെ", [
 ("A","wide","രമേശേട്ടാ, ഫോമിൽ കമ്പനി പേരിന്റെ കോളം. എന്താ എഴുതേണ്ടത്?"),
 ("V","V","സുധേ, ഞാൻ ആലോചിച്ച് വെച്ചിട്ടുണ്ട്. ആ വലിയ തേൻ ബ്രാൻഡ് ഇല്ലേ, എല്ലാ കടയിലും ഉള്ളത്. അതിന്റെ കൂടെ കേരള."),
 ("A","A","അത് അവരുടെ ബ്രാൻഡ് അല്ലേ? ചേട്ടന്റെ തേൻ ചേട്ടന്റേതല്ലേ?"),
 ("V","V","അതാ ബുദ്ധി. ആൾക്കാർ കണ്ടാൽ ഉടനെ വാങ്ങും."),
 ("A","wide","ബുദ്ധി കൂടിപ്പോയി. ട്രേഡ്മാർക്ക് ഉള്ള ബ്രാൻഡിനോട് സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകാം."),
 ("A","A","ചേട്ടന്റെ തേനീച്ചകൾ കാട്ടുപൂവിൽ നിന്നല്ലേ. അതുപോലെ സ്വന്തം ഒരു പേര്. മൂന്നെണ്ണം എഴുതി താ."),
 ("V","V","എന്റെ തേനീച്ചകൾക്ക് പേരുണ്ട്. ഒന്നാമത്തേത് റാണി."),
 ("A","A","റാണി കൊള്ളാം. അതുപോലെ രണ്ടെണ്ണം കൂടി."),
 ("V","wide","എങ്കിൽ റാണിയുടെ കൊട്ടാരം എന്റെ കമ്പനി!")],
 "വലിയ ബ്രാൻഡിന്റെ\nതണലിൽ പേര് വേണ്ട", CTA_NAME,
 cap_ml="ഒറ്റയ്ക്ക് തേനീച്ച വളർത്തുന്ന കർഷകന് കടയിലെ വലിയ തേൻ ബ്രാൻഡിന്റെ പോലുള്ള കമ്പനി പേര് വേണം. ട്രേഡ്മാർക്ക് ഉള്ള ബ്രാൻഡിനോട് സാമ്യമുള്ള പേര് റിജക്ട് ആകാം. സ്വന്തമായ മൂന്ന് പേരുകൾ കരുതിയാൽ രജിസ്ട്രേഷൻ വൈകില്ല.",
 cap_en="A solo beekeeper in Kerala wants to name his company after the biggest honey brand in the shops. A company name similar to a trademarked brand can be rejected, so keep three original names ready before you apply.",
 cap_mg="Ottaykku theneecha valarthunna karshakan-nu kadayile valiya honey brand pole ulla company name venam. Trademark ulla brand-inodu saamyam ulla peru reject aakaam. Swantham 3 company names ready aakku.")

# courier: Jaya + Aravind. Jaya posts Kerala spice packs to customers in Europe alone; she wants an OPC with her husband's house as the office.
duo("d1515", "solo", "A", "courier", "ഒറ്റയ്ക്ക് സ്പൈസ് പാർസൽ.\nയൂറോപ്പിലേക്ക്.\nഓഫീസ്? ഭർത്താവിന്റെ വീട്", [
 ("V","wide","ജയചേച്ചീ, ഇന്നും ഇരുപത് പാർസൽ? ഏലക്കയുടെ മണം കൗണ്ടർ മുഴുവൻ."),
 ("A","A","അരവിന്ദേ, ജർമനിയിലും ഹോളണ്ടിലും ഉള്ളവർക്കാ. ഇനി ഒരു ഷോപ്പ് ചെയിൻ സ്ഥിരം ഓർഡർ തരാമെന്ന്, കമ്പനി ആണെങ്കിൽ."),
 ("V","V","ചേച്ചി ഒറ്റയ്ക്കല്ലേ ഇത് മുഴുവൻ ചെയ്യുന്നത്?"),
 ("A","A","അതെ. OPC തുടങ്ങാമെന്ന് വെച്ചു. പക്ഷേ ഓഫീസ് വീട്ടിൽ ആണ്. വീട് ഭർത്താവിന്റെ പേരിൽ."),
 ("V","wide","അത് മതി ചേച്ചീ. വീടും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമ എന്ന നിലയിൽ ചേട്ടന്റെ NOC വേണം."),
 ("V","V","കൂടെ പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ല്. കറന്റോ വെള്ളമോ."),
 ("A","A","കമ്പനിയിൽ ചേരില്ല എന്ന് പറഞ്ഞ ആൾ NOC-യിൽ ഒപ്പിടുമോ?"),
 ("V","V","ഒപ്പിടാൻ ഡയറക്ടർ ആകേണ്ട. വീട്ടുടമ ആയാൽ മതി."),
 ("A","wide","ശരി. ഇന്ന് രാത്രി ഏലക്ക ചായയും NOC ഫോമും ഒരുമിച്ച്!")],
 "വീട് ആരുടെ പേരിലായാലും\nഓഫീസ് ആക്കാം", CTA_DOCS,
 cap_ml="യൂറോപ്പിലേക്ക് സ്പൈസ് പാർസൽ ഒറ്റയ്ക്ക് അയക്കുന്ന സംരംഭകയ്ക്ക് ഷോപ്പ് ചെയിനിന്റെ സ്ഥിരം ഓർഡർ, കമ്പനി വേണം. ഒറ്റയ്ക്ക് OPC തുടങ്ങാം. ഭർത്താവിന്റെ പേരിലുള്ള വീടും ഓഫീസ് ആക്കാം: വീട്ടുടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും മതി.",
 cap_en="A solo spice seller in Kerala posts packs to customers in Europe, and a shop chain wants regular orders from a company. She can register a One Person Company, with her husband's house as the registered office using his NOC as owner and a recent utility bill.",
 cap_mg="Europe-lekku spice parcel ottaykku ayakkunna aalkku shop chain-inte regular order, company venam. Ottaykku OPC thudangaam. Bharthavinte perilulla veedum office aakkam: owner NOC-um puthiya utility bill-um mathi.")

# chat: Gokul builds a Malayalam crossword app alone as an OPC; ten months, no revenue; his friend Nithin reminds him of annual filing.
chat("c973", "solo", "C", "മലയാളം ക്രോസ്‌വേഡ് ആപ്പ്.\nOPC ആയിട്ട് 10 മാസം.\nവരുമാനം: പൂജ്യം", ("ഗോകുൽ", "നിതിൻ"), [
 (0,"ഡാ, ആപ്പിന് പതിനായിരം ഡൗൺലോഡ്! പക്ഷേ ഇതുവരെ ഒരു രൂപ വരുമാനം ഇല്ല."),
 (1,"ഡൗൺലോഡ് ആദ്യം, പൈസ പിന്നെ. അത് സാധാരണയാ. കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ആലോചിച്ചോ?"),
 (0,"വരുമാനം ഇല്ലാത്ത കമ്പനിക്ക് എന്ത് ഫയലിംഗ്? ഞാൻ ഒറ്റയ്ക്കുള്ള OPC അല്ലേ."),
 (1,"വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം. OPC ആയാലും."),
 (1,"വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ."),
 (0,"ഒരു ദിവസം നൂറ്. ഒരു മാസം… ഇത് ക്രോസ്‌വേഡിനേക്കാൾ കഠിനമാണല്ലോ."),
 (1,"ഉത്തരം എളുപ്പം. ഡ്യൂ ഡേറ്റ് കലണ്ടറിൽ, ഒരു ഓഡിറ്റർ കൂടെ."),
 (0,"ശരി. അടുത്ത പസിലിന്റെ ഉത്തരം: ആനുവൽ ഫയലിംഗ്!")],
 "വരുമാനം ഇല്ലെങ്കിലും\nOPC ഫയൽ ചെയ്യണം", CTA_AFTER,
 cap_ml="ഒറ്റയ്ക്ക് മലയാളം ക്രോസ്‌വേഡ് ആപ്പ് ഉണ്ടാക്കിയ ഡെവലപ്പറുടെ OPC-ക്ക് 10 മാസം, ഡൗൺലോഡ് ഉണ്ട്, വരുമാനം ഇല്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും വൺ പേഴ്സൺ കമ്പനിയും ആനുവൽ ഫയലിംഗ് ചെയ്യണം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.",
 cap_en="A solo developer in Kerala built a Malayalam crossword app as a One Person Company; ten months in, plenty of downloads, zero revenue. An OPC still has to do its annual filings with zero revenue, and late filing costs Rs 100 per day per form.",
 cap_mg="Ottaykku Malayalam crossword app undaakkiya developer-nte OPC-kku 10 maasam, downloads undu, revenue illa. Zero revenue aanenkilum one person company-um annual filing cheyyanam. Vaikiyal oro form-inum divasam 100 roopa.")

lst("l972", "solo", "C", "ഒറ്റയ്ക്കാണോ?\nOPC-യെ കുറിച്ച്\nഅറിയേണ്ട 3 കാര്യം", [
 ("പാർട്ണർ വേണ്ട", "ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി. ഉടമയും ഡയറക്ടറും നിങ്ങൾ തന്നെ."),
 ("വലിയ ഓഫീസ് വേണ്ട", "വീടും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം: ഉടമയുടെ NOC, പുതിയ യൂട്ടിലിറ്റി ബില്ല്."),
 ("ഡേറ്റുകൾ മറക്കരുത്", "30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A, വരുമാനം ഇല്ലെങ്കിലും ആനുവൽ ഫയലിംഗ്.")],
 "ഒറ്റയ്ക്കും\nകമ്പനി ആകാം", CTA_START,
 cap_ml="ഒറ്റയ്ക്ക് ബിസിനസ് ചെയ്യുന്നവർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC): പാർട്ണർ വേണ്ട, വീട് ഓഫീസ് ആക്കാം (ഉടമയുടെ NOC, പുതിയ ബില്ല്), പക്ഷേ ഓഡിറ്റർ 30 ദിവസത്തിൽ, INC-20A 180 ദിവസത്തിൽ, ആനുവൽ ഫയലിംഗ് എല്ലാ വർഷവും.",
 cap_en="Running your business alone in Kerala? A One Person Company (OPC) needs no partner and can use your home as its registered office, but it still has the 30-day auditor, the 180-day INC-20A and annual filings even with zero revenue.",
 cap_mg="Ottaykku business cheyyunnavarkku one person company (OPC): partner venda, veedu office aakkam (owner NOC, puthiya bill), pakshe auditor 30 days-il, INC-20A 180 days-il, annual filing ella varshavum.")
