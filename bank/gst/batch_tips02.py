# Tips and tricks 02 (20 Nov): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_GST.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

lst('gt004', 'trader', "B", 'വിൽപ്പന ഇല്ലാത്ത\nമാസം: റിട്ടേൺ\nവേണ്ടേ?', [('നിൽ റിട്ടേൺ', 'വിൽപ്പന ഇല്ലെങ്കിലും റിട്ടേൺ ഫയൽ ചെയ്യണം.'), ('വൈകിയാൽ', 'നിൽ റിട്ടേണിന് ദിവസം ഇരുപത് രൂപ ലേറ്റ് ഫീ.'), ('പരമാവധി', 'നിൽ റിട്ടേണിന് 500 രൂപ വരെ.')],
 'ഒന്നും വിറ്റില്ലെങ്കിലും\nഫയൽ ചെയ്യൂ', CTA_PENALTY, theme="tip",
 cap_ml='GST രജിസ്ട്രേഷൻ ഉണ്ടെങ്കിൽ വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ ഫയൽ ചെയ്യണം. വൈകിയാൽ ദിവസം 20 രൂപ ലേറ്റ് ഫീ, പരമാവധി 500 രൂപ. നിങ്ങൾ നിൽ റിട്ടേൺ മുടക്കിയിട്ടുണ്ടോ?',
 cap_en='With a GST registration you must file a nil return even in a month with no sales. Filing late costs 20 rupees a day, up to 500 rupees for a nil return. Have you ever skipped one?',
 cap_mg='GST registration undenkil vilppana illaatha maasavum nil return file cheyyanam. Vaikiyaal divasam 20 rupees late fee, maximum 500. Ningal nil return mudakkiyittundo?')

lst('gt005', 'nri_business', "B", 'GST അപേക്ഷയ്ക്ക്\nമുമ്പ് ഈ രേഖകൾ\nഒരുക്കൂ', [('നിങ്ങളുടേത്', 'PAN, ആധാർ, ഫോട്ടോ. ആധാറിലെ മൊബൈലിൽ OTP വരും.'), ('കടയുടേത്', 'വാടകയെങ്കിൽ കരാർ, ഉടമയുടെ NOC, കറന്റ് ബിൽ.'), ('ബാങ്ക്', 'ക്യാൻസൽ ചെയ്ത ചെക്ക്, പാസ്ബുക്ക് അല്ലെങ്കിൽ സ്റ്റേറ്റ്മെന്റ്.')],
 'ഗൾഫിലാണെങ്കിൽ\nOTP ഫോൺ കൈയിൽ വേണം', CTA_GST, theme="tip",
 cap_ml='പ്രൊപ്രൈറ്റർ GST രജിസ്ട്രേഷന്: PAN, ആധാർ, ഫോട്ടോ, കടയുടെ അഡ്രസ്സ് പ്രൂഫ്, ബാങ്ക് പ്രൂഫ്. ആധാറുമായി ബന്ധിപ്പിച്ച മൊബൈലിൽ OTP വരും, ഗൾഫിലാണെങ്കിൽ ആ നമ്പർ കൈയിലുണ്ടോ എന്ന് നോക്കൂ. ഏത് രേഖയാണ് ബാക്കി?',
 cap_en="Documents for a proprietor's GST registration: PAN, Aadhaar, photo, shop address proof and bank proof. The OTP goes to the mobile linked to Aadhaar, so check you can receive it if you live in the Gulf. Which document is missing?",
 cap_mg='Proprietor GST registration-nu: PAN, Aadhaar, photo, kadayude address proof, bank proof. Aadhaar linked mobile-il OTP varum. Gulf-il aanel aa number kaiyil undo? Ethu rekha baakki?')

