# acc batch 01 (27 Nov refill): first 3D duo reels for monthly compliance. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns (STORY_THEMES rule). Facts only from topics.FACTS_ACC. No fees, no fixed due dates, no tax amounts.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

# faq, fix-it: the 3-year bar on old GST returns (homestay with returns pending since the slow season)
duo("acd001", "notice_holder", "B", "munnar", "പഴയ GST റിട്ടേൺ\nഫയൽ ചെയ്യാൻ നോക്കി.\nപോർട്ടൽ എടുക്കുന്നില്ല!", [
 ("A","wide","ബേസിലേ, ഹോംസ്റ്റേ അടച്ചിട്ട കാലത്തെ GST റിട്ടേണുകൾ ഇപ്പോഴും ബാക്കിയാ. അടുത്ത ആഴ്ച ഒന്നിച്ച് ഫയൽ ചെയ്യാം എന്ന് കരുതി."),
 ("V","V","സെലിനേ, ഒന്നിച്ച് എന്ന് പറഞ്ഞ് നീട്ടരുത്. ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയാൽ ആ റിട്ടേൺ പോർട്ടൽ പിന്നെ എടുക്കില്ല."),
 ("A","A","എന്നുവെച്ചാൽ പിന്നെ ഒരിക്കലും ഫയൽ ചെയ്യാൻ പറ്റില്ലേ?"),
 ("V","wide","2025 ജൂലൈ മുതലുള്ള റിട്ടേണുകൾക്ക് ഈ നിയമം ഉണ്ട്. ഏറ്റവും പഴയത് ആദ്യം ഫയൽ ചെയ്യുക. ലോക്ക് ആകും മുമ്പ്."),
 ("A","wide","ബാക്കി വെച്ച റിട്ടേൺ, പൂട്ടിയ വാതിൽ ആകും.")],
 "പഴയ റിട്ടേൺ ആദ്യം,\nലോക്ക് ആകും മുമ്പ്", CTA_ITR, theme="faq",
 cap_ml="ഫയൽ ചെയ്യാത്ത പഴയ GST റിട്ടേണുകൾ ഉണ്ടോ? 2025 ജൂലൈ ടാക്സ് പീരിയഡ് മുതൽ, ഡ്യൂ ഡേറ്റ് കഴിഞ്ഞ് 3 വർഷം ആയ റിട്ടേൺ പോർട്ടൽ ബ്ലോക്ക് ചെയ്യും. ഏറ്റവും പഴയത് ആദ്യം ഫയൽ ചെയ്യൂ. നിങ്ങൾക്ക് എത്ര മാസത്തെ റിട്ടേൺ ബാക്കിയുണ്ട്?",
 cap_en="A homestay owner plans to file all her pending GST returns together, some day. Since the July 2025 tax period, the GST portal blocks a return once 3 years have passed from its due date, so it can never be filed. File the oldest ones first, before they lock. How many months are pending for you?",
 cap_mg="File cheyyaatha pazhaya GST returns undo? 2025 July tax period muthal, due date kazhinju 3 varsham aaya return portal block cheyyum. Ettavum pazhayathu aadyam file cheyyu. Ningalkku ethra maasathe return baakkiyundu?")

