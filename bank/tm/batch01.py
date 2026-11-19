# Trademark seed batch 01 (19 Nov, run 12). Myth-first hooks, 6 lines max, payoff by line 4-5, quotable last line.
# Facts only from topics.FACTS_TM. Never mention fees or promise registration. All people, brands and towns invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

duo("tmd001", "copied_brand", "A", "bakery", "കമ്പനി പേര് കിട്ടി.\n6 മാസം കഴിഞ്ഞ് നോട്ടീസ്:\n\"ആ ബ്രാൻഡ് ഞങ്ങളുടേത്\"", [
 ("A","wide","സാബുച്ചേട്ടാ, ഈ വക്കീൽ നോട്ടീസ് നോക്ക്. നമ്മുടെ ചിപ്സിന്റെ പേര് വേറൊരാളുടേതാണെന്ന്."),
 ("V","V","ജിഷേ, കമ്പനിക്ക് ആ പേര് അപ്രൂവ് ആയതല്ലേ? അപ്പോ നമ്മുടേത് തന്നെ."),
 ("A","A","കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. അതിന് ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യണം."),
 ("V","V","അപ്പോ അവർ നമ്മളേക്കാൾ മുമ്പ് ഫയൽ ചെയ്തു, അല്ലേ?"),
 ("A","wide","അതേ. ഇനി ഏത് പുതിയ പേരിനും ആദ്യം സെർച്ച്, പിന്നെ ഫയലിംഗ്."),
 ("V","wide","ചിപ്സ് പൊരിച്ചത് നമ്മൾ, പേര് കൊണ്ടുപോയത് അവർ.")],
 "കമ്പനി പേര് കിട്ടിയാലും\nബ്രാൻഡ് സുരക്ഷിതമല്ല", CTA_TRADEMARK, theme="faq",
 cap_ml="കമ്പനി പേര് അപ്രൂവ് ആയാൽ ബ്രാൻഡ് സുരക്ഷിതമാകില്ല. ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് വേറെ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ ബ്രാൻഡ് ഫയൽ ചെയ്തോ: അതെ / ഇല്ല?",
 cap_en="A company name approval does not protect your brand name. A banana chips maker learns this from a legal notice six months later. Has your brand been filed as a trademark: yes or no?",
 cap_mg="Company peru approve aayaal brand safe aakilla. Brand-nu trademark vere file cheyyanam. Ningalude brand file cheytho: athe / illa?")

duo("tmd002", "d2c_brand", "B", "handloom", "ഫയൽ ചെയ്ത പിറ്റേന്ന്\nലേബലിൽ R ചിഹ്നം.\nതെറ്റ്", [
 ("A","wide","കുമാരേട്ടാ, പുതിയ ലേബൽ കണ്ടോ? ബ്രാൻഡിന്റെ അടുത്ത് R ചിഹ്നം."),
 ("V","V","ലീലേ, ഇന്നലെയല്ലേ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തത്? രജിസ്റ്റർ ആയിട്ടില്ലല്ലോ."),
 ("A","A","ഫയൽ ചെയ്താൽ മതിയെന്നാ ഞാൻ കരുതിയത്."),
 ("V","V","ഫയൽ ചെയ്താൽ TM ഇടാം. R ചിഹ്നം രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം."),
 ("A","wide","അപ്പോ അയ്യായിരം ലേബൽ വീണ്ടും പ്രിന്റ് ചെയ്യണം."),
 ("V","wide","ആദ്യം TM, ക്ഷമയുണ്ടെങ്കിൽ R.")],
 "ഫയൽ ചെയ്താൽ TM\nരജിസ്റ്റർ ആയാൽ R", CTA_BRAND, theme="new",
 cap_ml="ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്താൽ TM ചിഹ്നം ഉപയോഗിക്കാം. R ചിഹ്നം രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം. നിങ്ങളുടെ ലേബലിൽ TM ആണോ R ആണോ?",
 cap_en="A handloom brand prints the R symbol the day after filing. You may use TM once you file a trademark; the R symbol only after registration. Which one is on your label: TM or R?",
 cap_mg="Trademark file cheythaal TM use cheyyaam. R symbol registration kittiya shesham maathram. Ningalude label-il TM aano R aano?")

