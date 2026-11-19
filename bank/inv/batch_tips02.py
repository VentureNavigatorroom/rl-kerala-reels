# Tips and tricks 02 (20 Nov, refill to 10 tips). theme="tip". Facts only from topics.FACTS_INV. Never investment advice or returns.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING = topics.CTA_INVEST, topics.CTA_TERMSHEET, topics.CTA_FUNDING

lst('vt004', 'founder_raising', "B", 'ഇൻവെസ്റ്റ്മെന്റ്\nരേഖകൾ: ശരിയായ\nക്രമം', [('ഒന്ന്: ടേം ഷീറ്റ്', 'ഡീലിന്റെ ചട്ടക്കൂട്, മിക്കതും ബൈൻഡിംഗ് അല്ല.'), ('രണ്ട്: SSA', 'ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്: പണം, ഷെയർ.'), ('മൂന്ന്: SHA', 'ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്: അവകാശങ്ങൾ.')],
 'ക്രമം തെറ്റിയാൽ\nഡീൽ വൈകും', CTA_TERMSHEET, theme="tip",
 cap_ml='ഇൻവെസ്റ്റ്മെന്റിന്റെ രേഖകൾ ഈ ക്രമത്തിൽ: ടേം ഷീറ്റ്, പിന്നെ ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്, പിന്നെ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='Investment paperwork in order: term sheet, then the share subscription agreement (SSA), then the shareholders\' agreement (SHA). Which stage are you at?',
 cap_mg='Investment documents ee kramathil: term sheet, pinne SSA, pinne SHA. Ningal ethu stage-il aanu?')

lst('vt005', 'angel', "B", 'SHA ഒപ്പിട്ടു.\nഅവകാശം ഉറപ്പായോ?\nഒരു ചെക്ക്', [('ബോർഡ് സീറ്റ്', 'ആർട്ടിക്കിൾസിൽ എഴുതിയിട്ടുണ്ടോ?'), ('റൈറ്റ് ഓഫ് ഫസ്റ്റ് റെഫ്യൂസൽ', 'ഷെയർ വിൽക്കും മുമ്പ് ആദ്യ അവസരം: ആർട്ടിക്കിൾസിൽ?'), ('ടാഗ്, ഡ്രാഗ്', 'ആർട്ടിക്കിൾസ് മാറ്റിയില്ലെങ്കിൽ കമ്പനിക്ക് ബാധകമല്ല.')],
 'SHA പോരാ,\nആർട്ടിക്കിൾസും മാറ്റണം', CTA_INVEST, theme="tip",
 cap_ml='SHA-യിലെ അവകാശങ്ങൾ കമ്പനിക്ക് ബാധകമാകാൻ ആർട്ടിക്കിൾസ് ഓഫ് അസോസിയേഷനിലും എഴുതണം. ബോർഡ് സീറ്റ്, ഷെയർ കൈമാറ്റ നിയന്ത്രണം, ടാഗ്-ഡ്രാഗ് എല്ലാം. നിങ്ങളുടെ ആർട്ടിക്കിൾസ് മാറ്റിയോ?',
 cap_en='Rights in a shareholders\' agreement bind the company only if they are written into the Articles of Association: board seat, transfer limits, right of first refusal, tag-along and drag-along. Were your articles amended?',
 cap_mg='SHA-yile rights company-kku baadhakamaakaan Articles of Association-ilum ezhuthanam. Board seat, ROFR, tag-drag ellaam. Ningalude articles maatiyo?')

