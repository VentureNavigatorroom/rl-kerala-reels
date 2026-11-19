# ROC annual compliance seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, quotable last line.
# Facts only from topics.FACTS_ROC (statutory late fee of Rs 100 a day per form is a fact, not a price). People invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rcd001", "dormant_company", "A", "tailor", "ഈ വർഷം ഒരു ഓർഡറും\nഇല്ല. പിന്നെന്തിന്\nഫയലിംഗ്?", [
 ("A","wide","മോഹനേട്ടാ, കഥകളി വേഷത്തിന്റെ കമ്പനിക്ക് ഈ വർഷം ഒരു ഓർഡറും വന്നില്ല. ഫയലിംഗ് ഒഴിവാക്കാമല്ലോ?"),
 ("V","V","ഉഷേ, ബിസിനസ് ഇല്ലെങ്കിലും കമ്പനി ഉണ്ടല്ലോ. AGM, AOC-4, MGT-7 എല്ലാം വേണം."),
 ("A","A","ഫയൽ ചെയ്തില്ലെങ്കിൽ?"),
 ("V","V","ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ. പരിധിയില്ല."),
 ("A","wide","മൂന്ന് വർഷം ഇങ്ങനെ പോയാൽ ഡയറക്ടർമാർ അയോഗ്യരാകുമെന്നും കേട്ടു."),
 ("V","wide","ഓർഡർ ഉറങ്ങിയാലും കലണ്ടർ ഉറങ്ങില്ല.")],
 "ബിസിനസ് ഇല്ലെങ്കിലും\nഫയലിംഗ് ഉണ്ട്", CTA_FILING, theme="new",
 cap_ml="ബിസിനസ് ഇല്ലാത്ത വർഷവും പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി AGM നടത്തി AOC-4, MGT-7 ഫയൽ ചെയ്യണം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ, പരിധിയില്ല. നിങ്ങളുടെ കമ്പനി ഈ വർഷം ഫയൽ ചെയ്തോ?",
 cap_en="No orders this year, so no ROC filing? Wrong. A private limited company still holds its AGM and files AOC-4 and MGT-7; the late fee is Rs 100 a day per form with no cap. Has your company filed this year?",
 cap_mg="Business illaatha varshavum Pvt Ltd company AGM nadathi AOC-4, MGT-7 file cheyyanam. Vaikiyaal oro form-num divasam 100 roopa late fee, paridhiyilla. Ningalude company ee varsham file cheytho?")

duo("rcd002", "new_company_roc", "B", "courier", "സർട്ടിഫിക്കറ്റ് കിട്ടി,\nഫ്രെയിം ചെയ്തു.\nപിന്നെ ഒന്നും ചെയ്തില്ല", [
 ("A","wide","അരവിന്ദേ, കമ്പനി സർട്ടിഫിക്കറ്റ് ഓഫീസിൽ ഫ്രെയിം ചെയ്ത് വെച്ചു. ഇനി ബിസിനസ് മാത്രം."),
 ("V","V","ജയേ, ഫ്രെയിമിന് പുറമേ രണ്ട് ഡെഡ്ലൈൻ ഉണ്ട്. ആദ്യ ഓഡിറ്ററെ 30 ദിവസത്തിനുള്ളിൽ നിയമിക്കണം."),
 ("A","A","രണ്ടാമത്തേത്?"),
 ("V","V","180 ദിവസത്തിനുള്ളിൽ INC-20A ഫയൽ ചെയ്യണം."),
 ("A","wide","പാഴ്സൽ ട്രാക്ക് ചെയ്യുന്ന പോലെ ഡെഡ്ലൈനും ട്രാക്ക് ചെയ്യാം."),
 ("V","wide","പാഴ്സൽ വൈകിയാൽ ക്ഷമ, ഫയലിംഗ് വൈകിയാൽ പിഴ.")],
 "30 ദിവസം: ഓഡിറ്റർ\n180 ദിവസം: INC-20A", CTA_ROC, theme="faq",
 cap_ml="പുതിയ കമ്പനിക്ക് സർട്ടിഫിക്കറ്റ് കിട്ടിയ ശേഷം: 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ, 180 ദിവസത്തിനുള്ളിൽ INC-20A. കൊറിയർ ബിസിനസായാലും ആപ്പായാലും ഇത് ഒന്നുതന്നെ.",
 cap_en="Got your incorporation certificate? Two deadlines follow: appoint the first auditor within 30 days and file INC-20A within 180 days. First-year ROC compliance for new private limited companies.",
 cap_mg="Puthiya company-kku certificate kittiya shesham: 30 divasathinullil aadya auditor, 180 divasathinullil INC-20A. Courier business aayaalum app aayaalum ithu onnu thanne.")

