# Financial projections batch 06 (20 Nov night, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FP. Never mention our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST


# crm (C22 variant): the ask covered the machine, not the months until buyers pay
duo("fp029", "pre_revenue", "A", "fishmarket", "ചോദിച്ചത് മെഷീന്റെ\nപൈസ മാത്രം.\nമൂന്നാം മാസം കാലി", [
 ("A","wide","ആന്റണീ, ഉണക്കമീൻ പാക്കിംഗ് മെഷീന്റെ കൊട്ടേഷൻ മാത്രം കാണിച്ചാ ഞാൻ ഇൻവെസ്റ്റ്മെന്റ് ചോദിച്ചത്."),
 ("V","V","സുമേ, മെഷീൻ വന്നാൽ മീൻ വാങ്ങണം, ശമ്പളം കൊടുക്കണം. സൂപ്പർമാർക്കറ്റ് പൈസ തരുന്നത് 60 ദിവസം കഴിഞ്ഞല്ലേ?"),
 ("A","A","അയ്യോ, അത് ഷീറ്റിലേ ഇല്ല."),
 ("V","wide","ആദ്യ വർഷം മാസം തിരിച്ചുള്ള ക്യാഷ് ഫ്ലോ ഇട്ടാൽ ഏത് മാസം പൈസ തീരുമെന്ന് കാണാം. ചോദിക്കേണ്ട തുക അവിടെ നിന്നാ വരുന്നത്."),
 ("A","A","അപ്പോ മെഷീൻ മാത്രം വാങ്ങിയാൽ ബിസിനസ് ആയില്ല."),
 ("V","wide","മെഷീൻ മീൻ ഉണക്കും. ക്യാഷ് ഫ്ലോ കമ്പനി ഉണക്കാതെ നോക്കും.")],
 "മെഷീൻ മീൻ ഉണക്കും,\nക്യാഷ് ഫ്ലോ കമ്പനിയെ\nകാക്കും", CTA_PROJECTION, theme="crm",
 cap_ml="ഉണക്കമീൻ പാക്കിംഗ് യൂണിറ്റ് മെഷീന്റെ ചെലവ് മാത്രം നോക്കി ഇൻവെസ്റ്റ്മെന്റ് ചോദിച്ചു; വാങ്ങുന്നവർ പൈസ തരുന്നത് 60 ദിവസം കഴിഞ്ഞ്. ആദ്യ വർഷം മാസം തിരിച്ചുള്ള ക്യാഷ് ഫ്ലോ ഏത് മാസം പൈസ തീരുമെന്ന് കാണിക്കും. നിങ്ങളുടെ കസ്റ്റമർ എത്ര ദിവസത്തിൽ പൈസ തരും?",
 cap_en="A dried-fish packing unit asked investors for the machine's cost alone, while its supermarket buyers pay after 60 days. A month-by-month cash flow for year one shows the month the money runs out, and that is where the ask should come from. How many days do your customers take to pay?",
 cap_mg="Unakkameen packing unit machine-inte chelavu maathram nokki investment chodichu; vaangunnavar paisa tharunnathu 60 divasam kazhinju. Aadya varsham maasam thirichulla cash flow ethu maasam paisa theerumennu kaanikkum. Ningalude customer ethra divasathil paisa tharum?")

