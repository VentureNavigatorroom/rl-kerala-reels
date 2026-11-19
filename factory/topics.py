"""The three topics the account runs, each as if it were its own account (own banks, stock, keywords, captions).
co  = company registration   (bank/*.py,      since 1 Nov 2026)
gst = GST registration       (bank/gst/*.py,  from 20 Nov 2026)
inv = investor agreements    (bank/inv/*.py,  from 20 Nov 2026; clients are founders raising money AND people investing)
The worker (worker/src/index.js TOPICS) holds the posting stages; keep the keyword lists here and there in step.
sui = Startup India (DPIIT) recognition (bank/sui/*.py, from 20 Nov 2026)
sk  = Kerala Startup Mission Unique ID / KSUM schemes (bank/sk/*.py, from 20 Nov 2026)
Ids must be unique across all topics: gst ids start with "g", inv "v", sui "u", sk "m" (e.g. gd001, vc001, uk001, mt001).

STORIES FROM REAL ENQUIRIES: bank/STORY_THEMES.md holds anonymised situations distilled from the team's CRM (no names,
companies, places, numbers or anything that could identify a person). Build scripts on those situations, always with
invented names and changed details. Never put CRM details in the repo."""

NEW7 = ["tm", "roc", "fssai", "iec", "nda", "cfa", "fp", "val"]   # added 19 Nov evening (val = company valuation, 19:14)
DIRS = {"co": "bank", "gst": "bank/gst", "inv": "bank/inv", "sui": "bank/sui", "sk": "bank/sk", "ud": "bank/ud", **{t: f"bank/{t}" for t in NEW7}}
# share of each stock target (reels, carousels, stories, posters) kept for each topic; together <= 1 keeps the
# GitHub Pages site under its 1 GB limit. Company registration posts the most reels a day, so it keeps the biggest backup.
SHARE = {"co": 0.11, **{t: 0.068 for t in ["gst", "inv", "sui", "sk", "ud"] + NEW7}}   # same as the worker's REEL_SHARE

# general keywords (the worker's KW_TOPIC). Each post also gets its own unique keyword from build.KW_POOL.
BASES = {"co": ["START", "NAME", "AFTER", "CHECKLIST"], "gst": ["GST", "LIMIT", "PENALTY"], "inv": ["INVEST", "TERMSHEET", "FUNDING"],
         "sui": ["DPIIT", "BENEFITS"], "sk": ["KSUM", "GRANT"], "ud": ["UDYAM", "MSME"],
         "tm": ["TRADEMARK", "BRAND"], "roc": ["ROC", "FILING"], "fssai": ["FSSAI", "FOOD"], "iec": ["IEC", "EXPORT"], "nda": ["NDA", "SECRET"], "cfa": ["COFOUNDER", "VESTING"], "fp": ["PROJECTION", "FORECAST"], "val": ["VALUATION", "WORTH"]}
ALL_BASES = {k for v in BASES.values() for k in v}

