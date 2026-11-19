# Company valuation batch 02 (19 Nov, month backlog). Facts only from topics.FACTS_VAL. Never state a value or a fee. People, firms and towns invented.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_VAL. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

duo("qv004", "esop_plan", "A", "office", "ടീമിന് ഷെയർ\nവാഗ്ദാനം ചെയ്തു.\nകണക്ക് ആര് ചെയ്യും?", [
 ("A","wide","രാഹുലേ, ആദ്യത്തെ അഞ്ച് ജീവനക്കാർക്ക് ഇസോപ്പ് കൊടുക്കാമെന്ന് പറഞ്ഞു."),
 ("V","V","നേഹ, ഓരോരുത്തർക്കും എത്ര ഷെയർ എന്ന് എങ്ങനെ തീരുമാനിക്കും?"),
 ("A","A","ഇസോപ്പ് കൊടുക്കുമ്പോൾ കമ്പനിയുടെ വാല്യുവേഷൻ വേണം. ഊഹം മതിയാകില്ല."),
 ("V","V","അപ്പോ വാക്ക് കൊടുക്കും മുമ്പ് ആദ്യം വാല്യുവേഷൻ."),
 ("A","wide","അതെ. ഏത് ആവശ്യത്തിന്, ഏത് തീയതിക്ക് എന്നും എഴുതണം."),
 ("V","wide","വാഗ്ദാനം പിന്നെ, കണക്ക് ആദ്യം.")],
 "ഇസോപ്പിന് മുമ്പ്\nവാല്യുവേഷൻ", CTA_VALUATION, theme="faq",
 cap_ml="ജീവനക്കാർക്ക് ഇസോപ്പ് നൽകുമ്പോൾ കമ്പനിയുടെ വാല്യുവേഷൻ വേണം. വാഗ്ദാനം ചെയ്യുന്നതിന് മുമ്പ് കണക്ക് ശരിയാക്കൂ. നിങ്ങൾ ടീമിന് ഷെയർ വാഗ്ദാനം ചെയ്തിട്ടുണ്ടോ?",
 cap_en="Issuing ESOPs to your team needs a company valuation, not a guess. Get it done before you promise shares. Have you already promised shares to anyone?",
 cap_mg="Team-nu ESOP kodukkumbol company valuation venam. Vaagdaanam cheyyunnathinu mumpu kanakku shariyaakku. Ningal team-nu share vaagdaanam cheythittundo?")

duo("qv005", "share_transfer", "B", "veranda", "അച്ഛന്റെ ഷെയർ\nമകന്.\nകണക്ക് വേണോ?", [
 ("A","wide","ബാലേട്ടാ, കമ്പനിയിലെ ഷെയർ മോന്റെ പേരിലേക്ക് മാറ്റുകയാണോ?"),
 ("V","V","ശാന്തേ, അതെ. കുടുംബത്തിനുള്ളിൽ അല്ലേ, പേപ്പർ മാത്രം മതിയല്ലോ."),
 ("A","A","ഷെയർ കൈമാറ്റത്തിന് വാല്യുവേഷൻ വേണ്ടിവരാം. കുടുംബമായാലും."),
 ("V","V","അപ്പോ ഒപ്പിടും മുമ്പ് ഒരാളോട് ചോദിക്കണം."),
 ("A","wide","അതെ. പിന്നീട് ചോദ്യം വന്നാൽ ഉത്തരം ആ രേഖയാണ്."),
 ("V","wide","സ്നേഹം വീട്ടിൽ, കണക്ക് പേപ്പറിൽ.")],
 "കുടുംബത്തിനുള്ളിലും\nഷെയർ കൈമാറ്റം രേഖയോടെ", CTA_WORTH, theme="crm",
 cap_ml="കുടുംബാംഗങ്ങൾക്കിടയിലെ ഷെയർ കൈമാറ്റത്തിനും വാല്യുവേഷൻ ആവശ്യമായേക്കാം. ഒപ്പിടുന്നതിന് മുമ്പ് പരിശോധിക്കൂ. നിങ്ങളുടെ കമ്പനിയിൽ ഷെയർ കൈമാറ്റം വരുന്നുണ്ടോ?",
 cap_en="Even a share transfer inside the family can need a valuation. Check before anyone signs. Is a share transfer coming up in your company?",
 cap_mg="Kudumbathinullile share transfer-num valuation venddivarum. Oppidunnathinu mumpu nokku. Ningalude company-il share transfer varunnundo?")

