# Trademark batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_TM. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

duo("tm001", "copied_brand", "A", "ferry", "18 വർഷം ഒരേ പേര്.\nഇന്ന് അതേ പേരിൽ\nവേറൊരു ബോട്ട്", [
 ("A","wide","ടോണി, ജെട്ടിയിൽ അതേ 'നീലത്താമര' ബോർഡ് വെച്ച് വേറൊരു ബോട്ട്! 18 വർഷം നമ്മൾ ഓടിച്ച പേരാ."),
 ("V","V","ചേച്ചീ, ആ പേര് നമ്മൾ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തിട്ടുണ്ടോ?"),
 ("A","A","കമ്പനി രജിസ്ട്രേഷൻ ഉണ്ടല്ലോ. അത് പോരേ?"),
 ("V","wide","പോരാ. കമ്പനി പേര് കിട്ടിയാൽ ബ്രാൻഡ് സുരക്ഷിതമാകില്ല. ട്രേഡ് മാർക്സ് രജിസ്ട്രിയിൽ നമ്മുടെ ക്ലാസിൽ ഫയൽ ചെയ്യണം."),
 ("A","A","ഫയൽ ചെയ്താൽ?"),
 ("V","wide","അന്ന് മുതൽ TM. രജിസ്റ്റർ ആയാലേ R. 18 വർഷം കാത്തു, ഇനി ഒരു ദിവസം കൂടി വൈകരുത്.")],
 "കമ്പനി പേര് കിട്ടിയാൽ\nബ്രാൻഡ് സേഫ് അല്ല", CTA_TRADEMARK, theme="crm",
 cap_ml="18 വർഷം ഓടിച്ച ബോട്ട് ടൂർ പേര് ഇപ്പോൾ വേറൊരാൾ ഉപയോഗിക്കുന്നു. കമ്പനി പേര് അപ്രൂവ് ആയാലും ബ്രാൻഡ് സംരക്ഷിക്കപ്പെടില്ല; ട്രേഡ്മാർക്ക് നിങ്ങളുടെ ക്ലാസിൽ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ ബ്രാൻഡ് പേര് ട്രേഡ്മാർക്ക് ചെയ്തോ?",
 cap_en="A Kerala boat tour operator used one brand name for 18 years, and now a rival boat carries the same name. A company name approval does not protect a brand: file a trademark in the class you trade in. TM after filing, R only after registration. Is your brand name filed?",
 cap_mg="18 varsham odicha boat tour peru ippo vere oraal use cheyyunnu. Company name approve aayaalum brand safe alla; trademark ningalude class-il file cheyyanam. Ningalude brand peru trademark cheytho?")

chat("tm003", "d2c_brand", "A", "5,000 പാക്കറ്റിൽ\nലോഗോ പ്രിന്റ് ചെയ്തു.\nപേര് ആരുടേത്?", ("ദേവിക", "ജിഷ്ണു"), [
 (0,"ജിഷ്ണു, ചിപ്സ് പാക്കറ്റ് 5,000 എണ്ണം പ്രിന്റ് ആയി! ലോഗോ കിടു."),
 (1,"ആ പേര് ട്രേഡ്മാർക്ക് സെർച്ച് ചെയ്തോ? വേറെ ആരെങ്കിലും മുമ്പേ ഫയൽ ചെയ്തിട്ടുണ്ടോ?"),
 (0,"ഇല്ല... അത് വേണോ?"),
 (1,"വേണം. ഫയൽ ചെയ്ത ശേഷമേ TM ഇടാവൂ. ഒബ്ജക്ഷൻ വന്നാൽ 30 ദിവസത്തിനുള്ളിൽ മറുപടി കൊടുക്കണം."),
 (0,"അപ്പോ പ്രിന്റ് ആദ്യം, പേപ്പർ പിന്നെ എന്ന് ചെയ്തത് തെറ്റി."),
 (1,"അതെ. ആദ്യം പേര്, പിന്നെ പാക്കറ്റ്.")],
 "ആദ്യം ട്രേഡ്മാർക്ക്,\nപിന്നെ പ്രിന്റ്", CTA_TRADEMARK, theme="crm",
 cap_ml="ബ്രാൻഡ് പേര് പരിശോധിക്കാതെ 5,000 ചിപ്സ് പാക്കറ്റിൽ ലോഗോ പ്രിന്റ് ചെയ്തു. പ്രിന്റിന് മുമ്പ് ട്രേഡ്മാർക്ക് സെർച്ചും ഫയലിംഗും; TM ഫയൽ ചെയ്ത ശേഷം മാത്രം, ഒബ്ജക്ഷന് 30 ദിവസത്തിൽ മറുപടി.",
 cap_en="A snack brand printed its logo on 5,000 packets before checking the name. Search and file the trademark before you print: use TM only after filing, and reply to an objection within 30 days. Did you check your brand name before printing?",
 cap_mg="Brand peru check cheyyaathe 5,000 chips packet-il logo print cheythu. Print-nu munpu trademark search-um filing-um; TM file cheytha shesham maathram, objection-nu 30 divasathil marupadi.")
