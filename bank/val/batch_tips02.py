# Tips and tricks 02 (20 Nov, refill to 10 unposted tips per topic). theme="tip". Facts only from topics.FACTS_VAL. Never a value or a fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

lst('qvt004', 'esop_plan', "B", 'വാല്യുവേഷൻ റിപ്പോർട്ട്\nകൈയിൽ കിട്ടിയാൽ\nആദ്യം നോക്കേണ്ട 3', [('ആവശ്യം', 'ഏത് കാര്യത്തിനാണ് റിപ്പോർട്ട് എന്ന് എഴുതിയിട്ടുണ്ടോ?'), ('തീയതി', 'ഏത് ദിവസത്തെ മൂല്യമാണ് എന്ന് വ്യക്തമാണോ?'), ('രീതി', 'ഏത് അംഗീകൃത രീതി ഉപയോഗിച്ചു എന്ന് പറയുന്നുണ്ടോ?')],
 'മൂന്നും ഇല്ലെങ്കിൽ\nചോദിക്കൂ', CTA_VALUATION, theme="tip",
 cap_ml='ഒരു വാല്യുവേഷൻ റിപ്പോർട്ട് ഒരു പ്രത്യേക ആവശ്യത്തിനും ഒരു പ്രത്യേക തീയതിക്കുമാണ്. ആവശ്യം, തീയതി, രീതി: ഈ മൂന്നും റിപ്പോർട്ടിൽ നോക്കൂ. നിങ്ങളുടെ റിപ്പോർട്ടിൽ മൂന്നും ഉണ്ടോ?',
 cap_en='A valuation report is for one purpose and one date. Check that it states the purpose, the valuation date and the method used. Does yours show all three?',
 cap_mg='Valuation report oru aavashyathinum oru theeyathikkum aanu. Aavashyam, theeyathi, reethi: moonnum report-il nokku. Ningalude report-il moonnum undo?')

lst('qvt005', 'raising_round', "B", 'ലാഭം ഇല്ല,\nവരുമാനം കുറവ്.\nവാല്യുവേഷൻ പറ്റുമോ?', [('പറ്റും', 'ആദ്യഘട്ട സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും പ്രൊജക്ഷനും ആണ് ആശ്രയം.'), ('താരതമ്യം', 'സമാന കമ്പനികളും സമാന ഇടപാടുകളും.'), ('ട്രിക്ക്', 'പ്രൊജക്ഷനിലെ ഓരോ അനുമാനവും എഴുതി വെക്കൂ.')],
 'ലാഭം പിന്നെ,\nകണക്ക് ഇപ്പോൾ', CTA_WORTH, theme="tip",
 cap_ml='ലാഭമില്ലാത്ത ആദ്യഘട്ട സ്റ്റാർട്ടപ്പിനും വാല്യുവേഷൻ ചെയ്യാം. സമാന കമ്പനികളുമായുള്ള താരതമ്യവും പ്രൊജക്ഷനുമാണ് അടിസ്ഥാനം. നിങ്ങളുടെ സ്റ്റാർട്ടപ്പ് ലാഭത്തിലാണോ?',
 cap_en='An early startup with no profit can still be valued: comparables and projections carry most of the weight. Write down every assumption. Is your startup profitable yet?',
 cap_mg='Laabham illaatha early startup-num valuation cheyyaam. Comparables-um projection-um aanu adisthaanam. Ningalude startup laabhathilaano?')

lst('qvt006', 'partner_exit', "B", 'വാല്യുവേഷൻ:\nപലരും മറക്കുന്ന\n3 സന്ദർഭം', [('ബൈബാക്ക്', 'കമ്പനി സ്വന്തം ഷെയർ തിരികെ വാങ്ങുമ്പോൾ.'), ('മെർജർ', 'രണ്ട് കമ്പനികൾ ഒന്നാകുമ്പോൾ.'), ('NRI ഷെയർ', 'NRI നിക്ഷേപത്തിന് ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല.')],
 'ഫണ്ടിംഗിന് മാത്രമല്ല\nവാല്യുവേഷൻ', CTA_VALUATION, theme="tip",
 cap_ml='ഫണ്ടിംഗിന് മാത്രമല്ല വാല്യുവേഷൻ: ഷെയർ ബൈബാക്ക്, മെർജർ, NRI നിക്ഷേപം എന്നിവയ്ക്കും വേണം. ഇതിൽ ഏതാണ് നിങ്ങളുടെ മുന്നിൽ?',
 cap_en='Valuation is not only for fundraising: share buy-backs, mergers and NRI investment need it too. Which one is coming up for you?',
 cap_mg='Funding-nu maathramalla valuation: buyback, merger, NRI nikshepam ellaathinum venam. Ithil ethaanu ningalude munnil?')

lst('qvt007', 'partner_exit', "B", 'വാല്യുവറെ കാണും\nമുമ്പ് റെഡിയാക്കേണ്ടത്:\nഒരു ചെക്ക്ലിസ്റ്റ്', [('ആവശ്യവും തീയതിയും', 'എന്തിന്, ഏത് ദിവസത്തേക്ക് എന്ന് ആദ്യം പറയൂ.'), ('പ്രൊജക്ഷൻ', 'വരുമാനവും ചെലവും, അനുമാനങ്ങൾ സഹിതം.'), ('ആസ്തി ലിസ്റ്റ്', 'കമ്പനിയുടെ പേരിലുള്ള ആസ്തികൾ.')],
 'റെഡിയായി ചെന്നാൽ\nസമയം പകുതി', CTA_VALUATION, theme="tip",
 cap_ml='വാല്യുവേഷന് മുമ്പ്: ആവശ്യവും തീയതിയും, അനുമാനങ്ങളോടെ പ്രൊജക്ഷൻ, കമ്പനിയുടെ ആസ്തി ലിസ്റ്റ്. ഇതിൽ ഏതാണ് നിങ്ങളുടെ കൈയിൽ ഇല്ലാത്തത്?',
 cap_en='Before meeting a valuer, have three things ready: the purpose and date, projections with assumptions, and a list of the company\'s assets. Which one are you missing?',
 cap_mg='Valuer-ne kaanunnathinu mumpu: aavashyavum theeyathiyum, projection, company-yude aasthi list. Ithil ethaanu ningalude kaiyil illaathathu?')

