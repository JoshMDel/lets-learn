import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

WRITE_PROCESS = ['Beplan jou skryfwerk.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']
FIG = '/workbook/gr6-afr-b2/figures/'

STORY73 = """Jabu was ’n 14-jarige veewagter. Hy was baie trots op hoe hy sy pa se groot veekudde versorg. Een warm herfsdag, terwyl Jabu die diere op die koppie sit en dophou, kom sy maat Sipho daar aangedraf.
“Het jy die nuus gehoor, Jabu?” vra Sipho uitasem. “Bhubesi, die leeu, is verlede nag hier in die omgewing gesien. Hy het ’n koei doodgemaak. Die mans is besig om vir hom valstrikke te stel. Gaan sit jou vee terug in die kraal en dan gaan kyk ons hoe hulle die valstrikke stel.”
Jabu is geskok. “Ek kan die vee nie nou al kraal toe neem nie, Sipho. Dis te vroeg in die dag. Hulle moet eers klaar wei, en dan moet ek hulle rivier toe neem om water te drink voordat ek hulle terugneem huis toe.”
Sipho is teleurgesteld, maar hy weet dit help nie om met Jabu te redeneer nie.
“Oukei,” sê hy. “Ek sien jou later, miskien vanaand by die vuur. Ek gaan kyk wat die mans doen.” Hy vertrek weer op ’n drafstap.
Jabu begin toe die koeie bymekaar jaag en lei hulle na die rivier toe. Terwyl hulle drink, sit hy met sy voete in die water.
Toe hoor Jabu ’n geluid wat hom yskoud laat word van die skrik. Die koeie versteen ook in hulle spore. Dit is Bhubesi, en hy is baie naby! Jabu kyk versigtig rond. Met bewende knieë jaag hy die koeie bymekaar. Maar daardie brul het nie geklink soos ’n leeu wat sê “Ek gaan jou opvreet” nie, dink hy. Bhubesi klink asof hy in die moeilikheid is. Ek dink daardie brul was ’n noodkreet. Jabu stap dapper in die rigting van waar hy die geluid gehoor het.
Hy kry Bhubesi vasgevang in een van die valstrikke wat die mans gestel het. Sy kop sit in die valstrik vas, en hoe meer hy stoei, hoe stywer trek die strik. Jabu staan eers ’n hele rukkie na hom en staar. Nog nooit het hy die koning van die diere van so naby gesien nie.
Hy is waarlik ’n indrukwekkende dier. Terwyl Jabu kyk hoe Bhubesi om sy lewe worstel, begin hy vir hom jammer te voel. Op daardie oomblik sien die leeu die seun, en hy praat direk met hom.
Leeu: Ai! Oemfaan (seun)! Help my asseblief. Ek kan nie loskom nie. Sal jy nie asseblief hierdie balk wat my kop afdruk, kom oplig nie? Asseblief!
Jabu kyk in Bhubesi se oë, en hy kan sien hoe desperaat hy is.
Leeu: Asseblief, oemfaan! Asseblief! Voordat daardie jagters my kom doodmaak. Bevry my asseblief!
Jabu: Ek sou jou graag wil bevry, Bhubesi. Maar ek is bang dat jy my sal opvreet sodra ek dit doen.
Leeu: O, nee, oemfaan, ek sal nooit iemand kan opvreet wat my lewe gered het nie! Ek belowe dat ek nie ’n haar op jou kop sal seermaak nie. Ek belowe!"""
SENT73 = STORY73  # a string of paragraphs, one per line
GLOSS73 = [('veewagter', 'Iemand wat vee (koeie en skape) oppas.'), ('veekudde', '’n Groep diere soos koeie wat saam aangehou word.'), ('kraal', '’n Omheinde plek waar vee snags bly.'),
           ('valstrikke', 'Dinge waarmee jagters diere vang.'), ('noodkreet', '’n Harde roep om hulp.'), ('desperaat', 'Baie wanhopig; iemand wat baie graag hulp wil hê.'),
           ('indrukwekkende', 'Wat jou beïndruk omdat dit groot of pragtig is.'), ('oemfaan', 'Die Zulu-woord vir “seun”.')]

