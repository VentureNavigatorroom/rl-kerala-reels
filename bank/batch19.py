# Script bank, batch 19. New situations: a stationery shop in a church-trust building with a year of notebooks for six schools, a
# banana grower a baby-food startup wants 20% of, a fish-cleaning service a hotel chain wants in ten days, a halwa maker at day 24
# with a supermarket chain, a two-lorry haulier at day 140 whose cement client asks for INC-20A, a modest-fashion boutique whose
# daughter in Toronto wants in, a "shop to company: three questions" list; a Sharjah plumber who thinks NRIs can only hold shares,
# a man flying back to Jeddah ten days after incorporation, a Doha accountant's online tuition named after a famous university,
# retired parents whose UAE son wants the family house as a homestay company's office, a Riyadh worker saving for 50 lakh before
# a cold-storage company, a Dubai mall couple's abaya brand at day 172, a London engineer's two-year-old idle company; a retired
# rubber-seedling grower alone, a tailor who wants a famous suiting brand's name, a natural-dye scarf weaver with a Japanese buyer,
# a homestay that stayed empty all monsoon, a saree pre-pleating artist who rents the room above the textile shop, an underwater
# photographer at day 179.
# Same fact list and no-price rule as batch01. Segments proprietor 7, nri 7, solo 6; 16 duo3d in 16 different locations (none used
# in batch18; all the least used except the five Gulf places NRI stories need). Proprietor scripts again open on money waiting on
# the table (the d401 pattern); share kept at 7/40, no audience-led shift (INSIGHTS.md run 8).
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
# shop: Binu + Suresh. Suresh's stationery shop gets a school group's yearly notebook order for six schools, company only; the building belongs to a church trust.
duo("d2101", "proprietor", "C", "shop", "6 സ്കൂളിന് ഒരു വർഷത്തെ\nനോട്ട്ബുക്ക്. കട\nപള്ളിയുടെ കെട്ടിടത്തിൽ", [
 ("A","wide","സുരേഷേ, ഇന്ന് കടയിൽ എന്താ ഇത്ര തിരക്ക്? സ്കൂൾ തുറക്കാൻ ഇനിയും മാസങ്ങളുണ്ടല്ലോ."),
 ("V","V","ബിനൂ, ഒരു സ്കൂൾ ഗ്രൂപ്പ് വിളിച്ചു. ആറ് സ്കൂളിനും ഒരു വർഷത്തെ നോട്ട്ബുക്കും സ്റ്റേഷനറിയും നമ്മുടെ കടയിൽ നിന്ന്!"),
 ("A","A","ലോട്ടറി അടിച്ചല്ലോ! എന്താ ഇനി?"),
 ("V","V","കരാർ കമ്പനിയുമായി മാത്രം. പക്ഷേ കമ്പനിക്ക് ഓഫീസ് വേണ്ടേ? ഈ കെട്ടിടം പള്ളി ട്രസ്റ്റിന്റേതാ."),
 ("A","wide","ഈ കട തന്നെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. കെട്ടിട ഉടമയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും മതി."),
 ("V","V","അപ്പോ ട്രസ്റ്റ് സെക്രട്ടറിയുടെ ഒപ്പ് വേണം. അച്ചൻ ഞായറാഴ്ചയേ ഫ്രീ ആകൂ."),
 ("A","A","എങ്കിൽ ഞായറാഴ്ച കുർബാന കഴിഞ്ഞ് NOC. തിങ്കളാഴ്ച ബാക്കി പേപ്പറുകൾ."),
 ("V","wide","ശരി. ആദ്യത്തെ നോട്ട്ബുക്ക് അച്ചന്. കണക്കെഴുതാൻ!")],
 "വാടക കടയും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="സ്റ്റേഷനറി കട നടത്തുന്നയാൾക്ക് ആറ് സ്കൂളുകളുടെ ഒരു വർഷത്തെ നോട്ട്ബുക്ക് ഓർഡർ, കമ്പനിയുമായി മാത്രം കരാർ; കട പള്ളി ട്രസ്റ്റിന്റെ കെട്ടിടത്തിൽ. കെട്ടിട ഉടമയുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ വാടക കട തന്നെ കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.",
 cap_en="A Kerala stationery shop wins a school group's yearly notebook order for six schools, but the contract is only with a company and the shop sits in a church trust's building. With the building owner's NOC and a recent electricity bill, the rented shop itself can be the registered office.",
 cap_mg="Stationery kada nadathunna aalkku 6 school-ukalude oru varshathe notebook order, company-yumaayi maathram contract; kada palli trust-nte building-il. Building owner-nte NOC-um puthiya current bill-um undenkil vaadaka kada thanne company-yude registered office aakkaam.")

# farm: Vasu + Gopi. A baby-food startup wants Gopi's nendran supply locked in and offers money for 20% of his farm business.
duo("d2102", "proprietor", "A", "farm", "ബേബി ഫുഡ് സ്റ്റാർട്ടപ്പ്:\n\"നിന്റെ നേന്ത്രക്കായ\nബിസിനസിൽ 20% തരൂ\"", [
 ("A","wide","ഗോപീ, ആ കാറിൽ വന്ന ചെറുപ്പക്കാർ ആരാ? കുല മുഴുവൻ ഫോട്ടോ എടുത്തല്ലോ."),
 ("V","V","വാസുവേട്ടാ, കുട്ടികളുടെ ബേബി ഫുഡ് ഉണ്ടാക്കുന്ന ഒരു സ്റ്റാർട്ടപ്പ്. നമ്മുടെ നേന്ത്രക്കായ മുഴുവൻ അവർക്ക് വേണം."),
 ("V","V","അതും എല്ലാ വർഷവും. പകരം എന്റെ ബിസിനസിൽ പൈസ ഇട്ട് ഇരുപത് ശതമാനം ഷെയർ എടുക്കാമെന്ന്."),
 ("A","A","ഷെയറോ? നിന്റെ കൃഷി നിന്റെ പേരിൽ അല്ലേ? അതിന് ഷെയർ ഉണ്ടോ?"),
 ("A","wide","ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിനും പാർട്ണർഷിപ്പിനും LLP-ക്കും പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം എന്റെ തോട്ടം ഒരു കമ്പനി ആകണം."),
 ("A","A","അതേ. രണ്ട് ഡയറക്ടർ വേണം. നിന്റെ മോൻ കൃഷി ഓഫീസിൽ പോയി പഠിക്കുന്നില്ലേ? അവനെ കൂട്ട്."),
 ("V","wide","ശരി. വാഴക്കുലയ്ക്ക് ഇനി ബോർഡ് മീറ്റിംഗ്!")],
 "ഷെയർ ചോദിച്ചാൽ\nകൃഷിയും കമ്പനി ആകണം", CTA_START,
 cap_ml="നേന്ത്രവാഴ കൃഷി ചെയ്യുന്ന കർഷകന്റെ കായ മുഴുവൻ വാങ്ങാൻ ഒരു ബേബി ഫുഡ് സ്റ്റാർട്ടപ്പ് റെഡി, പകരം ബിസിനസിൽ പൈസ ഇട്ട് 20% ഷെയർ. പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും ഷെയർ കൊടുക്കാൻ പറ്റില്ല; ഇക്വിറ്റി ഇൻവെസ്റ്റ്മെന്റിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി മാത്രം.",
 cap_en="A Kerala banana farmer is offered a yearly buy-back by a baby-food startup that also wants to invest for 20% of his business. A proprietorship, partnership or LLP cannot issue shares; only a private limited company can take equity investment, so the farm becomes a Pvt Ltd first.",
 cap_mg="Nendran vaazha krishi cheyyunna karshakante kaaya muzhuvan vaangaan oru baby food startup ready, pakaram business-il paisa ittu 20% share. Proprietorship-num LLP-kkum share kodukkan pattilla; equity investment-nu Pvt Ltd company maathram.")

