import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

REPORT_CHECK = ['Ek het minstens twee sinne oor elke vraag geskryf.', 'Ek het gesê hoeveel maats ja en hoeveel nee gesê het.', 'Ek het my eie mening bygevoeg.', 'Ek het my spelling en punktuasie gekorrigeer.']

# ============================================================== 102 Gebruik 'n onderhoudsvraelys
L102 = lesson(102,
  skills=[LISTEN, WRITE],
  intro='Hoe vind ons uit wat mense dink? Ons gebruik ’n onderhoudsvraelys! Vandag doen jy ’n opname oor die skoolstelsel, teken die bevindinge aan en skryf ’n verslag.',
  objectives=['Verstaan hoekom ons ’n vraelys vir ’n onderhoud gebruik.', '’n Onderhoud voer met ’n vraelys en die bevindinge aanteken.', '’n Verslag oor die bevindinge skryf.'],
  learn=[
    text('Hoekom ’n vraelys?', bullets=['Hoe vind ons uit of mense van iemand of iets hou of nie? Een manier is om met hulle ’n onderhoud te voer en te vra wat hulle van die persoon of ding dink.', 'So ’n onderhoud moet voorberei word, anders vergeet ons dalk watter vrae om te stel of vra ons die verkeerde vrae.', 'Daarom stel ons ’n **vraelys** op wat ons tydens die onderhoud kan gebruik.'], page=78),
    text('Jou opname', bullets=['Gebruik die vraelys om uit te vind wat jou maats van die skoolstelsel dink en wat hulle graag sou wil verander.', 'By die laaste vraag staan “Ander”. Daar kan jy enige vraag van jou keuse invul, solank dit oor dieselfde onderwerp handel.', 'Vra **tien maats** om ja of nee op hierdie vrae te antwoord.', 'Maak ’n regmerkie vir ja of ’n kruisie vir nee in die kolomme langs die vrae.'], page=78),
  ],
  acts=[
    discuss('Ons doen: die opname', 'Gebruik hierdie vraelys om uit te vind wat jou maats van die skoolstelsel dink. Vra tien maats om ja of nee te antwoord op: 1. Ons behoort toegelaat te word om enige klere skool toe te dra, nie net skooldrag nie. 2. Ons behoort sport voor skool te beoefen, wanneer dit koeler is. 3. Die skooldag moet langer gemaak word om huiswerk onnodig te maak. 4. Aparte skole vir seuns en meisies is beter as gemengde skole. 5. Kinders behoort oor skoolreëls geraadpleeg te word. 6. Ander.', page=78, item='Ons doen'),
    match('Pas die stelling by die opskrif in die tabel', 'Verbind elke stelling met die opskrif in Tabel 1.', [('Ons behoort enige klere skool toe te dra.', 'Skaf skooldrag af'), ('Ons behoort sport voor skool te beoefen.', 'Oggendsport'), ('Die skooldag moet langer gemaak word.', 'Langer skooldae'), ('Aparte skole vir seuns en meisies is beter.', 'Aparte skole'), ('Kinders behoort oor skoolreëls geraadpleeg te word.', 'Raadpleging oor reëls')],
          'Die werkboek se tabel gebruik hierdie opskrifte.', src='workbook', page=78, item='tabel 1', status='derived_from_text'),
    writing('Vul jou resultate in', 'Vul die resultate van jou onderhoude in: hoeveel maats het met elke stelling saamgestem (regmerkies) en hoeveel het nie (kruisies)?', checklist=['Ek het tien maats gevra.', 'Ek het die totale ja’s en nee’s getel.', 'Ek het die tabel ingevul.'], lines=6, page=78, item='tabel 1'),
    writing('Skryf die bevindinge: vraag 1 tot 6', 'Beantwoord: Vraag 1: Het jou maats saamgestem dat hulle enige klere waarvan hulle hou, skool toe behoort te kan dra? Vraag 2: Wat het jou maats van sport voor skool gedink? Vraag 3: Het jou maats saamgestem dat die skooldag verleng behoort te word? Vraag 4: Verkies jou maats gemengde skole of aparte skole? Vraag 5: Het jou maats saamgestem dat leerders oor skoolreëls geraadpleeg behoort te word? Vraag 6: Watter “ander” vraag het jy gestel en wat het jou maats geantwoord?',
            checklist=REPORT_CHECK[:2], lines=10, page=79, item='vrae 1–6'),
    writing('Skryf jou verslag', 'Noudat jy uitgevind het hoe hulle oor hierdie sake voel, hoe dink jy behoort die skoolstelsel verander te word? Skryf nou ’n verslag oor jou bevindinge. Skryf minstens twee sinne oor elke vraag.', checklist=REPORT_CHECK, lines=14, page=79, item='verslag'),
    order('Die stappe van ’n opname', 'Sit die stappe in die regte volgorde.', ['Stel ’n vraelys met stellings op.', 'Vra tien maats om ja of nee te antwoord.', 'Maak ’n regmerkie of kruisie by elke vraag.', 'Tel die totale ja’s en nee’s.', 'Skryf ’n verslag oor die bevindinge.'], 'So werk ’n opname met ’n onderhoudsvraelys.', perm=[3, 0, 4, 1, 2], src='supplementary', status='derived_from_text'),
    tf('Waar of onwaar?', 'By “Ander” kan jy enige vraag invul, solank dit oor dieselfde onderwerp handel.', True, 'Die werkboek sê dit by die laaste vraag.', src='supplementary', status='official'),
  ],
  quiz=[
    q('main_idea', 'Hoekom stel ons ’n vraelys op vir ’n onderhoud?', 'Sodat ons nie vergeet watter vrae om te stel nie', ['Om die onderhoud langer te maak', 'Om mense te laat lag', 'Om die antwoorde te kan raai'], 'Die werkboek sê ’n onderhoud moet voorberei word.', status='official', src='supplementary', page=78),
    q('literal', 'Hoeveel maats moet jy vra om ja of nee te antwoord?', 'Tien', ['Twee', 'Vyf', 'Twintig'], 'Die werkboek sê: vra tien maats.', status='official', src='workbook', page=78),
    q('literal', 'Wat maak jy as ’n maat ja sê?', '’n Regmerkie', ['’n Kruisie', '’n Sirkel', 'Niks'], 'Die werkboek sê: regmerkie vir ja, kruisie vir nee.', status='official', src='workbook', page=78),
    q('literal', 'Wat maak jy as ’n maat nee sê?', '’n Kruisie', ['’n Regmerkie', '’n Sterretjie', 'Niks'], 'Kruisie vir nee.', status='official', src='workbook', page=78),
    q('literal', 'Wat staan by die laaste vraag in die vraelys?', 'Ander', ['Totaal', 'Ja', 'Nee'], 'By die laaste vraag staan “Ander”.', status='official', src='workbook', page=78),
    q('main_idea', 'Waaroor gaan die opname in hierdie werkkaart?', 'Die verandering van die skoolstelsel', ['Sokker', 'Haustiere', 'Weerberigte'], 'Die opskrif van die tabel is “Bevindinge van opname oor verandering van die skoolstelsel”.', status='official', src='workbook', page=78),
    q('main_idea', 'Hoeveel sinne moet jy minstens oor elke vraag in jou verslag skryf?', 'Twee', ['Een', 'Vyf', 'Tien'], 'Skryf minstens twee sinne oor elke vraag.', status='official', src='workbook', page=79),
    q('vocabulary', 'Wat is ’n vraelys?', '’n Lys vrae wat jy tydens ’n onderhoud kan gebruik', ['’n Soort gedig', '’n Brief aan ’n maat', '’n Prent van ’n skool'], 'Die werkboek verduidelik: ons stel ’n vraelys op wat ons tydens die onderhoud kan gebruik.', status='official', src='supplementary', page=78),
  ])

