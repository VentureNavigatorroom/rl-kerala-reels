# Data room batch 01 (28 Nov): first 3D duo reels. Facts only from topics.FACTS_DR. Never promise funding, an investor, a valuation or a timeline; no fees. Names invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE

duo('drd001', 'investor_asked', 'A', 'office', 'ഇൻവെസ്റ്റർ പറഞ്ഞു:\n"7 ദിവസത്തിനുള്ളിൽ\nരേഖകൾ"', [('A', 'wide', 'രാഹുലേ, ഇൻവെസ്റ്റർ ഒരാഴ്ചയ്ക്കുള്ളിൽ എല്ലാ രേഖകളും ചോദിച്ചു. എവിടെ തുടങ്ങും?'), ('V', 'V', 'നേഹ, വാട്സാപ്പിലും ഇമെയിലിലും ആയി എല്ലാം ചിതറിക്കിടക്കുകയാണ്.'), ('A', 'A', 'അതാണ് ഡാറ്റ റൂം. എല്ലാ രേഖകളും ഒരു സുരക്ഷിത ഓൺലൈൻ ഫോൾഡറിൽ.'), ('V', 'V', 'രജിസ്ട്രേഷൻ, കണക്ക്, കരാർ, ഫയലിംഗ്. ഓരോന്നിനും ഒരു ഫോൾഡർ.'), ('A', 'wide', 'ഇല്ലാത്തത് ഏതൊക്കെ എന്ന് ആദ്യം ലിസ്റ്റ് ചെയ്യാം.'), ('V', 'wide', 'ചിതറിയ രേഖ, ചിതറിയ വിശ്വാസം.')],
 'ഒരു ഫോൾഡർ,\nഎല്ലാ രേഖയും', CTA_DATAROOM, theme='faq',
 cap_ml='ഇൻവെസ്റ്റർ രേഖകൾ ചോദിക്കുമ്പോൾ എല്ലാം ഒരു സുരക്ഷിത ഓൺലൈൻ ഫോൾഡറിൽ വേണം: രജിസ്ട്രേഷൻ, കണക്ക്, കരാർ, ഫയലിംഗ്. നിങ്ങളുടെ രേഖകൾ ഇപ്പോൾ എവിടെയാണ്?',
 cap_en='An investor wants every document within a week, and it is all scattered across WhatsApp and email. A data room puts registration, accounts, agreements and filings in one secure online folder. Where are your documents right now?',
 cap_mg='Investor rekhakal chodikkumbol ellaam oru secure online folder-il venam: registration, accounts, agreements, filings. Ningalude rekhakal ippol evideyaanu?')

duo('drd002', 'raising_first', 'B', 'library', 'ഡാറ്റ റൂം എന്നാൽ\nപിച്ച് ഡെക്ക്\nമാത്രമല്ല', [('A', 'wide', 'അനൂപേ, പിച്ച് ഡെക്ക് റെഡി. ഇനി ഡാറ്റ റൂമിൽ അത് മാത്രം ഇട്ടാൽ മതിയല്ലോ?'), ('V', 'V', 'ഗ്രീഷ്മേ, ഇല്ല. ഡെക്ക് താൽപര്യം ഉണ്ടാക്കും, ഡാറ്റ റൂം അത് തെളിയിക്കും.'), ('A', 'A', 'അപ്പോ വേറെ എന്തൊക്കെ?'), ('V', 'V', 'ക്യാപ് ടേബിൾ, കരാറുകൾ, കണക്കുകൾ, പ്രൊജക്ഷൻ, GST, ROC ഫയലിംഗുകൾ, ട്രേഡ്മാർക്ക്.'), ('A', 'wide', 'ഡെക്ക് പറയുന്നത് രേഖകൾ തെളിയിക്കണം.'), ('V', 'wide', 'ഡെക്ക് വാഗ്ദാനം, ഡാറ്റ റൂം തെളിവ്.')],
 'ഡെക്ക് വാഗ്ദാനം,\nഡാറ്റ റൂം തെളിവ്', CTA_DATAROOM, theme='faq',
 cap_ml='പിച്ച് ഡെക്ക് താൽപര്യം ഉണ്ടാക്കും; ഡാറ്റ റൂം അത് തെളിയിക്കും. ക്യാപ് ടേബിൾ, കരാറുകൾ, കണക്കുകൾ, പ്രൊജക്ഷൻ, ഫയലിംഗുകൾ എല്ലാം വേണം. നിങ്ങളുടെ ഡെക്കിന് പിന്നിൽ രേഖകൾ റെഡിയാണോ?',
 cap_en='A pitch deck creates interest; the data room proves it. Investors check the cap table, agreements, accounts, projections, GST and ROC filings and trademarks behind the deck. Are your documents ready to back yours?',
 cap_mg='Pitch deck thaalparyam undaakkum; data room athu theliyikkum. Cap table, agreements, accounts, projection, filings ellaam venam. Ningalude deck-inu pinnil rekhakal ready aano?')

