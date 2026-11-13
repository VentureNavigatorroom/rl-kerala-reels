# Carousel bank 09. New angles: five company-prep jobs small enough for an office lunch break, the four questions a
# wholesale buyer asks a shop owner before signing a supply contract, five forwards from a Gulf-room WhatsApp group checked
# one by one. No prices; facts only from batch01.py. Every carousel carries cap_ml / cap_en / cap_mg for Instagram search.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
C = []
def car(id, segment, tag, hook, slides, end, cta, **kw): C.append(dict(id=id, kind="carousel", segment=segment, tag=tag, hook=hook, slides=slides, end=end, cta=cta, **kw))

car("k141", "salaried", "ലഞ്ച് ബ്രേക്ക്", "ജോലിക്കിടയിൽ കമ്പനി?\nലഞ്ച് ബ്രേക്കിൽ\nചെയ്യാവുന്ന 5 കാര്യം", [
 ("1. പേര് സെർച്ച് (15 മിനിറ്റ്)", "ഇതേ പോലുള്ള കമ്പനി/LLP പേരോ ട്രേഡ്മാർക്കോ ഉണ്ടോ എന്ന് നോക്കൂ. സാമ്യം ഉണ്ടെങ്കിൽ പേര് റിജക്ട് ആകാം."),
 ("2. ബാക്കപ്പ് പേരുകൾ (10 മിനിറ്റ്)", "2–3 പേര് കൂടി എഴുതിവെക്കൂ. Bank, Insurance പോലുള്ള വാക്കുകൾ ഒഴിവാക്കൂ."),
 ("3. വീട്ടുടമയ്ക്ക് ഒരു മെസ്സേജ്", "വീട് ഓഫീസ് ആക്കാൻ ഉടമയുടെ NOC വേണം. ഇന്ന് തന്നെ ചോദിച്ചുവെക്കൂ."),
 ("4. ഈ മാസത്തെ കറന്റ് ബിൽ", "ഓഫീസ് അഡ്രസ്സിന് പുതിയ ഒരു യൂട്ടിലിറ്റി ബിൽ വേണം. ഫോണിൽ ഫോട്ടോ എടുത്തുവെക്കൂ."),
 ("5. രണ്ടാമത്തെ ആളെ വിളിക്കൂ", "പ്രൈവറ്റ് ലിമിറ്റഡിന് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒറ്റയ്ക്കാണെങ്കിൽ OPC നോക്കാം.")],
 "അഞ്ച് ലഞ്ച് ബ്രേക്ക്.\nപകുതി ജോലി കഴിഞ്ഞു", CTA_DOCS,
 cap_ml="ജോലി വിടാതെ സൈഡ് ബിസിനസ് കമ്പനിയാക്കാൻ ആലോചിക്കുന്നവർക്ക്: കമ്പനി പേര് സെർച്ച്, ബാക്കപ്പ് പേരുകൾ, വീട്ടുടമയുടെ NOC, കറന്റ് ബിൽ, രണ്ടാമത്തെ ഡയറക്ടർ. ഓഫീസിലെ ലഞ്ച് ബ്രേക്കിൽ തീർക്കാവുന്ന അഞ്ച് ചെറിയ ജോലികൾ.",
 cap_en="Working a full-time job and planning company registration in Kerala on the side? Five small jobs you can finish in lunch breaks: company name search, backup names, the owner's NOC, a recent electricity bill, and your second director for a Pvt Ltd (or an OPC if you are alone).",
 cap_mg="Job-il irunnu thanne side business company register cheyyan plan undo? Company name search, backup names, veettudama-yude NOC, current bill, second director. Ellaam lunch break-il theerkkaam, Pvt Ltd allenkil OPC ethaanu ennum nokkaam.")