# fishmarket: Suma + Antony. A hotel chain wants Antony's cleaned and cut fish for eight hotels, from a company, starting in ten days.
duo("d2103", "proprietor", "A", "fishmarket", "8 ഹോട്ടലിന് ദിവസവും\nവൃത്തിയാക്കിയ മീൻ.\n\"പത്ത് ദിവസത്തിൽ തുടങ്ങണം\"", [
 ("A","wide","ആന്റണിച്ചേട്ടാ, ഇന്ന് കത്തിക്ക് മൂർച്ച കൂടുതലാണല്ലോ. എന്താ വിശേഷം?"),
 ("V","V","സുമേ, ഹോട്ടൽ ചെയിനിന്റെ ഷെഫ് വന്നിരുന്നു. എട്ട് ഹോട്ടലിനും വൃത്തിയാക്കി മുറിച്ച മീൻ ദിവസവും നമ്മൾ."),
 ("A","A","കർത്താവേ! എന്ന് തുടങ്ങണം?"),
 ("V","V","പത്ത് ദിവസത്തിൽ. പക്ഷേ ബില്ല് കമ്പനി പേരിൽ മാത്രം. ഒരാഴ്ച കൊണ്ട് കമ്പനി ആക്കിയാൽ മതിയല്ലോ."),
 ("A","wide","അത് നടക്കില്ല. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","ഇന്ന് തന്നെ ഡോക്യുമെന്റ്സ് കൊടുക്ക്. ഷെഫിനോട് സത്യം പറഞ്ഞ് രണ്ടാഴ്ച കൂടി ചോദിക്ക്."),
 ("V","V","ഷെഫ് നല്ല മനുഷ്യനാ. നമ്മുടെ കരിമീൻ കഴിച്ച ആളാ, കാത്തിരിക്കും."),
 ("A","wide","എങ്കിൽ ഇന്ന് മീൻ നേരത്തെ തീർക്കാം. ഉച്ചയ്ക്ക് പേപ്പർ പണി!")],
 "കമ്പനിക്ക് 7-15\nപ്രവൃത്തി ദിവസം", CTA_DOCS,
 cap_ml="മീൻ മാർക്കറ്റിൽ മീൻ വൃത്തിയാക്കി മുറിച്ച് കൊടുക്കുന്നയാൾക്ക് എട്ട് ഹോട്ടലുകളിലേക്ക് ദിവസവും സപ്ലൈ ചെയ്യാനുള്ള ഓർഡർ, പത്ത് ദിവസത്തിൽ തുടങ്ങണം, ബില്ല് കമ്പനി പേരിൽ. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; ഇന്ന് തന്നെ ഡോക്യുമെന്റ്സ്.",
 cap_en="A fish-cleaning stall in a Kerala market is asked to supply cleaned, cut fish to eight hotels daily, starting in ten days and billed by a company. Private limited company registration usually takes 7-15 working days, so file the documents today and ask the hotel for a little more time.",
 cap_mg="Meen market-il meen vrithiyaakki murichu kodukkunna aalkku 8 hotel-ukalilekku divasavum supply cheyyaanulla order, 10 divasathil thudanganam, bill company peril. Pvt Ltd register cheyyan saadharana 7-15 working days; innu thanne documents.")

# bakery: Jisha + Sabu. A supermarket chain stocks Sabu's Kozhikode halwa from next month; his company is 24 days old with no auditor.
duo("d2104", "proprietor", "B", "bakery", "ഹൽവ സൂപ്പർമാർക്കറ്റിലേക്ക്.\nകമ്പനിക്ക് 24 ദിവസം.\nഓഡിറ്റർ?", [
 ("A","wide","സാബുച്ചേട്ടാ, ഹൽവ പാക്ക് ചെയ്യുന്ന കവറിൽ ഇതെന്താ പുതിയ ലോഗോ?"),
 ("V","V","ജിഷേ, കമ്പനിയുടെ ലോഗോ! അടുത്ത മാസം മുതൽ ആ സൂപ്പർമാർക്കറ്റ് ചെയിനിൽ നമ്മുടെ ഹൽവ."),
 ("A","A","കമ്പനി എന്ന് രജിസ്റ്റർ ആയി?"),
 ("V","V","ഇരുപത്തിനാല് ദിവസം മുമ്പ്. ഇനി ഹൽവ ഇളക്കിയാൽ മാത്രം മതി."),
 ("A","wide","ഇളക്കുന്നതിന് മുമ്പ് ഒരു കാര്യം. ആദ്യത്തെ ഓഡിറ്ററെ മുപ്പത് ദിവസത്തിനുള്ളിൽ നിയമിക്കണം."),
 ("V","V","അയ്യോ, ഇനി ആറ് ദിവസമേ ഉള്ളൂ!"),
 ("A","A","അതുകൊണ്ട് ഇന്ന് തന്നെ വിളിക്ക്. സൂപ്പർമാർക്കറ്റും ആദ്യം ചോദിക്കുന്നത് പേപ്പറുകൾ ആയിരിക്കും."),
 ("V","wide","ശരി. ഓഡിറ്റർ വരുമ്പോൾ ഒരു കഷണം ഹൽവ. കണക്ക് മധുരമാകട്ടെ!")],
 "ഓർഡറിനൊപ്പം\n30 ദിവസത്തെ കണക്ക്", CTA_AFTER,
 cap_ml="കോഴിക്കോടൻ ഹൽവ ഉണ്ടാക്കുന്ന ബേക്കറിക്കാരന്റെ ഹൽവ അടുത്ത മാസം മുതൽ സൂപ്പർമാർക്കറ്റ് ചെയിനിൽ; കമ്പനിക്ക് 24 ദിവസം, ഓഡിറ്റർ ഇല്ല. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം.",
 cap_en="A Kerala baker's Kozhikode halwa goes into a supermarket chain next month, and his new private limited company is 24 days old with no auditor. The first auditor must be appointed within 30 days of incorporation, so he has six days left.",
 cap_mg="Kozhikodan halwa undaakkunna bakery-kkaarante halwa adutha maasam muthal supermarket chain-il; company-kku 24 divasam, auditor illa. Pvt Ltd registration kazhinju 30 divasathinullil first auditor-e appoint cheyyanam.")

