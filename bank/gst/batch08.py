# GST batch 08 (28 Nov night): more "fix-it" reels (HANDOVER 5b) with angles gd045-046 did not use: a missing owner's NOC,
# bank proof without a cheque book, a board photo as address proof, a clarification (not a document), working days, what REG-05
# means; plus the penalty minimum, late-fee caps per return, PAN enrolment after the limit, the services composition limit.
# Facts only from topics.FACTS_GST. Never promise approval. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

# crm (STORY 8) + fix-it: a bakery's GST query asks for the building owner's NOC; the owner lives in Qatar
duo("gd047", "trader", "B", "airport", "GST ഓഫീസറുടെ ചോദ്യം:\n\"ഉടമയുടെ NOC?\"\nഉടമ ഖത്തറിൽ", [
 ("A","wide","റഫീഖ്ക്കാ, ഹോട്ടൽ ഓർഡറിന് വേണ്ടി ബേക്കറിക്ക് GST അപേക്ഷിച്ചു. REG-03 വന്നു: കെട്ടിട ഉടമയുടെ NOC ഇല്ലെന്ന്. ഉടമ ഖത്തറിലാ!"),
 ("V","V","ഷമീറേ, വാടക സ്ഥലത്തിന് കരാർ മാത്രം പോരാ. ഉടമയുടെ NOC-യും ഒരു ബില്ലും വേണം."),
 ("A","A","എത്ര ദിവസം ഉണ്ട് മറുപടിക്ക്?"),
 ("V","V","REG-04-ൽ, 7 പ്രവൃത്തി ദിവസത്തിനകം. മറുപടി ഇല്ലെങ്കിൽ ഓഫീസർക്ക് REG-05-ൽ റിജക്ട് ചെയ്യാം."),
 ("A","A","എങ്കിൽ ഇന്ന് രാത്രി തന്നെ ഖത്തറിലേക്ക് വിളിക്കാം."),
 ("V","wide","ഉടമ ദൂരെയാകാം. NOC ദൂരെയാകരുത്.")],
 "ഉടമ ദൂരെയാകാം,\nNOC ദൂരെയാകരുത്", CTA_GST, theme="crm",
 cap_ml="വാടക കെട്ടിടത്തിൽ GST അപേക്ഷിച്ചാൽ വാടക കരാർ, ഉടമയുടെ NOC, ഒരു ബില്ല് എന്നിവ വേണം. NOC ഇല്ലെന്ന് REG-03 വന്നാൽ REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി കൊടുക്കണം, ഇല്ലെങ്കിൽ REG-05-ൽ റിജക്ട് ആകാം. ഉടമ ഗൾഫിലുള്ള ഒരു കൂട്ടുകാരന് ഇത് അയക്കൂ.",
 cap_en="Applying for GST from a rented building needs the rent agreement, the owner's NOC and a bill. If a REG-03 query says the NOC is missing, reply in REG-04 within 7 working days, or the application may be rejected in REG-05. Send this to a friend whose landlord lives in the Gulf.",
 cap_mg="Vaadaka kettidathil GST apekshichaal rent agreement, udamayude NOC, oru bill ennivaa venam. NOC illennu REG-03 vannaal REG-04-il 7 working days-inakam marupadi kodukkanam, illenkil REG-05-il reject aakaam. Udama Gulf-il ulla oru koottukaaranu ithu ayakku.")

