# Poster bank 04. New angles: a December start date worked through to June, a pre-investor-call check, "resident" means India
# not Kerala, a Christmas-order checklist, owners giving NOC to themselves, NRIs as shareholders only, machinery is not
# capital, director duties before any revenue, three name options, NRI directors and the officer penalty.
# Single 4:5 feed images (factory/poster.py). No prices; only statutory penalty numbers. Facts from batch01.py only.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
P = []
def fact(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="fact", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def myth(id, segment, myth, truth, caption, cta, tag="മിഥ്യ vs സത്യം"): P.append(dict(id=id, layout="myth", segment=segment, tag=tag, myth=myth, truth=truth, caption=caption, cta=cta))
def dead(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="deadline", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def check(id, segment, tag, title, items, caption, cta): P.append(dict(id=id, layout="check", segment=segment, tag=tag, title=title, items=items, caption=caption, cta=cta))

dead("p051", "freelancer", "ഡിസംബർ 10-ന് കമ്പനി ആയാൽ", "ജൂൺ 8", "INC-20A-യുടെ 180 ദിവസം അന്ന് തീരും. ആദ്യ ഓഡിറ്ററുടെ 30 ദിവസം ജനുവരി 9-ന്.", "നിങ്ങളുടെ തീയതി വെച്ച് ഇതുപോലെ എണ്ണിനോക്കൂ.", CTA_AFTER)
check("p052", "cofounders", "ഇൻവെസ്റ്റർ കോളിന് മുമ്പ്", "ഫൗണ്ടേഴ്സ്,\nഈ 4 എണ്ണം ടിക്ക് ആണോ?", ["കമ്പനി പ്രൈവറ്റ് ലിമിറ്റഡ് ആണ്, LLP അല്ല", "2 ഡയറക്ടർ, ഒരാൾ ഇന്ത്യയിൽ താമസം", "പേര് ട്രേഡ്മാർക്കുമായി ക്ലാഷ് ഇല്ല", "INC-20A 180 ദിവസത്തിനുള്ളിൽ ഫയൽ ചെയ്തു"], "പിച്ച് ഡെക്കിനേക്കാൾ മുമ്പ് ചോദിക്കുന്നത് ഇതാകാം.", CTA_START)
myth("p053", "salaried", "റെസിഡന്റ് ഡയറക്ടർ കേരളത്തിൽ തന്നെ താമസിക്കണം", "ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ മതി. ബാംഗ്ലൂരിലോ ചെന്നൈയിലോ ജോലി ചെയ്യുന്നവർക്കും ആകാം.", "റെസിഡന്റ് = ഇന്ത്യ. സംസ്ഥാനമല്ല.", CTA_START)
check("p054", "proprietor", "ക്രിസ്മസ് ഓർഡറിന് മുമ്പ്", "വലിയ ഓർഡർ\nകമ്പനി ചോദിച്ചാൽ", ["3 പേരുകൾ ചെക്ക് ചെയ്തു", "ഒറ്റയ്ക്കോ? OPC. കൂടെ ആളോ? Pvt Ltd", "ഓഫീസിന് NOC + പുതിയ ബിൽ", "15 പ്രവൃത്തി ദിവസം പിന്നോട്ട് എണ്ണി"], "ഓർഡർ വന്നിട്ടല്ല, വരും മുമ്പ്.", CTA_DOCS)
fact("p055", "solo", "വീട് നിങ്ങളുടെ പേരിലാണോ?", "സ്വന്തം NOC", "ഉടമ നിങ്ങളാണെങ്കിൽ NOC ഒപ്പിടുന്നതും നിങ്ങൾ. കൂടെ പുതിയ ഒരു യൂട്ടിലിറ്റി ബിൽ.", "സ്വന്തം വീടാണെങ്കിലും രേഖ വേണം.", CTA_DOCS)
fact("p056", "nri", "ഡയറക്ടർ ആകാൻ മടിയോ?", "ഷെയർ മാത്രം", "NRI-ക്ക് ഷെയർഹോൾഡർ മാത്രമായും നിൽക്കാം. കമ്പനിക്ക് 2 ഡയറക്ടർ വേണം, ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ.", "ഉടമസ്ഥതയിൽ പങ്ക്, നടത്തിപ്പ് നാട്ടിൽ.", CTA_START)
myth("p057", "proprietor", "കമ്പനി ആക്കും മുമ്പ് വലിയ മെഷീനും സ്റ്റോക്കും വാങ്ങണം", "മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല. ഇപ്പോഴുള്ള സൗകര്യം കൊണ്ട് തുടങ്ങാം.", "മെഷീൻ വളർച്ചയ്ക്ക്. കമ്പനി തുടക്കത്തിന്.", CTA_START)
myth("p058", "salaried", "വരുമാനം വരും വരെ ഡയറക്ടർക്ക് ഒരു ജോലിയുമില്ല", "30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A, എല്ലാ വർഷവും ഫയലിംഗ്. വരുമാനം ഇല്ലെങ്കിലും.", "ജോലിക്കൊപ്പം ഈ മൂന്നും ഓർക്കൂ.", CTA_AFTER)
fact("p059", "freelancer", "പേര് കൊടുക്കും മുമ്പ്", "3 പേര്", "ഒന്ന് മാത്രം കൊടുക്കരുത്. സാമ്യം, ട്രേഡ്മാർക്ക്, Bank പോലുള്ള വാക്കുകൾ ചെക്ക് ചെയ്ത 3 പേരുകൾ.", "ഒന്ന് പോയാൽ അടുത്തത് റെഡി.", CTA_NAME)
dead("p060", "nri", "ഡയറക്ടർ ഗൾഫിലാണെങ്കിലും", "1,000 രൂപ / ദിവസം", "INC-20A വൈകിയാൽ വീഴ്ച വരുത്തിയ ഓരോ ഓഫീസർക്കും, പരമാവധി 1 ലക്ഷം. ദൂരം പിഴ കുറയ്ക്കില്ല.", "നാട്ടിലെ കമ്പനി, നിങ്ങളുടെയും ഉത്തരവാദിത്തം.", CTA_AFTER)
