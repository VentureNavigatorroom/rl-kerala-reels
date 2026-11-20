# Startup India / DPIIT batch 06 (21 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_SUI. No promises of approval or benefits. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DPIIT, CTA_BENEFITS = topics.CTA_DPIIT, topics.CTA_BENEFITS

chat("uc003", "investor_ready", "C", "\"സ്റ്റാർട്ടപ്പ് ഇന്ത്യയിൽ\nഫോം ഇട്ടു.\nകമ്പനി ആയോ?\"", ("ഷഹാന", "ആസിഫ്"), [
 (1,"ഷഹാനാ, ഗൾഫിൽ ഇരുന്ന് സ്റ്റാർട്ടപ്പ് ഇന്ത്യ സൈറ്റിൽ ഫോം ഇട്ടു. നാട്ടിൽ എത്തുമ്പോഴേക്കും കമ്പനി റെഡി ആകുമല്ലോ?"),
 (0,"ആസിഫേ, ഏത് കമ്പനി? നിനക്ക് ഇതുവരെ കമ്പനിയോ LLP-യോ ഇല്ലല്ലോ."),
 (1,"DPIIT രജിസ്ട്രേഷൻ തന്നെയല്ലേ കമ്പനി?"),
 (0,"അല്ല. ഉള്ള കമ്പനിയെ DPIIT അംഗീകരിക്കുന്നതാ. ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ രജിസ്റ്റർ ചെയ്യണം, പിന്നെ അപേക്ഷ."),
 (1,"അപ്പോ വീടില്ലാതെ പാലുകാച്ചൽ നടത്താൻ നോക്കി."),
 (0,"ആദ്യം വീട്, പിന്നെ പാലുകാച്ചൽ.")],
 "ആദ്യം കമ്പനി,\nപിന്നെ അംഗീകാരം", CTA_DPIIT, theme="crm",
 cap_ml="ഗൾഫിലിരുന്ന് സ്റ്റാർട്ടപ്പ് ഇന്ത്യ ഫോം ഇട്ടാൽ കമ്പനി ആകുമെന്ന് കരുതിയോ? DPIIT റെക്കഗ്നിഷൻ നിലവിലുള്ള പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, രജിസ്റ്റേർഡ് പാർട്ണർഷിപ്പ് അല്ലെങ്കിൽ സഹകരണ സംഘത്തിനുള്ള അംഗീകാരമാണ്; കമ്പനി രജിസ്ട്രേഷൻ അല്ല. നിങ്ങൾ ഇപ്പോൾ നാട്ടിലോ ഗൾഫിലോ?",
 cap_en="Filled a Startup India form from the Gulf and thought it created your company? DPIIT recognition is for an existing private limited company, LLP, registered partnership or cooperative society; it does not register a company. Register first, then apply. Where are you now: Kerala or Gulf?",
 cap_mg="Gulf-ilirunnu Startup India form ittaal company aakumennu karuthiyo? DPIIT recognition nilavilulla Pvt Ltd, LLP, registered partnership allenkil sahakarana sanghathinulla angeekaaram aanu; company registration alla. Ningal ippol naattilo Gulf-ilo?")

