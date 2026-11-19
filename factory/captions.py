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
    # ---- seven topics added 19 Nov evening ----
    "VALUATION": dict(ml="ഫണ്ടിംഗ്, ESOP, ഷെയർ ട്രാൻസ്ഫർ, പാർട്ണർ എക്സിറ്റ്, NRI നിക്ഷേപം: കമ്പനി വാല്യുവേഷൻ വേണ്ട സമയങ്ങൾ.", en="Company valuation in Kerala for fundraising, ESOPs, share transfers, a partner's exit or NRI investment: methods, who signs and when you need it.", mg="Funding, ESOP, share transfer, partner exit, NRI investment: company valuation venda samayangal."),
    "WORTH": dict(ml="കമ്പനിയുടെ മൂല്യം: ഭാവി ക്യാഷ് ഫ്ലോ, സമാന കമ്പനികൾ, ആസ്തി മൂല്യം.", en="How a company's worth is worked out: discounted cash flow, comparable companies and net asset value.", mg="Company-yude moolyam: future cash flow, samaana companies, asset value."),
    "TRADEMARK": dict(ml="ട്രേഡ്മാർക്ക് ഫയൽ ചെയ്താൽ TM ഉപയോഗിക്കാം, രജിസ്ട്രേഷൻ കഴിഞ്ഞേ R. കമ്പനി പേര് കിട്ടിയാലും ബ്രാൻഡ് സുരക്ഷിതമല്ല.", en="Trademark registration in Kerala: use TM after filing and R only after registration; a company name approval does not protect your brand.", mg="Trademark file cheythaal TM upayogikkaam, registration kazhinje R. Company peru kittiyaalum brand safe alla."),
    "BRAND": dict(ml="ബ്രാൻഡ് പേര് ആരും കോപ്പി ചെയ്യാതിരിക്കാൻ ട്രേഡ്മാർക്ക്. 45 ക്ലാസുകൾ, 10 വർഷം വാലിഡിറ്റി.", en="Protect your brand name with a trademark: 45 classes, valid 10 years and renewable.", mg="Brand peru aarum copy cheyyathirikkaan trademark. 45 classes, 10 varsham validity."),
    "ROC": dict(ml="പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് എല്ലാ വർഷവും AOC-4, MGT-7, DIR-3 KYC. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100.", en="ROC annual compliance for private limited companies: AOC-4, MGT-7 and DIR-3 KYC every year; late filing costs Rs 100 a day per form.", mg="Pvt Ltd company-kku ella varshavum AOC-4, MGT-7, DIR-3 KYC. Vaikiyaal oro form-num divasam 100."),
    "FILING": dict(ml="ബിസിനസ് ഇല്ലെങ്കിലും കമ്പനി ഫയലിംഗ് നിർബന്ധം. 3 വർഷം ഫയൽ ചെയ്തില്ലെങ്കിൽ ഡയറക്ടർമാർക്ക് അയോഗ്യത.", en="Annual filings are due even with zero business; 3 years of non-filing can disqualify directors.", mg="Business illenkilum company filing nirbandham. 3 varsham file cheythillenkil directors-nu disqualification."),
    "FSSAI": dict(ml="ഫുഡ് ബിസിനസിന് FSSAI: 12 ലക്ഷം വരെ രജിസ്ട്രേഷൻ, 20 കോടി വരെ സ്റ്റേറ്റ് ലൈസൻസ്. ഹോം ബേക്കർമാർക്കും വേണം.", en="FSSAI for food businesses in Kerala: basic registration up to Rs 12 lakh turnover, state licence up to Rs 20 crore; home bakers need it too.", mg="Food business-nu FSSAI: 12 lakh vare registration, 20 crore vare state licence. Home bakers-num venam."),
    "FOOD": dict(ml="വീട്ടിൽ നിന്ന് ഫുഡ് വിൽക്കാനും FSSAI നമ്പർ വേണം. പായ്ക്കറ്റിൽ 14 അക്ക നമ്പർ.", en="Selling food from home or a shop legally: FSSAI registration and the 14-digit number on every packet.", mg="Veettil ninnu food vilkkaanum FSSAI number venam. Packet-il 14 akka number."),
    "IEC": dict(ml="ഇംപോർട്ട്, എക്സ്പോർട്ട് ചെയ്യാൻ IEC കോഡ്. എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് ചെയ്യണം.", en="Import Export Code (IEC) from DGFT: needed to import or export goods, and must be updated every year between April and June.", mg="Import, export cheyyaan IEC code. Ella varshavum April-June update cheyyanam."),
    "EXPORT": dict(ml="ആദ്യ എക്സ്പോർട്ടിന് മുമ്പ്: IEC, GST, ഫോറിൻ പേമെന്റ് കിട്ടുന്ന കറന്റ് അക്കൗണ്ട്.", en="Before your first export from Kerala: IEC, GST registration and a current account that can receive foreign payments.", mg="Aadya export-nu mumbu: IEC, GST, foreign payment kittunna current account."),
    "NDA": dict(ml="ഐഡിയ, കോഡ്, ക്ലയന്റ് ലിസ്റ്റ് സംരക്ഷിക്കാൻ NDA. ശരിയായി സ്റ്റാമ്പ് ചെയ്ത NDA ആണ് ബലം.", en="NDA (non-disclosure agreement) in India: protects ideas, code and client lists when properly drafted and stamped.", mg="Idea, code, client list samrakshikkaan NDA. Shariyaayi stamp cheytha NDA aanu balam."),
    "SECRET": dict(ml="ഐഡിയ പങ്കുവെക്കും മുമ്പ് NDA. പക്ഷേ പരസ്യമായ കാര്യങ്ങൾ NDA കൊണ്ട് സംരക്ഷിക്കാനാവില്ല.", en="Before sharing your idea, sign an NDA; but nothing can protect what is already public.", mg="Idea pankuvekkum mumbu NDA. Pakshe public aaya kaaryangal NDA kondu samrakshikkaan pattilla."),
    "COFOUNDER": dict(ml="കോ-ഫൗണ്ടർ എഗ്രിമെന്റ്: ഷെയർ, വെസ്റ്റിംഗ്, റോളുകൾ, ഒരാൾ പോയാൽ എന്ത്.", en="Co-founder agreement: equity split, vesting, roles, IP and what happens if a founder leaves.", mg="Co-founder agreement: share, vesting, roles, oraal poyaal enthu."),
    "VESTING": dict(ml="വെസ്റ്റിംഗ്: ഷെയർ സമയം കൊണ്ട് നേടുന്നത്. സാധാരണ 4 വർഷം, 1 വർഷ ക്ലിഫ്.", en="Founder vesting: shares earned over time, commonly 4 years with a 1-year cliff.", mg="Vesting: share samayam kondu nedunnathu. Saadharana 4 varsham, 1 varsha cliff."),
    "PROJECTION": dict(ml="ഇൻവെസ്റ്റർക്ക് വേണ്ടത്: 3 വർഷ പ്രൊജക്ഷൻ, P&L, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക് ഈവൻ, അസംപ്ഷനുകൾ.", en="Investor-ready financial projections: 3 years, P&L, cash flow, break-even and written assumptions.", mg="Investor-kku vendathu: 3 varsha projection, P&L, cash flow, break even, assumptions."),
    "FORECAST": dict(ml="3 വർഷ റവന്യൂ, ചെലവ് ഫോർകാസ്റ്റ്: യഥാർത്ഥ നമ്പറിൽ നിന്ന് തുടങ്ങൂ.", en="3-year revenue and expense forecast: start from real numbers, set growth drivers and check cash flow.", mg="3 varsha revenue, expense forecast: real numbers-il ninnu thudangoo."),
    # ---- Udyam / MSME (topic ud) ----
    "UDYAM": dict(
        ml="ഉദ്യം (MSME) രജിസ്ട്രേഷൻ: ആധാർ, പാൻ വെച്ച് ഓൺലൈനായി. മാനുഫാക്ചറിംഗ്, സർവീസ് യൂണിറ്റുകൾക്ക് ബയർ 45 ദിവസത്തിനുള്ളിൽ പണം തരണം, ഇല്ലെങ്കിൽ പലിശ. ലോണിനും ടെൻഡറിനും സഹായം.",
        en="Udyam (MSME) registration in Kerala: Aadhaar and PAN based, online. For manufacturing and service micro and small units, buyers must pay within 45 days or owe interest; it also helps with priority lending and government tenders. MSME registration explained.",
        mg="Udyam MSME registration: Aadhaar, PAN vechu online. Manufacturing, service units-nu buyer 45 divasathinullil paisa tharanam, illenkil palisha. Loan-num tender-num sahaayam."),
    "MSME": dict(
        ml="2025 മുതൽ MSME ലിമിറ്റ്: മൈക്രോ 2.5 കോടി നിക്ഷേപം, 10 കോടി ടേൺഓവർ. സ്മോൾ 25 കോടി, 100 കോടി. മീഡിയം 125 കോടി, 500 കോടി. രണ്ടും പാലിക്കണം.",
        en="New MSME classification from April 2025: micro up to Rs 2.5 crore investment and Rs 10 crore turnover, small up to Rs 25 crore and Rs 100 crore, medium up to Rs 125 crore and Rs 500 crore. Both limits must be met.",
        mg="2025 muthal MSME limit: micro 2.5 crore investment, 10 crore turnover. Small 25 crore, 100 crore. Medium 125 crore, 500 crore. Randum paalikkanam."),
    # ---- Startup India / DPIIT (topic sui) ----
    "DPIIT": dict(
        ml="സ്റ്റാർട്ടപ്പ് ഇന്ത്യ (DPIIT) റെക്കഗ്നിഷൻ ആർക്ക് കിട്ടും? പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ്. 10 വർഷത്തിൽ താഴെ പഴക്കം, ഒരു വർഷവും 200 കോടി കടക്കാത്ത ടേൺഓവർ, പുതുമയുള്ള ആശയം.",
        en="Who can get Startup India DPIIT recognition? A Pvt Ltd, LLP or registered partnership under 10 years old, turnover never above Rs 200 crore, working on innovation or a scalable model. Startup India registration in Kerala.",
        mg="Startup India DPIIT recognition aarkku kittum? Pvt Ltd, LLP, registered partnership. 10 varshathil thaazhe, 200 crore kadakkatha turnover, puthumayulla idea."),
    "BENEFITS": dict(
        ml="DPIIT റെക്കഗ്നിഷൻ കൊണ്ട് എന്ത് കിട്ടും? പേറ്റന്റ്, ട്രേഡ്മാർക്ക് ഫീസിൽ ഇളവ്, സെൽഫ് സർട്ടിഫിക്കേഷൻ, പല സ്കീമുകൾക്കും യോഗ്യത. 3 വർഷത്തെ ടാക്സ് ഹോളിഡേയ്ക്ക് വേറെ അപേക്ഷ വേണം.",
        en="DPIIT recognition benefits: patent and trademark fee rebates, self-certification, eligibility for government schemes and tenders. The 80-IAC tax holiday needs a separate approval. Startup India benefits explained.",
        mg="DPIIT recognition kondu enthu kittum? Patent, trademark fee-il ilavu, self certification, schemes-nu eligibility. 3 varshathe tax holiday-kku vere application venam."),
    # ---- Kerala Startup Mission (topic sk) ----
    "KSUM": dict(
        ml="കേരള സ്റ്റാർട്ടപ്പ് മിഷൻ യുണീക്ക് ഐഡി: KSUM ഗ്രാന്റുകൾക്കും ഇൻക്യുബേഷനും പ്രോഗ്രാമുകൾക്കും ഇത് വേണം. കേരളത്തിൽ രജിസ്റ്റർ ചെയ്ത സ്റ്റാർട്ടപ്പ് ആയിരിക്കണം.",
        en="Kerala Startup Mission (KSUM) Unique ID: needed for KSUM grants, incubation and programmes. The startup should be registered in Kerala. KSUM registration explained.",
        mg="Kerala Startup Mission unique ID: KSUM grants-num incubation-num programs-num ithu venam. Kerala-yil register cheytha startup aayirikkanam."),
    "GRANT": dict(
        ml="KSUM ഗ്രാന്റിന് മുമ്പ്: കേരളത്തിൽ കമ്പനി അല്ലെങ്കിൽ LLP, DPIIT റെക്കഗ്നിഷൻ, KSUM യുണീക്ക് ഐഡി. ഐഡിയ ഗ്രാന്റിന് നേരത്തെ അപേക്ഷിക്കാം, പക്ഷേ പൈസ കിട്ടും മുമ്പ് കമ്പനിയും ഐഡിയും വേണം.",
        en="Before a KSUM grant: a Pvt Ltd or LLP in Kerala, DPIIT recognition and the KSUM Unique ID. For the idea grant you can apply early, but the company and ID are needed before money is released. Kerala startup grants.",
        mg="KSUM grant-nu mumbu: Kerala-yil company allenkil LLP, DPIIT recognition, KSUM unique ID. Idea grant-nu nerathe apply cheyyaam, pakshe paisa kittum mumbu company-um ID-um venam."),
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
    "manufacturer": dict(ml="ചെറിയ മാനുഫാക്ചറിംഗ് യൂണിറ്റുകൾക്ക്.", en="For small manufacturing units in Kerala.", mg="Cheriya manufacturing units-nu."),
    "service_unit": dict(ml="കമ്പനികൾക്ക് സർവീസ് കൊടുക്കുന്ന ബിസിനസുകൾക്ക്.", en="For service businesses whose clients are companies.", mg="Companies-nu service kodukkunna business-nu."),
    "trader_ud": dict(ml="കടകൾക്കും ഹോൾസെയിൽ കച്ചവടക്കാർക്കും.", en="For shop owners and wholesalers.", mg="Kadakalkkum wholesale kachavadakkarkkum."),
    "loan_seeker": dict(ml="ബിസിനസ് ലോൺ നോക്കുന്നവർക്ക്.", en="For business owners applying for a loan.", mg="Business loan nokkunnavarkku."),
    "supplier_unpaid": dict(ml="വലിയ ബയർമാർ പണം വൈകിപ്പിക്കുന്ന സപ്ലയർമാർക്ക്.", en="For suppliers whose big buyers pay late.", mg="Valiya buyers paisa vaikippikkunna suppliers-nu."),
    "tech_founder": dict(ml="ആപ്പ്, സോഫ്റ്റ്‌വെയർ, പ്രോഡക്റ്റ് ഫൗണ്ടർമാർക്ക്.", en="For app, SaaS and product founders in Kerala.", mg="App, software, product founders-nu."),
    "grant_seeker": dict(ml="സർക്കാർ ഗ്രാന്റുകൾ നോക്കുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders applying for government startup grants and schemes.", mg="Government grants nokkunna founders-nu."),
    "traditional_innovator": dict(ml="ഫുഡ്, കൃഷി, ആയുർവേദം, മാനുഫാക്ചറിംഗ് രംഗത്ത് പുതിയത് ചെയ്യുന്നവർക്ക്.", en="For food, agri, ayurveda and manufacturing businesses doing something new.", mg="Food, agri, ayurveda, manufacturing-il puthiyathu cheyyunnavarkku."),
    "student_founder": dict(ml="പ്രോട്ടോടൈപ്പുമായി നിൽക്കുന്ന സ്റ്റുഡന്റ് ഫൗണ്ടർമാർക്ക്.", en="For student and young founders with a prototype.", mg="Prototype-umaayi nilkkunna student founders-nu."),
    "investor_ready": dict(ml="ഇൻവെസ്റ്റർമാരെ കാണാൻ തയ്യാറെടുക്കുന്നവർക്ക്.", en="For founders getting ready to meet investors.", mg="Investors-ne kaanaan thayyaredukkunnavarkku."),
    "idea_stage": dict(ml="ഐഡിയയോ പ്രോട്ടോടൈപ്പോ മാത്രമുള്ള ഫൗണ്ടർമാർക്ക്.", en="For idea and prototype stage founders in Kerala.", mg="Idea-yo prototype-o maathram ulla founders-nu."),
    "kerala_registered": dict(ml="കേരളത്തിൽ കമ്പനി ഉണ്ട്, പക്ഷേ KSUM-ൽ ഇതുവരെ രജിസ്റ്റർ ചെയ്തിട്ടില്ലാത്തവർക്ക്.", en="For Kerala companies and LLPs that have not registered with KSUM yet.", mg="Kerala-yil company undu, pakshe KSUM-il ithuvare register cheythittillaathavarkku."),
    "returnee": dict(ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തി സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്നവർക്ക്.", en="For Gulf returnees and NRIs starting up in Kerala.", mg="Gulf-il ninnu thirichethi startup thudangunnavarkku."),
    "campus": dict(ml="കോളേജിൽ നിന്ന് സ്റ്റാർട്ടപ്പ് തുടങ്ങുന്നവർക്ക്.", en="For student founders starting up from campus.", mg="College-il ninnu startup thudangunnavarkku."),
    "women_founder": dict(ml="സ്വന്തം സ്റ്റാർട്ടപ്പ് നടത്തുന്ന സ്ത്രീകൾക്ക്.", en="For women founders in Kerala.", mg="Swantham startup nadathunna sthreekalkku."),
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
                "UDYAM": ["#udyamregistration", "#msme", "#msmeregistration"], "MSME": ["#msme", "#msmeindia", "#smallbusinessindia"],
                "DPIIT": ["#startupindia", "#dpiit", "#startupregistration"], "BENEFITS": ["#startupindia", "#80iac", "#startupbenefits"],
                "KSUM": ["#ksum", "#keralastartupmission", "#keralastartup"], "GRANT": ["#startupgrant", "#ksum", "#seedfund"],
                "INVEST": ["#investment", "#shareholdersagreement", "#equity"], "TERMSHEET": ["#termsheet", "#fundraising", "#venturecapital"], "FUNDING": ["#funding", "#angelinvestor", "#seedfunding"]})