duo("qv006", "raising_round", "B", "rooftop", "\"അവർക്ക് കിട്ടിയത്ര\nനമുക്കും വേണം\"\nഅങ്ങനെയല്ല", [
 ("A","wide","ശ്യാമേ, അടുത്ത വീട്ടിലെ ആപ്പിന് കിട്ടിയ വാല്യുവേഷൻ നമുക്കും ചോദിക്കാം."),
 ("V","V","ആര്യേ, അവരുടെ കണക്കും നമ്മുടെ കണക്കും ഒന്നാണോ?"),
 ("A","A","താരതമ്യം ഒരു രീതിയാണ്. പക്ഷേ സമാന കമ്പനിയും സമാന ഘട്ടവും വേണം."),
 ("V","V","പിന്നെ നമ്മുടെ പ്രൊജക്ഷനും ട്രാക്ഷനും നോക്കും."),
 ("A","wide","അതെ. ആദ്യഘട്ട സ്റ്റാർട്ടപ്പുകൾക്ക് അതാണ് പ്രധാനം."),
 ("V","wide","അയൽക്കാരന്റെ നമ്പർ നമ്മുടേതല്ല.")],
 "താരതമ്യം ശരിയായ\nകമ്പനിയുമായി മാത്രം", CTA_VALUATION, theme="faq",
 cap_ml="ആദ്യഘട്ട സ്റ്റാർട്ടപ്പുകളുടെ വാല്യുവേഷൻ സമാന കമ്പനികളുമായുള്ള താരതമ്യവും പ്രൊജക്ഷനും അടിസ്ഥാനമാക്കിയാണ്. മറ്റൊരാളുടെ നമ്പർ പകർത്തരുത്. നിങ്ങൾ ഏത് കമ്പനിയുമായാണ് താരതമ്യം ചെയ്യുന്നത്?",
 cap_en="Early-stage valuations lean on comparable companies and your own projections. Copying another startup's number does not work. Which company are you comparing yourself to?",
 cap_mg="Early stage startup valuation comparable companies-um projections-um vechaanu. Vere aalude number copy cheyyaruthu. Ningal etha company-yumaayi compare cheyyunnu?")

duo("qv007", "partner_exit", "B", "tailor", "20 വർഷം പങ്കാളി.\nഇറങ്ങുമ്പോൾ\nതർക്കം", [
 ("A","wide","മോഹനേട്ടാ, കൂട്ടുകാരൻ ബിസിനസ്സിൽ നിന്ന് ഇറങ്ങുന്നു. അവന് എത്ര കൊടുക്കണം?"),
 ("V","V","ഉഷേ, അവൻ ഒരു തുക പറയുന്നു, ഞാൻ വേറൊന്ന്. രണ്ടും ഊഹമാണ്."),
 ("A","A","പങ്കാളി പുറത്തുപോകുമ്പോൾ വാല്യുവേഷനാണ് സാധാരണ വഴി. ആസ്തിയും വരുമാനവും നോക്കും."),
 ("V","V","അപ്പോ രണ്ടുപേരും അംഗീകരിക്കുന്ന ഒരു റിപ്പോർട്ട്."),
 ("A","wide","അതെ. തർക്കം കുറയും, സൗഹൃദവും നിൽക്കും."),
 ("V","wide","വാക്കിനേക്കാൾ നല്ലത് റിപ്പോർട്ട്.")],
 "പങ്കാളി ഇറങ്ങുമ്പോൾ\nഊഹമല്ല, റിപ്പോർട്ട്", CTA_WORTH, theme="crm",
 cap_ml="പങ്കാളി ബിസിനസ്സിൽ നിന്ന് പുറത്തുപോകുമ്പോൾ എത്ര കൊടുക്കണം എന്ന തർക്കം വാല്യുവേഷൻ റിപ്പോർട്ട് കുറയ്ക്കും. നിങ്ങളുടെ ബിസിനസ്സിൽ ആരെങ്കിലും പുറത്തുപോകുന്നുണ്ടോ?",
 cap_en="When a partner exits, a valuation report settles what their share is worth instead of two guesses. Is a partner planning to leave your business?",
 cap_mg="Partner purathu pokumbol ethra kodukkanam enna tharkkam valuation report kurakkum. Ningalude business-il aarenkilum purathu pokunnundo?")

