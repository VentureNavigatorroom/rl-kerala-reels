# Data room batch 02 (28 Nov night): 3D duo reels. Facts only from topics.FACTS_DR. Never promise funding, an investor, a valuation or a timeline; no fees. Names invented.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE

# crm (F3 style, invented): order money went into the founder's personal account, the company's bank statement shows nothing
duo('drd009', 'messy_docs', 'A', 'bank', 'ഇൻവെസ്റ്റർ ചോദിച്ചു:\nകമ്പനി ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്.\nപൈസ മുഴുവൻ എന്റെ അക്കൗണ്ടിൽ', [
 ('A', 'wide', 'മനോജേ, ഇൻവെസ്റ്റർ കമ്പനിയുടെ ബാങ്ക് സ്റ്റേറ്റ്മെന്റ് ചോദിച്ചു. പക്ഷേ ഓർഡർ പൈസ മുഴുവൻ വന്നത് എന്റെ സ്വന്തം അക്കൗണ്ടിൽ!'),
 ('V', 'V', 'ശ്രുതീ, അപ്പോ കമ്പനി സ്റ്റേറ്റ്മെന്റിൽ ബിസിനസ് കാണില്ല. കണക്കും ബാങ്കും തമ്മിൽ ചേരില്ല.'),
 ('A', 'A', 'ഡാറ്റ റൂമിൽ അത് അത്ര വലിയ കാര്യമാണോ?'),
 ('V', 'V', 'ഫിനാൻഷ്യൽ സ്റ്റേറ്റ്മെന്റും ബാങ്ക് സ്റ്റേറ്റ്മെന്റും ഡാറ്റ റൂമിൽ അടുത്തടുത്ത് ഇരിക്കും. രണ്ടും ചേർന്നില്ലെങ്കിൽ ചോദ്യം വരും.'),
 ('A', 'wide', 'ഇനി കമ്പനി പൈസ കമ്പനി അക്കൗണ്ടിൽ മാത്രം. പഴയത് കണക്കിൽ വ്യക്തമാക്കാം.'),
 ('V', 'wide', 'കണക്കും ബാങ്കും ഒരേ കഥ പറയണം.')],
 'കണക്കും ബാങ്കും\nഒരേ കഥ പറയണം', CTA_DILIGENCE, theme='crm',
 cap_ml='ഡാറ്റ റൂമിൽ ഫിനാൻഷ്യൽ സ്റ്റേറ്റ്മെന്റും ബാങ്ക് സ്റ്റേറ്റ്മെന്റും ഒരുമിച്ച് നോക്കും. കമ്പനി പൈസ സ്വന്തം അക്കൗണ്ടിൽ വന്നാൽ രണ്ടും ചേരില്ല. നിങ്ങളുടെ ബിസിനസ് പൈസ ഏത് അക്കൗണ്ടിലാണ്?',
 cap_en="The investor asked for the company's bank statements, but all the order money went into the founder's personal account. In a data room the financial statements and bank statements sit side by side, and they need to tell the same story. Which account does your business money land in?",
 cap_mg='Data room-il financial statement-um bank statement-um orumichu nokkum. Company paisa swantham account-il vannaal randum cherilla. Ningalude business paisa ethu account-ilaanu?')