chat("rcc001", "late_filer", "A", "30 സെപ്റ്റംബർ കഴിഞ്ഞു.\nഡയറക്ടർ KYC\nമറന്നു", ("ദിവ്യ", "നിഖിൽ"), [
 (0,"നിഖിൽ, നീ DIR-3 KYC ചെയ്തോ? ഇന്ന് ഒക്ടോബർ 5 ആയി."),
 (1,"അത് കമ്പനി ചെയ്യുന്നതല്ലേ? ഞാൻ ഒപ്പിട്ടാൽ പോരേ?"),
 (0,"ഇല്ല. ഓരോ ഡയറക്ടറും സ്വന്തം KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം."),
 (1,"വൈകിയാൽ?"),
 (0,"ലേറ്റ് ഫീ കൊടുത്ത് വേണം ശരിയാക്കാൻ. ഇന്ന് തന്നെ ചെയ്യ്."),
 (1,"ഷെയറിനൊപ്പം ഡ്യൂട്ടിയും വന്നു, അല്ലേ?")],
 "ഓരോ ഡയറക്ടറും\nസെപ്റ്റംബർ 30-നുള്ളിൽ", CTA_ROC, theme="new",
 cap_ml="കമ്പനിയിലെ ഓരോ ഡയറക്ടറും DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ചെയ്യണം. കമ്പനിയുടെ ഫയലിംഗ് അല്ല, ഓരോരുത്തരുടെയും ഉത്തരവാദിത്തം. നിങ്ങളുടെ കമ്പനിയിൽ എത്ര ഡയറക്ടർമാർ?",
 cap_en="Every director must complete DIR-3 KYC by 30 September; it is each director's own filing, not the company's. Missed it? A late fee applies. How many directors does your company have?",
 cap_mg="Company-ile oro director-um DIR-3 KYC September 30-nullil cheyyanam. Company-yude filing alla, ororutharudeyum uttharavaadithwam. Ningalude company-il ethra directors?")

duo("rcd003", "llp_owner", "A", "homestay", "LLP ആണ്, കമ്പനി അല്ല.\nഅപ്പോ ഫയലിംഗ്\nവേണ്ടേ?", [
 ("A","wide","ജോമോനേ, നമ്മുടെ ഹോംസ്റ്റേ LLP ആണല്ലോ. ROC ഫയലിംഗ് കമ്പനികൾക്കല്ലേ?"),
 ("V","V","ടീനേ, LLP-ക്കും ഉണ്ട്. വർഷത്തിൽ രണ്ട് ഫോം."),
 ("A","A","ഏതൊക്കെ, എപ്പോൾ?"),
 ("V","V","ഫോം 11 മെയ് 30-നുള്ളിൽ. ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. ബുക്കിംഗ് ഇല്ലാത്ത വർഷവും."),
 ("A","wide","മഴക്കാലത്ത് ഗസ്റ്റ് ഇല്ല, പക്ഷേ മെയ് 30 വരും."),
 ("V","wide","സീസൺ ഓഫ് ആകും, ഡെഡ്ലൈൻ ഓഫ് ആകില്ല.")],
 "LLP: മെയ് 30,\nഒക്ടോബർ 30", CTA_FILING, theme="faq",
 cap_ml="LLP-ക്കും വാർഷിക ഫയലിംഗ് ഉണ്ട്: ഫോം 11 മെയ് 30-നുള്ളിൽ, ഫോം 8 ഒക്ടോബർ 30-നുള്ളിൽ. ബിസിനസ് ഇല്ലാത്ത വർഷവും വേണം. നിങ്ങളുടേത് LLP ആണോ കമ്പനി ആണോ?",
 cap_en="An LLP has annual ROC filings too: Form 11 by 30 May and Form 8 by 30 October, even in a year with no bookings. Is your business an LLP or a company?",
 cap_mg="LLP-kkum annual filing undu: Form 11 May 30-nullil, Form 8 October 30-nullil. Business illaatha varshavum venam. Ningaludethu LLP aano company aano?")

