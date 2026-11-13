"""Captions in three languages (Malayalam, English, Manglish), written for Instagram search.
Instagram reads caption words to decide what a post is about and when to show it in search, so each caption names the
topic people actually type ("company registration Kerala", "private limited company", "LLP", "OPC", "company name",
"annual filing", "documents") in all three ways Malayalis search. Hashtags: at most 5 (Instagram's limit since Dec 2025).
A script may carry its own cap_ml / cap_en / cap_mg (written by the refill task); otherwise the topic text below is used.
No prices anywhere; facts only from the checked list in bank/batch01.py."""
import zlib

TOPIC = {
    "START": dict(
        ml="ഒറ്റയ്ക്കാണോ, കൂടെ പാർട്ണർമാരുണ്ടോ, ഭാവിയിൽ ഫണ്ടിംഗ് വേണോ? ഇതനുസരിച്ചാണ് പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, OPC ഇവയിൽ ഏത് വേണമെന്ന് തീരുമാനിക്കേണ്ടത്. കേരളത്തിൽ കമ്പനി രജിസ്ട്രേഷൻ ചെയ്യും മുമ്പ് ഇത് ഉറപ്പാക്കൂ.",
        en="Planning company registration in Kerala? Private Limited, LLP or One Person Company (OPC): the right one depends on how many founders you have and whether you plan to raise funding. Only a Private Limited can take equity investment.",
        mg="Company register cheyyan plan undo? Pvt Ltd aano LLP aano OPC aano nallathu ennu ningalude situation anusarichaanu theerumanikkendathu. Funding venel Pvt Ltd thanne venam."),
    "NAME": dict(
        ml="കമ്പനി പേര് റിജക്ട് ആകാതിരിക്കാൻ: നിലവിലുള്ള കമ്പനിയുമായോ LLP-യുമായോ ട്രേഡ്മാർക്കുമായോ സാമ്യം പാടില്ല. Bank, Insurance പോലുള്ള വാക്കുകൾക്ക് പ്രത്യേക അനുമതി വേണം. 2–3 ബാക്കപ്പ് പേരുകൾ കരുതുക.",
        en="Choosing a company name for registration? Names similar to an existing company, LLP or trademark get rejected, and words like Bank or Insurance need special approval. Keep 2-3 backup names ready.",
        mg="Company name select cheyyumbol existing company, LLP allenkil trademark-umaayi match aayaal reject aakum. Bank, Insurance pole ulla words-nu special approval venam. 2-3 backup names vechekku."),
    "AFTER": dict(
        ml="രജിസ്ട്രേഷൻ കഴിഞ്ഞാലും ജോലി തീർന്നില്ല: 30 ദിവസത്തിനുള്ളിൽ ആദ്യ ഓഡിറ്റർ, 180 ദിവസത്തിനുള്ളിൽ INC-20A, എല്ലാ വർഷവും ആനുവൽ ഫയലിംഗ്. വരുമാനം ഇല്ലെങ്കിലും ഫയലിംഗ് നിർബന്ധമാണ്.",
        en="After company registration: appoint the first auditor within 30 days, file INC-20A within 180 days, and complete annual ROC filings every year, even with zero revenue.",
        mg="Company registration kazhinjaal: 30 days-il first auditor, 180 days-il INC-20A, pinne ella varshavum annual filing. Revenue illenkilum filing nirbandham aanu."),
    "CHECKLIST": dict(
        ml="കമ്പനി രജിസ്ട്രേഷന് വേണ്ട ഡോക്യുമെന്റ്സ്: ഓരോ ഡയറക്ടറുടെയും PAN, ആധാർ, അഡ്രസ്സ് പ്രൂഫ്, ഫോട്ടോ, ഓഫീസിന്റെ കറന്റ് ബിൽ, ഉടമയുടെ NOC. വീടിന്റെ അഡ്രസ്സും ഓഫീസ് ആക്കാം.",
        en="Documents for company registration in India: PAN and Aadhaar of every director, address proof, photo, a recent utility bill for the office and the owner's NOC. Your home address can be the registered office.",
        mg="Company registration-nu documents enthokke venam? Oro director-nteyum PAN, Aadhaar, address proof, photo, office current bill, owner-nte NOC. Veedinte address-um office aakkam."),
}
SEGMENT = {
    "freelancer": dict(ml="ഫ്രീലാൻസിൽ നിന്ന് സ്വന്തം കമ്പനിയിലേക്ക് മാറാൻ ആലോചിക്കുന്നവർക്ക്.", en="For freelancers ready to turn their work into a registered company.", mg="Freelancing-il ninnu swantham company-lekku maaraan plan ullavarkku."),
    "cofounders": dict(ml="കൂട്ടുകാരുമായി ചേർന്ന് സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്നവർക്ക്.", en="For co-founders starting a startup together.", mg="Friends-umaayi chernnu startup thudangunnavarkku."),
    "proprietor": dict(ml="ഷോപ്പോ ചെറിയ ബിസിനസോ നടത്തുന്നവർക്ക്.", en="For shop owners and small business owners in Kerala.", mg="Shop allenkil small business nadathunnavarkku."),
    "salaried": dict(ml="ജോലിയോടൊപ്പം സൈഡ് ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For salaried professionals starting a side business.", mg="Job-inte koode side business thudangunnavarkku."),
    "solo": dict(ml="ഒറ്റയ്ക്ക് ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For solo founders starting on their own.", mg="Ottaykku business thudangunnavarkku."),
    "nri": dict(ml="ഗൾഫിലിരുന്ന് നാട്ടിൽ ബിസിനസ് തുടങ്ങുന്ന NRI-കൾക്ക്.", en="For NRIs in the Gulf starting a business back home in Kerala.", mg="Gulf-il irunnu naattil business thudangunna NRI-kalkku."),
}
CTA = dict(ml="{base} അല്ലെങ്കിൽ {kw} എന്ന് കമന്റ് ചെയ്യൂ, DM-ൽ അയച്ചുതരാം 👇",
           en="Comment {base} or {kw} and we'll send it to your DM 👇",
           mg="{base} allenkil {kw} ennu comment cheyyu, DM-il ayachu tharaam 👇")
