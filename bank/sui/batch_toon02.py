# Toon batch 02 (23 Nov), episodes 3-6: 2D cartoon story series (owner's new style, A/B test against the 3D tea-shop reels).
# Hero + mentor (appooppan / ammoomma) + friend; story -> breakdown card -> mentor's rules. Facts only from topics.py. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics

toon("ux03", "grant_seeker", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ"}, "DPIIT കിട്ടി.\nടാക്സ് ഹോളിഡേയും\nകിട്ടിയോ?", [
 ("A", "അമ്മൂമ്മേ, DPIIT കിട്ടിയല്ലോ. ഇനി 3 വർഷം ടാക്സ് വേണ്ടല്ലോ?"),
 ("B", "ഇല്ല മോനേ. 80-IAC ടാക്സ് ഹോളിഡേ വേറെ അപേക്ഷയാണ്. ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കണം.")],
 dict(title="80-IAC", rows=[("DPIIT", "ആദ്യം വേണം"), ("80-IAC", "വേറെ അപേക്ഷ"), ("അംഗീകാരം", "ബോർഡ്")], total=("ഓട്ടോമാറ്റിക്", "അല്ല")),
 ["DPIIT കിട്ടിയാൽ 80-IAC വേറെ അപേക്ഷിക്കുക.", "Pvt Ltd അല്ലെങ്കിൽ LLP ആയിരിക്കണം."],
 "DPIIT ≠\nടാക്സ് ഹോളിഡേ", topics.CTA_BENEFITS, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=3, next="പഴയ കമ്പനി", scene="office", theme="faq")

toon("ux04", "investor_ready", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ"}, "12 വർഷം പഴയ\nകമ്പനിക്ക്\nDPIIT?", [
 ("A", "അമ്മൂമ്മേ, എന്റെ കമ്പനിക്ക് 12 വർഷമായി. പുതിയ പ്രൊഡക്റ്റിന് DPIIT കിട്ടുമോ?"),
 ("B", "സാധാരണ 10 വർഷത്തിൽ താഴെ വേണം. ഡീപ്-ടെക് ആണെങ്കിൽ 20 വർഷം വരെ.")],
 dict(title="പ്രായവും ടേൺഓവറും", rows=[("സാധാരണ", "10 വർഷം"), ("ഡീപ്-ടെക്", "20 വർഷം"), ("ടേൺഓവർ", "200 കോടി വരെ")], total=("പ്രായം കടന്നാൽ", "കിട്ടില്ല")),
 ["സമയം കഴിയും മുമ്പ് അപേക്ഷിക്കുക.", "ഡീപ്-ടെക് ആണോ എന്ന് പരിശോധിക്കുക."],
 "10 വർഷം\nകഴിയും മുമ്പ്", topics.CTA_DPIIT, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=4, next="വിദ്യാർത്ഥികൾ", scene="office", theme="faq")

toon("ux05", "student_founder", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ", "C": "അമൽ"}, "കോളേജ് ടീം.\nDPIIT പറ്റുമോ?", [
 ("C", "വാസുച്ചേട്ടാ, ഞങ്ങൾ കോളേജ് ടീമാ. കമ്പനി ഇല്ല. DPIIT കിട്ടുമോ?"),
 ("B", "ആദ്യം Pvt Ltd, LLP അല്ലെങ്കിൽ രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് വേണം. ടീം മാത്രം പോരാ.")],
 dict(title="DPIIT-ക്ക് മുമ്പ്", rows=[("കോളേജ് ടീം", "പറ്റില്ല"), ("പ്രൊപ്രൈറ്റർഷിപ്പ്", "പറ്റില്ല"), ("Pvt Ltd / LLP", "പറ്റും")], total=("ആദ്യ സ്റ്റെപ്പ്", "സ്ട്രക്ചർ")),
 ["ടീം ആണെങ്കിൽ ആദ്യം കമ്പനി രജിസ്റ്റർ ചെയ്യുക.", "ഇന്നൊവേഷൻ വ്യക്തമായി എഴുതുക."],
 "ടീം → കമ്പനി →\nDPIIT", topics.CTA_DPIIT, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=5, next="ടെൻഡറുകൾ", scene="classroom", theme="faq")

toon("ux06", "tech_founder", "B", {"A": "വാസു", "B": "അമ്മൂമ്മ"}, "DPIIT ഉണ്ട്.\nഉറപ്പായും\nഗ്രാന്റ് കിട്ടുമോ?", [
 ("A", "അമ്മൂമ്മേ, DPIIT ഉള്ളതുകൊണ്ട് സർക്കാർ ഗ്രാന്റ് ഉറപ്പല്ലേ?"),
 ("B", "ഉറപ്പില്ല. DPIIT പല സ്കീമുകൾക്കും യോഗ്യത തരും. സെലക്ഷൻ ഓരോ സ്കീമിന്റെയും തീരുമാനമാണ്.")],
 dict(title="DPIIT തരുന്നത്", rows=[("സ്കീമുകൾക്ക്", "യോഗ്യത"), ("ടെൻഡറുകൾക്ക്", "യോഗ്യത"), ("സെൽഫ് സർട്ടിഫിക്കേഷൻ", "ലേബർ, എൻവയോൺമെന്റ്")], total=("ഗ്രാന്റ് ഉറപ്പ്", "ഇല്ല")),
 ["DPIIT-നെ ഒരു വാതിലായി കാണുക, ഉറപ്പായിട്ടല്ല.", "ഓരോ സ്കീമിന്റെയും നിബന്ധന വായിക്കുക."],
 "യോഗ്യത ≠\nഉറപ്പ്", topics.CTA_BENEFITS, mentor="B", series="വാസുവിന്റെ കയർ മെഷീൻ", ep=6, next="KSUM", scene="office", theme="faq")
