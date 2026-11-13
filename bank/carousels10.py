# Carousel bank 10. New angles: one investor knocking on three doors (partnership, LLP, Pvt Ltd), a shop owner's three weeks
# from the buyer's phone call to the signed contract, the dates an NRI hands over at the airport before flying back.
# No prices; facts only from batch01.py. Every carousel carries cap_ml / cap_en / cap_mg for Instagram search.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
C = []
def car(id, segment, tag, hook, slides, end, cta, **kw): C.append(dict(id=id, kind="carousel", segment=segment, tag=tag, hook=hook, slides=slides, end=end, cta=cta, **kw))

car("k144", "cofounders", "മൂന്ന് വാതിൽ", "ഒരേ ഇൻവെസ്റ്റർ,\nമൂന്ന് വാതിൽ:\nഏത് വാതിൽ തുറക്കും?", [
 ("വാതിൽ 1: പാർട്ണർഷിപ്പ്", "ഇൻവെസ്റ്റർ ചോദിക്കും: \"ഷെയർ എവിടെ?\" പാർട്ണർഷിപ്പിന് ഷെയർ ഇല്ല. നിക്ഷേപം എടുക്കാൻ പറ്റില്ല."),
 ("വാതിൽ 2: LLP", "പേരിൽ 'ലിമിറ്റഡ്' ഉണ്ടെങ്കിലും LLP-ക്കും ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പറ്റില്ല."),
 ("വാതിൽ 3: പ്രൈവറ്റ് ലിമിറ്റഡ്", "ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പറ്റുന്നത് ഇത് മാത്രം."),
 ("ഈ വാതിലിന് വേണ്ടത്", "കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒരു ഡയറക്ടർ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ."),
 ("എത്ര ദിവസം?", "രജിസ്ട്രേഷന് സാധാരണ 7-15 പ്രവൃത്തി ദിവസം. ഇൻവെസ്റ്റർ മീറ്റിംഗിന് മുമ്പേ തുടങ്ങൂ.")],
 "ഫണ്ടിംഗ് വേണമെങ്കിൽ\nവാതിൽ ഒന്നേയുള്ളൂ", CTA_START,
 cap_ml="സ്റ്റാർട്ടപ്പിൽ നിക്ഷേപിക്കാൻ ഇൻവെസ്റ്റർ റെഡി: പാർട്ണർഷിപ്പ്, LLP, പ്രൈവറ്റ് ലിമിറ്റഡ് ഇവയിൽ ഏതിൽ നടക്കും? ഷെയർ കൊടുത്ത് നിക്ഷേപം എടുക്കാൻ പ്രൈവറ്റ് ലിമിറ്റഡ് കമ്പനിക്ക് മാത്രമേ പറ്റൂ. കുറഞ്ഞത് 2 ഡയറക്ടർ, 7-15 പ്രവൃത്തി ദിവസം.",
 cap_en="An investor is ready for your startup in Kerala. Partnership, LLP or private limited company: which one can take the money? Only a Pvt Ltd can issue shares for equity investment. It needs at least two directors and usually 7 to 15 working days to register.",
 cap_mg="Startup-il invest cheyyan investor ready: partnership, LLP, Pvt Ltd, ethil nadakkum? Share koduthu investment edukkan Pvt Ltd company-kku maathrame pattu. Minimum 2 directors, register cheyyan 7-15 working days.")

