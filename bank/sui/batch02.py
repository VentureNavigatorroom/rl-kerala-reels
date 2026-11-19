# Startup India batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_SUI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

duo("ud005", "traditional_innovator", "A", "beach", "\"എന്റെ പുട്ട് കട\nസ്റ്റാർട്ടപ്പ് ആണോ?\"\nDPIIT നോക്കുന്നത്", [
 ("A","wide","നിഖിൽ, എന്റെ 20 തരം പുട്ട് കട ഹിറ്റ് ആണ്. DPIIT സ്റ്റാർട്ടപ്പ് റെക്കഗ്നിഷന് അപേക്ഷിച്ചാലോ?"),
 ("V","V","കട ആയതുകൊണ്ട് മാത്രം പോരാ. ഇന്നൊവേഷൻ, പ്രോസസ് മെച്ചപ്പെടുത്തൽ, അല്ലെങ്കിൽ സ്കെയിൽ ചെയ്യാവുന്ന മോഡൽ വേണം."),
 ("A","A","പുതിയ പ്രോസസിൽ റെഡി-ടു-കുക്ക് പുട്ട് മിക്സ്, കേരളം മുഴുവൻ ഫ്രാഞ്ചൈസി. അതാ പ്ലാൻ."),
 ("V","wide","അത് വേറെ കഥ. പക്ഷേ പ്രൊപ്രൈറ്റർഷിപ്പിന് കിട്ടില്ല. പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പോ വേണം."),
 ("A","A","അപ്പോ പുട്ടിനല്ല, ഐഡിയയ്ക്കാ റെക്കഗ്നിഷൻ."),
 ("V","wide","അതെ. പുട്ടിന് പീര. സ്റ്റാർട്ടപ്പിന് ഇന്നൊവേഷൻ.")],
 "കട അല്ല,\nഇന്നൊവേഷൻ നോക്കും", CTA_DPIIT, theme="faq",
 cap_ml="റെസ്റ്റോറന്റ് സ്റ്റാർട്ടപ്പ് ആണോ? DPIIT റെക്കഗ്നിഷന് ഇന്നൊവേഷനോ സ്കെയിൽ ചെയ്യാവുന്ന മോഡലോ വേണം; പ്രൊപ്രൈറ്റർഷിപ്പിന് കിട്ടില്ല. നിങ്ങളുടെ ബിസിനസിൽ എന്താണ് പുതുമ?",
 cap_en="Is a restaurant a startup? A Kerala puttu shop owner asks about DPIIT recognition. It needs innovation, a better product or process, or a scalable model, and a private limited company, LLP or registered partnership: a proprietorship can't be recognised. What's new in your business?",
 cap_mg="Restaurant startup aano? DPIIT recognition-nu innovation-o scale cheyyaavunna model-o venam; proprietorship-nu kittilla. Ningalude business-il enthaanu puthuma?")

