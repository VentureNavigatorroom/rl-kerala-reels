# Script bank, batch 10. New situations: a Thrissur bridal-blouse designer told an OPC needs a partner, a TV quiz writer with a
# ten-day season deadline, a coral-survey consultant away on a Lakshadweep ferry with the auditor clock running, an EV-conversion
# designer who wants "Tesla" in her name, a dubbing artist an ad agency wants to invest in, a court transcriptionist at the Akshaya
# centre with no INC-20A, a Kollam aquarium designer whose office is her father's house; a board-game cafe 25 days old, two auto
# drivers building a booking app on "10 lakh capital", corporate-offsite planners a hotel group wants to buy into, a parcel startup
# named "Speed Post Express", private-bus timing app founders with zero revenue, trainers adding a mother "to make it legal", a
# cofounder myths list; a KSEB engineer's pickle brand in his wife's house, an IT employee's wedding photo-booth name, a loco
# pilot's model-train company at four months, a runner who wants "Kochi Marathon" as a name, a side brand paused for maternity
# leave, a sales executive's phone-repair channel.
# Same fact list and no-price rule as batch01. Segments freelancer 7, cofounders 7, salaried 6; 16 duo3d in 16 different locations,
# default names. Every script carries cap_ml / cap_en / cap_mg for Instagram search (captions.py adds hook, CTA and hashtags).
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
# tailor: Usha + Mohanan. Usha designs bridal blouses on Instagram in Thrissur; Mohanan says a company needs a partner, so she plans to "borrow" her cousin.
duo("d1201", "freelancer", "A", "tailor", "ബ്രൈഡൽ ബ്ലൗസ് ഡിസൈനർ.\n\"കമ്പനിക്ക് ഒരു പാർട്ണർ വേണം,\nകസിനെ കടം വാങ്ങാം\"", [
 ("V","wide","ഉഷേ, ഈ ആഴ്ച എത്ര കല്യാണ ബ്ലൗസ്? മെഷീൻ നിർത്താതെ ഓടുകയാണല്ലോ."),
 ("A","A","മോഹനേട്ടാ, പതിനൊന്ന്. ഇൻസ്റ്റയിൽ നിന്ന് മാത്രം. ഇനി ഇത് ഒരു കമ്പനി ആക്കണം."),
 ("V","V","കമ്പനിക്ക് രണ്ടുപേർ വേണ്ടേ? നീ ഒറ്റയ്ക്കല്ലേ ഡിസൈൻ മുഴുവൻ ചെയ്യുന്നത്."),
 ("A","A","അതാ പ്ലാൻ. കസിൻ രേഷ്മയെ കടം വാങ്ങാം. ഒപ്പിടാൻ മാത്രം. തുണി തൊടണ്ട."),
 ("V","V","അവൾ കല്യാണം കഴിഞ്ഞ് ബാംഗ്ലൂരിലല്ലേ? പിന്നെ ഓരോ ഒപ്പിനും നീ അങ്ങോട്ട് ഓടുമോ?"),
 ("A","wide","പിന്നെ എന്ത് ചെയ്യും ചേട്ടാ?"),
 ("V","wide","ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി, OPC. ഒരാൾക്ക് തന്നെ കമ്പനി തുടങ്ങാം."),
 ("A","A","അപ്പോ രേഷ്മയെ തിരിച്ചു കൊടുക്കാം!"),
 ("V","V","കൊടുക്ക്. പകരം അവളുടെ കല്യാണ ബ്ലൗസ് ഫ്രീയായി തയ്ച്ചു കൊടുത്താൽ മതി.")],
 "ഒറ്റയ്ക്കാണോ?\nOPC ഉണ്ട്", CTA_START,
 cap_ml="തൃശൂരിൽ ഇൻസ്റ്റഗ്രാം വഴി ബ്രൈഡൽ ബ്ലൗസ് ഡിസൈൻ ചെയ്യുന്ന ഉഷ കരുതി, കമ്പനി രജിസ്ട്രേഷന് ഒരു പാർട്ണർ നിർബന്ധമാണെന്ന്. ഒറ്റയ്ക്ക് ബിസിനസ് നടത്തുന്നവർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) ആയി രജിസ്റ്റർ ചെയ്യാം. ഒപ്പിടാൻ മാത്രം ഒരാളെ ചേർക്കേണ്ട.",
 cap_en="A bridal blouse designer in Thrissur thought company registration needs a partner, so she planned to add a cousin just to sign. A solo founder can register a One Person Company (OPC) in Kerala. You do not need a name-only partner to start a company.",
 cap_mg="Thrissur-il Instagram vazhi bridal blouse design cheyyunna Usha vicharichu company register cheyyan oru partner venamennu. Ottaykkaanenkil One Person Company (OPC) aayi thudangaam. Sign cheyyan maathram oraale cherkkenda.")

# library: Greeshma + Anoop. Greeshma writes questions for a TV quiz show; the channel signs next season's vendors in ten days, only companies.
duo("d1202", "freelancer", "B", "library", "TV ക്വിസ് ഷോയ്ക്ക്\nചോദ്യം എഴുതുന്നു.\nപുതിയ സീസൺ കരാർ 10 ദിവസത്തിൽ", [
 ("V","wide","ഗ്രീഷ്മേ, ഈ ലൈബ്രറിയിലെ ജനറൽ നോളജ് ഷെൽഫ് മുഴുവൻ നീ ഒറ്റയ്ക്ക് തീർത്തോ?"),
 ("A","A","അനൂപേ, ക്വിസ് ഷോയുടെ പുതിയ സീസൺ. അഞ്ഞൂറ് ചോദ്യം വേണം. പക്ഷേ ചാനലിന് ഒരു പുതിയ റൂൾ."),
 ("V","V","എന്ത് റൂൾ? ഉത്തരം ഓപ്ഷൻ C ആകരുതെന്നോ?"),
 ("A","A","അല്ല. ഇനി വെണ്ടർമാരെല്ലാം കമ്പനി ആയിരിക്കണം. കരാർ ഒപ്പിടുന്നത് പത്ത് ദിവസം കഴിഞ്ഞ്."),
 ("V","V","പത്ത് ദിവസം! പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","അപ്പോ ഇത് ലൈഫ്‌ലൈൻ ഇല്ലാത്ത ചോദ്യമാണ്."),
 ("V","wide","പേര് റിജക്ട് ആയാൽ പിന്നെയും വൈകും. രണ്ടോ മൂന്നോ ബാക്കപ്പ് പേരുകൾ കൂടി കരുതിക്കോ."),
 ("A","A","ശരി. ഇന്ന് തന്നെ ഡോക്യുമെന്റ്സ് എടുക്കാം. ചോദ്യങ്ങൾ രാത്രി എഴുതാം."),
 ("V","wide","ഫൈനൽ ആൻസർ?"),
 ("A","wide","ഫൈനൽ ആൻസർ. ഇന്ന് തന്നെ തുടങ്ങും!")],
 "കരാറിന് മുമ്പ് കമ്പനി.\nഇന്ന് തന്നെ തുടങ്ങൂ", CTA_DOCS,
 cap_ml="ടിവി ക്വിസ് ഷോയ്ക്ക് ചോദ്യം എഴുതുന്ന ഫ്രീലാൻസർക്ക് ചാനലിന്റെ പുതിയ നിബന്ധന: വെണ്ടർ കമ്പനി ആയിരിക്കണം, കരാർ പത്ത് ദിവസത്തിൽ. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം വേണം. ഡോക്യുമെന്റ്സും ബാക്കപ്പ് കമ്പനി പേരുകളും നേരത്തെ റെഡിയാക്കൂ.",
 cap_en="A freelance quiz writer has ten days before a TV channel signs vendors, and it only signs with companies. Private limited company registration usually takes 7 to 15 working days, and a rejected company name adds more. Get your documents and two or three backup names ready before the deadline.",
 cap_mg="TV quiz show-nu question ezhuthunna freelancer-nu channel paranju vendor company aayirikkanam, contract 10 divasathil. Pvt Ltd register cheyyan saadharana 7-15 working days edukkum. Documents-um backup company names-um nerathe ready aakku.")