duo("ud049", "grant_seeker", "A", "weddinghall", "\"അടുത്ത സീസണിൽ\nനോക്കാം\" കമ്പനിക്ക്\n9 വയസ്സ് 8 മാസം", [
 ("A","wide","ശരത്തേ, നമ്മുടെ മടക്കിവെക്കാവുന്ന സ്റ്റേജ് ഫ്രെയിമിന് DPIIT അപേക്ഷ ഇനിയും നീട്ടണോ?"),
 ("V","V","കാവ്യേ, കല്യാണ സീസൺ ഒന്ന് കഴിയട്ടെ. അടുത്ത സീസണിൽ നോക്കാം."),
 ("A","A","കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ട് 9 വർഷവും 8 മാസവും ആയി."),
 ("A","wide","DPIIT-ന് ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷത്തിൽ താഴെ വേണം. അടുത്ത സീസൺ വരുമ്പോൾ നമ്മൾ ആ വര കടന്നിരിക്കും."),
 ("V","V","അപ്പോ ഈ സീസണിൽ തന്നെ അപേക്ഷ."),
 ("A","wide","സീസൺ വീണ്ടും വരും, പത്താം വർഷം വരില്ല.")],
 "സീസൺ വീണ്ടും വരും,\nപത്താം വർഷം വരില്ല", CTA_DPIIT, theme="crm",
 cap_ml="മടക്കിവെക്കാവുന്ന കല്യാണ സ്റ്റേജ് ഫ്രെയിം ഉണ്ടാക്കുന്ന കമ്പനിക്ക് 9 വർഷം 8 മാസം; പാർട്ണർ ഇപ്പോഴും 'അടുത്ത സീസൺ' എന്ന് പറയുന്നു. DPIIT-ന് ഇൻകോർപ്പറേഷൻ മുതൽ 10 വർഷത്തിൽ താഴെ വേണം (ഡീപ് ടെക്കിന് 20), അംഗീകാരം ഉറപ്പുമല്ല. നിങ്ങളുടെ കമ്പനിക്ക് എത്ര വയസ്സായി?",
 cap_en="A wedding-stage company with a new fold-away frame is 9 years and 8 months old, and one partner keeps saying 'next season'. DPIIT recognition needs the company to be under 10 years from incorporation (20 for Deep Tech), and approval is never guaranteed. How old is your company?",
 cap_mg="Madakkivekkaavunna kalyaana stage frame undaakkunna company-kku 9 varsham 8 maasam; partner ippozhum 'adutha season' ennu parayunnu. DPIIT-nu incorporation muthal 10 varshathil thaazhe venam (Deep Tech-nu 20), angeekaaram urappumalla. Ningalude company-kku ethra vayassaayi?")

duo("ud050", "investor_ready", "B", "railway", "\"6 വർഷം ഉറങ്ങിയ\nകമ്പനി. പ്രായം\nപൂജ്യം അല്ലേ?\"", [
 ("A","wide","ദിനേശേ, മുളകൊണ്ടുള്ള സൈക്കിൾ ഫ്രെയിം ഇറക്കിയിട്ട് ഒരു വർഷം. DPIIT-ന് ഇനിയും ഒമ്പത് വർഷം സമയമുണ്ടല്ലോ."),
 ("V","V","ഷീബേ, കമ്പനി ഉണ്ടാക്കിയത് എട്ട് വർഷം മുമ്പല്ലേ? ആറ് വർഷം അത് ഒന്നും ചെയ്യാതെ കിടന്നു."),
 ("A","A","ഉറങ്ങിയ വർഷവും എണ്ണുമോ?"),
 ("V","wide","എണ്ണും. പ്രായം തുടങ്ങുന്നത് ഇൻകോർപ്പറേഷൻ ദിവസം മുതലാ, പ്രോഡക്റ്റ് ഇറങ്ങിയ ദിവസമല്ല. ബാക്കി രണ്ട് വർഷം മാത്രം."),
 ("A","A","എങ്കിൽ ഈ മാസം തന്നെ അപേക്ഷ."),
 ("V","wide","കമ്പനി ഉറങ്ങിയാലും കലണ്ടർ ഉറങ്ങില്ല.")],
 "കമ്പനി ഉറങ്ങിയാലും\nകലണ്ടർ ഉറങ്ങില്ല", CTA_DPIIT, theme="crm",
 cap_ml="എട്ട് വർഷം മുമ്പ് തുടങ്ങിയ കമ്പനി ആറ് വർഷം വെറുതെ കിടന്നു, ഇപ്പോ മുള സൈക്കിൾ ഫ്രെയിം ഇറക്കുന്നു. DPIIT-ന്റെ 10 വർഷം എണ്ണുന്നത് ഇൻകോർപ്പറേഷൻ ദിവസം മുതലാണ്, പ്രോഡക്റ്റ് ഇറങ്ങിയ ദിവസം മുതലല്ല. നിങ്ങളുടെ കമ്പനി എന്നെങ്കിലും വെറുതെ കിടന്നിട്ടുണ്ടോ?",
 cap_en="A company incorporated eight years ago sat idle for six and now makes bamboo bicycle frames. The 10-year window for DPIIT recognition counts from the incorporation date, not from the product launch, so idle years count too. Has your company ever been dormant: yes or no?",
 cap_mg="Ettu varsham munpu thudangiya company aaru varsham veruthe kidannu, ippo mula cycle frame irakkunnu. DPIIT-nte 10 varsham ennunnathu incorporation divasam muthalaanu, product irangiya divasam muthalalla. Ningalude company ennenkilum veruthe kidannittundo?")