# crm (C23 variant): years of history, numbers scattered; start from actuals
duo("fp030", "early_revenue", "B", "teashop", "9 വർഷത്തെ ബിസിനസ്.\nകണക്ക് 3 ബാങ്കിലും\nഒരു ബുക്കിലും", [
 ("A","wide","വിഷ്ണൂ, ചായപ്പൊടി വിതരണം ഒമ്പത് വർഷമായി. ഇൻവെസ്റ്റർ മൂന്ന് വർഷത്തെ പ്രൊജക്ഷൻ ചോദിച്ചു. ഞാൻ എവിടെ തുടങ്ങും?"),
 ("V","V","അനൂ, പുതിയ നമ്പർ എഴുതും മുമ്പ് പഴയത് ഒന്നിച്ചാക്ക്. മൂന്ന് ബാങ്ക് സ്റ്റേറ്റ്മെന്റും ആ നോട്ടുബുക്കും."),
 ("A","A","വളർച്ച അത്ര വലുതല്ല. കുറച്ച് കൂട്ടി കാണിച്ചാലോ?"),
 ("V","wide","വേണ്ട. ഇന്നത്തെ വിൽപ്പനയിൽ നിന്ന് തുടങ്ങണം, ഓരോ വളർച്ചക്കും എഴുതിയ കാരണം വേണം. കൂട്ടിയ നമ്പർ വിശ്വാസം കളയും."),
 ("A","A","ഒമ്പത് വർഷം സ്ഥിരം നിന്നത് തന്നെ എന്റെ തെളിവ്."),
 ("V","wide","പഴയ കണക്ക് അടിത്തറ. പുതിയ കണക്ക് അതിന്റെ മുകളിലെ നില.")],
 "പഴയ കണക്ക് അടിത്തറ,\nപുതിയത് മുകളിലെ നില", CTA_FORECAST, theme="crm",
 cap_ml="ഒമ്പത് വർഷത്തെ ചായപ്പൊടി വിതരണം, കണക്ക് മൂന്ന് ബാങ്കിലും ഒരു നോട്ടുബുക്കിലും. പ്രൊജക്ഷൻ ഇന്നത്തെ യഥാർത്ഥ വിൽപ്പനയിൽ നിന്ന് തുടങ്ങണം, ഓരോ വളർച്ചക്കും എഴുതിയ കാരണം വേണം; കൂട്ടിക്കാണിച്ച നമ്പർ വിശ്വാസം കളയും. നിങ്ങളുടെ കണക്ക് എത്ര സ്ഥലത്താ?",
 cap_en="Nine years of tea-dust distribution, with the numbers spread over three bank accounts and a notebook. A projection starts from real sales today, with a written reason for every bit of growth; inflated numbers lose trust. In how many places are your numbers kept?",
 cap_mg="Ombathu varshathe chaayappodi vitharanam, kanakku moonnu bank-ilum oru notebook-ilum. Projection innathe yathaartha vilppanayil ninnu thudanganam, oro valarchakkum ezhuthiya kaaranam venam; koottikkaanicha number viswaasam kalayum. Ningalude kanakku ethra sthalathaa?")

# crm (C21 variant): rejected for no sales; tie projections to a small pilot
duo("fp031", "pre_revenue", "A", "hostel", "\"സെയിൽസ് ഇല്ല\"\nഎന്ന് റിജക്ഷൻ.\nമറുപടി: വലിയ ഷീറ്റ്", [
 ("A","wide","സഞ്ജൂ, സെയിൽസ് ഇല്ലെന്ന് പറഞ്ഞാ ഇൻവെസ്റ്റർ റിജക്റ്റ് ചെയ്തത്. ഞാൻ അഞ്ച് വർഷത്തെ വലിയ പ്രൊജക്ഷൻ ഉണ്ടാക്കി അയക്കട്ടെ?"),
 ("V","V","അലീനേ, വലിയ ഷീറ്റ് സെയിൽസ് ആവില്ല. നമ്മുടെ സ്പോക്കൺ ഇംഗ്ലീഷ് ആപ്പിന് ഒരു ചെറിയ പെയ്ഡ് ബാച്ച് ആദ്യം."),
 ("A","A","നാൽപ്പത് കുട്ടികൾ മതിയോ?"),
 ("V","wide","മതി. എത്ര പേർ ചേർന്നു, എത്ര പേർ തുടർന്നു എന്നത് വെച്ച് 3 വർഷത്തെ പ്രൊജക്ഷൻ. ട്രാക്ഷനോട് ചേർന്ന നമ്പറാ ഇൻവെസ്റ്റർ വിശ്വസിക്കുന്നത്."),
 ("A","A","അപ്പോ ആദ്യം ക്ലാസ്, പിന്നെ കണക്ക്."),
 ("V","wide","നാൽപ്പത് യഥാർത്ഥ കുട്ടികൾ, നാല്പതിനായിരം സ്വപ്നക്കുട്ടികളെക്കാൾ നല്ലത്.")],
 "40 യഥാർത്ഥ കസ്റ്റമർ,\n40,000 സ്വപ്നത്തെക്കാൾ\nഭാരം", CTA_PROJECTION, theme="crm",
 cap_ml="'സെയിൽസ് ഇല്ല' എന്ന് റിജക്ഷൻ കിട്ടിയപ്പോൾ മറുപടിയായി വലിയ ഷീറ്റ് അല്ല വേണ്ടത്. ചെറിയ പെയ്ഡ് പൈലറ്റ്, പിന്നെ അതിന്റെ നമ്പർ വെച്ച് 3 വർഷത്തെ പ്രൊജക്ഷൻ; ട്രാക്ഷനോട് ചേർന്ന നമ്പറാ വിശ്വാസം നേടുന്നത്. നിങ്ങൾക്ക് ആദ്യ പെയ്ഡ് കസ്റ്റമർ ഉണ്ടോ?",
 cap_en="Rejected for 'no sales', a spoken-English app founder wants to reply with a bigger 5-year spreadsheet. A small paid pilot comes first; then build the 3-year projection from how many joined and how many stayed. Numbers tied to traction are the ones investors trust. Do you have your first paying customer?",
 cap_mg="'Sales illa' ennu rejection kittiyappol marupadiyaayi valiya sheet alla vendathu. Cheriya paid pilot, pinne athinte number vechu 3 varshathe projection; traction-nodu chernna number aa viswaasam nedunnathu. Ningalkku aadya paid customer undo?")

