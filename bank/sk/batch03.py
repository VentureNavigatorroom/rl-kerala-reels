# Kerala Startup Mission (KSUM) seed batch 03 (19 Nov, backlog). Situations from bank/STORY_THEMES.md (anonymised; invented details).
# Facts only from topics.FACTS_SK. Never state grant amounts or promise selection.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

duo("md021", "kerala_registered", "A", "airport", "കേരളത്തിൽ രജിസ്റ്റർ\nചെയ്യാതെ KSUM\nഇല്ല", [
 ("A","wide","റഫീഖേ, ബെംഗളൂരുവിൽ രജിസ്റ്റർ ചെയ്ത കമ്പനി, KSUM-ന് അപേക്ഷിക്കാമോ?"),
 ("V","V","ഷമീറേ, സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം. അതാണ് ആദ്യ നിബന്ധന."),
 ("A","A","അപ്പോ ബെംഗളൂരു കമ്പനിക്ക് വഴിയില്ലേ?"),
 ("V","V","ഇല്ല. പക്ഷേ കേരളത്തിൽ ഒരു യൂണിറ്റ് തുടങ്ങിയാൽ കാര്യം മാറുമോ എന്ന് അവരോട് ചോദിക്കണം."),
 ("A","wide","അതെ. ഓരോ നിബന്ധനയും ഔദ്യോഗിക വെബ്സൈറ്റിൽ നോക്കൂ."),
 ("V","wide","തീരുമാനത്തിന് മുമ്പ് ഉറപ്പാക്കൂ.")],
 "ബെംഗളൂരു കമ്പനി?\nആദ്യ നിബന്ധന കേരളം", CTA_KSUM, theme="faq",
 cap_ml="KSUM പദ്ധതികൾക്ക് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം. മറ്റ് സംസ്ഥാനത്തെ കമ്പനിക്ക് ഇത് ബാധകമാണ്. നിങ്ങളുടെ കമ്പനി എവിടെയാണ് രജിസ്റ്റർ ചെയ്തത്?",
 cap_en="KSUM programmes ask that the startup is registered in Kerala. Where is your company registered?",
 cap_mg="KSUM padhathikalkku startup Kerala-il register cheythirikkanam. Ningalude company evide register cheythathu?")

duo("md022", "kerala_registered", "A", "office", "യുണീക്ക് ID\nഉണ്ടെങ്കിൽ പണം\nഉറപ്പാണോ?", [
 ("A","wide","രാഹുലേ, KSUM യുണീക്ക് ID കിട്ടിയാൽ പണം വീട്ടിലെത്തുമെന്നാണോ?"),
 ("V","V","നേഹ, ഇല്ല. ID സ്റ്റാർട്ടപ്പിന്റെ തിരിച്ചറിയൽ മാത്രമാണ്."),
 ("A","A","അപ്പോ ഗ്രാന്റ് വേറെ അപേക്ഷയാണോ?"),
 ("V","V","അതെ. സ്കീമുകളും ഗ്രാന്റുകളും ID ഉള്ളവർക്ക് മാത്രം. പക്ഷേ തിരഞ്ഞെടുപ്പ് വേറെ."),
 ("A","wide","അതെ. ID ആദ്യ പടി, അത്ര മാത്രം."),
 ("V","wide","ഉറപ്പെന്ന് കരുതരുത്, പ്രക്രിയ മനസ്സിലാക്കൂ.")],
 "ID ആദ്യ പടി മാത്രം,\nഗ്രാന്റ് തിരഞ്ഞെടുപ്പ് വേറെ", CTA_GRANT, theme="faq",
 cap_ml="KSUM യുണീക്ക് ID സ്റ്റാർട്ടപ്പിന്റെ തിരിച്ചറിയൽ മാത്രമാണ്. ഗ്രാന്റിനും പദ്ധതികൾക്കും പ്രത്യേക അപേക്ഷയും തിരഞ്ഞെടുപ്പും വേണം. നിങ്ങൾക്ക് ID ഉണ്ടോ?",
 cap_en="The KSUM Unique ID only identifies your startup. Grants and programmes need a separate application and selection. Do you already have a Unique ID?",
 cap_mg="KSUM Unique ID startup-nte thiricharivu maathram. Grants, padhathikalkku verae apekshayum selection-um venam. Ningalku ID undo?")