duo("tmd003", "food_brand", "A", "juiceshop", "ജ്യൂസിന് ട്രേഡ്മാർക്ക് ഉണ്ട്.\nഅച്ചാറിനും അതേ പേര്\nസുരക്ഷിതമോ?", [
 ("A","wide","നൗഷാദിക്കാ, നമ്മുടെ ജ്യൂസ് ബ്രാൻഡിൽ ഇനി അച്ചാറും ഇറക്കാം."),
 ("V","V","റസിയേ, പേര് ട്രേഡ്മാർക്ക് ചെയ്തതല്ലേ. ഏത് സാധനത്തിനും ഇടാമല്ലോ."),
 ("A","A","അങ്ങനെയല്ല. ട്രേഡ്മാർക്കിന് 45 ക്ലാസുകൾ ഉണ്ട്. നമ്മൾ ഫയൽ ചെയ്തത് ഡ്രിങ്ക്സിന്റെ ക്ലാസിൽ മാത്രം."),
 ("V","V","അപ്പോ അച്ചാറിന്റെ ക്ലാസിൽ വേറൊരാൾക്ക് ഇതേ പേര് ഫയൽ ചെയ്യാം?"),
 ("A","wide","അതുകൊണ്ട് കച്ചവടം ചെയ്യുന്ന ഓരോ ക്ലാസിലും ഫയൽ ചെയ്യണം."),
 ("V","wide","ജ്യൂസ് പുളിക്കരുത്, പേരും പുളിക്കരുത്.")],
 "ഓരോ പ്രോഡക്റ്റിനും\nശരിയായ ക്ലാസ്", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്കിന് 45 ക്ലാസുകൾ ഉണ്ട്. ജ്യൂസിന് ഫയൽ ചെയ്ത പേര് അച്ചാറിനെ സംരക്ഷിക്കണമെന്നില്ല: കച്ചവടം ചെയ്യുന്ന ഓരോ ക്ലാസിലും ഫയൽ ചെയ്യണം.",
 cap_en="Trademarks are filed in 45 classes. A juice brand filed only for drinks may not be protected when it launches pickles: file in every class you actually trade in. Food brand trademark tips for Kerala.",
 cap_mg="Trademark-nu 45 classes undu. Juice-nu file cheytha peru achaar-ine protect cheyyanamennilla: kachavadam cheyyunna oro class-ilum file cheyyanam.")

duo("tmd004", "salon_clinic", "B", "salon", "എതിരാളിയുടെ പുതിയ ബ്രാൻഡ്.\nനമ്മുടെ പേരിൽ നിന്ന്\nഒരക്ഷരം മാത്രം വ്യത്യാസം", [
 ("A","wide","വിനീതേ, ട്രേഡ്മാർക്ക് ജേണലിൽ ഒരു പേര് കണ്ടു. നമ്മുടെ സലൂണിന്റെ പേരിൽ ഒരക്ഷരം മാത്രം മാറ്റം."),
 ("V","V","സോണിയ ചേച്ചി, അവർ ഫയൽ ചെയ്തു കഴിഞ്ഞല്ലോ. ഇനി എന്ത് ചെയ്യാൻ?"),
 ("A","A","ജേണലിൽ വന്ന് 4 മാസത്തിനുള്ളിൽ ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം."),
 ("V","V","4 മാസം കഴിഞ്ഞാലോ?"),
 ("A","wide","ഓപ്പോസിഷന്റെ സമയം കഴിയും. അതുകൊണ്ട് ജേണൽ ഇടയ്ക്കിടെ നോക്കണം."),
 ("V","wide","കത്രിക നമ്മുടെ കയ്യിൽ, സമയം ജേണലിന്റെ കയ്യിൽ.")],
 "ജേണലിൽ വന്നാൽ\n4 മാസം മാത്രം", CTA_BRAND, theme="new",
 cap_ml="നിങ്ങളുടെ ബ്രാൻഡിനോട് സാമ്യമുള്ള പേര് ട്രേഡ്മാർക്ക് ജേണലിൽ വന്നാൽ 4 മാസത്തിനുള്ളിൽ ഓപ്പോസിഷൻ ഫയൽ ചെയ്യാം. സലൂൺ, ക്ലിനിക്ക് ബ്രാൻഡുകൾ ജേണൽ ശ്രദ്ധിക്കണം.",
 cap_en="A rival files a salon name one letter away from yours. Once it is published in the Trade Marks Journal, you have 4 months to file an opposition. Have you ever checked the journal for look-alike names?",
 cap_mg="Ningalude brand-nodu saamyamulla peru trademark journal-il vannaal 4 maasathinullil opposition file cheyyaam. Salon, clinic brands journal shraddhikkanam.")