# ============================================================== 103 Taalstrukture en -konvensies
L103 = lesson(103,
  skills=[LANG, WRITE],
  intro='Vandag werk jy met woordvorming, die ontkennende vorm, taalverskynsels (versagting, oordrywing, dubbelsinnigheid), idiome en afkortings.',
  objectives=['Basiswoorde, afleidings en samestellings uitken.', 'Sinne in die ontkennende vorm skryf.', 'Taalverskynsels herken (versagting, oordrywing, dubbelsinnigheid).', 'Idiome met hulle betekenisse verbind en afkortings opspoor.'],
  learn=[
    text('Woordvorming', bullets=['**Basiswoorde:** die kleinste sinvolle deel van ’n woord.', '**Afleidings:** basis + voorvoegsel en/of agtervoegsel of verbindingsklank.', '**Samestellings:** basis + basis.'], page=80),
    text('Die ontkennende vorm', 'In die ontkennende vorm word sake in die negatiewe vorm gestel, bv. Sy het nie gebel nie.', bullets=['Ons gebruik die **dubbele nie**, bv. Ek wil nie ’n onderhoud voer nie.', 'As die sin net ’n onderwerp bevat, gebruik ons net **een nie**, bv. Ek sal nie.', 'Gebruik woorde soos **moenie** saam met die woord **nie** in bevelsinne, bv. Moenie van my verwag om ’n onderhoud te voer nie!'], page=80),
    note('Ons kan ons taal bewustelik verryk deur sommige van hierdie tegnieke toe te pas: **versagting**, **oordrywing** en **dubbelsinnigheid**.', title='Taalverskynsels', page=81),
    note('Idiomatiese uitdrukkings is uitdrukkings wat eie aan die taal is. Idiome sluit spreekwoorde, segswyses, gesegdes en spreuke in.', title='Idiome', page=81),
  ],
  acts=[
    choices('Afleiding of samestelling?', 'Hierdie woorde kom uit Bobby se onderhoud. Afleiding of samestelling?', [('tienertyd', ['afleiding', 'samestelling'], 1), ('luisteraars', ['afleiding', 'samestelling'], 0), ('musiekster', ['afleiding', 'samestelling'], 1), ('laerskole', ['afleiding', 'samestelling'], 1), ('musiekbedryf', ['afleiding', 'samestelling'], 1)],
            'Samestelling = basis + basis (musiek + ster). Afleiding = basis + voor-/agtervoegsel (luister + -aar + -s).', src='workbook', page=80, item='tabel', status='derived_from_rule'),
    sa('Die ontkennende vorm', 'Skryf hierdie sinne in die ontkennende vorm: Sy onderhoud het baie goed afgeloop. / Die kinders se opnames was suksesvol. / Jy moet jou opname voltooi!', 'Sy onderhoud het nie baie goed afgeloop nie.\nDie kinders se opnames was nie suksesvol nie.\nJy moet nie jou opname voltooi nie! (of: Moenie jou opname onvoltooid laat nie!)', lines=4, page=80, item='ontkenning', status='derived_from_rule'),
    match('Taalverskynsels en hul betekenisse', 'Verbind elke woord links met sy betekenis regs.', [('versagting', 'verbloeming'), ('oordrywing', 'vergroting; verergering'), ('dubbelsinnig', 'met meer as een betekenis of vertolking')], 'Versagting maak iets sagter (’n eufemisme); oordrywing maak iets groter.', src='workbook', page=81, item='woorde', status='derived_from_rule'),
    choices('Watter taalverskynsel?', 'Dui die taalverskynsel in elke sin aan.', [('Ek het geluister na die gesing van die voëls wat deur die venster gekom het.', ['versagting', 'oordrywing', 'dubbelsinnig'], 2), ('As iemand dood is kan ons sê hy of sy het ontslaap.', ['versagting', 'oordrywing', 'dubbelsinnig'], 0),
             ('Hy gil en skree altyd.', ['versagting', 'oordrywing', 'dubbelsinnig'], 1), ('Ek het my doodgelag.', ['versagting', 'oordrywing', 'dubbelsinnig'], 1), ('Jy moet jou boek op die stoel lees.', ['versagting', 'oordrywing', 'dubbelsinnig'], 2)],
            'Dubbelsinnig = twee moontlike betekenisse; versagting = sagter sê; oordrywing = groter maak.', src='workbook', page=81, item='sinne', status='derived_from_rule'),
    match('Idiome en hul betekenisse', 'Verbind elke idioom met sy betekenis.', [('altyd op dieselfde aambeeld hamer', 'altyd oor dieselfde dinge praat'), ('kaatjie van die baan', 'die voorste pretmaker'), ('in die war wees', 'verward wees'), ('die gelag betaal', 'die gevolge dra'), ('te dik vir ’n daalder', 'onmoontlik om te glo')],
          'Idiome het ’n figuurlike betekenis.', src='workbook', page=81, item='idiome', status='derived_from_rule'),
    sa('Afkortings in die onderhoud', 'Voltooi die tabel deur 3 afkortings in die onderhoud met Bobby van Jaarsveld te soek. Skryf hulle en hulle betekenisse neer.', 'a.g.v. = as gevolg van\nnl. = naamlik\no.a. = onder andere', lines=4, page=81, item='afkortings', status='derived_from_text'),
    tf('Waar of onwaar?', 'In ’n ontkennende sin sonder voorwerp gebruik ons net een “nie”, bv. Ek sal nie.', True, 'Die werkboek sê: as die sin net ’n onderwerp bevat, gebruik ons net een nie.', src='supplementary', status='official'),
  ],
  quiz=[
    q('grammar', 'Watter woord is ’n samestelling?', 'musiekster', ['luisteraars', 'onderhoude', 'verskaf'], 'Musiek + ster.', status='derived_from_rule', src='workbook', page=80, item='tabel'),
    q('grammar', 'Watter sin is in die ontkennende vorm?', 'Ek wil nie ’n onderhoud voer nie.', ['Ek wil ’n onderhoud voer.', 'Ek het ’n onderhoud gevoer.', 'Ek sal ’n onderhoud voer.'], 'Die werkboek gebruik hierdie sin as voorbeeld.', status='official', src='workbook', page=80),
    q('grammar', 'Watter woord gebruik ons saam met “nie” in bevelsinne?', 'moenie', ['sal', 'het', 'is'], 'Voorbeeld: Moenie van my verwag om ’n onderhoud te voer nie!', status='official', src='workbook', page=80),
    q('vocabulary', 'Wat beteken “oordrywing”?', 'Vergroting of verergering', ['Verbloeming', 'Met twee betekenisse', 'Verkleining'], 'Die werkboek koppel oordrywing aan vergroting; verergering.', status='derived_from_rule', src='workbook', page=81, item='woorde'),
    q('inference', 'Watter taalverskynsel is “Ek het my doodgelag”?', 'Oordrywing', ['Versagting', 'Dubbelsinnigheid', 'Geen een nie'], 'Niemand lag werklik dood nie – dit is ’n oordrywing.', status='derived_from_rule', src='workbook', page=81, item='sinne'),
    q('inference', 'Watter taalverskynsel is “hy of sy het ontslaap”?', 'Versagting', ['Oordrywing', 'Dubbelsinnigheid', 'Beeldspraak'], 'Ontslaap is ’n sagter manier om te sê iemand is dood.', status='derived_from_rule', src='workbook', page=81, item='sinne'),
    q('vocabulary', 'Wat beteken die idioom “die gelag betaal”?', 'Die gevolge dra', ['Baie geld hê', 'Pret maak', 'Onmoontlik glo'], 'Dit is die betekenis volgens die werkboek.', status='derived_from_rule', src='workbook', page=81, item='idiome'),
    q('vocabulary', 'Waarvoor staan “a.g.v.”?', 'as gevolg van', ['aan gaan van', 'alles goed vir', 'agter geboue van'], 'Die afkorting kom in Bobby se onderhoud voor.', status='derived_from_text', src='workbook', page=81, item='afkortings'),
  ])