# CTAs: (pill text, promise). The first word of the pill is the keyword.
CTA_GST = ("GST എന്ന് കമന്റ് ചെയ്യൂ", "GST എപ്പോൾ വേണം എന്ന\nഗൈഡ് അയച്ചുതരാം")
CTA_LIMIT = ("LIMIT എന്ന് കമന്റ് ചെയ്യൂ", "ടേൺഓവർ ലിമിറ്റുകളുടെ\nലിസ്റ്റ് അയച്ചുതരാം")
CTA_PENALTY = ("PENALTY എന്ന് കമന്റ് ചെയ്യൂ", "ഒഴിവാക്കേണ്ട പിഴകളുടെ\nലിസ്റ്റ് അയച്ചുതരാം")
CTA_INVEST = ("INVEST എന്ന് കമന്റ് ചെയ്യൂ", "പൈസ വരും മുമ്പ് ഒപ്പിടേണ്ട\nഎഗ്രിമെന്റുകൾ അയച്ചുതരാം")
CTA_TERMSHEET = ("TERMSHEET എന്ന് കമന്റ് ചെയ്യൂ", "ടേം ഷീറ്റിൽ എന്ത് ബൈൻഡിംഗ്\nഎന്ന് അയച്ചുതരാം")
CTA_FUNDING = ("FUNDING എന്ന് കമന്റ് ചെയ്യൂ", "ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞാൽ\nഅടുത്ത സ്റ്റെപ്പുകൾ അയച്ചുതരാം")
CTA_DPIIT = ("DPIIT എന്ന് കമന്റ് ചെയ്യൂ", "നിങ്ങൾക്ക് കിട്ടുമോ എന്ന\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം")
CTA_BENEFITS = ("BENEFITS എന്ന് കമന്റ് ചെയ്യൂ", "റെക്കഗ്നിഷൻ കൊണ്ടുള്ള\nഗുണങ്ങൾ അയച്ചുതരാം")
CTA_KSUM = ("KSUM എന്ന് കമന്റ് ചെയ്യൂ", "യുണീക്ക് ഐഡി ഗൈഡ്\nഅയച്ചുതരാം")
CTA_GRANT = ("GRANT എന്ന് കമന്റ് ചെയ്യൂ", "ഗ്രാന്റിന് മുമ്പുള്ള\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം")
CTA_UDYAM = ("UDYAM എന്ന് കമന്റ് ചെയ്യൂ", "ഉദ്യം കൊണ്ടുള്ള\nഗുണങ്ങൾ അയച്ചുതരാം")
CTA_MSME = ("MSME എന്ന് കമന്റ് ചെയ്യൂ", "മൈക്രോയോ സ്മോളോ എന്ന്\nനോക്കാനുള്ള ലിസ്റ്റ് അയച്ചുതരാം")
_c = lambda kw, promise: (f"{kw} എന്ന് കമന്റ് ചെയ്യൂ", promise)
CTA_TRADEMARK, CTA_BRAND = _c("TRADEMARK", "ബ്രാൻഡ് സുരക്ഷിതമാക്കാനുള്ള\nഗൈഡ് അയച്ചുതരാം"), _c("BRAND", "പേര് ആരും കോപ്പി\nചെയ്യാതിരിക്കാൻ ചെക്ക്ലിസ്റ്റ്")
CTA_ROC, CTA_FILING = _c("ROC", "വർഷത്തെ ഫയലിംഗ്\nകലണ്ടർ അയച്ചുതരാം"), _c("FILING", "ബിസിനസ് ഇല്ലെങ്കിലും വേണ്ട\nഫയലിംഗുകൾ അയച്ചുതരാം")
CTA_FSSAI, CTA_FOOD = _c("FSSAI", "ഏത് FSSAI വേണം എന്ന\nഗൈഡ് അയച്ചുതരാം"), _c("FOOD", "ഫുഡ് നിയമപരമായി വിൽക്കാൻ\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം")
CTA_IEC, CTA_EXPORT = _c("IEC", "IEC ഗൈഡ്\nഅയച്ചുതരാം"), _c("EXPORT", "ആദ്യ എക്സ്പോർട്ടിന് മുമ്പുള്ള\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം")
CTA_NDA, CTA_SECRET = _c("NDA", "നല്ല NDA-യിൽ വേണ്ടത്\nഅയച്ചുതരാം"), _c("SECRET", "ഐഡിയ പങ്കുവെക്കും മുമ്പ്\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം")
CTA_COFOUNDER, CTA_VESTING = _c("COFOUNDER", "കോ-ഫൗണ്ടർ എഗ്രിമെന്റിന്റെ\nചെക്ക്ലിസ്റ്റ് അയച്ചുതരാം"), _c("VESTING", "വെസ്റ്റിംഗ് എങ്ങനെ എന്ന്\nഅയച്ചുതരാം")
CTA_PROJECTION, CTA_FORECAST = _c("PROJECTION", "ഇൻവെസ്റ്റർ നോക്കുന്നത് എന്ത്\nഎന്ന് അയച്ചുതരാം"), _c("FORECAST", "3 വർഷ ഫോർകാസ്റ്റ്\nഎങ്ങനെ എന്ന് അയച്ചുതരാം")
CTA_VALUATION, CTA_WORTH = _c("VALUATION", "എപ്പോൾ, ഏത് രീതി എന്ന\nഗൈഡ് അയച്ചുതരാം"), _c("WORTH", "കമ്പനിയുടെ മൂല്യം എങ്ങനെ\nകണക്കാക്കുന്നു എന്ന് അയച്ചുതരാം")
CTAS = {"val": [CTA_VALUATION, CTA_WORTH], "tm": [CTA_TRADEMARK, CTA_BRAND], "roc": [CTA_ROC, CTA_FILING], "fssai": [CTA_FSSAI, CTA_FOOD], "iec": [CTA_IEC, CTA_EXPORT],
        "nda": [CTA_NDA, CTA_SECRET], "cfa": [CTA_COFOUNDER, CTA_VESTING], "fp": [CTA_PROJECTION, CTA_FORECAST], "ud": [CTA_UDYAM, CTA_MSME], "gst": [CTA_GST, CTA_LIMIT, CTA_PENALTY], "inv": [CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING], "sui": [CTA_DPIIT, CTA_BENEFITS], "sk": [CTA_KSUM, CTA_GRANT]}

