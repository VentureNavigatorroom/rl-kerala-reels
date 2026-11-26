# FSSAI batch 07 (26 Nov, refill after the 24 Nov correction emptied the bank). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI (2026 limits). No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD


# crm (C9, investor diligence): frozen-porotta brand assumes its 2024 licence became perpetual
duo("fs038", "packaged_food", "B", "office", "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"2024-ലെ ലൈസൻസ്\nഇപ്പോഴും വാലിഡ് ആണോ?\"", [
 ("A","wide","രാഹുൽ, ഇൻവെസ്റ്ററുടെ ഡ്യൂ ഡിലിജൻസ് ലിസ്റ്റ് വന്നു. നമ്മുടെ ഫ്രോസൺ പൊറോട്ടയുടെ FSSAI ലൈസൻസ് വാലിഡ് ആണോ എന്ന്."),
 ("V","V","നേഹേ, അത് 2024-ൽ എടുത്തതല്ലേ. ഇപ്പോ എല്ലാ ലൈസൻസും സ്ഥിരം ആയില്ലേ?"),
 ("A","A","ഞാൻ FSSAI-യുടെ FAQ നോക്കി. 2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയതിന് മാത്രമാണ് സ്ഥിരം സാധുത ഉറപ്പ്. പഴയതിന് FoSCoS-ൽ കാലാവധി തീയതി നോക്കണം."),
 ("V","V","അപ്പോ ഇന്ന് തന്നെ FoSCoS തുറന്ന് തീയതി നോക്കാം."),
 ("A","wide","ഊഹം ഫയലിൽ കയറില്ല, തീയതി കയറും.")],
 "പഴയ ലൈസൻസ്?\nFoSCoS-ൽ തീയതി നോക്കൂ", CTA_FSSAI, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഫ്രോസൺ ഫുഡ് ബ്രാൻഡിന്റെ 2024-ലെ FSSAI ലൈസൻസ് വാലിഡ് ആണോ എന്ന് ചോദിച്ചു. 2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ ലൈസൻസിന് മാത്രമാണ് സ്ഥിരം സാധുത ഉറപ്പ്. പഴയതാണെങ്കിൽ FoSCoS-ൽ കാലാവധി തീയതി നോക്കി സമയത്ത് പുതുക്കുക. നിങ്ങളുടേത് ഏപ്രിലിന് മുമ്പോ ശേഷമോ?",
 cap_en="An investor's due-diligence list asks whether a frozen-porotta brand's 2024 FSSAI licence is still valid, and the founder assumes every licence is now permanent. Perpetual validity is certain only for licences issued on or after 1 April 2026; for an older one, check its expiry date on FoSCoS and renew on time. Was yours issued before or after April 2026?",
 cap_mg="Investor frozen food brand-inte 2024-le FSSAI licence valid aano ennu chodichu. 2026 April 1 muthal kittiya licence-inu maathramaanu perpetual validity urappu. Pazhayathaanel FoSCoS-il expiry date nokki samayathu renew cheyyuka. Ningaludethu April-nu mumpo shesham-o?")

