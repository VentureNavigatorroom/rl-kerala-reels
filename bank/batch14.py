# Script bank, batch 14. New situations: a cartoonist whose comic cat a toy company wants for 25%, a game-music composer in a
# Kakkanad co-living room, a medical illustrator at day 172 with a textbook deadline, a Varkala surf photographer with a rainy
# zero-revenue year, a thesis editor whose sister in Melbourne will be co-director, a calligrapher with 500 Christmas gift tags and
# one name; night food for hospital staff where a doctor wants shares, Fort Kochi electric-auto tours named after the metro, a
# pickleball pair where one wants to be the only director, destination-wedding planners in the off-season, kids' nature camps run
# from a father's flat, pharmacy graduates whose cofounder leaves for Ireland; a supermarket manager's juice counter for the
# Mandalam pilgrim season, a service advisor whose company certificate lands three days before the honeymoon, an estate officer's
# bungalow-booking site named after a tea brand, a tower technician about to pawn gold for "capital", a Wayanad remote worker's
# coffee subscription in his mother's house, a lab technician who changed jobs at day 175.
# Same fact list and no-price rule as batch01. Segments freelancer 7, cofounders 6, salaried 7; 15 duo3d in 15 different locations
# (none used in batch13, all among the least used), default names. Every script carries cap_ml / cap_en / cap_mg.
# Audience data: 16 posts, none 2+ days old, so no audience-led shift (see INSIGHTS.md run 6).
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
# metro: Anjali + Kiran. Kiran draws a comic cat; a toy company will fund soft toys for 25% of "his company", but he is a proprietor.
duo("d1601", "freelancer", "A", "metro", "കാർട്ടൂൺ പൂച്ചയ്ക്ക്\nടോയ് കമ്പനിയുടെ ഓഫർ:\n\"25% ഷെയർ തരൂ\"", [
 ("V","wide","അഞ്ജലീ, എന്റെ കാർട്ടൂൺ പൂച്ച കുഞ്ഞാപ്പിയെ സോഫ്റ്റ് ടോയ് ആക്കണമെന്ന് ഒരു ടോയ് കമ്പനി!"),
 ("A","A","കിരൺ, ഇൻസ്റ്റയിൽ മാത്രം ജീവിച്ച പൂച്ച ഇനി കുട്ടികളുടെ കട്ടിലിൽ! സൂപ്പർ."),
 ("V","V","അവർ പൈസ ഇടും. പകരം എന്റെ കമ്പനിയിൽ ഇരുപത്തഞ്ച് ശതമാനം ഷെയർ വേണമെന്ന്."),
 ("A","A","നിന്റെ കമ്പനിയോ? നീ ഫ്രീലാൻസർ അല്ലേ? ബില്ല് പോലും നിന്റെ സ്വന്തം പേരിലാണല്ലോ."),
 ("V","V","അത്… പൂച്ചയുടെ പേരിൽ ഒരു കമ്പനി ഉണ്ടെന്ന് ഞാൻ അങ്ങ് പറഞ്ഞുപോയി."),
 ("A","wide","ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി തന്നെ വേണം. പ്രൊപ്രൈറ്റർഷിപ്പിനും പാർട്ണർഷിപ്പിനും LLP-ക്കും പറ്റില്ല."),
 ("V","V","പ്രൈവറ്റ് ലിമിറ്റഡിന് രണ്ടുപേർ വേണ്ടേ? ഞാനും പൂച്ചയും പോരേ?"),
 ("A","A","പൂച്ചയ്ക്ക് ആധാർ ഇല്ല മോനേ. കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം."),
 ("V","wide","എങ്കിൽ അനിയനെ വിളിക്കാം. പൂച്ചയുടെ അമ്മാവൻ!")],
 "ഷെയർ കൊടുക്കണോ?\nആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്", CTA_START,
 cap_ml="കാർട്ടൂണിസ്റ്റിന്റെ പൂച്ച കഥാപാത്രത്തെ സോഫ്റ്റ് ടോയ് ആക്കാൻ ഒരു ടോയ് കമ്പനി പൈസ ഇടാം, പകരം 25% ഷെയർ. ഫ്രീലാൻസർ ആയി, സ്വന്തം പേരിൽ ബിൽ ചെയ്താൽ ഷെയർ കൊടുക്കാൻ പറ്റില്ല; അതിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം.",
 cap_en="A Kerala cartoonist gets an offer: a toy company will fund soft toys of his comic cat in exchange for 25% shares. A freelancer or proprietorship cannot issue shares; to take equity investment you need a private limited company with two directors and two shareholders.",
 cap_mg="Cartoonist-nte poocha character-ne soft toy aakkan toy company paisa idaam, pakaram 25% share. Freelancer aayi swantham peril bill cheythal share kodukkan pattilla. Investment edukkan Pvt Ltd company venam.")

# cafe: Alvin + Roshan. Roshan composes game music from a Kakkanad co-living room; the studio signs only with his company; whose NOC?
duo("d1602", "freelancer", "B", "cafe", "കോ-ലിവിംഗിൽ താമസം.\nകമ്പനി ഓഫീസ് അഡ്രസ്സ്\nഏത് കൊടുക്കും?", [
 ("A","wide","റോഷാ, ഹെഡ്ഫോൺ ഊരിയിട്ട് പറ. ഗെയിം സ്റ്റുഡിയോയുടെ കരാർ എന്തായി?"),
 ("V","V","ആൽവിനേ, മൂന്ന് ഗെയിമിന് മ്യൂസിക്. പക്ഷേ എന്റെ കമ്പനിയുമായി മാത്രമേ ഒപ്പിടൂ എന്ന്."),
 ("A","A","അപ്പോ കമ്പനി തുടങ്ങ്. എവിടെയാ ഓഫീസ്?"),
 ("V","V","കാക്കനാട്ടെ കോ-ലിവിംഗ് റൂം. ആറുപേരും ഒരു ഫ്രിഡ്ജും. അത് അഡ്രസ്സ് ആക്കാൻ പറ്റുമോ?"),
 ("A","wide","താമസിക്കുന്ന സ്ഥലം രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. പക്ഷേ ഉടമയുടെ NOC വേണം, പിന്നെ പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും."),
 ("V","V","ഞാൻ എന്നും സംസാരിക്കുന്നത് മാനേജറോട് ആണ്. ബിൽഡിംഗിന്റെ ഉടമ വേറെ ആളാ."),
 ("A","A","അതാ കാര്യം. ആരുടെ പേരിലാണോ സ്ഥലം, അവരുടെ NOC. കറന്റ് ബില്ലിന്റെ പുതിയ കോപ്പിയും ചോദിക്ക്."),
 ("V","wide","ഇന്ന് തന്നെ മെസ്സേജ് അയക്കാം. ബാക്ക്ഗ്രൗണ്ട് മ്യൂസിക് ഇട്ട്!")],
 "വാടക മുറിയും\nകമ്പനി ഓഫീസ് ആകാം", CTA_DOCS,
 cap_ml="കാക്കനാട്ടെ കോ-ലിവിംഗ് മുറിയിൽ താമസിക്കുന്ന ഗെയിം മ്യൂസിക് കമ്പോസർക്ക് കമ്പനി വേണം. താമസിക്കുന്ന സ്ഥലം രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം, പക്ഷേ മാനേജറുടെ അല്ല, കെട്ടിട ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം.",
 cap_en="A freelance game-music composer in a Kakkanad co-living room needs a company before the studio signs. Your rented room can be the registered office for company registration in Kochi, but you need the property owner's NOC (not the manager's) and a recent utility bill.",
 cap_mg="Kakkanad co-living room-il thaamasikkunna game music composer-nu company venam. Thaamasikkunna sthalam registered office aakkam, pakshe building owner-nte NOC-um puthiya utility bill-um venam. Company register cheyyan ithu aadyam ready aakku.")

