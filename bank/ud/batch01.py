# Udyam (MSME) seed batch 01 (19 Nov). Short, myth/conflict-first; situations from STORY_THEMES.md F17-F22 and CRM themes.
# Facts only from topics.FACTS_UD. Never mention fees, never promise loans or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

duo("yd001", "supplier_unpaid", "A", "textile", "ബിൽ കൊടുത്തിട്ട്\n90 ദിവസം. ബയർ:\n\"അടുത്ത മാസം നോക്കാം\"", [
 ("A","wide","പ്രകാശേട്ടാ, ആ വലിയ ഷോറൂമിന്റെ പണം കിട്ടിയോ?"),
 ("V","V","രമ്യേ, തൊണ്ണൂറ് ദിവസമായി. ഓരോ തവണ വിളിക്കുമ്പോഴും അടുത്ത മാസം എന്ന്."),
 ("A","A","നമ്മുടെ യൂണിറ്റിന് ഉദ്യം രജിസ്ട്രേഷൻ ഉണ്ടോ?"),
 ("V","V","ഇല്ല. അതെന്തിനാ?"),
 ("A","wide","ഉദ്യം ഉള്ള ചെറിയ മാനുഫാക്ചറിംഗ് യൂണിറ്റിന് 45 ദിവസത്തിനുള്ളിൽ പണം കിട്ടണം. വൈകിയാൽ ബയർ കൂട്ടുപലിശ കൊടുക്കണം."),
 ("V","wide","എങ്കിൽ അടുത്ത ബില്ലിൽ ഉദ്യം നമ്പറും.")],
 "45 ദിവസം കഴിഞ്ഞാൽ\nപലിശ ബയർക്ക്", CTA_UDYAM, theme="faq",
 cap_ml="തുണി യൂണിറ്റിന്റെ ബിൽ കൊടുത്തിട്ട് 90 ദിവസം, പണം കിട്ടിയില്ല. ഉദ്യം രജിസ്ട്രേഷനുള്ള മാനുഫാക്ചറിംഗ്, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക് 45 ദിവസത്തിനുള്ളിൽ പണം കിട്ടണം; വൈകിയാൽ ബയർ കൂട്ടുപലിശ. നിങ്ങളുടെ ബയർ എത്ര ദിവസം എടുക്കും?",
 cap_en="A small garment unit has waited 90 days for a showroom's payment. Udyam-registered manufacturing and service micro and small units must be paid within 45 days, or the buyer owes compound interest. How long does your buyer take to pay?",
 cap_mg="Thuni unit-nte bill koduthittu 90 divasam, paisa kittiyilla. Udyam ulla manufacturing, service micro small units-nu 45 divasathinullil paisa kittanam; vaikiyaal buyer koottupalisha. Ningalude buyer ethra divasam edukkum?")

duo("yd002", "trader_ud", "B", "shop", "കടയ്ക്ക് ഉദ്യം എടുത്തു.\n\"ഇനി പണം വൈകില്ല\"\nഇത് തെറ്റ്", [
 ("A","wide","സുരേഷേ, നീ ഉദ്യം എടുത്തെന്ന് കേട്ടു. ഇനി ഹോൾസെയിൽ കടക്കാർ പണം വൈകിക്കില്ലല്ലോ?"),
 ("V","V","അങ്ങനെയാ ഞാനും കരുതിയത്, ബിനൂ. പക്ഷേ അത് കച്ചവടക്കാർക്ക് ബാധകമല്ല."),
 ("A","A","അപ്പോ ഉദ്യം കൊണ്ട് എന്ത് കിട്ടും?"),
 ("V","V","കടകൾക്കും ഹോൾസെയിലിനും ബാങ്ക് ലോണിൽ മുൻഗണന മാത്രം. 45 ദിവസത്തെ സംരക്ഷണം മാനുഫാക്ചറിംഗിനും സർവീസിനും."),
 ("A","wide","അപ്പോ പണത്തിന്റെ കാര്യം എഗ്രിമെന്റിൽ എഴുതണം."),
 ("V","wide","അതേ. ഉദ്യം ലോണിന്, എഗ്രിമെന്റ് പണത്തിന്.")],
 "കടയ്ക്ക് ഉദ്യം:\nലോണിന് മാത്രം", CTA_UDYAM, theme="faq",
 cap_ml="ഹോൾസെയിൽ, റീട്ടെയിൽ കച്ചവടക്കാർക്കും ഉദ്യം എടുക്കാം, പക്ഷേ ബാങ്ക് ലോണിൽ മുൻഗണനയ്ക്ക് മാത്രം. 45 ദിവസത്തെ പേമെന്റ് സംരക്ഷണം മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്കാണ്.",
 cap_en="Shop owners and wholesalers can take Udyam registration, but only for priority sector lending. The 45-day payment protection is for manufacturing and service units, so traders should put payment terms in writing. MSME for traders in Kerala.",
 cap_mg="Wholesale, retail kachavadakkarkkum Udyam edukkaam, pakshe bank loan-il munganakku maathram. 45 divasathe payment protection manufacturing, service units-nu aanu.")

