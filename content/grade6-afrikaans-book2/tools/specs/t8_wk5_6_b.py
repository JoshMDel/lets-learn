import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

FIG = '/workbook/gr6-afr-b2/figures/'

# ============================================================== 117 Die kinders gaan kampeer
P117 = [
  'Vusi loop net agter sy maat Kallie, wat besig is om die tent se ritssluiter oop te maak. Vusi wip soos hy skrik toe sy maat ’n bloedstollende gil uiter, en hy bots met Bongi, wat agter hom staan.',
  '“S ... s ... slang!” skree Kallie terwyl hy vinnig retireer.',
  'Vusi se pa, mnr. Mosoma, kom van die kampvuur af aangehardloop. “Hoe seker is jy dis ’n slang?” vra hy met ’n onderdrukte glimlag terwyl hy na die drie bewende kinders kyk.',
  '“Sy tong flits in en uit, Pa, en hy lyk soos ’n yslike akkedis!” hyg Vusi.',
  '“Wag julle almal asseblief net hier terwyl ek die flits gaan haal. Dalk is dit nie ’n slang nie.”',
  'Bongi raak aan Kallie se skouer. “Hoe kan dit nie ’n slang wees nie? Weet julle van enige ander dier wie se tong uit sy mond uitskiet?” vra sy. Kallie en Vusi skud hul koppe. Hulle het nie ’n verduideliking nie.',
  'Mnr. Mosoma keer terug met ’n flits in die hand en ’n graaf in die ander. Hy roep vir Vusi na hom toe. “Vusi, ek het die graaf gebring net om hom van ons weg te hou, nie om hom seer te maak nie,” sê hy. “Hou jy net asseblief vir my die flits vas.”',
  '“Hoekom ek, Pa?” vra Vusi met ’n klein stemmetjie. “Moenie bekommerd wees nie,” sê sy pa, “ek sal voor stap.”',
  'Mnr. Mosoma lig die tentflap met een hand op, en Vusi lig met die flits in die tent in. Die ander twee kinders kom ook ’n bietjie nader, maar hulle sorg dat hulle op ’n veilige afstand van die tent af bly.',
  '“Ja, dis soos ek gedink het,” brom mnr. Mosoma terwyl hy na die kinders draai. “’n Veldlikkewaan. Maar hoe het hy hier ingekom? Het ek nie gesê julle moet die tentvloer aan die sykante vasmaak nie?”',
  'Vusi kyk na sy tekkies en die ander twee kyk met ’n skouerophaling na mekaar. Soos gewoonlik was hulle die oggend te haastig. Vusi besluit dit is tyd om die onderwerp te verander. “Wat is ’n veldlikkewaan, Pa? Kan hy byt of spoeg?”',
  'Bongi is gefassineer deur die voorkoms van die reuseakkedis. In die flits se lig word ’n patroon van wit blokkies op sy skubberige swart vel duidelik. Hy het lang, swart naels aan al vier beplooide pote. Sy wip toe die dier ’n harde sisgeluid maak.',
  '“Pasop, kinders, moenie met hom skoorsoek nie. As hy jou byt, laat hy nie sommer weer los nie,” sê mnr. Mosoma. “Jek!” brom Kallie terwyl hy verder uit die ligkring retireer.']
G117 = [('ritssluiter', 'Die toemaakding met tandjies aan ’n tent of klere.'), ('retireer', 'Agteruit beweeg; terugtrek.'), ('onderdrukte', 'Probeer wegsteek; nie heeltemal gewys nie.'), ('yslike', 'Baie groot.'), ('skoorsoek', 'Moeilikheid soek.'), ('veldlikkewaan', '’n Groot reptiel met ’n lang tong wat in Afrika voorkom.'), ('gefassineer', 'Baie belangstellend; jy kan nie ophou kyk nie.'), ('beplooide', 'Met plooie (soos ou, ronde vel).')]

