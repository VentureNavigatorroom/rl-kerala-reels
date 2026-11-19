# Tips and tricks 02 (20 Nov, refill writer): one tip reel per topic per day. theme="tip". Facts only from topics.py FACTS_ROC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

lst('rct004', 'nri_director', "B", 'ഗൾഫിലാണോ\nഡയറക്ടർ?\nKYC മറക്കല്ലേ', [('ആര്', 'എല്ലാ ഡയറക്ടർമാരും, വിദേശത്തുള്ളവരും.'), ('എപ്പോൾ', 'എല്ലാ വർഷവും സെപ്റ്റംബർ മുപ്പതിനുള്ളിൽ DIR-3 KYC.'), ('ട്രിക്ക്', 'AGM തീയതിക്കൊപ്പം ഓരോ ഡയറക്ടറെയും ഓർമ്മിപ്പിക്കൂ.')],
 'ദൂരം കൂടിയാലും\nതീയതി മാറില്ല', CTA_ROC, theme="tip",
 cap_ml='കമ്പനിയിലെ ഓരോ ഡയറക്ടറും, ഗൾഫിലോ വിദേശത്തോ ആണെങ്കിലും, സെപ്റ്റംബർ 30-നുള്ളിൽ DIR-3 KYC ചെയ്യണം. നിങ്ങളുടെ കമ്പനിയിൽ എത്ര ഡയറക്ടർമാർ പുറത്താണ്?',
 cap_en='Every director of a private limited company, even one living in the Gulf or abroad, must complete DIR-3 KYC by 30 September. How many of your directors live abroad?',
 cap_mg='Company-ile oro director-um, Gulf-il aanenkilum, September 30-nullil DIR-3 KYC cheyyanam. Ningalude company-il ethra director purathaanu?')

lst('rct005', 'late_filer', "B", 'ROC ലേറ്റ് ഫീ:\nഎവിടെ നിൽക്കും?\nനിൽക്കില്ല', [('ദിവസം', 'ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ.'), ('പരിധി', 'ഇല്ല. ദിവസം കൂടും തോറും കൂടും.'), ('കണക്ക്', 'നൂറ് ദിവസം വൈകിയാൽ ഒരു ഫോമിന് 10,000 രൂപ.')],
 'വൈകുന്ന ഓരോ ദിവസവും\nബില്ലിൽ ചേരും', CTA_FILING, theme="tip",
 cap_ml='ROC ഫോമുകൾ വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ, പരിധിയില്ല. നൂറ് ദിവസം വൈകിയാൽ ഒരു ഫോമിന് മാത്രം 10,000 രൂപ. നിങ്ങൾ ഇത് അറിഞ്ഞിരുന്നോ?',
 cap_en='Late ROC forms cost a late fee of 100 rupees a day per form, with no cap. 100 days late means 10,000 rupees for one form alone. Did you know this?',
 cap_mg='ROC form vaikiyaal oro form-num divasam 100 rupees late fee, limit illa. 100 divasam vaikiyaal oru form-nu 10,000 rupees. Ithu ariyaamaayirunno?')

lst('rct006', 'new_company_roc', "B", 'പുതിയ കമ്പനി:\nആദ്യ 180 ദിവസം\n2 തീയതി', [('മുപ്പത് ദിവസം', 'ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം.'), ('നൂറ്റിയെൺപത് ദിവസം', 'INC-20A, ബിസിനസ് തുടങ്ങിയെന്ന ഡിക്ലറേഷൻ.'), ('പിന്നെ എല്ലാ വർഷവും', 'സെപ്റ്റംബർ മുപ്പതിനുള്ളിൽ AGM.')],
 'തുടക്കം ശരിയായാൽ\nകലണ്ടർ എളുപ്പം', CTA_ROC, theme="tip",
 cap_ml='പുതിയ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി: 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ, 180 ദിവസത്തിനുള്ളിൽ INC-20A, പിന്നെ എല്ലാ വർഷവും സെപ്റ്റംബർ 30-നുള്ളിൽ AGM. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ദിവസമായി?',
 cap_en='New private limited company: first auditor within 30 days, INC-20A within 180 days, then an AGM by 30 September every year. How many days old is your company?',
 cap_mg='Puthiya Pvt Ltd: 30 divasathinullil first auditor, 180 divasathinullil INC-20A, pinne ella varshavum September 30-nullil AGM. Company-kku ethra divasamaayi?')