car("k142", "proprietor", "ബയറുടെ ചോദ്യങ്ങൾ", "ഹോൾസെയിൽ ബയർ\nകോൺട്രാക്ടിന് മുമ്പ്\nകടക്കാരനോട് ചോദിക്കുന്ന 4 ചോദ്യം", [
 ("\"നിങ്ങൾ രജിസ്റ്റേർഡ് കമ്പനി ആണോ?\"", "പല വലിയ ബയർമാരും കമ്പനിയുമായി മാത്രം കോൺട്രാക്ട് ഒപ്പിടും. പ്രൊപ്രൈറ്റർഷിപ്പ് മതിയാകണമെന്നില്ല."),
 ("\"അടുത്ത മാസം ഒപ്പിടാമോ?\"", "പ്രൈവറ്റ് ലിമിറ്റഡ് രജിസ്ട്രേഷന് സാധാരണ 7–15 പ്രവൃത്തി ദിവസം. പേര് റിജക്ട് ആയാൽ കൂടുതൽ."),
 ("\"കമ്പനി ഓഫീസ് അഡ്രസ്സ്?\"", "വീട് മതി. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും വേണം."),
 ("\"ഡയറക്ടർമാർ ആരൊക്കെ?\"", "കുറഞ്ഞത് 2 ഡയറക്ടർ, 2 ഷെയർഹോൾഡർ. ഒരാൾ ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം.")],
 "ബയർ ചോദിക്കും മുമ്പ്\nഉത്തരം റെഡിയാക്കൂ", CTA_START,
 cap_ml="വലിയ ഓർഡർ വരുമ്പോൾ ഹോൾസെയിൽ ബയർ ആദ്യം ചോദിക്കുന്നത് കമ്പനി രജിസ്ട്രേഷൻ ഉണ്ടോ എന്നാണ്. പ്രൊപ്രൈറ്റർഷിപ്പ് കട പ്രൈവറ്റ് ലിമിറ്റഡ് ആക്കാൻ എത്ര ദിവസം, ഓഫീസ് അഡ്രസ്സ്, ഡയറക്ടർമാർ: ഈ നാല് ഉത്തരവും ഒപ്പിടുന്നതിന് മുമ്പേ റെഡിയാക്കൂ.",
 cap_en="A wholesale buyer wants to sign a supply contract with your shop, but only with a registered company. Four questions they will ask a proprietor: are you a company, can you sign next month (Pvt Ltd registration usually takes 7-15 working days), what is the registered office, and who are the directors.",
 cap_mg="Kadayil valiya order vannu, pakshe buyer-nu registered company venam ennu. Proprietorship-il ninnu Pvt Ltd aakkan ethra divasam, office address, directors aarokke: ee naalu answer-um contract sign cheyyunnathinu munpe ready aakkikko.")

car("k143", "nri", "ഫോർവേഡ് ചെക്ക്", "ഗൾഫ് റൂമിലെ\nവാട്ട്സ്ആപ്പ് ഗ്രൂപ്പിൽ\nവന്ന 5 മെസ്സേജ്", [
 ("\"പ്രവാസിക്ക് നാട്ടിൽ ഡയറക്ടർ ആകാനാവില്ല\"", "തെറ്റ്. NRI-ക്കും ഇന്ത്യൻ പ്രൈവറ്റ് ലിമിറ്റഡിൽ ഡയറക്ടറും ഷെയർഹോൾഡറും ആകാം."),
 ("\"എല്ലാ ഡയറക്ടർമാരും ഗൾഫിൽ ആണെങ്കിലും ഓകെ\"", "തെറ്റ്. ഒരു ഡയറക്ടർ എങ്കിലും ഇന്ത്യയിൽ താമസിക്കുന്നയാൾ ആകണം."),
 ("\"കമ്പനി തുടങ്ങാൻ ആദ്യം ലക്ഷങ്ങൾ ഇടണം\"", "തെറ്റ്. പ്രൈവറ്റ് ലിമിറ്റഡിന് മിനിമം പെയ്ഡ്-അപ്പ് ക്യാപിറ്റൽ നിർബന്ധമില്ല."),
 ("\"നാട്ടിലെ വീട് ഓഫീസ് ആക്കാം\"", "ശരി. ഉടമയുടെ NOC-യും പുതിയ യൂട്ടിലിറ്റി ബില്ലും ഉണ്ടെങ്കിൽ."),
 ("\"ബിസിനസ് തുടങ്ങിയില്ലെങ്കിൽ ഫയലിംഗ് വേണ്ട\"", "തെറ്റ്. വരുമാനം ഇല്ലെങ്കിലും ആനുവൽ ഫയലിംഗ് വേണം. വൈകിയാൽ ഓരോ ഫോമിനും ദിവസം 100 രൂപ.")],
 "ഫോർവേഡ് ചെയ്യും മുമ്പ്\nഒന്ന് ചെക്ക് ചെയ്യൂ", CTA_START,
 cap_ml="ഗൾഫിലിരുന്ന് നാട്ടിൽ കമ്പനി തുടങ്ങാൻ ആലോചിക്കുന്ന പ്രവാസികളുടെ ഗ്രൂപ്പുകളിൽ വരുന്ന അഞ്ച് മെസ്സേജ്, ശരിയും തെറ്റും. NRI ഡയറക്ടർ, ഇന്ത്യയിൽ താമസിക്കുന്ന ഡയറക്ടർ, മൂലധനം, ഓഫീസ് അഡ്രസ്സ്, ആനുവൽ ഫയലിംഗ്.",
 cap_en="NRI business in Kerala: five forwards from a Gulf WhatsApp group, checked one by one. NRIs can be directors of a private limited company in India, but at least one director must live in India, and annual ROC filing is due even before the business starts earning.",
 cap_mg="Gulf-il irunnu naattil company register cheyyan nokkunna NRI-kal group-il kaanunna 5 message, sheriyum thettum. NRI-kkum Pvt Ltd director aakaam, pakshe oru director India-il thaamasikkunna aal venam. Revenue illenkilum annual filing venam.")