# new: shares promised verbally to the first three employees, no written ESOP plan
duo('drd010', 'raising_first', 'B', 'cafe', 'ആദ്യ 3 ജീവനക്കാർക്ക്\n"ഷെയർ തരാം" എന്ന്\nവാക്ക് കൊടുത്തു', [
 ('A', 'wide', 'റോഷാ, തുടക്കത്തിൽ മൂന്ന് പേർക്ക് ഞാൻ ഷെയർ തരാം എന്ന് പറഞ്ഞിരുന്നു. ഇപ്പോൾ ഇൻവെസ്റ്റർ ടീം ഫോൾഡർ ചോദിക്കുന്നു.'),
 ('V', 'V', 'ആൽവിനേ, എഴുതിയ ESOP പ്ലാൻ ഉണ്ടോ? അതോ വാക്ക് മാത്രമോ?'),
 ('A', 'A', 'വാക്ക് മാത്രം. അവർക്ക് ഓർമയുണ്ട്, എനിക്കും.'),
 ('V', 'V', 'ഡാറ്റ റൂമിൽ ടീം വിവരവും ESOP-ഉം വേണം. എഴുതാത്ത വാഗ്ദാനം ക്യാപ് ടേബിളിൽ ഒരു ചോദ്യചിഹ്നമാകും.'),
 ('A', 'wide', 'അപ്പോ ഫണ്ടിംഗ് സംസാരത്തിന് മുമ്പ് അത് എഴുതി ശരിയാക്കണം.'),
 ('V', 'wide', 'വാക്ക് കൊടുത്താൽ, കടലാസും കൊടുക്കണം.')],
 'കൊടുത്ത വാക്ക്\nകടലാസിലാക്കൂ', CTA_DILIGENCE, theme='new',
 cap_ml='ജീവനക്കാർക്ക് വാക്കാൽ ഷെയർ വാഗ്ദാനം ചെയ്തോ? ഡാറ്റ റൂമിൽ ടീം വിവരവും ESOP-ഉം എഴുതി വെച്ചിട്ടുണ്ടാകണം. നിങ്ങൾ ആർക്കെങ്കിലും ഷെയർ വാക്ക് കൊടുത്തിട്ടുണ്ടോ?',
 cap_en='A founder promised shares to his first three employees, only by word. A data room needs team details and ESOPs in writing; an unwritten promise becomes a question mark on the cap table. Have you promised shares to anyone?',
 cap_mg='Jeevanakkaarkku vaakkaal share vaagdaanam cheytho? Data room-il team vivaravum ESOP-um ezhuthiya roopathil venam. Ningal aarkkenkilum share vaakku koduthittundo?')

# faq: "GST is filed every month, so the tax folder is ready" - the income tax return is missing
duo('drd011', 'messy_docs', 'A', 'pharmacy', 'GST എല്ലാം കൃത്യം.\nഅപ്പോ ടാക്സ് ഫോൾഡർ\nറെഡി? അല്ല', [
 ('A', 'wide', 'പ്രവീണേ, ഡാറ്റ റൂമിന്റെ ടാക്സ് ഫോൾഡർ ഞാൻ നോക്കി. GST റിട്ടേൺ മാത്രമേ ഉള്ളൂ.'),
 ('V', 'V', 'സിനീ, GST എല്ലാ മാസവും കൃത്യമായി ഫയൽ ചെയ്യുന്നുണ്ടല്ലോ. അത് പോരേ?'),
 ('A', 'A', 'കഴിഞ്ഞ വർഷത്തെ കമ്പനിയുടെ ഇൻകം ടാക്സ് റിട്ടേൺ എവിടെ?'),
 ('V', 'V', 'അത് ഫയൽ ചെയ്തില്ല. ഡാറ്റ റൂമിൽ GST-യും ഇൻകം ടാക്സും ROC-യും എല്ലാം വേണം, അല്ലേ?'),
 ('A', 'wide', 'അതെ. ഒന്ന് പെൻഡിംഗ് ആയാലും ഇൻവെസ്റ്റർ അത് കാണും. ആദ്യം അത് തീർക്കാം.'),
 ('V', 'wide', 'ഒരു ടാക്സ് പോരാ, എല്ലാം വേണം.')],
 'GST മാത്രം പോരാ,\nഇൻകം ടാക്സും വേണം', CTA_DILIGENCE, theme='faq',
 cap_ml='ഡാറ്റ റൂമിന്റെ കംപ്ലയൻസ് ഫോൾഡറിൽ GST റിട്ടേൺ മാത്രം പോരാ: ഇൻകം ടാക്സ് റിട്ടേണും ROC ഫയലിംഗും വേണം. നിങ്ങളുടെ ഏതെങ്കിലും ഫയലിംഗ് പെൻഡിംഗ് ആണോ?',
 cap_en="GST returns are filed every month, so the tax folder is ready? Not if last year's company income tax return is missing. A data room's compliance folder needs GST returns, income tax and ROC filings. Is any of yours pending?",
 cap_mg='Data room-inte compliance folder-il GST return maathram poraa: income tax return-um ROC filing-um venam. Ningalude ethenkilum filing pending aano?')

