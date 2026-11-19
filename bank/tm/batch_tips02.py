# Tips and tricks 02 (20 Nov, refill writer): one tip reel per topic per day. theme="tip". Facts only from topics.py FACTS_TM.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

lst('tmt004', 'app_founder', "B", 'ലോഞ്ചിന് മുമ്പ്\nബ്രാൻഡ്: ഈ ക്രമം\nതെറ്റിക്കരുത്', [('ഒന്ന്', 'കമ്പനി പേര് കിട്ടിയാൽ ബ്രാൻഡ് സുരക്ഷിതമായി എന്ന് കരുതരുത്.'), ('രണ്ട്', 'കച്ചവടം ചെയ്യുന്ന ക്ലാസിൽ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യൂ.'), ('മൂന്ന്', 'ഫയൽ ചെയ്ത ശേഷം ലോഞ്ച്, ലോഗോയിൽ TM.')],
 'ആദ്യം ഫയൽ\nപിന്നെ ലോഞ്ച്', CTA_TRADEMARK, theme="tip",
 cap_ml='ആപ്പ് ലോഞ്ചിന് മുമ്പ് ബ്രാൻഡ്: കമ്പനി പേര് ട്രേഡ്മാർക്ക് സംരക്ഷണം നൽകില്ല. ശരിയായ ക്ലാസിൽ ഫയൽ ചെയ്ത ശേഷം TM ഉപയോഗിക്കാം. നിങ്ങൾ ലോഞ്ചിന് എത്ര അടുത്താണ്?',
 cap_en='Before an app or product launch: a company name does not protect your brand. File the trademark in the class you trade in, then launch with the TM symbol. How close is your launch?',
 cap_mg='Launch-nu mumpu brand: company name trademark protection tharilla. Sheriyaya class-il file cheythittu TM upayogikkaam. Launch-nu ethra aduthaanu?')

lst('tmt005', 'salon_clinic', "B", 'സലൂണിനും\nക്ലിനിക്കിനും\nട്രേഡ്മാർക്ക്?', [('തെറ്റിദ്ധാരണ', 'ട്രേഡ്മാർക്ക് പാക്കറ്റ് ഉൽപ്പന്നങ്ങൾക്ക് മാത്രം എന്ന്.'), ('സത്യം', 'നാല്പത്തിയഞ്ച് ക്ലാസിൽ സേവനങ്ങൾക്കും ക്ലാസുകൾ ഉണ്ട്.'), ('ടിപ്പ്', 'നിങ്ങൾ നൽകുന്ന സേവനത്തിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യൂ.')],
 'ബോർഡിലെ പേരും\nഒരു ബ്രാൻഡാണ്', CTA_BRAND, theme="tip",
 cap_ml='സലൂൺ, ക്ലിനിക്, സ്പാ പോലുള്ള സർവീസ് ബിസിനസ്സുകൾക്കും ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യാം. നാല്പത്തിയഞ്ച് ക്ലാസുകളിൽ സേവനങ്ങൾക്കും ക്ലാസുണ്ട്. നിങ്ങളുടേത് പ്രോഡക്റ്റോ സർവീസോ?',
 cap_en='Salons, clinics and other service businesses can file a trademark too: the 45 classes include services. File in the class of the service you offer. Product or service?',
 cap_mg='Salon, clinic pole service business-num trademark file cheyyaam. 45 class-il service-num class undu. Ningaludethu product-o service-o?')

lst('tmt006', 'copied_brand', "B", 'ട്രേഡ്മാർക്ക്\nഒബ്ജക്ഷൻ വന്നോ?\nആദ്യം ഇത്', [('ഒബ്ജക്ഷൻ', 'അവസാന വാക്കല്ല, മറുപടി നൽകാനുള്ള അവസരമാണ്.'), ('സമയം', 'മുപ്പത് ദിവസത്തിനുള്ളിൽ മറുപടി നൽകണം.'), ('ട്രിക്ക്', 'ഫയൽ ചെയ്ത ഇമെയിലും സ്പാം ഫോൾഡറും ആഴ്ചയിൽ നോക്കൂ.')],
 'മിണ്ടാതിരുന്നാൽ\nഅവസരം പോകും', CTA_TRADEMARK, theme="tip",
 cap_ml='ട്രേഡ്മാർക്ക് ഒബ്ജക്ഷൻ കിട്ടിയാൽ പേടിക്കേണ്ട, പക്ഷേ മുപ്പത് ദിവസത്തിനുള്ളിൽ മറുപടി നൽകണം. അപേക്ഷയിലെ ഇമെയിൽ പതിവായി നോക്കൂ. നിങ്ങൾക്ക് ഒബ്ജക്ഷൻ വന്നിട്ടുണ്ടോ?',
 cap_en='Got a trademark objection? It is a chance to reply, not the end, but the reply is due within 30 days. Check the email on your application every week. Have you had one?',
 cap_mg='Trademark objection vannaal pedikkenda, pakshe 30 divasathinullil reply kodukkanam. Application-ile email pathivaayi nokku. Ningalkku objection vannittundo?')