duo("ud051", "traditional_innovator", "C", "shop", "\"മുദ്രപ്പത്രത്തിലെ\nപാർട്ണർഷിപ്പ്.\nDPIIT മടങ്ങി\"", [
 ("A","wide","സുരേഷേ, എണ്ണയില്ലാത്ത കണ്ണിമാങ്ങ അച്ചാർ പൗച്ചിന് DPIIT നോക്കിയപ്പോ ഒരു ചോദ്യം: ഫേം രജിസ്റ്റർ ചെയ്തതാണോ?"),
 ("V","V","ബിനൂ, നമ്മുടെ മുദ്രപ്പത്രത്തിലെ പാർട്ണർഷിപ്പ് ഡീഡ് ഉണ്ടല്ലോ. അത് പോരേ?"),
 ("A","A","ഡീഡ് എഴുതി, ഒപ്പിട്ടു. പക്ഷേ ഫേം ഇതുവരെ രജിസ്റ്റർ ചെയ്തിട്ടില്ല."),
 ("A","wide","പാർട്ണർഷിപ്പിന് DPIIT കിട്ടണമെങ്കിൽ അത് രജിസ്റ്റേർഡ് ആയിരിക്കണം. അല്ലെങ്കിൽ കമ്പനിയോ LLP-യോ സഹകരണ സംഘമോ."),
 ("V","V","അപ്പോ ഡീഡ് മാത്രം പോരാ, രജിസ്ട്രേഷനും വേണം."),
 ("A","wide","അച്ചാറിന് ഉപ്പ്, ഫേമിന് രജിസ്ട്രേഷൻ.")],
 "അച്ചാറിന് ഉപ്പ്,\nഫേമിന് രജിസ്ട്രേഷൻ", CTA_DPIIT, theme="crm",
 cap_ml="രണ്ട് സഹോദരന്മാരുടെ എണ്ണയില്ലാത്ത അച്ചാർ ബിസിനസ് മുദ്രപ്പത്രത്തിലെ ഡീഡിൽ മാത്രം; ഫേം രജിസ്റ്റർ ചെയ്തിട്ടില്ല. DPIIT-ന് പാർട്ണർഷിപ്പ് രജിസ്റ്റേർഡ് ആയിരിക്കണം; പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP, സഹകരണ സംഘം എന്നിവയും പറ്റും. നിങ്ങളുടെ ഫേം രജിസ്റ്റേർഡ് ആണോ?",
 cap_en="Two brothers run an oil-free pickle business on a stamp-paper partnership deed, but the firm was never registered. For DPIIT recognition a partnership must be a registered firm; a private limited company, LLP or cooperative society also qualifies. Is your firm registered: yes or no?",
 cap_mg="Randu sahodaranmaarude ennayillaatha achaar business mudrappathrathile deed-il maathram; firm register cheythittilla. DPIIT-nu partnership registered aayirikkanam; Pvt Ltd, LLP, sahakarana sangham ennivayum pattum. Ningalude firm registered aano?")