# crm (#26 Gulf returnee): opening a bakery-cafe at home, expects yearly renewal like his Gulf job
duo("fs039", "cafe_owner", "A", "gulfroom", "ഗൾഫിൽ എല്ലാ കൊല്ലവും\nലൈസൻസ് പുതുക്കാൻ ഓടി.\nനാട്ടിലോ?", [
 ("A","wide","ഷംസൂ, ഇവിടെ കഫ്റ്റീരിയയിൽ എല്ലാ കൊല്ലവും ലൈസൻസ് പുതുക്കാൻ ഓടിയത് ഞാനാ. നാട്ടിലെ ബേക്കറിക്കും അതേ ഓട്ടം വേണോ?"),
 ("V","V","നസീറേ, നാട്ടിൽ FSSAI നീ ഇനിയല്ലേ എടുക്കുന്നത്? 2026 ഏപ്രിൽ മുതൽ കിട്ടുന്ന രജിസ്ട്രേഷനും ലൈസൻസിനും സ്ഥിരം സാധുതയാണ്. പുതുക്കൽ ഇല്ല."),
 ("A","A","അപ്പോ ഒരിക്കൽ എടുത്താൽ പിന്നെ ഒന്നും വേണ്ട!"),
 ("V","wide","അങ്ങനെയല്ല. FSSAI-ക്കുള്ള വാർഷിക അടവ് തുടരും. വേണമെങ്കിൽ കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് അടയ്ക്കാം."),
 ("A","A","പുതുക്കലിന്റെ ഓട്ടം നിന്നു, അടവ് നിന്നില്ല."),
 ("V","wide","ഓട്ടം പോയി, ഓർമ്മ വേണം.")],
 "പുതുക്കൽ പോയി,\nവാർഷിക അടവ് ബാക്കി", CTA_FOOD, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചു വന്ന് നാട്ടിൽ ബേക്കറി തുടങ്ങുകയാണോ? 2026 ഏപ്രിൽ 1 മുതൽ കിട്ടുന്ന FSSAI രജിസ്ട്രേഷനും ലൈസൻസിനും സ്ഥിരം സാധുത, പുതുക്കൽ വേണ്ട. പക്ഷേ FSSAI-ക്കുള്ള വാർഷിക അടവ് തുടരും; കുറച്ച് വർഷത്തേത് ഒരുമിച്ച് അടയ്ക്കാം. നിങ്ങൾ എപ്പോൾ നാട്ടിലേക്ക്?",
 cap_en="A Gulf returnee opening a bakery-cafe in Kerala expects to chase a licence renewal every year, as he did abroad. FSSAI registrations and licences issued on or after 1 April 2026 have perpetual validity, so no renewal, but the yearly payment to FSSAI continues and can be paid for several years at once. When are you moving back?",
 cap_mg="Gulf-il ninnu thirichu vannu naattil bakery thudangukayaano? 2026 April 1 muthal kittunna FSSAI registration-num licence-num perpetual validity, renew venda. Pakshe FSSAI-kkulla annual payment thudarum; kurachu varshathethu orumichu adakkaam. Ningal eppol naattilekku?")

# new: night thattukada grew into a highway hotel, still on basic registration
duo("fs040", "cafe_owner", "C", "thattukada", "തട്ടുകട ഹോട്ടലായി.\nടേൺഓവർ 1.8 കോടി.\nഇപ്പോഴും ബേസിക്?", [
 ("A","wide","ബിജൂ, നമ്മുടെ രാത്രി തട്ടുകട ഇപ്പോ 24 മണിക്കൂർ ഹൈവേ ഹോട്ടൽ. ഈ കൊല്ലം ടേൺഓവർ 1.8 കോടി!"),
 ("V","V","സിജോ, അടിപൊളി! FSSAI ഇപ്പോഴും ആ പഴയ ബേസിക് രജിസ്ട്രേഷൻ തന്നെയാണോ?"),
 ("A","A","കട ഒന്ന് തന്നെയല്ലേ. പഴയത് മതിയെന്ന് കരുതി."),
 ("V","wide","കടയുടെ വലിപ്പമല്ല, ടേൺഓവർ ആണ് നോക്കുന്നത്. 1.5 കോടി കടന്നാൽ സ്റ്റേറ്റ് ലൈസൻസ് വേണം. 50 കോടി വരെ അത് മതി."),
 ("A","A","തട്ടിൽ നിന്ന് ഹോട്ടലായി, പേപ്പറും മാറണം."),
 ("V","wide","ദോശ പരന്നാൽ ലൈസൻസും വളരണം.")],
 "1.5 കോടി കടന്നാൽ\nസ്റ്റേറ്റ് ലൈസൻസ്", CTA_FSSAI, theme="new",
 cap_ml="രാത്രി തട്ടുകട 24 മണിക്കൂർ ഹൈവേ ഹോട്ടലായി, ടേൺഓവർ 1.8 കോടി, FSSAI ഇപ്പോഴും ബേസിക് രജിസ്ട്രേഷൻ. 2026 ഏപ്രിൽ മുതൽ 1.5 കോടി വരെ രജിസ്ട്രേഷൻ, അതിന് മുകളിൽ 50 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്. നിങ്ങളുടെ കട ഈ കൊല്ലം എത്ര വളർന്നു?",
 cap_en="A night thattukada has grown into a 24-hour highway hotel with 1.8 crore turnover, and it is still on basic FSSAI registration. Since April 2026, registration covers turnover up to 1.5 crore; above that, up to 50 crore, you need a state licence. How much did your food business grow this year?",
 cap_mg="Raathri thattukada 24 manikkoor highway hotel aayi, turnover 1.8 crore, FSSAI ippozhum basic registration. 2026 April muthal 1.5 crore vare registration, athinu mukalil 50 crore vare State licence. Ningalude kada ee kollam ethra valarnnu?")