# faq, fix-it: the officer asks for bank proof; the new current account has no cheque book yet
duo("gd048", "new_company", "B", "bank", "GST ചോദ്യം: \"ബാങ്ക്\nപ്രൂഫ്?\" ചെക്ക് ബുക്ക്\nവന്നിട്ടില്ല", [
 ("A","wide","മനോജേ, പുതിയ കറന്റ് അക്കൗണ്ട് തുറന്ന് GST അപേക്ഷിച്ചു. REG-03-ൽ ബാങ്ക് പ്രൂഫ് ചോദിച്ചു. ചെക്ക് ബുക്ക് ഇതുവരെ വന്നില്ല."),
 ("V","V","ശ്രുതീ, ക്യാൻസൽ ചെയ്ത ചെക്ക് മാത്രമല്ല വഴി. പാസ്ബുക്കോ ബാങ്ക് സ്റ്റേറ്റ്മെന്റോ കൊടുക്കാം."),
 ("A","A","അപ്പോ ചെക്ക് ബുക്കിന് കാത്തിരിക്കണ്ട?"),
 ("V","V","വേണ്ട. സ്റ്റേറ്റ്മെന്റ് ചേർത്ത് REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി കൊടുക്ക്."),
 ("A","A","ബ്രാഞ്ചിൽ നിന്ന് ഇപ്പോ തന്നെ സ്റ്റേറ്റ്മെന്റ് എടുക്കാം."),
 ("V","wide","ചെക്ക് വൈകിയാലും മറുപടി വൈകരുത്.")],
 "ചെക്ക് ഇല്ലെങ്കിൽ\nസ്റ്റേറ്റ്മെന്റ്", CTA_GST, theme="faq",
 cap_ml="GST-ക്ക് ബാങ്ക് പ്രൂഫ് ആയി ക്യാൻസൽ ചെയ്ത ചെക്ക്, പാസ്ബുക്ക്, അല്ലെങ്കിൽ ബാങ്ക് സ്റ്റേറ്റ്മെന്റ് കൊടുക്കാം. REG-03-ൽ ബാങ്ക് പ്രൂഫ് ചോദിച്ചാൽ ചെക്ക് ബുക്കിന് കാത്തിരിക്കാതെ REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി കൊടുക്കൂ. നിങ്ങൾ ഏതാണ് കൊടുത്തത്?",
 cap_en="For GST, bank proof can be a cancelled cheque, a passbook or a bank statement. If a REG-03 query asks for it, don't wait for the cheque book: reply in REG-04 within 7 working days. Which one did you upload?",
 cap_mg="GST-kku bank proof aayi cancel cheytha cheque, passbook, allenkil bank statement kodukkaam. REG-03-il bank proof chodichaal cheque book-inu kaathirikkaathe REG-04-il 7 working days-inakam marupadi kodukku. Ningal ethaanu koduthathu?")

# new, fix-it: own building, but the "address proof" uploaded was a photo of the shop board
duo("gd049", "trader", "B", "home", "\"കടയുടെ ബോർഡിന്റെ\nഫോട്ടോ ഇട്ടു\"\nGST: അഡ്രസ് പ്രൂഫ്?", [
 ("A","wide","അരുണേ, നിന്റെ സ്റ്റേഷനറി കടയുടെ GST അപേക്ഷയ്ക്ക് REG-03. അഡ്രസ് പ്രൂഫ് ശരിയല്ല എന്ന്. എന്താ അപ്‌ലോഡ് ചെയ്തത്?"),
 ("V","V","സ്നേഹേ, കടയുടെ ബോർഡിന്റെ നല്ല ഫോട്ടോ. പേരും സ്ഥലവും വലുതായി ഉണ്ടല്ലോ."),
 ("A","A","ബോർഡ് നമ്മൾ തന്നെ എഴുതിയതല്ലേ? സ്വന്തം കെട്ടിടമാണെങ്കിൽ ഒരു ബില്ലോ കരം അടച്ച രസീതോ ആണ് വേണ്ടത്."),
 ("V","V","കരം രസീത് ഫയലിൽ ഉണ്ട്. അത് മതിയോ?"),
 ("A","A","മതി. അത് ചേർത്ത് REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി. ചോദിച്ചതിന് മാത്രം."),
 ("V","wide","ബോർഡ് നമ്മുടേത്. തെളിവ് രസീത്.")],
 "ബോർഡ് നമ്മുടേത്,\nതെളിവ് രസീത്", CTA_GST, theme="new",
 cap_ml="GST-ക്ക് അഡ്രസ് പ്രൂഫ് എന്നാൽ കടയുടെ ബോർഡിന്റെ ഫോട്ടോ അല്ല. സ്വന്തം കെട്ടിടമാണെങ്കിൽ ബില്ലോ കരം അടച്ച രസീതോ, വാടകയാണെങ്കിൽ കരാർ, ഉടമയുടെ NOC, ബില്ല്. REG-03 വന്നാൽ REG-04-ൽ 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി. നിങ്ങളുടെ കട സ്വന്തമോ വാടകയോ?",
 cap_en="For GST, address proof is not a photo of your shop board. Own building: a bill or a property tax receipt; rented: the rent agreement, the owner's NOC and a bill. Got a REG-03 query? Reply in REG-04 within 7 working days. Is your shop owned or rented?",
 cap_mg="GST-kku address proof ennaal kadayude board-inte photo alla. Swantham kettidamaanenkil billo karam adacha raseetho, vaadakayaanenkil agreement, udamayude NOC, bill. REG-03 vannaal REG-04-il 7 working days-inakam marupadi. Ningalude kada swanthamo vaadakayo?")

