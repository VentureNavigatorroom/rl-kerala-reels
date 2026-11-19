# Tips and tricks 02 (20 Nov, refill to 10 unposted tips per topic). theme="tip". Same checked facts as batch01.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
S = []
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))

lst('kt004', 'cofounders', "B", 'പ്രൈവറ്റ് ലിമിറ്റഡ്:\nമിനിമം വേണ്ടത്\n10 സെക്കൻഡിൽ', [('ഡയറക്ടർ', 'കുറഞ്ഞത് രണ്ട് പേർ.'), ('ഷെയർഹോൾഡർ', 'കുറഞ്ഞത് രണ്ട് പേർ.'), ('ഒരാൾ ഇന്ത്യയിൽ', 'ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ.')],
 'രണ്ടുപേർ റെഡിയെങ്കിൽ\nതുടങ്ങാം', CTA_START, theme="tip",
 cap_ml='പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് കുറഞ്ഞത് രണ്ട് ഡയറക്ടർമാരും രണ്ട് ഷെയർഹോൾഡർമാരും വേണം. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാളാകണം. നിങ്ങളുടെ കൂടെ ആരുണ്ട്?',
 cap_en='A private limited company needs at least 2 directors and 2 shareholders, and at least one director resident in India. Who is starting with you?',
 cap_mg='Pvt Ltd company-kku kuranjathu randu director-um randu shareholder-um venam. Oru director enkilum India-il thaamasikkunna aalaakanam. Ningalude koode aarundu?')

lst('kt005', 'proprietor', "B", 'ഇൻവെസ്റ്റർക്ക്\nഷെയർ കൊടുക്കാൻ\nഏത് സ്ട്രക്ചർ?', [('പ്രൊപ്രൈറ്റർഷിപ്പ്', 'ഷെയർ ഇറക്കാൻ പറ്റില്ല.'), ('LLP, പാർട്ണർഷിപ്പ്', 'ഇവയ്ക്കും ഷെയർ ഇറക്കാൻ പറ്റില്ല.'), ('പ്രൈവറ്റ് ലിമിറ്റഡ്', 'ഇക്വിറ്റി നിക്ഷേപം സ്വീകരിക്കാൻ ഇതിന് മാത്രം പറ്റും.')],
 'പൈസ വരും മുമ്പ്\nസ്ട്രക്ചർ ശരിയാക്കൂ', CTA_START, theme="tip",
 cap_ml='ഇക്വിറ്റി നിക്ഷേപം സ്വീകരിക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ. പ്രൊപ്രൈറ്റർഷിപ്പിനും LLP-ക്കും പാർട്ണർഷിപ്പിനും ഷെയർ ഇറക്കാൻ കഴിയില്ല. നിങ്ങളുടേത് ഏത് സ്ട്രക്ചർ?',
 cap_en='Only a private limited company can take equity investment. A proprietorship, LLP or partnership cannot issue shares. Which structure is yours?',
 cap_mg='Equity investment sweekarikkaan Pvt Ltd company-kku maathrame pattoo. Proprietorship, LLP, partnership-nu share irakkaan pattilla. Ningaludethu ethu structure?')

lst('kt006', 'salaried', "B", 'PAN-ൽ "കെ. പി. രാജി",\nആധാറിൽ മുഴുവൻ പേര്.\nഒരു ക്വിക്ക് ചെക്ക്', [('PAN', 'അതിലെ പേര് അക്ഷരം തോറും നോക്കൂ.'), ('ആധാർ', 'അതേ പേര്, അതേ ക്രമം ആണോ?'), ('ഇനീഷ്യൽ', 'വ്യത്യാസമുണ്ടെങ്കിൽ അപേക്ഷയ്ക്ക് മുമ്പ് ശരിയാക്കൂ.')],
 'രേഖകളിൽ പേര് ഒന്ന്,\nഅപേക്ഷ വേഗം', CTA_DOCS, theme="tip",
 cap_ml='കേരള ശൈലിയിലെ ഇനീഷ്യലുകൾ കാരണം PAN-ലെയും ആധാറിലെയും പേര് വ്യത്യാസപ്പെടാം. കമ്പനി അപേക്ഷയ്ക്ക് മുമ്പ് രണ്ടിലെയും പേര് ഒന്നാക്കൂ. നിങ്ങളുടെ രണ്ട് രേഖയിലും പേര് ഒന്നാണോ?',
 cap_en='Kerala-style initials often make the name on PAN differ from Aadhaar, and the company application stalls. Match both documents before you apply. Do yours match?',
 cap_mg='Kerala style initial kaaranam PAN-ileyum Aadhaar-ileyum peru vyathyaasappedaam. Company apeksha-kku mumpu randum onnaakku. Ningalude randu rekhayilum peru onnaano?')

