# Tips and tricks 02 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_SK.
# Never state grant amounts or promise selection (calls change; the team checks the live call).
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

lst('mt004', 'kerala_registered', "B", 'ഗ്രാന്റിന് മുമ്പ്\nMCA-യിൽ ഒരു വാക്ക്\nനോക്കൂ: Active', [('എവിടെ', 'MCA-യിൽ കമ്പനിയുടെ സ്റ്റാറ്റസ്.'), ('എന്തിന്', 'മിക്ക ഗ്രാന്റുകളും സീഡ് ഫണ്ടും \'ആക്ടീവ്\' ചോദിക്കും.'), ('അല്ലെങ്കിൽ', 'അപേക്ഷയ്ക്ക് മുമ്പ് അത് ശരിയാക്കൂ.')],
 'ഒരു വാക്ക്,\nഒരു അവസരം', CTA_GRANT, theme="tip",
 cap_ml='KSUM ഗ്രാന്റിനും സീഡ് ഫണ്ടിനും മിക്കപ്പോഴും MCA-യിൽ കമ്പനി സ്റ്റാറ്റസ് \'ആക്ടീവ്\' ആയിരിക്കണം. അപേക്ഷിക്കും മുമ്പ് ഒരിക്കൽ നോക്കൂ. നിങ്ങളുടെ കമ്പനി സ്റ്റാറ്റസ് എന്താണ്?',
 cap_en="Most KSUM grants and the seed fund ask for a private limited company or LLP with 'Active' status at MCA. Check it once before you apply. What does your company status say?",
 cap_mg="KSUM grant-inum seed fund-inum mikkappozhum MCA-il company status 'Active' aayirikkanam. Apekshikkum mumpu orikkal nokku. Ningalude company status enthaanu?")

lst('mt005', 'idea_stage', "B", 'KSUM യുണീക്ക് ID\nvs DPIIT:\n10 സെക്കൻഡിൽ', [('യുണീക്ക് ID', 'കേരള സ്റ്റാർട്ടപ്പ് മിഷന്റെ തിരിച്ചറിയൽ.'), ('DPIIT', 'കേന്ദ്രത്തിന്റെ സ്റ്റാർട്ടപ്പ് ഇന്ത്യ അംഗീകാരം.'), ('ട്രിക്ക്', 'പല KSUM ഗ്രാന്റുകളും രണ്ടും ചോദിക്കും.')],
 'ഒന്ന് കേരളം,\nഒന്ന് ഇന്ത്യ', CTA_KSUM, theme="tip",
 cap_ml='KSUM യുണീക്ക് ID കേരള സ്റ്റാർട്ടപ്പ് മിഷന്റേതാണ്, DPIIT റെക്കഗ്നിഷൻ കേന്ദ്രത്തിന്റെ സ്റ്റാർട്ടപ്പ് ഇന്ത്യയുടേതും. പല KSUM ഗ്രാന്റുകളും സീഡ് ഫണ്ടും രണ്ടും ചോദിക്കും. നിങ്ങൾക്ക് ഏതാണ് ഉള്ളത്?',
 cap_en='The KSUM Unique ID is Kerala Startup Mission\'s; DPIIT recognition is the central Startup India one. Many KSUM grants and the seed fund ask for both. Which one do you have?',
 cap_mg='KSUM Unique ID Kerala Startup Mission-nteyaanu, DPIIT recognition central Startup India-yudethum. Pala KSUM grant-um seed fund-um randum chodikkum. Ningalkku ethaanu ullathu?')

