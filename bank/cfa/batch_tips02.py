# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_CFA. Never decide a split. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_COFOUNDER, CTA_VESTING = topics.CTA_COFOUNDER, topics.CTA_VESTING

lst('cft004', 'friends_cofounders', "B", 'ഷെയർ ഉണ്ട്,\nകരാർ ഇല്ല?\n3 ചോദ്യം ചോദിക്കൂ', [('ഒരാൾ പോയാൽ?', 'വെസ്റ്റ് ചെയ്യാത്ത ഷെയർ എന്താകും എന്ന് എഴുതിയിട്ടുണ്ടോ?'), ('കോഡും ഡിസൈനും?', 'കമ്പനിയുടെ പേരിൽ ആണോ, ഒരാളുടെ ലാപ്ടോപ്പിൽ ആണോ?'), ('വഴക്ക് വന്നാൽ?', 'എങ്ങനെ തീർക്കും എന്ന് മുൻകൂട്ടി എഴുതിയോ?')],
 'ഒന്നിനെങ്കിലും "ഇല്ല"\nഎങ്കിൽ ഇന്ന് തുടങ്ങൂ', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർമാർക്ക് ഷെയർ ഉണ്ട്, പക്ഷേ എഴുതിയ കരാർ ഇല്ലേ? മൂന്ന് ചോദ്യം: ഒരാൾ പോയാൽ ഷെയർ എന്താകും, IP ആരുടേത്, തർക്കം എങ്ങനെ തീർക്കും. നിങ്ങൾക്ക് എത്ര "ഇല്ല"?',
 cap_en='Co-founders with shares but no written agreement: ask three questions. What happens to unvested shares if one leaves, who owns the code and designs, and how will disputes be settled? How many "no" answers do you have?',
 cap_mg='Co-founders-nu share undu, pakshe agreement illa? Moonnu chodyam: oraal poyaal share enthaakum, IP aarudethu, tharkkam engane theerkkum. Ningalkku ethra "illa"?')

lst('cft005', 'late_joiner', "B", 'വെസ്റ്റഡ് ഷെയറും\nഅൺവെസ്റ്റഡ് ഷെയറും:\nവ്യത്യാസം', [('വെസ്റ്റഡ്', 'സമയം കഴിഞ്ഞ് സ്വന്തമായ ഭാഗം.'), ('അൺവെസ്റ്റഡ്', 'ഇനിയും സമയം ബാക്കിയുള്ള ഭാഗം; പോയാൽ കമ്പനി തിരികെ വാങ്ങാം.'), ('ട്രിക്ക്', 'തിരികെ വാങ്ങുന്ന രീതി ലീവർ ക്ലോസിൽ വ്യക്തമായി എഴുതൂ.')],
 'സമയം കൊടുത്തത്\nസ്വന്തം, ബാക്കി കമ്പനിക്ക്', CTA_VESTING, theme="tip",
 cap_ml='വെസ്റ്റഡ് ഷെയർ സമയം കൊണ്ട് സ്വന്തമായ ഭാഗം. അൺവെസ്റ്റഡ് ഷെയർ ഒരാൾ പോകുമ്പോൾ കമ്പനിക്ക് തിരികെ വാങ്ങാം, ലീവർ ക്ലോസിൽ എഴുതിയിട്ടുണ്ടെങ്കിൽ. നിങ്ങളുടെ കരാറിൽ ലീവർ ക്ലോസ് ഉണ്ടോ?',
 cap_en="Vested shares are the part a co-founder has earned with time; unvested shares can be bought back by the company when someone leaves, if the leaver clause says how. Does your co-founder agreement have a leaver clause?",
 cap_mg='Vested share samayam kondu swanthamaaya bhaagam. Unvested share oraal pokumbol company-kku thirike vaangaam, leaver clause-il ezhuthiyittundenkil. Ningalude agreement-il leaver clause undo?')

