"""The three topics the account runs, each as if it were its own account (own banks, stock, keywords, captions).
co  = company registration   (bank/*.py,      since 1 Nov 2026)
gst = GST registration       (bank/gst/*.py,  from 20 Nov 2026)
inv = investor agreements    (bank/inv/*.py,  from 20 Nov 2026; clients are founders raising money AND people investing)
The worker (worker/src/index.js TOPICS) holds the posting stages; keep the keyword lists here and there in step.
Ids must be unique across all topics: gst ids start with "g", inv ids with "v" (e.g. gd001, gc001, gk001, gp001, gt001)."""

DIRS = {"co": "bank", "gst": "bank/gst", "inv": "bank/inv"}
# share of each stock target (reels, carousels, stories, posters) kept for each topic; together <= 1 keeps the
# GitHub Pages site under its 1 GB limit. Company registration posts the most reels a day, so it keeps the biggest backup.
SHARE = {"co": 0.5, "gst": 0.25, "inv": 0.25}

# general keywords (the worker's KW_TOPIC). Each post also gets its own unique keyword from build.KW_POOL.
BASES = {"co": ["START", "NAME", "AFTER", "CHECKLIST"], "gst": ["GST", "LIMIT", "PENALTY"], "inv": ["INVEST", "TERMSHEET", "FUNDING"]}
ALL_BASES = {k for v in BASES.values() for k in v}

# CTAs: (pill text, promise). The first word of the pill is the keyword.
CTA_GST = ("GST എന്ന് കമന്റ് ചെയ്യൂ", "GST എപ്പോൾ വേണം എന്ന\nഗൈഡ് അയച്ചുതരാം")
CTA_LIMIT = ("LIMIT എന്ന് കമന്റ് ചെയ്യൂ", "ടേൺഓവർ ലിമിറ്റുകളുടെ\nലിസ്റ്റ് അയച്ചുതരാം")
CTA_PENALTY = ("PENALTY എന്ന് കമന്റ് ചെയ്യൂ", "ഒഴിവാക്കേണ്ട പിഴകളുടെ\nലിസ്റ്റ് അയച്ചുതരാം")
CTA_INVEST = ("INVEST എന്ന് കമന്റ് ചെയ്യൂ", "പൈസ വരും മുമ്പ് ഒപ്പിടേണ്ട\nഎഗ്രിമെന്റുകൾ അയച്ചുതരാം")
CTA_TERMSHEET = ("TERMSHEET എന്ന് കമന്റ് ചെയ്യൂ", "ടേം ഷീറ്റിൽ എന്ത് ബൈൻഡിംഗ്\nഎന്ന് അയച്ചുതരാം")
CTA_FUNDING = ("FUNDING എന്ന് കമന്റ് ചെയ്യൂ", "ഇൻവെസ്റ്റർ യെസ് പറഞ്ഞാൽ\nഅടുത്ത സ്റ്റെപ്പുകൾ അയച്ചുതരാം")
CTAS = {"gst": [CTA_GST, CTA_LIMIT, CTA_PENALTY], "inv": [CTA_INVEST, CTA_TERMSHEET, CTA_FUNDING]}

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