# ============================================================== 73 Jabu en die leeu
L73 = lesson(73,
  intro='Vandag lees ons ’n Zulu-volksverhaal oor Jabu en ’n leeu. Dink eers hoe jy dink dit gaan eindig!',
  objectives=['Voorspel waaroor ’n storie gaan deur na die titel en prente te kyk.', 'Die kenmerke van ’n volksverhaal ken.', 'Vrae oor ’n fiktiewe teks bespreek en jou mening gee.',
              'In ’n groep ’n einde vir die storie beplan en dit as rolspel opvoer.'],
  pass_=passage('Jabu en die leeu', SENT73, glossary=GLOSS73),
  learn=[
    text('Wat is ’n volksverhaal?', 'Volksverhale word mondeling (met die mond) van een geslag na die volgende oorgedra. Mense vertel hierdie verhale vir hulle kinders en kleinkinders – hulle skryf dit nie neer nie.',
         bullets=['Volksverhale bevat gewoonlik ’n **moraal** of **sedeles** en dien as vermaak.', 'Dit verenig ook mense: die kinders van ’n bepaalde kultuurgroep hoor almal dieselfde volksverhale en voel hulle hoort saam.',
                  'In die meeste volksverhale kom ons diere teë wat kan praat. Volksverhale is meestal **fiksie**, aangesien diere nie werklik kan praat nie.'], page=18),
  ],
  acts=[
    discuss('Ons praat: Voorspel', 'Kyk na die titel en illustrasies van die storie, en voorspel waaroor die storie handel. (Die prente is op die oorspronklike werkboekbladsy.)', page=18, item='Ons praat'),
    discuss('Luister na die storie', 'Druk die knoppie en luister terwyl jy saamlees.', src='supplementary', speak='passage'),
    discuss('Hoe sal die storie eindig?', 'Praat daaroor.', points=['Hoe dink jy gaan die storie eindig?', 'Dink jy Jabu gaan die leeu bevry?'], page=19, item='Ons praat'),
    discuss('Rolspel: ’n einde vir die storie', 'Beplan in groepverband ’n einde vir hierdie storie. Stel ’n rolspel saam en bied dit vir die klas aan.',
            points=['Een van julle is Jabu, iemand is Sipho en iemand is Bhubesi, die leeu.', 'Julle sal ook ’n paar koeie nodig hê.', 'Besluit watter groep die beste einde het.'], page=19, item='Ons praat'),
    sa('Vraag 1: Hoofkarakters', 'Wie is die hoofkarakters in hierdie storie?', 'Jabu, Sipho en Bhubesi, die leeu.', lines=1, page=19, item=1),
    sa('Vraag 2: Waarom opgewonde?', 'Waarom was Sipho opgewonde toe hy by Jabu aangehardloop gekom het?', 'Hy wou vir Jabu die nuus vertel dat Bhubesi die leeu gesien is, ’n koei doodgemaak het en dat die mans valstrikke stel.', lines=2, page=19, item=2),
    sa('Vraag 3: Waar was Jabu?', 'Waar was Jabu toe Sipho hom gekry het?', 'Op die koppie, besig om sy pa se vee dop te hou.', lines=1, page=19, item=3),
    discuss('Vraag 4–5: Praat daaroor', 'Bespreek met jou maat.', points=['Kyk na die prentjies en beskryf die plek waar die storie hom afgespeel het. Lyk die plek anders as die plek waar jy woon? Hoe verskil dit?',
            'Dink jy Jabu was ’n verantwoordelike mens? Waarom sê jy so?'], page=19, item='4–5'),
    tf('Waar of onwaar?', 'Volksverhale word gewoonlik eers neergeskryf en dan voorgelees.', False, 'Volksverhale word mondeling van een geslag na die volgende oorgedra – mense vertel dit; hulle skryf dit nie neer nie.', status='official'),
    fill('Voltooi die sin', 'Jabu is ’n {{1}} wat sy pa se {{2}} oppas. Hy kry die leeu in ’n {{3}} vasgevang.', {1: 'veewagter', 2: ['vee', 'veekudde', 'koeie'], 3: ['valstrik', 'strik']},
         'Veewagters pas vee op; die mans het valstrikke gestel om die leeu te vang.', bank=['veewagter', 'vee', 'valstrik', 'kraal']),
    match('Pas die woord by sy betekenis', 'Verbind elke woord met die korrekte betekenis.',
          [('veewagter', 'Iemand wat vee oppas'), ('kraal', '’n Omheinde plek waar vee snags bly'), ('noodkreet', '’n Harde roep om hulp'), ('desperaat', 'Baie wanhopig')],
          'Jy kan ook op ’n woord in die storie tik om te sien wat dit beteken.'),
    order('Wat het eerste gebeur?', 'Sit die gebeure in die volgorde waarin hulle in die storie gebeur het.',
          ['Jabu sit op die koppie en pas die koeie op.', 'Sipho vertel van die leeu en die valstrikke.', 'Jabu neem die koeie rivier toe.', 'Jabu hoor ’n brul en vind die leeu in die valstrik.', 'Die leeu smeek Jabu om hom te bevry.'],
          'Die storie volg die gebeure van die oggend op die koppie tot by die valstrik.', perm=[3, 0, 4, 2, 1]),
  ],
  quiz=[
    q('literal', 'Hoe oud was Jabu?', '14 jaar oud', ['10 jaar oud', '16 jaar oud', '21 jaar oud'], 'Die storie sê Jabu was ’n 14-jarige veewagter.', ev=['14-jarige']),
    q('literal', 'Wat is Jabu se werk in die storie?', 'Hy pas sy pa se vee op.', ['Hy jag leeus.', 'Hy is ’n onderwyser.', 'Hy werk op ’n plaas se kombuis.'], 'Jabu is ’n veewagter wat sy pa se groot veekudde versorg.', ev=['veewagter']),
    q('literal', 'Watter nuus het Sipho vir Jabu gebring?', 'Die leeu is gesien en het ’n koei doodgemaak.', ['Jabu se pa is siek.', 'Die rivier is droog.', 'Daar is ’n nuwe skool.'], 'Sipho het gehoor Bhubesi, die leeu, is gesien en het ’n koei doodgemaak.', ev=['verlede nag hier in die omgewing gesien']),
    q('inference', 'Waarom was Sipho teleurgesteld?', 'Jabu wou nie dadelik saam met hom na die valstrikke gaan kyk nie.', ['Hy het nie ’n koei gehad nie.', 'Die leeu het weggehardloop.', 'Jabu het hom uitgeskel.'], 'Jabu kon nie sy vee nou al kraal toe neem nie.', ev=['Sipho is teleurgesteld']),
    q('literal', 'Wat het Jabu by die rivier gehoor?', '’n Geluid wat hom yskoud laat word het – die leeu se brul', ['Sipho wat roep', 'Die jagters wat sing', 'Sy ma wat hom roep'], 'Jabu hoor ’n geluid wat hom yskoud laat word van die skrik.', ev=['Toe hoor Jabu ’n geluid']),
    q('inference', 'Wat dink Jabu van die leeu se brul?', 'Dit was ’n noodkreet.', ['Dit was ’n dreigement.', 'Dit was ’n liedjie.', 'Dit was die jagters.'], 'Hy dink Bhubesi klink asof hy in die moeilikheid is.', ev=['noodkreet']),
    q('literal', 'Waar het Jabu die leeu gekry?', 'Vasgevang in ’n valstrik', ['By die kraal', 'Op die koppie', 'In die rivier'], 'Bhubesi was vasgevang in een van die valstrikke wat die mans gestel het.', ev=['vasgevang in een van die valstrikke']),
    q('literal', 'Wat het die leeu aan Jabu belowe?', 'Dat hy hom nie sal opvreet nie', ['Dat hy hom ’n koei sal gee', 'Dat hy hom sal wys waar die jagters is', 'Dat hy altyd sy vriend sal wees'], 'Die leeu belowe om nie ’n haar op Jabu se kop seer te maak nie.', ev=['Ek belowe dat ek nie']),
    q('vocabulary', 'Wat is ’n volksverhaal?', '’n storie wat mondeling van een geslag na die volgende oorgedra word', ['’n Koerantberig', '’n Dagboekinskrywing', '’n Brief aan ’n vriend'], 'Die werkboek verduidelik dat volksverhale mondeling oorgedra word.', status='official', page=18),
  ])