lst('cft006', 'tech_nontech', "B", 'ഇൻവെസ്റ്റർ വന്നാൽ\nകോ-ഫൗണ്ടർ കരാർ\nമതിയാകുമോ?', [('കോ-ഫൗണ്ടർ കരാർ', 'നിങ്ങൾ തമ്മിലുള്ള ധാരണ.'), ('SHA-യും ആർട്ടിക്കിൾസും', 'അതേ ഷെയർ അവകാശങ്ങൾ അവിടെയും വരണം.'), ('ട്രിക്ക്', 'മൂന്നും ഒരേ കാര്യം പറയുന്നുണ്ടോ എന്ന് ഒത്തുനോക്കൂ.')],
 'മൂന്ന് രേഖ,\nഒരേ വാക്ക്', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർ എഗ്രിമെന്റിലെ ഷെയർ അവകാശങ്ങൾ ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റിലും കമ്പനിയുടെ ആർട്ടിക്കിൾസിലും അതേപോലെ വരണം. ഇൻവെസ്റ്റർ വരും മുമ്പ് ഒത്തുനോക്കൂ. നിങ്ങളുടെ ആർട്ടിക്കിൾസ് അവസാനം വായിച്ചത് എപ്പോൾ?',
 cap_en="The share rights in your co-founder agreement should be mirrored in the shareholders' agreement and the company's articles. Check that all three match before an investor comes in. When did you last read your articles?",
 cap_mg='Co-founder agreement-ile share rights SHA-yilum company articles-ilum athepole varanam. Investor varum mumpu othunokku. Ningalude articles avasaanam vaayichathu eppol?')

lst('cft007', 'family_cofounders', "B", 'തർക്കം വരും മുമ്പ്\nഎഴുതേണ്ട\n3 വരി', [('ആദ്യ പടി', 'തർക്കം വന്നാൽ ആദ്യം എന്ത് ചെയ്യും.'), ('പരിഹാര രീതി', 'ഏത് വഴിക്ക് തീർക്കും എന്ന് കരാറിൽ.'), ('അതുവരെ', 'രഹസ്യാത്മകത രണ്ടുപേരും പാലിക്കണം.')],
 'സ്നേഹമുള്ളപ്പോൾ\nഎഴുതൂ, വഴക്കിൽ അല്ല', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ തർക്ക പരിഹാര രീതി വഴക്ക് വരും മുമ്പ് തന്നെ എഴുതണം. കുടുംബാംഗങ്ങൾ ചേർന്ന ബിസിനസിൽ പ്രത്യേകിച്ച്. നിങ്ങളുടെ കരാറിൽ ഈ ഭാഗം ഉണ്ടോ?',
 cap_en='Write the dispute resolution method into your co-founder agreement while everyone still gets along, especially in a family business. Does your agreement have this clause?',
 cap_mg='Co-founder agreement-il tharkka parihaara reethi vazhakku varum mumpu thanne ezhuthanam. Kudumba business-il prathyekichu. Ningalude agreement-il ee bhaagam undo?')

lst('cft008', 'tech_nontech', "B", 'ലോഗോ, കോഡ്, ഡിസൈൻ:\nആരുടെ പേരിൽ?\n20 സെക്കൻഡ് ചെക്ക്', [('ഇപ്പോൾ ചെയ്യുന്നത്', 'എല്ലാം കമ്പനിക്ക് അസൈൻ ചെയ്യണം.'), ('കമ്പനിക്ക് മുമ്പ് ചെയ്തത്', 'അതും കമ്പനിക്ക് അസൈൻ ചെയ്യാൻ എഴുതൂ.'), ('ട്രിക്ക്', 'കരാറിൽ IP അസൈൻമെന്റ് ക്ലോസ് തിരയൂ.')],
 'ഉണ്ടാക്കിയത് ആര്,\nഉടമ കമ്പനി', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർമാർ ഉണ്ടാക്കിയ കോഡ്, ലോഗോ, ഡിസൈൻ എല്ലാം കമ്പനിക്ക് അസൈൻ ചെയ്യണം; കമ്പനി രജിസ്റ്റർ ചെയ്യും മുമ്പ് ചെയ്ത ജോലിയും. നിങ്ങളുടെ കോഡ് ഇപ്പോൾ ആരുടെ പേരിലാണ്?',
 cap_en="All IP the co-founders create, code, logo and designs, should be assigned to the company, including work done before it was registered. Whose name is your code under right now?",
 cap_mg='Co-founders undaakkiya code, logo, design ellaam company-kku assign cheyyanam; company register cheyyum mumpu cheytha joliyum. Ningalude code ippol aarude peril aanu?')