# ferry: Meera + Tony. Meera's coral-survey consultancy became a company 21 days ago; she leaves for a ten-day Lakshadweep survey tonight.
duo("d1203", "freelancer", "C", "ferry", "കമ്പനിക്ക് 21 ദിവസം.\nഇന്ന് രാത്രി ലക്ഷദ്വീപിലേക്ക്\n10 ദിവസത്തെ സർവേ", [
 ("V","wide","മീര, ഈ പെട്ടി നിറയെ എന്താ? ഡൈവിംഗ് മാസ്കും ക്യാമറയും മാത്രമല്ലല്ലോ."),
 ("A","A","ടോണീ, ലക്ഷദ്വീപിൽ പവിഴപ്പുറ്റ് സർവേ. പത്ത് ദിവസം. കമ്പനിയുടെ പേരിലുള്ള ആദ്യ പ്രോജക്ട്!"),
 ("V","V","കമ്പനി ആയിട്ട് എത്ര ദിവസമായി?"),
 ("A","A","ഇരുപത്തൊന്ന് ദിവസം. എന്താ, കേക്ക് മുറിക്കണോ?"),
 ("V","V","കേക്ക് പിന്നെ. ആദ്യത്തെ ഓഡിറ്ററെ വെച്ചോ?"),
 ("A","A","അത് മാർച്ചിൽ കണക്ക് നോക്കുമ്പോൾ പോരേ?"),
 ("V","wide","പോരാ. കമ്പനി ആയി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം. ഇനി ഒൻപത് ദിവസം മാത്രം."),
 ("A","A","ഞാൻ തിരിച്ചെത്തുന്നത് പത്താം ദിവസം. അതായത് ഒരു ദിവസം വൈകും!"),
 ("V","V","അതുകൊണ്ട് ഈ ഫെറി പോകും മുമ്പ് ഫോൺ എടുത്ത് വിളിക്ക്."),
 ("A","wide","പവിഴപ്പുറ്റ് കാത്തിരിക്കും. ഡെഡ്‌ലൈൻ കാത്തിരിക്കില്ല!")],
 "യാത്രയ്ക്ക് മുമ്പ്\nഓഡിറ്ററെ ഉറപ്പാക്കൂ", CTA_AFTER,
 cap_ml="പവിഴപ്പുറ്റ് സർവേ ചെയ്യുന്ന കൺസൾട്ടന്റ് മീരയുടെ കമ്പനിക്ക് 21 ദിവസം, ഇന്ന് പത്ത് ദിവസത്തെ ലക്ഷദ്വീപ് യാത്ര. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം. യാത്രയോ പ്രോജക്ടോ ആണെങ്കിലും ഈ തീയതി മാറില്ല.",
 cap_en="A marine survey consultant's new company is 21 days old, and she leaves tonight for ten days in Lakshadweep. After company registration in India, the first auditor must be appointed within 30 days of incorporation. Sort it out before the trip, not after.",
 cap_mg="Coral survey cheyyunna Meera-yude company-kku 21 divasam, innu raathri 10 divasathe Lakshadweep trip. Company register cheythu 30 days-nullil first auditor-ne appoint cheyyanam. Trip-nu munpe athu set aakku.")

# garage: Aishwarya + Jithin. Aishwarya designs EV conversions for old scooters in Kozhikode and wants "Tesla" in her company name.
duo("d1204", "freelancer", "B", "garage", "പഴയ സ്കൂട്ടർ ഇലക്ട്രിക് ആക്കുന്നു.\nകമ്പനി പേര്:\n\"ടെസ്‌ല കോഴിക്കോട്\"", [
 ("V","wide","ഐശ്വര്യേ, ഈ പഴയ സ്കൂട്ടർ ഇപ്പോ ശബ്ദമില്ലാതെ ഓടുന്നു! പെട്രോൾ ടാങ്ക് എവിടെ?"),
 ("A","A","ജിതിൻ ചേട്ടാ, ടാങ്ക് പോയി, ബാറ്ററി വന്നു. ഇപ്പോ ആഴ്ചയിൽ ആറ് ഓർഡർ. ഇനി കമ്പനി ആക്കാൻ പോകുന്നു."),
 ("V","V","പേര് വല്ലതും ഇട്ടോ?"),
 ("A","wide","ഇട്ടു! ടെസ്‌ല കോഴിക്കോട്. കേൾക്കുമ്പോൾ തന്നെ ഒരു ഇന്റർനാഷണൽ ഫീൽ."),
 ("V","V","ഫീൽ ഒക്കെ ഉണ്ട്. പക്ഷേ ആ പേര് വേറൊരാളുടെ ട്രേഡ്മാർക്ക് അല്ലേ?"),
 ("A","A","അവർ അമേരിക്കയിൽ. ഞാൻ കോഴിക്കോട്. ആര് അറിയാൻ?"),
 ("V","wide","ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് രജിസ്ട്രേഷനിൽ തന്നെ റിജക്ട് ആകും."),
 ("V","V","പിന്നെ നിന്റെ സ്കൂട്ടർ പോലെ ശബ്ദമില്ലാതെ ഒരാഴ്ച കൂടി പോകും."),
 ("A","A","എന്നാൽ സ്വന്തം പേര് ആലോചിക്കാം. മൂന്ന് ബാക്കപ്പും."),
 ("V","wide","അതാ നല്ലത്. സ്കൂട്ടർ നിന്റേത്. പേരും നിന്റേത് ആകട്ടെ.")],
 "വലിയ ബ്രാൻഡിന്റെ പേര്\nകടം വാങ്ങരുത്", CTA_NAME,
 cap_ml="പഴയ സ്കൂട്ടറുകൾ ഇലക്ട്രിക് ആക്കുന്ന ഐശ്വര്യ കമ്പനിക്ക് ഒരു വിദേശ ബ്രാൻഡിന്റെ പേര് ഇടാൻ നോക്കി. ട്രേഡ്മാർക്കുമായി സാമ്യമുള്ള കമ്പനി പേര് രജിസ്ട്രേഷനിൽ റിജക്ട് ആകും. സ്വന്തമായ ഒരു പേരും രണ്ടോ മൂന്നോ ബാക്കപ്പ് പേരുകളും കരുതൂ.",
 cap_en="An EV conversion designer in Kozhikode wanted a famous car brand in her company name. A company name that clashes with an existing trademark gets rejected at registration. Pick an original name and keep two or three backups before you apply.",
 cap_mg="Pazhaya scooter electric aakkunna Aishwarya company name-il oru famous brand-inte peru idaan nokki. Trademark-umaayi match aakunna company name reject aakum. Swantham peru-um 2-3 backup names-um ready aakku.")

# metro: Anjali + Kiran. Anjali, a dubbing and voice-over artist, gets an offer from a Bengaluru ad agency to fund a studio for 30% of her company.
duo("d1205", "freelancer", "A", "metro", "ഡബ്ബിംഗ് ആർട്ടിസ്റ്റ്.\nആഡ് ഏജൻസി: \"സ്റ്റുഡിയോ\nഞങ്ങൾ ഇടാം, 30% ഷെയർ\"", [
 ("V","wide","അഞ്ജലീ, മെട്രോയിലെ അനൗൺസ്‌മെന്റ് നിന്റെ ശബ്ദം പോലെ തോന്നി!"),
 ("A","A","കിരണേ, അത് ഞാനല്ല. പക്ഷേ ഇന്ന് ഒരു ശബ്ദമുള്ള ന്യൂസ് ഉണ്ട്."),
 ("A","A","ബാംഗ്ലൂരിലെ ഒരു ആഡ് ഏജൻസി. അവരുടെ മലയാളം ആഡുകൾ മുഴുവൻ എനിക്ക്. ഒരു സ്റ്റുഡിയോ സെറ്റ് ചെയ്യാൻ പൈസ അവർ ഇടും."),
 ("V","V","എന്നിട്ട്? വെറുതെ തരുമോ?"),
 ("A","A","ഇല്ല. പകരം എന്റെ കമ്പനിയിൽ മുപ്പത് ശതമാനം ഷെയർ. ഞാൻ OPC തുടങ്ങാൻ ഇരിക്കുകയായിരുന്നു."),
 ("V","wide","ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കണമെങ്കിൽ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം."),
 ("V","V","അതിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ. ആരൊക്കെ എന്ന് ഇപ്പോഴേ തീരുമാനിക്ക്."),
 ("A","A","അപ്പോ ആദ്യം സ്ട്രക്ചർ. പിന്നെ സ്റ്റുഡിയോ."),
 ("V","wide","അടുത്ത സ്റ്റേഷൻ: പ്രൈവറ്റ് ലിമിറ്റഡ്. ഇറങ്ങാൻ മറക്കല്ലേ!")],
 "നിക്ഷേപം വരുന്നുണ്ടോ?\nOPC പോരാ", CTA_START,
 cap_ml="ഡബ്ബിംഗ് ആർട്ടിസ്റ്റിന്റെ സ്റ്റുഡിയോയ്ക്ക് പൈസ ഇടാൻ ഒരു ആഡ് ഏജൻസി തയ്യാർ, പകരം 30% ഷെയർ. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ കഴിയൂ. അതിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും വേണം.",
 cap_en="A freelance voice-over artist was about to start an OPC when an ad agency offered to fund her studio for 30% equity. Only a private limited company can take equity investment, and a Pvt Ltd needs at least two directors and two shareholders. Choose the structure before the money comes in.",
 cap_mg="Dubbing artist Anjali OPC thudangan irikkumbol oru ad agency studio-kku paisa idaam ennu paranju, pakaram 30% share. Share koduthu investment edukkan Pvt Ltd thanne venam. Athinu minimum 2 directors-um 2 shareholders-um venam.")

