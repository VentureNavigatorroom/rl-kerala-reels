# Tips and tricks 04 for gst (28 Nov night): tips written as duo3d scenes, not lists (26 Nov review). theme="tip". Facts only from topics.FACTS_GST. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_GST, CTA_LIMIT, CTA_PENALTY = topics.CTA_GST, topics.CTA_LIMIT, topics.CTA_PENALTY

# tip: how long GST approval takes, three answers (plan the application before the order)
duo("gt102", "new_company", "B", "juiceshop", "GST അപ്രൂവൽ\n3 ദിവസമോ 30 ദിവസമോ?\nമൂന്ന് ഉത്തരം", [
 ("A","wide","നൗഷാദിക്കാ, GST അപ്രൂവലിന് എത്ര ദിവസം എന്ന് ചോദിച്ചാൽ മൂന്ന് ഉത്തരം ഉണ്ട്."),
 ("A","A","ഒന്ന്: ലോ-റിസ്ക് അപേക്ഷയ്ക്ക് 2025 നവംബർ 1 മുതൽ 3 പ്രവൃത്തി ദിവസത്തിനകം ഓട്ടോ അപ്രൂവൽ."),
 ("V","V","രണ്ട്: അല്ലാത്തവയ്ക്ക് 7 പ്രവൃത്തി ദിവസം. മൂന്ന്: സ്ഥലം നേരിട്ട് പരിശോധിക്കണമെങ്കിൽ 30 ദിവസം വരെ."),
 ("A","A","ഇതിൽ ഏതാണ് നിങ്ങളുടേത് എന്ന് മുൻകൂട്ടി അറിയില്ല. അതുകൊണ്ട് ഓർഡർ വരും മുമ്പ് അപേക്ഷിക്കൂ."),
 ("V","wide","മൂന്ന് ദിവസം പ്രതീക്ഷിക്കാം. മുപ്പത് ദിവസം പ്ലാൻ ചെയ്യണം.")],
 "3 ദിവസം പ്രതീക്ഷ,\n30 ദിവസം പ്ലാൻ", CTA_GST, theme="tip",
 cap_ml="GST അപ്രൂവൽ: 2025 നവംബർ 1 മുതൽ ലോ-റിസ്ക് അപേക്ഷകൾക്ക് 3 പ്രവൃത്തി ദിവസത്തിനകം ഓട്ടോ അപ്രൂവൽ, മറ്റുള്ളവയ്ക്ക് 7 പ്രവൃത്തി ദിവസം, നേരിട്ടുള്ള പരിശോധന വേണ്ടിവന്നാൽ 30 ദിവസം വരെ. വലിയ ഓർഡർ വരും മുമ്പ് അപേക്ഷിക്കൂ. ഓർഡർ കാത്തിരിക്കുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="GST approval: since 1 November 2025 low-risk applications are auto-approved within 3 working days; others take 7 working days, and up to 30 days if physical verification is needed. You can't know in advance which one you'll get, so apply before the big order arrives. Send this to someone waiting on an order.",
 cap_mg="GST approval: 2025 November 1 muthal low-risk apekshakalkku 3 working days-inakam auto approval, mattullavaykku 7 working days, nerittulla parishodhana vendivannaal 30 divasam vare. Valiya order varum mumpu apekshikku. Order kaathirikkunna oraalkku ithu ayakku.")