# crm (business shrank after losing a contract): catering firm can surrender its licence for registration
duo("fs041", "cloud_kitchen", "B", "hotellobby", "വലിയ കോൺട്രാക്ട് പോയി.\nടേൺഓവർ 3 കോടിയിൽ\nനിന്ന് 1.2 കോടി", [
 ("A","wide","ജെയ്സൺ, ഹോട്ടലിന്റെ കാറ്ററിംഗ് കോൺട്രാക്ട് പോയതോടെ നമ്മുടെ ടേൺഓവർ 3 കോടിയിൽ നിന്ന് 1.2 കോടിയായി."),
 ("V","V","നീതൂ, എന്നിട്ടും നമ്മൾ സ്റ്റേറ്റ് ലൈസൻസ് തന്നെ വെക്കണോ?"),
 ("A","A","FSSAI-യുടെ പുതിയ നിയമത്തിൽ 1.5 കോടി വരെ രജിസ്ട്രേഷൻ മതി."),
 ("V","wide","താഴ്ന്ന കാറ്റഗറിയിൽ ആയ ബിസിനസിന് ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം. പക്ഷേ ആദ്യം FoSCoS-ൽ നമ്മുടെ ബിസിനസ് തരം നോക്കണം."),
 ("A","A","അപ്പോ ആദ്യം കാറ്റഗറി, പിന്നെ സറണ്ടർ."),
 ("V","wide","കയറാൻ മാത്രമല്ല, ഇറങ്ങാനും വഴിയുണ്ട്.")],
 "ടേൺഓവർ കുറഞ്ഞാൽ\nസറണ്ടർ ചെയ്യാം", CTA_FSSAI, theme="crm",
 cap_ml="വലിയ കോൺട്രാക്ട് പോയി ടേൺഓവർ 1.5 കോടിക്ക് താഴെ ആയോ? താഴ്ന്ന കാറ്റഗറിയിൽ ആയ ബിസിനസിന് FSSAI ലൈസൻസ് സറണ്ടർ ചെയ്ത് രജിസ്ട്രേഷൻ എടുക്കാം. ചില ബിസിനസിന് ടേൺഓവർ നോക്കാതെ ലൈസൻസ് വേണം, അതുകൊണ്ട് ആദ്യം FoSCoS-ൽ കാറ്റഗറി നോക്കുക. നിങ്ങളുടെ ടേൺഓവർ കൂടിയോ കുറഞ്ഞോ?",
 cap_en="A catering firm lost its big hotel contract and its turnover fell from 3 crore to 1.2 crore. A business that now falls in a lower FSSAI category can surrender its licence for a registration, but some kinds of business need a licence whatever the turnover, so check your category on FoSCoS first. Did your turnover go up or down this year?",
 cap_mg="Valiya contract poyi turnover 1.5 crore-nu thaazhe aayo? Thaazhnna category-il aaya business-inu FSSAI licence surrender cheythu registration edukkaam. Chila business-inu turnover nokkaathe licence venam, athukondu aadyam FoSCoS-il category nokkuka. Ningalude turnover koodiyo kuranjo?")