# crm (C24 variant): mentee built only the P&L
duo("fp032", "investor_pitch", "B", "canteen", "\"ലാഭം കാണിച്ചാൽ\nമതിയല്ലോ\" മെന്റീ\nഒറ്റ ഷീറ്റുമായി", [
 ("A","wide","അമലേ, ഇൻകുബേറ്ററിലെ മെന്ററാ നീ. എന്റെ P&L നോക്ക്, മൂന്നാം വർഷം ലാഭം. ഇത് മതിയല്ലോ?"),
 ("V","V","ആതിരേ, P&L ഒരു ഷീറ്റ് മാത്രം. ഇൻവെസ്റ്റർ കൂടെ രണ്ടെണ്ണം കൂടി നോക്കും."),
 ("A","A","ഇനിയും രണ്ടോ? ഏതൊക്കെ?"),
 ("V","wide","ക്യാഷ് ഫ്ലോ, ബ്രേക്ക്-ഈവൻ. പിന്നെ ഓരോ നമ്പറിന്റെയും പിന്നിൽ എഴുതിയ അനുമാനങ്ങൾ."),
 ("A","A","ലാഭം ഉത്തരം. ബാക്കി എല്ലാം ആ ഉത്തരത്തിന്റെ വഴി."),
 ("V","wide","ഉത്തരം മാത്രം എഴുതിയാൽ മാർക്ക് കിട്ടില്ല. വഴിയും കാണിക്കണം.")],
 "ഉത്തരം മാത്രം പോരാ,\nവഴിയും കാണിക്കണം", CTA_PROJECTION, theme="crm",
 cap_ml="മൂന്നാം വർഷം ലാഭം കാണിക്കുന്ന ഒരു P&L മാത്രം മതിയോ? ഇൻവെസ്റ്റർ ക്യാഷ് ഫ്ലോയും ബ്രേക്ക്-ഈവനും ഓരോ നമ്പറിന്റെ പിന്നിലെ എഴുതിയ അനുമാനങ്ങളും കൂടി നോക്കും. നിങ്ങളുടെ പ്രൊജക്ഷനിൽ എത്ര ഷീറ്റ് ഉണ്ട്?",
 cap_en="Is one P&L showing profit in year three enough? Investors also look at the cash flow, the break-even point and the written assumptions behind every number. Profit is the answer; they want to see the working. How many sheets are in your projection?",
 cap_mg="Moonnaam varsham laabham kaanikkunna oru P&L maathram mathiyo? Investor cash flow-um break-even-um oro number-inte pinnile ezhuthiya anumaanangalum koodi nokkum. Ningalude projection-il ethra sheet undu?")

