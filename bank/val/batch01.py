# Company valuation batch 01 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_VAL. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_VALUATION, CTA_WORTH = topics.CTA_VALUATION, topics.CTA_WORTH

duo("qv001", "raising_round", "A", "canteen", "\"20 ലക്ഷം തരാം,\nഎത്ര ശതമാനം തരും?\"\nഉത്തരം ഇല്ല", [
 ("A","wide","അമൽ, നമ്മുടെ ടിഫിൻ സബ്സ്ക്രിപ്ഷന് ഒരു ഡോക്ടർ 20 ലക്ഷം ഇടാമെന്ന്. പക്ഷേ ചോദിച്ചു, എത്ര ശതമാനം തരും?"),
 ("V","V","നീ എന്ത് പറഞ്ഞു?"),
 ("A","A","ഒന്നും പറഞ്ഞില്ല. ഊഹിച്ച് 10% എന്ന് പറയാൻ പോയതാ."),
 ("V","wide","ഊഹിക്കരുത്. അതിനാ വാല്യുവേഷൻ. ഭാവി ക്യാഷ് ഫ്ലോ, സമാന കമ്പനികൾ, ആസ്തി. തുടക്കക്കാർക്ക് താരതമ്യവും പ്രൊജക്ഷനും."),
 ("A","A","അപ്പോ ശതമാനം കണക്കിൽ നിന്ന്, മൂഡിൽ നിന്നല്ല."),
 ("V","wide","അതെ. ടിഫിൻ പോലെ, അളന്ന് കൊടുക്കണം.")],
 "ശതമാനം ഊഹിക്കല്ലേ,\nവാല്യുവേഷൻ ചെയ്യൂ", CTA_VALUATION, theme="crm",
 cap_ml="ഇൻവെസ്റ്റർ ചോദിച്ചു: എത്ര ശതമാനം തരും? ഊഹിച്ച് ഷെയർ കൊടുക്കരുത്. വാല്യുവേഷൻ രീതികൾ: ഡിസിഎഫ്, സമാന കമ്പനികൾ, ആസ്തി മൂല്യം; തുടക്ക സ്റ്റാർട്ടപ്പുകൾക്ക് താരതമ്യവും പ്രൊജക്ഷനും. നിങ്ങൾ ആണെങ്കിൽ എത്ര ശതമാനം പറഞ്ഞേനെ?",
 cap_en="An angel offers money to a tiffin subscription startup and asks what percentage he gets. Don't guess: that's what a valuation is for. Methods include discounted cash flow, comparable companies and net asset value; early startups lean on comparables and projections.",
 cap_mg="Investor chodichu: ethra shathamaanam tharum? Oohichu share kodukkaruthu. Valuation methods: DCF, comparable companies, net asset value; early startups-nu comparables-um projection-um.")

