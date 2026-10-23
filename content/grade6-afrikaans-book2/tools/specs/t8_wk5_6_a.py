import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

READ_STEPS = ['Kyk na die prente en opskrifte en probeer voorspel waaroor die teks handel.', 'Vluglees die bladsy om vinnig meer te wete te kom.', 'Kyk terwyl jy lees of jou voorspellings korrek was.', 'Lees dit weer stadig en hardop as jy ’n deel nie verstaan nie.']

# ============================================================== 113 Die biblioteekmonster
P113 = [
  '“Dis Boekeweek, kinders!” sê mevrou Roos. Tumi en die res van die klas sit regop, in hulle skik. Boekeweek beteken kompetisies en uitstappies na die biblioteek op die dorp – en baie stories.',
  '“Hierdie jaar se Boekeweektema is wilde diere,” sê mevrou Roos. “Ons gaan dus plakkate maak en stories skryf oor bedreigde spesies wat in gevaar verkeer om uit te sterf. Onthou julle dat ons verlede week hieroor gepraat het?” Sy wys na prente wat teen die muur opgesit is.',
  '“Sommige diere verkeer in gevaar omdat mense hulle jag vir hulle pels, ivoor of horings,” sê Tumi, wat altyd alles weet. “En soms sterf hulle uit omdat hulle nie die regte kos kan kry om te eet nie.”',
  '“Jy’s reg, Tumi,” sê mevrou Roos. “Dus, kinders,” gaan sy voort, “begin solank aan plakkate en stories oor hierdie soorte diere dink.”',
  'Sommige kinders in die klas teken luiperds en pelsdiere soos jakkalse. Party teken renosters en olifante, en ander teken die dodo en die kwagga. Maar die meeste van hulle – Tumi ook – teken die dinosourus. Nie enige dinosourus nie, maar ’n baie spesiale een – die iguanodon, waarvan hulle die vorige week geleer het.',
  'Tumi onthou die prentjie van die monster baie goed. Hy het twee kort voorbene en ’n kort, baie dik stert. Aan sy pote is vyf stomp tone. Hy het vyf vingers aan elke hand en ’n kort, horingagtige duim. Die iguanodon eet plante – en enigiets wat van plante gemaak is.',
  'Al die skole van die omgewing neem aan die dorpsbiblioteek se Boekeweek deel. Die afgelope weke het die kinders reeds plakkate geteken en geverf, en dit sal na die biblioteek gestuur word.',
  'Toe die dag aanbreek waarop die plakkate en stories by die biblioteek uitgestal gaan word, klim Tumi se klas in die bus en ry biblioteek toe. Dis ’n koue wintersdag en die wind waai.',
  'Toe hulle daar aankom, gaan hulle heel eerste hulle plakkate soek. “Hier’s myne!” sê Tumi. Op die plakkaat is ’n glimlaggende dinosourus met ’n blom in sy bek, om te wys dat hy plante eet. “Hier’s my storie oor die ysbeer!” sê Bongi. “En hier’s myne oor die renoster!” sê Christo trots.',
  'Toe al die kinders daar is, sê mevrou Botha, die bibliotekaresse, “Ek het vir julle ’n verrassing.”',
  'Die kinders gaan op die vloer sit en wonder wat die verrassing kan wees. Toe gaan die deur oop en ’n ysbeer met ’n pragtige laslaponderbaadjie kom ingestap, gevolg deur ’n leeu en ’n pandabeer. “Dis regte diere!” skree een kind. “Nee, nee,” sê ’n ander een. “Dis mense wat soos diere aangetrek is.”',
  'Die ysbeer doen ’n klein dansie en huppel heen en weer. Toe doen sy ’n rondte en groet al die kinders met die hand.']
G113 = [('in hulle skik', 'baie bly en opgewonde'), ('bedreigde spesies', 'Diere of plante wat in gevaar is om uit te sterf.'), ('uitsterf', 'Nie meer bestaan nie – almal van die soort is dood.'), ('ivoor', 'Die harde wit tand van ’n olifant.'), ('iguanodon', '’n Plantvretende dinosourus van baie lank gelede.'), ('uitgestal', 'Op ’n plek gesit sodat almal dit kan sien.'), ('bibliotekaresse', 'Die vrou wat in ’n biblioteek werk.'), ('verrassing', 'Iets onverwags en lekkers.')]