# crm (#16 Gulf investor in a cousin's Kerala business): growth plan says 60 crore, licence plan missing
duo("fs042", "spice_exporter", "C", "gulfoffice", "ദുബായിലെ കസിൻ ചോദിച്ചു:\n\"60 കോടി ആയാൽ\nഏത് ലൈസൻസ്?\"", [
 ("A","wide","ആസിഫേ, 3 വർഷം കൊണ്ട് മസാല ബ്രാൻഡ് 60 കോടി എന്ന പ്ലാൻ കൊള്ളാം. പക്ഷേ അപ്പോൾ ഏത് FSSAI ലൈസൻസ്? അത് പ്ലാനിൽ കണ്ടില്ല."),
 ("V","V","ഇപ്പോ സ്റ്റേറ്റ് ലൈസൻസ് ഉണ്ടല്ലോ ഷഹാനാ. അത് മതിയാകില്ലേ?"),
 ("A","A","സ്റ്റേറ്റ് ലൈസൻസ് 50 കോടി വരെ മാത്രം. അതിന് മുകളിൽ സെൻട്രൽ ലൈസൻസ് വേണം."),
 ("V","V","അപ്പോ 50 കോടി കടക്കുന്ന വർഷം സെൻട്രൽ. അതും പ്ലാനിൽ ചേർക്കാം."),
 ("A","wide","വളർച്ച മാത്രം എഴുതിയാൽ പോരാ, ലൈസൻസും എഴുതണം.")],
 "50 കോടി കടന്നാൽ\nസെൻട്രൽ ലൈസൻസ്", CTA_FSSAI, theme="crm",
 cap_ml="ഗൾഫിലുള്ള ബന്ധു നാട്ടിലെ ഫുഡ് ബ്രാൻഡിൽ പണം ഇടുമ്പോൾ ഗ്രോത്ത് പ്ലാനിനൊപ്പം ലൈസൻസ് പ്ലാനും ചോദിക്കും. സ്റ്റേറ്റ് FSSAI ലൈസൻസ് 50 കോടി ടേൺഓവർ വരെ മാത്രം; അതിന് മുകളിൽ സെൻട്രൽ ലൈസൻസ് വേണം. നിങ്ങളുടെ 3 വർഷ പ്ലാനിൽ ഇത് ഉണ്ടോ?",
 cap_en="A Gulf-based cousin reviewing a Kerala spice brand's plan to reach 60 crore asks which FSSAI licence it will need. A state licence covers turnover up to 50 crore; above 50 crore you need a central licence. Is the licence step in your 3-year plan?",
 cap_mg="Gulf-il ulla bandhu naattile food brand-il paisa idumpol growth plan-inoppam licence plan-um chodikkum. State FSSAI licence 50 crore turnover vare maathram; athinu mukalil Central licence venam. Ningalude 3 varsha plan-il ithu undo?")

# crm (#5, two businesses under one name): spice wholesaler with a state licence starts importing dry fruits
duo("fs043", "spice_exporter", "B", "shop", "\"സ്റ്റേറ്റ് ലൈസൻസ്\nഉണ്ടല്ലോ. ഇറക്കുമതിക്കും\nഅത് പോരേ?\"", [
 ("A","wide","സുരേഷേ, മസാല കച്ചവടത്തിനൊപ്പം ഒമാനിൽ നിന്ന് ഡ്രൈ ഫ്രൂട്ട്സ് ഇറക്കാൻ അളിയൻ ഒരു ഡീൽ ശരിയാക്കി."),
 ("V","V","ബിനൂ, ഇറക്കുമതിക്ക് ഏത് FSSAI ലൈസൻസ് ആണ് എടുക്കുന്നത്?"),
 ("A","A","നമുക്ക് സ്റ്റേറ്റ് ലൈസൻസ് ഉണ്ടല്ലോ. ടേൺഓവർ 3 കോടിയേ ഉള്ളൂ."),
 ("V","wide","ഫുഡ് ഇറക്കുമതി ചെയ്യുന്നവർക്ക് ടേൺഓവർ എത്ര ആയാലും സെൻട്രൽ ലൈസൻസ് വേണം."),
 ("A","A","അപ്പോ ആദ്യ ലോഡ് ബുക്ക് ചെയ്യും മുമ്പ് സെൻട്രൽ."),
 ("V","wide","കടയ്ക്ക് സ്റ്റേറ്റ്, ഇറക്കുമതിക്ക് സെൻട്രൽ.")],
 "കടയ്ക്ക് സ്റ്റേറ്റ്,\nഇറക്കുമതിക്ക് സെൻട്രൽ", CTA_FOOD, theme="crm",
 cap_ml="സ്റ്റേറ്റ് FSSAI ലൈസൻസുള്ള മസാല കച്ചവടക്കാരൻ ഗൾഫിൽ നിന്ന് ഡ്രൈ ഫ്രൂട്ട്സ് ഇറക്കാൻ തുടങ്ങുന്നു. ഫുഡ് ഇറക്കുമതി ചെയ്യുന്നവർക്ക് ടേൺഓവർ എത്ര ചെറുതായാലും സെൻട്രൽ ലൈസൻസ് വേണം. നിങ്ങൾ എന്തെങ്കിലും ഇറക്കുമതി ചെയ്യുന്നുണ്ടോ?",
 cap_en="A spice wholesaler with a state FSSAI licence and 3 crore turnover starts importing dry fruits from Oman through a relative. Food importers need a central FSSAI licence whatever their turnover, so get it before the first load is booked. Do you import any food: yes or no?",
 cap_mg="State FSSAI licence ulla masala kachavadakkaaran Gulf-il ninnu dry fruits irakkaan thudangunnu. Food import cheyyunnavarkku turnover ethra cheruthaayaalum Central licence venam. Ningal enthenkilum import cheyyunnundo?")