# akshaya: Sudha + Ramesh. Sudha transcribes court depositions; her company is four months old and she thinks opening the bank account was "starting business".
duo("d1206", "freelancer", "C", "akshaya", "കോടതി രേഖകൾ ടൈപ്പ് ചെയ്യുന്നു.\nകമ്പനിക്ക് 4 മാസം.\n\"ബാങ്ക് അക്കൗണ്ട് തുറന്നില്ലേ?\"", [
 ("V","wide","സുധേ, ഇന്ന് എന്താ അക്ഷയയിൽ? ആധാർ അപ്ഡേറ്റ് ആണോ?"),
 ("A","A","രമേശേട്ടാ, അല്ല. എന്റെ കമ്പനിയുടെ കാര്യം. കോടതി ട്രാൻസ്ക്രിപ്ഷൻ വർക്ക് ഇപ്പോ കമ്പനിയുടെ പേരിലാ."),
 ("V","V","കൊള്ളാം. എത്ര മാസമായി?"),
 ("A","A","നാല് മാസം. ബാങ്ക് അക്കൗണ്ട് തുറന്നു, ഇൻവോയ്സ് അയച്ചു. ഇനി ബാക്കി ഒന്നുമില്ല."),
 ("V","V","ബിസിനസ് തുടങ്ങിയെന്ന ഡിക്ലറേഷൻ, INC-20A, ഫയൽ ചെയ്തോ?"),
 ("A","A","അക്കൗണ്ട് തുറന്നപ്പോൾ അത് തനിയെ ആകില്ലേ?"),
 ("V","wide","ഇല്ല. അത് വേറെ ഫയൽ ചെയ്യണം. കമ്പനി ആയി നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ."),
 ("V","V","വൈകിയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ വേറെയും."),
 ("A","A","കോടതി രേഖകൾ ഞാൻ ഒരു വാക്ക് വിടാതെ ടൈപ്പ് ചെയ്യും. സ്വന്തം ഫോം വിട്ടുപോയി!"),
 ("V","wide","ഇനി രണ്ട് മാസം ഉണ്ട്. ഈ ആഴ്ച തന്നെ ചെയ്യ്.")],
 "അക്കൗണ്ട് തുറന്നാൽ പോരാ.\nINC-20A വേറെ", CTA_AFTER,
 cap_ml="കോടതി രേഖകൾ ടൈപ്പ് ചെയ്യുന്ന സുധ കരുതി, ബാങ്ക് അക്കൗണ്ട് തുറന്നാൽ ബിസിനസ് തുടങ്ങിയതായി എന്ന്. കമ്പനി രജിസ്ട്രേഷന് ശേഷം 180 ദിവസത്തിനുള്ളിൽ INC-20A പ്രത്യേകം ഫയൽ ചെയ്യണം. വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപയും ഡയറക്ടർക്ക് ദിവസവും പിഴ വരും.",
 cap_en="A freelance court transcriptionist thought opening the company bank account counted as starting business. INC-20A, the declaration of commencement of business, must be filed separately within 180 days of incorporation. Missing it means a penalty of Rs 50,000 on the company plus a daily penalty for each officer in default.",
 cap_mg="Court documents type cheyyunna Sudha vicharichu bank account thurannaal business thudangiyathaayi ennu. Company register cheythu 180 days-nullil INC-20A separate aayi file cheyyanam. Vaikiyaal company-kku 50,000 roopa penalty, director-kku divasavum penalty.")

# chat: Neethu (aquarium designer, Kollam) + Amma. The house is in her father's name; she needs his NOC and a recent bill to use it as the registered office.
chat("c901", "freelancer", "B", "അക്വേറിയം ഡിസൈനർ.\nകമ്പനി ഓഫീസ് അച്ഛന്റെ വീട്.\nഒപ്പ് വാങ്ങാൻ ആര് പോകും?", ("നീതു", "അമ്മ"), [
 (0,"അമ്മേ, ഒരു ചെറിയ കാര്യം. എന്റെ അക്വേറിയം കമ്പനിയുടെ ഓഫീസ് അഡ്രസ്സ് നമ്മുടെ വീട് ആക്കിക്കോട്ടെ?"),
 (1,"അതിനെന്താ മോളേ. പക്ഷേ മീൻ ടാങ്ക് ഇനിയും ഹാളിൽ വെക്കില്ല. ഇപ്പോ തന്നെ ആറെണ്ണം ഉണ്ട് 😅"),
 (0,"ടാങ്ക് അല്ല അമ്മേ, അഡ്രസ്സ് മാത്രം. പക്ഷേ വീട് അച്ഛന്റെ പേരിലല്ലേ. ഉടമയുടെ NOC വേണം."),
 (1,"NOC എന്ന് വെച്ചാൽ?"),
 (0,"അച്ഛൻ ഒപ്പിടുന്ന ഒരു സമ്മതപത്രം. പിന്നെ പുതിയ ഒരു കറന്റ് ബില്ലോ വെള്ളക്കരം ബില്ലോ."),
 (1,"ബിൽ ഫ്രിഡ്ജിന്റെ മുകളിൽ ഉണ്ട്. ഒപ്പിന് അച്ഛനെ ഞാൻ നോക്കിക്കോളാം."),
 (0,"അമ്മ എങ്ങനെ സമ്മതിപ്പിക്കും?"),
 (1,"അച്ഛന് ഇഷ്ടപ്പെട്ട ആ ഗോൾഡ് ഫിഷ് ഇല്ലേ. അതൊന്ന് കൊണ്ടുവാ. ഒപ്പ് താനേ വരും 🐟")],
 "വീട് ഓഫീസ് ആക്കാം.\nNOC-യും ബില്ലും മതി", CTA_DOCS,
 cap_ml="കൊല്ലത്തെ അക്വേറിയം ഡിസൈനർ നീതുവിന് കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് അച്ഛന്റെ പേരിലുള്ള വീട് ആക്കണം. വീടിന്റെ അഡ്രസ്സ് കമ്പനി ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും മതി. കേരളത്തിൽ കമ്പനി രജിസ്ട്രേഷന് പ്രത്യേക ഓഫീസ് മുറി വാടകയ്ക്ക് എടുക്കേണ്ടതില്ല.",
 cap_en="An aquarium designer in Kollam wants her parents' house, in her father's name, as her company's registered office. A home address works for company registration with the owner's NOC and a recent utility bill. No separate rented office is needed to start.",
 cap_mg="Kollam-ile aquarium designer Neethu-vinu company office address achante perilulla veedu aakkanam. Veedu registered office aakkan owner-nte NOC-um puthiya oru current bill-um mathi. Company register cheyyan separate office vaadakaykku edukkenda.")