# crm (C23 style, invented): a farm with years of history, numbers only in a diary, applies for an expansion loan
duo('drd012', 'loan_dd', 'B', 'farm', '15 വർഷത്തെ കൃഷി.\nകണക്ക് മുഴുവൻ\nഒരു ഡയറിയിൽ', [
 ('A', 'wide', 'ഗോപീ, ഫാം വലുതാക്കാൻ ലോൺ ചോദിച്ചു. ബാങ്ക് കണക്കും പ്രൊജക്ഷനും ചോദിക്കുന്നു.'),
 ('V', 'V', 'വാസുവേട്ടാ, പതിനഞ്ച് വർഷത്തെ കണക്ക് മുഴുവൻ ആ പഴയ ഡയറിയിൽ അല്ലേ?'),
 ('A', 'A', 'അതെ. ബിസിനസ് നന്നായി നടക്കുന്നുണ്ട്. പക്ഷേ കടലാസിൽ കാണിക്കാൻ ഒന്നുമില്ല.'),
 ('V', 'V', 'ലോൺ തരുന്നവരും രേഖ നോക്കും: കണക്കുകൾ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, പ്രൊജക്ഷൻ, ബിസിനസ് മോഡൽ. എല്ലാം ഒരു ഫോൾഡറിൽ വേണം.'),
 ('A', 'wide', 'അപ്പോ ഡയറിയിലെ കണക്ക് ആദ്യം ശരിയായ സ്റ്റേറ്റ്മെന്റ് ആക്കണം.'),
 ('V', 'wide', 'ഡയറി നമുക്ക്, ഫോൾഡർ ബാങ്കിന്.')],
 'ഡയറിയിലെ കണക്ക്\nഫോൾഡറിലാക്കൂ', CTA_DATAROOM, theme='crm',
 cap_ml='ബാങ്ക് ലോണിനും ലെൻഡർ രേഖകൾ നോക്കും: കണക്കുകൾ, ബാങ്ക് സ്റ്റേറ്റ്മെന്റ്, പ്രൊജക്ഷൻ, ബിസിനസ് മോഡൽ. ഡയറിയിലെ കണക്ക് ഒരു ഫോൾഡറിലാക്കൂ. നിങ്ങളുടെ കണക്ക് ഇപ്പോൾ എവിടെയാണ്?',
 cap_en="Fifteen years of farming, and every number is in one old diary. Lenders review documents too: accounts, bank statements, projections and the business model, in one organised folder. Where are your numbers kept today?",
 cap_mg='Bank loan-inum lender rekhakal nokkum: accounts, bank statement, projection, business model. Diary-yile kanakku oru folder-ilaakku. Ningalude kanakku ippol evideyaanu?')

# new: a buyer for the bakery asks whether the suppliers will stay; nothing is written with them
duo('drd013', 'selling_business', 'A', 'bakery', 'ബേക്കറി വാങ്ങാൻ ആൾ.\nചോദ്യം: "സപ്ലയർമാർ\nതുടരുമോ?"', [
 ('A', 'wide', 'സാബൂ, ബേക്കറി വാങ്ങാൻ വന്നയാൾ ചോദിച്ചു, മൈദയും ബട്ടറും തരുന്ന സപ്ലയർമാർ തുടരുമോ എന്ന്.'),
 ('V', 'V', 'ജിഷേ, അവരുമായി വർഷങ്ങളുടെ ബന്ധമാ. പക്ഷേ ഒരു കരാറും എഴുതിയിട്ടില്ല.'),
 ('A', 'A', 'വാങ്ങുന്നയാൾക്ക് നമ്മുടെ ബന്ധം കാണാൻ പറ്റില്ലല്ലോ.'),
 ('V', 'V', 'ശരിയാ. വാങ്ങുന്നയാളും ഡ്യൂ ഡിലിജൻസ് ചെയ്യും. പ്രധാന സപ്ലയർ, കസ്റ്റമർ കരാറുകൾ ഡാറ്റ റൂമിൽ വേണം.'),
 ('A', 'wide', 'അപ്പോ ചർച്ചയ്ക്ക് മുമ്പ് പ്രധാന സപ്ലയർമാരുമായി എഴുതിയ കരാർ.'),
 ('V', 'wide', 'ബന്ധം നല്ലത്, കരാർ അതിലും നല്ലത്.')],
 'ബന്ധം നല്ലത്,\nകരാർ അതിലും നല്ലത്', CTA_DILIGENCE, theme='new',
 cap_ml='ബിസിനസ് വിൽക്കുമ്പോൾ വാങ്ങുന്നയാൾ പ്രധാന സപ്ലയർ, കസ്റ്റമർ കരാറുകൾ നോക്കും. വാക്കാലുള്ള ബന്ധം ഡാറ്റ റൂമിൽ കാണില്ല. നിങ്ങളുടെ പ്രധാന സപ്ലയർമാരുമായി കരാറുണ്ടോ?',
 cap_en='A buyer for the bakery asks whether the suppliers will stay, and nothing with them is in writing. Buyers run due diligence too, and key supplier and customer contracts belong in the data room. Do you have contracts with your key suppliers?',
 cap_mg='Business vilkkumbol vaangunnayaal pradhaana supplier, customer karaarukal nokkum. Vaakkaalulla bandham data room-il kaanilla. Ningalude pradhaana supplier-maarumaayi karaarundo?')