L117 = lesson(117,
  skills=[READ, LANG],
  intro='Iets kruip in die tent! Lees hoe Vusi, Kallie en Bongi vir ’n skrikgeleentheid te staan kom, en soek sinonieme in die storie.',
  objectives=['’n Fiktiewe teks lees en verstaan.', 'Vrae oor die teks beantwoord.', 'Sinonieme vir woorde en frases uit die teks opspoor.'],
  pass_=passage('Die kinders gaan kampeer', P117, glossary=G117),
  learn=[
    note('**Sinonieme** is woorde met min of meer dieselfde betekenis, soos praat en gesels.', title='Sinonieme', page=111),
  ],
  acts=[
    discuss('Ons praat', 'Bespreek: Wat is die groot verskil tussen soogdiere en reptiele? Hoeveel reptiele kan jy opnoem? Indien jy ’n onverwagte ontmoeting met ’n reptiel gehad het, vertel die klas daarvan.', page=110, item='Ons praat'),
    match('Sinonieme in die storie', 'Lees die storie weer. Verbind elke woord of frase met ’n sinoniem uit die storie.', [('agteruit beweeg', 'retireer'), ('enorme', 'yslike'), ('mompel', 'brom'), ('moeilikheid soek', 'skoorsoek'), ('skree', 'gil')], 'Die storie gebruik retireer, yslike, brom en skoorsoek vir die eerste vier; vir “skree” kan ’n mens “gil” gebruik.', src='workbook', page=111, item='Ons skryf', status='needs_review'),
    choices('Is dit waar volgens die storie?', 'Lees die sinne en kies reg of verkeerd.', [('Kallie skree “slang!”.', ['reg', 'verkeerd'], 0), ('Mnr. Mosoma haal ’n graaf en ’n flits.', ['reg', 'verkeerd'], 0), ('Die tentvloer was aan die sykante vasgemaak.', ['reg', 'verkeerd'], 1), ('Die likkewaan het ’n patroon van wit blokkies op sy vel.', ['reg', 'verkeerd'], 0)],
            'Die tentvloer was nie vasgemaak nie – dit is hoe die likkewaan ingekom het.', src='supplementary', status='derived_from_text'),
    sa('Wat het jy geleer?', 'Skryf een ding wat jy uit die storie geleer het oor veldlikkewane.', 'Veldlikkewane het skubberige swart vel met wit blokkies, lang naels, sis en byt; hulle laat nie maklik los nie.', lines=3, page=111, item='geleer', status='needs_review'),
  ],
  quiz=[
    q('literal', 'Wie gil toe die tent oopgemaak word?', 'Kallie', ['Bongi', 'Mnr. Mosoma', 'Vusi'], 'Kallie uiter ’n bloedstollende gil.', ev=['Kallie']),
    q('literal', 'Waarmee bots Vusi?', 'Met Bongi', ['Met Kallie', 'Met sy pa', 'Met die tent'], 'Vusi bots met Bongi.', ev=['bots met Bongi']),
    q('literal', 'Wat dink die kinders is in die tent?', '’n Slang', ['’n Hond', '’n Hiëna', '’n Rooibok'], 'Kallie skree “slang!”.', ev=['slang']),
    q('literal', 'Wat bring mnr. Mosoma saam?', '’n Flits en ’n graaf', ['’n Gewere en ’n tou', '’n Emmer en water', '’n Kamera'], 'Hy keer terug met ’n flits en ’n graaf.', ev=['flits in die hand en ’n graaf']),
    q('literal', 'Wat was in die tent?', '’n Veldlikkewaan', ['’n Slang', '’n Krokodil', '’n Muis'], 'Mnr. Mosoma sê: “’n Veldlikkewaan”.', ev=['Veldlikkewaan']),
    q('inference', 'Hoe het die likkewaan in die tent ingekom?', 'Die tentvloer was nie aan die sykante vasgemaak nie', ['Hy het ’n gat gebyt', 'Die tent was oop', 'Kallie het hom ingelaat'], 'Mnr. Mosoma vra of hulle nie die tentvloer moes vasmaak nie.', ev=['tentvloer aan die sykante vasmaak']),
    q('inference', 'Hoe weet ons Vusi probeer die onderwerp verander?', 'Hy vra “Wat is ’n veldlikkewaan, Pa?”', ['Hy loop weg', 'Hy lag', 'Hy sê niks'], 'Hy verander die onderwerp met ’n vraag.', ev=['dit is tyd om die onderwerp te verander']),
    q('vocabulary', 'Wat beteken “skoorsoek”?', 'Moeilikheid soek', ['Hardloop', 'Skree', 'Loop'], 'Mnr. Mosoma sê: “moenie met hom skoorsoek nie”.', ev=['moenie met hom skoorsoek nie']),
  ])