duo("yd003", "loan_seeker", "A", "bank", "ലോൺ അപേക്ഷ.\nമാനേജർ: \"ഉദ്യം\nസർട്ടിഫിക്കറ്റ് ഉണ്ടോ?\"", [
 ("A","wide","മനോജ് സാറേ, മെഷീൻ വാങ്ങാനുള്ള ലോൺ അപേക്ഷ കൊണ്ടുവന്നു."),
 ("V","V","ശ്രുതി, പേപ്പർ എല്ലാം ഉണ്ടോ? ഉദ്യം സർട്ടിഫിക്കറ്റ് കണ്ടില്ലല്ലോ."),
 ("A","A","അത് നിർബന്ധമാണോ?"),
 ("V","V","MSME ആയി രജിസ്റ്റർ ചെയ്താൽ മുൻഗണനാ വായ്പയും ഈടില്ലാത്ത ലോൺ സ്കീമുകളും നോക്കാം."),
 ("A","wide","ആധാറും പാനും വെച്ച് ഓൺലൈൻ ആണല്ലോ. നാളെ തന്നെ."),
 ("V","wide","എങ്കിൽ ഫയൽ ഇവിടെ കാത്തിരിക്കും.")],
 "ലോണിന് മുമ്പ്\nഉദ്യം", CTA_UDYAM, theme="faq",
 cap_ml="മെഷീൻ വാങ്ങാൻ ബിസിനസ് ലോൺ അപേക്ഷിക്കുമ്പോൾ ബാങ്ക് ഉദ്യം സർട്ടിഫിക്കറ്റ് ചോദിക്കും. MSME രജിസ്ട്രേഷൻ മുൻഗണനാ വായ്പയ്ക്കും ഈടില്ലാത്ത ലോൺ സ്കീമുകൾക്കും വഴി തുറക്കും.",
 cap_en="Applying for a machinery loan and the bank asks for your Udyam certificate? MSME registration opens priority sector lending and collateral-free loan schemes. Udyam registration for business loans in Kerala.",
 cap_mg="Machine vaangaan business loan apply cheyyumbol bank Udyam certificate chodikkum. MSME registration priority lending-num collateral free loan schemes-num vazhi thurakkum.")

duo("yd004", "manufacturer", "B", "bakery", "ടേൺഓവർ 8 കോടി.\nമെഷീൻ 3 കോടി.\nമൈക്രോയോ സ്മോളോ?", [
 ("A","wide","സാബുച്ചേട്ടാ, നമ്മുടെ ബിസ്ക്കറ്റ് യൂണിറ്റ് മൈക്രോ ആണല്ലോ? ടേൺഓവർ 10 കോടിയിൽ താഴെ."),
 ("V","V","ജിഷേ, പുതിയ മെഷീൻ കൂടി വന്നപ്പോൾ നിക്ഷേപം 3 കോടി ആയി."),
 ("A","A","അപ്പോ?"),
 ("V","V","മൈക്രോ ആകാൻ നിക്ഷേപം 2.5 കോടിയിലും ടേൺഓവർ 10 കോടിയിലും താഴെ വേണം. രണ്ടും."),
 ("A","wide","ഒന്ന് കടന്നാൽ സ്മോൾ. ഉദ്യത്തിൽ ഡീറ്റെയിൽസ് പുതുക്കണം."),
 ("V","wide","മെഷീൻ വലുതായി, കാറ്റഗറിയും.")],
 "രണ്ട് ലിമിറ്റും\nനോക്കണം", CTA_MSME, theme="faq",
 cap_ml="2025 ഏപ്രിൽ മുതൽ മൈക്രോ ആകാൻ നിക്ഷേപം 2.5 കോടിയിലും ടേൺഓവർ 10 കോടിയിലും താഴെ വേണം. ഒന്ന് കടന്നാൽ സ്മോൾ. നിങ്ങളുടെ യൂണിറ്റ് ഏതാണ്?",
 cap_en="Turnover Rs 8 crore but machinery worth Rs 3 crore: micro or small? Since April 2025, micro means investment up to Rs 2.5 crore AND turnover up to Rs 10 crore; cross either and you are small. Which is your unit?",
 cap_mg="2025 April muthal micro aakaan investment 2.5 crore-ilum turnover 10 crore-ilum thaazhe venam. Onnu kadannaal small. Ningalude unit ethaanu?")

