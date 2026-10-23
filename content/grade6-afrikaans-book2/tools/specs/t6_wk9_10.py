import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

PLAY93 = [
  'Toneel: In Hennie se sitkamer. Hy lê op die rusbank en kyk na ’n rugbywedstryd op TV. Sy ma en pa kyk besorg na hom omdat hy nie sy huiswerk doen nie.',
  'MOEDER: Hennie, het jy jou huiswerk gedoen?',
  'HENNIE: Hm … aa … wel, min of meer. Hm … ek het nie regtig baie huiswerk nie, Ma. Al wat ek moet doen, is om ’n storie van 300 woorde oor iets te skryf. Ek sal dit doen, maar ek wil net gou eers die res van die wedstryd kyk.',
  'MOEDER: Hennie Havenga, gaan doen nou dadelik jou huiswerk! [Tel boeketas van die vloer af op en sit dit bo-op die tafel neer.]',
  'HENNIE: Ai Ma! Hoe kan ons onderwyser ons vra om ’n storie van 300 woorde te skryf? Ek is nie Shakespeare nie! Driehonderd woorde! Dit sal ’n ewigheid duur! Waaroor sal ek skryf? Kan ek nie net gou eers na hierdie wedstryd tussen die Bulle en die Leeus kyk nie? Ek sal direk ná die wedstryd my huiswerk begin doen, ek belowe!',
  'VADER: [Haal ’n boek uit die skoolsak en maak dit oop.] Dalk sal dit jou help. Kyk na hierdie breinkaart in jou werkboek. Dit sê jy moet jou onderwerp in die middel skryf, en dan jou vier hoofgedagtes in elk van hierdie vier raampies. Dis baie maklik! Komaan, seun.',
  'HENNIE: Maar Pa, waaroor kan ek skryf? Ek sal begin met my naam en van. Dan het ek reeds twee woorde. Nog het 298 woorde! Ek wens ek kan net die wedstryd klaar kyk. Okei, okei, ek sal begin dink. Waaroor sal ek skryf? [Hennie raak aan die slaap met sy kop op sy boeketas.]',
  'VERTELLER: Hoe meer Hennie aan ’n onderwerp probeer dink, hoe vaker word hy. Hy gaap luidrugtig en sit sy kop op sy boeketas neer. Gou is hy vas aan die slaap. Hy droom van die wedstryd waarna hy besig was om te kyk. Hy sit by Loftus in die voorste ry, net agter die doelpale. Hy hou die bal senuweeagtig dop. Sy span verloor en daar bly nog net vyf minute oor. Die flank loop mank, en die beseerde losskakel is pas van die veld af gedra. Uit desperaatheid spring Hennie self op die veld en onderskep die bal by die opponente. Hy is vinniger en ratser as enige van die ander span se spelers. Dan span Hennie elke spier in sy liggaam in, en konsentreer hy soos nog nooit tevore nie. Drie sekondes voordat die eindfluitjie blaas, mik hy ’n skepskop pale toe. Die bal trek soos ’n pyl uit ’n boog en seil perfek tussen die pale deur! Hennie se glimlaggende gesig verskyn op miljoene TV’s oor die hele land. Die kommentator skree opgewonde: Hennie Havenga het pas die wenpunte aangeteken! Ons het ’n nuwe rugbyster, Hennie Havenga! Suid-Afrika, hier is julle nuwe ster!',
  'MOEDER: [Maak vir Hennie wakker.] Hennie, word wakker! Jy het huiswerk om te doen!',
  'HENNIE: Wat? Wat is aan die gang?',
  'VADER: Hennie! Wat dink jy doen jy? Jy moet jou huiswerk klaarmaak!',
  'MOEDER: Dalk het die slapie jou die energie gegee wat jy nodig het om jou storie te skryf. Wil jy hê ek moet jou help dink aan ’n onderwerp vir jou storie?',
  'HENNIE: [Met ’n breë glimlag.] Nee dankie, Ma. Ek weet presies waaroor ek gaan skryf!']
