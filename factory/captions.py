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
    # ---- GST registration (topic gst) ----
    "GST": dict(
        ml="കേരളത്തിൽ ജിഎസ്ടി രജിസ്ട്രേഷൻ എപ്പോൾ വേണം? സാധനങ്ങൾക്ക് വർഷം 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം ടേൺഓവർ കടന്നാൽ. മറ്റ് സംസ്ഥാനങ്ങളിലേക്ക് സാധനം വിൽക്കുന്നെങ്കിൽ, ഓൺലൈൻ ഓർഡർ ആണെങ്കിലും, ആദ്യ വിൽപ്പന മുതൽ.",
        en="When do you need GST registration in Kerala? Above Rs 40 lakh turnover for goods or Rs 20 lakh for services, and from the first sale if you sell goods to other states, including online orders through Amazon, Flipkart or Meesho. GST number, GSTIN, GST registration online.",
        mg="GST registration eppol venam? Goods-nu 40 lakh, service-nu 20 lakh turnover kadannaal. Other state-ilekku saadhanam vilkkunnenkil, online order aanenkilum, first sale muthal GST venam."),
    "LIMIT": dict(
        ml="ജിഎസ്ടി ലിമിറ്റ്: സാധനങ്ങൾക്ക് 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം. കോമ്പോസിഷൻ സ്കീം സാധനങ്ങൾക്ക് 1.5 കോടി വരെ, സർവീസിന് 50 ലക്ഷം വരെ. മറ്റ് സംസ്ഥാനങ്ങളിലേക്കുള്ള സാധന വിൽപ്പനയ്ക്ക് ലിമിറ്റ് ഇല്ല.",
        en="GST turnover limit in Kerala: Rs 40 lakh for goods, Rs 20 lakh for services. Composition scheme up to Rs 1.5 crore (goods) or Rs 50 lakh (services). No limit for selling goods to other states, online or offline.",
        mg="GST limit: goods 40 lakh, service 20 lakh. Composition scheme goods 1.5 crore vare, service 50 lakh vare. Other state-ilekku goods vilkkunnavarkku limit illa."),
    "PENALTY": dict(
        ml="ജിഎസ്ടി പിഴ: രജിസ്റ്റർ ചെയ്യേണ്ടപ്പോൾ ചെയ്തില്ലെങ്കിൽ ടാക്സും 18% പലിശയും, കൂടെ 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10%. റിട്ടേൺ വൈകിയാൽ ദിവസം 50, വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ വേണം.",
        en="GST penalties: not registering when required means the tax, 18% interest and a penalty of Rs 10,000 or 10% of the tax, whichever is higher. A late GSTR-3B costs Rs 50 a day, and nil returns are due even with no sales.",
        mg="GST penalty: register cheyyendappol cheythillenkil tax-um 18% interest-um, koode 10,000 allenkil tax-inte 10%. Return late aayaal divasam 50. Sales illatha maasavum nil return venam."),
    # ---- investor agreements (topic inv) ----
    "INVEST": dict(
        ml="ഇൻവെസ്റ്ററുടെ പൈസ വരും മുമ്പ്: ടേം ഷീറ്റ്, ഷെയർ സബ്സ്ക്രിപ്ഷൻ എഗ്രിമെന്റ്, ഷെയർഹോൾഡേഴ്സ് എഗ്രിമെന്റ്. ആർട്ടിക്കിൾസ് മാറ്റിയാലേ ആ അവകാശങ്ങൾ കമ്പനിയെ ബാധിക്കൂ. പൈസ കിട്ടി 60 ദിവസത്തിനുള്ളിൽ ഷെയർ അലോട്ട് ചെയ്യണം.",
        en="Investor agreement checklist for founders and investors in Kerala: term sheet, share subscription agreement, shareholders' agreement (SHA), updated articles, and share allotment within 60 days of receiving the money. Startup funding done right.",
        mg="Investor-inte paisa varum mumbu: term sheet, share subscription agreement, shareholders agreement. Articles maattiyaale aa rights company-ye bind cheyyu. Paisa kitti 60 divasathinullil share allot cheyyanam."),
    "TERMSHEET": dict(
        ml="ടേം ഷീറ്റ് ഒപ്പിട്ടാൽ എല്ലാം ഉറച്ചോ? വാല്യുവേഷനും തുകയും സാധാരണ ബൈൻഡിംഗ് അല്ല. പക്ഷേ കോൺഫിഡൻഷ്യാലിറ്റി, എക്സ്ക്ലൂസിവിറ്റി പോലുള്ള ക്ലോസുകൾ ഒപ്പിട്ട ദിവസം മുതൽ ബാധകം.",
        en="Signing a term sheet for startup funding in India? Valuation and amount are usually non-binding, but confidentiality, exclusivity (no-shop), costs and governing law bind you from the day you sign.",
        mg="Term sheet sign cheythaal ellaam urachoo? Valuation-um amount-um saadharana binding alla. Pakshe confidentiality, exclusivity pole ulla clauses sign cheytha divasam muthal binding aanu."),
    "FUNDING": dict(
        ml="ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞാൽ: എഗ്രിമെന്റുകൾ, ബോർഡ്, ഷെയർഹോൾഡർ അനുമതി, PAS-4, പ്രത്യേക ബാങ്ക് അക്കൗണ്ട്, 60 ദിവസത്തിൽ അലോട്ട്മെന്റ്, 15 ദിവസത്തിൽ PAS-3. NRI ഇൻവെസ്റ്ററാണെങ്കിൽ 30 ദിവസത്തിൽ FC-GPR.",
        en="After an investor says yes: agreements, board and shareholder approvals, PAS-4 offer letter, a separate bank account, allotment within 60 days, PAS-3 within 15 days, and FC-GPR within 30 days for NRI or foreign investors.",
        mg="Investor yes paranjaal: agreements, board-um shareholder approval-um, PAS-4, separate bank account, 60 divasathil allotment, 15 divasathil PAS-3. NRI investor aanenkil 30 divasathil FC-GPR."),
}
SEGMENT = {   # who it is for, using the phrases each group searches
    "freelancer": dict(ml="ഫ്രീലാൻസിൽ നിന്ന് സ്വന്തം കമ്പനിയിലേക്ക് മാറാൻ ആലോചിക്കുന്ന ഫ്രീലാൻസർമാർക്ക്: വലിയ ക്ലയന്റുകൾ കമ്പനി ഡീറ്റെയിൽസ് ചോദിക്കും.", en="For freelancers in Kerala moving from freelancing to a registered company, when bigger clients ask for company details.", mg="Freelancer aano? Freelancing-il ninnu swantham company register cheyyan time aayo ennu nokkaam."),
    "cofounders": dict(ml="കൂട്ടുകാരുമായി ചേർന്ന് സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്ന കോ-ഫൗണ്ടർമാർക്ക്: ഷെയറും ഫണ്ടിംഗും ആദ്യമേ ശരിയാക്കാം.", en="For co-founders starting a startup in Kerala: get shares and funding plans right from day one.", mg="Friends-umaayi chernnu startup thudangunna co-founders-nu: shares-um funding-um aadyame set aakkaam."),
    "proprietor": dict(ml="ഷോപ്പോ ചെറിയ ബിസിനസോ പ്രൊപ്രൈറ്റർഷിപ്പായി നടത്തുന്നവർക്ക്: കമ്പനി ആക്കാൻ സമയമായോ?", en="For shop owners and proprietorship businesses in Kerala thinking about converting to a company.", mg="Shop allenkil proprietorship business nadathunnavarkku: company aakkan time aayo?"),
    "salaried": dict(ml="ജോലിയോടൊപ്പം സൈഡ് ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For salaried professionals in Kerala starting a side business or planning to quit their job.", mg="Job-inte koode side business thudangunnavarkku, allenkil job vittu business plan ullavarkku."),
    "solo": dict(ml="ഒറ്റയ്ക്ക് ബിസിനസ് തുടങ്ങുന്നവർക്ക്: വൺ പേഴ്സൺ കമ്പനി (OPC) ഒരു വഴിയാണ്.", en="For solo founders: a One Person Company (OPC) lets you start a company on your own.", mg="Ottaykku business thudangunnavarkku: One Person Company (OPC) oru option aanu."),
    "nri": dict(ml="ഗൾഫിലിരുന്ന് നാട്ടിൽ കമ്പനി തുടങ്ങുന്ന NRI-കൾക്ക്: NRI-ക്കും ഡയറക്ടർ ആകാം.", en="For NRIs in the Gulf starting a company in Kerala: NRIs can be directors and shareholders.", mg="Gulf-il irunnu naattil company thudangunna NRI-kalkku: NRI-kkum director aakaam."),
    "online_seller": dict(ml="ആമസോൺ, ഫ്ലിപ്കാർട്ട്, മീഷോ, ഇൻസ്റ്റഗ്രാം വഴി വിൽക്കുന്നവർക്ക്.", en="For online sellers in Kerala on Amazon, Flipkart, Meesho and Instagram.", mg="Amazon, Flipkart, Meesho, Instagram vazhi vilkkunnavarkku."),
    "trader": dict(ml="കടകൾക്കും ഹോൾസെയിൽ, ഹോം ഫുഡ്, സ്പൈസ് ബിസിനസുകൾക്കും.", en="For shop owners, wholesalers, home-food and spice businesses in Kerala.", mg="Shop, wholesale, home food, spice business nadathunnavarkku."),
    "service_pro": dict(ml="കൺസൾട്ടന്റുകൾക്കും ഏജൻസികൾക്കും ഫ്രീലാൻസർമാർക്കും: B2B ക്ലയന്റുകൾ GSTIN ചോദിക്കും.", en="For consultants, agencies and freelancers in Kerala whose B2B clients ask for a GSTIN.", mg="Consultants, agencies, freelancers: B2B clients GSTIN chodikkum."),
    "new_company": dict(ml="പുതിയതായി രജിസ്റ്റർ ചെയ്ത കമ്പനികൾക്കും LLP-കൾക്കും.", en="For newly registered companies and LLPs in Kerala getting their first corporate clients.", mg="Puthiyathaayi register cheytha company-kalkkum LLP-kalkkum."),
    "nri_business": dict(ml="ഗൾഫിലിരുന്ന് നാട്ടിലെ ബിസിനസ് നടത്തുന്ന NRI-കൾക്ക്.", en="For NRIs in the Gulf running or starting a business in Kerala.", mg="Gulf-il irunnu naattile business nadathunna NRI-kalkku."),
    "founder_raising": dict(ml="ഫണ്ടിംഗ് എടുക്കുന്ന സ്റ്റാർട്ടപ്പ് ഫൗണ്ടർമാർക്ക്.", en="For startup founders in Kerala raising angel or seed funding.", mg="Funding edukkunna startup founders-nu."),
    "family_money": dict(ml="ബന്ധുക്കളിൽ നിന്നോ സുഹൃത്തുക്കളിൽ നിന്നോ പൈസ എടുക്കുന്നവർക്ക്: അതും നിക്ഷേപമാണ്.", en="For founders taking money from family or friends: it is still an investment that needs proper papers.", mg="Family-yil ninno friends-il ninno paisa edukkunnavarkku: athum investment aanu."),
    "nri_investor": dict(ml="നാട്ടിലെ കമ്പനിയിൽ നിക്ഷേപിക്കുന്ന ഗൾഫ് മലയാളികൾക്ക്.", en="For Gulf Malayalis and NRIs investing in a Kerala company.", mg="Naattile company-il invest cheyyunna Gulf Malayalikalkku."),
    "angel": dict(ml="ആദ്യമായി ഒരു സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കുന്നവർക്ക്: നിങ്ങളുടെ പൈസ സുരക്ഷിതമാക്കൂ.", en="For first-time angel investors: protect your money with the right agreement.", mg="Aadyamaayi startup-il invest cheyyunnavarkku: ningalude paisa safe aakkoo."),
    "cofounder_split": dict(ml="ഷെയർ എങ്ങനെ വീതിക്കണം എന്ന് ആലോചിക്കുന്ന കോ-ഫൗണ്ടർമാർക്ക്.", en="For co-founders deciding the share split before outside money arrives.", mg="Share engane veethikkanam ennu aalochikkunna co-founders-nu."),
}
CTA = dict(ml="{base} അല്ലെങ്കിൽ {kw} എന്ന് കമന്റ് ചെയ്യൂ, DM-ൽ അയച്ചുതരാം 👇",
           en="Comment {base} or {kw} and we'll send it to your DM 👇",
           mg="{base} allenkil {kw} ennu comment cheyyu, DM-il ayachu tharaam 👇")
