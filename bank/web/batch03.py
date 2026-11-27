# Tech development (web, widened 28 Nov): apps, MVPs, software. Business-first angle; monthly parts; never a price, instalment, timeline or promised result.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_WEBSITE, CTA_WEBPLAN = topics.CTA_WEBSITE, topics.CTA_WEBPLAN

duo('wbd101', 'app_idea', 'A', 'office', 'ആപ്പ് ഉണ്ടാക്കി.\nആരും ഉപയോഗിച്ചില്ല.\nകാരണം?', [('A', 'wide', 'രാഹുലേ, കഴിഞ്ഞ വർഷം ഒരു ഡെവലപ്പറെ വെച്ച് ആപ്പ് ഉണ്ടാക്കി. ഡൗൺലോഡ് ആരും ചെയ്തില്ല.'), ('V', 'V', 'നേഹ, ആപ്പ് എന്ത് പ്രശ്നം തീർക്കുന്നു എന്ന് ആദ്യം ചോദിച്ചിരുന്നോ?'), ('A', 'A', 'ഇല്ല. ഫീച്ചറുകൾ മാത്രം ലിസ്റ്റ് ചെയ്തു.'), ('V', 'V', 'കോഡ് എഴുതും മുമ്പ് ബിസിനസ് മനസ്സിലാക്കണം: ആർ, എന്തിന്, എങ്ങനെ പണം വരും.'), ('A', 'wide', 'ഡെവലപ്പർ ചോദിച്ചതേ ഉണ്ടാക്കൂ. ബിസിനസ് അറിയുന്നവർ ശരിയായത് ഉണ്ടാക്കും.'), ('V', 'wide', 'ഫീച്ചർ അല്ല, പ്രശ്നം ആദ്യം.')],
 'ഫീച്ചർ അല്ല,\nപ്രശ്നം ആദ്യം', CTA_WEBPLAN, theme='crm',
 cap_ml='ആപ്പ് ഉണ്ടാക്കും മുമ്പ് ബിസിനസ് മനസ്സിലാക്കണം: ആർക്ക് വേണ്ടി, ഏത് പ്രശ്നം, എങ്ങനെ വരുമാനം. ബിസിനസ് അറിയുന്ന ടീമിനൊപ്പം ഉണ്ടാക്കാം, മാസ തവണയായി അടയ്ക്കാം. നിങ്ങളുടെ ആപ്പ് ഏത് പ്രശ്നം തീർക്കും?',
 cap_en='Last year he paid a developer to build an app, and nobody downloaded it. Before any code: who is it for, which problem does it solve, and how does it earn? Build with a team that understands business, and pay in monthly parts. What problem will your app solve?',
 cap_mg='App undaakkum mumpu business manassilaakkanam: aarkku vendi, ethu prashnam, engane varumaanam. Business ariyunna team-odoppam undaakkaam, maasa thavanayaayi adaykkaam. Ningalude app ethu prashnam theerkkum?')

duo('wbd102', 'mvp_founder', 'B', 'library', 'എല്ലാ ഫീച്ചറും\nഒന്നിച്ച് വേണം.\nഅവിടെയാണ് തെറ്റ്', [('A', 'wide', 'അനൂപേ, എന്റെ ആപ്പിൽ ചാറ്റ്, പേയ്മെന്റ്, ഡാഷ്ബോർഡ്, എല്ലാം ആദ്യ വേർഷനിൽ തന്നെ വേണം.'), ('V', 'V', 'ഗ്രീഷ്മേ, എല്ലാം ഒന്നിച്ച് ഉണ്ടാക്കിയാൽ ഉപയോക്താക്കൾ ശരിക്കും എന്ത് ഉപയോഗിക്കുന്നു എന്ന് അറിയില്ല.'), ('A', 'A', 'അപ്പോ എന്ത് ചെയ്യണം?'), ('V', 'V', 'പ്രധാന പ്രശ്നം തീർക്കുന്ന ചെറിയ വേർഷൻ ആദ്യം. MVP. പിന്നെ ഫീഡ്ബാക്ക് നോക്കി വളർത്തുക.'), ('A', 'wide', 'ചെറുതായി തുടങ്ങി, ശരിയായി വളരാം.'), ('V', 'wide', 'ആദ്യം ചെറുത്, പിന്നെ ശരിയായത്.')],
 'ആദ്യം ചെറുത്,\nപിന്നെ ശരിയായത്', CTA_WEBPLAN, theme='faq',
 cap_ml='പുതിയ ആപ്പിന് എല്ലാ ഫീച്ചറും ഒന്നിച്ച് വേണ്ട. പ്രധാന പ്രശ്നം തീർക്കുന്ന ചെറിയ വേർഷൻ (MVP) ആദ്യം, പിന്നെ ഫീഡ്ബാക്ക് നോക്കി വളർത്തുക. നിങ്ങളുടെ ആപ്പിന്റെ ഒരേയൊരു പ്രധാന ജോലി എന്താണ്?',
 cap_en='A founder wants chat, payments and dashboards all in version one. Start with the smallest version that solves the main problem (an MVP), then grow it from real feedback. What is the one job your app must do?',
 cap_mg='Puthiya app-inu ella feature-um onnichu venda. Pradhaana prashnam theerkkunna cheriya version (MVP) aadyam, pinne feedback nokki valarthuka. Ningalude app-inte orey oru pradhaana joli enthaanu?')

