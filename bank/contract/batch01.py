# contract batch 01 (28 Nov night): seed 3D reels. Facts only from topics.FACTS_CONTRACT. No prices, no promised results.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_CONTRACT, CTA_VENDOR = topics.CTA_CONTRACT, topics.CTA_VENDOR

duo('kcd001', 'unpaid_dues', 'A', 'office', 'ജോലി തീർത്തു.\nപണം തന്നില്ല.\nകരാർ ഇല്ല', [('A', 'wide', 'രാഹുലേ, ക്ലയന്റിന് ജോലി മുഴുവൻ ചെയ്തുകൊടുത്തു. ഇപ്പോൾ പണം തരുന്നില്ല. കരാർ ഒന്നും ഇല്ല.'), ('V', 'V', 'നേഹ, മെസേജുകളും ഇമെയിലുകളും സൂക്ഷിച്ചോ? അവ ചിലപ്പോൾ സഹായിക്കും.'), ('A', 'A', 'ഉണ്ട്. പക്ഷേ അത് മതിയോ?'), ('V', 'V', 'ഒപ്പിട്ട, ശരിയായി സ്റ്റാമ്പ് ചെയ്ത കരാർ ആണ് ഏറ്റവും ശക്തം. സ്കോപ്പും പേയ്മെന്റ് നിബന്ധനയും എഴുതി.'), ('A', 'wide', 'അടുത്ത ക്ലയന്റ് മുതൽ ജോലി തുടങ്ങും മുമ്പ് കരാർ.'), ('V', 'wide', 'ആദ്യം കരാർ, പിന്നെ ജോലി.')],
 'ആദ്യം കരാർ,\nപിന്നെ ജോലി', CTA_CONTRACT, theme='crm',
 cap_ml='കരാർ ഇല്ലാതെ ജോലി ചെയ്താൽ പണം കിട്ടാതെ കുടുങ്ങാം. മെസേജുകൾ സഹായിക്കുമെങ്കിലും ഒപ്പിട്ട, സ്റ്റാമ്പ് ചെയ്ത കരാറാണ് ഏറ്റവും ശക്തം. നിങ്ങൾ ജോലി തുടങ്ങും മുമ്പ് കരാർ ഒപ്പിടാറുണ്ടോ?',
 cap_en="He finished the work and the client won't pay, and there's no contract. Messages and emails can help prove the deal, but a signed, properly stamped contract with scope and payment terms is far stronger. Do you sign before you start?",
 cap_mg='Karaar illaathe joli cheythaal panam kittaathe kudungaam. Messages sahaayikkumenkilum oppitta, stamp cheytha karaar aanu ettavum shaktham. Ningal joli thudangum mumpu karaar oppidaarundo?')

duo('kcd002', 'vendor_deal', 'B', 'library', 'സപ്ലയർ വൈകി.\nകരാറിൽ ഒന്നും\nപറഞ്ഞിട്ടില്ല', [('A', 'wide', 'അനൂപേ, സപ്ലയർ രണ്ടാഴ്ച വൈകി. ഓർഡർ നഷ്ടമായി. കരാറിൽ വൈകിയാൽ എന്ത് എന്ന് എഴുതിയിട്ടില്ല.'), ('V', 'V', 'ഗ്രീഷ്മേ, വെണ്ടർ കരാറിൽ ഡെലിവറി തീയതിയും വൈകിയാൽ എന്തും വേണം.'), ('A', 'A', 'വേറെ എന്തൊക്കെ?'), ('V', 'V', 'കൃത്യമായ സ്പെക്, ഗുണനിലവാരം, ഡെലിവറിയുമായി ബന്ധിപ്പിച്ച പേയ്മെന്റ്, ഡിഫെക്ട്, ടെർമിനേഷൻ.'), ('A', 'wide', 'ശരിയായി സ്റ്റാമ്പ് ചെയ്ത് ഒപ്പിടുക.'), ('V', 'wide', 'പ്രശ്നം വരും മുമ്പ് എഴുതുക.')],
 'പ്രശ്നം വരും മുമ്പ്\nഎഴുതുക', CTA_VENDOR, theme='faq',
 cap_ml='വെണ്ടർ കരാറിൽ സ്പെക്, ഗുണനിലവാരം, ഡെലിവറി തീയതി, വൈകിയാൽ എന്ത്, പേയ്മെന്റ്, ഡിഫെക്ട്, ടെർമിനേഷൻ എന്നിവ വേണം. നിങ്ങളുടെ സപ്ലയർ കരാറിൽ ഇതെല്ലാം ഉണ്ടോ?',
 cap_en='Her supplier was two weeks late and she lost the order, but the contract said nothing about delays. A vendor agreement should cover specs, quality, delivery dates, what happens if late, payment, defects and termination. Does yours?',
 cap_mg='Vendor karaaril spec, gunanilavaaram, delivery date, vaikiyaal enthu, payment, defect, termination venam. Ningalude supplier karaaril ithellaam undo?')

duo('kcd003', 'client_deal', 'A', 'home', 'വെള്ളക്കടലാസിൽ\nഒപ്പിട്ട കരാർ.\nകോടതിയിൽ?', [('A', 'wide', 'അരുണേ, കരാർ സാധാരണ കടലാസിൽ ടൈപ്പ് ചെയ്ത് ഒപ്പിട്ടു. സ്റ്റാമ്പ് ഒന്നും ഇല്ല.'), ('V', 'V', 'സ്നേഹേ, കേരളത്തിൽ കേരള സ്റ്റാമ്പ് ആക്ട് ബാധകമാണ്. ശരിയായി സ്റ്റാമ്പ് ചെയ്യാത്ത കരാർ തെളിവായി എടുക്കാതിരിക്കാം.'), ('A', 'A', 'പിന്നെ എന്ത് ചെയ്യും?'), ('V', 'V', 'കുറവുള്ള ഡ്യൂട്ടിയും പിഴയും അടച്ചാലേ പരിഗണിക്കൂ. ഇ-സ്റ്റാമ്പിംഗ് ലഭ്യമാണ്.'), ('A', 'wide', 'ഒപ്പിടുന്ന ദിവസം തന്നെ ശരിയായി സ്റ്റാമ്പ് ചെയ്യുക.'), ('V', 'wide', 'ഒപ്പ് മാത്രം പോരാ, സ്റ്റാമ്പും.')],
 'ഒപ്പ് മാത്രം പോരാ,\nസ്റ്റാമ്പും', CTA_CONTRACT, theme='new',
 cap_ml='കേരള സ്റ്റാമ്പ് ആക്ട് പ്രകാരം ശരിയായി സ്റ്റാമ്പ് ചെയ്യാത്ത കരാർ, കുറവുള്ള ഡ്യൂട്ടിയും പിഴയും അടയ്ക്കുന്നത് വരെ തെളിവായി എടുക്കാതിരിക്കാം. ഇ-സ്റ്റാമ്പിംഗ് ലഭ്യമാണ്. നിങ്ങളുടെ കരാറുകൾ സ്റ്റാമ്പ് ചെയ്തതാണോ?',
 cap_en="He signed a contract on plain paper with no stamp. Under the Kerala Stamp Act, an agreement that isn't properly stamped can be refused as evidence until the deficit duty and a penalty are paid; e-stamping is available. Are your contracts stamped?",
 cap_mg='Kerala Stamp Act prakaaram shariyaayi stamp cheyyaatha karaar, kuravulla duty-um pizhayum adaykkunnathu vare thelivaayi edukkaathirikkaam. E-stamping labhyamaanu. Ningalude karaarukal stamp cheythathaano?')