# ---------------- cofounders ----------------
# cafe: Alvin + Roshan. Their board-game cafe became a company 25 days ago; Roshan says auditors are a March thing.
duo("d1207", "cofounders", "C", "cafe", "ബോർഡ് ഗെയിം കഫേ.\nകമ്പനിക്ക് 25 ദിവസം.\n\"ഓഡിറ്റർ മാർച്ചിൽ\"", [
 ("A","wide","റോഷാ, ഈ ഷെൽഫിൽ ഇനി ഒരു ഗെയിം കൂടി വെക്കാൻ സ്ഥലമില്ല."),
 ("V","V","ആൽവിനേ, ശനിയാഴ്ച ലോഞ്ച് അല്ലേ. നൂറ്റിയിരുപത് ഗെയിം. ചെസ്സ് മുതൽ മോണോപ്പൊളി വരെ."),
 ("A","A","കമ്പനി ആയിട്ട് ഇരുപത്തഞ്ച് ദിവസമായി. ഓഡിറ്ററുടെ കാര്യം ആരെങ്കിലും നോക്കിയോ?"),
 ("V","V","ഓഡിറ്റർ ഒക്കെ മാർച്ചിൽ അല്ലേ ഡാ? കണക്ക് അടയ്ക്കുമ്പോൾ."),
 ("A","wide","അല്ല അളിയാ. കമ്പനി ആയി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം."),
 ("V","V","മുപ്പത് മൈനസ് ഇരുപത്തഞ്ച്. അഞ്ച് ദിവസം!"),
 ("A","A","ലോഞ്ച് തിരക്കിൽ ഇത് പോയാൽ ആദ്യ റൗണ്ടിൽ തന്നെ നമ്മൾ ഔട്ട്."),
 ("V","wide","എന്നാൽ ഇന്ന് ഗെയിം വേണ്ട. ആദ്യം ഓഡിറ്റർ. പിന്നെ ലോഞ്ച്!")],
 "ലോഞ്ച് തിരക്കിലും\n30 ദിവസം മറക്കരുത്", CTA_AFTER,
 cap_ml="കൊച്ചിയിൽ ബോർഡ് ഗെയിം കഫേ തുടങ്ങുന്ന രണ്ട് കോ-ഫൗണ്ടേഴ്സ് കരുതി, ഓഡിറ്റർ മാർച്ചിലെ കാര്യമാണെന്ന്. കമ്പനി രജിസ്ട്രേഷൻ കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം. ലോഞ്ച് തിരക്കിൽ ഈ ഡെഡ്‌ലൈൻ മുങ്ങിപ്പോകരുത്.",
 cap_en="Two co-founders opening a board-game cafe thought the auditor was a March problem, but their company was already 25 days old. Every private limited company must appoint its first auditor within 30 days of incorporation. Put it in the launch checklist.",
 cap_mg="Board game cafe thudangunna randu co-founders vicharichu auditor March-il mathi ennu. Company register cheythu 30 days-nullil first auditor-ne vekkanam. Launch thirakkil ee deadline miss aakkaruthu.")

# autostand: Saji + Shaji. Two auto drivers built a booking app for their town's stand; Shaji believes a company needs 10 lakh in the bank first.
duo("d1208", "cofounders", "A", "autostand", "രണ്ട് ഓട്ടോ ഡ്രൈവർമാരുടെ\nബുക്കിംഗ് ആപ്പ്.\n\"ആദ്യം 10 ലക്ഷം വേണം\"", [
 ("A","wide","ഷാജീ, ഇന്നലെ ആപ്പിൽ നാൽപ്പത് ബുക്കിംഗ്! സ്റ്റാൻഡിലെ എല്ലാ ഓട്ടോയും ഓടി."),
 ("V","V","സജീ, നമ്മുടെ മോൻ ഉണ്ടാക്കിയ ആപ്പ് ഇത്ര ഹിറ്റ് ആകുമെന്ന് വിചാരിച്ചില്ല."),
 ("A","A","അടുത്ത ടൗണിലെ സ്റ്റാൻഡുകാരും ചോദിക്കുന്നു. ഇനി ഇത് കമ്പനി ആക്കണം."),
 ("V","V","അതിന് ബാങ്കിൽ പത്ത് ലക്ഷം വേണമെന്ന് പെട്രോൾ പമ്പിലെ ചേട്ടൻ പറഞ്ഞു."),
 ("A","A","പത്ത് ലക്ഷം! അത്രയും ഉണ്ടെങ്കിൽ ഞാൻ ഓട്ടോ ഓടിക്കുമോ?"),
 ("V","wide","അപ്പോ കമ്പനി സ്വപ്നം ഗിയർ മാറ്റാതെ നിൽക്കും."),
 ("A","wide","കേട്ടോ. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ എന്നൊന്നില്ല."),
 ("A","A","നമ്മൾ രണ്ടുപേർ മതി. രണ്ട് ഡയറക്ടർ, രണ്ട് ഷെയർഹോൾഡർ."),
 ("V","V","എന്നാൽ പമ്പിലെ ചേട്ടന് ഇനി ഫ്രീ റൈഡ് ഇല്ല!")],
 "കമ്പനിക്ക് മിനിമം\nക്യാപിറ്റൽ നിബന്ധനയില്ല", CTA_START,
 cap_ml="സ്വന്തം ടൗണിൽ ഓട്ടോ ബുക്കിംഗ് ആപ്പ് ഹിറ്റാക്കിയ രണ്ട് ഡ്രൈവർമാർ കരുതി, കമ്പനി തുടങ്ങാൻ ബാങ്കിൽ പത്ത് ലക്ഷം വേണമെന്ന്. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിബന്ധനയില്ല. രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും ഉണ്ടെങ്കിൽ സ്റ്റാർട്ടപ്പ് കമ്പനി രജിസ്റ്റർ ചെയ്യാം.",
 cap_en="Two auto drivers whose booking app took off were told they need 10 lakh in the bank to register a company. There is no minimum paid-up capital for a private limited company in India. Two founders can be the two directors and two shareholders a Pvt Ltd needs.",
 cap_mg="Auto booking app hit aakkiya randu drivers vicharichu company register cheyyan bank-il 10 lakh venamennu. Pvt Ltd-nu minimum paid-up capital illa. Randu per mathi, 2 directors 2 shareholders aayi startup company thudangaam.")

# hotellobby: Neethu + Jayson. Their corporate-offsite planning firm is a partnership; a hotel group wants to put money in for 15%.
duo("d1209", "cofounders", "A", "hotellobby", "ഓഫ്‌സൈറ്റ് പ്ലാനിംഗ് സ്റ്റാർട്ടപ്പ്.\nഹോട്ടൽ ഗ്രൂപ്പ്: \"15% തരൂ,\nപൈസ ഞങ്ങൾ ഇടാം\"", [
 ("V","wide","നീതു, ജനറൽ മാനേജർ എന്തിനാ നമ്മളെ മാത്രം കാബിനിലേക്ക് വിളിച്ചത്?"),
 ("A","A","ജെയ്സൺ, നമ്മൾ കൊണ്ടുവന്ന ഐടി ടീമുകളുടെ ഓഫ്‌സൈറ്റ് അവർക്ക് ഇഷ്ടപ്പെട്ടു. ഇനി അവരുടെ എല്ലാ റിസോർട്ടിലും നമ്മൾ."),
 ("V","V","അടിപൊളി! ഓർഡർ മാത്രമാണോ?"),
 ("A","A","അല്ല. നമ്മുടെ സ്റ്റാർട്ടപ്പിൽ പൈസ ഇടാം എന്ന്. പകരം പതിനഞ്ച് ശതമാനം ഷെയർ."),
 ("V","V","നമ്മുടേത് പാർട്ണർഷിപ്പ് ഡീഡ് അല്ലേ? അതിൽ ഒരു പേജ് കൂടി ചേർത്താൽ പോരേ?"),
 ("A","wide","പോരാ. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡിനേ പറ്റൂ."),
 ("A","A","പാർട്ണർഷിപ്പിനും LLP-ക്കും ഇങ്ങനെ ഷെയർ കൊടുക്കാൻ പറ്റില്ല."),
 ("V","V","അപ്പോ ടേം ഷീറ്റിന് മുമ്പ് കമ്പനി."),
 ("A","wide","അതേ. ഓഫ്‌സൈറ്റ് പ്ലാൻ ചെയ്യുന്ന നമ്മൾ, സ്വന്തം കമ്പനി പ്ലാൻ ചെയ്യാൻ മറക്കരുത്!")],
 "ഷെയർ ചോദിച്ചാൽ\nഡീഡ് പോരാ", CTA_START,
 cap_ml="കോർപ്പറേറ്റ് ഓഫ്‌സൈറ്റ് പ്ലാൻ ചെയ്യുന്ന രണ്ട് കോ-ഫൗണ്ടേഴ്സിന്റെ സ്റ്റാർട്ടപ്പിൽ ഒരു ഹോട്ടൽ ഗ്രൂപ്പ് 15% ഷെയറിന് നിക്ഷേപിക്കാൻ തയ്യാർ. പാർട്ണർഷിപ്പിനോ LLP-ക്കോ ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ കഴിയില്ല. അതിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി രജിസ്ട്രേഷൻ വേണം.",
 cap_en="A hotel group wants 15% of a two-founder offsite-planning startup that still runs as a partnership. A partnership firm or LLP cannot issue shares to an investor; only a private limited company can take equity investment. Register the Pvt Ltd before the term sheet.",
 cap_mg="Corporate offsite plan cheyyunna startup-il oru hotel group 15% share-nu invest cheyyaan ready. Partnership-nu allenkil LLP-kku share koduthu investment edukkan pattilla. Athinu Pvt Ltd register cheyyanam.")

