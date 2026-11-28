# Toon batch 04 for iec (28 Nov night), episodes 8-10 of "ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്" (ep 7 teased "അടുത്ത സീസൺ").
# ep 8: one IEC for import and export; ep 9: a consulting service for the buyer (SEIS gone, IEC on the date of service);
# ep 10: his sister's own pickle business needs its own IEC (one per PAN). Facts only from topics.FACTS_IEC. No fees.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "../_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
toon, S, C, T, topics = _h.toon, _h.S, _h.C, _h.T, _h.topics
SER = "ഫൈസലിന്റെ സ്പൈസ് എക്സ്പോർട്ട്"

toon("iex08", "importer", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ", "C": "ഷഫീഖ്"}, "കയറ്റുമതിക്ക് IEC ഉണ്ട്.\nമെഷീൻ ഇറക്കാൻ\nവേറെ കോഡ്?", [
 ("C", "ഫൈസലേ, ഈ സീസണിൽ ജർമ്മനിയിൽ നിന്ന് ഒരു ഏലം ഗ്രേഡിംഗ് മെഷീൻ വരുത്താം. ഇറക്കുമതിക്ക് പുതിയ കോഡ് എടുക്കണ്ടേ?"),
 ("A", "അപ്പൂപ്പാ, നമ്മുടെ IEC കയറ്റുമതിക്ക് വേണ്ടി എടുത്തതാ. ഇറക്കുമതിക്ക് വേറെ അപേക്ഷ വേണോ?"),
 ("B", "IEC എന്നാൽ ഇംപോർട്ട് എക്സ്പോർട്ട് കോഡ്. ഒരു PAN-ന് ഒന്ന് മാത്രം. ഇറക്കുമതിക്കും കയറ്റുമതിക്കും അതേ കോഡ്."),
 ("A", "അപ്പോ കസ്റ്റംസ് ചോദിക്കുമ്പോൾ അതേ നമ്പർ കൊടുത്താൽ മതി."),
 ("B", "അതെ. ഈ വർഷത്തെ ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് ചെയ്തിട്ടുണ്ടെന്ന് മാത്രം ഉറപ്പാക്കുക.")],
 dict(title="ഒരു IEC കൊണ്ട്", rows=[("കയറ്റുമതി", "ഇതേ കോഡ്"), ("ഇറക്കുമതി", "ഇതേ കോഡ്"), ("രണ്ടാമത്തെ അപേക്ഷ", "വേണ്ട")], total=("ഒരു PAN", "ഒരു IEC")),
 ["പുതിയ കോഡിന് ഓടും മുമ്പ് ഉള്ള IEC ഏത് PAN-ൽ എന്ന് നോക്കുക.", "ഏത് ദിശയിലായാലും ആ ഒരു IEC ആക്ടീവ് ആയി വെക്കുക."],
 "പോകാനും വരാനും\nഒരേ കോഡ്", topics.CTA_IEC, mentor="B", series=SER, ep=8, next="ബയർക്ക് ഒരു സർവീസ്", scene="shop", theme="faq",
 cap_ml="കയറ്റുമതിക്ക് എടുത്ത IEC കൊണ്ട് ഇറക്കുമതിയും ചെയ്യാം. ഒരു PAN-ന് ഒരു IEC മാത്രം; ഇംപോർട്ടിനും എക്സ്പോർട്ടിനും അതേ കോഡ്, വർഷം തോറും ഏപ്രിൽ-ജൂണിൽ അപ്ഡേറ്റ് ചെയ്താൽ മതി. നിങ്ങൾ കയറ്റുമതിയോ ഇറക്കുമതിയോ?",
 cap_en="Faisal's IEC was taken for spice exports; now he wants to import a cardamom grading machine. No second code is needed: one PAN has one IEC, and the same code works for imports and exports, as long as it is updated every year between April and June. Do you export, import or both?",
 cap_mg="Export-inu eduttha IEC kondu import-um cheyyaam. Oru PAN-inu oru IEC maathram; import-inum export-inum athe code, varsham thorum April-June-il update cheythaal mathi. Ningal export-o import-o?")

