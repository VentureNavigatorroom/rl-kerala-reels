# Investor agreements seed carousels/stories (20 Nov). Facts only from topics.py; no prices; anonymised situations only.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
tip("vt001", "cofounder_split", "ഷെയർ വീതിക്കും\nമുമ്പ്", "വെസ്റ്റിംഗ് എഴുതി വെക്കൂ. കോ-ഫൗണ്ടർ പോയാലും ഷെയർ മുഴുവൻ പോകില്ല.")
tip("vt002", "family_money", "വീട്ടുകാരുടെ\nപൈസയും", "ഇൻവെസ്റ്റ്മെന്റ് തന്നെ. കടമോ ഷെയറോ എന്ന് എഴുതി വെക്കൂ.")
quiz("vq001", "founder_raising", "ഇൻവെസ്റ്റർ പൈസ\nവന്നു. ഷെയർ എത്ര\nദിവസത്തിൽ?\n\nA) 60 ദിവസം\nB) 1 വർഷം", "A", "60 ദിവസത്തിനുള്ളിൽ അലോട്ട്മെന്റ്. പിന്നെ 15 ദിവസത്തിൽ PAS-3.")
contact("vx001", "angel", "സ്റ്റാർട്ടപ്പിൽ\nനിക്ഷേപിക്കാൻ\nആലോചനയുണ്ടോ?", "INVEST")
contact("vx002", "founder_raising", "ടേം ഷീറ്റ് കയ്യിൽ\nകിട്ടിയോ?", "TERMSHEET")
