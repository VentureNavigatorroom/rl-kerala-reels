# pg batch 02 (27 Nov evening refill): 3D duo reels. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns (STORY_THEMES rule). Facts only from topics.FACTS_PG. Never a gateway's fees, never promise activation, never recommend one gateway.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_GATEWAY, CTA_PAYMENT = topics.CTA_GATEWAY, topics.CTA_PAYMENT

# new: a home bakery's settlement account is in the husband's name, the business is in the wife's
duo("pgd006", "proprietor_pg", "B", "bakery", "ബേക്കറി എന്റെ പേരിൽ.\nബാങ്ക് അക്കൗണ്ട്\nഭർത്താവിന്റെ പേരിൽ", [
 ("A","wide","സാബൂ, കേക്ക് ഓർഡറിന്റെ ഗേറ്റ്‌വേ അപേക്ഷ നിന്നുപോയി. ബാങ്ക് അക്കൗണ്ട് ശരിയല്ല എന്ന്."),
 ("V","V","ജിഷേ, എന്റെ അക്കൗണ്ട് അല്ലേ കൊടുത്തത്? നമ്മൾ രണ്ടാളും ഒന്നല്ലേ?"),
 ("A","A","വീട്ടിൽ ഒന്നാണ്. പക്ഷേ ബിസിനസ് രേഖ എന്റെ പേരിൽ. പൈസ വരേണ്ട അക്കൗണ്ടും ബിസിനസിന്റെ പേരിൽ തന്നെ വേണം."),
 ("V","V","അപ്പോ ആദ്യം ബേക്കറിയുടെ പേരിൽ ഒരു അക്കൗണ്ട്. പിന്നെ അപേക്ഷ."),
 ("A","wide","ഒരു വീട്, പക്ഷേ ബിസിനസിന് സ്വന്തം അക്കൗണ്ട്.")],
 "ബിസിനസ് പേര്,\nഅതേ പേരിൽ അക്കൗണ്ട്", CTA_PAYMENT, theme="new",
 cap_ml="ബിസിനസ് ഒരാളുടെ പേരിൽ, ബാങ്ക് അക്കൗണ്ട് മറ്റൊരാളുടെ പേരിൽ ആണോ? പേയ്മെന്റ് ഗേറ്റ്‌വേയിൽ പൈസ വരുന്ന അക്കൗണ്ട് ബിസിനസിന്റെ പേരിൽ തന്നെ വേണം. പേര് ഒത്തുപോയില്ലെങ്കിൽ ആക്ടിവേഷൻ വൈകും. നിങ്ങളുടെ ബിസിനസ് അക്കൗണ്ട് ആരുടെ പേരിലാണ്?",
 cap_en="A home baker's gateway application stalls because she gave her husband's bank account. The settlement account has to be in the business's name, matching the business documents; a mismatch delays or blocks activation. Whose name is your business account in?",
 cap_mg="Business oraalude perilum bank account vereyaalude perilum aano? Payment gateway-il paisa varunna account business-inte peril thanne venam. Peru othupoyillenkil activation vaikum. Ningalude business account aarude perilaanu?")

# faq: a two-director garage company applies with one director's signature and no board resolution
duo("pgd007", "new_company_pg", "B", "garage", "രണ്ട് ഡയറക്ടർ.\nഒരാൾ ഒറ്റയ്ക്ക് ഒപ്പിട്ടു.\nഗേറ്റ്‌വേ ചോദ്യം വന്നു", [
 ("A","wide","ജിതിനേ, ഗേറ്റ്‌വേ ചോദിക്കുന്നു: കമ്പനിക്ക് വേണ്ടി ഒപ്പിടാൻ ഐശ്വര്യക്ക് ആര് അധികാരം തന്നു എന്ന്."),
 ("V","V","നീ ഡയറക്ടർ അല്ലേ? അത് മതിയല്ലോ."),
 ("A","A","കമ്പനിയുടെ കാര്യത്തിൽ അത് പോരാ. ബോർഡ് റെസല്യൂഷനോ ഓതറൈസേഷനോ വേണം. ഒപ്പിടുന്ന ആളിന്റെ KYC-യും."),
 ("V","V","ശരി, ഇന്ന് തന്നെ ബോർഡ് റെസല്യൂഷൻ പാസാക്കാം. രണ്ടാളും ഒപ്പിടാം."),
 ("A","wide","ഡയറക്ടർ ആയാൽ പോരാ, ബോർഡിന്റെ സമ്മതം വേണം.")],
 "ആര് ഒപ്പിടും?\nബോർഡ് തീരുമാനിക്കണം", CTA_GATEWAY, theme="faq",
 cap_ml="കമ്പനിക്ക് ഗേറ്റ്‌വേ അപേക്ഷിക്കുമ്പോൾ ഒരു ഡയറക്ടർ ഒറ്റയ്ക്ക് ഒപ്പിട്ടാൽ മതിയോ? പ്രൈവറ്റ് ലിമിറ്റഡിന് ബോർഡ് റെസല്യൂഷനോ ഓതറൈസേഷനോ, ഒപ്പിടുന്ന ആളിന്റെ KYC-യും ചോദിക്കും. നിങ്ങളുടെ കമ്പനിയിൽ ആരാണ് ഒപ്പിടുന്നത്?",
 cap_en="Two directors run a garage company; one signs the gateway application alone and the gateway asks who authorised her. A private limited company needs a board resolution or authorisation, plus KYC of the person signing. Who signs for your company?",
 cap_mg="Company-kku gateway apekshikkumbol oru director ottaykku oppittaal mathiyo? Private limited-inu board resolution-o authorisation-o, oppidunna aalinte KYC-yum chodikkum. Ningalude company-il aaraanu oppidunnathu?")

