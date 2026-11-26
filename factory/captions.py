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
    "ITR": dict(ml="വിൽപ്പന ഇല്ലെങ്കിലും GST റിട്ടേൺ വേണം. 3 വർഷം കഴിഞ്ഞാൽ ഫയൽ ചെയ്യാനാവില്ല.", en="GST returns are due even with no sales, and since July 2025 a return older than 3 years can't be filed at all.", mg="Vilpana illenkilum GST return venam. 3 varsham kazhinjaal file cheyyaan pattilla."),
    "ACCOUNTS": dict(ml="മാസക്കണക്ക്: ബില്ലുകൾ, ബാങ്ക് മാച്ചിംഗ്, GST, TDS, വർഷാവസാനം ITR.", en="Monthly accounts: every bill recorded, bank matched, GST and TDS from the books, ITR at year-end.", mg="Maasakkanakku: billukal, bank matching, GST, TDS, varshaavasaanam ITR."),
    "SHOPS": dict(ml="കേരളത്തിലെ ഓരോ കടയ്ക്കും ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ: സ്റ്റാഫ് ഇല്ലെങ്കിലും, 60 ദിവസത്തിനകം.", en="Every shop in Kerala registers under the Shops and Commercial Establishments Act within 60 days, even with no staff.", mg="Kadaykku Shops Act registration: staff illenkilum, 60 divasathinakam."),
    "KSMART": dict(ml="കടയ്ക്ക് ആദ്യം തദ്ദേശ സ്ഥാപനത്തിന്റെ ലൈസൻസ്; നഗരങ്ങളിൽ K-SMART വഴി.", en="A business place needs a local-body licence first; towns and cities use the K-SMART portal.", mg="Kadaykku aadyam local body licence; nagarangalil K-SMART vazhi."),
    "PRAVASI": dict(ml="2 വർഷം വിദേശത്ത് ജോലി ചെയ്ത മലയാളികൾക്ക് NORKA NDPREM: 15% മൂലധന സബ്സിഡി, 3% പലിശ സബ്സിഡി.", en="NORKA NDPREM for Keralites who worked abroad 2+ years: 15% capital subsidy and 3% interest subsidy on bank loans.", mg="2 varsham videshathu joli cheytha malayaalikalkku NORKA NDPREM."),
    "NORKA": dict(ml="ലോൺ തീരുമാനിക്കുന്നത് ബാങ്ക്. നല്ല പ്രോജക്റ്റ് റിപ്പോർട്ട് ആണ് പ്രധാനം.", en="The bank decides the loan; a strong project report matters most.", mg="Loan theerumaanikkunnathu bank. Nalla project report aanu pradhaanam."),
    "ESIC": dict(ml="10 സ്റ്റാഫ് ആയാൽ ESIC, 20 ആയാൽ EPF. പുതിയ ലേബർ കോഡുകൾ 2025 നവംബർ മുതൽ.", en="ESIC from 10 employees and EPF from 20, under the Labour Codes in force since November 2025.", mg="10 staff aayaal ESIC, 20 aayaal EPF."),
    "PAYROLL": dict(ml="ശമ്പള സ്ലിപ്പ്, PF, ESI, പ്രൊഫഷണൽ ടാക്സ്: എല്ലാ മാസവും കൃത്യമായി.", en="Monthly payroll: salary slips, PF, ESI and professional tax, on time every month.", mg="Shambala slip, PF, ESI, professional tax: ella maasavum."),
    "GATEWAY": dict(ml="ഓൺലൈൻ പേയ്മെന്റ് ഗേറ്റ്‌വേയ്ക്ക് KYC നിർബന്ധം. രേഖകൾ ബിസിനസ് തരം അനുസരിച്ച്; ബിസിനസ് പേര് PAN-ലും ബാങ്കിലും ഒരുപോലെ വേണം.", en="Every online payment gateway runs KYC on your business first. Documents depend on your business type, and the business name must match on PAN, bank and registration.", mg="Online payment gateway-kku KYC nirbandham. Rekhakal business type anusarichu; business peru PAN-ilum bank-ilum orupole venam."),
    "PAYMENT": dict(ml="ഓൺലൈൻ പേയ്മെന്റ് എടുക്കും മുമ്പ്: ബിസിനസ് തരം, രജിസ്ട്രേഷൻ, ബിസിനസ് പേരിൽ ബാങ്ക് അക്കൗണ്ട്, KYC രേഖകൾ.", en="Before taking online payments: pick the business type, register it, open a bank account in its name and keep KYC documents ready.", mg="Online payment edukkum munpu: business type, registration, business peril bank account, KYC rekhakal."),
    "WEBSITE": dict(ml="നല്ല ബിസിനസ് വെബ്സൈറ്റ്: ഫോണിൽ ശരിയായി, ബിസിനസ് പേരിൽ ഡൊമെയ്ൻ, വ്യക്തമായ കോൺടാക്റ്റ്, യഥാർത്ഥ ഫോട്ടോ. മാസ തവണയായി അടയ്ക്കാനും പറ്റും.", en="A good business website works well on phones, uses a domain in your business name, shows clear contact details and real photos. With us you can pay for it in monthly parts.", mg="Nalla business website: phone-il shariyaayi, business peril domain, clear contact, real photos. Maasa thavanayaayi adakkaanum pattum."),
    "WEBPLAN": dict(ml="വെബ്സൈറ്റ് ഇപ്പോൾ, അടവ് മാസം തോറും: ഒറ്റയടിക്ക് വലിയ തുക വേണ്ട. എത്ര എന്ന് പ്രോജക്റ്റ് നോക്കി ടീം പറയും.", en="Get your website now and pay in monthly parts instead of one big amount. Our team shares the exact plan after understanding your project.", mg="Website ippol, adavu maasam thorum: ottayadikku valiya thuka venda. Ethra ennu project nokki team parayum."),
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
    # tm
    "d2c_brand": dict(ml="ഓൺലൈനായി സ്വന്തം ബ്രാൻഡ് വിൽക്കുന്ന D2C ബ്രാൻഡുകൾക്ക്.", en="For D2C brands in Kerala selling their own products online.", mg="Online-il swantham brand vilkkunna D2C brands-nu."),
    "food_brand": dict(ml="സ്വന്തം പേരിൽ ഫുഡ് പ്രോഡക്റ്റുകൾ വിൽക്കുന്ന ഫുഡ് ബ്രാൻഡുകൾക്ക്.", en="For food brands in Kerala selling under their own name.", mg="Swantham peril food products vilkkunna food brands-nu."),
    "salon_clinic": dict(ml="സലൂണും ക്ലിനിക്കും നടത്തുന്നവർക്ക്.", en="For salon and clinic owners in Kerala.", mg="Salon-um clinic-um nadathunnavarkku."),
    "app_founder": dict(ml="സ്വന്തം ആപ്പ് ലോഞ്ച് ചെയ്യുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders launching an app under their own brand name.", mg="Swantham app launch cheyyunna founders-nu."),
    "copied_brand": dict(ml="ബ്രാൻഡ് പേര് മറ്റാരെങ്കിലും കോപ്പി ചെയ്തെന്ന് സംശയിക്കുന്നവർക്ക്.", en="For business owners who think someone has copied their brand name.", mg="Brand name aarenkilum copy cheythu ennu samshayikkunnavarkku."),
    # roc
    "dormant_company": dict(ml="രജിസ്റ്റർ ചെയ്തിട്ടും ബിസിനസ് ഒന്നും നടക്കാത്ത കമ്പനികൾക്ക്.", en="For companies in Kerala that are registered but not doing any business yet.", mg="Register cheythittum business onnum nadakkaatha company-kalkku."),
    "new_company_roc": dict(ml="ആദ്യ വർഷത്തെ ROC ഫയലിംഗിലേക്ക് എത്തുന്ന പുതിയ കമ്പനികൾക്ക്.", en="For newly registered companies coming up to their first year of ROC filings.", mg="First year ROC filing-ilekku ethunna puthiya company-kalkku."),
    "late_filer": dict(ml="ROC ഫയലിംഗ് വൈകിപ്പോയ കമ്പനികൾക്ക്.", en="For companies that have missed or delayed their ROC filings.", mg="ROC filing late aayippoya company-kalkku."),
    "llp_owner": dict(ml="LLP നടത്തുന്ന പാർട്ണർമാർക്ക്.", en="For partners running an LLP in Kerala.", mg="LLP nadathunna partners-nu."),
    "nri_director": dict(ml="ഗൾഫിലിരുന്ന് നാട്ടിലെ കമ്പനിയുടെ ഡയറക്ടറായ NRI-കൾക്ക്.", en="For NRI directors in the Gulf with a company in Kerala.", mg="Gulf-il irunnu naattile company-yude director aaya NRI-kalkku."),
    # fssai
    "home_baker": dict(ml="വീട്ടിൽ നിന്ന് കേക്കും സ്നാക്സും വിൽക്കുന്ന ഹോം ബേക്കർമാർക്ക്.", en="For home bakers in Kerala selling cakes and snacks from home.", mg="Veettil ninnu cake-um snacks-um vilkkunna home bakers-nu."),
    "cloud_kitchen": dict(ml="സ്വിഗ്ഗി, സൊമാറ്റോ വഴി വിൽക്കുന്ന ക്ലൗഡ് കിച്ചണുകൾക്ക്.", en="For cloud kitchens in Kerala selling on Swiggy and Zomato.", mg="Swiggy, Zomato vazhi vilkkunna cloud kitchens-nu."),
    "spice_exporter": dict(ml="സ്പൈസസ് പായ്ക്ക് ചെയ്ത് വിൽക്കുന്നവർക്കും എക്സ്പോർട്ട് ചെയ്യുന്നവർക്കും.", en="For spice packers and exporters in Kerala.", mg="Spices pack cheythu vilkkunnavarkkum export cheyyunnavarkkum."),
    "cafe_owner": dict(ml="കഫേയും ചെറിയ റെസ്റ്റോറന്റും നടത്തുന്നവർക്ക്.", en="For cafe and small restaurant owners in Kerala.", mg="Cafe-um cheriya restaurant-um nadathunnavarkku."),
    "packaged_food": dict(ml="പായ്ക്ക് ചെയ്ത ഫുഡ് പ്രോഡക്റ്റുകൾ ഉണ്ടാക്കി വിൽക്കുന്നവർക്ക്.", en="For businesses making and selling packaged food.", mg="Packaged food products undaakki vilkkunnavarkku."),
    # iec
    "first_exporter": dict(ml="ആദ്യമായി എക്സ്പോർട്ട് ചെയ്യാൻ ഒരുങ്ങുന്നവർക്ക്.", en="For businesses in Kerala getting ready for their first export order.", mg="Aadyamaayi export cheyyaan orungunnavarkku."),
    "importer": dict(ml="വിദേശത്ത് നിന്ന് സാധനങ്ങൾ ഇമ്പോർട്ട് ചെയ്യുന്നവർക്ക്.", en="For businesses importing goods from abroad.", mg="Foreign-il ninnu saadhanangal import cheyyunnavarkku."),
    "spice_trade": dict(ml="സ്പൈസസ് കച്ചവടം വിദേശത്തേക്ക് എത്തിക്കാൻ ആലോചിക്കുന്നവർക്ക്.", en="For spice traders in Kerala looking for buyers abroad.", mg="Spice kachavadam foreign-ilekku ethikkaan aalochikkunnavarkku."),
    "handicraft_export": dict(ml="കൈത്തറി, കയർ, കരകൗശല ഉൽപ്പന്നങ്ങൾ വിദേശത്ത് വിൽക്കാൻ ആലോചിക്കുന്നവർക്ക്.", en="For handloom, coir and handicraft makers in Kerala selling abroad.", mg="Handloom, coir, handicraft products foreign-il vilkkaan aalochikkunnavarkku."),
    "service_export": dict(ml="വിദേശ ക്ലയന്റുകൾക്ക് സർവീസ് കൊടുക്കുന്ന ഫ്രീലാൻസർമാർക്കും ഏജൻസികൾക്കും.", en="For freelancers and agencies in Kerala serving clients abroad.", mg="Foreign clients-nu service kodukkunna freelancers-num agencies-num."),
    # nda
    "founder_pitching": dict(ml="ഐഡിയ മറ്റുള്ളവരോട് പിച്ച് ചെയ്യാൻ പോകുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders about to pitch their idea to others.", mg="Idea mattullavarodu pitch cheyyaan pokunna founders-nu."),
    "online_seller_pg": dict(ml="ഇൻസ്റ്റഗ്രാമിലും വാട്സ്ആപ്പിലും വിൽക്കുന്നവർക്ക്: ഓൺലൈൻ പേയ്മെന്റ് എടുക്കാൻ.", en="For Instagram and WhatsApp sellers who want to take online payments.", mg="Instagram-ilum WhatsApp-ilum vilkkunnavarkku: online payment edukkaan."),
    "service_pro_pg": dict(ml="ട്യൂഷൻ, കൺസൾട്ടിംഗ്, സർവീസ് ബിസിനസുകൾക്ക്.", en="For tutors, consultants and service businesses.", mg="Tuition, consulting, service businesses-inu."),
    "proprietor_pg": dict(ml="ഒറ്റയ്ക്ക് ബിസിനസ് നടത്തുന്ന പ്രൊപ്രൈറ്റർമാർക്ക്.", en="For proprietors running a business on their own.", mg="Ottaykku business nadathunna proprietor-maarkku."),
    "new_company_pg": dict(ml="പുതുതായി രജിസ്റ്റർ ചെയ്ത കമ്പനികൾക്ക്.", en="For newly registered companies.", mg="Puthuthaayi register cheytha companies-inu."),
    "app_founder_pg": dict(ml="ആപ്പോ വെബ്സൈറ്റോ തുടങ്ങുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders launching an app or website.", mg="App-o website-o thudangunna founders-inu."),
    "nil_filer": dict(ml="വിൽപ്പന ഇല്ലാത്ത മാസവും GST റിട്ടേൺ ഫയൽ ചെയ്യേണ്ടവർക്ക്.", en="For GST-registered businesses with months of no sales.", mg="Vilpana illaatha maasavum GST return file cheyyendavarkku."),
    "freelancer_itr": dict(ml="ITR ഫയൽ ചെയ്യുന്ന ഫ്രീലാൻസർമാർക്കും പ്രൊഫഷണലുകൾക്കും.", en="For freelancers and professionals filing income-tax returns.", mg="ITR file cheyyunna freelancers-inum professionals-inum."),
    "small_trader_acc": dict(ml="കണക്ക് സൂക്ഷിക്കാൻ സമയം ഇല്ലാത്ത ചെറിയ കച്ചവടക്കാർക്ക്.", en="For small traders with no time to keep accounts.", mg="Kanakku sookshikkaan samayam illaatha cheriya kachavadakkaarkku."),
    "new_company_acc": dict(ml="പുതുതായി തുടങ്ങിയ കമ്പനികൾക്കും LLP-കൾക്കും.", en="For newly started companies and LLPs.", mg="Puthuthaayi thudangiya companies-inum LLP-kalkkum."),
    "notice_holder": dict(ml="GST അല്ലെങ്കിൽ ഇൻകം ടാക്സ് നോട്ടീസ് കിട്ടിയവർക്ക്.", en="For businesses that received a GST or income-tax notice.", mg="GST allenkil income tax notice kittiyavarkku."),
    "new_shop": dict(ml="പുതിയ കട തുടങ്ങുന്നവർക്ക്.", en="For people opening a new shop in Kerala.", mg="Puthiya kada thudangunnavarkku."),
    "home_office": dict(ml="വീട്ടിൽ നിന്നോ ചെറിയ ഓഫീസിൽ നിന്നോ ബിസിനസ് നടത്തുന്നവർക്ക്.", en="For businesses run from home or a small office.", mg="Veettil ninno cheriya office-il ninno business nadathunnavarkku."),
    "no_staff_shop": dict(ml="സ്റ്റാഫ് ഇല്ലാതെ ഒറ്റയ്ക്ക് കട നടത്തുന്നവർക്ക്.", en="For shop owners running the shop alone, with no staff.", mg="Staff illaathe ottaykku kada nadathunnavarkku."),
    "salaried_staff_kl": dict(ml="ശമ്പളത്തിന് സ്റ്റാഫ് ഉള്ള കടകൾക്കും ഓഫീസുകൾക്കും.", en="For shops and offices with staff on salary.", mg="Shambalathinu staff ulla kadakalkkum officekalkkum."),
    "town_business": dict(ml="മുനിസിപ്പാലിറ്റി, കോർപ്പറേഷൻ പ്രദേശത്തെ ബിസിനസുകൾക്ക്.", en="For businesses in municipality and corporation areas.", mg="Municipality, corporation pradeshathe businesses-inu."),
    "gulf_returnee": dict(ml="ഗൾഫിൽ നിന്ന് തിരിച്ചെത്തി ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For Gulf returnees starting a business in Kerala.", mg="Gulf-il ninnu thirichethi business thudangunnavarkku."),
    "nri_investing": dict(ml="നാട്ടിലെ കമ്പനിയിൽ ഷെയർ എടുക്കുന്ന പ്രവാസികൾക്ക്.", en="For NRIs taking shares in a company back home.", mg="Naattile company-il share edukkunna pravaasikalkku."),
    "returnee_loan": dict(ml="ബിസിനസ് ലോണിന് അപേക്ഷിക്കുന്ന പ്രവാസികൾക്ക്.", en="For returnees applying for a business loan.", mg="Business loan-inu apekshikkunna pravaasikalkku."),
    "family_business_nri": dict(ml="പ്രവാസി പൈസ കൊണ്ട് കുടുംബ ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For families starting a business with money earned abroad.", mg="Pravaasi paisa kondu kudumba business thudangunnavarkku."),
    "mudra_repeat": dict(ml="ആദ്യ മുദ്ര ലോൺ കഴിഞ്ഞ് വലിയ ലോൺ നോക്കുന്നവർക്ക്.", en="For owners who repaid a Mudra loan and want a bigger one.", mg="Aadya Mudra loan kazhinju valiya loan nokkunnavarkku."),
    "first_hire": dict(ml="ആദ്യമായി സ്റ്റാഫിനെ എടുക്കുന്നവർക്ക്.", en="For owners hiring their first staff.", mg="Aadyamaayi staff-ine edukkunnavarkku."),
    "ten_staff": dict(ml="10 സ്റ്റാഫിന് അടുത്തെത്തിയ ബിസിനസുകൾക്ക്.", en="For businesses nearing 10 employees.", mg="10 staff-inu aduthethiya businesses-inu."),
    "twenty_staff": dict(ml="20 സ്റ്റാഫിന് അടുത്തെത്തിയ ബിസിനസുകൾക്ക്.", en="For businesses nearing 20 employees.", mg="20 staff-inu aduthethiya businesses-inu."),
    "salary_split": dict(ml="ശമ്പളം ബേസിക്കും അലവൻസും ആയി പിരിക്കുന്നവർക്ക്.", en="For employers splitting pay into basic and allowances.", mg="Shambalam basic-um allowance-um aayi pirikkunnavarkku."),
    "new_hires_incentive": dict(ml="ഈ വർഷം കൂടുതൽ പേരെ എടുക്കാൻ പോകുന്നവർക്ക്.", en="For employers planning to hire more people this year.", mg="Ee varsham kooduthal pere edukkaan pokunnavarkku."),
    "no_website": dict(ml="ഇതുവരെ വെബ്സൈറ്റ് ഇല്ലാത്ത ബിസിനസുകൾക്ക്.", en="For businesses that don't have a website yet.", mg="Ithuvare website illaatha businesses-inu."),
    "insta_only": dict(ml="ഇൻസ്റ്റഗ്രാം പേജ് മാത്രം വെച്ച് കച്ചവടം ചെയ്യുന്നവർക്ക്.", en="For businesses that sell only through an Instagram page.", mg="Instagram page maathram vechu kachavadam cheyyunnavarkku."),
    "old_website": dict(ml="പഴയ വെബ്സൈറ്റ് പുതുക്കേണ്ടവർക്ക്.", en="For businesses with an old website that needs a refresh.", mg="Pazhaya website puthukkendavarkku."),
    "service_business": dict(ml="എൻക്വയറികൾ വേണ്ട സർവീസ് ബിസിനസുകൾക്ക്.", en="For service businesses that need more enquiries.", mg="Enquiries venda service businesses-inu."),
    "online_shop": dict(ml="ഓൺലൈനായി സാധനം വിൽക്കാൻ പ്ലാൻ ചെയ്യുന്നവർക്ക്.", en="For businesses planning to sell products online.", mg="Online aayi saadhanam vilkkaan plan cheyyunnavarkku."),
    "agency_client": dict(ml="ക്ലയന്റിന്റെ രഹസ്യ വിവരങ്ങൾ കൈകാര്യം ചെയ്യുന്ന ഏജൻസികൾക്ക്.", en="For agencies in Kerala handling confidential client information.", mg="Client-inte confidential details handle cheyyunna agencies-nu."),
    "freelancer_nda": dict(ml="ക്ലയന്റ് NDA ഒപ്പിടാൻ ആവശ്യപ്പെടുന്ന ഫ്രീലാൻസർമാർക്ക്.", en="For freelancers whose clients ask them to sign an NDA.", mg="Client NDA sign cheyyaan parayunna freelancers-nu."),
    "vendor_supplier": dict(ml="വെണ്ടർമാരുമായും സപ്ലയർമാരുമായും വിവരങ്ങൾ പങ്കുവെക്കുന്ന ബിസിനസുകൾക്ക്.", en="For businesses sharing details with vendors and suppliers.", mg="Vendors-umaayum suppliers-umaayum details share cheyyunna business-nu."),
    "employee_nda": dict(ml="ആദ്യമായി ജീവനക്കാരെ എടുക്കുന്ന ബിസിനസുകൾക്ക്.", en="For business owners in Kerala hiring their first employees.", mg="Aadyamaayi staff-ne edukkunna business owners-nu."),
    # cfa
    "friends_cofounders": dict(ml="സുഹൃത്തുക്കളുമായി ചേർന്ന് ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For friends starting a business together in Kerala.", mg="Friends-umaayi chernnu business thudangunnavarkku."),
    "tech_nontech": dict(ml="ടെക്, നോൺ-ടെക് കോ-ഫൗണ്ടർമാർ ഒന്നിച്ച് തുടങ്ങുന്ന സ്റ്റാർട്ടപ്പുകൾക്ക്.", en="For startups with one tech and one non-tech co-founder.", mg="Tech, non-tech co-founders orumichu thudangunna startups-nu."),
    "family_cofounders": dict(ml="കുടുംബാംഗങ്ങൾ ചേർന്ന് ബിസിനസ് തുടങ്ങുന്നവർക്ക്.", en="For family members starting a business together.", mg="Family members chernnu business thudangunnavarkku."),
    "late_joiner": dict(ml="തുടങ്ങിയ ശേഷം പുതിയ കോ-ഫൗണ്ടറെ ചേർക്കുന്ന സ്റ്റാർട്ടപ്പുകൾക്ക്.", en="For startups bringing in a co-founder after they have started.", mg="Thudangiya shesham puthiya co-founder-ne cherkkunna startups-nu."),
    "remote_cofounder": dict(ml="ഗൾഫിലോ മറ്റൊരു നഗരത്തിലോ ഉള്ള കോ-ഫൗണ്ടറുമായി സ്റ്റാർട്ടപ്പ് നടത്തുന്നവർക്ക്.", en="For startups with a co-founder working from the Gulf or another city.", mg="Gulf-ilo vere city-yilo ulla co-founder-umaayi startup nadathunnavarkku."),
    # val
    "raising_round": dict(ml="ഫണ്ടിംഗ് റൗണ്ടിന് ഒരുങ്ങുന്ന സ്റ്റാർട്ടപ്പ് ഫൗണ്ടർമാർക്ക്.", en="For startup founders in Kerala preparing for a funding round.", mg="Funding round-nu orungunna startup founders-nu."),
    "esop_plan": dict(ml="ടീമിന് ESOP കൊടുക്കാൻ ആലോചിക്കുന്ന കമ്പനികൾക്ക്.", en="For companies planning ESOPs for their team.", mg="Team-nu ESOP kodukkaan aalochikkunna company-kalkku."),
    "partner_exit": dict(ml="ഒരു പാർട്ണറോ ഡയറക്ടറോ കമ്പനി വിടുന്ന സാഹചര്യത്തിലുള്ളവർക്ക്.", en="For companies where a partner or director is exiting.", mg="Oru partner-o director-o company vidunna situation-il ullavarkku."),
    "nri_share_issue": dict(ml="NRI-കൾക്ക് ഷെയർ കൊടുക്കാൻ ആലോചിക്കുന്ന കമ്പനികൾക്ക്.", en="For companies issuing shares to NRI investors.", mg="NRI-kalkku shares kodukkaan aalochikkunna company-kalkku."),
    "share_transfer": dict(ml="ഷെയറുകൾ കൈമാറ്റം ചെയ്യാൻ ആലോചിക്കുന്ന ഷെയർഹോൾഡർമാർക്ക്.", en="For shareholders planning to transfer shares.", mg="Shares transfer cheyyaan aalochikkunna shareholders-nu."),
    # fp
    "investor_pitch": dict(ml="ഇൻവെസ്റ്റർമാരോട് പിച്ച് ചെയ്യാൻ ഒരുങ്ങുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders preparing to pitch to investors.", mg="Investors-inodu pitch cheyyaan orungunna founders-nu."),
    "bank_loan": dict(ml="ബാങ്ക് ലോണിന് അപേക്ഷിക്കുന്ന ബിസിനസുകൾക്ക്.", en="For businesses in Kerala applying for a bank loan.", mg="Bank loan-nu apply cheyyunna business-nu."),
    "grant_application": dict(ml="സ്റ്റാർട്ടപ്പ് ഗ്രാന്റിന് അപേക്ഷിക്കുന്ന ഫൗണ്ടർമാർക്ക്.", en="For founders applying for a startup grant.", mg="Startup grant-nu apply cheyyunna founders-nu."),
    "early_revenue": dict(ml="ആദ്യ വരുമാനം വന്നു തുടങ്ങിയ സ്റ്റാർട്ടപ്പുകൾക്ക്.", en="For startups that have started earning their first revenue.", mg="First revenue vannu thudangiya startups-nu."),
    "pre_revenue": dict(ml="ഇതുവരെ വരുമാനം ഇല്ലാത്ത സ്റ്റാർട്ടപ്പുകൾക്ക്.", en="For pre-revenue startups with no sales yet.", mg="Ithuvare revenue illaatha startups-nu."),
}
# 26 Nov review (GROWTH_PLAN rule 3: 134k reach, ~6 keyword comments): ONE keyword per caption and the concrete thing
# they get. The post's own unique keyword still works in the worker (kwmap) but is no longer shown.
CTA = dict(ml="{base} എന്ന് കമന്റ് ചെയ്യൂ 👇 {promise_ml} DM-ൽ അയച്ചുതരാം",
           en="Comment {base} 👇 and we'll DM you {promise_en}",
           mg="{base} ennu comment cheyyu 👇 {promise_mg} DM-il ayachu tharaam")