car("k145", "proprietor", "3 ആഴ്ച", "ബയർ വിളിച്ചു:\n\"കമ്പനി ആണെങ്കിൽ ഓർഡർ\"\nഅടുത്ത 3 ആഴ്ച ഇങ്ങനെ", [
 ("ദിവസം 1: കോൾ കഴിഞ്ഞ ഉടനെ", "ആരൊക്കെ ഡയറക്ടർ എന്ന് തീരുമാനിക്കൂ. Pvt Ltd-ന് 2 പേർ, ഒറ്റയ്ക്കാണെങ്കിൽ OPC."),
 ("ദിവസം 2-3: പേരും അഡ്രസ്സും", "സാമ്യമില്ലാത്ത 3 പേര്. ഓഫീസിന് ഉടമയുടെ NOC, പുതിയ യൂട്ടിലിറ്റി ബില്ല്."),
 ("ആഴ്ച 1-3: രജിസ്ട്രേഷൻ", "Pvt Ltd-ന് സാധാരണ 7-15 പ്രവൃത്തി ദിവസം. പേര് റിജക്ട് ആയാൽ കൂടുതൽ."),
 ("സർട്ടിഫിക്കറ്റ് വന്ന ദിവസം", "ബയറിന് കമ്പനി ഡീറ്റെയിൽസ് അയക്കൂ. 30 ദിവസത്തിൽ ആദ്യ ഓഡിറ്ററെ വെക്കണം."),
 ("കലണ്ടറിൽ ഇപ്പോഴേ", "180 ദിവസത്തിൽ INC-20A. പിന്നെ എല്ലാ വർഷവും ആനുവൽ ഫയലിംഗ്.")],
 "ഓർഡർ കാത്തുനിൽക്കും,\nഅധികം നാൾ അല്ല", CTA_DOCS,
 cap_ml="വലിയ ബയർ കമ്പനിയുമായി മാത്രം ഓർഡർ ഒപ്പിടുമെന്ന് പറഞ്ഞാൽ കടക്കാരന്റെ അടുത്ത മൂന്നാഴ്ച: ഡയറക്ടർമാർ, കമ്പനി പേര്, ഓഫീസ് ഡോക്യുമെന്റ്സ്, 7-15 പ്രവൃത്തി ദിവസത്തെ രജിസ്ട്രേഷൻ, പിന്നെ ഓഡിറ്ററും INC-20A-യും.",
 cap_en="A buyer will place the order only if your shop is a company. Your next three weeks in Kerala: decide the directors, pick three company names, get the office NOC and utility bill, register (usually 7 to 15 working days), then appoint the auditor within 30 days.",
 cap_mg="Buyer company aanenkil maathram order ennu paranjaal kadakkarante adutha 3 aazhcha: directors, company name, office documents, 7-15 working days registration, pinne auditor-um INC-20A-yum. Company register cheyyan timeline.")

car("k146", "nri", "എയർപോർട്ട് ഹാൻഡ്ഓവർ", "ലീവ് കഴിഞ്ഞ് തിരികെ.\nഎയർപോർട്ടിൽ വെച്ച്\nനാട്ടിലെ ഡയറക്ടറെ\nഏൽപ്പിക്കേണ്ട 3 ഡേറ്റ്", [
 ("ഡേറ്റ് 1: ഇൻകോർപ്പറേഷൻ + 30 ദിവസം", "ആദ്യ ഓഡിറ്ററെ നിയമിക്കണം. നിങ്ങൾ ഗൾഫിൽ ആണെങ്കിലും ഡേറ്റ് മാറില്ല."),
 ("ഡേറ്റ് 2: ഇൻകോർപ്പറേഷൻ + 180 ദിവസം", "INC-20A. മിസ്സ് ആയാൽ കമ്പനിക്ക് 50,000 രൂപ പിഴ."),
 ("ഡേറ്റ് 2-ന്റെ ബാക്കി", "വീഴ്ച വരുത്തിയ ഓരോ ഡയറക്ടർക്കും ദിവസം 1,000 രൂപ, 1 ലക്ഷം വരെ."),
 ("ഡേറ്റ് 3: എല്ലാ വർഷത്തെയും ഫയലിംഗ്", "വരുമാനം ഇല്ലെങ്കിലും ആനുവൽ ഫയലിംഗ്. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.")],
 "ഫ്ലൈറ്റ് പോകും,\nഡേറ്റുകൾ പോകില്ല", CTA_AFTER,
 cap_ml="ലീവിൽ വന്ന് നാട്ടിൽ കമ്പനി തുടങ്ങിയ NRI-കൾ തിരികെ പോകും മുമ്പ് നാട്ടിലെ ഡയറക്ടറെ ഏൽപ്പിക്കേണ്ട ഡേറ്റുകൾ: 30 ദിവസത്തിൽ ഓഡിറ്റർ, 180 ദിവസത്തിൽ INC-20A, എല്ലാ വർഷവും ആനുവൽ ഫയലിംഗ്.",
 cap_en="NRIs who registered a company in Kerala during their leave: before you fly back, hand these dates to the director at home. First auditor within 30 days, INC-20A within 180 days (Rs 50,000 penalty if missed), and annual filings every year even with zero revenue.",
 cap_mg="Leave-il vannu naattil company thudangiya NRI-kal thirichu pokunnathinu munpu naattile director-ne elpikkenda dates: 30 days-il auditor, 180 days-il INC-20A, ella varshavum annual filing (ROC).")
