import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

WRITE_PROCESS = ['Beplan jou skryfwerk met ’n breinkaart.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.',
                 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']

# ============================================================== 70 Spelling en spelpatrone
# (sentence, [option, option], index of the correct option) -- the answer key is printed at the bottom of workbook page 13.
BOARD = [
  ('Matthew het saam met sy ___ gaan stap.', ['hondde', 'honde'], 1), ('Hy het oor ___ geval.', ['stompe', 'stomps'], 0), ('Ek het ___ gekry.', ['fossiele', 'fossiels'], 0),
  ('Matthew het oorblyfsels in sy ___ gehad.', ['handde', 'hande'], 1), ('Die ___ hou daarvan om in die veld te stap.', ['seune', 'seuns'], 1),
  ('Hy het twee ___ vasgehou.', ['sleutelbene', 'sleutelbenne'], 0), ('Hulle het nog dele van die ___ gekry.', ['skelete', 'skelette'], 1),
  ('Daar word vermoed ___ het hulle gejaag.', ['diere', 'dierre'], 0), ('Die wetenskaplike ___ sê die fossiel behoort tot die hominiede spesie.', ['spane', 'spanne'], 1),
  ('Hulle het kleinerige ___ gehad.', ['tande', 'tandde'], 0), ('Die ___ het die spesie Sediba gedoop.', ['wetenskaplikes', 'wetenskaplikkes'], 0),
  ('Die spesie het nog in ___ gelewe.', ['bomme', 'bome'], 1), ('Die Sediba-spesie se ___ was primitief.', ['voette', 'voete'], 1),
  ('Hulle het regop op hulle lang ___ geloop.', ['beene', 'bene'], 1), ('Hulle het nie ___ gedra nie.', ['hemde', 'hempte'], 0), ('Daar was nie ___ nie.', ['padde', 'paaie'], 1),
  ('Hulle het baie ___ gehad.', ['kindere', 'kinders'], 1), ('Die Sediba-spesie was ___.', ['boere', 'boerre'], 0), ('Hulle het ___ aangehou.', ['skaape', 'skape'], 1),
  ('Die Sediba-spesie het nie in ___ gewoon nie.', ['huisse', 'huise'], 1), ('Saans het hulle om ___ gekuier.', ['vuure', 'vure'], 1), ('Die Sediba-spesie het 2 ___ gehad.', ['ooge', 'oë'], 1),
  ('Hulle het daarvan gehou om in die ___ te sit.', ['skadus', 'skadu’s'], 1), ('Hulle was bang vir ___.', ['wolfe', 'wolwe'], 1), ('Hulle het nie geweet van ___ nie.', ['skepe', 'skippe'], 0),
  ('Hulle het uit groot ___ bestaan.', ['families', 'familieë'], 0), ('Hulle het ___ gejag vir voedsel.', ['bokke', 'boks'], 0), ('___ is op die werklikheid gebaseer.', ['Koerantberigte', 'Koerantberigtte'], 0),
]

def board_card(n):
    rows = BOARD[(n - 1) * 7:n * 7]
    return choices(f'Spelreëlspeletjie ({n} van 4)', 'Kies die korrekte spelling van die meervoud.', rows,
                   'Onthou die reëls: kort klank – verdubbel die medeklinker + e; lang klank – een klinker val weg + e; tweeklank – voeg -e of -s by. Daar is altyd uitsonderings.',
                   src='workbook', page=12, item=f'speletjie {n}', status='official', hint='Probeer weer – kyk watter spelling die reël volg.')

L70 = lesson(70,
  intro='Vandag speel ons die spelreëlspeletjie! Jy hersien hoe meervoude gevorm word en kies elke keer die korrekte spelling.',
  objectives=['Hersien hoe meervoude gevorm word.', 'Die korrekte spelling van meervoude kies.', 'Spelreëls vir kort klanke, lang klanke en tweeklanke gebruik.'],
  learn=[
    text('Kom ons kyk weer na hoe meervoude gevorm word', 'Onthou: daar is altyd uitsonderings op elke reël.', page=12),
    table('Meervoudsreëls', ['Klank', 'Reël', 'Voorbeeld'], [['Kort klanke', 'Die medeklinker aan die einde van die woord verdubbel en die woord kry ’n “-e” by.', 'kat – katte'],
          ['Lang klanke', 'Een van die klinkers in die middel val weg en die woord kry ’n “-e” by.', 'boom – bome'], ['Tweeklanke', 'Ons voeg ’n -e of ’n -s by.', 'boek – boeke, seun – seuns']], page=12),
    text('Die spelreëls van die speletjie', bullets=['Plaas jou merker aan die begin.', 'Gooi die dobbelsteen en skuif die aantal plekke.', 'Omkring die korrekte spelling van die meervoud.', 'Gaan jou antwoord na.',
         'Verkeerd? Jy slaan ’n beurt oor.', 'Die eerste een by nommer 35 is die wenner.'], page=12),
  ],
  examples=[example(table('Kyk hoe die reëls werk', ['Enkelvoud', 'Meervoud', 'Reël'], [['hond', 'honde', 'voeg -e by'], ['kat', 'katte', 'kort klank: verdubbel + e'], ['boom', 'bome', 'lang klank: een klinker val weg + e'],
          ['kind', 'kinders', 'uitsondering: -ers']], src='supplementary', page=12))],
  acts=[board_card(1), board_card(2), board_card(3), board_card(4),
    fill('Maak die meervoud', 'Een kat, twee {{1}}. Een boom, drie {{2}}. Een boek, vier {{3}}.', {1: 'katte', 2: 'bome', 3: 'boeke'},
         'kat: kort klank → katte; boom: lang klank → bome; boek: tweeklank → boeke.', bank=['katte', 'bome', 'boeke'], src='supplementary', status='official'),
    tf('Waar of onwaar?', 'Die meervoud van “kind” is “kinde”.', False, 'Die meervoud van kind is kinders – ’n uitsondering op die reël.', status='derived_from_rule'),
  ],
  quiz=[
    q('spelling', 'Wat is die korrekte meervoud van “hond”?', 'honde', ['hondde', 'honds', 'hondjes'], 'Tweeklank-reël: voeg -e by.', status='official', src='workbook', page=13, item='1'),
    q('spelling', 'Wat is die meervoud van “fossiel”?', 'fossiele', ['fossiels', 'fossielle', 'fossielen'], 'Die werkboek gee die antwoord: fossiele.', status='official', src='workbook', page=13, item='3'),
    q('spelling', 'Watter spelling van die meervoud van “skelet” is korrek?', 'skelette', ['skelete', 'skelettes', 'skeletten'], 'Kort klank: verdubbel die medeklinker + e → skelette.', status='official', src='workbook', page=13, item='8'),
    q('spelling', 'Wat is die meervoud van “boom”?', 'bome', ['bomme', 'booms', 'boome'], 'Lang klank: een klinker val weg + e → bome.', status='official', src='workbook', page=13, item='14'),
    q('spelling', 'Watter spelling is korrek?', 'kinders', ['kindere', 'kinderen', 'kindes'], 'Kind – kinders is ’n uitsondering.', status='official', src='workbook', page=13, item='21'),
    q('spelling', 'Wat is die meervoud van “oog”?', 'oë', ['ooge', 'oogs', 'ogen'], 'Die werkboek gee die antwoord: oë.', status='official', src='workbook', page=13, item='27'),
    q('spelling', 'Watter spelling is korrek?', 'wolwe', ['wolfe', 'wolfs', 'wolvve'], 'Die f verander in w: wolf – wolwe.', status='official', src='workbook', page=13, item='29'),
    q('spelling', 'Wat is die meervoud van “skaap”?', 'skape', ['skaape', 'skaaps', 'skapen'], 'Lang klank: een a val weg + e → skape.', status='official', src='workbook', page=13, item='23'),
    q('spelling', 'Watter spelling is korrek?', 'skadu’s', ['skadus', 'skaduwe', 'skadue'], 'Die werkboek gee die antwoord: skadu’s.', status='official', src='workbook', page=13, item='28'),
    q('spelling', 'Watter reël pas by “kat – katte”?', 'Kort klank: verdubbel die medeklinker en voeg -e by', ['Lang klank: een klinker val weg', 'Net ’n -s byvoeg', 'Die woord bly dieselfde'], 'Die werkboek gee hierdie voorbeeld by die reël vir kort klanke.', status='official', src='workbook', page=12),
  ])

# ============================================================== 71 Nelson Mandela gaan hoërskool toe
BIO71 = [
  'Een nag toe ek nege jaar oud was het ek ’n beroering in ons huishouding gehoor. Ek het my pa in my ma se hut aangetref waar hy besig was om onophoudelike te hoes. Later het ek uitgevind dat hy aan ’n ernstige longsiekte gely het. Kort hierna is my pa oorlede, en het my lewe radikaal verander. Ek moes by my oom gaan bly. Hy sou vir my sorg en toesien dat ek skoolgaan. Ek het my paar besittings ingepak, en saam met my ma na my nuwe huis toe geloop.',
  'Dit was vir my swaar om Qunu te verlaat. Ek het omgedraai en vir oulaas gekyk na die huis waar ek so gelukkig was. Ek het na die hutte gekyk, en na die mense wat met hulle dagtake voortgegaan het. Ek het die stroompie gesien, waar ek saam met die ander seuns geplas en gespeel het. My oë het tot rus gekom op die drie hutte waaruit ons tuiste bestaan het. Ek kon myself glad nie voorstel hoe my nuwe toekoms gaan wees nie.',
  'Ek het by my oom Jongi in Mqhekezweni, ’n dorpie daar naby, gaan woon. Hy was ook my pa se beste vriend. Ek het Qunu en my familie gemis, maar ek het ’n goeie lewe by oom Jongi gelei. Ek het met sy seun, Justice, gespeel, en ons het baie pret saam gehad. My oom het my soos sy eie kind behandel. Ek het ’n eenvertrekskooltjie daar naby bygewoon en Engels, Xhosa, Wiskunde, Geskiedenis en Aardrykskunde geleer. Ek het goed gevaar op skool, omdat ek baie hard gewerk het en my tante saans my huiswerk nagegaan het.',
  'Toe ek sestien geword het, het Oom Jongi my na die Clarkebury-skool toe gestuur. Net soos my pa het my oom geglo dat opvoeding baie belangrik is.',
  'Clarkebury was ’n baie groter en beter skool as Mqhekezweni. Die skool het bestaan uit ’n groep van ongeveer twee dosyn geboue in die koloniale styl.',
  'Op my eerste skooldag het ek my nuwe stewels aangetrek. Terwyl ek oor die blink houtvloer van die klaskamer ingekletter het, het ek opgemerk dat twee meisies in die voorste ry my flou vertoning geamuseerd dophou. Later het ek een van daardie meisies goed leer ken, en het sy my beste vriendin by Clarkebury geword.',
  'Ek het gou by my nuwe lewe by Clarkebury aangepas. Ek het so dikwels as moontlik aan sport deelgeneem, alhoewel ek gemiddelde prestasies behaal het. Die meeste van my klasmaats kon vinniger as ek hardloop en het beter as ek in die klas presteer. Ek het baie gehad om in te haal.',
  'Ná my wankelrige begin het ek agtergekom hoe dinge werk en kon ek vinniger begin vorder. Ek het die junior sertifikaat (graad agt tot tien) binne twee jaar, in plaas van die gebruiklike drie jaar, voltooi. Ek het die reputasie gekry dat ek ’n uitstekende geheue het, maar eintlik was ek net ’n harde werker.',
  'Op die ouderdom van een-en-twintig het ek by die Fort Hare-universiteitskollege gaan studeer. Dit is egter stories vir ’n ander keer.']

L71 = lesson(71,
  intro='Nelson Mandela het ook eens ’n skoolkind gewees. Lees hoe sy lewe verander het toe hy nege jaar oud was en wat hy op skool beleef het.',
  skills=[LISTEN, READ, WRITE, LANG],
  objectives=['Voorspel waaroor ’n teks gaan en ’n uittreksel uit ’n outobiografie lees.', 'Die outobiografie hervertel en ’n tydlyn van die gebeure opstel.',
              'Woorddele (basiswoorde, afleidings en samestellings) uitken.', 'Afkortings, akronieme en verkortings verstaan.'],
  pass_=passage('Nelson Mandela gaan hoërskool toe', BIO71, glossary=[
      ('beroering', 'Onrus of ’n harde geraas.'), ('longsiekte', '’n Siekte van die longe.'), ('oorlede', 'Dood (’n beleefde woord).'), ('radikaal', 'Heeltemal of baie groot.'),
      ('besittings', 'Dinge wat jy besit, soos klere en speelgoed.'), ('koloniale', 'Van die tyd toe ’n ander land oor Suid-Afrika regeer het.'),
      ('prestasies', 'Resultate wat jy behaal het, soos in sport of op skool.'), ('wankelrige', 'Onseker of nie stewig nie.')]),
  learn=[
    note('’n Outobiografie is ’n storie wat iemand oor sy of haar eie lewe skryf. Hierdie storie is gebaseer op die outobiografie deur Nelson Mandela. Ons het dit verkort en makliker gemaak om te lees.', title='Wat is ’n outobiografie?', page=14),
    text('Woorde word só gevorm', bullets=['**Basiswoorde**', '**Afleidings** (basis + voorvoegsel en/of agtervoegsel, en/of verbindingsklank)', '**Samestellings** (basis + basis)'], page=15),
    text('’n Lettergreep', '’n Lettergreep is ’n deeltjie van ’n woord. Indien woorde aan die einde van ’n reël afgebreek moet word, moet dit tussen twee lettergrepe gedoen word.', page=15),
    text('Drie soorte afkortings', bullets=['**Gewone afkortings**: ons spreek die oorspronklike woord volledig uit (“bl.” word “bladsy”).',
         '**Akronieme (letterwoorde)**: die letters van verskeie woorde word as een woord uitgespreek, bv. Sasol.', '**Verkortings**: ons spreek oorspronklike lettergrepe of dele van verskeie woorde as een woord uit, bv. “Australasië” vir Australië en Asië.'], page=15),
  ],
  examples=[example(table('Voorbeelde van woorddele', ['Woord', 'Lettergrepe', 'Soort'], [['huiswerk', 'huis-werk', 'samestelling (huis + werk)'], ['longsiekte', 'long-siek-te', 'samestelling (long + siekte)']], src='supplementary', page=15))],
  acts=[
    discuss('Ons praat: Voorspel', 'Voorspel volgens die opskrif en illustrasies waaroor hierdie teks handel.', page=14, item='Ons praat'),
    discuss('Luister na die teks', 'Druk die knoppie en luister terwyl jy die teks saamlees.', src='supplementary', speak='passage'),
    discuss('Ons praat: Hervertel', 'Bespreek met ’n maat.', points=['Hervertel die outobiografie vir jou maat.', 'Beskryf Nelson Mandela se kinderdae na die dood van sy vader.', 'Hoe het sy lewe verander?'], page=15, item='Ons praat'),
    sa('Gebeure op 9, 16 en 21', 'Lees weer die outobiografie. Skryf neer watter gebeure plaasgevind het toe Nelson Mandela 9, 16 en 21 jaar oud was (jou tydlyn).',
       '9 jaar: Sy pa is oorlede en hy het by sy oom Jongi in Mqhekezweni gaan bly.\n16 jaar: Oom Jongi het hom na die Clarkebury-skool gestuur.\n21 jaar: Hy het by die Fort Hare-universiteitskollege gaan studeer.', lines=6, page=15, item='tydlyn', status='derived_from_text'),
    order('Tydlyn', 'Sit die gebeure in die volgorde waarin hulle in die teks gebeur het.',
          ['Mandela se pa is oorlede.', 'Hy gaan bly by oom Jongi in Mqhekezweni.', 'Oom Jongi stuur hom na die Clarkebury-skool.', 'Hy voltooi die junior sertifikaat binne twee jaar.', 'Op 21 gaan hy studeer by Fort Hare.'],
          'Die teks vertel sy lewe in die volgorde van sy ouderdom: 9, 16, daarna die junior sertifikaat, en op 21 Fort Hare.', perm=[3, 0, 4, 2, 1], src='supplementary'),
    match('Afkortings en hulle betekenisse', 'Gebruik jou woordeboek: verbind elke afkorting met sy betekenis.',
          [('a.g.v.', 'as gevolg van'), ('d.m.v.', 'deur middel van'), ('e-pos', 'elektroniese pos'), ('i.v.m.', 'in verband met'), ('ESKOM', 'Elektrisiteitsvoorsieningskommissie')],
          'Hierdie is uit die tabel in die werkboek (bladsy 15).', src='workbook', page=15, item='afkortings', status='derived_from_rule'),
    choices('Watter soort afkorting?', 'Is dit ’n gewone afkorting, ’n akroniem of ’n verkorting?',
            [('a.g.v.', ['gewone afkorting', 'akroniem', 'verkorting'], 0), ('d.m.v.', ['gewone afkorting', 'akroniem', 'verkorting'], 0), ('e-pos', ['gewone afkorting', 'akroniem', 'verkorting'], 2),
             ('i.v.m.', ['gewone afkorting', 'akroniem', 'verkorting'], 0), ('ESKOM', ['gewone afkorting', 'akroniem', 'verkorting'], 1)],
            'Gewone afkortings word voluit gelees; ’n akroniem word as een woord uitgespreek; ’n verkorting plak dele van woorde saam.', src='workbook', page=15, item='afkortings', status='needs_review'),
    choices('Afleiding of samestelling?', 'Hierdie woorde kom uit die teks. Is dit ’n afleiding of ’n samestelling?',
            [('beroering', ['afleiding', 'samestelling'], 0), ('longsiekte', ['afleiding', 'samestelling'], 1), ('omgedraai', ['afleiding', 'samestelling'], 0), ('huiswerk', ['afleiding', 'samestelling'], 1)],
            'Samestelling = basis + basis (long + siekte, huis + werk). Afleiding = basis + voor- of agtervoegsel (be-roer-ing, om-ge-draai).', src='workbook', page=15, item='woorddele', status='derived_from_rule'),
    fill('Lettergrepe', 'beroering: {{1}}\nlongsiekte: {{2}}\nomgedraai: {{3}}\nhuiswerk: {{4}}',
         {1: ['be-roe-ring', 'be roe ring'], 2: ['long-siek-te', 'long siek te'], 3: ['om-ge-draai', 'om ge draai'], 4: ['huis-werk', 'huis werk']},
         'Skryf die lettergrepe met koppeltekens, bv. huis-werk.', prompt='Verdeel elke woord in lettergrepe (skei met ’n koppelteken).', src='workbook', page=15, item='woorddele', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Nelson Mandela se pa het hom na die Clarkebury-skool gestuur.', False, 'Sy pa was reeds oorlede; oom Jongi het hom na Clarkebury gestuur.'),
  ],
  quiz=[
    q('literal', 'Hoe oud was Nelson Mandela toe sy pa oorlede is?', 'Nege jaar oud', ['Sestien jaar oud', 'Een-en-twintig jaar oud', 'Twaalf jaar oud'], 'Die teks begin: “Een nag toe ek nege jaar oud was …”.', ev=['nege jaar oud']),
    q('literal', 'Aan watter siekte het sy pa gely?', '’n Ernstige longsiekte', ['Malaria', '’n Beenbreuk', 'Griep'], 'Hy het aan ’n ernstige longsiekte gely.', ev=['longsiekte gely']),
    q('literal', 'By wie het Nelson gaan bly?', 'Sy oom Jongi', ['Sy tante', 'Sy ouma', 'Sy vriend Justice'], 'Sy oom Jongi, sy pa se beste vriend.', ev=['Ek moes by my oom gaan bly', 'oom Jongi in Mqhekezweni']),
    q('literal', 'Waarheen het oom Jongi hom op sestien gestuur?', 'Na die Clarkebury-skool', ['Na Fort Hare', 'Na Qunu', 'Na ’n eenvertrekskooltjie'], 'Toe hy sestien was, het oom Jongi hom na Clarkebury gestuur.', ev=['Clarkebury-skool toe gestuur']),
    q('literal', 'Hoe lank het hy oor die junior sertifikaat gedoen?', 'Twee jaar', ['Drie jaar', 'Vyf jaar', 'Een jaar'], 'Hy het dit binne twee jaar in plaas van die gebruiklike drie voltooi.', ev=['binne twee jaar']),
    q('inference', 'Hoekom het Nelson die reputasie gekry dat hy ’n goeie geheue het?', 'Omdat hy vinnig geleer het, maar eintlik net hard gewerk het.', ['Omdat hy nooit huiswerk gedoen het nie.', 'Omdat hy die beste sportman was.', 'Omdat hy by Fort Hare was.'], 'Die teks sê hy was “net ’n harde werker”.', ev=['uitstekende geheue'], status='derived_from_text'),
    q('vocabulary', 'Wat beteken die afkorting “a.g.v.”?', 'as gevolg van', ['aan die gang van', 'altyd goed vir', 'agter die gebou van'], 'Dit is ’n gewone afkorting wat as “as gevolg van” gelees word.', status='derived_from_rule', src='workbook', page=15),
    q('vocabulary', 'Watter woord is ’n samestelling?', 'huiswerk', ['beroering', 'omgedraai', 'radikaal'], 'Huiswerk = huis + werk (twee basiswoorde).', status='derived_from_rule', src='workbook', page=15, item='woorddele'),
    q('vocabulary', 'ESKOM is ’n …', 'akroniem', ['gewone afkorting', 'samestelling', 'basiswoord'], 'Die letters van die woorde word as een woord uitgespreek: ’n akroniem (soos Sasol).', status='needs_review', src='workbook', page=15),
    q('main_idea', 'Waaroor gaan hierdie uittreksel hoofsaaklik?', 'Hoe Nelson Mandela se lewe en skoolgang ná sy pa se dood verander het', ['Hoe om sokker te speel', 'Hoe hy president geword het', 'Hoe hy ’n huis gebou het'], 'Dit vertel van sy kinderdae en skoolgang tot op 21.', status='needs_review'),
  ])

# ============================================================== 72 Kom ons skryf 'n storie
L72 = lesson(72,
  intro='Jy het ook ’n lewensverhaal! Vandag beplan jy ’n dagboekinskrywing oor die hoogtepunte van jou lewe.',
  objectives=['’n Geheuekaart gebruik om skryfwerk te beplan.', '’n Dagboekinskrywing in die eerste persoon skryf.', 'Gebeure in die korrekte volgorde vertel en tydwoorde gebruik.', 'Jou werk hersien en foute korrigeer.'],
  learn=[
    text('Dagboekinskrywings – let op die volgende', bullets=['Dui die datum aan.', 'Vertel in die eerste persoon (“ek”).', 'Begin elke paragraaf met ’n tydwoord.', 'Vertel die gebeure in die korrekte volgorde.'], page=17),
    note('Liewe Dagboek\nVandag dink ek terug oor my lewenspad en besef ek hoe geseënd ek is, al was daar ook swaar tye …', title='Só kan jy begin', page=16),
    text('Die skryfproses', bullets=['**Beplan** jou dagboekinskrywing deur die breinkaart in te vul.', 'Skryf jou **eerste weergawe** in jou klaswerkboek.', 'Laat ’n maat jou werk **hersien**.', '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** vir publikasie.'], page=16),
  ],
  acts=[
    writing('Beginjare', 'Skryf wanneer en waar jy gebore is, en spesiale gebeurtenisse van jou kleuterjare.', lines=6, page=16, item='Beginjare'),
    writing('Middeljare', 'Skryf spesiale gebeurtenisse in Graad 1 tot 3.', lines=6, page=16, item='Middeljare'),
    writing('Huidige jare', 'Skryf spesiale gebeurtenisse in Graad 4 tot 6.', lines=6, page=16, item='Huidige jare'),
    order('Dele van jou dagboekinskrywing', 'Sit die dele van die dagboekinskrywing in die regte volgorde.',
          ['Aanhef: “Liewe Dagboek”', 'Beginjare', 'Middeljare', 'Huidige jare'], 'Jy begin met die aanhef en vertel dan die gebeure van jonk na ouer.', src='supplementary', status='derived_from_rule'),
    writing('My dagboekinskrywing (finale weergawe)', 'Skryf die finale weergawe van jou dagboekinskrywing: “Liewe Dagboek, vandag dink ek terug oor my lewenspad …”',
            checklist=['Ek het die datum aangedui.', 'Ek het in die eerste persoon (“ek”) vertel.', 'Elke paragraaf begin met ’n tydwoord.', 'Die gebeure is in die korrekte volgorde.', 'Ek het my spelling en punktuasie gekorrigeer.'],
            tips=WRITE_PROCESS, lines=14, page=17, item='Finale weergawe'),
    choices('Hoort dit in ’n dagboekinskrywing?', 'Kies Ja of Nee.',
            [('Die datum', ['Ja', 'Nee'], 0), ('“Ek” (eerste persoon)', ['Ja', 'Nee'], 0), ('Gebeure deurmekaar sonder volgorde', ['Ja', 'Nee'], 1), ('’n Tydwoord aan die begin van ’n paragraaf', ['Ja', 'Nee'], 0)],
            'Die werkboek sê: dui die datum aan, vertel in die eerste persoon, begin elke paragraaf met ’n tydwoord en gebruik die korrekte volgorde.', src='supplementary', status='official'),
    fill('Voltooi die reël', 'Ek skryf ’n dagboekinskrywing in die {{1}} persoon. Elke paragraaf begin met ’n {{2}}.', {1: 'eerste', 2: 'tydwoord'}, 'Eerste persoon = “ek”. ’n Tydwoord soos eers, toe, daarna of later.', bank=['eerste', 'tweede', 'tydwoord', 'naamwoord'], src='supplementary', status='official'),
  ],
  quiz=[
    q('grammar', 'Watter aanhef begin ’n dagboekinskrywing?', 'Liewe Dagboek', ['Geagte Meneer', 'Beste vriend', 'Aan wie dit mag aangaan'], 'Die werkboek se voorbeeld begin met “Liewe Dagboek”.', status='official', src='supplementary', page=16),
    q('grammar', 'In watter persoon word ’n dagboekinskrywing geskryf?', 'Die eerste persoon (“ek”)', ['Die tweede persoon (“jy”)', 'Die derde persoon (“hy/sy”)', 'Dit maak nie saak nie'], 'Vertel in die eerste persoon (“ek”).', status='official', src='supplementary', page=17),
    q('grammar', 'Waarmee begin elke paragraaf in ’n dagboekinskrywing?', '’n Tydwoord', ['’n Vraag', '’n Prent', '’n Rympie'], 'Begin elke paragraaf met ’n tydwoord.', status='official', src='supplementary', page=17),
    q('sequencing', 'In watter volgorde vertel jy die gebeure?', 'In die korrekte (tyd)volgorde', ['Van die einde na die begin', 'Deurmekaar', 'Net die ergste gebeure'], 'Vertel die gebeure in die korrekte volgorde.', status='official', src='supplementary', page=17),
    q('grammar', 'Watter woord is ’n tydwoord?', 'Daarna', ['Mooi', 'Hond', 'Groot'], 'Tydwoorde wys wanneer iets gebeur: eers, toe, daarna, later, uiteindelik.', status='derived_from_rule'),
    q('main_idea', 'Wat is die eerste stap van die skryfproses?', 'Beplan', ['Publiseer', 'Korrigeer', 'Skryf die finale weergawe'], 'Die skryfproses begin met beplanning.', status='official', src='supplementary', page=16),
    q('main_idea', 'Wat doen jy ná jou eerste weergawe?', 'Laat ’n maat dit hersien en korrigeer die foute', ['Gooi dit weg', 'Skryf dit presies so oor', 'Gee dit dadelik vir die onderwyser'], 'Volgens die skryfproses hersien ’n maat jou werk en jy korrigeer spelfoute en punktuasie.', status='official', src='supplementary', page=16),
    q('main_idea', 'Hoekom gebruik jy ’n geheuekaart voordat jy skryf?', 'Om jou skryfwerk te beplan', ['Om te teken', 'Om jou handskrif te oefen', 'Om die datum te onthou'], 'Die geheuekaart help jou om jou dagboekinskrywing te beplan.', status='derived_from_text', src='supplementary', page=16),
  ])
