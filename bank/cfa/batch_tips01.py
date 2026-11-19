# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

lst('cft001', 'friends_cofounders', "B", 'കോ-ഫൗണ്ടർ\nഎഗ്രിമെന്റിൽ\nവേണ്ട 4 കാര്യം', [('ഷെയർ വിഭജനം', 'ആർക്ക് എത്ര.'), ('റോളുകൾ', 'ആര് എന്ത് തീരുമാനിക്കും.'), ('IP', 'എല്ലാം കമ്പനിക്ക് അസൈൻ ചെയ്യണം.')],
 'സൗഹൃദം നിലനിൽക്കാൻ\nകരാർ', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ ഷെയർ വിഭജനം, വെസ്റ്റിംഗ്, റോളുകൾ, എല്ലാ IP-യും കമ്പനിക്ക്, പുറത്തുപോകുന്നവരുടെ വ്യവസ്ഥ, തർക്ക പരിഹാരം എന്നിവ വേണം. നിങ്ങളുടേതിൽ എന്താണ് ഇല്ലാത്തത്?',
 cap_en='A co-founder agreement covers the equity split, vesting, roles, IP assigned to the company, leaver terms and dispute resolution. What is missing from yours?',
 cap_mg='Co-founder agreement-il share split, vesting, roles, IP company-kku, leaver terms, tharkka parihaaram venam. Ningaludethil enthaanu illaathathu?')

lst('cft002', 'late_joiner', "B", 'വെസ്റ്റിംഗ്:\nനാല് വർഷം,\nഒരു വർഷ ക്ലിഫ്', [('നാല് വർഷം', 'ഷെയർ പതുക്കെ സ്വന്തമാകും.'), ('ഒരു വർഷ ക്ലിഫ്', 'ആദ്യ വർഷം കഴിയാതെ ഒന്നുമില്ല.'), ('പോയാൽ', 'വെസ്റ്റ് ചെയ്യാത്ത ഷെയർ കമ്പനി തിരികെ വാങ്ങും.')],
 'പോയവർ ഷെയറുമായി\nപോകില്ല', CTA_VESTING, theme="tip",
 cap_ml='പൊതുവായ രീതി: നാല് വർഷ വെസ്റ്റിംഗ്, ഒരു വർഷ ക്ലിഫ്. ആരെങ്കിലും നേരത്തെ പോയാൽ വെസ്റ്റ് ചെയ്യാത്ത ഷെയർ തിരികെ വാങ്ങാം. നിങ്ങളുടെ ടീമിന് വെസ്റ്റിംഗ് ഉണ്ടോ?',
 cap_en='A common practice is 4-year vesting with a 1-year cliff; unvested shares of someone who leaves can be bought back. Does your team have vesting?',
 cap_mg='Common reethi: 4 varsha vesting, 1 varsha cliff. Nerathe poyaal vest cheyyaatha share thirike vaangaam. Ningalude team-nu vesting undo?')

lst('cft003', 'remote_cofounder', "B", 'നോൺ-കോമ്പീറ്റ്\nഎഴുതിയാൽ\nരക്ഷയാകുമോ?', [('പോയ ശേഷം നോൺ-കോമ്പീറ്റ്', 'ഇന്ത്യയിൽ പൊതുവെ നടപ്പാകില്ല.'), ('രഹസ്യാത്മകത', 'നടപ്പാക്കാം.'), ('നോൺ-സോളിസിറ്റ്', 'ടീമിനെയും ക്ലയന്റിനെയും കൊണ്ടുപോകാതിരിക്കാൻ.')],
 'നടക്കുന്നത്\nഎഴുതൂ', CTA_COFOUNDER, theme="tip",
 cap_ml='ഇന്ത്യയിൽ പുറത്തുപോയ ശേഷമുള്ള നോൺ-കോമ്പീറ്റ് പൊതുവെ നടപ്പാകില്ല. രഹസ്യാത്മകതയും നോൺ-സോളിസിറ്റും നടപ്പാക്കാം. നിങ്ങളുടെ കരാറിൽ ഏതാണ് ഉള്ളത്?',
 cap_en='In India a post-exit non-compete is generally not enforceable, but confidentiality and non-solicit can be. Which does your agreement rely on?',
 cap_mg='India-yil purathu poya seshamulla non-compete pothuve nadappaakilla. Confidentiality-um non-solicit-um nadappaakkaam. Ningalude karaaril ethaanu?')

