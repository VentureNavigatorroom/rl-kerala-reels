# Trademark batch 06 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_TM. Never promise registration or mention fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_TRADEMARK, CTA_BRAND = topics.CTA_TRADEMARK, topics.CTA_BRAND

# CRM C4 (two related businesses, only one protected): rubber thread brand filed, the new glove brand not
duo("tm032", "copied_brand", "A", "rubber", "അപ്പന്റെ ബ്രാൻഡിന്\nട്രേഡ്മാർക്ക് ഉണ്ട്.\nമകന്റെ ഗ്ലൗസിന്?", [
 ("A","wide","തോമസേ, നമ്മുടെ പുതിയ ഗ്ലൗസ് ബ്രാൻഡിന്റെ അതേ പേരിൽ വേറൊരാൾ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്തിരിക്കുന്നു."),
 ("V","V","ജോയിച്ചായാ, അപ്പന്റെ റബ്ബർ നൂൽ ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഉണ്ടല്ലോ. അത് പോരേ?"),
 ("A","A","അത് വേറെ പേരാ. ഗ്ലൗസിന്റെ പേര് കമ്പനി പേരിൽ മാത്രം ഉണ്ട്."),
 ("V","wide","കമ്പനി പേര് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല. ഓരോ ബ്രാൻഡും അത് കച്ചവടം ചെയ്യുന്ന ക്ലാസിൽ വെവ്വേറെ ഫയൽ ചെയ്യണം."),
 ("A","A","അപ്പന്റെ കുട എനിക്ക് മഴ തടയില്ല."),
 ("V","V","ഒരു വീട്, രണ്ട് ബ്രാൻഡ്, രണ്ട് ഫയലിംഗ്.")],
 "ഒരു വീട്, രണ്ട് ബ്രാൻഡ്,\nരണ്ട് ഫയലിംഗ്", CTA_BRAND, theme="crm",
 cap_ml="കുടുംബത്തിന്റെ റബ്ബർ നൂൽ ബ്രാൻഡിന് ട്രേഡ്മാർക്ക് ഉണ്ട്, പുതിയ ഗ്ലൗസ് ബ്രാൻഡിന് ഇല്ല. കമ്പനി പേര് ബ്രാൻഡിനെ സംരക്ഷിക്കില്ല; ഓരോ ബ്രാൻഡും അതിന്റെ ക്ലാസിൽ വെവ്വേറെ ഫയൽ ചെയ്യണം. നിങ്ങൾക്ക് എത്ര ബ്രാൻഡ് ഉണ്ട്?",
 cap_en="The family's rubber thread brand has a trademark; the son's new glove brand does not. A company name does not protect a brand: every brand is filed separately in the class it trades in. How many brands do you run?",
 cap_mg="Kudumbathinte rubber thread brand-inu trademark undu, puthiya glove brand-inu illa. Company name brand-ine samrakshikkilla; oro brand-um athinte class-il vevvere file cheyyanam. Ningalkku ethra brand undu?")

# CRM #25 (student founder with a prototype, wants credibility before investors)
duo("tm033", "app_founder", "B", "classroom", "ഡെമോ ഡേ നാളെ.\n\"ആപ്പിന്റെ പേര്\nആരുടേത്?\"", [
 ("A","wide","ആദർശേ, നാളെ ഡെമോ ഡേയിൽ കുട്ടികളുടെ കോഡിംഗ് ആപ്പ് കാണിക്കും. ഒരു മെന്റർ ചോദിച്ചു: പേര് സുരക്ഷിതമാണോ?"),
 ("V","V","നിമ്മീ, ഇൻകുബേറ്ററിന്റെ സർട്ടിഫിക്കറ്റിൽ ആപ്പിന്റെ പേര് ഉണ്ടല്ലോ."),
 ("A","A","അത് ഞങ്ങൾ ടീം ആണെന്നതിന്റെ രേഖ മാത്രം. പേരിന്റേതല്ല."),
 ("V","wide","എങ്കിൽ ഇന്ന് ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്യാം. ഫയൽ ചെയ്താൽ സ്ലൈഡിലെ ലോഗോയിൽ TM ഇടാം."),
 ("A","A","R രജിസ്റ്റർ ആയ ശേഷം മാത്രം, അല്ലേ?"),
 ("V","V","ആപ്പിന് ബഗ് ഉണ്ടാകാം, പേരിന് ബാക്കപ്പ് വേണം.")],
 "സർട്ടിഫിക്കറ്റ് ടീമിന്,\nട്രേഡ്മാർക്ക് പേരിന്", CTA_TRADEMARK, theme="crm",
 cap_ml="കോളേജ് ഇൻകുബേറ്ററിന്റെ സർട്ടിഫിക്കറ്റ് ആപ്പിന്റെ പേര് സംരക്ഷിക്കില്ല. ഡെമോ ഡേയ്ക്ക് മുമ്പ് ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്താൽ ലോഗോയിൽ TM ഇടാം; R രജിസ്ട്രേഷന് ശേഷം മാത്രം. നിങ്ങളുടെ ആപ്പിന്റെ പേര് ഫയൽ ചെയ്തോ?",
 cap_en="A college incubator certificate does not protect your app's name. File the trademark before demo day and you can put TM on the logo in your slides; R only after registration. Is your app's name filed: yes or no?",
 cap_mg="College incubator certificate app-inte peru samrakshikkilla. Demo day-kku mumpu trademark file cheythaal logo-yil TM idaam; R registration-inu shesham maathram. Ningalude app-inte peru file cheytho?")