# ============================================================== 74 Jabu hoor die leeu se gebrul
L74 = lesson(74,
  skills=[READ, WRITE, LANG],
  intro='Vandag gebruik jy soeklees om vrae oor die storie te beantwoord, sit prente in volgorde en werk met sinonieme en homofone.',
  objectives=['Soeklees om meerkeusevrae oor die teks te beantwoord.', 'Prente in die korrekte volgorde nommer.', 'Beskrywende sinne by prente skryf.', 'Sinonieme en antonieme vind.', 'Die regte homofoon kies.'],
  pass_=passage('Jabu en die leeu (werkkaart 73)', SENT73, glossary=GLOSS73),
  learn=[
    note('Onthou jy nog dat ’n mens ’n teks **vluglees** om ’n algemene indruk te kry van waaroor die teks handel, en **soeklees** om spesifieke inligting te verkry?', title='Vluglees en soeklees', page=20),
    note('Homofone klink dieselfde, maar word verskillend gespel en het verskillende betekenisse. Homonieme is woorde wat dieselfde lyk en klink, maar wat verskillende betekenisse het.', title='Homofone en homonieme', page=21),
  ],
  acts=[
    mcq('Soeklees 1', 'Jabu wou nie na die valstrikke gaan kyk nie want:', ['Dit was te ver om te loop.', 'Hy was te moeg.', 'Hy moes die vee rivier toe neem.', 'Hy het geweet hoe die valstrikke lyk.'], 2,
        'Jabu sê die vee moet eers klaar wei en dan rivier toe gaan om water te drink.', per_option={0: 'Die storie sê niks van die afstand nie.', 1: 'Jabu was nie moeg nie – hy het sy werk gedoen.', 3: 'Dit is nie die rede wat Jabu noem nie.'}, page=20, item=1),
    mcq('Soeklees 2', 'Wat bedoel die storieverteller met “die koeie versteen in hulle spore”?', ['Hulle het koud gekry.', 'Hulle was te bang om te beweeg.', 'Hulle wou nie na die rivier toe gaan nie.', 'Hulle het in klip verander.'], 1,
        'Versteen beteken hier dat die koeie van skrik doodstil gestaan het.', per_option={0: 'Die woord “versteen” gaan oor skrik, nie koue nie.', 2: 'Hulle was reeds by die rivier.', 3: 'Dis ’n beeldspraak; hulle het nie letterlik in klip verander nie.'}, page=20, item=2),
    mcq('Soeklees 3', 'Waarom het Jabu se knieë gebewe?', ['Hy het koud gekry.', 'Hy was bang vir die leeu.', 'Hy kon nie die vee bymekaar kry nie.', 'Hy het sy knieë seergemaak.'], 1,
        'Hy het ’n geluid gehoor wat hom yskoud van die skrik laat word het – Bhubesi was baie naby.', per_option={0: 'Dit was ’n warm herfsdag.', 2: 'Hy het die koeie bymekaar gejaag – die bewing was van skrik.', 3: 'Die storie sê niks hiervan nie.'}, page=20, item=3),
    mcq('Soeklees 4', 'Hoe weet ons dat Jabu ’n verantwoordelike mens was?', ['Hy het die koeie versorg.', 'Hy het die koeie alleen gelaat.', 'Hy het op die koppie gesit.', 'Hy het met die leeu gepraat.'], 0,
        'Jabu het sy pa se vee versorg en wou nie sy werk verlaat nie.', per_option={1: 'Dit sou onverantwoordelik wees – en Jabu het dit nie gedoen nie.', 2: 'Net sit is nie verantwoordelik nie.', 3: 'Met die leeu praat wys eerder moed.'}, page=20, item=4),
    order('Nommer die prente in die regte volgorde', 'Sit die prente in die volgorde waarin dit in die storie gebeur.',
          ['Jabu sit op die koppie by sy koeie.', 'Jabu sê vir Sipho: “Jammer, Sipho, ek kan nie saam met jou gaan nie.”', 'Jabu is by die rivier en die leeu is naby.', 'Die leeu lê vasgevang en Jabu kyk na hom.'],
          'Die storie begin op die koppie, dan kom Sipho, dan gaan Jabu rivier toe, en uiteindelik vind hy die leeu in die valstrik.', perm=[3, 1, 0, 2],
          images=[FIG + 'wk074-prent-koppie.webp', FIG + 'wk074-prent-sipho.webp', FIG + 'wk074-prent-rivier.webp', FIG + 'wk074-prent-lion.webp'], src='workbook', page=20, item='Ons doen', status='derived_from_text'),
    sa('Skryf ’n beskrywende sin by elke prent', 'Skryf ’n beskrywende sin vir elke prent in die prente-oefening hierbo (1 tot 4).', None, lines=5, page=21, item='prente'),
    sa('Sinonieme en antonieme', 'Soek sinonieme (woorde met dieselfde betekenis) in die storie vir die volgende woorde/frases en gee dan jou eie antonieme (woorde met die teenoorgestelde betekenis): intensiewe vorm vir koud; aand; maklik om by te kom; vader; aan die begin van die dag.',
       None, lines=6, page=21, item='tabel'),
    match('Kies ’n sinoniem vir elke werkwoord', 'Verbind elke werkwoord met ’n sinoniem uit die lys.',
          [('bevry', 'losmaak'), ('smeek', 'pleit'), ('loop', 'wandel'), ('begeer', 'verlang'), ('gesels', 'praat'), ('wegneem', 'verwyder'), ('kry', 'ontdek'), ('volg', 'agternaloop')],
          'Sinonieme het dieselfde betekenis. In die werkboek is “praat” vir “gesels” reeds ingevul.', src='workbook', page=21, item='werkwoorde', status='derived_from_rule'),
    choices('Omkring die regte homofoon', 'Kies die woord wat in die sin pas.',
            [('Jabu ___ na Indië.', ['reis', 'rys'], 0), ('Jabu eet ___ saam met ander groente.', ['reis', 'rys'], 1), ('Hy gaan die beeste by die rivier ___.', ['haal', 'hael'], 0),
             ('Dit het gereën en ge___.', ['gehaal', 'gehael'], 1), ('Alhoewel Sipho baie eet, is hy ___.', ['maar', 'maer'], 1), ('Jabu is bang vir die leeu ___ hy stap dapper nader.', ['maar', 'maer'], 0)],
            'Lees die sin: die woord wat die sin laat sin maak, is die regte homofoon.', src='workbook', page=21, item='homofone', status='derived_from_rule'),
    fill('Homofone of homonieme?', 'Woorde wat dieselfde klink maar verskillend gespel word, noem ons {{1}}. Woorde wat dieselfde lyk en klink maar verskillende betekenisse het, noem ons {{2}}.',
         {1: 'homofone', 2: 'homonieme'}, 'Die werkboek verduidelik die verskil in die geel nota.', bank=['homofone', 'homonieme', 'sinonieme'], status='official'),
  ],
  quiz=[
    q('inference', 'Jabu wou nie na die valstrikke gaan kyk nie want:', 'Hy moes die vee rivier toe neem.', ['Dit was te ver om te loop.', 'Hy was te moeg.', 'Hy het geweet hoe die valstrikke lyk.'], 'Die vee moes eers wei en dan water gaan drink.', ev=['Hulle moet eers klaar wei'], src='workbook', page=20, item=1),
    q('vocabulary', 'Wat bedoel die storieverteller met “die koeie versteen in hulle spore”?', 'Hulle was te bang om te beweeg.', ['Hulle het koud gekry.', 'Hulle wou nie na die rivier toe gaan nie.', 'Hulle het in klip verander.'], 'Versteen beteken hier doodstil van skrik.', ev=['Die koeie versteen'], src='workbook', page=20, item=2),
    q('inference', 'Waarom het Jabu se knieë gebewe?', 'Hy was bang vir die leeu.', ['Hy het koud gekry.', 'Hy kon nie die vee bymekaar kry nie.', 'Hy het sy knieë seergemaak.'], 'Hy het die leeu se brul gehoor en geskrik.', ev=['Met bewende knieë'], src='workbook', page=20, item=3),
    q('inference', 'Hoe weet ons dat Jabu ’n verantwoordelike mens was?', 'Hy het die koeie versorg.', ['Hy het die koeie alleen gelaat.', 'Hy het op die koppie gesit.', 'Hy het met die leeu gepraat.'], 'Hy was trots daarop om sy pa se vee te versorg.', ev=['versorg'], src='workbook', page=20, item=4),
    q('vocabulary', 'Watter woord is ’n sinoniem vir “smeek”?', 'pleit', ['wandel', 'verwyder', 'agternaloop'], 'Smeek en pleit beteken amper dieselfde.', status='derived_from_rule', src='workbook', page=21, item='werkwoorde'),
    q('vocabulary', 'Watter woord is ’n sinoniem vir “bevry”?', 'losmaak', ['verlang', 'ontdek', 'praat'], 'Om iemand te bevry, is om hom los te maak.', status='derived_from_rule', src='workbook', page=21, item='werkwoorde'),
    q('spelling', 'Watter woord pas in die sin: “Jabu ___ na Indië”?', 'reis', ['rys', 'reiz', 'rijs'], 'Reis beteken ’n reis maak; rys is ’n graansoort.', status='derived_from_rule', src='workbook', page=21, item='homofone'),
    q('spelling', 'Watter woord pas: “Alhoewel Sipho baie eet, is hy ___”?', 'maer', ['maar', 'mear', 'maer-'], 'Maer is die teenoorgestelde van vet. Maar is ’n voegwoord.', status='derived_from_rule', src='workbook', page=21, item='homofone'),
    q('vocabulary', 'Wat is homofone?', 'Woorde wat dieselfde klink, maar verskillend gespel word en verskillende betekenisse het', ['Woorde met dieselfde betekenis', 'Woorde met teenoorgestelde betekenis', 'Woorde wat dieselfde lyk en klink'], 'Dit is die werkboek se verduideliking van homofone.', status='official', src='workbook', page=21),
  ])