duo("ud006", "tech_founder", "B", "gym", "DPIIT കിട്ടി.\nഅക്കൗണ്ടിൽ പൈസ\nവരുന്നതും നോക്കി", [
 ("A","wide","ജസ്റ്റിൻ, ഫിറ്റ്നസ് ട്രാക്കർ ആപ്പിന് DPIIT റെക്കഗ്നിഷൻ കിട്ടി! പൈസ എപ്പോ അക്കൗണ്ടിൽ വരും?"),
 ("V","V","റെക്കഗ്നിഷൻ പൈസ അല്ല. പല സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും അപേക്ഷിക്കാനുള്ള യോഗ്യതയാണ്."),
 ("A","A","അപ്പോ വേറെ ഗുണം ഒന്നുമില്ലേ?"),
 ("V","wide","ഉണ്ട്. പേറ്റന്റ് ഫയലിംഗിന് 80% റിബേറ്റ്, ട്രേഡ്മാർക്കിന് 50%, വേഗത്തിലുള്ള IP പരിശോധന."),
 ("A","A","ടാക്സ് ഹോളിഡേയോ?"),
 ("V","wide","അത് 80-IAC, വേറെ അപേക്ഷ. ജിമ്മിൽ ചേർന്നാൽ മസിൽ വരില്ല, വർക്കൗട്ട് ചെയ്യണം.")],
 "റെക്കഗ്നിഷൻ യോഗ്യതയാണ്,\nപൈസ അല്ല", CTA_BENEFITS, theme="faq",
 cap_ml="DPIIT റെക്കഗ്നിഷൻ കിട്ടിയാൽ പൈസ കിട്ടുമോ? ഇല്ല. സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും അപേക്ഷിക്കാനുള്ള യോഗ്യത, പേറ്റന്റിന് 80%, ട്രേഡ്മാർക്കിന് 50% റിബേറ്റ്. 80-IAC ടാക്സ് ഹോളിഡേ വേറെ അപേക്ഷ.",
 cap_en="Does DPIIT recognition put money in your account? No. It makes you eligible to apply for many schemes and tenders, gives an 80% rebate on patent filing and 50% on trademarks, and faster IP examination. The 80-IAC tax holiday is a separate application.",
 cap_mg="DPIIT recognition kittiyaal paisa kittumo? Illa. Schemes-num tenders-num apekshikkaanulla yogyatha, patent-nu 80%, trademark-nu 50% rebate. 80-IAC tax holiday vere application.")

duo("ud007", "traditional_innovator", "A", "tailor", "പുതിയ ഇന്നൊവേഷൻ.\nപക്ഷേ കമ്പനിക്ക്\n11 വയസ്സ്", [
 ("A","wide","മോഹനേട്ടാ, നമ്മുടെ കമ്പനി ഉണ്ടാക്കിയ ആന്റി-ബാക്ടീരിയൽ യൂണിഫോം തുണി പുതിയ ഐറ്റമാണ്. DPIIT കിട്ടില്ലേ?"),
 ("V","V","കമ്പനി തുടങ്ങിയിട്ട് 11 വർഷമായില്ലേ? ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷത്തിൽ താഴെ ആയിരിക്കണം. ഡീപ് ടെക്കിന് 20."),
 ("A","A","പ്രൊഡക്റ്റ് പുതിയതല്ലേ, അത് നോക്കില്ലേ?"),
 ("V","wide","പ്രൊഡക്റ്റ് പുതിയതായാലും കമ്പനിയുടെ പ്രായവും നോക്കും. അതാ നിയമം."),
 ("A","A","അപ്പോ 10 വർഷം ആകും മുമ്പ് അപേക്ഷിക്കേണ്ടതായിരുന്നു."),
 ("V","wide","അളവ് തെറ്റിയാൽ തുണി പാഴ്. വർഷം തെറ്റിയാൽ അവസരം പാഴ്.")],
 "10 വർഷം കഴിയും\nമുമ്പ് അപേക്ഷിക്കൂ", CTA_DPIIT, theme="new",
 cap_ml="പുതിയ ഉൽപ്പന്നം ഉണ്ടെങ്കിലും 11 വർഷം പഴക്കമുള്ള കമ്പനിക്ക് DPIIT റെക്കഗ്നിഷൻ കിട്ടില്ല. ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷത്തിനുള്ളിൽ (ഡീപ് ടെക്കിന് 20) അപേക്ഷിക്കണം. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര വയസ്സായി?",
 cap_en="A textile company with a new anti-bacterial uniform fabric asks about DPIIT recognition, but it was incorporated 11 years ago. Recognition is only for entities under 10 years old (20 for deep tech). How old is your company?",
 cap_mg="Puthiya product undenkilum 11 varsham pazhakkamulla company-kku DPIIT recognition kittilla. Incorporation muthal 10 varshathinullil (deep tech-nu 20) apekshikkanam.")
