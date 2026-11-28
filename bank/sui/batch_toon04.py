# Toon batch 04 for sui (28 Nov night), episodes 9-11 of "വാസുവിന്റെ കയർ മെഷീൻ" (ep 8 teased "അടുത്ത സീസൺ"). Facts only from topics.FACTS_SUI.
# Never promise approval or a benefit; no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

# NEW: the tax-holiday window: 3 consecutive years must fit inside the first 10, so "after profits grow" can be too late
toon("ux09", "tech_founder", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ", "C": "അമൽ"}, "\"ലാഭം കൂടട്ടെ,\nഎന്നിട്ട് ടാക്സ് ഹോളിഡേ\"\nകമ്പനിക്ക് 8 വയസ്സ്", [
 ("C", "വാസുച്ചേട്ടാ, എന്റെ കമ്പനിക്ക് 8 വയസ്സായി. ലാഭം നന്നായി കൂടുന്നത് മൂന്ന് വർഷം കഴിഞ്ഞാ. അപ്പോൾ ടാക്സ് ഹോളിഡേ എടുക്കാം."),
 ("A", "അമ്മൂമ്മേ, ടാക്സ് ഹോളിഡേ എപ്പോൾ വേണമെങ്കിലും തുടങ്ങാമോ?"),
 ("B", "ഇല്ല മോനേ. ആദ്യ 10 വർഷത്തിനുള്ളിലെ തുടർച്ചയായ 3 വർഷമാണ്. മൂന്ന് വർഷം കഴിഞ്ഞ് തുടങ്ങാൻ നോക്കിയാൽ ആ ജനൽ അടഞ്ഞിരിക്കും."),
 ("C", "അപ്പോ ലാഭം നോക്കുന്നതിനൊപ്പം കലണ്ടറും നോക്കണം.")],
 dict(title="ടാക്സ് ഹോളിഡേ ജനൽ", rows=[("എത്ര", "ലാഭത്തിന്റെ 100%, 3 വർഷം"), ("ഏത് വർഷം", "ആദ്യ 10-ൽ തുടർച്ചയായ 3"), ("ആർക്ക്", "പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP")], total=("അപേക്ഷ", "DPIIT-ൽ നിന്ന് വേറെ")),
 ["ഇൻകോർപ്പറേഷൻ തീയതി നോക്കി 10 വർഷം എണ്ണി വെക്കുക.", "ടാക്സ് ഹോളിഡേ ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കേണ്ട വേറെ അപേക്ഷയാണ്."],
 "ആദ്യ 10 വർഷം കഴിഞ്ഞാൽ\nജനൽ അടയും", topics.CTA_BENEFITS, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=9, next="രണ്ടാം കമ്പനി", scene="office", theme="new",
 cap_ml='ടാക്സ് ഹോളിഡേ (80-IAC) ആദ്യ 10 വർഷത്തിനുള്ളിലെ തുടർച്ചയായ 3 വർഷത്തേക്കാണ്, അത് DPIIT-ൽ നിന്ന് വേറെ അപേക്ഷയും. 8 വയസ്സുള്ള കമ്പനി 3 വർഷം കാത്തിരുന്നാൽ ജനൽ അടയും. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര വയസ്സായി?',
 cap_en='The section 80-IAC tax holiday covers 3 consecutive years within the first 10 years, and it is a separate application from DPIIT recognition. A company that is 8 years old and waits 3 more years will find the window closed. How old is your company?',
 cap_mg='Tax holiday (80-IAC) aadya 10 varshathinullile thudarchayaaya 3 varshathekkaanu, athu DPIIT-il ninnu vere apekshayum. 8 vayassulla company 3 varsham kaathirunnaal janal adayum. Ningalude companykku ethra vayassaayi?')

