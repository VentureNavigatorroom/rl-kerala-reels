# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_FP. Never mention our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

lst('fpt004', 'early_revenue', "B", 'ലാഭം ഉണ്ട്,\nകയ്യിൽ പണം ഇല്ല?\nരണ്ട് ഷീറ്റ് നോക്കൂ', [('ലാഭനഷ്ട കണക്ക്', 'കടലാസിൽ എത്ര സമ്പാദിച്ചു, എത്ര ചെലവായി.'), ('ക്യാഷ് ഫ്ലോ', 'പണം ശരിക്കും എന്ന് കയ്യിൽ വരും, എന്ന് പോകും.'), ('ട്രിക്ക്', 'രണ്ടും മാസം തോറും ഒരുമിച്ച് നോക്കൂ.')],
 'ലാഭവും പണവും\nരണ്ടാണ്', CTA_FORECAST, theme="tip",
 cap_ml='ലാഭനഷ്ട കണക്കിൽ ലാഭം കാണിച്ചാലും ക്യാഷ് ഫ്ലോയിൽ പണം തീരാം. ഫിനാൻഷ്യൽ പ്രൊജക്ഷനിൽ രണ്ട് ഷീറ്റും മാസം തോറും വേണം. നിങ്ങൾ ഏതാണ് നോക്കുന്നത്: ലാഭമോ ക്യാഷോ?',
 cap_en='A profit and loss sheet can show profit while the cash flow runs dry. A financial projection needs both, month by month. Which one do you track: profit or cash?',
 cap_mg='P&L-il laabham kaanichaalum cash flow-il paisa theeraam. Financial projection-il randu sheet-um maasam thorum venam. Ningal ethaanu nokkunnathu: laabhamo cash-o?')

lst('fpt005', 'early_revenue', "B", 'പുതിയ ആളെ\nഎടുക്കും മുമ്പ്\nഷീറ്റിൽ 3 വരി', [('എന്ന് ജോയിൻ ചെയ്യും', 'ഏത് മാസം മുതൽ ശമ്പളം തുടങ്ങും.'), ('മാസ ചെലവ്', 'ശമ്പളം ചെലവ് കോളത്തിൽ ചേർക്കൂ.'), ('എന്ത് കൊണ്ടുവരും', 'ആ ആൾ കൊണ്ടുള്ള വരുമാന വളർച്ച എഴുതൂ.')],
 'ടീം വളർന്നാൽ\nചെലവും വളരും', CTA_PROJECTION, theme="tip",
 cap_ml='ഹയറിംഗ് പ്ലാൻ ഇല്ലാത്ത പ്രൊജക്ഷൻ പകുതി കണക്കാണ്. ഓരോ പുതിയ ആളും ഏത് മാസം ജോയിൻ ചെയ്യും, ശമ്പളം എത്ര, എന്ത് വളർച്ച കൊണ്ടുവരും എന്ന് എഴുതൂ. അടുത്ത വർഷം നിങ്ങൾ എത്ര പേരെ എടുക്കും?',
 cap_en='A projection without a hiring plan is half a forecast. For every new hire, write the joining month, the monthly salary cost and the growth they bring. How many people will you hire next year?',
 cap_mg='Hiring plan illaatha projection pakuthi kanakkaanu. Oro puthiya aalum ethu maasam join cheyyum, salary ethra, enthu valarcha kondu varum ennu ezhuthu. Adutha varsham ethra perey edukkum?')

