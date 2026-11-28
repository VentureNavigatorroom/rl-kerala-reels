# kl batch 04 (28 Nov night): 3D duo reels. Facts only from topics.FACTS_KL.
# Never a home-business rule, a penalty, a fee amount, a validity period or "renewed every year". Invented names and places.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_SHOPS, CTA_KSMART = topics.CTA_SHOPS, topics.CTA_KSMART

# faq: a pharmacy assistant adds up her slips and finds 3,000 a year taken as professional tax; the maximum is 2,500
duo("lcd008", "salaried_staff_kl", "B", "pharmacy", "വർഷം മുഴുവൻ\nപ്രൊഫഷണൽ ടാക്സ്:\n3,000 രൂപ പിടിച്ചു!", [
 ("A","wide","പ്രവീണേട്ടാ, ഈ വർഷത്തെ ശമ്പള സ്ലിപ്പുകൾ കൂട്ടിനോക്കി. പ്രൊഫഷണൽ ടാക്സ് ആയി 3,000 രൂപ പിടിച്ചിട്ടുണ്ട്."),
 ("V","V","സിനീ, സോഫ്റ്റ്‌വെയർ എല്ലാ മാസവും ഒരേ തുക പിടിക്കും. പഴയ ആൾ സെറ്റ് ചെയ്തതാ, ശരിയായിരിക്കും."),
 ("A","A","പക്ഷേ പ്രൊഫഷണൽ ടാക്സ് വർഷം പരമാവധി 2,500 രൂപയല്ലേ? 2024 ഒക്ടോബറിൽ നിരക്ക് പുതുക്കിയതും നോക്കിയോ?"),
 ("V","V","ഇല്ല. തദ്ദേശ സ്ഥാപനത്തിലെ ഇപ്പോഴത്തെ നിരക്ക് നോക്കി സോഫ്റ്റ്‌വെയർ തിരുത്താം. കൂടുതൽ പിടിച്ചതിന്റെ കാര്യം ടീമിനോട് ചോദിക്കാം."),
 ("A","wide","മരുന്നിന് ഡോസ് ഉള്ളപോലെ, ഈ ടാക്സിനും ഒരു പരിധിയുണ്ട്.")],
 "പ്രൊഫഷണൽ ടാക്സ്\nവർഷം പരമാവധി 2,500", CTA_SHOPS, theme="faq",
 cap_ml="ശമ്പള സ്ലിപ്പിലെ പ്രൊഫഷണൽ ടാക്സ് വർഷം മുഴുവൻ കൂട്ടിനോക്കിയിട്ടുണ്ടോ? കേരളത്തിൽ അത് വർഷം പരമാവധി 2,500 രൂപയാണ്. നിരക്ക് 2024 ഒക്ടോബർ 1-ന് പുതുക്കി. തൊഴിലുടമ പിടിച്ച് തദ്ദേശ സ്ഥാപനത്തിൽ അടയ്ക്കണം. നിങ്ങളുടെ സ്ലിപ്പിൽ എത്രയാണ്?",
 cap_en="Have you added up the professional tax on your payslips for the whole year? In Kerala it is at most 2,500 rupees a year; the rates were revised on 1 Oct 2024. The employer deducts it and pays it to the local body. How much is on your slip?",
 cap_mg="Shambala slip-ile professional tax varsham muzhuvan koottinokkiyittundo? Keralathil athu varsham paramaavadhi 2,500 rupees aanu. Nirakku 2024 October 1-nu puthukki. Thozhiludama pidichu thadesha sthaapanathil adaykkanam. Ningalude slip-il ethrayaanu?")

# crm: a bike-service garage owner wants to wait for profit before any licence; the Shops Act counts days from starting, not profit
duo("lcd009", "new_shop", "B", "garage", "\"ആദ്യം ലാഭം വരട്ടെ,\nപിന്നെ രജിസ്ട്രേഷൻ\"\nകട തുടങ്ങിയിട്ട് 40 ദിവസം", [
 ("V","wide","ഐശ്വര്യേ, ബൈക്ക് സർവീസ് തുടങ്ങിയിട്ട് 40 ദിവസം. ആദ്യം കുറച്ച് ലാഭം വരട്ടെ, പിന്നെ ലൈസൻസും രജിസ്ട്രേഷനും."),
 ("A","A","ജിതിനേ, ഷോപ്സ് ആക്ട് ലാഭം നോക്കിയല്ല, ദിവസം നോക്കിയാ. സ്ഥാപനം തുടങ്ങി 60 ദിവസത്തിനകം രജിസ്റ്റർ ചെയ്യണം."),
 ("V","V","അപ്പോ ഇനി 20 ദിവസമേ ഉള്ളൂ!"),
 ("A","A","അതെ. ആദ്യം തദ്ദേശ സ്ഥാപനത്തിന്റെ ലൈസൻസ്, അതിന്റെ കോപ്പി വെച്ച് ഓൺലൈനായി ഷോപ്സ് ആക്ട്. ഇന്ന് തന്നെ തുടങ്ങ്."),
 ("V","wide","ബൈക്കിന് സർവീസ് ഡേറ്റ് ഉള്ളപോലെ, കടയ്ക്കും ഒരു ഡേറ്റ്.")],
 "ലാഭം നോക്കിയല്ല,\n60 ദിവസം നോക്കി", CTA_KSMART, theme="crm",
 cap_ml="ലാഭം വന്നിട്ട് ലൈസൻസ് എടുക്കാം എന്നാണോ പ്ലാൻ? കേരളത്തിൽ ഷോപ്സ് ആക്ട് രജിസ്ട്രേഷൻ സ്ഥാപനം തുടങ്ങി 60 ദിവസത്തിനകം വേണം, ഓൺലൈനായി, തദ്ദേശ സ്ഥാപന ലൈസൻസിന്റെ കോപ്പിയോടൊപ്പം. നിങ്ങളുടെ കട തുടങ്ങിയിട്ട് എത്ര ദിവസമായി?",
 cap_en="Planning to get licences once the profit comes in? In Kerala, Shops Act registration is due within 60 days of starting, online, with the local-body licence copy attached. How many days since your shop opened?",
 cap_mg="Laabham vannittu licence edukkaam ennaano plan? Keralathil Shops Act registration sthaapanam thudangi 60 divasathinakam venam, online-aayi, thadesha sthaapana licence-inte copy-odoppam. Ningalude kada thudangiyittu ethra divasamaayi?")