# hashtags: 1 core + 1 local + 1 topic + 1 segment + 1 rotating (5 total, Instagram's cap)
H_LOCAL = ["#kerala", "#kochi", "#keralabusiness", "#malayali", "#startupkerala"]
H_TOPIC = {"START": ["#privatelimitedcompany", "#pvtltd", "#llp", "#opc"], "NAME": ["#companyname", "#trademark", "#businessname"],
           "AFTER": ["#compliance", "#rocfiling", "#annualfiling"], "CHECKLIST": ["#businessregistration", "#documents", "#startupindia"]}
H_TOPIC.update({"GST": ["#gstregistration", "#gstin", "#gstnumber"], "LIMIT": ["#gstlimit", "#gstindia", "#compositionscheme"], "PENALTY": ["#gstreturn", "#gstr3b", "#gstcompliance"],
                "INVEST": ["#investment", "#shareholdersagreement", "#equity"], "TERMSHEET": ["#termsheet", "#fundraising", "#venturecapital"], "FUNDING": ["#funding", "#angelinvestor", "#seedfunding"]})
H_SEG = {"freelancer": "#freelancer", "cofounders": "#startup", "proprietor": "#smallbusiness", "salaried": "#sidebusiness", "solo": "#entrepreneur", "nri": "#nri",
         "online_seller": "#onlineseller", "trader": "#smallbusiness", "service_pro": "#consultant", "new_company": "#startup", "nri_business": "#nri",
         "founder_raising": "#startupfunding", "family_money": "#familybusiness", "nri_investor": "#nriinvestment", "angel": "#angelinvesting", "cofounder_split": "#cofounder"}
CORE = {"co": "#companyregistration", "gst": "#gstregistration", "inv": "#investoragreement"}
H_EXTRA_T = {"gst": ["#gst", "#taxindia", "#keralabusiness", "#msme", "#smallbusinessindia"], "inv": ["#startupindia", "#keralastartup", "#investors", "#startuplaw", "#founders"]}
H_EXTRA = ["#mca", "#incorporation", "#startupindia", "#businessowner", "#keralastartup"]

def _pick(xs, key): return xs[zlib.crc32(key.encode()) % len(xs)]

def hashtags(item_id, base, segment, topic="co"):
    extra = H_EXTRA_T.get(topic, H_EXTRA)
    tags = [CORE.get(topic, CORE["co"]), _pick(H_LOCAL, item_id + "l"), _pick(H_TOPIC.get(base, extra), item_id + "t"), H_SEG.get(segment, "#entrepreneur")]
    tags = list(dict.fromkeys(tags))
    for x in [_pick(extra, item_id + "x")] + extra:
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
    parts.append(hashtags(s["id"], base, seg, s.get("topic") or "co"))
    out = "\n\n".join(parts)[:2200]
    assert out.count("#") <= 5, s["id"]
    return out