duo("qv008", "nri_share_issue", "A", "gulfoffice", "ദുബായിൽ നിന്ന്\nനിക്ഷേപം.\nഫെയർ വാല്യു ആര് പറയും?", [
 ("A","wide","ആസിഫേ, നാട്ടിലെ കമ്പനിയിൽ നിക്ഷേപിക്കുന്നു. വാല്യുവേഷൻ ആര് ചെയ്യണം?"),
 ("V","V","ഷഹാനാ, ഏതെങ്കിലും ഒരാൾ എഴുതിയാൽ മതിയോ?"),
 ("A","A","പോരാ. അംഗീകൃത രീതിയിൽ CA, സെബി രജിസ്റ്റർ ചെയ്ത മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ്."),
 ("V","V","ഷെയർ ഫെയർ വാല്യുവിന് താഴെ കൊടുക്കാൻ പറ്റില്ലല്ലോ."),
 ("A","wide","അതെ. റിപ്പോർട്ട് ആദ്യം, പണം അയക്കൽ പിന്നെ."),
 ("V","wide","ആരുടെ ഒപ്പാണ് എന്നതും പ്രധാനം.")],
 "NRI നിക്ഷേപത്തിന്\nഅംഗീകൃത വാല്യുവർ", CTA_VALUATION, theme="faq",
 cap_ml="NRI അല്ലെങ്കിൽ വിദേശ നിക്ഷേപത്തിന് ഷെയർ ഫെയർ വാല്യുവിന് താഴെയാകരുത്. CA, സെബി രജിസ്റ്റർ ചെയ്ത മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സാക്ഷ്യപ്പെടുത്തണം. നിങ്ങളുടെ നിക്ഷേപകൻ വിദേശത്താണോ?",
 cap_en="For NRI or foreign investment, shares cannot go below fair value, certified by a CA, SEBI-registered merchant banker or cost accountant. Is your investor abroad?",
 cap_mg="NRI investment-nu share fair value-nu thaazhe aakaruthu. CA, SEBI merchant banker allenkil cost accountant certify cheyyanam. Ningalude investor videshathaano?")

duo("qv009", "raising_round", "A", "library", "പഴയ റിപ്പോർട്ട്\nപുതിയ റൗണ്ടിന്.\nപറ്റുമോ?", [
 ("A","wide","അനൂപേ, കഴിഞ്ഞ വർഷത്തെ വാല്യുവേഷൻ റിപ്പോർട്ട് ഈ റൗണ്ടിനും ഉപയോഗിക്കാമല്ലോ."),
 ("V","V","ഗ്രീഷ്മേ, അത് ഏത് തീയതിക്കായിരുന്നു?"),
 ("A","A","കഴിഞ്ഞ മാർച്ച്. ആവശ്യം വേറെയായിരുന്നു."),
 ("V","V","വാല്യുവേഷൻ ഒരു ആവശ്യത്തിനും ഒരു തീയതിക്കുമാണ്. പുതിയ റൗണ്ടിന് പുതിയത്."),
 ("A","wide","അപ്പോ കഴിഞ്ഞ വർഷത്തെ കണക്ക് ഇപ്പോൾ ബാധകമല്ല."),
 ("V","wide","തീയതി മാറിയാൽ റിപ്പോർട്ടും മാറും.")],
 "ഒരു റിപ്പോർട്ട്,\nഒരു ആവശ്യം, ഒരു തീയതി", CTA_VALUATION, theme="faq",
 cap_ml="വാല്യുവേഷൻ ഒരു പ്രത്യേക ആവശ്യത്തിനും തീയതിക്കുമുള്ളതാണ്. പഴയ റിപ്പോർട്ട് പുതിയ റൗണ്ടിന് ഉപയോഗിക്കാനാവില്ല. നിങ്ങളുടെ അവസാന റിപ്പോർട്ട് എന്ന് ചെയ്തതാണ്?",
 cap_en="A valuation is for a specific purpose and a specific date. Last year's report does not cover a new round. When was your last valuation done?",
 cap_mg="Valuation oru purpose-num oru date-num maathram. Pazhaya report puthiya round-nu pattilla. Ningalude last report eppol cheythathu?")