duo("md023", "kerala_registered", "B", "bank", "കമ്പനി 'ആക്ടീവ്'\nഅല്ലെങ്കിൽ ഗ്രാന്റ്\nതടസ്സം", [
 ("A","wide","മനോജേ, നമ്മുടെ കമ്പനി MCA-യിൽ ആക്ടീവ് അല്ലെന്ന് കണ്ടു. ഗ്രാന്റ് കിട്ടുമോ?"),
 ("V","V","ശ്രുതീ, ആക്ടീവ് ആകണം. അതിന് ഫയലിംഗ് ശരിയാക്കണം."),
 ("A","A","അപ്പോ തുടക്കത്തിൽ തന്നെ ഈ കാര്യം നോക്കണം."),
 ("V","V","അതെ. പല സ്കീമുകളും ഇത് ചോദിക്കും."),
 ("A","wide","ഫയലിംഗ് കുടിശ്ശിക ഉണ്ടെങ്കിൽ ആദ്യം തീർക്കണം."),
 ("V","wide","രേഖ MCA-യിൽ പരിശോധിച്ച ശേഷം അപേക്ഷിക്കൂ.")],
 "MCA-യിൽ ആക്ടീവ് അല്ലെങ്കിൽ\nഗ്രാന്റ് വാതിൽ അടയും", CTA_GRANT, theme="new",
 cap_ml="KSUM ഗ്രാന്റുകൾക്ക് പലപ്പോഴും MCA-യിൽ 'ആക്ടീവ്' സ്റ്റാറ്റസ് ഉള്ള പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനി അല്ലെങ്കിൽ LLP വേണം. ഫയലിംഗ് കുടിശ്ശിക ആദ്യം തീർക്കൂ. നിങ്ങളുടെ MCA സ്റ്റാറ്റസ് എന്താണ്?",
 cap_en="Many KSUM grants ask for a private limited company or LLP with 'ആക്ടീവ്' status at MCA. Clear any filing backlog first. What is your MCA status?",
 cap_mg="KSUM grants-il MCA-yil Active status ulla private limited allenkil LLP venam. Filing kudisika aadyam theerkkoo. Ningalude MCA status enthaanu?")

duo("md024", "campus", "B", "gym", "DPIIT ഇല്ലാതെ\nKSUM ഗ്രാന്റ്?\nചെക്ക് ചെയ്യൂ", [
 ("A","wide","ജസ്റ്റിനേ, ഈ ഗ്രാന്റിന് DPIIT വേണമെന്ന് ലിസ്റ്റിൽ കണ്ടു. ഞങ്ങളുടെ കമ്പനിക്ക് ഇല്ല."),
 ("V","V","റിയാ, പല KSUM ഗ്രാന്റുകളും DPIIT അംഗീകാരം ചോദിക്കാറുണ്ട്."),
 ("A","A","അപ്പോ DPIIT ആദ്യം വേണോ?"),
 ("V","V","ഓരോ കോളും നോക്കണം. ചിലതിൽ ഇത് നിർബന്ധം."),
 ("A","wide","ലൈവ് കോൾ പരിശോധിച്ച് മാത്രം തീരുമാനിക്കൂ."),
 ("V","wide","ഓർമ്മയിൽ വെച്ച് അപേക്ഷിക്കരുത്.")],
 "DPIIT ചോദിക്കുന്ന കോൾ,\nലൈവ് ലിസ്റ്റ് നോക്കൂ", CTA_GRANT, theme="faq",
 cap_ml="പല KSUM ഗ്രാന്റുകളും DPIIT അംഗീകാരം ആവശ്യപ്പെടാറുണ്ട്, പക്ഷേ ഓരോ കോളിനും വ്യത്യാസമുണ്ട്. ലൈവ് കോൾ നോക്കി മാത്രം തീരുമാനിക്കൂ. നിങ്ങൾ എന്തിനാണ് ഗ്രാന്റ് നോക്കുന്നത്?",
 cap_en="Many KSUM grants ask for DPIIT recognition, but each call differs. Check the live call before deciding. What are you looking for funding for?",
 cap_mg="KSUM grants-il DPIIT venam ennu chilappol undu. Oro call-um vyathyasam. Live call nokkiyittu mathram theerumaanikkoo. Ningal enthinu grant nokkunnu?")