duo("ud052", "investor_ready", "A", "mall", "ഒരു വർഷം 210 കോടി.\nഇപ്പോ 160.\n\"ഇനി DPIIT ആകാമോ?\"", [
 ("A","wide","ജാഫറേ, ആ വലിയ റോഡ് ഓർഡർ വന്ന വർഷം നമ്മുടെ കയർ ജിയോടെക്സ്റ്റൈൽ കമ്പനി 210 കോടി കടന്നു."),
 ("V","V","സുമയ്യാ, ഈ വർഷം 160 അല്ലേ ഉള്ളൂ? 200-ന് താഴെ. ഇനി DPIIT-ന് അപേക്ഷിക്കാം."),
 ("A","A","നോക്കുന്നത് ഈ വർഷം മാത്രമല്ല."),
 ("A","wide","തുടങ്ങിയത് മുതൽ ഒരു വർഷവും 200 കോടി കടന്നിട്ടുണ്ടാകരുത്. ഡീപ് ടെക്കിന് 300 കോടി."),
 ("V","V","ഒരു നല്ല വർഷം മതിയായിരുന്നു, വാതിൽ അടയാൻ."),
 ("A","wide","ടേൺഓവർ താഴും, റെക്കോർഡ് താഴില്ല.")],
 "ടേൺഓവർ താഴും,\nറെക്കോർഡ് താഴില്ല", CTA_DPIIT, theme="faq",
 cap_ml="ഒരു വലിയ ഓർഡർ കാരണം ഒരു വർഷം 210 കോടി; ഇപ്പോ 160. ഇനി DPIIT കിട്ടുമെന്ന് കരുതിയോ? 2026 ഫെബ്രുവരി 4-ലെ നോട്ടിഫിക്കേഷൻ പ്രകാരം ഒരു വർഷവും ടേൺഓവർ 200 കോടി (ഡീപ് ടെക്കിന് 300) കടന്നിട്ടുണ്ടാകരുത്. നിങ്ങളുടെ ഏറ്റവും വലിയ വർഷം ഏതായിരുന്നു?",
 cap_en="A coir geotextile company crossed 210 crore in one bumper year and is back at 160 crore now. DPIIT recognition needs turnover never above 200 crore in any year since incorporation (300 crore for Deep Tech), under the 4 Feb 2026 notification, so this year alone does not decide it. Which was your biggest year?",
 cap_mg="Oru valiya order kaaranam oru varsham 210 crore; ippo 160. Ini DPIIT kittumennu karuthiyo? 2026 February 4-le notification prakaaram oru varshavum turnover 200 crore (Deep Tech-nu 300) kadannittundaakaruthu. Ningalude ettavum valiya varsham ethaayirunnu?")

duo("ud053", "traditional_innovator", "B", "canteen", "\"പേറ്റന്റ് ഇല്ല.\nഅപ്പോ DPIIT-ഉം\nഇല്ലല്ലോ?\"", [
 ("A","wide","അമലേ, ഇളനീർ ചെത്തി തുളയിടുന്ന നമ്മുടെ മെഷീന് പേറ്റന്റ് കിട്ടിയിട്ടില്ല. DPIIT അത് കഴിഞ്ഞ് നോക്കാം."),
 ("V","V","ആതിരേ, DPIIT-ന് പേറ്റന്റ് വേണമെന്ന് ആരാ പറഞ്ഞത്?"),
 ("A","A","സ്റ്റാർട്ടപ്പ് എന്നാൽ പേറ്റന്റ് അല്ലേ?"),
 ("V","wide","നോക്കുന്നത് പ്രോഡക്റ്റിലോ പ്രോസസിലോ ഉള്ള പുതുമ, അല്ലെങ്കിൽ വളരാവുന്ന മോഡൽ. പേറ്റന്റ് ഒരു നിബന്ധനയല്ല."),
 ("A","A","അപ്പോ ഇത്രയും കാലം വെറുതെ കാത്തിരുന്നു."),
 ("V","wide","ഇളനീരിന് തുള മതി, DPIIT-ന് പുതുമ മതി.")],
 "ഇളനീരിന് തുള മതി,\nDPIIT-ന് പുതുമ മതി", CTA_DPIIT, theme="faq",
 cap_ml="ഇളനീർ ചെത്തി തുളയിടുന്ന മെഷീന് പേറ്റന്റ് കിട്ടുംവരെ DPIIT അപേക്ഷ മാറ്റിവെച്ചു. DPIIT നോക്കുന്നത് പ്രോഡക്റ്റിലോ പ്രോസസിലോ ഉള്ള പുതുമ, അല്ലെങ്കിൽ വളരാവുന്ന മോഡൽ; പേറ്റന്റ് നിർബന്ധമല്ല, അംഗീകാരം ഉറപ്പുമല്ല. നിങ്ങൾ എന്തിനായി കാത്തിരിക്കുന്നു?",
 cap_en="A tender-coconut cutting machine maker put off DPIIT recognition until a patent came through. Recognition looks at innovation or improvement of a product or process, or a scalable business model; a patent is not a condition, and approval is never guaranteed. What are you waiting for?",
 cap_mg="Ilaneer chethi thulayidunna machine-nu patent kittumvare DPIIT apeksha maattivechu. DPIIT nokkunnathu product-ilo process-ilo ulla puthuma, allenkil valaraavunna model; patent nirbandhamalla, angeekaaram urappumalla. Ningal enthinaayi kaathirikkunnu?")