# faq: three years month by month? only year one
duo("fp033", "bank_loan", "C", "cafe", "36 മാസം,\n36 കോളം.\n\"ഇത് ഞാൻ തീർക്കില്ല\"", [
 ("A","wide","റോഷാ, കഫേ ലോണിന് മൂന്ന് വർഷം പ്രൊജക്ഷൻ. 36 മാസം, 36 കോളം. ഞാൻ ഇന്ന് ഉറങ്ങില്ല."),
 ("V","V","ആൽവിനേ, എല്ലാ വർഷവും മാസം തിരിക്കണ്ട. മാസം തിരിച്ച് വേണ്ടത് ആദ്യ വർഷം മാത്രം."),
 ("A","A","അപ്പോ രണ്ടും മൂന്നും വർഷം?"),
 ("V","wide","അവ വർഷം തിരിച്ച് മതി. ആദ്യ 12 മാസത്തിലാ മഴക്കാലവും പുതിയ മെഷീനും ഒക്കെ ക്യാഷിനെ തൊടുന്നത്."),
 ("A","A","12 കോളം കൃത്യം, ബാക്കി രണ്ട് കോളം."),
 ("V","wide","അടുത്ത മാസം അടുത്ത് കാണണം, മൂന്നാം വർഷം ദൂരെ നിന്ന് മതി.")],
 "അടുത്തുള്ളത് അടുത്ത്,\nദൂരെയുള്ളത് ദൂരെ നിന്ന്", CTA_FORECAST, theme="faq",
 cap_ml="3 വർഷത്തെ പ്രൊജക്ഷൻ എന്നാൽ 36 മാസത്തെ കോളം വേണോ? വേണ്ട. ആദ്യ വർഷം മാസം തിരിച്ച്, രണ്ടും മൂന്നും വർഷം വർഷം തിരിച്ച്. നിങ്ങളുടെ ഷീറ്റിൽ എത്ര കോളം ഉണ്ട്?",
 cap_en="Does a 3-year projection mean 36 monthly columns? No: month by month for the first year, then year by year for years two and three. The first 12 months are where seasons and new purchases hit your cash. How many columns does your sheet have?",
 cap_mg="3 varshathe projection ennaal 36 maasathe column veno? Venda. Aadya varsham maasam thirichu, randum moonnum varsham varsham thirichu. Ningalude sheet-il ethra column undu?")

# faq: best festival day copied into every day of the year
duo("fp034", "early_revenue", "A", "juiceshop", "ഓണം വീക്കിലെ\n300 ഷേക്ക്.\nഷീറ്റിൽ 365 ദിവസവും", [
 ("A","wide","നൗഷാദേ, ഓണം വീക്കിൽ ഒരു ദിവസം 300 ഷേക്ക് വിറ്റു. ഷീറ്റിൽ വർഷം മുഴുവൻ ദിവസം 300 എന്നിട്ടു!"),
 ("V","V","റസിയേ, ജൂണിൽ മഴയത്ത് 60 കടന്നിട്ടുണ്ടോ? കോളേജ് അവധിക്ക് അതിലും കുറവ്."),
 ("A","A","ഒരു ശരാശരി ഇടാമെന്ന് കരുതി."),
 ("V","wide","ആദ്യ വർഷം മാസം തിരിച്ച് എഴുതണം. ഓരോ നമ്പറിനും എഴുതിയ കാരണം വേണം. ഊതിവീർപ്പിച്ച നമ്പർ വിശ്വാസം കളയും."),
 ("A","A","അപ്പോ ഓണവും മഴയും ഷീറ്റിൽ വേറെ വേറെ."),
 ("V","wide","ഒരു ദിവസത്തെ തിരക്ക് ഒരു വർഷത്തെ കണക്കല്ല.")],
 "ഒരു ദിവസത്തെ തിരക്ക്\nഒരു വർഷത്തെ\nകണക്കല്ല", CTA_PROJECTION, theme="faq",
 cap_ml="ഓണം വീക്കിലെ ഏറ്റവും നല്ല ദിവസത്തെ വിൽപ്പന വർഷം മുഴുവൻ ഷീറ്റിൽ ഇട്ടാൽ എന്താകും? ആദ്യ വർഷം മാസം തിരിച്ച് എഴുതണം, ഓരോ നമ്പറിനും കാരണം വേണം; ഊതിവീർപ്പിച്ച നമ്പർ വിശ്വാസം കളയും. നിങ്ങളുടെ ബിസിനസിന്റെ മോശം മാസം ഏത്?",
 cap_en="A juice shop sold 300 shakes on its best Onam day and put 300 a day into every day of its projection. Year one has to be month by month, with a written reason for each number, so rainy and holiday months show; inflated numbers lose trust. Which is your slowest month?",
 cap_mg="Onam week-ile ettavum nalla divasathe vilppana varsham muzhuvan sheet-il ittaal enthaakum? Aadya varsham maasam thirichu ezhuthanam, oro number-num kaaranam venam; oothiveerppicha number viswaasam kalayum. Ningalude business-inte mosham maasam ethu?")