# faq, fix-it: a physio clinic ignored REG-03 and got REG-05; what the rejection says
duo("gd050", "service_pro", "B", "hospital", "\"REG-05 വന്നു.\nGST റിജക്ട്.\nഇനി ഒരിക്കലും ഇല്ലേ?\"", [
 ("A","wide","ജോസഫ് ചേട്ടാ, ഫിസിയോ ക്ലിനിക്കിന്റെ GST അപേക്ഷ REG-05-ൽ റിജക്ട് ആയി. ഇനി ഒരിക്കലും കിട്ടില്ലേ?"),
 ("V","V","ലക്ഷ്മീ, അതിന് മുമ്പ് REG-03 എന്ന ഒരു ചോദ്യം വന്നിരുന്നോ?"),
 ("A","A","വന്നു. ഒപി തിരക്കിൽ മറുപടി കൊടുത്തില്ല."),
 ("V","V","മറുപടി ഇല്ലെങ്കിൽ ഓഫീസർക്ക് റിജക്ട് ചെയ്യാം, കാരണം എഴുതി തന്നെ. ആ കാരണം ആദ്യം വായിക്ക്, അതാണ് ശരിയാക്കേണ്ടത്."),
 ("A","A","അപ്പോ അടുത്ത തവണ ആ പേപ്പർ ആദ്യം റെഡി."),
 ("V","wide","നോട്ടീസ് മാറ്റിവെച്ചാൽ, അപേക്ഷയും മാറിനിൽക്കും.")],
 "REG-05 വന്നാൽ\nകാരണം വായിക്കൂ", CTA_GST, theme="faq",
 cap_ml="GST അപേക്ഷയ്ക്ക് REG-03-ൽ വന്ന ചോദ്യത്തിന് മറുപടി ഇല്ലെങ്കിൽ ഓഫീസർക്ക് REG-05-ൽ റിജക്ട് ചെയ്യാം, കാരണം എഴുതി തന്നെ. ആ കാരണം ആദ്യം വായിക്കൂ, അതാണ് ശരിയാക്കേണ്ടത്. GST നോട്ടീസ് മാറ്റിവെക്കുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="If a REG-03 query on your GST application gets no reply, the officer may reject it in REG-05, with the reasons in writing. Read those reasons first: they tell you what to fix. Send this to a friend who keeps putting GST notices aside.",
 cap_mg="GST apekshaykku REG-03-il vanna chodyathinu marupadi illenkil officer-kku REG-05-il reject cheyyaam, kaaranam ezhuthi thanne. Aa kaaranam aadyam vaayikku, athaanu shariyaakkendathu. GST notice maattivekkunna oraalkku ithu ayakku.")