lst('gt006', 'trader', "B", 'ലിമിറ്റ് കടന്നിട്ടും\nരജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ?', [('ടാക്സ്', 'അടയ്ക്കേണ്ട നികുതി മുഴുവൻ അടയ്ക്കണം.'), ('പലിശ', 'അതിന് പതിനെട്ട് ശതമാനം പലിശ.'), ('പിഴ', 'പതിനായിരം രൂപ, അല്ലെങ്കിൽ നികുതിയുടെ പത്ത് ശതമാനം. ഏതാണോ കൂടുതൽ.')],
 'വൈകിയാൽ മൂന്ന് ബിൽ\nഒരുമിച്ച്', CTA_PENALTY, theme="tip",
 cap_ml='GST ലിമിറ്റ് കടന്നിട്ടും രജിസ്റ്റർ ചെയ്തില്ലെങ്കിൽ: നികുതി, 18% പലിശ, പിന്നെ 10,000 രൂപ അല്ലെങ്കിൽ നികുതിയുടെ 10% പിഴ, ഏതാണോ കൂടുതൽ. നിങ്ങളുടെ ടേൺഓവർ അവസാനം നോക്കിയത് എപ്പോൾ?',
 cap_en='Crossed the GST limit without registering? You pay the tax, 18% interest, and a penalty of 10,000 rupees or 10% of the tax, whichever is higher. When did you last check your turnover?',
 cap_mg='GST limit kadannittum register cheythillenkil: tax, 18% interest, pinne 10,000 allenkil tax-nte 10% penalty, ethaano kooduthal. Ningal turnover avasaanam nokkiyathu eppol?')

lst('gt007', 'new_company', "B", 'GST അപ്രൂവൽ:\nഎത്ര ദിവസം?\nമൂന്ന് ഉത്തരം', [('മൂന്ന് പ്രവൃത്തി ദിവസം', 'റിസ്ക് കുറഞ്ഞ അപേക്ഷകൾക്ക് ഓട്ടോ അപ്രൂവൽ.'), ('ഏഴ് പ്രവൃത്തി ദിവസം', 'മറ്റ് അപേക്ഷകൾക്ക് സാധാരണ സമയം.'), ('മുപ്പത് ദിവസം വരെ', 'നേരിട്ടുള്ള പരിശോധന വേണ്ടി വന്നാൽ.')],
 'ഓർഡറിന് മുമ്പ്\nഅപേക്ഷിക്കൂ', CTA_GST, theme="tip",
 cap_ml='2025 നവംബർ മുതൽ റിസ്ക് കുറഞ്ഞ GST അപേക്ഷകൾ 3 പ്രവൃത്തി ദിവസത്തിൽ ഓട്ടോ അപ്രൂവ് ആകും. മറ്റുള്ളവയ്ക്ക് 7 പ്രവൃത്തി ദിവസം, പരിശോധന വേണമെങ്കിൽ 30 ദിവസം വരെ. നിങ്ങളുടേതിന് എത്ര ദിവസം എടുത്തു?',
 cap_en='Since November 2025, low-risk GST applications are auto-approved within 3 working days. Others take 7 working days, or up to 30 days if physical verification is needed. How long did yours take?',
 cap_mg='November 2025 muthal risk kuranja GST application 3 working days-il auto approve aakum. Mattullavakku 7 working days, verification venel 30 divasam vare. Ningaludethinu ethra divasam eduthu?')

lst('gt008', 'service_pro', "B", 'ലിമിറ്റിന് താഴെ.\nഎന്നിട്ടും GST\nഎടുക്കണോ?', [('ആർക്കും', 'ടേൺഓവർ കുറവാണെങ്കിലും സ്വമേധയാ രജിസ്റ്റർ ചെയ്യാം.'), ('ക്ലയന്റ്', 'വലിയ കമ്പനികൾ പലപ്പോഴും GSTIN ചോദിക്കും.'), ('ക്രെഡിറ്റ്', 'ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം.')],
 'ലിമിറ്റ് ഒരു കാരണം\nക്ലയന്റ് മറ്റൊന്ന്', CTA_LIMIT, theme="tip",
 cap_ml='ലിമിറ്റിന് താഴെയാണെങ്കിലും ആർക്കും സ്വമേധയാ GST രജിസ്റ്റർ ചെയ്യാം. കമ്പനി ക്ലയന്റുകൾ GSTIN ചോദിക്കാറുണ്ട്, ഇൻപുട്ട് ടാക്സ് ക്രെഡിറ്റ് രജിസ്റ്റർ ചെയ്തവർക്ക് മാത്രം. നിങ്ങളുടെ ക്ലയന്റ് GSTIN ചോദിച്ചിട്ടുണ്ടോ?',
 cap_en='Anyone can register for GST voluntarily, even below the limit. Company clients often ask for a GSTIN, and only registered businesses get input tax credit. Has a client asked for yours?',
 cap_mg='Limit-nu thaazhe aanelum aarkkum voluntary aayi GST register cheyyaam. Company clients GSTIN chodikkum, input tax credit register cheythavarkku maathram. Ningalude client GSTIN chodicho?')