duo("qv010", "share_transfer", "A", "juiceshop", "ഷെയർ വിൽക്കുന്നു.\nഒരു നിബന്ധന\nആദ്യം നോക്കൂ", [
 ("A","wide","നൗഷാദേ, കടയുടെ കമ്പനിയിലെ എന്റെ ഷെയർ ഒരു സുഹൃത്തിന് കൊടുക്കാൻ ആലോചിക്കുന്നു."),
 ("V","V","റസിയാ, രണ്ടുപേരും സമ്മതിച്ച തുകയല്ലേ, പിന്നെന്ത്?"),
 ("A","A","ഷെയർ കൈമാറ്റത്തിന് ടാക്സ് നിയമപ്രകാരം ഫെയർ വാല്യു നോക്കും. കുറഞ്ഞാൽ ചോദ്യം വരാം."),
 ("V","V","അപ്പോ ആദ്യം വാല്യുവേഷൻ, പിന്നെ കരാർ."),
 ("A","wide","അതെ. രേഖയുണ്ടെങ്കിൽ ഇരുവർക്കും സുരക്ഷ."),
 ("V","wide","സമ്മതം മാത്രം പോരാ, രേഖയും വേണം.")],
 "ഷെയർ കൈമാറ്റത്തിന്\nഫെയർ വാല്യു നോക്കും", CTA_WORTH, theme="new",
 cap_ml="ഷെയർ കൈമാറ്റത്തിൽ ഫെയർ വാല്യു പ്രധാനമാണ്. സമ്മതിച്ച തുക മാത്രം പോരാ, വാല്യുവേഷൻ രേഖ ഇരുവർക്കും സുരക്ഷ നൽകും. നിങ്ങൾ ഷെയർ വിൽക്കാനോ വാങ്ങാനോ ആലോചിക്കുന്നുണ്ടോ?",
 cap_en="In a share transfer, fair value matters, not just the amount two people agree. A valuation protects both sides. Are you planning to buy or sell shares?",
 cap_mg="Share transfer-il fair value pradhaanam. Sammathicha thuka maathram pora, valuation rekha randu perkkum suraksha. Ningal share vilkkaano vaangaano aalochikkunnundo?")

duo("qv011", "raising_round", "B", "farm", "ഫാമിന്റെ മൂല്യം\nഭൂമി മാത്രമോ?\nവരുമാനവും", [
 ("A","wide","ഗോപീ, ഇൻവെസ്റ്റർ നമ്മുടെ ഫാമിന്റെ മൂല്യം ചോദിച്ചു. ഭൂമിയുടെ കണക്ക് കൊടുത്താലോ?"),
 ("V","V","വാസൂ, ഭൂമി മാത്രം നോക്കിയാൽ മതിയോ?"),
 ("A","A","ആസ്തി നോക്കുന്നത് ഒരു രീതി. വരുമാനം വെച്ചുള്ള ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ മറ്റൊന്ന്."),
 ("V","V","അപ്പോ ഏത് രീതി എന്ന് ആവശ്യം നോക്കി തീരുമാനിക്കും."),
 ("A","wide","അതെ. പലപ്പോഴും ഒന്നിലധികം രീതി ചേർത്ത് നോക്കും."),
 ("V","wide","നിലം മാത്രമല്ല, വിളവും കണക്കിൽ.")],
 "ആസ്തി ഒരു രീതി,\nവരുമാനം മറ്റൊന്ന്", CTA_VALUATION, theme="crm",
 cap_ml="വാല്യുവേഷന് പല രീതികളുണ്ട്: ആസ്തി അടിസ്ഥാനമാക്കിയ നെറ്റ് അസറ്റ് വാല്യു, വരുമാനം അടിസ്ഥാനമാക്കിയ ഡിസ്കൗണ്ടഡ് ക്യാഷ് ഫ്ലോ, താരതമ്യം. നിങ്ങളുടെ ബിസിനസ്സിന്റെ ശക്തി ആസ്തിയോ വരുമാനമോ?",
 cap_en="Valuation methods include net asset value, discounted cash flow and comparables. A farm is not only its land. Is your business's strength its assets or its income?",
 cap_mg="Valuation-nu pala reethikal: net asset value, discounted cash flow, comparables. Farm-nte bhoomi maathramalla. Ningalude business-nte shakthi assets-o income-o?")

