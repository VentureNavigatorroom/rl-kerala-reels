# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Same facts as batch01.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
S = []
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))

lst('kt001', 'freelancer', "B", 'രജിസ്ട്രേഷൻ കഴിഞ്ഞ്\n30 ദിവസത്തിനുള്ളിൽ\nചെയ്യേണ്ടത്', [('ആദ്യ ഓഡിറ്റർ', 'ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് മുപ്പത് ദിവസത്തിനുള്ളിൽ നിയമിക്കണം.'), ('ബാങ്ക് അക്കൗണ്ട്', 'കമ്പനിയുടെ പേരിൽ തന്നെ തുറക്കണം.'), ('രേഖകൾ ഒരിടത്ത്', 'സർട്ടിഫിക്കറ്റും PAN-ഉം സുരക്ഷിതമായി സൂക്ഷിക്കൂ.')],
 'ആദ്യ മാസം\nഅശ്രദ്ധ വേണ്ട', CTA_AFTER, theme="tip",
 cap_ml='Company registration കഴിഞ്ഞ് ആദ്യ മുപ്പത് ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം. കമ്പനി പേരിൽ ബാങ്ക് അക്കൗണ്ടും തുറക്കണം. ഇതിൽ ഏതാണ് ബാക്കി?',
 cap_en="Within 30 days of incorporation, appoint the first auditor and open the company's bank account. Which one is still pending for you?",
 cap_mg='Registration kazhinju 30 divasathinullil first auditor-ne appoint cheyyanam, company perilu bank account thurakkanam. Ethaanu baakki?')

lst('kt002', 'solo', "B", '180 ദിവസം:\nINC-20A\nമറന്നാൽ?', [('എന്താണ്', 'ബിസിനസ് തുടങ്ങിയെന്ന ഡിക്ലറേഷൻ.'), ('എപ്പോൾ', 'ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് നൂറ്റിയെൺപത് ദിവസത്തിനുള്ളിൽ.'), ('ട്രിക്ക്', 'ആദ്യ ദിവസം തന്നെ കലണ്ടറിൽ തീയതി ഇടൂ.')],
 'ഒരു റിമൈൻഡർ\nഒരുപാട് തലവേദന ഒഴിവാക്കും', CTA_AFTER, theme="tip",
 cap_ml='INC-20A എന്ന ബിസിനസ് തുടക്ക ഡിക്ലറേഷൻ ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്യണം. നിങ്ങളുടെ കമ്പനി എത്ര ദിവസമായി?',
 cap_en='File INC-20A, the commencement of business declaration, within 180 days of incorporation. Put the date in your calendar on day one. How many days old is your company?',
 cap_mg='INC-20A 180 divasathinullil file cheyyanam. Aadya divasam thanne calendar-il date idu. Ningalude company ethra divasamaayi?')

lst('kt003', 'cofounders', "B", 'കമ്പനി രജിസ്ട്രേഷന്\nരേഖകൾ: ഒരു\nചെക്ക്ലിസ്റ്റ്', [('ഓരോ ഡയറക്ടർക്കും', 'PAN, ആധാർ, അഡ്രസ്സ് പ്രൂഫ്, ഫോട്ടോ.'), ('ഓഫീസിന്', 'പുതിയ കറന്റ് ബില്ലും ഉടമയുടെ NOC-യും.'), ('ട്രിക്ക്', 'വീടിന്റെ അഡ്രസ്സും ഓഫീസാക്കാം.')],
 'രേഖ റെഡിയെങ്കിൽ\nപകുതി ജോലി കഴിഞ്ഞു', CTA_DOCS, theme="tip",
 cap_ml='കമ്പനി രജിസ്ട്രേഷന്: ഓരോ ഡയറക്ടറുടെയും PAN, ആധാർ, അഡ്രസ്സ് പ്രൂഫ്, ഫോട്ടോ; ഓഫീസിന് കറന്റ് ബില്ലും NOC-യും. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് ഇല്ലാത്തത്?',
 cap_en="Company registration documents: PAN, Aadhaar, address proof and photo for every director, plus a recent utility bill and the owner's NOC for the office. Which one are you missing?",
 cap_mg='Company registration-nu: oro director-nteyum PAN, Aadhaar, address proof, photo; office-nu current bill-um NOC-um. Ethaanu ningalkku illaathathu?')

