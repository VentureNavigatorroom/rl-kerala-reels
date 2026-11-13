# Story bank 04. New angles: two salaried spouses as both directors, a client's brand inside your company name, a rented
# home as an OPC office, auditor first at the founders' first meeting; quizzes on when the 180 days start, who can be the
# resident director, and a 30-day auditor date; contact cards for a freelance brand name, a retired solo consultant and a
# mother-owned house as office. Same kinds and rules as stories01-03 (checked facts from batch01.py only, no prices).
T = []
def tip(id, segment, title, body): T.append(dict(id=id, kind="tip", segment=segment, title=title, body=body))
def quiz(id, segment, q, a, why): T.append(dict(id=id, kind="quiz", segment=segment, q=q, a=a, why=why))
def contact(id, segment, line, kw): T.append(dict(id=id, kind="contact", segment=segment, line=line, kw=kw))

# ---------------- tips ----------------
tip("t028", "salaried", "ഭാര്യയും ഭർത്താവും\nജോലിക്കാരാണോ?", "രണ്ടുപേർക്കും ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. പ്രൈവറ്റ് ലിമിറ്റഡിന് അത്രയും മതി. ഒരാൾ ഡെഡ്‌ലൈൻ നോക്കൂ, മറ്റേയാൾ ഓർമിപ്പിക്കൂ.")
tip("t029", "freelancer", "ക്ലയന്റിന്റെ പേര്\nകമ്പനി പേരിലോ?", "ക്ലയന്റിന്റെ ബ്രാൻഡ് പേരോ ട്രേഡ്മാർക്കോ ചേർത്താൽ കമ്പനി പേര് റിജക്ട് ആകാം. സ്വന്തമായ ഒരു വാക്ക് ഉപയോഗിക്കൂ.")
tip("t030", "solo", "OPC തുടങ്ങാൻ, വീട്\nവാടകയ്ക്കാണോ?", "വീട്ടുടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ വാടക വീടും രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.")
tip("t031", "cofounders", "ഫൗണ്ടേഴ്സിന്റെ ആദ്യ\nമീറ്റിംഗിൽ ആദ്യ വിഷയം", "ആദ്യ ഓഡിറ്റർ. ഇൻകോർപ്പറേഷൻ കഴിഞ്ഞ് 30 ദിവസമേ ഉള്ളൂ. ലോഗോയുടെ നിറം അടുത്ത മീറ്റിംഗിൽ.")

# ---------------- quizzes ----------------
quiz("q016", "proprietor", "INC-20A-യുടെ 180 ദിവസം\nഎണ്ണുന്നത് എന്ന് മുതൽ?\n\nA) കടയിലെ ആദ്യ വിൽപ്പന\nB) ഇൻകോർപ്പറേഷൻ തീയതി", "B) ഇൻകോർപ്പറേഷൻ തീയതി", "വിൽപ്പന തുടങ്ങിയാലും ഇല്ലെങ്കിലും, സർട്ടിഫിക്കറ്റിലെ തീയതി മുതൽ ക്ലോക്ക് ഓടും.")
quiz("q017", "nri", "നാട്ടിലെ കമ്പനിയിൽ\nറെസിഡന്റ് ഡയറക്ടർ\nആകാൻ പറ്റുന്നത്?\n\nA) ചെന്നൈയിൽ ജോലിയുള്ള അനിയൻ\nB) ദുബായിലുള്ള കസിൻ", "A) ചെന്നൈയിലെ അനിയൻ", "ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ മതി. കേരളത്തിൽ തന്നെ ആകണമെന്നില്ല.")
quiz("q018", "salaried", "ഇൻകോർപ്പറേഷൻ മാർച്ച് 1.\nആദ്യ ഓഡിറ്ററെ വെക്കേണ്ട\nഅവസാന ദിവസം?\n\nA) മാർച്ച് 31\nB) ഏപ്രിൽ 30", "A) മാർച്ച് 31", "ഇൻകോർപ്പറേഷൻ തീയതി മുതൽ 30 ദിവസം. \"അടുത്ത മാസം എപ്പോഴെങ്കിലും\" അല്ല.")

# ---------------- contact cards ----------------
contact("x022", "freelancer", "ഫ്രീലാൻസ് ബ്രാൻഡ് പേര്\nകമ്പനി പേരാക്കാൻ\nപറ്റുമോ എന്ന് സംശയമോ?", "NAME")
contact("x023", "solo", "റിട്ടയർ ചെയ്തു,\nഒറ്റയ്ക്ക് കൺസൾട്ടൻസി\nതുടങ്ങാൻ ആലോചനയുണ്ടോ?", "START")
contact("x024", "nri", "അമ്മയുടെ പേരിലുള്ള\nനാട്ടിലെ വീട് ഓഫീസ്\nആക്കാൻ എന്തൊക്കെ വേണം?", "CHECKLIST")
