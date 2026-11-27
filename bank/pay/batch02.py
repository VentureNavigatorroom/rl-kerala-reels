# pay batch 02 (27 Nov evening refill): 3D duo reel. Max 6 lines, painful moment first, payoff by line 4-5.
# Invented names, sectors and towns. Facts only from topics.FACTS_PAY. Never promise an incentive, never our fee.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, S, C, T, topics = _h.duo, _h.S, _h.C, _h.T, _h.topics
CTA_ESIC, CTA_PAYROLL = topics.CTA_ESIC, topics.CTA_PAYROLL

# new: a fish-processing unit lets a new hire go after 3 months and still counts on PM-VBRY
duo("pyd007", "new_hires_incentive", "B", "fishmarket", "പുതിയ ആളെ 3 മാസം\nകഴിഞ്ഞ് വിട്ടു.\nസഹായം ഇപ്പോഴും കിട്ടുമോ?", [
 ("A","wide","ആന്റണീ, പുതിയ പാക്കിംഗ് സ്റ്റാഫിനെ 3 മാസം കഴിഞ്ഞ് വിട്ടല്ലോ. എന്നിട്ടും PM-VBRY കണക്കിൽ കൂട്ടിയോ?"),
 ("V","V","സുമേ, സർക്കാർ ഓരോ പുതിയ ആൾക്കും 3,000 രൂപ തരും എന്നല്ലേ കേട്ടത്?"),
 ("A","A","3,000 രൂപ വരെ എന്നാണ്. നിബന്ധനകൾ ഉണ്ട്. ആ ആൾ കുറഞ്ഞത് 6 മാസം ജോലിയിൽ തുടരണം. EPFO രജിസ്ട്രേഷനും വേണം."),
 ("V","V","അപ്പോ ഇത് ഉറപ്പുള്ള പൈസ അല്ല. കണക്കിൽ നിന്ന് മാറ്റാം."),
 ("A","wide","സഹായം കണക്കിൽ കൂട്ടും മുമ്പ് നിബന്ധന വായിക്കൂ.")],
 "\"വരെ\" എന്നാൽ ഉറപ്പല്ല.\n6 മാസം വേണം", CTA_PAYROLL, theme="new",
 cap_ml="PM-VBRY: EPFO-യിൽ രജിസ്റ്റർ ചെയ്ത തൊഴിലുടമകൾക്ക് പുതിയ ഓരോ ജീവനക്കാരനും മാസം 3,000 രൂപ വരെ, 2 വർഷം, നിബന്ധനകളോടെ. ജീവനക്കാരൻ കുറഞ്ഞത് 6 മാസം തുടരണം, തുക ശമ്പള സ്ലാബ് അനുസരിച്ച്, കുറഞ്ഞ പുതിയ നിയമനങ്ങളും വേണം. ഉറപ്പായി കണക്കിൽ കൂട്ടരുത്. നിങ്ങൾ ഈ വർഷം പുതിയ ആളെ എടുത്തോ?",
 cap_en="A fish-processing unit lets a new packer go after 3 months and still counts on PM-VBRY. The scheme gives EPFO-registered employers up to 3,000 rupees a month per additional employee for 2 years, subject to conditions: the employee must stay at least 6 months, the amount depends on the wage slab, and there is a minimum number of new hires. Don't count it as certain. Did you hire this year?",
 cap_mg="PM-VBRY: EPFO-yil register cheytha employers-inu puthiya oro jeevanakkaaranum maasam 3,000 rupees vare, 2 varsham, nibandhanakalode. Jeevanakkaaran kuranjathu 6 maasam thudaranam, thuka salary slab anusarichu, kuranja puthiya niyamanangalum venam. Urappaayi kanakkil koottaruthu. Ningal ee varsham puthiya aale edutho?")
