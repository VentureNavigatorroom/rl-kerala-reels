# Idea validation batch 01 (28 Nov): 3D duo reels from the anonymised call (C29). Facts only from topics.FACTS_IDEA. Never promise demand, sales, funding or results; no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALIDATE, CTA_IDEA = topics.CTA_VALIDATE, topics.CTA_IDEA

duo('ivd001', 'build_first', 'A', 'office', 'ആപ്പിന് പണം\nചെലവാക്കി.\nകസ്റ്റമർ വന്നില്ല', [('A', 'wide', 'രാഹുലേ, ആപ്പിന് ഒരുപാട് പണം ചെലവാക്കി. ആറ് മാസമായി ഒരു ഓർഡർ പോലുമില്ല.'), ('V', 'V', 'നേഹ, ആപ്പ് ഉണ്ടാക്കും മുമ്പ് ആരെങ്കിലും വാങ്ങുമോ എന്ന് നോക്കിയോ?'), ('A', 'A', 'ഇല്ല. എല്ലാവരും ഐഡിയ നല്ലതെന്ന് പറഞ്ഞു.'), ('V', 'V', 'നല്ലതെന്ന് പറയുന്നതും പണം കൊടുത്ത് വാങ്ങുന്നതും രണ്ടാണ്. ആദ്യം പത്ത് ഓർഡർ കൈകൊണ്ട്.'), ('A', 'wide', 'ഡിമാൻഡ് തെളിഞ്ഞ ശേഷം മാത്രം ടെക്.'), ('V', 'wide', 'അഭിനന്ദനം അല്ല, ഓർഡർ.')],
 'അഭിനന്ദനം അല്ല,\nഓർഡർ', CTA_VALIDATE, theme='new',
 cap_ml='ആളുകൾ ഐഡിയ നല്ലതെന്ന് പറയുന്നതും പണം കൊടുത്ത് വാങ്ങുന്നതും രണ്ടാണ്. ആപ്പിന് പണം ചെലവാക്കും മുമ്പ് യഥാർത്ഥ ഓർഡറുകൾ കൊണ്ട് ടെസ്റ്റ് ചെയ്യൂ. നിങ്ങളുടെ ആദ്യ ഓർഡർ കിട്ടിയോ?',
 cap_en='He spent heavily on an app and six months later has no orders. People saying the idea is good is not the same as people paying for it, so get your first orders by hand before you build. Have you had your first order?',
 cap_mg='Aalukal idea nallathennu parayunnathum panam koduthu vaangunnathum randaanu. App-inu panam chelavaakkum mumpu real orders kondu test cheyyu. Ningalude aadya order kittiyo?')

duo('ivd002', 'marketplace_idea', 'B', 'library', 'കസ്റ്റമറോ\nസപ്ലയറോ?\nഏതാണ് പ്രയാസം', [('A', 'wide', 'അനൂപേ, പ്ലാറ്റ്ഫോമിന് കസ്റ്റമറെ കിട്ടുന്നുണ്ട്. പക്ഷേ ഉണ്ടാക്കിത്തരാൻ ആളെ കിട്ടുന്നില്ല.'), ('V', 'V', 'ഗ്രീഷ്മേ, മാർക്കറ്റ്പ്ലേസിൽ രണ്ട് വശമുണ്ട്. ഏതാണ് കൂടുതൽ പ്രയാസം എന്ന് ആദ്യം കണ്ടെത്തണം.'), ('A', 'A', 'അപ്പോ പരസ്യം നിർത്തണോ?'), ('V', 'V', 'പ്രയാസമുള്ള വശത്ത് ആദ്യം ശ്രദ്ധിക്കുക. ഇവിടെ വിശ്വസിക്കാവുന്ന സപ്ലയർമാർ.'), ('A', 'wide', 'ഡെലിവറി പറ്റാത്ത ഓർഡർ ബ്രാൻഡ് കളയും.'), ('V', 'wide', 'ദുർബലമായ വശം ആദ്യം.')],
 'ദുർബലമായ വശം\nആദ്യം', CTA_VALIDATE, theme='faq',
 cap_ml='മാർക്കറ്റ്പ്ലേസിന് രണ്ട് വശമുണ്ട്: കസ്റ്റമർമാരും സപ്ലയർമാരും. ഏതാണ് കിട്ടാൻ പ്രയാസം എന്ന് ആദ്യം കണ്ടെത്തി അവിടെ ശ്രദ്ധിക്കൂ. നിങ്ങൾക്ക് ഏതാണ് പ്രയാസം?',
 cap_en="Customers are coming, but she can't find enough people to make the orders. A marketplace has two sides, buyers and suppliers; find out which is harder and fix that first. Which side is harder for you?",
 cap_mg='Marketplace-inu randu vashamundu: customers-um suppliers-um. Ethaanu kittaan prayaasam ennu aadyam kandethi avide shraddhikku. Ningalkku ethaanu prayaasam?')