toon("iex09", "service_export", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ", "C": "ഹന്ന"}, "ദുബായ് ബയർക്ക്\nതോട്ടം കണ്ടെത്താൻ\nകൺസൾട്ടിംഗ് കരാർ", [
 ("A", "അപ്പൂപ്പാ, ദുബായ് ബയർ ഇനി ഏലം മാത്രമല്ല ചോദിക്കുന്നത്. നല്ല തോട്ടങ്ങൾ കണ്ടെത്തിക്കൊടുക്കാൻ മാസം തോറും കൺസൾട്ടിംഗും."),
 ("C", "ഫൈസലേ, സർവീസ് കയറ്റുമതിക്ക് സർക്കാർ 7% തരുമെന്ന് ഒരു വീഡിയോയിൽ കണ്ടു."),
 ("B", "ആ 7% പഴയ SEIS സ്കീമാണ്. 2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ അത് നിർത്തി. ഇന്ന് അങ്ങനെ ഒരു കാശില്ല."),
 ("A", "അപ്പോ ഈ സർവീസിന് IEC നോക്കണോ?"),
 ("B", "നയത്തിലെ ആനുകൂല്യത്തിന് സർവീസ് ചെയ്യുന്ന ദിവസം IEC കയ്യിൽ വേണം. നിന്റെ IEC ആദ്യ ബില്ലിന് മുമ്പ് ആക്ടീവ് ആണോ എന്ന് നോക്കൂ.")],
 dict(title="സർവീസ് ബിൽ ചെയ്യുമ്പോൾ", rows=[("പഴയ 7% SEIS", "ഇപ്പോൾ ഇല്ല"), ("നയത്തിലെ ആനുകൂല്യം", "IEC വേണം"), ("IEC എപ്പോൾ", "സർവീസ് ദിവസം")], total=("പിന്നെ എടുത്താൽ", "പഴയ ബില്ലിന് ഉപകാരമില്ല")),
 ["വീഡിയോയിൽ കേട്ട സ്കീം ഇന്നും ഉണ്ടോ എന്ന് ആദ്യം നോക്കുക.", "ആദ്യ സർവീസ് ബില്ലിന് മുമ്പ് IEC ആക്ടീവ് ആണെന്ന് ഉറപ്പാക്കുക."],
 "7% പഴങ്കഥ,\nIEC ഇന്നത്തെ കാര്യം", topics.CTA_EXPORT, mentor="B", series=SER, ep=9, next="അനിയത്തിയുടെ അച്ചാർ", scene="office", theme="faq",
 cap_ml="വിദേശ ബയർക്ക് കൺസൾട്ടിംഗ് പോലുള്ള സർവീസ് ചെയ്യുമ്പോൾ 7% കിട്ടുമെന്ന് പറയുന്നത് പഴയ SEIS സ്കീമാണ്; 2023-ലെ വിദേശ വ്യാപാര നയത്തിൽ അത് നിർത്തി. നയത്തിലെ ആനുകൂല്യം വേണമെങ്കിൽ സർവീസ് ചെയ്യുന്ന ദിവസം IEC വേണം. നിങ്ങൾ സാധനമോ സർവീസോ കയറ്റി അയക്കുന്നത്?",
 cap_en="Faisal's Dubai buyer now wants a monthly consulting service too, and a friend says service exporters get 7% from the government. That was the old SEIS scheme, discontinued under the Foreign Trade Policy 2023. To claim FTP benefits, the IEC must be held on the date the service is rendered. Do you export goods or services?",
 cap_mg="Videsha buyer-inu consulting pole service cheyyumbol 7% kittum ennu parayunnathu pazhaya SEIS scheme aanu; 2023-le FTP-yil athu nirthi. FTP benefit venamenkil service cheyyunna divasam IEC venam. Ningal saadhanamo service-o export cheyyunnathu?")