H_TOPIC.update({"VALUATION": ["#valuation", "#companyvaluation", "#startupvaluation"], "WORTH": ["#valuation", "#startupfunding", "#investors"], 'TRADEMARK': ['#trademark', '#trademarkregistration', '#brandprotection'], 'BRAND': ['#brand', '#brandprotection', '#trademark'], 'ROC': ['#roc', '#annualcompliance', '#mca'], 'FILING': ['#compliance', '#roc', '#privatelimited'], 'FSSAI': ['#fssai', '#fssailicense', '#foodsafety'], 'FOOD': ['#foodbusiness', '#homebaker', '#fssai'], 'IEC': ['#iec', '#importexportcode', '#dgft'], 'EXPORT': ['#export', '#exportbusiness', '#iec'], 'NDA': ['#nda', '#confidentiality', '#contract'], 'SECRET': ['#nda', '#startuptips', '#confidentiality'], 'COFOUNDER': ['#cofounder', '#cofounderagreement', '#founders'], 'VESTING': ['#vesting', '#equity', '#cofounder'], 'PROJECTION': ['#financialprojections', '#pitchdeck', '#startupfunding'], 'FORECAST': ['#forecast', '#businessplan', '#financialplanning']})
H_SEG = {"freelancer": "#freelancer", "cofounders": "#startup", "proprietor": "#smallbusiness", "salaried": "#sidebusiness", "solo": "#entrepreneur", "nri": "#nri",
         "online_seller": "#onlineseller", "trader": "#smallbusiness", "service_pro": "#consultant", "new_company": "#startup", "nri_business": "#nri",
         "manufacturer": "#manufacturing", "service_unit": "#smallbusiness", "trader_ud": "#retail", "loan_seeker": "#businessloan", "supplier_unpaid": "#msme",
         "tech_founder": "#saas", "grant_seeker": "#startupgrant", "traditional_innovator": "#innovation", "student_founder": "#studentstartup", "investor_ready": "#fundraising",
         "idea_stage": "#ideastage", "kerala_registered": "#keralastartup", "returnee": "#nri", "campus": "#studentstartup", "women_founder": "#womenentrepreneurs",
         "founder_raising": "#startupfunding", "family_money": "#familybusiness", "nri_investor": "#nriinvestment", "angel": "#angelinvesting", "cofounder_split": "#cofounder"}
