# Tips and tricks 02 (20 Nov): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_IEC.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_IEC, CTA_EXPORT = topics.CTA_IEC, topics.CTA_EXPORT

lst('iet004', 'importer', "B", 'IEC ഡീആക്ടിവേറ്റ്\nആയാൽ എന്ത്\nസംഭവിക്കും?', [('കസ്റ്റംസ്', 'കോഡ് ചോദിക്കും, ഇറക്കുമതി മുന്നോട്ട് പോകില്ല.'), ('ബാങ്ക്', 'വിദേശ പേമെന്റിനും IEC ചോദിക്കും.'), ('പരിഹാരം', 'വർഷത്തെ ഓൺലൈൻ അപ്ഡേറ്റ് ഒരിക്കലും മുടക്കരുത്.')],
 'കോഡ് ഉറങ്ങിയാൽ\nകച്ചവടവും ഉറങ്ങും', CTA_IEC, theme="tip",
 cap_ml='IEC ഡീആക്ടിവേറ്റ് ആയാൽ കസ്റ്റംസും ബാങ്കും ചോദിക്കുമ്പോൾ കാണിക്കാൻ സജീവ കോഡ് ഇല്ല. എല്ലാ വർഷവും ഏപ്രിൽ മുതൽ ജൂൺ വരെയുള്ള അപ്ഡേറ്റാണ് രക്ഷ. നിങ്ങളുടെ IEC സജീവമാണോ?',
 cap_en='If your IEC is deactivated, you have no active code to show when customs and banks ask. The yearly April to June online update keeps it alive. Is your IEC active?',
 cap_mg='IEC deactivate aayaal customs-um bank-um chodikkumbol kaanikkaan active code illa. Ella varshavum April muthal June vare update aanu raksha. Ningalude IEC active aano?')

lst('iet005', 'first_exporter', "B", 'ആദ്യ കയറ്റുമതിക്ക്\nമുമ്പ് 3 ചെക്ക്', [('IEC', 'ബിസിനസ് PAN-ൽ എടുത്തോ?'), ('ബാങ്ക്', 'വിദേശ പണം വരുന്ന ബാങ്കിന് IEC നൽകിയോ?'), ('കലണ്ടർ', 'ഏപ്രിൽ മുതൽ ജൂൺ വരെ അപ്ഡേറ്റ് റിമൈൻഡർ ഇട്ടോ?')],
 'മൂന്നും ശരിയെങ്കിൽ\nപെട്ടി അയക്കൂ', CTA_EXPORT, theme="tip",
 cap_ml='ആദ്യ കയറ്റുമതിക്ക് മുമ്പ്: ബിസിനസ് PAN-ൽ IEC, വിദേശ പണം സ്വീകരിക്കുന്ന ബാങ്കിന് IEC വിവരം, വർഷത്തെ അപ്ഡേറ്റിന് കലണ്ടർ റിമൈൻഡർ. ഇതിൽ ഏതാണ് ബാക്കി?',
 cap_en='Before your first export: an IEC on the business PAN, your bank (which receives the foreign payment) has the IEC, and a calendar reminder for the yearly update. Which one is pending?',
 cap_mg='First export-nu mumpu: business PAN-il IEC, foreign panam varunna bank-nu IEC, yearly update-nu calendar reminder. Ethaanu baakki?')

lst('iet006', 'service_export', "B", 'സാധനമോ സർവീസോ?\nIEC നിയമം\nരണ്ട് വിധം', [('സാധനം കയറ്റുമതി', 'IEC നിർബന്ധം. കസ്റ്റംസും ബാങ്കും ചോദിക്കും.'), ('സർവീസ് കയറ്റുമതി', 'എക്സ്പോർട്ട് ആനുകൂല്യം ക്ലെയിം ചെയ്യാൻ IEC വേണം.'), ('രണ്ടും ചെയ്താൽ', 'ഒരേ PAN-ൽ ഒരു IEC മതി.')],
 'ആവശ്യം ഏതെന്ന്\nആദ്യം അറിയൂ', CTA_IEC, theme="tip",
 cap_ml='സാധനം കയറ്റുമതി ചെയ്യാൻ IEC നിർബന്ധമാണ്. സർവീസ് കയറ്റുമതിക്കാർക്ക് എക്സ്പോർട്ട് ആനുകൂല്യങ്ങൾ ക്ലെയിം ചെയ്യാൻ IEC വേണം. രണ്ടും ചെയ്യുന്നവർക്ക് ഒരേ PAN-ൽ ഒരു IEC മതി. നിങ്ങൾ വിൽക്കുന്നത് സാധനമോ സർവീസോ?',
 cap_en='Exporting goods needs an IEC. Service exporters need one to claim export benefits. If you do both, one IEC on the same PAN covers it. Do you export goods or services?',
 cap_mg='Sadhanam export cheyyaan IEC nirbandham. Service export-nu benefits claim cheyyaan IEC venam. Randum cheyyunnavarkku oru PAN-il oru IEC mathi. Ningal goods-o service-o?')

