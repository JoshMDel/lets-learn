import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

BEELD = [('Vergelyking', 'vergelyk twee enerse goed met die woord “soos”. Ons gebruik in vergelykings dikwels dierebeelde.'),
         ('Metafoor', 'vergelyk twee dinge deur te sê dat die een ding die ander ding is, sonder om die woord “soos” te gebruik.'),
         ('Alliterasie', 'is wanneer opeenvolgende woorde met dieselfde letter begin om die aandag te trek.'),
         ('Assonansie', 'is die herhaling van vokale (klinkers) om ’n bepaalde stemming te skep.'),
         ('Personifikasie', 'is wanneer ons menslike/persoonlike eienskappe aan dooie dinge gee, bv. “Die wind huil om die hoeke”.')]

# ============================================================== 121 Maandag-malligheid
P121 = poem('Maandag-malligheid', [
  ['Ek word wakker van my wekker', 'dis nog vroeg, ek voel nie lekker.', 'Die hond se woef-woef', 'maak in my kop: doef-doef', 'Ek is laat en die kar toet al', 'die oggend begin sirkus-mal!'],
  ['Die skoolklok lui skril', 'soos meisies wat gil.', 'Juffrou hou nie op raas', 'in haar klas is sy mos baas.', 'Pouse roep en soek die kinders mekaar', 'nie eers die interkom laat hul bedaar.'],
  ['Uiteindelik is die dag verby', 'my ore steeds nie geraas-vry.', 'Tuis wil niemand die TV afsit,', 'nie eers as ons voor ete bid.', 'Net as ek slaap is dit doodstil', 'tot die wekker my weer wakker gil.']],
  glossary=[('interkom', 'Toestel waarmee ’n skool aankondigings oor luidsprekers maak.'), ('bedaar', 'Rustig word.'), ('geraas-vry', 'Sonder lawaai.'), ('malligheid', 'Gekheid; dwase of dol gedrag.'), ('raas', 'Hard en kwaad praat.')])