duo("md025", "campus", "A", "library", "ഒരു പദ്ധതിക്ക് മാത്രം\nഅപേക്ഷിക്കരുത്.\nഎല്ലാം നോക്കൂ", [
 ("A","wide","അനൂപേ, ഈ ഗ്രാന്റ് നോക്കിയിരുന്നു. എല്ലാ വർഷവും ഒരേ തീയതിയോ?"),
 ("V","V","ഗ്രീഷ്മേ, ഇല്ല. കോളുകൾ മാറും, പുതിയ പദ്ധതിയും വരും."),
 ("A","A","അപ്പോ ഒന്ന് മാത്രം നോക്കിയാൽ മതിയോ?"),
 ("V","V","ഇല്ല. പല പദ്ധതികളും ഒരേ രേഖകൾ ചോദിക്കും, അതുകൊണ്ട് ഒരുക്കം മുൻകൂട്ടി വെക്കൂ."),
 ("A","wide","രേഖകൾ ഒരിടത്ത് വെച്ചാൽ വേഗം അപേക്ഷിക്കാം."),
 ("V","wide","ഓരോ കോളിനും പുതുതായി പരിശോധിക്കൂ.")],
 "കോളുകൾ മാറും,\nരേഖകൾ മുൻകൂട്ടി ഒരുക്കൂ", CTA_GRANT, theme="new",
 cap_ml="KSUM പദ്ധതികളും കോളുകളും മാറിക്കൊണ്ടിരിക്കും. ഒരേ രേഖകൾ പലപ്പോഴും ചോദിക്കും, അതുകൊണ്ട് മുൻകൂട്ടി ഒരുക്കി വെക്കൂ. നിങ്ങളുടെ രേഖകൾ എല്ലാം ഒരിടത്തുണ്ടോ?",
 cap_en="KSUM programmes and calls keep changing, and they often ask for the same papers. Keep your documents ready in one place. Are all your papers in one folder?",
 cap_mg="KSUM padhathikalum calls maarikondirikkum. Orae rekhakal pala pravashyam chodikkum. Rekhakal ellaam orituthu sookshikkoo. Ningalude rekhakal oru idathundo?")