GL93 = [('besorg', 'Bekommerd en omgee.'), ('boeketas', '’n Skooltas vir boeke.'), ('losskakel', '’n Posisie in rugby (’n speler).'), ('flank', '’n Posisie in rugby (’n speler aan die kant).'), ('opponente', 'Teenstanders.'), ('skepskop', '’n Hoë skop in rugby wat oor die kruisbalk mik.'), ('desperaatheid', 'Wanhoop; ’n gevoel dat jy nie kan wag nie.'), ('Shakespeare', '’n Beroemde Engelse skrywer.')]

# ============================================================== 93 Hennie is ’n rugbyster!
L93 = lesson(93,
  skills=[LISTEN, READ, WRITE],
  intro='Hennie wil liewer rugby kyk as huiswerk doen – tot hy droom dat hy ’n rugbyster is! Voer die toneelstuk op en ontdek waaroor Hennie skryf.',
  objectives=['’n Toneelstuk lees en opvoer (moeder, vader, seun en verteller).', 'Vrae oor ’n toneelstuk beantwoord.', 'Die agtergrond van ’n toneelstuk beskryf.', 'Die toneelstuk in drie gebeure opsom.'],
  pass_=passage('Hennie is ’n rugbyster!', PLAY93, glossary=GL93),
  learn=[
    text('Hoe lees ons ’n toneelstuk?', bullets=['Die karakters se woorde (die **dialoog**) kom ná hulle name.', 'Die **verteller** lees die dele tussen die dialoog (wat nie deur die karakters voorgestel word nie).', 'Die **toneel- en verhoogaanwysings** verskyn tussen vierkantige hakies [ ].',
         'Ons skryf die name van die karakters in **hoofletters**, gevolg deur ’n **dubbelpunt** (:). Ons gebruik **geen aanhalingstekens** nie.'], page=60),
  ],
  acts=[
    discuss('Voer die toneelstuk op', 'Voer hierdie toneelstuk op. Julle sal ’n moeder, ’n vader, ’n seun en ’n verteller nodig hê. Die verteller moet die dele tussen die dialoog lees.', speak='passage', page=60, item='Ons lees'),
    sa('Waaroor gaan Hennie skryf?', 'Waaroor dink jy gaan Hennie skryf?', 'Hy gaan skryf oor sy droom: hoe hy ’n rugbyster geword het deur die wenpunte aan te teken.', lines=2, page=61, item=1, status='needs_review'),
    sa('Shakespeare', 'Wat bedoel Hennie wanneer hy sê: “Ek is nie Shakespeare nie”?', 'Hy bedoel hy is nie ’n groot, beroemde skrywer nie en kan nie sommer ’n storie van 300 woorde skryf nie.', lines=2, page=61, item=2, status='derived_from_text'),
    sa('Die agtergrond', 'Beskryf die agtergrond waarteen die toneelstuk hom afspeel. (Waar vind die gebeure plaas?)', 'In Hennie se sitkamer, waar hy op die rusbank na ’n rugbywedstryd op TV kyk; sy droom speel by Loftus af.', lines=2, page=61, item=3, status='derived_from_text'),
    sa('Drie gebeure', 'Som die toneelstuk in drie gebeure op.', '1. Hennie wil TV kyk en nie sy huiswerk doen nie.\n2. Hy raak aan die slaap en droom hy is ’n rugbyster wat die wenpunte aanteken.\n3. Hy word wakker en weet presies waaroor hy gaan skryf.', lines=4, page=61, item=4, status='derived_from_text'),
    order('Die gebeure in volgorde', 'Sit die gebeure in die volgorde waarin hulle in die toneelstuk gebeur.', ['Hennie kyk rugby op TV.', 'Sy ma en pa sê hy moet sy huiswerk doen.', 'Hennie raak aan die slaap.', 'Hy droom hy skop die wenpunte.', 'Sy ma maak hom wakker.', 'Hy weet waaroor hy gaan skryf.'],
          'Die toneelstuk begin by die TV en eindig by Hennie se glimlag.', perm=[3, 0, 5, 1, 4, 2], src='supplementary'),
    match('Pas die woord by sy betekenis', 'Verbind elke woord met sy betekenis.', [('opponente', 'teenstanders'), ('boeketas', 'skooltas vir boeke'), ('besorg', 'bekommerd en omgee'), ('desperaatheid', 'wanhoop')], 'Tik op ’n woord in die toneelstuk om sy betekenis te sien.', status='derived_from_rule'),
    tf('Waar of onwaar?', 'In ’n toneelstuk word die karakters se woorde tussen aanhalingstekens geskryf.', False, 'Die werkboek sê: ons gebruik geen aanhalingstekens nie; die naam kom in hoofletters met ’n dubbelpunt.', src='supplementary', status='official'),
  ],
  quiz=[
    q('literal', 'Waarom kyk Hennie se ouers besorg na hom?', 'Hy doen nie sy huiswerk nie.', ['Hy is siek.', 'Hy het die TV stukkend gemaak.', 'Hy is laat.'], 'Die toneelaanwysing sê dit.', ev=['omdat hy nie sy huiswerk doen nie']),
    q('literal', 'Hoeveel woorde moet Hennie se storie hê?', '300', ['30', '100', '3000'], 'Hy sê: “’n storie van 300 woorde”.', ev=['storie van 300 woorde']),
    q('vocabulary', 'Wat bedoel Hennie met “Ek is nie Shakespeare nie”?', 'Hy is nie ’n groot skrywer nie', ['Hy is nie ’n akteur nie', 'Hy hou nie van Engels nie', 'Hy is moeg'], 'Shakespeare was ’n beroemde skrywer.', ev=['Ek is nie Shakespeare nie'], status='derived_from_text'),
    q('literal', 'Waar sit Hennie in sy droom?', 'By Loftus, in die voorste ry', ['By die skool', 'In die sitkamer', 'Op die veld'], 'Die verteller vertel van sy droom by Loftus.', ev=['Hy sit by Loftus']),
    q('literal', 'Wat doen Hennie in sy droom om die wedstryd te wen?', 'Hy skop ’n skepskop tussen die pale deur', ['Hy dra die bal oor die lyn', 'Hy gee die bal vir die losskakel', 'Hy blaas die fluitjie'], 'Drie sekondes voor die einde mik hy ’n skepskop.', ev=['mik hy ’n skepskop pale toe']),
    q('inference', 'Hoe weet ons dat Hennie nie meer bekommerd is aan die einde nie?', 'Hy glimlag en weet waaroor hy gaan skryf', ['Hy gaan weer slaap', 'Hy kyk weer TV', 'Hy gaan huis toe'], 'Hy sê: “Ek weet presies waaroor ek gaan skryf!”', ev=['Ek weet presies waaroor ek gaan skryf'], status='derived_from_text'),
    q('grammar', 'Hoe word ’n karakter se naam in ’n toneelstuk geskryf?', 'In hoofletters, gevolg deur ’n dubbelpunt', ['In kleinletters met aanhalingstekens', 'In hakies', 'Onderstreep'], 'Die werkboek sê dit in die nota.', status='official', src='workbook', page=60),
    q('grammar', 'Waar verskyn die toneel- en verhoogaanwysings?', 'Tussen vierkantige hakies', ['Tussen aanhalingstekens', 'Aan die einde van die toneelstuk', 'In hoofletters'], 'Die werkboek sê: tussen vierkantige hakies.', status='official', src='workbook', page=60),
  ])