SEGMENTS = {
    "co": ["freelancer", "cofounders", "proprietor", "salaried", "solo", "nri"],
    # GST: who in Kerala and the Gulf actually needs it soon (researched Nov 2026)
    "gst": ["online_seller",   # Amazon / Flipkart / Meesho / Instagram sellers of goods: GST from the first sale via a marketplace
            "trader",          # shops, wholesalers, home-food and spice sellers nearing Rs 40 lakh, or selling to other states
            "service_pro",     # consultants, agencies, freelancers, clinics near Rs 20 lakh or with B2B clients asking for a GSTIN
            "new_company",     # newly registered companies / LLPs whose corporate clients want a GSTIN on invoices
            "nri_business"],   # Gulf Malayalis running or starting a business in Kerala from abroad
    # Investor agreements: both sides of the table
    "inv": ["founder_raising", # startup founders raising angel / seed money
            "family_money",    # money from friends, family, a relative in the Gulf: still needs papers
            "nri_investor",    # Gulf Malayalis investing in Kerala companies (FEMA reporting)
            "angel",           # doctors, business owners, first-time angel investors protecting their money
            "cofounder_split"],# co-founders splitting shares before outside money arrives
    # Startup India (DPIIT): registered startups that want credibility, schemes, tenders, tax holiday
    "sui": ["tech_founder",    # app / SaaS / product founders with a Pvt Ltd or LLP
            "grant_seeker",    # founders chasing government grants and schemes (KSUM, seed fund)
            "traditional_innovator",  # food, agri, ayurveda, manufacturing businesses with a new process or product
            "student_founder", # college / young founders with a prototype
            "investor_ready"], # founders preparing to raise who want recognition first
    # Kerala Startup Mission
    "sk": ["idea_stage",       # idea / prototype founders wanting the idea grant and incubation
           "kerala_registered",# Pvt Ltd / LLP in Kerala that never applied for the Unique ID
           "returnee",         # Gulf returnees and NRIs starting a startup in Kerala
           "campus",           # students, IEDC / college incubator founders
           "women_founder"],   # women-led startups
    # Udyam / MSME: small manufacturers and service businesses chasing payments, loans and tenders
    "ud": ["manufacturer",     # small units: food processing, furniture, garments, printing, coir, rubber products
           "service_unit",     # service businesses selling to companies: IT, agencies, repair, transport, catering
           "trader_ud",        # shops / wholesalers (Udyam only for priority lending)
           "loan_seeker",      # owners applying for a business loan
           "supplier_unpaid"], # suppliers whose big buyers pay late
    "tm": ["d2c_brand", "food_brand", "salon_clinic", "app_founder", "copied_brand"],
    "roc": ["dormant_company", "new_company_roc", "late_filer", "llp_owner", "nri_director"],
    "fssai": ["home_baker", "cloud_kitchen", "spice_exporter", "cafe_owner", "packaged_food"],
    "iec": ["first_exporter", "importer", "spice_trade", "handicraft_export", "service_export"],
    "nda": ["founder_pitching", "agency_client", "freelancer_nda", "vendor_supplier", "employee_nda"],
    "cfa": ["friends_cofounders", "tech_nontech", "family_cofounders", "late_joiner", "remote_cofounder"],
    "val": ["raising_round", "esop_plan", "partner_exit", "nri_share_issue", "share_transfer"],
    "fp": ["investor_pitch", "bank_loan", "grant_application", "early_revenue", "pre_revenue"],
}