# NEW: recognition belongs to the entity, not the founder: Vasu's new LLP must meet the criteria and apply on its own
toon("ux10", "tech_founder", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ"}, "പുതിയ LLP തുടങ്ങി.\n\"എനിക്ക് DPIIT\nഉണ്ടല്ലോ\"", [
 ("A", "അമ്മൂമ്മേ, കയർ ജിയോടെക്സ്റ്റൈലിന് ഞാൻ പുതിയൊരു LLP തുടങ്ങി. എനിക്ക് DPIIT ഉള്ളതുകൊണ്ട് അതിനും ബാധകമല്ലേ?"),
 ("B", "മോനേ, DPIIT നിനക്കല്ല, നിന്റെ കയർ മെഷീൻ കമ്പനിക്കാ കിട്ടിയത്. റെക്കഗ്നിഷൻ സ്ഥാപനത്തിനാണ്, ആൾക്കല്ല."),
 ("B", "പുതിയ LLP ഘടന, പ്രായം, ടേൺഓവർ, ഇന്നൊവേഷൻ എല്ലാം സ്വന്തമായി തെളിയിച്ച് വേറെ അപേക്ഷിക്കണം."),
 ("A", "അപ്പോ ഓരോ കുട്ടിക്കും സ്വന്തം ജനന സർട്ടിഫിക്കറ്റ്.")],
 dict(title="ഒരാൾ, രണ്ട് സ്ഥാപനം", rows=[("കയർ മെഷീൻ കമ്പനി", "DPIIT ഉണ്ട്"), ("പുതിയ LLP", "സ്വന്തം അപേക്ഷ"), ("ചെക്ക്", "ഘടന, പ്രായം, ടേൺഓവർ, ഇന്നൊവേഷൻ")], total=("റെക്കഗ്നിഷൻ", "സ്ഥാപനത്തിന്, ആൾക്കല്ല")),
 ["ഓരോ ഫോമിലും ഏത് സ്ഥാപനത്തിന്റെ DPIIT എന്ന് നോക്കുക.", "പുതിയ സ്ഥാപനത്തിന് പഴയതിന്റെ സർട്ടിഫിക്കറ്റ് ഉപയോഗിക്കരുത്."],
 "DPIIT കമ്പനിക്കാ,\nഫൗണ്ടർക്കല്ല", topics.CTA_DPIIT, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=10, next="പെട്ടിയിലെ ലോഗോ", scene="office", theme="new",
 cap_ml='DPIIT റെക്കഗ്നിഷൻ സ്ഥാപനത്തിനാണ്, ഫൗണ്ടർക്കല്ല. ഒരേ ആൾ പുതിയ LLP തുടങ്ങിയാൽ ആ LLP ഘടന, പ്രായം, ടേൺഓവർ, ഇന്നൊവേഷൻ നോക്കി സ്വന്തമായി അപേക്ഷിക്കണം. നിങ്ങൾക്ക് എത്ര സ്ഥാപനങ്ങളുണ്ട്?',
 cap_en='DPIIT recognition belongs to the entity, not the founder. If the same founder starts a new LLP, that LLP must apply on its own, meeting the structure, age, turnover and innovation tests. How many entities do you run?',
 cap_mg='DPIIT recognition sthaapanathinaanu, founderkkalla. Ore aal puthiya LLP thudangiyaal aa LLP structure, praayam, turnover, innovation nokki swanthamaayi apekshikkanam. Ningalkku ethra sthaapanangal undu?')

# FAQ: printing "government approved" on the product box because of DPIIT; recognition is startup status for the company, not a product quality mark
toon("ux11", "traditional_innovator", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ", "C": "അമൽ"}, "ചവിട്ടി പെട്ടിയിൽ:\n\"സർക്കാർ അംഗീകൃത\nഗുണനിലവാരം\"", [
 ("C", "വാസുച്ചേട്ടാ, പുതിയ കയർ ചവിട്ടിയുടെ പെട്ടിയിൽ വലുതായി എഴുതാം: DPIIT അംഗീകൃതം, സർക്കാർ ഉറപ്പുള്ള ഗുണനിലവാരം!"),
 ("A", "അമ്മൂമ്മേ, അത് നല്ല മാർക്കറ്റിംഗ് അല്ലേ?"),
 ("B", "അത് സത്യമല്ല മോനേ. DPIIT നിന്റെ കമ്പനിയെ സ്റ്റാർട്ടപ്പ് ആയി അംഗീകരിച്ചതാ. ചവിട്ടിയുടെ ഗുണനിലവാരം അത് നോക്കിയിട്ടില്ല."),
 ("A", "അപ്പോ പെട്ടിയിൽ ഗുണം, സർട്ടിഫിക്കറ്റ് ഫയലിൽ.")],
 dict(title="DPIIT എന്താണ്, എന്തല്ല", rows=[("ആണ്", "കമ്പനിക്ക് സ്റ്റാർട്ടപ്പ് അംഗീകാരം"), ("തുറക്കുന്നത്", "IP ഇളവ്, സ്കീം യോഗ്യത"), ("അല്ല", "ഉൽപ്പന്ന ഗുണനിലവാര മുദ്ര")], total=("പെട്ടിയിൽ", "സത്യം മാത്രം")),
 ["ബയറെ തെറ്റിദ്ധരിപ്പിക്കുന്ന ഒന്നും പെട്ടിയിൽ എഴുതരുത്.", "DPIIT കൊണ്ടുള്ള ഗുണം കമ്പനിക്കാണ്, ഉൽപ്പന്നത്തിന്റെ ഉറപ്പല്ല."],
 "ചവിട്ടിയുടെ ഗുണം\nചവിട്ടി തന്നെ പറയട്ടെ", topics.CTA_BENEFITS, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=11, next="വലിയ ഓർഡർ", scene="shop", theme="faq",
 cap_ml="DPIIT കമ്പനിയെ സ്റ്റാർട്ടപ്പ് ആയി അംഗീകരിക്കുന്നതാണ്, ഉൽപ്പന്നത്തിന്റെ ഗുണനിലവാര മുദ്രയല്ല. പെട്ടിയിൽ 'സർക്കാർ ഉറപ്പുള്ള ഗുണനിലവാരം' എന്ന് എഴുതരുത്. നിങ്ങളുടെ പാക്കിൽ എന്താണ് എഴുതിയത്?",
 cap_en="DPIIT recognises your company as a startup; it is not a quality mark for your product. Don't print 'government-certified quality' on the box because of it. What does your pack say?",
 cap_mg="DPIIT companye startup aayi angeekarikkunnathaanu, ulpannathinte gunanilavaara mudrayalla. Pettiyil 'sarkkaar urappulla gunanilavaaram' ennu ezhutharuthu. Ningalude packil enthaanu ezhuthiyathu?")