# crm (C17 style, invented): a founder with 55% brings in a new partner, who wants to see everything first
duo('drd014', 'investor_asked', 'B', 'salon', 'പുതിയ പാർട്ണർ പറഞ്ഞു:\n"ചേരും മുമ്പ്\nഎല്ലാം കാണണം"', [
 ('A', 'wide', 'വിനീതേ, സലൂൺ ചെയിനിൽ പൈസ ഇട്ട് ചേരാൻ വരുന്ന പാർട്ണർ എല്ലാ രേഖകളും കാണണം എന്ന്. എനിക്ക് ദേഷ്യം വന്നു.'),
 ('V', 'V', 'സോണിയേച്ചീ, ദേഷ്യപ്പെടേണ്ട. പണം ഇടുന്ന പാർട്ണറും ഇൻവെസ്റ്ററെപ്പോലെ ഡ്യൂ ഡിലിജൻസ് ചെയ്യും.'),
 ('A', 'A', 'സത്യം പറഞ്ഞാൽ എന്റെ 55 ശതമാനം ഷെയർ രേഖയിൽ ശരിയാണോ എന്ന് എനിക്ക് തന്നെ ഉറപ്പില്ല.'),
 ('V', 'V', 'അതുകൊണ്ട് ആദ്യം ഡാറ്റ റൂം: ക്യാപ് ടേബിൾ, ഷെയർ രേഖ, കരാറുകൾ, കണക്ക്. അവർ നോക്കും മുമ്പ് നമ്മൾ ഒത്തുനോക്കാം.'),
 ('A', 'wide', 'ശരി. നമ്മുടെ സ്വന്തം ഷെയർ രേഖ ആദ്യം ശരിയാക്കാം.'),
 ('V', 'wide', 'അവർ നോക്കും മുമ്പ്, നമ്മൾ നോക്കണം.')],
 'അവർ നോക്കും മുമ്പ്\nനിങ്ങൾ നോക്കൂ', CTA_DATAROOM, theme='crm',
 cap_ml='പണം ഇട്ട് ചേരുന്ന പുതിയ പാർട്ണറും ഡ്യൂ ഡിലിജൻസ് ചെയ്യും: ക്യാപ് ടേബിൾ, ഷെയർ രേഖ, കരാറുകൾ, കണക്ക്. അവർ നോക്കും മുമ്പ് നിങ്ങൾ ഒത്തുനോക്കൂ. നിങ്ങളുടെ ഷെയർ രേഖ ശരിയാണോ?',
 cap_en="A new partner wants to see every document before joining, and the founder isn't sure her own 55 percent is right on paper. Partners who bring money run due diligence like investors: cap table, share records, agreements, accounts. Check them before they do. Are your share records right?",
 cap_mg='Paisa ittu cherunna puthiya partner-um due diligence cheyyum: cap table, share rekha, karaarukal, kanakku. Avar nokkum mumbu ningal othunokku. Ningalude share rekha shariyaano?')

# faq: 10,000 users, but no answer to "how will money come in?" - the business model folder
duo('drd015', 'raising_first', 'A', 'hostel', '"പൈസ എങ്ങനെ വരും?"\nആപ്പിന് 10,000 യൂസർ.\nഉത്തരം ഇല്ല', [
 ('A', 'wide', 'സഞ്ജൂ, ഇൻവെസ്റ്റർ ചോദിച്ചു, പതിനായിരം പേർ ഉപയോഗിക്കുന്ന നമ്മുടെ ആപ്പിൽ നിന്ന് പൈസ എങ്ങനെ വരും എന്ന്.'),
 ('V', 'V', 'അലീനേ, അത് പിന്നീട് ആലോചിക്കാം എന്നല്ലേ നമ്മൾ കരുതിയത്?'),
 ('A', 'A', 'ഡാറ്റ റൂമിൽ പ്രൊജക്ഷനൊപ്പം ബിസിനസ് മോഡലും വേണം എന്ന് അവർ പറഞ്ഞു.'),
 ('V', 'V', 'അപ്പോ എഴുതണം: ആര് പൈസ തരും, എന്തിന്, എങ്ങനെ. അത് പ്രൊജക്ഷനിലെ നമ്പറുകളുമായി ചേരണം.'),
 ('A', 'wide', 'യൂസർ എണ്ണം കഥയുടെ പകുതി മാത്രം.'),
 ('V', 'wide', 'യൂസർ ഉണ്ട്, ഇനി വരുമാന വഴി എഴുതണം.')],
 'യൂസർ പകുതി,\nബിസിനസ് മോഡൽ ബാക്കി', CTA_DATAROOM, theme='faq',
 cap_ml='യൂസർമാർ ഉണ്ട്, പക്ഷേ പൈസ എങ്ങനെ വരും? ഡാറ്റ റൂമിൽ പ്രൊജക്ഷനൊപ്പം ബിസിനസ് മോഡലും വേണം, രണ്ടും ചേരണം. നിങ്ങളുടെ വരുമാന വഴി എഴുതിയിട്ടുണ്ടോ?',
 cap_en="Ten thousand users, and no answer when the investor asks how money will come in. A data room holds the business model next to the projections, and the two must match. Have you written down how you earn?",
 cap_mg='Users undu, pakshe paisa engane varum? Data room-il projection-oppam business model-um venam, randum cheranam. Ningalude varumaana vazhi ezhuthiyittundo?')