duo('ivd003', 'side_project', 'A', 'rooftop', 'ജോലി വിടണോ?\nആദ്യം ഇത്\nനോക്കൂ', [('A', 'wide', 'ശ്യാമേ, AI കാരണം ജോലി മാറണം എന്ന് തോന്നുന്നു. ബിസിനസ് തുടങ്ങാൻ ഉടനെ ജോലി വിടട്ടെ?'), ('V', 'V', 'ആര്യേ, ആദ്യം ജോലിക്കൊപ്പം ചെറുതായി ടെസ്റ്റ് ചെയ്താലോ?'), ('A', 'A', 'എങ്ങനെ?'), ('V', 'V', 'ഒരു ഉൽപ്പന്നം, ഇൻസ്റ്റഗ്രാമിൽ കാണിക്കുക, ആദ്യ ഓർഡറുകൾ കൈകൊണ്ട്. കണക്ക് എഴുതുക.'), ('A', 'wide', 'കണക്ക് ശരിയായാൽ ധൈര്യത്തോടെ മാറാം.'), ('V', 'wide', 'ചാട്ടം അല്ല, ടെസ്റ്റ്.')],
 'ചാട്ടം അല്ല,\nടെസ്റ്റ്', CTA_IDEA, theme='crm',
 cap_ml='ജോലി മാറി ബിസിനസ് തുടങ്ങാൻ ആലോചിക്കുന്നുണ്ടോ? ആദ്യം ജോലിക്കൊപ്പം ചെറുതായി ടെസ്റ്റ് ചെയ്യൂ: ഒരു ഉൽപ്പന്നം, യഥാർത്ഥ ഓർഡറുകൾ, എഴുതിയ കണക്ക്. നിങ്ങൾ ഇപ്പോൾ ജോലിയിലാണോ?',
 cap_en='With AI changing her field, she wants to quit and start a business right away. Test small alongside the job first: one product, real orders, written numbers, then switch with confidence. Are you still in a job?',
 cap_mg='Joli maari business thudangaan aalochikkunnundo? Aadyam jolikkoppam cheruthaayi test cheyyu: oru product, real orders, ezhuthiya kanakku. Ningal ippol joliyilaano?')

duo('ivd004', 'occasion_products', 'B', 'beach', 'ഓണത്തിന് ഓർഡർ\nനിറഞ്ഞു. പിന്നെ\nആരുമില്ല', [('A', 'wide', 'നിഖിലേ, ഓണത്തിന് ഗിഫ്റ്റ് ഓർഡർ നിറഞ്ഞു. അതിന് ശേഷം ഒന്നുമില്ല!'), ('V', 'V', 'ദിവ്യേ, വിശേഷാവസരങ്ങളിലെ ഉൽപ്പന്നങ്ങൾക്ക് ഇത് സാധാരണയാണ്. വീണ്ടും വാങ്ങുന്നവർ കുറവ്.'), ('A', 'A', 'അപ്പോ ബിസിനസ് നടക്കില്ലേ?'), ('V', 'V', 'നടക്കാം. പക്ഷേ ഓരോ കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ് ഒരു ഓർഡറിലെ വരുമാനത്തേക്കാൾ കുറവായിരിക്കണം.'), ('A', 'wide', 'അടുത്ത അവസരത്തിന് അവരെ വീണ്ടും എങ്ങനെ കൊണ്ടുവരും എന്നും ആലോചിക്കണം.'), ('V', 'wide', 'സീസൺ അല്ല, ആവർത്തനം.')],
 'സീസൺ അല്ല,\nആവർത്തനം', CTA_VALIDATE, theme='faq',
 cap_ml='ഗിഫ്റ്റ് പോലുള്ള വിശേഷാവസര ഉൽപ്പന്നങ്ങൾക്ക് വീണ്ടും വാങ്ങുന്നവർ കുറവായിരിക്കും. ഒരു കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ് ഒരു ഓർഡറിലെ വരുമാനത്തേക്കാൾ കുറവാണോ എന്ന് നോക്കൂ. നിങ്ങളുടെ കസ്റ്റമർ വീണ്ടും വരുന്നുണ്ടോ?',
 cap_en='Onam gift orders flooded in, then nothing. Occasion-based products often have few repeat buyers, so check that what each customer costs to win stays below what each order earns. Do your customers come back?',
 cap_mg='Gift pole visheshaavasara products-inu veendum vaangunnavar kuravaayirikkum. Oru customer-e kittaanulla chelavu oru order-ile varumaanathekkaal kuravaano ennu nokku. Ningalude customer veendum varunnundo?')

