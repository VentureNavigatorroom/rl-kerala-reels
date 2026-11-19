# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_UD.
# Never a fee; never promise a loan, subsidy or recovery.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_UDYAM, CTA_MSME = topics.CTA_UDYAM, topics.CTA_MSME

lst('yt004', 'supplier_unpaid', "B", 'വിളിച്ചിട്ടും\nപണം വരുന്നില്ല.\nഅടുത്ത പടി?', [('പരാതി', 'MSME സമാധാൻ പോർട്ടലിൽ നൽകാം.'), ('ആര് കേൾക്കും', 'MSME ഫെസിലിറ്റേഷൻ കൗൺസിൽ.'), ('ആർക്ക്', 'ഉദ്യം ഉള്ള മാനുഫാക്ചറിംഗ്, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക്.')],
 'ഫോൺ വിളി മാത്രമല്ല\nവഴി', CTA_UDYAM, theme="tip",
 cap_ml='വലിയ ബയർ പണം വൈകിച്ചാൽ ഉദ്യം ഉള്ള മാനുഫാക്ചറിംഗ്, സർവീസ് മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾക്ക് MSME സമാധാൻ പോർട്ടലിൽ പരാതി നൽകാം. ഫെസിലിറ്റേഷൻ കൗൺസിൽ ആണ് കേൾക്കുന്നത്. നിങ്ങൾക്ക് പണം വൈകിയിട്ടുണ്ടോ?',
 cap_en='If a big buyer delays payment, a manufacturing or service micro or small unit with Udyam can file a complaint on the MSME Samadhaan portal; the facilitation council hears it. Has a buyer ever paid you late?',
 cap_mg='Valiya buyer panam vaikichaal Udyam ulla manufacturing, service micro, small unit-ukalkku MSME Samadhaan portal-il complaint kodukkaam. Facilitation council aanu kelkkunnathu. Ningalkku panam vaikiyittundo?')

lst('yt005', 'service_unit', "B", 'ബയർമാർക്ക് ഒരു\nടാക്സ് ടിപ്പ്:\nവൈകിയാൽ നഷ്ടം', [('ആർക്ക് പണം', 'ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സപ്ലയർക്ക്.'), ('എപ്പോൾ വരെ', 'സമ്മതിച്ച സമയം, പരമാവധി നാല്പത്തിയഞ്ച് ദിവസം.'), ('വൈകിയാൽ', 'പണം കൊടുക്കും വരെ ഇൻകം ടാക്സ് ഡിഡക്ഷൻ കിട്ടില്ല.')],
 'സപ്ലയറുടെ ഉദ്യം\nബയറുടെ ടാക്സ്', CTA_MSME, theme="tip",
 cap_ml='ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ സപ്ലയർക്ക് സമ്മതിച്ച സമയത്ത്, പരമാവധി 45 ദിവസത്തിനുള്ളിൽ, പണം കൊടുത്തില്ലെങ്കിൽ ബയർക്ക് സെക്ഷൻ 43B(h) പ്രകാരം പണം കൊടുക്കും വരെ ടാക്സ് ഡിഡക്ഷൻ കിട്ടില്ല. അതുകൊണ്ടാണ് വലിയ കമ്പനികൾ ഉദ്യം ചോദിക്കുന്നത്. നിങ്ങളോട് ചോദിച്ചിട്ടുണ്ടോ?',
 cap_en='If a buyer does not pay an Udyam-registered micro or small supplier within the agreed time (at most 45 days), section 43B(h) denies the buyer the income-tax deduction until payment. That is why big companies ask whether you are MSME-registered. Has a client asked you?',
 cap_mg='Udyam ulla micro, small supplier-nu 45 divasathinullil panam koduthillenkil buyer-nu 43B(h) prakaaram payment vare tax deduction kittilla. Athukondaanu valiya company-kal Udyam chodikkunnathu. Ningalodu chodichittundo?')

