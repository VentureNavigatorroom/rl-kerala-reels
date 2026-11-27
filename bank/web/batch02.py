# web batch 02 (27 Nov evening refill): 3D duo reels. Max 6 lines, painful moment first, payoff by line 4-5.
# OUR service: never a price, instalment amount or delivery date; never promise rankings or sales. Facts only from topics.FACTS_WEB.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_WEBSITE, CTA_WEBPLAN = topics.CTA_WEBSITE, topics.CTA_WEBPLAN

# faq: a handloom unit's free site lives on someone else's address, not a domain in its own name
duo("wbd006", "no_website", "B", "handloom", "സൈറ്റിന്റെ അഡ്രസിൽ\nനമ്മുടെ പേരിന് മുമ്പ്\nവേറൊരു കമ്പനി", [
 ("A","wide","കുമാറേ, ബാംഗ്ലൂരിലെ ബയർക്ക് നമ്മുടെ കൈത്തറി സൈറ്റിന്റെ ലിങ്ക് അയച്ചു. അവർ ചോദിച്ചു, ഇത് നിങ്ങളുടെ സ്വന്തം സൈറ്റ് ആണോ എന്ന്."),
 ("V","V","ലീലേ, അത് ഫ്രീ ആയി കിട്ടിയ പേജ് അല്ലേ. ലിങ്കിൽ ആ കമ്പനിയുടെ പേരാണ് ആദ്യം."),
 ("A","A","അതുകൊണ്ടാണ് സംശയം. ബിസിനസിന്റെ പേരിൽ ഒരു ഡൊമെയ്ൻ വേണം. അത് നമ്മുടേതായിരിക്കണം."),
 ("V","V","ശരി. നമ്മുടെ കൈത്തറിയുടെ പേര് തന്നെ ലിങ്കിൽ വരട്ടെ."),
 ("A","wide","ലിങ്കിൽ നമ്മുടെ പേര്, അപ്പോൾ വിശ്വാസം.")],
 "ബിസിനസ് പേരിൽ\nസ്വന്തം ഡൊമെയ്ൻ", CTA_WEBSITE, theme="faq",
 cap_ml="നിങ്ങളുടെ വെബ്സൈറ്റ് ലിങ്കിൽ ആദ്യം വരുന്നത് വേറൊരു കമ്പനിയുടെ പേരാണോ? ബിസിനസിന്റെ പേരിൽ സ്വന്തം ഡൊമെയ്ൻ ഉണ്ടെങ്കിൽ ബയർക്കും കസ്റ്റമർക്കും വിശ്വാസം കൂടും, ഓർക്കാനും എളുപ്പം. നിങ്ങളുടെ ലിങ്കിൽ ആരുടെ പേരാണ്?",
 cap_en="A handloom unit sends its site link to a Bangalore buyer, who asks if it is really their own site: the link starts with the free builder's name. A domain in the business's own name builds trust and is easier to remember. Whose name is in your link?",
 cap_mg="Ningalude website link-il aadyam varunnathu veroru company-yude peraano? Business-inte peril swantham domain undenkil buyer-kkum customer-kkum viswaasam koodum, orkkaanum eluppam. Ningalude link-il aarude peraanu?")