lst('mt006', 'returnee', "B", 'കമ്പനി മറ്റൊരു\nസംസ്ഥാനത്ത്.\nKSUM കിട്ടുമോ?', [('നിയമം', 'സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതാകണം.'), ('ആദ്യം നോക്കൂ', 'കമ്പനിയുടെ രജിസ്റ്റേർഡ് ഓഫീസ് ഏത് സംസ്ഥാനത്ത്.'), ('ട്രിക്ക്', 'കേരളത്തിൽ തുടങ്ങാനാണ് പ്ലാൻ എങ്കിൽ ഇവിടെ രജിസ്റ്റർ ചെയ്യൂ.')],
 'വിലാസം കേരളം,\nവഴി തുറക്കും', CTA_KSUM, theme="tip",
 cap_ml='KSUM യുണീക്ക് ID-ക്കും സ്കീമുകൾക്കും സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തതാകണം. ഗൾഫിൽ നിന്ന് മടങ്ങി കേരളത്തിൽ തുടങ്ങുന്നവർ കമ്പനി ഇവിടെ തന്നെ രജിസ്റ്റർ ചെയ്യൂ. നിങ്ങളുടെ കമ്പനി ഏത് സംസ്ഥാനത്താണ്?',
 cap_en='For the KSUM Unique ID and its schemes, the startup should be registered in Kerala. Returning from the Gulf to build here? Register the company in Kerala. Which state is yours in?',
 cap_mg='KSUM Unique ID-kkum scheme-kalkkum startup Kerala-il register cheythathaakanam. Gulf-il ninnu madangi Kerala-il thudangunnavar company ivide thanne register cheyyu. Ningalude company ethu samsthaanathaanu?')

lst('mt007', 'idea_stage', "B", 'ഗ്രാന്റ് കോൾ\nവന്നു! ആദ്യം\nഈ 3 കാര്യം', [('യോഗ്യത', 'ആ കോളിലെ യോഗ്യത വരികൾ മുഴുവൻ വായിക്കൂ.'), ('രേഖകൾ', 'കമ്പനി, യുണീക്ക് ID, DPIIT: ഏതൊക്കെ ചോദിക്കുന്നു.'), ('അവസാന തീയതി', 'കലണ്ടറിൽ ഇട്ട് പിന്നോട്ട് പ്ലാൻ ചെയ്യൂ.')],
 'ഓരോ കോളും\nവേറെയാണ്', CTA_GRANT, theme="tip",
 cap_ml='KSUM ഗ്രാന്റ് കോളുകളും അവയുടെ നിബന്ധനകളും മാറാം. ഓരോ കോൾ വരുമ്പോഴും യോഗ്യത, ചോദിക്കുന്ന രേഖകൾ, അവസാന തീയതി ആദ്യം നോക്കൂ. നിങ്ങൾ ഇപ്പോൾ ഏത് കോളിനാണ് നോക്കുന്നത്?',
 cap_en='KSUM grant calls and their conditions change. When a call opens, check three things first: eligibility, the documents it asks for, and the deadline. Which call are you watching?',
 cap_mg='KSUM grant call-kalum avayude nibandhanakalum maaraam. Oro call varumpozhum yogyatha, chodikkunna rekhakal, avasaana theeyathi aadyam nokku. Ningal ippol ethu call-inaanu nokkunnathu?')

lst('mt008', 'campus', "B", 'കോൾ വരും മുമ്പ്\nഇന്ന് ചെയ്യാവുന്ന\nഒരു കാര്യം', [('ഇന്ന്', 'KSUM സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ യുണീക്ക് ID-ക്ക് അപേക്ഷിക്കൂ.'), ('ഈ മാസം', 'യോഗ്യതയുണ്ടെങ്കിൽ DPIIT റെക്കഗ്നിഷനും.'), ('കോൾ ദിവസം', 'ഫോം മാത്രം ബാക്കി, ഓട്ടം വേണ്ട.')],
 'നേരത്തെ എടുത്താൽ\nഅവസാന നിമിഷം ശാന്തം', CTA_KSUM, theme="tip",
 cap_ml='ഗ്രാന്റ് കോൾ വന്ന ശേഷം യുണീക്ക് ID-ക്ക് ഓടിയാൽ സമയം തികയാതെ വരാം. ഇന്ന് തന്നെ KSUM പോർട്ടലിൽ അപേക്ഷിക്കൂ, യോഗ്യതയുണ്ടെങ്കിൽ DPIIT-യും. നിങ്ങൾക്ക് യുണീക്ക് ID ഉണ്ടോ: യെസ് or നോ?',
 cap_en="Rushing for the Unique ID after a grant call opens can cost you the call. Apply on the KSUM startup portal today, and for DPIIT recognition too if you're eligible. Do you have your Unique ID: yes or no?",
 cap_mg='Grant call vanna shesham Unique ID-kku odiyaal samayam thikayaathe varaam. Innu thanne KSUM portal-il apekshikku, yogyathayundenkil DPIIT-yum. Ningalkku Unique ID undo: yes or no?')