duo('drd003', 'messy_docs', 'A', 'rooftop', 'ROC ഫയലിംഗ്\nരണ്ട് വർഷം പെൻഡിംഗ്.\nഇൻവെസ്റ്റർ കണ്ടു', [('A', 'wide', 'ശ്യാമേ, ഇൻവെസ്റ്റർ MCA-യിൽ നോക്കി. നമ്മുടെ ROC ഫയലിംഗ് രണ്ട് വർഷം ബാക്കി!'), ('V', 'V', 'ആര്യേ, ബിസിനസ് ചെറുതായിരുന്നു. അതുകൊണ്ട് വിട്ടുപോയി.'), ('A', 'A', 'ഡ്യൂ ഡിലിജൻസിൽ ഇത് ആദ്യം കാണുന്ന റെഡ് ഫ്ലാഗുകളിൽ ഒന്നാണ്.'), ('V', 'V', 'അപ്പോ ആദ്യം പെൻഡിംഗ് ഫയലിംഗ് തീർക്കണം.'), ('A', 'wide', 'അതെ. GST റിട്ടേണുകളും ഒത്തുനോക്കണം.'), ('V', 'wide', 'പിന്നത്തേക്ക് വെച്ചത് മുന്നിൽ വരും.')],
 'പെൻഡിംഗ് ഫയലിംഗ്\n= റെഡ് ഫ്ലാഗ്', CTA_DILIGENCE, theme='crm',
 cap_ml='ഡ്യൂ ഡിലിജൻസിൽ ഇൻവെസ്റ്റർ ആദ്യം നോക്കുന്നത് പെൻഡിംഗ് ROC, GST ഫയലിംഗുകളാണ്. ഫണ്ടിംഗിന് മുമ്പ് അവ തീർക്കൂ. നിങ്ങളുടെ ഫയലിംഗുകൾ അപ്ഡേറ്റ് ആണോ?',
 cap_en='The investor checked MCA records and found two years of pending ROC filings. Pending ROC or GST filings are among the first red flags in due diligence, so clear them before you raise. Are your filings up to date?',
 cap_mg='Due diligence-il investor aadyam nokkunnathu pending ROC, GST filings aanu. Funding-inu mumpu avayokke theerkku. Ningalude filings update aano?')

duo('drd004', 'loan_dd', 'B', 'hospital', 'ബാങ്ക് ലോണിനും\nരേഖകളുടെ\nഫോൾഡർ വേണം', [('A', 'wide', 'ജോസഫേ, ക്ലിനിക്ക് വികസിപ്പിക്കാൻ ബാങ്ക് ലോൺ. അവർ ഒരുപാട് രേഖകൾ ചോദിക്കുന്നു.'), ('V', 'V', 'ലക്ഷ്മീ, ഇൻവെസ്റ്റർക്ക് മാത്രമല്ല, ലോണിനും ഒരു ഡാറ്റ റൂം സഹായിക്കും.'), ('A', 'A', 'അതിൽ എന്തൊക്കെ ഇടണം?'), ('V', 'V', 'കണക്കുകൾ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, പ്രൊജക്ട് റിപ്പോർട്ട്, ഫയലിംഗുകൾ, രജിസ്ട്രേഷൻ.'), ('A', 'wide', 'ഒരിക്കൽ ഒരുക്കിയാൽ ഓരോ ആവശ്യത്തിനും വേഗം അയക്കാം.'), ('V', 'wide', 'ഒരുക്കം ഒരിക്കൽ, ഉപകാരം പലതവണ.')],
 'ഒരുക്കം ഒരിക്കൽ,\nഉപകാരം പലതവണ', CTA_DATAROOM, theme='new',
 cap_ml='ബാങ്ക് ലോണിനും വലിയ ഇടപാടുകൾക്കും ഒരു ഡാറ്റ റൂം സഹായിക്കും: കണക്കുകൾ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, പ്രൊജക്ട് റിപ്പോർട്ട്, ഫയലിംഗുകൾ. നിങ്ങൾ എന്തിനാണ് രേഖകൾ ഒരുക്കുന്നത്?',
 cap_en='A clinic owner applying for an expansion loan is buried in document requests. A data room helps with lenders too: accounts, bank statements, project report, filings and registration, ready to share each time. What are you preparing documents for?',
 cap_mg='Bank loan-inum valiya idapaadukalkkum data room sahaayikkum: accounts, bank statement, project report, filings. Ningal enthinaanu rekhakal orukkunnathu?')