# faq: growth with no marketing cost behind it
duo("fp035", "pre_revenue", "B", "gym", "ആദ്യ വർഷം\n500 മെമ്പർ.\nമാർക്കറ്റിംഗ് ചെലവ്: 0", [
 ("A","wide","ജസ്റ്റിനേ, ലേഡീസ് ഫിറ്റ്നസ് ആപ്പിന് ആദ്യ വർഷം 500 മെമ്പർ. ചെലവിൽ റെന്റും ട്രെയിനറും മാത്രം."),
 ("V","V","റിയേ, 500 പേർ എങ്ങനെ അറിയും? പരസ്യം, ഓഫർ, ഇൻസ്റ്റാഗ്രാം. അതിനൊന്നും ചെലവില്ലേ?"),
 ("A","A","വാമൊഴി മതിയെന്ന് കരുതി."),
 ("V","wide","കസ്റ്റമർ കൂടുമ്പോൾ ചെലവും കൂടണം. വളർച്ചയും ചെലവും ഒരേ ഷീറ്റിൽ ചേരാതെ വന്നാൽ നമ്പർ വിശ്വസിക്കില്ല."),
 ("A","A","അപ്പോ ഓരോ മെമ്പറിന്റെ പിന്നിലും ഒരു ചെലവുണ്ട്."),
 ("V","wide","മസിൽ വെറുതെ വളരില്ല. മെമ്പർഷിപ്പും.")],
 "മസിലും മെമ്പർഷിപ്പും\nവെറുതെ വളരില്ല", CTA_FORECAST, theme="faq",
 cap_ml="ആദ്യ വർഷം 500 മെമ്പർമാർ, പക്ഷേ മാർക്കറ്റിംഗ് ചെലവ് പൂജ്യം. കസ്റ്റമർ വളർച്ച കാണിക്കുമ്പോൾ അത് കൊണ്ടുവരാനുള്ള ചെലവും പ്രൊജക്ഷനിൽ വേണം; ചേരാത്ത നമ്പർ വിശ്വാസം കളയും. നിങ്ങളുടെ കസ്റ്റമർ വരുന്നത് എവിടെ നിന്ന്?",
 cap_en="500 members in year one, and zero marketing cost in the sheet. When a projection shows customers growing, the cost of getting them has to be in it too; growth and costs that don't match lose trust. Where do your customers come from?",
 cap_mg="Aadya varsham 500 members, pakshe marketing chelavu poojyam. Customer valarcha kaanikkumbol athu konduvaraanulla chelavum projection-il venam; cheraatha number viswaasam kalayum. Ningalude customer varunnathu evide ninnu?")

