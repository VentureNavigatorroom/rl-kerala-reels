# Web tips 01 (27 Nov): tip reels as duo3d scenes (not lists). theme="tip". Facts only from topics.FACTS_WEB.
# Our service: never a price, instalment amount or delivery date; never promise rankings or sales.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_WEBSITE, CTA_WEBPLAN = topics.CTA_WEBSITE, topics.CTA_WEBPLAN

duo("wbt001", "no_website", "B", "akshaya", "വെബ്സൈറ്റ് ടീമിനെ\nവിളിക്കും മുമ്പ്\nഈ 3 കാര്യം", [
 ("A","wide","രമേശേ, വെബ്സൈറ്റ് ടീമിനെ വിളിക്കും മുമ്പ് മൂന്ന് കാര്യം റെഡി ആക്കിക്കോ."),
 ("V","V","എന്തൊക്കെ, സുധേച്ചീ?"),
 ("A","A","ഒന്ന്, എന്ത് വിൽക്കുന്നു, ആർക്ക്. രണ്ട്, നിങ്ങളുടെ യഥാർത്ഥ ഫോട്ടോകൾ. മൂന്ന്, ബിസിനസ് പേരിൽ ഡൊമെയ്നും ശരിയായ ഫോൺ നമ്പറും."),
 ("V","V","അത് റെഡി ആണെങ്കിൽ കോളിൽ മാസ തവണ പ്ലാനും കൃത്യമായി ചോദിക്കാം."),
 ("A","wide","തയ്യാറായി വിളിച്ചാൽ, പകുതി പണി കഴിഞ്ഞു.")],
 "തയ്യാറായി വിളിക്കൂ,\nപകുതി പണി കഴിഞ്ഞു", CTA_WEBPLAN, theme="tip",
 cap_ml="വെബ്സൈറ്റ് ടീമിനെ വിളിക്കും മുമ്പ് മൂന്ന് കാര്യം റെഡി ആക്കൂ: എന്ത് വിൽക്കുന്നു, ആർക്ക്; നിങ്ങളുടെ യഥാർത്ഥ ഫോട്ടോകൾ; ബിസിനസ് പേരിൽ ഡൊമെയ്നും ശരിയായ ഫോൺ നമ്പറും. മാസ തവണയായി അടയ്ക്കാം; എത്ര എന്ന് ടീം കോളിൽ കൃത്യമായി പറയും. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് ഇനിയും റെഡി ആകാത്തത്?",
 cap_en="Before you call a website team, get three things ready: what you sell and to whom, real photos of your work, and a domain in your business's name with the right phone number. You can pay in monthly parts; the team gives the exact quote on a call. Which of the three is still missing for you?",
 cap_mg="Website team-ine vilikkum mumpu moonnu kaaryam ready aakku: enthu vilkkunnu, aarkku; ningalude real photos; business perilu domain-um shariyaaya phone number-um. Monthly parts aayi adakkaam; ethra ennu team call-il krithyamaayi parayum. Ithil ethaanu ningalkku iniyum ready aakaathathu?")

duo("wbt002", "service_business", "B", "photocopy", "സ്വന്തം സൈറ്റ്\nഫോണിൽ അവസാനം\nതുറന്നത് എപ്പോൾ?", [
 ("A","wide","ഉണ്ണീ, സ്വന്തം വെബ്സൈറ്റ് ഫോണിൽ അവസാനം തുറന്നു നോക്കിയത് എപ്പോഴാ?"),
 ("V","V","ഉണ്ടാക്കിയ ദിവസം. പിന്നെ നോക്കിയിട്ടില്ല."),
 ("A","A","മാസത്തിൽ ഒരിക്കൽ നോക്കൂ: പെട്ടെന്ന് തുറക്കുന്നുണ്ടോ? വാട്സ്ആപ്പ് ബട്ടൺ പ്രവർത്തിക്കുന്നുണ്ടോ? നമ്പർ ഇപ്പോഴത്തേതാണോ?"),
 ("V","V","മൂന്ന് ചോദ്യം, രണ്ട് മിനിറ്റ്. അത് ഞാൻ ചെയ്യാം."),
 ("A","wide","കസ്റ്റമർ കാണുന്നത് നിങ്ങളും കാണണം.")],
 "കസ്റ്റമർ കാണുന്നത്\nനിങ്ങളും കാണണം", CTA_WEBSITE, theme="tip",
 cap_ml="മാസത്തിൽ ഒരിക്കൽ സ്വന്തം വെബ്സൈറ്റ് ഫോണിൽ തുറന്ന് ഈ മൂന്ന് ചോദ്യം ചോദിക്കൂ: പെട്ടെന്ന് തുറക്കുന്നുണ്ടോ? വാട്സ്ആപ്പ് ബട്ടൺ പ്രവർത്തിക്കുന്നുണ്ടോ? നമ്പറും അഡ്രസും ഇപ്പോഴത്തേതാണോ? രണ്ട് മിനിറ്റ് മതി. നിങ്ങളുടെ സൈറ്റ് അവസാനം ഫോണിൽ നോക്കിയത് എപ്പോൾ?",
 cap_en="Once a month, open your own website on a phone and ask three questions: does it load fast, does the WhatsApp button work, are the number and address current? It takes two minutes. When did you last check your site on a phone?",
 cap_mg="Maasathil orikkal swantham website phone-il thurannu ee moonnu chodyam chodikku: pettennu thurakkunnundo? WhatsApp button work cheyyunnundo? Number-um address-um ippozhathethaano? Randu minute mathi. Ningalude site avasaanam phone-il nokkiyathu eppol?")