# crm (STORY 10): tax due is small, so he thinks the penalty is 10% of it; the law says Rs 10,000 or 10%, whichever is higher
duo("gd051", "trader", "B", "canteen", "\"ടാക്സ് 30,000 മാത്രം.\nപിഴ 10% അല്ലേ,\n3,000 പോരേ?\"", [
 ("A","wide","ഗോകുലേ, കാന്റീനുകളിലേക്ക് പലഹാരം കൊടുക്കുന്ന നിന്റെ യൂണിറ്റ് 40 ലക്ഷം കടന്നിട്ടും GST എടുത്തില്ലല്ലോ."),
 ("V","V","ദീപ്തീ, കണക്ക് നോക്കി. അടയ്ക്കേണ്ട ടാക്സ് 30,000 രൂപ. പിഴ അതിന്റെ 10% അല്ലേ, 3,000 രൂപ."),
 ("A","A","നിയമം പറയുന്നത് 10,000 രൂപ അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ. നിനക്ക് 10,000."),
 ("V","V","അപ്പോ പിഴ ടാക്സിന്റെ മൂന്നിലൊന്ന്!"),
 ("A","A","കൂടെ ടാക്സും 18% പലിശയും. ഇന്ന് തന്നെ രജിസ്റ്റർ ചെയ്യ്."),
 ("V","wide","ടാക്സ് ചെറുത്. പിഴയ്ക്ക് മിനിമം ഉണ്ട്.")],
 "ടാക്സ് ചെറുതായാലും\nപിഴ 10,000 മുതൽ", CTA_PENALTY, names=("ദീപ്തി","ഗോകുൽ"), theme="crm",
 cap_ml="GST ലിമിറ്റ് കടന്നിട്ടും രജിസ്റ്റർ ചെയ്യാതിരുന്നാൽ ടാക്സ്, 18% പലിശ, പിന്നെ 10,000 രൂപ അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ അത് പിഴ. ടാക്സ് 30,000 രൂപ ആണെങ്കിലും പിഴ 3,000 അല്ല, 10,000. 'ടാക്സ് ചെറുതല്ലേ' എന്ന് പറയുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="Crossed the GST limit and didn't register? You pay the tax, 18% interest and a penalty of 10,000 or 10% of the tax due, whichever is higher. On 30,000 of tax the penalty is not 3,000 but 10,000. Send this to someone who says 'my tax is small anyway'.",
 cap_mg="GST limit kadannittum register cheyyaathirunnaal tax, 18% palisha, pinne 10,000 roopa allenkil tax-inte 10%, ethaano kooduthal athu pizha. Tax 30,000 roopa aanenkilum pizha 3,000 alla, 10,000. 'Tax cheruthalle' ennu parayunna oraalkku ithu ayakku.")

# faq: a student brand registered voluntarily, then exams: several nil returns missed, each with its own late fee
duo("gd052", "online_seller", "B", "hostel", "പരീക്ഷക്കാലം. 6 മാസം\nഒരു വിൽപ്പനയുമില്ല.\n\"ഒരു റിട്ടേൺ മതിയോ?\"", [
 ("A","wide","സഞ്ജൂ, നമ്മുടെ ടീ-ഷർട്ട് ബ്രാൻഡിന് GST എടുത്തിട്ട് പരീക്ഷ കാരണം 6 മാസം ഒന്നും വിറ്റില്ല. റിട്ടേണും ഫയൽ ചെയ്തില്ല."),
 ("V","V","അലീനേ, ഒന്നും വിറ്റില്ലല്ലോ. എല്ലാം ചേർത്ത് ഒരു നിൽ റിട്ടേൺ ഇട്ടാൽ പോരേ?"),
 ("A","A","പോരാ. ഫയൽ ചെയ്യാത്ത ഓരോ റിട്ടേണും വെവ്വേറെ ഫയൽ ചെയ്യണം. ഓരോന്നിനും വെവ്വേറെ ലേറ്റ് ഫീ."),
 ("V","V","ലേറ്റ് ഫീ എത്രയാ?"),
 ("A","A","നിൽ GSTR-3B-ക്ക് ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ. ഇന്ന് തന്നെ തീർത്താൽ അത്രയും കുറയും."),
 ("V","wide","പരീക്ഷ ഒന്ന്. റിട്ടേൺ പലത്.")],
 "പരീക്ഷ ഒന്ന്,\nറിട്ടേൺ പലത്", CTA_PENALTY, theme="faq",
 cap_ml="GST രജിസ്ട്രേഷൻ ഉണ്ടെങ്കിൽ വിൽപ്പന ഇല്ലാത്ത മാസങ്ങളിലും നിൽ റിട്ടേൺ വേണം. ഫയൽ ചെയ്യാത്ത ഓരോ റിട്ടേണിനും വെവ്വേറെ ലേറ്റ് ഫീ: നിൽ GSTR-3B-ക്ക് ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ. പരീക്ഷയ്ക്കിടയിൽ ബിസിനസ് നടത്തുന്ന ഒരു കൂട്ടുകാരന് ഇത് അയക്കൂ.",
 cap_en="A GST registration means nil returns even in months with no sales, and every return you missed has its own late fee: 20 a day for a nil GSTR-3B, up to 500 per return. Send this to a friend running a side business through exam season.",
 cap_mg="GST registration undenkil vilpana illaatha maasangalilum nil return venam. File cheyyaatha oro return-inum vevvere late fee: nil GSTR-3B-kku divasam 20 roopa, oru return-inu 500 vare. Pareekshaykkidayil business nadathunna oru koottukaaranu ithu ayakku.")