lst('kt007', 'solo', "B", 'ഒറ്റയ്ക്കാണോ?\nകമ്പനി തുടങ്ങാൻ\n3 ഉത്തരം', [('ഒരാൾ മതി', 'വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം.'), ('മൂലധനം', 'മിനിമം പെയ്ഡ്-അപ്പ് മൂലധനം ആവശ്യമില്ല.'), ('സമയം', 'ഏകദേശം ഏഴ് മുതൽ പതിനഞ്ച് പ്രവൃത്തി ദിവസം.')],
 'ഒറ്റയ്ക്കും\nകമ്പനി ഉടമ', CTA_START, theme="tip",
 cap_ml='ഒറ്റയ്ക്ക് തുടങ്ങുന്നവർക്ക് വൺ പേഴ്സൺ കമ്പനി (OPC) തുടങ്ങാം. മിനിമം മൂലധനം വേണ്ട. രജിസ്ട്രേഷന് ഏകദേശം 7-15 പ്രവൃത്തി ദിവസം. നിങ്ങൾ ഒറ്റയ്ക്കാണോ തുടങ്ങുന്നത്?',
 cap_en='Starting alone? You can form a One Person Company (OPC). No minimum paid-up capital, and registration takes about 7-15 working days. Are you a solo founder?',
 cap_mg='Ottaykku thudangunnavarkku One Person Company (OPC) thudangaam. Minimum capital venda. Registration-nu 7-15 working days. Ningal ottaykkaano?')

lst('kt008', 'nri', "B", 'ഗൾഫിൽ ഇരുന്ന്\nനാട്ടിൽ കമ്പനി:\n3 ഉത്തരം', [('ഡയറക്ടർ ആകാമോ?', 'NRI-ക്ക് ഡയറക്ടർ ആകാം.'), ('ഷെയർ എടുക്കാമോ?', 'ഷെയർഹോൾഡറും ആകാം.'), ('ഒരു നിബന്ധന', 'ബോർഡിൽ ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ വേണം.')],
 'ദൂരം തടസ്സമല്ല', CTA_START, theme="tip",
 cap_ml='NRI-ക്ക് ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിയിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. പക്ഷേ ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാളാകണം. നിങ്ങൾ ഏത് രാജ്യത്താണ്?',
 cap_en='NRIs can be directors and shareholders of an Indian private limited company, but at least one director must be resident in India. Which country are you in?',
 cap_mg='NRI-kku Pvt Ltd company-il director-um shareholder-um aakaam. Pakshe oru director enkilum India-il thaamasikkunna aalaakanam. Ningal ethu raajyathaanu?')

lst('kt009', 'freelancer', "B", 'ഈ വർഷം\nവരുമാനം പൂജ്യം.\nഫയലിംഗ് വേണോ?', [('വേണം', 'വരുമാനം ഇല്ലെങ്കിലും വാർഷിക ഫയലിംഗ് നിർബന്ധം.'), ('വൈകിയാൽ', 'ഓരോ ഫോമിനും ദിവസം നൂറ് രൂപ ലേറ്റ് ഫീ.'), ('ട്രിക്ക്', 'ഫയലിംഗ് തീയതികൾ ഇന്ന് തന്നെ കലണ്ടറിൽ ഇടൂ.')],
 'ബിസിനസ് ഉറങ്ങിയാലും\nഫയലിംഗ് ഉണരണം', CTA_AFTER, theme="tip",
 cap_ml='വരുമാനം ഇല്ലാത്ത വർഷവും കമ്പനിക്ക് വാർഷിക ഫയലിംഗ് നിർബന്ധമാണ്. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ. നിങ്ങളുടെ ഫയലിംഗ് കഴിഞ്ഞോ?',
 cap_en='Annual filings are due even in a year with zero revenue. Filing late costs a late fee of 100 rupees a day per form. Are your filings done?',
 cap_mg='Varumaanam illaatha varshavum annual filing nirbandham. Vaikiyaal oro form-num divasam 100 roopa late fee. Ningalude filing kazhinjo?')

lst('kt010', 'proprietor', "B", 'INC-20A\n180 ദിവസം കടന്നാൽ\nഎത്ര പിഴ?', [('കമ്പനിക്ക്', 'അമ്പതിനായിരം രൂപ പിഴ.'), ('ഓരോ ഓഫീസർക്കും', 'ദിവസം ആയിരം രൂപ, പരമാവധി ഒരു ലക്ഷം.'), ('ട്രിക്ക്', 'ബിസിനസ് തുടങ്ങിയാൽ ഉടൻ ഫയൽ ചെയ്യൂ.')],
 'ഒരു ഫോം,\nഒരുപാട് പിഴ', CTA_AFTER, theme="tip",
 cap_ml='INC-20A ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തില്ലെങ്കിൽ കമ്പനിക്ക് 50,000 രൂപയും ഓരോ ഓഫീസർക്കും ദിവസം 1,000 രൂപയും (പരമാവധി 1 ലക്ഷം) പിഴ. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര ദിവസമായി?',
 cap_en='Miss INC-20A within 180 days of incorporation and the penalty is 50,000 rupees on the company plus 1,000 rupees a day for each officer in default, up to 1 lakh. How old is your company?',
 cap_mg='INC-20A 180 divasathinullil file cheythillenkil company-kku 50,000 roopa, oro officer-num divasam 1,000 roopa (max 1 lakh) pizha. Ningalude company-kku ethra divasamaayi?')