# ============================================================== 104 Ontwerp 'n onderhoudsvraelys
L104 = lesson(104,
  skills=[LISTEN, WRITE],
  intro='Nou is dit jou beurt om jou eie onderhoudsvraelys te ontwerp! Kies ’n onderwerp, skryf ses stellings, vra tien maats en skryf ’n verslag.',
  objectives=['’n Eie onderhoudsvraelys op ’n templaat ontwerp.', 'Tien maats ondervra en die bevindinge aanteken.', '’n Verslag oor die bevindinge skryf.'],
  learn=[
    text('Ontwerp jou vraelys', bullets=['Kies ’n **onderwerp** wat jy wil navors en skryf dit boaan die onderhoudsvraelys.', 'Stel **6 stellings of vrae** saam en vul dit in die eerste kolom by nommer 1 tot 6 in.', 'Vra **tien maats** om ja of nee op hierdie stellings of vrae te antwoord.', 'Vul ’n regmerkie vir ja en ’n kruisie vir nee in die kolomme langs die vrae.', 'Vul die totale getal regmerkies of kruisies in.'], page=82),
  ],
  acts=[
    writing('My onderwerp en ses stellings', 'Kies ’n onderwerp wat jy wil navors en skryf dit neer. Stel dan ses stellings of vrae saam.', checklist=['Ek het ’n onderwerp gekies.', 'Ek het ses stellings of vrae geskryf.', 'Elke stelling kan met ja of nee beantwoord word.'], lines=8, page=82, item='onderwerp'),
    choices('Is dit ’n goeie stelling vir ja of nee?', 'Kan jy hierdie stelling met ja of nee beantwoord?', [('Ons behoort meer pouses te kry.', ['Ja', 'Nee'], 0), ('Hoe voel jy oor pouses?', ['Ja', 'Nee'], 1), ('Skoolwerk moet minder wees.', ['Ja', 'Nee'], 0), ('Waarom hou jy van sokker?', ['Ja', 'Nee'], 1)],
            'By ’n ja/nee-vraelys is die stellings sodat mens saam kan stem of nie.', src='supplementary', status='derived_from_rule'),
    discuss('Ondervra tien maats', 'Vra tien maats om ja of nee te antwoord op jou stellings. Maak ’n regmerkie of kruisie. Tel die totale ja’s en nee’s.', page=82, item='Ons doen'),
    writing('Skryf die bevindinge', 'Skryf by elke vraag (vraag 1 tot 6) wat jou maats geantwoord het.', checklist=['Ek het by elke vraag geskryf wat my maats gesê het.'], lines=10, page=83, item='vrae 1–6'),
    writing('Hoe voel jy self?', 'Noudat jy uitgevind het hoe hulle oor hierdie sake voel, som op hoe jy self daaroor voel.', lines=5, page=83, item='self'),
    writing('Skryf jou verslag', 'Skryf nou ’n verslag oor jou bevindinge. Skryf minstens twee sinne oor elke vraag.', checklist=REPORT_CHECK, lines=14, page=83, item='verslag'),
    tf('Waar of onwaar?', 'Jy moet ses stellings of vrae in jou vraelys skryf.', True, 'Die werkboek sê: stel 6 stellings/vrae saam.', src='supplementary', status='official'),
  ],
  quiz=[
    q('main_idea', 'Hoeveel stellings of vrae stel jy saam?', 'Ses', ['Een', 'Drie', 'Twintig'], 'Die werkboek sê: 6 stellings/vrae.', status='official', src='workbook', page=82),
    q('main_idea', 'Hoeveel maats ondervra jy?', 'Tien', ['Twee', 'Ses', 'Honderd'], 'Vra tien maats.', status='official', src='workbook', page=82),
    q('main_idea', 'Waar skryf jy die onderwerp?', 'Boaan die onderhoudsvraelys', ['Onder die antwoorde', 'In die kantlyn', 'Nêrens nie'], 'Skryf dit boaan die onderhoudsvraelys.', status='official', src='workbook', page=82),
    q('main_idea', 'Wat gebruik jy om ja te antwoord?', '’n Regmerkie', ['’n Kruisie', '’n Sterretjie', '’n Vraagteken'], 'Regmerkie vir ja; kruisie vir nee.', status='official', src='workbook', page=82),
    q('sequencing', 'Wat doen jy EERSTE?', 'Kies ’n onderwerp', ['Skryf die verslag', 'Tel die ja’s', 'Vra tien maats'], 'Die eerste stap in die werkboek is om ’n onderwerp te kies.', status='official', src='workbook', page=82),
    q('main_idea', 'Wat doen jy ná jy tien maats gevra het?', 'Vul die totale ja’s en nee’s in en skryf ’n verslag', ['Begin oor', 'Gooi die vraelys weg', 'Stuur dit per e-pos'], 'Vul die totale getal in en skryf ’n verslag.', status='official', src='workbook', page=82),
    q('grammar', 'Watter een is ’n goeie stelling vir ’n ja/nee-vraelys?', 'Skoolwerk moet minder wees.', ['Hoe voel jy oor skool?', 'Waarom hou jy van pouses?', 'Wat is jou gunstelingvak?'], 'Op ’n stelling kan mens ja of nee antwoord.', status='derived_from_rule', src='supplementary'),
    q('main_idea', 'Hoeveel sinne skryf jy minstens per vraag in die verslag?', 'Twee', ['Een', 'Agt', 'Geen'], 'Skryf minstens twee sinne oor elke vraag.', status='official', src='workbook', page=83),
  ])