lst('rct007', 'llp_owner', "B", 'പ്രൈവറ്റ് ലിമിറ്റഡോ\nLLP-യോ? ഫയലിംഗ്\nതീയതി വേറെ', [('പ്രൈവറ്റ് ലിമിറ്റഡ്', 'സെപ്റ്റംബർ മുപ്പതിനുള്ളിൽ AGM, പിന്നെ AOC-4, MGT-7.'), ('LLP', 'മെയ് മുപ്പത് ഫോം പതിനൊന്ന്, ഒക്ടോബർ മുപ്പത് ഫോം എട്ട്.'), ('ട്രിക്ക്', 'സർട്ടിഫിക്കറ്റിൽ നോക്കി ഏതാണ് നിങ്ങൾ എന്ന് ഉറപ്പിക്കൂ.')],
 'ശരിയായ ഘടന\nശരിയായ കലണ്ടർ', CTA_FILING, theme="tip",
 cap_ml='പ്രൈവറ്റ് ലിമിറ്റഡിന് AGM, AOC-4, MGT-7; LLP-ക്ക് മെയ് 30-ന് ഫോം 11, ഒക്ടോബർ 30-ന് ഫോം 8. ഘടന അനുസരിച്ച് തീയതി മാറും. നിങ്ങളുടേത് കമ്പനിയോ LLP-യോ?',
 cap_en='Private limited: AGM by 30 September, then AOC-4 and MGT-7. LLP: Form 11 by 30 May and Form 8 by 30 October. Company or LLP?',
 cap_mg='Pvt Ltd-nu AGM, AOC-4, MGT-7; LLP-kku May 30 Form 11, October 30 Form 8. Ningaludethu company-o LLP-yo?')

lst('rct008', 'dormant_company', "B", 'ഡയറക്ടർക്ക്\nഅയോഗ്യത: അത്\nഎന്താണ്?', [('എപ്പോൾ', 'കമ്പനി മൂന്ന് വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ.'), ('ആർക്ക്', 'ആ കമ്പനിയുടെ ഡയറക്ടർമാർക്ക്.'), ('എത്ര കാലം', 'അഞ്ച് വർഷം വരെ.')],
 'ഉറങ്ങിയ കമ്പനി\nഉണർത്തുന്നത് ഡയറക്ടറെ', CTA_FILING, theme="tip",
 cap_ml='പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി മൂന്ന് വർഷം ഫയലിംഗ് ചെയ്യാതിരുന്നാൽ ഡയറക്ടർമാർക്ക് അഞ്ച് വർഷം വരെ അയോഗ്യത വരാം. നിങ്ങളുടെ കമ്പനി എത്ര വർഷമായി ഫയൽ ചെയ്തിട്ടില്ല?',
 cap_en='If a private limited company does not file for 3 years, its directors can be disqualified for 5 years. How long since your company last filed?',
 cap_mg='Pvt Ltd company 3 varsham file cheythillenkil director-maarkku 5 varsham vare disqualification varaam. Ningalude company ethra varshamaayi file cheythittilla?')