# new: three drafts of the shareholder agreement in email, the signed copy only on paper somewhere
duo('drd016', 'messy_docs', 'B', 'hotellobby', 'ഷെയർഹോൾഡർ കരാർ:\nമെയിലിൽ മൂന്ന് വേർഷൻ.\nഒപ്പിട്ടത് ഏത്?', [
 ('A', 'wide', 'ജെയ്സണേ, ഡാറ്റ റൂമിനായി ഷെയർഹോൾഡർ കരാർ തിരഞ്ഞു. മെയിലിൽ മൂന്ന് വേർഷൻ, ഒന്നിലും ഒപ്പില്ല!'),
 ('V', 'V', 'നീതൂ, ഒപ്പിട്ട പേപ്പർ കോപ്പി ഓഫീസിലെ ഏതോ ഫയലിൽ ഉണ്ട്. സ്കാൻ ചെയ്തിട്ടില്ല.'),
 ('A', 'A', 'ഇൻവെസ്റ്റർ ഡ്രാഫ്റ്റ് കണ്ടാൽ ഏതാണ് ശരി എന്ന് എങ്ങനെ അറിയും?'),
 ('V', 'V', 'അറിയില്ല. അതുകൊണ്ട് ഒപ്പിട്ട അവസാന കോപ്പി മാത്രം സ്കാൻ ചെയ്ത് ഇടണം. കുഴഞ്ഞ രേഖ ഡ്യൂ ഡിലിജൻസ് വൈകിക്കും.'),
 ('A', 'wide', 'ഇന്ന് തന്നെ ആ ഫയൽ തപ്പിയെടുക്കാം.'),
 ('V', 'wide', 'ഡ്രാഫ്റ്റ് ചർച്ചയ്ക്ക്, ഒപ്പിട്ടത് ഡാറ്റ റൂമിന്.')],
 'ഡ്രാഫ്റ്റ് ചർച്ചയ്ക്ക്,\nഒപ്പിട്ടത് ഡാറ്റ റൂമിന്', CTA_DILIGENCE, theme='new',
 cap_ml='ഡാറ്റ റൂമിൽ ഡ്രാഫ്റ്റ് അല്ല, ഒപ്പിട്ട അവസാന കരാർ വേണം. മൂന്ന് വേർഷൻ കണ്ടാൽ ഇൻവെസ്റ്റർ ആശയക്കുഴപ്പത്തിലാകും, ഡ്യൂ ഡിലിജൻസ് വൈകും. നിങ്ങളുടെ ഒപ്പിട്ട കോപ്പി എവിടെയാണ്?',
 cap_en='Three drafts of the shareholder agreement in email, none signed, and the signed copy is somewhere on paper. A data room needs the final signed version only; messy documents slow due diligence. Where is your signed copy?',
 cap_mg='Data room-il draft alla, oppitta avasaana karaar venam. Moonnu version kandaal investor aashayakkuzhappathilaakum, due diligence vaikum. Ningalude oppitta copy evideyaanu?')