# courier: Jaya + Aravind. Their same-day parcel startup for Kochi boutiques wants the name "Speed Post Express".
duo("d1210", "cofounders", "B", "courier", "ബൂട്ടീക്കുകൾക്ക് സെയിം-ഡേ ഡെലിവറി.\nകമ്പനി പേര്:\n\"സ്പീഡ് പോസ്റ്റ് എക്സ്പ്രസ്\"", [
 ("V","wide","ജയ, ഇന്ന് മാത്രം അറുപത് പാർസൽ! കൊച്ചിയിലെ എല്ലാ ബൂട്ടീക്കും നമ്മളെ അറിയാം."),
 ("A","A","അരവിന്ദേ, അതുകൊണ്ട് ഇനി കമ്പനി. പേര് ഞാൻ ഫിക്സ് ചെയ്തു. സ്പീഡ് പോസ്റ്റ് എക്സ്പ്രസ്!"),
 ("V","V","കേൾക്കാൻ നല്ല സ്പീഡ് ഉണ്ട്. പക്ഷേ സ്പീഡ് പോസ്റ്റ് ആരുടെ സർവീസ് ആണെന്ന് ഓർമ്മയുണ്ടോ?"),
 ("A","A","പോസ്റ്റ് ഓഫീസിന്റെ. അതിന്?"),
 ("V","wide","നിലവിലുള്ള ബ്രാൻഡിനോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യമുള്ള പേര് റിജക്ട് ആകും."),
 ("V","V","പിന്നെ ആദ്യം മുതൽ വീണ്ടും അപേക്ഷ. നമ്മുടെ സെയിം-ഡേ അപ്പോൾ നെക്സ്റ്റ് വീക്ക് ആകും."),
 ("A","A","ശരി. എന്നാൽ നമ്മുടെ സ്വന്തം പേര് ആലോചിക്കാം. മൂന്നെണ്ണം."),
 ("V","V","അതിൽ ഒന്നിലും 'പോസ്റ്റ്' വേണ്ട."),
 ("A","wide","സമ്മതിച്ചു. പോസ്റ്റ്മാന്റെ പേര് പോസ്റ്റ്മാന്. നമ്മുടെ പേര് നമുക്ക്!")],
 "അറിയുന്ന ബ്രാൻഡിന്റെ\nപേര് വേണ്ട", CTA_NAME,
 cap_ml="കൊച്ചിയിൽ ബൂട്ടീക്കുകൾക്ക് സെയിം-ഡേ ഡെലിവറി ചെയ്യുന്ന സ്റ്റാർട്ടപ്പിന് ഫൗണ്ടേഴ്സ് ഇട്ട പേര് ഒരു അറിയപ്പെടുന്ന സർവീസിന്റേത്. നിലവിലുള്ള കമ്പനിയുമായോ ട്രേഡ്മാർക്കുമായോ സാമ്യമുള്ള കമ്പനി പേര് റിജക്ട് ആകും. അപേക്ഷിക്കും മുമ്പ് സ്വന്തമായ പേരുകൾ കണ്ടെത്തൂ.",
 cap_en="Two co-founders running a same-day delivery startup for Kochi boutiques picked a name borrowed from a well-known postal service. Company names similar to an existing company or a trademark are rejected. Shortlist original names before you file for company registration.",
 cap_mg="Kochi-yile boutiques-nu same-day delivery cheyyunna startup-nu founders itta peru oru famous service-inte peru. Existing company-umaayo trademark-umaayo match aakunna company name reject aakum. Apply cheyyunnathinu munpe swantham names kandupidikku.")

# chat: Jibin + Akhil (WhatsApp). Their private-bus timing app had zero revenue in year one; Akhil says no money, no filing.
chat("c902", "cofounders", "C", "ബസ് ടൈമിംഗ് ആപ്പ്.\nഒരു വർഷം, ഒരു രൂപ വരുമാനമില്ല.\n\"ഫയലിംഗ് എന്തിന്?\"", ("ജിബിൻ", "അഖിൽ"), [
 (0,"അഖിലേ, ആപ്പിന് ഇന്ന് ഇരുപതിനായിരം ഡൗൺലോഡ്! പാലക്കാട്-തൃശൂർ റൂട്ടിലെ എല്ലാ ബസും ഉണ്ട് 🚌"),
 (1,"സൂപ്പർ. പക്ഷേ ഒരു പരസ്യം പോലുമില്ല. വരുമാനം പൂജ്യം."),
 (0,"അതാ പറയാൻ വന്നത്. കമ്പനിക്ക് ഒരു വർഷമായി. ആനുവൽ ഫയലിംഗ് സമയമായി."),
 (1,"വരുമാനം ഇല്ലാത്തപ്പോൾ എന്ത് ഫയൽ ചെയ്യാനാ? കണക്കിൽ എല്ലാം സീറോ അല്ലേ."),
 (0,"സീറോ ആണെങ്കിലും ROC-യിൽ ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്."),
 (0,"വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ. അത് എണ്ണിക്കൊണ്ടിരിക്കും."),
 (1,"ബസ് വൈകിയാൽ ആപ്പ് പറയും. ഫയലിംഗ് വൈകിയാൽ ആര് പറയും? 😅"),
 (0,"ഞാൻ ഇപ്പോ പറഞ്ഞില്ലേ. ഈ ആഴ്ച തന്നെ ചെയ്യാം.")],
 "വരുമാനം പൂജ്യം.\nഫയലിംഗ് നിർബന്ധം", CTA_AFTER,
 cap_ml="പ്രൈവറ്റ് ബസ് ടൈമിംഗ് ആപ്പ് ഉണ്ടാക്കിയ രണ്ട് കോ-ഫൗണ്ടേഴ്സിന് ആദ്യ വർഷം വരുമാനം പൂജ്യം, അതുകൊണ്ട് ഫയലിംഗ് വേണ്ടെന്ന് ഒരാൾ കരുതി. വരുമാനം ഇല്ലെങ്കിലും ROC ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="Two startup co-founders built a bus-timing app with thousands of downloads and zero revenue in year one. Annual ROC filings are due even when a company earns nothing, and a late filing adds Rs 100 per day for each form. Zero revenue does not mean zero compliance.",
 cap_mg="Bus timing app undaakkiya startup-nu first year revenue zero, appo filing venda ennu oru co-founder vicharichu. Revenue illenkilum ROC annual filing nirbandham aanu. Vaikiyaal oro form-inum divasam 100 roopa penalty.")