toon("iex10", "first_exporter", "B", {"A": "ഫൈസൽ", "B": "അപ്പൂപ്പൻ", "C": "സൽമ"}, "അനിയത്തിയുടെ\nഅച്ചാറിന് ഖത്തർ ഓർഡർ.\n\"ഇക്കാന്റെ IEC മതി\"", [
 ("C", "ഇക്കാ, എന്റെ അച്ചാർ ബ്രാൻഡിന് ഖത്തറിൽ നിന്ന് ആദ്യ ഓർഡർ! ഇക്കാന്റെ IEC നമ്പർ ഇട്ട് ഞാൻ അയച്ചോട്ടെ?"),
 ("A", "അപ്പൂപ്പാ, ഒരേ കുടുംബമല്ലേ. എന്റെ കോഡ് അവൾക്ക് ഉപയോഗിക്കാമോ?"),
 ("B", "IEC ബിസിനസിന്റെ PAN-മായി ബന്ധിപ്പിച്ചതാണ്. സൽമയുടെ അച്ചാർ ബിസിനസിന് വേറെ PAN ആണെങ്കിൽ അതിന് സ്വന്തം IEC വേണം."),
 ("C", "കുടുംബം ഒന്ന്, പക്ഷേ PAN രണ്ട്. അപ്പോ കോഡും രണ്ട്."),
 ("B", "അതെ. ബിൽ ആരുടെ പേരിലോ, IEC-യും അവരുടെ PAN-ൽ. പിന്നെ എല്ലാ വർഷവും ഏപ്രിൽ-ജൂൺ അപ്ഡേറ്റ് രണ്ടുപേരും ചെയ്യണം.")],
 dict(title="ആരുടെ IEC?", rows=[("ഫൈസലിന്റെ സ്പൈസ്", "ഫൈസലിന്റെ IEC"), ("സൽമയുടെ അച്ചാർ", "സ്വന്തം IEC"), ("കുടുംബത്തിന് ഒന്ന്", "ഇല്ല")], total=("ഒരു PAN", "ഒരു IEC")),
 ["ഓരോ ബിസിനസിന്റെയും PAN നോക്കി IEC എടുക്കുക.", "ആദ്യ ഓർഡർ വരും മുമ്പ് സ്വന്തം കോഡ് റെഡിയാക്കുക."],
 "കുടുംബം ഒന്ന്,\nPAN രണ്ട്, IEC രണ്ട്", topics.CTA_EXPORT, mentor="B", series=SER, ep=10, next="അടുത്ത സീസൺ", scene="home", theme="crm",
 cap_ml="ഒരേ കുടുംബത്തിലെ രണ്ട് ബിസിനസുകൾക്ക് ഒരു IEC മതിയാകില്ല. IEC ബിസിനസിന്റെ PAN-മായി ബന്ധിപ്പിച്ചതാണ്; വേറെ PAN ഉള്ള ബിസിനസിന് സ്വന്തം IEC വേണം, രണ്ടും വർഷം തോറും ഏപ്രിൽ-ജൂണിൽ അപ്ഡേറ്റ് ചെയ്യണം. നിങ്ങളുടെ വീട്ടിൽ എത്ര ബിസിനസ് ഉണ്ട്?",
 cap_en="Faisal's sister got her first pickle order from Qatar and wanted to ship it on her brother's IEC. The IEC is linked to the business PAN, so a separate business with its own PAN needs its own IEC, and each must be updated every year between April and June. How many businesses run in your family?",
 cap_mg="Ore kudumbathile randu business-inu oru IEC mathiyaakilla. IEC business PAN-umaayi bandhippichathaanu; vere PAN ulla business-inu swantham IEC venam, randum varsham thorum April-June-il update cheyyanam. Ningalude veettil ethra business undu?")