# ============================================================== 118 'n Veldavontuur
L118 = lesson(118,
  skills=[READ, WRITE, LANG],
  intro='Terug by die veldlikkewaan! Beantwoord vrae oor die storie, leer oor oorsaak en gevolg en skryf vier paragrawe oor ’n kampeerervaring.',
  objectives=['Vrae oor die storie beantwoord.', 'Oorsake met hul gevolge verbind en voegwoorde gebruik.', 'Vier paragrawe oor ’n kampeerervaring skryf.'],
  learn=[
    text('Oorsaak en gevolg', 'Baiekeer wil ons oor die oorsaak en gevolg van iets praat. Om dit te kan doen, gebruik ons woorde soos **omdat**, **daarom**, **want** of **dus**.', bullets=['Die kinders het nie die tentvloer vasgemaak nie, **daarom** het die likkewaan ingekom. (oorsaak → gevolg)', 'Die likkewaan het ingekom, **omdat** die tentvloer nie vasgemaak was nie. (gevolg ← oorsaak)'], page=112),
  ],
  acts=[
    order('In watter volgorde loop die kinders na die tent toe?', 'Sit die kinders in die volgorde waarin hulle loop: 1ste, 2de, 3de.', ['Kallie', 'Vusi', 'Bongi'], 'Vusi loop net agter Kallie en Bongi staan agter Vusi.', perm=[1, 2, 0], src='workbook', page=112, item='1', status='derived_from_text'),
    sa('Dink jy Vusi het al ooit ’n veldlikkewaan gesien?', 'Dink jy Vusi het al ooit ’n veldlikkewaan gesien? Waarom sê jy so?', 'Nee, waarskynlik nie, want hy vra: “Wat is ’n veldlikkewaan, Pa?” en hy dink eers dis ’n akkedis/slang.', lines=3, page=112, item='2', status='needs_review'),
    sa('Waarom bots Vusi met Bongi?', 'Waarom bots Vusi met Bongi?', 'Omdat hy skrik toe Kallie ’n bloedstollende gil uiter, en Bongi agter hom staan.', lines=2, page=112, item='3', status='derived_from_text'),
    sa('Is mnr. Mosoma bang vir reptiele?', 'Is mnr. Mosoma bang vir reptiele? Gee redes vir jou antwoord.', 'Nee. Hy glimlag, bly kalm, haal ’n flits en graaf, stap voor en lig self die tentflap op.', lines=3, page=112, item='4', status='needs_review'),
    sa('Hoe weet ons die kinders is bang?', 'Hoe weet ons die kinders is bang vir reptiele?', 'Hulle is bewend, Kallie skree en retireer, hulle bly op ’n veilige afstand en Kallie sê “Jek!”.', lines=3, page=112, item='5', status='needs_review'),
    sa('Hoe het die likkewaan ingekom?', 'Hoe het die likkewaan in die tent ingekom?', 'Die kinders het die tentvloer aan die sykante nie vasgemaak nie.', lines=2, page=112, item='6', status='derived_from_text'),
    match('Oorsaak en gevolg', 'Verbind elke oorsaak met sy gevolg.', [('Die kinders het die tentvloer nie vasgemaak nie.', 'Die likkewaan het in die tent ingekom.'), ('Mnr. Mosoma wou ’n flitslig hê.', 'Hy het na die motor toe gegaan.'), ('Kallie het gedink hy sien ’n slang.', 'Hy het ’n groot tree agteruit gegee.'), ('Die likkewaan het vasgekeer gevoel.', 'Hy het sisgeluide gemaak en sy tong in en uit beweeg.')],
          'Die storie gee die oorsake; die gevolge staan regs.', src='workbook', page=112, item='oorsaak-gevolg', status='derived_from_text'),
    writing('Skryf saamgestelde sinne', 'Skryf die sinne wat jy verbind het oor as een saamgestelde sin met omdat, daarom, want of dus.', checklist=['Ek het omdat/daarom/want/dus gebruik.', 'Elke sin maak sin.'], lines=6, page=113, item='saamgestelde sinne'),
    writing('My kampervaring: beplan en skryf', 'Skryf vier paragrawe oor ’n keer toe jy gaan kamp het. (As jy nog nooit gaan kamp het nie, skryf hoe jy jou dit voorstel.) Paragraaf 1: waar is die kampeerplek en hoe lyk dit? Paragraaf 2: ’n onverwagte gebeurtenis. Paragraaf 3: hoe die gebeurtenis hanteer is. Paragraaf 4: die oplossing van die gebeurtenis. Woorde wat kan help: tent, graaf, emmer, water, hout, vuur, driebeenpot, muskiete, boom, rooibok, reptiel, hiëna, alleen, bang, krieke, grondpaaie, wildpark, plaas, band, vars lug, voëls, kwetter.',
            checklist=['Paragraaf 1: waar is die kampeerplek en hoe lyk dit?', 'Paragraaf 2: ’n onverwagte gebeurtenis', 'Paragraaf 3: hoe die gebeurtenis hanteer is', 'Paragraaf 4: die oplossing', 'Ek het ’n maat my werk laat hersien.', 'Ek het gekorrigeer en netjies oorgeskryf.'], lines=16, page=113, item='My kampervaring'),
    tf('Waar of onwaar?', '“Want” kan ’n oorsaak aandui, bv. Kallie het agteruit gegee, want hy het gedink hy sien ’n slang.', True, 'Voegwoorde soos want, omdat, daarom en dus verbind oorsaak en gevolg.', src='supplementary', status='derived_from_rule'),
  ],
  quiz=[
    q('sequencing', 'Wie loop eerste na die tent toe?', 'Kallie', ['Vusi', 'Bongi', 'Mnr. Mosoma'], 'Vusi loop net agter Kallie.', status='derived_from_text', src='workbook', page=112, item='1'),
    q('inference', 'Waarom bots Vusi met Bongi?', 'Omdat hy skrik toe Kallie gil', ['Omdat hy hardloop', 'Omdat hy kwaad is', 'Omdat dit donker is'], 'Hy skrik en bots met Bongi, wat agter hom staan.', status='derived_from_text', src='workbook', page=112, item='3'),
    q('inference', 'Hoe het die likkewaan in die tent ingekom?', 'Die tentvloer was nie vasgemaak nie', ['Hy het oor die tent geklim', 'Iemand het hom ingedra', 'Die tent was oop'], 'Mnr. Mosoma sê hulle moes die tentvloer vasmaak.', status='derived_from_text', src='workbook', page=112, item='6'),
    q('grammar', 'Watter woord dui ’n oorsaak aan?', 'omdat', ['maar', 'en', 'of'], 'Die werkboek noem omdat, daarom, want en dus.', status='official', src='workbook', page=112),
    q('grammar', 'Kies die korrekte sin.', 'Hy het agteruit gegee, want hy het gedink hy sien ’n slang.', ['Hy het agteruit gegee, maar hy het gedink hy sien ’n slang.', 'Hy het agteruit gegee, of hy het gedink hy sien ’n slang.', 'Hy het agteruit gegee, en hy het gedink hy sien ’n slang.'], '“Want” gee die rede.', status='derived_from_rule', src='supplementary'),
    q('main_idea', 'Hoeveel paragrawe skryf jy oor jou kampeerervaring?', 'Vier', ['Een', 'Twee', 'Tien'], 'Skryf vier paragrawe.', status='official', src='workbook', page=113),
    q('main_idea', 'Wat skryf jy in paragraaf 2?', '’n Onverwagte gebeurtenis', ['Waar die kampeerplek is', 'Die oplossing', 'Jou naam'], 'Paragraaf 2 is ’n onverwagte gebeurtenis.', status='official', src='workbook', page=113),
    q('main_idea', 'Watter paragraaf skryf oor die oplossing van die gebeurtenis?', 'Paragraaf 4', ['Paragraaf 1', 'Paragraaf 2', 'Paragraaf 3'], 'Paragraaf 4 is die oplossing.', status='official', src='workbook', page=113),
  ])