# faq + d904: coir machine maker banking on one big order
duo("fp036", "investor_pitch", "C", "garage", "കയർ റോബോട്ട്:\n\"ഒറ്റ വലിയ ഓർഡർ\nമതി, കണക്ക് വേണ്ട\"", [
 ("A","wide","ജിതിനേ, കയർ പിരിക്കുന്ന റോബോട്ടിന് ഒരു സൊസൈറ്റിയിൽ നിന്ന് വലിയ ഓർഡർ വരും. അത് മതി, പ്രൊജക്ഷൻ എന്തിന്?"),
 ("V","V","ഐശ്വര്യേ, 'വരും' എന്നത് ഓർഡർ അല്ല. അത് വന്നില്ലെങ്കിൽ നമ്മൾ എവിടെ?"),
 ("A","A","പക്ഷേ ഇൻവെസ്റ്റർക്ക് വലിയ നമ്പറല്ലേ ഇഷ്ടം?"),
 ("V","wide","ഇൻവെസ്റ്റർ, ബാങ്ക്, ഗ്രാന്റ് പാനൽ, എല്ലാരും 3 വർഷത്തെ പ്രൊജക്ഷൻ ചോദിക്കും. ട്രാക്ഷനോട് ചേർന്ന നമ്പർ. വലുതാക്കിയാൽ വിശ്വാസം പോകും."),
 ("A","A","അപ്പോ ഇതുവരെ വിറ്റ ആറ് മെഷീനിൽ നിന്ന് തുടങ്ങാം."),
 ("V","wide","കയർ ഒറ്റ നാരിൽ പിരിയില്ല. ബിസിനസ് ഒറ്റ ഓർഡറിലും.")],
 "കയർ ഒറ്റ നാരിൽ\nപിരിയില്ല, ബിസിനസ്\nഒറ്റ ഓർഡറിലും", CTA_PROJECTION, theme="faq",
 cap_ml="ചകിരി കയർ പിരിക്കുന്ന റോബോട്ട് സ്റ്റാർട്ടപ്പ് ഒരു വലിയ ഓർഡറിന്റെ പ്രതീക്ഷയിൽ പ്രൊജക്ഷൻ വേണ്ടെന്ന് വെച്ചു. ഇൻവെസ്റ്റർ, ബാങ്ക്, ഗ്രാന്റ് പാനൽ എല്ലാരും ചോദിക്കും; നമ്പർ ഇതുവരെയുള്ള വിൽപ്പനയോട് ചേർന്നതാകണം. നിങ്ങളുടെ ബിസിനസ് ഒറ്റ കസ്റ്റമറിലാണോ?",
 cap_en="A coir-spinning robot startup skips projections because one big co-operative order is 'coming'. Investors, banks and grant panels all ask for 3-year projections tied to real traction, here six machines sold, not a hoped-for order. Does your business depend on one customer?",
 cap_mg="Chakiri kayar pirikkunna robot startup oru valiya order-inte prathheekshayil projection vendennu vechu. Investor, bank, grant panel ellaarum chodikkum; number ithuvareyulla vilppanayodu chernnathaakanam. Ningalude business otta customer-il aano?")

# new + d904: elephant-care products; "few customers, no projection"
duo("fp037", "early_revenue", "B", "shop", "ആനയ്ക്ക് ആയുർവേദ എണ്ണ.\n\"കസ്റ്റമർ കുറവ്,\nകണക്ക് വേണ്ട\"", [
 ("A","wide","സുരേഷേ, ആനകൾക്കുള്ള ആയുർവേദ എണ്ണയ്ക്ക് കസ്റ്റമർ കുറച്ച് ആന ഉടമകൾ മാത്രം. ഇതിന് എന്ത് പ്രൊജക്ഷൻ?"),
 ("V","V","ബിനൂ, കസ്റ്റമർ കുറവാണെങ്കിൽ കണക്ക് കൂടുതൽ എളുപ്പമാ. എത്ര ഉടമകൾ, ഒരാൾ മാസം എത്ര ടിൻ?"),
 ("A","A","ഉത്സവ സീസണിൽ കൂടും, കർക്കിടകത്തിൽ സുഖചികിത്സയ്ക്ക് വേറെയും."),
 ("V","wide","അതാ റെവന്യൂ ഡ്രൈവർ: കസ്റ്റമർ, ഓരോരുത്തരും വാങ്ങുന്ന അളവ്, വളർച്ച. ആദ്യ വർഷം മാസം തിരിച്ച് എഴുതിയാൽ സീസണും കാണാം."),
 ("A","A","ആന വലുതാ, കണക്ക് ചെറുത്."),
 ("V","wide","ആനയെ മെരുക്കാൻ തോട്ടി. ബിസിനസ് മെരുക്കാൻ കണക്ക്.")],
 "ആനയ്ക്ക് തോട്ടി,\nബിസിനസിന് കണക്ക്", CTA_FORECAST, theme="new",
 cap_ml="ആനകൾക്കുള്ള ആയുർവേദ എണ്ണ വിൽക്കുന്ന ബിസിനസിന് കസ്റ്റമർ കുറച്ച് പേർ മാത്രം. അപ്പോഴും പ്രൊജക്ഷൻ വേണം: എത്ര ഉടമകൾ, എത്ര ടിൻ, ഏത് മാസം; ആദ്യ വർഷം മാസം തിരിച്ച്. നിങ്ങളുടെ ബിസിനസിന് സീസൺ ഉണ്ടോ?",
 cap_en="A business selling ayurvedic oil for temple elephants has only a few elephant owners as customers, so why a projection? Few customers make the maths easier: how many owners, how many tins each, and which months, month by month for year one. Does your business have a season?",
 cap_mg="Aanakalkkulla ayurveda enna vilkkunna business-nu customer kurachu per maathram. Appozhum projection venam: ethra udamakal, ethra tin, ethu maasam; aadya varsham maasam thirichu. Ningalude business-nu season undo?")

