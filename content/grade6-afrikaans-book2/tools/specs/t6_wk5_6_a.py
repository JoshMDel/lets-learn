import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

WRITE_PROCESS = ['Beplan jou skryfwerk.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']

STORY81 = """Daar was eenmaal ’n hasie wat altyd bekommerd was. “Ag tog,” het hy heeldag gemompel, “Ag toggie, tog, tog.”
Sy grootste bekommernis was dat daar ’n aardbewing sou kom. “Want as dit gebeur,” het hy vir homself gesê, “wat op aarde word dan van my?”
Hy was een oggend juis besonder bekommerd hieroor toe ’n yslike vrug skielik van ’n boom naby hom afval – KABOEM – en die hele aarde laat skud.
“Aardbewing!” skree hy.
En hy hardloop oor die veld om sy neefs en niggies te gaan waarsku.
“Aardbewing! Hardloop vir die vale!”
Al die hase peul uit die lande en hardloop verwoed agter hom aan. Hulle snel oor vlaktes, deur woude en riviere tot in die heuwels en waarsku nog neefs en niggies sover hulle gaan.
Net toe kom hasie ’n olifant teë. “Aardbewing!” roep hy. “Hardloop vir die vale!”
Die olifant begin agter die hase aanhardloop, en die aarde bewe van sy swaar stampende pote.
Hulle hardloop by ’n groep kameelperde verby. “Aardbewing!” roep die hasie. “Hardloop vir die vale!”
Die kameelperde begin aanhardloop agter die olifant, wat die hase volg.
Teen die tyd dat hulle die berg bereik, klink die tien duisend hase, die olifant en ’n hele klomp kameelperde soos donderweer teen die berghange. Die voorste haas kyk om of die aardbewing al nader kom, maar al wat hy kan sien, is ’n groot trop stormende diere.
Terwyl hy staan en hyg, kom daar ’n leeu aan.
“Wat is aan die gang?” vra die leeu.
“Aardbewing, aardbewing!” babbel die hasie.
“’n Aardbewing?” vra die leeu. “Wie het dit gesien? Wie het dit gehoor?”
“Nie ek nie,” antwoord die olifant.
“Vra hom, vra hom!” gil al die hasies, en hulle wys na die eerste hasie.
Die leeu kyk na die hasie.
“Asseblief, Meneer,” sê die hasie skamerig, “ek het rustig by my huis gesit toe daar ’n vreeslike slag was. Die aarde het geskud, en ek het geweet dit moet ’n aardbewing wees, Meneer. Toe hardloop ek so vining as wat my bene my kon dra om die ander te waarsku om te hardloop dat hulle klein word.”
“My boetie, sal jy dapper genoeg kan wees om my te wys waar hierdie vreeslike ramp hom afgespeel het?” vra die leeu.
“Oe, ek kan nooit weer soontoe teruggaan nie!” sê die hasie.
“Spring op my rug dan neem ek jou soontoe. Ek sal jou oppas,” sê die leeu.
Baie skrikkerig spring die hasie toe op die leeu se rug en daar trek hulle, oor berge en dale, deur riviere en woude, oor grasvelde en vlaktes, totdat hulle by die hasie se huis kom.
“Dit is waar ek dit gehoor het, Meneer. En ook gevoel het. Die grond het gebewe.”
Die leeu kyk rond – en baie gou sien hy die enorme kokosneut wat met ’n slag van die boom afgeval het. Hy sien ook ’n apie in die boom sit. Die leeu tel die kokosneut op, klim op ’n rotsblok en laat die neut op die grond val.
KABOEM!
Die hasie wip ’n meter hoog. “Aardbewing! Daar gebeur dit weer! Gou-gou – ons moet maak dat ons wegkom!”
Hasie sien die oopgebarste kokosneut voor sy voete en hoor hoe lekker die leeu uit sy maag lag. Hasie besef toe wat gebeur het.
“O,” fluister hy. “Dit was toe nie regtig ’n aardbewing nie, of hoe?”
“Nee,” sê die leeu, “dit was nie, en jy hoef nie bang te gewees het nie.”
“Was ek nie ’n simpel hasie nie!”
Die leeu glimlag vriendelik. “Toe maar, my ou boetie. Almal van ons – selfs ek ook – is partykeer bang vir die dinge wat ons nie verstaan nie.”
En met daardie woorde loop hy terug na die tien duisend hase, die olifant en die kameelperde wat nog steeds bo-op die berg staan en wag, om vir hulle te vertel dat alles heeltemal veilig is om huis toe te kan gaan."""
GLOSS81 = [('bekommerd', 'Bang of ongelukkig oor iets wat dalk kan gebeur.'), ('yslike', 'Baie groot.'), ('verwoed', 'Baie wild en haastig, soos in woede.'), ('waarsku', 'Vir iemand sê dat daar gevaar is.'),
           ('skamerig', 'Effens skaam.'), ('skrikkerig', 'Maklik bang.'), ('kokosneut', '’n Groot, harde vrug van die kokospalm.'), ('ramp', '’n Groot ongeluk of verskriklike gebeurtenis.'), ('simpel', 'Dwaas of onnosel.')]