# tip: what a REG-04 reply can and cannot carry
duo("gt103", "new_company", "B", "photocopy", "GST ചോദ്യത്തിന്\nമറുപടി: എന്ത് മാറ്റാം,\nഎന്ത് പറ്റില്ല", [
 ("A","wide","ഉണ്ണീ, GST അപേക്ഷയ്ക്ക് REG-03 വന്നാൽ REG-04-ൽ എന്ത് കൊടുക്കാം എന്ന് ഒറ്റ നോട്ടത്തിൽ."),
 ("A","A","കൊടുക്കാവുന്നത്: ചോദിച്ച രേഖകൾ, വിശദീകരണം. 7 പ്രവൃത്തി ദിവസത്തിനകം."),
 ("V","V","ഈ വഴി മാറ്റാൻ പറ്റാത്തത്: PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ. അത് അപേക്ഷിക്കും മുമ്പ് ശരിയാക്കണം."),
 ("A","A","മറുപടി കിട്ടിയാൽ ഓഫീസർ 7 പ്രവൃത്തി ദിവസത്തിനകം തീരുമാനിക്കും."),
 ("V","wide","രേഖ മാറ്റാം. PAN മാറ്റാൻ പറ്റില്ല.")],
 "രേഖ മാറ്റാം,\nPAN മാറ്റാൻ പറ്റില്ല", CTA_GST, theme="tip",
 cap_ml="GST REG-04 മറുപടിയിൽ ചോദിച്ച രേഖകളും വിശദീകരണവും 7 പ്രവൃത്തി ദിവസത്തിനകം കൊടുക്കാം. PAN, സംസ്ഥാനം, മൊബൈൽ, ഇമെയിൽ ഈ വഴി മാറ്റാൻ പറ്റില്ല, അതുകൊണ്ട് അപേക്ഷിക്കും മുമ്പ് ഒത്തുനോക്കൂ. GST അപേക്ഷിക്കാൻ പോകുന്ന ഒരാൾക്ക് ഇത് അയക്കൂ.",
 cap_en="A REG-04 reply to a GST query can carry the documents and clarification asked, within 7 working days. PAN, State, mobile and e-mail cannot be changed this way, so check them before you apply. Send this to someone about to apply for GST.",
 cap_mg="GST REG-04 marupadiyil chodicha rekhakalum vishadeekaranavum 7 working days-inakam kodukkaam. PAN, State, mobile, email ee vazhi maattaan pattilla, athukondu apekshikkum mumpu othunokku. GST apekshikkaan pokunna oraalkku ithu ayakku.")

# tip: which penalty applies when you register late: 10% of the tax only once the tax is above 1 lakh
duo("gt104", "trader", "B", "petrolpump", "വൈകി രജിസ്റ്റർ ചെയ്താൽ\nപിഴ 10,000 ആണോ 10%?\nഒരു എളുപ്പവഴി", [
 ("A","wide","ഷിബൂ, ലിമിറ്റ് കടന്നിട്ടും GST എടുക്കാതിരുന്നാൽ പിഴ എത്ര എന്ന് ഒരു എളുപ്പവഴി."),
 ("A","A","നിയമം: 10,000 രൂപ അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ."),
 ("V","V","ടാക്സ് 1 ലക്ഷം രൂപ വരെ ആണെങ്കിൽ 10% പതിനായിരത്തിൽ താഴെ. അപ്പോ പിഴ 10,000."),
 ("A","A","ടാക്സ് അതിന് മുകളിലാണെങ്കിൽ 10%. കൂടെ ടാക്സും 18% പലിശയും."),
 ("V","wide","ഒരു ലക്ഷം വരെ പതിനായിരം. അതിന് മുകളിൽ പത്ത് ശതമാനം.")],
 "ഏതാണോ കൂടുതൽ,\nഅതാണ് പിഴ", CTA_PENALTY, theme="tip",
 cap_ml="GST ലിമിറ്റ് കടന്നിട്ടും രജിസ്റ്റർ ചെയ്യാതിരുന്നാൽ ടാക്സ്, 18% പലിശ, പിന്നെ 10,000 രൂപ അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ. ടാക്സ് 1 ലക്ഷം രൂപ വരെ ആണെങ്കിൽ പിഴ 10,000; അതിന് മുകളിൽ 10%. ഈ കണക്ക് ഒരു കൂട്ടുകാരന് അയക്കൂ.",
 cap_en="Crossed the GST limit and didn't register? You pay the tax, 18% interest, and a penalty of 10,000 or 10% of the tax due, whichever is higher. With tax up to 1 lakh the penalty is 10,000; above that, 10%. Send this quick rule to a friend.",
 cap_mg="GST limit kadannittum register cheyyaathirunnaal tax, 18% palisha, pinne 10,000 roopa allenkil tax-inte 10%, ethaano kooduthal. Tax 1 lakh roopa vare aanenkil pizha 10,000; athinu mukalil 10%. Ee kanakku oru koottukaaranu ayakku.")