# faq: "small turnover always means basic registration"
duo("fs044", "packaged_food", "A", "juiceshop", "\"ടേൺഓവർ 40 ലക്ഷമേ ഉള്ളൂ.\nരജിസ്ട്രേഷൻ മതി,\nഉറപ്പല്ലേ?\"", [
 ("A","wide","നൗഷാദേ, ജ്യൂസ് കടയ്ക്ക് പുറമെ ഒരു ചെറിയ യൂണിറ്റിൽ ഫ്രൂട്ട് പൾപ്പ് പാക്ക് ചെയ്ത് വിൽക്കാൻ പോകുവാ നമ്മൾ."),
 ("V","V","റസിയാ, ടേൺഓവർ 40 ലക്ഷമേ വരൂ. 1.5 കോടി വരെ രജിസ്ട്രേഷൻ. അപ്പോ അത് ഉറപ്പല്ലേ?"),
 ("A","A","മിക്കവർക്കും അതെ. പക്ഷേ ചില തരം ബിസിനസിന് ടേൺഓവർ എത്ര ചെറുതായാലും ലൈസൻസ് തന്നെ വേണം."),
 ("V","V","അപ്പോ നമ്മുടേത് ഏത് തരം എന്ന് എങ്ങനെ അറിയും?"),
 ("A","wide","FoSCoS-ൽ നമ്മുടെ ബിസിനസ് കാറ്റഗറി നോക്കിയിട്ട് മാത്രം അപേക്ഷിക്കണം."),
 ("V","wide","ടേൺഓവർ ഒന്നാമത്തെ ചോദ്യം, കാറ്റഗറി രണ്ടാമത്തേത്.")],
 "ടേൺഓവർ മാത്രമല്ല,\nകാറ്റഗറിയും നോക്കൂ", CTA_FSSAI, theme="faq",
 cap_ml="1.5 കോടി വരെ ടേൺഓവറിന് സാധാരണ FSSAI രജിസ്ട്രേഷൻ മതി. പക്ഷേ ചില തരം ഫുഡ് ബിസിനസിന് ടേൺഓവർ എത്ര ചെറുതായാലും ലൈസൻസ് വേണം. അപേക്ഷിക്കും മുമ്പ് FoSCoS-ൽ നിങ്ങളുടെ കാറ്റഗറി നോക്കുക. നിങ്ങൾ ഏത് ഫുഡ് ആണ് ഉണ്ടാക്കുന്നത്?",
 cap_en="A juice shop starting a small fruit-pulp packing unit assumes 40 lakh turnover means basic FSSAI registration for sure. Registration usually covers turnover up to 1.5 crore, but some kinds of food business need a licence whatever the turnover. Check your category on FoSCoS before you apply. What food do you make?",
 cap_mg="1.5 crore vare turnover-inu saadhaarana FSSAI registration mathi. Pakshe chila tharam food business-inu turnover ethra cheruthaayaalum licence venam. Apekshikkum mumpu FoSCoS-il ningalude category nokkuka. Ningal ethu food aanu undaakkunnathu?")