# CRM #26 (Gulf returnee bringing his business home)
duo("tm034", "food_brand", "C", "airport", "മസ്കറ്റിൽ 9 വർഷം.\n\"നാട്ടിൽ എത്തിയിട്ട്\nപേര് നോക്കാം\"", [
 ("A","wide","റഫീഖേ, മസ്കറ്റിലെ എന്റെ ബിരിയാണി മസാല നാട്ടിലും ഇറക്കും. ട്രേഡ്മാർക്ക് ഒക്കെ എത്തിയിട്ട് ആലോചിക്കാം."),
 ("V","V","ഷമീറിക്കാ, ഗ്രൂപ്പിൽ നിങ്ങളുടെ ബോക്സിന്റെ ഫോട്ടോ ആയിരം പേർ കണ്ടു. അതിൽ ഒരാൾ ആദ്യം ഫയൽ ചെയ്താലോ?"),
 ("A","A","അവിടത്തെ പേപ്പർ ഒക്കെ എന്റെ കയ്യിലുണ്ടല്ലോ."),
 ("V","wide","നാട്ടിലെ സംരക്ഷണത്തിന് ഇന്ത്യയിലെ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ മസാലയുടെ ക്ലാസിൽ ഫയൽ ചെയ്യണം. അത് ഇവിടെ നിന്ന് തന്നെ തുടങ്ങാം."),
 ("A","A","ബോർഡിംഗ് പാസിന് മുമ്പ് ഫയലിംഗ്."),
 ("V","V","ലഗേജ് പിന്നെ വരും, പേര് ആദ്യം എത്തണം.")],
 "ലഗേജ് പിന്നെ,\nപേര് ആദ്യം", CTA_BRAND, theme="crm",
 cap_ml="ഗൾഫിൽ നിന്ന് തിരിച്ചുവരുന്നവർ \"നാട്ടിൽ എത്തിയിട്ട് ട്രേഡ്മാർക്ക്\" എന്ന് കരുതും. ഇന്ത്യയിൽ സംരക്ഷണത്തിന് ഇന്ത്യയിലെ ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഉൽപ്പന്നത്തിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യണം, വരുന്നതിന് മുമ്പേ തുടങ്ങാം. നിങ്ങൾ എന്ന് നാട്ടിലേക്ക്?",
 cap_en="Gulf returnees often plan to sort the trademark after landing. Protection in India needs a filing with India's Trade Marks Registry in your product's class, and you can start before you fly home. When are you moving back?",
 cap_mg="Gulf-il ninnu thirichu varunnavar 'naattil ethiyittu trademark' ennu karuthum. India-yil samrakshanathinu India-yile Trade Marks Registry-il product-inte class-il file cheyyanam, varunnathinu mumpe thudangaam. Ningal ennu naattilekku?")