duo("ud054", "traditional_innovator", "C", "teashop", "\"DPIIT കിട്ടി.\nഇനി തൊഴിൽ നിയമം\nബാധകമല്ല\"", [
 ("A","wide","വിഷ്ണൂ, നിന്റെ ഫൈബർ വള്ളം യാർഡിൽ ഇപ്പോ മുപ്പത് പണിക്കാരില്ലേ? അവരുടെ രേഖകൾ ഒക്കെ ശരിയാണോ?"),
 ("V","V","അനൂ, DPIIT കിട്ടിയില്ലേ? ഇനി തൊഴിൽ നിയമമൊന്നും നമുക്ക് ബാധകമല്ല."),
 ("A","A","അങ്ങനെ ആരാ പറഞ്ഞത്?"),
 ("A","wide","ചില തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ സ്വയം സാക്ഷ്യപ്പെടുത്താം എന്നേ ഉള്ളൂ. നിയമം പാലിക്കണം, ഒപ്പിടുന്നത് നീ തന്നെ."),
 ("V","V","അപ്പോ ഉത്തരവാദിത്തം കൂടി, കുറഞ്ഞില്ല."),
 ("A","wide","വള്ളം പുതിയത്, കടമ പഴയത്.")],
 "വള്ളം പുതിയത്,\nകടമ പഴയത്", CTA_BENEFITS, theme="faq",
 cap_ml="ഫൈബർ വള്ളം നിർമ്മിക്കുന്ന യാർഡിന് DPIIT കിട്ടിയപ്പോൾ തൊഴിൽ നിയമങ്ങൾ ഇനി ബാധകമല്ലെന്ന് ഉടമ കരുതി. റെക്കഗ്നിഷൻ കൊണ്ട് ചില തൊഴിൽ, പരിസ്ഥിതി നിയമങ്ങളിൽ സ്വയം സാക്ഷ്യപ്പെടുത്താം; നിയമം പാലിക്കൽ ഒഴിവാകില്ല. നിങ്ങളുടെ ടീമിൽ എത്ര പേരുണ്ട്?",
 cap_en="A fibre-boat yard got DPIIT recognition and the owner thought labour laws no longer applied. Recognition allows self-certification under some labour and environment laws; the laws still apply and the founder signs for compliance. How many people are on your team?",
 cap_mg="Fibre vallam nirmmikkunna yard-inu DPIIT kittiyappol thozhil niyamangal ini baadhakamallennu udama karuthi. Recognition kondu chila thozhil, paristhithi niyamangalil swayam saakshyappeduthaam; niyamam paalikkal ozhivaakilla. Ningalude team-il ethra perundu?")

