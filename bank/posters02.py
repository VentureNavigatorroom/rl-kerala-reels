# Poster bank 02. New angles only: penalty totals, the 180-day clock start, myth framings not used in posters01.
# Single 4:5 feed images (factory/poster.py). No prices; only statutory penalty numbers. Facts from batch01.py only.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
P = []
def fact(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="fact", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def myth(id, segment, myth, truth, caption, cta, tag="മിഥ്യ vs സത്യം"): P.append(dict(id=id, layout="myth", segment=segment, tag=tag, myth=myth, truth=truth, caption=caption, cta=cta))
def dead(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="deadline", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def check(id, segment, tag, title, items, caption, cta): P.append(dict(id=id, layout="check", segment=segment, tag=tag, title=title, items=items, caption=caption, cta=cta))

dead("p031", "cofounders", "2 ഡയറക്ടർമാർ, 100 ദിവസം വൈകി", "2,50,000 രൂപ", "INC-20A: കമ്പനിക്ക് 50,000 + ഓരോ ഡയറക്ടർക്കും പരമാവധി 1 ലക്ഷം.", "ഒരു ഫോം മറന്നാൽ ഇത്രയും.", CTA_AFTER)
dead("p032", "freelancer", "ക്ലോക്ക് തുടങ്ങുന്നത്", "ദിവസം 1", "180 ദിവസം എണ്ണുന്നത് ഇൻകോർപ്പറേഷൻ ദിവസം മുതൽ. ആദ്യ ക്ലയന്റ് വന്ന ദിവസം മുതലല്ല.", "INC-20A തീയതി ഇന്നുതന്നെ കലണ്ടറിൽ.", CTA_AFTER)
myth("p033", "salaried", "കമ്പനി രജിസ്ട്രേഷന് മാസങ്ങൾ എടുക്കും", "ഡോക്യുമെന്റ്സ് ശരിയാണെങ്കിൽ പ്രൈവറ്റ് ലിമിറ്റഡിന് സാധാരണ 7–15 പ്രവൃത്തി ദിവസം.", "നോട്ടീസ് പീരിയഡിൽ തന്നെ തുടങ്ങാം.", CTA_START)
myth("p034", "nri", "ഗൾഫിലുള്ള 2 പേർ ഡയറക്ടർമാരായാൽ കമ്പനി റെഡി", "കുറഞ്ഞത് ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ വേണം. നാട്ടിലുള്ള ഒരാളെ ചേർക്കൂ.", "പ്രവാസി ടീമിന് ഒരു നാട്ടുകാരൻ.", CTA_START)
check("p035", "proprietor", "കട ഉടമകൾക്ക്", "കട കമ്പനി ആക്കും\nമുമ്പ് 4 തീരുമാനം", ["ആരൊക്കെ 2 ഡയറക്ടർമാർ?", "ആർക്ക് എത്ര ഷെയർ?", "ഓഫീസ്: വീടോ കടയോ?", "പേരും 2 ബാക്കപ്പും"], "വീട്ടിൽ ഇരുന്ന് ആദ്യം സംസാരിക്കൂ.", CTA_START)
check("p036", "solo", "ഒറ്റയ്ക്കാണോ?", "OPC തുടങ്ങാൻ\nറെഡിയാണോ?", ["ബിസിനസ് ഞാൻ ഒറ്റയ്ക്ക്", "ഓഫീസിന് NOC + പുതിയ ബിൽ", "2–3 പേരുകൾ ചെക്ക് ചെയ്തു", "30, 180 ദിവസം കലണ്ടറിൽ"], "നാലും ടിക് ആയാൽ തുടങ്ങാം.", CTA_DOCS)
fact("p037", "cofounders", "ടീം ചെറുതാണോ?", "2 പേർ മതി", "അതേ രണ്ടുപേർക്ക് ഡയറക്ടർമാരും ഷെയർഹോൾഡർമാരും ആകാം. പ്രൈവറ്റ് ലിമിറ്റഡിന് അത്രയും മതി.", "നാലുപേരെ തേടി നടക്കേണ്ട.", CTA_START)
myth("p038", "proprietor", "കമ്പനി ആക്കാൻ ലക്ഷങ്ങൾ ബാങ്കിൽ കാണിക്കണം", "പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല.", "കടയുടെ വളർച്ച കാത്തുനിൽക്കേണ്ട.", CTA_START)
check("p039", "nri", "പ്രവാസികൾക്ക്", "റെസിഡന്റ് ഡയറക്ടർ\nആകേണ്ടയാൾ", ["ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ", "പൂർണ്ണ വിശ്വാസമുള്ളയാൾ", "ഡെഡ്‌ലൈനുകൾ നോക്കുന്നയാൾ", "വിളിച്ചാൽ ഫോൺ എടുക്കുന്നയാൾ"], "സ്നേഹം മാത്രം നോക്കി തിരഞ്ഞെടുക്കരുത്.", CTA_START)
dead("p040", "salaried", "ആനുവൽ ഫയലിംഗ് വൈകിയാൽ", "6,000 രൂപ", "2 ഫോമുകൾ 30 ദിവസം വൈകിയാൽ: 100 രൂപ × 2 ഫോം × 30 ദിവസം.", "ഓരോ ദിവസവും ഓരോ ഫോമിനും.", CTA_AFTER)