# crm (F3-style, invented): a new hotel company gives the old proprietorship's bank account for the company's gateway
duo("pgd008", "new_company_pg", "B", "hotellobby", "കമ്പനി പുതിയത്.\nബാങ്ക് അക്കൗണ്ട്\nപഴയ പ്രൊപ്രൈറ്ററുടേത്", [
 ("A","wide","ജെയ്സണേ, ഹോട്ടൽ ഇപ്പോൾ പ്രൈവറ്റ് ലിമിറ്റഡ് ആണ്. പക്ഷേ ഗേറ്റ്‌വേയിൽ കൊടുത്തത് പഴയ പ്രൊപ്രൈറ്റർഷിപ്പ് അക്കൗണ്ട്."),
 ("V","V","നീതൂ, പൈസ വരാൻ ഏത് അക്കൗണ്ട് ആയാലെന്താ? അതിൽ ട്രാൻസാക്ഷൻ ഒക്കെ ഉണ്ടല്ലോ."),
 ("A","A","കമ്പനിയുടെ PAN, കമ്പനിയുടെ പേര്, പഴയ അക്കൗണ്ടിൽ വേറെ പേര്. പേര് ഒത്തില്ലെങ്കിൽ ആക്ടിവേഷൻ വൈകും, റിജക്ടും ആകാം."),
 ("V","V","അപ്പോ ആദ്യം കമ്പനിയുടെ പേരിൽ കറന്റ് അക്കൗണ്ട്. എന്നിട്ട് ഗേറ്റ്‌വേ."),
 ("A","wide","ബിസിനസ് മാറിയാൽ അക്കൗണ്ടും മാറണം.")],
 "പുതിയ കമ്പനി,\nപുതിയ അക്കൗണ്ട്", CTA_GATEWAY, theme="crm",
 cap_ml="പ്രൊപ്രൈറ്റർഷിപ്പിൽ നിന്ന് കമ്പനി ആയോ? ഗേറ്റ്‌വേയിൽ കമ്പനിയുടെ PAN, കമ്പനിയുടെ പേര്, അതേ പേരിൽ ഉള്ള ബാങ്ക് അക്കൗണ്ട് വേണം. പഴയ അക്കൗണ്ട് കൊടുത്താൽ ആക്ടിവേഷൻ വൈകാം. നിങ്ങൾ കമ്പനിയുടെ പേരിൽ കറന്റ് അക്കൗണ്ട് തുറന്നോ?",
 cap_en="A hotel turned its proprietorship into a private limited company, then gave the old proprietorship's bank account to the gateway. The company's PAN, name and settlement account must match, or activation is delayed or rejected. Has your company opened its own current account?",
 cap_mg="Proprietorship-il ninnu company aayo? Gateway-il company-yude PAN, company-yude peru, athe peril ulla bank account venam. Pazhaya account koduthaal activation vaikaam. Ningal company-yude peril current account thurannu-o?")

# new: "which gateway is the best?" (we never pick one) - the KYC set is the same whichever you choose
duo("pgd009", "service_pro_pg", "B", "gym", "\"ഏത് ഗേറ്റ്‌വേ ആണ്\nബെസ്റ്റ്?\" എന്ന്\nമൂന്ന് ദിവസം ചർച്ച", [
 ("A","wide","ജസ്റ്റിനേ, ഫിറ്റ്നസ് ക്ലാസിന്റെ ഓൺലൈൻ പേയ്മെന്റിന് ഏത് ഗേറ്റ്‌വേ എടുക്കും? മൂന്ന് ദിവസമായി ആലോചിക്കുന്നു."),
 ("V","V","റിയേ, ഏത് എടുത്താലും ആദ്യം അവർ ബിസിനസിന്റെ KYC ചെയ്യും. അത് RBI നിയമമാണ്."),
 ("A","A","അപ്പോ ആദ്യം രേഖകൾ ശരിയാക്കിയാൽ ഏത് ഗേറ്റ്‌വേ ആയാലും എളുപ്പം?"),
 ("V","V","അതെ. ID, ബിസിനസ് രേഖ, ബിസിനസ് പേരിൽ അക്കൗണ്ട്. പേര് എല്ലാത്തിലും ഒരുപോലെ."),
 ("A","wide","ഗേറ്റ്‌വേ ഏതായാലും, രേഖകളാണ് ആദ്യം.")],
 "ഏത് ഗേറ്റ്‌വേ ആയാലും\nരേഖകൾ ആദ്യം", CTA_PAYMENT, theme="new",
 cap_ml="ഏത് പേയ്മെന്റ് ഗേറ്റ്‌വേ എടുക്കണം എന്ന് ആലോചിച്ച് സമയം പോകുന്നുണ്ടോ? ഏത് എടുത്താലും ലൈവ് പേയ്മെന്റിന് മുമ്പ് ബിസിനസിന്റെ KYC ഉണ്ട്. ID, ബിസിനസ് രേഖ, ബിസിനസ് പേരിൽ ബാങ്ക് അക്കൗണ്ട്, എല്ലാത്തിലും ഒരേ പേര്. നിങ്ങളുടെ രേഖകൾ റെഡി ആണോ?",
 cap_en="A fitness coach spends three days deciding which gateway to pick. Whichever one you choose, it runs KYC on your business before live payments: ID, a business proof, an account in the business's name, the same name everywhere. Get those ready first. Are yours ready?",
 cap_mg="Ethu payment gateway edukkanam ennu aalochichu samayam pokunnundo? Ethu eduthaalum live payment-inu mumbu business-inte KYC undu. ID, business rekha, business peril bank account, ellaathilum ore peru. Ningalude rekhakal ready aano?")