# faq: incorporation certificate, MOA, AOA and PAN only in an old email from the accountant
duo('drd017', 'messy_docs', 'A', 'photocopy', 'MOA എവിടെ?\n"തുടങ്ങിയ സമയത്തെ\nCA-യുടെ മെയിലിൽ"', [
 ('A', 'wide', 'ഉണ്ണീ, ഇൻകോർപ്പറേഷൻ സർട്ടിഫിക്കറ്റ്, MOA, AOA, കമ്പനി PAN. ഒന്നിന്റെയും കോപ്പി നമ്മുടെ കയ്യിലില്ലേ?'),
 ('V', 'V', 'അശ്വതീ, കമ്പനി തുടങ്ങിയപ്പോൾ CA ഒരു മെയിൽ അയച്ചിരുന്നു. ആ മെയിൽ ഇപ്പോൾ കാണുന്നില്ല.'),
 ('A', 'A', 'ഡാറ്റ റൂമിന്റെ ആദ്യ ഫോൾഡർ തന്നെ ഇതാണ്. അതില്ലാതെ തുടങ്ങാൻ പറ്റില്ല.'),
 ('V', 'V', 'ശരി. ഇവ കണ്ടെത്തി കമ്പനിയുടെ സ്വന്തം ഫോൾഡറിൽ സേവ് ചെയ്യാം. ഇനി ആരുടെയും ഇൻബോക്സിൽ മാത്രം വെക്കില്ല.'),
 ('A', 'wide', 'കമ്പനി രേഖ, കമ്പനിയുടെ കയ്യിൽ.')],
 'കമ്പനി രേഖ\nകമ്പനിയുടെ കയ്യിൽ', CTA_DATAROOM, theme='faq',
 cap_ml='ഇൻകോർപ്പറേഷൻ സർട്ടിഫിക്കറ്റ്, MOA, AOA, കമ്പനി PAN: ഡാറ്റ റൂമിന്റെ ആദ്യ ഫോൾഡർ. അവ ആരുടെയെങ്കിലും പഴയ മെയിലിൽ മാത്രമാണോ? നിങ്ങളുടെ MOA ഇപ്പോൾ എവിടെ?',
 cap_en="The incorporation certificate, MOA, AOA and company PAN are the first folder of a data room, and here they're lost in an old email from the accountant. Keep them in the company's own folder, not someone's inbox. Where is your MOA right now?",
 cap_mg='Incorporation certificate, MOA, AOA, company PAN: data room-inte aadya folder. Ava aarudeyenkilum pazhaya mail-il maathramaano? Ningalude MOA ippol evide?')

# faq: the checklist shows half the pieces missing - the data room team prepares what is missing too
duo('drd018', 'investor_asked', 'B', 'canteen', 'ചെക്ക്ലിസ്റ്റിൽ 10 എണ്ണം.\nകയ്യിൽ ഉള്ളത്\nനാലെണ്ണം', [
 ('A', 'wide', 'അമലേ, ഡാറ്റ റൂം ചെക്ക്ലിസ്റ്റ് നോക്കി. പ്രൊജക്ഷൻ ഇല്ല, വാല്യുവേഷൻ ഇല്ല, കരാർ ഇല്ല, ROC പെൻഡിംഗ്.'),
 ('V', 'V', 'ആതിരേ, ഇല്ലാത്തത് ഓർത്ത് വിഷമിക്കേണ്ട. ആദ്യം അത് കണ്ടുപിടിക്കാൻ കൂടിയാണ് ചെക്ക്ലിസ്റ്റ്.'),
 ('A', 'A', 'ഇതൊക്കെ ഓരോന്നായി ആരെക്കൊണ്ട് ചെയ്യിക്കും?'),
 ('V', 'V', 'ഡാറ്റ റൂം ടീം ഫോൾഡർ മാത്രമല്ല ഉണ്ടാക്കുന്നത്. ഇല്ലാത്തതും ഒരുക്കും: പ്രൊജക്ഷൻ, വാല്യുവേഷൻ, കരാറുകൾ, പെൻഡിംഗ് ഫയലിംഗ്.'),
 ('A', 'wide', 'അപ്പോ ആദ്യം ഇല്ലാത്തതിന്റെ ലിസ്റ്റ്.'),
 ('V', 'wide', 'ഇല്ലാത്തത് അറിയുന്നതാണ് ആദ്യ പടി.')],
 'ഇല്ലാത്തത് അറിയൂ,\nഅതാണ് ആദ്യ പടി', CTA_DATAROOM, theme='faq',
 cap_ml='ഡാറ്റ റൂം ചെക്ക്ലിസ്റ്റിൽ പകുതിയും ഇല്ലേ? ഞങ്ങളുടെ ടീം ഫോൾഡർ മാത്രമല്ല, ഇല്ലാത്തതും ഒരുക്കും: രജിസ്ട്രേഷൻ, പ്രൊജക്ഷൻ, വാല്യുവേഷൻ, കരാറുകൾ, പെൻഡിംഗ് ഫയലിംഗ്. നിങ്ങൾക്ക് ഏതാണ് ഇല്ലാത്തത്?',
 cap_en='Ten items on the data room checklist, four in hand. Our team does not just set up the folder; it prepares what is missing too: registration, projections, valuation, agreements and pending filings. Which pieces are you missing?',
 cap_mg='Data room checklist-il pakuthiyum ille? Njangalude team folder maathramalla, illaathathum orukkum: registration, projection, valuation, karaarukal, pending filing. Ningalkku ethaanu illaathathu?')