lst('tmt007', 'food_brand', "B", 'പത്ത് വർഷം\nപഴയ ബ്രാൻഡ്?\nഇന്ന് ഒന്ന് നോക്കൂ', [('കാലാവധി', 'രജിസ്ട്രേഷൻ പത്ത് വർഷത്തേക്ക്.'), ('പുതുക്കൽ', 'പുതുക്കാം, പക്ഷേ ആരെങ്കിലും ഓർക്കണം.'), ('ട്രിക്ക്', 'രജിസ്ട്രേഷൻ തീയതി കലണ്ടറിൽ ഇടൂ, ഒരു വർഷം മുമ്പ് റിമൈൻഡർ.')],
 'ബ്രാൻഡ് പഴകും\nസംരക്ഷണം പുതുക്കണം', CTA_BRAND, theme="tip",
 cap_ml='ട്രേഡ്മാർക്ക് രജിസ്ട്രേഷൻ പത്ത് വർഷത്തേക്കാണ്, പിന്നെ പുതുക്കണം. പഴയ ബ്രാൻഡുകളുടെ തീയതി ഇന്ന് തന്നെ നോക്കൂ. നിങ്ങളുടെ ബ്രാൻഡിന് എത്ര വയസ്സായി?',
 cap_en='A trademark registration lasts 10 years and then must be renewed. Check the dates on your older brands today. How old is your brand?',
 cap_mg='Trademark registration 10 varshathekku, pinne puthukkanam. Pazhaya brand-inte date innu thanne nokku. Ningalude brand-inu ethra vayassaayi?')

lst('tmt008', 'd2c_brand', "B", 'പുതിയ പ്രോഡക്റ്റ്\nലൈൻ? ബ്രാൻഡ്\nചെക്ക് ചെയ്യൂ', [('ചോദ്യം', 'പുതിയ ഉൽപ്പന്നം നിലവിലെ ക്ലാസിൽ വരുമോ?'), ('ഇല്ലെങ്കിൽ', 'ആ ക്ലാസിലും ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യണം.'), ('ചിഹ്നം', 'പുതിയ ക്ലാസിൽ ഫയൽ ചെയ്ത ശേഷം ആ ലേബലിൽ TM.')],
 'പുതിയ ഉൽപ്പന്നം\nപഴയ സംരക്ഷണം പോരാ', CTA_TRADEMARK, theme="tip",
 cap_ml='സോപ്പിൽ നിന്ന് ഷാംപൂവിലേക്കോ, ടീ-ഷർട്ടിൽ നിന്ന് ബാഗിലേക്കോ? പുതിയ ഉൽപ്പന്നം നിലവിലെ ട്രേഡ്മാർക്ക് ക്ലാസിൽ വരുമോ എന്ന് നോക്കൂ. അടുത്തത് എന്ത് ലോഞ്ച് ചെയ്യുന്നു?',
 cap_en='Adding a new product line? Check whether it falls in the class your trademark already covers; if not, file in that class too. What are you launching next?',
 cap_mg='Puthiya product line? Athu ippozhathe trademark class-il varumo ennu nokku; illenkil aa class-ilum file cheyyanam. Adutha launch enthaanu?')

lst('tmt009', 'copied_brand', "B", 'നിങ്ങളുടെ പേരിന്\nസമാനമായ അപേക്ഷ\nവന്നാൽ?', [('എവിടെ കാണാം', 'ട്രേഡ്മാർക്ക് ജേണലിൽ പ്രസിദ്ധീകരിക്കും.'), ('എത്ര സമയം', 'പ്രസിദ്ധീകരിച്ച് നാല് മാസത്തിനുള്ളിൽ എതിർക്കാം.'), ('ട്രിക്ക്', 'നിങ്ങളുടെ പേരിന് സമാനമായവ ഇടയ്ക്കിടെ തിരയൂ.')],
 'കണ്ടില്ലെങ്കിൽ\nഎതിർക്കാനും പറ്റില്ല', CTA_BRAND, theme="tip",
 cap_ml='ആരെങ്കിലും നിങ്ങളുടെ ബ്രാൻഡിന് സമാനമായ പേര് ഫയൽ ചെയ്താൽ, ജേണലിൽ വന്ന് നാല് മാസത്തിനുള്ളിൽ എതിർപ്പ് നൽകാം. സമാന പേരുകൾ ഇടയ്ക്ക് നോക്കൂ. നിങ്ങളുടെ പേര് കോപ്പി ചെയ്യപ്പെട്ടിട്ടുണ്ടോ?',
 cap_en='If someone files a name close to your brand, you can oppose it within 4 months of its publication in the Trade Marks Journal. Search for look-alike names now and then. Has your name been copied?',
 cap_mg='Aarenkilum ningalude brand-inu samaanamaaya peru file cheythaal, journal-il vannu 4 maasathinullil oppose cheyyaam. Idakku search cheyyu. Ningalude peru copy aayittundo?')

lst('tmt010', 'app_founder', "B", 'ഫയൽ ചെയ്തു.\nതീർന്നോ?\nഇല്ല, തുടങ്ങിയതേ ഉള്ളൂ', [('ഇപ്പോൾ', 'TM ചിഹ്നം ഉപയോഗിക്കാം.'), ('വരാവുന്നത്', 'ഒബ്ജക്ഷനോ ജേണലിന് ശേഷം എതിർപ്പോ.'), ('ഇനിയും അല്ല', 'R ചിഹ്നം, രജിസ്ട്രേഷൻ കിട്ടുന്നത് വരെ.')],
 'ഫയലിംഗ് തുടക്കം\nരജിസ്ട്രേഷൻ ലക്ഷ്യം', CTA_TRADEMARK, theme="tip",
 cap_ml='ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്താൽ TM ഉപയോഗിക്കാം. പക്ഷേ ഒബ്ജക്ഷനോ എതിർപ്പോ വരാം, R രജിസ്ട്രേഷന് ശേഷം മാത്രം. നിങ്ങളുടെ അപേക്ഷ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='Filing a trademark lets you use TM, but an objection or an opposition can still come, and the R symbol waits for registration. What stage is your application at?',
 cap_mg='Trademark file cheythaal TM upayogikkaam. Pakshe objection-o opposition-o varaam, R registration-nu shesham maathram. Ningalude application ethu stage-il?')