lst('yt006', 'trader_ud', "B", 'ഉദ്യം രജിസ്ട്രേഷൻ:\nഎങ്ങനെ? 3 വാക്കിൽ', [('ഓൺലൈൻ', 'സർക്കാരിന്റെ ഉദ്യം പോർട്ടലിൽ.'), ('ആധാർ അടിസ്ഥാനം', 'ഒപ്പം PAN, ഉണ്ടെങ്കിൽ GSTIN.'), ('സ്വയം പ്രഖ്യാപനം', 'നൽകുന്ന വിവരങ്ങൾ നിങ്ങൾ തന്നെ ഉറപ്പ് പറയുന്നു.')],
 'വിവരം ശരിയായാൽ\nരജിസ്ട്രേഷൻ എളുപ്പം', CTA_UDYAM, theme="tip",
 cap_ml='ഉദ്യം രജിസ്ട്രേഷൻ ഓൺലൈനാണ്: ആധാർ അടിസ്ഥാനമാക്കി, PAN-ഉം ഉണ്ടെങ്കിൽ GSTIN-ഉം വെച്ച്, സ്വയം പ്രഖ്യാപനത്തോടെ. നൽകുന്ന വിവരങ്ങൾ ശരിയാണെന്ന് ഉറപ്പാക്കൂ. നിങ്ങൾക്ക് ഉദ്യം ഉണ്ടോ?',
 cap_en='Udyam registration is online and Aadhaar-based, with your PAN and GSTIN if you have one, on a self-declaration. Make sure every detail you enter is correct. Do you have Udyam yet?',
 cap_mg='Udyam registration online aanu: Aadhaar adisthaanam, PAN-um undenkil GSTIN-um, self-declaration. Kodukkunna details sheriyaanennu urappaakku. Ningalkku Udyam undo?')

lst('yt007', 'manufacturer', "B", 'ഉദ്യം പുതുക്കണോ?\nവേണ്ട. പക്ഷേ\nഇത് മറക്കരുത്', [('പുതുക്കൽ', 'ഇല്ല. ഒരിക്കൽ എടുത്താൽ മതി.'), ('അപ്ഡേറ്റ്', 'വിലാസം, നിക്ഷേപം, ടേൺഓവർ, GSTIN മാറിയാൽ.'), ('ട്രിക്ക്', 'വർഷത്തിൽ ഒരിക്കൽ ഡീറ്റെയിൽസ് തുറന്ന് നോക്കൂ.')],
 'ഒരിക്കൽ എടുത്തു,\nഎന്നും ശരിയാക്കി വെക്കൂ', CTA_MSME, theme="tip",
 cap_ml='ഉദ്യം രജിസ്ട്രേഷന് പുതുക്കൽ ഇല്ല. പക്ഷേ വിലാസം, നിക്ഷേപം, ടേൺഓവർ, GSTIN മാറിയാൽ വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്യണം. അവസാനം എപ്പോഴാണ് നിങ്ങൾ നോക്കിയത്?',
 cap_en='Udyam has no renewal, but you must update it when your address, investment, turnover or GSTIN changes. When did you last check yours?',
 cap_mg='Udyam-nu renewal illa. Pakshe address, nikshepam, turnover, GSTIN maariyaal details update cheyyanam. Avasaanam eppozhaanu ningal nokkiyathu?')

lst('yt008', 'loan_seeker', "B", 'ഉദ്യം തുറക്കുന്ന\n3 വാതിലുകൾ', [('വായ്പ', 'മുൻഗണനാ വിഭാഗത്തിൽ അപേക്ഷിക്കാം.'), ('ഈടില്ലാ സ്കീം', 'CGTMSE പോലുള്ള സ്കീമുകൾ നോക്കാം.'), ('ടെൻഡർ', 'സർക്കാർ ടെൻഡറുകളിൽ മുൻഗണനകൾ.')],
 'വാതിൽ തുറക്കും,\nതീരുമാനം ബാങ്കിന്', CTA_UDYAM, theme="tip",
 cap_ml='ഉദ്യം രജിസ്ട്രേഷൻ മുൻഗണനാ വായ്പ, CGTMSE പോലുള്ള ഈടില്ലാത്ത ലോൺ സ്കീമുകൾ, സർക്കാർ ടെൻഡർ മുൻഗണനകൾ എന്നിവയ്ക്ക് സഹായിക്കും. ലോൺ ഉറപ്പല്ല, തീരുമാനം ബാങ്കിന്റേതാണ്. നിങ്ങൾക്ക് ഏത് വാതിലാണ് വേണ്ടത്?',
 cap_en='Udyam helps with priority sector lending, collateral-free loan schemes such as CGTMSE, and preferences in government tenders. It does not guarantee a loan; the bank decides. Which door do you need?',
 cap_mg='Udyam priority lending, CGTMSE pole ulla collateral-free loan scheme, sarkaar tender munganana ennivaykku sahaayikkum. Loan urappalla, theerumaanam bank-intethaanu. Ningalkku ethu vaathil venam?')