L121 = lesson(121,
  skills=[READ, LISTEN, LANG],
  intro='Wat ’n lawaaierige Maandagoggend! Lees die gedig “Maandag-malligheid”, dramatiseer die klanke, soek die rymwoorde en ontdek die beeldspraak.',
  objectives=['’n Gedig hardop lees en dramatiseer.', 'Rymwoorde in ’n gedig uitken.', 'Vrae oor ’n gedig beantwoord.', 'Voorbeelde van beeldspraak (vergelyking, metafoor, alliterasie, assonansie, personifikasie) gee.'],
  pass_=P121,
  learn=[
    text('Wat is beeldspraak?', 'Beeldspraak beteken om ’n figuurlike betekenis oor te dra deur vergelykings, metafore, personifikasie, idiomatiese uitdrukkings, ens.', page=118),
    table('Soorte beeldspraak', ['Term', 'Verduideliking'], [[a, b] for a, b in BEELD], page=118),
  ],
  acts=[
    discuss('Dramatiseer die gedig', 'Lees die gedig “Maandag-malligheid” hardop. Dramatiseer die gedig deur die klanke na te boots om die malligheid waarmee die Maandag begin, voor te stel (woef-woef, doef-doef, toet, die skoolklok, die wekker).', speak='passage', page=118, item='Ons lees'),
    match('Rymwoorde', 'Omkring die woorde wat rym: verbind elke woord met sy rymwoord in die gedig.', [('wekker', 'lekker'), ('woef-woef', 'doef-doef'), ('al', 'mal'), ('skril', 'gil'), ('raas', 'baas'), ('mekaar', 'bedaar'), ('verby', 'geraas-vry'), ('afsit', 'bid')], 'Die rymwoorde kom aan die einde van reëls wat saam ’n paar vorm.', src='workbook', page=118, item='rym', status='derived_from_text'),
    sa('Strofes en versreëls', 'Uit hoeveel strofes bestaan die gedig? Hoeveel versreëls is daar in elke strofe? Dui die rymskema aan.', 'Die gedig bestaan uit 3 strofes.\nElke strofe het 6 versreëls.\nRymskema: aabbcc (die reëls rym twee-twee).', lines=3, page=119, item='1–3', status='derived_from_text'),
    choices('Watter soort beeldspraak?', 'Kies die regte soort beeldspraak.', [('Die skoolklok lui skril soos meisies wat gil.', ['vergelyking', 'metafoor', 'personifikasie'], 0), ('Die wind huil om die hoeke.', ['vergelyking', 'metafoor', 'personifikasie'], 2), ('Sy het ’n hart van goud.', ['vergelyking', 'metafoor', 'personifikasie'], 1), ('Hy is so trots soos ’n pou.', ['vergelyking', 'metafoor', 'personifikasie'], 0), ('Die wekker gil my wakker.', ['vergelyking', 'metafoor', 'personifikasie'], 2)],
            'Vergelyking gebruik “soos”; metafoor sê iets ís iets anders; personifikasie gee menslike eienskappe aan dooie dinge.', src='workbook', page=118, item='beeldspraak', status='derived_from_rule'),
    sa('Voorbeelde uit die gedig', 'Gee voorbeelde vir elk uit die gedig: alliterasie, assonansie, metafoor, vergelyking.', 'Alliterasie: “wakker van my wekker” / “weer wakker gil”\nAssonansie: “woef-woef … doef-doef” (die oe-klank)\nMetafoor: “die oggend begin sirkus-mal” (die oggend is ’n sirkus)\nVergelyking: “Die skoolklok lui skril soos meisies wat gil.”', lines=5, page=119, item='beeldspraak', status='needs_review'),
    sa('Die spreker en sy gevoelens', 'Wie is die spreker in die gedig? Beskryf die emosies/gevoelens wat die spreker beleef in jou eie woorde.', 'Die spreker is ’n skoolkind. Hy of sy voel moeg, geïrriteerd en oorweldig deur al die geraas.', lines=4, page=119, item='spreker', status='needs_review'),
    tf('Waar of onwaar?', 'In die gedig is dit die hele dag stil.', False, 'Dit is ’n lawaaierige dag; eers as die spreker slaap, is dit doodstil.', src='supplementary', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Wat maak die spreker wakker?', '’n Wekker', ['Die hond', 'Die kar', 'Die skoolklok'], 'Hy word wakker van sy wekker.', ev=['Ek word wakker van my wekker']),
    q('literal', 'Met watter klank word die hond beskryf?', 'woef-woef', ['miaau', 'toet', 'lui'], 'Die hond se woef-woef maak “doef-doef” in sy kop.', ev=['Die hond se woef-woef']),
    q('literal', 'Waarmee word die skoolklok vergelyk?', 'Meisies wat gil', ['Hondjies wat blaf', 'Kinders wat lag', 'Voëls wat sing'], 'Die skoolklok lui skril soos meisies wat gil.', ev=['soos meisies wat gil']),
    q('literal', 'Wie hou nie op raas nie?', 'Juffrou', ['Die skoolhoof', 'Die hond', 'Die kinders'], 'Juffrou hou nie op raas nie.', ev=['Juffrou hou nie op raas']),
    q('literal', 'Wat wil niemand tuis afsit nie?', 'Die TV', ['Die radio', 'Die kar', 'Die wekker'], 'Tuis wil niemand die TV afsit nie.', ev=['Tuis wil niemand die TV afsit']),
    q('literal', 'Wanneer is dit doodstil?', 'As die spreker slaap', ['In die klas', 'By pouse', 'Op pad skool toe'], 'Net as hy slaap is dit doodstil.', ev=['Net as ek slaap is dit doodstil']),
    q('grammar', 'Hoeveel strofes het die gedig?', '3', ['2', '4', '6'], 'Die gedig bestaan uit drie strofes van ses reëls.', status='derived_from_text', src='workbook', page=119, item='1–3'),
    q('grammar', 'Watter soort beeldspraak is “Die skoolklok lui skril soos meisies wat gil”?', 'Vergelyking', ['Metafoor', 'Alliterasie', 'Assonansie'], 'Daar is die woord “soos”.', ev=['soos meisies wat gil'], status='derived_from_rule'),
  ])

# ============================================================== 122 My eie gedig
L122 = lesson(122,
  skills=[WRITE],
  intro='Nou is jy die digter! Skryf ’n gedig oor ’n slim dier. Beplan met ’n geheuekaart, soek rymwoorde en skryf vier strofes van vier reëls.',
  objectives=['’n Geheuekaart gebruik om ’n gedig te beplan.', 'Beskrywende woorde en rymwoorde saamstel.', '’n Gedig van 4 strofes van 4 reëls skryf.', 'Beeldspraak in jou gedig gebruik.'],
  learn=[
    text('Die opdrag', bullets=['Skryf ’n gedig oor ’n **slim dier**. Dit moet uit **4 strofes** (verse) van **4 reëls** elk bestaan.', 'Beskryf hoe die dier lyk en watter karaktertrekke hy het. Wat is uniek aan hom? Wat doen hy wat hom slim maak?', 'Bespreek die dier in groepverband.', 'Gebruik die rymwoorde aan die einde van elke twee reëls.', 'Onthou om beeldspraak te gebruik.'], page=120),
    table('Geheuekaart vir jou gedig', ['Strofe', 'Onderwerp'], [['Strofe 1', 'Fisiese voorkoms'], ['Strofe 2', 'Karaktertrekke'], ['Strofe 3', 'Uniekheid'], ['Strofe 4', 'Wat hom slim maak']], page=120),
  ],
  acts=[
    match('Beplan jou strofes', 'Verbind elke strofe met sy onderwerp.', [('Strofe 1', 'Fisiese voorkoms'), ('Strofe 2', 'Karaktertrekke'), ('Strofe 3', 'Uniekheid'), ('Strofe 4', 'Wat hom slim maak')], 'Dit is die vier dele van die geheuekaart.', src='workbook', page=120, item='geheuekaart', status='official'),
    discuss('Bespreek die dier', 'Bespreek die dier in groepverband: Hoe lyk hy? Watter karaktertrekke het hy? Wat is uniek aan hom? Wat doen hy wat hom slim maak?', page=120, item='bespreking'),
    writing('Geheuekaart: woorde en rymwoorde', 'Skryf woorde neer wat die dier beskryf. Voeg dan woorde by wat rym met die beskrywende woorde. Doen dit vir elke strofe.', checklist=['Strofe 1: woorde en rymwoorde', 'Strofe 2: woorde en rymwoorde', 'Strofe 3: woorde en rymwoorde', 'Strofe 4: woorde en rymwoorde'], lines=10, page=120, item='geheuekaart'),
    choices('Rym of nie?', 'Rym die woorde?', [('kat – mat', ['ja', 'nee'], 0), ('slim – klim', ['ja', 'nee'], 0), ('vos – hond', ['ja', 'nee'], 1), ('pote – note', ['ja', 'nee'], 0), ('stert – berg', ['ja', 'nee'], 1)],
            'Woorde rym as hulle op dieselfde klank eindig.', src='supplementary', status='derived_from_rule'),
    writing('Skryf die eerste weergawe', 'Skryf die eerste weergawe van jou gedig in jou klaswerkboek. Laat ’n maat dit hersien en korrigeer waar nodig.', checklist=['Die gedig het 4 strofes.', 'Elke strofe het 4 reëls.', 'Ek het rymwoorde aan die einde van elke twee reëls gebruik.', 'Ek het beeldspraak gebruik.', 'My maat het my gedig hersien.'], lines=14, page=120, item='eerste weergawe'),
    writing('Skryf die finale weergawe', 'Skryf die finale weergawe van jou gedig hier neer. Teken ook ’n bypassende prent.', checklist=['Ek het ’n titel gekies.', 'Ek het gekorrigeer.', 'Ek het ’n prent geteken.'], lines=14, page=121, item='finale weergawe'),
  ],
  quiz=[
    q('main_idea', 'Waaroor skryf jy jou gedig?', '’n Slim dier', ['My ma', 'Die weer', 'My skool'], 'Dit is die opdrag.', status='official', src='workbook', page=120),
    q('literal', 'Uit hoeveel strofes bestaan jou gedig?', 'Vier', ['Een', 'Twee', 'Agt'], 'Vier strofes.', status='official', src='workbook', page=120),
    q('literal', 'Hoeveel reëls het elke strofe?', 'Vier', ['Twee', 'Ses', 'Tien'], 'Elke strofe het 4 reëls.', status='official', src='workbook', page=120),
    q('literal', 'Waaroor gaan strofe 1?', 'Fisiese voorkoms', ['Karaktertrekke', 'Uniekheid', 'Wat hom slim maak'], 'Strofe 1 is die fisiese voorkoms.', status='official', src='workbook', page=120),
    q('literal', 'Waaroor gaan strofe 4?', 'Wat hom slim maak', ['Fisiese voorkoms', 'Karaktertrekke', 'Uniekheid'], 'Strofe 4 is wat hom slim maak.', status='official', src='workbook', page=120),
    q('literal', 'Waar gebruik jy die rymwoorde?', 'Aan die einde van elke twee reëls', ['Aan die begin van die gedig', 'Net in die titel', 'In die middel van elke reël'], 'Dit is die opdrag.', status='official', src='workbook', page=120),
    q('main_idea', 'Wat moet jy ook in jou gedig gebruik?', 'Beeldspraak', ['’n Resep', '’n Kaart', 'Getalle'], 'Onthou om beeldspraak te gebruik.', status='official', src='workbook', page=120),
    q('grammar', 'Watter woord rym met “klim”?', 'slim', ['vos', 'berg', 'groot'], 'Slim en klim eindig op dieselfde klank.', status='derived_from_rule', src='supplementary'),
  ])

# ============================================================== 123 Rooikappie en die wolf
P123 = poem('Rooikappie en die wolf', [
  ['Wolf beleef ’n gevoel', 'Sy maag is aan die woel.', 'Hy besluit om aan Ouma se deur te klop.', 'Ouma maak dadelik oop, hy’t haar gefop.', 'Sy sien die skerp tande, die aaklige gryns.', '“Mag ek inkom?” vra Wolfie geveins.', 'Arme Ouma skrik haar boeglam,', '“Hy gaan my opeet!” roep sy bang.', 'En sy slaan die bal glad nie mis –', 'Hy maak van haar ’n smaaklike dis.'],
  ['Maar Ouma was maar tingerig en klein,', 'En Wolfie kla, “Dit help nie my hongerpyn!', 'Ek het nog glad nie genoeg gehad,', 'Ek het byna niks daarby gebaat!”', 'Op en af stap hy in die huis,', 'En hy deursoek die hele kombuis.'],
  ['Toe gee hy ’n harde, lelike lag.', '“Ek gaan net hier wag', 'Tot Rooikappie kom,', 'en my intussen vermom!”'],
  ['Kort daarna kom die meisie huis toe.', 'Sy stop. Sy staar. En sy sê toe:', '“Ouma, waarom is jou ore so groot?”', '“Sodat ek beter kan luister, soos dit hoort!”'],
  ['Hy sit vir haar en kyk en dink', 'Hoe lekker sy tande weg gaan sink.', 'Vergeleke met die ou vrou', 'Gaan sy smaak soos kabeljou.', 'Rooikappie begin nader staan.', '“Maar ouma, jy’t dan ’n pelsjas aan!”'],
  ['“Nee,” roep Wolf, dis verkeerd!', 'Jy’t vergeet om te vra oor my tande so wreed!', 'Maar ag nou ja, ongeag wat jy sê,', 'Ek gaan jou nou vir aandete hê.”', 'Die dogtertjie glimlag en trek haar swart belt styf.'],
  ['Sy laat reën karatehoue oor die wolf se lyf.', 'Toe mik sy na die dier se kop,', 'En baie gou is hy diep in die sop.'],
  ['’n Paar weke later, daar in die woud,', 'Kom ek Rooikappie teë, en dis lekker koud.', 'Sy lyk heel anders! Geen baadjie van rooi,', 'En met geen kappie opgetooi.', 'Sy sê: “Hallo, hoe gaan dit met jou?', 'Ek hoop jy sal van my wolfbaadjie hou.”']],
  glossary=[('gefop', 'Kul; mislei.'), ('geveins', 'Voorgee; nie opreg nie.'), ('boeglam', 'Heeltemal verlam van skrik.'), ('tingerig', 'Maer en swak.'), ('vermom', 'Jou lyk anders maak sodat niemand jou herken nie.'), ('opgetooi', 'Mooi aangetrek of versier.'), ('ongeag', 'Ongeag wat; maak nie saak wat nie.')])

L123 = lesson(123,
  skills=[READ, LISTEN],
  intro='Almal ken Rooikappie en die wolf – maar in hierdie gedig verdedig Rooikappie haarself met karatehoue! Lees, beantwoord vrae en voer ’n rolspel op.',
  objectives=['’n Gedig hardop in groepverband lees.', 'Ooreenkomste en verskille met die sprokie bespreek.', 'Vrae oor die gedig beantwoord.', '’n Rolspel van die gedig beplan en opvoer.'],
  pass_=P123,
  learn=[
    text('Strofes en verse', 'Gedigte bestaan uit strofes of verse. Elke strofe bestaan uit ’n aantal versreëls. Sommige gedigte het net een strofe, terwyl ander uit meer strofes bestaan.', page=122),
    note('Jy sal opmerk dat die gedig baie met die sprokiesverhaal ooreenstem, behalwe dat die digter ’n kinkel in die gedig invoeg deurdat Rooikappie haarself teen die wolf verdedig.', title='Gee ag', page=122),
  ],
  acts=[
    discuss('Lees hardop', 'Lees hierdie gedig hardop in groepverband.', speak='passage', page=122, item='Ons lees'),
    sa('Hoeveel strofes?', 'Uit hoeveel strofes bestaan die gedig?', '8 strofes (van 10, 6, 4, 4, 6, 5, 3 en 6 reëls).', lines=2, page=122, item='strofes', status='derived_from_text'),
    sa('Soortgelyk aan die sprokie', 'Watter dele van hierdie gedig is soortgelyk aan die sprokie van Rooikappie?', 'Die wolf vermom hom as Ouma; Rooikappie vra “Ouma, waarom is jou ore so groot?”; die wolf wil Rooikappie eet.', lines=3, page=123, item='1', status='derived_from_text'),
    sa('Hoe verskil die slot?', 'Hoe verskil die slot van die gedig van dié van die sprokie? (Hoe verdedig Rooikappie haarself?)', 'Rooikappie wen met karatehoue en verslaan die wolf; in die sprokie word sy gered (deur ’n jagter).', lines=3, page=123, item='2', status='derived_from_text'),
    sa('Die digter en Rooikappie', 'Hoe weet ons dat die digter Rooikappie raakgeloop het? (Kyk na die laaste strofe.)', 'Die digter sê: “Kom ek Rooikappie teë” en gesels met haar in die woud.', lines=3, page=123, item='3', status='derived_from_text'),
    choices('Wie sê dit?', 'Watter karakter sê dit?', [('“Ouma, waarom is jou ore so groot?”', ['Rooikappie', 'Die wolf', 'Ouma'], 0), ('“Sodat ek beter kan luister, soos dit hoort!”', ['Rooikappie', 'Die wolf', 'Ouma'], 1), ('“Hy gaan my opeet!”', ['Rooikappie', 'Die wolf', 'Ouma'], 2), ('“Ek hoop jy sal van my wolfbaadjie hou.”', ['Rooikappie', 'Die wolf', 'Ouma'], 0)],
            'Dit volg uit die gebeure in die gedig.', src='supplementary', status='derived_from_text'),
    discuss('Rolspel', 'Beplan en berei ’n rolspel van die gedig in groepverband voor. Julle sal hierdie karakters nodig hê: Rooikappie, haar ouma, die wolf en die digter.', page=123, item='Ons rolspeel'),
  ],
  quiz=[
    q('literal', 'Wie klop aan Ouma se deur?', 'Die wolf', ['Rooikappie', 'Die digter', 'Die jagter'], 'Wolf besluit om aan Ouma se deur te klop.', ev=['Hy besluit om aan Ouma se deur te klop']),
    q('literal', 'Wat gebeur met Ouma?', 'Die wolf eet haar op', ['Sy loop weg', 'Sy gaan slaap', 'Sy bak koek'], 'Hy maak van haar ’n smaaklike dis.', ev=['Hy maak van haar ’n smaaklike dis']),
    q('literal', 'Waarom is die wolf nog honger?', 'Ouma was maer en klein', ['Hy het niks geëet nie', 'Hy hou nie van vleis nie', 'Hy het te veel geëet'], 'Ouma was tingerig en klein.', ev=['Maar Ouma was maar tingerig en klein']),
    q('inference', 'Wat doen die wolf om Rooikappie te kul?', 'Hy vermom hom', ['Hy gaan weg', 'Hy loop weg', 'Hy roep die jagter'], 'Hy sê hy gaan hom vermom.', ev=['en my intussen vermom']),
    q('inference', 'Waarom vra Rooikappie oor Ouma se groot ore?', 'Sy merk dat dit nie Ouma is nie', ['Sy het nie goed gesien nie', 'Sy wil die wolf help', 'Sy is bang'], 'Sy raak agterdogtig.', ev=['waarom is jou ore so groot']),
    q('literal', 'Hoe verdedig Rooikappie haarself?', 'Met karatehoue', ['Sy hardloop weg', 'Sy skree vir hulp', 'Sy gooi water'], 'Sy laat karatehoue reën.', ev=['karatehoue']),
    q('inference', 'Wie is die “ek” in die laaste strofe?', 'Die digter', ['Ouma', 'Rooikappie', 'Die wolf'], 'Die digter sê hy kom Rooikappie teë.', ev=['Kom ek Rooikappie teë']),
    q('literal', 'Waarmee is Rooikappie aan die einde aangetrek?', 'Met ’n wolfbaadjie', ['Met ’n rooi kappie', 'Met ’n pelsjas', 'Met ’n karatebelt net'], 'Sy lyk anders: geen rooi baadjie, maar ’n wolfbaadjie.', ev=['wolfbaadjie hou']),
  ])