# hospital: Lakshmi + Joseph. Lakshmi draws anatomy for a textbook due Friday; her company is 172 days old and INC-20A is not filed.
duo("d1603", "freelancer", "C", "hospital", "അനാട്ടമി ടെക്സ്റ്റ്ബുക്ക് ഡെഡ്‌ലൈൻ.\nകമ്പനിക്ക് 172 ദിവസം", [
 ("V","wide","ലക്ഷ്മീ, ഇന്നും രാത്രി മുഴുവൻ ഹൃദയം വരയ്ക്കുവാണോ?"),
 ("A","A","ജോസഫേ, ടെക്സ്റ്റ്ബുക്കിന് നാൽപ്പത് ചിത്രം വെള്ളിയാഴ്ചയ്ക്കുള്ളിൽ. ഹൃദയവും വൃക്കയും എല്ലാം ഞാൻ തന്നെ."),
 ("V","V","കമ്പനി തുടങ്ങിയിട്ട് എത്ര ദിവസമായി?"),
 ("A","A","നൂറ്റി എഴുപത്തിരണ്ട്. എന്താ, പിറന്നാൾ ആഘോഷിക്കണോ?"),
 ("V","wide","ആഘോഷം അല്ല. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം. ബിസിനസ് തുടങ്ങി എന്ന് കാണിക്കുന്ന ഫോം."),
 ("A","A","എട്ട് ദിവസമേ ബാക്കിയുള്ളോ? മിസ്സ് ആയാൽ എന്താ?"),
 ("V","V","കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർക്ക് ദിവസം ആയിരം രൂപ വേറെ, ഒരു ലക്ഷം വരെ."),
 ("A","wide","ആ കണക്ക് കേട്ടപ്പോൾ എന്റെ സ്വന്തം ഹൃദയം ഒന്ന് നിന്നു."),
 ("V","V","നാളെ രാവിലെ ആദ്യം ഫോം. പിന്നെ വൃക്ക.")],
 "180 ദിവസം കഴിയും മുമ്പ്\nINC-20A", CTA_AFTER,
 cap_ml="ടെക്സ്റ്റ്ബുക്കിന് അനാട്ടമി ചിത്രങ്ങൾ വരയ്ക്കുന്ന മെഡിക്കൽ ഇല്ലസ്ട്രേറ്ററുടെ കമ്പനിക്ക് 172 ദിവസം, INC-20A ഇതുവരെ ഇല്ല. 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർക്ക് ദിവസം 1,000 രൂപ (1 ലക്ഷം വരെ).",
 cap_en="A freelance medical illustrator in Kerala is 172 days into her company and buried in a textbook deadline. INC-20A, the commencement of business form, is due within 180 days of incorporation: miss it and the penalty is 50,000 on the company plus 1,000 a day per officer, up to 1 lakh.",
 cap_mg="Textbook-nu anatomy chithram varakkunna medical illustrator-nte company-kku 172 divasam, INC-20A ithuvare illa. 180 days-inullil file cheythillenkil company-kku 50,000 pizha, director-kku divasam 1,000 (1 lakh vare).")