# ============================================================== 75 Wat het met die leeu gebeur?
STORY75 = """Bhubesi smeek en pleit so jammerlik dat Jabu uiteindelik besluit om hom te vertrou en hom vry te laat. Hy lig die balk wat die leeu se kop vashou. Die leeu spring los en skud sy maanhare.
Leeu: O dankie, oemfaan! Ek skuld jou regtig iets. My nek was besig om so styf te word in daardie valstrik, en ek was bang die jagters sou my doodmaak. Maar nou is ek so dors, asseblief oemfaan – kan jy my wys waar die rivier is?
Jabu: Dis net hier anderkant. Kom saam met my.
Leeu: Ek moet egter sê, dit sal darem baie jammer wees om so ’n sappige maaltyd te vermors!
Jabu: O nee! Ek het jou van die jagters gered, en jy het belowe om my nie op te vreet nie.
Leeu: Ja, jy is reg. Ek het wel belowe. Maar noudat ek vry is, is dit nie meer vir my so belangrik om daardie belofte na te kom nie.
Jabu: Jy maak ’n groot fout. Jy behoort nooit ’n belofte te verbreek nie.
Leeu: Ag, watse onsin! Ek gaan jou nou opvreet, seun. Al hierdie gepraat maak my net hongerder.
Jabu: Maar jy het belowe, en as jy ’n belofte verbreek, sal jy gestraf word.
Op daardie oomblik kom ’n slim ou jakkals wat hulle afgeluister het, nader om meer te wete te kom.
Jakkals: Watter belofte het jy gemaak, Nkosi (groot Kaptein)? En waarom het jy dit gemaak?
Jabu: Ek het die leeu uit die valstrik bevry, en hy het belowe om my nie op te vreet nie, maar nou wil hy sy belofte verbreek.
Jakkals: Ag, wat ’n lawwe storie. Wil jy vir my sê jy, die groot koning van die diere, is gevang in ’n valstrik wat mense gemaak het? Onmoontlik! Ek glo dit nie!
Leeu: Dit is waar! Dit was ’n sterk en verskriklike valstrik!
Jakkals: Ai, ek kan nie glo enigiets is sterker as my koning nie. Ek moet daardie valstrik sien. Voordat jy jou aandete eet, wys my asseblief die strik waarvan jy praat. Dan kan jy jou maaltyd geniet.
Die leeu, die jakkals en Jabu gaan toe terug na die valstrik toe.
Jakkals: Ek laat my nie vertel dat hierdie ou dingetjie regtig jou kop kon vashou nie! Nooit! Ek kan my dit regtig nie voorstel nie. Nkosi, as jy nie omgee nie, steek jou kop hier in sodat ek kan sien hoe jy gelyk het toe die seun op jou afgekom het?
Leeu: Ai tog. Jy maak my moeg met jou vrae. Ek sal hierdie laaste ding vir jou doen, en dan moet jy my met rus laat sodat ek my ete kan geniet.
Toe steek Bhubesi sy kop tussen die klampe in, net soos dit was toe Jabu hom gekry het. Vinniger as ’n weerligstraal klap die jakkals die valstrik toe. Bhubesi sit weer vasgevang!
Jakkals: Nou sien ek hoe jy gevang is. Dis jammer dat jy weer op dieselfde manier verstrik is. Maar die seun is reg, Nkosi. Verbreekte beloftes haal jou altyd in!
Bhubesi brul van woede, maar die sterk valstrik hou hom goed vas. Jabu bedank die jakkals. Hy hardloop terug na sy koeie en jaag hulle aan huis toe en in die kraal in. Wat ’n dag het hy nie beleef nie!
Sipho sien hom en roep uit: “Jabu, Jabu! Die leeu is in ’n valstrik naby die rivier gevang! Jy het die hele avontuur misgeloop!” Jabu glimlag net en sê vir homself: “Ek het genoeg avontuur vir een dag gehad.” Sipho gaan toe weer terug na die jagters toe om die storie te hoor van die magtige leeu wat in die valstrik gevang is, en Jabu gaan huis toe.
Hy groet sy ma, gaan sit en gee ’n groot sug.
Daardie aand luister Jabu by die vuur na die mans terwyl hulle gesels en die storie vertel van die leeu se vangs, van die stryd wat dit gekos het, en van hoe vernuftig hulle was om hom te vang."""
SENT75 = STORY75  # a string of paragraphs, one per line

