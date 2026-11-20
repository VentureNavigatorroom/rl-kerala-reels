# Tips and tricks 03 (20 Nov, refill to 10 unposted tips: one co tip posted). theme="tip". Same checked facts as batch01.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
S = []
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))


lst('kt011', 'solo', "B", 'കമ്പനിയുടെ പേര്\nറിജക്റ്റ്.\n3 കാരണങ്ങൾ', [('സാമ്യം', 'നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം.'), ('ട്രേഡ്മാർക്ക്', 'മറ്റൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ്.'), ('നിയന്ത്രിത വാക്കുകൾ', 'ബാങ്ക്, ഇൻഷുറൻസ് പോലുള്ള വാക്കുകൾ അനുമതി ഇല്ലാതെ.')],
 'അപേക്ഷിക്കും മുമ്പ്\nമൂന്നും നോക്കൂ', CTA_NAME, theme="tip",
 cap_ml='കമ്പനി പേര് റിജക്റ്റ് ആകുന്നത് മിക്കവാറും മൂന്ന് കാരണത്താൽ: നിലവിലുള്ള കമ്പനിയുടെയോ LLP-യുടെയോ പേരിനോട് സാമ്യം, മറ്റൊരാളുടെ ട്രേഡ്മാർക്കുമായി ക്ലാഷ്, ബാങ്ക് ഇൻഷുറൻസ് പോലുള്ള നിയന്ത്രിത വാക്കുകൾ. നിങ്ങളുടെ പേരിൽ ഇതിൽ ഏതെങ്കിലും ഉണ്ടോ?',
 cap_en='A company name is usually rejected for one of three reasons: it is too similar to an existing company or LLP, it clashes with someone else\'s trademark, or it uses restricted words such as Bank or Insurance. Does your name pass all three?',
 cap_mg='Company peru reject aakunnathu mikkavaarum moonnu kaaranathaal: ippozhulla company-yudeyo LLP-yudeyo perinodu saamyam, mattoraalude trademark-umaayi clash, Bank, Insurance pole restricted words. Ningalude perinu ithil ethenkilum undo?')