# beach: Divya + Nikhil. Nikhil photographs surfers at Varkala; in the monsoon there are no surfers and no income; he wants to skip filing.
duo("d1604", "freelancer", "B", "beach", "മഴക്കാലം. തിരയുണ്ട്,\nസർഫറില്ല, വരുമാനവുമില്ല", [
 ("A","wide","നിഖിലേ, ക്യാമറ കവറിൽ ഇട്ട് കടലും നോക്കി ഇരിപ്പാണോ?"),
 ("V","V","ദിവ്യേ, മഴക്കാലം ആയതോടെ വർക്കലയിൽ സർഫ് ചെയ്യാൻ ആരുമില്ല. ഫോട്ടോയും ഇല്ല, വരുമാനവും ഇല്ല."),
 ("A","A","കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് സമയം ആയില്ലേ?"),
 ("V","V","ഈ വർഷം കാര്യമായ വരുമാനം ഇല്ല. പിന്നെന്തിന് ഫയലിംഗ്? കടലിന് പോലും അറിയാം."),
 ("A","wide","കടലിന് അറിയാം, പക്ഷേ നിയമത്തിന് അറിയില്ല. വരുമാനം പൂജ്യം ആണെങ്കിലും ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("V","V","വൈകിയാലോ?"),
 ("A","A","ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. മഴ പോലെ നിർത്താതെ കൂടും."),
 ("V","wide","എങ്കിൽ ആദ്യം ഫയലിംഗ്. പിന്നെ അടുത്ത സീസണിലെ തിര!")],
 "വരുമാനം ഇല്ലാത്ത വർഷവും\nഫയലിംഗ് ഉണ്ട്", CTA_AFTER,
 cap_ml="വർക്കലയിലെ സർഫ് ഫോട്ടോഗ്രാഫർക്ക് മഴക്കാലത്ത് വരുമാനം ഇല്ല, അതുകൊണ്ട് ഫയലിംഗും വേണ്ടെന്ന് കരുതി. വരുമാനം പൂജ്യം ആയാലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.",
 cap_en="A Varkala surf photographer's company earns nothing in the monsoon, so he plans to skip annual filing. ROC annual filing is due even with zero revenue, and filing late costs a penalty of 100 per day for each form.",
 cap_mg="Varkala-yile surf photographer-nu mazhakkaalathu varumanam illa, athukondu filing-um venda ennu karuthi. Varumanam zero aayaalum company annual filing cheyyanam; vaikiyal oro form-inum divasam 100 pizha.")

# library: Greeshma + Anoop. Greeshma edits PhD theses; her sister in Melbourne should be the second director; someone said NRIs can't.
duo("d1605", "freelancer", "A", "library", "തീസിസ് എഡിറ്റിംഗ് കമ്പനി.\nരണ്ടാമത്തെ ഡയറക്ടർ\nഓസ്ട്രേലിയയിൽ", [
 ("V","wide","ഗ്രീഷ്മേ, ഈ ലൈബ്രറിയിലെ പകുതി ഗവേഷകരും നിന്റെ ക്ലയന്റ്സ് ആണല്ലോ."),
 ("A","A","അനൂപേ, ഇപ്പോ ബാംഗ്ലൂരിലെ രണ്ട് യൂണിവേഴ്സിറ്റിയിൽ നിന്നും വർക്ക് വരുന്നു. കമ്പനി ആക്കാൻ സമയമായി."),
 ("V","V","പ്രൈവറ്റ് ലിമിറ്റഡിന് രണ്ട് ഡയറക്ടർ വേണ്ടേ? രണ്ടാമത്തെ ആൾ?"),
 ("A","A","എന്റെ സഹോദരി. പക്ഷേ അവൾ മെൽബണിൽ ആണ്. അതുകൊണ്ട് നടക്കില്ല എന്ന് ആരോ പറഞ്ഞു."),
 ("V","wide","നടക്കും. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("V","V","ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. അത് നീ തന്നെ."),
 ("A","A","അപ്പോ ഞാൻ ഇവിടെ കോമ തിരുത്തും. അവൾ അവിടെ ബോർഡ് മീറ്റിംഗിന് ഉറക്കമൊഴിക്കും."),
 ("V","wide","ടൈം സോൺ കൊണ്ട് ഒരു ഗുണം. കമ്പനി ഇരുപത്തിനാല് മണിക്കൂറും ഉണർന്നിരിക്കും!")],
 "പങ്കാളി വിദേശത്താണോ?\nഡയറക്ടർ ആകാം", CTA_START,
 cap_ml="പിഎച്ച്ഡി തീസിസ് എഡിറ്റ് ചെയ്യുന്ന ഫ്രീലാൻസർക്ക് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം, രണ്ടാമത്തെ ഡയറക്ടർ ഓസ്ട്രേലിയയിലുള്ള സഹോദരി. NRI-ക്കും ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം; ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി.",
 cap_en="A Kerala freelancer who edits PhD theses wants a private limited company with her sister in Melbourne as co-director. NRIs can be directors and shareholders of an Indian Pvt Ltd; you just need at least one director resident in India.",
 cap_mg="PhD thesis edit cheyyunna freelancer-nu Pvt Ltd company venam, randamathe director Australia-yil ulla sister. NRI-kkum director-um shareholder-um aakaam; oru director India-yil thaamasikkunna aal aayal mathi.")

# chat: Arathi + Devika. Arathi does calligraphy; an IT company wants 500 Christmas gift tags billed by a company in 15 days; one name only.
chat("c981", "freelancer", "B", "ക്രിസ്മസ് ഗിഫ്റ്റിന് 500 ടാഗ്.\nകമ്പനി പേര്: ഒന്ന് മാത്രം", ("ആരതി", "ദേവിക"), [
 (0,"ദേവൂ, ഒരു ഐടി കമ്പനി അവരുടെ ക്രിസ്മസ് ഗിഫ്റ്റിന് അഞ്ഞൂറ് കാലിഗ്രഫി ടാഗ് ചോദിച്ചു!"),
 (1,"ആരതീ, നിന്റെ കൈയക്ഷരം ഇനി കോർപ്പറേറ്റ്! എപ്പോ വേണം?"),
 (0,"പതിനഞ്ച് ദിവസം കഴിഞ്ഞ്. പക്ഷേ ബില്ല് കമ്പനിയിൽ നിന്ന് വേണം. അതുകൊണ്ട് രജിസ്ട്രേഷൻ ഇന്ന് തുടങ്ങുന്നു."),
 (1,"പേര് റെഡിയാണോ?"),
 (0,"ഒന്നേ ഉള്ളൂ. ഇങ്ക് ആൻഡ് ഗ്രേസ്. വേറെ ആലോചിച്ചിട്ടില്ല."),
 (1,"ഒന്നിൽ നിർത്തല്ലേ. നിലവിലുള്ള കമ്പനിയോടോ ട്രേഡ്മാർക്കിനോടോ സാമ്യം ഉണ്ടെങ്കിൽ പേര് റിജക്ട് ആകാം."),
 (1,"റിജക്ട് ആയാൽ വീണ്ടും അപേക്ഷ. പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ തന്നെ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം."),
 (0,"അയ്യോ. അപ്പോ ഇന്ന് രാത്രി മൂന്ന് പേര് എഴുതാം. നല്ല കൈയക്ഷരത്തിൽ തന്നെ!")],
 "ഒരു പേര് പോരാ,\nമൂന്ന് കരുതൂ", CTA_NAME,
 cap_ml="കാലിഗ്രഫി ആർട്ടിസ്റ്റിന് ക്രിസ്മസിന് 500 ഗിഫ്റ്റ് ടാഗിന്റെ കോർപ്പറേറ്റ് ഓർഡർ, ബില്ല് കമ്പനിയിൽ നിന്ന് വേണം, പേര് ഒന്നേ ഉള്ളൂ. സാമ്യമുള്ള പേര് റിജക്ട് ആയാൽ ദിവസങ്ങൾ പോകും; മൂന്ന് കമ്പനി പേരുകൾ കരുതൂ.",
 cap_en="A freelance calligrapher gets a corporate order for 500 Christmas gift tags, billed by a company, and has only one company name in mind. Names similar to an existing company or a trademark get rejected, and Pvt Ltd registration already takes 7-15 working days, so keep three names ready.",
 cap_mg="Calligraphy artist-nu Christmas-nu 500 gift tag corporate order, bill company-yil ninnu venam, company name onne ullu. Saamyam ulla name reject aayaal divasangal pokum; moonnu company names karuthu.")

lst("l981", "freelancer", "C", "ഫ്രീലാൻസർ: OPC-യോ\nപ്രൈവറ്റ് ലിമിറ്റഡോ?\n3 ചോദ്യം കൊണ്ട് തീരുമാനിക്കാം", [
 ("ഒറ്റയ്ക്കാണോ?", "കൂടെ ആരുമില്ലെങ്കിൽ വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം. പാർട്ണറെ കടം വാങ്ങേണ്ട."),
 ("ആരെങ്കിലും ഷെയർ ചോദിക്കുന്നുണ്ടോ?", "ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം. അതിന് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ."),
 ("പങ്കാളി വിദേശത്താണോ?", "NRI-ക്കും ഡയറക്ടർ ആകാം. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.")],
 "ശരിയായ സ്ട്രക്ചർ\nആദ്യം", CTA_START,
 cap_ml="ഫ്രീലാൻസർ കമ്പനി ആക്കുമ്പോൾ OPC വേണോ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണോ? ഒറ്റയ്ക്കാണെങ്കിൽ OPC; ആരെങ്കിലും ഷെയർ ചോദിക്കുന്നുണ്ടെങ്കിൽ Pvt Ltd; പങ്കാളി വിദേശത്താണെങ്കിൽ ഒരു ഡയറക്ടർ നാട്ടിൽ.",
 cap_en="Freelancer in Kerala choosing between a One Person Company and a private limited company? Alone: OPC. Someone wants shares: Pvt Ltd with two directors and two shareholders. Partner abroad: fine, as long as one director lives in India.",
 cap_mg="Freelancer company aakkumbol OPC venO Pvt Ltd venO? Ottaykku aanenkil One Person Company; aarenkilum share chodikkunnundenkil Pvt Ltd; partner videshathaanenkil oru director naattil.")

# ---------------- cofounders ----------------
# thattukada: Sijo + Biju. Their night-food delivery for hospital staff is a partnership; a cardiologist wants to invest for shares.
duo("d1606", "cofounders", "A", "thattukada", "രാത്രി ഷിഫ്റ്റ് ഡോക്ടർമാർക്ക്\nപുട്ടും ബീഫും.\nഒരു ഡോക്ടർ ഷെയർ ചോദിക്കുന്നു", [
 ("A","wide","ബിജൂ, മൂന്ന് ആശുപത്രിയിലേക്കുള്ള രാത്രി ഓർഡർ റെഡി. നൂറ്റിയിരുപത് പുട്ട്!"),
 ("V","V","സിജോ, ഒരു വാർത്ത. കാർഡിയോളജിയിലെ ഡോക്ടർ ഇന്നലെ ചോദിച്ചു, നമ്മുടെ ബിസിനസിൽ പൈസ ഇടട്ടേ എന്ന്."),
 ("A","A","ആഹാ! നമ്മുടെ ബീഫ് ഡോക്ടറുടെ ഹൃദയം കീഴടക്കി!"),
 ("V","V","പകരം ഷെയർ വേണം. നമ്മൾ രണ്ടുപേരും പാർട്ണർഷിപ്പ് അല്ലേ. അതിൽ ഷെയർ കൊടുക്കാമോ?"),
 ("A","wide","ഇല്ല. ഷെയർ കൊടുത്ത് പൈസ വാങ്ങാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം. പാർട്ണർഷിപ്പിനും LLP-ക്കും പറ്റില്ല."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനി. നമ്മൾ രണ്ടുപേരും ഡയറക്ടർ."),
 ("A","A","അതെ. ഡോക്ടർ പിന്നെ ഷെയർഹോൾഡർ. പക്ഷേ ഒരു കാര്യം. ബീഫിന്റെ റെസിപ്പി ഷെയർ ചെയ്യില്ല!"),
 ("V","wide","അത് ട്രേഡ് സീക്രട്ട്. ഡോക്ടർക്ക് പോലും ഓപ്പറേറ്റ് ചെയ്ത് എടുക്കാൻ പറ്റില്ല!")],
 "ഇൻവെസ്റ്റർ വന്നോ?\nആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ്", CTA_START,
 cap_ml="ആശുപത്രി ജീവനക്കാർക്ക് രാത്രി ഭക്ഷണം എത്തിക്കുന്ന രണ്ട് കൂട്ടുകാരുടെ പാർട്ണർഷിപ്പിൽ ഒരു ഡോക്ടർ പൈസ ഇടാം, പകരം ഷെയർ. പാർട്ണർഷിപ്പിനും LLP-ക്കും ഷെയർ കൊടുക്കാൻ പറ്റില്ല; ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി.",
 cap_en="Two friends deliver night food to hospital staff in Kochi, and a doctor wants to invest for shares. A partnership or LLP cannot take equity investment; convert to a private limited company first, with both founders as directors.",
 cap_mg="Hospital staff-nu raathri food ethikkunna randu friends-nte partnership-il oru doctor paisa idaam, pakaram share. Partnership-inum LLP-kkum share kodukkan pattilla; aadyam Pvt Ltd company register cheyyu.")

# autostand: Saji + Shaji. Electric-auto tours of Fort Kochi; Shaji wants the name "Kochi Metro Autos".
duo("d1607", "cofounders", "B", "autostand", "ഫോർട്ട് കൊച്ചിയിൽ ഇലക്ട്രിക്\nഓട്ടോ ടൂർ. പേര്:\n\"കൊച്ചി മെട്രോ ഓട്ടോസ്\"", [
 ("V","wide","സജിയേട്ടാ, പത്ത് ഇലക്ട്രിക് ഓട്ടോ. വിദേശികളെ ഫോർട്ട് കൊച്ചി മുഴുവൻ കാണിക്കുന്ന ടൂർ. കമ്പനി ആക്കാം!"),
 ("A","A","ഷാജീ, ഐഡിയ കൊള്ളാം. പേര് ഇട്ടോ?"),
 ("V","V","കൊച്ചി മെട്രോ ഓട്ടോസ്. മെട്രോ എന്ന് കേട്ടാൽ ആളുകൾക്ക് പെട്ടെന്ന് വിശ്വാസം വരും."),
 ("A","wide","അതാ പ്രശ്നം. നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ നമ്മുടെ പേര് റിജക്ട് ആകാം."),
 ("A","A","കൊച്ചിയിൽ മെട്രോ എന്ന് കേട്ടാൽ ആദ്യം ആരെ ഓർക്കും?"),
 ("V","V","ട്രെയിനിനെ. അയ്യോ, അത് ഞാൻ ഓർത്തില്ല."),
 ("A","A","നമ്മുടേതായ ഒരു പേര് വേണം. സാമ്യമില്ലാത്ത രണ്ടുമൂന്ന് പേരും കരുതണം."),
 ("V","wide","എങ്കിൽ ചീനവല ഓട്ടോസ്. വല വീശി ടൂറിസ്റ്റിനെ പിടിക്കാം!")],
 "വലിയ പേരിന്റെ നിഴലിൽ\nനിൽക്കരുത്", CTA_NAME,
 cap_ml="ഫോർട്ട് കൊച്ചിയിൽ ഇലക്ട്രിക് ഓട്ടോ ടൂർ തുടങ്ങുന്ന രണ്ട് കൂട്ടുകാർക്ക് കമ്പനിക്ക് 'കൊച്ചി മെട്രോ ഓട്ടോസ്' എന്ന് പേര് വേണം. നിലവിലുള്ള കമ്പനിയുടെ പേരിനോട് സാമ്യം ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം; സ്വന്തമായ, വേറിട്ട പേരുകൾ കരുതൂ.",
 cap_en="Two cofounders launching electric-auto tours in Fort Kochi want to call their company 'Kochi Metro Autos'. A company name close to an existing company's name can be rejected; pick something of your own and keep backups.",
 cap_mg="Fort Kochi-yil electric auto tour thudangunna randu friends-nu company-kku 'Kochi Metro Autos' ennu peru venam. Existing company-yude perinodu saamyam undenkil reject aakaam; swanthamaaya company name-um backup-um karuthu.")

# gym: Riya + Justin. Pickleball coaching; Justin wants to be the only director and Riya only a shareholder.
duo("d1608", "cofounders", "B", "gym", "പിക്കിൾബോൾ കോച്ചിംഗ്.\n\"ഡയറക്ടർ ഞാൻ മാത്രം,\nനീ ഷെയർ മാത്രം\"", [
 ("V","wide","റിയ, പിക്കിൾബോൾ ബാച്ച് ഫുൾ! അടുത്ത മാസം രണ്ട് കോർട്ട് കൂടി എടുക്കാം."),
 ("A","A","ജസ്റ്റിൻ, അപ്പോ കമ്പനി ഇപ്പോ തന്നെ രജിസ്റ്റർ ചെയ്യണം."),
 ("V","V","ഒരു പ്ലാൻ ഉണ്ട്. ഡയറക്ടർ ഞാൻ മാത്രം. നിനക്ക് പകൽ ജോലിയുണ്ടല്ലോ, നീ ഷെയർ മാത്രം എടുത്താൽ മതി."),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡിന് കുറഞ്ഞത് രണ്ട് ഡയറക്ടറും രണ്ട് ഷെയർഹോൾഡറും വേണം. ഒരു ഡയറക്ടർ കൊണ്ട് നടക്കില്ല."),
 ("V","V","അപ്പോ രണ്ടുപേരും ഡയറക്ടർ. രണ്ടുപേരും ഷെയർഹോൾഡർ."),
 ("A","A","അതേ. ആ രണ്ടുപേർ തന്നെ മതി. നാല് പേരെ തേടി നടക്കണ്ട."),
 ("V","V","എന്നാൽ ബോർഡ് മീറ്റിംഗ് കോർട്ടിൽ വെച്ച്. തോൽക്കുന്നയാൾ മിനിറ്റ്സ് എഴുതും!"),
 ("A","wide","അപ്പോ എല്ലാ മിനിറ്റ്സും നീ തന്നെ എഴുതേണ്ടി വരും.")],
 "ഒരാൾ കൊണ്ട്\nപ്രൈവറ്റ് ലിമിറ്റഡ് ആകില്ല", CTA_START,
 cap_ml="പിക്കിൾബോൾ കോച്ചിംഗ് തുടങ്ങുന്ന രണ്ടുപേരിൽ ഒരാൾക്ക് ഡയറക്ടർ ഒറ്റയ്ക്ക് മതി, മറ്റേയാൾ ഷെയർഹോൾഡർ മാത്രം. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് കുറഞ്ഞത് 2 ഡയറക്ടറും 2 ഷെയർഹോൾഡറും വേണം; അതേ രണ്ടുപേർ ആകാം.",
 cap_en="Two cofounders start a pickleball coaching business in Kerala and one wants to be the only director. A private limited company needs at least two directors and two shareholders, and the same two people can be both.",
 cap_mg="Pickleball coaching thudangunna randu peril oraalkku director ottaykku mathi ennu. Pvt Ltd company-kku kuranjathu 2 director-um 2 shareholder-um venam; athe randu per thanne aakaam.")

# hotellobby: Neethu + Jaison. Destination-wedding planners; no weddings this off-season, so they plan to skip annual filing.
duo("d1609", "cofounders", "C", "hotellobby", "ഡെസ്റ്റിനേഷൻ വെഡ്ഡിംഗ് കമ്പനി.\nഓഫ് സീസണിൽ കല്യാണമില്ല.\nഫയലിംഗും വേണ്ടേ?", [
 ("V","wide","നീതു, ഈ ലോബിയിൽ ഇരുന്നാൽ കഴിഞ്ഞ സീസണിലെ പതിനെട്ട് കല്യാണം ഓർമ്മ വരുന്നു."),
 ("A","A","ജെയ്സൺ, ഇപ്പോ ബുക്കിംഗ് ഒന്നുമില്ല. ഈ വർഷം കമ്പനിക്ക് വരുമാനം ഏതാണ്ട് പൂജ്യം."),
 ("V","V","എങ്കിൽ ഫയലിംഗ് ഈ വർഷം സ്കിപ്പ് ചെയ്യാം. കല്യാണം ഇല്ലെങ്കിൽ കണക്കും ഇല്ലല്ലോ."),
 ("A","wide","അങ്ങനെ ഇല്ല. വരുമാനം കുറഞ്ഞാലും പൂജ്യം ആയാലും കമ്പനിയുടെ ആനുവൽ ഫയലിംഗ് ചെയ്യണം."),
 ("V","V","മിസ്സ് ആയാൽ?"),
 ("A","A","ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ. കല്യാണപ്പന്തലിലെ പൂവിനേക്കാൾ വേഗം കൂടും."),
 ("V","V","ശരി. ഓഫ് സീസൺ ഇനി ഫയലിംഗ് സീസൺ."),
 ("A","wide","പിന്നെ അടുത്ത കല്യാണ സീസണിന് ഫ്രഷ് ആയി ഇറങ്ങാം!")],
 "ഓഫ് സീസണിലും\nഫയലിംഗ് ഓൺ", CTA_AFTER,
 cap_ml="ഡെസ്റ്റിനേഷൻ വെഡ്ഡിംഗ് പ്ലാൻ ചെയ്യുന്ന രണ്ട് കോ-ഫൗണ്ടർമാർക്ക് ഓഫ് സീസണിൽ ബുക്കിംഗ് ഇല്ല, അതുകൊണ്ട് ഫയലിംഗ് സ്കിപ്പ് ചെയ്യാമെന്ന് കരുതി. വരുമാനം പൂജ്യം ആയാലും ആനുവൽ ഫയലിംഗ് വേണം; വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.",
 cap_en="Destination-wedding planners in Kerala have no bookings this off-season and want to skip the company's annual filing. Annual filings with the ROC are due even with zero revenue, and filing late costs 100 per day per form.",
 cap_mg="Destination wedding plan cheyyunna randu cofounders-nu off season-il booking illa, athukondu filing skip cheyyaam ennu karuthi. Varumanam zero aayaalum annual filing venam; vaikiyal oro form-inum divasam 100.")

# park: Gayathri + Ananthu. Kids' nature camps; the office will be Ananthu's father's flat and "no papers are needed".
duo("d1610", "cofounders", "A", "park", "കുട്ടികളുടെ നേച്ചർ ക്യാമ്പ്.\nഓഫീസ് അച്ഛന്റെ ഫ്ലാറ്റിൽ.\n\"പേപ്പർ ഒന്നും വേണ്ട\"", [
 ("A","wide","അനന്തു, ഈ ശനിയാഴ്ച നാൽപ്പത് കുട്ടികൾ. പക്ഷികളെ കാണാൻ, പൂമ്പാറ്റകളെ എണ്ണാൻ!"),
 ("V","V","ഗായത്രീ, സ്കൂളുകൾ ഇപ്പോ ചോദിക്കുന്നു കമ്പനി ആണോന്ന്. നമുക്ക് രജിസ്റ്റർ ചെയ്യാം."),
 ("A","A","ഓഫീസ് അഡ്രസ്സ് എവിടെ കൊടുക്കും?"),
 ("V","V","അച്ഛന്റെ ഫ്ലാറ്റ്. എന്റെ സ്വന്തം അച്ഛൻ ആണല്ലോ, പേപ്പർ ഒന്നും വേണ്ട."),
 ("A","wide","സ്വന്തം അച്ഛൻ ആയാലും ഉടമ അച്ഛനാണ്. ഫ്ലാറ്റ് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC വേണം. പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും."),
 ("V","V","അച്ഛനോട് ഒപ്പ് ചോദിച്ചാൽ ആദ്യം ഒരു മണിക്കൂർ പ്ലാൻ മുഴുവൻ കേൾക്കും."),
 ("A","A","കേൾക്കട്ടെ. നമ്മുടെ ആദ്യത്തെ ബോർഡ് മീറ്റിംഗ് ആണെന്ന് കരുതിക്കോ."),
 ("V","wide","ശരി. ഇന്ന് രാത്രി അച്ഛന് ചായ ഞാൻ ഇട്ടുകൊടുക്കാം!")],
 "വീട്ടുകാരുടെ വീടായാലും\nNOC വേണം", CTA_DOCS,
 cap_ml="കുട്ടികൾക്ക് നേച്ചർ ക്യാമ്പ് നടത്തുന്ന രണ്ട് കോ-ഫൗണ്ടർമാരുടെ കമ്പനി ഓഫീസ് ഒരാളുടെ അച്ഛന്റെ ഫ്ലാറ്റിൽ. സ്വന്തം അച്ഛന്റേതായാലും ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും രജിസ്ട്രേഷന് വേണം.",
 cap_en="Two cofounders running kids' nature camps want their company's registered office at one founder's father's flat. Even a parent's home needs the owner's NOC and a recent utility bill for company registration in Kerala.",
 cap_mg="Kuttikalkku nature camp nadathunna randu cofounders-nte company office oraalude achante flat-il. Swantham achante aanenkilum owner-nte NOC-um puthiya utility bill-um company registration-nu venam.")

# chat: Saranya + Jishnu. Pharmacy graduates' medicine-reminder app; Saranya leaves for an MS in Ireland in January.
chat("c982", "cofounders", "A", "മരുന്ന് ഓർമ്മിപ്പിക്കുന്ന ആപ്പ്.\nകോ-ഫൗണ്ടർക്ക് അയർലണ്ടിൽ അഡ്മിഷൻ", ("ശരണ്യ", "ജിഷ്ണു"), [
 (0,"ജിഷ്ണൂ, അയർലണ്ടിൽ എംഎസ് അഡ്മിഷൻ കിട്ടി! ജനുവരിയിൽ പോകണം."),
 (1,"കൺഗ്രാറ്റ്സ്! പക്ഷേ നമ്മുടെ മരുന്ന് ഓർമ്മിപ്പിക്കുന്ന ആപ്പ്? കമ്പനി രജിസ്ട്രേഷൻ ഈ മാസം അല്ലേ?"),
 (0,"അതാ ടെൻഷൻ. ഞാൻ വിദേശത്ത് പോയാൽ ഡയറക്ടർ ആകാൻ പറ്റില്ലല്ലോ."),
 (1,"പറ്റും. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 (1,"ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്ന ആളാകണം. അത് ഞാൻ."),
 (0,"അപ്പോ ഞാൻ ഡബ്ലിനിൽ ഇരുന്ന് ആപ്പിന്റെ റിമൈൻഡർ നോക്കും. നീ ഇവിടെ കമ്പനിയുടെ ഡേറ്റുകളും."),
 (1,"ഡീൽ. ആദ്യത്തെ റിമൈൻഡർ: പോകും മുമ്പ് ഡോക്യുമെന്റ്സ് എല്ലാം തന്നിട്ട് പോകണം."),
 (0,"ശരി. ആപ്പിനേക്കാൾ സ്ട്രിക്ട് ആണല്ലോ നീ!")],
 "കോ-ഫൗണ്ടർ വിദേശത്തേക്കോ?\nകമ്പനി നടക്കും", CTA_START,
 cap_ml="മരുന്ന് ഓർമ്മിപ്പിക്കുന്ന ആപ്പ് തുടങ്ങുന്ന രണ്ട് ഫാർമസി ബിരുദധാരികളിൽ ഒരാൾ പഠിക്കാൻ അയർലണ്ടിലേക്ക്. വിദേശത്ത് പോയാലും ഡയറക്ടർ ആകാം; പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആയാൽ മതി.",
 cap_en="Two pharmacy graduates are building a medicine-reminder app, and one cofounder leaves for a master's in Ireland. She can still be a director and shareholder of their Indian private limited company, as long as one director lives in India.",
 cap_mg="Marunnu ormippikkunna app thudangunna randu pharmacy graduates-il oral padikkan Ireland-ilekku. Videshathu poyaalum director aakaam; Pvt Ltd-il oru director India-yil thaamasikkunna aal aayal mathi.")

# ---------------- salaried ----------------
# juiceshop: Rasiya + Noushad. Noushad manages a supermarket floor; a pilgrim-halt contractor offers juice counters for the Mandalam season.
duo("d1611", "salaried", "A", "juiceshop", "മണ്ഡലകാലത്ത് ഇടത്താവളത്തിൽ\nജ്യൂസ് കൗണ്ടർ.\nകരാർ കമ്പനിയുമായി മാത്രം", [
 ("A","wide","നൗഷാദിക്കാ, സൂപ്പർമാർക്കറ്റിലെ ഡ്യൂട്ടി കഴിഞ്ഞ് വന്നതേ ഫോണിൽ ആണല്ലോ."),
 ("V","V","റസിയാ, ഇടത്താവളത്തിലെ കോൺട്രാക്ടർ വിളിച്ചു. മണ്ഡലകാലം മുഴുവൻ നമ്മുടെ ജ്യൂസ് കൗണ്ടർ വെക്കാം എന്ന്."),
 ("A","A","നാൽപ്പത്തൊന്ന് ദിവസം, ആയിരക്കണക്കിന് തീർത്ഥാടകർ! ഇനി കരിമ്പ് തികയുമോ?"),
 ("V","V","പക്ഷേ കരാർ കമ്പനിയുമായി മാത്രം. മൂന്നാഴ്ചയ്ക്കുള്ളിൽ ഒപ്പിടണം. ഞാൻ ലീവ് കിട്ടുമ്പോൾ നോക്കാം."),
 ("A","wide","പിന്നെ അല്ല, ഇന്ന്. പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം എടുക്കും."),
 ("A","A","ഞാനും ഇക്കയും ഡയറക്ടർ. രണ്ടുപേരുടെയും ഡോക്യുമെന്റ്സ്, ഓഫീസ് അഡ്രസ്സിന്റെ പേപ്പർ, ഇന്ന് രാത്രി തന്നെ റെഡി."),
 ("V","V","ജോലിക്കിടയിൽ ഇതൊക്കെ നടക്കുമോ?"),
 ("A","wide","ഇക്ക ഷിഫ്റ്റ് നോക്ക്. പേപ്പർ ഞാൻ നോക്കാം. കരിമ്പ് നമ്മൾ രണ്ടുപേരും കൂടി!")],
 "സീസൺ കാത്തിരിക്കില്ല.\nരജിസ്ട്രേഷൻ ഇന്ന്", CTA_DOCS,
 cap_ml="സൂപ്പർമാർക്കറ്റിൽ ജോലി ചെയ്യുന്ന ഭർത്താവിനും ഭാര്യയ്ക്കും മണ്ഡലകാലത്ത് ഇടത്താവളത്തിൽ ജ്യൂസ് കൗണ്ടർ കരാർ, കമ്പനിയുമായി മാത്രം, മൂന്നാഴ്ചയ്ക്കുള്ളിൽ. Pvt Ltd രജിസ്ട്രേഷന് സാധാരണ 7 മുതൽ 15 പ്രവൃത്തി ദിവസം; ഡോക്യുമെന്റ്സ് ഇന്ന് തന്നെ.",
 cap_en="A salaried supermarket manager and his wife can run juice counters at a pilgrim halt for the whole Mandalam season, but the contractor signs only with a company within three weeks. Private limited company registration in Kerala usually takes 7-15 working days, so start the documents today.",
 cap_mg="Supermarket-il joli cheyyunna bharthavinum bharyakkum Mandalakaalathu idathavalathil juice counter contract, company-yumaayi maathram, moonnaazhchaykkullil. Pvt Ltd register cheyyan saadharana 7-15 working days; documents innu thanne.")

# garage: Aishwarya + Jithin. Jithin, a showroom service advisor, restores vintage bikes; the company certificate arrives three days before their honeymoon.
duo("d1612", "salaried", "B", "garage", "കമ്പനി സർട്ടിഫിക്കറ്റ് വന്നു.\nമൂന്ന് ദിവസം കഴിഞ്ഞ്\nഹണിമൂൺ, രണ്ടാഴ്ച", [
 ("A","wide","ജിതിൻ, ഷോറൂമിലെ ഡ്യൂട്ടി കഴിഞ്ഞിട്ടും ഈ പഴയ ബുള്ളറ്റിന്റെ അടുത്ത് തന്നെ!"),
 ("V","V","ഐശൂ, നമ്മുടെ വിന്റേജ് ബൈക്ക് റീസ്റ്റോറേഷൻ കമ്പനിയുടെ സർട്ടിഫിക്കറ്റ് ഇന്ന് വന്നു!"),
 ("A","A","അടിപൊളി! മൂന്ന് ദിവസം കഴിഞ്ഞ് കാശ്മീർ. ഹണിമൂൺ കഴിഞ്ഞ് വന്നിട്ട് ബാക്കി നോക്കാം."),
 ("V","V","എന്ത് ബാക്കി? രജിസ്ട്രേഷൻ കഴിഞ്ഞല്ലോ."),
 ("A","wide","കമ്പനി ഉണ്ടായി മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യത്തെ ഓഡിറ്ററെ വെക്കണം. അത് ഞാൻ ഇന്നലെ വായിച്ചു."),
 ("V","V","രണ്ടാഴ്ച കാശ്മീർ, പിന്നെ ബന്ധുവീടുകളിലെ വിരുന്നുകൾ. മുപ്പത് ദിവസം പറന്നുപോകും."),
 ("A","A","അതുകൊണ്ട് പോകും മുമ്പ് നാളെ തന്നെ ഓഡിറ്ററെ കാണാം. പിന്നെ മഞ്ഞിൽ ടെൻഷൻ ഇല്ലാതെ ഇരിക്കാം."),
 ("V","wide","ശരി. ബുള്ളറ്റ് പോലെ സ്റ്റാർട്ട്, ബ്രേക്ക് ഇല്ലാതെ!")],
 "ആഘോഷത്തിന് മുമ്പ്\nഓഡിറ്ററെ വെക്കൂ", CTA_AFTER,
 cap_ml="ഷോറൂമിൽ ജോലി ചെയ്യുന്ന ജിതിന്റെ വിന്റേജ് ബൈക്ക് കമ്പനിയുടെ സർട്ടിഫിക്കറ്റ് വന്നത് ഹണിമൂണിന് മൂന്ന് ദിവസം മുമ്പ്. കമ്പനി രജിസ്റ്റർ ചെയ്ത് 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം; യാത്രയ്ക്ക് മുമ്പ് തന്നെ ചെയ്യൂ.",
 cap_en="A salaried service advisor's vintage-bike restoration company is incorporated three days before his two-week honeymoon. The first auditor must be appointed within 30 days of incorporation, so sort it out before the trip.",
 cap_mg="Showroom-il joli cheyyunna aalude vintage bike company-yude certificate vannathu honeymoon-nu moonnu divasam munpu. Company register cheythu 30 days-inullil first auditor-ne vekkanam; yaathraykku munpu thanne cheyyu.")

# munnar: Selin + Basil. Basil, an estate field officer, builds a booking site for old estate bungalows and wants a big tea brand's name.
duo("d1613", "salaried", "C", "munnar", "എസ്റ്റേറ്റിൽ ജോലി.\nസൈഡിൽ ബംഗ്ലാവ് ബുക്കിംഗ്.\nപേര് ഒരു വലിയ ടീ ബ്രാൻഡിന്റേത്", [
 ("A","wide","ബേസിലേ, ഫീൽഡ് റൗണ്ട്സ് കഴിഞ്ഞോ? അതോ വീണ്ടും വെബ്സൈറ്റ് പണി ആണോ?"),
 ("V","V","സെലിനേ, പഴയ എസ്റ്റേറ്റ് ബംഗ്ലാവുകൾ ടൂറിസ്റ്റുകൾക്ക് ബുക്ക് ചെയ്യുന്ന സൈറ്റ്. ആറ് ബംഗ്ലാവ് ഇപ്പോഴേ റെഡി."),
 ("A","A","സൂപ്പർ. കമ്പനിക്ക് പേര് എന്താ?"),
 ("V","V","എല്ലാവർക്കും അറിയാവുന്ന ആ വലിയ ചായ ബ്രാൻഡിന്റെ പേര്, പിന്നെ സ്റ്റേയ്സ്. ആളുകൾ പെട്ടെന്ന് വിശ്വസിക്കും."),
 ("A","wide","ആളുകൾ വിശ്വസിക്കും. പക്ഷേ ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ആകുന്ന പേര് റിജക്ട് ആകാം."),
 ("A","A","പിന്നെ ടൂറിസ്റ്റുകൾ കരുതും, ഇത് ആ കമ്പനിയുടേതാണെന്ന്. അത് നിന്റെ ബിസിനസ് അല്ലല്ലോ."),
 ("V","V","ശരിയാ. എന്റെ സൈഡ് ബിസിനസ് വേറൊരാളുടെ പേരിൽ അറിയപ്പെടണ്ട."),
 ("A","A","സ്വന്തം പേര് ഉണ്ടാക്ക്. മൂന്ന് ഓപ്ഷൻ, ആരുടെയും ഛായ ഇല്ലാതെ."),
 ("V","wide","എങ്കിൽ കോടമഞ്ഞ് ബംഗ്ലാവ്സ്. മഞ്ഞിന് ട്രേഡ്മാർക്ക് ഇല്ലല്ലോ!")],
 "വലിയ ബ്രാൻഡിന്റെ പേര്\nകടം വാങ്ങല്ലേ", CTA_NAME,
 cap_ml="മൂന്നാറിലെ എസ്റ്റേറ്റിൽ ജോലി ചെയ്യുന്ന ബേസിലിന്റെ സൈഡ് ബിസിനസ്: പഴയ ബംഗ്ലാവുകൾ ബുക്ക് ചെയ്യുന്ന സൈറ്റ്. കമ്പനിക്ക് ഒരു വലിയ ടീ ബ്രാൻഡിന്റെ പേര് ഇട്ടാൽ ട്രേഡ്മാർക്ക് ക്ലാഷ് കാരണം റിജക്ട് ആകാം; സ്വന്തം പേര് കണ്ടെത്തൂ.",
 cap_en="An estate field officer in Munnar starts a side business booking old tea-estate bungalows and wants a famous tea brand's name for his company. A company name that clashes with a trademark can be rejected; choose a name that is yours.",
 cap_mg="Munnar estate-il joli cheyyunna aalude side business: pazhaya bungalow book cheyyunna site. Company-kku oru valiya tea brand-nte peru ittaal trademark clash kaaranam reject aakaam; swantham company name kandethu.")

# mobileshop: Hanna + Fahad. Fahad, a telecom tower technician, is about to pawn Hanna's gold to show "5 lakh capital" for his booster-kit company.
duo("d1614", "salaried", "B", "mobileshop", "ഭാര്യയുടെ സ്വർണ്ണം പണയം വെച്ച്\nകമ്പനിക്ക് 5 ലക്ഷം?", [
 ("A","wide","ഫഹദേ, ഇതെന്താ എന്റെ വള ഒക്കെ ഒരു കവറിൽ?"),
 ("V","V","ഹന്നാ, ടവർ ജോലി കഴിഞ്ഞ് ഞാൻ ഉണ്ടാക്കുന്ന സിഗ്നൽ ബൂസ്റ്റർ കിറ്റിന് കമ്പനി തുടങ്ങണം. അഞ്ച് ലക്ഷം വേണം."),
 ("A","A","ആര് പറഞ്ഞു അഞ്ച് ലക്ഷം വേണമെന്ന്?"),
 ("V","V","ടവർ സൈറ്റിലെ സൂപ്പർവൈസർ. കമ്പനിക്ക് മിനിമം ക്യാപിറ്റൽ കാണിക്കണം എന്ന്."),
 ("A","wide","പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇപ്പോൾ ഇല്ല. സ്വർണ്ണം പണയം വെക്കേണ്ട."),
 ("V","V","അപ്പോ സൂപ്പർവൈസർ പറഞ്ഞതോ?"),
 ("A","A","സൂപ്പർവൈസർക്ക് ടവറിന്റെ സിഗ്നൽ അറിയാം. കമ്പനി നിയമത്തിന്റെ സിഗ്നൽ കിട്ടിയിട്ടില്ല."),
 ("V","wide","ശരി. വള തിരിച്ച് അലമാരയിൽ. കമ്പനി ഇപ്പോ തന്നെ!")],
 "സ്വർണ്ണം പണയം വേണ്ട.\nമിനിമം ക്യാപിറ്റൽ ഇല്ല", CTA_START,
 cap_ml="ടെലികോം ടവർ ടെക്നീഷ്യൻ സൈഡ് ബിസിനസിന് കമ്പനി തുടങ്ങാൻ ഭാര്യയുടെ സ്വർണ്ണം പണയം വെച്ച് 5 ലക്ഷം കാണിക്കാൻ പോകുന്നു. പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് ഇപ്പോൾ മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല.",
 cap_en="A telecom tower technician was about to pawn his wife's gold to show 5 lakh of capital before registering his side business. There is no minimum paid-up capital for a private limited company in India, so you can register first.",
 cap_mg="Telecom tower technician side business-nu company thudangan bharyayude swarnam panayam vechu 5 lakh kaanikkan pokunnu. Pvt Ltd company-kku ippol minimum paid-up capital illa; company register cheyyan athu venda.")

# homestay: Teena + Jomon. Jomon works remotely for a Bengaluru IT firm from Wayanad; his coffee subscription's office is his mother's house.
duo("d1615", "salaried", "A", "homestay", "വയനാട്ടിൽ ഇരുന്ന് ഐടി ജോലി.\nസൈഡിൽ കാപ്പി സബ്സ്ക്രിപ്ഷൻ.\nവീട് അമ്മയുടെ പേരിൽ", [
 ("A","wide","ജോമോനേ, മീറ്റിംഗ് കഴിഞ്ഞോ? കാപ്പിപ്പൊടി പാക്കറ്റിൽ ലേബൽ ഒട്ടിക്കാൻ ആളെ വേണം."),
 ("V","V","ടീനാ, ബാംഗ്ലൂർ ക്ലയന്റിന്റെ കോൾ കഴിഞ്ഞു. ഇനി നമ്മുടെ കാപ്പി! ഇരുന്നൂറ് പേർ മാസം തോറും ഓർഡർ ചെയ്യുന്നു."),
 ("A","A","എന്നാ കമ്പനി ആക്കണം. ഓഫീസ് ഈ വീട് തന്നെ, അല്ലേ?"),
 ("V","V","അതേ. ഞാൻ ഇവിടെ താമസിക്കുന്നുണ്ടല്ലോ. അതുമതി."),
 ("A","wide","പോരാ. വീട് അമ്മയുടെ പേരിലാണ്. വീട് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ ഒരു യൂട്ടിലിറ്റി ബില്ലും വേണം."),
 ("V","V","അമ്മ ഒപ്പിടും. പക്ഷേ ആദ്യം ഒരു ചോദ്യം ഉണ്ടാകും. കാപ്പി എന്റെ തോട്ടത്തിലെ അല്ലേ എന്ന്."),
 ("A","A","എങ്കിൽ ആദ്യത്തെ പാക്കറ്റ് അമ്മയ്ക്ക് സമ്മാനം. ബില്ലും NOC-യും ഇന്ന് തന്നെ."),
 ("V","wide","ഡീൽ. കമ്പനിയുടെ ആദ്യ സപ്പോർട്ടർ അമ്മ!")],
 "സ്വന്തം വീടായാലും\nഉടമയുടെ NOC", CTA_DOCS,
 cap_ml="വയനാട്ടിൽ ഇരുന്ന് ഐടി ജോലി ചെയ്യുന്ന ജോമോന്റെ കാപ്പി സബ്സ്ക്രിപ്ഷന് കമ്പനി വേണം, ഓഫീസ് അമ്മയുടെ പേരിലുള്ള വീട്. വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം.",
 cap_en="A remote IT employee in Wayanad turns his family-estate coffee subscription into a company, with the registered office at the house in his mother's name. A home address works as the registered office with the owner's NOC and a recent utility bill.",
 cap_mg="Wayanad-il irunnu IT joli cheyyunna aalude coffee subscription-nu company venam, office ammayude perilulla veedu. Veedu registered office aakkan owner-nte NOC-um puthiya utility bill-um venam.")

# chat: Shweta + her husband. Shweta, a lab technician, changed jobs; her baby-photoshoot props company is 175 days old.
chat("c983", "salaried", "C", "പുതിയ ജോലി, പുതിയ ഷിഫ്റ്റ്.\nസൈഡ് കമ്പനിക്ക് 175 ദിവസം", ("ശ്വേത", "ഭർത്താവ്"), [
 (0,"ഏട്ടാ, പുതിയ ലാബിൽ ആദ്യത്തെ ആഴ്ച കഴിഞ്ഞു. രാത്രി ഷിഫ്റ്റ് കുറച്ച് കഠിനം."),
 (1,"ശരി. പക്ഷേ നമ്മുടെ ബേബി ഫോട്ടോഷൂട്ട് പ്രോപ്സ് കമ്പനിക്ക് ഇന്ന് എത്ര ദിവസമായി എന്ന് നോക്കിയോ?"),
 (0,"ജോലി മാറ്റത്തിനിടയിൽ മറന്നു. നൂറ്റി എഴുപത്തഞ്ച്?"),
 (1,"അതെ. നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം. അഞ്ച് ദിവസം മാത്രം ബാക്കി."),
 (0,"അത് വലിയ കമ്പനികൾക്കല്ലേ? നമ്മുടേത് കുഞ്ഞുങ്ങളുടെ തൊപ്പിയും പുതപ്പും അല്ലേ."),
 (1,"നമ്മുടേത് പോലുള്ള കമ്പനിക്കും വേണം. മിസ്സ് ആയാൽ കമ്പനിക്ക് അമ്പതിനായിരം രൂപ പിഴ. ഡയറക്ടർമാർക്ക് ദിവസം ആയിരം രൂപ വേറെ."),
 (0,"അയ്യോ. നാളെ ഷിഫ്റ്റിന് മുമ്പ് തന്നെ ഫോം ചെയ്യാം."),
 (1,"ഗുഡ്. ബേബി പ്രോപ്സ് സോഫ്റ്റ് ആണ്. ഡെഡ്‌ലൈൻ അങ്ങനെ അല്ല!")],
 "ജോലി മാറിയാലും\nINC-20A മാറില്ല", CTA_AFTER,
 cap_ml="ലാബ് ടെക്നീഷ്യൻ ജോലി മാറുന്ന തിരക്കിൽ സൈഡ് കമ്പനിയുടെ INC-20A മറന്നു; കമ്പനിക്ക് 175 ദിവസം. 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ, ഡയറക്ടർമാർക്ക് ദിവസം 1,000 രൂപ.",
 cap_en="A lab technician switching jobs forgot her side company's INC-20A, and it is day 175. The commencement of business filing is due within 180 days of incorporation; the penalty is 50,000 on the company and 1,000 a day per officer in default.",
 cap_mg="Lab technician joli maarunna thirakkil side company-yude INC-20A marannu; company-kku 175 divasam. 180 days-inullil file cheythillenkil company-kku 50,000 pizha, director-maarkku divasam 1,000.")

lst("l982", "salaried", "A", "ജോലിക്കൊപ്പം കമ്പനി:\nവീട്ടുകാരോട് ചോദിക്കേണ്ട\n3 ചോദ്യം", [
 ("രണ്ടാമത്തെ ഡയറക്ടർ ആര്?", "Pvt Ltd-ന് കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC നോക്കാം."),
 ("ആരുടെ വീട് ഓഫീസ് ആകും?", "വീട് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം."),
 ("തീയതികൾ ആര് ഓർക്കും?", "30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ. 180 ദിവസത്തിനുള്ളിൽ INC-20A. ഷിഫ്റ്റിനിടയിൽ മറക്കരുത്.")],
 "വീട്ടിൽ ഉറപ്പിച്ചാൽ\nപകുതി ജോലി കഴിഞ്ഞു", CTA_DOCS,
 cap_ml="ജോലിയിൽ ഇരുന്ന് കമ്പനി തുടങ്ങും മുമ്പ് വീട്ടിൽ തീരുമാനിക്കേണ്ട 3 കാര്യം: രണ്ടാമത്തെ ഡയറക്ടർ ആര്, ആരുടെ വീട് ഓഫീസ് (NOC, യൂട്ടിലിറ്റി ബിൽ), 30 ദിവസത്തെ ഓഡിറ്ററും 180 ദിവസത്തെ INC-20A-യും ആര് ഓർക്കും.",
 cap_en="Salaried and starting a company on the side in Kerala? Settle three things at home first: who is the second director, whose house is the registered office (owner's NOC and utility bill), and who tracks the 30-day auditor and 180-day INC-20A dates.",
 cap_mg="Joliyil irunnu company thudangum munpu veettil theerumanikkenda 3 kaaryam: randamathe director aaru, aarude veedu office (NOC, utility bill), 30 divasathe auditor-um 180 divasathe INC-20A-yum aaru orkkum.")
