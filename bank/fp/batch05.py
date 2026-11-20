# Financial projections batch 05 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FP. Never mention our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

duo("fp020", "investor_pitch", "A", "office", "ഇൻവെസ്റ്റർ: \"ഡാറ്റ\nറൂം ലിങ്ക് അയക്കൂ\"\nഫൗണ്ടർ: \"തലയിലുണ്ട്\"", [
 ("A","wide","രാഹുലേ, ഇൻവെസ്റ്റർ ഡാറ്റ റൂം ലിങ്ക് ചോദിച്ചു. ഞാൻ പറഞ്ഞു, എല്ലാം എന്റെ തലയിലുണ്ടെന്ന്."),
 ("V","V","നേഹേ, നിന്റെ തല അവർക്ക് ഫോർവേഡ് ചെയ്യാൻ പറ്റില്ലല്ലോ."),
 ("A","A","അപ്പോ ആദ്യം എന്താ എഴുതിയുണ്ടാക്കേണ്ടത്?"),
 ("V","wide","മൂന്ന് വർഷത്തെ പ്രൊജക്ഷൻ, ആദ്യ വർഷം മാസം തോറും. കസ്റ്റമർ, വളർച്ച, ചെലവ്, ഓരോന്നിന്റെയും അനുമാനം എഴുതി."),
 ("A","A","ശരി. ഇന്ന് രാത്രി തല ഷീറ്റിലേക്ക് പകർത്താം."),
 ("V","wide","തലയിലുള്ളത് സ്വപ്നം, ഷീറ്റിലുള്ളത് പ്ലാൻ.")],
 "തലയിലുള്ളത് സ്വപ്നം,\nഷീറ്റിലുള്ളത് പ്ലാൻ", CTA_PROJECTION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ഡാറ്റ റൂം ചോദിച്ചപ്പോൾ ഫൗണ്ടറുടെ കയ്യിൽ ഐഡിയ മാത്രം, അതും തലയിൽ. ആദ്യം വേണ്ടത്: 3 വർഷത്തെ പ്രൊജക്ഷൻ, ആദ്യ വർഷം മാസം തോറും, ഓരോ നമ്പറിന്റെയും അനുമാനം എഴുതി. നിങ്ങളുടെ പ്ലാൻ ഇപ്പോൾ എവിടെ: തലയിലോ ഷീറ്റിലോ?",
 cap_en="An investor asked for a data room link and the founder had only the plan in her head. Start with 3-year financial projections, month by month for year one, with the assumption behind every number written down. Where is your plan right now: head or sheet?",
 cap_mg="Investor data room chodichappol founder-ude kayyil idea maathram, athum thalayil. Aadyam vendathu: 3 varshathe projection, aadya varsham maasam thorum, oro number-inteyum anumaanam ezhuthi. Ningalude plan ippol evide: thalayilo sheet-ilo?")

duo("fp021", "early_revenue", "B", "kitchen", "ആങ്ങളയുടെ ചോദ്യം:\n\"എന്റെ പൈസ എന്ന്\nതിരിച്ചു കിട്ടും?\"", [
 ("A","wide","രാജേഷേ, എന്റെ ആങ്ങള വിളിച്ചിരുന്നു. കപ്പപ്പൊടി യൂണിറ്റിൽ ഇട്ട പൈസ എന്ന് തിരിച്ചു കിട്ടും എന്ന്."),
 ("V","V","ബിന്ദൂ, ബിസിനസ് ഒന്ന് പിടിക്കുമ്പോൾ എന്ന് പറഞ്ഞേക്ക്."),
 ("A","A","അത് തീയതിയല്ല. അവൻ ചോദിക്കുന്നത് മാസമാ."),
 ("V","wide","ശരി. മാസം തോറും ക്യാഷ് ഫ്ലോ എഴുതി ബ്രേക്ക്-ഈവൻ മാസം കണ്ടുപിടിക്കാം. അതിന് ശേഷം മിച്ചം വരുന്ന മാസങ്ങൾ അപ്പോൾ കാണാം."),
 ("A","A","അപ്പോ ആങ്ങളയ്ക്കുള്ള ഉത്തരം ഷീറ്റിലാ."),
 ("V","wide","ബന്ധം കാക്കാൻ കണക്ക് കാക്കണം.")],
 "ബന്ധം കാക്കാൻ\nകണക്ക് കാക്കണം", CTA_FORECAST, theme="crm",
 cap_ml="കുടുംബത്തിൽ നിന്ന് പൈസ എടുത്ത് തുടങ്ങിയ കപ്പപ്പൊടി യൂണിറ്റ്. 'എന്ന് തിരിച്ചു കിട്ടും?' എന്ന ചോദ്യത്തിന് ഉത്തരം മാസ ക്യാഷ് ഫ്ലോയിലും ബ്രേക്ക്-ഈവൻ മാസത്തിലുമാണ്. നിങ്ങളുടെ ബിസിനസിൽ കുടുംബ പൈസ ഉണ്ടോ?",
 cap_en="A tapioca flour unit started with a brother-in-law's money, and now he asks when he gets it back. 'When business picks up' is not an answer: a monthly cash flow and the break-even month are. Family money in your business: yes or no?",
 cap_mg="Kudumbathil ninnu paisa eduthu thudangiya kappappodi unit. 'Ennu thirichu kittum?' enna chodyathinu utharam monthly cash flow-ilum break-even maasathilumaanu. Ningalude business-il kudumba paisa undo?")