lst('gt009', 'online_seller', "B", 'GSTR-3B വൈകി:\nഓരോ ദിവസവും\nകണക്ക് കൂടും', [('സാധാരണ റിട്ടേൺ', 'ദിവസം അമ്പത് രൂപ ലേറ്റ് ഫീ.'), ('പരമാവധി', 'ഒന്നര കോടി വരെ ടേൺഓവറിന് 2,000 രൂപ.'), ('ട്രിക്ക്', 'ഓരോ മാസവും ഫയലിംഗ് തീയതി ഫോണിൽ റിമൈൻഡറാക്കൂ.')],
 'ഒരു റിമൈൻഡർ\nദിവസവും ലാഭം', CTA_PENALTY, theme="tip",
 cap_ml='GSTR-3B വൈകിയാൽ ദിവസം 50 രൂപ ലേറ്റ് ഫീ. 1.5 കോടി വരെ ടേൺഓവറുള്ളവർക്ക് പരമാവധി 2,000 രൂപ. ഫയലിംഗ് തീയതി ഫോണിൽ റിമൈൻഡർ വെച്ചിട്ടുണ്ടോ?',
 cap_en='A late GSTR-3B costs 50 rupees a day in late fees, capped at 2,000 rupees for turnover up to 1.5 crore. Is the filing date in your phone reminders?',
 cap_mg='GSTR-3B vaikiyaal divasam 50 rupees late fee. 1.5 kodi vare turnover-nu maximum 2,000. Filing date phone-il reminder vechittundo?')

lst('gt010', 'service_pro', "B", 'കേരളത്തിന് പുറത്ത്\nജോലി: GST എപ്പോൾ?', [('സർവീസ് പുറത്തേക്ക്', 'ഇരുപത് ലക്ഷം വരെ ഒഴിവ് തുടരും.'), ('സാധനം പുറത്തേക്ക്', 'ആദ്യ വിൽപ്പന മുതൽ GST വേണം.'), ('മറ്റ് സംസ്ഥാനത്ത് താൽക്കാലിക സ്റ്റാൾ', 'കാഷ്വൽ ടാക്സബിൾ വ്യക്തി: ടേൺഓവർ നോക്കാതെ GST.')],
 'സർവീസും സാധനവും\nഒരുപോലെയല്ല', CTA_LIMIT, theme="tip",
 cap_ml='മറ്റ് സംസ്ഥാനങ്ങളിലേക്കുള്ള സർവീസിന് 20 ലക്ഷം വരെ GST ഒഴിവുണ്ട്. പക്ഷേ സാധനം മറ്റ് സംസ്ഥാനത്തേക്ക് വിറ്റാൽ ആദ്യ വിൽപ്പന മുതൽ GST വേണം. താൽക്കാലിക സ്റ്റാളിന് കാഷ്വൽ രജിസ്ട്രേഷനും. നിങ്ങൾ വിൽക്കുന്നത് സർവീസോ സാധനമോ?',
 cap_en='Services to other states stay exempt up to 20 lakh. Goods sold to another state need GST from the first sale, and a temporary stall in another state needs casual registration whatever the turnover. Do you sell services or goods?',
 cap_mg='Other state-ilekku service-nu 20 lakh vare GST ozhivu. Pakshe sadhanam other state-il vittaal aadya vilppana muthal GST. Temporary stall-nu casual registration. Ningal vilkkunnathu service-o sadhanamo?')