# new + d904: pookkalam flower delivery; break-even written as a month
duo("fp038", "grant_application", "A", "busstop", "ഗ്രാന്റ് ഫോം:\n\"ബ്രേക്ക്-ഈവൻ എപ്പോൾ?\"\nപൂക്കാരൻ: \"ഓണത്തിന്\"", [
 ("A","wide","അഖിലേ, ഗ്രാന്റ് ഫോമിൽ ബ്രേക്ക്-ഈവൻ എപ്പോൾ എന്ന് ചോദിച്ചു. ഞാൻ എഴുതി: ഓണത്തിന്."),
 ("V","V","ജിബിനേ, ഏത് ഓണം? ആദ്യത്തെയോ മൂന്നാമത്തെയോ? പൂക്കളത്തിന് പൂ എത്തിക്കുന്ന നമുക്ക് ബാക്കി മാസം എന്താ?"),
 ("A","A","കല്യാണ സീസണിൽ കുറച്ച്, പിന്നെ വളരെ കുറവ്."),
 ("V","wide","അതാ എഴുതേണ്ടത്. മാസം തിരിച്ച് വിൽപ്പനയും ചെലവും, പിന്നെ വരുമാനം ചെലവിനെ കടക്കുന്ന മാസം. അതാ ബ്രേക്ക്-ഈവൻ."),
 ("A","A","അപ്പോ ഉത്തരം ഒരു ഉത്സവമല്ല, ഒരു മാസം."),
 ("V","wide","പൂക്കളം ഒരു ദിവസം. കണക്ക് പന്ത്രണ്ട് മാസം.")],
 "പൂക്കളം ഒരു ദിവസം,\nകണക്ക് പന്ത്രണ്ട് മാസം", CTA_PROJECTION, theme="new",
 cap_ml="പൂക്കളത്തിന് പൂ എത്തിക്കുന്ന സ്റ്റാർട്ടപ്പ് ഗ്രാന്റ് ഫോമിൽ ബ്രേക്ക്-ഈവൻ 'ഓണത്തിന്' എന്ന് എഴുതി. മാസം തിരിച്ചുള്ള വിൽപ്പനയും ചെലവും വെച്ച് വരുമാനം ചെലവിനെ കടക്കുന്ന മാസമാണ് ഉത്തരം. നിങ്ങളുടെ ബ്രേക്ക്-ഈവൻ ഏത് മാസം?",
 cap_en="A pookkalam flower-delivery startup wrote 'at Onam' as its break-even on a grant form. Grant panels want the month, from monthly sales and costs: the month revenue first covers costs. Which month is your break-even?",
 cap_mg="Pookkalathinu poo ethikkunna startup grant form-il break-even 'Onathinu' ennu ezhuthi. Maasam thirichulla vilppanayum chelavum vechu varumaanam chelavine kadakkunna maasamaanu utharam. Ningalude break-even ethu maasam?")