# crm (STORY 11): a Kerala-only marketplace seller on PAN-based enrolment crosses Rs 40 lakh
duo("gd053", "online_seller", "B", "metro", "PAN നമ്പർ വെച്ച്\nഓൺലൈൻ കച്ചവടം.\nഈ വർഷം 43 ലക്ഷം", [
 ("A","wide","വരുണേ, എന്റെ ചക്കവരട്ടി കേരളത്തിനകത്ത് മാത്രമാ ഓൺലൈനിൽ വിൽക്കുന്നത്, PAN വെച്ചുള്ള എൻറോൾമെന്റിൽ. ഈ വർഷം 43 ലക്ഷം!"),
 ("V","V","ശ്വേതേ, ആ എൻറോൾമെന്റ് ലിമിറ്റിന് താഴെയുള്ളവർക്കാ. സാധനത്തിന് കേരളത്തിൽ ലിമിറ്റ് 40 ലക്ഷം."),
 ("A","A","അപ്പോ PAN നമ്പർ ഇനി പോരാ?"),
 ("V","V","പോരാ, GST രജിസ്ട്രേഷൻ വേണം. വേണ്ട സമയത്ത് എടുത്തില്ലെങ്കിൽ ടാക്സും 18% പലിശയും പിഴയും."),
 ("A","A","എങ്കിൽ ഇന്ന് തന്നെ അപേക്ഷ."),
 ("V","wide","ഇളവ് ലിമിറ്റ് വരെ. അത് കഴിഞ്ഞാൽ GSTIN.")],
 "ഇളവ് ലിമിറ്റ് വരെ,\nപിന്നെ GSTIN", CTA_LIMIT, names=("ശ്വേത","വരുൺ"), theme="crm",
 cap_ml="കേരളത്തിനകത്ത് മാത്രം മാർക്കറ്റ്പ്ലേസിൽ വിൽക്കുന്ന, ലിമിറ്റിന് താഴെയുള്ള സെല്ലർക്ക് PAN വെച്ചുള്ള എൻറോൾമെന്റ് മതിയാകാം (മാർക്കറ്റ്പ്ലേസ് അനുവദിച്ചാൽ). സാധനങ്ങൾക്ക് 40 ലക്ഷം കടന്നാൽ GST രജിസ്ട്രേഷൻ വേണം. വൈകിയാൽ ടാക്സ്, 18% പലിശ, പിഴ. നിങ്ങൾ ഇപ്പോൾ എത്രയിലാണ്?",
 cap_en="A marketplace seller below the limit who sells only within Kerala may use a PAN-based enrolment number, if the marketplace supports it. Once goods sales cross 40 lakh, GST registration is needed; registering late means the tax, 18% interest and a penalty. Where is your turnover now?",
 cap_mg="Keralathinakathu maathram marketplace-il vilkkunna, limit-inu thaazheyulla seller-kku PAN vechulla enrolment mathiyaakaam (marketplace anuvadichaal). Goods-nu 40 lakh kadannaal GST registration venam. Vaikiyaal tax, 18% palisha, pizha. Ningal ippol ethrayilaanu?")