# CRM #7 (women's clothing brand on Instagram wants to export)
duo("tm035", "d2c_brand", "A", "tailor", "ഖത്തറിലെ ബൊട്ടീക്ക്\nചോദിച്ചു: \"ബ്രാൻഡ്\nരജിസ്റ്റേർഡ് ആണോ?\"", [
 ("A","wide","മോഹനേട്ടാ, ഖത്തറിലെ ഒരു ബൊട്ടീക്ക് നമ്മുടെ ബ്ലൗസ് ലേബൽ എടുക്കാം എന്ന്. ചോദിച്ചത് ബ്രാൻഡ് രജിസ്റ്റേർഡ് ആണോ എന്ന്."),
 ("V","V","ഉഷേ, കഴിഞ്ഞ മാസം ഫയൽ ചെയ്തല്ലോ. ലേബലിൽ R അടിച്ചാൽ തീർന്നില്ലേ?"),
 ("A","A","ഫയൽ ചെയ്തു, പക്ഷേ ഇതുവരെ രജിസ്റ്റർ ആയിട്ടില്ല."),
 ("V","wide","എങ്കിൽ ഇപ്പോൾ TM മാത്രം. R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം. സത്യം പറഞ്ഞാൽ മതി: ഫയൽ ചെയ്തു, നടപടി നടക്കുന്നു."),
 ("A","A","തുന്നൽ നേരെ, മറുപടിയും നേരെ."),
 ("V","V","സൂചി കുത്തിയാൽ മാറും, തെറ്റായ R കുത്തിയാൽ മാറില്ല.")],
 "ഫയൽ ചെയ്താൽ TM,\nരജിസ്റ്റർ ആയാൽ R", CTA_TRADEMARK, theme="crm",
 cap_ml="ഇൻസ്റ്റഗ്രാമിൽ തുടങ്ങിയ ബ്ലൗസ് ലേബലിനോട് ഗൾഫിലെ ബൊട്ടീക്ക് ചോദിച്ചു: ബ്രാൻഡ് രജിസ്റ്റേർഡ് ആണോ? ഫയൽ ചെയ്താൽ TM മാത്രം, R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം. നിങ്ങളുടെ ലേബലിൽ TM ആണോ R ആണോ?",
 cap_en="A blouse label that started on Instagram was asked by a Gulf boutique whether the brand is registered. After filing you may use TM; R only after registration. TM or R on your label?",
 cap_mg="Instagram-il thudangiya blouse label-inodu Gulf-ile boutique chodichu: brand registered aano? File cheythaal TM maathram, R registration kittiya shesham. Ningalude label-il TM aano R aano?")

# FAQ: "the R looks premium, everyone puts it" (new place: pump-side car wash)
duo("tm036", "d2c_brand", "B", "petrolpump", "പമ്പിലെ കാർ വാഷ്\nബോർഡിൽ വലിയ R.\n\"ഭംഗിക്ക് ഇട്ടതാ\"", [
 ("A","wide","ഷിബൂ, പുതിയ കാർ വാഷ് ബോർഡിൽ പേരിന് അടുത്ത് ഒരു R ഇട്ടിട്ടുണ്ട്. കാണാൻ ഒരു ക്ലാസ് ഉണ്ട്."),
 ("V","V","സന്തോഷേട്ടാ, ആ പേര് ട്രേഡ്മാർക്ക് ആയി രജിസ്റ്റർ ആയോ?"),
 ("A","A","ഇല്ല. ഫയൽ പോലും ചെയ്തിട്ടില്ല. പക്ഷേ എല്ലാവരും ഇടുന്നുണ്ടല്ലോ."),
 ("V","wide","R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം. ഫയൽ ചെയ്താൽ TM ഇടാം. ഇപ്പോൾ ആദ്യം ഫയലിംഗ്."),
 ("A","A","അപ്പോ ഇന്ന് R മായ്ക്കണം, നാളെ ഫയൽ ചെയ്യണം."),
 ("V","V","കാർ കഴുകി തിളങ്ങട്ടെ, ബോർഡ് കള്ളം പറഞ്ഞ് തിളങ്ങരുത്.")],
 "R ഭംഗിക്കല്ല,\nരജിസ്ട്രേഷന് ശേഷം", CTA_BRAND, theme="faq",
 cap_ml="ബോർഡിൽ R ഭംഗിക്ക് ഇടാമോ? ഇല്ല. R രജിസ്ട്രേഷൻ കിട്ടിയ ശേഷം മാത്രം; ഫയൽ ചെയ്താൽ TM ഇടാം. നിങ്ങളുടെ ബോർഡിൽ ഏത് ചിഹ്നം?",
 cap_en="Can you put an R on your signboard because it looks premium? No. R only after registration; after filing you may use TM. Which symbol is on your board?",
 cap_mg="Board-il R bhangikku idaamo? Illa. R registration kittiya shesham maathram; file cheythaal TM idaam. Ningalude board-il ethu chihnam?")