duo('ivd005', 'build_first', 'A', 'classroom', 'ആദ്യ ദിവസം തന്നെ\nപ്രൈവറ്റ് ലിമിറ്റഡ്?\nകാത്തിരിക്കൂ', [('A', 'wide', 'ആദർശേ, ഐഡിയ ടെസ്റ്റ് ചെയ്യുന്നതിന് മുമ്പ് തന്നെ പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്റ്റർ ചെയ്യണോ?'), ('V', 'V', 'നിമ്മീ, ടെസ്റ്റ് ഘട്ടത്തിൽ പ്രൊപ്രൈറ്റർഷിപ്പും ഉദ്യമും മതിയാകും.'), ('A', 'A', 'പ്രശ്നമൊന്നുമില്ലേ?'), ('V', 'V', 'ഒന്നുണ്ട്. പ്രൊപ്രൈറ്റർഷിപ്പിൽ വ്യക്തിയും ബിസിനസും നിയമപരമായി ഒന്നാണ്. ബാധ്യതയും.'), ('A', 'wide', 'ഇൻവെസ്റ്റർ വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡിലേക്ക് മാറാം.'), ('V', 'wide', 'ആദ്യം തെളിവ്, പിന്നെ ഘടന.')],
 'ആദ്യം തെളിവ്,\nപിന്നെ ഘടന', CTA_IDEA, theme='faq',
 cap_ml='ഐഡിയ ടെസ്റ്റ് ചെയ്യുമ്പോൾ പ്രൊപ്രൈറ്റർഷിപ്പും സൗജന്യ ഉദ്യമും മതിയാകും; പക്ഷേ വ്യക്തിയും ബിസിനസും നിയമപരമായി ഒന്നാണ്. ഇൻവെസ്റ്റർ വരുമ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡ്. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്?',
 cap_en='Should you register a private limited company before testing the idea? A proprietorship with free Udyam is often enough to test, but personal and business liability are the same; move to a private limited company when investors come in. Which stage are you at?',
 cap_mg='Idea test cheyyumbol proprietorship-um free Udyam-um mathiyaakum; pakshe vyakthiyum business-um niyamaparamaayi onnaanu. Investor varumbol private limited. Ningal ethu ghattathilaanu?')

duo('ivd006', 'marketplace_idea', 'B', 'gym', 'തുടരണോ, മാറ്റണോ,\nനിർത്തണോ?\nഓർഡർ പറയും', [('A', 'wide', 'ജസ്റ്റിനേ, മൂന്ന് മാസം ടെസ്റ്റ് ചെയ്തു. ഇനി തുടരണോ എന്ന് അറിയില്ല.'), ('V', 'V', 'റിയാ, ഓർഡറുകൾ, ഓരോന്നിലെ വരുമാനം, കസ്റ്റമറെ കിട്ടാനുള്ള ചെലവ്. എഴുതിയിട്ടുണ്ടോ?'), ('A', 'A', 'ഉണ്ട്. ഒരു ഉൽപ്പന്നം നന്നായി പോകുന്നു, ബാക്കി ഇല്ല.'), ('V', 'V', 'എങ്കിൽ ആ ഒന്നിലേക്ക് മാറാം. മുഴുവൻ നിർത്തേണ്ട.'), ('A', 'wide', 'യഥാർത്ഥ ഓർഡറുകളാണ് തീരുമാനിക്കേണ്ടത്, തോന്നൽ അല്ല.'), ('V', 'wide', 'തോന്നൽ അല്ല, ഡാറ്റ.')],
 'തോന്നൽ അല്ല,\nഡാറ്റ', CTA_VALIDATE, theme='new',
 cap_ml='ടെസ്റ്റിന് ശേഷം തുടരണോ, മാറ്റണോ, നിർത്തണോ എന്ന് യഥാർത്ഥ ഓർഡറുകളും കണക്കുകളും തീരുമാനിക്കട്ടെ. നിങ്ങളുടെ ഏത് ഉൽപ്പന്നമാണ് നന്നായി പോകുന്നത്?',
 cap_en="After three months of testing he doesn't know whether to continue. Let real orders, earnings per order and the cost to win customers decide whether to continue, change direction or stop. Which of your products is working?",
 cap_mg='Test-inu sesham thudaranno, maattano, nirthano ennu real orders-um kanakkukalum theerumaanikkatte. Ningalude ethu product aanu nannaayi pokunnathu?')

