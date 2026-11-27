# nri batch 03 (27 Nov night): PMEGP reels from the verified PMEGP line added to topics.FACTS_NRI (27 Nov).
# Never promise a loan or subsidy; banks sanction the loan; tell people to check the live guidelines. Invented names and places.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_PRAVASI, CTA_NORKA = topics.CTA_PRAVASI, topics.CTA_NORKA

# faq: a returnee who already runs a thattukada wants PMEGP to expand it; PMEGP is for new units
duo("pvd007", "family_business_nri", "B", "thattukada", "തട്ടുകട വലുതാക്കാൻ\nPMEGP എടുക്കാം\nഎന്ന് പ്ലാൻ", [
 ("A","wide","ബിജൂ, ഗൾഫിൽ നിന്ന് വന്ന് തുടങ്ങിയ ഈ തട്ടുകട വലുതാക്കാൻ PMEGP-ക്ക് അപേക്ഷിക്കാം എന്ന് കരുതി."),
 ("V","V","സിജോ, PMEGP പുതിയ യൂണിറ്റുകൾക്കാണ്. ഇപ്പോൾ നടക്കുന്ന യൂണിറ്റിന് ആ സ്കീം പറ്റില്ല."),
 ("A","A","അപ്പോ വലുതാക്കാൻ വേറെ വഴി നോക്കണം. ബാങ്കിനോട് ചോദിക്കാം."),
 ("V","V","അതെ. ഏത് സ്കീമിനും മുമ്പ് നിബന്ധന വായിക്കണം. ലോൺ തീരുമാനിക്കുന്നത് ബാങ്കാണ്."),
 ("A","wide","സ്കീമിന്റെ പേര് മാത്രം പോരാ, നിബന്ധനയും വേണം.")],
 "PMEGP പുതിയ\nയൂണിറ്റുകൾക്ക്", CTA_PRAVASI, theme="faq",
 cap_ml="ഇപ്പോൾ നടക്കുന്ന കട വലുതാക്കാൻ PMEGP നോക്കുന്നുണ്ടോ? PMEGP പുതിയ യൂണിറ്റുകൾക്കാണ്; നിലവിലുള്ള യൂണിറ്റുകൾക്കും മറ്റൊരു സർക്കാർ സബ്സിഡി കിട്ടിയ യൂണിറ്റുകൾക്കും അർഹതയില്ല. ലോൺ ബാങ്കാണ് തീരുമാനിക്കുന്നത്; ഇപ്പോഴത്തെ നിബന്ധനകൾ നോക്കൂ. നിങ്ങളുടെ ബിസിനസ് പുതിയതാണോ, നിലവിലുള്ളതാണോ?",
 cap_en="A Gulf returnee plans to use PMEGP to expand the thattukada he already runs. PMEGP is for new units: existing units, and units that already got another government subsidy, are not eligible. Banks sanction the loan; check the current guidelines. Is your business new or already running?",
 cap_mg="Ippol nadakkunna kada valuthaakkaan PMEGP nokkunnundo? PMEGP puthiya unit-ukalkkaanu; nilavilulla unit-ukalkkum mattoru sarkkaar subsidy kittiya unit-ukalkkum arhathayilla. Loan bank aanu theerumaanikkunnathu; ippozhathe nibandhanakal nokku. Ningalude business puthiyathaano, nilavilullathaano?")

