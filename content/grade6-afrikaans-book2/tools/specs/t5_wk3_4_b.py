import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

WRITE_PROCESS = ['Beplan jou skryfwerk.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']
JLO = ['Jabu', 'die leeu', 'die jakkals']

# ============================================================== 77 Dink na oor die karakters
L77 = lesson(77,
  skills=[LISTEN, WRITE, LANG],
  intro='Hoe leer ons ’n karakter ken? Vandag beskryf jy Jabu, die leeu en iemand wat jy self ken – met byvoeglike naamwoorde.',
  objectives=['Byvoeglike naamwoorde gebruik om karakters te beskryf.', '’n Karakterskets van Jabu skryf.', 'Die leeu in ’n paragraaf beskryf.', '’n Persoon wat jy ken, beskryf.'],
  learn=[
    note('Ons leer die karakters in ’n storie ken uit wat hulle sê of doen of wat ander ons van hulle vertel.', title='Hoe leer ons karakters ken?', page=26),
    text('Byvoeglike naamwoorde', 'Byvoeglike naamwoorde is beskrywende woorde. Hulle sê meer van ’n persoon of ding, bv. ’n **dapper** seun, ’n **slim** jakkals.', src='supplementary', page=26),
    text('Die skryfproses', bullets=['**Beplan** jou karakterskets deur byvoeglike naamwoorde in die raampies in te vul.', 'Skryf jou **eerste weergawe** in jou klaswerkboek.', 'Laat ’n maat jou werk **hersien**.', '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** vir publikasie.'], page=26),
  ],
  acts=[
    discuss('Dinkskrum oor Jabu', 'Hou ’n dinkskrum saam met jou maats om soveel beskrywende woorde moontlik te kry wat Jabu se karakter beskryf.', page=26, item='dinkskrum'),
    fill('Jabu se naam en ouderdom', 'Naam: {{1}}\nOuderdom: {{2}}', {1: 'Jabu', 2: ['14', '14 jaar', 'veertien']}, 'Die storie sê: Jabu was ’n 14-jarige veewagter.', src='workbook', page=26, item='raampies', status='derived_from_text'),
    choices('Wat beskryf Jabu?', 'Pas die woord by Jabu se karakter? Kies Ja of Nee.',
            [('verantwoordelik', ['Ja', 'Nee'], 0), ('dapper', ['Ja', 'Nee'], 0), ('lui', ['Ja', 'Nee'], 1), ('gulsig', ['Ja', 'Nee'], 1), ('meelewend (hy het jammer gevoel vir die leeu)', ['Ja', 'Nee'], 0), ('oneerlik', ['Ja', 'Nee'], 1)],
            'Jabu pas sy pa se vee goed op, stap dapper na die geluid en voel jammer vir die leeu.', src='workbook', page=26, item='karaktertrekke', status='derived_from_text'),
    writing('Karakterskets van Jabu', 'Gebruik jou byvoeglike naamwoorde om ’n karakterskets van Jabu te skryf.', checklist=['Ek het sy naam en ouderdom genoem.', 'Ek het minstens vier byvoeglike naamwoorde gebruik.', 'Ek het gesê wat hy doen of sê wat wys hoe hy is.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=8, page=26, item='Jabu'),
    sa('Ses woorde oor die leeu', 'Vul ses byvoeglike naamwoorde in wat die leeu beskryf.', 'sterk, gulsig, oneerlik, desperaat, magtig, slinks', lines=2, page=26, item='leeu', status='needs_review'),
    writing('Paragraaf oor die leeu', 'Gebruik die byvoeglike naamwoorde om ’n paragraaf te skryf waarin jy die leeu beskryf. Skryf jou eerste weergawe in jou klaswerkboek, vra ’n maat om dit te hersien en skryf dan die finale weergawe.',
            checklist=['Ek het die ses byvoeglike naamwoorde gebruik.', 'My paragraaf het ’n begin, ’n middel en ’n einde.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=8, page=26, item='paragraaf'),
    writing('Beplan jou eie karakter', 'Kies ’n karakter wat jy ken en vul die inligting in.', checklist=['Volle naam en van', 'Vroulik of manlik', 'Ouderdom', 'Beroep', 'Fisiese voorkoms', 'Talente of vaardighede', 'Waarom ek hom of haar gekies het'], lines=8, page=27, item='raampies'),
    writing('Beskryf die persoon wat jy ken', 'Beskryf nou die karakter van ’n persoon wat jy ken. Kies iemand oor wie jy wil skryf. Die persoon kan ’n held of heldin wees, hy of sy kan vandag lewe of kan reeds oorlede wees.',
            checklist=['Ek het byvoeglike naamwoorde op die breinkaart ingevul.', 'Ek het my eerste weergawe laat hersien.', 'Ek het spel- en punktuasiefoute reggemaak.'], tips=WRITE_PROCESS, lines=10, page=27, item='persoon'),
    match('Pas die woord by sy betekenis', 'Verbind elke byvoeglike naamwoord met sy betekenis.', [('verantwoordelik', 'kan vertrou word om sy werk te doen'), ('dapper', 'nie bang om gevaar te trotseer nie'), ('gulsig', 'wil altyd meer eet of hê'), ('oneerlik', 'praat of doen nie wat reg is nie')],
          'Byvoeglike naamwoorde beskryf mense en diere.', status='derived_from_rule'),
    fill('Kies die byvoeglike naamwoord', 'Die {{1}} jakkals het die leeu uitoorlê. Die {{2}} leeu was vasgevang.', {1: ['slim', 'slu', 'slinkse'], 2: ['sterk', 'desperate', 'magtige', 'gulsige']}, 'Slim, slu en slinks beskryf die jakkals; die leeu was sterk maar desperaat.', bank=['slim', 'sterk', 'lui'], status='needs_review'),
  ],
  quiz=[
    q('grammar', 'Wat is ’n byvoeglike naamwoord?', '’n Woord wat ’n persoon of ding beskryf', ['’n Woord wat ’n aksie aandui', '’n Woord wat twee sinne verbind', '’n Woord wat ’n naam is'], 'Byvoeglike naamwoorde beskryf selfstandige naamwoorde, soos “dapper” in “’n dapper seun”.', status='derived_from_rule'),
    q('grammar', 'Watter woord in die sin is ’n byvoeglike naamwoord: “Die slim jakkals het die leeu gevang”?', 'slim', ['jakkals', 'gevang', 'leeu'], 'Slim beskryf die jakkals.', status='derived_from_rule'),
    q('main_idea', 'Hoe leer ons die karakters in ’n storie ken?', 'Uit wat hulle sê of doen of wat ander ons van hulle vertel', ['Net uit die titel', 'Net uit die prente', 'Net uit die einde van die storie'], 'Die werkboek verduidelik dit in die blou nota.', status='official', src='workbook', page=26),
    q('inference', 'Watter woord beskryf Jabu die beste?', 'verantwoordelik', ['gulsig', 'oneerlik', 'lui'], 'Jabu pas sy pa se vee goed op.', status='derived_from_text'),
    q('inference', 'Watter woord beskryf die leeu wat sy belofte verbreek het?', 'oneerlik', ['betroubaar', 'verantwoordelik', 'bedeesd'], 'Hy het belowe om nie Jabu op te vreet nie, maar het sy belofte verbreek.', status='needs_review'),
    q('vocabulary', 'Wat beteken “dapper”?', 'Nie bang om gevaar te trotseer nie', ['Baie moeg', 'Baie honger', 'Baie slim'], 'Jabu het dapper na die leeu se geluid toe gestap.', status='derived_from_rule'),
    q('vocabulary', 'Wat beteken “gulsig”?', 'Iemand wat altyd meer wil eet of hê', ['Iemand wat baie lui is', 'Iemand wat baie bang is', 'Iemand wat baie vriendelik is'], 'Die leeu wou Jabu opvreet al het hy belowe om dit nie te doen nie.', status='derived_from_rule'),
    q('grammar', 'Watter sin bevat twee byvoeglike naamwoorde?', 'Die sterk, slim leeu het die jakkals gesien.', ['Die leeu het die jakkals gesien.', 'Jabu stap huis toe.', 'Sipho hardloop vinnig.'], 'Sterk en slim beskryf albei die leeu.', status='derived_from_rule'),
  ])

# ============================================================== 78 Werk met sinne
L78 = lesson(78,
  intro='Sinne is soos legkaarte: onderwerp, gesegde, voorwerp en bepaling. Vandag oefen jy verskillende soorte sinne en werkwoordvorme.',
  objectives=['Onderwerp, gesegde, voorwerp en bepaling in ’n enkelvoudige sin uitwys.', 'Die hoofsin en bysin in ’n veelvoudige sin uitken.', 'Gesegdes in ’n saamgestelde sin vind.', 'Die korrekte vorm van werkwoorde skryf (teenwoordige, verlede en toekomende tyd).'],
  learn=[
    text('Drie soorte sinne', bullets=['’n **Enkelvoudige sin** het net een gesegde (werkwoord/-stuk). Dit kan ook bepalings hê.', '’n **Saamgestelde sin** het altyd twee of meer gesegdes (werkwoorde/-stukke) en bestaan uit meer as een hoofsin.',
         '’n **Veelvoudige sin** het ’n hoofsin en ’n bysin.'], page=28),
    note('Indien die selfstandige naamwoord of die werkwoord beskryf word, word die beskrywende woord die **bepaling** genoem.', title='Bepaling', page=28),
    table('Voorbeeld van ’n enkelvoudige sin', ['Onderwerp', 'Gesegde', 'Voorwerp'], [['Jabu', 'bevry', 'die groot leeu']], page=28),
    text('Werkwoordvorme', bullets=['**Teenwoordige tyd:** Ek help.', '**Verlede tyd:** Ek het ge**help** (het + ge + werkwoord).', '**Toekomende tyd:** Ek sal / gaan help.', '**Infinitief:** te + werkwoord, bv. om te help.'], page=29),
  ],
  acts=[
    fill('Onderwerp en gesegde (enkelvoudige sinne)', '1. Die leeu pleit jammerlik by Jabu.  Onderwerp: {{1}} · Gesegde: {{2}}\n2. Die slim jakkals het hulle afgeluister.  Onderwerp: {{3}} · Gesegde: {{4}}\n3. Jakkals klap die valstrik vinnig toe.  Onderwerp: {{5}} · Gesegde: {{6}}\n4. Jabu bedank die slim jakkals.  Onderwerp: {{7}} · Gesegde: {{8}}\n5. Sipho luister aandagtig na die jagters.  Onderwerp: {{9}} · Gesegde: {{10}}',
         {1: 'Die leeu', 2: 'pleit', 3: ['Die slim jakkals', 'jakkals'], 4: ['het afgeluister', 'afgeluister'], 5: 'Jakkals', 6: ['klap toe', 'klap … toe', 'klap']  , 7: 'Jabu', 8: 'bedank', 9: 'Sipho', 10: 'luister'},
         'Wie doen iets? (onderwerp). Wat doen hy? (gesegde).', prompt='Skryf die onderwerp en die gesegde van elke sin.', src='workbook', page=28, item='1–5', status='derived_from_rule'),
    choices('Veelvoudige sinne: kies die bysin', 'Elke sin het ’n hoofsin en ’n bysin. Kies die bysin.',
            [('Jabu, die getroue veewagter, het die leeu vertrou.', ['Jabu het die leeu vertrou', 'die getroue veewagter'], 1), ('Jakkals, wat hul afgeluister het, kom nader gestap.', ['Jakkals kom nader gestap', 'wat hul afgeluister het'], 1),
             ('Jakkals, die slinkse dier van die oerwoud, het Leeu uitoorlê.', ['Jakkals het Leeu uitoorlê', 'die slinkse dier van die oerwoud'], 1), ('Leeu, wat nie sy belofte nagekom het nie, moes leer dat verbreekte beloftes jou altyd inhaal.', ['wat nie sy belofte nagekom het nie', 'Leeu moes leer dat verbreekte beloftes jou altyd inhaal'], 0)],
            'Die bysin is die deel wat by die hoofsin “ingevoeg” word en meer vertel.', src='workbook', page=28, item='veelvoudig', status='needs_review'),
    fill('Gesegdes in saamgestelde sinne', '1. Hy lig die balk wat die leeu se kop vashou.  Gesegdes: {{1}} en {{2}}\n2. Die leeu spring los en skud sy maanhare.  Gesegdes: {{3}} en {{4}}\n3. Jabu bedank die jakkals en hardloop terug na sy beeste toe.  Gesegdes: {{5}} en {{6}}\n4. Sipho sien vir Jabu en roep hom nader.  Gesegdes: {{7}} en {{8}}\n5. Die leeu brul van woede toe die valstrik hom vastrek.  Gesegdes: {{9}} en {{10}}',
         {1: 'lig', 2: 'vashou', 3: ['spring los', 'spring'], 4: 'skud', 5: 'bedank', 6: ['hardloop terug', 'hardloop'], 7: 'sien', 8: ['roep', 'roep … nader', 'roep nader'], 9: 'brul', 10: ['vastrek', 'rek vas']},
         'Soek die werkwoorde: elke werkwoord (of werkwoordstuk) is ’n gesegde.', prompt='Skryf die twee gesegdes (werkwoorde) van elke saamgestelde sin.', src='workbook', page=28, item='saamgestel', status='derived_from_rule'),
    fill('Kom ons speel met werkwoorde (1)', 'Vul die korrekte vorm van die werkwoord in.\n3. Moenie vergeet om vanaand my boek saam {{1}} nie. (bring)\n4. {{2}} hy saam met ons? (kom)\n5. Hy hou daarvan om sy toebroodjies saam met sy maats {{3}}. (eet)\n7. Ek {{4}} gister baie lank vir hulle {{5}}. (wag)\n9. Ek leer hoe om Xitsonga {{6}}. (praat)\n11. Ek het die ete klaar {{7}}. (kook)\n14. {{8}} sy vandag saam met julle? (werk)\n16. Ons juffrou {{9}} ons altyd mooi hoe om alles te doen. (wys)\n18. Die tier {{10}} verlede week op die jakkals {{11}}. (spring)\n19. Ons is almal baie lief daarvoor om {{12}}. (skryf)',
         {1: 'te bring', 2: 'Kom', 3: 'te eet', 4: 'het', 5: 'gewag', 6: 'te praat', 7: 'gekook', 8: 'Werk', 9: 'wys', 10: 'het', 11: 'gespring', 12: 'te skryf'},
         'Verlede tyd: het + ge + werkwoord. Infinitief: te + werkwoord. Teenwoordige tyd: die gewone vorm.', src='workbook', page=29, item='1–20 (a)', status='derived_from_rule'),
    fill('Kom ons speel met werkwoorde (2)', 'Vul die korrekte vorm van die werkwoord in.\n6. Volgende week {{1}} ons per bus see toe {{2}}. (reis)\n8. Ek {{3}} nie vanaand kan {{4}} nie. (gaan)\n10. Ek {{5}} nie nou al {{6}} nie. (vertrek)\n12. Ek {{7}} moet {{8}} om my boek môre saam te neem. (onthou)\n13. Ek {{9}} probeer om sokker {{10}}. (speel)\n15. As die weer volgende vakansie lekker is, {{11}} ons baie {{12}}. (swem)\n17. Hulle {{13}} vanaand baie stil moet {{14}} om nie die ander mense te steur nie. (sit)\n20. Die vleuel {{15}} verlede Saterdag tydens die wedstryd soos die wind {{16}}. (hardloop)',
         {1: ['sal', 'gaan'], 2: 'reis', 3: ['sal', 'gaan', 'kan'], 4: 'gaan', 5: ['sal', 'gaan', 'wil'], 6: 'vertrek', 7: ['sal', 'gaan'], 8: 'onthou', 9: ['gaan', 'sal'], 10: 'te speel', 11: ['sal', 'gaan'], 12: 'swem', 13: ['sal', 'gaan'], 14: 'sit', 15: 'het', 16: 'gehardloop'},
         'Toekomende tyd: sal/gaan + werkwoord. Verlede tyd: het + ge + werkwoord. Daar is soms meer as een korrekte antwoord.', src='workbook', page=29, item='1–20 (b)', status='needs_review'),
    tf('Waar of onwaar?', '’n Saamgestelde sin het net een gesegde.', False, 'Die werkboek sê: ’n saamgestelde sin het altyd twee of meer gesegdes.', status='official'),
    choices('Watter soort sin?', 'Is die sin enkelvoudig of saamgestel?', [('Jabu bedank die jakkals.', ['enkelvoudig', 'saamgestel'], 0), ('Jabu bedank die jakkals en hardloop huis toe.', ['enkelvoudig', 'saamgestel'], 1), ('Die leeu brul.', ['enkelvoudig', 'saamgestel'], 0)],
            'Tel die gesegdes: een = enkelvoudig; twee of meer = saamgestel.', status='derived_from_rule'),
  ],
  quiz=[
    q('grammar', 'Wat is die onderwerp in: “Die leeu pleit jammerlik by Jabu”?', 'Die leeu', ['pleit', 'jammerlik', 'Jabu'], 'Wie pleit? Die leeu.', status='derived_from_rule', src='workbook', page=28, item='1'),
    q('grammar', 'Wat is die gesegde in: “Jabu bedank die slim jakkals”?', 'bedank', ['Jabu', 'slim', 'jakkals'], 'Die gesegde is die werkwoord: bedank.', status='derived_from_rule', src='workbook', page=28, item='4'),
    q('grammar', 'Wat is die bepaling in: “Die leeu pleit jammerlik by Jabu”?', 'jammerlik', ['Die leeu', 'pleit', 'by'], 'Jammerlik beskryf hoe die leeu pleit (die werkwoord).', status='derived_from_rule', src='workbook', page=28),
    q('grammar', 'Hoeveel gesegdes het ’n enkelvoudige sin?', 'Net een', ['Twee', 'Drie', 'Geen'], 'Die werkboek sê ’n enkelvoudige sin het net een gesegde.', status='official', src='workbook', page=28),
    q('grammar', 'Watter sin is saamgestel?', 'Die leeu spring los en skud sy maanhare.', ['Die leeu spring los.', 'Jabu bedank die jakkals.', 'Sipho luister aandagtig.'], 'Twee gesegdes: spring los en skud.', status='derived_from_rule', src='workbook', page=28, item='saamgestel'),
    q('grammar', 'Wat is die verlede tyd van “wag”?', 'het gewag', ['sal wag', 'wag', 'gaan wag'], 'Verlede tyd: het + ge + werkwoord.', status='official', src='workbook', page=29, item='7'),
    q('grammar', 'Watter vorm is korrek: “Ek leer hoe om Xitsonga …”?', 'te praat', ['praat', 'gepraat', 'het praat'], 'Na “om” gebruik ons die infinitief: te + werkwoord.', status='derived_from_rule', src='workbook', page=29, item='9'),
    q('grammar', 'Wat is ’n veelvoudige sin?', '’n Sin met ’n hoofsin en ’n bysin', ['’n Sin met net een werkwoord', '’n Sin met net een woord', '’n Vraag'], 'Dit is die werkboek se verduideliking.', status='official', src='workbook', page=28),
  ])

# ============================================================== 79 ’n Vriendskaplike brief
LETTER = ['Olifantstraat 7', 'Middelburg', 'Mpumalanga', '1050', '1 Augustus 2015', 'Liewe Bianca'] + [
  'Eerstens wil ek dankie sê omdat jy die afgelope vakansie by my kom kuier het. Ek vertrou dit gaan baie goed met jou en jou familie.',
  'Ons het die afgelope week by die skool ’n fiksieverhaal behandel. Die karakters was Jabu, Sipho, Leeu, Jakkals en jagters.',
  'Jabu het beeste opgepas toe Sipho hom nooi om saam met hom te gaan kyk hoe die jagters valstrikke vir die leeu stel. Jabu het die uitnodiging egter van die hand gewys aangesien hy die beeste rivier toe moes neem. Terwyl hy die beeste opgepas het, het hy die leeu hoor brul, maar dit was ’n benoude brul. Hy het ondersoek gaan instel en gesien dat die leeu in een van die jagters se valstrikke vasgevang was.',
  'Die leeu het Jabu gesmeek om hom te bevry. Hy het hom belowe dat hy hom nie sou opvreet nie. Jabu het die leeu bevry, maar toe wou die leeu Jabu bespring. Net toe het die slinkse jakkals sy verskyning maak.',
  'Die jakkals oortuig die leeu toe om hom te gaan wys hoe hy in die valstrik vasgesit het. Net toe die leeu sy kop onder die valstrik se balk indruk, klap die jakkals die valstrik toe en daar sit die leeu toe weer in die valstrik vas.',
  'Die sedeles wat ons uit hierdie Zulu-fabel geleer het, was: Verbreekte beloftes haal jou altyd in!',
  'Mag jy ’n suksesvolle en voorspoedige kwartaal beleef by die skool en by die huis.'] + ['Groete', 'Chantelle']  # list of paragraphs

L79 = lesson(79,
  skills=[LISTEN, READ, WRITE],
  intro='Een brief kan baie vertel. Luister na ’n vriendskaplike brief en skryf dan self een aan jou maat.',
  objectives=['Na die voorlesing van ’n vriendskaplike brief luister.', 'Die dele van ’n brief uitken (adres, datum, aanhef, inhoud, slot).', '’n Vriendskaplike brief volgens die korrekte formaat skryf.'],
  pass_=passage('’n Vriendskaplike brief', LETTER, glossary=[('benoude', 'Bang of angstig.'), ('uitnodiging', 'Wanneer iemand jou vra om iewers saam te kom.'), ('oortuig', 'Iemand oortuig dat jy reg is.'), ('sedeles', 'Die les wat ’n storie ons leer.'), ('voorspoedige', 'Suksesvol en met geluk.')]),
  learn=[
    table('Dele van ’n vriendskaplike brief', ['Deel', 'Voorbeeld uit die brief'], [['Adres (straat, dorp, provinsie, poskode)', 'Olifantstraat 7, Middelburg, Mpumalanga, 1050'], ['Datum', '1 Augustus 2015'], ['Aanhef', 'Liewe Bianca'], ['Inhoud', 'Eerstens wil ek dankie sê …'], ['Slot en groet', 'Groete, Chantelle']], src='supplementary', page=30),
  ],
  acts=[
    discuss('Luister na die brief', 'Luister na hierdie brief terwyl jou onderwyser dit vir jou voorlees. (Jy kan ook die knoppie druk.)', src='workbook', speak='passage', page=30, item='Ons lees'),
    sa('Wie skryf aan wie?', 'Wie skryf die brief en aan wie?', 'Chantelle skryf die brief aan Bianca.', lines=1, src='supplementary', status='derived_from_text'),
    sa('Waaroor gaan die brief?', 'Waaroor skryf Chantelle in die brief?', 'Sy dank Bianca vir die kuier en vertel haar van ’n fiksieverhaal (’n Zulu-fabel oor Jabu en die leeu) wat hulle by die skool behandel het.', lines=3, src='supplementary', status='derived_from_text'),
    choices('Watter deel van die brief is dit?', 'Kies die deel van die brief.',
            [('Olifantstraat 7', ['adres', 'datum', 'aanhef', 'groet'], 0), ('1 Augustus 2015', ['adres', 'datum', 'aanhef', 'groet'], 1), ('Liewe Bianca', ['adres', 'datum', 'aanhef', 'groet'], 2), ('Groete, Chantelle', ['adres', 'datum', 'aanhef', 'groet'], 3)],
            'Die adres staan bo-aan, dan die datum, die aanhef, die inhoud en laaste die groet.', src='supplementary', status='derived_from_text'),
    order('Die dele van ’n brief in volgorde', 'Sit die dele van ’n vriendskaplike brief in die regte volgorde.', ['Adres', 'Datum', 'Aanhef (Liewe …)', 'Inhoud', 'Slot en groet'], 'Volgorde: adres, datum, aanhef, inhoud, slot en groet.', perm=[3, 0, 4, 1, 2], src='supplementary', status='derived_from_rule'),
    writing('Skryf jou eie brief', 'Skryf ’n brief aan jou maat waarin jy hom of haar vertel van ’n fiksieverhaal wat jy gehoor of gelees het.',
            checklist=['Ek het my straatnaam en -nommer geskryf.', 'Ek het my dorp, provinsie en poskode geskryf.', 'Ek het die datum geskryf.', 'Ek het begin met “Beste …” of “Liewe …”.', 'Ek het die verhaal vertel en die sedeles genoem.', 'Ek het ’n slot geskryf (bv. “Beste wense”) en my naam.', 'Ek het my spelling en punktuasie gekorrigeer.'],
            tips=['Beplan jou brief deur ’n geheuekaart in jou klaswerkboek op te stel.'] + WRITE_PROCESS[1:], lines=14, page=31, item='Ons skryf'),
    tf('Waar of onwaar?', 'In ’n vriendskaplike brief kom die datum bo-aan die brief.', True, 'Die adres en die datum staan bo-aan, voor die aanhef.', status='derived_from_text'),
    fill('Voltooi die brief', 'Ons begin ’n vriendskaplike brief met “{{1}} Bianca” en ons sluit af met “{{2}}”.', {1: ['Liewe', 'Beste'], 2: ['Groete', 'Beste wense']}, 'Chantelle begin met “Liewe Bianca” en sluit af met “Groete”.', bank=['Liewe', 'Groete', 'Môre'], status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Wie skryf die brief?', 'Chantelle', ['Bianca', 'Jabu', 'Sipho'], 'Die brief eindig met “Groete, Chantelle”.', ev=['Chantelle']),
    q('literal', 'Aan wie is die brief gerig?', 'Bianca', ['Chantelle', 'Jakkals', 'Die onderwyser'], 'Die aanhef is “Liewe Bianca”.', ev=['Liewe Bianca']),
    q('literal', 'In watter straat woon Chantelle?', 'Olifantstraat', ['Leeustraat', 'Jakkalsstraat', 'Skoolstraat'], 'Die adres bo-aan is Olifantstraat 7.', ev=['Olifantstraat 7']),
    q('literal', 'Wat is die datum van die brief?', '1 Augustus 2015', ['15 Augustus 2015', '1 Julie 2015', '1 Augustus 2005'], 'Die datum staan bo-aan die brief.', ev=['1 Augustus 2015']),
    q('literal', 'Waarvoor dank Chantelle vir Bianca?', 'Dat sy in die vakansie kom kuier het', ['Vir ’n present', 'Vir ’n brief', 'Vir ’n boek'], 'Sy skryf: “Eerstens wil ek dankie sê omdat jy die afgelope vakansie by my kom kuier het.”', ev=['Eerstens wil ek dankie sê']),
    q('main_idea', 'Wat is die sedeles van die fabel in die brief?', 'Verbreekte beloftes haal jou altyd in.', ['Leeus is gevaarlik.', 'Jy moet jagters help.', 'Kinders moet nie by riviere speel nie.'], 'Dit staan in die tweede-laaste paragraaf van die brief.', ev=['Die sedeles wat ons uit hierdie Zulu-fabel geleer het']),
    q('grammar', 'Wat staan altyd bo-aan ’n vriendskaplike brief?', 'Die adres en die datum', ['Die groet', 'Die sedeles', 'Die handtekening'], 'Eers kom die adres en datum, dan die aanhef.', status='derived_from_rule', src='supplementary'),
    q('grammar', 'Watter groet pas by ’n vriendskaplike brief?', 'Groete of Beste wense', ['Hoogagtend', 'Aan wie dit mag aangaan', 'Geagte Meneer'], 'Chantelle sluit af met “Groete”; die werkboek se sjabloon het “Beste wense”.', status='derived_from_text', src='supplementary', page=31),
  ])

# ============================================================== 80 Voeg hulle saam
L80 = lesson(80,
  intro='Voegwoorde is die “gom” wat sinne verbind. Vandag voeg jy sinne saam, ontdek jy afkortings en oefen jy die lydende vorm.',
  objectives=['Voegwoorde gebruik om saamgestelde sinne te vorm.', 'Die werkwoorde in saamgestelde sinne uitwys.', 'Afkortings, akronieme en verkortings opsoek.', 'Woorddele (afleidings en samestellings) uitken.', 'Sinne in die lydende vorm skryf.'],
  learn=[
    text('Voegwoorde', 'Ons gebruik voegwoorde om sinne te verbind. Hulle speel ’n belangrike rol, want sonder voegwoorde sou ons spraak en skryfwerk rukkerig gewees het.',
         bullets=['Voegwoorde in hierdie les: **en, omdat, daarom, maar, terwyl, alhoewel**.', 'Ons gebruik ook “**egter**” om sinne saam te voeg. Egter beteken dieselfde as maar – albei wys ’n kontras tussen twee dele van die sin.'], page=32),
    table('Voorbeeld: twee sinne word een', ['Twee enkelvoudige sinne', 'Een saamgestelde sin'], [['Gerrie het skielik omgedraai. Gerrie het hom teen die tafel gestamp.', 'Gerrie het skielik omgedraai **en** hom teen die tafel gestamp.']], page=32),
    note('Gerrie is die onderwerp van albei sinne, daarom hoef jy sy naam net een keer te sê. Soms moet die woordorde aangepas word wanneer sinne saamgestel word.', title='Onthou', page=32),
    note('’n Enkelvoudige sin het een onderwerp en een werkwoord. ’n Saamgestelde sin het meer as een werkwoord en mag meer as een onderwerp hê.', title='Enkelvoudig of saamgestel?', page=32),
  ],
  acts=[
    match('Verbind die sinne met ’n voegwoord', 'Verbind elke paar enkelvoudige sinne met die voegwoord wat die beste pas.',
          [('Sipho nooi Jabu saam. Jabu moet die beeste oppas.', 'maar'), ('Leeu het ’n koei gevang. Die jagters het valstrikke gestel.', 'daarom'), ('Jabu hoor ’n leeu brul. Jabu pas beeste op.', 'terwyl'),
           ('Jabu gaan stel ondersoek in. Hy sien Leeu sit vas in ’n valstrik.', 'en'), ('Leeu het nie sy belofte nagekom nie. Jabu het leeu bevry.', 'alhoewel'), ('Jakkals klap die valstrik toe. Leeu het nie sy belofte nagekom nie.', 'omdat')],
          'Daar kan soms meer as een voegwoord pas, maar dit is die beste passing by die betekenis.', src='workbook', page=32, item='voegwoorde', status='needs_review'),
    sa('Skryf die saamgestelde sinne', 'Skryf die ses saamgestelde sinne neer en onderstreep die werkwoorde.',
       'Sipho nooi Jabu saam, maar Jabu moet die beeste oppas.\nLeeu het ’n koei gevang, daarom het die jagters valstrikke gestel.\nJabu hoor ’n leeu brul terwyl hy beeste oppas.\nJabu gaan stel ondersoek in en sien Leeu sit vas in ’n valstrik.\nAlhoewel Jabu leeu bevry het, het Leeu nie sy belofte nagekom nie.\nJakkals klap die valstrik toe omdat Leeu nie sy belofte nagekom het nie.', lines=8, page=32, item='sinne', status='needs_review'),
    fill('Voegwoord invul', 'Die jagters stel valstrikke {{1}} Jabu pas die beeste op. Jabu moes die beeste oppas, {{2}} hy is nie saam met Sipho nie.', {1: ['terwyl', 'en'], 2: ['daarom', 'want', 'omdat']}, 'Terwyl wys twee dinge wat gelyktydig gebeur; daarom wys ’n gevolg.', bank=['terwyl', 'daarom', 'maar'], src='supplementary', status='derived_from_rule'),
    match('Afkortings en betekenisse', 'Gebruik jou woordeboek: verbind elke afkorting met sy betekenis.', [('alg.', 'algemeen'), ('ens.', 'ensovoorts'), ('cm', 'sentimeter'), ('RSA', 'Republiek van Suid-Afrika'), ('NASA', 'Amerikaanse ruimte-agentskap (National Aeronautics and Space Administration)')],
          'Hierdie is uit die tabel in die werkboek (bladsy 33).', src='workbook', page=33, item='afkortings', status='derived_from_rule'),
    choices('Afleiding of samestelling?', 'Is die woord ’n afleiding of ’n samestelling?', [('jammerlik', ['afleiding', 'samestelling'], 0), ('vashou', ['afleiding', 'samestelling'], 1), ('vermors', ['afleiding', 'samestelling'], 0), ('verskriklike', ['afleiding', 'samestelling'], 0)],
            'Samestelling = basis + basis (vas + hou). Afleiding = basis + voorvoegsel/agtervoegsel (jammer + -lik; ver- + mors).', src='workbook', page=33, item='woorddele', status='derived_from_rule'),
    sa('Skryf in die lydende vorm', 'Onderstreep die onderwerp en die voorwerp. Skryf dan die sinne in die lydende vorm oor: Die jagters stel valstrikke. / Jabu pas beeste op. / Sipho hou die jagters dop. / Leeu maak ’n belofte. / Jabu bevry die leeu. / Jakkals help vir Jabu.',
       'Valstrikke word deur die jagters gestel.\nBeeste word deur Jabu opgepas.\nDie jagters word deur Sipho dopgehou.\n’n Belofte word deur Leeu gemaak.\nDie leeu word deur Jabu bevry.\nJabu word deur Jakkals gehelp.', lines=7, page=33, item='lydende vorm', status='derived_from_rule'),
    tf('Waar of onwaar?', '“Egter” beteken dieselfde as “maar”.', True, 'Die werkboek sê egter beteken dieselfde as maar; albei wys ’n kontras.', status='official'),
    ek_kan(EK_KAN_T5, 34),
  ],
  quiz=[
    q('grammar', 'Watter voegwoord pas: “Sipho nooi Jabu saam, ___ Jabu moet die beeste oppas”?', 'maar', ['daarom', 'omdat', 'en'], 'Daar is ’n kontras tussen die uitnodiging en Jabu se plig.', status='needs_review', src='workbook', page=32),
    q('grammar', 'Watter voegwoord wys ’n gevolg?', 'daarom', ['maar', 'en', 'terwyl'], 'Daarom wys die gevolg van iets, bv. Leeu het ’n koei gevang, daarom stel die jagters valstrikke.', status='derived_from_rule', src='workbook', page=32),
    q('grammar', 'Watter voegwoord wys dat twee dinge gelyktydig gebeur?', 'terwyl', ['omdat', 'maar', 'alhoewel'], 'Jabu hoor die leeu terwyl hy beeste oppas.', status='derived_from_rule', src='workbook', page=32),
    q('vocabulary', 'Wat beteken “egter”?', 'Dieselfde as “maar”', ['Dieselfde as “en”', 'Dieselfde as “omdat”', 'Dieselfde as “daarom”'], 'Die werkboek sê egter beteken dieselfde as maar.', status='official', src='workbook', page=32),
    q('grammar', 'Wat is ’n saamgestelde sin?', '’n Sin met meer as een werkwoord', ['’n Sin met net een woord', '’n Sin sonder onderwerp', '’n Vraag'], 'Dit is die werkboek se verduideliking.', status='official', src='workbook', page=32),
    q('vocabulary', 'Waarvoor staan “ens.”?', 'ensovoorts', ['ensiklopedie', 'enigste', 'eenvoudig'], 'Ens. is ’n gewone afkorting vir ensovoorts.', status='derived_from_rule', src='workbook', page=33, item='afkortings'),
    q('vocabulary', 'Watter woord is ’n samestelling?', 'vashou', ['jammerlik', 'vermors', 'verskriklike'], 'Vashou = vas + hou.', status='derived_from_rule', src='workbook', page=33, item='woorddele'),
    q('grammar', 'Wat is die lydende vorm van: “Jabu bevry die leeu”?', 'Die leeu word deur Jabu bevry.', ['Jabu word deur die leeu bevry.', 'Die leeu bevry Jabu.', 'Jabu het die leeu bevry.'], 'Die voorwerp (die leeu) word die onderwerp.', status='derived_from_rule', src='workbook', page=33, item='lydende vorm'),
  ])
