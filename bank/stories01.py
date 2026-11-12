# Story bank 01. Stories that make people follow and reply (replies land in DMs, where the bot answers).
# kinds: tip (one useful fact + follow), quiz (question card, answer card posted 2 slots later), contact (reply-with-keyword card)
# The API cannot add poll/question/link stickers, so every story asks for a reply instead. No prices.
T = []
def tip(id, segment, title, body): T.append(dict(id=id, kind="tip", segment=segment, title=title, body=body))
def quiz(id, segment, q, a, why): T.append(dict(id=id, kind="quiz", segment=segment, q=q, a=a, why=why))
def contact(id, segment, line, kw): T.append(dict(id=id, kind="contact", segment=segment, line=line, kw=kw))

tip("t001", "salaried", "പ്രൈവറ്റ് ലിമിറ്റഡിന്\nമിനിമം മൂലധനം?", "ഇപ്പോൾ നിർബന്ധിത മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല.")
tip("t002", "solo", "ഒറ്റയ്ക്കാണോ?", "വൺ പേഴ്സൺ കമ്പനി (OPC) വഴി ഒറ്റയ്ക്കും കമ്പനി തുടങ്ങാം.")
tip("t003", "nri", "പ്രവാസികൾക്ക്", "NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം.")
tip("t004", "freelancer", "ഓഫീസ് ഇല്ലേ?", "ഉടമയുടെ NOC-യും പുതിയ ബില്ലും ഉണ്ടെങ്കിൽ വീടിന്റെ അഡ്രസ്സ് രജിസ്റ്റേർഡ് ഓഫീസ് ആക്കാം.")
tip("t005", "cofounders", "രജിസ്ട്രേഷന് ശേഷം\nആദ്യ 30 ദിവസം", "ആദ്യത്തെ ഓഡിറ്ററെ നിയമിക്കണം. മറക്കല്ലേ.")
tip("t006", "proprietor", "വരുമാനം ഇല്ലാത്ത വർഷം?", "എങ്കിലും ആനുവൽ ഫയലിംഗ് വേണം. താമസിച്ചാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ ലേറ്റ് ഫീ.")
tip("t007", "cofounders", "ഫണ്ടിംഗ് പ്ലാനുണ്ടോ?", "ഷെയർ കൊടുത്ത് ഇക്വിറ്റി ഫണ്ട് എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് വേണം. LLP-ക്ക് പറ്റില്ല.")
quiz("q001", "freelancer", "കമ്പനി രജിസ്ട്രേഷന്\nസാധാരണ എത്ര ദിവസം?\n\nA) 2 ദിവസം\nB) 7–15 പ്രവൃത്തി ദിവസം\nC) 3 മാസം", "B) 7–15 പ്രവൃത്തി ദിവസം", "ഡോക്യുമെന്റ്സും പേരും ശരിയാണെങ്കിൽ സാധാരണ ഇത്രയും സമയം.")
quiz("q002", "cofounders", "പ്രൈവറ്റ് ലിമിറ്റഡിന്\nകുറഞ്ഞത് എത്ര ഡയറക്ടർമാർ?\n\nA) 1\nB) 2\nC) 5", "B) 2", "ഒരാളെങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC.")
quiz("q003", "nri", "ഗൾഫിലുള്ള NRI-ക്ക്\nനാട്ടിൽ കമ്പനി ഡയറക്ടർ ആകാമോ?\n\nA) ആകാം\nB) ആകില്ല", "A) ആകാം", "ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാളായിരിക്കണം എന്ന് മാത്രം.")
quiz("q004", "proprietor", "\"ബിസിനസ് തുടങ്ങി\" ഡിക്ലറേഷൻ\nഎത്ര ദിവസത്തിനുള്ളിൽ?\n\nA) 30\nB) 180\nC) 365", "B) 180 ദിവസം", "മിസ്സ് ആയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ.")
contact("x001", "freelancer", "ബിസിനസിന് ഏത് സ്ട്രക്ചർ\nഎന്ന് സംശയമുണ്ടോ?", "START")
contact("x002", "freelancer", "മനസ്സിലുള്ള കമ്പനി പേര്\nഅപ്രൂവ് ആകുമോ?\nഞങ്ങൾ ചെക്ക് ചെയ്യാം.", "NAME")
contact("x003", "cofounders", "രജിസ്ട്രേഷൻ കഴിഞ്ഞോ?\nഅടുത്ത ഡെഡ്‌ലൈനുകൾ\nഅറിയണോ?", "AFTER")
contact("x004", "nri", "ഗൾഫിൽ ഇരുന്ന്\nനാട്ടിൽ ബിസിനസ്\nപ്ലാൻ ചെയ്യുന്നുണ്ടോ?", "START")