# new: a tailor with small income thinks a late ITR costs nothing
duo("acd002", "freelancer_itr", "C", "tailor", "\"ചെറിയ വരുമാനമല്ലേ,\nITR വൈകിയാലും\nഒന്നുമില്ല\"", [
 ("A","wide","മോഹനേട്ടാ, ഈ വർഷത്തെ ITR ഫയൽ ചെയ്തോ? കഴിഞ്ഞ വർഷം വൈകിയാണല്ലോ ചെയ്തത്."),
 ("V","V","എന്റേത് ചെറിയ തയ്യൽ വരുമാനമല്ലേ ഉഷേ. വൈകിയാലും ആരും ചോദിക്കില്ല."),
 ("A","A","ഫയൽ ചെയ്യേണ്ട ആളാണെങ്കിൽ, വരുമാനം 5 ലക്ഷം വരെയാണെങ്കിലും വൈകിയാൽ 1,000 രൂപ ലേറ്റ് ഫീ വരാം. അതിന് മുകളിൽ കൂടുതൽ."),
 ("V","V","അപ്പോ ചെറിയ വരുമാനത്തിനും വൈകലിന് കൂലിയുണ്ട്!"),
 ("A","wide","തയ്യൽ സമയത്ത് തീർക്കും പോലെ, ITR-ഉം.")],
 "ചെറിയ വരുമാനം,\nവൈകിയാൽ ലേറ്റ് ഫീ", CTA_ITR, theme="new",
 cap_ml="വരുമാനം ചെറുതാണെന്ന് കരുതി ITR വൈകിക്കല്ലേ. ഫയൽ ചെയ്യേണ്ട ആളാണെങ്കിൽ, വരുമാനം 5 ലക്ഷം വരെയാണെങ്കിലും വൈകിയാൽ 1,000 രൂപ ലേറ്റ് ഫീ വരാം; അതിന് മുകളിൽ കൂടുതൽ. ഈ വർഷത്തെ ഡ്യൂ ഡേറ്റ് ടീമിനോട് ഉറപ്പാക്കൂ. നിങ്ങളുടെ ITR ഈ വർഷം ഫയൽ ചെയ്തോ?",
 cap_en="A tailor thinks a late income-tax return costs nothing because his income is small. If you have to file, a late ITR carries a late fee of 1,000 rupees even when income is up to 5 lakh, and more above that. Check this year's due date with the team. Have you filed yours this year?",
 cap_mg="Varumaanam cheruthaanennu karuthi ITR vaikikkalle. File cheyyenda aalaanenkil, varumaanam 5 lakh vareyaanenkilum vaikiyaal 1,000 rupees late fee varaam; athinu mukalil kooduthal. Ee varshathe due date team-inodu urappaakku. Ningalude ITR ee varsham file cheytho?")

# crm (C6-style, invented): two friends' new company did no business in its first months, nobody filed GST returns
duo("acd003", "new_company_acc", "A", "photocopy", "കമ്പനി തുടങ്ങി,\nഒരു ബിസിനസും നടന്നില്ല.\nഅപ്പോ റിട്ടേണും വേണ്ട?", [
 ("A","wide","ഉണ്ണീ, നമ്മുടെ ഇവന്റ് കമ്പനി എടുത്തിട്ട് ആറ് മാസം. ഒരു ഓർഡറും വന്നില്ല. GST റിട്ടേൺ ഒന്നും ചെയ്തിട്ടില്ല."),
 ("V","V","അശ്വതീ, ബിസിനസ് ഇല്ലാത്തപ്പോൾ എന്ത് റിട്ടേൺ? ഓർഡർ വരുമ്പോൾ തുടങ്ങാം."),
 ("A","A","അങ്ങനെയല്ല. GST രജിസ്ട്രേഷൻ ഉള്ളിടത്തോളം വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ ഫയൽ ചെയ്യണം."),
 ("V","V","അപ്പോ ഈ ആറ് മാസവും ബാക്കിയാണ്. ഇന്ന് തന്നെ തുടങ്ങാം."),
 ("A","wide","ഓർഡർ ഇല്ലാത്ത മാസത്തിനും ഒരു റിട്ടേൺ ഉണ്ട്.")],
 "ബിസിനസ് ഇല്ലാത്ത മാസം,\nനിൽ റിട്ടേൺ വേണം", CTA_ACCOUNTS, theme="crm",
 cap_ml="പുതിയ കമ്പനി എടുത്തു, പക്ഷേ ഒരു ഓർഡറും വന്നില്ലേ? GST രജിസ്ട്രേഷൻ ഉണ്ടെങ്കിൽ വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ ഫയൽ ചെയ്യണം. ബാക്കിയായാൽ ലേറ്റ് ഫീ. നിങ്ങളുടെ കമ്പനി എത്ര മാസം മുമ്പ് തുടങ്ങി?",
 cap_en="Two friends registered an events company, got no orders for six months and filed no GST returns. While you are registered, a nil return is due even in a month with no sales; leaving them pending brings late fees. How long ago did your company start?",
 cap_mg="Puthiya company eduthu, pakshe oru order-um vannille? GST registration undenkil vilpana illaatha maasavum nil return file cheyyanam. Baakkiyaayaal late fee. Ningalude company ethra maasam mumbu thudangi?")

