# FSSAI batch 06 (20 Nov, month backlog). Max 6 lines, painful moment or myth first, payoff by line 4-5, short punch.
# Situations from bank/STORY_THEMES.md (anonymised; names, sectors and numbers invented). Facts only from topics.FACTS_FSSAI. No prices.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_FSSAI, CTA_FOOD = topics.CTA_FSSAI, topics.CTA_FOOD


# faq / d904: seasonal summer drink stall
duo("fs029", "packaged_food", "B", "busstop", "\"വേനലിൽ 3 മാസം\nസംഭാരം മാത്രം.\nലൈസൻസ് എന്തിന്?\"", [
 ("A","wide","അഖിലേ, ഈ വേനലിൽ ബസ് സ്റ്റാൻഡുകളിൽ കുപ്പി സംഭാരം. ദിവസം 400 കുപ്പി പോകുന്നു."),
 ("V","V","ജിബിനേ, FSSAI എടുത്തോ? കുപ്പിയിൽ നമ്പറും കണ്ടില്ല."),
 ("A","A","മൂന്ന് മാസത്തെ പരിപാടിയല്ലേ. മഴ വന്നാൽ നിർത്തും."),
 ("V","wide","സീസൺ നോക്കിയല്ല നിയമം. FSSAI ഇല്ലാതെ വിറ്റാൽ 5 ലക്ഷം വരെ പിഴ, 6 മാസം വരെ തടവും ആകാം."),
 ("A","A","അപ്പോ മോര് തണുപ്പിക്കും മുമ്പ് രജിസ്ട്രേഷൻ."),
 ("V","wide","വേനൽ മൂന്ന് മാസം, പിഴ കൊല്ലം മുഴുവൻ.")],
 "വേനൽ മൂന്ന് മാസം,\nപിഴ കൊല്ലം മുഴുവൻ", CTA_FSSAI, theme="faq",
 cap_ml="വേനലിൽ മൂന്ന് മാസം മാത്രം ബസ് സ്റ്റാൻഡുകളിൽ കുപ്പി സംഭാരം വിൽക്കുന്നവർക്കും FSSAI വേണം. ലൈസൻസില്ലാതെ ഫുഡ് വിറ്റാൽ 5 ലക്ഷം വരെ പിഴയും 6 മാസം വരെ തടവും ആകാം. നിങ്ങളുടെ ബിസിനസ് സീസണലോ?",
 cap_en="Selling bottled spiced buttermilk at bus stands for just three summer months still needs FSSAI. Selling food without it can mean a penalty up to 5 lakh and up to 6 months in prison. Is your food business seasonal?",
 cap_mg="Venalil moonnu maasam maathram bus standukalil kuppi sambharam vilkkunnavarkkum FSSAI venam. License illaathe food vittaal 5 lakh vare pizhayum 6 maasam vare thadavum aakaam. Ningalude business seasonal-o?")

# new / d904: homestay "free" breakfast

# crm (investor asks about licences): tea kiosks crossing the basic limit

# faq / d904: small coffee roaster importing beans

# crm (family business in a relative's name): grandfather's old halwa shop certificate

# crm (food delivery concept "starting soon", no licence planned): Ramadan snack boxes

# faq: "a women's group unit needs no FSSAI"

# crm (bank / investor diligence): seafood processor crossing 20 crore

# new / d904: cooking YouTuber selling masala packets through a link

# faq: "the delivery app will give us the licence"