# ============================================================== 105 Taalstrukture en -konvensies
L105 = lesson(105,
  skills=[LANG, WRITE],
  intro='Spelling, meervoude, verkleinwoorde, direkte rede en leestekens – vandag hersien jy belangrike taalreëls.',
  objectives=['Die korrekte spelling kies met die hulp van spelreëls.', 'Meervoude en verkleinwoorde vorm.', 'Sinne in die direkte rede skryf.', 'Hoofletters en lees- en skryftekens korrek gebruik.'],
  learn=[
    text('Spelreëls en spelpatrone', bullets=['As jy nie seker is of ’n woord met ’n -d of ’n -t eindig nie, sê die meervoud of vorm ’n ander woord, bv. hond – honde, goed – goedere.', 'V staan nooit aan die einde van ’n woord of lettergreep nie.', '**y/ei:** alles wat met tyd te doen het, word met ’n “lang” y geskryf.', '**Kort klanke:** die medeklinker verdubbel + e, bv. kat – katte. **Lang klanke:** een klinker val weg + e, bv. boom – bome. **Tweeklanke:** voeg -e of -s by, bv. dier – diere.'], page=84),
    table('Verkleinwoorde', ['Agtervoegsel', 'Reël', 'Voorbeeld'], [['-jie', 'woorde op -t of -d', 'hond – hondjie'], ['-tjie', '', 'venster – venstertjie'], ['-kie', 'meerlettergrepige woorde op -ng: gooi die g weg', 'doring – dorinkie'], ['-etjie', 'eenlettergrepige woorde op -ng', 'wang – wangetjie'], ['-pie', 'woorde op -m', 'arm – armpie'], ['-ie', '', 'oog – ogie']], page=84),
    text('Lees- en skryftekens', bullets=['Die ^ (kappie) kom net op klinkers en dui ’n lang klank aan.', 'Die deelteken (¨) op aangrensende klinkers van verskillende lettergrepe.', 'Die afkappingsteken (’): pa – pa’s; impi – impi’s; balju – balju’s; hobo – hobo’s; Roux – Roux’s.', 'Aanhalingstekens dui direkte spraak aan: Piet sê: “Ek hou van jou.” Die aanhalingsteken sluit ná die laaste leesteken.', 'Die aksentteken beklemtoon iets, bv. ongelóóflik.'], page=85),
  ],
  acts=[
    choices('Omkring die korrekte spelling', 'Kies die korrekte woord in elke sin.', [('Ons ___ elke Vrydagaand brood en konfyt.', ['eet', 'eed'], 0), ('Ons eet elke ___ brood en konfyt.', ['Vrydagaand', 'Frydagaant'], 0), ('Ons eet ___ en konfyt.', ['brood', 'broot'], 0), ('Ons eet brood en ___.', ['konfyt', 'konvyt'], 0),
             ('Ons ___ hou van vinnige feetjies.', ['familie', 'vamilie'], 0), ('Ons familie hou van ___ feetjies.', ['finnige', 'vinnige'], 1), ('Ons familie hou van vinnige ___ en kleurvolle flaminke.', ['veetjies', 'feetjies'], 1), ('Hulle hou van ___ flaminke.', ['kleurvolle', 'kleurfolle'], 0), ('Hulle hou van kleurvolle ___.', ['flaminke', 'vlaminke'], 0),
             ('Die ___ kyk altyd na die dolfyne.', ['kaptein', 'kaptyn'], 0), ('Die kaptein ___ altyd na die dolfyne.', ['keik', 'kyk'], 1), ('Die kaptein kyk ___ na die dolfyne.', ['alteid', 'altyd'], 1), ('Die kaptein kyk altyd na die ___.', ['dolfeine', 'dolfyne'], 1), ('Hy ___ op die see.', ['vaar', 'faar'], 0)],
            'Onthou: v staan nooit aan die einde van ’n lettergreep nie en alles wat met tyd te doen het, kry ’n lang y.', src='workbook', page=84, item='spelling', status='derived_from_rule'),
    fill('Meervoud en verkleining (1)', 'atleet: {{1}} / {{2}}\ndogter: {{3}} / {{4}}\nfee: {{5}} / {{6}}\nhemp: {{7}} / {{8}}', {1: 'atlete', 2: ['atleetjie', 'atletie'], 3: 'dogters', 4: 'dogtertjie', 5: ['feë', 'fees'], 6: ['feetjie', 'feëtjie'], 7: 'hemde', 8: ['hempie', 'hempie']},
         'Skryf die meervoud (voor die skuinsstreep) en die verkleining (daarna).', prompt='Voltooi die tabel.', src='workbook', page=84, item='tabel 1', status='needs_review'),
    fill('Meervoud en verkleining (2)', 'orkes: {{1}} / {{2}}\nplakkaat: {{3}} / {{4}}\nstad: {{5}} / {{6}}', {1: ['orkeste', 'orkeste'], 2: ['orkesjie', 'orkestjie'], 3: 'plakkate', 4: 'plakkaatjie', 5: ['stede', 'stad’s'], 6: 'stadjie'},
         'Kyk na die reëls vir kort klanke, lang klanke en tweeklanke.', prompt='Voltooi die tabel.', src='workbook', page=84, item='tabel 2', status='needs_review'),
    sa('Direkte rede', 'Herskryf hierdie sin in die direkte rede: Danie sê dat hy ongelóóflik opgewonde is oor sy onderhoud wat hy met Bobby van Jaarsveld gaan voer.', 'Danie sê: “Ek is ongelóóflik opgewonde oor my onderhoud wat ek met Bobby van Jaarsveld gaan voer.”', lines=2, page=85, item='direk', status='derived_from_rule'),
    sa('Dialoogformaat', 'Herskryf die gesprek tussen Danie en een van sy kollegas in dialoogformaat en vul die nodige hoofletters en lees- en skryftekens in: is jy reg vir jou onderhoud met die beroemde sanger vanmiddag vra my kollega toe ek by die ateljee instap … ja ek dink so maar ’n mens bly maar ’n bietjie senuweeagtig antwoord ek haar … (die res: Danie se voorbereiding en sy vraag om aanbevelings).',
       'KOLLEGA: Is jy reg vir jou onderhoud met die beroemde sanger vanmiddag?\nDANIE: Ja, ek dink so, maar ’n mens bly maar ’n bietjie senuweeagtig.\nDANIE: Ek het lank voorberei en my onderhoudsvrae goed deurdink. Dit is vir my belangrik dat die vrae aan die verwagtinge van die tieners moet voldoen. Ek poog egter ook om die mas en pas se aandag vas te vang. Sal jy asseblief die vrae vir my deurgaan en aanbevelings doen voordat ek met die onderhoud moet begin?', lines=8, page=85, item='dialoog', status='needs_review'),
    tf('Waar of onwaar?', 'Alles wat met tyd te doen het, word met ’n “lang” y geskryf.', True, 'Die werkboek sê dit by die spelreëls (bv. altyd, tyd).', src='supplementary', status='official'),
  ],
  quiz=[
    q('spelling', 'Watter spelling is korrek?', 'altyd', ['alteid', 'altijd', 'alteyd'], 'Alles wat met tyd te doen het, kry ’n lang y.', status='official', src='workbook', page=84),
    q('spelling', 'Watter spelling is korrek?', 'vinnige', ['finnige', 'vinige', 'fienige'], 'V staan nooit aan die einde van ’n lettergreep nie; hier is dit aan die begin: vinnige.', status='derived_from_rule', src='workbook', page=84, item='spelling'),
    q('spelling', 'Watter spelling is korrek?', 'dolfyne', ['dolfeine', 'dolfyne-', 'dolfyn’e'], 'Dolfyn word met ’n y geskryf; meervoud dolfyne.', status='derived_from_rule', src='workbook', page=84, item='spelling'),
    q('spelling', 'Wat is die meervoud van “stad”?', 'stede', ['stads', 'stadde', 'stadte'], 'Lang klank: een klinker val weg + e, maar stad – stede is ’n uitsondering.', status='needs_review', src='workbook', page=84, item='tabel 2'),
    q('spelling', 'Wat is die verkleinwoord van “atleet”?', 'atleetjie', ['atleetie', 'atleetjie’s', 'atlete'], 'Woorde op -t kry -jie: atleetjie.', status='derived_from_rule', src='workbook', page=84, item='tabel 1'),
    q('grammar', 'Waar sluit die aanhalingsteken in direkte spraak?', 'Ná die laaste leesteken', ['Voor die laaste woord', 'Voor die eerste woord', 'Dit sluit nie'], 'Die werkboek sê dit by die lees- en skryftekens.', status='official', src='workbook', page=85),
    q('grammar', 'Wat is die meervoud van “pa”?', 'pa’s', ['pas', 'pa-e', 'pa’e'], 'Die afkappingsteken word by die meervoud gebruik: pa – pa’s.', status='official', src='workbook', page=85),
    q('grammar', 'Waarvoor word die aksentteken gebruik?', 'Om iets te beklemtoon', ['Om klinkers te verdubbel', 'Om woorde te verbind', 'Om ’n vraag te vra'], 'Voorbeeld: ongelóóflik.', status='official', src='workbook', page=85),
  ])
