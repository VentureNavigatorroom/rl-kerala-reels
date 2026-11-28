# ROC tips 03 (28 Nov night), written as duo3d scenes (theme="tip"). Facts only from topics.FACTS_ROC; late-fee arithmetic only in
# check_bank-approved amounts. No prices of ours.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_ROC, CTA_FILING = topics.CTA_ROC, topics.CTA_FILING

duo("rct012", "nri_director", "B", "gulf", "ഡയറക്ടർ ആകാൻ\nവിളി വന്നോ?\nഒപ്പിടും മുമ്പ് 3 ചോദ്യം", [
 ("A","wide","ഫൈസലേ, നാട്ടിൽ അളിയന്റെ കമ്പനിയിൽ എന്നെ ഡയറക്ടർ ആക്കാമെന്ന്. ഒപ്പിട്ടാൽ മതിയെന്ന്."),
 ("V","V","ഷിജൂ, ഒപ്പിടും മുമ്പ് മൂന്ന് ചോദ്യം. ഒന്ന്: എല്ലാ വർഷവും AGM, AOC-4, MGT-7 സമയത്ത് ചെയ്യുന്നുണ്ടോ?"),
 ("A","A","രണ്ട്?"),
 ("V","V","എന്റെ DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ആര് ഓർമ്മിപ്പിക്കും? മൂന്ന്: ഫയലിംഗ് മുടങ്ങിയ വർഷങ്ങൾ ഉണ്ടോ?"),
 ("A","wide","3 വർഷം മുടങ്ങിയാൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത, അല്ലേ? അപ്പോ ഒപ്പ് ഒരു വരയല്ല."),
 ("V","wide","ഒപ്പിടും മുമ്പ് ഫയലിംഗ് ചോദിക്ക്.")],
 "ഒപ്പിടും മുമ്പ്\nഫയലിംഗ് ചോദിക്കൂ", CTA_ROC, theme="tip",
 cap_ml="ബന്ധുവിന്റെയോ കൂട്ടുകാരന്റെയോ കമ്പനിയിൽ ഡയറക്ടർ ആകും മുമ്പ് 3 ചോദ്യം: എല്ലാ വർഷവും AGM, AOC-4, MGT-7 ചെയ്യുന്നുണ്ടോ? നിങ്ങളുടെ DIR-3 KYC സെപ്റ്റംബർ 30-നുള്ളിൽ ആര് നോക്കും? മുടങ്ങിയ വർഷങ്ങൾ ഉണ്ടോ? 3 വർഷം മുടങ്ങിയാൽ ഡയറക്ടർക്ക് 5 വർഷം അയോഗ്യത.",
 cap_en="Asked to become a director in a relative's company? Ask 3 things first: are the AGM, AOC-4 and MGT-7 done every year, who tracks your DIR-3 KYC by 30 September, and are any years unfiled? Three years of non-filing can disqualify directors for 5 years.",
 cap_mg="Bandhuvinteyo koottukaaranteyo company-il director aakum mumbu 3 chodyam: ella varshavum AGM, AOC-4, MGT-7 cheyyunnundo? Ningalude DIR-3 KYC September 30-nullil aaru nokkum? Mudangiya varshangal undo? 3 varsham mudangiyaal director-kku 5 varsham ayogyatha.")

duo("rct013", "llp_owner", "A", "garage", "ജൂൺ 4. LLP ഫോം 11\nഅഞ്ച് ദിവസം വൈകി.\nഇനി എന്ത്?", [
 ("A","wide","ജിതിനേ, നമ്മുടെ LLP-യുടെ ഫോം 11 മെയ് 30-ന് വിട്ടുപോയി. ഇന്ന് ജൂൺ 4."),
 ("V","V","ഐശ്വര്യേ, ഫോമിന് ദിവസം 100 രൂപ. അഞ്ച് ദിവസം, 500 രൂപ. ഇന്ന് ചെയ്താൽ അവിടെ നിൽക്കും."),
 ("A","A","ഒക്ടോബറിൽ ഫോം 8-ന്റെ കൂടെ ചെയ്താലോ?"),
 ("V","V","ഫോം 8 ഒക്ടോബർ 30-നാ. അത്രയും കാത്താൽ ഫോം 11-ന് മാത്രം 15,000 രൂപയിൽ കൂടുതൽ."),
 ("A","wide","ശരി, ഇന്ന് തന്നെ 500-ൽ നിർത്താം."),
 ("V","wide","വൈകിയത് ഇന്ന് തീർത്താൽ ചെറുത്.")],
 "വൈകിയാൽ ഇന്ന് തന്നെ;\nകാത്താൽ വലുതാകും", CTA_FILING, theme="tip",
 cap_ml="LLP-യുടെ ഫോം 11 മെയ് 30-നുള്ളിൽ. അഞ്ച് ദിവസം വൈകിയാൽ 500 രൂപ; ഫോം 8-ന്റെ കൂടെ ഒക്ടോബർ വരെ കാത്താൽ 15,000 രൂപയിൽ കൂടുതൽ. വൈകിയ ഫോം അന്ന് തന്നെ ഫയൽ ചെയ്യൂ.",
 cap_en="An LLP's Form 11 is due by 30 May. Five days late costs Rs 500; wait until Form 8 in October and it passes Rs 15,000 for that one form. File a late form the day you notice.",
 cap_mg="LLP-yude Form 11 May 30-nullil. Anchu divasam vaikiyaal 500 roopa; Form 8-nte koode October vare kaathaal 15,000 roopayil kooduthal. Vaikiya form annu thanne file cheyyoo.")