# gym: Riya + Justin. Two trainers starting a women's fitness studio want to add Riya's mother as a third director "to make it legal".
duo("d1211", "cofounders", "B", "gym", "രണ്ട് ട്രെയിനർമാർ.\nലേഡീസ് ഫിറ്റ്നസ് സ്റ്റുഡിയോ.\n\"അമ്മയെ കൂടി ചേർക്കാം\"", [
 ("V","wide","റിയ, ഫോം എഴുതിയോ? പുതിയ സ്റ്റുഡിയോയ്ക്ക് കമ്പനി എന്ന് നമ്മൾ തീരുമാനിച്ചതല്ലേ."),
 ("A","A","ജസ്റ്റിൻ, എഴുതി. ഡയറക്ടർമാർ: ഞാൻ, നീ, പിന്നെ എന്റെ അമ്മ."),
 ("V","V","അമ്മയോ? അമ്മ ജിമ്മിൽ വരുന്നത് പോലും വിരളമല്ലേ?"),
 ("A","A","അതൊന്നും വേണ്ട. മൂന്ന് പേരില്ലെങ്കിൽ കമ്പനി ലീഗൽ ആകില്ലെന്ന് കസിൻ പറഞ്ഞു."),
 ("V","wide","തെറ്റാണ്. പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും മതി."),
 ("V","V","നമ്മൾ രണ്ടുപേർ. അത് തികഞ്ഞു."),
 ("A","A","അപ്പോ അമ്മയ്ക്ക് ഡയറക്ടർ പോസ്റ്റ് ഇല്ല."),
 ("V","V","പോസ്റ്റ് ഇല്ല. പകരം ഫ്രീ മെമ്പർഷിപ്പ് കൊടുക്കാം."),
 ("A","wide","അത് അമ്മ എടുക്കില്ല. പക്ഷേ ഓഫർ കേട്ട് ചിരിക്കും!")],
 "മൂന്നാമത്തെ ആൾ വേണ്ട.\nരണ്ടുപേർ മതി", CTA_START,
 cap_ml="ലേഡീസ് ഫിറ്റ്നസ് സ്റ്റുഡിയോ തുടങ്ങുന്ന രണ്ട് ട്രെയിനർമാർ കരുതി, കമ്പനി ലീഗൽ ആകാൻ മൂന്നാമതൊരു ഡയറക്ടർ വേണമെന്ന്. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി രജിസ്ട്രേഷന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും മതി. രണ്ട് കോ-ഫൗണ്ടേഴ്സ് മാത്രം മതി തുടങ്ങാൻ.",
 cap_en="Two fitness trainers starting a women's studio planned to add a mother as a third director just to make the company legal. A private limited company needs a minimum of two directors and two shareholders, so two co-founders are enough. Add people for real roles, not to fill a form.",
 cap_mg="Ladies fitness studio thudangunna randu trainers vicharichu company legal aakan moonnamathoru director venamennu. Pvt Ltd register cheyyan minimum 2 directors-um 2 shareholders-um mathi. Randu co-founders mathi company thudangan.")

# list: myths heard in a founders' group chat.
lst("l901", "cofounders", "C", "ഫൗണ്ടേഴ്സ് ഗ്രൂപ്പിൽ\nഈ ആഴ്ച കേട്ട\n3 തെറ്റിദ്ധാരണ", [
 ("\"LLP ആയാലും ഇൻവെസ്റ്റർക്ക് ഷെയർ കൊടുക്കാം\"", "തെറ്റ്. ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡിനേ പറ്റൂ."),
 ("\"കമ്പനി തുടങ്ങാൻ ലക്ഷങ്ങൾ ക്യാപിറ്റൽ വേണം\"", "തെറ്റ്. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിബന്ധനയില്ല."),
 ("\"രണ്ട് ഫൗണ്ടേഴ്സും ഗൾഫിൽ, എന്നിട്ടും ഓക്കെ\"", "പോരാ. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.")],
 "ഗ്രൂപ്പിൽ കേട്ടത്\nഉറപ്പിച്ചിട്ട് തുടങ്ങൂ", CTA_START,
 cap_ml="സ്റ്റാർട്ടപ്പ് ഫൗണ്ടേഴ്സ് ഗ്രൂപ്പുകളിൽ കേൾക്കുന്ന മൂന്ന് തെറ്റിദ്ധാരണകൾ: LLP-ക്ക് ഇൻവെസ്റ്റർക്ക് ഷെയർ കൊടുക്കാം, കമ്പനിക്ക് ലക്ഷങ്ങൾ ക്യാപിറ്റൽ വേണം, രണ്ട് ഡയറക്ടർമാരും വിദേശത്ത് ആയാലും മതി. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം ക്യാപിറ്റൽ ഇല്ല, ഇക്വിറ്റി നിക്ഷേപം അതിന് മാത്രം, ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.",
 cap_en="Three myths from a startup founders' group: an LLP can give investors shares, a company needs lakhs of capital, and both directors can live abroad. In fact only a private limited company can take equity investment, there is no minimum paid-up capital, and at least one director must be resident in India.",
 cap_mg="Founders group-il kelkkunna 3 myths: LLP-kku investor-nu share kodukkaam, company thudangan lakhs capital venam, randu directors-um abroad aayaalum mathi. Sathyam: equity investment Pvt Ltd-nu maathram, minimum capital illa, oru director India-yil thaamasikkunna aal aakanam.")

# ---------------- salaried ----------------
# kitchen: Bindu + Rajesh. Rajesh (KSEB engineer) sells mango pickle online on weekends; the house is in Bindu's name, so she gives the NOC.
duo("d1212", "salaried", "B", "kitchen", "KSEB എഞ്ചിനീയറുടെ\nവീക്കെൻഡ് അച്ചാർ ബ്രാൻഡ്.\nവീട് ഭാര്യയുടെ പേരിൽ", [
 ("A","wide","രാജേഷേട്ടാ, ഈ ആഴ്ച ഇരുന്നൂറ് കുപ്പി മാങ്ങാ അച്ചാർ! അടുക്കള മുഴുവൻ ഭരണി."),
 ("V","V","ബിന്ദൂ, ഓൺലൈൻ ഓർഡർ കൂടി. ഒരു സൂപ്പർമാർക്കറ്റ് ചെയിൻ കമ്പനി ഇൻവോയ്സ് ചോദിച്ചു."),
 ("A","A","അപ്പോ കമ്പനി ആക്കാം. ഓഫീസ് അഡ്രസ്സ് എവിടെ കൊടുക്കും? ചേട്ടന്റെ KSEB ഓഫീസ് പറ്റില്ലല്ലോ."),
 ("V","V","ഹ ഹ. അത് പറ്റില്ല. ഈ വീട് തന്നെ കൊടുക്കാം."),
 ("A","A","വീട് എന്റെ പേരിലാണേ. ഓർമ്മയുണ്ടല്ലോ."),
 ("V","wide","അതുകൊണ്ട് ഉടമയായ നിന്റെ NOC വേണം. പിന്നെ പുതിയ ഒരു കറന്റ് ബില്ലും."),
 ("A","A","കറന്റ് ബിൽ നോക്കാൻ KSEB എഞ്ചിനീയർ തന്നെ വീട്ടിൽ ഉണ്ടല്ലോ."),
 ("V","V","പിന്നെ ഡയറക്ടർമാർ രണ്ടുപേർ വേണം. ഞാനും നീയും."),
 ("A","wide","എന്നാൽ NOC-യിൽ ഒപ്പിടാം. പകരം അച്ചാർ ലേബലിൽ എന്റെ പേരും വേണം!")],
 "വീട് ഓഫീസ് ആക്കാൻ\nഉടമയുടെ NOC", CTA_DOCS,
 cap_ml="KSEB-യിൽ ജോലി ചെയ്യുന്ന രാജേഷിന്റെ വീക്കെൻഡ് അച്ചാർ ബിസിനസിന് സൂപ്പർമാർക്കറ്റ് കമ്പനി ഇൻവോയ്സ് ചോദിച്ചു, വീട് ഭാര്യയുടെ പേരിലും. വീട് കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും മതി. പ്രൈവറ്റ് ലിമിറ്റഡിന് രണ്ട് ഡയറക്ടർമാർ വേണം.",
 cap_en="A salaried KSEB engineer's weekend pickle brand needs company invoices, and the family house is in his wife's name. A home can be the registered office with the owner's NOC and a recent utility bill. A private limited company also needs at least two directors.",
 cap_mg="KSEB engineer Rajesh-nte weekend pickle business-nu supermarket company invoice chodichu, veedu bhaaryayude perilum. Veedu registered office aakkan owner-nte NOC-um puthiya current bill-um mathi. Pvt Ltd-nu 2 directors venam.")