# ============================================================== 119 Blindheid het my nie gekeer nie
P119 = [
  'Ek is in 1967 op ’n plattelandse dorpie in Venda, in die Limpopoprovinsie, gebore. Op die ouderdom van ses het ek masels gekry – ’n alledaagse kindersiekte. Ek was ongelukkig – daar was komplikasies en ek het blind geword. Ek het hopeloos, magteloos en verlore gevoel. Hoe kon ek ooit met my lewe voortgaan?',
  'In 1973 het my ouers my by die Boseleskool vir Blindes ingeskryf. Daar het ek geleer om Braille te lees. Ek het die gehalte-onderrig wat ek daar ontvang het, ten volle benut. Ek het besef ek moet goed vaar in matriek. Skoolkinders besef nie altyd hoe belangrik dit is om hard te werk op skool nie, en dan kry hulle later in hulle lewens baie spyt.',
  'Na skool, in 1987, het ek aan die Universiteit van die Noorde in Limpopo gaan studeer, en in 1991 het ek nagraadse studie aan die Universiteit van die Witwatersrand in Johannesburg aangepak. Ek wou aanvanklik ’n prokureur word. My ouma wou egter hê dat ek ’n onderwyser moes word. Sy was reg, want dit is eintlik my voorliefde.',
  'In 1997 het ek ’n Fullbright-beurs ontvang. Dit het beteken dat ek Amerika toe kon gaan om ’n meestersgraad aan die Bostonse Kollege te verwerf. Ek was in die wolke. Ek, Obert Maguvhe, op ’n vliegtuig op pad na ’n plek wat baie ver weg was van my huis op ’n plattelandse dorpie in Venda! Die volgende stop sou Amerika wees! Ek kon my dit nie indink nie. Maar ek het op die vliegtuig geklim en die reis aangepak. In die VSA het ek alleen gewoon, en die tweejaarprogram binne slegs twaalf maande afgehandel. My professore het gedink ek is ’n uitsonderlike student en ek kon ’n hele jaar vroeër huis toe kom as wat ons almal verwag het.',
  'Sewe jaar nadat ek van die VSA teruggekeer het, het ek my doktorsgraad aan die Universiteit van Pretoria verwerf. Enigiets is moontlik as jy in jouself glo en bereid is om hard te werk.',
  'Niks is onmoontlik nie! Iets wat my gehelp het om van jongs af in myself te glo, was die feit dat my pa van my verwag het om alles te doen wat siende kinders kon doen, soos om die beeste en bokke op te pas en onkruid in ons mielieland uit te trek. Snaaks genoeg, my beste vriend by Vhufuli was ’n dowe seun. Alhoewel ons nie vingertaal kon gebruik om te kommunikeer nie, het ons mekaar verstaan en het ons saam gespeel soos alle ander kinders. Ons het diere en voëls gemaak van klei, ons het geswem, ons het die bokke gemelk en boom geklim. Al kon ek nie sien nie en kon my maat nie hoor nie, het dit nooit by my opgekom dat hierdie dinge ons enigsins minderwaardig maak nie.',
  'In 2008 het ek by die Department van Basiese Onderwys aangesluit om ’n afdeling van die Kha Ri Gude-geletterdheidsveldtog te lei. Die veldtog is daarop gemik om 3,5 miljoen Suid-Afrikaanse volwassenes te leer lees en skryf, en my afdeling is in beheer daarvan om blindes in Braille te leer lees. Ons kan nie ons oë gebruik om te lees nie, ons gebruik ons vingers!',
  'Ek was baie opgewonde toe ek in 2013 as Medeprofessor aan die Universiteit van Suid-Afrika aangestel is. In my nuwe pos word daar van my verwag om onderwysers op te lei om kinders met gestremdhede te onderrig. Dit is vir my wonderlik om ander mense te kan help.',
  'My boodskap aan elke jongmens is om alles te leer wat jy kan terwyl jy op skool is. Moenie toelaat dat moeilike tye of hartseer jou onderkry nie. Almal van ons verdien ons drome, en al wat dit verg om hulle te verwesenlik, is harde werk!']
