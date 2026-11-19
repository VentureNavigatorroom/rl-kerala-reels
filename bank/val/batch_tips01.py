# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

lst('qvt001', 'raising_round', "B", 'വാല്യുവേഷൻ\nവേണ്ട 5\nസന്ദർഭങ്ങൾ', [('നിക്ഷേപം', 'പുതിയ ഷെയർ ഇറക്കുമ്പോൾ.'), ('ഇസോപ്പ്', 'ജീവനക്കാർക്ക് ഷെയർ നൽകുമ്പോൾ.'), ('കൈമാറ്റം', 'ഷെയർ വിൽക്കുമ്പോൾ, പങ്കാളി പോകുമ്പോൾ.')],
 'ഈ നിമിഷങ്ങളിൽ\nഊഹം വേണ്ട', CTA_VALUATION, theme="tip",
 cap_ml='നിക്ഷേപം, ഇസോപ്പ്, ഷെയർ കൈമാറ്റം, പങ്കാളി പുറത്തുപോകൽ, NRI നിക്ഷേപം എന്നിവയ്ക്ക് വാല്യുവേഷൻ വേണം. നിങ്ങൾക്ക് ഏതിനാണ്?',
 cap_en='You need a valuation when raising, issuing ESOPs, transferring shares, when a partner exits, and for NRI or foreign investment. Which one is coming up for you?',
 cap_mg='Investment, ESOP, share transfer, partner exit, NRI investment ivaykku valuation venam. Ningalkku ethinaanu?')

lst('qvt002', 'nri_share_issue', "B", 'ആര് ഒപ്പിടണം?\nവാല്യുവേഷൻ\nഒരു ടിപ്പ്', [('NRI നിക്ഷേപം', 'CA, സെബി മർച്ചന്റ് ബാങ്കർ, കോസ്റ്റ് അക്കൗണ്ടന്റ്.'), ('പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റ്', 'രജിസ്റ്റേർഡ് വാല്യുവർ.'), ('ട്രിക്ക്', 'ആവശ്യം ആദ്യം പറയൂ.')],
 'ശരിയായ ഒപ്പ്,\nശരിയായ റിപ്പോർട്ട്', CTA_WORTH, theme="tip",
 cap_ml='NRI അല്ലെങ്കിൽ വിദേശ നിക്ഷേപത്തിന് CA, സെബി മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ്. പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന് രജിസ്റ്റേർഡ് വാല്യുവർ. നിങ്ങളുടെ ആവശ്യം ഏതാണ്?',
 cap_en='NRI or foreign investment needs certification by a CA, SEBI-registered merchant banker or cost accountant; a preferential allotment needs a registered valuer. Which is your case?',
 cap_mg='NRI investment-nu CA, SEBI merchant banker allenkil cost accountant. Preferential allotment-nu registered valuer. Ningalude aavashyam ethaanu?')

lst('qvt003', 'partner_exit', "B", 'വാല്യുവേഷൻ\nരീതികൾ:\n3 എണ്ണം', [('ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ', 'ഭാവി വരുമാനം അടിസ്ഥാനം.'), ('താരതമ്യം', 'സമാന കമ്പനികളും ഇടപാടുകളും.'), ('നെറ്റ് അസറ്റ്', 'ആസ്തി അടിസ്ഥാനം.')],
 'ഒരു തീയതി,\nഒരു ആവശ്യം', CTA_VALUATION, theme="tip",
 cap_ml='വാല്യുവേഷൻ രീതികൾ: ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, സമാന കമ്പനികളുമായുള്ള താരതമ്യം, നെറ്റ് അസറ്റ് വാല്യു. ഓരോ റിപ്പോർട്ടും ഒരു ആവശ്യത്തിനും തീയതിക്കുമാണ്. നിങ്ങളുടെ ബിസിനസ്സിന് ഏത് യോജിക്കും?',
 cap_en='Valuation methods: discounted cash flow, comparable companies and deals, and net asset value. Each report is for one purpose and one date. Which fits your business?',
 cap_mg='Valuation reethikal: DCF, comparables, net asset value. Oro report-um oru aavashyathinum oru date-num. Ningalude business-nu ethu cheru?')