PROMISE_EN = {"START": "which structure fits you: Pvt Ltd, LLP or OPC", "NAME": "the company-name checklist", "AFTER": "the after-registration compliance list",
              "CHECKLIST": "the registration documents checklist", "DOCS": "the registration documents checklist",
              "GST": "the guide on when you need GST", "LIMIT": "the GST turnover limits list", "PENALTY": "the list of GST penalties to avoid",
              "INVEST": "the agreements to sign before investor money comes in", "TERMSHEET": "what is binding in a term sheet", "FUNDING": "the next steps after an investor says yes",
              "DPIIT": "the DPIIT eligibility checklist", "BENEFITS": "the benefits of DPIIT recognition", "KSUM": "the KSUM Unique ID guide", "GRANT": "the checklist before a KSUM grant",
              "UDYAM": "the benefits of Udyam registration", "MSME": "the micro / small / medium check", "TRADEMARK": "the guide to protecting your brand",
              "BRAND": "the checklist to stop name copying", "ROC": "the yearly ROC filing calendar", "FILING": "the filings due even with no business",
              "FSSAI": "the guide to which FSSAI you need", "FOOD": "the checklist to sell food legally", "IEC": "the IEC guide", "EXPORT": "the checklist before your first export",
              "NDA": "what a strong NDA must have", "SECRET": "the checklist before sharing your idea", "COFOUNDER": "the co-founder agreement checklist",
              "VESTING": "how vesting protects co-founders", "PROJECTION": "what investors check in projections", "FORECAST": "how to build a 3-year forecast",
              "VALUATION": "when you need a valuation and which method fits", "WORTH": "how a company's worth is worked out"}

