import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

OPEN = '(Eie antwoord – daar is nie net een regte antwoord nie.)'
WRITE_PROCESS = ['Beplan jou skryfwerk met ’n breinkaart.', 'Skryf jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.',
                 'Korrigeer spelfoute en punktuasie.', 'Skryf jou finale weergawe netjies neer.']

# ============================================================== 66 Charl soek verder
BODY66 = """’n Paar weke later sien Charl ’n pamflet wat jongmense nooi om by ’n nuwe sanggroep aan te sluit. Dadelik besluit hy om te gaan uitvind of hy goed genoeg is. Maar terwyl hy sing, begin sy stem te kraak en te piep. Een van die beoordelaars trek ’n skewe gesig, en toe weet Charl hy sal nie gekies word nie.
Charl stap met hangskouers terug huis toe en gaan reguit na die tuin toe. “Al my maats het spesiale talente,” dink hy. “Ek wens daar was iets wat ek regtig goed kon doen.” Die res van die skoolvakansie hou Charl aan om te soek na sy talent, en elke keer stap hy moedeloos terug huis toe om tyd in die tuin deur te bring.
Teen die einde van die vakansie sien Charl weer sy maats Dingani en Jan. “Hoe het dit met die groot sokkertoernooi gegaan?” vra hy vir Dingani.
“Ons het gewen!” antwoord Dingani.
“En hoe was die konsert?” vra Charl vir Jan.
“Dit vind môre plaas,” antwoord Jan. “Maar ons koor het regtig hard gewerk, en ek gaan ’n solo sing!”
“Veels geluk,” sê Charl vir hulle. “Ek wens ek het iets gehad waarop ek trots kon wees.”
“Jy maak seker ’n grap?” vra Jan. “Kyk hoe groot is die groente in jou tuin! Dit lyk so smaaklik en gesond! Elke keer wanneer ek iets probeer kweek, word dit bruin en gaan dood. Ek wens ek het jou hand met ’n plant gehad.”
“Regtig?” antwoord Charl. “Ek het nooit aan tuinmaak as iets besonders gedink nie.” Hy glimlag. “Waarom kom julle nie albei môre saam met my Dingani se sokkeroorwinning vier nie? Kom sommer vir aandete. Ons sal vars groente uit my tuin eet, en dan kan ons Jan se konsert bywoon!”"""