# ============================================================== 81 Hasie maak alarm
L81 = lesson(81,
  intro='Hasie is bang vir ’n aardbewing – en toe val daar iets van ’n boom af! Lees die storie en dink na oor vriendskap en vrees.',
  objectives=['Na ’n kortverhaal luister en dit self lees.', 'Die kenmerke van ’n verhaal bespreek (soos die tydvorm).', 'Oordrywing en stereotipes in ’n storie uitken.', 'Jou eie mening gee oor vriendskap tussen verskillende groepe.'],
  pass_=passage('Hasie maak alarm', STORY81, glossary=GLOSS81),
  learn=[
    text('Pre-lees, lees en post-lees', bullets=['**Voor jy lees (pre-lees):** bespreek die kenmerke van die verhaal, soos die tydvorm waarin dit geskryf is.', '**Terwyl jy lees:** luister aandagtig terwyl jou onderwyser dit voorlees, en lees dan self in groepverband.',
         '**Ná jy gelees het (post-lees):** praat oor wat die storie vir jou leer.'], page=36),
    note('Bron (soos in die werkboek): Aangepas uit “Rabbit Heralds the Earth Quake” deur Rosalind Kerven in PIRLS Reader, The Natural World, Main Survey 2001. IEA.', title='Bron van die storie', page=37),
  ],
  acts=[
    discuss('Luister aandagtig', 'Luister aandagtig na die kortverhaal terwyl jou onderwyser dit vir jou voorlees. (Of druk die knoppie.) Lees dit daarna self in groepverband.', src='workbook', speak='passage', page=36, item='Ons lees'),
    discuss('Pre-lees: die tydvorm', 'Bespreek die kenmerke van die verhaal: die tydvorm waarin die verhaal geskryf is.', page=36, item='Pre-lees'),
    mcq('In watter tyd is die storie geskryf?', 'In watter tyd is hierdie storie geskryf?', ['Teenwoordige tyd', 'Verlede tyd', 'Toekomende tyd'], 1, 'Die storie gebruik woorde soos “was”, “het … gesê” en “hardloop … het”: dit vertel van iets wat gebeur het – die verlede tyd.',
        per_option={0: 'Die storie sê “Daar was eenmaal …” – dit het reeds gebeur.', 2: 'Niks in die storie gaan oor wat nog sal gebeur nie.'}, src='supplementary', status='derived_from_text'),
    discuss('Post-lees: praat daaroor', 'Bespreek hierdie vrae in jou groep.', points=['Die haas en die leeu behoort aan verskillende spesies, en tog is hulle maats. Wat leer jy uit jou vriendskap met kinders uit ander kultuurgroepe?',
            'Watter positiewe sosiale eienskap leer die leeu ons aan die einde van die storie?', 'Bespreek of daar enige stereotipe gedrag in die storie voorkom, en hoe dit die luisteraar beïnvloed.', 'Bespreek of daar oordrywing in die storie plaasvind.'], page=36, item='Post-lees'),
    order('Die gebeure in volgorde', 'Sit die gebeure in die volgorde waarin hulle in die storie gebeur het.',
          ['Die vrug val van die boom en die aarde skud.', 'Hasie skree “Aardbewing!” en waarsku sy familie.', 'Die olifant en die kameelperde hardloop saam.', 'Die leeu vra wie die aardbewing gesien het.', 'Die leeu laat die kokosneut weer val.', 'Hasie besef dit was nie ’n aardbewing nie.'],
          'Die storie begin met die val van die kokosneut en eindig by Hasie se besef.', perm=[3, 5, 1, 0, 4, 2], src='supplementary'),
    match('Pas die woord by sy betekenis', 'Verbind elke woord met sy betekenis.', [('bekommerd', 'bang of ongelukkig oor iets wat dalk kan gebeur'), ('yslike', 'baie groot'), ('waarsku', 'sê dat daar gevaar is'), ('skamerig', 'effens skaam')],
          'Tik op ’n woord in die storie om sy betekenis te sien.', src='supplementary', status='derived_from_text'),
    fill('Voltooi die sin', 'Die {{1}} was altyd bekommerd, maar die {{2}} het hom gewys dat dit net ’n kokosneut was.', {1: ['hasie', 'haas'], 2: 'leeu'}, 'Hasie is die bekommerde een; die leeu is die dapper vriend.', bank=['hasie', 'leeu', 'olifant'], src='supplementary'),
    tf('Waar of onwaar?', 'Die leeu het die hasie uitgelag en laat voel dat hy dom was.', False, 'Die leeu het vriendelik geglimlag en gesê almal is partykeer bang vir dinge wat hulle nie verstaan nie.', src='supplementary'),
  ],
  quiz=[
    q('literal', 'Wat was die hasie se grootste bekommernis?', 'Dat daar ’n aardbewing sou kom', ['Dat ’n leeu hom sou vang', 'Dat hy sy huis sou verloor', 'Dat dit sou reën'], 'Sy grootste bekommernis was dat daar ’n aardbewing sou kom.', ev=['Sy grootste bekommernis']),
    q('literal', 'Wat het werklik die aarde laat skud?', '’n Kokosneut wat van die boom afgeval het', ['’n Aardbewing', 'Die olifant', 'Die leeu'], 'Die yslike vrug wat van die boom afval, het die aarde laat bewe.', ev=['yslike vrug skielik van ’n boom']),
    q('literal', 'Wie het die hase op die berg gekry?', 'Die leeu', ['Die olifant', 'Die kameelperde', 'Die apie'], 'Terwyl die voorste haas hyg, kom die leeu aan.', ev=['kom daar ’n leeu aan']),
    q('inference', 'Waarom het die leeu die kokosneut op die grond laat val?', 'Om die hasie te wys wat gebeur het', ['Om die hasie te laat weghol', 'Om die hasie te help om die vrug te eet', 'Om die hasie te laat lag'], 'Die leeu wou hê die hasie moet self sien dat dit net ’n kokosneut was.', ev=['laat die neut op die grond val'], src='supplementary'),
    q('inference', 'Hoe het die hasie gevoel nadat die leeu die kokosneut laat val het?', 'Verleë', ['Kwaad', 'Teleurgesteld', 'Bekommerd'], 'Hy sê: “Was ek nie ’n simpel hasie nie!”', ev=['Was ek nie ’n simpel hasie nie'], src='supplementary', status='needs_review'),
    q('main_idea', 'Wat is die verskuilde boodskap van die storie?', 'Maak seker van die feite voordat jy paniekerig word.', ['Hardloop weg van moeilikheid.', 'Hase hardloop die vinnigste.', 'Leeus is altyd gevaarlik.'], 'Die hasie het paniekerig geraak sonder om uit te vind wat die slag was.', ev=['Dit was toe nie regtig ’n aardbewing nie'], status='needs_review'),
    q('vocabulary', 'Wat beteken “bekommerd”?', 'Bang of ongelukkig oor iets wat dalk kan gebeur', ['Baie bly', 'Baie moeg', 'Baie sterk'], 'Die hasie was altyd bekommerd oor ’n aardbewing.', ev=['wat altyd bekommerd was'], status='derived_from_rule'),
    q('inference', 'Watter positiewe eienskap het die leeu aan die einde gewys?', 'Vriendelikheid en begrip', ['Koppigheid', 'Gierigheid', 'Humeurigheid'], 'Hy het vriendelik geglimlag en gesê almal is partykeer bang.', ev=['Toe maar, my ou boetie'], status='needs_review'),
    q('sequencing', 'Wat het EERSTE gebeur?', 'Die vrug het van die boom afgeval.', ['Die leeu het by die hase aangekom.', 'Die olifant het begin hardloop.', 'Die hasie het op die leeu se rug geklim.'], 'Die slag (KABOEM) het alles laat begin.', ev=['yslike vrug skielik van ’n boom']),
  ])