# faq: "perpetual, so nothing more to file"
duo("fs045", "cloud_kitchen", "B", "akshaya", "\"സ്ഥിരം രജിസ്ട്രേഷൻ.\nഇനി ഒരു ഫയലിംഗും\nവേണ്ടല്ലോ?\"", [
 ("A","wide","രമേശേട്ടാ, ക്ലൗഡ് കിച്ചണിന്റെ FSSAI രജിസ്ട്രേഷൻ ഈ മേയിൽ കിട്ടി. ഇനി ഇതിന്റെ പേരിൽ ഇങ്ങോട്ട് വരേണ്ടല്ലോ?"),
 ("V","V","സുധേ, 2026 ഏപ്രിൽ മുതൽ കിട്ടിയതിന് പുതുക്കൽ വേണ്ട. അത് ശരിയാ."),
 ("A","A","അപ്പോ ഇനി ഒന്നും ചെയ്യാനില്ല!"),
 ("V","wide","ഉണ്ട്. വാർഷിക റിട്ടേൺ തുടരും, FSSAI-ക്കുള്ള വാർഷിക അടവും തുടരും."),
 ("A","A","അപ്പോ രണ്ടും കലണ്ടറിൽ എഴുതി വെക്കാം."),
 ("V","wide","സ്ഥിരം എന്നാൽ മറക്കാം എന്നല്ല.")],
 "പുതുക്കൽ പോയി,\nറിട്ടേൺ പോയില്ല", CTA_FOOD, theme="faq",
 cap_ml="2026 ഏപ്രിൽ 1 മുതൽ കിട്ടിയ FSSAI രജിസ്ട്രേഷന് സ്ഥിരം സാധുതയാണ്, പുതുക്കൽ വേണ്ട. പക്ഷേ വാർഷിക റിട്ടേണും FSSAI-ക്കുള്ള വാർഷിക അടവും തുടരും. സ്ഥിരം എന്നാൽ മറക്കാം എന്നല്ല. ഇത് നിങ്ങൾക്ക് പുതിയ അറിവാണോ?",
 cap_en="A cloud kitchen got its FSSAI registration in May 2026 and thinks it never has to file anything again. Registrations issued on or after 1 April 2026 need no renewal, but annual returns and the yearly payment to FSSAI continue. Perpetual doesn't mean forget it. Did you know this: yes or no?",
 cap_mg="2026 April 1 muthal kittiya FSSAI registration-inu perpetual validity aanu, renew venda. Pakshe annual return-um FSSAI-kkulla annual payment-um thudarum. Sthiram ennaal marakkaam ennalla. Ithu ningalkku puthiya arivaano?")

# faq: home baker told she needs a state licence at 80 lakh (old limits doing the rounds)
duo("fs046", "home_baker", "A", "bakery", "കേക്ക് വിൽപ്പന 80 ലക്ഷം.\n\"ഇനി സ്റ്റേറ്റ്\nലൈസൻസ് വേണം\"", [
 ("A","wide","സാബുച്ചേട്ടാ, വീട്ടിലെ കേക്ക് ഓർഡർ ഈ കൊല്ലം 80 ലക്ഷം കടന്നു. ഇനി സ്റ്റേറ്റ് ലൈസൻസ് വേണമെന്ന് ബന്ധു പറഞ്ഞു."),
 ("V","V","ജിഷേ, അത് പഴയ കണക്കാ. ഓടും മുമ്പ് പുതിയ നിയമം നോക്ക്."),
 ("A","A","എന്താ പുതിയ നിയമം?"),
 ("V","wide","2026 ഏപ്രിൽ മുതൽ വർഷം 1.5 കോടി വരെ ടേൺഓവറിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. ഹോം ബേക്കർമാർക്കും അങ്ങനെ തന്നെ."),
 ("A","A","അപ്പോ രജിസ്ട്രേഷൻ മതി. അതിന്റെ കാലാവധി FoSCoS-ൽ ഒന്ന് നോക്കാം."),
 ("V","wide","കേട്ട കണക്കല്ല, പുതിയ കണക്ക്.")],
 "1.5 കോടി വരെ\nരജിസ്ട്രേഷൻ മതി", CTA_FSSAI, theme="faq",
 cap_ml="വീട്ടിലെ കേക്ക് വിൽപ്പന 80 ലക്ഷം കടന്നപ്പോൾ സ്റ്റേറ്റ് ലൈസൻസ് വേണമെന്ന് കേട്ടോ? 2026 ഏപ്രിൽ മുതൽ വർഷം 1.5 കോടി വരെ ടേൺഓവറിന് FSSAI രജിസ്ട്രേഷൻ മതി, ഹോം ബേക്കർമാർക്കും. പഴയ രജിസ്ട്രേഷൻ ആണെങ്കിൽ കാലാവധി FoSCoS-ൽ നോക്കുക. നിങ്ങൾ ഈ പഴയ കണക്ക് കേട്ടിട്ടുണ്ടോ?",
 cap_en="A home baker's cake orders crossed 80 lakh this year and a relative says she now needs a state licence. Since April 2026, FSSAI registration covers turnover up to 1.5 crore a year, home bakers included. If your registration is older, check its expiry on FoSCoS. Heard the old limit too: yes or no?",
 cap_mg="Veettile cake vilppana 80 lakh kadannappol State licence venamennu ketto? 2026 April muthal varsham 1.5 crore vare turnover-inu FSSAI registration mathi, home bakers-num. Pazhaya registration aanel expiry FoSCoS-il nokkuka. Ningal ee pazhaya kanakku kettittundo?")

