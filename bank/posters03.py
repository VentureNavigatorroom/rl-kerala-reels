# Poster bank 03. New angles: sound-alike names, fill-in deadline owners, OPC deadlines, festival holidays inside the
# 30 days, old shop names, NRI shareholding, gulf partners for shops. Single 4:5 feed images (factory/poster.py).
# No prices; only statutory penalty numbers. Facts from batch01.py only.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
P = []
def fact(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="fact", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def myth(id, segment, myth, truth, caption, cta, tag="മിഥ്യ vs സത്യം"): P.append(dict(id=id, layout="myth", segment=segment, tag=tag, myth=myth, truth=truth, caption=caption, cta=cta))
def dead(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="deadline", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def check(id, segment, tag, title, items, caption, cta): P.append(dict(id=id, layout="check", segment=segment, tag=tag, title=title, items=items, caption=caption, cta=cta))

myth("p041", "freelancer", "ഒരക്ഷരം മാറ്റിയാൽ ആരുടെ പേരും എടുക്കാം", "കേൾക്കുമ്പോൾ സാമ്യമുള്ള പേരും റിജക്ട് ആകാം. സ്വന്തമായ ഒരു വാക്ക് ചേർക്കൂ.", "സ്പെല്ലിംഗ് മാറിയാൽ പേര് മാറില്ല.", CTA_NAME)
myth("p042", "nri", "നാട്ടിലെ വീട് ഓഫീസ് ആക്കാൻ ഞാൻ നാട്ടിൽ ഉണ്ടാകണം", "വീടിന്റെ ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും മതി. നിങ്ങൾ ഗൾഫിൽ ആയാലും.", "വീട് ആരുടെ പേരിൽ എന്ന് ആദ്യം നോക്കൂ.", CTA_DOCS)
check("p043", "salaried", "ജോലിക്കാർക്ക്", "ഓഫീസിൽ ഇരുന്ന്\nഈ ആഴ്ച ചെയ്യാവുന്നത്", ["3 കമ്പനി പേരുകൾ ചെക്ക്", "രണ്ടാമത്തെ ഡയറക്ടർ ആര്?", "ആർക്ക് എത്ര ഷെയർ?", "വീട്ടുടമയുടെ NOC + പുതിയ ബിൽ"], "ലീവ് എടുക്കാതെ പകുതി ജോലി തീർക്കാം.", CTA_START)
fact("p044", "nri", "ബന്ധുവിന്റെ ബിസിനസിൽ പൈസ?", "സ്വന്തം ഷെയർ", "നാട്ടിലെ പ്രൈവറ്റ് ലിമിറ്റഡിൽ NRI-ക്ക് ഷെയർഹോൾഡർ ആകാം. പൈസ കമ്പനിയിലേക്ക്, ഷെയർ നിങ്ങളുടെ പേരിൽ.", "വിയർപ്പിന്റെ പൈസയ്ക്ക് രേഖ വേണം.", CTA_START)
check("p045", "cofounders", "ഫൗണ്ടേഴ്സ്, പേര് എഴുതൂ", "ഈ ഡെഡ്‌ലൈൻ\nആരുടെ ചുമതല?", ["ആദ്യ ഓഡിറ്റർ (30 ദിവസം): ______", "INC-20A (180 ദിവസം): ______", "ആനുവൽ ഫയലിംഗ്: ______", "കലണ്ടർ രണ്ടുപേർക്കും ഷെയർ ചെയ്തു"], "ബ്ലാങ്ക് ആയാൽ, അപകടം.", CTA_AFTER)
fact("p046", "proprietor", "പാർട്ണർ ഗൾഫിലാണോ?", "പറ്റും", "NRI-ക്കും ഡയറക്ടർ ആകാം. കടയിലുള്ള നിങ്ങൾ ഇന്ത്യയിലെ റെസിഡന്റ് ഡയറക്ടർ.", "അളിയൻ സൗദിയിലാണെങ്കിലും ടീം റെഡി.", CTA_START)
myth("p047", "solo", "OPC ആയാൽ ഡെഡ്‌ലൈനുകൾ ഒന്നും ഇല്ല", "ഒറ്റയാൾ കമ്പനിക്കും 30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A, എല്ലാ വർഷവും ഫയലിംഗ്.", "ഒറ്റയ്ക്കാണ്, ഓർമിപ്പിക്കാൻ ആരുമില്ല.", CTA_AFTER)
dead("p048", "freelancer", "ഉത്സവ അവധി വരുന്നോ?", "30 ദിവസം", "ആദ്യ ഓഡിറ്ററുടെ 30 ദിവസത്തിൽ അവധി ദിവസങ്ങളും പെടും. ഓണവും ക്രിസ്മസും ക്ലോക്ക് നിർത്തില്ല.", "സർട്ടിഫിക്കറ്റ് വന്ന ദിവസം കലണ്ടർ.", CTA_AFTER)
myth("p049", "proprietor", "കടയ്ക്ക് 40 വർഷത്തെ പഴക്കം. ആ പേര് കമ്പനിക്കും കിട്ടും", "പഴക്കം നോക്കില്ല. ആ പേരിൽ കമ്പനിയോ LLP-യോ ട്രേഡ്മാർക്കോ ഉണ്ടെങ്കിൽ റിജക്ട് ആകാം.", "പഴയ ബോർഡ്, പുതിയ ചെക്കിംഗ്.", CTA_NAME)
check("p050", "nri", "ലീവിന് മുമ്പ്", "ഗൾഫിൽ ഇരുന്ന്\nറെഡിയാക്കാവുന്നത്", ["നാട്ടിലെ ഡയറക്ടർ ആര്?", "ആർക്ക് എത്ര ഷെയർ?", "വീട്ടുടമയുടെ NOC + പുതിയ ബിൽ", "3 പേരുകൾ ചെക്ക് ചെയ്തു", "ഡെഡ്‌ലൈൻ നോക്കുന്നയാൾ"], "ലീവ് ദിവസങ്ങൾ കുടുംബത്തിന്.", CTA_DOCS)