# faq: a services business at Rs 62 lakh wants the composition scheme; for services the limit is Rs 50 lakh
duo("gd054", "service_pro", "B", "cafe", "\"കോമ്പോസിഷൻ എടുത്താൽ\nകണക്ക് എളുപ്പം\"\nവരുമാനം 62 ലക്ഷം", [
 ("A","wide","റോഷാ, എന്റെ ആപ്പ് ടെസ്റ്റിംഗ് സർവീസ് ഈ വർഷം 62 ലക്ഷം. കോമ്പോസിഷൻ എടുത്താൽ കണക്ക് എളുപ്പമാകുമല്ലോ."),
 ("V","V","ആൽവിനേ, സർവീസിന് കോമ്പോസിഷൻ 50 ലക്ഷം വരെയാ. നീ അത് കടന്നു."),
 ("A","A","ഒന്നര കോടി വരെ എന്ന് കേട്ടല്ലോ?"),
 ("V","V","ഒന്നര കോടി സാധനം വിൽക്കുന്നവർക്കാ. സർവീസിന് 50 ലക്ഷം."),
 ("A","A","അപ്പോ സാധാരണ റിട്ടേൺ തന്നെ. കണക്ക് നോക്കാൻ ഒരാളെ വെക്കാം."),
 ("V","wide","എളുപ്പവഴിക്കും ഒരു ലിമിറ്റുണ്ട്.")],
 "സർവീസിന്\nകോമ്പോസിഷൻ 50 ലക്ഷം വരെ", CTA_LIMIT, theme="faq",
 cap_ml="GST കോമ്പോസിഷൻ സ്കീം: സാധനങ്ങൾക്ക് 1.5 കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ. ഒന്നര കോടി എന്ന് കേട്ട് സർവീസ് ബിസിനസ് കോമ്പോസിഷൻ നോക്കിയാൽ തെറ്റും. നിങ്ങൾ സാധനമാണോ സർവീസ് ആണോ വിൽക്കുന്നത്?",
 cap_en="The GST composition scheme goes up to 1.5 crore turnover for goods but only 50 lakh for services. A service business that heard '1.5 crore' and plans on composition at 62 lakh gets it wrong. Do you sell goods or services?",
 cap_mg="GST composition scheme: goods-nu 1.5 crore vare, service-nu 50 lakh vare turnover. Onnara crore ennu kettu service business composition nokkiyaal thettum. Ningal goods aano service aano vilkkunnathu?")

# new, fix-it: a query arrived just before the Onam holidays; the 7 days are working days
duo("gd055", "trader", "B", "autostand", "GST നോട്ടീസ് വന്നത്\nഓണം അവധിക്ക് മുമ്പ്.\n\"7 ദിവസം പോയി\"", [
 ("A","wide","ഷാജീ, സ്പെയർ പാർട്സ് കടയുടെ GST അപേക്ഷയ്ക്ക് REG-03 വന്നത് ഓണം അവധിക്ക് തൊട്ടുമുമ്പാ. 7 ദിവസം കഴിഞ്ഞു, ഇനി പോയി."),
 ("V","V","സജീ, 7 ദിവസം അല്ല, 7 പ്രവൃത്തി ദിവസം. അവധി ദിവസങ്ങൾ അതിൽ കൂടില്ല."),
 ("A","A","അപ്പോ ഇനിയും സമയമുണ്ടോ?"),
 ("V","V","നോട്ടീസിലെ തീയതി മുതൽ എണ്ണി നോക്ക്. സമയമുണ്ടെങ്കിൽ ഇന്ന് തന്നെ REG-04-ൽ മറുപടി. അവസാന ദിവസം കാത്തിരിക്കല്ലേ."),
 ("A","A","ചോദിച്ച രേഖ ഇപ്പോ തന്നെ സ്കാൻ ചെയ്യാം."),
 ("V","wide","അവധി കലണ്ടറിന്. ഫയലിന് അല്ല.")],
 "പ്രവൃത്തി ദിവസം എണ്ണൂ,\nഅവസാനം വരെ കാക്കല്ലേ", CTA_GST, theme="new",
 cap_ml="GST അപേക്ഷയ്ക്ക് REG-03 വന്നാൽ മറുപടി REG-04-ൽ, 7 പ്രവൃത്തി ദിവസത്തിനകം. 7 കലണ്ടർ ദിവസമല്ല. നോട്ടീസിലെ തീയതി മുതൽ എണ്ണി, അവസാന ദിവസം വരെ കാത്തിരിക്കാതെ മറുപടി കൊടുക്കൂ. അവധിക്ക് മുമ്പ് നോട്ടീസ് കിട്ടിയ ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="A REG-03 query on your GST application is answered in REG-04 within 7 working days, not 7 calendar days. Count from the date on the notice and reply without waiting for the last day. Send this to someone whose notice arrived just before a holiday.",
 cap_mg="GST apekshaykku REG-03 vannaal marupadi REG-04-il, 7 working days-inakam. 7 calendar days alla. Notice-ile theeyathi muthal enni, avasaana divasam vare kaathirikkaathe marupadi kodukku. Avadhikku mumpu notice kittiya oraalkku ithu ayakku.")