# faq: "only inside the apartment WhatsApp group, so no FSSAI"
chat("fsc004", "home_baker", "C", "\"ഫ്ലാറ്റിലെ ഗ്രൂപ്പിൽ\nമാത്രം മീൻകറി ഊണ്.\nആര് പിടിക്കാൻ?\"", ("വരുൺ", "ദേവിക"), [
 (1,"വരുണേ, ഫ്ലാറ്റിലെ വാട്സ്ആപ്പ് ഗ്രൂപ്പിൽ മീൻകറി ഊണ് ഇട്ടു. ദിവസം 40 ഓർഡർ!"),
 (0,"ദേവികേ, സൂപ്പർ! FSSAI രജിസ്ട്രേഷൻ എടുത്തോ?"),
 (1,"ഗ്രൂപ്പിൽ മാത്രമല്ലേ. പുറത്ത് ആരും അറിയില്ല."),
 (0,"ഗ്രൂപ്പ് ചെറുതായാലും ഇത് ഫുഡ് ബിസിനസ് തന്നെ. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം."),
 (1,"അപ്പോ ബേസിക് രജിസ്ട്രേഷൻ ഇന്ന് തന്നെ."),
 (0,"ഗ്രൂപ്പ് പ്രൈവറ്റ്, നിയമം പബ്ലിക്.")],
 "ഗ്രൂപ്പ് പ്രൈവറ്റ്,\nനിയമം പബ്ലിക്", CTA_FOOD, theme="faq",
 cap_ml="ഫ്ലാറ്റിലെ വാട്സ്ആപ്പ് ഗ്രൂപ്പിൽ മാത്രം ഊണ് വിൽക്കുന്നതും ഫുഡ് ബിസിനസ് തന്നെ. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും വരാം. വീട്ടിൽ നിന്നുള്ള ചെറിയ കച്ചവടത്തിന് ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങളുടെ ഫ്ലാറ്റ് ഗ്രൂപ്പിൽ ഇങ്ങനെ ആരെങ്കിലും ഉണ്ടോ?",
 cap_en="Selling fish-curry meals only inside your apartment's WhatsApp group is still a food business. Selling without FSSAI can mean a penalty up to 5 lakh and up to 6 months in prison; a small home kitchen usually needs only basic registration. Does someone in your apartment group sell food?",
 cap_mg="Flat-ile WhatsApp group-il maathram oonu vilkkunnathum food business thanne. FSSAI illaathe vittaal 5 lakh vare pizhayum 6 maasam vare thadavum varaam. Veettil ninnulla cheriya kachavadathinu basic registration mathi. Ningalude flat group-il ingane aarenkilum undo?")