# crm (returnee planning a village unit, invented): a woman weaver in a village; special category rural rate, own share 5%
duo("pvd008", "gulf_returnee", "B", "handloom", "ഗ്രാമത്തിൽ\nകൈത്തറി യൂണിറ്റ്.\nസ്വന്തം പങ്ക് എത്ര?", [
 ("A","wide","കുമാറേ, ഷാർജയിലെ ജോലി വിട്ടു. ഗ്രാമത്തിൽ ഒരു കൈത്തറി യൂണിറ്റ് തുടങ്ങണം. PMEGP-യിൽ എന്റെ പങ്ക് എത്ര വേണം?"),
 ("V","V","ലീലേ, സ്ത്രീകൾ പ്രത്യേക വിഭാഗത്തിലാണ്. സ്വന്തം പങ്ക് പ്രോജക്റ്റിന്റെ 5%. ജനറൽ വിഭാഗത്തിന് 10%."),
 ("A","A","സബ്സിഡിയോ? അതും ഗ്രാമമാണോ നഗരമാണോ എന്ന് നോക്കിയാണോ?"),
 ("V","V","അതെ, പ്രത്യേക വിഭാഗത്തിന് ഗ്രാമത്തിൽ 35%, നഗരത്തിൽ 25%. പക്ഷേ ലോൺ ബാങ്ക് അനുവദിച്ചാൽ മാത്രം."),
 ("A","wide","അർഹത നോക്കി, പങ്ക് ഒരുക്കി, പിന്നെ അപേക്ഷ.")],
 "സ്വന്തം പങ്ക് ആദ്യം\nഒരുക്കൂ", CTA_PRAVASI, theme="crm",
 cap_ml="PMEGP-യിൽ സ്വന്തം പങ്ക്: ജനറൽ വിഭാഗം പ്രോജക്റ്റിന്റെ 10%, സ്ത്രീകൾ ഉൾപ്പെടെ പ്രത്യേക വിഭാഗങ്ങൾ 5%. മാർജിൻ മണി സബ്സിഡി ജനറൽ 15% (നഗരം) / 25% (ഗ്രാമം), പ്രത്യേക വിഭാഗം 25% / 35%. ലോൺ ബാങ്കാണ് അനുവദിക്കുന്നത്; സബ്സിഡി ഉറപ്പല്ല. ഇപ്പോഴത്തെ ഗൈഡ്‌ലൈൻ നോക്കൂ. നിങ്ങളുടെ യൂണിറ്റ് ഗ്രാമത്തിലാണോ നഗരത്തിലാണോ?",
 cap_en="A woman back from Sharjah plans a handloom unit in her village. Under PMEGP, own contribution is 10% of project cost for the general category and 5% for special categories, women included. Margin-money subsidy: general 15% urban / 25% rural, special 25% / 35%. The bank sanctions the loan, so nothing is certain; check the current guidelines. Is your unit rural or urban?",
 cap_mg="PMEGP-yil swantham panku: general category project-inte 10%, sthreekal ulppede special categories 5%. Margin money subsidy general 15% (nagaram) / 25% (graamam), special 25% / 35%. Loan bank aanu anuvadikkunnathu; subsidy urappalla. Ippozhathe guidelines nokku. Ningalude unit graamathilaano nagarathilaano?")

# new: a returnee who already got a NORKA subsidy for the same unit plans PMEGP subsidy on top
duo("pvd009", "returnee_loan", "B", "veranda", "ഒരു യൂണിറ്റിന്\nരണ്ട് സബ്സിഡി\nഎന്നാ കണക്ക്", [
 ("A","wide","ബാലേട്ടാ, മോന്റെ പ്രിന്റിംഗ് യൂണിറ്റിന് ഒരു സർക്കാർ സബ്സിഡി കിട്ടി. ഇനി PMEGP സബ്സിഡിയും ചോദിക്കാം എന്ന് അവൻ പറയുന്നു."),
 ("V","V","ശാന്തേ, മറ്റൊരു കേന്ദ്ര, സംസ്ഥാന സർക്കാർ സ്കീമിൽ സബ്സിഡി കിട്ടിയ യൂണിറ്റിന് PMEGP-ക്ക് അർഹതയില്ല."),
 ("A","A","അപ്പോ രണ്ടും കണക്കിൽ കൂട്ടിയത് തെറ്റാണ്."),
 ("V","V","അതെ. ഏത് സ്കീം ഏത് യൂണിറ്റിന് എന്ന് ആദ്യം ഉറപ്പാക്കണം."),
 ("A","wide","ഒരു യൂണിറ്റ്, ഒരു വഴി.")],
 "ഒരു യൂണിറ്റിന്\nരണ്ട് സബ്സിഡി ഇല്ല", CTA_PRAVASI, theme="new",
 cap_ml="ഒരു യൂണിറ്റിന് ഒരു സർക്കാർ സബ്സിഡി കിട്ടിയ ശേഷം PMEGP-യും ചോദിക്കാൻ പ്ലാനുണ്ടോ? മറ്റൊരു കേന്ദ്ര / സംസ്ഥാന സർക്കാർ സ്കീമിൽ സബ്സിഡി കിട്ടിയ യൂണിറ്റിന് PMEGP-ക്ക് അർഹതയില്ല. ഏത് സ്കീം എന്ന് ആദ്യം ഉറപ്പാക്കൂ. നിങ്ങളുടെ യൂണിറ്റിന് ഇതുവരെ ഏതെങ്കിലും സബ്സിഡി കിട്ടിയോ?",
 cap_en="A returnee family plans a PMEGP subsidy for a printing unit that already got another government subsidy. A unit that has already availed a subsidy under another central or state government scheme is not eligible for PMEGP. Decide which scheme fits first. Has your unit had a subsidy before?",
 cap_mg="Oru unit-inu oru sarkkaar subsidy kittiya shesham PMEGP-yum chodikkaan plan undo? Mattoru central / state sarkkaar scheme-il subsidy kittiya unit-inu PMEGP-kku arhathayilla. Ethu scheme ennu aadyam urappaakku. Ningalude unit-inu ithuvare ethenkilum subsidy kitti-o?")