# FAQ: "trademarks are only for products, not for a class or a studio" (yoga studio in a mall)
duo("tm037", "salon_clinic", "C", "mall", "\"യോഗ ക്ലാസിന്\nഎന്ത് ട്രേഡ്മാർക്ക്?\nസാധനം ഒന്നും ഇല്ലല്ലോ\"", [
 ("A","wide","ജാഫറേ, മാളിലെ യോഗ സ്റ്റുഡിയോയുടെ പേര് മൂന്നാം നിലയിലെ പുതിയ ജിമ്മും ഇട്ടിരിക്കുന്നു."),
 ("V","V","സുമയ്യാ, നമ്മൾ ഒരു സാധനവും വിൽക്കുന്നില്ലല്ലോ. സർവീസിന് ട്രേഡ്മാർക്ക് കിട്ടുമോ?"),
 ("A","A","അതാ ഞാനും കരുതിയത്. അതുകൊണ്ട് ഫയൽ ചെയ്തില്ല."),
 ("V","wide","45 ക്ലാസിൽ സർവീസുകൾക്കും ക്ലാസുണ്ട്. നിങ്ങൾ നൽകുന്ന സർവീസിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യാം."),
 ("A","A","ശ്വാസം ഫ്രീ, പേര് ഫ്രീ അല്ല."),
 ("V","V","പോസ് പഠിപ്പിക്കാം, പേര് കൊടുക്കേണ്ട.")],
 "സർവീസിനും ക്ലാസുണ്ട്,\nപേരിനും സംരക്ഷണമുണ്ട്", CTA_TRADEMARK, theme="faq",
 cap_ml="യോഗ സ്റ്റുഡിയോ, ട്യൂഷൻ, സലൂൺ: സാധനം വിൽക്കാത്തവർക്കും ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യാം. 45 ക്ലാസിൽ സർവീസുകൾക്കും ക്ലാസുണ്ട്; നിങ്ങളുടെ സർവീസിന്റെ ക്ലാസിൽ ഫയൽ ചെയ്യൂ. നിങ്ങൾ വിൽക്കുന്നത് സാധനമോ സർവീസോ?",
 cap_en="Yoga studios, tuition centres, salons: you can file a trademark even if you sell no product. The 45 classes include classes for services; file in the one for your service. Do you sell goods or a service?",
 cap_mg="Yoga studio, tuition, salon: saadhanam vilkkaathavarkkum trademark file cheyyaam. 45 class-il service-inum class undu; ningalude service-inte class-il file cheyyoo. Ningal vilkkunnathu saadhanamo service-o?")

# FAQ: "I can oppose a copycat whenever I find it" (window already closed)
duo("tm038", "copied_brand", "A", "foodcourt", "ഷവർമ ബ്രാൻഡിന്റെ\nഡ്യൂപ്ലിക്കേറ്റ് ജേണലിൽ.\n5 മാസം മുമ്പ്", [
 ("A","wide","ഡെന്നിസേ, നമ്മുടെ ഷവർമ കൗണ്ടറിന്റെ പോലത്തെ പേര് ജേണലിൽ വന്നിട്ട് 5 മാസമായി. ഇന്ന് എതിർക്കാം."),
 ("V","V","മരിയേ, ജേണലിൽ വന്നാൽ എതിർക്കാൻ എത്ര സമയം ഉണ്ട് എന്ന് അറിയാമോ?"),
 ("A","A","എപ്പോൾ വേണേലും പറ്റും എന്നാ കരുതിയത്."),
 ("V","wide","ജേണലിൽ പ്രസിദ്ധീകരിച്ച് 4 മാസത്തിനുള്ളിൽ മാത്രം ഓപ്പോസിഷൻ. നമ്മൾ ഒരു മാസം വൈകി."),
 ("A","A","അപ്പോ ഇനി നമ്മുടെ പേര് ആദ്യം ഫയൽ ചെയ്യണം, ജേണലും സ്ഥിരം നോക്കണം."),
 ("V","V","ഷവർമ ചൂടോടെ, എതിർപ്പ് സമയത്തോടെ.")],
 "ജേണലിൽ വന്നാൽ\nനാല് മാസം മാത്രം", CTA_BRAND, theme="faq",
 cap_ml="സമാനമായ ബ്രാൻഡ് ട്രേഡ്മാർക്ക് ജേണലിൽ വന്നാൽ എപ്പോൾ വേണേലും എതിർക്കാമോ? ഇല്ല. പ്രസിദ്ധീകരിച്ച് 4 മാസത്തിനുള്ളിൽ മാത്രം ഓപ്പോസിഷൻ. നിങ്ങൾ ജേണൽ നോക്കാറുണ്ടോ?",
 cap_en="Can you oppose a look-alike brand in the Trade Marks Journal whenever you notice it? No: opposition is only within 4 months of publication. Do you check the journal?",
 cap_mg="Samaanamaaya brand trademark journal-il vannaal eppol venelum ethirkkaamo? Illa. Publish cheythu 4 maasathinullil maathram opposition. Ningal journal nokkaarundo?")