# weddinghall: Kavya + Sharath. Sharath (IT) runs a weekend photo-booth; the hall's vendor list closes soon and his name "SnapBox" is close to an existing company.
duo("d1213", "salaried", "A", "weddinghall", "ഐടി ജോലി. വീക്കെൻഡിൽ\nകല്യാണ ഫോട്ടോ ബൂത്ത്.\nപേര് \"സ്നാപ്പ് ബോക്സ്\"", [
 ("A","wide","ശരത്, ഈ ബൂത്തിന് മുന്നിൽ അമ്മാവന്മാരുടെ ക്യൂ! ഇതുവരെ ഞാൻ ഇങ്ങനെ കണ്ടിട്ടില്ല."),
 ("V","V","കാവ്യാ, തിങ്കൾ മുതൽ വെള്ളി വരെ കോഡ്. ശനിയും ഞായറും ഫോട്ടോ ബൂത്ത്. രണ്ടും ഹിറ്റ്."),
 ("A","A","ഹാൾ മാനേജ്മെന്റ് വെണ്ടർ ലിസ്റ്റ് ഉണ്ടാക്കുന്നു. കമ്പനികൾ മാത്രം. പേര് എന്താ?"),
 ("V","V","സ്നാപ്പ് ബോക്സ് പ്രൈവറ്റ് ലിമിറ്റഡ്. കൊള്ളാമോ?"),
 ("A","A","കൊള്ളാം. പക്ഷേ ഇന്നലെ ഒരു ഇവന്റ് കമ്പനിയുടെ കാർഡ് കണ്ടു. സ്നാപ്പ്ബോക്സ് ഇവന്റ്സ് എന്ന്."),
 ("V","wide","അയ്യോ. നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യമുണ്ടെങ്കിൽ റിജക്ട് ആകുമല്ലേ?"),
 ("A","wide","അതേ. അതുകൊണ്ട് അപേക്ഷിക്കും മുമ്പ് രണ്ടോ മൂന്നോ ബാക്കപ്പ് പേരുകൾ കരുതിക്കോ."),
 ("V","V","ശരി. ഈ കല്യാണം കഴിഞ്ഞ് പേര് ആലോചിക്കാം."),
 ("A","wide","കല്യാണത്തിന് ബാക്കപ്പ് ചെക്കൻ ഇല്ല. കമ്പനിക്ക് ബാക്കപ്പ് പേര് വേണം!")],
 "ഇഷ്ടപ്പെട്ട പേരിനൊപ്പം\nബാക്കപ്പും കരുതൂ", CTA_NAME,
 cap_ml="ഐടി ജോലിക്കൊപ്പം വീക്കെൻഡിൽ കല്യാണ ഫോട്ടോ ബൂത്ത് നടത്തുന്ന ശരത് കമ്പനിക്ക് ഇട്ട പേരിനോട് സാമ്യമുള്ള ഒരു ഇവന്റ് കമ്പനി നിലവിലുണ്ട്. നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യമുള്ള പേര് റിജക്ട് ആകും. കമ്പനി രജിസ്ട്രേഷന് മുമ്പ് ബാക്കപ്പ് പേരുകൾ കരുതൂ.",
 cap_en="An IT employee runs a wedding photo-booth on weekends, and the company name he chose sounds like an existing event company. Names similar to an existing company or LLP get rejected during registration. Keep two or three backup company names ready.",
 cap_mg="IT job-inte koode weekend-il wedding photo booth nadathunna Sharath company-kku itta peru oru existing event company-yude perupole. Existing company allenkil LLP name-umaayi match aayaal reject aakum. Backup company names ready aakku.")

# railway: Sheeba + Dinesh. Dinesh, a loco pilot, 3D-prints model trains; his company is four months old and he thinks INC-20A is for big companies.
duo("d1214", "salaried", "C", "railway", "ലോക്കോ പൈലറ്റിന്റെ\nമോഡൽ ട്രെയിൻ കമ്പനി.\nനാല് മാസം, INC-20A ഇല്ല", [
 ("A","wide","ദിനേശേട്ടാ, ഡ്യൂട്ടി കഴിഞ്ഞ് സ്റ്റേഷനിൽ ഇരുന്ന് എന്താ ബോക്സ് തുറക്കുന്നത്?"),
 ("V","V","ഷീബേ, നമ്മുടെ 3D പ്രിന്റ് ചെയ്ത മോഡൽ ട്രെയിൻ. ജർമ്മനിയിൽ നിന്ന് വരെ ഓർഡർ വന്നു."),
 ("A","A","കമ്പനി ആക്കിയിട്ട് എത്ര മാസമായി?"),
 ("V","V","നാല് മാസം. INC-20A ഒക്കെ വലിയ കമ്പനികൾക്കല്ലേ? നമ്മുടേത് ഒരു ടോയ് ട്രെയിൻ."),
 ("A","wide","ട്രെയിൻ ചെറുതാണ്. നിയമം എല്ലാവർക്കും ഒന്നാണ്."),
 ("A","A","ബിസിനസ് തുടങ്ങിയെന്ന ഡിക്ലറേഷൻ നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം."),
 ("V","V","ഇല്ലെങ്കിൽ?"),
 ("A","wide","കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ, പരമാവധി ഒരു ലക്ഷം."),
 ("V","V","എന്റെ ട്രെയിൻ ഒരിക്കലും ലേറ്റ് ആയിട്ടില്ല. ഫോമും ലേറ്റ് ആകില്ല!")],
 "ചെറിയ കമ്പനിക്കും\n180 ദിവസം ബാധകം", CTA_AFTER,
 cap_ml="ലോക്കോ പൈലറ്റ് ദിനേശിന്റെ സൈഡ് ബിസിനസായ മോഡൽ ട്രെയിൻ കമ്പനിക്ക് നാല് മാസം, INC-20A വലിയ കമ്പനികൾക്കുള്ളതാണെന്ന് അദ്ദേഹം കരുതി. എല്ലാ കമ്പനിയും 180 ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം. വൈകിയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ.",
 cap_en="A loco pilot's model-train side business is a four-month-old company, and he assumed INC-20A was only for big companies. Every company must file INC-20A within 180 days of incorporation, whatever its size. The penalty for missing it is Rs 50,000 on the company plus a daily penalty for officers.",
 cap_mg="Loco pilot Dinesh-nte model train side business company-kku 4 maasam, INC-20A valiya company-kalkku maathram ennu vicharichu. Ethu company aayaalum 180 days-nullil INC-20A file cheyyanam. Vaikiyaal company-kku 50,000 roopa penalty.")