duo("fp022", "investor_pitch", "C", "gulfoffice", "\"ഫേസ് 1-ന് ചെറിയ\nതുക, 3 വർഷത്തിൽ\nഇരട്ടി\" എങ്ങനെ?", [
 ("A","wide","ആസിഫേ, നിന്റെ മെസ്സേജ് കണ്ടു. 'ഫേസ് വണ്ണിന് ചെറിയ തുക, മൂന്ന് വർഷത്തിൽ ഇരട്ടി.' ഡെക്ക് എവിടെ?"),
 ("V","V","ഷഹാനാ, ഡെക്ക് ഇല്ല. പക്ഷേ നാട്ടിലെ ഫുട്ബോൾ ടർഫ് ഉറപ്പായും ഓടും."),
 ("A","A","'ഇരട്ടി' എന്ന വാക്ക് ഞാൻ എല്ലാ ആഴ്ചയും കേൾക്കുന്നതാ. അതിന്റെ പിന്നിലെ കണക്കാ എനിക്ക് വേണ്ടത്."),
 ("V","wide","എന്ത് കണക്ക്?"),
 ("A","wide","ടർഫ് ദിവസം എത്ര മണിക്കൂർ ബുക്ക് ആകും, എത്ര കൂടും, ചെലവ്, ക്യാഷ് ഫ്ലോ. ആദ്യ വർഷം മാസം തോറും, ഇന്നത്തെ ട്രാക്ഷനിൽ നിന്ന്."),
 ("V","V","വാക്ക് കൊണ്ട് ഇരട്ടിയാകില്ല, കണക്ക് കൊണ്ടേ.")],
 "വാക്ക് കൊണ്ട് ഇരട്ടിയില്ല,\nകണക്ക് കൊണ്ടേ", CTA_PROJECTION, theme="crm",
 cap_ml="'3 വർഷത്തിൽ ഇരട്ടി' എന്ന് മെസ്സേജ് അയച്ചു, ഡെക്കും നമ്പറും ഇല്ല. ഇൻവെസ്റ്റർ ചോദിക്കുന്നത് അതിന്റെ പിന്നിലെ കണക്ക്: ബുക്കിംഗ്, വളർച്ച, ചെലവ്, ക്യാഷ് ഫ്ലോ, ആദ്യ വർഷം മാസം തോറും. നിങ്ങൾ 'ഇരട്ടി' എന്ന് പറഞ്ഞിട്ടുണ്ടോ?",
 cap_en="A founder messages a Gulf investor: small money for phase one, double in three years. No deck, no numbers. Investors want the maths behind 'double': bookings, growth, costs and cash flow, month by month for year one, tied to traction. Ever promised 'double'?",
 cap_mg="'3 varshathil iratti' ennu message ayachu, deck-um number-um illa. Investor chodikkunnathu athinte pinnile kanakku: booking, valarcha, chelavu, cash flow, aadya varsham maasam thorum. Ningal 'iratti' ennu paranjittundo?")