duo('drd005', 'selling_business', 'A', 'beach', 'ബിസിനസ് വിൽക്കാൻ\nആലോചന. വാങ്ങുന്നയാൾ\nആദ്യം ചോദിച്ചത്', [('A', 'wide', 'നിഖിലേ, ഒരാൾ നമ്മുടെ ബിസിനസ് വാങ്ങാൻ താൽപര്യം കാണിച്ചു. ആദ്യം രേഖകൾ ചോദിച്ചു.'), ('V', 'V', 'ദിവ്യേ, വാങ്ങുന്നയാളും ഡ്യൂ ഡിലിജൻസ് ചെയ്യും. ഇൻവെസ്റ്ററെപ്പോലെ തന്നെ.'), ('A', 'A', 'എന്തൊക്കെ നോക്കും?'), ('V', 'V', 'കരാറുകൾ, കണക്കുകൾ, ഫയലിംഗുകൾ, ട്രേഡ്മാർക്ക്, പ്രധാന ക്ലയന്റ് കരാറുകൾ.'), ('A', 'wide', 'അപ്പോ ഡാറ്റ റൂം ആദ്യം, ചർച്ച പിന്നെ.'), ('V', 'wide', 'വൃത്തിയുള്ള രേഖ, ശക്തമായ ചർച്ച.')],
 'രേഖ വൃത്തിയെങ്കിൽ\nചർച്ച ശക്തം', CTA_DILIGENCE, theme='new',
 cap_ml='ബിസിനസ് വിൽക്കുമ്പോഴും പാർട്ണറെ കൊണ്ടുവരുമ്പോഴും ഡ്യൂ ഡിലിജൻസ് ഉണ്ട്. കരാറുകൾ, കണക്കുകൾ, ഫയലിംഗുകൾ, ട്രേഡ്മാർക്ക് ഒരുക്കി വെക്കൂ. നിങ്ങൾ എന്തിനാണ് തയ്യാറെടുക്കുന്നത്?',
 cap_en='A buyer is interested in the business and asks for documents first. Buyers and new partners run due diligence just like investors: agreements, accounts, filings, trademarks and key client contracts. What are you preparing for?',
 cap_mg='Business vilkkumbozhum partner-e konduvarumbozhum due diligence undu. Karaarukal, kanakkukal, filings, trademark orukki vekku. Ningal enthinaanu thayyaaredukkunnathu?')

duo('drd006', 'raising_first', 'B', 'classroom', 'ബ്രാൻഡ് പേര്\nമറ്റൊരാളുടെ\nട്രേഡ്മാർക്ക്!', [('A', 'wide', 'ആദർശേ, ഡാറ്റ റൂം ചെക്ക് ചെയ്യുമ്പോൾ ഇൻവെസ്റ്റർ ഒരു കാര്യം ചോദിച്ചു. ബ്രാൻഡ് നമ്മുടേതാണോ?'), ('V', 'V', 'നിമ്മീ, ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തിട്ടില്ലെങ്കിൽ അത് ഒരു റിസ്ക് ആയി കാണും.'), ('A', 'A', 'ഇപ്പോൾ ചെയ്താൽ മതിയോ?'), ('V', 'V', 'ഫയൽ ചെയ്ത രേഖ ഡാറ്റ റൂമിൽ ഇടാം. IP ഫോൾഡർ ശൂന്യമാകരുത്.'), ('A', 'wide', 'ബ്രാൻഡ് ആണ് പലപ്പോഴും ഏറ്റവും വലിയ മുതൽ.'), ('V', 'wide', 'പേര് നിങ്ങളുടേതെന്ന് രേഖ പറയണം.')],
 'ബ്രാൻഡ് നിങ്ങളുടേതെന്ന്\nരേഖ പറയണം', CTA_DILIGENCE, theme='faq',
 cap_ml='ഡാറ്റ റൂമിൽ IP ഫോൾഡർ ശൂന്യമെങ്കിൽ ഇൻവെസ്റ്റർ അത് റിസ്ക് ആയി കാണും. ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്ത രേഖ ഉൾപ്പെടുത്തൂ. നിങ്ങളുടെ ബ്രാൻഡ് സംരക്ഷിച്ചോ?',
 cap_en='During data room checks the investor asks a simple question: is the brand yours? An empty IP folder with no trademark filed is seen as a risk. Is your brand protected?',
 cap_mg='Data room-il IP folder shoonyamenkil investor athu risk aayi kaanum. Trademark file cheytha rekha ulppeduthu. Ningalude brand samrakshicho?')