# FAQ F5: "we searched, nobody has the name, so we're safe" (searched, never filed)
duo("tm039", "food_brand", "B", "canteen", "\"സെർച്ച് ചെയ്തു,\nആർക്കും ഇല്ല.\nനമ്മൾ സേഫ്!\"", [
 ("A","wide","അമലേ, ഓഫീസ് മീൽ ബോക്സിന്റെ പേര് ഞാൻ സെർച്ച് ചെയ്തു. ആരും ഫയൽ ചെയ്തിട്ടില്ല. നമ്മൾ സേഫ്."),
 ("V","V","ആതിരേ, ഇന്ന് ആരുമില്ല. നാളെ വേറൊരാൾ ആദ്യം ഫയൽ ചെയ്താലോ?"),
 ("A","A","സെർച്ച് ചെയ്താൽ പേര് നമ്മുടേതാകില്ലേ?"),
 ("V","wide","ഇല്ല. സെർച്ച് ഒരു നോട്ടം മാത്രം. ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്താലേ TM ഇടാൻ പറ്റൂ."),
 ("A","A","അപ്പോ സെർച്ചിന്റെ അതേ ദിവസം ഫയലിംഗും."),
 ("V","V","പേര് ഒഴിഞ്ഞുകിടക്കുന്നത് കണ്ടാൽ, ആദ്യം ഇരിക്കണം.")],
 "സെർച്ച് ഒരു നോട്ടം,\nഫയലിംഗ് ഒരു സീറ്റ്", CTA_TRADEMARK, theme="faq",
 cap_ml="ട്രേഡ്മാർക്ക് സെർച്ചിൽ ആരുമില്ല എന്ന് കണ്ടാൽ പേര് നിങ്ങളുടേതാകില്ല. ട്രേഡ് മാർക്ക്സ് രജിസ്ട്രിയിൽ ഫയൽ ചെയ്താലേ TM ഇടാൻ പറ്റൂ. നിങ്ങൾ സെർച്ച് ചെയ്തിട്ട് എത്ര ദിവസമായി?",
 cap_en="An empty trademark search does not make the name yours. Only a filing with the Trade Marks Registry lets you use TM. How long ago did you search?",
 cap_mg="Trademark search-il aarumilla ennu kandaal peru ningaludethaakilla. Trade Marks Registry-il file cheythaale TM idaan pattoo. Ningal search cheythittu ethra divasamaayi?")

