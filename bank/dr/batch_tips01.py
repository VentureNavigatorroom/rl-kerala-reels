# Data room tips 01 (28 Nov): tip reels as duo scenes, theme="tip". Facts only from topics.FACTS_DR.
import importlib.util, os
_s = importlib.util.spec_from_file_location("h", os.path.join(os.path.dirname(__file__), "..", "_topic_helpers.py")); _h = importlib.util.module_from_spec(_s); _s.loader.exec_module(_h)
duo, chat, lst, car, tip, quiz, contact, S, C, T, topics = _h.duo, _h.chat, _h.lst, _h.car, _h.tip, _h.quiz, _h.contact, _h.S, _h.C, _h.T, _h.topics
CTA_DATAROOM, CTA_DILIGENCE = topics.CTA_DATAROOM, topics.CTA_DILIGENCE

duo('drt001', 'raising_first', 'B', 'gym', 'ഡാറ്റ റൂമിന്റെ\n6 ഫോൾഡറുകൾ:\n30 സെക്കൻഡിൽ', [('A', 'wide', 'ജസ്റ്റിനേ, ഡാറ്റ റൂമിന് ഒരു ലളിതമായ ഘടന പറയാമോ?'), ('V', 'V', 'റിയാ, രജിസ്ട്രേഷൻ, ഷെയർ, കരാറുകൾ, കണക്കും പ്രൊജക്ഷനും, ഫയലിംഗുകൾ, IP. ആറ് ഫോൾഡർ.'), ('A', 'A', 'ഓരോ ഫോൾഡറിലും എന്ത് ഇല്ല എന്ന് എങ്ങനെ അറിയും?'), ('V', 'V', 'ഓരോ ഫോൾഡറിനും ഒരു ചെക്ക്ലിസ്റ്റ് വെക്കുക. ശൂന്യമായത് ആദ്യം നിറയ്ക്കുക.'), ('A', 'wide', 'ലളിതം, പക്ഷേ ഇൻവെസ്റ്റർക്ക് വേഗം കിട്ടും.'), ('V', 'wide', 'ആറ് ഫോൾഡർ, ഒരു ചെക്ക്ലിസ്റ്റ്.')],
 'ആറ് ഫോൾഡർ,\nഒരു ചെക്ക്ലിസ്റ്റ്', CTA_DATAROOM, theme='tip',
 cap_ml='ലളിതമായ ഡാറ്റ റൂം: രജിസ്ട്രേഷൻ, ഷെയർ, കരാറുകൾ, കണക്കും പ്രൊജക്ഷനും, ഫയലിംഗുകൾ, IP എന്നിങ്ങനെ ആറ് ഫോൾഡർ. നിങ്ങൾക്ക് ഏത് ഫോൾഡറാണ് ശൂന്യം?',
 cap_en='A simple data room has six folders: registration, shares, agreements, accounts and projections, filings, and IP. Keep a checklist for each and fill the empty ones first. Which of yours is empty?',
 cap_mg='Laalithamaaya data room: registration, share, agreements, accounts-um projection-um, filings, IP ennee aaru folder. Ningalkku ethu folder aanu shoonyam?')

duo('drt002', 'messy_docs', 'A', 'office', 'ഫയലുകൾക്ക്\nപേര് നൽകാൻ\nഒരു ട്രിക്ക്', [('A', 'wide', "രാഹുലേ, ഫോൾഡറിൽ ഫൈനൽ, ഫൈനൽ രണ്ട്, പുതിയ ഫൈനൽ എന്നൊക്കെയാണ് ഫയൽ പേരുകൾ!"), ('V', 'V', 'നേഹ, ഓരോ ഫയലിനും രേഖയുടെ പേരും തീയതിയും വെക്കുക. ഉദാഹരണം: GST റിട്ടേൺ, മാർച്ച്.'), ('A', 'A', 'പഴയ വേർഷനുകൾ എന്ത് ചെയ്യും?'), ('V', 'V', 'വേറെ ഒരു ആർക്കൈവ് ഫോൾഡറിലേക്ക് മാറ്റുക. ഡാറ്റ റൂമിൽ ഏറ്റവും പുതിയത് മാത്രം.'), ('A', 'wide', 'ഇൻവെസ്റ്റർ തിരഞ്ഞ് സമയം കളയരുത്.'), ('V', 'wide', 'പേരും തീയതിയും, അത്ര മാത്രം.')],
 'പേരും തീയതിയും,\nഅത്ര മാത്രം', CTA_DATAROOM, theme='tip',
 cap_ml="ഡാറ്റ റൂമിൽ ഓരോ ഫയലിനും രേഖയുടെ പേരും തീയതിയും നൽകൂ, പഴയ വേർഷനുകൾ ആർക്കൈവിലേക്ക് മാറ്റൂ. നിങ്ങളുടെ ഫോൾഡറിൽ എത്ര ഫൈനൽ ഉണ്ട്?",
 cap_en="Files named final, final2 and new final slow investors down. Name every file with the document and the date, and move old versions to an archive so only the latest stays. How many 'finals' are in your folder?",
 cap_mg="Data room-il oro file-inum rekhayude perum theeyathiyum kodukku, pazhaya versions archive-ilekku maattu. Ningalude folder-il ethra 'final' undu?")

duo('drt003', 'investor_asked', 'B', 'library', 'ആർക്ക് എന്ത്\nകാണാം? ഡാറ്റ റൂം\nസുരക്ഷ', [('A', 'wide', 'അനൂപേ, ഇൻവെസ്റ്റർക്ക് ലിങ്ക് അയക്കുമ്പോൾ എല്ലാവർക്കും എല്ലാം തുറന്നിടണോ?'), ('V', 'V', 'ഗ്രീഷ്മേ, വേണ്ട. ആർക്ക് എന്ത് കാണാം എന്ന് നിയന്ത്രിക്കുന്ന സുരക്ഷിത ഫോൾഡർ ആയിരിക്കണം.'), ('A', 'A', 'NDA വേണോ?'), ('V', 'V', 'വിശദമായ രേഖകൾ പങ്കുവെക്കും മുമ്പ് NDA ചോദിക്കാം. പല ഇൻവെസ്റ്റർമാരും ആദ്യ ഘട്ടത്തിൽ ഒപ്പിടില്ല.'), ('A', 'wide', 'അപ്പോ ഘട്ടം ഘട്ടമായി തുറക്കാം.'), ('V', 'wide', 'ആദ്യം കാഴ്ച, പിന്നെ വിശദാംശം.')],
 'ആദ്യം കാഴ്ച,\nപിന്നെ വിശദാംശം', CTA_DATAROOM, theme='tip',
 cap_ml='ഡാറ്റ റൂം ആർക്ക് എന്ത് കാണാം എന്ന് നിയന്ത്രിക്കുന്ന സുരക്ഷിത ഫോൾഡറാകണം. വിശദമായ രേഖകൾ ഘട്ടം ഘട്ടമായി തുറക്കൂ. നിങ്ങളുടെ ലിങ്ക് ആർക്കൊക്കെ തുറക്കാം?',
 cap_en="Don't open everything to everyone. A data room should control who sees what, and detailed documents can open step by step; you can ask for an NDA first, though many investors won't sign one early. Who can open your link?",
 cap_mg='Data room aarkku enthu kaanaam ennu niyanthrikkunna secure folder aakanam. Vishadamaaya rekhakal ghattam ghattamaayi thurakku. Ningalude link aarkkokke thurakkaam?')

