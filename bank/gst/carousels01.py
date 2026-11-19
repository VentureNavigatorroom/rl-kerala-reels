# GST seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
car("gk001", "trader", "GST ചെക്ക്", "നിങ്ങൾക്ക് GST\nവേണോ? 4 സ്ലൈഡിൽ\nഉത്തരം", [
 ("ടേൺഓവർ", "സാധനങ്ങൾക്ക് വർഷം 40 ലക്ഷം, സർവീസിന് 20 ലക്ഷം കടന്നാൽ നിർബന്ധം."),
 ("മറ്റ് സംസ്ഥാനം", "സാധനം കേരളത്തിന് പുറത്ത് വിൽക്കുന്നെങ്കിൽ ആദ്യ വിൽപ്പന മുതൽ."),
 ("സ്വമേധയാ", "ലിമിറ്റിൽ താഴെയും എടുക്കാം. വലിയ ബയർമാർ GSTIN ചോദിക്കും."),
 ("ഡോക്യുമെന്റ്", "പാൻ, ആധാർ, ഫോട്ടോ, അഡ്രസ്സ് പ്രൂഫ്, ബാങ്ക് ഡീറ്റെയിൽസ്.")],
 "സംശയം ബാക്കിയുണ്ടോ?", topics.CTA_GST,
 cap_ml="GST രജിസ്ട്രേഷൻ വേണോ എന്ന് നാല് സ്ലൈഡിൽ: ടേൺഓവർ ലിമിറ്റ് 40 ലക്ഷം, 20 ലക്ഷം; മറ്റ് സംസ്ഥാനത്തേക്ക് വിൽപ്പന; സ്വമേധയാ രജിസ്ട്രേഷൻ; ആവശ്യമായ ഡോക്യുമെന്റുകൾ.",
 cap_en="Do you need GST registration in Kerala? Turnover limits (Rs 40 lakh goods, Rs 20 lakh services), selling to other states, voluntary registration and the documents you need, in four slides.",
 cap_mg="GST registration veno ennu 4 slide-il: turnover limit 40 lakh, 20 lakh; other state sales; voluntary registration; documents.")
car("gk002", "service_pro", "പിഴ", "GST വൈകിയാൽ\nവരുന്ന 3 ചെലവ്", [
 ("ടാക്സ്", "പിരിക്കേണ്ടിയിരുന്ന ടാക്സ് സ്വന്തം കയ്യിൽ നിന്ന്."),
 ("പലിശ", "വർഷം 18% പലിശ."),
 ("പിഴ", "10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10%, ഏതാണോ കൂടുതൽ."),
 ("റിട്ടേൺ", "രജിസ്റ്റർ ചെയ്ത ശേഷം വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ.")],
 "വൈകും മുമ്പ്\nരജിസ്റ്റർ ചെയ്യൂ", topics.CTA_PENALTY,
 cap_ml="GST രജിസ്ട്രേഷൻ വൈകിയാൽ: ടാക്സ്, 18% പലിശ, 10,000 അല്ലെങ്കിൽ ടാക്സിന്റെ 10% പിഴ. രജിസ്റ്റർ ചെയ്ത ശേഷം വിൽപ്പന ഇല്ലാത്ത മാസവും നിൽ റിട്ടേൺ വേണം.",
 cap_en="What a late GST registration costs: the tax itself, 18% interest and a penalty of Rs 10,000 or 10% of the tax. After registering, nil returns are due even in months with no sales.",
 cap_mg="GST registration vaikiyaal: tax, 18% interest, 10,000 allenkil tax-inte 10% penalty. Register cheytha shesham sales illaatha maasavum nil return.")