# Facts the scripts may use (checked Nov 2026; sources in the INSIGHTS notes). Nothing else, and never a service price.
FACTS_GST = """
- Kerala: GST registration needed when aggregate turnover crosses Rs 40 lakh a year (goods) or Rs 20 lakh (services)
- compulsory regardless of turnover: inter-state supply of goods (online orders from other states too); casual taxable
  persons. Selling goods on Amazon / Flipkart / Meesho also needs GST from the first sale, EXCEPT (since 1 Oct 2023,
  notification 34/2023) a seller below the limit who sells only within Kerala may use a PAN-based enrolment number if
  the marketplace supports it. Never say "every online seller needs GST". Inter-state SERVICES stay exempt up to Rs 20 lakh
- anyone may register voluntarily (B2B clients often ask for a GSTIN; input tax credit only for registered persons)
- composition scheme: up to Rs 1.5 crore turnover for goods, Rs 50 lakh for services
- approval: since 1 Nov 2025 low-risk applicants are auto-approved within 3 working days; otherwise 7 working days,
  up to 30 days if physical verification is needed
- proprietor documents: PAN, Aadhaar (OTP to its linked mobile), photo, business address proof (own: bill / tax receipt;
  rented: rent agreement + owner's NOC + bill), bank proof (cancelled cheque / passbook / statement)
- not registering when required: pay the tax, 18% interest, and a penalty of Rs 10,000 or 10% of the tax due, whichever higher
- GSTR-3B late fee: Rs 50 a day, Rs 20 a day for a nil return (capped at Rs 500 for nil, Rs 2,000 for turnover up to Rs 1.5 crore)
- returns are due even in months with no sales (nil returns)
"""
FACTS_INV = """
- only a private limited company can take equity investment (LLP / partnership / proprietorship cannot issue shares)
- term sheet: mostly non-binding; confidentiality, exclusivity (no-shop), costs and governing law usually bind from signing
- documents: term sheet -> share subscription agreement (SSA) -> shareholders' agreement (SHA)
- SHA rights (share transfer limits, right of first refusal, tag-along, drag-along, board seat, anti-dilution, founder
  vesting) bind the company only if written into the Articles of Association: amend the AoA
- private placement: special resolution, offer letter PAS-4, money only from the investor's own bank account into a
  separate bank account; allot within 60 days of receiving the money or refund within the next 15 days (else 12% interest);
  file PAS-3 within 15 days of allotment; the money cannot be used until PAS-3 is filed
- angel tax abolished for all investors from FY 2024-25
- NRI / foreign investor on repatriation basis: price not below fair value (valuation report), report FC-GPR to RBI within
  30 days of allotment; NRI investment on non-repatriation basis is treated as domestic (no FC-GPR)
- money from friends and family is still an investment: shares, agreement and filings are needed the same way
"""

FACTS_SUI = """
- DPIIT recognition (Startup India): private limited company, LLP, registered partnership or cooperative society;
  under 10 years since incorporation/registration (20 for Deep Tech); turnover never above Rs 200 crore in any year
  (Rs 300 crore Deep Tech) since the 4 Feb 2026 notification (was Rs 100 crore); working on innovation / improvement of
  products or services, or a scalable business model. A proprietorship cannot be recognised
- recognition opens: 80% rebate on patent filing fees, 50% on trademark fees, faster IP examination, self-certification
  under labour and environment laws, eligibility for many central and state schemes and tenders
- section 80-IAC tax holiday (100% of profits for 3 consecutive years out of the first 10; Pvt Ltd / LLP) is a SEPARATE
  application approved by the Inter-Ministerial Board: never say recognition gives it automatically
- never promise approval or a benefit
"""
FACTS_SK = """
- KSUM Unique ID: Kerala Startup Mission's identity for startups; KSUM schemes, grants, incubation and programmes are for
  startups that hold it; apply on KSUM's startup portal
- startup should be registered in Kerala; most KSUM grants and the seed fund also ask for DPIIT recognition and a
  private limited company or LLP with 'Active' status at MCA
- idea grant: you may apply before incorporating, but the company and the Unique ID are needed before money is released
- never state grant amounts or promise selection (amounts and calls change; the team checks the live call)
"""