duo("md026", "returnee", "A", "metro", "മറ്റൊരു സംസ്ഥാനത്ത്\nരജിസ്റ്റർ, പിന്നെ\nകേരളത്തിൽ വരാം", [
 ("A","wide","കിരണേ, ഗുജറാത്തിൽ കമ്പനി രജിസ്റ്റർ ചെയ്ത് പിന്നെ കേരളത്തിൽ വരാം എന്ന് തോന്നുന്നു."),
 ("V","V","അഞ്ജലീ, അത് നേരിട്ട് ചെയ്യാൻ കഴിയില്ല. കേരളത്തിൽ തുടങ്ങിയാൽ മാത്രമേ KSUM-ന് യോഗ്യത."),
 ("A","A","അപ്പോ പുതിയ കമ്പനി കേരളത്തിൽ തന്നെ രജിസ്റ്റർ ചെയ്യണോ?"),
 ("V","V","അതെ. ഓഫീസ് ഉണ്ടെന്ന് മാത്രം പോരാ, രജിസ്ട്രേഷൻ കേരളത്തിൽ വേണം."),
 ("A","wide","തീരുമാനിക്കുന്നതിന് മുമ്പ് ഒരു പ്രൊഫഷണലിനോട് ചോദിക്കൂ."),
 ("V","wide","ഓരോ കേസും വ്യത്യസ്തമാണ്, ഉറപ്പില്ലാതെ മാറ്റരുത്.")],
 "കേരളത്തിൽ തുടങ്ങണം,\nഓഫീസ് മാത്രം പോരാ", CTA_KSUM, theme="faq",
 cap_ml="KSUM യോഗ്യതയ്ക്ക് സ്റ്റാർട്ടപ്പ് കേരളത്തിൽ രജിസ്റ്റർ ചെയ്തിരിക്കണം. മറ്റൊരു സംസ്ഥാനത്തെ കമ്പനി പിന്നീട് മാറ്റിയാൽ യോഗ്യത ആകില്ല. നിങ്ങളുടെ കമ്പനി എവിടെയാണ്?",
 cap_en="KSUM eligibility needs the startup registered in Kerala. Having an office here is not enough. Where is your company registered?",
 cap_mg="KSUM yogyathakku startup Kerala-il register cheythirikkanam. Office mathram pora. Ningalude company evide?")

duo("md027", "kerala_registered", "B", "rooftop", "തെരഞ്ഞെടുപ്പ് ഉറപ്പല്ല.\nതയ്യാറെടുപ്പ്\nമാത്രം", [
 ("A","wide","ശ്യാമേ, KSUM ഇൻകുബേഷനിൽ ഇടം കിട്ടിയില്ല. എവിടെയാണ് പിഴച്ചത്?"),
 ("V","V","ആര്യേ, തെരഞ്ഞെടുപ്പ് ഉറപ്പല്ല. അപേക്ഷ എല്ലാവരെയും ഒരുപോലെ വിലയിരുത്തുന്നു."),
 ("A","A","അപ്പോ എന്ത് മെച്ചപ്പെടുത്തണം?"),
 ("V","V","അപേക്ഷ വ്യക്തമാക്കുക, പ്രശ്നം എന്താണെന്ന് തെളിയിക്കുക, ടീം വ്യക്തമാക്കുക."),
 ("A","wide","അതെ. അടുത്ത കോളിനായി തയ്യാറാകൂ."),
 ("V","wide","ഒരു തവണ കിട്ടിയില്ലെങ്കിൽ നിരാശപ്പെടേണ്ട.")],
 "തെരഞ്ഞെടുപ്പ് ഉറപ്പല്ല,\nഅടുത്ത കോളിന് തയ്യാറാകൂ", CTA_KSUM, theme="new",
 cap_ml="KSUM തെരഞ്ഞെടുപ്പ് ഉറപ്പല്ല. അപേക്ഷയിൽ പ്രശ്നം, പരിഹാരം, ടീം എന്നിവ വ്യക്തമാക്കിയാൽ അടുത്ത കോളിന് മെച്ചപ്പെടും. നിങ്ങളുടെ അപേക്ഷയിൽ പ്രശ്നം എന്താണ് എന്ന് വ്യക്തമാണോ?",
 cap_en="KSUM selection is never guaranteed. A clear problem, solution and team in the application helps for the next call. Is your problem statement clear in your application?",
 cap_mg="KSUM selection urappalla. Apekshayil prashnam, parihaaram, team vyakthamaakkiyaal adutha callinu meccham. Ningalude prashnam vyakthamaano?")