L75 = lesson(75,
  intro='Wat het met die leeu gebeur? Lees die tweede deel van die volksverhaal en ontdek die sedeles.',
  objectives=['Die tweede deel van ’n volksverhaal lees en vrae daaroor beantwoord.', 'Die sedeles (moraal) van ’n storie uitwys.', 'Jou eie perspektief uitspreek en motiveer.'],
  pass_=passage('Wat het met die leeu gebeur?', SENT75, glossary=[
      ('maanhare', 'Die lang hare om ’n leeu se nek en kop.'), ('belofte', 'Wat jy sê jy sal doen en moet nakom.'), ('verbreek', 'Nie nakom nie; breek (’n belofte).'), ('vernuftig', 'Slim en vindingryk.'),
      ('klampe', 'Die houtstukke van die valstrik wat toeklap.'), ('verstrik', 'Vasgevang soos in ’n strik.'), ('jakkals', '’n Slim, honde-agtige wilde dier.'), ('Nkosi', 'Zulu-woord vir “groot kaptein” of “meneer”.')]),
  learn=[note('Die **moraal** of **sedeles** van ’n storie is die les wat die storie ons leer.', title='Wat is ’n sedeles?', src='supplementary', page=22)],
  acts=[
    discuss('Luister na die storie', 'Druk die knoppie en luister terwyl jy saamlees.', src='supplementary', speak='passage'),
    discuss('Dink na oor die storie', 'Jy weet nou hoe die storie geëindig het. Dink na oor die volgende vrae.', points=['Het die storie geëindig soos jy verwag het?', 'Hoe het jy daaroor gevoel dat die leeu sy belofte verbreek het?',
            'Dink jy die jakkals was slim? Waarom sê jy so?', 'Sipho het vir Jabu gesê hy het die hele avontuur misgeloop. Stem jy saam met Sipho? Motiveer jou antwoord.'], page=23, item='Ons praat'),
    sa('Die sedeles', 'Wat is die moraal of sedeles van die storie?', 'Jy moet ’n belofte nakom – verbreekte beloftes haal jou altyd in.', lines=2, page=23, item='sedeles', status='needs_review'),
    tf('Waar of onwaar?', 'Die leeu het sy belofte gehou en Jabu nie opgevreet nie.', False, 'Die leeu het gesê sy belofte is nie meer belangrik noudat hy vry is nie en wou Jabu opvreet.'),
    mcq('Hoe het die jakkals die leeu gevang?', 'Hoe het die jakkals die leeu weer in die valstrik gekry?', ['Hy het Jabu gevra om dit te doen.', 'Hy het die leeu gevra om sy kop in die valstrik te steek en toe die strik toegeklap.', 'Hy het die jagters gaan roep.', 'Hy het die leeu uitgetart om weg te hardloop.'], 1,
        'Die jakkals het gesê hy kan nie glo die leeu is gevang nie en gevra dat die leeu wys hoe dit gebeur het. Toe die leeu sy kop insteek, het hy die strik toegeklap.', per_option={0: 'Jabu het niks gedoen nie – die jakkals was slim.', 2: 'Die jagters kom nie in hierdie deel voor nie.', 3: 'Die leeu is weer verstrik nadat hy sy kop ingesteek het.'}, src='supplementary', status='derived_from_text'),
    order('Volgorde van die gebeure', 'Sit hierdie gebeure in die regte volgorde.',
          ['Jabu laat die leeu vry.', 'Die leeu sê hy gaan Jabu opvreet.', 'Die jakkals kom luister.', 'Die leeu steek sy kop in die valstrik.', 'Die jakkals klap die valstrik toe.'],
          'Eers bevry Jabu die leeu, dan wil die leeu hom opvreet, dan kom die jakkals en vang hy die leeu weer.', perm=[2, 4, 0, 3, 1]),
    fill('Vul die woord in', 'Die leeu het sy {{1}} verbreek, maar die {{2}} het hom slim weer in die valstrik gekry.', {1: 'belofte', 2: 'jakkals'}, 'Die jakkals is die slim een in die verhaal.', bank=['belofte', 'jakkals', 'seun']),
    match('Wie het dit gesê?', 'Verbind elke sin met die karakter wat dit gesê het.', [('“Ek belowe dat ek nie ’n haar op jou kop sal seermaak nie.”', 'die leeu'), ('“Jy behoort nooit ’n belofte te verbreek nie.”', 'Jabu'), ('“Verbreekte beloftes haal jou altyd in!”', 'die jakkals'), ('“Jy het die hele avontuur misgeloop!”', 'Sipho')], 'Volg die gesprek in die storie.'),
  ],
  quiz=[
    q('inference', 'Waarom het Jabu die leeu uiteindelik vrygelaat?', 'Die leeu het so jammerlik gesmeek en belowe om hom nie seer te maak nie.', ['Die jagters het hom gevra.', 'Hy was bang vir die jakkals.', 'Hy wou die leeu se maanhare sien.'], 'Bhubesi het gesmeek en gepleit en Jabu besluit om hom te vertrou.', ev=['Bhubesi smeek en pleit']),
    q('literal', 'Wat wou die leeu doen sodra hy vry was?', 'Jabu opvreet', ['Rivier toe gaan en slaap', 'Die jagters gaan jag', 'Sipho gaan soek'], 'Hy sê: “Ek gaan jou nou opvreet, seun.”', ev=['Ek gaan jou nou opvreet']),
    q('inference', 'Hoekom het die jakkals gesê hy glo nie die leeu was in ’n valstrik nie?', 'Hy het die leeu uitgetart om te wys hoe dit gebeur het.', ['Hy was bang vir die leeu.', 'Hy het die valstrik self gestel.', 'Hy het Jabu nie vertrou nie.'], 'Die jakkals het dit gesê sodat die leeu sy kop weer sou insteek.', ev=['Ek glo dit nie']),
    q('literal', 'Wie het die valstrik toegeklap?', 'Die jakkals', ['Jabu', 'Sipho', 'Die leeu self'], 'Vinniger as ’n weerligstraal klap die jakkals die valstrik toe.', ev=['klap die jakkals die valstrik toe']),
    q('main_idea', 'Wat is die moraal van die storie?', 'Ons moet beloftes nakom.', ['Leeus is altyd gevaarlik.', 'Slim mense is altyd bang.', 'Jy moet nooit kinders vertrou nie.'], 'Die jakkals sê: “Verbreekte beloftes haal jou altyd in!”', ev=['Verbreekte beloftes haal jou altyd in'], status='needs_review'),
    q('inference', 'Wat sê die storie oor Jabu se karakter?', 'Hy was vriendelik, dapper en het gedink aan reg en verkeerd.', ['Hy was gulsig en slu.', 'Hy was lui en bang.', 'Hy was oneerlik.'], 'Hy het die leeu gehelp en vir regverdigheid gepleit.', ev=['Jy maak ’n groot fout'], status='needs_review'),
    q('literal', 'Wat het Sipho gesê toe Jabu terug by die kraal was?', 'Dat Jabu die hele avontuur misgeloop het', ['Dat die leeu weg is', 'Dat hy die leeu gevang het', 'Dat die jagters huis toe is'], 'Sipho roep uit dat die leeu gevang is en Jabu die avontuur misgeloop het.', ev=['Jy het die hele avontuur misgeloop']),
    q('vocabulary', 'Wat beteken “vernuftig”?', 'Slim en vindingryk', ['Baie moeg', 'Baie bang', 'Baie sterk'], 'Die mans was vernuftig om die leeu te vang.', ev=['vernuftig'], status='derived_from_rule'),
    q('sequencing', 'Wat gebeur LAASTE in die storie?', 'Jabu luister by die vuur na die mans se storie van die leeu se vangs.', ['Die leeu belowe om Jabu nie op te vreet nie.', 'Die jakkals kom nader.', 'Jabu maak die leeu los.'], 'Die storie eindig daardie aand by die vuur.', ev=['Daardie aand luister Jabu']),
  ])