duo("fp023", "grant_application", "A", "library", "ഇൻക്യുബേഷൻ ഫോം:\n\"അടുത്ത 3 വർഷം?\"\nഅവൾ എഴുതി: \"വളരും\"", [
 ("A","wide","അനൂപേ, മില്ലറ്റ് സ്നാക്ക് ബിസിനസിന്റെ ഇൻക്യുബേഷൻ ഫോമിൽ ഒരു ചോദ്യം: അടുത്ത മൂന്ന് വർഷം. ഞാൻ 'വളരും' എന്ന് എഴുതി."),
 ("V","V","ഗ്രീഷ്മേ, പാനൽ ഒരു വാക്കല്ല, ഒരു ഷീറ്റാ പ്രതീക്ഷിക്കുന്നത്."),
 ("A","A","എന്റെ കടയിൽ ആഴ്ചയിൽ എൺപത് പാക്കറ്റ് പോകുന്നുണ്ട്. അത് മതിയോ?"),
 ("V","wide","അതാ തുടക്കം. അതിൽ നിന്ന് കസ്റ്റമർ വളർച്ച, ചെലവ്, ആളെ എടുക്കുന്ന മാസം, ബ്രേക്ക്-ഈവൻ. ഗ്രാന്റ് പാനലും പ്രൊജക്ഷൻ ചോദിക്കും."),
 ("A","A","എൺപത് പാക്കറ്റിൽ നിന്ന് ഒരു കഥ, നമ്പറിൽ."),
 ("V","wide","വളരും എന്ന് എഴുതരുത്, എങ്ങനെ എന്ന് എഴുതൂ.")],
 "വളരും എന്ന് എഴുതരുത്,\nഎങ്ങനെ എന്ന് എഴുതൂ", CTA_FORECAST, theme="crm",
 cap_ml="മില്ലറ്റ് സ്നാക്ക് തുടങ്ങിയ ഒരു വനിതാ ഫൗണ്ടർ ഇൻക്യുബേഷൻ ഫോമിൽ 'അടുത്ത 3 വർഷം' എന്ന ചോദ്യത്തിന് 'വളരും' എന്ന് എഴുതി. ഗ്രാന്റ് പാനലുകൾ നോക്കുന്നത് ഇന്നത്തെ വിൽപ്പനയിൽ നിന്ന് തുടങ്ങുന്ന പ്രൊജക്ഷൻ. നിങ്ങൾ ഇൻക്യുബേഷന് അപേക്ഷിച്ചിട്ടുണ്ടോ?",
 cap_en="A woman founder selling millet snacks answers 'next 3 years?' on an incubation form with one word: grow. Incubators and grant panels ask for projections that start from today's sales: customer growth, costs, hiring and break-even. Applied for incubation yet?",
 cap_mg="Millet snack thudangiya oru vanitha founder incubation form-il 'adutha 3 varsham' enna chodyathinu 'valarum' ennu ezhuthi. Grant panel-ukal nokkunnathu innathe vilppanayil ninnu thudangunna projection. Ningal incubation-nu apekshichittundo?")