L66 = lesson(66,
  intro='Charl soek nog steeds sy talent. Lees die tweede deel van die storie en ontdek wat Jan vir hom sê.',
  objectives=['Lees die tweede deel van ’n storie en beantwoord meerkeusevrae.', 'Soek sinonieme (woorde met dieselfde betekenis) in die teks.',
              'Praat oor hoe die karakters voel en gee jou eie mening.', 'Skryf ’n dagboekinskrywing in die eerste persoon.'],
  pass_=passage('Charl soek verder', BODY66, glossary=[
      ('pamflet', '’n Klein gedrukte blad met inligting wat uitgedeel word.'),
      ('beoordelaars', 'Mense wat besluit of jy goed genoeg is.'),
      ('hangskouers', 'Skouers wat swaar hang omdat jy teleurgesteld of moedeloos is.'),
      ('moedeloos', 'Teleurgesteld en sonder hoop om aan te hou probeer.'),
      ('talent', '’n Spesiale vermoë om iets baie goed te doen.'),
      ('solo', 'Wanneer een persoon alleen sing of speel.'),
      ('sokkeroorwinning', 'Die wen van ’n sokkerwedstryd.')]),
  learn=[
    note('Sinonieme is woorde met dieselfde betekenis.', title='Wat is sinonieme?', page=5),
    text('’n Dagboekinskrywing moet bevat:', bullets=['die datum', 'jou eerstepersoonvertelling (“ek”)', 'die korrekte volgorde van die gebeure', 'saamgestelde sinne'], page=5),
    text('Die skryfproses', bullets=['**Beplan** jou skryfwerk met ’n breinkaart.', '**Skryf** jou eerste weergawe.', 'Laat ’n maat jou werk **hersien**.',
                                      '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** vir publikasie.'], page=5),
  ],
  acts=[
    discuss('Luister na die storie', 'Druk die knoppie en luister terwyl jy saamlees.', src='supplementary', speak='passage'),
    sa('Skryfvraag 1', 'Hoe weet jy dat Dingani se span goed sokker speel?', 'Hulle het die groot sokkertoernooi gewen.', lines=2, page=4, item=1),
    mcq('Meerkeusevraag 1', 'Wat het Jan vir Charl aan die einde van die storie help besef?',
        ['Dat daar reeds iets is wat hy goed doen.', 'Dat hy goed sokker speel.', 'Dat tuinmaak harde werk is.', 'Dat sy maats meer talentvol is as hy.'], 0,
        'Jan sê hoe groot en gesond Charl se groente is en dat hy self nie plante kan laat groei nie. So help hy Charl besef dat tuinmaak sy talent is.',
        per_option={1: 'Charl het swak sokker gespeel.', 2: 'Jan sê nie dat tuinmaak harde werk is nie – hy bewonder dit.', 3: 'Jan sê juis dat hy wens hy kon plante kweek soos Charl.'},
        page=4, item='A'),
    mcq('Meerkeusevraag 2', 'Waarom het Charl sy vriende oorgenooi vir aandete?',
        ['Om die einde van die somer te vier.', 'Om sy talent asook hulle s’n te vier.', 'Om sokker te speel.', 'Om hulle te leer hoe om tuin te maak.'], 1,
        'Charl nooi hulle om Dingani se sokkeroorwinning te vier, met groente uit sy eie tuin (sy talent), en om Jan se konsert by te woon.',
        per_option={0: 'Die storie praat nie van die einde van die somer nie.', 2: 'Hulle gaan eet; Dingani se sokker is reeds gespeel.', 3: 'Charl wil vier, nie leer nie.'}, page=4, item='B'),
    match('Sinonieme in die storie', 'Verbind elke beskrywing met die korrekte woord uit die storie (werkkaarte 65 en 66).',
          [('met trae treë (werkkaart 65)', 'sleepvoetend'), ('prewel (werkkaart 65)', 'mompel'), ('wanneer iemand alleen sing (werkkaart 66)', 'solo'),
           ('’n buitengewone vermoë (werkkaart 66)', 'talent')],
          'Kyk na die vetgedrukte woorde in die twee stories.', src='workbook', page=5, item='sinonieme', status='derived_from_text'),
    sa('Sinoniem 5', '’n baie spesiale vermoë (werkkaart 66) – watter woord uit die storie kan jy gebruik?', 'talent (die storie praat ook van “spesiale talente”)', lines=1, page=5, item='sinonieme 5', status='needs_review'),
    sa('Skryfvraag 2', 'Aan watter aktiwiteite het Charl probeer deelneem?', 'Hy het sokker probeer speel en by ’n sanggroep se oudisie probeer aansluit.', lines=2, page=5, item=1),
    discuss('Ons praat', 'Bespreek hierdie vrae met ’n maat.', points=['Hoe het Charl gevoel toe hy nie een van die aktiwiteite kon regkry nie?', 'Het jy al ooit so gevoel?',
            'Hoe het Charl gevoel toe hy besef dat hy ’n talentvolle tuinier is?'], page=5, item='Ons praat'),
    writing('Ons skryf: Dagboekinskrywing', 'Maak asof jy Charl is en skryf ’n dagboekinskrywing waarin jy opsom hoe jy gevoel het toe jy ontdek het dat jy tog ’n talent het.',
            checklist=['Ek het die datum bo-aan geskryf.', 'Ek het in die eerste persoon (“ek”) vertel.', 'Ek het die gebeure in die korrekte volgorde vertel.',
                       'Ek het saamgestelde sinne gebruik.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=10, page=5, item='Ons skryf'),
    fill('Vul die woord in', 'Charl stap met {{1}} terug huis toe, want hy voel {{2}}.', {1: 'hangskouers', 2: ['moedeloos', 'teleurgesteld']},
         'Hangskouers wys dat jy teleurgesteld of moedeloos voel.', bank=['hangskouers', 'moedeloos', 'solo']),
    tf('Waar of onwaar?', 'Charl het die oudisie vir die sanggroep gewen.', False, 'Sy stem het begin kraak en een van die beoordelaars het ’n skewe gesig getrek – Charl het geweet hy sal nie gekies word nie.'),
    order('Sit die gebeure in volgorde', 'Sit hierdie gebeure in die volgorde waarin hulle in die storie gebeur het.',
          ['Charl sien ’n pamflet oor ’n nuwe sanggroep.', 'Charl se stem kraak by die oudisie.', 'Charl stap met hangskouers huis toe.', 'Jan sê Charl se groente is groot en smaaklik.', 'Charl nooi sy maats vir aandete.'],
          'Die storie vertel die gebeure in die volgorde van die tyd.'),
  ],
  quiz=[
    q('inference', 'Wat het Jan vir Charl aan die einde van die storie help besef?', 'Dat daar reeds iets is wat hy goed doen.',
      ['Dat hy goed sokker speel.', 'Dat tuinmaak harde werk is.', 'Dat sy maats meer talentvol is as hy.'], 'Jan bewonder Charl se groente en help hom so besef dat tuinmaak sy talent is.', ev=['Kyk hoe groot is die groente'], src='workbook', page=4, item='A'),
    q('inference', 'Waarom het Charl sy vriende oorgenooi vir aandete?', 'Om sy talent asook hulle s’n te vier.',
      ['Om die einde van die somer te vier.', 'Om sokker te speel.', 'Om hulle te leer hoe om tuin te maak.'], 'Charl vier Dingani se oorwinning met groente uit sy tuin en gaan na Jan se konsert.', ev=['Waarom kom julle nie albei'], src='workbook', page=4, item='B'),
    q('literal', 'Wat het gebeur toe Charl by die oudisie gesing het?', 'Sy stem het begin kraak en piep.',
      ['Hy het die solo gekry.', 'Hy het die liedjie vergeet.', 'Hy is dadelik gekies.'], 'Die beoordelaar het ’n skewe gesig getrek en Charl het geweet hy sal nie gekies word nie.', ev=['begin sy stem te kraak', 'skewe gesig']),
    q('literal', 'Wie het die groot sokkertoernooi gewen?', 'Dingani se span', ['Jan se koor', 'Charl se span', 'Niemand nie'], 'Dingani antwoord: “Ons het gewen!”', ev=['Ons het gewen']),
    q('vocabulary', 'Wat beteken “hangskouers” in die sin “Charl stap met hangskouers terug huis toe”?', 'teleurgesteld en moedeloos',
      ['bly en trots', 'kwaad en vol selfvertroue', 'baie moeg van die sokker'], 'Skouers wat hang, wys dat iemand teleurgesteld is.', ev=['hangskouers']),
    q('inference', 'Waarom sê Jan: “Ek wens ek het jou hand met ’n plant gehad”?', 'Hy bewonder Charl se vermoë om plante te kweek.',
      ['Hy hou nie van groente nie.', 'Hy wil Charl se tuin koop.', 'Hy is kwaad vir Charl.'], 'Jan se plante gaan dood, terwyl Charl se groente groot en gesond is – Jan bewonder dit.', ev=['jou hand met ’n plant']),
    q('main_idea', 'Wat is die hoofgedagte van die hele storie?', 'Elkeen het ’n talent, al sien jy dit nie dadelik nie.',
      ['Sokker is beter as sing.', 'Groente kweek is maklik.', 'Die skoolvakansie is vervelig.'], 'Charl dink hy het geen talent nie, maar hy is baie goed met plante.', ev=['nooit aan tuinmaak'], status='needs_review'),
    q('sequencing', 'Wat het EERSTE in hierdie deel van die storie gebeur?', 'Charl het by die sanggroep se oudisie gaan sing.',
      ['Charl het sy maats vir aandete genooi.', 'Jan het gesê Charl se groente is groot.', 'Dingani het gesê sy span het gewen.'], 'Die deel begin met die pamflet en die oudisie.', ev=['pamflet']),
    q('literal', 'Wat gaan Jan môre doen?', 'Hy gaan ’n solo by die konsert sing.', ['Hy gaan sokker speel.', 'Hy gaan groente plant.', 'Hy gaan na ’n oudisie gaan.'],
      'Jan sê: “Dit vind môre plaas … en ek gaan ’n solo sing!”', ev=['gaan ’n solo sing']),
  ])

# ============================================================== 67 Ons skryf 'n verslag
L67 = lesson(67,
  intro='Vandag word jy ’n verslaggewer! Jy beplan en skryf ’n koerantberig oor Charl se storie.',
  objectives=['Beplan ’n koerantberig met die vrae wie, waar, wanneer en wat.', 'Die hoofgedagte en die probleem van ’n storie uitwys.',
              'Gebeure in die korrekte (chronologiese) volgorde plaas.', 'Skryf ’n verslag (koerantberig) oor die Julievakansie.'],
  learn=[
    text('Wat staan in ’n koerantberig?', bullets=['die naam van die koerant', 'die opskrif van die verslag', 'die verslaggewer (jou naam) en die datum', 'wie die hoofkarakters is',
                                                    'waar en wanneer dit gebeur het', 'die gebeure in chronologiese (tyd-)volgorde'], page=7),
    text('Beplan met vrae', bullets=['Wat is die titel van die storie?', 'Wie is die hoofkarakters?', 'Waar speel die storie hom af?', 'Wanneer speel die storie af?',
                                                   'Wat is die probleem in die storie?', 'Word die gebeure in chronologiese volgorde beskryf?'], page=6),
    text('Die skryfproses', bullets=['**Beplan** jou verslag deur die vrae te beantwoord.', '**Skryf** jou eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk **hersien**.',
                                      '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** op bladsy 7.'], page=6),
  ],
  acts=[
    discuss('Ons praat', 'Kyk weer na die storie van “Die Seun wat sy Talent gaan Soek het” en bespreek hierdie vrae met ’n maat.',
            points=['Wat is die titel van die storie?', 'Wie is die hoofkarakters?', 'Waar speel die storie hom af?', 'Wanneer speel die storie af?', 'Wat is die probleem in die storie?',
                    'Word die gebeure in chronologiese volgorde beskryf?'], page=6, item='Ons praat'),
    sa('Beplan: Hoofkarakters', 'Wie is die hoofkarakters?', 'Charl, Dingani en Jan.', lines=1, page=6, item=1),
    sa('Beplan: Waar en wanneer', 'Waar en wanneer speel die gebeure hulle af?', 'In Limpopo, tydens die Julievakansie van 2015.', lines=2, page=6, item=2),
    sa('Beplan: Hoofgedagte en probleem', 'Wat is die hoofgedagte en die probleem van die storie?',
       'Probleem: Charl dink hy het geen spesiale talent soos sy maats nie. Hoofgedagte: Elkeen het ’n talent; jy moet net ontdek wat joune is.', lines=3, page=6, item=3, status='needs_review'),
    order('Plaas die gebeure in die korrekte volgorde', 'Nommer die sinne van 1 tot 6: sit hulle in die volgorde waarin die gebeure plaasgevind het.',
          ['Gedurende die Julievakansie werk Charl in die gemeenskapstuin.', 'Hy gesels met Dingani en probeer sokker speel, maar hy vaar nie goed nie.', 'Charl voel moedeloos omdat hy geen spesiale talent het nie.',
           'Later praat hy met Jan en word hy gemotiveer om aan oudisies vir ’n sanggroep deel te neem. Hy slaag egter ook nie daarin nie.',
           'Jan wys Charl daarop dat hy wel ’n spesiale talent het – die vermoë om buitengewone groente en vrugte te kweek.', 'Die drie seuns vier hulle talente en suksesse tydens ’n aandete.'],
          'Volg die storie van die begin (die vakansie begin) tot die einde (die aandete).', perm=[2, 4, 0, 5, 1, 3], src='workbook', page=6, item='Ons doen', status='derived_from_text'),
    sa('Wat noem ons ’n verslaggewer?', 'Wat noem ons ’n persoon wat koerantberigte skryf? Gee ook ’n sinoniem vir die woord.', 'verslaggewer / joernalis', lines=1, page=6, item=4, status='official'),
    sa('Jou opskrif', 'Wat gaan die opskrif van jou verslag (koerantberig) wees?', None, lines=1, page=6, item=5),
    writing('Skryf jou verslag', 'Skryf nou jou verslag (koerantberig) oor die gebeure van die Julievakansie.',
            checklist=['Ek het die naam van die koerant neergeskryf.', 'Ek het ’n opskrif geskryf.', 'Ek het my naam as verslaggewer en die datum bygevoeg.', 'Ek sê wie, waar en wanneer.',
                       'Ek vertel die gebeure in chronologiese volgorde.', 'Ek het my spelling en punktuasie gekorrigeer.'], tips=WRITE_PROCESS, lines=14, page=7, item='Skryf jou verslag'),
    tf('Waar of onwaar?', 'In ’n koerantberig vertel jy die gebeure deurmekaar, sonder volgorde.', False, 'Gebeure word in chronologiese volgorde vertel: eers wat eerste gebeur het, dan wat daarna gebeur het.', status='derived_from_rule'),
    fill('Voltooi die sin', 'Die persoon wat ’n koerantberig skryf, word ’n {{1}} of ’n {{2}} genoem.', {1: ['verslaggewer', 'joernalis'], 2: ['joernalis', 'verslaggewer']},
         'Albei woorde beteken dieselfde – hulle is sinonieme.', bank=['verslaggewer', 'joernalis', 'digter'], status='official'),
    choices('Wat hoort in ’n koerantberig?', 'Kies vir elke ding of dit in ’n koerantberig hoort.',
            [('’n Opskrif', ['Ja', 'Nee'], 0), ('Die naam van die verslaggewer', ['Ja', 'Nee'], 0), ('’n Gedig met rym', ['Ja', 'Nee'], 1), ('Wie, waar en wanneer', ['Ja', 'Nee'], 0), ('Gebeure in tydvolgorde', ['Ja', 'Nee'], 0)],
            '’n Koerantberig het ’n opskrif, ’n verslaggewer en feite oor wie, waar en wanneer – in volgorde vertel.', status='derived_from_rule'),
  ],
  quiz=[
    q('vocabulary', 'Wat noem ons ’n persoon wat koerantberigte skryf?', '’n verslaggewer (joernalis)', ['’n digter', '’n storieverteller', '’n drukker'], 'Die werkboek gee die antwoord: verslaggewer/joernalis.', src='workbook', status='official', page=6, item=4),
    q('sequencing', 'Watter gebeurtenis kom EERSTE in Charl se storie?', 'Charl werk in die gemeenskapstuin.', ['Charl en Jan vier hulle talente.', 'Jan sê Charl het ’n talent.', 'Charl gaan na die oudisie.'], 'Die vakansie begin en Charl werk in die tuin.', status='derived_from_text'),
    q('sequencing', 'Watter gebeurtenis kom LAASTE in die storie?', 'Die drie seuns vier hulle talente tydens ’n aandete.', ['Charl probeer sokker speel.', 'Charl gaan na ’n oudisie.', 'Jan wys Charl op sy talent.'], 'Die storie eindig met die aandete.', status='derived_from_text'),
    q('literal', 'Wie is die drie hoofkarakters in die storie?', 'Charl, Dingani en Jan', ['Charl, Tumi en Jan', 'Dingani, Jan en Pieter', 'Charl, Sipho en Dingani'], 'Die storie gaan oor Charl en sy maats Dingani en Jan.', status='derived_from_text'),
    q('main_idea', 'Wat is die probleem in Charl se storie?', 'Hy dink hy het geen spesiale talent nie.', ['Hy het nie ’n sokkerbal nie.', 'Hy kan nie in die tuin werk nie.', 'Hy het geen maats nie.'], 'Charl voel moedeloos omdat sy maats talente het en hy nie dink hy het een nie.', status='needs_review'),
    q('literal', 'Waar en wanneer speel Charl se storie af?', 'In Limpopo, tydens die Julievakansie', ['In die Wes-Kaap, tydens Kersfees', 'In Gauteng, in die winter', 'By die skool, in Maart'], 'Die storie noem Julie 2015 en dat Charl in Limpopo woon.', status='derived_from_text'),
    q('vocabulary', 'Wat is ’n chronologiese volgorde?', 'Die gebeure in die volgorde waarin hulle gebeur het', ['Die gebeure deurmekaar', 'Net die belangrikste gebeure', 'Net die laaste gebeurtenis'], 'Chronologies beteken in tydvolgorde.', status='derived_from_rule'),
    q('literal', 'Watter inligting hoort NIE in ’n koerantberig nie?', '’n Rympie vir jou maat', ['Die opskrif', 'Die verslaggewer se naam', 'Die datum'], '’n Koerantberig bevat opskrif, verslaggewer, datum en feite – nie ’n rympie nie.', status='derived_from_rule'),
  ])