FACTS_UD = """
- Udyam registration = the government's MSME registration (since 1 July 2020): online, Aadhaar-based, PAN (and GSTIN
  where the business has one), self-declaration; no renewal, but keep details updated. Never mention any fee
- classification since 1 Apr 2025, BOTH limits must be met: micro = investment up to Rs 2.5 crore and turnover up to
  Rs 10 crore; small = Rs 25 crore and Rs 100 crore; medium = Rs 125 crore and Rs 500 crore (crossing either moves you up)
- manufacturing and service micro / small units: buyers must pay within 15 days, or the agreed time up to 45 days; after
  that they owe compound interest at 3x the RBI bank rate; complaints go to the MSME Samadhaan portal / facilitation
  council; a buyer paying late loses the income-tax deduction until payment (section 43B(h))
- retail and wholesale traders can register (since July 2021) but only for priority sector lending: NO 45-day protection
- registration helps with priority sector lending, collateral-free loan schemes (CGTMSE) and preferences in government
  tenders. Never promise a loan, subsidy or recovery
"""

# Facts for the seven topics added 19 Nov evening. The worker's NEWT holds the same facts for the DM bot.
FACTS_TM = """trademark: filed with the Trade Marks Registry; TM symbol after filing, R symbol only after registration; 45 classes,
file in the classes you trade in; objection reply within 30 days; opposition within 4 months of journal publication;
valid 10 years, renewable; a company name approval does NOT protect a brand. Never promise registration or mention fees."""
FACTS_ROC = """ROC (Pvt Ltd): AGM by 30 September; AOC-4 within 30 days of AGM; MGT-7/7A within 60 days of AGM; DIR-3 KYC for every
director by 30 September; late fee Rs 100 per day per form, no cap; INC-20A within 180 days of incorporation; first
auditor within 30 days; 3 years of non-filing can disqualify directors for 5 years and the company can be struck off;
LLP: Form 11 by 30 May, Form 8 by 30 October; due even with zero business."""
FACTS_FSSAI = """FSSAI: basic registration up to Rs 12 lakh turnover a year (home bakers too); state licence up to Rs 20 crore; central
licence above that and for importers; 14-digit FSSAI number printed on packaged food; selling without it: penalty up to
Rs 5 lakh and up to 6 months' imprisonment; valid 1-5 years, renew before expiry; delivery apps ask for the number."""
FACTS_IEC = """IEC: 10-digit Import Export Code from DGFT linked to the business PAN; needed to import or export goods (customs and
banks ask); one per PAN; never expires but must be updated online every year between April and June or it is
deactivated; not needed for personal-use imports; service exporters need it to claim export benefits."""
FACTS_NDA = """NDA: enforceable contract in India if properly drafted and stamped per the state's stamp law; one-way or mutual;
define confidential information, exclusions (already public, independently developed), duration and remedies such as
an injunction; cannot protect what is already public; many investors don't sign NDAs at pitch stage."""
FACTS_CFA = """co-founder agreement: equity split, vesting (a common practice is 4 years with a 1-year cliff), roles and decisions,
all IP assigned to the company, leaver/buy-back of unvested shares, dispute resolution; post-exit non-compete is
generally not enforceable in India but confidentiality and non-solicit can be; mirror the share rights in the SHA and
articles. Never decide the split."""
FACTS_FP = """financial projections: investors, banks and grant panels ask for them; 3 years, month by month for year 1; revenue
drivers (customers, price, growth), costs and hiring, P&L, cash flow, break-even, written assumptions; realistic and
tied to traction (inflated numbers lose trust); banks may ask for a project report for loans. NEVER mention our fee."""
FACTS_VAL = """company valuation: needed when raising investment, issuing ESOPs, transferring shares, a founder/partner exits,
buy-backs, mergers, and for NRI/foreign investment (shares not below fair value by an accepted method, certified by a CA,
SEBI-registered merchant banker or cost accountant); preferential allotment of shares needs a registered valuer's report;
methods: discounted cash flow, comparable companies/deals, net asset value; early startups lean on comparables and
projections; a valuation is for a specific purpose and date. NEVER state a value or our fee."""