duo("ud055", "student_founder", "A", "photocopy", "ഇൻകുബേറ്റർ കത്ത്,\nപത്ത് കോപ്പി.\n\"ഇതാണ് DPIIT\"", [
 ("A","wide","ഉണ്ണീ, കോളേജ് ഇൻകുബേറ്ററിന്റെ കത്തിന് പത്ത് കോപ്പി എന്തിനാ?"),
 ("V","V","അശ്വതീ, ഗ്രാന്റ് ഫോമിൽ DPIIT നമ്പർ ചോദിക്കുന്നു. ഈ കത്ത് തന്നെയല്ലേ സ്റ്റാർട്ടപ്പ് സർട്ടിഫിക്കറ്റ്?"),
 ("A","A","അല്ല. അത് കോളേജ് നിങ്ങളെ ഇൻകുബേറ്ററിൽ എടുത്തു എന്ന കത്താ."),
 ("A","wide","DPIIT റെക്കഗ്നിഷൻ വേറെ അപേക്ഷയാ. അതിന് ആദ്യം പ്രൈവറ്റ് ലിമിറ്റഡോ LLP-യോ പോലൊരു ഘടന വേണം."),
 ("V","V","ഞങ്ങൾക്ക് ഇതുവരെ കമ്പനി പോലും ഇല്ല."),
 ("A","wide","കോപ്പി കൂട്ടിയാൽ ഒറിജിനൽ ആകില്ല.")],
 "കോപ്പി കൂട്ടിയാൽ\nഒറിജിനൽ ആകില്ല", CTA_DPIIT, theme="faq",
 cap_ml="കോളേജ് ഇൻകുബേറ്ററിന്റെ കത്ത് DPIIT സർട്ടിഫിക്കറ്റ് ആണെന്ന് കരുതി ഗ്രാന്റ് ഫോമിന് കോപ്പി എടുത്ത വിദ്യാർത്ഥി ടീം. DPIIT റെക്കഗ്നിഷൻ വേറെ അപേക്ഷയാണ്, അതിന് പ്രൈവറ്റ് ലിമിറ്റഡ്, LLP പോലൊരു ഘടന ആദ്യം വേണം. നിങ്ങൾ ഇൻകുബേറ്ററിലാണോ?",
 cap_en="A student team photocopied their college incubator's letter, thinking it was their DPIIT certificate for a grant form. DPIIT recognition is a separate application, and it first needs an eligible structure such as a private limited company or LLP. Are you in an incubator: yes or no?",
 cap_mg="College incubator-inte kathu DPIIT certificate aanennu karuthi grant form-inu copy edutha vidyaarthi team. DPIIT recognition vere apekshayaanu, athinu Pvt Ltd, LLP poloru ghadana aadyam venam. Ningal incubator-ilaano?")

duo("ud056", "tech_founder", "B", "courier", "\"ടാക്സ് ഹോളിഡേ\nകിട്ടി. ഇനി GST\nബില്ല് വേണ്ട\"", [
 ("A","wide","അരവിന്ദേ, ഉത്സവത്തിന്റെ ഡ്രോൺ ഷോ കഴിഞ്ഞ് അയച്ച ബില്ലിൽ GST ഇല്ലല്ലോ. എന്ത് പറ്റി?"),
 ("V","V","ജയേ, നമ്മുടെ 80-IAC ടാക്സ് ഹോളിഡേ അപേക്ഷ ബോർഡ് അംഗീകരിച്ചില്ലേ? ഇനി ടാക്സ് ഒന്നുമില്ല."),
 ("A","A","ആ അവധി ഏത് ടാക്സിനാ എന്ന് വായിച്ചോ?"),
 ("A","wide","80-IAC മൂന്ന് തുടർച്ചയായ വർഷത്തെ ലാഭത്തിന്മേലുള്ള ഇൻകം ടാക്സിനാ. ബില്ലിലെ GST അതിൽ പെടില്ല."),
 ("V","V","അപ്പോ ബില്ല് വീണ്ടും ഉണ്ടാക്കണം."),
 ("A","wide","ലാഭത്തിനാ അവധി, ബില്ലിനല്ല.")],
 "ലാഭത്തിനാ അവധി,\nബില്ലിനല്ല", CTA_BENEFITS, theme="new",
 cap_ml="ഉത്സവങ്ങൾക്ക് ഡ്രോൺ ഷോ നടത്തുന്ന കമ്പനിക്ക് 80-IAC ടാക്സ് ഹോളിഡേ കിട്ടിയപ്പോൾ ബില്ലിൽ നിന്ന് GST ഒഴിവാക്കി. 80-IAC ആദ്യ 10 വർഷത്തിൽ തുടർച്ചയായ 3 വർഷത്തെ ലാഭത്തിനുള്ള ഇൻകം ടാക്സ് ഇളവാണ്, ഇന്റർ-മിനിസ്റ്റീരിയൽ ബോർഡ് അംഗീകരിക്കേണ്ട വേറെ അപേക്ഷ; GST അതിൽ പെടില്ല. നിങ്ങൾ 80-IAC-ന് അപേക്ഷിച്ചോ?",
 cap_en="A festival drone-show company got its 80-IAC tax holiday approved and dropped GST from its invoices. Section 80-IAC covers 100% of profits for 3 consecutive years out of the first 10, as a separate application approved by the Inter-Ministerial Board; it is income tax, not GST. Have you applied for 80-IAC: yes or no?",
 cap_mg="Ulsavangalkku drone show nadathunna company-kku 80-IAC tax holiday kittiyappol bill-il ninnu GST ozhivaakki. 80-IAC aadya 10 varshathil thudarchayaaya 3 varshathe laabhathinulla income tax ilavaanu, Inter-Ministerial Board angeekarikkenda vere apeksha; GST athil pedilla. Ningal 80-IAC-nu apekshicho?")