# crm (#16, invented): a Gulf Malayali wants to put money into a relative's Kerala company; the relative is hurt when asked for documents
duo('drd019', 'investor_asked', 'A', 'gulfroom', 'ബന്ധുവിന്റെ കമ്പനിയിൽ\nപൈസ ഇടാൻ. രേഖ\nചോദിച്ചപ്പോൾ പിണക്കം', [
 ('A', 'wide', 'ഷംസൂ, നാട്ടിലെ അനന്തരവന്റെ ഫുഡ് കമ്പനിയിൽ പൈസ ഇടാം എന്ന് പറഞ്ഞു. രേഖ ചോദിച്ചപ്പോൾ അവന് പിണക്കം.'),
 ('V', 'V', 'നസീറേ, ബന്ധു ആയാലും ചോദിക്കണം. അത് അവനും നല്ലതാ.'),
 ('A', 'A', 'എന്തൊക്കെ ചോദിക്കണം? എനിക്ക് വലിയ പിടിയില്ല.'),
 ('V', 'V', 'കമ്പനി രേഖകൾ, ക്യാപ് ടേബിൾ, കണക്കുകൾ, പെൻഡിംഗ് ഫയലിംഗ് ഉണ്ടോ എന്ന്. ഒരു ഡാറ്റ റൂം ഉണ്ടെങ്കിൽ എല്ലാം ഒരിടത്ത് കാണാം.'),
 ('A', 'wide', 'അപ്പോ അവനോട് ആദ്യം ഒരു ഡാറ്റ റൂം ഒരുക്കാൻ പറയാം.'),
 ('V', 'wide', 'ബന്ധുവാണെങ്കിലും, രേഖ നോക്കണം.')],
 'ബന്ധുവാണെങ്കിലും\nരേഖ നോക്കണം', CTA_DATAROOM, theme='crm',
 cap_ml='ബന്ധുവിന്റെ കമ്പനിയിൽ പൈസ ഇടുമ്പോഴും രേഖ നോക്കണം: കമ്പനി രേഖകൾ, ക്യാപ് ടേബിൾ, കണക്കുകൾ, പെൻഡിംഗ് ഫയലിംഗ്. ഡാറ്റ റൂം ഉണ്ടെങ്കിൽ എല്ലാം ഒരിടത്ത്. ഈ റീൽ ആർക്ക് അയക്കും?',
 cap_en="A Gulf Malayali wants to invest in his nephew's Kerala food company, and the nephew is hurt when asked for documents. Family or not, check the company records, cap table, accounts and pending filings; a data room puts them in one place. Who would you send this to?",
 cap_mg='Bandhuvinte company-il paisa idumbozhum rekha nokkanam: company rekhakal, cap table, kanakkukal, pending filing. Data room undenkil ellaam oridathu. Ee reel aarkku ayakkum?')