duo('drd007', 'unregistered_dr', 'A', 'metro', 'ഇൻവെസ്റ്റർ ഓക്കെ.\nപക്ഷേ ഇപ്പോഴും\nപാർട്ണർഷിപ്പ്', [('A', 'wide', 'കിരണേ, ഇൻവെസ്റ്റർ ഓഹരി എടുക്കാൻ തയ്യാർ. പക്ഷേ നമ്മുടേത് പാർട്ണർഷിപ്പ് ഫേം ആണ്.'), ('V', 'V', 'അഞ്ജലീ, ഇക്വിറ്റി നിക്ഷേപത്തിന് പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം.'), ('A', 'A', 'അപ്പോ ഡാറ്റ റൂം പിന്നെയോ?'), ('V', 'V', 'ആദ്യം കമ്പനി, പിന്നെ ഷെയർ രേഖകൾ, എന്നിട്ട് ഡാറ്റ റൂം. ക്രമം പ്രധാനം.'), ('A', 'wide', 'ഇപ്പോൾ തുടങ്ങിയാൽ സമയം ലാഭിക്കാം.'), ('V', 'wide', 'ഘടന ആദ്യം, ഫോൾഡർ പിന്നെ.')],
 'ഘടന ആദ്യം,\nഫോൾഡർ പിന്നെ', CTA_DATAROOM, theme='crm',
 cap_ml='ഇക്വിറ്റി നിക്ഷേപം സ്വീകരിക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി വേണം. ആദ്യം കമ്പനി, പിന്നെ ഷെയർ രേഖകൾ, എന്നിട്ട് ഡാറ്റ റൂം. നിങ്ങളുടെ ബിസിനസ് ഏത് ഘടനയിലാണ്?',
 cap_en='The investor is ready to take shares, but the business is still a partnership firm. Equity investment needs a private limited company: company first, then share records, then the data room. What structure is your business in?',
 cap_mg='Equity nikshepam sweekarikkaan private limited company venam. Aadyam company, pinne share rekhakal, ennittu data room. Ningalude business ethu ghadanayilaanu?')

duo('drd008', 'investor_asked', 'B', 'home', 'ക്യാപ് ടേബിളും\nഷെയർ രേഖയും\nചേരുന്നില്ല', [('A', 'wide', 'അരുണേ, ക്യാപ് ടേബിളിൽ അമ്മാവന് 10 ശതമാനം. പക്ഷേ ഷെയർ രേഖയിൽ പേരില്ല!'), ('V', 'V', 'സ്നേഹേ, ഇൻവെസ്റ്റർ ഇത് കണ്ടാൽ ഉടമസ്ഥത വ്യക്തമല്ലെന്ന് കരുതും.'), ('A', 'A', 'എങ്ങനെ ശരിയാക്കും?'), ('V', 'V', 'ഷെയർ അലോട്ട്മെന്റ് രേഖയും ഫയലിംഗും ശരിയാക്കി ക്യാപ് ടേബിൾ ഒത്തുനോക്കണം.'), ('A', 'wide', 'വാക്കാലുള്ള ഷെയർ ഡാറ്റ റൂമിൽ കാണില്ല.'), ('V', 'wide', 'ടേബിളും രേഖയും ഒന്നായിരിക്കണം.')],
 'ടേബിളും രേഖയും\nഒന്നായിരിക്കണം', CTA_DILIGENCE, theme='crm',
 cap_ml='ക്യാപ് ടേബിളും ഷെയർ രേഖകളും ചേരുന്നില്ലെങ്കിൽ ഡ്യൂ ഡിലിജൻസിൽ റെഡ് ഫ്ലാഗ്. ഫണ്ടിംഗിന് മുമ്പ് ഒത്തുനോക്കി ശരിയാക്കൂ. നിങ്ങളുടെ ക്യാപ് ടേബിൾ അപ്ഡേറ്റ് ആണോ?',
 cap_en="The cap table says an uncle owns 10 percent, but the share records don't show him. A mismatch like this is a due diligence red flag; fix the allotment records and filings before raising. Is your cap table up to date?",
 cap_mg='Cap table-um share rekhakalum cherunnillenkil due diligence-il red flag. Funding-inu mumpu othunokki shariyaakku. Ningalude cap table update aano?')