duo("md028", "campus", "B", "hospital", "പണം വരുന്നതിന് മുമ്പ്\nUnique ID വേണം.\nഇല്ലെങ്കിലോ?", [
 ("A","wide","ജോസഫേ, ഗ്രാന്റ് അനുവദിച്ചു എന്ന് മെസ്സേജ് കിട്ടി. പണം എപ്പോൾ?"),
 ("V","V","ലക്ഷ്മീ, പണം കിട്ടുന്നതിന് മുമ്പ് കമ്പനിയും യുണീക്ക് ID-യും വേണം."),
 ("A","A","ID ഇല്ലെങ്കിലോ?"),
 ("V","V","അപ്പോ പണം വിട്ടുകിട്ടില്ല. അതുകൊണ്ട് രേഖ ഉടൻ പൂർത്തിയാക്കൂ."),
 ("A","wide","അതെ. തടസ്സമുണ്ടെങ്കിൽ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ സഹായം തേടൂ."),
 ("V","wide","അനുമതിക്ക് ശേഷമെ പണം ഉപയോഗിക്കാവൂ.")],
 "അനുവദിച്ചാലും ID\nഇല്ലെങ്കിൽ പണം തടയും", CTA_GRANT, theme="faq",
 cap_ml="KSUM ഗ്രാന്റ് അനുവദിച്ചാലും കമ്പനിയും യുണീക്ക് ID-യും ഇല്ലെങ്കിൽ പണം വിട്ടുകിട്ടില്ല. രേഖകൾ ഉടൻ പൂർത്തിയാക്കൂ. നിങ്ങൾക്ക് ID കിട്ടിയോ?",
 cap_en="Even when a KSUM grant is approved, money is not released without the company and the Unique ID. Finish the papers early. Have you received your Unique ID?",
 cap_mg="KSUM grant anuvadhichaalum company-yum Unique ID-yum illenkil panam kittilla. Rekhakal udan poortthiyaakkoo. Ningalku ID kittiyo?")

duo("md029", "idea_stage", "A", "beach", "സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ\nഅപേക്ഷ. ആദ്യം\nരജിസ്റ്റർ", [
 ("A","wide","നിഖിലേ, KSUM അപേക്ഷ എവിടെയാണ് കൊടുക്കുന്നത്?"),
 ("V","V","ദിവ്യേ, അവരുടെ സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ. ആദ്യം അക്കൗണ്ട് ഉണ്ടാക്കണം."),
 ("A","A","അപ്പോ ഓഫീസിൽ പോകേണ്ടതില്ലേ?"),
 ("V","V","ആദ്യ ഘട്ടം ഓൺലൈൻ. ചിലപ്പോൾ രേഖകൾ ആവശ്യപ്പെടാം."),
 ("A","wide","ഏറ്റവും പുതിയ പ്രക്രിയ വെബ്സൈറ്റിൽ നോക്കൂ."),
 ("V","wide","ഏജന്റിനെ വിശ്വസിക്കരുത്, സ്വയം പോർട്ടലിൽ ചെയ്യൂ.")],
 "അപേക്ഷ ഔദ്യോഗിക പോർട്ടലിൽ,\nഏജന്റ് വേണ്ട", CTA_KSUM, theme="new",
 cap_ml="KSUM അപേക്ഷ അവരുടെ ഔദ്യോഗിക സ്റ്റാർട്ടപ്പ് പോർട്ടലിലാണ് നൽകുന്നത്. ആദ്യം അക്കൗണ്ട് ഉണ്ടാക്കണം. ഏജന്റിനെ നൽകുന്നതിന് മുമ്പ് ഒന്ന് ആലോചിക്കൂ. നിങ്ങൾ ഇതുവരെ അപേക്ഷിച്ചോ?",
 cap_en="KSUM applications are submitted on its official startup portal, and you create an account first. Before paying anyone to apply, check the official route. Have you applied yet?",
 cap_mg="KSUM apekshayude official startup portal-il aanu. Aadyam account undaakkanam. Agent-ne nalkunnathinu mumpu oru aalochikkoo. Ningal ithuvare apply cheyyo?")
