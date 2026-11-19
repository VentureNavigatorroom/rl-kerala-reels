# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

lst('rct002', 'dormant_company', "B", 'ബിസിനസ് ഇല്ല.\nഫയലിംഗും\nവേണ്ടേ?', [('തെറ്റ്', 'ബിസിനസ് ഇല്ലെങ്കിലും ഫയലിംഗ് നിർബന്ധം.'), ('മൂന്ന് വർഷം', 'ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് അയോഗ്യത.'), ('അപകടം', 'കമ്പനി സ്ട്രൈക്ക് ഓഫ് ആകാം.')],
 'ഉറങ്ങുന്ന കമ്പനിക്കും\nകലണ്ടർ ഉണ്ട്', CTA_FILING, theme="tip",
 cap_ml='ബിസിനസ് ഇല്ലെങ്കിലും ROC ഫയലിംഗ് നിർബന്ധം. മൂന്ന് വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് 5 വർഷം അയോഗ്യതയും കമ്പനി സ്ട്രൈക്ക് ഓഫും വരാം. നിങ്ങളുടെ കമ്പനി എത്ര കാലമായി ഉറങ്ങുന്നു?',
 cap_en='Filing is due even with zero business. Three years of non-filing can disqualify directors for 5 years and get the company struck off. How long has yours been idle?',
 cap_mg='Business illenkilum ROC filing nirbandham. 3 varsham file cheythillenkil directors-nu 5 varsham ayogyatha, company strike off aakaam. Ningalude company ethra kaalamaayi urangunnu?')

lst('rct003', 'llp_owner', "B", 'LLP-ക്ക് രണ്ട്\nതീയതി മാത്രം\nഓർത്താൽ മതി', [('മെയ് മുപ്പത്', 'ഫോം പതിനൊന്ന്.'), ('ഒക്ടോബർ മുപ്പത്', 'ഫോം എട്ട്.'), ('ഓർക്കൂ', 'ബിസിനസ് ഇല്ലെങ്കിലും രണ്ടും വേണം.')],
 'രണ്ട് തീയതി,\nഒരു കലണ്ടർ', CTA_ROC, theme="tip",
 cap_ml='LLP: ഫോം 11 മെയ് 30-നകം, ഫോം 8 ഒക്ടോബർ 30-നകം. ബിസിനസ് ഇല്ലെങ്കിലും ഫയൽ ചെയ്യണം. നിങ്ങളുടെ LLP ഈ വർഷം ഫയൽ ചെയ്തോ?',
 cap_en='LLP filings: Form 11 by 30 May and Form 8 by 30 October, due even with zero business. Has your LLP filed this year?',
 cap_mg='LLP: Form 11 May 30-nakam, Form 8 October 30-nakam. Business illenkilum file cheyyanam. Ningalude LLP ee varsham file cheytho?')