chat("yc001", "service_unit", "A", "വലിയ കമ്പനി ചോദിച്ചു:\n\"നിങ്ങൾ MSME\nരജിസ്റ്റേർഡ് ആണോ?\"", ("നീതു", "ജെയ്സൺ"), [
 (0,"ജെയ്സൺ, ആ ഐടി കമ്പനിയുടെ വെണ്ടർ ഫോമിൽ ഒരു ചോദ്യം: MSME രജിസ്റ്റേർഡ് ആണോ?"),
 (1,"അവർക്കെന്താ അതിൽ കാര്യം?"),
 (0,"MSME സപ്ലയർക്ക് 45 ദിവസത്തിനുള്ളിൽ പണം കൊടുത്തില്ലെങ്കിൽ അവർക്ക് ടാക്സ് ഡിഡക്ഷൻ പണം കൊടുക്കുന്ന വർഷത്തേക്ക് മാറും."),
 (1,"അപ്പോ നമുക്ക് പണം വേഗം കിട്ടും!"),
 (0,"അതിന് ആദ്യം ഉദ്യം വേണം. നമ്മുടെ ക്ലീനിംഗ് സർവീസിന് ഇതുവരെ എടുത്തിട്ടില്ല."),
 (1,"ഫോം ഇന്ന് പൂരിപ്പിക്കേണ്ട. ആദ്യം ഉദ്യം.")],
 "ബയർ ചോദിക്കുന്നത്\nവെറുതെയല്ല", CTA_UDYAM, theme="faq",
 cap_ml="വലിയ കമ്പനികൾ സപ്ലയർമാരോട് MSME രജിസ്റ്റേർഡ് ആണോ എന്ന് ചോദിക്കുന്നു: 45 ദിവസത്തിനുള്ളിൽ പണം കൊടുത്തില്ലെങ്കിൽ അവർക്ക് ടാക്സ് ഡിഡക്ഷൻ വൈകും (43B(h)). സർവീസ് യൂണിറ്റുകൾക്കും ഉദ്യം എടുക്കാം.",
 cap_en="Why do big companies ask suppliers whether they are MSME registered? Under section 43B(h), paying a micro or small supplier late delays the buyer's tax deduction. Service businesses can register on Udyam too.",
 cap_mg="Valiya companies suppliers-nodu MSME registered aano ennu chodikkunnu: 45 divasathinullil paisa koduthillenkil avarkku tax deduction vaikum. Service units-num Udyam edukkaam.")

lst("yl001", "manufacturer", "B", "ഉദ്യം എടുക്കും\nമുമ്പ് അറിയേണ്ട\n3 കാര്യം", [
 ("കാറ്റഗറി", "നിക്ഷേപവും ടേൺഓവറും രണ്ടും നോക്കി മൈക്രോ, സ്മോൾ, മീഡിയം."),
 ("45 ദിവസം", "മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്ക് മാത്രം. കടകൾക്ക് ഇല്ല."),
 ("പഴയ ഉദ്യോഗ് ആധാർ", "ഉണ്ടെങ്കിൽ ഉദ്യത്തിലേക്ക് മാറ്റണം.")],
 "ഏതാണ് നിങ്ങൾക്ക്\nപുതിയ അറിവ്?", CTA_MSME, theme="faq",
 cap_ml="ഉദ്യം MSME രജിസ്ട്രേഷന് മുമ്പ്: കാറ്റഗറി നിക്ഷേപവും ടേൺഓവറും നോക്കി; 45 ദിവസ സംരക്ഷണം മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്ക്; പഴയ ഉദ്യോഗ് ആധാർ ഉദ്യത്തിലേക്ക് മാറ്റണം.",
 cap_en="Three things to know before Udyam registration: your category depends on both investment and turnover, the 45-day payment protection is for manufacturing and service units only, and an old Udyog Aadhaar must move to Udyam.",
 cap_mg="Udyam edukkum mumbu: category investment-um turnover-um nokki; 45 divasa protection manufacturing, service units-nu; pazhaya Udyog Aadhaar Udyam-ilekku maattanam.")