# faq: what changed in 2026 and what didn't
lst("fsl003", "cafe_owner", "B", "FSSAI 2026:\nമാറിയതും\nമാറാത്തതും", [
 ("മാറിയത്: ലിമിറ്റ്", "1.5 കോടി വരെ രജിസ്ട്രേഷൻ, 50 കോടി വരെ സ്റ്റേറ്റ്, അതിന് മുകളിൽ സെൻട്രൽ."),
 ("മാറിയത്: പുതുക്കൽ", "2026 ഏപ്രിൽ മുതൽ കിട്ടിയതിന് സ്ഥിരം. പഴയതിന് FoSCoS-ൽ തീയതി നോക്കൂ."),
 ("മാറാത്തത്", "വാർഷിക അടവ്, പാക്കറ്റിലെ 14 അക്ക നമ്പർ, 5 ലക്ഷം വരെ പിഴ.")],
 "നിയമം മാറി,\nഉത്തരവാദിത്തം മാറിയില്ല", CTA_FSSAI, theme="faq",
 cap_ml="FSSAI-യിൽ 2026 ഏപ്രിൽ 1 മുതൽ മാറിയത്: 1.5 കോടി വരെ രജിസ്ട്രേഷൻ, 50 കോടി വരെ സ്റ്റേറ്റ്, അതിന് മുകളിൽ സെൻട്രൽ; പുതിയതിന് സ്ഥിരം സാധുത. മാറാത്തത്: വാർഷിക അടവ്, പാക്കറ്റിലെ 14 അക്ക നമ്പർ, 5 ലക്ഷം വരെ പിഴ. പഴയ ലൈസൻസ് ആണെങ്കിൽ FoSCoS-ൽ കാലാവധി നോക്കുക. ഏതാണ് നിങ്ങൾക്ക് പുതിയത്?",
 cap_en="What changed in FSSAI from 1 April 2026: registration up to 1.5 crore turnover, state licence up to 50 crore, central above that, and perpetual validity for anything issued from that date. What didn't change: the yearly payment to FSSAI, the 14-digit number on packets, and the penalty of up to 5 lakh. Older licence? Check its expiry on FoSCoS. Which part was new to you?",
 cap_mg="FSSAI-il 2026 April 1 muthal maariyathu: 1.5 crore vare registration, 50 crore vare State, athinu mukalil Central; puthiyathinu perpetual validity. Maaraathathu: annual payment, packet-ile 14 akka number, 5 lakh vare pizha. Pazhaya licence aanel FoSCoS-il expiry nokkuka. Ethaanu ningalkku puthiyathu?")

# new: auto driver sells his wife's homemade avalose podi packets to passengers
duo("fs047", "packaged_food", "C", "autostand", "\"ഓട്ടോയിൽ വെച്ച്\nഅവലോസ്പൊടി വിറ്റാൽ\nലൈസൻസോ?\"", [
 ("A","wide","ഷാജീ, ഭാര്യ ഉണ്ടാക്കുന്ന അവലോസ്പൊടി പാക്കറ്റ് ഞാൻ ഓട്ടോയിൽ വെച്ച് യാത്രക്കാർക്ക് വിൽക്കുന്നു. മാസം 300 പാക്കറ്റ്!"),
 ("V","V","സജീ, ആ പാക്കറ്റിൽ FSSAI നമ്പർ ഉണ്ടോ?"),
 ("A","A","ഓട്ടോയിൽ ആര് ചെക്ക് ചെയ്യാനാ? സൈഡ് ബിസിനസ് അല്ലേ."),
 ("V","wide","പാക്ക് ചെയ്ത് വിൽക്കുന്ന ഫുഡിൽ 14 അക്ക FSSAI നമ്പർ വേണം. വീട്ടിലെ ചെറിയ യൂണിറ്റിന് സാധാരണ ബേസിക് രജിസ്ട്രേഷൻ മതി."),
 ("A","A","അപ്പോ ഇനി പാക്കറ്റിൽ നമ്പർ അടിച്ചിട്ടേ വിൽപ്പനയുള്ളൂ."),
 ("V","wide","മീറ്റർ ഓട്ടോയ്ക്ക്, നമ്പർ പാക്കറ്റിന്.")],
 "മീറ്റർ ഓട്ടോയ്ക്ക്,\nനമ്പർ പാക്കറ്റിന്", CTA_FOOD, theme="new",
 cap_ml="ഓട്ടോയിൽ വെച്ച് യാത്രക്കാർക്ക് വീട്ടിലെ അവലോസ്പൊടി പാക്കറ്റ് വിൽക്കുന്നതിനും FSSAI വേണം. പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്യണം; വീട്ടിലെ ചെറിയ യൂണിറ്റിന് സാധാരണ ബേസിക് രജിസ്ട്രേഷൻ മതി. നിങ്ങളുടെ സൈഡ് ബിസിനസ് എന്താണ്?",
 cap_en="An auto driver sells 300 packets a month of his wife's homemade avalose podi to his passengers. Packaged food must carry the 14-digit FSSAI number, and a small home unit usually needs only basic registration. What's your side business?",
 cap_mg="Auto-yil vechu yaathrakkaarkku veettile avalose podi packet vilkkunnathinum FSSAI venam. Pack cheytha food-il 14 akka number print cheyyanam; veettile cheriya unit-inu saadhaarana basic registration mathi. Ningalude side business enthaanu?")