# ============================================================== 82 Ons dink na oor die storie
L82 = lesson(82,
  skills=[LISTEN, READ, WRITE],
  intro='Wat het in die storie gebeur en wat leer dit ons? Gebruik soekleesvaardighede, kyk na idiome en dink na oor die hasie se gevoelens.',
  objectives=['Soeklees om vrae oor ’n storie te beantwoord.', 'Idiomatiese uitdrukkings in ’n storie uitken.', 'Die intrige en die verskuilde boodskap van ’n storie uitwys.', 'Jou eie mening motiveer.'],
  pass_=passage('Hasie maak alarm (werkkaart 81)', STORY81, glossary=GLOSS81),
  learn=[
    note('Idiomatiese uitdrukkings is uitdrukkings wat eie aan die taal is. Idiome sluit in: spreekwoorde, segswyses, gesegdes en spreuke.', title='Wat is idiome?', page=38),
    note('Die intrige van ’n verhaal is die verwikkelinge van gebeure wat ’n skrywer uitdink waarop die verhaal gebaseer is.', title='Wat is die intrige?', page=39),
  ],
  acts=[
    mcq('Soeklees 1', 'Wat was die hasie se grootste bekommernis?', ['’n Leeu', '’n Slag', '’n Aardbewing', '’n Vallende boom'], 2, 'Die storie sê sy grootste bekommernis was dat daar ’n aardbewing sou kom.', per_option={0: 'Die leeu het eers later in die storie opgedaag.', 1: 'Die slag was ’n gevolg van die kokosneut.', 3: 'Dit was ’n kokosneut wat die slag veroorsaak het – nie sy grootste bekommernis nie.'}, page=38, item=1),
    mcq('Soeklees 2', 'Wat het die hele aarde laat skud?', ['’n Aardbewing', '’n Enorme kokosneut', 'Die vlugtende hasies', '’n Vallende boom'], 1, 'Die storie sê ’n yslike vrug (’n kokosneut) het van die boom afgeval – KABOEM – en die aarde laat skud.', per_option={0: 'Dit was nie ’n regte aardbewing nie.', 2: 'Hulle het eers gehardloop ná die slag.', 3: 'Dit was die vrug, nie die boom nie.'}, page=38, item=2),
    mcq('Soeklees 3', 'Waarom het die leeu die kokosneut op die grond laat val?', ['Om die hasie te laat weghol', 'Om die hasie te help om die vrug te eet', 'Om die hasie te wys wat gebeur het', 'Om die hasie te laat lag'], 2, 'Die leeu wou die hasie wys dat die slag net van die kokosneut af gekom het.', page=38, item=3),
    mcq('Soeklees 4', 'Hoe het die hasie gevoel nadat die leeu die kokosneut op die grond laat val het?', ['Kwaad', 'Teleurgesteld', 'Verleë', 'Bekommerd'], 2, 'Hy het besef hy was dwaas om so te skrik en gesê: “Was ek nie ’n simpel hasie nie!”', per_option={0: 'Hy was nie kwaad vir die leeu nie.', 1: 'Hy is nie teleurgesteld nie – hy skaam hom.', 3: 'Hy is nie meer bekommerd nie, want hy weet nou wat gebeur het.'}, page=38, item=4, status='needs_review'),
    mcq('Die verskuilde boodskap', 'Wat is die verskuilde boodskap van die storie?', ['Hardloop weg van moeilikheid.', 'Maak seker van die feite voordat jy paniekerig word.', 'Hase hardloop die vinnigste.'], 1, 'Hasie het gehardloop sonder om uit te vind wat die slag was.', page=38, item=5, status='needs_review'),
    sa('Dinge het vinnig gebeur', 'Dinge het vinnig gebeur nadat die hasie “Aardbewing!” geskree het. Kopieer twee woorde uit die storie wat dit vir ons sê.', 'verwoed, snel (ook: stormende, donderweer)', lines=1, page=38, item=6, status='derived_from_text'),
    sa('Waarheen?', 'Waarheen het die leeu die hasie versoek om hom te neem?', 'Na die plek waar die “ramp” gebeur het – by die hasie se huis.', lines=1, page=38, item=7, status='derived_from_text'),
    sa('Idiome', 'Onderstreep drie idiomatiese uitdrukkings in die storie “Hasie maak alarm”. Skryf hulle hier neer.', 'bv. “Hardloop vir die vale”, “uit sy maag lag”, “soos donderweer”, “so vining as wat my bene my kon dra”', lines=3, page=38, item=8, status='needs_review'),
    sa('Die leeu se woorde', 'Aan die einde van die storie het die leeu iets gesê om hasie beter te laat voel. Skryf die aanhaling uit die teks neer.', '“Toe maar, my ou boetie. Almal van ons – selfs ek ook – is partykeer bang vir die dinge wat ons nie verstaan nie.”', lines=2, page=38, item=9, status='derived_from_text'),
    writing('Hoe het die hasie se gevoelens verander?', 'Voltooi die sinne: Aan die begin van die storie het die hasie … gevoel want … Aan die einde van die storie het die hasie … gevoel want … Aan die einde was dit duidelik dat die leeu van die hasie hou want …',
            checklist=['Ek het ’n gevoel by die begin genoem en gesê hoekom.', 'Ek het ’n gevoel by die einde genoem en gesê hoekom.', 'Ek het gewys hoe die leeu gewys het dat hy van die hasie hou.'], lines=6, page=39, item='gevoelens'),
    sa('Waar speel die storie af?', 'Waar speel die storie hom af?', 'In die veld en in die natuur, by ’n boom naby die hasie se huis, en op die pad na die berg.', lines=1, page=39, item='tabel 1', status='needs_review'),
    sa('Die twee hoofkarakters', 'Wie is die 2 hoofkarakters van die storie?', 'Die hasie en die leeu.', lines=1, page=39, item='tabel 2', status='derived_from_text'),
    sa('Die intrige', 'Omskryf die intrige van die verhaal in jou eie woorde.', None, lines=4, page=39, item='tabel 3'),
    discuss('Jou mening', 'Dink en motiveer jou antwoord.', points=['Dink jy dit is goed dat die hasie en die leeu vriende is, al behoort hulle aan verskillende spesies? Motiveer jou antwoord.', 'Dink jy dit is goed om maats te wees met iemand uit ’n ander kultuurgroep? Motiveer jou antwoord.',
            'Watter sosiale waardes kan ons aan die einde van die storie by die leeu leer?'], page=39, item='mening'),
    tf('Waar of onwaar?', 'Die intrige van ’n storie is die boodskap wat die skrywer wil oordra.', False, 'Die intrige is die gebeure (die storielyn). Die boodskap is die tema.', status='derived_from_rule'),
  ],
  quiz=[
    q('literal', 'Wat was die hasie se grootste bekommernis?', 'Dat daar ’n aardbewing sou kom', ['’n Leeu', '’n Slag', '’n Vallende boom'], 'Dit staan duidelik aan die begin van die storie.', ev=['Sy grootste bekommernis'], src='workbook', page=38, item=1),
    q('literal', 'Wat het die hele aarde laat skud?', '’n Enorme kokosneut', ['’n Aardbewing', 'Die vlugtende hasies', '’n Vallende boom'], 'Die yslike vrug (kokosneut) het die aarde laat skud.', ev=['yslike vrug skielik van ’n boom'], src='workbook', page=38, item=2),
    q('inference', 'Waarom het die leeu die kokosneut op die grond laat val?', 'Om die hasie te wys wat gebeur het', ['Om die hasie te laat weghol', 'Om die hasie te help om die vrug te eet', 'Om die hasie te laat lag'], 'Die leeu wou die hasie die waarheid wys.', ev=['laat die neut op die grond val'], src='workbook', page=38, item=3),
    q('inference', 'Hoe het die hasie gevoel nadat die leeu die kokosneut laat val het?', 'Verleë', ['Kwaad', 'Teleurgesteld', 'Bekommerd'], 'Hy het besef dat hy dwaas was.', ev=['Was ek nie ’n simpel hasie nie'], src='workbook', page=38, item=4, status='needs_review'),
    q('main_idea', 'Wat is die verskuilde boodskap van die storie?', 'Maak seker van die feite voordat jy paniekerig word.', ['Hardloop weg van moeilikheid.', 'Hase hardloop die vinnigste.'], 'Hasie het paniek gemaak sonder om uit te vind wat werklik gebeur het.', src='workbook', page=38, item=5, status='needs_review'),
    q('vocabulary', 'Wat is idiome?', 'Uitdrukkings wat eie aan die taal is, soos spreekwoorde en segswyses', ['Woorde met dieselfde betekenis', 'Lang stories', 'Woorde wat dieselfde klink'], 'Die werkboek verduidelik: idiomatiese uitdrukkings is uitdrukkings wat eie aan die taal is.', status='official', src='workbook', page=38),
    q('vocabulary', 'Wat is die “intrige” van ’n verhaal?', 'Die verwikkelinge van gebeure waarop die verhaal gebaseer is', ['Die plek van die verhaal', 'Die karakters', 'Die titel'], 'Die werkboek sê dit in die nota op bladsy 39.', status='official', src='workbook', page=39),
    q('inference', 'Wat dink die leeu van die hasie se vrees?', 'Dis normaal om partykeer bang te wees vir dinge wat ons nie verstaan nie.', ['Dit is dom om bang te wees.', 'Net hasies word bang.', 'Bang wees is verkeerd.'], 'Hy sê: “Almal van ons … is partykeer bang vir die dinge wat ons nie verstaan nie.”', ev=['partykeer bang vir die dinge'], status='derived_from_text'),
  ])