duo("tmd005", "app_founder", "A", "hostel", "ട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ.\nമെയിൽ കിടന്നത്\nസ്പാം ഫോൾഡറിൽ", [
 ("A","wide","സഞ്ജൂ, നമ്മുടെ ആപ്പിന്റെ ട്രേഡ്മാർക്കിന് ഒബ്ജക്ഷൻ വന്നിട്ടുണ്ട്. മെയിൽ സ്പാമിൽ കിടക്കുകയായിരുന്നു."),
 ("V","V","എന്ന് വന്നതാ?"),
 ("A","A","മൂന്നാഴ്ച മുമ്പ്."),
 ("V","V","ഒബ്ജക്ഷന് 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. ഇനി ഒരാഴ്ചയേ ബാക്കിയുള്ളൂ."),
 ("A","wide","ഇന്ന് തന്നെ മറുപടി തയ്യാറാക്കാം. ഇനി സ്പാം ഫോൾഡറും ദിവസവും നോക്കണം."),
 ("V","wide","കോഡിലെ ബഗ് നമ്മൾ കാണും, മെയിലിലെ ബഗ് കാണില്ല.")],
 "ഒബ്ജക്ഷൻ വന്നാൽ\n30 ദിവസം", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് അപേക്ഷയ്ക്ക് ഒബ്ജക്ഷൻ വന്നാൽ 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം. ആപ്പ് ഫൗണ്ടർമാർ മെയിലും സ്പാം ഫോൾഡറും ശ്രദ്ധിക്കണം.",
 cap_en="An app founder finds a trademark objection three weeks late, in the spam folder. A reply to an objection is due within 30 days. Who checks your trademark emails?",
 cap_mg="Trademark application-nu objection vannaal 30 divasathinullil marupadi kodukkanam. App founders mail-um spam folder-um shraddhikkanam.")

lst("tml001", "d2c_brand", "B", "ബ്രാൻഡിനെക്കുറിച്ച്\nഎല്ലാവരും വിശ്വസിക്കുന്ന\n3 തെറ്റുകൾ", [
 ("കമ്പനി പേര് = ബ്രാൻഡ്", "കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. ട്രേഡ്മാർക്ക് വേറെ."),
 ("ഫയൽ ചെയ്താൽ R", "ഫയൽ ചെയ്താൽ TM. R ചിഹ്നം രജിസ്ട്രേഷന് ശേഷം മാത്രം."),
 ("ഒരിക്കൽ മതി", "രജിസ്ട്രേഷൻ 10 വർഷത്തേക്ക്. പിന്നെ പുതുക്കണം.")],
 "ഏതാണ് നിങ്ങൾ\nവിശ്വസിച്ചിരുന്നത്?", CTA_BRAND, theme="faq",
 cap_ml="ബ്രാൻഡിനെക്കുറിച്ചുള്ള 3 തെറ്റുകൾ: കമ്പനി പേര് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല, R ചിഹ്നം രജിസ്ട്രേഷന് ശേഷം മാത്രം, ട്രേഡ്മാർക്ക് 10 വർഷം കഴിഞ്ഞ് പുതുക്കണം. ഏതാണ് നിങ്ങൾ വിശ്വസിച്ചിരുന്നത്: 1, 2, 3?",
 cap_en="Three trademark myths: a company name does not protect a brand, the R symbol comes only after registration, and a registration lasts 10 years before renewal. Which one did you believe: 1, 2 or 3?",
 cap_mg="Brand-ne kurichulla 3 thettukal: company peru brand protect cheyyilla, R symbol registration-nu shesham maathram, trademark 10 varsham kazhinju puthukkanam. Ethaanu ningal vishvasichirunnathu: 1, 2, 3?")
