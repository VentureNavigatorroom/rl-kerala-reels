# Tips and tricks 03 (20 Nov, refill to 10 unposted tips: gt001 posted). theme="tip". Facts only from topics.FACTS_GST.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

lst('gt011', 'online_seller', "B", 'ടേൺഓവർ 40 ലക്ഷം\nഎത്തിയില്ല.\nഎന്നിട്ടും GST?', [('മറ്റ് സംസ്ഥാനത്തേക്ക് സാധനം', 'ഒരു ഓർഡർ ആണെങ്കിലും ആദ്യ വിൽപ്പന മുതൽ GST.'), ('മറ്റ് സംസ്ഥാനത്ത് മേള സ്റ്റാൾ', 'കാഷ്വൽ ടാക്സബിൾ വ്യക്തിക്ക് ടേൺഓവർ നോക്കാതെ GST.'), ('മാർക്കറ്റ്പ്ലേസിൽ സാധനം', 'ആദ്യ വിൽപ്പന മുതൽ. കേരളത്തിൽ മാത്രം, ലിമിറ്റിന് താഴെ എങ്കിൽ PAN എൻറോൾമെന്റ് പറ്റിയേക്കും.')],
 'ലിമിറ്റ് മാത്രം\nനോക്കിയാൽ പോരാ', CTA_LIMIT, theme="tip",
 cap_ml='കേരളത്തിൽ സാധനത്തിന് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം ആണ് GST ലിമിറ്റ്. പക്ഷേ മറ്റ് സംസ്ഥാനത്തേക്ക് സാധനം അയക്കുമ്പോഴും, മറ്റ് സംസ്ഥാനത്ത് താൽക്കാലിക സ്റ്റാൾ ഇടുമ്പോഴും, മാർക്കറ്റ്പ്ലേസിൽ സാധനം വിൽക്കുമ്പോഴും ടേൺഓവർ നോക്കാതെ GST വേണ്ടിവരാം. ഇതിൽ ഏതാണ് നിങ്ങളുടേത്?',
 cap_en='The Kerala GST limit is 40 lakh for goods and 20 lakh for services, but three cases can need GST below it: goods shipped to another state, a temporary stall in another state (casual taxable person), and goods sold on a marketplace (a Kerala-only seller under the limit may use PAN enrolment if the platform supports it). Which one is yours?',
 cap_mg='Kerala-il goods-nu 40 lakh, service-nu 20 lakh aanu GST limit. Pakshe vere state-lekku goods ayakkumbol, vere state-il temporary stall idumbol, marketplace-il goods vilkkumbol turnover nokkaathe GST venam. Ithil ethaanu ningaludethu?')