lst('fpt006', 'investor_pitch', "B", 'നിങ്ങളുടെ നമ്പർ\nവിശ്വസിക്കാമോ?\n3 ചെക്ക്', [('തുടക്കം', 'ഇന്നത്തെ വിൽപ്പനയിൽ നിന്നാണോ ഗ്രാഫ് തുടങ്ങുന്നത്?'), ('വളർച്ച', 'അതിന് വേണ്ട ആളും പണവും ചെലവ് ഷീറ്റിൽ ഉണ്ടോ?'), ('വലിയ നമ്പർ', 'കാരണമില്ലാത്ത വലിയ നമ്പർ വിശ്വാസം കളയും.')],
 'വിശ്വാസമാണ്\nആദ്യ നിക്ഷേപം', CTA_PROJECTION, theme="tip",
 cap_ml='ഇൻവെസ്റ്റർ പ്രൊജക്ഷനിൽ നോക്കുന്നത് വലിപ്പമല്ല, വിശ്വാസ്യതയാണ്. ഇന്നത്തെ ട്രാക്ഷനിൽ നിന്ന് തുടങ്ങൂ, വളർച്ചയ്ക്ക് വേണ്ട ചെലവും ചേർക്കൂ. നിങ്ങളുടെ ഗ്രാഫ് എവിടെ നിന്നാണ് തുടങ്ങുന്നത്?',
 cap_en='Investors judge projections on credibility, not size. Start from your real traction today and add the costs your growth needs; inflated numbers lose trust. Where does your graph start?',
 cap_mg='Investor projection-il nokkunnathu valuppamalla, vishwaasyathayaanu. Innathe traction-il ninnu thudangu, valarchakku venda chelavum cherkku. Ningalude graph evide ninnaanu thudangunnathu?')

lst('fpt007', 'bank_loan', "B", 'ബാങ്ക് ചോദിച്ചു:\n"പ്രോജക്റ്റ്\nറിപ്പോർട്ട്?"', [('എന്താണ്', 'ലോണിന് വേണ്ടി നമ്പറുകളോടെയുള്ള ബിസിനസ് പ്ലാൻ.'), ('ഉള്ളിൽ', 'ലോൺ എന്തിന്, തിരിച്ചടവ് ഏത് ക്യാഷ് ഫ്ലോയിൽ നിന്ന്.'), ('ട്രിക്ക്', 'നിങ്ങളുടെ പ്രൊജക്ഷനിലെ അതേ നമ്പറുകൾ ഉപയോഗിക്കൂ.')],
 'ഒരു കണക്ക്,\nരണ്ട് ഉപയോഗം', CTA_FORECAST, theme="tip",
 cap_ml='ബിസിനസ് ലോണിന് ബാങ്കുകൾ പ്രോജക്റ്റ് റിപ്പോർട്ട് ചോദിക്കാം. ലോൺ എന്തിന്, തിരിച്ചടവ് ഏത് ക്യാഷ് ഫ്ലോയിൽ നിന്ന് എന്ന് അതിൽ കാണിക്കണം. ലോണിന് അപേക്ഷിക്കാൻ പ്ലാൻ ഉണ്ടോ?',
 cap_en='Banks may ask for a project report for a business loan: what the loan is for and which cash flow repays it. Use the same numbers as your financial projection. Planning a loan?',
 cap_mg='Business loan-nu bank project report chodikkaam. Loan enthinu, thirichadavu ethu cash flow-il ninnu ennu athil kaanikkanam. Loan-nu apekshikkaan plan undo?')

lst('fpt008', 'pre_revenue', "B", 'കയ്യിലെ പണം\nഎത്ര മാസം തികയും?\nഒരു ചെക്ക്', [('ഇന്ന്', 'ബാങ്കിൽ ഇപ്പോൾ ഉള്ള പണം.'), ('മാസ വിടവ്', 'ക്യാഷ് ഫ്ലോയിൽ: മാസം പോകുന്നത് മൈനസ് വരുന്നത്.'), ('ഹരിക്കൂ', 'ആദ്യത്തേതിനെ രണ്ടാമത്തേത് കൊണ്ട്: ബാക്കി മാസങ്ങൾ.')],
 'പണം തീരും മുമ്പ്\nഅറിയണം', CTA_FORECAST, theme="tip",
 cap_ml='ക്യാഷ് ഫ്ലോ പ്രൊജക്ഷൻ ഒരു ചോദ്യത്തിന് ഉത്തരം തരും: കയ്യിലെ പണം എത്ര മാസം തികയും? ഇന്നത്തെ പണം, മാസം പോകുന്നതും വരുന്നതും തമ്മിലുള്ള വ്യത്യാസം കൊണ്ട് ഹരിക്കൂ. നിങ്ങൾക്ക് എത്ര മാസം ബാക്കി?',
 cap_en='Your cash flow projection answers one question: how many months will your cash last? Divide the cash in the bank by the monthly gap between money going out and coming in. How many months do you have?',
 cap_mg='Cash flow projection oru chodyathinu utharam tharum: kayyile paisa ethra maasam thikayum? Innathe paisa, maasam pokunnathum varunnathum thammilulla vyathyaasam kondu harikku. Ningalkku ethra maasam baakki?')