CORE = {"val": "#companyvaluation", "tm": "#trademarkregistration", "roc": "#roccompliance", "fssai": "#fssairegistration", "iec": "#importexportcode", "nda": "#nda", "cfa": "#cofounder", "fp": "#financialprojections", "ud": "#udyamregistration", "co": "#companyregistration", "gst": "#gstregistration", "inv": "#investoragreement", "sui": "#startupindia", "sk": "#keralastartupmission"}
H_EXTRA_T = {"gst": ["#gst", "#taxindia", "#keralabusiness", "#msme", "#smallbusinessindia"], "inv": ["#startupindia", "#keralastartup", "#investors", "#startuplaw", "#founders"],
             "val": ["#valuation", "#startupfunding", "#esop", "#founders", "#keralabusiness"],
             "tm": ["#trademark", "#brandprotection", "#startupindia", "#keralabusiness", "#brand"],
             "roc": ["#annualcompliance", "#privatelimited", "#mca", "#keralabusiness", "#compliance"],
             "fssai": ["#fssai", "#homebaker", "#foodbusiness", "#cloudkitchen", "#keralafood"],
             "iec": ["#iec", "#export", "#exportbusiness", "#importexport", "#keralaexports"],
             "nda": ["#nda", "#startuplaw", "#confidentiality", "#founders", "#contract"],
             "cfa": ["#cofounderagreement", "#startuplaw", "#vesting", "#founders", "#startupindia"],
             "fp": ["#financialplanning", "#startupfunding", "#businessplan", "#pitchdeck", "#founders"],
             "ud": ["#msme", "#keralabusiness", "#smallbusinessindia", "#makeinindia", "#entrepreneur"],
             "sui": ["#startup", "#founders", "#keralastartup", "#entrepreneurindia", "#makeinindia"], "sk": ["#startup", "#kochi", "#trivandrum", "#founders", "#keralabusiness"]}
H_EXTRA = ["#mca", "#incorporation", "#startupindia", "#businessowner", "#keralastartup"]

def _pick(xs, key): return xs[zlib.crc32(key.encode()) % len(xs)]

def hashtags(item_id, base, segment, topic="co"):
    extra = H_EXTRA_T.get(topic, H_EXTRA)
    tags = [CORE.get(topic, CORE["co"]), _pick(H_LOCAL, item_id + "l"), _pick(H_TOPIC.get(base, extra), item_id + "t"), H_SEG.get(segment, "#entrepreneur")]
    tags = list(dict.fromkeys(tags))
    for x in [_pick(extra, item_id + "x")] + extra + H_EXTRA:
        if len(tags) >= 5: break
        if x not in tags: tags.append(x)
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