lst('vt006', 'cofounder_split', "B", 'ഇൻവെസ്റ്റർക്ക്\nഷെയർ കൊടുക്കാമോ?\nഘടന നോക്കൂ', [('പ്രൈവറ്റ് ലിമിറ്റഡ്', 'ഷെയർ ഇറക്കാം, ഇക്വിറ്റി നിക്ഷേപം എടുക്കാം.'), ('LLP', 'ഷെയർ ഇറക്കാൻ പറ്റില്ല.'), ('പാർട്ണർഷിപ്പ്, പ്രൊപ്രൈറ്റർ', 'ഷെയർ എന്ന ഒന്നില്ല.')],
 'ഷെയർ വേണോ?\nകമ്പനി വേണം', CTA_FUNDING, theme="tip",
 cap_ml='ഇക്വിറ്റി നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ കഴിയൂ. LLP, പാർട്ണർഷിപ്പ്, പ്രൊപ്രൈറ്റർഷിപ്പ് ഇവയ്ക്ക് ഷെയർ ഇറക്കാൻ പറ്റില്ല. നിങ്ങളുടെ ബിസിനസ് ഏത് ഘടനയിലാണ്?',
 cap_en='Only a private limited company can take equity investment. An LLP, partnership or proprietorship cannot issue shares. What structure is your business?',
 cap_mg='Equity investment edukkaan private limited company-kku maathrame kazhiyoo. LLP, partnership, proprietorship-nu share irakkaan pattilla. Ningalude business ethu structure?')

lst('vt007', 'nri_investor', "B", 'ഗൾഫിലെ ബന്ധു\nനിക്ഷേപിക്കുന്നു:\n2 വഴികൾ', [('റിപാട്രിയേഷൻ', 'ഫെയർ വാല്യുവിൽ കുറയരുത്, മുപ്പത് ദിവസത്തിനുള്ളിൽ FC-GPR.'), ('നോൺ-റിപാട്രിയേഷൻ', 'ആഭ്യന്തര നിക്ഷേപം പോലെ, FC-GPR വേണ്ട.'), ('ട്രിക്ക്', 'പണം വരും മുമ്പ് ഏത് വഴി എന്ന് തീരുമാനിക്കൂ.')],
 'വഴി ആദ്യം,\nപണം പിന്നീട്', CTA_INVEST, theme="tip",
 cap_ml='NRI റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ നിക്ഷേപിച്ചാൽ ഷെയർ ഫെയർ വാല്യുവിൽ കുറയരുത്: വാല്യുവേഷൻ റിപ്പോർട്ടും അലോട്ട്മെന്റ് കഴിഞ്ഞ് 30 ദിവസത്തിനുള്ളിൽ RBI-ക്ക് FC-GPR-ഉം വേണം. നോൺ-റിപാട്രിയേഷൻ ആഭ്യന്തരമായി കണക്കാക്കും. ഏത് വഴിയാണ് നിങ്ങളുടേത്?',
 cap_en='An NRI investing on a repatriation basis must issue shares at not below fair value (valuation report) and an FC-GPR filing with RBI within 30 days of allotment. Non-repatriation investment is treated as domestic. Which route is yours?',
 cap_mg='NRI repatriation basis-il nikshepichaal fair value report-um 30 divasathinullil FC-GPR-um venam. Non-repatriation domestic aayi kanakkaakkum. Ethu vazhi?')

lst('vt008', 'family_money', "B", '60 ദിവസം കഴിഞ്ഞു,\nഷെയർ നൽകിയില്ല.\nഇനി?', [('റീഫണ്ട്', 'അടുത്ത പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ പണം തിരികെ നൽകണം.'), ('വൈകിയാൽ', 'പന്ത്രണ്ട് ശതമാനം പലിശയോടെ.'), ('ഒഴിവാക്കാൻ', 'പണം വരും മുമ്പ് രേഖകൾ റെഡിയാക്കൂ.')],
 'ബന്ധുവിന്റെ പണവും\nതീയതി നോക്കും', CTA_FUNDING, theme="tip",
 cap_ml='നിക്ഷേപ പണം കിട്ടി 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്തില്ലെങ്കിൽ അടുത്ത 15 ദിവസത്തിനുള്ളിൽ തിരികെ നൽകണം, ഇല്ലെങ്കിൽ 12% പലിശ. ബന്ധുവിന്റെ പണത്തിനും ഇതേ നിയമം. നിങ്ങളുടെ പണം വന്നിട്ട് എത്ര ദിവസമായി?',
 cap_en='If shares are not allotted within 60 days of receiving investment money, it must be refunded within the next 15 days, or with 12% interest. Family money follows the same rule. How many days since your money came in?',
 cap_mg='Panam kitti 60 divasathinullil share allot cheythillenkil adutha 15 divasathinullil thirike kodukkanam, illenkil 12% palisha. Bandhuvinte panathinum ithe niyamam. Ethra divasamaayi?')