duo("qv012", "esop_plan", "B", "cafe", "ഇസോപ്പ് പൂൾ\nഉണ്ടാക്കി.\nരേഖ എവിടെ?", [
 ("A","wide","റോഷാ, ടീമിന് ഇസോപ്പ് പൂൾ പ്രഖ്യാപിച്ചു. ഇനി എന്ത്?"),
 ("V","V","ആൽവിനേ, ഓരോ ഗ്രാന്റിനും ആ തീയതിയിലെ വാല്യുവേഷൻ വേണ്ടിവരും."),
 ("A","A","ഒരു തവണ ചെയ്താൽ എപ്പോഴും മതിയാകില്ലേ?"),
 ("V","V","ഇല്ല. വാല്യുവേഷൻ ഒരു തീയതിക്കുള്ളതാണ്. കമ്പനി വളരുമ്പോൾ മാറും."),
 ("A","wide","അപ്പോ ഓരോ ഘട്ടത്തിലും പുതുക്കണം."),
 ("V","wide","ടീമിന് വാക്ക്, കമ്പനിക്ക് രേഖ.")],
 "ഓരോ ഇസോപ്പ് ഗ്രാന്റിനും\nആ തീയതിയിലെ കണക്ക്", CTA_VALUATION, theme="new",
 cap_ml="ഇസോപ്പ് നൽകുമ്പോൾ ആ തീയതിയിലെ വാല്യുവേഷൻ വേണം. കമ്പനി വളരുമ്പോൾ അത് പുതുക്കണം. നിങ്ങളുടെ കമ്പനിയിൽ ഇസോപ്പ് പൂൾ ഉണ്ടോ?",
 cap_en="Each ESOP grant needs a valuation as of that date, and it changes as the company grows. Does your company have an ESOP pool yet?",
 cap_mg="ESOP kodukkumbol aa date-ile valuation venam. Company valarumbol puthukkanam. Ningalude company-il ESOP pool undo?")

duo("qv013", "raising_round", "A", "busstop", "റിപ്പോർട്ട് ഇല്ലാതെ\nപുതിയ ഷെയർ.\nരജിസ്റ്റേർഡ് വാല്യുവർ", [
 ("A","wide","അഖിലേ, പുതിയ നിക്ഷേപകർക്ക് പ്രിഫറൻഷ്യൽ ആയി ഷെയർ കൊടുക്കുന്നു."),
 ("V","V","ജിബിനേ, അതിന് വാല്യുവേഷൻ റിപ്പോർട്ട് വേണ്ടേ?"),
 ("A","A","വേണം. പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന് രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം."),
 ("V","V","അപ്പോ ഏതെങ്കിലും കണക്ക് പോരാ."),
 ("A","wide","അതെ. ആര് ഒപ്പിടുന്നു എന്നതും നിയമമാണ്."),
 ("V","wide","ഷെയർ കൊടുക്കും മുമ്പ് വാല്യുവർ.")],
 "പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിന്\nരജിസ്റ്റേർഡ് വാല്യുവർ", CTA_VALUATION, theme="faq",
 cap_ml="പ്രിഫറൻഷ്യൽ അലോട്ട്മെന്റിലൂടെ ഷെയർ നൽകുമ്പോൾ രജിസ്റ്റേർഡ് വാല്യുവറുടെ റിപ്പോർട്ട് വേണം. നിങ്ങൾ പുതിയ നിക്ഷേപകർക്ക് ഷെയർ നൽകുന്നുണ്ടോ?",
 cap_en="A preferential allotment of shares needs a registered valuer's report. Are you issuing new shares to investors soon?",
 cap_mg="Preferential allotment-il share kodukkumbol registered valuer-nte report venam. Ningal puthiya investors-nu share kodukkunnundo?")