duo("fp024", "investor_pitch", "B", "petrolpump", "ആദ്യ വർഷം നഷ്ടം\nകാണിച്ചാൽ ഇൻവെസ്റ്റർ\nഓടുമോ?", [
 ("A","wide","ഷിബൂ, നമ്മുടെ ഡ്രോൺ വളം തളിക്കൽ സർവീസിന്റെ ഷീറ്റിൽ ആദ്യ വർഷം മുഴുവൻ നഷ്ടം. ആ വരി മായ്ച്ചാലോ?"),
 ("V","V","സന്തോഷേ, മായ്ച്ചാൽ ഇൻവെസ്റ്റർ ആദ്യം കാണുന്നത് അതുതന്നെയാ: മറച്ചുവെച്ചത്."),
 ("A","A","പക്ഷേ ചുവന്ന നമ്പർ കണ്ടാൽ അവർ പേടിക്കില്ലേ?"),
 ("V","wide","പുതിയ ബിസിനസിൽ ആദ്യം നഷ്ടം വരാം. അവർ നോക്കുന്നത് ക്യാഷ് ഫ്ലോയും ബ്രേക്ക്-ഈവൻ മാസവും. പെരുപ്പിച്ച നമ്പർ വിശ്വാസം കളയും."),
 ("A","A","അപ്പോ ചുവപ്പ് മറയ്ക്കണ്ട, അത് പച്ചയാകുന്ന മാസം കാണിക്കണം."),
 ("V","wide","നഷ്ടം ഒളിപ്പിച്ചാൽ വിശ്വാസം നഷ്ടം.")],
 "നഷ്ടം ഒളിപ്പിച്ചാൽ\nവിശ്വാസം നഷ്ടം", CTA_PROJECTION, theme="faq",
 cap_ml="പാടത്ത് ഡ്രോൺ കൊണ്ട് വളം തളിക്കുന്ന സ്റ്റാർട്ടപ്പ്, ആദ്യ വർഷത്തെ നഷ്ടം ഷീറ്റിൽ നിന്ന് മായ്ക്കാൻ നോക്കി. ഇൻവെസ്റ്റർ നോക്കുന്നത് റിയലിസ്റ്റിക് നമ്പറും ബ്രേക്ക്-ഈവൻ മാസവുമാണ്; പെരുപ്പിച്ച കണക്ക് വിശ്വാസം കളയും. നിങ്ങളുടെ ഷീറ്റിൽ ചുവപ്പ് ഉണ്ടോ?",
 cap_en="A paddy drone-spraying startup wants to delete the year-one loss from its projections. Investors look for realistic numbers, the cash flow and the break-even month; hidden or inflated numbers lose trust. Any red in your sheet?",
 cap_mg="Paadathu drone kondu valam thalikkunna startup, aadya varshathe nashtam sheet-il ninnu maaykkaan nokki. Investor nokkunnathu realistic number-um break-even maasavumaanu; peruppicha kanakku vishwaasam kalayum. Ningalude sheet-il chuvappu undo?")

duo("fp025", "early_revenue", "C", "textile", "\"എല്ലാവരും 20%\nവളർച്ച ഇടുന്നു,\nനമ്മളും ഇട്ടാലോ?\"", [
 ("A","wide","പ്രകാശേ, വാഴനാര് ബാഗിന്റെ പ്രൊജക്ഷനിൽ ഓരോ വർഷവും ഇരുപത് ശതമാനം വളർച്ച ഇട്ടു. എല്ലാവരും അങ്ങനെയാ ഇടുന്നത്."),
 ("V","V","രമ്യേ, ആ ഇരുപത് എവിടുന്ന് വന്നു? എല്ലാവരിൽ നിന്നോ, നമ്മുടെ കടയിൽ നിന്നോ?"),
 ("A","A","കേട്ടറിവാ."),
 ("V","wide","വളർച്ച ഒരു ശതമാനത്തിൽ തുടങ്ങില്ല. എത്ര കസ്റ്റമർ, ഒരാൾ എത്ര വാങ്ങും, എത്ര കൂടും. ഓരോന്നിനും എഴുതിയ കാരണം വേണം."),
 ("A","A","ഈ വർഷം രണ്ട് ഹോട്ടലുകൾ ഓർഡർ ആവർത്തിച്ചു. അവിടെ നിന്ന് തുടങ്ങാം."),
 ("V","wide","കേട്ട ശതമാനമല്ല, കണ്ട കസ്റ്റമർ.")],
 "കേട്ട ശതമാനമല്ല,\nകണ്ട കസ്റ്റമർ", CTA_FORECAST, theme="faq",
 cap_ml="വാഴനാര് ബാഗ് ബ്രാൻഡ് 'എല്ലാവരും ഇടുന്നു' എന്ന് പറഞ്ഞ് 20% വളർച്ച ഷീറ്റിൽ ഇട്ടു. വളർച്ച ഡ്രൈവറുകളിൽ നിന്ന് വരണം: കസ്റ്റമർ എത്ര, ഒരാൾ എത്ര വാങ്ങും, എത്ര കൂടും, കാരണം എഴുതി. നിങ്ങളുടെ വളർച്ച ശതമാനം എവിടുന്ന് വന്നു?",
 cap_en="A banana-fibre bag brand puts 20% growth a year in its projections because 'everyone does'. Growth should come from revenue drivers: how many customers, how much each buys, how fast that grows, with written reasons. Where did your growth number come from?",
 cap_mg="Vaazhanaaru bag brand 'ellaavarum idunnu' ennu paranju 20% valarcha sheet-il ittu. Valarcha drivers-il ninnu varanam: customer ethra, oraal ethra vaangum, ethra koodum, kaaranam ezhuthi. Ningalude valarcha shathamaanam evidunnu vannu?")

