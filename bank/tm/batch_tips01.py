# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

lst('tmt001', 'd2c_brand', "B", 'TM-ഉം R-ഉം:\n10 സെക്കൻഡ്\nവ്യത്യാസം', [('TM', 'ഫയൽ ചെയ്താൽ ഉപയോഗിക്കാം.'), ('R', 'രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം.'), ('ട്രിക്ക്', 'ലേബൽ പ്രിന്റിന് മുമ്പ് സ്റ്റാറ്റസ് നോക്കൂ.')],
 'തെറ്റായ ചിഹ്നം\nലേബൽ പാഴാക്കും', CTA_BRAND, theme="tip",
 cap_ml='ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്താൽ TM ഉപയോഗിക്കാം. R ചിഹ്നം രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം. നിങ്ങളുടെ ലേബലിൽ ഏതാണ്?',
 cap_en='Use TM once you have filed a trademark; the R symbol only after registration. Which one is on your label?',
 cap_mg='Trademark file cheythaal TM. R registration kittiya sesham maathram. Ningalude label-il ethaanu?')

lst('tmt002', 'copied_brand', "B", 'ട്രേഡ്മാർക്ക്\nതീയതികൾ:\nമറക്കരുത്', [('മുപ്പത് ദിവസം', 'ഒബ്ജക്ഷന് മറുപടി നൽകാൻ.'), ('നാല് മാസം', 'ജേണലിൽ വന്നാൽ എതിർപ്പിനുള്ള സമയം.'), ('പത്ത് വർഷം', 'രജിസ്ട്രേഷൻ കാലാവധി, പുതുക്കാം.')],
 'ഒരു തീയതി മിസ്സായാൽ\nബ്രാൻഡ് അപകടത്തിൽ', CTA_TRADEMARK, theme="tip",
 cap_ml='ട്രേഡ്മാർക്ക്: ഒബ്ജക്ഷന് 30 ദിവസത്തിനുള്ളിൽ മറുപടി, ജേണലിൽ വന്നാൽ 4 മാസം എതിർപ്പിന്, രജിസ്ട്രേഷൻ 10 വർഷം, പുതുക്കാം. നിങ്ങളുടെ അപേക്ഷ ഏത് ഘട്ടത്തിൽ?',
 cap_en='Trademark dates: reply to an objection within 30 days, opposition window of 4 months after journal publication, registration valid 10 years and renewable. Where is your application?',
 cap_mg='Trademark: objection-nu 30 divasathinullil marupadi, journal-il vannaal 4 maasam opposition, registration 10 varsham. Ningalude application etha ghattathil?')

lst('tmt003', 'food_brand', "B", 'ക്ലാസ് തെറ്റിയാൽ\nബ്രാൻഡ് തുറന്നുകിടക്കും', [('നാല്പത്തിയഞ്ച് ക്ലാസ്', 'ഓരോ ഉൽപ്പന്നത്തിനും സേവനത്തിനും ഒന്ന്.'), ('ട്രിക്ക്', 'നിങ്ങൾ കച്ചവടം ചെയ്യുന്ന ക്ലാസിൽ ഫയൽ ചെയ്യൂ.'), ('ഓർക്കൂ', 'കമ്പനി പേര് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല.')],
 'ശരിയായ ക്ലാസ്,\nശരിയായ സംരക്ഷണം', CTA_TRADEMARK, theme="tip",
 cap_ml='ട്രേഡ്മാർക്കിന് 45 ക്ലാസുകളുണ്ട്. നിങ്ങൾ കച്ചവടം ചെയ്യുന്ന ക്ലാസുകളിൽ ഫയൽ ചെയ്യൂ. കമ്പനി പേര് അപ്രൂവൽ ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. നിങ്ങളുടെ ഉൽപ്പന്നം എന്താണ്?',
 cap_en='There are 45 trademark classes; file in the ones you actually trade in. A company name approval does not protect your brand. What do you sell?',
 cap_mg='Trademark-nu 45 class undu. Ningal kachavadam cheyyunna class-il file cheyyu. Company name approval brand-ine samrakshikkilla. Ningalude product enthaanu?')

