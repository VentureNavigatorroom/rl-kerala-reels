# Tips and tricks 03 (20 Nov, writer run): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.FACTS_SK.
# Never state grant amounts or promise selection.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_KSUM, CTA_GRANT = topics.CTA_KSUM, topics.CTA_GRANT

lst('mt011', 'idea_stage', "B", 'ഗ്രൂപ്പിൽ വന്ന\nKSUM മെസേജ്:\nഫോർവേഡ് മുമ്പ് 3 ചെക്ക്', [('"ഗ്രാന്റ് തുക ഇത്ര"', 'തുകയും കോളും മാറും. KSUM-ന്റെ ലൈവ് കോൾ നോക്കൂ.'), ('"സെലക്ഷൻ ഉറപ്പ്"', 'ആർക്കും ഉറപ്പില്ല. അങ്ങനെ പറയുന്നത് വിശ്വസിക്കരുത്.'), ('"ലിങ്കിൽ അപേക്ഷിക്കൂ"', 'അപേക്ഷ KSUM-ന്റെ സ്വന്തം സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ.')],
 'ഫോർവേഡ് ചെയ്യും മുമ്പ്\nഒന്ന് ചെക്ക് ചെയ്യൂ', CTA_GRANT, theme="tip",
 cap_ml='KSUM ഗ്രാന്റിനെക്കുറിച്ച് വാട്ട്സ്ആപ്പിൽ വരുന്ന മെസേജ് ഫോർവേഡ് ചെയ്യും മുമ്പ് 3 കാര്യം നോക്കൂ: തുകയും കോളും മാറും, സെലക്ഷൻ ആർക്കും ഉറപ്പില്ല, അപേക്ഷ KSUM-ന്റെ സ്വന്തം സ്റ്റാർട്ടപ്പ് പോർട്ടലിൽ. ഇങ്ങനെ ഒരു മെസേജ് കിട്ടിയിട്ടുണ്ടോ?',
 cap_en='Before you forward that KSUM grant message in your group, check 3 things: amounts and calls change, so read the live call; nobody can guarantee selection; and applications go through KSUM\'s own startup portal. Ever received a message like this: yes or no?',
 cap_mg='KSUM grant-ine kurichu WhatsApp-il varunna message forward cheyyum mumpu 3 kaaryam nokkoo: thukayum call-um maarum, selection aarkkum urappilla, apeksha KSUM-inte swantham startup portal-il. Ingane oru message kittiyittundo?')