duo("fp026", "investor_pitch", "A", "mobileshop", "ഇൻവെസ്റ്റർ ചോദിച്ചു:\n\"ഈ നമ്പർ എങ്ങനെ?\"\nഫൗണ്ടർ പാർട്ണറെ നോക്കി", [
 ("A","wide","ഫഹദേ, മീറ്റിംഗിൽ ഇൻവെസ്റ്റർ ചോദിച്ചു: മൂന്നാം മാസം റിപ്പയർ ഓർഡർ ഇരട്ടിയാകുന്നത് എങ്ങനെ? ഞാൻ നിന്നെ നോക്കി."),
 ("V","V","ഹന്നാ, ഷീറ്റ് ഞാൻ ഉണ്ടാക്കിയതാ. പക്ഷേ മീറ്റിംഗിൽ സംസാരിക്കേണ്ടത് നീയാ."),
 ("A","A","എനിക്ക് കസ്റ്റമറെ അറിയാം, ഷീറ്റിലെ ഫോർമുല അറിയില്ല."),
 ("V","wide","ഫോർമുല വേണ്ട. ഓരോ നമ്പറിന്റെയും അനുമാനം എഴുതി വെക്കാം: എത്ര കടകൾ, എത്ര ഓർഡർ, ആളെ എപ്പോൾ എടുക്കും. നീ അത് പറഞ്ഞാൽ മതി."),
 ("A","A","ഷീറ്റ് നിന്റേത്, കഥ എന്റേത്."),
 ("V","wide","ഷീറ്റ് ആര് ഉണ്ടാക്കിയാലും, ഉത്തരം ഫൗണ്ടറുടേതാ.")],
 "ഷീറ്റ് ആര് ഉണ്ടാക്കിയാലും,\nഉത്തരം ഫൗണ്ടറുടേത്", CTA_PROJECTION, theme="faq",
 cap_ml="ഫോൺ റിപ്പയർ സ്റ്റാർട്ടപ്പിന്റെ പ്രൊജക്ഷൻ കോ-ഫൗണ്ടർ ഉണ്ടാക്കി, ഇൻവെസ്റ്റർ ചോദിച്ചപ്പോൾ ഫൗണ്ടർക്ക് വിശദീകരിക്കാൻ പറ്റിയില്ല. ഓരോ നമ്പറിന്റെയും അനുമാനം എഴുതി വെച്ചാൽ ആർക്കും പറയാം. നിങ്ങളുടെ ടീമിൽ ഷീറ്റ് ഉണ്ടാക്കുന്നത് ആരാ?",
 cap_en="A co-founder built the projections for their phone-repair startup, and when the investor asked how orders double by month three, the founder couldn't explain. Write the assumption behind every number so whoever pitches can answer. Who builds the sheet in your team?",
 cap_mg="Phone repair startup-inte projection co-founder undaakki, investor chodichappol founder-kku vishadeekarikkaan pattiyilla. Oro number-inteyum anumaanam ezhuthi vechaal aarkkum parayaam. Ningalude team-il sheet undaakkunnathu aaraa?")