# ============================================================== 94 Sleutelkenmerke van 'n dramateks
L94 = lesson(94,
  skills=[READ, LANG],
  intro='Wat maak ’n toneelstuk ’n toneelstuk? Vandag leer jy die sleutelkenmerke van ’n dramateks en soek jy die tegnieke wat die gehoor se aandag hou.',
  objectives=['Die kenmerke van ’n dramateks bestudeer (doel, uitleg, toneelaanwysings).', 'Toneeltegnieke identifiseer: tydsprong, konflik, onverwagse gebeure, beeldspraak en klankeffekte.', 'Stereotipes uitken.'],
  pass_=passage('Hennie is ’n rugbyster! (werkkaart 93)', PLAY93, glossary=GL93),
  learn=[
    table('Sleutelkenmerke van ’n dramateks', ['Kenmerk', 'Wat dit beteken'], [['**Drama/toneelstuk**', 'teks wat geskryf word met die doel om opgevoer te word'], ['**Uitleg**', 'karakters se woorde in dialoogformaat: die naam in hoofletters, ’n dubbelpunt, dan die woorde'],
          ['**Toneelaanwysings**', 'tussen hakies; dit beskryf waar die toneel hom afspeel, hoe karakters moet aantrek of optree, en klankeffekte']], page=62),
    text('Tegnieke om die gehoor se aandag gevange te hou', bullets=['tydspronge', 'konflik tussen mense', 'onverwagte gebeure', 'beeldspraak en klankeffekte', 'Ons maak ook seker dat die teikengroep hulle met die gebeure in die drama kan vereenselwig.'], page=62),
    note('Stereotiepe stellings is veralgemenings, bv. “Alle seuns moet rugby speel.”', title='Stereotipes', page=62),
  ],
  acts=[
    discuss('Lees die toneelstuk weer', 'Lees die toneelstuk op bladsy 60 en 61 weer. Dui aan watter tegnieke in die toneelstuk gebruik is en hoe hulle toegepas is.', speak='passage', page=62, item='Ons skryf'),
    choices('Watter tegniek is dit?', 'Watter tegniek word in die toneelstuk gebruik?',
            [('Hennie raak aan die slaap en droom van ’n rugbywedstryd (die toneel spring van die sitkamer na Loftus).', ['tydsprong', 'konflik', 'klankeffek'], 0), ('Hennie en sy ouers stry oor sy huiswerk.', ['tydsprong', 'konflik', 'klankeffek'], 1),
             ('Hennie word skielik ’n rugbyster in sy droom.', ['onverwagse gebeure', 'konflik', 'beeldspraak'], 0), ('“Die bal trek soos ’n pyl uit ’n boog.”', ['beeldspraak', 'konflik', 'tydsprong'], 0)],
            'Tydsprong = tyd of plek spring; konflik = stry; onverwags = verbasend; beeldspraak = vergelyking of prentjie met woorde.', src='workbook', page=62, item='tegnieke', status='needs_review'),
    sa('Tegnieke en hoe hulle toegepas is', 'Skryf neer hoe die tegnieke in die toneelstuk gebruik is.', 'Tydsprong: Hennie droom van die wedstryd. Konflik: tussen Hennie en sy ouers oor sy huiswerk. Onverwagse gebeure: hy word skielik ’n rugbyster in sy droom. Beeldspraak: “soos ’n pyl uit ’n boog”. Klankeffekte: die eindfluitjie en die kommentator se geskree.', lines=6, page=62, item='tabel', status='needs_review'),
    match('Pas die kenmerk by sy betekenis', 'Verbind die kenmerk met sy betekenis.', [('dramateks', 'teks wat geskryf word om opgevoer te word'), ('dialoog', 'die woorde wat karakters vir mekaar sê'), ('toneelaanwysing', 'tussen hakies: waar en hoe die toneel speel'), ('stereotipe stelling', '’n veralgemening, bv. Alle seuns moet rugby speel')],
          'Dit is die werkboek se verduideliking.', src='supplementary', status='official'),
    tf('Waar of onwaar?', '“Alle seuns moet rugby speel” is ’n stereotipe stelling.', True, 'Die werkboek gee dit as voorbeeld van ’n veralgemening.', src='supplementary', status='official'),
    tf('Waar of onwaar?', 'Toneelaanwysings word in aanhalingstekens geskryf.', False, 'Hulle word tussen hakies geskryf.', src='supplementary', status='official'),
  ],
  quiz=[
    q('vocabulary', 'Wat is ’n dramateks?', 'Teks wat geskryf word met die doel om opgevoer te word', ['Teks wat in ’n koerant staan', 'Teks wat net vir lees is', '’n Brief'], 'Die werkboek sê dit in die blou nota.', status='official', src='workbook', page=62),
    q('grammar', 'Hoe word karakters se woorde in ’n dramateks uiteengesit?', 'In dialoogformaat: naam in hoofletters, dubbelpunt, dan die woorde', ['In paragrawe sonder name', 'In kolomme', 'In ’n tabel'], 'Dit is die uitleg van ’n dramateks.', status='official', src='workbook', page=62),
    q('grammar', 'Wat beskryf toneelaanwysings?', 'Waar die toneel hom afspeel, hoe karakters aantrek of optree en klankeffekte', ['Wat die karakters sê', 'Wie die skrywer is', 'Hoeveel woorde in die teks is'], 'Toneelaanwysings word tussen hakies aangedui.', status='official', src='workbook', page=62),
    q('vocabulary', 'Wat is ’n stereotiepe stelling?', '’n Veralgemening, bv. “Alle seuns moet rugby speel”', ['’n Feit wat altyd waar is', '’n Vraag', '’n Beskrywing van ’n plek'], 'Die werkboek gee hierdie voorbeeld.', status='official', src='workbook', page=62),
    q('inference', 'Watter tegniek is die droom in die toneelstuk?', 'Tydsprong', ['Klankeffek', 'Beeldspraak', 'Stereotipe'], 'Die toneel spring van die sitkamer na Hennie se droom by Loftus.', status='needs_review', src='workbook', page=62, item='tegnieke'),
    q('inference', 'Waar is daar konflik in die toneelstuk?', 'Tussen Hennie en sy ouers oor sy huiswerk', ['Tussen Hennie en die TV', 'Tussen die ouers en die dokter', 'Tussen die verteller en die gehoor'], 'Hulle stry oor die huiswerk.', status='needs_review', src='workbook', page=62, item='tegnieke'),
    q('vocabulary', 'Watter van die volgende is beeldspraak?', '“Die bal trek soos ’n pyl uit ’n boog.”', ['“Hennie, het jy jou huiswerk gedoen?”', '[Tel boeketas van die vloer af op.]', '“Ek is nie Shakespeare nie.”'], 'Dit is ’n vergelyking: die bal is soos ’n pyl.', ev=None, status='derived_from_rule', src='workbook', page=62, item='tegnieke'),
    q('main_idea', 'Hoekom gebruik skrywers tegnieke soos tydspronge en konflik?', 'Om die gehoor se aandag gevange te hou', ['Om die toneelstuk langer te maak', 'Om die karakters te verwar', 'Om die teks mooi te maak sonder rede'], 'Die werkboek lys dit as tegnieke om die gehoor se aandag te hou.', status='official', src='workbook', page=62),
  ])