lst('cft009', 'remote_cofounder', "B", 'ആര് എന്ത്\nതീരുമാനിക്കും?\nഒരു ലളിത ലിസ്റ്റ്', [('ദിവസേന', 'ഓരോരുത്തരുടെ റോളിലുള്ളത് അവർ തന്നെ.'), ('വലിയ തീരുമാനം', 'പുതിയ പാർട്ണർ, പുതിയ ഷെയർ: എല്ലാവരും ചേർന്ന്.'), ('ട്രിക്ക്', 'ഈ ലിസ്റ്റ് കരാറിൽ എഴുതി വെക്കൂ.')],
 'ഓരോ ഫയലിനും\nരണ്ടുപേരുടെ ഒപ്പ് വേണ്ട', CTA_COFOUNDER, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർ എഗ്രിമെന്റിൽ റോളുകളും തീരുമാനങ്ങൾ ആര് എടുക്കും എന്നതും എഴുതണം: ദിവസേനയുള്ളത് റോൾ അനുസരിച്ച്, വലിയവ ഒരുമിച്ച്. നിങ്ങളുടെ ടീമിൽ ഇത് വ്യക്തമാണോ?',
 cap_en="A co-founder agreement should spell out roles and who decides what: daily calls by role, big decisions like new partners or new shares together. Is this clear in your team?",
 cap_mg='Co-founder agreement-il role-um theerumaanam aaru edukkum ennathum ezhuthanam: dhivasenayullathu role anusarichu, valiyava orumichu. Ningalude team-il ithu vyakthamaano?')

lst('cft010', 'friends_cofounders', "B", 'ഷെയർ വിഭജനം:\nശതമാനം ഞങ്ങൾ പറയില്ല,\nഈ 3 ചോദ്യം ചോദിക്കൂ', [('ആര് എന്ത് കൊണ്ടുവരുന്നു', 'സമയം, പണം, കഴിവ്, ക്ലയന്റുകൾ.'), ('ആര് മുഴുവൻ സമയം', 'ഇപ്പോഴും അടുത്ത വർഷങ്ങളിലും.'), ('ഏത് ശതമാനമായാലും', 'വെസ്റ്റിംഗും എഴുതി ചേർക്കൂ.')],
 'ശതമാനം നിങ്ങളുടേത്,\nകരാർ രണ്ടുപേരുടേത്', CTA_VESTING, theme="tip",
 cap_ml='കോ-ഫൗണ്ടർ ഷെയർ വിഭജനം നിങ്ങൾ തന്നെ തീരുമാനിക്കണം. ആര് എന്ത് കൊണ്ടുവരുന്നു, ആര് മുഴുവൻ സമയം എന്ന് ചോദിക്കൂ; ഏത് ശതമാനമായാലും വെസ്റ്റിംഗ് എഴുതൂ. നിങ്ങളുടെ ടീമിൽ എല്ലാവരും മുഴുവൻ സമയമാണോ?',
 cap_en="Only the co-founders can decide their equity split. Ask who brings what and who is full-time, and whatever the split, add vesting. Is everyone on your team full-time?",
 cap_mg='Co-founder share vibhajanam ningal thanne theerumaanikkanam. Aaru enthu konduvarunnu, aaru muzhuvan samayam ennu chodikku; ethu shathamaanam aayaalum vesting ezhuthu. Ningalude team-il ellaavarum full-time aano?')