lst('iet007', 'spice_trade', "B", 'നിങ്ങളുടെ IEC\nആരൊക്കെ ചോദിക്കും?', [('കസ്റ്റംസ്', 'ഓരോ കയറ്റുമതിക്കും ഇറക്കുമതിക്കും.'), ('ബാങ്ക്', 'വിദേശ പണം വരുമ്പോഴും പോകുമ്പോഴും.'), ('DGFT', 'വർഷം തോറും ഏപ്രിൽ മുതൽ ജൂൺ വരെ അപ്ഡേറ്റ്.')],
 'കോഡ് ഒന്ന്\nചോദിക്കുന്നവർ മൂന്ന്', CTA_IEC, theme="tip",
 cap_ml='IEC കസ്റ്റംസ് ചോദിക്കും, വിദേശ പണം കൈകാര്യം ചെയ്യുമ്പോൾ ബാങ്കും ചോദിക്കും. DGFT-ൽ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റും വേണം. നിങ്ങളുടെ IEC നമ്പർ ഓർമ്മയുണ്ടോ?',
 cap_en='Customs ask for your IEC, banks ask when foreign payments move, and DGFT needs the yearly April to June update. Do you know your IEC number by heart?',
 cap_mg='IEC customs chodikkum, foreign payment varumbol bank-um chodikkum. DGFT-il ella varshavum April-June update venam. Ningalude IEC number orma undo?')

lst('iet008', 'first_exporter', "B", 'പ്രൊപ്രൈറ്റർഷിപ്പിൽ\nനിന്ന് കമ്പനിയിലേക്ക്:\nIEC?', [('പഴയ സ്ഥാപനം', 'പഴയ IEC പഴയ PAN-ന്റേത്.'), ('പുതിയ കമ്പനി', 'പുതിയ PAN, അതിന് സ്വന്തം IEC വേണം.'), ('ട്രിക്ക്', 'ആദ്യ ഷിപ്പ്മെന്റിന് മുമ്പ് പുതിയ കോഡ് എടുക്കൂ.')],
 'PAN മാറിയാൽ\nകോഡും മാറും', CTA_IEC, theme="tip",
 cap_ml='IEC ബിസിനസ് PAN-മായി ബന്ധിപ്പിച്ചതാണ്, ഒരു PAN-ന് ഒരു IEC. പ്രൊപ്രൈറ്റർഷിപ്പിൽ നിന്ന് കമ്പനിയിലേക്ക് മാറുമ്പോൾ പുതിയ PAN-ന് പുതിയ IEC വേണം. നിങ്ങളുടെ ബിസിനസ് കമ്പനിയാക്കാൻ പ്ലാനുണ്ടോ?',
 cap_en='An IEC is tied to the business PAN, one per PAN. Moving from a proprietorship to a company means a new PAN, so the company needs its own IEC. Planning to convert your business?',
 cap_mg='IEC business PAN-umaayi linked, oru PAN-nu oru IEC. Proprietorship-il ninnu company-lekku maarumbol puthiya PAN-nu puthiya IEC venam. Company aakkaan plan undo?')

lst('iet009', 'handicraft_export', "B", 'വിദേശത്തിരുന്ന്\nനാട്ടിലെ സാധനം\nകയറ്റുമതി: 3 പടി', [('ഒന്ന്', 'നാട്ടിൽ PAN ഉള്ള ഒരു ബിസിനസ്.'), ('രണ്ട്', 'ആ PAN-ൽ DGFT-യിൽ ഓൺലൈനായി IEC.'), ('മൂന്ന്', 'വർഷം തോറും ഏപ്രിൽ മുതൽ ജൂൺ വരെ അപ്ഡേറ്റ്.')],
 'ദൂരം പ്രശ്നമല്ല\nക്രമം പ്രധാനം', CTA_EXPORT, theme="tip",
 cap_ml='ഗൾഫിലിരുന്ന് നാട്ടിലെ ഉൽപ്പന്നം കയറ്റുമതി ചെയ്യാൻ: നാട്ടിലെ ബിസിനസിന്റെ PAN, ആ PAN-ൽ DGFT-യിൽ ഓൺലൈനായി IEC, പിന്നെ വർഷത്തെ അപ്ഡേറ്റ്. നിങ്ങൾ ഏത് രാജ്യത്താണ്?',
 cap_en='Exporting Kerala products while living abroad: a Kerala business with its own PAN, an IEC on that PAN applied online with DGFT, then the yearly update. Which country are you in?',
 cap_mg='Gulf-il irunnu naattile product export cheyyaan: naattile business PAN, aa PAN-il DGFT-il online IEC, pinne yearly update. Ningal ethu raajyathaanu?')

lst('iet010', 'importer', "B", 'കടയ്ക്കോ ഫാക്ടറിക്കോ\nഇറക്കുമതി: IEC\nവേണോ?', [('വിൽക്കാൻ', 'വേണം.'), ('ബിസിനസിന്റെ മെഷീന്', 'വേണം. സ്വന്തം ഉപയോഗമല്ല, ബിസിനസ് ഉപയോഗം.'), ('വീട്ടിലെ ഉപയോഗത്തിന്', 'വേണ്ട.')],
 'വിൽക്കാതെയും\nബിസിനസ് ഇറക്കുമതി', CTA_IEC, theme="tip",
 cap_ml='വിൽക്കാനുള്ള സാധനത്തിന് മാത്രമല്ല, ബിസിനസിന് വേണ്ടിയുള്ള മെഷീൻ ഇറക്കുമതി ചെയ്യാനും IEC വേണം. വീട്ടിലെ സ്വന്തം ഉപയോഗത്തിന് മാത്രം വേണ്ട. നിങ്ങളുടെ ബിസിനസിന് ഇറക്കുമതി മെഷീനുണ്ടോ?',
 cap_en='An IEC is needed not only for goods you resell but also for machinery imported for your business. Only imports for personal use at home are exempt. Does your business run on imported machines?',
 cap_mg='Vilkkaanulla sadhanathinu maathramalla, business-nu vendi machine import cheyyaanum IEC venam. Veettile swantham upayogathinu maathram venda. Ningalude business-nu imported machine undo?')
