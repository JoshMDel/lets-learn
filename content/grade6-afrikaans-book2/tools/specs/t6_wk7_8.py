import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

WRITE_PROCESS = ['Beplan jou skryfwerk.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']
FP = '/workbook/gr6-afr-b2/'

# ============================================================== 89 Supa Strikas
L89 = lesson(89,
  skills=[READ, LISTEN],
  intro='Strokiesprente vertel ’n storie met baie prente en min woorde. Lees die Supa Strikas-strokiesprent en let op die praatborrels en die klanknabootsende woorde!',
  objectives=['Weet wat ’n strokiesprentverhaal is.', 'Verstaan wat in elke raampie gebeur.', 'Die verskillende soorte praatborrels en die klanknabootsende woorde herken.', 'Die uitleg en woordeskat van ’n strokiesprent bespreek.'],
  learn=[
    note('Die strokiesprentverhaal is ’n **genre**. Tot dusver vanjaar het jy verskillende soorte tekste gelees: volksverhale, gedigte, advertensies, verslae, dialoë, inligtingtekste en instruksionele tekste. Die strokiesprentverhaal is nog ’n soort teks. Daar is minder woorde en baie prente, sodat jy kan sien hoe die karakters lyk en wat hulle doen. Die storie word in ’n reeks raampies vertel. Soms is daar woorde, soms nie.', title='Wat is ’n strokiesprentverhaal?', page=52),
    text('Waarop moet jy let?', bullets=['Fokus op wat in elk van die raampies gebeur.', 'Let op die verskillende soorte **praatborrels**.', 'Kyk na die praatborrels in raam 4, 5, 6, 7 en 8: hulle wys wat die kommentators sê.', 'Let op die **klanknabootsende woorde** (onomatopeë) en hoe hulle geskryf is, bv. PRRRRT, SKARRA!, DWOOSJ.'], page=52),
  ],
  acts=[
    figure('Die strokiesprent (bladsy 1: rame 1–7)', FP + 'p056.webp', 'Supa Strikas-strokiesprent, bladsy 1 met rame 1 tot 7.', page=52, section='activity'),
    figure('Die strokiesprent (bladsy 2: rame 8–14)', FP + 'p057.webp', 'Supa Strikas-strokiesprent, bladsy 2 met rame 8 tot 14.', page=53, section='activity'),
    discuss('Ons lees: Vluglees', 'Lees die twee bladsye uit ’n Supa Strika-strokiesprent. Fokus op wat in elk van die raampies gebeur en let op die praatborrels en die klanknabootsende woorde.', page=52, item='Ons lees'),
    mcq('Teen watter span speel Supa Strikas?', 'Teen watter span speel die Supa Strikas?', ['United', 'Spur', 'Caltex', 'Shakes'], 0, 'Die kommentator sê: “Die Strikas reageer met oorgawe op United se doel.”', per_option={1: 'Spur is die naam wat op ’n advertensiebord in raam 12 staan.', 2: 'Caltex is ’n advertensie op die veld.', 3: 'Shakes is een van die spelers.'}, src='supplementary', status='derived_from_text'),
    mcq('Wie moet die held word?', 'Wie wil die afrigter vandag die held maak?', ['Shakes', 'Die skeidsregter', 'Die kommentator', 'United se doelwagter'], 0, 'In raam 10 sê die persoon: “Dit lyk my ons afrigter wil jou vandag die held maak, Shakes!”', src='supplementary', status='derived_from_text'),
    mcq('Wat het Shakes laas keer gedoen?', 'Wat het die kommentator oor Shakes se laaste finale wedstryd teen United gesê?', ['Hy het ’n stelskop misgeskop.', 'Hy het ’n doel aangeteken.', 'Hy het ’n rooi kaart gekry.', 'Hy was seergemaak.'], 0, 'Raam 11: “Laas toe Shakes ’n stelskop in ’n finale wedstryd teen United gehad het, het hy misgeskop.”', src='supplementary', status='derived_from_text'),
    match('Pas die woord by sy betekenis', 'Verbind elke woord met wat dit in die strokiesprent beteken.', [('praatborrel', 'wys wat ’n karakter sê'), ('raampie', 'een blokkie in die strokiesprent'), ('klanknabootsende woord', 'woord wat ’n klank naboots, bv. PRRRRT'), ('dubbelmuur', 'twee rye verdedigers voor die doel')],
          'In ’n strokiesprent vertel die rame en die praatborrels saam die storie.', src='supplementary', status='derived_from_rule'),
    tf('Waar of onwaar?', 'In ’n strokiesprent is daar altyd net woorde en geen prente nie.', False, 'Die werkboek sê: daar is minder woorde en baie prente.', src='supplementary', status='official'),
  ],
  quiz=[
    q('vocabulary', 'Wat is ’n strokiesprentverhaal?', '’n Genre waar ’n storie met prente en min woorde in raampies vertel word', ['’n Lang brief', '’n Koerantberig met ’n opskrif', '’n Gedig met rym'], 'Die werkboek sê: minder woorde en baie prente, ’n reeks raampies.', status='official', src='workbook', page=52),
    q('literal', 'Teen watter span speel die Supa Strikas in die strokiesprent?', 'United', ['Spur', 'Caltex', 'Metropolitan'], 'Die kommentator praat van “United se doel”.', status='derived_from_text', src='supplementary'),
    q('literal', 'Wie wil die afrigter die held maak?', 'Shakes', ['Die doelwagter', 'Die skeidsregter', 'Die kommentator'], 'Raam 10 noem Shakes.', status='derived_from_text', src='supplementary'),
    q('literal', 'Watter klanknabootsende woord kom in die laaste raam voor?', 'DWOOSJ', ['KABOEM', 'WROEM', 'SPLOSJ'], 'Raam 14 het die groot woord DWOOSJ.', status='derived_from_text', src='supplementary'),
    q('literal', 'Wat wou Shakes se plan wees om die “dubbelmuur” te troef?', '’n Dubbelkurwe', ['’n Lang skop', '’n Gelykopskop', '’n Strafskop'], 'Raam 13 en 14: “Want om ’n dubbelmuur te troef … het jy ’n dubbelkurwe nodig!”', status='derived_from_text', src='supplementary'),
    q('vocabulary', 'Waarvoor word praatborrels in strokiesprente gebruik?', 'Om te wys wat die karakters sê of dink', ['Om advertensies te wys', 'Om die telling te hou', 'Om die datum te wys'], 'Praatborrels bevat die karakters se woorde.', status='derived_from_rule', src='supplementary'),
    q('inference', 'Wat beteken “Koel … dis Shakes teenoor Dingaan!”?', 'Die kommentator se opwinding oor die twee spelers wat teenoor mekaar staan', ['Dit is te koud om sokker te speel', 'Die skeidsregter is kwaad', 'Die publiek is weg'], 'Die kommentator reageer opgewonde op die twee spelers.', status='needs_review', src='supplementary'),
    q('vocabulary', 'Wat is ’n klanknabootsende woord (onomatopee)?', '’n Woord wat ’n klank naboots, soos PRRRRT', ['’n Woord met dieselfde betekenis', '’n Woord met teenoorgestelde betekenis', '’n Woord wat ’n naam is'], 'Dit word geskryf soos die klank klink.', status='derived_from_rule', src='supplementary'),
  ])