# faq (F9): shop closed for good, owner now in Dubai, GSTIN still active, no returns for 8 months
duo("gd056", "nri_business", "B", "gulfoffice", "കട പൂട്ടി ദുബായിലേക്ക്.\nGSTIN ഇപ്പോഴും ആക്ടീവ്.\n8 മാസം റിട്ടേൺ ഇല്ല", [
 ("A","wide","ഇർഫാനേ, നാട്ടിലെ മൊബൈൽ ആക്സസറി കട പൂട്ടിയിട്ടാണല്ലോ നീ ഇങ്ങോട്ട് വന്നത്. GST എന്ത് ചെയ്തു?"),
 ("V","V","സൽമാ, കട ഇല്ലല്ലോ. GST-യും കടയുടെ കൂടെ പോയി എന്നാ വിചാരം."),
 ("A","A","പോർട്ടലിൽ GSTIN ആക്ടീവ് ആണോ എന്ന് നോക്ക്. രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം വിൽപ്പന ഇല്ലെങ്കിലും നിൽ റിട്ടേൺ വേണം."),
 ("V","V","8 മാസമായി ഒന്നും ഫയൽ ചെയ്തില്ല..."),
 ("A","A","നിൽ റിട്ടേൺ വൈകിയാൽ ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ. ഇനി എന്ത് വേണം എന്ന് ഇന്ന് തന്നെ ഒരു പ്രൊഫഷണലിനോട് ചോദിക്ക്."),
 ("V","wide","നാട് വിട്ടാലും GSTIN നാട്ടിൽ തന്നെ.")],
 "നാട് വിട്ടാലും\nGSTIN നാട്ടിൽ തന്നെ", CTA_PENALTY, names=("സൽമ","ഇർഫാൻ"), theme="faq",
 cap_ml="കട പൂട്ടിയാലും GST രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം റിട്ടേൺ വേണം, വിൽപ്പന ഇല്ലെങ്കിൽ നിൽ റിട്ടേൺ. നിൽ റിട്ടേൺ വൈകിയാൽ ദിവസം 20 രൂപ, ഒരു റിട്ടേണിന് 500 വരെ ലേറ്റ് ഫീ. കട പൂട്ടി ഗൾഫിലേക്ക് പോയ ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="Closing the shop doesn't close the GST registration: while you are registered, returns are due, nil returns in months with no sales. A late nil return costs 20 a day, up to 500 per return. Send this to someone who shut a shop and moved to the Gulf.",
 cap_mg="Kada poottiyaalum GST registration ullidatholam return venam, vilpana illenkil nil return. Nil return vaikiyaal divasam 20 roopa, oru return-inu 500 vare late fee. Kada pootti Gulf-ilekku poya oraalkku ithu ayakku.")

# new, fix-it: the query asks for a clarification of the business, not a document
duo("gd057", "service_pro", "B", "tailor", "GST ഓഫീസർ ചോദിച്ചു:\n\"ശരിക്കും എന്താ\nബിസിനസ്?\"", [
 ("A","wide","സുജിത്തേ, എന്റെ ബ്ലൗസ് ഡിസൈനിംഗിന്റെ GST അപേക്ഷയ്ക്ക് REG-03. ബിസിനസ് എന്താണെന്ന് വ്യക്തമാക്കാൻ."),
 ("V","V","ഷൈനീ, അപേക്ഷയിൽ എന്താ എഴുതിയത്?"),
 ("A","A","'തയ്യലും വിൽപ്പനയും' എന്ന് മാത്രം. രേഖ ഒന്നും ചോദിച്ചിട്ടില്ല."),
 ("V","V","REG-04-ൽ രേഖ മാത്രമല്ല, വിശദീകരണവും കൊടുക്കാം. ചെയ്യുന്നത് കൃത്യമായി എഴുതി 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി കൊടുക്ക്."),
 ("A","A","തുന്നൽ മാത്രമാണോ, തുണിയും വിൽക്കുന്നുണ്ടോ എന്ന് വ്യക്തമായി എഴുതാം."),
 ("V","wide","അളവ് പോലെ, മറുപടിയും കൃത്യം.")],
 "അളവ് പോലെ\nമറുപടിയും കൃത്യം", CTA_GST, names=("ഷൈനി","സുജിത്"), theme="new",
 cap_ml="GST അപേക്ഷയ്ക്ക് വരുന്ന REG-03 എപ്പോഴും രേഖ ചോദിക്കില്ല. ബിസിനസ് എന്താണെന്ന് വ്യക്തമാക്കാൻ ചോദിച്ചാൽ REG-04-ൽ വിശദീകരണം എഴുതി 7 പ്രവൃത്തി ദിവസത്തിനകം മറുപടി കൊടുക്കാം. നിങ്ങളുടെ അപേക്ഷയിൽ ബിസിനസ് വ്യക്തമായി എഴുതിയോ?",
 cap_en="A REG-03 query on a GST application doesn't always ask for a document. If the officer asks you to clarify what the business does, write a clear explanation in REG-04 within 7 working days. Did your application describe the business clearly?",
 cap_mg="GST apekshaykku varunna REG-03 eppozhum rekha chodikkilla. Business enthaanennu vyakthamaakkaan chodichaal REG-04-il vishadeekaranam ezhuthi 7 working days-inakam marupadi kodukkaam. Ningalude apekshayil business vyakthamaayi ezhuthiyo?")