# hashtags: 1 core + 1 local + 1 topic + 1 segment + 1 rotating (5 total, Instagram's cap)
H_LOCAL = ["#kerala", "#kochi", "#keralabusiness", "#malayali", "#startupkerala"]
H_TOPIC = {"START": ["#privatelimitedcompany", "#pvtltd", "#llp", "#opc"], "NAME": ["#companyname", "#trademark", "#businessname"],
           "AFTER": ["#compliance", "#rocfiling", "#annualfiling"], "CHECKLIST": ["#businessregistration", "#documents", "#startupindia"]}
H_SEG = {"freelancer": "#freelancer", "cofounders": "#startup", "proprietor": "#smallbusiness", "salaried": "#sidebusiness", "solo": "#entrepreneur", "nri": "#nri"}
H_EXTRA = ["#mca", "#incorporation", "#startupindia", "#businessowner", "#keralastartup"]

def _pick(xs, key): return xs[zlib.crc32(key.encode()) % len(xs)]

def hashtags(item_id, base, segment):
    tags = ["#companyregistration", _pick(H_LOCAL, item_id + "l"), _pick(H_TOPIC.get(base, H_EXTRA), item_id + "t"), H_SEG.get(segment, "#entrepreneur")]
    for x in [_pick(H_EXTRA, item_id + "x")] + H_EXTRA:
        if x not in tags: tags.append(x); break
    return " ".join(tags[:5])

def caption(s, head):
    """s: script (needs id, segment, base, kw; optional cap_ml/cap_en/cap_mg). head: the first line people see (hook)."""
    base, kw, seg = s["base"], s["kw"], s.get("segment", "")
    t, g = TOPIC.get(base, TOPIC["START"]), SEGMENT.get(seg, {})
    parts = [head.strip()]
    for lang in ("ml", "en", "mg"):
        body = s.get("cap_" + lang) or t[lang]
        para = body + (" " + g[lang] if g and not s.get("cap_" + lang) else "")
        parts.append(para + "\n" + CTA[lang].format(base=base, kw=kw))
    parts.append(hashtags(s["id"], base, seg))
    return "\n\n".join(parts)[:2200]