# crm (C15 style, invented): the whole app was built by a freelancer friend with no written agreement
duo('drd020', 'raising_first', 'B', 'park', 'ആപ്പ് മുഴുവൻ ഉണ്ടാക്കിയത്\nഒരു കൂട്ടുകാരൻ.\nടീം ലിസ്റ്റിൽ ഇല്ല', [
 ('A', 'wide', 'അനന്തൂ, ഡാറ്റ റൂമിന്റെ ടീം ഫോൾഡറിൽ ഞാനും നീയും മാത്രം. പക്ഷേ ആപ്പ് മുഴുവൻ ഉണ്ടാക്കിയത് ജിതിൻ അല്ലേ?'),
 ('V', 'V', 'ഗായത്രീ, അവൻ ഫ്രീലാൻസ് ആയി ചെയ്യുന്നതാ. എഴുതിയ ഒരു കരാറും ഇല്ല.'),
 ('A', 'A', 'ഇൻവെസ്റ്റർ ചോദിക്കും, ശരിക്കും ടീം ആരാണ് എന്ന്.'),
 ('V', 'V', 'അതെ. ടീം വിവരവും പ്രധാന കരാറുകളും ഡാറ്റ റൂമിൽ വേണം. പ്രധാന ആളുമായി കരാർ ഇല്ലെങ്കിൽ അത് റിസ്കായി കാണും.'),
 ('A', 'wide', 'അവനുമായി സംസാരിച്ച് എഴുതിയ കരാർ ഉണ്ടാക്കാം.'),
 ('V', 'wide', 'ടീമിൽ ഉണ്ടെങ്കിൽ, രേഖയിലും വേണം.')],
 'ടീമിൽ ഉണ്ടെങ്കിൽ\nരേഖയിലും വേണം', CTA_DILIGENCE, theme='crm',
 cap_ml='ആപ്പ് ഉണ്ടാക്കിയ പ്രധാന ആൾ ടീം ലിസ്റ്റിലും കരാറിലും ഇല്ലെങ്കിൽ ഇൻവെസ്റ്റർ അത് റിസ്കായി കാണും. ടീം വിവരവും പ്രധാന കരാറുകളും ഡാറ്റ റൂമിൽ വേണം. നിങ്ങളുടെ പ്രധാന ആളുമായി കരാറുണ്ടോ?',
 cap_en='The whole app was built by a freelancer friend, and he is not in the team folder or any written agreement. A data room needs team details and key agreements, and a missing one is seen as a risk. Is your key person on paper?',
 cap_mg='App undaakkiya pradhaana aal team list-ilum karaarilum illenkil investor athu risk aayi kaanum. Team vivaravum pradhaana karaarukalum data room-il venam. Ningalude pradhaana aalumaayi karaarundo?')

# faq myth: "let the investor say yes first, then I'll get the documents ready"
duo('drd021', 'raising_first', 'A', 'ferry', '"ഇൻവെസ്റ്റർ യെസ് പറയട്ടെ,\nഎന്നിട്ട് രേഖ\nഒരുക്കാം"', [
 ('A', 'wide', 'ടോണീ, രേഖകൾ ഒക്കെ ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞിട്ട് ഒരുക്കാം. ഇപ്പോൾ എന്തിനാ ടെൻഷൻ?'),
 ('V', 'V', 'മീരേ, താൽപര്യം കാണിച്ചാലും ഡ്യൂ ഡിലിജൻസിൽ അവർ രേഖ നോക്കും. അതിന് ശേഷമേ കാര്യം മുന്നോട്ട് പോകൂ.'),
 ('A', 'A', 'അപ്പോൾ പെട്ടെന്ന് ഒരുക്കിയാൽ പോരേ?'),
 ('V', 'V', 'പെൻഡിംഗ് ഫയലിംഗ്, ഒപ്പിടാത്ത കരാർ, പ്രൊജക്ഷൻ ഇല്ല. ഇതൊന്നും ഒറ്റ രാത്രിയിൽ ശരിയാകില്ല. കുഴഞ്ഞ രേഖ എല്ലാം വൈകിക്കും.'),
 ('A', 'wide', 'അപ്പോ ഫോൾഡർ ഇപ്പോൾ, മീറ്റിംഗ് പിന്നെ.'),
 ('V', 'wide', 'യെസ് കേട്ടിട്ട് ഓടരുത്, മുമ്പേ ഒരുങ്ങണം.')],
 'യെസിന് മുമ്പേ\nഫോൾഡർ റെഡി', CTA_DATAROOM, theme='faq',
 cap_ml='ഇൻവെസ്റ്റർ താൽപര്യം കാണിച്ചാലും ഡ്യൂ ഡിലിജൻസിൽ രേഖ നോക്കും. പെൻഡിംഗ് ഫയലിംഗും ഒപ്പിടാത്ത കരാറും ഒറ്റ രാത്രിയിൽ ശരിയാകില്ല. നിങ്ങളുടെ ഫോൾഡർ ഇപ്പോൾ റെഡിയാണോ?',
 cap_en="\"Let the investor say yes, then I'll get the documents ready.\" Even after interest, due diligence reviews every document, and pending filings, unsigned agreements or missing projections can't be fixed overnight. Messy documents slow everything. Is your folder ready now?",
 cap_mg='Investor thaalparyam kaanichaalum due diligence-il rekha nokkum. Pending filing-um oppidaatha karaarum otta raathriyil shariyaakilla. Ningalude folder ippol ready aano?')