duo("rcd004", "nri_director", "B", "gulfroom", "ദുബായിൽ ഇരുന്ന്\nനാട്ടിലെ കമ്പനി\n3 വർഷം മറന്നു", [
 ("A","wide","ഷംസൂ, നാട്ടിലെ കമ്പനിയുടെ കാര്യം ഓർമ്മയുണ്ടോ? 3 വർഷമായി ഒന്നും ഫയൽ ചെയ്തിട്ടില്ല."),
 ("V","V","നസീറേ, ബിസിനസ് നിന്നുപോയില്ലേ. അത് തനിയെ അടഞ്ഞുപോകും."),
 ("A","A","അങ്ങനെയല്ല. 3 വർഷം ഫയൽ ചെയ്യാതിരുന്നാൽ ഡയറക്ടർമാരെ 5 വർഷത്തേക്ക് അയോഗ്യരാക്കാം."),
 ("V","V","അപ്പോ പുതിയ കമ്പനി തുടങ്ങാനും പറ്റില്ലേ?"),
 ("A","wide","അയോഗ്യനായാൽ വേറെ കമ്പനിയിലും ഡയറക്ടർ ആകാൻ പറ്റില്ല. കമ്പനി സ്ട്രൈക്ക് ഓഫും ആകാം."),
 ("V","wide","നാട് വിട്ടാലും ROC നമ്മളെ വിടില്ല.")],
 "മറന്ന കമ്പനി\nനമ്മളെ മറക്കില്ല", CTA_ROC, theme="new",
 cap_ml="ഗൾഫിലിരുന്ന് നാട്ടിലെ കമ്പനി മറന്നാൽ: 3 വർഷം ഫയലിംഗ് ഇല്ലെങ്കിൽ ഡയറക്ടർമാരെ 5 വർഷത്തേക്ക് അയോഗ്യരാക്കാം, കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം. NRI ഡയറക്ടർമാർ ശ്രദ്ധിക്കുക.",
 cap_en="An NRI director in Dubai forgets his Kerala company for 3 years. Three years without filings can disqualify directors for 5 years and get the company struck off. A company does not close by itself.",
 cap_mg="Gulf-il irunnu naattile company marannaal: 3 varsham filing illenkil directors-ne 5 varshathekku ayogyaraakkaam, company strike off aakaam. NRI directors shraddhikkuka.")

duo("rcd005", "new_company_roc", "A", "canteen", "AGM എന്ന് കേട്ടപ്പോൾ\nവലിയ ഹാളും മൈക്കും\nഓർത്തു", [
 ("A","wide","അമലേ, AGM നടത്തണമെന്ന് ഓഡിറ്റർ പറഞ്ഞു. ഹാൾ ബുക്ക് ചെയ്യണോ?"),
 ("V","V","ആതിരേ, ഹാൾ വേണ്ട, നമ്മൾ രണ്ട് ഷെയർഹോൾഡർമാരേ ഉള്ളൂ. പക്ഷേ തീയതി പ്രധാനം."),
 ("A","A","എന്നാണ് അവസാന തീയതി?"),
 ("V","V","AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. പിന്നെ 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7."),
 ("A","wide","വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ, അല്ലേ?"),
 ("V","wide","മൈക്ക് വേണ്ട, കലണ്ടർ മതി.")],
 "AGM: സെപ്റ്റംബർ 30\nപിന്നെ 30, 60 ദിവസം", CTA_ROC, theme="faq",
 cap_ml="ചെറിയ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്കും AGM സെപ്റ്റംബർ 30-നുള്ളിൽ. പിന്നെ 30 ദിവസത്തിൽ AOC-4, 60 ദിവസത്തിൽ MGT-7. നിങ്ങളുടെ കലണ്ടറിൽ ഇത് ഉണ്ടോ?",
 cap_en="Even a two-shareholder private limited company holds its AGM by 30 September, then files AOC-4 within 30 days and MGT-7 within 60 days. Is this in your calendar?",
 cap_mg="Cheriya Pvt Ltd company-kkum AGM September 30-nullil. Pinne 30 divasathil AOC-4, 60 divasathil MGT-7. Ningalude calendar-il ithu undo?")