# crm (expanding small manufacturer, invented): a rubber-products unit's site shows photos copied from the internet
duo("wbd007", "old_website", "B", "rubber", "ഡീലർ ചോദിച്ചു:\n\"ഈ ഫോട്ടോ നിങ്ങളുടെ\nഫാക്ടറിയിലേതാണോ?\"", [
 ("A","wide","തോമസേ, തമിഴ്നാട്ടിലെ ഡീലർ സൈറ്റ് നോക്കി വിളിച്ചു. ഫോട്ടോയിലെ ഫാക്ടറി നമ്മുടേതാണോ എന്ന് ചോദിച്ചു."),
 ("V","V","ജോയിച്ചായാ, അത് സൈറ്റ് ഉണ്ടാക്കിയപ്പോൾ ഇന്റർനെറ്റിൽ നിന്ന് എടുത്ത ഫോട്ടോ ആണ്."),
 ("A","A","അതാണ് പ്രശ്നം. നമ്മൾ ഉണ്ടാക്കുന്ന റബ്ബർ മാറ്റും നമ്മുടെ യൂണിറ്റും തന്നെ കാണിക്കണം."),
 ("V","V","നാളെ രാവിലെ യൂണിറ്റിലെ യഥാർത്ഥ ഫോട്ടോ എടുക്കാം. മെഷീനും സ്റ്റോക്കും ടീമും."),
 ("A","wide","കടം വാങ്ങിയ ഫോട്ടോ, കടം വാങ്ങിയ വിശ്വാസം.")],
 "നിങ്ങൾ ഉണ്ടാക്കുന്നത്\nനിങ്ങളുടെ ഫോട്ടോയിൽ", CTA_WEBSITE, theme="crm",
 cap_ml="വെബ്സൈറ്റിൽ ഇന്റർനെറ്റിൽ നിന്ന് എടുത്ത ഫോട്ടോ ആണോ? ബയർമാർ നോക്കുന്നത് നിങ്ങൾ ശരിക്കും ഉണ്ടാക്കുന്നതും വിൽക്കുന്നതും ആണ്. യൂണിറ്റിന്റെയും ഉൽപ്പന്നത്തിന്റെയും ടീമിന്റെയും യഥാർത്ഥ ഫോട്ടോ ഇടൂ. നിങ്ങളുടെ സൈറ്റിലെ ഫോട്ടോ ആരുടേതാണ്?",
 cap_en="A rubber-products unit gets a call from a dealer in Tamil Nadu: is the factory in the photos really yours? The site used pictures from the internet. Show real photos of what you make, your unit and your team. Whose photos are on your site?",
 cap_mg="Website-il internet-il ninnu edutha photo aano? Buyers nokkunnathu ningal sherikkum undaakkunnathum vilkkunnathum aanu. Unit-inteyum product-inteyum team-inteyum yathaartha photo idu. Ningalude site-ile photo aarudethaanu?")

# faq: "a website in monthly parts? how much a month?" (we never state an amount: the team quotes on a call)
duo("wbd008", "no_website", "B", "juiceshop", "വെബ്സൈറ്റിന്\nഒറ്റയടിക്ക് പൈസ വേണ്ട?\nമാസ തവണ?", [
 ("A","wide","നൗഷാദിക്കാ, ജ്യൂസ് കടയ്ക്ക് ഓർഡർ എടുക്കാൻ ഒരു വെബ്സൈറ്റ് വേണം. പക്ഷേ ഒറ്റയടിക്ക് വലിയ തുക ഇല്ല."),
 ("V","V","റസിയാ, മാസ ഭാഗങ്ങളായി അടയ്ക്കാവുന്ന രീതിയുണ്ട്. മുഴുവൻ തുക ആകുന്നതുവരെ മാസം തോറും."),
 ("A","A","അപ്പോ മാസം എത്ര വരും? എപ്പോൾ റെഡി ആകും?"),
 ("V","V","അത് ഓരോ പ്രോജക്റ്റിനും വേറെയാണ്. എന്ത് വേണം എന്ന് പറഞ്ഞാൽ ടീം കോളിൽ കൃത്യമായി പറയും."),
 ("A","wide","ആദ്യം എന്ത് വേണം എന്ന് ഉറപ്പിക്കാം, പിന്നെ കോൾ.")],
 "ആവശ്യം പറയൂ,\nടീം കോളിൽ പറയും", CTA_WEBPLAN, theme="faq",
 cap_ml="വെബ്സൈറ്റ് വേണം, പക്ഷേ ഒറ്റയടിക്ക് വലിയ തുക ഇല്ലേ? മുഴുവൻ തുക ആകുന്നതുവരെ മാസ ഭാഗങ്ങളായി അടയ്ക്കാം. തുക പ്രോജക്റ്റ് അനുസരിച്ചാണ്; എന്ത് വേണം എന്ന് പറഞ്ഞാൽ ടീം കോളിൽ കൃത്യമായി പറയും. നിങ്ങളുടെ സൈറ്റിൽ ആദ്യം വേണ്ടത് എന്താണ്?",
 cap_en="A juice shop owner wants a website for orders but has no big amount to pay at once. With us it can be paid in monthly parts until the total is paid. The amount depends on the project; tell the team what you need and they give the exact quote on a call. What would your site need first?",
 cap_mg="Website venam, pakshe ottayadikku valiya thuka ille? Muzhuvan thuka aakunnathu vare maasa bhaagangalaayi adaykkaam. Thuka project anusarichaanu; enthu venam ennu paranjaal team call-il kruthyamaayi parayum. Ningalude site-il aadyam vendathu enthaanu?")