duo("qv002", "nri_share_issue", "B", "airport", "സൗദിയിലെ ചേട്ടൻ\nഷെയർ വാങ്ങുന്നു.\n\"വാല്യുവേഷൻ എന്തിന്?\"", [
 ("A","wide","റഫീഖ്, അനിയന്റെ കൊച്ചിയിലെ കമ്പനിയിൽ ഞാൻ ഷെയർ എടുക്കുന്നു. അവൻ പറയുന്നു വാല്യുവേഷൻ റിപ്പോർട്ട് വേണമെന്ന്. സ്വന്തം അനിയനല്ലേ?"),
 ("V","V","ഇക്കാ, NRI ആയി റിപാട്രിയേഷൻ ബേസിസിൽ ഇട്ടാൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ കൊടുക്കാൻ പാടില്ല."),
 ("A","A","ആര് സർട്ടിഫൈ ചെയ്യും?"),
 ("V","wide","CA, SEBI രജിസ്റ്റേർഡ് മർച്ചന്റ് ബാങ്കർ, അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ്. അംഗീകൃത രീതിയിൽ."),
 ("A","A","കുടുംബമായാലും നിയമം ഒന്ന്, അല്ലേ?"),
 ("V","wide","അതെ. സ്നേഹം കുടുംബത്തിന്. ഫെയർ വാല്യു ഷെയറിന്.")],
 "NRI ഷെയറിന്\nഫെയർ വാല്യു വേണം", CTA_WORTH, theme="faq",
 cap_ml="ഗൾഫിലെ ചേട്ടൻ അനിയന്റെ കമ്പനിയിൽ ഷെയർ എടുക്കുമ്പോഴും വാല്യുവേഷൻ വേണം. NRI റിപാട്രിയേഷൻ ബേസിസിൽ ഷെയർ ഫെയർ വാല്യുവിൽ താഴെ പാടില്ല; CA, SEBI മർച്ചന്റ് ബാങ്കർ അല്ലെങ്കിൽ കോസ്റ്റ് അക്കൗണ്ടന്റ് സർട്ടിഫൈ ചെയ്യണം.",
 cap_en="A Malayali in Saudi Arabia is buying shares in his brother's Kochi company and asks why a valuation is needed. NRI investment on repatriation basis cannot be below fair value, certified by a CA, a SEBI-registered merchant banker or a cost accountant. Family or not, the rule is the same.",
 cap_mg="Gulf-ile chettan aniyante company-il share edukkumbozhum valuation venam. NRI repatriation basis-il share fair value-il thaazhe paadilla; CA, SEBI merchant banker allenkil cost accountant certify cheyyanam.")

duo("qv003", "partner_exit", "A", "courier", "പാർട്ണർ പോകുന്നു.\n\"എന്റെ 30%-ന്\nഎത്ര കിട്ടും?\"", [
 ("A","wide","അരവിന്ദ്, ഗിരീഷ് കമ്പനി വിടുകയാ. അവന്റെ 30% ഷെയറിന് എത്ര തരണം എന്ന് ചോദിക്കുന്നു."),
 ("V","V","അവൻ ഒരു നമ്പർ പറഞ്ഞോ?"),
 ("A","A","പറഞ്ഞു. ഞാൻ വേറൊന്ന്. രണ്ടും വായുവിൽ നിന്ന്."),
 ("V","wide","അതുകൊണ്ടാ വാല്യുവേഷൻ. പാർട്ണർ എക്സിറ്റിനും ഷെയർ ട്രാൻസ്ഫറിനും ഒരു നിശ്ചിത തീയതിയിലെ മൂല്യം, അംഗീകൃത രീതിയിൽ."),
 ("A","A","അപ്പോ തർക്കം കുറയും."),
 ("V","wide","അതെ. പിരിയുന്നത് സുഹൃത്തുക്കളായി. കണക്ക് റിപ്പോർട്ടിൽ.")],
 "എക്സിറ്റിന് മുമ്പ്\nവാല്യുവേഷൻ", CTA_VALUATION, theme="new",
 cap_ml="പാർട്ണർ കമ്പനി വിടുമ്പോൾ അയാളുടെ 30% ഷെയറിന് എത്ര? ഊഹക്കണക്ക് തർക്കമാകും. പാർട്ണർ എക്സിറ്റിനും ഷെയർ ട്രാൻസ്ഫറിനും ഒരു നിശ്ചിത ആവശ്യത്തിനും തീയതിക്കുമുള്ള വാല്യുവേഷൻ.",
 cap_en="A co-founder of a courier franchise is leaving and asks what his 30% is worth; both sides have numbers pulled from thin air. A valuation for a partner exit or share transfer gives a value for that purpose and date, by an accepted method, and keeps the split friendly.",
 cap_mg="Partner company vidumbol ayaalude 30% share-nu ethra? Oohakkanakku tharkkamaakum. Partner exit-num share transfer-num oru nishchitha purpose-num date-num ulla valuation.")