duo('wbd103', 'ops_software', 'A', 'hospital', 'ബുക്കിംഗ് എക്സൽ ഷീറ്റിൽ,\nബിൽ വാട്സാപ്പിൽ,\nസ്റ്റോക്ക് ഓർമയിൽ', [('A', 'wide', 'ജോസഫേ, ക്ലിനിക്കിൽ ബുക്കിംഗ് എക്സൽ ഷീറ്റിൽ, ബിൽ വാട്സാപ്പിൽ. ദിവസവും എന്തെങ്കിലും വിട്ടുപോകുന്നു.'), ('V', 'V', 'ലക്ഷ്മീ, നിങ്ങളുടെ ജോലി രീതിക്ക് ചേരുന്ന ഒരു ലളിതമായ സോഫ്റ്റ്\u200cവെയർ ആലോചിച്ചോ?'), ('A', 'A', 'വലിയ കമ്പനികൾക്ക് മാത്രമല്ലേ അത്?'), ('V', 'V', 'അല്ല. ആദ്യം ബിസിനസ് എങ്ങനെ നടക്കുന്നു എന്ന് നോക്കി, ഏറ്റവും സമയം കളയുന്നത് ആദ്യം ശരിയാക്കാം.'), ('A', 'wide', 'ഒറ്റയടിക്ക് വലിയ തുക വേണ്ട, മാസ തവണയായി അടയ്ക്കാം.'), ('V', 'wide', 'ബിസിനസിന് ചേരുന്ന ടൂൾ, ടൂളിന് ചേരുന്ന ബിസിനസ് അല്ല.')],
 'ബിസിനസിന് ചേരുന്ന\nസോഫ്റ്റ്\u200cവെയർ', CTA_WEBPLAN, theme='new',
 cap_ml='എക്സൽ ഷീറ്റും വാട്സാപ്പും കൊണ്ട് ബിസിനസ് നടത്തി കാര്യങ്ങൾ വിട്ടുപോകുന്നുണ്ടോ? ബിസിനസ് രീതി മനസ്സിലാക്കി ചേരുന്ന സോഫ്റ്റ്\u200cവെയർ ഉണ്ടാക്കാം, മാസ തവണയായി അടയ്ക്കാം. നിങ്ങൾക്ക് ഏറ്റവും സമയം പോകുന്നത് എവിടെ?',
 cap_en='A clinic runs bookings on Excel and bills on WhatsApp, and something slips every day. Software built around how your business actually works fixes the biggest time-waster first, and you can pay in monthly parts. Where do you lose the most time?',
 cap_mg='Excel-um WhatsApp-um kondu business nadathi kaaryangal vittupokunnundo? Business reethi manassilaakki cherunna software undaakkaam, maasa thavanayaayi adaykkaam. Ningalkku ettavum samayam pokunnathu evide?')

duo('wbd104', 'insta_only', 'B', 'rooftop', 'ഡെവലപ്പർ ചോദിച്ചു:\n"എന്ത് വേണം?"\nഅതാണ് പ്രശ്നം', [('A', 'wide', 'ശ്യാമേ, ഡെവലപ്പർ ചോദിച്ചു എന്ത് വേണം എന്ന്. എനിക്ക് അറിയില്ലായിരുന്നു.'), ('V', 'V', "ആര്യേ, ശരിയായ ചോദ്യം 'ബിസിനസിന് എന്ത് വേണം' എന്നാണ്. കസ്റ്റമർ, പേയ്മെന്റ്, KYC, വളർച്ച."), ('A', 'A', 'അതൊക്കെ ഡെവലപ്പർ ചിന്തിക്കില്ലേ?'), ('V', 'V', 'എല്ലാവരും ചിന്തിക്കില്ല. ബിസിനസ് അറിയുന്നവർ ആ ചോദ്യങ്ങൾ ആദ്യം ചോദിക്കും.'), ('A', 'wide', 'അതാണ് വ്യത്യാസം. കോഡ് മാത്രമല്ല, ബിസിനസും.'), ('V', 'wide', 'ആര് ഉണ്ടാക്കുന്നു എന്നതും പ്രധാനം.')],
 'കോഡ് മാത്രമല്ല,\nബിസിനസും', CTA_WEBSITE, theme='faq',
 cap_ml="വെബ്സൈറ്റോ ആപ്പോ ഉണ്ടാക്കുമ്പോൾ ശരിയായ ചോദ്യം 'ബിസിനസിന് എന്ത് വേണം' എന്നാണ്: കസ്റ്റമർ, പേയ്മെന്റ്, KYC, വളർച്ച. ബിസിനസ് അറിയുന്ന ടീമിനൊപ്പം ഉണ്ടാക്കൂ. നിങ്ങളുടെ ബിസിനസ് എന്താണ്?",
 cap_en="The developer asked what she wanted, and she didn't know. The right question is what the business needs: customers, payments, KYC and growth. Build your website or app with a team that understands business, not just code. What does your business do?",
 cap_mg="Website-o app-o undaakkumbol shariyaaya chodyam 'business-inu enthu venam' ennaanu: customer, payment, KYC, valarcha. Business ariyunna team-odoppam undaakku. Ningalude business enthaanu?")