# NEW (d904 pattern): an auto driver's tour name, painted and copied
duo("tm040", "copied_brand", "C", "autostand", "\"മൂന്നാർ റൈഡ്\"\nഎന്റെ ഓട്ടോയിൽ.\nഇപ്പോ 4 ഓട്ടോയിൽ", [
 ("A","wide","ഷാജീ, ഞാൻ ഇട്ട ടൂർ പേര് ഇപ്പോ സ്റ്റാൻഡിലെ നാല് ഓട്ടോയിൽ. ടൂറിസ്റ്റുകൾ എന്നെ എന്ന് കരുതി അവരെ വിളിക്കുന്നു."),
 ("V","V","സജിയേട്ടാ, ആ പേര് എവിടെയെങ്കിലും ഫയൽ ചെയ്തോ, അതോ പെയിന്റ് മാത്രമേ ഉള്ളോ?"),
 ("A","A","പെയിന്റും ഇൻസ്റ്റഗ്രാം പേജും മാത്രം."),
 ("V","wide","ടൂർ സർവീസിന്റെ ക്ലാസിൽ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യൂ. ഫയൽ ചെയ്താൽ TM, രജിസ്റ്റർ ആയാൽ R."),
 ("A","A","അപ്പോ പെയിന്റ് എല്ലാർക്കും വാങ്ങാം, പേര് ഫയൽ ചെയ്യുന്നവന്."),
 ("V","V","മീറ്റർ ഓടുന്നതിന് മുമ്പ് പേര് ഓടിക്കണം.")],
 "പെയിന്റ് എല്ലാർക്കും,\nപേര് ഫയൽ ചെയ്യുന്നവന്", CTA_BRAND, theme="new",
 cap_ml="ഓട്ടോയിൽ പെയിന്റ് ചെയ്ത ടൂർ പേര് കോപ്പി ചെയ്യാൻ എളുപ്പമാണ്. ടൂർ സർവീസിന്റെ ക്ലാസിൽ ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്യൂ: ഫയൽ ചെയ്താൽ TM, രജിസ്റ്റർ ആയാൽ R. നിങ്ങളുടെ പേര് പെയിന്റിലോ പേപ്പറിലോ?",
 cap_en="A tour name painted on an auto-rickshaw is easy to copy. File a trademark in the class for tour services: TM once filed, R once registered. Is your name only paint, or on paper?",
 cap_mg="Auto-yil paint cheytha tour peru copy cheyyaan eluppamaanu. Tour service-inte class-il trademark file cheyyoo: file cheythaal TM, register aayaal R. Ningalude peru paint-ilo paper-ilo?")

# NEW (d904 pattern): a famous private-bus name on toy bus models
duo("tm041", "d2c_brand", "A", "busstop", "ബസിന്റെ പേര്\nനാട്ടിൽ എല്ലാർക്കും അറിയാം.\nകളിപ്പാട്ട ബസിന്?", [
 ("A","wide","അഖിലേ, നമ്മുടെ ബസിന്റെ പേരിൽ കളിപ്പാട്ട ബസ് മോഡലുകൾ ഇറക്കാം. കുട്ടികൾക്ക് ആ പേര് ഭ്രാന്താ."),
 ("V","V","ജിബിനേ, ബസ് സർവീസിന്റെ പേര് ട്രേഡ്മാർക്ക് ചെയ്തിട്ടുണ്ടോ? ചെയ്തെങ്കിൽ ഏത് ക്ലാസിൽ?"),
 ("A","A","യാത്രാ സർവീസിന് ഫയൽ ചെയ്തിട്ടുണ്ട്. കളിപ്പാട്ടവും അതിൽ പെടില്ലേ?"),
 ("V","wide","ഇല്ല. 45 ക്ലാസുണ്ട്. കളിപ്പാട്ടം വേറെ ക്ലാസാ. ആ ക്ലാസിൽ കൂടി ഫയൽ ചെയ്യണം, എന്നിട്ട് ബോക്സിൽ TM."),
 ("A","A","റൂട്ട് ഒന്ന്, ക്ലാസ് രണ്ട്."),
 ("V","V","ബസ് റോഡിൽ ഓടും, കളിപ്പാട്ടം വേറെ ക്ലാസിൽ ഓടും.")],
 "റൂട്ട് ഒന്ന്,\nക്ലാസ് രണ്ട്", CTA_TRADEMARK, theme="new",
 cap_ml="നാട്ടിൽ പ്രശസ്തമായ ബസിന്റെ പേരിൽ കളിപ്പാട്ട മോഡൽ ഇറക്കുമ്പോൾ, യാത്രാ സർവീസിന്റെ ട്രേഡ്മാർക്ക് മതിയാകില്ല. 45 ക്ലാസിൽ കളിപ്പാട്ടം വേറെ ക്ലാസാണ്, അവിടെയും ഫയൽ ചെയ്യണം. നിങ്ങളുടെ നാട്ടിലെ ഫേവറിറ്റ് ബസ്?",
 cap_en="Launching toy models under a famous private bus's name? The trademark for the transport service does not cover toys: of the 45 classes, toys are a different one, so file there too. Your favourite local bus?",
 cap_mg="Naattil prasasthamaaya bus-inte peril kalippaatta model irakkumbol, yaathra service-inte trademark mathiyaakilla. 45 class-il kalippaattam vere class aanu, avideyum file cheyyanam. Ningalude naattile favourite bus?")