# ============================================================== 95 Skryf jul eie drama
L95 = lesson(95,
  skills=[LISTEN, WRITE],
  intro='Nou skryf julle self ’n toneelstuk! Werk in ’n groep: beplan die karakters, die agtergrond en die storielyn, en skryf dan die drama.',
  objectives=['In ’n groep ’n toneelstuk beplan (karakters, agtergrond, intrige).', 'Die eerste weergawe skryf, hersien en korrigeer.', '’n Plakkaat ontwerp om die toneelstuk te adverteer.'],
  learn=[
    text('Planning in ’n groep', bullets=['Hou saam met jou groep ’n dinkskrum om idees vir die teks te kry.', 'Gebruik die geheuekaart om jou idees te organiseer.', 'Besluit wie die karakters is, wat die agtergrond is en wat die storielyn (intrige) is.', 'Vul die name in van die maats wat die verskillende rolle sal speel.'], page=63),
    text('Onthou die dramaformaat', bullets=['Die naam van die karakter in **hoofletters**, gevolg deur ’n **dubbelpunt** (:).', '**Geen aanhalingstekens** nie.', 'Toneelaanwysings tussen **vierkantige hakies** [ ].', 'Gebruik ’n **verteller** vir die dele tussen die dialoog.'], page=60),
  ],
  acts=[
    discuss('Dinkskrum', 'Hou saam met jou groep ’n dinkskrum om idees vir die teks te kry, en gebruik die geheuekaart om jou idees te organiseer.', page=63, item='Ons skryf'),
    writing('Beplan: Karakters en agtergrond', 'Vul die tabel in: wie die karakters is (wie dit sal speel, ’n beskrywing van elkeen, wat hy of sy moet aantrek en wat hy of sy sal sê). Beskryf ook die agtergrond (die toneel) en gee jou toneelstuk ’n titel.',
            checklist=['Ons het die karakters gekies en wie hulle gaan speel.', 'Ons het elke karakter beskryf.', 'Ons het gesê wat hulle moet aantrek.', 'Ons het die agtergrond beskryf.', 'Ons het ’n titel gekies.'], lines=8, page=63, item='beplanning'),
    writing('Beplan: die storielyn', 'Beskryf die storielyn (intrige) deur te sê wat gebeur Eers, Toe, Later en Uiteindelik.', checklist=['Eers: ons het die begin beskryf.', 'Toe: ons het die volgende gebeure beskryf.', 'Later: ons het die hoogtepunt beskryf.', 'Uiteindelik: ons het die einde beskryf.'], lines=6, page=63, item='storielyn'),
    order('Die storielyn in volgorde', 'Sit die woorde wat jy gebruik om die storielyn te beplan, in die regte volgorde.', ['Eers', 'Toe', 'Later', 'Uiteindelik'], 'Hierdie woorde help jou om die gebeure in volgorde te beplan.', perm=[2, 0, 3, 1], src='workbook', page=63, item='storielyn', status='official'),
    writing('Skryf jul drama', 'Skryf die eerste weergawe van julle toneelstuk in jou klaswerkboek. Hersien en korrigeer waar nodig en skryf dan die finale weergawe. Voltooi julle drama.',
            checklist=['Ons toneelstuk het ’n titel, ’n agtergrond en karakters.', 'Die karakters se name is in hoofletters met ’n dubbelpunt.', 'Daar is geen aanhalingstekens nie.', 'Die toneelaanwysings is tussen vierkantige hakies.', 'Ons het minstens een tegniek gebruik (tydsprong, konflik, onverwagse gebeure, beeldspraak of klankeffekte).', 'Ons het ons werk hersien en gekorrigeer.'],
            tips=['Beplan jul toneelstuk.', 'Skryf die eerste weergawe in jou klaswerkboek.', 'Hersien en korrigeer.', 'Skryf die finale weergawe netjies neer.'], lines=16, page=64, item='finale weergawe'),
    writing('Plakkaat vir die toneelstuk', 'Ontwerp ’n plakkaat om julle toneelstuk te adverteer. Skryf wat op die plakkaat sal staan (titel, plek, tyd, karakters en ’n pakkende sin).', lines=5, page=65, item='plakkaat'),
    tf('Waar of onwaar?', 'In ’n dramateks gebruik ons aanhalingstekens vir die karakters se woorde.', False, 'Die werkboek sê: geen aanhalingstekens nie.', src='supplementary', status='official'),
  ],
  quiz=[
    q('grammar', 'Hoe skryf ons die name van karakters in ’n dramateks?', 'In hoofletters met ’n dubbelpunt', ['In kleinletters met ’n koppelteken', 'Tussen aanhalingstekens', 'In hakies'], 'Die werkboek sê dit by die toneelstuk.', status='official', src='supplementary', page=60),
    q('grammar', 'Wat gebruik ons NIE in ’n dramateks nie?', 'Aanhalingstekens', ['Dubbelpunte', 'Hoofletters', 'Hakies'], 'Ons gebruik geen aanhalingstekens nie.', status='official', src='supplementary', page=60),
    q('main_idea', 'Wat is die doel van ’n geheuekaart?', 'Om idees te organiseer', ['Om te teken', 'Om te spel', 'Om te lees'], 'Die werkboek sê: gebruik die geheuekaart om jou idees te organiseer.', status='official', src='supplementary', page=63),
    q('sequencing', 'Watter woorde help om die storielyn te beplan?', 'Eers, toe, later, uiteindelik', ['Mooi, groot, klein', 'Hy, sy, ons', 'En, maar, of'], 'Die tabel het hierdie vier woorde.', status='official', src='supplementary', page=63),
    q('main_idea', 'Hoe adverteer jy jou toneelstuk?', 'Met ’n plakkaat', ['Met ’n brief', 'Met ’n gedig', 'Met ’n toets'], 'Die werkboek vra: ontwerp ’n plakkaat om julle toneelstuk te adverteer.', status='official', src='supplementary', page=63),
    q('vocabulary', 'Wat is ’n intrige?', 'Wat in die storie gebeur', ['Die naam van die skrywer', 'Die plek alleen', 'Die titel'], 'Die intrige is die storielyn.', status='derived_from_rule', src='supplementary'),
    q('grammar', 'Waar skryf jy toneelaanwysings?', 'Tussen vierkantige hakies', ['In hoofletters', 'Tussen aanhalingstekens', 'Nêrens nie'], 'Die toneelstuk op bladsy 60 gebruik vierkantige hakies.', status='official', src='supplementary', page=60),
    q('main_idea', 'Wie vertel die dele wat nie deur die karakters voorgestel word nie?', 'Die verteller', ['Die gehoor', 'Die skeidsregter', 'Die onderwyser'], 'Die verteller vertel daardie dele.', status='official', src='supplementary', page=60),
  ])