# ============================================================== 76 Kom ons dink na oor die storie
L76 = lesson(76,
  skills=[LISTEN, WRITE, LANG],
  intro='Kom ons dink na oor die storie van Jabu en die leeu: hoe het dit begin, wat het in die middel gebeur en hoe het dit geëindig?',
  objectives=['Die agtergrond, karakters, intrige en tema van ’n storie uitwys.', 'Die karakters met byvoeglike naamwoorde beskryf.', 'Sinne wat nie by die onderwerp pas nie, uitken en die res in volgorde sit.', '’n Opsomming van die storie skryf.'],
  learn=[
    table('Dele van ’n storie', ['Deel', 'Wat dit beteken'], [['**Agtergrond**', 'wanneer en waar die gebeure plaasvind'], ['**Karakters**', 'mense of diere in die storie'], ['**Intrige**', 'wat in die storie gebeur'], ['**Tema**', 'die boodskap wat oorgedra word']], page=24),
    text('Die skryfproses', bullets=['Beplan jou opsomming deur dit met jou maat te bespreek.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe neer.'], page=24),
  ],
  acts=[
    discuss('Ons praat: Die karakters', 'Praat oor elkeen van die karakters (Jabu, die leeu en die jakkals).', page=24, item='Ons praat'),
    choices('Watter byvoeglike naamwoord pas by watter karakter?', 'Besluit watter karakter elke woord die beste beskryf: Jabu, die leeu of die jakkals.',
            [('verantwoordelik', ['Jabu', 'die leeu', 'die jakkals'], 0), ('jonk', ['Jabu', 'die leeu', 'die jakkals'], 0), ('betroubaar', ['Jabu', 'die leeu', 'die jakkals'], 0), ('goed', ['Jabu', 'die leeu', 'die jakkals'], 0),
             ('oneerlik', ['Jabu', 'die leeu', 'die jakkals'], 1), ('sterk', ['Jabu', 'die leeu', 'die jakkals'], 1), ('gulsig', ['Jabu', 'die leeu', 'die jakkals'], 1), ('naar', ['Jabu', 'die leeu', 'die jakkals'], 1),
             ('slu', ['Jabu', 'die leeu', 'die jakkals'], 2), ('slim', ['Jabu', 'die leeu', 'die jakkals'], 2), ('wys', ['Jabu', 'die leeu', 'die jakkals'], 2), ('vreesloos', ['Jabu', 'die leeu', 'die jakkals'], 2)],
            'Dink aan wat elke karakter in die storie gedoen het. (Daar kan meer as een goeie antwoord wees – bespreek dit met jou maat.)', src='workbook', page=24, item='karakters', status='needs_review'),
    sa('Die opsomming: begin, middel en einde', 'Skryf ’n opsomming van die storie. Skryf hoe die storie begin het, wat in die middel gebeur het en hoe dit geëindig het. Noem die agtergrond, karakters, intrige en tema.',
       'Begin: Jabu, ’n veewagter, pas sy pa se vee op toe Sipho hom vertel dat die leeu gesien is. Middel: Jabu hoor die leeu by die rivier brul, vind hom in ’n valstrik en laat hom vry nadat die leeu belowe om hom nie op te vreet nie. Einde: Die leeu wil sy belofte verbreek, maar die jakkals vang hom weer in die valstrik. Tema: Jy moet beloftes nakom.',
       lines=10, page=24, item='opsomming', status='needs_review'),
    choices('Watter sinne handel NIE oor die onderwerp nie?', 'Die onderwerp is: Jabu is verantwoordelik. Kies by elke sin of dit hoort of nie hoort nie.',
            [('Jabu was ’n baie verantwoordelike mens.', ['hoort', 'hoort nie'], 0), ('Hy het sy pa se koeie opgepas toe Sipho hom van die leeuaanval vertel het.', ['hoort', 'hoort nie'], 0), ('Die bome het lang takke gehad.', ['hoort', 'hoort nie'], 1),
             ('Jabu het nie saam met Sipho gegaan nie want hy moes die vee rivier toe neem.', ['hoort', 'hoort nie'], 0), ('Die vee was moeg.', ['hoort', 'hoort nie'], 1), ('Jabu het geweet hy moet sy vee baie goed oppas.', ['hoort', 'hoort nie'], 0)],
            'Sinne wat nie oor Jabu se verantwoordelikheid gaan nie, hoort nie in die paragraaf nie.', src='workbook', page=25, item='sinne', status='needs_review'),
    order('Die korrekte volgorde van die gebeure', 'Sit die vier sinne wat wel by die onderwerp hoort in die korrekte volgorde.',
          ['Jabu was ’n baie verantwoordelike mens.', 'Hy het sy pa se koeie opgepas toe Sipho hom van die leeuaanval vertel het.', 'Jabu het nie saam met Sipho gegaan nie want hy moes die vee rivier toe neem.', 'Jabu het geweet hy moet sy vee baie goed oppas.'],
          'Eers die stelling oor Jabu, dan wat gebeur het, die rede en die slotsom.', perm=[2, 0, 3, 1], src='workbook', page=25, item='sinne', status='needs_review'),
    figure('Prent 1', FIG + 'wk076-prent-1.webp', 'Jabu sit met sy kierie by die koeie op die koppie.', page=25, section='activity'),
    figure('Prent 2', FIG + 'wk076-prent-2.webp', 'Jabu en ander sit snags om die vuur en luister na die mans.', page=25, section='activity'),
    sa('Beskryf die prente', 'Skryf nou ’n beskrywende sin oor die gebeure in elke prent.', None, lines=4, page=25, item='prente'),
    writing('My woordeboek: Nuwe woorde', 'Skryf nuwe woorde uit die storie neer wat jy wil onthou.', lines=4, page=25, item='My woordeboek'),
    match('Pas die deel van ’n storie by sy betekenis', 'Verbind elke deel met wat dit beteken.', [('Agtergrond', 'wanneer en waar die gebeure plaasvind'), ('Karakters', 'mense of diere in die storie'), ('Intrige', 'wat in die storie gebeur'), ('Tema', 'die boodskap wat oorgedra word')],
          'Dit is die werkboek se verduideliking van die dele van ’n storie.', status='official'),
  ],
  quiz=[
    q('vocabulary', 'Wat beteken “agtergrond” in ’n storie?', 'Wanneer en waar die gebeure plaasvind', ['Wie die skrywer is', 'Wat die boodskap is', 'Die titel van die storie'], 'Die werkboek sê agtergrond is wanneer en waar die gebeure plaasvind.', status='official', src='workbook', page=24),
    q('vocabulary', 'Wat is die “intrige” van ’n storie?', 'Wat in die storie gebeur', ['Die mense in die storie', 'Die boodskap van die storie', 'Die plek van die storie'], 'Die intrige is die gebeure of storielyn.', status='official', src='workbook', page=24),
    q('vocabulary', 'Wat is die “tema” van ’n storie?', 'Die boodskap wat oorgedra word', ['Die karakters', 'Die gebeure', 'Die plek'], 'Die tema is die boodskap van die storie.', status='official', src='workbook', page=24),
    q('vocabulary', 'Wat is “karakters” in ’n storie?', 'Mense of diere in die storie', ['Die gebeure', 'Die boodskap', 'Die plek en tyd'], 'Karakters is die mense of diere in die storie.', status='official', src='workbook', page=24),
    q('inference', 'Watter byvoeglike naamwoord beskryf die jakkals die beste?', 'slu', ['gulsig', 'verantwoordelik', 'jonk'], 'Die jakkals het die leeu slim in die strik gevang.', status='needs_review', src='workbook', page=24, item='karakters'),
    q('inference', 'Watter byvoeglike naamwoord beskryf die leeu in die storie?', 'oneerlik', ['betroubaar', 'verantwoordelik', 'wys'], 'Die leeu het sy belofte verbreek.', status='needs_review', src='workbook', page=24, item='karakters'),
    q('inference', 'Watter sin handel NIE oor Jabu se verantwoordelikheid nie?', 'Die bome het lang takke gehad.', ['Jabu was ’n baie verantwoordelike mens.', 'Jabu het geweet hy moet sy vee baie goed oppas.', 'Hy het sy pa se koeie opgepas.'], 'Die sin oor die bome pas nie by die onderwerp nie.', status='needs_review', src='workbook', page=25, item='sinne'),
    q('main_idea', 'Wat is die tema van die volksverhaal van Jabu en die leeu?', 'Jy moet ’n belofte nakom.', ['Leeus is bang vir jakkalse.', 'Veewagters is baie sterk.', 'Dit is altyd gevaarlik by die rivier.'], 'Die storie wys wat gebeur as jy ’n belofte verbreek.', status='needs_review'),
  ])
