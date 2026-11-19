# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

lst('gt001', 'trader', "B", 'GST ലിമിറ്റ്:\n30 സെക്കൻഡിൽ\nഓർത്തുവെക്കാം', [('സാധനം', 'വർഷം നാല്പത് ലക്ഷം.'), ('സർവീസ്', 'വർഷം ഇരുപത് ലക്ഷം.'), ('ട്രിക്ക്', 'മാസം തോറും ആകെ വിൽപ്പന കൂട്ടി നോക്കൂ.')],
 'ലിമിറ്റ് അടുത്താൽ\nആദ്യം രജിസ്റ്റർ', CTA_LIMIT, theme="tip",
 cap_ml='കേരളത്തിൽ GST ലിമിറ്റ്: സാധനങ്ങൾക്ക് വർഷം 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം. മാസം തോറും ആകെ വിൽപ്പന നോക്കൂ. നിങ്ങൾ ലിമിറ്റിന് അടുത്താണോ?',
 cap_en='Kerala GST limits: 40 lakh a year for goods, 20 lakh for services. Add up your sales every month. Are you close to the limit?',
 cap_mg='Kerala GST limit: goods-nu 40 lakh, service-nu 20 lakh. Maasam thorum aake vilppana nokku. Ningal limit-nu aduthaano?')

lst('gt002', 'online_seller', "B", 'ഓൺലൈനിൽ വിൽക്കും\nമുമ്പ് ഈ 3\nചോദ്യം', [('മറ്റ് സംസ്ഥാനത്തേക്ക്?', 'അയക്കുന്നുണ്ടെങ്കിൽ ആദ്യ വിൽപ്പന മുതൽ GST.'), ('കേരളത്തിൽ മാത്രം?', 'ലിമിറ്റിന് താഴെയെങ്കിൽ PAN എൻറോൾമെന്റ് മതിയാകാം.'), ('മാർക്കറ്റ്പ്ലേസ്?', 'ആ സൗകര്യം അവർ നൽകുന്നുണ്ടോ എന്ന് നോക്കൂ.')],
 'ലിസ്റ്റ് ചെയ്യും മുമ്പ്\nചോദിക്കൂ', CTA_GST, theme="tip",
 cap_ml='ഓൺലൈൻ വിൽപ്പനയ്ക്ക് മുമ്പ്: മറ്റ് സംസ്ഥാനത്തേക്ക് അയച്ചാൽ ആദ്യ വിൽപ്പന മുതൽ GST. കേരളത്തിൽ മാത്രം, ലിമിറ്റിന് താഴെ, ആണെങ്കിൽ PAN അടിസ്ഥാന എൻറോൾമെന്റ് മതിയാകാം. നിങ്ങൾ എവിടേക്കാണ് അയക്കുന്നത്?',
 cap_en='Before selling online: shipping to other states needs GST from the first sale. Selling only inside Kerala and below the limit, a PAN-based enrolment may be enough if the marketplace supports it. Where do you ship to?',
 cap_mg='Online vilkkunnathinu mumpu: other state-ilekku ayachaal aadya vilppana muthal GST. Kerala-il maathram, limit-nu thaazhe aanel PAN enrolment mathiyaakaam. Ningal evidekku ayakkunnu?')

lst('gt003', 'service_pro', "B", 'കോമ്പോസിഷൻ\nസ്കീം: ആർക്ക്?\nഒരു ടിപ്പ്', [('സാധനം', 'ഒന്നര കോടി വരെ ടേൺഓവർ.'), ('സർവീസ്', 'അമ്പത് ലക്ഷം വരെ.'), ('ടിപ്പ്', 'ലളിതമായ റിട്ടേൺ വേണോ എന്ന് ആദ്യം ആലോചിക്കൂ.')],
 'ചെറുകിട ബിസിനസ്സിന്\nഒരു ലളിത വഴി', CTA_GST, theme="tip",
 cap_ml='GST കോമ്പോസിഷൻ സ്കീം: സാധനങ്ങൾക്ക് 1.5 കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ ടേൺഓവർ. നിങ്ങളുടെ ബിസിനസ് ഇതിൽ വരുമോ?',
 cap_en='GST composition scheme limits: up to 1.5 crore turnover for goods, 50 lakh for services. Does your business fit?',
 cap_mg='GST composition scheme: goods-nu 1.5 kodi vare, service-nu 50 lakh vare. Ningalude business ithil varumo?')