L113 = lesson(113,
  skills=[READ, LANG],
  intro='Dis Boekeweek by Tumi se skool! Lees ’n storie oor ’n spesiale verrassing in die biblioteek en leer hoe om hoofwerkwoorde en hulpwerkwoorde te herken.',
  objectives=['’n Fiktiewe teks lees en verstaan.', 'Vooruit voorspel en vluglees as leesstrategie gebruik.', 'Hoofwerkwoorde en hulpwerkwoorde uitken.', 'Vrae oor die teks bespreek.'],
  pass_=passage('Die biblioteekmonster', P113, glossary=G113),
  learn=[
    text('Voordat en terwyl jy lees', bullets=READ_STEPS, page=102),
    note('**Werkwoorde** is die aksie- of doenwoorde in ’n sin. **Hulpwerkwoorde** (bv. het, sal, moet, kan, mag, sou, moes, wou, kon) help ons om meer omtrent die werkwoord te sê. Die **hoofwerkwoord** sê wat gebeur.', title='Werkwoorde', src='supplementary', page=103),
  ],
  acts=[
    discuss('Bespreek die storie', 'Bespreek hierdie vrae: Het julle ’n Boekeweek by julle skool of op julle dorp? Hoe werk dit? / Tumi het twee redes gegee waarom diere uitsterf. Noem hulle. / Het die dodo en die kwagga reeds uitgesterf, of is hulle nog bedreigde spesies? / Van watter aspek van Boekeweek hou Tumi die meeste? / Watter soort dinosourus het die kinders reeds geken? / Is die leeu ’n bedreigde spesie? Motiveer jou antwoord. / Wat beteken die vetgedrukte woorde?', page=103, item='Ons praat'),
    choices('Hoofwerkwoord of hulpwerkwoord?', 'Dui aan wat die gemerkte woord in die sin is.', [('Ons gaan plakkate maak. (gaan)', ['hoofwerkwoord', 'hulpwerkwoord'], 1), ('Ons gaan plakkate maak. (maak)', ['hoofwerkwoord', 'hulpwerkwoord'], 0), ('Die kinders het plakkate geteken. (het)', ['hoofwerkwoord', 'hulpwerkwoord'], 1), ('Die kinders het plakkate geteken. (geteken)', ['hoofwerkwoord', 'hulpwerkwoord'], 0), ('Die plakkate sal na die biblioteek gestuur word. (sal)', ['hoofwerkwoord', 'hulpwerkwoord'], 1)],
            'Die hulpwerkwoord help; die hoofwerkwoord sê wat gebeur.', src='workbook', page=103, item='Ons doen', status='derived_from_rule'),
    sa('Werkwoorde in die leesstuk', 'Onderstreep al die hoofwerkwoorde in die leesstuk met groen en die hulpwerkwoorde met oranje. Skryf vyf hoofwerkwoorde en drie hulpwerkwoorde neer.', 'Hoofwerkwoorde (bv.): sit, teken, klim, ry, gaan, soek\nHulpwerkwoorde (bv.): gaan (gaan plakkate maak), sal (sal gestuur word), het (het geteken)', lines=3, page=103, item='Ons doen', status='needs_review'),
    order('Wat het gebeur?', 'Sit die gebeure in die regte volgorde.', ['Mevrou Roos kondig die Boekeweektema aan.', 'Die kinders teken plakkate en skryf stories.', 'Die klas ry met die bus na die biblioteek.', 'Mevrou Botha wys hulle ’n verrassing: diere in kostuums.'], 'Dit is die volgorde in die storie.', perm=[2, 0, 3, 1], src='supplementary', status='derived_from_text'),
    tf('Waar of onwaar?', 'Die iguanodon eet vleis.', False, 'Die iguanodon eet plante – en enigiets wat van plante gemaak is.', src='supplementary', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Wat is die Boekeweektema?', 'Wilde diere', ['Ruimtereise', 'Die see', 'Sprokies'], 'Mevrou Roos sê dit.', ev=['wilde diere']),
    q('literal', 'Wie is die klas se onderwyser?', 'Mevrou Roos', ['Mevrou Botha', 'Mnr. Mosoma', 'Tumi'], 'Sy kondig die Boekeweek aan.', ev=['mevrou Roos']),
    q('literal', 'Wat teken die meeste kinders?', 'Die dinosourus', ['Die leeu', 'Die ysbeer', 'Die jakkals'], 'Die meeste teken die dinosourus.', ev=['teken die dinosourus']),
    q('literal', 'Wat eet die iguanodon?', 'Plante', ['Vleis', 'Vis', 'Insekte'], 'Die iguanodon eet plante.', ev=['Die iguanodon eet plante']),
    q('literal', 'Watter weer is dit op die dag by die biblioteek?', '’n Koue wintersdag', ['’n Warm somersdag', '’n Reënerige lentedag', '’n Mistige oggend'], 'Die storie sê dit is ’n koue wintersdag.', ev=['koue wintersdag']),
    q('literal', 'Wie is mevrou Botha?', 'Die bibliotekaresse', ['Die skoolhoof', 'Tumi se ma', 'Die onderwyseres'], 'Sy is die bibliotekaresse.', ev=['mevrou Botha, die bibliotekaresse']),
    q('literal', 'Watter diere kom in die biblioteek in?', 'Die ysbeer, die leeu en die pandabeer', ['Die dodo en die kwagga', 'Die jakkals en die renoster', 'Net ’n hond'], 'Die ysbeer word gevolg deur ’n leeu en ’n pandabeer.', ev=['leeu en ’n pandabeer']),
    q('inference', 'Wat toon die prent op Tumi se plakkaat?', '’n Dinosourus met ’n blom in sy bek', ['’n Leeu', '’n Renoster', '’n Boek'], 'Die blom wys dat die dinosourus plante eet.', ev=['blom in sy bek']),
  ])

# ============================================================== 114 Wie eet ons boeke?
P114 = [
  'Mevrou Botha maak haar net gereed om te begin lees toe die deur weer oopgaan en nog ’n figuur met ’n skubberige kop wat heen en weer swaai, ingestap kom.',
  '“Is dit nie wonderlik nie!” sê een van die onderwysers. “Dis die heel beste kostuum van almal!”',
  '“O, kyk,” sê die kinders, “dis ’n iguanodon!”',
  '“Wel!” sê mevrou Botha, “’n dinosourus!” Sy is ’n bietjie verbaas, want sy kan nie onthou dat sy ’n dinosouruskostuum bestel het nie.',
  'Die dinosourus hop na die kinders toe asof hy na iemand soek. Toe merk hy vir Tumi heel agter op. Hy hop na Tumi toe en skud haar hand. “Hallo!” sê Tumi.',
  'Al die kinders wil nou die dinosourus se hand skud, en hy stap rond en gee sy skubberige poot vir almal om te skud. Toe gaan hy langs Tumi sit. Hy gaap, sit sy kop op sy pote neer en raak aan die slaap. Tumi probeer om mevrou Botha van die dinosourus te vertel, maar sy wil hê dat Tumi moet wag totdat sy die storie van die ysbeer klaar gelees het.',
  'Tumi kan nie met aandag na die storie luister nie, want die eienaardigste geluide kom van die kreatuur langs haar. Die dinosourus snork! Die klanke word harder en harder. Almal kyk om om te sien wat aangaan. “Ignoreer hom net,” sê mevrou Botha.',
  'Die storie is klaar en steeds slaap die dinosourus voort. Al die kinders staan op en begin na die boeke kyk. Mevrou Botha is besig om vir die kinders ’n boek oor voëls te wys, toe sy ’n stem agter haar hoor. Dis die skoolhoof.',
  '“Jammer,” sê die skoolhoof. “Ek het gemeen om vroeër in te loer. Het alles goed gegaan? Ek sien die kostuums het opgedaag.”',
  '“Maar ek dag dis jy wat die dinosouruskostuum aanhet, Meneer,” sê mevrou Botha verward. “As dit nie jy is nie, wie is dit?”',
  '“Ek het probeer om julle te sê,” sê Tumi. “Ek het geweet dis nie iemand wat soos ’n dinosourus aangetrek is nie.”',
  '“O aarde!” sê iemand anders en wys na die boekrakke. Die dinosourus is besig om ’n boek, Groot oseane en riviere van die wêreld, op te vreet.',
  'Tumi probeer verduidelik. “Dis ’n iguanodon,” sê sy aan mevrou Botha. “Hulle eet plante, en papier kom natuurlik van hout en hout van bome en bome is plante. Dis waarom hy van papier hou.”',
  'Die kinders kyk hoe die dinosourus hoofstuk ses van die boek oor oseane vreet. “O genade,” sê mevrou Botha, “dis glad nie goed nie.”',
  'Die dinosourus sien ’n nuwe stapel boeke. Die helderkleurige buiteblaaie is blink en hard. “Kraak!” hap die dinosourus. “Kraak!” en die eerste storieboek verdwyn tussen sy reusekake.',
  'Almal probeer dink aan ’n manier om die honger dinosourus van die boeke weg te lok.']
G114 = [('figuur', 'Die vorm van iemand of iets wat jy nie goed kan sien nie.'), ('skubberig', 'Met skubbe soos ’n vis of reptiel.'), ('ignoreer', 'Nie aandag aan iets gee nie.'), ('eienaardigste', 'Die vreemdste.'), ('verward', 'Deurmekaar; nie verstaan nie.'), ('reusekake', 'Baie groot kake.'), ('verduidelik', 'Maak duidelik hoe iets werk.'), ('loer', 'Vinnig en stilletjies kyk.')]

L114 = lesson(114,
  skills=[READ, LISTEN, LANG],
  intro='Wie vreet die biblioteek se boeke? Lees verder in die storie, soek byvoeglike naamwoorde, bedink ’n einde en voer dit as ’n rolspel op.',
  objectives=['’n Fiktiewe teks lees en verstaan.', 'Byvoeglike naamwoorde uitken.', 'Saam ’n einde vir die storie bedink en opvoer.', 'Die beste einde neerskryf.'],
  pass_=passage('Wie eet ons boeke?', P114, glossary=G114),
  learn=[
    note('Die iguanodon het ongeveer 130 miljoen jaar gelede geleef, het plante geëet en het ongeveer 2 000 kg geweeg. Hy was byna 3 meter breed by sy heupe en 6 tot 10 meter hoog. Hy het sy naam gekry omdat sy tande soos dié van die iguana-akkedis gelyk het.', title='Feite oor die iguanodon', page=104),
    note('’n **Byvoeglike naamwoord** vertel ons meer van ’n selfstandige naamwoord, bv. ’n skubberige kop, die helderkleurige buiteblaaie.', title='Byvoeglike naamwoorde', src='supplementary', page=104),
  ],
  acts=[
    sa('Byvoeglike naamwoorde', 'Omkring die byvoeglike naamwoorde in die leesstuk met blou. Skryf vyf neer.', 'skubberige (kop)\nbeste (kostuum)\neienaardigste (geluide)\nhelderkleurige (buiteblaaie)\nnuwe (stapel)', lines=5, page=104, item='Ons doen', status='needs_review'),
    discuss('Bedink ’n einde (groepwerk)', 'Niemand wil hê dat hulle biblioteek deur ’n dinosourus opgevreet moet word nie. Wat kan die kinders in hierdie storie doen om die dinosourus van hulle biblioteek af weg te lok? Bespreek dit in groepverband en voer julle idees voor die klas op.', page=105, item='Ons doen'),
    writing('Skryf die beste einde', 'Nadat julle almal se idees gesien het, besluit wie s’n die beste is en skryf die oplossing neer. Nou het julle ’n slot vir die storie “Die Biblioteekmonster”.', checklist=['Ek het die beste idee gekies.', 'My einde los die probleem op.', 'Ek het spelling en punktuasie nagegaan.'], lines=8, page=105, item='Ons skryf'),
    order('Wat gebeur in die storie?', 'Sit die gebeure in die regte volgorde.', ['’n Dinosourus stap in en skud Tumi se hand.', 'Die dinosourus raak aan die slaap en snork.', 'Die skoolhoof sê hy het nie die kostuum aan nie.', 'Die dinosourus begin boeke vreet.'], 'Dit is die volgorde in die storie.', perm=[1, 3, 0, 2], src='supplementary', status='derived_from_text'),
    tf('Waar of onwaar?', 'Tumi weet reg van die begin af dat dit ’n regte dinosourus is.', True, 'Sy sê: “Ek het geweet dis nie iemand wat soos ’n dinosourus aangetrek is nie.”', src='supplementary', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Wie skud Tumi se hand?', 'Die dinosourus', ['Die ysbeer', 'Mevrou Roos', 'Die skoolhoof'], 'Hy hop na Tumi toe en skud haar hand.', ev=['skud haar hand']),
    q('literal', 'Wat doen die dinosourus nadat hy langs Tumi gaan sit?', 'Hy raak aan die slaap', ['Hy dans', 'Hy eet ’n boek', 'Hy loop weg'], 'Hy gaap en raak aan die slaap.', ev=['raak aan die slaap']),
    q('literal', 'Watter eienaardige geluid maak die dinosourus?', 'Hy snork', ['Hy sing', 'Hy brul', 'Hy fluit'], 'Die dinosourus snork!', ev=['Die dinosourus snork']),
    q('literal', 'Wie is die stem agter mevrou Botha?', 'Die skoolhoof', ['Tumi', 'Die onderwyser', 'Bongi'], 'Dis die skoolhoof.', ev=['Dis die skoolhoof']),
    q('literal', 'Watter boek vreet die dinosourus?', 'Groot oseane en riviere van die wêreld', ['Boeke oor voëls', 'Boeke oor diere', 'Storieboeke vir kleuters'], 'Hy vreet ’n boek oor oseane.', ev=['Groot oseane en riviere van die wêreld']),
    q('inference', 'Hoekom hou die dinosourus van papier?', 'Papier kom van hout, en hout van bome, en bome is plante', ['Dit is sag', 'Dit is sout', 'Dit is warm'], 'Tumi verduidelik: bome is plante.', ev=['papier kom natuurlik van hout']),
    q('literal', 'Waarom het die iguanodon sy naam gekry?', 'Sy tande het soos dié van die iguana-akkedis gelyk', ['Hy het soos ’n akkedis geloop', 'Hy het in die see gewoon', 'Hy was groen'], 'Dit staan in die inligtingsblokkie.', ev=None, status='official', src='workbook', page=104),
    q('inference', 'Wat dink mevrou Botha eers van die dinosourus?', 'Dat dit die skoolhoof in ’n kostuum is', ['Dat dit ’n regte dinosourus is', 'Dat dit Tumi se pa is', 'Dat dit ’n robot is'], 'Sy sê: “Ek dag dis jy wat die dinosouruskostuum aanhet, Meneer.”', ev=['dis jy wat die dinosouruskostuum aanhet']),
  ])

# ============================================================== 115 Boekeweek
L115 = lesson(115,
  skills=[READ, WRITE, LANG],
  intro='Terug by die Boekeweek-storie: soeklees vir inligting, teken die iguanodon, skryf ’n dagboekinskrywing en kyk weer na woordvorming en idiome.',
  objectives=['Soekleesvaardighede toepas.', 'Uit ’n beskrywing ’n dinosourus teken.', '’n Dagboekinskrywing in die eerste persoon en verlede tyd skryf.', 'Basiswoorde, afleidings en samestellings herken.', 'Idiome met hul betekenisse verbind.'],
  learn=[
    text('Soek-lees', 'Soek-lees beteken jy soek vinnig na ’n spesifieke antwoord in ’n teks. Jy lees nie elke woord nie.', bullets=['Kyk watter woorde in die vraag belangrik is.', 'Soek daardie woorde in die teks.', 'Lees net daar noukeurig.'], src='supplementary', page=106),
    text('Letterlike en figuurlike taal', bullets=['**Letterlike taalgebruik** verwys na die letterlike betekenis van woorde of uitdrukkings.', '**Figuurlike taalgebruik** beteken om woorde te gebruik wat beelde (in konteks/sinsverband) in die gedagtes oproep.', '**Beeldspraak** is die gebruik van vergelykings, metafore, personifikasie, idiomatiese uitdrukkings, ens.'], page=107),
    text('Woordvorming', bullets=['**Basiswoorde**', '**Afleidings** = basis + voorvoegsel en/of agtervoegsel', '**Samestellings** = basis + basis'], page=107),
    text('Dagboekinskrywing', bullets=['Skryf in die **eerste persoon** (gebruik “ek”).', 'Skryf in die **verlede tyd**.', 'Begin met “Liewe Dagboek”.'], page=106),
  ],
  acts=[
    sa('Soek-lees', 'Pas soekleesvaardighede toe en beantwoord hierdie vraag: Watter gebeure is vir Boekeweek beplan?', 'Kompetisies, uitstappies na die biblioteek op die dorp, en baie stories; ook plakkate en stories oor bedreigde diere.', lines=3, page=106, item='Ons skryf', status='derived_from_text'),
    writing('Teken die iguanodon', 'Lees die beskrywing in die storie en teken die dinosourus. Merk af wat jou prent bevat.', checklist=['twee kort voorbene', '’n kort, baie dik stert', 'vyf stomp tone aan die pote', 'vyf vingers aan elke hand', '’n kort, horingagtige duim'], no_text=True, lines=1, page=106, item='Ons skryf'),
    writing('Skryf ’n dagboekinskrywing', 'Verbeel jou dat jy een van die kinders in die storie is. Skryf ’n opsomming in die vorm van ’n dagboekinskrywing oor wat vandag in die biblioteek gebeur het. Begin: “Liewe Dagboek, Vandag het ’n monster in die biblioteek ingekom ...”', checklist=['Ek het in die eerste persoon geskryf (“ek”).', 'Ek het die verlede tyd gebruik.', 'Ek het die belangrikste gebeure genoem.'], lines=10, page=106, item='dagboek'),
    choices('Afleiding of samestelling?', 'Dui aan of die woord ’n afleiding of ’n samestelling is.', [('geweet', ['afleiding', 'samestelling'], 0), ('boekrak', ['afleiding', 'samestelling'], 1), ('reusekake', ['afleiding', 'samestelling'], 1), ('ontslae', ['afleiding', 'samestelling'], 0), ('storieboek', ['afleiding', 'samestelling'], 1)],
            'Samestelling = basis + basis; afleiding = basis + voor- of agtervoegsel.', src='workbook', page=107, item='tabel', status='derived_from_rule'),
    match('Idiome en hul betekenisse', 'Verbind elke idioom met sy betekenis.', [('As die kat weg is, is die muis baas.', 'Wanneer die baas weg is, doen die onderhoriges wat hulle wil.'), ('Hond se gedagtes kry.', 'Agterdogtig raak.'), ('Iemand laat bokspring.', 'Iemand afransel.'), ('Oor koeitjies en kalfies gesels.', 'Oor alledaagse dinge praat.'), ('Jou kop in ’n bynes steek.', 'Jou met iets bemoei wat groot probleme kan veroorsaak.')],
          'Idiome is figuurlik: hulle beteken nie wat die woorde letterlik sê nie.', src='workbook', page=107, item='idiome', status='derived_from_rule'),
    choices('Letterlik of figuurlik?', 'Is die taalgebruik letterlik of figuurlik?', [('Die dinosourus het ’n blom in sy bek.', ['letterlik', 'figuurlik'], 0), ('Hy het sy kop in ’n bynes gesteek.', ['letterlik', 'figuurlik'], 1), ('Sy het oor koeitjies en kalfies gesels.', ['letterlik', 'figuurlik'], 1)],
            'Idiome en beelde is figuurlik; wat werklik gebeur, is letterlik.', src='supplementary', status='derived_from_rule'),
    tf('Waar of onwaar?', 'Jy skryf ’n dagboekinskrywing in die derde persoon.', False, 'Dit moet in die eerste persoon (“ek”) en verlede tyd wees.', src='workbook', page=106, item='dagboek', status='official'),
  ],
  quiz=[
    q('literal', 'In watter persoon skryf jy die dagboekinskrywing?', 'Eerste persoon (“ek”)', ['Tweede persoon (“jy”)', 'Derde persoon (“hy/sy”)', 'Enige persoon'], 'Die werkboek sê: eerste persoon.', status='official', src='workbook', page=106),
    q('literal', 'In watter tyd skryf jy die dagboekinskrywing?', 'Verlede tyd', ['Teenwoordige tyd', 'Toekomende tyd', 'Enige tyd'], 'Die werkboek sê: verlede tyd.', status='official', src='workbook', page=106),
    q('literal', 'Hoeveel vingers het die iguanodon aan elke hand?', 'Vyf', ['Twee', 'Drie', 'Tien'], 'Hy het vyf vingers aan elke hand.', status='derived_from_text', src='workbook', page=106),
    q('literal', 'Hoe lyk die iguanodon se stert?', 'Kort en baie dik', ['Lank en dun', 'Gepunt', 'Skubberig en kort'], 'Dit staan in die storie (Die biblioteekmonster).', status='derived_from_text', src='workbook', page=106),
    q('grammar', 'Watter woord is ’n samestelling?', 'boekrak', ['geweet', 'ontslae', 'gebou'], 'Boek + rak.', status='derived_from_rule', src='workbook', page=107, item='tabel'),
    q('vocabulary', 'Wat beteken “oor koeitjies en kalfies gesels”?', 'Oor alledaagse dinge praat', ['Oor diere skryf', 'Oor boerdery lees', 'Hard praat'], 'Dit is ’n idioom.', status='derived_from_rule', src='workbook', page=107, item='idiome'),
    q('vocabulary', 'Wat beteken “hond se gedagtes kry”?', 'Agterdogtig raak', ['Honger kry', 'Slaperig word', 'Bly word'], 'Dit is die betekenis van die idioom.', status='derived_from_rule', src='workbook', page=107, item='idiome'),
    q('vocabulary', 'Wat is figuurlike taalgebruik?', 'Woorde wat beelde in die gedagtes oproep', ['Net die letterlike betekenis van woorde', 'Spelling', 'Punktuasie'], 'Dit is die verduideliking op bladsy 107.', status='official', src='workbook', page=107),
  ])

# ============================================================== 116 Skryf 'n resensie
L116 = lesson(116,
  skills=[WRITE],
  intro='Wat dink jy van ’n storie wat jy gelees het? Skryf ’n boekresensie – eers beplan jy op ’n organiseerder, dan skryf jy.',
  objectives=['’n Resensie beplan op ’n grafiese organiseerder.', '’n Resensie in paragraafvorm skryf.', 'Jou werk hersien en korrigeer.'],
  learn=[
    text('Wat is ’n resensie?', bullets=['’n Resensie vertel ander wat jy van ’n storie dink en of jy dit sal aanbeveel.', 'Jy kan ’n storie kies wat jy gelees het – ook enige van die stories in jou werkboek.'], src='supplementary', page=108),
    table('Die organiseerder', ['Deel', 'Vraag'], [['Titel van die storie', ''], ['Skrywer', ''], ['Agtergrond', 'Waar en wanneer speel die storie hom af?'], ['Karakters', 'Wie is die mense in die storie?'], ['Intrige', 'Wat gebeur in die storie? Is die storie feit of fiksie?'], ['Tema', 'Waaroor handel die storie? Wat is sy boodskap?'], ['Waarvan het jy gehou?', ''], ['Aanbeveling', 'Waarom sal jy die storie vir ’n maat aanbeveel?']], page=108),
  ],
  acts=[
    match('Pas die deel by die vraag', 'Verbind elke deel van die organiseerder met die vraag wat dit stel.', [('Agtergrond', 'Waar en wanneer speel die storie hom af?'), ('Karakters', 'Wie is die mense in die storie?'), ('Intrige', 'Wat gebeur in die storie?'), ('Tema', 'Waaroor handel die storie? Wat is sy boodskap?'), ('Aanbeveling', 'Waarom sal jy die storie vir ’n maat aanbeveel?')], 'Dit is die vrae wat by elke deel van die organiseerder staan.', src='workbook', page=108, item='organiseerder', status='official'),
    writing('Beplan jou resensie', 'Voltooi die grafiese organiseerder: titel van die storie, skrywer, agtergrond, karakters, intrige, tema, waarvan jy gehou het en aanbeveling.', checklist=['Titel en skrywer', 'Agtergrond (waar en wanneer)', 'Karakters', 'Intrige (feit of fiksie)', 'Tema en boodskap', 'Waarvan ek gehou het', 'Aanbeveling'], lines=12, page=108, item='organiseerder'),
    order('Die skryfproses', 'Sit die stappe in die regte volgorde.', ['Voltooi die organiseerder.', 'Skryf die eerste weergawe in paragraafvorm in jou klaswerkboek.', 'Laat ’n maat jou resensie hersien.', 'Korrigeer waar nodig.', 'Skryf die finale weergawe neer.'], 'Dit is die volgorde wat die werkboek gee.', perm=[2, 0, 4, 1, 3], src='workbook', page=109, item='proses', status='official'),
    writing('Skryf jou resensie', 'Skryf die finale weergawe van jou resensie.', checklist=['Ek het in paragrawe geskryf.', 'Al die dele van die organiseerder is gedek.', 'My maat het my werk hersien.', 'Ek het gekorrigeer.'], lines=14, page=109, item='finale weergawe'),
    tf('Waar of onwaar?', 'Jy moet ’n resensie oor ’n storie skryf wat jy nog nooit gelees het nie.', False, 'Die werkboek sê: oor ’n storie wat jy gelees het.', src='workbook', page=108, item='opdrag', status='official'),
  ],
  quiz=[
    q('main_idea', 'Waaroor skryf jy ’n resensie?', '’n Storie wat jy gelees het', ['’n Film', '’n Liedjie', '’n Reisverslag'], 'Dit is die opdrag.', status='official', src='workbook', page=108),
    q('literal', 'Waar plan jy jou resensie?', 'Op ’n grafiese organiseerder', ['Op die bord', 'In ’n dagboek', 'Op ’n plakkaat'], 'Voltooi die grafiese organiseerder.', status='official', src='workbook', page=108),
    q('literal', 'Watter deel vra “Waar en wanneer speel die storie hom af?”', 'Agtergrond', ['Karakters', 'Tema', 'Intrige'], 'Dit is die vraag by Agtergrond.', status='official', src='workbook', page=108),
    q('literal', 'Watter deel vra “Wie is die mense in die storie?”', 'Karakters', ['Agtergrond', 'Aanbeveling', 'Titel'], 'Dit is die vraag by Karakters.', status='official', src='workbook', page=108),
    q('literal', 'Waarvoor staan “Tema”?', 'Waaroor die storie handel en wat sy boodskap is', ['Waar die storie hom afspeel', 'Die titel', 'Die skrywer se naam'], 'Dit is die vraag by Tema.', status='official', src='workbook', page=108),
    q('literal', 'Waarom skryf jy ’n aanbeveling?', 'Om te sê waarom jy die storie vir ’n maat sal aanbeveel', ['Om die skrywer te bedank', 'Om die storie te verkoop', 'Om die intrige te kopieer'], 'Dit is die vraag by Aanbeveling.', status='official', src='workbook', page=108),
    q('sequencing', 'Wat doen jy EERS: skryf die eerste weergawe of voltooi die organiseerder?', 'Voltooi die organiseerder', ['Skryf die eerste weergawe', 'Skryf die finale weergawe', 'Laat ’n maat hersien'], 'Eers beplan, dan skryf.', status='derived_from_text', src='workbook', page=108),
    q('literal', 'Waar skryf jy die eerste weergawe?', 'In paragraafvorm in jou klaswerkboek', ['Op die bladsy self', 'Op die internet', 'Op ’n plakkaat'], 'Die eerste weergawe gaan in jou klaswerkboek.', status='official', src='workbook', page=109),
  ])