duo("fp027", "early_revenue", "B", "hospital", "സർവീസ് ബിസിനസാ,\nസ്റ്റോക്ക് ഇല്ല. പിന്നെ\nപ്രൊജക്ഷൻ എന്തിന്?", [
 ("A","wide","ജോസഫേ, വീട്ടിൽ ചെന്ന് ഫിസിയോ ചെയ്യുന്നതല്ലേ നമ്മുടെ ബിസിനസ്. സ്റ്റോക്കും മെഷീനും ഇല്ല. പിന്നെന്തിനാ പ്രൊജക്ഷൻ?"),
 ("V","V","ലക്ഷ്മീ, നമ്മുടെ സ്റ്റോക്ക് തെറാപ്പിസ്റ്റിന്റെ സമയമാ. ഒരാൾക്ക് ദിവസം എത്ര വീട്ടിൽ പോകാൻ പറ്റും?"),
 ("A","A","ട്രാഫിക്കിൽ... അഞ്ച്, കൂടിയാൽ ആറ്."),
 ("V","wide","അപ്പോ രോഗികൾ കൂടിയാൽ ആളെയും എടുക്കണം. എത്ര രോഗി, എത്ര തെറാപ്പിസ്റ്റ്, ഏത് മാസം എടുക്കും, ശമ്പളച്ചെലവ്. അതാണ് നമ്മുടെ പ്രൊജക്ഷൻ."),
 ("A","A","സാധനം വിൽക്കുന്നവർക്ക് സ്റ്റോക്ക്, നമുക്ക് മണിക്കൂർ."),
 ("V","wide","മണിക്കൂർ തീർന്നാൽ വളർച്ചയും തീരും.")],
 "മണിക്കൂർ തീർന്നാൽ\nവളർച്ചയും തീരും", CTA_FORECAST, theme="faq",
 cap_ml="വീട്ടിൽ ചെന്ന് ഫിസിയോതെറാപ്പി ചെയ്യുന്ന സർവീസ് ബിസിനസിന് സ്റ്റോക്ക് ഇല്ല, പക്ഷേ ഓരോ തെറാപ്പിസ്റ്റിനും ദിവസം കുറച്ച് മണിക്കൂർ മാത്രം. വളർച്ചയുടെ കണക്കിൽ ആളെ എടുക്കുന്ന മാസവും ശമ്പളച്ചെലവും വേണം. നിങ്ങളുടെ ബിസിനസ്: സാധനമോ സർവീസോ?",
 cap_en="A home-visit physiotherapy service thinks projections are only for businesses with stock. Its stock is therapist hours: each can do only so many visits a day, so growth needs hiring, and hiring needs a month and a salary cost in the projection. Your business: goods or services?",
 cap_mg="Veettil chennu physiotherapy cheyyunna service business-nu stock illa, pakshe oro therapist-inum divasam kurachu manikkoor maathram. Valarchayude kanakkil aale edukkunna maasavum shambalachelavum venam. Ningalude business: saadhanamo service-o?")

duo("fp028", "early_revenue", "C", "railway", "സ്റ്റേഷനിൽ മാസം\n3,000 കരിക്ക്.\n\"എല്ലാം ലാഭമല്ലേ?\"", [
 ("A","wide","ദിനേശേ, നാല് സ്റ്റേഷനിലെ കരിക്ക് കിയോസ്കിൽ മാസം മൂവായിരം കരിക്ക് പോകുന്നു. പത്ത് സ്റ്റേഷനാക്കിയാൽ ലാഭം കുതിക്കും."),
 ("V","V","ഷീബേ, ആ ഷീറ്റിൽ വരുമാനം മാത്രമേ ഉള്ളൂ. കിയോസ്ക് വാടക, ജോലിക്കാർ, ലോറി, ചീഞ്ഞുപോകുന്ന കരിക്ക് എവിടെ?"),
 ("A","A","അതൊക്കെ ചെറിയ കാര്യങ്ങളല്ലേ?"),
 ("V","wide","പത്ത് സ്റ്റേഷനാകുമ്പോൾ ചെറുതല്ല. ചെലവും ആളെ എടുക്കലും ചേർത്ത് ലാഭനഷ്ട കണക്കും മാസ ക്യാഷ് ഫ്ലോയും നോക്കണം."),
 ("A","A","ഓരോ കരിക്കിന്റെ പിന്നിലും ഒരു ചെലവുണ്ട്, അല്ലേ?"),
 ("V","wide","കരിക്ക് വെട്ടാൻ കത്തി, ചെലവ് വെട്ടാൻ കണക്ക്.")],
 "കരിക്ക് വെട്ടാൻ കത്തി,\nചെലവ് വെട്ടാൻ കണക്ക്", CTA_PROJECTION, theme="new",
 cap_ml="റെയിൽവേ സ്റ്റേഷനിലെ കരിക്ക് കിയോസ്കുകൾ 4-ൽ നിന്ന് 10 ആക്കാൻ പ്ലാൻ, ഷീറ്റിൽ വരുമാനം മാത്രം. വാടക, ജോലിക്കാർ, ട്രാൻസ്പോർട്ട്, കേടാകുന്ന സ്റ്റോക്ക് ചേർത്ത് ലാഭനഷ്ട കണക്കും മാസ ക്യാഷ് ഫ്ലോയും വേണം. നിങ്ങളുടെ ഷീറ്റിൽ ചെലവ് കോളം ഉണ്ടോ?",
 cap_en="A tender-coconut kiosk business at railway stations plans to grow from 4 stations to 10 with a sheet that shows only sales. Rent, staff, transport and spoiled stock belong in the P&L and the monthly cash flow too. Does your sheet have a cost column?",
 cap_mg="Railway station-ile karikku kiosk-ukal 4-il ninnu 10 aakkaan plan, sheet-il varumaanam maathram. Vaadaka, jolikkaar, transport, kedaakunna stock cherthu P&L-um monthly cash flow-um venam. Ningalude sheet-il chelavu column undo?")