def _promise_ml(s):
    sub = (s.get("cta") or ("", ""))[1] or ""
    sub = sub.replace("എന്ന് കമന്റ് ചെയ്യൂ", "").replace("\n", " ").strip()
    for tail in ("അയച്ചുതരാം",): sub = sub.removesuffix(tail).strip()
    return sub or "ഗൈഡ്"
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
CORE = {"acc": "#gstfiling", "kl": "#keralabusiness", "nri": "#pravasi", "pay": "#payroll", "pg": "#paymentgateway", "web": "#websitedevelopment", "val": "#companyvaluation", "tm": "#trademarkregistration", "roc": "#roccompliance", "fssai": "#fssairegistration", "iec": "#importexportcode", "nda": "#nda", "cfa": "#cofounder", "fp": "#financialprojections", "ud": "#udyamregistration", "co": "#companyregistration", "gst": "#gstregistration", "inv": "#investoragreement", "sui": "#startupindia", "sk": "#keralastartupmission"}
H_EXTRA_T = {"acc": ["#incometax", "#gstreturn", "#smallbusinessindia", "#accounting", "#keralabusiness"], "kl": ["#tradelicence", "#shopsact", "#kerala", "#smallbusiness", "#ksmart"], "nri": ["#norka", "#gulfmalayali", "#nri", "#businessloan", "#keralabusiness"], "pay": ["#epf", "#esic", "#labourcodes", "#hrcompliance", "#smallbusinessindia"], "pg": ["#onlinepayments", "#smallbusinessindia", "#keralabusiness", "#ecommerce", "#startupindia"], "web": ["#website", "#smallbusiness", "#keralabusiness", "#digitalmarketing", "#startupindia"], "gst": ["#gst", "#taxindia", "#keralabusiness", "#msme", "#smallbusinessindia"], "inv": ["#startupindia", "#keralastartup", "#investors", "#startuplaw", "#founders"],
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
    tags = hashtags(s["id"], base, seg, s.get("topic") or "co")
    def build(with_seg):
        parts = [head.strip()]
        for lang in ("ml", "en", "mg"):
            own = s.get("cap_" + lang)
            para = own or t[lang]
            if g and (with_seg or not own):   # topic text always had the segment; custom text gets it on its own line
                para += ("\n" if own else " ") + g[lang]
            parts.append(para + "\n" + CTA[lang].format(base=base, promise_ml=_promise_ml(s), promise_en=PROMISE_EN.get(base, "our free guide"), promise_mg=PROMISE_EN.get(base, "free guide").removeprefix("the ")))
        return "\n\n".join(parts + [tags])
    out = build(True)
    if len(out) > 2200: out = build(False)   # too long: drop the segment line from custom captions, never the CTA / hashtags
    if len(out) > 2200:                       # still too long: shorten the opening line, keep the end intact
        cut = len(out) - 2200 + 1
        out = out[:max(0, len(head.strip()) - cut)] + "…" + out[len(head.strip()):]
    assert out.count("#") <= 5 and len(out) <= 2200, s["id"]
    return out