duo("ud057", "traditional_innovator", "A", "veranda", "\"62 വയസ്സായി.\nഇനി എനിക്ക്\nസ്റ്റാർട്ടപ്പോ?\"", [
 ("A","wide","ബാലേട്ടാ, പപ്പടം പരത്തുന്ന ആ യന്ത്രം നാല് കടകളിൽ ഓടുന്നുണ്ടല്ലോ. എന്തേ DPIIT നോക്കാത്തത്?"),
 ("V","V","ശാന്തേ, അറുപത്തിരണ്ട് വയസ്സായി. സ്റ്റാർട്ടപ്പ് ഒക്കെ പിള്ളേർക്കുള്ളതല്ലേ?"),
 ("A","A","DPIIT നോക്കുന്നത് ആരുടെ പ്രായമാ എന്നറിയാമോ?"),
 ("A","wide","കമ്പനിയുടെ പ്രായം: 10 വർഷത്തിൽ താഴെ. പിന്നെ പ്രോസസിലെ പുതുമ. ഫൗണ്ടറുടെ പ്രായം ചോദിക്കുന്നില്ല."),
 ("V","V","എങ്കിൽ ആദ്യം യന്ത്രത്തിന് ഒരു കമ്പനി."),
 ("A","wide","പ്രായം കമ്പനിക്ക്, ചെറുപ്പം ഐഡിയയ്ക്ക്.")],
 "പ്രായം കമ്പനിക്ക്,\nചെറുപ്പം ഐഡിയയ്ക്ക്", CTA_DPIIT, theme="new",
 cap_ml="62-ാം വയസ്സിൽ പപ്പടം പരത്തുന്ന യന്ത്രം ഉണ്ടാക്കി, പക്ഷേ സ്റ്റാർട്ടപ്പ് ചെറുപ്പക്കാർക്ക് മാത്രമെന്ന് കരുതി. DPIIT നോക്കുന്നത് കമ്പനിയുടെ പ്രായവും (10 വർഷത്തിൽ താഴെ) ഘടനയും പുതുമയുമാണ്, ഫൗണ്ടറുടെ പ്രായമല്ല; അംഗീകാരം ഉറപ്പുമല്ല. നിങ്ങളുടെ വീട്ടിലുണ്ടോ ഇങ്ങനെ ഒരു ഇന്നൊവേറ്റർ?",
 cap_en="At 62 he built a pappadam-pressing machine that now runs in four shops, but thought startups are only for the young. DPIIT recognition looks at the company's age (under 10 years), its structure and its innovation, not the founder's age, and approval is never guaranteed. Is there an innovator like this in your family?",
 cap_mg="62-aam vayassil pappadam parathunna yanthram undaakki, pakshe startup cheruppakkaarkku maathramennu karuthi. DPIIT nokkunnathu company-yude praayavum (10 varshathil thaazhe) ghadanayum puthumayumaanu, founder-ude praayamalla; angeekaaram urappumalla. Ningalude veettilundo ingane oru innovator?")