# park: Gayathri + Ananthu. Gayathri, a bank officer, runs a weekend running club and wants to name her company after the city's marathon.
duo("d1215", "salaried", "B", "park", "ബാങ്ക് ജോലി. ഞായറാഴ്ച\nറണ്ണിംഗ് ക്ലബ്.\nകമ്പനി പേര്: \"കൊച്ചി മാരത്തൺ\"", [
 ("V","wide","ഗായത്രീ, ഇന്ന് പാർക്കിൽ എത്ര പേർ ഓടാൻ വന്നു?"),
 ("A","A","അനന്തൂ, എൺപത്! ഇനി ട്രെയിനിംഗ് പ്ലാനും ജേഴ്സിയും വിൽക്കണം. ഒരു കമ്പനി തുടങ്ങണം."),
 ("V","V","ബാങ്ക് ജോലിയും ഓട്ടവും ഒരുമിച്ച്. പേര് തീരുമാനിച്ചോ?"),
 ("A","wide","കൊച്ചി മാരത്തൺ. ആരും സെർച്ച് ചെയ്താൽ നമ്മൾ ആദ്യം വരും."),
 ("V","V","പക്ഷേ ആ പേരിൽ ഒരു വലിയ ഇവന്റ് ഇപ്പോൾ തന്നെ ഇല്ലേ? അവർക്ക് കമ്പനിയോ ട്രേഡ്മാർക്കോ ഉണ്ടാകും."),
 ("A","A","ഓ. അത് ഞാൻ ആലോചിച്ചില്ല."),
 ("V","wide","നിലവിലുള്ള കമ്പനിയുടെയോ ട്രേഡ്മാർക്കിന്റെയോ പേരിനോട് സാമ്യമുണ്ടെങ്കിൽ റിജക്ട് ആകും."),
 ("A","A","എന്നാൽ സ്വന്തം പേര്. ക്ലബിന്റെ അംഗങ്ങളോട് തന്നെ ചോദിക്കാം."),
 ("V","wide","അതാ നല്ലത്. എൺപത് പേർ, എൺപത് പേര്!")],
 "മറ്റൊരാളുടെ ഇവന്റ് പേര്\nകമ്പനിക്ക് വേണ്ട", CTA_NAME,
 cap_ml="ബാങ്കിൽ ജോലി ചെയ്യുന്ന ഗായത്രി ഞായറാഴ്ച റണ്ണിംഗ് ക്ലബ് നടത്തുന്നു, കമ്പനിക്ക് നഗരത്തിലെ ഒരു വലിയ ഇവന്റിന്റെ പേര് ഇടാൻ നോക്കി. നിലവിലുള്ള കമ്പനി പേരിനോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യമുള്ള പേര് റിജക്ട് ആകും. സ്വന്തമായ കമ്പനി പേര് കണ്ടെത്തി ബാക്കപ്പും കരുതൂ.",
 cap_en="A salaried bank officer turning her weekend running club into a business wanted to name the company after a big city marathon. A company name similar to an existing company or a trademark gets rejected. Choose an original name for your company registration in Kochi and keep backups.",
 cap_mg="Bank-il job cheyyunna Gayathri Sunday running club nadathunnu, company-kku city-ile oru valiya event-inte peru idaan nokki. Existing company name allenkil trademark-umaayi match aayaal reject aakum. Swantham company name kandupidichu backup-um vekku.")

# chat: Deepthi (side brand of handmade baby slings, on maternity leave) + Saranya. Revenue paused for the year; filings still due.
chat("c903", "salaried", "C", "മെറ്റേണിറ്റി ലീവ്.\nസൈഡ് ബിസിനസ് ഒരു വർഷം നിർത്തി.\nകമ്പനി ഫയലിംഗും നിർത്താമോ?", ("ദീപ്തി", "ശരണ്യ"), [
 (0,"ശരണ്യേ, ഒരു ഡൗട്ട്. മോൾ ഉണ്ടായ ശേഷം ബേബി സ്ലിംഗ് ബിസിനസ് മുഴുവൻ നിർത്തി വെച്ചിരിക്കുകയാ 👶"),
 (1,"അത് നല്ലതാ. ഇപ്പോ ഉറക്കമാണ് പ്രധാനം. എന്താ ഡൗട്ട്?"),
 (0,"ഈ വർഷം ഒരു ഓർഡറും ഇല്ല. അപ്പോ കമ്പനിയുടെ ആനുവൽ ഫയലിംഗും ഈ വർഷം വേണ്ടല്ലോ?"),
 (1,"വേണം. വരുമാനം ഇല്ലാത്ത വർഷവും ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്."),
 (1,"വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ. ലീവ് കഴിഞ്ഞ് വരുമ്പോൾ ഒരു വലിയ സംഖ്യ കാത്തിരിക്കും."),
 (0,"അയ്യോ. ഓഫീസിലെ ലീവ് പോലെ കമ്പനിക്ക് ലീവ് ഇല്ലല്ലേ 😅"),
 (1,"ഇല്ല. പക്ഷേ ഡേറ്റ് നേരത്തെ അറിഞ്ഞാൽ മോൾ ഉറങ്ങുന്ന സമയത്ത് പ്ലാൻ ചെയ്യാം."),
 (0,"ശരി. ഡേറ്റ് ഇന്ന് തന്നെ ഫോണിൽ ഇടുന്നു.")],
 "ബിസിനസിന് ബ്രേക്ക്.\nഫയലിംഗിന് ബ്രേക്കില്ല", CTA_AFTER,
 cap_ml="ജോലിക്കൊപ്പം ബേബി സ്ലിംഗ് ബ്രാൻഡ് നടത്തുന്ന ദീപ്തി മെറ്റേണിറ്റി ലീവിൽ ബിസിനസ് ഒരു വർഷം നിർത്തി വെച്ചു. വരുമാനം ഇല്ലാത്ത വർഷവും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് നിർബന്ധമാണ്. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A salaried mother paused her side brand for a year of maternity leave and assumed the company could skip its filings. Annual filings are due even in a year with zero revenue, and late forms cost Rs 100 per day each. Note the ROC due dates before the break starts.",
 cap_mg="Job-inte koode baby sling brand nadathunna Deepthi maternity leave-il business oru varsham nirthi. Revenue illaatha varshavum company annual filing nirbandham aanu. Vaikiyaal oro form-inum divasam 100 roopa penalty.")

# mobileshop: Hanna + Fahad. Fahad, a sales executive, runs a phone-repair YouTube channel and wants it as a company of his own, alone.
duo("d1216", "salaried", "A", "mobileshop", "സെയിൽസ് ജോലി. രാത്രി\nഫോൺ റിപ്പയർ യൂട്യൂബ്.\nകമ്പനി ഒറ്റയ്ക്ക് പറ്റുമോ?", [
 ("A","wide","ഫഹദിക്കാ, ഇന്നലത്തെ വീഡിയോ ഒരു ലക്ഷം വ്യൂസ്! ഡിസ്പ്ലേ മാറ്റുന്നത് ഞാൻ വരെ പഠിച്ചു."),
 ("V","V","ഹന്നാ, ടൂൾ കിറ്റ് ബ്രാൻഡുകൾ സ്പോൺസർഷിപ്പ് ചോദിക്കുന്നു. കമ്പനിയുടെ പേരിൽ എഗ്രിമെന്റ് വേണമെന്ന്."),
 ("A","A","പകൽ ഷോറൂമിൽ സെയിൽസ്. രാത്രി യൂട്യൂബ്. ആരെ കൂട്ടുപിടിക്കും?"),
 ("V","V","അതാ പ്രശ്നം. കമ്പനിക്ക് രണ്ടുപേർ വേണ്ടേ? ആരും ഇല്ല."),
 ("A","wide","ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി, OPC. ഒരാൾക്ക് മാത്രമായി കമ്പനി."),
 ("V","V","അപ്പോ ചാനലും കമ്പനിയും എന്റേത് മാത്രം!"),
 ("A","A","പിന്നീട് നിക്ഷേപം വേണ്ടി വന്നാൽ പ്രൈവറ്റ് ലിമിറ്റഡ് ആലോചിക്കാം."),
 ("V","wide","എന്നാൽ അടുത്ത വീഡിയോ: കമ്പനി എങ്ങനെ റിപ്പയർ ചെയ്യാം. ഹ ഹ!")],
 "സൈഡ് ബിസിനസ് ഒറ്റയ്ക്ക്?\nOPC നോക്കൂ", CTA_START,
 cap_ml="ഷോറൂമിൽ സെയിൽസ് ജോലി ചെയ്യുന്ന ഫഹദിന്റെ ഫോൺ റിപ്പയർ യൂട്യൂബ് ചാനലിന് ബ്രാൻഡ് സ്പോൺസർഷിപ്പ് വരുന്നു, കമ്പനിയുടെ പേരിൽ എഗ്രിമെന്റ് വേണം. ഒറ്റയ്ക്കാണെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC) ആയി തുടങ്ങാം. നിക്ഷേപം വേണ്ടി വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡ് ആലോചിക്കാം.",
 cap_en="A salaried sales executive's phone-repair YouTube channel is getting brand sponsorships that need a company agreement, and he has no partner. A solo founder can register a One Person Company (OPC). If investors come in later, a private limited company is the structure that can take equity.",
 cap_mg="Showroom-il sales job cheyyunna Fahad-nte phone repair YouTube channel-nu sponsorship varunnu, company perilulla agreement venam. Ottaykkaanenkil One Person Company (OPC) aayi thudangaam. Investment venamenkil pinne Pvt Ltd nokkaam.")
