# Tips and tricks 04 (28 Nov night): written as duo3d scenes, not lists (26 Nov review). theme="tip". Facts only from topics.FACTS_SUI.
# Never promise approval or a benefit; no fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

# calendar tip: three dates to note on the day recognition arrives
duo("ut012", "tech_founder", "B", "railway", "DPIIT കിട്ടിയ ദിവസം\nകലണ്ടറിൽ\n3 തീയതി എഴുതൂ", [
 ("V","wide","ഷീബേ, DPIIT സർട്ടിഫിക്കറ്റ് വന്നു! ഫ്രെയിം ചെയ്യാൻ കടയിൽ പോകുവാ."),
 ("A","A","ദിനേശേ, ഫ്രെയിമിന് മുമ്പ് ഫോണിലെ കലണ്ടർ തുറക്ക്. മൂന്ന് തീയതി ഇടണം."),
 ("A","wide","ഒന്ന്: ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷം തികയുന്ന ദിവസം, ഡീപ് ടെക്കിന് 20. അതോടെ സ്റ്റാർട്ടപ്പ് പ്രായം കഴിയും."),
 ("A","A","രണ്ട്: ടാക്സ് ഹോളിഡേ തീരുമാനിക്കാനുള്ള ദിവസം. ആദ്യ 10 വർഷത്തിലെ തുടർച്ചയായ 3 വർഷം, അതിന് വേറെ അപേക്ഷ."),
 ("A","wide","മൂന്ന്: ഓരോ വർഷവും ടേൺഓവർ നോക്കുന്ന ദിവസം. 200 കോടി കടക്കരുത്, ഡീപ് ടെക്കിന് 300."),
 ("V","V","ഫ്രെയിം ചുമരിൽ, തീയതി ഫോണിൽ.")],
 "സർട്ടിഫിക്കറ്റ് ചുമരിൽ,\nതീയതികൾ ഫോണിൽ", CTA_DPIIT, theme="tip",
 cap_ml="DPIIT കിട്ടിയ ദിവസം മൂന്ന് തീയതി കലണ്ടറിൽ ഇടുക: ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷം (ഡീപ് ടെക്കിന് 20), ടാക്സ് ഹോളിഡേ തീരുമാനിക്കാനുള്ള സമയം (ആദ്യ 10-ൽ തുടർച്ചയായ 3 വർഷം, വേറെ അപേക്ഷ), ഓരോ വർഷത്തെയും ടേൺഓവർ ചെക്ക് (200 കോടി, ഡീപ് ടെക്കിന് 300). നിങ്ങളുടെ കലണ്ടറിൽ ഇത് ഉണ്ടോ?",
 cap_en="The day DPIIT recognition arrives, put three dates in your calendar: 10 years from incorporation (20 for deep tech), the time to decide on the tax holiday (3 consecutive years within the first 10, a separate application), and a yearly turnover check (never above 200 crore, 300 for deep tech). Are these in your calendar?",
 cap_mg="DPIIT kittiya divasam moonnu theeyathi calendar-il iduka: incorporation muthal 10 varsham (deep tech-inu 20), tax holiday theerumaanikkaanulla samayam (aadya 10-il thudarchayaaya 3 varsham, vere apeksha), oro varshatheyum turnover check (200 crore, deep tech-inu 300). Ningalude calendar-il ithu undo?")