lst('mt009', 'women_founder', "B", 'KSUM എന്നാൽ\nഗ്രാന്റ് മാത്രമല്ല:\n3 വാതിൽ', [('സ്കീമുകളും ഗ്രാന്റുകളും', 'യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്ക്.'), ('ഇൻക്യുബേഷൻ', 'ജോലി ചെയ്യാനുള്ള ഇടവും പിന്തുണയും.'), ('പ്രോഗ്രാമുകൾ', 'എല്ലാത്തിനും ആദ്യ താക്കോൽ യുണീക്ക് ID തന്നെ.')],
 'ഒരു താക്കോൽ,\nപല വാതിൽ', CTA_KSUM, theme="tip",
 cap_ml='KSUM-ൽ ഗ്രാന്റ് മാത്രമല്ല: സ്കീമുകൾ, ഇൻക്യുബേഷൻ, പ്രോഗ്രാമുകൾ എല്ലാം യുണീക്ക് ID ഉള്ള സ്റ്റാർട്ടപ്പുകൾക്കാണ്. തിരഞ്ഞെടുപ്പ് ഓരോന്നിനും വേറെയാണ്. നിങ്ങൾക്ക് ഏതാണ് കൂടുതൽ വേണ്ടത്: ഇടമോ പണമോ?',
 cap_en='KSUM is not only grants: its schemes, incubation and programmes are for startups that hold the Unique ID. Selection is separate for each. What do you need more: space or money?',
 cap_mg='KSUM-il grant maathramalla: scheme-kal, incubation, programme-kal ellaam Unique ID ulla startup-kalkkaanu. Therenjeduppu oronninum vereyaanu. Ningalkku ethaanu kooduthal vendathu: idamo panamo?')

lst('mt010', 'idea_stage', "B", 'ഐഡിയ ഗ്രാന്റ്\nvs സീഡ് ഫണ്ട്:\nഎന്ത് ചോദിക്കും', [('ഐഡിയ ഗ്രാന്റ്', 'കമ്പനിക്ക് മുമ്പും അപേക്ഷിക്കാം.'), ('സീഡ് ഫണ്ട്', 'സാധാരണ DPIIT-യും ആക്ടീവ് കമ്പനിയും ചോദിക്കും.'), ('രണ്ടിനും', 'പണം വരും മുമ്പ് കമ്പനിയും യുണീക്ക് ID-യും.')],
 'ഘട്ടം നോക്കി\nവാതിൽ തിരഞ്ഞെടുക്കൂ', CTA_GRANT, theme="tip",
 cap_ml='ഐഡിയ ഗ്രാന്റിന് കമ്പനി രജിസ്റ്റർ ചെയ്യും മുമ്പും അപേക്ഷിക്കാം; സീഡ് ഫണ്ട് സാധാരണ DPIIT-യും ആക്ടീവ് കമ്പനിയും ചോദിക്കും. രണ്ടിനും പണം വരും മുമ്പ് കമ്പനിയും യുണീക്ക് ID-യും വേണം. നിങ്ങൾ ഏത് ഘട്ടത്തിലാണ്: ഐഡിയയോ കമ്പനിയോ?',
 cap_en='You may apply for the KSUM idea grant before incorporating; the seed fund usually asks for DPIIT recognition and an active company. Both need the company and the Unique ID before money is released. Which stage are you at: idea or company?',
 cap_mg='Idea grant-inu company register cheyyum mumpum apekshikkaam; seed fund saadhaarana DPIIT-yum active company-yum chodikkum. Randinum paisa varum mumpu company-yum Unique ID-yum venam. Ningal ethu ghattathilaanu: idea-yo company-yo?')