lst('yt009', 'supplier_unpaid', "B", 'ഓരോ ബില്ലിനും\nഒരു കലണ്ടർ ട്രിക്ക്', [('ബിൽ ദിവസം', 'ഇൻവോയ്സ് തീയതി കലണ്ടറിൽ ഇടൂ.'), ('സമ്മതിച്ച ദിവസം', 'പരമാവധി നാല്പത്തിയഞ്ച്; കരാറില്ലെങ്കിൽ പതിനഞ്ച്.'), ('അത് കഴിഞ്ഞാൽ', 'കൂട്ടുപലിശ ഓർമ്മിപ്പിച്ച് മെയിൽ അയക്കൂ.')],
 'തീയതി ഓർത്താൽ\nപണം ഓർക്കും', CTA_UDYAM, theme="tip",
 cap_ml='ഉദ്യം ഉള്ള മൈക്രോ, സ്മോൾ യൂണിറ്റുകൾ ഓരോ ഇൻവോയ്സ് തീയതിയും കലണ്ടറിൽ ഇടൂ. കരാറില്ലെങ്കിൽ 15 ദിവസം, ഉണ്ടെങ്കിൽ പരമാവധി 45 ദിവസം. അത് കഴിഞ്ഞാൽ കൂട്ടുപലിശയുടെ കാര്യം ബയറെ ഓർമ്മിപ്പിക്കൂ. നിങ്ങൾ ബില്ലുകൾ ട്രാക്ക് ചെയ്യുന്നുണ്ടോ?',
 cap_en='Micro and small units with Udyam: put every invoice date in your calendar. Without an agreement the buyer has 15 days; with one, at most 45. After that, remind the buyer in writing that compound interest applies. Do you track your bills?',
 cap_mg='Udyam ulla micro, small unit-ukal oro invoice date-um calendar-il idu. Karaar illenkil 15 divasam, undenkil paramaavadhi 45. Athu kazhinjaal koottupalisha karyam buyer-ne ormippikku. Ningal bill track cheyyunnundo?')

lst('yt010', 'service_unit', "B", 'GST ഇല്ല.\nഉദ്യം കിട്ടുമോ?\nഒരു ഉത്തരം', [('GSTIN ഇല്ലെങ്കിൽ', 'ആധാറും PAN-ഉം വെച്ച് രജിസ്റ്റർ ചെയ്യാം.'), ('GSTIN ഉണ്ടെങ്കിൽ', 'അതും നൽകണം.'), ('പിന്നീട് GST എടുത്താൽ', 'ഉദ്യമിലെ വിവരങ്ങൾ അപ്ഡേറ്റ് ചെയ്യൂ.')],
 'GST ഇല്ലെങ്കിലും\nഉദ്യം വഴി തുറന്ന്', CTA_MSME, theme="tip",
 cap_ml='GST രജിസ്ട്രേഷൻ ഇല്ലാത്ത ചെറിയ സർവീസ് യൂണിറ്റിനും ആധാറും PAN-ഉം വെച്ച് ഉദ്യം എടുക്കാം. GSTIN ഉള്ളവർ അതും നൽകണം; പിന്നീട് GST എടുത്താൽ ഉദ്യം അപ്ഡേറ്റ് ചെയ്യൂ. നിങ്ങൾക്ക് GST ഉണ്ടോ?',
 cap_en='A small service unit without GST can still register on Udyam with Aadhaar and PAN. If you have a GSTIN, add it; if you register for GST later, update your Udyam details. Do you have GST?',
 cap_mg='GST illaatha cheriya service unit-num Aadhaar-um PAN-um vechu Udyam edukkaam. GSTIN ullavar athum kodukkanam; pinneedu GST eduthaal Udyam update cheyyu. Ningalkku GST undo?')