lst('vt009', 'angel', "B", 'ഏഞ്ചൽ ടാക്സ്\nഇപ്പോഴും ഉണ്ടോ?\nഒരു അപ്ഡേറ്റ്', [('ഏഞ്ചൽ ടാക്സ്', 'സാമ്പത്തിക വർഷം 2024-25 മുതൽ എല്ലാവർക്കും നിർത്തലാക്കി.'), ('മാറാത്തത്', 'ഷെയർ, എഗ്രിമെന്റ്, ഫയലിംഗുകൾ അതേപടി വേണം.'), ('NRI നിക്ഷേപം', 'ഫെയർ വാല്യു റിപ്പോർട്ട് ഇപ്പോഴും വേണം.')],
 'ടാക്സ് പോയി,\nപേപ്പർ പോയില്ല', CTA_INVEST, theme="tip",
 cap_ml='ഏഞ്ചൽ ടാക്സ് 2024-25 സാമ്പത്തിക വർഷം മുതൽ എല്ലാ നിക്ഷേപകർക്കും നിർത്തലാക്കി. പക്ഷേ ഷെയർ അലോട്ട്മെന്റും എഗ്രിമെന്റും ഫയലിംഗും ഇപ്പോഴും വേണം. ഇത് നിങ്ങൾക്ക് പുതിയ അറിവാണോ?',
 cap_en='Angel tax was abolished for all investors from FY 2024-25. Share allotment, agreements and filings are still needed, and NRI investment on a repatriation basis still needs a fair value report. Was this news to you?',
 cap_mg='Angel tax 2024-25 muthal ellaa investors-num nirthalaakki. Pakshe share allotment-um agreement-um filing-um ippozhum venam. Ithu puthiya arivaano?')

lst('vt010', 'founder_raising', "B", 'പ്രൈവറ്റ്\nപ്ലേസ്മെന്റ്:\n3 രേഖകൾ', [('സ്പെഷ്യൽ റെസല്യൂഷൻ', 'ഷെയർഹോൾഡർമാരുടെ അംഗീകാരം ആദ്യം.'), ('PAS-4', 'നിക്ഷേപകന് നൽകുന്ന ഓഫർ ലെറ്റർ.'), ('PAS-3', 'അലോട്ട്മെന്റ് കഴിഞ്ഞ് പതിനഞ്ച് ദിവസത്തിനുള്ളിൽ ഫയൽ.')],
 'മൂന്ന് രേഖ,\nഒരു ക്ലീൻ റൗണ്ട്', CTA_FUNDING, theme="tip",
 cap_ml='പ്രൈവറ്റ് പ്ലേസ്മെന്റിൽ ഷെയർ ഇറക്കാൻ: സ്പെഷ്യൽ റെസല്യൂഷൻ, PAS-4 ഓഫർ ലെറ്റർ, അലോട്ട്മെന്റ് കഴിഞ്ഞ് 15 ദിവസത്തിനുള്ളിൽ PAS-3. ഇതിൽ ഏതാണ് നിങ്ങൾക്ക് പുതിയത്?',
 cap_en='Issuing shares by private placement needs a special resolution, a PAS-4 offer letter to the investor, and PAS-3 filed within 15 days of allotment. Which one is new to you?',
 cap_mg='Private placement-il share irakkaan: special resolution, PAS-4 offer letter, allotment kazhinju 15 divasathinullil PAS-3. Ithil ethaanu puthiyathu?')