# faq: a phone shop found a wrong bill in GSTR-1 and fixed it in time
duo("acd004", "small_trader_acc", "B", "mobileshop", "GSTR-1-ൽ ഒരു ബില്ല്\nതെറ്റി. 3B ഫയൽ\nചെയ്യാൻ പോകുന്നു", [
 ("A","wide","ഫഹദേ, നിർത്ത്. GSTR-1-ൽ ആ ഫോൺ ബില്ലിന്റെ തുക ഒരു പൂജ്യം കൂടിപ്പോയി."),
 ("V","V","സാരമില്ല ഹന്ന. 3B-ൽ ശരിയായ കണക്ക് അടിച്ചാൽ പോരേ?"),
 ("A","A","ഇപ്പോൾ പറ്റില്ല. 3B-ലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരും. തിരുത്തേണ്ടത് GSTR-1A-യിൽ."),
 ("V","V","അപ്പോ ആദ്യം 1A, പിന്നെ 3B. ക്രമം തെറ്റിയാൽ തെറ്റ് അതേപടി പോകും."),
 ("A","wide","ഒരു പൂജ്യം, ഒരു മാസത്തെ തലവേദന.")],
 "തെറ്റ് കണ്ടാൽ\nആദ്യം GSTR-1A", CTA_ITR, theme="faq",
 cap_ml="GSTR-1-ൽ തെറ്റ് കണ്ടോ? 2025 ജൂലൈ മുതൽ GSTR-3B-യിലെ വിൽപ്പന കണക്ക് GSTR-1-ൽ നിന്ന് ലോക്ക് ആയി വരും. അതുകൊണ്ട് 3B-ക്ക് മുമ്പ് GSTR-1A-യിൽ തിരുത്തണം. നിങ്ങൾ ഫയൽ ചെയ്യും മുമ്പ് ബില്ലുകൾ ഒത്തുനോക്കാറുണ്ടോ?",
 cap_en="A phone shop spots an extra zero on one bill in GSTR-1, just before filing GSTR-3B. Since July 2025 the sales figures in 3B come locked from GSTR-1, so the fix goes into GSTR-1A first, then 3B. Do you check your bills before filing?",
 cap_mg="GSTR-1-il thettu kando? 2025 July muthal GSTR-3B-yile vilpana kanakku GSTR-1-il ninnu lock aayi varum. Athukondu 3B-kku mumbu GSTR-1A-yil thiruthanam. Ningal file cheyyum mumbu billukal othunokkaarundo?")

# new: a cafe's UPI receipts never reached the books
duo("acd005", "small_trader_acc", "C", "cafe", "ബാങ്കിൽ പൈസ കൂടുതൽ.\nകണക്കിൽ കുറവ്.\nഏതാ ശരി?", [
 ("A","wide","റോഷാ, ഈ മാസം ബാങ്കിൽ വന്ന പൈസയും നമ്മുടെ കണക്കുബുക്കിലെ വിൽപ്പനയും ഒത്തുപോകുന്നില്ല."),
 ("V","V","ക്യൂ ആർ സ്കാൻ ചെയ്ത് വന്ന പേയ്മെന്റുകൾ ഞാൻ ബുക്കിൽ എഴുതിയില്ല ആൽവിനേ. കാഷ് മാത്രമേ എഴുതിയുള്ളൂ."),
 ("A","A","GST റിട്ടേണും വർഷാവസാനം ITR-ഉം ഈ ബുക്കിൽ നിന്നാണ് പോകുന്നത്. ബാങ്കും ബുക്കും എല്ലാ മാസവും ഒത്തുനോക്കണം."),
 ("V","V","ഇനി മാസാവസാനം ഒരു മണിക്കൂർ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റും ബുക്കും ഒരുമിച്ച്."),
 ("A","wide","ബാങ്ക് പറയുന്നതും ബുക്ക് പറയുന്നതും ഒന്നാകണം.")],
 "ബാങ്കും ബുക്കും\nഎല്ലാ മാസവും ഒത്തുനോക്കൂ", CTA_ACCOUNTS, theme="new",
 cap_ml="ഓൺലൈനായി വന്ന പേയ്മെന്റുകൾ കണക്കുബുക്കിൽ കയറിയിട്ടുണ്ടോ? GST റിട്ടേണും ITR-ഉം ആ കണക്കിൽ നിന്നാണ്. എല്ലാ മാസവും ബാങ്ക് സ്റ്റേറ്റ്മെന്റും ബുക്കും ഒത്തുനോക്കൂ. നിങ്ങൾ അവസാനമായി എപ്പോൾ ഒത്തുനോക്കി?",
 cap_en="Two friends running a cafe find more money in the bank than sales in their books: the scan-and-pay receipts were never written down. GST returns and the year-end ITR come from those books, so match the bank statement with the books every month. When did you last match yours?",
 cap_mg="Online aayi vanna payments kanakkubookil kayariyittundo? GST return-um ITR-um aa kanakkil ninnaanu. Ella maasavum bank statement-um book-um othunokku. Ningal avasaanamaayi eppol othunokki?")