lst('qvt008', 'esop_plan', "B", 'ഇസോപ്പ് ഗ്രാന്റ്:\nതീയതി കുറിച്ചോ?\nഒരു റിമൈൻഡർ', [('ഗ്രാന്റ് ദിവസം', 'ഓരോ ഗ്രാന്റിനും ആ തീയതിയിലെ വാല്യുവേഷൻ.'), ('അടുത്ത ബാച്ച്', 'കമ്പനി വളർന്നെങ്കിൽ പുതിയ കണക്ക്.'), ('ട്രിക്ക്', 'ഗ്രാന്റുകൾ ഒരേ ദിവസങ്ങളിൽ കൂട്ടി വെക്കൂ.')],
 'ടീമിന് ഷെയർ,\nകലണ്ടറിൽ തീയതി', CTA_VALUATION, theme="tip",
 cap_ml='ഇസോപ്പ് നൽകുമ്പോൾ ഓരോ ഗ്രാന്റിനും ആ തീയതിയിലെ വാല്യുവേഷൻ വേണം. ഗ്രാന്റുകൾ ഒരേ ദിവസങ്ങളിൽ കൂട്ടിവെച്ചാൽ ജോലി കുറയും. നിങ്ങളുടെ അടുത്ത ഗ്രാന്റ് എപ്പോൾ?',
 cap_en='Every ESOP grant needs a valuation as of that grant date. Batch grants on the same dates to keep it simple. When is your next grant?',
 cap_mg='ESOP kodukkumbol oro grant-num aa theeyathiyile valuation venam. Grant-ukal ore divasangalil koottivechaal joli kurayum. Adutha grant eppol?')

lst('qvt009', 'nri_share_issue', "B", 'NRI ബന്ധു\nഷെയർ എടുക്കുന്നു.\nഎന്ത് നോക്കണം?', [('താഴ്ന്ന പരിധി', 'റിപാട്രിയേഷൻ നിക്ഷേപമെങ്കിൽ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല.'), ('രീതി', 'അംഗീകൃത രീതിയിൽ ചെയ്ത വാല്യുവേഷൻ.'), ('ക്രമം', 'റിപ്പോർട്ട് ആദ്യം, പണം അയക്കൽ പിന്നെ.')],
 'ബന്ധുവായാലും\nഫെയർ വാല്യു', CTA_WORTH, theme="tip",
 cap_ml='NRI ബന്ധു റിപാട്രിയേഷൻ അടിസ്ഥാനത്തിൽ ഷെയർ എടുക്കുമ്പോൾ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാൻ പാടില്ല. അംഗീകൃത രീതിയിലുള്ള റിപ്പോർട്ട് ആദ്യം. നിങ്ങളുടെ ബന്ധു ഏത് രാജ്യത്താണ്?',
 cap_en='When an NRI relative takes shares in your Kerala company on a repatriation basis, the shares cannot go below fair value. Get the valuation by an accepted method first. Where does your relative live?',
 cap_mg='NRI bandhu repatriation basis-il share edukkumbol fair value-il thaazhe kodukkaan paadilla. Report aadyam, panam ayakkal pinne. Ningalude bandhu ethu raajyathaanu?')

lst('qvt010', 'share_transfer', "B", 'വാല്യുവേഷൻ:\n3 മിഥ്യകൾ\n30 സെക്കൻഡിൽ', [('ഒരിക്കൽ മതി?', 'ഇല്ല. ഓരോ റിപ്പോർട്ടും ഒരു തീയതിക്ക്.'), ('കുടുംബമായാൽ വേണ്ട?', 'ഷെയർ കൈമാറ്റത്തിന് കുടുംബത്തിലും വേണ്ടിവരാം.'), ('ആര് ഒപ്പിട്ടാലും മതി?', 'പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന് രജിസ്റ്റേർഡ് വാല്യുവർ.')],
 'മിഥ്യ മാറ്റൂ,\nരേഖ നേടൂ', CTA_WORTH, theme="tip",
 cap_ml='വാല്യുവേഷനെക്കുറിച്ചുള്ള മൂന്ന് മിഥ്യകൾ: ഒരിക്കൽ ചെയ്താൽ മതി, കുടുംബത്തിൽ വേണ്ട, ആര് ഒപ്പിട്ടാലും മതി. മൂന്നും തെറ്റാണ്. ഇതിൽ ഏതാണ് നിങ്ങൾ കേട്ടത്?',
 cap_en='Three valuation myths: one report lasts forever, family deals need none, anyone can sign. All three are wrong. Which one have you heard?',
 cap_mg='Valuation-ine kurichu moonnu mithyakal: orikkal mathi, kudumbathil venda, aaru oppittaalum mathi. Moonnum thettaanu. Ithil ethaanu ningal kettathu?')