lst('fpt009', 'grant_application', "B", 'ഇൻവെസ്റ്റർ, ബാങ്ക്,\nഗ്രാന്റ് പാനൽ:\nആര് എന്ത് നോക്കും', [('ഇൻവെസ്റ്റർ', 'ട്രാക്ഷനോട് ചേർന്ന വളർച്ച.'), ('ബാങ്ക്', 'തിരിച്ചടവിനുള്ള ക്യാഷ് ഫ്ലോ, ചിലപ്പോൾ പ്രോജക്റ്റ് റിപ്പോർട്ട്.'), ('ഗ്രാന്റ് പാനൽ', 'യാഥാർത്ഥ്യമുള്ള നമ്പറും ബ്രേക്ക്-ഈവനും.')],
 'ഒരേ കണക്ക്,\nമൂന്ന് കണ്ണട', CTA_PROJECTION, theme="tip",
 cap_ml='ഇൻവെസ്റ്ററും ബാങ്കും ഗ്രാന്റ് പാനലും ഫിനാൻഷ്യൽ പ്രൊജക്ഷൻ ചോദിക്കും, പക്ഷേ ഓരോരുത്തരും ആദ്യം നോക്കുന്നത് വേറെയാണ്. ഒരേ സത്യസന്ധമായ കണക്ക്, ഓരോരുത്തർക്കും വേണ്ട ഭാഗം മുന്നിൽ. നിങ്ങൾ ആർക്കാണ് അയക്കുന്നത്?',
 cap_en='Investors, banks and grant panels all ask for projections, but each looks first at something different: growth tied to traction, cash flow for repayment, realistic numbers and break-even. Who are you sending yours to?',
 cap_mg='Investor-um bank-um grant panel-um financial projection chodikkum, pakshe oro aalum aadyam nokkunnathu vereyaanu. Ore kanakku, oro aalkkum venda bhaagam munnil. Ningal aarkkaanu ayakkunnathu?')

lst('fpt010', 'investor_pitch', "B", 'ബ്രേക്ക്-ഈവൻ\nമാസം കണ്ടുപിടിക്കാൻ\n3 സ്റ്റെപ്പ്', [('വരുമാന വരി', 'ഓരോ മാസത്തെയും പ്രതീക്ഷിക്കുന്ന വരുമാനം.'), ('ചെലവ് വരി', 'ശമ്പളം, വാടക, നടത്തിപ്പ്: ഓരോ മാസവും.'), ('കണ്ടുപിടിക്കൂ', 'വരുമാനം ചെലവിനെ കടക്കുന്ന ആദ്യ മാസം.')],
 'ആ മാസമാണ്\nഎല്ലാവരും ചോദിക്കുന്നത്', CTA_FORECAST, theme="tip",
 cap_ml='ബ്രേക്ക്-ഈവൻ കണ്ടുപിടിക്കാൻ: മാസ വരുമാനവും മാസ ചെലവും ഒരേ ഷീറ്റിൽ, വരുമാനം ചെലവിനെ കടക്കുന്ന ആദ്യ മാസം. ഇൻവെസ്റ്ററും ബാങ്കും ഇത് ചോദിക്കും. നിങ്ങളുടെ ബ്രേക്ക്-ഈവൻ എത്ര മാസം അകലെ?',
 cap_en='Find your break-even month: monthly revenue and monthly costs on one sheet, then the first month revenue beats costs. Investors and banks will ask. How many months away is yours?',
 cap_mg='Break-even kandupidikkaan: maasa varumaanavum maasa chelavum ore sheet-il, varumaanam chelavine kadakkunna aadya maasam. Investor-um bank-um ithu chodikkum. Ningalude break-even ethra maasam akale?')