lst('rct009', 'new_company_roc', "B", 'AGM തീയതി\nഅറിഞ്ഞാൽ ബാക്കി\nകണക്കാക്കാം', [('ഉദാഹരണം', 'AGM ഓഗസ്റ്റ് ഇരുപത്.'), ('മുപ്പത് ദിവസം', 'AOC-4: സെപ്റ്റംബർ പത്തൊമ്പതിനുള്ളിൽ.'), ('അറുപത് ദിവസം', 'MGT-7: ഒക്ടോബർ പത്തൊമ്പതിനുള്ളിൽ.')],
 'ഒരു തീയതി\nരണ്ട് ഡെഡ്‌ലൈൻ', CTA_ROC, theme="tip",
 cap_ml='AOC-4 AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ, MGT-7 60 ദിവസത്തിനുള്ളിൽ. AGM നടത്തിയ ഉടനെ രണ്ട് തീയതിയും കലണ്ടറിൽ ഇടൂ. നിങ്ങളുടെ AGM എന്നായിരുന്നു?',
 cap_en='AOC-4 is due within 30 days of the AGM and MGT-7 within 60 days. Put both dates in the calendar the day you hold the AGM. When was yours?',
 cap_mg='AOC-4 AGM kazhinju 30 divasathinullil, MGT-7 60 divasathinullil. AGM kazhinjaal udane randu date-um calendar-il idu. Ningalude AGM ennaayirunnu?')

lst('rct010', 'late_filer', "B", 'രണ്ട് ഫോം\nപത്ത് ദിവസം വൈകി.\nലേറ്റ് ഫീ എത്ര?', [('ഓരോ ഫോമും', 'ലേറ്റ് ഫീ വെവ്വേറെ കണക്കാക്കും.'), ('കണക്ക്', 'രണ്ട് ഫോം, പത്ത് ദിവസം, ദിവസം നൂറ് രൂപ.'), ('ആകെ', '2,000 രൂപ. ഒരുമിച്ചല്ല, ഫോം തോറും.')],
 'ഫോം കൂടിയാൽ\nലേറ്റ് ഫീയും കൂടും', CTA_FILING, theme="tip",
 cap_ml='ROC ലേറ്റ് ഫീ ഓരോ ഫോമിനും വെവ്വേറെയാണ്: രണ്ട് ഫോം പത്ത് ദിവസം വൈകിയാൽ 2,000 രൂപ. എല്ലാ ഫോമും സമയത്ത് ഫയൽ ചെയ്യൂ. നിങ്ങളുടെ കമ്പനിക്ക് വർഷം എത്ര ഫോം?',
 cap_en='The ROC late fee is counted per form: two forms 10 days late cost 2,000 rupees. File every form on time. How many forms does your company file a year?',
 cap_mg='ROC late fee oro form-num separate: randu form 10 divasam vaikiyaal 2,000 rupees. Ella form-um samayathu file cheyyu. Company-kku varsham ethra form?')

lst('rct011', 'nri_director', "B", 'ഒക്ടോബറിൽ\nഅക്കൗണ്ടന്റിനോട്\n3 ചോദ്യം', [('ഒന്ന്', 'AGM സെപ്റ്റംബർ മുപ്പതിനുള്ളിൽ നടന്നോ?'), ('രണ്ട്', 'AOC-4: AGM കഴിഞ്ഞ് മുപ്പത് ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തോ?'), ('മൂന്ന്', 'MGT-7: അറുപത് ദിവസത്തിനുള്ളിലെ തീയതി കുറിച്ചോ?')],
 'ചോദിക്കാൻ ഒരു മിനിറ്റ്\nമറന്നാൽ ദിവസവും പിഴ', CTA_ROC, theme="tip",
 cap_ml='ഡയറക്ടർ ഗൾഫിലാണെങ്കിലും ഈ മൂന്ന് ചോദ്യം ചോദിക്കാം: AGM സെപ്റ്റംബർ 30-നുള്ളിൽ നടന്നോ, AOC-4 AGM കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തോ, MGT-7 60 ദിവസത്തിനുള്ളിൽ ഉണ്ടോ. നിങ്ങൾ ചോദിച്ചോ?',
 cap_en='Three questions to ask your accountant every October, even from the Gulf: was the AGM held by 30 September, was AOC-4 filed within 30 days of it, and is MGT-7 diarised within 60 days? Have you asked?',
 cap_mg='October-il accountant-inodu 3 chodyam: AGM September 30-nullil nadanno, AOC-4 30 divasathinullil file cheytho, MGT-7 60 divasathinullil undo. Ningal chodicho?')