# ============================================================== 83 Kom ons skryf die storie
L83 = lesson(83,
  skills=[LISTEN, WRITE],
  pass_=passage('Hasie maak alarm (werkkaart 81)', STORY81, glossary=GLOSS81),
  intro='Nou is dit jou beurt om die storie van Hasie en die leeu weer te vertel – in jou eie woorde en in die regte volgorde.',
  objectives=['’n Geheuekaart gebruik om ’n storie te beplan.', 'Die gebeure van ’n storie in die korrekte volgorde oorvertel.', 'Die skryfproses volg.'],
  learn=[
    text('Die skryfproses', bullets=['**Beplan** jou storie deur die breinkaart te voltooi.', 'Skryf jou **eerste weergawe** in jou klaswerkboek.', 'Laat ’n maat jou werk **hersien**.', '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** vir publikasie.'], page=41),
    text('Woorde wat help om te vertel', 'Gebruik woorde soos **eers**, **toe**, **daarna**, **later** en **uiteindelik** om die gebeure in die regte volgorde te vertel.', src='supplementary', page=40),
  ],
  acts=[
    discuss('Dinkskrum', 'Gebruik die geheuekaart om jou te help om die storie “Hasie maak alarm” in die korrekte volgorde oor te vertel. Hou ’n dinkskrum saam met jou maats oor wat in die storie gebeur.', page=40, item='dinkskrum'),
    order('Die storie in ses stappe', 'Sit die ses hoofgebeure van die storie in die regte volgorde (soos die ses blokkies in die geheuekaart).',
          ['Hasie is bekommerd oor ’n aardbewing.', 'Die kokosneut val en Hasie hardloop weg.', 'Al die diere hardloop saam met Hasie.', 'Die leeu stop hulle en vra wat aan die gang is.', 'Die leeu en Hasie gaan na die boom en die leeu laat die neut val.', 'Hasie besef dit was ’n kokosneut en die leeu stel hom gerus.'],
          'Die storie volg hierdie ses stappe van die begin tot die einde.', perm=[2, 5, 0, 4, 1, 3], src='supplementary'),
    writing('Skryf jou idees by die prente', 'Skryf jou idees langs die ses prente (1 tot 6) in die geheuekaart neer.', lines=8, page=40, item='geheuekaart'),
    writing('Jou finale weergawe', 'Skryf jou finale weergawe van die storie netjies neer (een paragraaf vir elke prent).',
            checklist=['Ek het die gebeure in die korrekte volgorde vertel.', 'Ek het woorde soos eers, toe, daarna, later en uiteindelik gebruik.', 'Ek het my storie in my eie woorde oorvertel.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=14, page=41, item='finale weergawe'),
    fill('Verbindingswoorde', '{{1}} was Hasie bekommerd. {{2}} het ’n kokosneut geval en daarna het hy gehardloop. {{3}} het die leeu hom gewys dat dit net ’n kokosneut was.', {1: 'Eers', 2: 'Toe', 3: ['Uiteindelik', 'Later']}, 'Tydwoorde help ons die gebeure in volgorde vertel.', bank=['Eers', 'Toe', 'Uiteindelik'], src='supplementary', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Jy hoef nie jou eerste weergawe te laat hersien nie.', False, 'Die skryfproses sê: laat ’n maat jou werk hersien en korrigeer die foute.', status='official'),
  ],
  quiz=[
    q('sequencing', 'Wat is die eerste stap van die skryfproses?', 'Beplan', ['Publiseer', 'Korrigeer', 'Hersien'], 'Die werkboek begin met beplan (die breinkaart).', status='official', src='supplementary', page=41),
    q('sequencing', 'Wie hersien jou eerste weergawe?', '’n Maat', ['Die skrywer van die storie', 'Niemand nie', 'Die leeu'], 'Die skryfproses sê: laat ’n maat jou werk hersien.', status='official', src='supplementary', page=41),
    q('sequencing', 'Wat gebeur in die storie ná die kokosneut val?', 'Hasie hardloop weg en waarsku die ander.', ['Die leeu eet die hasie.', 'Die olifant gaan huis toe.', 'Die apie val.'], 'Hasie skree “Aardbewing!” en waarsku sy neefs en niggies.', ev=['Aardbewing!” skree hy'], status='derived_from_text'),
    q('grammar', 'Watter woord help om gebeure in volgorde te vertel?', 'daarna', ['mooi', 'groot', 'hond'], 'Tydwoorde soos daarna wys volgorde.', status='derived_from_rule', src='supplementary'),
    q('main_idea', 'Hoekom het die leeu die hasie teruggeneem na die boom?', 'Om hom te wys wat die slag veroorsaak het', ['Om hom te vang', 'Om kokosneute te eet', 'Om ’n huis te bou'], 'Die leeu het die kokosneut laat val om die waarheid te wys.', ev=['laat die neut op die grond val'], status='derived_from_text'),
    q('literal', 'Wie het saam met die hase gehardloop?', 'Die olifant en die kameelperde', ['Die leeu en die apie', 'Net die jakkals', 'Niemand nie'], 'Die olifant en die kameelperde het agter die hase aangehardloop.', ev=['Die kameelperde begin aanhardloop'], status='derived_from_text'),
    q('sequencing', 'Wat is die LAASTE gebeurtenis in die storie?', 'Die leeu vertel die ander diere dat alles veilig is.', ['Die hasie hardloop weg.', 'Die kokosneut val.', 'Die leeu kry die hase.'], 'Aan die einde loop die leeu terug en sê dit is veilig om huis toe te gaan.', ev=['alles heeltemal veilig is'], status='derived_from_text'),
    q('main_idea', 'Hoeveel stappe het die geheuekaart vir die storie?', 'Ses', ['Twee', 'Drie', 'Tien'], 'Daar is ses prente (1 tot 6) in die geheuekaart.', status='official', src='supplementary', page=40),
  ])

# ============================================================== 84 Ons hersien briewe
LETTER84 = ['Appelweg 27', 'Kaapstad', '8001', '17 Julie 2015', 'Liewe Danie',
  'Sjoe, ek was baie gelukkig die vakansie: ek kon saam met my nefies Kaapstad toe gaan! Ons het 12 Julie met die trein vertrek en die volgende dag daar aangekom. Dit was pret om met die trein te ry. Ons het ons eie kompartement gehad, en ek het op die boonste slaapbank geslaap!',
  'Die eerste ding wat ek gesien het toe ons in Kaapstad aangekom het, was Tafelberg met sy wit, watteagtige “tafeldoek”. Die berg was indrukwekkender as wat ek ooit verwag het dit sou wees.',
  'Kyk na die foto’s wat ek aangeheg het, dan sal jy sien wat ek bedoel.',
  'Die tweede dag het ons Robbeneiland besoek. Ons het per boot na die eiland gevaar. Ons het na die sel gaan kyk waarin Nelson Mandela 18 jaar lank aangehou is! Die eiland is baie rotsagtig, en ons het baie pikkewyne gesien.',
  'Op die derde dag het ons weer die pikkewyne gesien. Hierdie keer was dit op ’n strandjie wat hulle Boulders noem. Ons het ook Kaapse pelsrobbe daar gesien. Kaapstad loods ’n projek om die robbe te beskerm, aangesien hulle aan die uitsterf is. Die projek beskerm ook die pikkewyne.',
  'Op dag vier het ons Kaappunt besoek. Dit is die suidelikste punt van Afrika, waar twee oseane mekaar ontmoet. Dit is hier dat die koue water van die Atlantiese Oseaan en die warm seestrome van die Indiese Oseaan saamvloei.',
  'Vandag – ons laaste dag – het ons na die seelewe in die Twee Oseane-akwarium gaan kyk. Dit was ’n fantastiese belewenis! Ek was nog nooit tevore so naby aan ’n haai nie! Daar was net ’n glaspaneel tussen ons, en die haaie was nie skaam om hulle rye tande vir ons te wys nie. Ons het ook allerhande soorte stervisse gesien – party met vyftig arms! As hulle ’n arm verloor, groei daar ’n nuwe een in sy plek.',
  'Môre vertrek ons weer huis toe. Ek kan nie wag om julle almal weer by die skool te sien nie.', 'Jou maat', 'Jan']

L84 = lesson(84,
  skills=[LISTEN, READ, WRITE, LANG],
  intro='Jan het ’n wonderlike vakansie in Kaapstad gehad – en hy vertel sy maat Danie daarvan in ’n brief. Luister, lees en hersien hoe ’n brief werk.',
  objectives=['Na ’n vriendskaplike brief luister en die eienskappe van ’n brief bespreek.', 'Spesifieke vrae oor ’n brief soeklees en beantwoord.', 'Die teenwoordige, verlede en toekomende tyd, en die ontkenningsvorm herken.', 'Woorde in ’n woordeboek naslaan en in sinne gebruik.'],
  pass_=passage('Ons hersien briewe: Jan se brief', LETTER84, glossary=[('watteagtige', 'Soos watte: sag en wit.'), ('indrukwekkender', 'Meer indrukwekkend (wat jou beïndruk).'), ('loods', 'Begin of stel in werking.'), ('uitsterf', 'Heeltemal verdwyn, sodat daar geen meer oor is nie.'), ('stervisse', 'Seediere met arms in die vorm van ’n ster.'), ('kompartement', '’n Aparte afdeling of hokkie in ’n trein.')]),
  learn=[
    table('Tydvorme en ontkenning', ['Vorm', 'Wat dit beteken'], [['Teenwoordige tyd', 'verwys na die hede'], ['Verlede tyd', 'verwys na gebeure wat reeds gebeur het'], ['Toekomende tyd', 'verwys na dinge wat nog moet gebeur'],
          ['Ontkenning', 'word in die negatiewe vorm gestel, bv. Sy het nie gebel nie.']], page=43),
    text('Wat staan in ’n vriendskaplike brief?', bullets=['Die adres en die datum bo-aan', 'Die aanhef (“Liewe …”)', 'Die inhoud in paragrawe', 'Die groet en jou naam (bv. “Jou maat, Jan”)'], src='supplementary', page=42),
  ],
  acts=[
    discuss('Luister na die brief', 'Luister aandagtig na hierdie vriendskaplike brief terwyl jou onderwyser dit voorlees. (Of druk die knoppie.)', speak='passage', page=42, item='Ons lees'),
    discuss('Eienskappe van ’n brief', 'Bespreek die eienskappe van ’n brief nadat jy na die brief geluister het.', page=42, item='Ons praat'),
    mcq('Vraag 1', 'Waarom skryf Jan hierdie brief aan Danie?', ['Om hom van die haaie te vertel.', 'Om hom van sy heerlike vakansie te vertel.', 'Om te sê dat hy binnekort terug sal wees.', 'Om hom van die treinrit te vertel.'], 1,
        'Jan vertel van sy hele vakansie in Kaapstad, nie net van een ding nie.', per_option={0: 'Die haaie is net een deel van die vakansie.', 2: 'Dit is slegs ’n klein deel van die slot.', 3: 'Die treinrit is net die begin van sy vakansie.'}, page=43, item=1),
    mcq('Vraag 2', 'Wat bedoel Jan wanneer hy sê dat die haaie “nie skaam was” om hulle rye tande te wys nie?', ['Die haaie was vriendelik.', 'Die haaie het hulle vermaak.', 'Die haaie het hulle bekke oopgemaak.', 'Die haaie het ander visse gevreet.'], 2,
        '“Rye tande wys” beteken om die bek oop te maak sodat jy die tande kan sien.', page=43, item=2),
    sa('Goeie maats', 'Skryf ’n frase uit die brief neer wat wys dat Jan en Danie goeie maats is.', '“Jou maat” / “Ek kan nie wag om julle almal weer by die skool te sien nie.”', lines=1, page=43, item=3, status='needs_review'),
    sa('Ewe oud', 'Haal ’n sin uit die brief aan wat aandui dat Jan en Danie ewe oud is.', 'Dit is nie direk gesê nie. Aanvaarbaar: “Ek kan nie wag om julle almal weer by die skool te sien nie” (hulle is in dieselfde skool).', lines=2, page=43, item=4, status='needs_review'),
    sa('Eerste keer in Kaapstad', 'Haal ’n sin uit die brief aan wat aandui dat Jan nog nooit tevore in Kaapstad was nie.', 'Die berg was indrukwekkender as wat ek ooit verwag het dit sou wees.', lines=2, page=43, item=5, status='needs_review'),
    choices('Watter tyd of vorm?', 'Dui die tyd of vorm van elke sin aan.',
            [('Ons het ons eie kompartement gehad.', ['verlede tyd', 'teenwoordige tyd', 'toekomende tyd', 'ontkenning'], 0), ('Dit is die suidelikste punt van Afrika.', ['verlede tyd', 'teenwoordige tyd', 'toekomende tyd', 'ontkenning'], 1),
             ('Môre vertrek ons weer huis toe.', ['verlede tyd', 'teenwoordige tyd', 'toekomende tyd', 'ontkenning'], 2), ('Ek kan nie wag om julle almal weer by die skool te sien nie.', ['verlede tyd', 'teenwoordige tyd', 'toekomende tyd', 'ontkenning'], 3)],
            'Verlede = het … gehad; teenwoordig = is; toekomend = môre (iets wat nog gaan gebeur); ontkenning = nie … nie.', src='workbook', page=43, item='tydvorme', status='needs_review'),
    sa('Woordeboek: indrukwekkend en uitsterf', 'Slaan hierdie woorde in ’n woordeboek na en gebruik hulle dan in ’n sin om te wys wat hulle beteken: indrukwekkend; uitsterf.', None, lines=3, page=43, item='woordeboek'),
    order('Jan se reis in volgorde', 'Sit Jan se uitstappies in die volgorde waarin hulle in die brief genoem word.', ['Hy ry met die trein na Kaapstad.', 'Hy sien Tafelberg.', 'Hy besoek Robbeneiland.', 'Hy sien pikkewyne en robbe by Boulders.', 'Hy besoek Kaappunt.', 'Hy besoek die Twee Oseane-akwarium.'],
          'Jan vertel sy reis dag vir dag.', perm=[4, 1, 5, 0, 3, 2], src='supplementary'),
    fill('Voltooi die brief-reël', 'Jan sluit sy brief af met “{{1}} maat”. Hy skryf die datum ({{2}} Julie 2015) en sy adres bo-aan.', {1: 'Jou', 2: '17'}, 'Die brief eindig met “Jou maat, Jan”; die datum is 17 Julie 2015.', src='supplementary', bank=['Jou', 'Julle', '17']),
  ],
  quiz=[
    q('literal', 'Op watter datum het Jan die brief geskryf?', '17 Julie 2015', ['12 Julie 2015', '13 Julie 2015', '1 Augustus 2015'], 'Die datum staan bo-aan die brief.', ev=['17 Julie 2015']),
    q('literal', 'Hoe het Jan en sy nefies na Kaapstad gereis?', 'Met die trein', ['Met die bus', 'Met die vliegtuig', 'Met ’n motor'], 'Ons het 12 Julie met die trein vertrek.', ev=['met die trein vertrek']),
    q('literal', 'Wat het Jan op die eerste dag in Kaapstad gesien?', 'Tafelberg', ['Robbeneiland', 'Kaappunt', '’n Haai'], 'Die eerste ding was Tafelberg met sy wit “tafeldoek”.', ev=['Die eerste ding wat ek gesien het']),
    q('literal', 'Wie was vir 18 jaar op Robbeneiland aangehou?', 'Nelson Mandela', ['Jan', 'Danie', 'Die burgemeester'], 'Hulle het na die sel gaan kyk waarin Nelson Mandela 18 jaar lank aangehou is.', ev=['Nelson Mandela 18 jaar lank']),
    q('literal', 'Wat is Kaappunt?', 'Die suidelikste punt van Afrika', ['’n Strand vir pikkewyne', '’n Eiland', '’n Akwarium'], 'Dit is die suidelikste punt van Afrika, waar twee oseane ontmoet.', ev=['suidelikste punt van Afrika']),
    q('inference', 'Waarom skryf Jan die brief?', 'Om sy maat van sy heerlike vakansie te vertel', ['Om om hulp te vra', 'Om te kla', 'Om ’n verjaardag te onthou'], 'Hy vertel van sy hele reis.', ev=['Sjoe, ek was baie gelukkig'], src='workbook', page=43, item=1, status='derived_from_text'),
    q('vocabulary', 'Wat beteken “die haaie was nie skaam om hulle rye tande te wys nie”?', 'Die haaie het hulle bekke oopgemaak.', ['Die haaie was vriendelik.', 'Die haaie het ander visse gevreet.', 'Die haaie het geslaap.'], 'Hulle het hul bekke oopgemaak sodat die tande sigbaar was.', ev=['rye tande vir ons te wys'], src='workbook', page=43, item=2, status='derived_from_text'),
    q('grammar', 'Watter sin is in die verlede tyd?', 'Ons het per boot na die eiland gevaar.', ['Dit is die suidelikste punt van Afrika.', 'Môre vertrek ons weer huis toe.', 'Ek kan nie wag nie.'], 'Verlede tyd gebruik “het” + ge-vorm of ’n verlede werkwoord.', ev=['per boot na die eiland'], src='workbook', page=43, item='tydvorme', status='derived_from_rule'),
    q('grammar', 'Hoe lyk die ontkenningsvorm?', 'Die woord “nie” verskyn gewoonlik twee keer.', ['Die woord “nie” verskyn nooit.', 'Die sin begin altyd met “nee”.', 'Die sin eindig altyd met ’n vraagteken.'], 'Die werkboek gee as voorbeeld: Sy het nie gebel nie.', status='official', src='workbook', page=43),
  ])

# ============================================================== 85 Kom ons skryf ook 'n brief
L85 = lesson(85,
  skills=[WRITE],
  intro='Jan het vir Danie geskryf – nou skryf jy ook ’n brief aan jou maat! Die werkboek gee vir jou idees vir elke paragraaf.',
  objectives=['’n Brief met die korrekte uitleg skryf (adres, datum, aanhef, paragrawe, slot).', '’n Maat vir sy of haar brief bedank.', 'Skryf oor gebeure en aktiwiteite van nou en van die toekoms.'],
  learn=[
    text('Idees vir elke paragraaf', bullets=['**Paragraaf 1:** bedank jou maat vir haar of sy brief.', '**Paragraaf 2:** skryf oor jou eerste gebeurtenis of aktiwiteit.', '**Paragraaf 3:** skryf oor jou tweede gebeurtenis of aktiwiteit.', '**Paragraaf 4:** sluit af deur te verwys na iets wat in die toekoms gaan gebeur.'], page=44),
    table('Die uitleg van jou brief', ['Deel', 'Wat jy skryf'], [['Adres', 'Jou adres (bo-aan)'], ['Datum', 'Die datum'], ['Aanhef', 'Liewe … (jou maat se naam)'], ['Inhoud', 'Die vier paragrawe'], ['Slot', 'Sluit jou brief af; “Jou maat” en jou naam']], page=45),
  ],
  acts=[
    discuss('Beplan jou brief', 'Skryf ’n brief aan jou maat waarin jy hom of haar vertel van die dinge waarmee jy tuis en by die skool besig is, of van aktiwiteite wat in die toekoms gaan plaasvind. Praat eers met ’n maat daaroor.', page=44, item='Ons skryf'),
    order('Die paragrawe in volgorde', 'Sit die dele van jou brief in die regte volgorde.', ['Aanhef: Liewe … (jou maat se naam)', 'Bedank jou maat vir sy of haar brief.', 'Skryf oor jou eerste gebeurtenis of aktiwiteit.', 'Skryf oor jou tweede gebeurtenis of aktiwiteit.', 'Sluit af met iets wat in die toekoms gaan gebeur.'],
          'Die werkboek gee die volgorde van die idees vir elke paragraaf.', perm=[3, 0, 4, 1, 2], src='workbook', page=44, item='paragrawe', status='official'),
    writing('Skryf jou brief', 'Skryf ’n brief aan jou maat. Gebruik die uitleg wat die werkboek vir jou voorsien.',
            checklist=['Ek het my adres bo-aan geskryf.', 'Ek het die datum geskryf.', 'Ek het begin met “Liewe …” en my maat se naam.', 'Paragraaf 1: ek het my maat bedank vir sy of haar brief.', 'Paragraaf 2 en 3: ek het oor twee gebeurtenisse of aktiwiteite geskryf.', 'Paragraaf 4: ek het verwys na iets wat in die toekoms gaan gebeur.', 'Ek het “Jou maat” en my naam onderaan geskryf.', 'Ek het my spelling en punktuasie gekorrigeer.'],
            tips=['Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe vir publikasie.'], lines=14, page=45, item='brief'),
    choices('Watter paragraaf is dit?', 'Watter paragraaf pas by watter idee?', [('Dankie vir jou brief!', ['Paragraaf 1', 'Paragraaf 2', 'Paragraaf 4'], 0), ('Môre gaan ek saam met my ouma na die mark.', ['Paragraaf 1', 'Paragraaf 2', 'Paragraaf 4'], 2), ('Verlede week het ek ’n sokkerwedstryd gewen.', ['Paragraaf 1', 'Paragraaf 2', 'Paragraaf 4'], 1)],
            'Paragraaf 1 bedank; paragrawe 2 en 3 vertel gebeure; paragraaf 4 verwys na die toekoms.', src='supplementary', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Die aanhef van jou brief is “Liewe” gevolg deur jou maat se naam.', True, 'Die werkboek gee “Liewe ________” as die aanhef.', status='official'),
  ],
  quiz=[
    q('main_idea', 'Waarmee begin jou brief direk onder die datum?', 'Met ’n aanhef (“Liewe …”)', ['Met die groet', 'Met ’n prent', 'Met jou handtekening'], 'Die werkboek sê: begin met ’n aanhef.', status='official', src='supplementary', page=45),
    q('main_idea', 'Waaroor gaan paragraaf 1 van die brief?', 'Om jou maat vir sy of haar brief te bedank', ['Om te kla', 'Om die toekoms te beplan', 'Om jou adres te gee'], 'Die werkboek sê: bedank jou maat vir haar of sy brief.', status='official', src='supplementary', page=44),
    q('main_idea', 'Waaroor gaan die laaste paragraaf?', 'Iets wat in die toekoms gaan gebeur', ['Die verlede', 'Net die weer', 'Die datum'], 'Sluit af deur te verwys na iets wat in die toekoms gaan gebeur.', status='official', src='supplementary', page=44),
    q('grammar', 'Wat skryf jy bo-aan jou brief?', 'Jou adres en die datum', ['Net jou naam', 'Die aanhef en handtekening', 'Die sedeles'], 'Die uitleg wys eers die adres en datum.', status='derived_from_rule', src='supplementary', page=45),
    q('grammar', 'Hoe sluit jy jou vriendskaplike brief af?', 'Met “Jou maat” en jou naam', ['Met “Hoogagtend”', 'Met “Geagte meneer”', 'Met niks nie'], 'Die werkboek se uitleg het “Jou maat” onderaan.', status='official', src='supplementary', page=45),
    q('grammar', 'Watter sin verwys na die toekoms?', 'Volgende week gaan ek jou besoek.', ['Gister het ek jou gebel.', 'Ek was by die skool.', 'Ek het nie gebel nie.'], '“gaan + werkwoord” of “sal” wys die toekoms.', status='derived_from_rule', src='supplementary'),
    q('sequencing', 'Wat doen jy ná jou eerste weergawe?', 'Laat ’n maat jou werk hersien', ['Gooi dit weg', 'Stuur dit sonder om dit te lees', 'Skryf dit nie oor nie'], 'Die werkboek sê: laat ’n maat jou werk hersien en korrigeer spelfoute.', status='official', src='supplementary', page=44),
    q('main_idea', 'Oor wat kan jy in paragraaf 2 en 3 skryf?', 'Dinge waarmee jy tuis en by die skool besig is', ['Net die weer', 'Net jou naam', 'Net jou adres'], 'Die opdrag sê jy skryf oor gebeurtenisse of aktiwiteite.', status='official', src='supplementary', page=44),
  ])

# ============================================================== 86 'n E-pos van 'n maat
EMAIL86 = ['Aan: anita@skool.com; danie@skool.com', 'Van: kin@biblioteek.com', '13 Augustus 2015 11:56', 'Liewe Anita en Danie,',
  'Ek veronderstel julle het die nuus gelees oor die geweldige aardbewing in Japan. Na die gebeure het ek by my neef in Suid-Japan kom woon, en ek sal hier bly totdat die situasie tuis in Tokio verbeter. Alhoewel ek dankbaar is dat ek nou ver van die episentrum af is, mis ek my gesin en my maats by ons Internasionale Laerskool baie.',
  'Ek geniet dit om by my neef te kuier. Hy is ook 12 en ons is albei in graad 6. My nefie woon gelukkig naby die sentrale park, waar ons op die rondomtalie en swaaie kan speel.',
  'As dit net nie so koud was nie! Tussen ons speeltye bestee ek tyd aan my gunstelingstokperdjies – lees en rekenaarspeletjies. Ek lees ook nou die Oerwoudboek, en ek wens ek kon in Afrika woon. Ek is amper halfpad deur die boek.',
  'Ek hoop ek hoor gou van julle.', 'Julle maat', 'Kin Hosh']

L86 = lesson(86,
  skills=[READ, WRITE, LANG],
  intro='Vandag lees jy ’n e-pos van Kin, wat ver van die huis af bly. Jy leer ook meer oor homonieme, homofone, woordvorming en verkleinwoorde.',
  objectives=['’n E-pos lees en bepaalde vrae soeklees.', 'Inligting uit ’n e-pos in ’n tabel invul.', 'Homonieme en homofone uitken.', 'Samestellings en afleidings uitken en verkleinwoorde vorm.'],
  pass_=passage('’n E-pos van ’n maat', EMAIL86, glossary=[('episentrum', 'Die punt op die aarde direk bo die plek waar ’n aardbewing begin.'), ('situasie', 'Hoe dinge op ’n bepaalde tyd is.'), ('rondomtalie', '’n Draaiende speeltoestel waarop kinders ry.'), ('gunstelingstokperdjies', 'Die stokperdjies (tydverdryf) wat jy die liefste het.'), ('Internasionale', 'Van baie lande; tussen lande.')]),
  learn=[
    note('Ons kan ook met maats of ander mense kommunikeer deur vir hulle e-posse te skryf, wat deur middel van die internet gestuur word. Ons stuur dikwels e-posse in plaas van gewone briewe om nuus met vriende te deel. Om vir iemand ’n e-pos te stuur, het jy sy of haar e-posadres nodig, en moet jy toegang tot die internet hê.', title='Wat is ’n e-pos?', page=46),
    note('**Homonieme** is woorde wat dieselfde lyk en klink, maar verskillende betekenisse het. **Homofone** klink dieselfde, maar word verskillend gespel en het verskillende betekenisse.', title='Homonieme en homofone', page=47),
    table('Verkleinwoorde: agtervoegsels', ['Agtervoegsel', 'Reël', 'Voorbeeld'], [['-jie', 'woorde wat op -t of -d eindig', 'hond – hondjie'], ['-tjie', '', 'venster – venstertjie'], ['-kie', 'meerlettergrepige woorde op -ng: gooi die g weg', 'doring – dorinkie'], ['-etjie', 'eenlettergrepige woorde op -ng', 'wang – wangetjie'], ['-pie', 'woorde wat op -m eindig', 'arm – armpie'], ['-ie', '', 'oog – ogie']], page=47),
  ],
  acts=[
    discuss('Luister na die e-pos', 'Druk die knoppie en luister terwyl jy die e-pos saamlees.', src='supplementary', speak='passage'),
    sa('By wie kuier Kin?', 'By wie kuier Kin?', 'By sy neef in Suid-Japan.', lines=1, page=46, item=1, status='derived_from_text'),
    sa('Waarom is hy daar?', 'Waarom het hy daarheen gegaan?', 'Daar was ’n geweldige aardbewing in Japan en hy bly by sy neef totdat die situasie tuis in Tokio verbeter.', lines=2, page=46, item=2, status='derived_from_text'),
    fill('Datum, naam en inligting', 'Op watter datum het hy die e-pos geskryf? {{1}}\nNaam: {{2}}\nOuderdom: {{3}}\nGraad: {{4}}\nSkool: {{5}}', {1: '13 Augustus 2015', 2: 'Kin Hosh', 3: ['12', '12 jaar'], 4: ['6', 'graad 6'], 5: ['Internasionale Laerskool', 'Internasionale laerskool']},
         'Die inligting kom uit die e-pos: die datum bo-aan, sy naam onderaan, “Hy is ook 12” en “albei in graad 6”.', src='workbook', page=46, item='tabel', status='derived_from_text'),
    sa('Kin se stokperdjies', 'Wat is Kin se stokperdjies? (Vul in die tabel.)', 'Lees en rekenaarspeletjies.', lines=1, page=46, item='tabel 6', status='derived_from_text'),
    choices('Homoniem of homofoon?', 'Is die onderstreepte woordpare homonieme of homofone?',
            [('reis / rys (Hy reis na Japan. – In Japan eet hulle rys.)', ['homoniem', 'homofoon'], 1), ('berg (Tafelberg is ’n hoë berg. – Hulle berg die voedsel in die koelkamers.)', ['homoniem', 'homofoon'], 0),
             ('bly (Ek bly baie lekker in Tokio. – Ek was baie bly toe ek jou e-pos ontvang het.)', ['homoniem', 'homofoon'], 0), ('lei / ly (Kin lei die debat. – Sy ma ly aan asma.)', ['homoniem', 'homofoon'], 1),
             ('vlei / vly (Die eend swem in die vlei. – Die meisie vly haar op die bank neer.)', ['homoniem', 'homofoon'], 1), ('brak (Ek kan nie hierdie brak water drink nie. – Die brak blaf.)', ['homoniem', 'homofoon'], 0)],
            'Homonieme lyk en klink dieselfde. Homofone klink dieselfde maar word anders gespel.', src='workbook', page=47, item='homonieme', status='derived_from_rule'),
    choices('Afleiding of samestelling?', 'Hierdie woorde kom uit Kin se e-pos. Afleiding of samestelling?',
            [('gebeure', ['afleiding', 'samestelling'], 0), ('veronderstel', ['afleiding', 'samestelling'], 0), ('rekenaarspeletjie', ['afleiding', 'samestelling'], 1), ('halfpad', ['afleiding', 'samestelling'], 1), ('swaaie', ['afleiding', 'samestelling'], 0)],
            'Samestelling = twee basiswoorde (rekenaar + speletjie; half + pad). Afleiding = basis + voor- of agtervoegsel.', src='workbook', page=47, item='woorddele', status='needs_review'),
    fill('Verkleinwoorde', 'aardbewing: {{1}}\nlaerskool: {{2}}\nneef: {{3}}\npark: {{4}}\ngesin: {{5}}\nswaai: {{6}}\nmaats: {{7}}\nboek: {{8}}',
         {1: 'aardbewinkie', 2: 'laerskooltjie', 3: ['neefie', 'nefie'], 4: 'parkie', 5: ['gesinnetjie', 'gesinnie'], 6: 'swaaitjie', 7: ['maatjies', 'maatjie'], 8: 'boekie'},
         'Kyk na die reëls vir -jie, -tjie, -kie, -etjie, -pie en -ie.', prompt='Gee die verkleiningsvorm van hierdie woorde uit Kin se e-pos.', src='workbook', page=47, item='verkleinwoorde', status='needs_review'),
    tf('Waar of onwaar?', 'Jy het ’n e-posadres en toegang tot die internet nodig om ’n e-pos te stuur.', True, 'Die werkboek sê dit in die nota oor e-posse.', status='official'),
  ],
  quiz=[
    q('literal', 'By wie bly Kin?', 'By sy neef in Suid-Japan', ['By sy ouma in Tokio', 'By sy maats by die skool', 'By sy onderwyser'], 'Hy het by sy neef in Suid-Japan kom woon.', ev=['by my neef in Suid-Japan'], src='workbook', page=46, item=1),
    q('literal', 'Waarom is Kin nie by die huis nie?', 'Daar was ’n geweldige aardbewing in Japan.', ['Hy is op vakansie.', 'Sy skool is gesluit.', 'Hy is verlore.'], 'Hy bly by sy neef totdat die situasie tuis verbeter.', ev=['geweldige aardbewing in Japan'], src='workbook', page=46, item=2),
    q('literal', 'Op watter datum het Kin die e-pos geskryf?', '13 Augustus 2015', ['15 Augustus 2015', '13 Julie 2015', '3 Augustus 2015'], 'Die datum staan bo-aan die e-pos.', ev=['13 Augustus 2015'], src='workbook', page=46, item=3),
    q('literal', 'Hoe oud is Kin se neef?', '12 jaar', ['10 jaar', '14 jaar', '16 jaar'], 'Die e-pos sê: “Hy is ook 12.”', ev=['Hy is ook 12']),
    q('literal', 'Wat is Kin se gunstelingstokperdjies?', 'Lees en rekenaarspeletjies', ['Sokker en swem', 'Kook en teken', 'Sing en dans'], 'Dit staan in die derde paragraaf.', ev=['gunstelingstokperdjies']),
    q('vocabulary', 'Wat beteken “homofone”?', 'Woorde wat dieselfde klink, maar verskillend gespel word', ['Woorde wat dieselfde lyk en klink', 'Woorde met teenoorgestelde betekenis', 'Woorde met dieselfde betekenis'], 'Dit is die werkboek se verduideliking.', status='official', src='workbook', page=47),
    q('grammar', 'Watter paar is homofone?', 'reis en rys', ['berg en berg', 'bly en bly', 'brak en brak'], 'Reis en rys klink dieselfde maar word verskillend gespel.', status='derived_from_rule', src='workbook', page=47, item='homonieme'),
    q('spelling', 'Wat is die verkleiningsvorm van “boek”?', 'boekie', ['boekje', 'boektjie', 'boekpie'], 'Boek eindig op -k: ons voeg -ie by.', status='derived_from_rule', src='workbook', page=47, item='verkleinwoorde'),
    q('spelling', 'Wat is die verkleiningsvorm van “aardbewing”?', 'aardbewinkie', ['aardbewingie', 'aardbewingetjie', 'aardbewingjie'], 'Meerlettergrepige woorde op -ng: gooi die g weg en voeg -kie by.', status='derived_from_rule', src='workbook', page=47, item='verkleinwoorde'),
  ])
