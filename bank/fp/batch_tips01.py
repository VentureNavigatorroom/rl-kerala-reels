# Tips and tricks 01 (19 Nov night, owner): one tip reel per topic per day, in reserved slots. theme="tip". Facts only from topics.py.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_PROJECTION, CTA_FORECAST = topics.CTA_PROJECTION, topics.CTA_FORECAST

lst('fpt001', 'investor_pitch', "B", 'പ്രൊജക്ഷനിൽ\nഇൻവെസ്റ്റർ ആദ്യം\nനോക്കുന്നത്', [('മൂന്ന് വർഷം', 'ആദ്യ വർഷം മാസം തോറും.'), ('അനുമാനങ്ങൾ', 'എഴുതി വെക്കണം.'), ('ട്രാക്ഷൻ', 'നമ്പറുകൾ അതുമായി ചേരണം.')],
 'വലിയ നമ്പർ അല്ല,\nവിശ്വസനീയ നമ്പർ', CTA_PROJECTION, theme="tip",
 cap_ml='ഫിനാൻഷ്യൽ പ്രൊജക്ഷൻ: മൂന്ന് വർഷം, ആദ്യ വർഷം മാസം തോറും, എഴുതിയ അനുമാനങ്ങൾ, ട്രാക്ഷനുമായി ചേരുന്ന നമ്പറുകൾ. വലിച്ചുനീട്ടിയ നമ്പറുകൾ വിശ്വാസം കളയും. നിങ്ങളുടേത് ഏത് ഘട്ടത്തിൽ?',
 cap_en='Projections: 3 years, month by month for year 1, written assumptions, and numbers tied to traction. Inflated numbers lose trust. Where are yours?',
 cap_mg='Projection: 3 varsham, aadya varsham maasam thorum, ezhuthiya assumptions, traction-umaayi chernna numbers. Ningaludethu etha ghattathil?')

lst('fpt002', 'bank_loan', "B", 'ലോൺ അപേക്ഷയ്ക്ക്\nപ്രൊജക്ഷനിൽ\n3 ഭാഗം', [('ലാഭനഷ്ടം', 'വരുമാനവും ചെലവും.'), ('ക്യാഷ് ഫ്ലോ', 'പണം എപ്പോൾ വരും, പോകും.'), ('ബ്രേക്ക് ഈവൻ', 'എന്ന് മുതൽ ലാഭം.')],
 'ബാങ്ക് ചോദിക്കും\nമുമ്പ് റെഡി', CTA_FORECAST, theme="tip",
 cap_ml='ലോണിന് ബാങ്കുകൾ പ്രൊജക്ട് റിപ്പോർട്ട് ചോദിക്കാം. ലാഭനഷ്ടം, ക്യാഷ് ഫ്ലോ, ബ്രേക്ക് ഈവൻ എന്നിവ വ്യക്തമാകണം. നിങ്ങൾ ഏത് ലോണിനാണ് അപേക്ഷിക്കുന്നത്?',
 cap_en='Banks may ask for a project report for a loan: P&L, cash flow and break-even should be clear. Which loan are you applying for?',
 cap_mg='Loan-nu bank project report chodikkaam: P&L, cash flow, break-even vyaktham venam. Ningal etha loan-nu apply cheyyunnu?')

lst('fpt003', 'pre_revenue', "B", 'വരുമാനം\nഇല്ലാതെ\nപ്രൊജക്ഷൻ?', [('ഡ്രൈവറുകൾ', 'എത്ര കസ്റ്റമർ, എത്ര വളർച്ച.'), ('ചെലവ്', 'ടീമും നടത്തിപ്പും.'), ('ട്രിക്ക്', 'ഓരോ നമ്പറിനും ഒരു കാരണം എഴുതൂ.')],
 'ഊഹമല്ല,\nകാരണമുള്ള കണക്ക്', CTA_PROJECTION, theme="tip",
 cap_ml='വരുമാനം തുടങ്ങാത്ത സ്റ്റാർട്ടപ്പിനും പ്രൊജക്ഷൻ ഉണ്ടാക്കാം: കസ്റ്റമർ എണ്ണം, വളർച്ച, ടീം, ചെലവ്. ഓരോ നമ്പറിനും കാരണം എഴുതൂ. നിങ്ങളുടെ ആദ്യ കസ്റ്റമർ ആരാണ്?',
 cap_en='Even before revenue, you can build projections from drivers: customers, growth, team and costs, with a written reason for every number. Who is your first customer?',
 cap_mg='Revenue thudangaatha startup-num projection undaakkaam: customers, growth, team, chelavu. Oro number-num kaaranam ezhuthu. Ningalude first customer aaru?')

