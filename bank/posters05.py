# Poster bank 05. New angles: a supplier who wants shares in a proprietorship, the "2 days before the client deadline" myth,
# an OPC founder's 100-day INC-20A delay, a fill-in role chart for co-founders, NRIs not needing to send lakhs, an old bill
# for a rented flat, day 179 for a shop that became a company, three phone reminders for an OPC, a Gulf husband + home wife
# team is enough, an Instagram handle is not a company name.
# Single 4:5 feed images (factory/poster.py). No prices; only statutory penalty numbers. Facts from batch01.py only.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
P = []
def fact(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="fact", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def myth(id, segment, myth, truth, caption, cta, tag="മിഥ്യ vs സത്യം"): P.append(dict(id=id, layout="myth", segment=segment, tag=tag, myth=myth, truth=truth, caption=caption, cta=cta))
def dead(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="deadline", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def check(id, segment, tag, title, items, caption, cta): P.append(dict(id=id, layout="check", segment=segment, tag=tag, title=title, items=items, caption=caption, cta=cta))

fact("p061", "proprietor", "സപ്ലയർ ഷെയർ ചോദിച്ചോ?", "ഷെയർ = Pvt Ltd", "പ്രൊപ്രൈറ്റർഷിപ്പ് കടയ്ക്ക് ഷെയർ കൊടുക്കാൻ പറ്റില്ല. പൈസ ഇറക്കുന്നയാൾക്ക് ഷെയർ വേണമെങ്കിൽ പ്രൈവറ്റ് ലിമിറ്റഡ്.", "പൈസ വരുന്നതിന് മുമ്പ് സ്ട്രക്ചർ ശരിയാക്കൂ.", CTA_START)
myth("p062", "freelancer", "ക്ലയന്റ് ഡെഡ്‌ലൈൻ അടുത്താൽ 2 ദിവസം കൊണ്ട് കമ്പനി റെഡിയാക്കാം", "ഡോക്യുമെന്റ്സ് ശരിയാണെങ്കിലും സാധാരണ 7–15 പ്രവൃത്തി ദിവസം. ക്ലയന്റ് ചോദിക്കും മുമ്പ് തുടങ്ങൂ.", "അവസാന നിമിഷത്തെ ഓട്ടം ഒഴിവാക്കാം.", CTA_DOCS)
dead("p063", "solo", "OPC, INC-20A 100 ദിവസം വൈകി", "100 ദിവസം", "കമ്പനിക്ക് 50,000 രൂപ. ഡയറക്ടറായ നിങ്ങൾക്ക് ദിവസം 1,000 രൂപ, ഇവിടെ 1 ലക്ഷം വരെ.", "ഒറ്റയാൾ കമ്പനിയിൽ പിഴയും ഒറ്റയ്ക്ക് താങ്ങണം.", CTA_AFTER)
check("p064", "cofounders", "ഫയൽ ചെയ്യും മുമ്പ്", "റോൾ ചാർട്ട്:\nപേര് എഴുതൂ", ["ഡയറക്ടർ 1: ______", "ഡയറക്ടർ 2: ______ (ഇന്ത്യയിൽ താമസം)", "ഷെയർഹോൾഡർ 1, 2: ______", "ഓഫീസ് ഉടമ, NOC ഒപ്പിടാൻ: ______"], "ഒഴിഞ്ഞ കോളം ഇല്ലെങ്കിൽ ഫയൽ ചെയ്യാം.", CTA_START)
fact("p065", "nri", "ലക്ഷങ്ങൾ അയക്കണോ?", "വേണ്ട", "നാട്ടിലെ പ്രൈവറ്റ് ലിമിറ്റഡിന് നിർബന്ധിത മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ ഇല്ല. പൈസ ആവശ്യത്തിന് മാത്രം.", "ആദ്യം കമ്പനി, പിന്നെ പ്ലാൻ അനുസരിച്ച് പൈസ.", CTA_START)
myth("p066", "salaried", "വാടക ഫ്ലാറ്റിന്റെ പഴയ കറന്റ് ബിൽ ഓഫീസ് അഡ്രസ്സിന് മതി", "പുതിയ യൂട്ടിലിറ്റി ബിൽ വേണം. കൂടെ ഫ്ലാറ്റ് ഉടമയുടെ NOC.", "ബിൽ പഴയതായാൽ അപേക്ഷ വൈകും.", CTA_DOCS)
dead("p067", "proprietor", "കട കമ്പനി ആയിട്ട്", "ദിവസം 179", "നാളെ INC-20A-യുടെ 180 ദിവസം തികയും. ഇന്ന് തീർത്താൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ ഒഴിവാക്കാം.", "നിങ്ങളുടെ കമ്പനി ഇന്ന് എത്രാം ദിവസത്തിലാണ്?", CTA_AFTER)
check("p068", "solo", "OPC ഫൗണ്ടർ, ഫോൺ എടുക്കൂ", "ഇന്ന് തന്നെ\n3 റിമൈൻഡർ", ["ദിവസം 20: ആദ്യ ഓഡിറ്റർ ഉറപ്പിച്ചോ?", "ദിവസം 170: INC-20A റെഡിയാണോ?", "എല്ലാ വർഷവും: ആനുവൽ ഫയലിംഗ്, വരുമാനം ഇല്ലെങ്കിലും"], "ഓർമിപ്പിക്കാൻ ആരുമില്ലെങ്കിൽ ഫോൺ ഓർമിപ്പിക്കും.", CTA_AFTER)
myth("p069", "nri", "ഭർത്താവ് ഗൾഫിൽ, ഭാര്യ നാട്ടിൽ. കമ്പനി തുടങ്ങാൻ ഇത്രയും പോരാ", "മതി. രണ്ടുപേർക്കും ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം. നാട്ടിലുള്ള ഭാര്യ റെസിഡന്റ് ഡയറക്ടർ.", "രണ്ടുപേർ, രണ്ട് രാജ്യം, ഒരു കമ്പനി.", CTA_START)
fact("p070", "freelancer", "ഇൻസ്റ്റ ഹാൻഡിൽ കിട്ടി", "പേര് കിട്ടിയോ?", "ഹാൻഡിൽ കിട്ടിയാൽ കമ്പനി പേര് കിട്ടണമെന്നില്ല. സമാന കമ്പനിയോ ട്രേഡ്മാർക്കോ ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം.", "ഹാൻഡിലിന് മുമ്പ് പേര് ചെക്ക് ചെയ്യൂ.", CTA_NAME)
