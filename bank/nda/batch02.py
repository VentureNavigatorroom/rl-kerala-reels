# NDA batch 02 (19 Nov run). Short scripts (max 6 lines) that open on the painful moment; payoff by line 4-5, then a short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_NDA. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_NDA, CTA_SECRET = topics.CTA_NDA, topics.CTA_SECRET

duo("nd002", "agency_client", "B", "photocopy", "ക്ലയന്റിന് 3 ഡിസൈൻ\nഅയച്ചു. ഒന്ന് വേറെ\nഏജൻസിയുടെ പേരിൽ", [
 ("A","wide","ഉണ്ണി, ആ റിസോർട്ടിന് നമ്മൾ അയച്ച 3 ബ്രോഷർ ഡിസൈനിൽ ഒന്ന് ഇപ്പോ വേറെ ഏജൻസിയുടെ പേരിൽ പ്രിന്റ് ആയി!"),
 ("V","V","അവരുമായി എന്തെങ്കിലും എഗ്രിമെന്റ് ഉണ്ടായിരുന്നോ?"),
 ("A","A","ഇല്ല. വാട്സ്ആപ്പിൽ അയച്ചു, അത്രേ."),
 ("V","wide","അതാ പ്രശ്നം. ഷെയർ ചെയ്യും മുമ്പ് NDA, സ്റ്റാമ്പ് നിയമപ്രകാരം. എന്താണ് രഹസ്യം, എത്ര കാലം, ലംഘിച്ചാൽ എന്ത്, എല്ലാം എഴുതണം."),
 ("A","A","ഇനി ഡ്രാഫ്റ്റ് അയക്കും മുമ്പ് NDA. ഉറപ്പ്."),
 ("V","wide","ഡിസൈൻ നമ്മുടേത്. തെളിവും നമ്മുടെ കയ്യിൽ വേണം.")],
 "ഡ്രാഫ്റ്റ് അയക്കും\nമുമ്പ് NDA", CTA_NDA, theme="crm",
 cap_ml="ക്ലയന്റിന് അയച്ച ഡിസൈൻ വേറെ ഏജൻസിയുടെ പേരിൽ പ്രിന്റ് ആയി. ഷെയർ ചെയ്യും മുമ്പ് ശരിയായി തയ്യാറാക്കി സ്റ്റാമ്പ് ചെയ്ത NDA: രഹസ്യ വിവരം, കാലാവധി, ലംഘിച്ചാലുള്ള പരിഹാരം എല്ലാം എഴുതണം.",
 cap_en="A small design agency sent three brochure drafts on WhatsApp, and one turned up under another agency's name. Before sharing work, sign an NDA drafted and stamped under the state's stamp law, defining what is confidential, for how long, and the remedies.",
 cap_mg="Client-nu ayacha design vere agency-yude peril print aayi. Share cheyyum munpu shariyaayi thayyaaraakki stamp cheytha NDA: rahasya vivaram, kaalaavadhi, remedies ellaam ezhuthanam.")