# faq: a 3B (with sales) two months late: Rs 50 a day, but capped at Rs 2,000 per return for turnover up to Rs 1.5 crore
duo("gd058", "trader", "B", "mall", "\"60 ദിവസം വൈകി.\nദിവസം 50 വെച്ച്\n3,000 അടയ്ക്കണ്ടേ?\"", [
 ("A","wide","ഷഫീഖേ, കടയുടെ GSTR-3B രണ്ട് മാസം വൈകി. ദിവസം 50 രൂപ വെച്ച് 60 ദിവസം, 3,000 രൂപ ലേറ്റ് ഫീ ആകുമല്ലോ."),
 ("V","V","നസ്രിനേ, നിന്റെ വർഷ ടേൺഓവർ ഒന്നര കോടിക്ക് താഴെയല്ലേ? അവർക്ക് ഒരു റിട്ടേണിന് 2,000 രൂപ വരെ മാത്രം."),
 ("A","A","ഹാവൂ! അപ്പോ ഇനിയും വൈകിയാലും 2,000 അല്ലേ?"),
 ("V","V","ആ റിട്ടേണിന് മാത്രം. അടുത്ത റിട്ടേണിനും വൈകിയാൽ അതിനും വേറെ ലേറ്റ് ഫീ. ഇന്ന് തന്നെ ഫയൽ ചെയ്യ്."),
 ("A","A","ശരി, ഇന്ന് രാത്രി തന്നെ."),
 ("V","wide","ക്യാപ് ഉണ്ടെന്ന് കരുതി ഉറങ്ങല്ലേ.")],
 "ക്യാപ് ഉണ്ട്,\nഉറങ്ങാൻ ലൈസൻസ് ഇല്ല", CTA_PENALTY, names=("നസ്രിൻ","ഷഫീഖ്"), theme="faq",
 cap_ml="GSTR-3B വൈകിയാൽ ദിവസം 50 രൂപ ലേറ്റ് ഫീ. ഒന്നര കോടി വരെ ടേൺഓവർ ഉള്ളവർക്ക് ഒരു റിട്ടേണിന് 2,000 രൂപ വരെ. പക്ഷേ ഓരോ റിട്ടേണിനും വെവ്വേറെ, അതുകൊണ്ട് അടുത്തതും വൈകിക്കരുത്. നിങ്ങളുടെ അവസാന 3B എപ്പോഴാണ് ഫയൽ ചെയ്തത്?",
 cap_en="A late GSTR-3B costs a late fee of 50 a day, capped at 2,000 per return for turnover up to 1.5 crore. The cap is per return, so don't let the next one slip too. When did you file your last 3B?",
 cap_mg="GSTR-3B vaikiyaal divasam 50 roopa late fee. Onnara crore vare turnover ullavarkku oru return-inu 2,000 roopa vare. Pakshe oro return-inum vevvere, athukondu adutha return-um vaikikkaruthu. Ningalude avasaana 3B eppozhaanu file cheythathu?")