# petrolpump: Santhosh + Shibu. Shibu owns two lorries; a cement company offers a 3-year haulage contract and its vendor form asks for INC-20A; company is 140 days old.
duo("d2105", "proprietor", "B", "petrolpump", "സിമന്റ് കമ്പനിയുടെ\n3 വർഷത്തെ കരാർ.\nഫോമിൽ \"INC-20A?\"", [
 ("A","wide","ഷിബൂ, ഫുൾ ടാങ്ക്! രണ്ട് ലോറിയും ഇന്ന് എങ്ങോട്ടാ?"),
 ("V","V","സന്തോഷേ, സിമന്റ് കമ്പനിയുടെ ഗോഡൗണിലേക്ക്. അവർ മൂന്ന് വർഷത്തെ കരാർ തരുന്നു!"),
 ("V","V","പക്ഷേ അവരുടെ വെണ്ടർ ഫോമിൽ ഒരു ചോദ്യം. INC-20A ഫയൽ ചെയ്തോ എന്ന്."),
 ("A","A","നിന്റെ കമ്പനിക്ക് എത്ര ദിവസമായി?"),
 ("V","V","നൂറ്റിനാൽപ്പത്. ഷെയർ പൈസ ഇട്ടു. ഫോം മാത്രം ചെയ്തില്ല."),
 ("A","wide","ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ആ ഫോം നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ വേണം. നിനക്ക് ഇനി നാൽപ്പത് ദിവസം."),
 ("A","A","വിട്ടുപോയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. പിന്നെ ഡയറക്ടർമാർക്ക് ദിവസം ആയിരം രൂപ വേറെയും."),
 ("V","wide","ഇന്ന് ലോഡ് ഇറക്കിയിട്ട് തന്നെ ഫയൽ ചെയ്യാം. കരാറിന് മുമ്പ് ആ ടിക്ക് വേണം!")],
 "വെണ്ടർ ഫോം ചോദിക്കും\nINC-20A", CTA_AFTER,
 cap_ml="രണ്ട് ലോറി ഓടിക്കുന്ന ഉടമയ്ക്ക് സിമന്റ് കമ്പനിയുടെ മൂന്ന് വർഷത്തെ കരാർ; വെണ്ടർ ഫോമിൽ INC-20A ചോദിക്കുന്നു, കമ്പനിക്ക് 140 ദിവസം. INC-20A രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 180 ദിവസത്തിനുള്ളിൽ; വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴയും ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ (പരമാവധി 1 ലക്ഷം).",
 cap_en="A Kerala lorry owner with two trucks is offered a three-year haulage contract by a cement company whose vendor form asks whether INC-20A is filed; his company is 140 days old. The commencement-of-business filing is due within 180 days, or the company pays 50,000 rupees and each officer 1,000 rupees a day, up to 1 lakh.",
 cap_mg="2 lorry odikkunna owner-nu cement company-yude 3 varshathe contract; vendor form-il INC-20A chodikkunnu, company-kku 140 divasam. INC-20A registration kazhinju 180 divasathinullil; vaikiyaal company-kku 50,000 roopa pizhayum director-nu divasam 1,000 roopa (max 1 lakh).")