# myth-buster tip: three things recognition does not do
duo("ut013", "grant_seeker", "A", "park", "DPIIT ചെയ്യാത്ത\n3 കാര്യങ്ങൾ.\nഅറിഞ്ഞാൽ നിരാശ കുറയും", [
 ("V","wide","ഗായത്രീ, DPIIT കിട്ടി. ഇനി പണം, ടാക്സ് ഇളവ്, നിയമം ഒന്നും നോക്കേണ്ടല്ലോ?"),
 ("A","A","അനന്തൂ, മൂന്നും തെറ്റ്. ഒന്ന്: DPIIT പണം തരില്ല. സ്കീമുകൾക്കും ടെൻഡറുകൾക്കും അപേക്ഷിക്കാൻ യോഗ്യത തരും."),
 ("A","wide","രണ്ട്: ടാക്സ് ഹോളിഡേ സ്വയം വരില്ല. ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡിന് വേറെ അപേക്ഷ, പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കും മാത്രം."),
 ("A","A","മൂന്ന്: തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ സ്വയം സാക്ഷ്യപ്പെടുത്താം. പക്ഷേ നിയമം ഇല്ലാതാകുന്നില്ല."),
 ("V","V","അപ്പോ ഇത് താക്കോൽക്കൂട്ടമാ, നിധിയല്ല."),
 ("A","wide","ശരിയായ വാതിൽ തുറന്നാലേ ഗുണമുള്ളൂ.")],
 "DPIIT താക്കോലാ,\nനിധിയല്ല", CTA_BENEFITS, theme="tip",
 cap_ml="DPIIT റെക്കഗ്നിഷൻ ചെയ്യാത്ത മൂന്ന് കാര്യം: പണം തരില്ല (സ്കീമുകൾക്ക് യോഗ്യത മാത്രം), 80-IAC ടാക്സ് ഹോളിഡേ സ്വയം വരില്ല (വേറെ അപേക്ഷ, പ്രൈവറ്റ് ലിമിറ്റഡിനും LLP-ക്കും), തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങൾ ഇല്ലാതാക്കില്ല (സ്വയം സാക്ഷ്യപ്പെടുത്തൽ മാത്രം). ഇതിൽ ഏതാ നിങ്ങൾ കരുതിയിരുന്നത്?",
 cap_en="Three things DPIIT recognition does not do: it gives no money (only eligibility for schemes and tenders), it does not bring the section 80-IAC tax holiday by itself (separate application, Pvt Ltd and LLP only), and it does not remove labour and environment laws (it allows self-certification). Which one did you believe?",
 cap_mg="DPIIT recognition cheyyaatha moonnu kaaryam: panam tharilla (scheme-ukalkku yogyatha maathram), 80-IAC tax holiday swayam varilla (vere apeksha, Pvt Ltd-inum LLP-kkum), thozhil, paristhithi niyamangal illaathaakkilla (swayam saakshyappeduthal maathram). Ithil ethaa ningal karuthiyirunnathu?")

# form-filling tip: three questions before typing the DPIIT number into a scheme form
duo("ut014", "grant_seeker", "C", "akshaya", "സ്കീം ഫോമിൽ\nDPIIT നമ്പർ ഇടും മുമ്പ്\n3 ചോദ്യം", [
 ("V","wide","സുധേ, ഈ സ്കീം ഫോം DPIIT നമ്പർ ചോദിക്കുന്നു. എന്റെ കൈയിൽ ഉണ്ട്, ഇപ്പോ തന്നെ അടിക്കാം."),
 ("A","A","രമേശേ, മൂന്ന് ചോദ്യം ആദ്യം. ഒന്ന്: അപേക്ഷിക്കുന്ന സ്ഥാപനവും സർട്ടിഫിക്കറ്റിലെ സ്ഥാപനവും ഒന്നാണോ?"),
 ("A","wide","രണ്ട്: കമ്പനിക്ക് ഇപ്പോഴും 10 വർഷത്തിൽ താഴെയാണോ? ഒരു വർഷവും ടേൺഓവർ 200 കോടി കടന്നിട്ടില്ലല്ലോ?"),
 ("A","A","മൂന്ന്: DPIIT യോഗ്യത മാത്രം തരും. സെലക്ഷൻ ആ സ്കീമിന്റെ നിബന്ധന പോലെ."),
 ("V","V","അപ്പോ നമ്പർ ശരി, പക്ഷേ ചോദ്യം ആദ്യം."),
 ("A","wide","ഫോം വേഗം, ചെക്ക് അതിലും മുമ്പ്.")],
 "നമ്പർ അടിക്കും മുമ്പ്\nമൂന്ന് ചോദ്യം", CTA_DPIIT, theme="tip",
 cap_ml="സ്കീം ഫോമിൽ DPIIT നമ്പർ ഇടും മുമ്പ് മൂന്ന് ചോദ്യം: അപേക്ഷിക്കുന്ന സ്ഥാപനം തന്നെയാണോ സർട്ടിഫിക്കറ്റിൽ? കമ്പനി ഇപ്പോഴും 10 വർഷത്തിൽ താഴെയും ടേൺഓവർ ഒരു വർഷവും 200 കോടി കടക്കാതെയും ആണോ? DPIIT യോഗ്യത മാത്രം; സെലക്ഷൻ സ്കീമിന്റെ നിബന്ധന പോലെ. നിങ്ങൾ ഇപ്പോൾ ഏത് സ്കീമിനാ അപേക്ഷിക്കുന്നത്?",
 cap_en="Before typing your DPIIT number into a scheme form, ask three questions: is the applicant the same entity named on the certificate? Is the company still under 10 years old, with turnover never above 200 crore in any year? And remember recognition gives eligibility only; selection follows the scheme's own rules. Which scheme are you applying for?",
 cap_mg="Scheme form-il DPIIT number idum mumbu moonnu chodyam: apekshikkunna sthaapanam thanneyaano certificate-il? Company ippozhum 10 varshathil thaazheyum turnover oru varshavum 200 crore kadakkaatheyum aano? DPIIT yogyatha maathram; selection scheme-inte nibandhana pole. Ningal ippol ethu scheme-inaa apekshikkunnathu?")