chat("fpc002", "early_revenue", "A", "ബ്രേക്ക്-ഈവൻ ഒമ്പതാം\nമാസം എന്ന് എഴുതി.\nഒമ്പതാം മാസം വന്നു", ("ഗായത്രി", "അനന്തു"), [
 (0,"അനന്തു, ഒമ്പതാം മാസമായി. കയാക്ക് ടൂറിന് ഇപ്പോഴും നഷ്ടം. നമ്മുടെ പ്രൊജക്ഷൻ മുഴുവൻ തെറ്റായിരുന്നോ?"),
 (1,"ഗായത്രീ, മുഴുവനല്ല. അനുമാനങ്ങൾ എഴുതി വെച്ചിരുന്നല്ലോ. ഓരോന്നും ഇന്നത്തെ നമ്പറുമായി ഒത്തുനോക്കാം."),
 (0,"വീക്കെൻഡ് ബുക്കിംഗ് ശരി. ചെലവും ശരി. ഇടദിവസങ്ങളിൽ കരുതിയതിന്റെ പകുതി ആളേ വരുന്നുള്ളൂ."),
 (1,"അതാണ് കാരണം. അനുമാനം എഴുതിയതുകൊണ്ട് തെറ്റിയ വരി ഒരു മിനിറ്റിൽ കിട്ടി. ഇനി അത് മാത്രം ശരിയാക്കിയാൽ മതി."),
 (0,"അപ്പോ ഇടദിവസത്തേക്ക് കോളേജ് ടൂറുകൾ പിടിക്കാം."),
 (1,"എഴുതിയ അനുമാനം തെറ്റിയാലും വഴി കാട്ടും.")],
 "എഴുതിയ അനുമാനം\nതെറ്റിയാലും വഴി കാട്ടും", CTA_FORECAST, theme="new",
 cap_ml="കായലിലെ കയാക്ക് ടൂർ ബിസിനസ് ബ്രേക്ക്-ഈവൻ 9-ാം മാസം എന്ന് കണക്കാക്കി, 9-ാം മാസം വന്നിട്ടും നഷ്ടം. അനുമാനങ്ങൾ എഴുതി വെച്ചതുകൊണ്ട് തെറ്റിയത് ഏത് വരി എന്ന് ഉടനെ കിട്ടി. നിങ്ങളുടെ അനുമാനങ്ങൾ എഴുതി വെച്ചിട്ടുണ്ടോ?",
 cap_en="A backwater kayak-tour business expected to break even in month 9; month 9 came with a loss. Because every assumption was written down, they found the one line that was wrong (weekday visitors) in a minute. Are your assumptions written down?",
 cap_mg="Kaayalile kayak tour business break-even 9-aam maasam ennu kanakkaakki, 9-aam maasam vannittum nashtam. Anumaanangal ezhuthi vechathukondu thettiyathu ethu vari ennu udane kitti. Ningalude anumaanangal ezhuthi vechittundo?")