G119 = [('outobiografie', '’n Storie wat iemand oor sy of haar eie lewe skryf.'), ('komplikasies', 'Moeilikhede wat by ’n siekte bykom.'), ('Braille', '’n Stelsel van opgehewe kolletjies waarmee blinde mense met hul vingers lees.'), ('nagraadse', 'Studie ná die eerste universiteitsgraad.'), ('beurs', 'Geld wat jy kry om te kan studeer.'), ('uitsonderlike', 'Besonder goed.'), ('geletterdheid', 'Die vermoë om te lees en te skryf.'), ('minderwaardig', 'Nie so goed soos ander nie.')]

L119 = lesson(119,
  skills=[READ, WRITE],
  intro='Dr. Obert Maguvhe het op sesjarige ouderdom blind geword – en tog het hy ’n professor geword! Lees sy outobiografie, stel ’n tydlyn op en leer jou naam in Braille skryf.',
  objectives=['’n Outobiografie lees en verstaan.', '’n Tydlyn van gebeure opstel.', 'Die boodskap van die skrywer verstaan.', 'Jou naam in Braille skryf.'],
  pass_=passage('Blindheid het my nie gekeer nie', P119, glossary=G119),
  learn=[
    note('’n **Outobiografie** is ’n storie wat iemand oor sy of haar eie lewe skryf. ’n **Biografie** word deur iemand anders geskryf. Obert het hierdie outobiografie spesiaal vir jou geskryf.', title='Outobiografie en biografie', page=115),
    text('Wat is Braille?', 'Braille is ’n stelsel wat deur blinde mense gebruik word om met hulle vingers te lees en skryf. Elke letter van die alfabet word verteenwoordig deur ’n patroon van opgehewe kolletjies wat hulle met hul vingerpunte kan voel en herken.', page=115),
    figure('Die Braille-alfabet', FIG + 'braille-alphabet.webp', 'Die Braille-alfabet: elke letter van A tot Z met sy patroon van kolletjies.', caption='Die tabel wys die kolletjiepatroon vir elke letter.', page=115),
  ],
  acts=[
    discuss('Ons praat', 'Bespreek: Het jy al ooit gevoel dat jy moed wil opgee – dat dinge net eenvoudig te moeilik raak? Het jy probleme wat jou aandag van jou skoolwerk aftrek?', page=114, item='Ons praat'),
    match('Obert se tydlyn', 'Verbind elke jaar met wat toe in Obert se lewe gebeur het.', [('1973', 'Hy gaan skool by die Boseleskool vir Blindes.'), ('1987', 'Hy studeer aan die Universiteit van die Noorde.'), ('1991', 'Hy doen nagraadse studie aan Wits.'), ('1997', 'Hy ontvang ’n Fullbright-beurs.'), ('2008', 'Hy sluit by die Kha Ri Gude-veldtog aan.'), ('2013', 'Hy word Medeprofessor aan Unisa.')], 'Die jaartalle en gebeure staan in die outobiografie.', src='workbook', page=115, item='tabel', status='derived_from_text'),
    sa('Die jaar 2004', 'Die tabel vra ook vir 2004. Wat het in daardie tydperk in Obert se lewe gebeur? (Werk self die jaartal uit.)', 'Hy het sy doktorsgraad aan die Universiteit van Pretoria verwerf (sewe jaar nadat hy uit die VSA teruggekeer het).', lines=2, page=115, item='2004', status='needs_review'),
    sa('Obert se boodskap', 'Watter spesiale boodskap het Obert vir alle jongmense?', 'Leer alles wat jy kan terwyl jy op skool is; moenie toelaat dat moeilike tye of hartseer jou onderkry nie; almal verdien hulle drome en harde werk bring dit.', lines=3, page=115, item='boodskap', status='derived_from_text'),
    discuss('Skryf jou naam in Braille', 'Skryf nou jou naam in Braille. Plaas die letters van jou naam in die onderste ry en die kolletjies vir elke letter in die boonste ry. Gebruik die Braille-alfabet hierbo. (Dit is ’n teken-/skryfaktiwiteit: werk in jou werkboek.)', page=115, item='Ons doen'),
    choices('Outobiografie of biografie?', 'Watter soort teks is dit?', [('Ek is in 1967 in Venda gebore.', ['outobiografie', 'biografie'], 0), ('Obert is in 1967 in Venda gebore.', ['outobiografie', 'biografie'], 1), ('Ek het my doktorsgraad verwerf.', ['outobiografie', 'biografie'], 0)],
            'In ’n outobiografie skryf iemand self oor sy of haar lewe (“ek”).', src='supplementary', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Obert het op die ouderdom van ses blind geword nadat hy masels gekry het.', True, 'Dit staan in die eerste paragraaf.', src='supplementary', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'In watter jaar is Obert gebore?', '1967', ['1973', '1987', '1997'], 'Hy is in 1967 gebore.', ev=['1967']),
    q('literal', 'Hoekom het Obert blind geword?', 'Hy het masels gekry en daar was komplikasies', ['Hy het ’n ongeluk gehad', 'Hy is blind gebore', 'Hy het te veel gelees'], 'Op ses het hy masels gekry met komplikasies.', ev=['masels gekry']),
    q('literal', 'Watter skool het Obert bygewoon?', 'Die Boseleskool vir Blindes', ['’n Gewone dorpskool', 'Wits', 'Universiteit van Pretoria'], 'Sy ouers het hom daar ingeskryf.', ev=['Boseleskool vir Blindes']),
    q('literal', 'Wat het Obert op skool geleer?', 'Om Braille te lees', ['Om vingertaal te gebruik', 'Om te sing', 'Om te swem'], 'Hy het geleer om Braille te lees.', ev=['Braille te lees']),
    q('literal', 'Watter beurs het Obert in 1997 ontvang?', '’n Fullbright-beurs', ['’n Sportbeurs', '’n Skoolbeurs', '’n Pretoriabeurs'], 'Dit het hom gehelp om Amerika toe te gaan.', ev=['Fullbright-beurs']),
    q('literal', 'Wat was Obert se beste vriend by Vhufuli?', '’n Dowe seun', ['’n Blinde meisie', '’n Onderwyser', '’n Hond'], 'Hy noem dat sy beste vriend ’n dowe seun was.', ev=['dowe seun']),
    q('inference', 'Wat is Obert se boodskap?', 'Leer alles wat jy kan en moenie opgee nie', ['Los skool vroeg', 'Wag vir hulp', 'Volg ander na'], 'Hy moedig jongmense aan om hard te werk.', ev=['alles te leer wat jy kan']),
    q('vocabulary', 'Wat is ’n outobiografie?', '’n Storie wat iemand oor sy of haar eie lewe skryf', ['’n Storie oor iemand anders', '’n Gedig', '’n Brief'], 'Dit staan in die blokkie op bladsy 115.', status='official', src='workbook', page=115),
  ])

# ============================================================== 120 Nog 'n kykie na taal
L120 = lesson(120,
  skills=[LANG],
  intro='Nog ’n kykie na taal: werkwoorde saam met die regte prentjies, vier soorte bywoorde en die intensiewe vorme van kleure.',
  objectives=['Werkwoorde by die regte woorde laat pas.', 'Vier soorte bywoorde uitken.', 'Intensiewe vorme van byvoeglike naamwoorde verbind en gebruik.'],
  learn=[
    text('Bywoorde', 'Bywoorde vertel ons meer van ander woorde. Daar word vier tipes onderskei:', bullets=['**Bywoorde van tyd:** wanneer en hoe dikwels iets gedoen word, bv. nou, vandag, nooit.', '**Bywoorde van wyse:** hoe iets gedoen word, bv. pragtig, grasieus, swak, duidelik.', '**Bywoorde van plek:** waar iets gedoen word, bv. bokant, onderkant, hier, daar, binnenshuis.', '**Bywoorde van graad:** hoeveel of hoe min iets gedoen word, bv. baie, genoeg, byna.'], page=117),
    note('**Intensiewe vorme** is byvoeglike naamwoorde waarmee ons meer gevoel as gewoonlik wil oordra, bv. bloedrooi.', title='Intensiewe vorme', page=117),
  ],
  acts=[
    match('Werkwoorde (1)', 'Verbind elke prentjie-frase met die werkwoord wat daarby pas. Elke werkwoord word net een keer gebruik.', [('’n fiets', 'ry'), ('na ’n teater', 'gaan'), ('televisie', 'kyk'), ('koffie', 'drink'), ('aandete', 'kook'), ('huiswerk', 'doen'), ('brille', 'dra'), ('blokkies', 'bou'), ('kitskos', 'eet')], 'Dink watter werkwoord ’n mens met elke ding gebruik.', src='workbook', page=116, item='prentjies', status='derived_from_rule'),
    match('Werkwoorde (2)', 'Verbind die res van die prentjie-frases met die werkwoorde.', [('tennis', 'speel'), ('die kersies uit', 'blaas'), ('na die radio', 'luister'), ('’n Volkswagen', 'bestuur'), ('in ’n woonstel', 'woon'), ('Duits', 'praat'), ('’n koerant', 'lees'), ('’n koek', 'bak'), ('van my hond', 'hou')], 'Elke werkwoord pas by net een prentjie-frase.', src='workbook', page=116, item='prentjies', status='derived_from_rule'),
    choices('Watter soort bywoord?', 'Dui die soort bywoord aan.', [('Jy moet daagliks jou huiswerk doen.', ['tyd', 'wyse', 'plek', 'graad'], 0), ('Ek voel baie tevrede met die gedig.', ['tyd', 'wyse', 'plek', 'graad'], 3), ('Sit jou boek daar op die tafel neer.', ['tyd', 'wyse', 'plek', 'graad'], 2), ('Skryf jou gedig netjies in jou boek.', ['tyd', 'wyse', 'plek', 'graad'], 1), ('Jy moet soggens vroeg genoeg opstaan.', ['tyd', 'wyse', 'plek', 'graad'], 0), ('Jy moet soggens vroeg genoeg opstaan.', ['tyd', 'wyse', 'plek', 'graad'], 3)],
            'Tyd = wanneer; wyse = hoe; plek = waar; graad = hoeveel.', src='workbook', page=117, item='bywoorde', status='derived_from_rule'),
    match('Intensiewe vorme', 'Verbind elke kleur met sy intensiewe vorm.', [('geel', 'goudgeel'), ('blou', 'potblou'), ('groen', 'grasgroen'), ('wit', 'spierwit')], 'Die intensiewe vorm sê hoe sterk of suiwer die kleur is.', src='workbook', page=117, item='intensiewe vorme', status='derived_from_text'),
    sa('Sinne met intensiewe vorme', 'Gebruik die intensiewe vorme in sinne.', 'Die gras was grasgroen.\nDie hemp was spierwit.\nDie lig was goudgeel.\nDie see was potblou.', lines=4, page=117, item='sinne', status='derived_from_rule'),
    tf('Waar of onwaar?', '“Nooit” is ’n bywoord van tyd.', True, 'Die werkboek gee “nooit” as voorbeeld van ’n bywoord van tyd.', src='workbook', page=117, item='feit', status='official'),
  ],
  quiz=[
    q('grammar', 'Watter soort bywoord is “nou”?', 'Tyd', ['Plek', 'Graad', 'Wyse'], 'Nou, vandag, nooit is bywoorde van tyd.', status='official', src='workbook', page=117),
    q('grammar', 'Watter soort bywoord is “pragtig”?', 'Wyse', ['Tyd', 'Plek', 'Graad'], 'Pragtig is ’n bywoord van wyse.', status='official', src='workbook', page=117),
    q('grammar', 'Watter soort bywoord is “binnenshuis”?', 'Plek', ['Tyd', 'Wyse', 'Graad'], 'Binnenshuis is ’n bywoord van plek.', status='official', src='workbook', page=117),
    q('grammar', 'Watter soort bywoord is “byna”?', 'Graad', ['Tyd', 'Wyse', 'Plek'], 'Byna is ’n bywoord van graad.', status='official', src='workbook', page=117),
    q('grammar', 'Wat is die intensiewe vorm van “wit”?', 'spierwit', ['grasgroen', 'goudgeel', 'potblou'], 'Spierwit is die sterk vorm van wit.', status='derived_from_text', src='workbook', page=117, item='intensiewe vorme'),
    q('grammar', 'Wat is die intensiewe vorm van “blou”?', 'potblou', ['spierwit', 'goudgeel', 'grasgroen'], 'Potblou is die sterk vorm van blou.', status='derived_from_text', src='workbook', page=117, item='intensiewe vorme'),
    q('grammar', 'Watter werkwoord pas by “televisie”?', 'kyk', ['eet', 'ry', 'bou'], 'Ons kyk televisie.', status='derived_from_rule', src='workbook', page=116, item='prentjies'),
    q('grammar', 'Wat is ’n intensiewe vorm?', '’n Byvoeglike naamwoord wat meer gevoel as gewoonlik oordra', ['’n Soort werkwoord', '’n Bywoord van tyd', '’n Voorsetsel'], 'Bv. bloedrooi.', status='official', src='workbook', page=117),
  ])