chat("c1031", "proprietor", "A", "ബുട്ടീക്കിന് ഓൺലൈൻ\nഓർഡർ. ടൊറന്റോയിലെ മകൾ:\n\"ഞാനും ഡയറക്ടർ\"", ("നസ്രിൻ", "ഫാത്തിമ"), [
 (0,"മോളേ, ആ ഓൺലൈൻ ഫാഷൻ സൈറ്റ് വിളിച്ചു. നമ്മുടെ ബുട്ടീക്കിലെ അബായയും ഷോളും എല്ലാ മാസവും വേണമെന്ന്."),
 (1,"ഉമ്മാ! ഞാൻ പറഞ്ഞില്ലേ, ഡിസൈൻ കണ്ടാൽ ആരും വിടില്ലെന്ന്."),
 (0,"പക്ഷേ അവർ കമ്പനിയുമായി മാത്രം കരാർ ഒപ്പിടും. നീ ടൊറന്റോയിൽ, ഞാൻ ഇവിടെ ഒറ്റയ്ക്ക്."),
 (1,"ഞാനും ഡയറക്ടർ ആകാം. NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 (0,"നീ അവിടെ ഇരുന്നോ? എല്ലാ ഡയറക്ടർമാരും നാട്ടിൽ വേണ്ടേ?"),
 (1,"വേണ്ട ഉമ്മാ. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. അത് ഉമ്മ."),
 (0,"അപ്പോ ഞാനും നീയും. രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ."),
 (1,"അതേ. ഡിസൈൻ മീറ്റിംഗ് വീഡിയോ കോളിൽ. ഉമ്മയുടെ ചായ മാത്രം മിസ്സ് ആകും!")],
 "മകൾ വിദേശത്ത്.\nകമ്പനിയിൽ ഡയറക്ടർ", CTA_START,
 cap_ml="അബായയും ഷോളും വിൽക്കുന്ന ബുട്ടീക്കിന് ഓൺലൈൻ ഫാഷൻ സൈറ്റിന്റെ മാസ ഓർഡർ, കരാർ കമ്പനിയുമായി മാത്രം; മകൾ ടൊറന്റോയിൽ. NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം; ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി.",
 cap_en="A Kerala boutique selling abayas and shawls gets a monthly order from an online fashion site that signs only with companies, while the owner's daughter lives in Toronto. An NRI can be a director and shareholder of an Indian private limited company, as long as one director is resident in India.",
 cap_mg="Abaya-um shawl-um vilkkunna boutique-nu online fashion site-nte maasa order, contract company-yumaayi maathram; makal Toronto-il. NRI-kku Indian Pvt Ltd-il director-um shareholder-um aakaam; oru director India-yil thaamasikkunna aal aayaal mathi.")

lst("l1031", "proprietor", "B", "കടയെ കമ്പനിയാക്കും\nമുമ്പ് സ്വയം ചോദിക്കേണ്ട\n3 ചോദ്യം", [
 ("രണ്ടാമത്തെ ഡയറക്ടർ ആര്?", "Pvt Ltd-ന് കുറഞ്ഞത് 2 ഡയറക്ടറും 2 ഷെയർഹോൾഡറും. ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ."),
 ("കടയുടെ പേര് കിട്ടുമോ?", "നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിലോ ട്രേഡ്മാർക്ക് ക്ലാഷ് ആയാലോ റിജക്ട് ആകും."),
 ("നാളെ ഇൻവെസ്റ്റർ വന്നാലോ?", "ഷെയർ കൊടുത്ത് ഇൻവെസ്റ്റ്മെന്റ് എടുക്കാൻ Pvt Ltd-ന് മാത്രമേ പറ്റൂ.")],
 "ഉത്തരം അറിഞ്ഞിട്ട്\nരജിസ്ട്രേഷൻ", CTA_START,
 cap_ml="വർഷങ്ങളായി നടത്തുന്ന കട പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി ആക്കാൻ ആലോചിക്കുന്നവർ ആദ്യം ചോദിക്കേണ്ട മൂന്ന് ചോദ്യങ്ങൾ: രണ്ടാമത്തെ ഡയറക്ടർ, കടയുടെ പേര് കിട്ടുമോ, ഇൻവെസ്റ്റർ വന്നാൽ ഷെയർ കൊടുക്കാൻ പറ്റുമോ.",
 cap_en="Turning your family shop in Kerala into a private limited company? Ask three questions first: who is the second director, will the shop's name pass the similarity and trademark check, and can you give shares if an investor walks in tomorrow.",
 cap_mg="Varshangalaayi nadathunna kada Pvt Ltd company aakkaan aalochikkunnavar aadyam chodikkenda 3 chodyangal: randaamathe director, kadayude peru kittumo, investor vannaal share kodukkan pattumo.")

# ---------------- nri ----------------
# gulf: Shiju + Faisal. Faisal, a plumber in Sharjah, plans a plumbing-service company in Kollam with two cousins; he thinks an NRI can only hold shares.
duo("d2106", "nri", "A", "gulf", "ഷാർജയിൽ പ്ലംബർ.\nകൊല്ലത്ത് കമ്പനി.\n\"NRI-ക്ക് ഷെയർ മാത്രം\"", [
 ("A","wide","ഫൈസലേ, ഡ്യൂട്ടി കഴിഞ്ഞിട്ടും ഫോണിൽ എന്താ ഇത്ര കണക്ക്?"),
 ("V","V","ഷിജൂ, കൊല്ലത്ത് ഒരു പ്ലംബിംഗ് സർവീസ് കമ്പനി. എന്റെ രണ്ട് കസിൻസ് അവിടെ പണി നോക്കും. ഫ്ലാറ്റുകളുടെ കരാർ കിട്ടും."),
 ("A","A","കൊള്ളാം. നീ അതിൽ എന്താ?"),
 ("V","V","ഞാൻ പൈസ ഇടും, ഷെയർ മാത്രം. NRI-ക്ക് ഡയറക്ടർ ആകാൻ പറ്റില്ലല്ലോ."),
 ("A","wide","ആര് പറഞ്ഞു? NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം."),
 ("A","A","ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളായാൽ മതി. നിന്റെ കസിൻസ് ഉണ്ടല്ലോ."),
 ("V","V","അപ്പോ ഞാനും ഡയറക്ടർ! ഇവിടെ പൈപ്പ് നന്നാക്കുന്നവൻ അവിടെ ബോർഡിൽ."),
 ("A","wide","ബോർഡ് മീറ്റിംഗിൽ ലീക്ക് ഉണ്ടാകില്ലെന്ന് ഉറപ്പ്!")],
 "ഗൾഫിൽ ഇരുന്നും\nഡയറക്ടർ ആകാം", CTA_START,
 cap_ml="ഷാർജയിൽ പ്ലംബറായി ജോലി ചെയ്യുന്ന പ്രവാസി കൊല്ലത്ത് കസിൻസുമായി പ്ലംബിംഗ് സർവീസ് കമ്പനി തുടങ്ങുന്നു; NRI-ക്ക് ഷെയർ മാത്രമേ പറ്റൂ എന്ന് കരുതി. NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഷെയർഹോൾഡറും ഡയറക്ടറും ആകാം; ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി.",
 cap_en="A plumber in Sharjah is starting a plumbing-service company in Kollam with two cousins and thinks an NRI can only hold shares. NRIs can be both shareholders and directors of an Indian private limited company; only one director needs to be resident in India.",
 cap_mg="Sharjah-il plumber aayi joli cheyyunna pravaasi Kollam-il cousins-umaayi plumbing service company thudangunnu; NRI-kku share maathrame pattoo ennu karuthi. NRI-kku Indian Pvt Ltd-il shareholder-um director-um aakaam; oru director India-yil thaamasikkunna aal aayaal mathi.")

# airport: Shameer + Rafeeq. Rafeeq flies back to Jeddah tomorrow; his Kerala company is 10 days old; he thinks the auditor can wait until he is home again.
duo("d2107", "nri", "B", "airport", "നാളെ ജിദ്ദയിലേക്ക്.\nകമ്പനിക്ക് 10 ദിവസം.\n\"ബാക്കി വന്നിട്ട്\"", [
 ("A","wide","റഫീഖേ, ബോർഡിംഗ് പാസ് കിട്ടിയോ? ബാഗിന്റെ ഭാരം ഓക്കെ ആണോ?"),
 ("V","V","ഷമീറേ, ഭാരം ഓക്കെ. മനസ്സിൽ മാത്രം ഭാരം. പത്ത് ദിവസം മുമ്പല്ലേ കമ്പനി രജിസ്റ്റർ ആയത്."),
 ("A","A","അതിനെന്താ? അനിയൻ നാട്ടിൽ കട നോക്കുമല്ലോ."),
 ("V","V","ബാക്കി കാര്യങ്ങൾ എട്ട് മാസം കഴിഞ്ഞ് ലീവിന് വന്നിട്ട് ചെയ്യാം എന്ന് വിചാരിച്ചു."),
 ("A","wide","എല്ലാം അങ്ങനെ കാത്തിരിക്കില്ല. ആദ്യത്തെ ഓഡിറ്ററെ കമ്പനി തുടങ്ങി മുപ്പത് ദിവസത്തിനുള്ളിൽ നിയമിക്കണം."),
 ("V","V","മുപ്പതോ? അപ്പോ ഇനി ഇരുപത് ദിവസം!"),
 ("A","A","അനിയനും ഡയറക്ടർ അല്ലേ? ഗേറ്റിൽ ഇരുന്ന് തന്നെ അവനെ വിളിക്ക്. ഈ ആഴ്ച തന്നെ ഓഡിറ്ററെ കാണാൻ പറ."),
 ("V","wide","ശരി. ഫ്ലൈറ്റ് കയറും മുമ്പ് ഒരു കോൾ. ലാൻഡ് ചെയ്താൽ ഒരു മെസേജ്!")],
 "ലീവ് കഴിഞ്ഞാലും\n30 ദിവസം ഓടും", CTA_AFTER,
 cap_ml="നാട്ടിൽ കമ്പനി രജിസ്റ്റർ ചെയ്ത് പത്ത് ദിവസം കഴിഞ്ഞ് ജിദ്ദയിലേക്ക് തിരിച്ചു പോകുന്ന പ്രവാസി ബാക്കി കാര്യങ്ങൾ അടുത്ത ലീവിന് ചെയ്യാമെന്ന് കരുതി. ആദ്യത്തെ ഓഡിറ്ററെ രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ നിയമിക്കണം; നാട്ടിലുള്ള ഡയറക്ടർ ഈ ആഴ്ച തന്നെ ചെയ്യണം.",
 cap_en="An NRI flying back to Jeddah ten days after registering his Kerala company plans to finish the rest on his next leave in eight months. The first auditor must be appointed within 30 days of incorporation, so the director at home acts this week.",
 cap_mg="Naattil company register cheythu 10 divasam kazhinju Jeddah-ilekku thirichu pokunna pravaasi baakki kaaryangal adutha leave-nu cheyyaam ennu karuthi. First auditor-e registration kazhinju 30 divasathinullil appoint cheyyanam; naattilulla director ee aazhcha thanne cheyyanam.")

# gulfoffice: Shahana + Asif. Asif, an accountant in Doha, starts online tuition for Gulf children and wants a famous university's name in the company name.
duo("d2108", "nri", "C", "gulfoffice", "ദോഹയിൽ അക്കൗണ്ടന്റ്.\nഓൺലൈൻ ട്യൂഷന് പേര്:\nഒരു ലോകപ്രശസ്ത യൂണിവേഴ്സിറ്റി", [
 ("A","wide","ആസിഫ്, ലഞ്ച് ബ്രേക്കിൽ പോലും ഈ സ്ലൈഡുകൾ എന്താ?"),
 ("V","V","ഷഹാനാ, ഗൾഫിലെ മലയാളി കുട്ടികൾക്ക് ഓൺലൈൻ കണക്ക് ട്യൂഷൻ. കമ്പനി നാട്ടിൽ, ടീച്ചർമാർ നാട്ടിൽ."),
 ("A","A","നല്ല ഐഡിയ. പേര് ആലോചിച്ചോ?"),
 ("V","V","ആ ലോകപ്രശസ്ത ഇംഗ്ലീഷ് യൂണിവേഴ്സിറ്റിയുടെ പേര്, പിന്നെ ട്യൂഷൻ. രക്ഷിതാക്കൾ കണ്ടാൽ ഉടനെ ചേർക്കും."),
 ("A","wide","രജിസ്ട്രാർ കണ്ടാൽ ഉടനെ റിജക്ട് ചെയ്യും. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് കിട്ടില്ല."),
 ("A","A","നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉള്ളതും റിജക്ട് ആകും."),
 ("V","V","എങ്കിൽ നമ്മുടെ നാടിന്റെ പേര് ചേർത്ത് ഒന്ന്. കണക്കിന് ഒരു മലയാളം വാക്ക്."),
 ("A","wide","അതാണ് നല്ലത്. മൂന്ന് പേര് എഴുതി വെക്ക്. ഒന്ന് ഉറപ്പായും കിട്ടും.")],
 "പ്രശസ്തമായ പേര്\nകടം വാങ്ങരുത്", CTA_NAME,
 cap_ml="ദോഹയിൽ അക്കൗണ്ടന്റായ പ്രവാസി ഗൾഫിലെ മലയാളി കുട്ടികൾക്കായി ഓൺലൈൻ ട്യൂഷൻ കമ്പനി കേരളത്തിൽ തുടങ്ങുന്നു; പേരിൽ ഒരു ലോകപ്രശസ്ത യൂണിവേഴ്സിറ്റിയുടെ പേര് വേണം. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്നതോ നിലവിലുള്ള കമ്പനിയോട് സാമ്യമുള്ളതോ ആയ പേര് റിജക്ട് ആകും.",
 cap_en="An accountant in Doha is starting a Kerala company that tutors Gulf Malayali children online, and wants a world-famous university's name in it. A company name that clashes with a trademark or resembles an existing company is rejected, so write three original options.",
 cap_mg="Doha-il accountant aaya pravaasi Gulf-ile Malayali kuttikalkku online tuition company Kerala-il thudangunnu; peril oru world famous university-yude peru venam. Trademark-umaayi clash aakunnatho ippozhulla company-yodu saamyam ullatho aaya peru reject aakum.")

# veranda: Shantha + Balan. Their son in the UAE wants a homestay company with the family house as its office; the house is in Balan's name.
duo("d2109", "nri", "C", "veranda", "മകൻ യുഎഇയിൽ.\nതറവാട് ഹോംസ്റ്റേ കമ്പനി.\nഅച്ഛന്റെ ഒരു ഒപ്പ്", [
 ("A","wide","ബാലേട്ടാ, മോൻ വീഡിയോ കോളിൽ ഇപ്പോഴും ഈ വരാന്ത കാണിച്ചു തരാൻ പറഞ്ഞു."),
 ("V","V","ശാന്തേ, അവന്റെ പ്ലാൻ കേട്ടില്ലേ? നമ്മുടെ തറവാട് ഹോംസ്റ്റേ. വിദേശികൾ ഈ വരാന്തയിൽ ഇരിക്കും."),
 ("A","A","അവൻ ദുബായിൽ ഇരുന്ന് കമ്പനി തുടങ്ങും. പക്ഷേ ഓഫീസ് എവിടെ?"),
 ("V","V","അതാ എനിക്ക് മനസ്സിലാകാത്തത്. ടൗണിൽ മുറി എടുക്കണം എന്നാ ഞാൻ വിചാരിച്ചത്."),
 ("A","wide","വേണ്ടെന്ന് അവൻ പറഞ്ഞു. ഈ വീട് തന്നെ കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം."),
 ("A","A","വീട് നിങ്ങളുടെ പേരിൽ അല്ലേ? നിങ്ങളുടെ NOC-യും പുതിയ കറന്റ് ബില്ലും മതി."),
 ("V","V","അപ്പോ എന്റെ ഒരു ഒപ്പ് കൊണ്ട് മോന്റെ കമ്പനിക്ക് ഓഫീസ്!"),
 ("A","wide","ഒപ്പിടും മുമ്പ് കണ്ണട വെക്ക്. കറന്റ് ബില്ലും തപ്പി എടുക്ക്!")],
 "തറവാടും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="യുഎഇയിലുള്ള മകൻ നാട്ടിലെ തറവാട് വീട് ഹോംസ്റ്റേ കമ്പനി ആക്കാൻ ആലോചിക്കുന്നു; വീട് അച്ഛന്റെ പേരിൽ. ഉടമയായ അച്ഛന്റെ NOC-യും പുതിയ കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ ഈ വീട് തന്നെ കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം; ടൗണിൽ മുറി വേണ്ട.",
 cap_en="An NRI son in the UAE wants to turn the family tharavad in Kerala into a homestay company, and the house is in his father's name. With the father's NOC as owner and a recent electricity bill, the house itself can be the company's registered office, no town office needed.",
 cap_mg="UAE-ilulla makan naattile tharavaadu veedu homestay company aakkaan aalochikkunnu; veedu achante peril. Udamayaaya achante NOC-um puthiya current bill-um undenkil ee veedu thanne company-yude registered office aakkaam; town-il muri venda.")

# gulfroom: Naseer + Shamsu. Shamsu in Riyadh wants a cold-storage company in Malappuram but thinks he must save 50 lakh before he can even register.
duo("d2110", "nri", "A", "gulfroom", "റിയാദിൽ മൂന്ന് വർഷം\nസേവ് ചെയ്യുന്നു.\n\"50 ലക്ഷം ആയിട്ട് കമ്പനി\"", [
 ("A","wide","ഷംസൂ, ഈ ഡയറിയിൽ എന്താ എഴുതുന്നത്? പ്രേമലേഖനം ആണോ?"),
 ("V","V","നസീർക്കാ, ഇത് എന്റെ സേവിംഗ്സ് കണക്ക്. മലപ്പുറത്ത് ഒരു കോൾഡ് സ്റ്റോറേജ്. പച്ചക്കറിക്കാർക്ക് വേണ്ടി."),
 ("A","A","നല്ല പ്ലാൻ. എന്നാ തുടങ്ങുന്നത്?"),
 ("V","V","അമ്പത് ലക്ഷം ആയിട്ട്. അത്രയും ഇല്ലാതെ കമ്പനി രജിസ്റ്റർ ചെയ്യാൻ പറ്റില്ലല്ലോ."),
 ("A","wide","അത് തെറ്റാണ്. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല."),
 ("A","A","കമ്പനി ഇപ്പോൾ തന്നെ തുടങ്ങാം. കെട്ടിടവും മെഷീനും പൈസ ആകുന്ന മുറയ്ക്ക്."),
 ("V","V","അപ്പോ ഞാൻ മൂന്ന് വർഷം കാത്തിരുന്നത് വെറുതെ!"),
 ("A","wide","വെറുതെ അല്ല, ആ പൈസ ബിസിനസിന് വേണം. പക്ഷേ കമ്പനിക്ക് കാത്തിരിക്കണ്ട.")],
 "കമ്പനിക്ക് മുമ്പ്\nലക്ഷങ്ങൾ വേണ്ട", CTA_START,
 cap_ml="റിയാദിൽ ജോലി ചെയ്യുന്ന പ്രവാസി മലപ്പുറത്ത് കോൾഡ് സ്റ്റോറേജ് കമ്പനി തുടങ്ങാൻ 50 ലക്ഷം സേവ് ആകുന്നത് വരെ കാത്തിരിക്കുന്നു. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല; NRI-ക്ക് ഇപ്പോൾ തന്നെ കമ്പനി രജിസ്റ്റർ ചെയ്യാം.",
 cap_en="A worker in Riyadh has been saving for three years and plans to register his Malappuram cold-storage company only after he reaches 50 lakh. A private limited company has no minimum paid-up capital, so the company can be registered now and funded as the business grows.",
 cap_mg="Riyadh-il joli cheyyunna pravaasi Malappuram-il cold storage company thudangaan 50 lakh save aakunnathu vare kaathirikkunnu. Pvt Ltd company-kku minimum paid-up capital illa; NRI-kku ippo thanne company register cheyyaam.")

# mall: Sumayya + Jafar. A Dubai mall couple's abaya brand company in Kerala is 172 days old; they plan to "commence" next leave.
duo("d2111", "nri", "B", "mall", "ദുബായ് മാളിൽ ജോലി.\nനാട്ടിൽ അബായ ബ്രാൻഡ്.\nകമ്പനിക്ക് 172 ദിവസം", [
 ("A","wide","ജാഫർ, ആ അബായയുടെ ഡിസൈൻ നോക്ക്. നമ്മുടെ ബ്രാൻഡിന് ഇതുപോലെ ഒന്ന് വേണം."),
 ("V","V","സുമയ്യാ, ഡിസൈൻ ഒക്കെ റെഡി. അടുത്ത ലീവിന് നാട്ടിൽ ചെന്ന് ബിസിനസ് തുടങ്ങാം. കമ്പനി ഇപ്പോഴേ ഉണ്ടല്ലോ."),
 ("A","A","കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ട് എത്ര ദിവസമായി?"),
 ("V","V","നൂറ്റിയെഴുപത്തിരണ്ട്. ഷെയർ പൈസ പോലും അക്കൗണ്ടിൽ ഇട്ടിട്ടില്ല."),
 ("A","wide","ജാഫർ! ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന INC-20A നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ വേണം. ഇനി എട്ട് ദിവസം."),
 ("V","V","ലീവ് വരെ കാത്തിരുന്നാൽ?"),
 ("A","A","കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർമാർക്ക് ദിവസം ആയിരം രൂപ, ഒരു ലക്ഷം വരെ."),
 ("V","wide","എങ്കിൽ ഇന്ന് തന്നെ ഷെയർ പൈസ അയക്കാം. നാട്ടിലെ കാര്യങ്ങൾ നോക്കുന്ന ഡയറക്ടറോട് ഫയൽ ചെയ്യാൻ പറയാം.")],
 "ലീവ് വരെ\nINC-20A കാത്തിരിക്കില്ല", CTA_AFTER,
 cap_ml="ദുബായ് മാളിൽ ജോലി ചെയ്യുന്ന ദമ്പതികളുടെ നാട്ടിലെ അബായ ബ്രാൻഡ് കമ്പനിക്ക് 172 ദിവസം; ഷെയർ പൈസ ഇട്ടിട്ടില്ല, അടുത്ത ലീവിന് തുടങ്ങാമെന്ന് കരുതി. INC-20A 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം; ഇല്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴയും ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ (പരമാവധി 1 ലക്ഷം).",
 cap_en="An NRI couple working at a Dubai mall registered a Kerala company for their abaya brand 172 days ago and planned to begin on their next leave. INC-20A is due within 180 days of incorporation; missing it costs the company 50,000 rupees and each officer 1,000 rupees a day, up to 1 lakh.",
 cap_mg="Dubai mall-il joli cheyyunna couple-nte naattile abaya brand company-kku 172 divasam; share paisa ittittilla, adutha leave-nu thudangaam ennu karuthi. INC-20A 180 divasathinullil file cheyyanam; illenkil company-kku 50,000 roopa pizhayum director-nu divasam 1,000 roopa (max 1 lakh).")

chat("c1032", "nri", "C", "ലണ്ടനിൽ എഞ്ചിനീയർ.\nരണ്ട് വർഷം മുമ്പ് കമ്പനി.\nഒരു ഫയലിംഗും ഇല്ല", ("ആദിത്യൻ", "ഗോകുൽ"), [
 (0,"ഗോകുലേ, ഒരു സംശയം. രണ്ട് വർഷം മുമ്പ് നാട്ടിൽ ഒരു ഇവി ചാർജിംഗ് കമ്പനി രജിസ്റ്റർ ചെയ്തത് ഓർമ്മയുണ്ടോ?"),
 (1,"ഉണ്ട്. ലണ്ടനിൽ നിന്ന് വന്ന് തുടങ്ങുമെന്ന് പറഞ്ഞ കമ്പനി. എന്തായി?"),
 (0,"ഒന്നും ആയില്ല. ഒരു രൂപ പോലും വരുമാനം ഇല്ല. അതുകൊണ്ട് ഒന്നും ഫയൽ ചെയ്തില്ല."),
 (1,"അയ്യോ. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 (0,"ഇപ്പോ ചെയ്താൽ മതിയോ?"),
 (1,"ചെയ്യണം, ഇന്ന് തന്നെ തുടങ്ങണം. വൈകിയ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. രണ്ട് വർഷത്തെ ദിവസങ്ങൾ എണ്ണി നോക്ക്."),
 (0,"എണ്ണാൻ പേടിയാകുന്നു. നാട്ടിലെ ഡയറക്ടർ അമ്മാവനെ ഇന്ന് വിളിക്കാം."),
 (1,"അതാ ശരി. ഇനി എല്ലാ വർഷവും കലണ്ടറിൽ ഒരു ചുവന്ന വട്ടം!")],
 "ഉറങ്ങുന്ന കമ്പനിക്കും\nഫയലിംഗ് വേണം", CTA_AFTER,
 cap_ml="ലണ്ടനിൽ ജോലി ചെയ്യുന്ന പ്രവാസി രണ്ട് വർഷം മുമ്പ് നാട്ടിൽ രജിസ്റ്റർ ചെയ്ത കമ്പനിക്ക് ഒരു വരുമാനവും ഇല്ലാത്തതിനാൽ ഒരു ഫയലിംഗും ചെയ്തില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് നിർബന്ധം; വൈകിയ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="An NRI engineer in London registered a Kerala company two years ago, earned nothing and filed nothing. Annual filing with the ROC is required even with zero revenue, and each late form adds 100 rupees per day, so a dormant company still needs its filings.",
 cap_mg="London-il joli cheyyunna pravaasi 2 varsham munpu naattil register cheytha company-kku oru varumaanavum illaathathinaal oru filing-um cheythilla. Varumaanam poojyam aanenkilum annual filing nirbandham; vaikiya oro form-inum divasam 100 roopa late penalty.")

# ---------------- solo ----------------
# rubber: Joy + Thomas. Thomas, retired and alone, grows rubber seedlings; a Karnataka plantation wants 20,000 a year from a company; he thinks a company needs two people.
duo("d2112", "solo", "A", "rubber", "റിട്ടയർ ചെയ്ത് റബ്ബർ തൈ.\nകർണാടകയിൽ നിന്ന് ഓർഡർ.\nകൂടെ ആരുമില്ല", [
 ("A","wide","തോമാച്ചാ, ഈ തൈകൾ എല്ലാം എണ്ണി വെച്ചിരിക്കുന്നത് എന്തിനാ?"),
 ("V","V","ജോയീ, കർണാടകയിലെ ഒരു തോട്ടം വർഷം ഇരുപതിനായിരം തൈ ചോദിച്ചു. പക്ഷേ കമ്പനിയിൽ നിന്ന് മാത്രം വാങ്ങും."),
 ("A","A","എങ്കിൽ കമ്പനി തുടങ്ങിക്കോ. റിട്ടയർ ചെയ്ത മുതലാളി!"),
 ("V","V","കമ്പനിക്ക് രണ്ട് പേര് വേണ്ടേ? മക്കൾ രണ്ടും അമേരിക്കയിൽ. ഭാര്യ പോയിട്ട് മൂന്ന് വർഷം."),
 ("A","wide","ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി ഉണ്ട്. OPC. ഒരാൾ മാത്രം മതി."),
 ("V","V","ഒരാൾ മാത്രം മതിയോ? ഞാനും എന്റെ തൈകളും?"),
 ("A","A","അതേ. ഈ തോട്ടം, ഈ കൈ, ഒരു കമ്പനി. പേപ്പറുകൾ ഞാൻ എടുത്തു തരാം."),
 ("V","wide","എങ്കിൽ ആദ്യത്തെ ഇൻവോയ്സ് കർണാടകയിലേക്ക്. റിട്ടയർമെന്റ് ഇനി വീണ്ടും തുടങ്ങുന്നു!")],
 "ഒറ്റയ്ക്കാണോ?\nOPC തുടങ്ങാം", CTA_START,
 cap_ml="റിട്ടയർ ചെയ്ത ശേഷം റബ്ബർ തൈ വളർത്തുന്നയാൾക്ക് കർണാടകയിലെ തോട്ടത്തിൽ നിന്ന് വർഷം 20,000 തൈയുടെ ഓർഡർ, കമ്പനിയിൽ നിന്ന് മാത്രം; മക്കൾ വിദേശത്ത്, കൂടെ ആരുമില്ല. ഒറ്റയ്ക്കുള്ളവർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം.",
 cap_en="A retired rubber-seedling grower in Kerala gets a yearly order of 20,000 plants from a Karnataka plantation that buys only from companies, and his children live abroad. A solo founder can form a One Person Company (OPC), so he does not need a second person.",
 cap_mg="Retire cheytha shesham rubber thai valarthunna aalkku Karnataka-yile thottathil ninnu varsham 20,000 thai-yude order, company-yil ninnu maathram; makkal videshathu, koode aarumilla. Ottaykkulla aalkku One Person Company (OPC) thudangaam.")

# tailor: Usha + Mohanan. Mohanan, a solo gents' tailor, gets office-uniform orders and wants a famous suiting brand's name for his company.
duo("d2113", "solo", "B", "tailor", "ഒറ്റയ്ക്ക് തയ്യൽക്കട.\nകമ്പനിക്ക് പേര്:\nപ്രശസ്ത സ്യൂട്ടിംഗ് ബ്രാൻഡ്", [
 ("A","wide","മോഹനേട്ടാ, ഈ നൂറ് യൂണിഫോം ഷർട്ട് ആർക്കാ?"),
 ("V","V","ഉഷേ, ഒരു ഐടി കമ്പനിയുടെ സ്റ്റാഫിന്. അവർ കമ്പനി ബില്ല് ചോദിച്ചു. ഞാൻ ഒരു OPC തുടങ്ങുന്നു."),
 ("A","A","നല്ല കാര്യം. പേര്?"),
 ("V","V","ആ വലിയ സ്യൂട്ടിംഗ് ബ്രാൻഡിന്റെ പേര്, പിന്നെ ടെയ്ലേഴ്സ്. ആളുകൾ കണ്ടാൽ വിശ്വസിക്കും."),
 ("A","wide","ആളുകൾ വിശ്വസിക്കും, പക്ഷേ രജിസ്ട്രാർ സമ്മതിക്കില്ല. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് റിജക്ട് ആകും."),
 ("A","A","മുപ്പത് വർഷമായി ഈ നാട്ടിൽ എല്ലാവർക്കും മോഹനേട്ടന്റെ തയ്യൽ അറിയാം. ആ പേര് മതി."),
 ("V","V","എങ്കിൽ എന്റെ അച്ഛന്റെ പഴയ കടയുടെ പേര്. അത് ആരും എടുത്തിട്ടുണ്ടാകില്ല."),
 ("A","wide","അതാണ് പേര്. പക്ഷേ രണ്ട് ബാക്കപ്പ് പേര് കൂടി എഴുതിക്കോ.")],
 "സ്വന്തം പേരാണ്\nനല്ല ബ്രാൻഡ്", CTA_NAME,
 cap_ml="ഒറ്റയ്ക്ക് തയ്യൽക്കട നടത്തുന്നയാൾക്ക് ഐടി കമ്പനിയുടെ യൂണിഫോം ഓർഡർ; OPC-ക്ക് ഒരു പ്രശസ്ത സ്യൂട്ടിംഗ് ബ്രാൻഡിന്റെ പേര് ഇടാൻ നോക്കുന്നു. ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന കമ്പനി പേര് റിജക്ട് ആകും; സ്വന്തം കടയുടെ കഥയുള്ള പേരും ബാക്കപ്പുകളും വെക്കുക.",
 cap_en="A solo gents' tailor in Kerala gets a uniform order from an IT company and wants a famous suiting brand's name for his One Person Company. A name that clashes with a trademark is rejected at registration, so use the name his town already trusts and keep two backups.",
 cap_mg="Ottaykku thayyal kada nadathunna aalkku IT company-yude uniform order; OPC-kku oru famous suiting brand-nte peru idaan nokkunnu. Trademark-umaayi clash aakunna company name reject aakum; swantham kadayude kadha ulla perum backup-um vekkuka.")

# handloom: Leela + Kumar. Leela weaves natural-dye scarves alone; a Japanese buyer's first shipment needs a company invoice in three weeks.
duo("d2114", "solo", "A", "handloom", "പ്രകൃതി നിറത്തിൽ\nഷാൾ. ജപ്പാൻ ബയർ:\n\"3 ആഴ്ചയിൽ ആദ്യ ഷിപ്മെന്റ്\"", [
 ("A","wide","കുമാരേട്ടാ, ഈ മഞ്ഞ നോക്ക്. മഞ്ഞളിൽ മുക്കിയതാ. ജപ്പാനിലെ ബയർക്ക് ഇത് മതിയെന്ന്!"),
 ("V","V","ലീലേ, അഭിനന്ദനങ്ങൾ! എത്ര എണ്ണം?"),
 ("A","A","ആദ്യം ഇരുനൂറ് ഷാൾ, മൂന്ന് ആഴ്ചയിൽ. ബില്ല് കമ്പനി പേരിൽ വേണം. ഞാൻ ഒറ്റയ്ക്കാ നെയ്യുന്നത്."),
 ("V","V","ഒറ്റയ്ക്ക് ആണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി തുടങ്ങാം. പക്ഷേ ഇന്ന് തന്നെ തുടങ്ങണം."),
 ("A","A","ഇന്നോ? ഞാൻ ഷാൾ തീർന്നിട്ട് ചെയ്യാമെന്ന് വിചാരിച്ചു."),
 ("V","wide","രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം. ഷാൾ തീരുമ്പോൾ ബില്ല് റെഡി ആകണ്ടേ?"),
 ("A","A","ശരിയാ. തറിയുടെ ഒരു ഭാഗത്ത് ഷാൾ, മറ്റേ ഭാഗത്ത് പേപ്പർ."),
 ("V","wide","രണ്ടും ഒരേ സമയം. അതാണ് ലീലയുടെ സ്റ്റൈൽ!")],
 "ഷിപ്മെന്റിന് മുമ്പ്\nകമ്പനി റെഡി", CTA_DOCS,
 cap_ml="പ്രകൃതിദത്ത നിറങ്ങളിൽ ഷാൾ നെയ്യുന്ന സ്ത്രീക്ക് ജപ്പാനിലെ ബയറിൽ നിന്ന് 200 ഷാളിന്റെ ഓർഡർ, മൂന്ന് ആഴ്ചയിൽ, ബില്ല് കമ്പനി പേരിൽ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC; രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം, അതുകൊണ്ട് ഇന്ന് തന്നെ തുടങ്ങണം.",
 cap_en="A Kerala weaver who makes natural-dye scarves alone gets a Japanese buyer's first order of 200, due in three weeks and invoiced by a company. A solo founder can form a One Person Company, and since registration usually takes 7-15 working days, the paperwork starts alongside the weaving.",
 cap_mg="Prakruthi niranglil shawl neyyunna sthreekku Japan-ile buyer-il ninnu 200 shawl-nte order, 3 aazhchayil, bill company peril. Ottaykku aanenkil OPC; register cheyyan saadharana 7-15 working days, athukondu innu thanne thudanganam.")

# homestay: Teena + Jomon. Jomon's homestay OPC was formed in April; the monsoon brought zero guests; he thinks there is nothing to file.
duo("d2115", "solo", "C", "homestay", "ഏപ്രിലിൽ OPC.\nമഴക്കാലത്ത് ഒരു\nഅതിഥിയും വന്നില്ല", [
 ("A","wide","ജോമോനേ, മുറ്റം മുഴുവൻ വൃത്തിയാക്കിയല്ലോ. അതിഥികൾ വരുന്നുണ്ടോ?"),
 ("V","V","ടീനേ, ഡിസംബറിൽ ആദ്യത്തെ ബുക്കിംഗ്! ഏപ്രിലിൽ കമ്പനി തുടങ്ങി, പിന്നെ മഴ. ആറ് മാസം ഒരാളും വന്നില്ല."),
 ("A","A","അപ്പോ ഈ വർഷത്തെ കമ്പനി ഫയലിംഗ്?"),
 ("V","V","വരുമാനം ഇല്ലല്ലോ. പിന്നെ എന്ത് ഫയൽ ചെയ്യാൻ? അടുത്ത വർഷം ഒന്നിച്ച് ചെയ്യാം."),
 ("A","wide","അങ്ങനെ പറ്റില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("A","A","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. ഒരു വർഷം വൈകിയാൽ കണക്ക് നോക്ക്."),
 ("V","V","അത് ഒരു സീസണിലെ മുഴുവൻ ബുക്കിംഗ് പോലെ ആകുമല്ലോ!"),
 ("A","wide","അതുകൊണ്ട് ഡേറ്റ് മാർക്ക് ചെയ്യ്. അതിഥി ഇല്ലെങ്കിലും ഫയലിംഗ് ഉണ്ട്.")],
 "അതിഥി ഇല്ലെങ്കിലും\nഫയലിംഗ് ഉണ്ട്", CTA_AFTER,
 cap_ml="ഏപ്രിലിൽ OPC ആയി രജിസ്റ്റർ ചെയ്ത ഹോംസ്റ്റേയിൽ മഴക്കാലം മുഴുവൻ ഒരു അതിഥിയും വന്നില്ല; വരുമാനം ഇല്ലാത്തതിനാൽ ഫയലിംഗ് വേണ്ടെന്ന് കരുതി. വരുമാനം പൂജ്യം ആണെങ്കിലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് നിർബന്ധം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A Kerala homestay owner registered a One Person Company in April, then the monsoon brought no guests for six months, so he planned to skip this year's filing. Annual filing is due even with zero revenue, and every late form costs 100 rupees a day.",
 cap_mg="April-il OPC aayi register cheytha homestay-il mazhakkaalam muzhuvan oru athithiyum vannilla; varumaanam illaathathinaal filing venda ennu karuthi. Varumaanam poojyam aanenkilum company annual filing nirbandham; vaikiyaal oro form-inum divasam 100 roopa late penalty.")

# textile: Ramya + Prakash. Ramya pre-pleats bridal sarees alone in the room she rents above Prakash's textile shop; three bridal stores want her; she thinks she needs a partner.
duo("d2116", "solo", "A", "textile", "വധുവിന്റെ സാരി\nപ്ലീറ്റ് ചെയ്യുന്നത് ഞാൻ.\nമൂന്ന് ബ്രൈഡൽ സ്റ്റോർ വിളിച്ചു", [
 ("V","wide","രമ്യേ, മുകളിലത്തെ മുറിയിൽ നിന്ന് ഇന്നലെ രാത്രി രണ്ട് മണി വരെ ലൈറ്റ് കണ്ടല്ലോ."),
 ("A","A","പ്രകാശേട്ടാ, പത്ത് കല്യാണസാരി പ്രീ-പ്ലീറ്റ് ചെയ്യാനുണ്ടായിരുന്നു. ഇനി മൂന്ന് ബ്രൈഡൽ സ്റ്റോറുകൾ സ്ഥിരമായി വിളിക്കുന്നു."),
 ("V","V","അപ്പോ കമ്പനി ആക്കിക്കൂടേ? അവർക്കും അതാ സൗകര്യം."),
 ("A","A","കമ്പനിക്ക് ഒരു പാർട്ണർ വേണ്ടേ? ഇത് ഞാൻ ഒറ്റയ്ക്ക് ചെയ്യുന്ന പണിയാണ്."),
 ("V","wide","വേണ്ട. ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി തുടങ്ങാം. OPC."),
 ("A","A","ഓഫീസ് ഈ മുറി മതിയോ? ഇത് ചേട്ടന്റെ കെട്ടിടമല്ലേ?"),
 ("V","V","മതി. ഉടമയായ എന്റെ NOC-യും പുതിയ കറന്റ് ബില്ലും. ഒപ്പ് ഞാൻ ഇപ്പോൾ തന്നെ തരാം."),
 ("A","wide","എങ്കിൽ കമ്പനിയുടെ ആദ്യത്തെ പ്ലീറ്റ് ചേട്ടന്റെ മോളുടെ കല്യാണസാരിക്ക്!")],
 "ഒറ്റയ്ക്കുള്ള പണിക്ക്\nOPC", CTA_START,
 cap_ml="കല്യാണസാരികൾ പ്രീ-പ്ലീറ്റ് ചെയ്യുന്ന യുവതിയെ മൂന്ന് ബ്രൈഡൽ സ്റ്റോറുകൾ സ്ഥിരമായി വിളിക്കുന്നു; ടെക്സ്റ്റൈൽ കടയുടെ മുകളിലെ വാടക മുറിയിലാണ് പണി. ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC); കെട്ടിട ഉടമയുടെ NOC-യും കറന്റ് ബില്ലും ഉണ്ടെങ്കിൽ ആ മുറി രജിസ്റ്റേർഡ് ഓഫീസ്.",
 cap_en="A Kerala saree pre-pleating artist working alone from a rented room above a textile shop is in demand at three bridal stores. A solo founder can form a One Person Company (OPC), and with the building owner's NOC and a recent electricity bill, that room can be the registered office.",
 cap_mg="Kalyaana saree pre-pleat cheyyunna yuvathiye 3 bridal store-ukal sthiramaayi vilikkunnu; textile kadayude mukalile vaadaka muriyil aanu pani. Ottaykku aanenkil One Person Company (OPC); building owner-nte NOC-um current bill-um undenkil aa muri registered office.")

chat("c1033", "solo", "A", "കോവളത്ത് അണ്ടർവാട്ടർ\nഫോട്ടോഗ്രാഫർ. OPC-ക്ക്\nനാളെ 180-ാം ദിവസം", ("ആൽബിൻ", "ഡെൽന"), [
 (0,"ഡെൽനാ, ഇന്നത്തെ ഡൈവിൽ ഒരു കടലാമയെ കിട്ടി! ഫോട്ടോ അയക്കാം."),
 (1,"വൗ! പിന്നെ ആൽബിൻ, നിന്റെ OPC രജിസ്റ്റർ ആയത് മേയ് അവസാനം അല്ലേ?"),
 (0,"അതേ. എന്താ?"),
 (1,"ഇന്ന് നൂറ്റിയെഴുപത്തിയൊമ്പതാം ദിവസം. INC-20A ഫയൽ ചെയ്തോ?"),
 (0,"അത് എന്താ? വെള്ളത്തിനടിയിൽ ഇരുന്നപ്പോൾ ഒന്നും കേട്ടില്ല."),
 (1,"ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന ഫോം. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ വേണം. അതായത് നാളെ വരെ."),
 (0,"മിസ്സ് ആയാൽ?"),
 (1,"കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ വേറെ. കര കയറിയാൽ ആദ്യം ഇത്!")],
 "180-ാം ദിവസം\nINC-20A", CTA_AFTER,
 cap_ml="കോവളത്ത് അണ്ടർവാട്ടർ ഫോട്ടോഗ്രാഫറായി ഒറ്റയ്ക്ക് ജോലി ചെയ്യുന്നയാളുടെ OPC-ക്ക് ഇന്ന് 179-ാം ദിവസം; INC-20A ഇതുവരെ ഫയൽ ചെയ്തിട്ടില്ല. ബിസിനസ് തുടങ്ങിയെന്ന് കാണിക്കുന്ന INC-20A 180 ദിവസത്തിനുള്ളിൽ; വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴയും ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ (പരമാവധി 1 ലക്ഷം).",
 cap_en="A solo underwater photographer in Kovalam is at day 179 of his One Person Company and has never heard of INC-20A. The commencement-of-business filing is due within 180 days of incorporation; missing it means a 50,000 rupee penalty on the company plus 1,000 rupees a day for the officer in default.",
 cap_mg="Kovalam-il underwater photographer aayi ottaykku joli cheyyunna aalude OPC-kku innu 179-aam divasam; INC-20A ithuvare file cheythittilla. Business thudangi ennu kaanikkunna INC-20A 180 divasathinullil; vaikiyaal company-kku 50,000 roopa pizhayum director-nu divasam 1,000 roopa (max 1 lakh).")