# ============================================================== 96 Taalstrukture en -konvensies
L96 = lesson(96,
  skills=[LANG],
  intro='Sinonieme, antonieme, klank- en lettergrepe, spelling, idiome en direkte en indirekte rede – ’n groot hersiening van die tema se taalreëls!',
  objectives=['Sinonieme en antonieme in die toneelstuk vind.', 'Woorde in klank- en lettergrepe verdeel.', '-t of -d en v- of f- korrek invul.', 'Idiome met hulle betekenisse verbind.', 'Tussen direkte en indirekte rede verander.'],
  pass_=passage('Hennie is ’n rugbyster! (werkkaart 93)', PLAY93, glossary=GL93),
  learn=[
    text('Indirekte rede: die vereistes', bullets=['Aanhalingstekens val weg.', 'Hooflettergebruik verander.', 'Voornaamwoorde verander.', '’n Vraagsin in die direkte rede vra nie meer ’n vraag in die indirekte rede nie; die vraag word nou ’n stelsin. Die vraagteken val ook weg.'], page=67),
  ],
  acts=[
    match('Sinonieme in die toneelstuk', 'Soek in die toneelstuk sinonieme: verbind elke betekenis met die woord.', [('’n vertrek in ’n huis waar daar gekuier word', 'sitkamer'), ('’n kind se vroulike ouer', 'moeder'), ('die werk wat jy na skool doen', 'huiswerk'), ('’n baie lang tydperk', 'ewigheid'), ('teenstanders', 'opponente')],
          'Al hierdie woorde kom in die toneelstuk voor.', src='workbook', page=66, item='sinonieme', status='derived_from_text'),
    match('Antonieme', 'Verbind elke woord met sy antoniem (teenoorgestelde).', [('dogter', 'seun'), ('wen', 'verloor'), ('ontspanne', 'gespanne'), ('saggies', 'luidrugtig')], 'Antonieme het die teenoorgestelde betekenis.', src='workbook', page=66, item='antonieme', status='needs_review'),
    fill('Klankgrepe en lettergrepe', 'opponente – klankgrepe: {{1}}  lettergrepe: {{2}}\nhulle – klankgrepe: {{3}}  lettergrepe: {{4}}\nplekke – klankgrepe: {{5}}  lettergrepe: {{6}}\nkommunikeer – klankgrepe: {{7}}  lettergrepe: {{8}}\nboeksakke – klankgrepe: {{9}}  lettergrepe: {{10}}',
         {1: 'o-ppo-nen-te', 2: 'op-po-nen-te', 3: 'hu-lle', 4: 'hul-le', 5: 'ple-kke', 6: 'plek-ke', 7: 'ko-mmu-ni-keer', 8: 'kom-mu-ni-keer', 9: ['boek-sa-kke', 'boe-ksa-kke'], 10: 'boek-sak-ke'},
         'Klankgrepe breek voor die dubbele medeklinker; lettergrepe tussen die twee ewe medeklinkers.', prompt='Verdeel die woorde in klank- en lettergrepe (skei met koppeltekens).', src='workbook', page=66, item='tabel', status='derived_from_rule'),
    fill('-t of -d?', 'Hennie dra ’n groo{{1}}, swar{{2}} hoe{{3}} by die rugbywe{{4}}stry{{5}} wan{{6}} hy is bang die son bran{{7}} hom.', {1: 't', 2: 't', 3: 'd', 4: 'd', 5: 'd', 6: 't', 7: 'd'}, 'Sê die meervoud: groot – groot (groter), swart – swart, hoede, wedstryde, brand – brande.', prompt='Vul -t of -d in.', src='workbook', page=67, item='t/d', status='derived_from_rule'),
    fill('v- of f-?', 'Die {{1}}rou ry {{2}}innig met haar {{3}}iets winkel toe om ’n {{4}}is te gaan koop.', {1: 'v', 2: 'v', 3: 'f', 4: 'v'}, 'vrou, vinnig, fiets, vis.', prompt='Vul v- of f- in.', src='workbook', page=67, item='v/f', status='derived_from_rule'),
    match('Uitdrukkings en hul betekenisse', 'Verbind elke uitdrukking met sy betekenis.', [('op die planke bring', '’n nuwe toneelstuk opvoer'), ('onder die dekmantel van', 'onder die masker van'), ('min of meer', 'naastenby'), ('in die kollig wees', 'die middelpunt van die aandag wees')],
          'Idiome het ’n figuurlike betekenis.', src='workbook', page=67, item='uitdrukkings', status='derived_from_rule'),
    sa('’n Vergelyking uit die toneelstuk', 'Skryf ’n vergelyking uit die toneelstuk op bladsy 60 tot 61 hier neer.', '“Die bal trek soos ’n pyl uit ’n boog.”', lines=1, page=67, item='vergelyking', status='derived_from_text'),
    sa('Indirekte rede', 'Herskryf hierdie sin in die indirekte rede: MOEDER: Hennie Havenga, gaan doen nou dadelik jou huiswerk!', 'Die moeder het vir Hennie Havenga gesê dat hy dadelik sy huiswerk moes gaan doen.', lines=2, page=67, item='indirek', status='derived_from_rule'),
    sa('Direkte rede', 'Herskryf hierdie sin in die direkte rede en vul die nodige hoofletters asook lees- en skryftekens in: hennie maar pa waaroor kan ek skryf', 'Hennie vra: “Maar Pa, waaroor kan ek skryf?”', lines=2, page=67, item='direk', status='derived_from_rule'),
    ek_kan(EK_KAN_T6, 68),
  ],
  quiz=[
    q('vocabulary', 'Watter woord is ’n sinoniem vir “opponente”?', 'teenstanders', ['spelers', 'kykers', 'vriende'], 'Opponente beteken teenstanders.', status='derived_from_text', src='workbook', page=66),
    q('vocabulary', 'Wat is die antoniem van “wen”?', 'verloor', ['speel', 'skop', 'kyk'], 'Wen en verloor is teenoorgesteld.', status='derived_from_rule', src='workbook', page=66, item='antonieme'),
    q('grammar', 'Hoe word “opponente” in lettergrepe verdeel?', 'op-po-nen-te', ['o-ppo-nen-te', 'opp-onen-te', 'oppo-nen-te'], 'Lettergrepe breek tussen die twee ewe medeklinkers.', status='derived_from_rule', src='workbook', page=66, item='tabel'),
    q('spelling', 'Watter spelling is korrek?', 'vinnig', ['finnig', 'vinig', 'fienig'], 'V staan nooit aan die einde van ’n woord of lettergreep nie.', status='derived_from_rule', src='workbook', page=67, item='v/f'),
    q('spelling', 'Watter spelling is korrek?', 'wedstryd', ['wedstryt', 'wetstryd', 'wetstryt'], 'Meervoud: wedstryde.', status='derived_from_rule', src='workbook', page=67, item='t/d'),
    q('vocabulary', 'Wat beteken “in die kollig wees”?', 'Die middelpunt van die aandag wees', ['In die donker wees', 'Naastenby wees', '’n Nuwe toneelstuk opvoer'], 'Dit is die betekenis volgens die werkboek se uitdrukkingslys.', status='derived_from_rule', src='workbook', page=67, item='uitdrukkings'),
    q('grammar', 'Wat verander in die indirekte rede?', 'Aanhalingstekens val weg en voornaamwoorde verander', ['Niks verander nie', 'Die sin kry meer aanhalingstekens', 'Die sin word altyd ’n vraag'], 'Dit is die werkboek se vereistes vir die indirekte rede.', status='official', src='workbook', page=67),
    q('grammar', 'Wat gebeur met ’n vraag in die indirekte rede?', 'Dit word ’n stelsin en die vraagteken val weg', ['Dit bly ’n vraag', 'Dit word ’n uitroep', 'Dit kry twee vraagtekens'], 'Die werkboek sê dit by die vereistes.', status='official', src='workbook', page=67),
    q('vocabulary', 'Wat beteken “min of meer”?', 'naastenby', ['presies', 'nooit', 'altyd'], 'Dit is die betekenis volgens die werkboek.', status='derived_from_rule', src='workbook', page=67, item='uitdrukkings'),
  ])
