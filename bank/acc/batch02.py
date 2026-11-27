# acc batch 02 (27 Nov evening refill): 3D duo reel. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns. Facts only from topics.FACTS_ACC + the verified GSTR-3B late fees in topics.FACTS_GST. No fixed due dates, no tax amounts, no fees of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ITR, CTA_ACCOUNTS = topics.CTA_ITR, topics.CTA_ACCOUNTS

# faq: a tour-taxi owner skipped nil returns in the monsoon months, thinking a nil return has no late fee
duo("acd006", "nil_filer", "B", "autostand", "മഴക്കാലം, ഓട്ടമില്ല.\nനിൽ റിട്ടേൺ വൈകി.\n\"അതിന് പിഴയില്ലല്ലോ\"", [
 ("A","wide","ഷാജീ, മഴക്കാലത്ത് ടൂർ ഓട്ടം ഇല്ലാത്ത മാസങ്ങളിലെ GST റിട്ടേൺ ഇട്ടോ?"),
 ("V","V","സജീ, ഒരു രൂപ വരവില്ല. നിൽ റിട്ടേൺ വൈകിയാൽ ആർക്കാ നഷ്ടം?"),
 ("A","A","നിനക്ക് തന്നെ. നിൽ ആയ GSTR-3B വൈകിയാലും ദിവസം 20 രൂപ ലേറ്റ് ഫീ. ഒരു റിട്ടേണിന് 500 രൂപ വരെ."),
 ("V","V","മൂന്ന് മാസം ബാക്കി. ഇന്ന് തന്നെ മൂന്നും ഫയൽ ചെയ്യാം."),
 ("A","wide","വരവില്ലാത്ത മാസത്തിനും ഒരു റിട്ടേൺ.")],
 "നിൽ റിട്ടേണും\nവൈകിയാൽ ലേറ്റ് ഫീ", CTA_ITR, theme="faq",
 cap_ml="വരുമാനം ഇല്ലാത്ത മാസത്തെ നിൽ GST റിട്ടേൺ വൈകിയാൽ ഒന്നുമില്ല എന്ന് കരുതിയോ? നിൽ GSTR-3B വൈകിയാലും ദിവസം 20 രൂപ ലേറ്റ് ഫീ, ഒരു റിട്ടേണിന് 500 രൂപ വരെ. ബാക്കിയുള്ളത് ഇന്ന് തന്നെ ഫയൽ ചെയ്യൂ. നിങ്ങൾക്ക് എത്ര നിൽ റിട്ടേൺ ബാക്കിയുണ്ട്?",
 cap_en="A tour-taxi owner skipped his nil GST returns for the monsoon months with no trips. A late nil GSTR-3B still carries a late fee of 20 rupees a day, up to 500 rupees per return. File the pending ones today. How many nil returns are pending for you?",
 cap_mg="Varumaanam illaatha maasathe nil GST return vaikiyaal onnumilla ennu karuthiyo? Nil GSTR-3B vaikiyaalum divasam 20 rupees late fee, oru return-inu 500 rupees vare. Baakkiyullathu innu thanne file cheyyu. Ningalkku ethra nil return baakkiyundu?")
