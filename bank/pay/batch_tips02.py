# pay tips 02 (27 Nov night): ESIC month-end check as a duo3d scene, from the verified esic.gov.in line in topics.FACTS_PAY. theme="tip".
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ESIC, CTA_PAYROLL = topics.CTA_ESIC, topics.CTA_PAYROLL

duo("pyt003", "ten_staff", "B", "courier", "ESI ഉള്ള സ്ഥാപനമാണോ?\nമാസാവസാനം\n3 ചെക്ക്", [
 ("A","wide","അരവിന്ദേ, ESI ഉള്ള സ്ഥാപനത്തിന് മാസാവസാനം മൂന്ന് ചെക്ക്."),
 ("A","A","ഒന്ന്: ജീവനക്കാരന്റെ പങ്ക് 0.75% മാത്രം പിടിച്ചോ? 3.25% നമ്മുടേത്."),
 ("V","V","രണ്ട്: ദിവസക്കൂലി ശരാശരി 176 രൂപ വരെ ഉള്ളവരുടെ പങ്ക് പിടിക്കരുത്. നമ്മുടെ പങ്ക് അടയ്ക്കണം."),
 ("A","A","മൂന്ന്: മാസം കഴിഞ്ഞ് 15 ദിവസത്തിനകം അടച്ചോ?"),
 ("V","wide","0.75, 3.25, 15 ദിവസം.")],
 "0.75%, 3.25%,\n15 ദിവസത്തിനകം", CTA_ESIC, theme="tip",
 cap_ml="ESI മാസാവസാന ചെക്ക്: ജീവനക്കാരന്റെ പങ്ക് 0.75%, തൊഴിലുടമയുടേത് 3.25%; ദിവസക്കൂലി ശരാശരി 176 രൂപ വരെ ഉള്ളവർ സ്വന്തം പങ്ക് അടയ്ക്കേണ്ട, തൊഴിലുടമ അടയ്ക്കണം; മാസം കഴിഞ്ഞ് 15 ദിവസത്തിനകം അടയ്ക്കുക. ഇതിൽ ഏതാണ് നിങ്ങൾ നോക്കാറുള്ളത്?",
 cap_en="ESI month-end check: employee share 0.75% of wages, employer 3.25%; employees with an average daily wage up to 176 rupees pay no employee share, but the employer pays its own; deposit within 15 days of the end of the month. Which of these do you check?",
 cap_mg="ESI maasaavasaana check: jeevanakkaarante panku 0.75%, thozhiludamayudethu 3.25%; divasakkooli sharaashari 176 rupees vare ullavar swantham panku adaykkenda, thozhiludama adaykkanam; maasam kazhinju 15 divasathinakam adaykkuka. Ithil ethaanu ningal nokkaarullathu?")
