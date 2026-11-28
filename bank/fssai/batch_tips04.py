# Tips and tricks 04 (28 Nov night): tips written as duo3d scenes, not lists (26 Nov review). theme="tip". Facts only from topics.FACTS_FSSAI (2026 limits). No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD

# tip: three checks before listing a kitchen on a delivery app
duo("fst018", "cloud_kitchen", "B", "mobileshop", "ഡെലിവറി ആപ്പിൽ\nലിസ്റ്റ് ചെയ്യും മുമ്പ്\n3 FSSAI ചെക്ക്", [
 ("A","wide","ഫഹദേ, അടുക്കള ആപ്പിൽ ഇടും മുമ്പ് മൂന്ന് ചെക്ക്. ആപ്പ് ആദ്യം ചോദിക്കുന്നത് FSSAI നമ്പറാ."),
 ("A","A","ഒന്ന്: നമ്പർ നിങ്ങളുടെ സ്വന്തം അടുക്കളയുടേതാണോ? കടം വാങ്ങിയ നമ്പർ വേണ്ട."),
 ("V","V","രണ്ട്: FoSCoS-ൽ കാറ്റഗറി. 1.5 കോടി വരെ സാധാരണ രജിസ്ട്രേഷൻ, ചില ബിസിനസിന് ലൈസൻസ്."),
 ("A","A","മൂന്ന്: പാക്ക് ചെയ്ത് അയക്കുന്നതിൽ 14 അക്ക നമ്പർ പ്രിന്റ് ചെയ്തോ?"),
 ("V","wide","സ്വന്തം നമ്പർ, ശരിയായ കാറ്റഗറി, പാക്കറ്റിൽ പ്രിന്റ്.")],
 "ലിസ്റ്റിംഗിന് മുമ്പ്\nനമ്പർ റെഡി", CTA_FOOD, theme="tip",
 cap_ml="ഡെലിവറി ആപ്പിൽ അടുക്കള ലിസ്റ്റ് ചെയ്യും മുമ്പ് 3 ചെക്ക്: FSSAI നമ്പർ സ്വന്തം അടുക്കളയുടേതാണോ, FoSCoS-ൽ കാറ്റഗറി ശരിയാണോ (1.5 കോടി വരെ സാധാരണ രജിസ്ട്രേഷൻ), പാക്ക് ചെയ്ത ഫുഡിൽ 14 അക്ക നമ്പർ ഉണ്ടോ. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് ബാക്കി?",
 cap_en="Three checks before you list a kitchen on a delivery app: is the FSSAI number your own kitchen's, is your category right on FoSCoS (up to 1.5 crore usually means registration), and is the 14-digit number printed on packed food? Which one is still pending for you?",
 cap_mg="Delivery app-il adukkala list cheyyum mumpu 3 check: FSSAI number swantham adukkalayudethaano, FoSCoS-il category shariyaano (1.5 crore vare saadhaarana registration), pack cheytha food-il 14 akka number undo. Ithil ethaanu ningalkku baakki?")

# tip: a year-end FSSAI check (calendar reminder)
duo("fst019", "packaged_food", "B", "photocopy", "വർഷം തീരും മുമ്പ്\nFSSAI-യിൽ\n3 മിനിറ്റ് ചെക്ക്", [
 ("A","wide","ഉണ്ണീ, ഡിസംബറിൽ ഫുഡ് ബിസിനസുകാർ ചെയ്യേണ്ട ഒരു മൂന്ന് മിനിറ്റ് FSSAI ചെക്ക്."),
 ("A","A","ഒന്ന്: ലൈസൻസ് കിട്ടിയ തീയതി. 2026 ഏപ്രിൽ 1-ന് മുമ്പാണെങ്കിൽ FoSCoS-ൽ കാലാവധി നോക്കൂ."),
 ("V","V","രണ്ട്: ഈ വർഷത്തെ ടേൺഓവർ. 1.5 കോടി കടന്നോ? 50 കോടി കടന്നോ? ലെവൽ മാറിയോ?"),
 ("A","A","മൂന്ന്: FSSAI-ക്കുള്ള വാർഷിക അടവും വാർഷിക റിട്ടേണും സമയത്ത് ആയോ?"),
 ("V","wide","തീയതി, ടേൺഓവർ, അടവ്. മൂന്നും നോക്കി പുതുവർഷം.")],
 "തീയതി, ടേൺഓവർ,\nഅടവ്", CTA_FSSAI, theme="tip",
 cap_ml="വർഷാവസാനം FSSAI-യിൽ 3 ചെക്ക്: ലൈസൻസ് 2026 ഏപ്രിൽ 1-ന് മുമ്പ് കിട്ടിയതാണെങ്കിൽ FoSCoS-ൽ കാലാവധി, ഈ വർഷത്തെ ടേൺഓവർ (1.5 കോടി / 50 കോടി), FSSAI-ക്കുള്ള വാർഷിക അടവും വാർഷിക റിട്ടേണും. ഫുഡ് ബിസിനസ് ചെയ്യുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="A 3-minute FSSAI check before the year ends: if your licence was issued before 1 April 2026, its expiry on FoSCoS; this year's turnover against 1.5 crore and 50 crore; and whether the yearly payment and annual return are done. Send this to a friend who runs a food business.",
 cap_mg="Varshaavasaanam FSSAI-yil 3 check: licence 2026 April 1-nu mumpu kittiyathaanenkil FoSCoS-il expiry, ee varshathe turnover (1.5 crore / 50 crore), FSSAI-kkulla annual payment-um annual return-um. Food business cheyyunna oraalkku ithu ayakku.")