# ============================================================== 90 Ons skryf oor die Supa Strikas
L90 = lesson(90,
  skills=[LISTEN, READ, WRITE],
  intro='Vandag dink jy dieper na oor die strokiesprent, skryf jy ’n opsomming en kyk jy wat ’n advertensie jou probeer laat doen.',
  objectives=['Vrae oor ’n strokiesprent beantwoord.', 'Die uitleg, taalgebruik en klanknabootsende woorde van ’n strokiesprent bespreek.', 'Die strokiesprent in jou eie woorde in paragraafvorm opsom.', 'Televisie-advertensies bespreek en ’n strokiesprentadvertensie ontleed.'],
  learn=[
    text('Bespreek in die klas', bullets=['hoe die toneel beskryf word', 'die karakters se taalgebruik (die praatborrels)', 'die klanknabootsende woorde (onomatopeë) en hoe hulle geskryf is', 'die toepaslikheid en effektiwiteit van die grafiese voorstellings', 'nuwe woorde', 'hoe woordkeuse lyftaal beïnvloed', 'die gebruik van die direkte rede en die indirekte rede'], page=54),
  ],
  acts=[
    figure('Die Supa Strikas-strokiesprent (bladsy 1)', FP + 'p056.webp', 'Supa Strikas-strokiesprent, rame 1 tot 7.', page=52, section='activity'),
    figure('Die Supa Strikas-strokiesprent (bladsy 2)', FP + 'p057.webp', 'Supa Strikas-strokiesprent, rame 8 tot 14.', page=53, section='activity'),
    discuss('Ons praat: bespreek die strokiesprent', 'Bespreek wat in elke raam van die strokiesprentverhaal gebeur. Bespreek ook die punte hierbo in klasverband.', page=54, item='Ons praat'),
    sa('Vraag 1', 'Wat doen die Supa Strikas-verdediging net so graag as wat hulle sokker speel?', None, lines=2, page=54, item=1),
    sa('Vraag 2: Die opponente', 'Teen watter span speel die Supa Strikas-span?', 'United', lines=1, page=54, item=2, status='derived_from_text'),
    sa('Vraag 3: Die fluitjie', 'Watter klank maak die skeidsregter se fluitjie? Waarom blaas hy sy fluitjie in raam 4?', 'PRRRRT. Hy blaas omdat daar ’n oortreding was – ’n speler het geval en gesê “Eina! Dit moet seermaak!”', lines=2, page=54, item=3, status='needs_review'),
    sa('Vraag 4: Die telling', 'Wat is die telling? (Wenk: Kyk na raam 5 en 7.)', None, lines=1, page=54, item=4),
    sa('Vraag 5: Klanknabootsende woorde', 'Maak ’n lys van al die klanknabootsende woorde in die strokiesprent.', 'PRRRRT, SKARRA!, DWOOSJ', lines=2, page=54, item=5, status='derived_from_text'),
    sa('Vraag 6–7: Die advertensies', 'Watter advertensies sien jy in die strokiesprent? Op wie is die advertensies gerig?', 'Advertensies op die advertensiebords langs die veld, bv. Caltex, Metropolitan en Spur. Hulle is op sokkerkykers (die kykers by die wedstryd en voor die TV) gerig.', lines=3, page=54, item='6–7', status='needs_review'),
    writing('Som die strokiesprent op', 'Som die strokiesprent in jou eie woorde in paragraafvorm op.', checklist=['Ek het gesê wie speel en teen wie.', 'Ek het die gebeure in volgorde vertel.', 'Ek het gesê wat Shakes se plan was.', 'Ek het in paragrawe geskryf.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=10, page=54, item='opsomming'),
    discuss('Ons praat: TV-advertensies', 'Praat met jou maat.', points=['Wat is jou gunstelingadvertensie op die radio of TV?', 'Wat word daardeur geadverteer?', 'Waarom hou jy daarvan?', 'Sou jy die produk wat geadverteer word, koop?', 'Identifiseer die teikengroep wat die produk sou koop.', 'Gebruik die advertensie ’n slagspreuk vir die produk?', 'Is die grafiese voorstellings toepaslik en effektief?'], page=55, item='Ons praat'),
    figure('Strokiesprente vir reklame: die Woematjor', FP + 'p059.webp', 'Strokiesprentadvertensie vir die Woematjor, ’n afstandsbeheer-renmotor.', page=55, section='activity'),
    sa('Die Woematjor: wat wil die advertensie hê jy moet doen?', 'Wat probeer die advertensie jou oorreed om te doen?', 'Om die Woematjor so gou moontlik te koop (“Skaf hom so gou moontlik aan”).', lines=2, page=55, item='ad 1', status='derived_from_text'),
    sa('Die Woematjor: oordrywing', 'Oordryf of belowe die advertensie enigiets? Verduidelik jou antwoord.', 'Ja – dit sê jy sal die gewildste outjie in die suidelike halfrond wees en dat die Woematjor hom deur niks laat keer nie.', lines=3, page=55, item='ad 2', status='derived_from_text'),
    fill('Die Woematjor: klanknabootsende woorde', 'Die advertensie gebruik klanknabootsende woorde soos {{1}} (oor land) en {{2}} (deur water).', {1: ['wroem', 'wroem wroem', 'wroem, wroem'], 2: ['splosj', 'woerrrrrrr']}, 'In die advertensie staan: “wroem, wroem!” en “splosj – woerrrrrrr!”', bank=['wroem', 'splosj', 'kaboem'], src='workbook', page=55, item='ad 3', status='derived_from_text'),
    sa('Die Woematjor: teikengehoor', 'Op wie is die advertensie gemik? Is die teikengehoor jongmense of bejaardes, seuns of meisies?', 'Op jongmense, veral seuns (kinders wat van afstandsbeheer-motors hou).', lines=2, page=55, item='ad 4', status='needs_review'),
  ],
  quiz=[
    q('literal', 'Teen watter span speel die Supa Strikas?', 'United', ['Spur', 'Caltex', 'Metropolitan'], 'Die kommentator praat van “United se doel”.', status='derived_from_text', src='workbook', page=54, item=2),
    q('literal', 'Watter klank maak die skeidsregter se fluitjie in die strokiesprent?', 'PRRRRT', ['SKARRA!', 'DWOOSJ', 'KABOEM'], 'In raam 4 staan PRRRRT by die fluitjie.', status='derived_from_text', src='workbook', page=54, item=3),
    q('literal', 'Wat is die Woematjor?', '’n Afstandsbeheer-renmotor', ['’n Sokkerbal', '’n Boot', '’n Vliegtuig'], 'Die advertensie sê: “Die Woematjor is ’n afstandsbeheer-renmotor.”', status='derived_from_text', src='workbook', page=55),
    q('literal', 'Watter klanknabootsende woord word gebruik wanneer die Woematjor oor land ry?', 'wroem, wroem', ['splosj', 'woerrrrrrr', 'dwoosj'], 'Die advertensie het “wroem, wroem!”.', status='derived_from_text', src='workbook', page=55, item='ad 3'),
    q('literal', 'Watter klanknabootsende woord word gebruik wanneer die Woematjor deur water ry?', 'splosj', ['wroem', 'skarra', 'prrrrt'], 'Die advertensie het “splosj – woerrrrrrr!”.', status='derived_from_text', src='workbook', page=55, item='ad 3'),
    q('inference', 'Wat is die doel van ’n advertensie?', 'Om jou te oorreed om iets te koop of te doen', ['Om ’n storie te vertel', 'Om die nuus te lees', 'Om jou iets te leer teken'], 'Die advertensie sê: “Skaf hom so gou moontlik aan.”', status='derived_from_rule', src='supplementary'),
    q('vocabulary', 'Wat is ’n teikengroep (teikengehoor)?', 'Die mense vir wie die advertensie bedoel is', ['Die mense wat die advertensie maak', 'Die dele van ’n strokiesprent', 'Die skrywers van die produk'], 'Dit is die groep wat die produk sou koop.', status='derived_from_rule', src='supplementary'),
    q('vocabulary', 'Wat is oordrywing in ’n advertensie?', 'Om te sê iets is baie groter of beter as wat dit werklik is', ['Om die waarheid sê', 'Om iets kleiner te maak', 'Om ’n prys te noem'], 'Die Woematjor sou jou die gewildste outjie in die suidelike halfrond maak – ’n oordrywing.', status='derived_from_rule', src='supplementary'),
  ])

# ============================================================== 91 Skryf jou eie advertensie
L91 = lesson(91,
  skills=[LISTEN, WRITE],
  intro='Nou is jy die advertensiemaker! Beplan en skryf die teks vir jou eie TV-advertensie in vier tonele en voer dit saam met jou groep op.',
  objectives=['’n TV-advertensie beplan (produk, doel, teikengroep, agtergrond en karakters).', 'Die advertensie in vier tonele verdeel.', 'Klanknabootsende woorde gebruik.', 'Jou advertensie opvoer.'],
  learn=[
    text('Stap vir stap', bullets=['Besluit wat jy gaan adverteer, wat jy met jou advertensie wil bereik en wie jou teikengroep is.', 'Besluit teen watter agtergrond jou advertensie hom gaan afspeel, en wie die karakter(s) gaan wees.', 'Besluit ook hoe jy aksie by jou advertensie sal voeg.', 'Verdeel jou advertensie in vier tonele.', 'Teken ’n prentjie of plak prente in om elke toneel te illustreer.', 'Skryf ’n teks om presies aan te dui wat elke persoon sal sê.'], page=56),
    note('Onthou om klanknabootsende woorde te gebruik. Jy kan ook jou eie nuwe woorde skep.', title='Wenk', page=56),
  ],
  acts=[
    writing('Beplan jou advertensie', 'Beantwoord hierdie vrae op jou advertensiebeplanner: Wat gaan jy adverteer? Wat is die doel van die advertensie? Wie is die teikengroep? Waar speel die advertensie hom af? Wie is die karakters in die advertensie?',
            checklist=['Ek weet wat ek gaan adverteer.', 'Ek weet wat die doel van my advertensie is.', 'Ek weet wie my teikengroep is.', 'Ek weet waar die advertensie hom afspeel.', 'Ek het my karakters gekies.'], lines=8, page=56, item='beplanner'),
    writing('Toneel 1 en 2', 'Skryf jou eerste weergawe vir toneel 1 en toneel 2 (blok 1 en 2). Skryf presies wat elke persoon sal sê en gebruik klanknabootsende woorde.', lines=8, page=56, item='blok 1–2'),
    writing('Toneel 3 en 4', 'Skryf jou eerste weergawe vir toneel 3 en toneel 4 (blok 3 en 4).', checklist=['Ek het die advertensie in vier tonele verdeel.', 'Ek het aangedui wat elke karakter sê.', 'Ek het klanknabootsende woorde gebruik.', 'Ek het my teks hersien en gekorrigeer.'], tips=['Gebruik ’n geheuekaart om jou skryfwerk te beplan.', 'Voltooi jou eerste weergawe in blok 1 tot 4.', 'Hersien en korrigeer jou teks.', 'Skryf jou finale weergawe op bladsy 57.'], lines=8, page=57, item='blok 3–4'),
    discuss('Ons doen: Speel jou advertensie', 'Wanneer jy die hele teks vir jou TV-advertensie geskryf het, kies lede van jou groep om dit te dramatiseer en te wys hoe dit op TV sal lyk.', page=57, item='Ons doen'),
    order('Die stappe van die advertensiebeplanner', 'Sit die stappe in die volgorde waarin jy dit sal doen.', ['Besluit wat jy gaan adverteer en wie jou teikengroep is.', 'Besluit teen watter agtergrond en met watter karakters.', 'Verdeel die advertensie in vier tonele.', 'Teken of plak prente by elke toneel.', 'Skryf wat elke persoon sal sê.'], 'Die werkboek gee hierdie volgorde.', perm=[3, 0, 4, 2, 1], src='supplementary', status='official'),
    tf('Waar of onwaar?', 'Jy moet jou TV-advertensie in vier tonele verdeel.', True, 'Die werkboek sê: Verdeel jou advertensie in vier tonele.', src='supplementary', status='official'),
  ],
  quiz=[
    q('main_idea', 'In hoeveel tonele verdeel jy jou advertensie?', 'Vier', ['Twee', 'Ses', 'Tien'], 'Die werkboek sê vier tonele.', status='official', src='supplementary', page=56),
    q('main_idea', 'Watter inligting moet jy eerste besluit?', 'Wat jy gaan adverteer, wat jy wil bereik en wie jou teikengroep is', ['Die kleur van die papier', 'Wie die beste teken', 'Die datum'], 'Dit is die eerste stap in die werkboek.', status='official', src='supplementary', page=56),
    q('vocabulary', 'Wat is ’n teikengroep?', 'Die mense vir wie jy die advertensie maak', ['Die akteurs', 'Die onderwyser', 'Die klas'], 'Dit is die groep wat die produk sou koop.', status='derived_from_rule', src='supplementary'),
    q('main_idea', 'Wat skryf jy in die teks van jou advertensie?', 'Presies wat elke persoon sal sê', ['Net die prys', 'Net die naam van die winkel', 'Net die datum'], 'Die werkboek sê: skryf ’n teks om presies aan te dui wat elke persoon sal sê.', status='official', src='supplementary', page=56),
    q('vocabulary', 'Watter soort woorde moet jy onthou om te gebruik?', 'Klanknabootsende woorde', ['Net lang woorde', 'Net vreemde woorde', 'Net getalle'], 'Die werkboek sê onthou om klanknabootsende woorde te gebruik.', status='official', src='supplementary', page=56),
    q('sequencing', 'Wat doen jy nadat jy jou advertensie geskryf het?', 'Jy dramatiseer dit saam met lede van jou groep', ['Jy gooi dit weg', 'Jy ruil dit vir ’n ander teks', 'Jy skryf dit nie opnuut nie'], 'Ons doen: kies lede van jou groep om dit te dramatiseer.', status='official', src='supplementary', page=57),
    q('main_idea', 'Hoe wys jy waar die advertensie hom afspeel?', 'Jy besluit teen watter agtergrond dit afspeel', ['Jy skryf dit nêrens neer nie', 'Jy los dit uit', 'Jy vra die onderwyser'], 'Die werkboek vra: teen watter agtergrond gaan jou advertensie hom afspeel?', status='official', src='supplementary', page=56),
    q('main_idea', 'Hoe voeg jy aksie by?', 'Jy besluit hoe die karakters beweeg en wat hulle doen', ['Jy gebruik net teks', 'Jy gebruik net prente', 'Jy skryf ’n gedig'], 'Die werkboek sê besluit hoe jy aksie by jou advertensie sal voeg.', status='derived_from_text', src='supplementary', page=56),
  ])

# ============================================================== 92 Taalstrukture en -konvensies
L92 = lesson(92,
  skills=[LANG],
  intro='Klank of letter? Idiome en vergelykings, spelreëls en leestekens – vandag hersien ons die belangrikste taalreëls.',
  objectives=['Die verskil tussen ’n klank en ’n letter verstaan en woorde in klank- en lettergrepe verdeel.', 'Idiome en vaste uitdrukkings met hulle betekenisse verbind.', '’n Vergelyking skryf.', 'Spelreëls (meervoud, verkleining) en leestekens toepas.'],
  learn=[
    note('Daar is ’n verskil tussen ’n klank en ’n letter. Klanke is dit wat mense hoor, terwyl letters geskryf word. In die spreektaal verdeel ons ’n woord in klankgrepe (asemstote), maar as ons skryf, gebruik ons lettergrepe.', title='Klank en letter', page=58),
    table('Gesproke taal en geskrewe taal', ['Gesproke taal', 'Geskrewe taal'], [['spraak', 'skrif'], ['klank', 'letters'], ['uitspraak', 'spelling'], ['plakkers → pla-kkers (klankgreep)', 'plakkers → plak-kers (lettergreep)']], page=58),
    text('Beeldspraak', bullets=['**Beeldspraak** beteken om iets figuurliks oor te dra deur ’n vergelyking, ’n metafoor, personifikasie, idiomatiese uitdrukkings, ens.', '**Idiomatiese en vaste uitdrukkings** is uitdrukkings wat eie aan die taal is.', 'Dikwels beskryf ons iets deur te sê dat dit soos iets anders is: ’n **vergelyking**. Ons gebruik dikwels dierebeelde in vergelykings.'], page=58),
    text('Spelreëls', bullets=['As jy nie seker is of ’n woord met ’n -d of ’n -t eindig nie, sê die meervoud of vorm ’n ander woord, bv. hond – honde, goed – goedere.', 'V staan nooit aan die einde van ’n woord of lettergreep nie.', '**Kort klanke:** die medeklinker verdubbel + e, bv. kat – katte. **Lang klanke:** een klinker val weg + e, bv. boom – bome. **Tweeklanke:** voeg -e of -s by, bv. dier – diere.'], page=59),
    text('Leestekens', bullets=['Die ^ (kappie) kom net op klinkers, bv. lê.', 'Die deelteken (¨) staan op aangrensende klinkers van verskillende lettergrepe, bv. leë.', 'Die afkappingsteken (’) by die meervoud of verkleining van woorde wat op ’n beklemtoonde a, i, o of u eindig, bv. pa – pa’s.', 'Aanhalingstekens dui direkte spraak aan: Piet sê: “Ek hou van jou.” Die aanhalingsteken sluit ná die laaste leesteken.', 'Die aksentteken beklemtoon iets, bv. ongelóóflik.'], page=59),
  ],
  acts=[
    fill('Klankgrepe en lettergrepe', 'debatteer – klankgrepe: {{1}}  lettergrepe: {{2}}\nbotter – klankgrepe: {{3}}  lettergrepe: {{4}}\nbakkie – klankgrepe: {{5}}  lettergrepe: {{6}}\nbejammer – klankgrepe: {{7}}  lettergrepe: {{8}}\nspinnekop – klankgrepe: {{9}}  lettergrepe: {{10}}',
         {1: ['de-ba-tteer', 'de-ba-tte-er'], 2: ['de-bat-teer', 'de-bat-te-er'], 3: 'bo-tter', 4: 'bot-ter', 5: 'ba-kkie', 6: 'bak-kie', 7: 'be-ja-mmer', 8: 'be-jam-mer', 9: 'spi-nne-kop', 10: 'spin-ne-kop'},
         'Klankgrepe breek ná die klinker (voor die dubbele medeklinker); lettergrepe breek tussen die twee ewe medeklinkers (plak-kers).', prompt='Verdeel hierdie woorde in klank- en lettergrepe (skei met koppeltekens).', src='workbook', page=58, item='tabel 1', status='derived_from_rule'),
    sa('Sinonieme en antonieme', 'Soek sinonieme vir hierdie woorde of frases in die strokiesprent en die advertensie en gee dan jou eie antonieme: iets wat uit die lug op die aarde arriveer; hoe jy voel wanneer jy lank laas geëet het; gewild; die “onderste” helfte van die aarde.',
       'gewild – populêr (antoniem: ongewild); die “onderste” helfte van die aarde – die suidelike halfrond (antoniem: noordelike halfrond). (Die ander twee: eie antwoord.)', lines=5, page=58, item='tabel 2', status='needs_review'),
    match('Verbind die uitdrukkings met hul betekenisse', 'Verbind elke uitdrukking met sy betekenis.',
          [('aan bewind kom', 'beheer oorneem'), ('baanbrekerswerk doen', 'as pionier optree'), ('op jouself aangewese wees', 'op jouself moet staatmaak'), ('blad skud', 'met die hand groet'), ('standvastig bly', 'onbeweeglik bly')],
          'Idiome het ’n figuurlike betekenis wat anders is as die gewone woorde.', src='workbook', page=58, item='uitdrukkings', status='needs_review'),
    sa('Jou eie vergelyking', 'Skryf jou eie vergelyking waarin jy die spoed of krag van die Woematjor met dié van ’n dier vergelyk.', 'Die Woematjor is so vinnig soos ’n jagluiperd.', lines=2, page=58, item='vergelyking', status='needs_review'),
    choices('Omkring die korrekte spelling', 'Kies die korrekte spelling.', [('Die ___ blaf.', ['hont', 'hond'], 1), ('Die hond blaf ___.', ['ferskriklik', 'verskriklik'], 1), ('Hy blaf vir die ___ mense.', ['freemde', 'vreemde'], 1), ('Die ___ word deur ’n man afgelewer.', ['brief', 'briev'], 0), ('Hy ry op ’n ___.', ['pert', 'perd'], 1)],
            'Sê die meervoud: hond – honde, perd – perde, brief – briewe. V staan nooit aan die einde van ’n woord nie.', src='workbook', page=59, item='spelling', status='derived_from_rule'),
    fill('Meervoud en verkleining', 'laan: meervoud {{1}}, verkleining {{2}}\nspan: meervoud {{3}}, verkleining {{4}}\nenjin: meervoud {{5}}, verkleining {{6}}\nmetaal: meervoud {{7}}, verkleining {{8}}',
         {1: 'lane', 2: 'laantjie', 3: 'spanne', 4: 'spannetjie', 5: ['enjins', 'enjinne'], 6: ['enjintjie', 'enjinetjie'], 7: ['metale', 'metaalsoorte'], 8: 'metaaltjie'},
         'Kort klank: verdubbel + e (span – spanne). Lang klank: een klinker val weg (laan – lane).', prompt='Voltooi die tabel.', src='workbook', page=59, item='tabel', status='needs_review'),
    sa('Leestekens en hoofletters', 'Herskryf hierdie sinne en vul die nodige hoofletters asook lees- en skryftekens in: danie vra anna sal jy asseblief die sker gaan bere / ons gesin het ’n tradisie om videos te kyk en springmielies te eet as dit reen',
       'Danie vra: “Anna, sal jy asseblief die skêr gaan bêre?”\nOns gesin het ’n tradisie om video’s te kyk en springmielies te eet as dit reën.', lines=3, page=59, item='leestekens', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Klanke is dit wat mense hoor, en letters is dit wat geskryf word.', True, 'Dit is presies wat die werkboek sê.', src='supplementary', status='official'),
  ],
  quiz=[
    q('grammar', 'Wat is ’n lettergreep?', '’n Deeltjie van ’n woord wat ons skryf', ['’n Woord met twee betekenisse', '’n Leesteken', '’n Soort sin'], 'In die skryftaal gebruik ons lettergrepe (plak-kers).', status='official', src='workbook', page=58),
    q('grammar', 'Hoe word “plakkers” in klankgrepe verdeel?', 'pla-kkers', ['plak-kers', 'pl-akkers', 'plakk-ers'], 'Die werkboek gee: plakkers – pla-kkers (klankgreep).', status='official', src='workbook', page=58),
    q('grammar', 'Hoe word “plakkers” in lettergrepe verdeel?', 'plak-kers', ['pla-kkers', 'pl-akkers', 'plakk-ers'], 'Die werkboek gee: plakkers – plak-kers (lettergreep).', status='official', src='workbook', page=58),
    q('grammar', 'Wat is die meervoud van “hond”?', 'honde', ['hondde', 'honds', 'hondjies'], 'Sê die meervoud om te weet of die woord op -d of -t eindig: hond – honde.', status='official', src='workbook', page=59),
    q('grammar', 'Wat is die verkleiningsvorm van “hond”?', 'hondjie', ['hondtjie', 'hondie', 'hondkie'], 'Woorde wat op -t of -d eindig, kry -jie.', status='official', src='workbook', page=59),
    q('vocabulary', 'Wat is ’n vergelyking?', 'Wanneer ons iets beskryf deur te sê dit is soos iets anders', ['’n Woord met dieselfde betekenis', '’n Woord met teenoorgestelde betekenis', '’n Klank'], 'Dit is die werkboek se verduideliking.', status='official', src='workbook', page=58),
    q('vocabulary', 'Wat beteken die idioom “aan bewind kom”?', 'Beheer oorneem', ['Onbeweeglik bly', 'Met die hand groet', 'As pionier optree'], 'Die uitdrukking betrek die oorneem van beheer of regering.', status='derived_from_rule', src='workbook', page=58, item='uitdrukkings'),
    q('grammar', 'Wat is die meervoud van “pa”?', 'pa’s', ['pas', 'pa-e', 'pa’e'], 'Die werkboek gee as voorbeeld: pa – pa’s.', status='official', src='workbook', page=59),
    q('grammar', 'Waar staan die aanhalingsteken wat die direkte spraak sluit?', 'Ná die laaste leesteken', ['Voor die laaste woord', 'In die middel van die sin', 'Dit staan nêrens nie'], 'Die werkboek: die aanhalingsteken sluit ná die laaste leesteken.', status='official', src='workbook', page=59),
  ])
