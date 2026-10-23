import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

# ============================================================== 106 Die sewe kontinente
L106 = lesson(106,
  skills=[READ, WRITE],
  intro='Op die wêreldkaart sien ons kontinente en oseane. Vandag leer jy waar hulle is en hoe die denkbeeldige lyne op die kaart plekke vir ons vind.',
  objectives=['Die sewe kontinente en die groot oseane op ’n wêreldkaart uitken.', 'Verstaan wat lengte- en breedtegrade is.', 'Die ewenaar, die keerkringe en die poolsirkels met hul grade verbind.'],
  learn=[
    text('Lengte- en breedtegrade', 'Die lengte- en breedtegrade wat op die kaart aangedui word, is denkbeeldige lyne wat ons gebruik om plekke op die aarde te kry.', bullets=['Die **breedtegrade** loop van oos na wes (of van links na regs).', 'Die **lengtegrade** loop van die noordpool na die suidpool (van bo na onder).', 'Hulle kruis mekaar dus.'], page=86),
    table('Belangrike breedtegrade', ['Lyn', 'Ligging'], [['Ewenaar', '0° – ’n denkbeeldige lyn om die aarde se middellyn'], ['Kreefskeerkring', '23° noord van die ewenaar (23° N)'], ['Steenbokskeerkring', '23° suid van die ewenaar (23° S)'], ['Noordpoolsirkel', 'ongeveer 66° noord van die ewenaar (66° N)'], ['Suidpoolsirkel', '66° suid van die ewenaar (66° S)']], page=87),
    text('Kyk op die kaart', 'Die kaart agter in die werkboek (bl. 88–89) wys die sewe kontinente en die groot oseane. Gebruik dit om die name op bladsy 86 in te vul.', bullets=['Kontinente op die kaart: Noord-Amerika, Suid-Amerika, Afrika, Europa, Asië, Oseanië en Antarktika.', 'Oseane op die kaart: die Noordelike en Suidelike Stille Oseaan, die Noord- en Suid-Atlantiese Oseaan, die Indiese Oseaan en die Arktiese See.'], page=86, src='workbook'),
  ],
  acts=[
    fill('Op watter kontinent?', 'Suid-Afrika lê in {{1}}.\nBrasilië lê in {{2}}.\nKanada lê in {{3}}.\nChina en Indië lê in {{4}}.\nFrankryk en Duitsland lê in {{5}}.\nDie koue kontinent by die Suidpool is {{6}}.\nAustralië en Nieu-Seeland lê in {{7}}.',
         {1: 'Afrika', 2: 'Suid-Amerika', 3: 'Noord-Amerika', 4: 'Asië', 5: 'Europa', 6: 'Antarktika', 7: ['Oseanië', 'Australië']},
         'Kyk op die wêreldkaart agter in die werkboek: elke land lê op die kontinent met sy naam langsaan.', bank=['Afrika', 'Suid-Amerika', 'Noord-Amerika', 'Asië', 'Europa', 'Antarktika', 'Oseanië'], prompt='Vul die sewe kontinente in.', src='workbook', page=86, item='kontinente', status='derived_from_text'),
    choices('Watter oseaan?', 'Kies die regte oseaan of see.', [('Die oseaan wat jy oorkruis om van Suid-Afrika na Australië te kom.', ['Indiese Oseaan', 'Arktiese See', 'Noordelike Stille Oseaan'], 0), ('Die oseaan aan Suid-Afrika se westekant.', ['Suid-Atlantiese Oseaan', 'Indiese Oseaan', 'Arktiese See'], 0), ('Die see in die verre noorde, bokant Kanada en Groenland.', ['Arktiese See', 'Suidelike Stille Oseaan', 'Suid-Atlantiese Oseaan'], 0)],
            'Die name staan op die wêreldkaart op bladsy 88–89 van die werkboek.', src='workbook', page=86, item='oseane', status='derived_from_text'),
    match('Pas die lyn by sy ligging', 'Verbind elke lyn op die kaart met sy ligging.', [('ewenaar', '0°'), ('Kreefskeerkring', '23° N'), ('Steenbokskeerkring', '23° S'), ('Noordpoolsirkel', '66° N'), ('Suidpoolsirkel', '66° S')], 'Dit is die inligting in die blokkie op bladsy 87.', src='workbook', page=87, item='byskrifte', status='official'),
    choices('Lengte- of breedtegrade?', 'Watter soort lyne is dit?', [('Hulle loop van oos na wes (van links na regs).', ['breedtegrade', 'lengtegrade'], 0), ('Hulle loop van die noordpool na die suidpool.', ['breedtegrade', 'lengtegrade'], 1), ('Die ewenaar is een van hierdie lyne.', ['breedtegrade', 'lengtegrade'], 0)],
            'Breedtegrade loop links na regs; lengtegrade loop bo na onder.', src='workbook', page=86, item='grade', status='official'),
    discuss('Skryf byskrifte op die kaart', 'Neem die kaart op bladsy 87 en skryf by elke lyn die regte naam en gradetal. Gebruik die inligting uit die blokkie. (Dit is ’n kaartaktiwiteit: werk in jou werkboek.)', page=87, item='Ons doen'),
    tf('Waar of onwaar?', 'Die Kreefskeerkring lê 23° suid van die ewenaar.', False, 'Dit is die Steenbokskeerkring wat 23° suid lê; die Kreefskeerkring lê 23° noord.', src='workbook', page=87, item='feit', status='official'),
  ],
  quiz=[
    q('literal', 'Hoeveel kontinente is daar?', 'Sewe', ['Vyf', 'Nege', 'Twaalf'], 'Die werkkaart se opskrif is “Die sewe kontinente”.', status='official', src='workbook', page=86),
    q('literal', 'Die breedtegrade loop van ...', 'oos na wes', ['noord na suid', 'bo na onder', 'wes na noord'], 'Breedtegrade loop van oos na wes (links na regs).', status='official', src='workbook', page=86),
    q('literal', 'Die lengtegrade loop van ...', 'die noordpool na die suidpool', ['oos na wes', 'links na regs', 'die ewenaar na die oseaan'], 'Lengtegrade loop van bo na onder.', status='official', src='workbook', page=86),
    q('literal', 'Wat is die ewenaar?', '’n Denkbeeldige lyn om die aarde se middellyn', ['’n Berg op die kaart', '’n Oseaan', '’n Land in Afrika'], 'Dit is die beskrywing op bladsy 87.', status='official', src='workbook', page=87),
    q('literal', 'Waar lê die Kreefskeerkring?', '23° noord van die ewenaar', ['23° suid van die ewenaar', '66° noord van die ewenaar', 'Op die ewenaar'], 'Die Kreefskeerkring lê 23° noord.', status='official', src='workbook', page=87),
    q('literal', 'Waar loop die Steenbokskeerkring?', '23° suid van die ewenaar', ['23° noord van die ewenaar', '66° suid van die ewenaar', 'By die noordpool'], 'Die Steenbokskeerkring loop 23° suid van die ewenaar.', status='official', src='workbook', page=87),
    q('literal', 'Hoeveel grade noord van die ewenaar is die Noordpoolsirkel ongeveer?', '66°', ['23°', '0°', '90°'], 'Die Noordpoolsirkel is ongeveer 66° noord.', status='official', src='workbook', page=87),
    q('inference', 'Hoe kom ons by die kontinent Oseanië?', 'Dit is die kontinent met Australië en Nieu-Seeland', ['Dit is die kontinent met Brasilië', 'Dit is die kontinent met Frankryk', 'Dit lê by die Noordpool'], 'Op die wêreldkaart is Australië en Nieu-Seeland in Oseanië.', status='derived_from_text', src='workbook', page=89, item='kaart'),
  ])

# ============================================================== 107 Vasvra oor die wêreldkaart
L107 = lesson(107,
  skills=[READ, LISTEN],
  intro='Speel die wêreldkaart-speletjie met ’n maat! Skiet ’n muntstuk op, skuif vorentoe en beantwoord die vrae met die hulp van die kaart.',
  objectives=['Inligting op ’n wêreldkaart opspoor.', 'Vrae oor lande, hoofstede, oseane en kompasrigtings beantwoord.', '’n Bordspeletjie met ’n maat speel.'],
  learn=[
    text('Hoe speel jy?', bullets=['Speel die speletjie saam met ’n maat.', 'Skiet ’n muntstuk op. As jy **kop** kry, skuif jy **twee plekke** vorentoe. As jy **munt** kry, skuif jy **net een plek** vorentoe.', 'Beantwoord elke vraag waarop jy land.', 'Kyk na die kaart om die antwoorde te kry.'], page=88),
    note('Die kompas op die kaart wys vir ons die vier hoofrigtings: noord (bo), suid (onder), oos (regs) en wes (links).', title='Kompasrigtings', page=88),
  ],
  acts=[
    discuss('Speel die speletjie', 'Speel die speletjie saam met ’n maat deur die vrae op die kaart (bl. 88–89) te beantwoord. Die vrae wissel van “In watter land woon jy?” tot “Hoekom word Somalië die horing van Afrika genoem?”', page=88, item='speletjie'),
    choices('Kompasrigtings op die kaart', 'Waar op die kaart?', [('Waar is noord op die kaart?', ['Bo', 'Onder', 'Links', 'Regs'], 0), ('Waar is suid op die kaart?', ['Bo', 'Onder', 'Links', 'Regs'], 1), ('Waar is oos op die kaart?', ['Bo', 'Onder', 'Links', 'Regs'], 3), ('Waar is wes op die kaart?', ['Bo', 'Onder', 'Links', 'Regs'], 2)],
            'Die kompas op die kaart wys: Noord bo, Suid onder, Oos regs, Wes links.', src='workbook', page=88, item='kompas', status='derived_from_text'),
    choices('Lande en kontinente', 'Kyk op die kaart.', [('Waar kom die piramides voor?', ['Egipte', 'Brasilië', 'Kanada'], 0), ('Waar is die Eiffeltoring?', ['Parys, Frankryk', 'Tokio, Japan', 'Washington, VSA'], 0), ('Watter oseaan oorkruis jy om van Suid-Afrika na Australië te kom?', ['Indiese Oseaan', 'Arktiese See', 'Noord-Atlantiese Oseaan'], 0), ('Noem ’n land in die suidelike deel van Afrika.', ['Namibië', 'Egipte', 'Marokko'], 0)],
            'Die kaart wys hierdie plekke en lande.', src='workbook', page=89, item='kaart', status='derived_from_text'),
    match('Hoofstad en land', 'Verbind elke hoofstad met sy land.', [('Windhoek', 'Namibië'), ('Brasília', 'Brasilië'), ('Washington D.C.', 'VSA'), ('Parys', 'Frankryk')], 'Hierdie hoofstede kom uit algemene kennis; die werkboek laat jou die antwoorde op die kaart of in ’n atlas opsoek.', src='supplementary', status='needs_review'),
    choices('Algemene kennis', 'Kies die beste antwoord.', [('Wat is die geldeenheid van die VSA?', ['Dollar', 'Rand', 'Euro'], 0), ('Wat is die geldeenheid van baie lande in Europa?', ['Euro', 'Dollar', 'Pond'], 0), ('Watter taal word in China gepraat?', ['Chinees (Mandaryns)', 'Frans', 'Japannees'], 0), ('Watter taal word in Australië gepraat?', ['Engels', 'Portugees', 'Duits'], 0), ('Wat is die grootste land in die wêreld?', ['Rusland', 'Kanada', 'Brasilië'], 0)],
            'Hierdie feite kom uit algemene kennis (nie uit ’n amptelike antwoordsleutel nie). Kyk jou antwoorde na in ’n atlas.', src='workbook', page=89, item='vrae', status='needs_review'),
    discuss('Dink na', 'Dink aan die vrae: Waarom verkluim ysbere en pikkewyne nie? Waarvan word ’n igloe gemaak? Woon pikkewyne net by die Suidpool? Bespreek met jou maat en kyk dan in ’n boek of op die internet.', page=88, item='dink'),
  ],
  quiz=[
    q('literal', 'Hoeveel plekke skuif jy vorentoe as jy “kop” kry?', 'Twee', ['Een', 'Drie', 'Vier'], 'Kop: twee plekke. Munt: een plek.', status='official', src='workbook', page=89),
    q('literal', 'Hoeveel plekke skuif jy vorentoe as jy “munt” kry?', 'Een', ['Twee', 'Drie', 'Geen'], 'Munt: net een plek vorentoe.', status='official', src='workbook', page=89),
    q('literal', 'Wat doen jy as jy op ’n vierkant land?', 'Beantwoord die vraag', ['Gaan terug na BEGIN', 'Skuif nog drie plekke', 'Laat jou maat antwoord'], 'Beantwoord elke vraag waarop jy land.', status='official', src='workbook', page=89),
    q('inference', 'Waar is noord op die kaart?', 'Bo', ['Onder', 'Links', 'Regs'], 'Op die kompas wys noord boontoe.', status='derived_from_text', src='workbook', page=88, item='kompas'),
    q('inference', 'Waar is oos op die kaart?', 'Regs', ['Links', 'Bo', 'Onder'], 'Oos is regs op die kompas.', status='derived_from_text', src='workbook', page=88, item='kompas'),
    q('inference', 'Watter oseaan oorkruis jy van Suid-Afrika na Australië?', 'Indiese Oseaan', ['Noordelike Stille Oseaan', 'Arktiese See', 'Noord-Atlantiese Oseaan'], 'Suid-Afrika en Australië lê aan weerskante van die Indiese Oseaan.', status='derived_from_text', src='workbook', page=89, item='kaart'),
    q('inference', 'In watter kontinent is die piramides?', 'Afrika', ['Asië', 'Europa', 'Oseanië'], 'Die piramides kom in Egipte voor – dit lê in Afrika.', status='derived_from_text', src='workbook', page=89, item='kaart'),
    q('inference', 'In watter land staan die Eiffeltoring?', 'Frankryk', ['Brasilië', 'Japan', 'Kanada'], 'Die kaart wys die Eiffeltoring by Parys in Frankryk.', status='derived_from_text', src='workbook', page=88, item='kaart'),
  ])

# ============================================================== 108 Soveel kulture
L108 = lesson(108,
  skills=[LISTEN, WRITE],
  intro='Suid-Afrika het baie kulture en godsdienste. Vandag gaan jy navorsing doen: voer ’n onderhoud met iemand van ’n ander geloof en leer meer oor ’n land.',
  objectives=['’n Onderhoud voer oor ’n godsdiens wat van joune verskil.', 'Antwoorde in ’n tabel aanteken.', 'Navorsing oor ’n land doen en die land op die kaart merk.'],
  learn=[
    text('Respek vir ander kulture', 'In Suid-Afrika het ons baie verskillende kulture en godsdienste.', bullets=['Voer ’n onderhoud met iemand **wie se godsdiens van joune verskil**.', 'Luister mooi en wees beleef: jy leer iets nuuts.', 'Skryf die antwoorde in die regterkantse kolom van die tabel.'], page=90),
    table('Vrae vir die onderhoud', ['Vraag'], [['Wie word in hierdie godsdiens aanbid?'], ['Waar vind die aanbidding plaas?'], ['Hoe dikwels aanbid julle?'], ['Watter godsdienstige seremonies, feeste of dienste het julle?'], ['Hoe trek die mense vir hierdie geleenthede aan?'], ['Aanbid die mans en vroue saam?']], page=90),
    text('Navorsing oor ’n land', bullets=['Kies ’n land en raadpleeg verskillende bronne.', 'Waar is die land – op watter kontinent? Merk die land op die kaart.', 'Wat is party van hulle gewoontes?', 'Watter ander interessante inligting kan jy nog opspoor?'], page=90),
  ],
  acts=[
    discuss('Ons doen: die onderhoud', 'Voer ’n onderhoud met iemand wie se godsdiens van joune verskil. Gebruik die vrae in die tabel en vul die antwoorde in die regterkantse kolom in.', page=90, item='onderhoud'),
    writing('Skryf die antwoorde', 'Skryf die antwoorde op die ses vrae neer: wie aanbid word, waar, hoe dikwels, seremonies/feeste/dienste, hoe mense aantrek, en of mans en vroue saam aanbid.', checklist=['Ek het ses vrae gevra.', 'Ek het die antwoorde neergeskryf.', 'Ek was beleef en het mooi geluister.'], lines=12, page=90, item='tabel'),
    order('Stappe vir jou navorsing', 'Sit die stappe in ’n sinvolle volgorde.', ['Kies ’n land.', 'Soek inligting in verskillende bronne.', 'Merk die land op die kaart.', 'Skryf party gewoontes en ander interessante inligting neer.'], 'Eers kies jy ’n land; dan soek jy inligting; dan merk en skryf jy.', perm=[1, 0, 3, 2], src='supplementary', status='derived_from_text'),
    writing('Navorsing oor my land', 'Skryf die naam van jou land, die kontinent, party gewoontes en nog interessante inligting neer.', checklist=['Ek het die land en kontinent geskryf.', 'Ek het gewoontes genoem.', 'Ek het interessante inligting bygevoeg.'], lines=8, page=90, item='land'),
    tf('Waar of onwaar?', 'Die onderhoud moet met iemand wees wie se godsdiens dieselfde as joune is.', False, 'Die werkboek vra vir iemand wie se godsdiens van joune verskil.', src='supplementary', status='official'),
  ],
  quiz=[
    q('main_idea', 'Met wie voer jy die onderhoud?', 'Iemand wie se godsdiens van joune verskil', ['Iemand met dieselfde godsdiens', 'Jou onderwyser alleen', 'Jou beste vriend/vriendin'], 'Die werkboek sê dit.', status='official', src='workbook', page=90),
    q('literal', 'Waar skryf jy die antwoorde neer?', 'In die regterkantse kolom van die tabel', ['In die kantlyn', 'Agter in die boek', 'Op die kaart'], 'Die werkboek sê: regterkantse kolom.', status='official', src='workbook', page=90),
    q('literal', 'Watter vraag is deel van die onderhoud?', 'Wie word in hierdie godsdiens aanbid?', ['Hoeveel is 2 + 2?', 'Wat is jou gunstelingkos?', 'Waar woon jy?'], 'Dit is die eerste vraag in die tabel.', status='official', src='workbook', page=90),
    q('literal', 'Watter vraag gaan oor die aanbidding se plek?', 'Waar vind die aanbidding plaas?', ['Hoe dikwels aanbid julle?', 'Wie word aanbid?', 'Aanbid mans en vroue saam?'], 'Dit is die tweede vraag in die tabel.', status='official', src='workbook', page=90),
    q('literal', 'Wat doen jy met die land wat jy kies?', 'Merk dit op die kaart', ['Skryf dit uit vir ’n vriend', 'Teken die vlag net', 'Niks'], 'Die werkboek sê: Merk die land op die kaart.', status='official', src='workbook', page=90),
    q('main_idea', 'Hoekom voer ons so ’n onderhoud?', 'Om meer oor ander kulture en godsdienste te leer', ['Om te wen', 'Om mense te laat verander', 'Om punte te verdien'], 'Suid-Afrika het baie verskillende kulture en godsdienste.', status='derived_from_text', src='workbook', page=90),
    q('main_idea', 'Hoe moet jy jou gedra tydens die onderhoud?', 'Beleef wees en mooi luister', ['Baie praat', 'Lag as dit snaaks is', 'Die persoon korrigeer'], 'Respek vir ander se geloof is belangrik.', status='needs_review', src='supplementary', page=90),
    q('literal', 'Wat moet jy by jou landnavorsing ook opspoor?', 'Interessante inligting', ['Die land se ouderdom', 'Net die vlag', 'Net die hoofstad'], 'Die werkboek vra vir gewoontes en nog interessante inligting.', status='official', src='workbook', page=90),
  ])

# ============================================================== 109 Ons behoort aan een familie
P109 = [
  'Ons woon almal op die planeet Aarde',
  'Ons is almal aardbewoners. Ons woon orals, in oorbevolkte stede en op klein dorpies. Ons woon op wit ysvelde en in groen, warm woude. Ons lewe in woestyne, teen berghange en op eilande in die see.',
  'Ons het vele verskillende kleure. Party van ons het warm, ligbruin velle soos sonlig op sand. Party van ons het donkerbruin velle soos ryk sjokolade. Ander het rosige pienk velle soos die lug teen dagbreek. En party van ons se velle wys ’n tikkie rooi. Ons oë en hare het ook verskillende kleure. Ons het blou oë, bruin oë, grou oë of groen oë. Ons hare is blond of bruin of rooi of swart. Dit kan reguit wees of krullerig.',
  'Ons het allerhande vorms en groottes. Party van ons is lank en ander is kort. Daar is dié wat maer is en ander wat mollig is. Ons het verskillende lewenswyses en baie uiteenlopende oortuigings en gewoontes. Ons hou van verskillende soorte kos. Ons bou ons huise op verskillende maniere. Ons behoort aan baie verskillende families, groepe, stamme en nasies.',
  'Maar ons is ook eners in baie belangrike opsigte. Ons het almal kos nodig om te lewe. Ons wil almal veilig, gemaklik en gelukkig wees. Ons het almal liefde en vriendskap nodig. Ons hou almal van mooi goed.',
  'En ons behoort almal aan een groot familie – die menslike familie van meer as 7 biljoen mense. Ons het almal dieselfde voorouers. Ja, ons is almal inwoners van die planeet Aarde, en ons het ons oorsprong hier, in Suid-Afrika, gehad.',
  'Alle mense het kos, klere en skuiling nodig om aan die lewe te bly. Ons eet egter nie dieselfde soorte kos nie. Ons dra nie dieselfde klere nie, en ons woon ook nie in dieselfde soorte huise nie. Ons gesinne en families verskil ook.',
  'Chloe behoort aan die Inuïetstam. (Tevore is hulle die Eskimo’s genoem.) Sy is 12 jaar oud. Sy woon in die noorde van Kanada. Sy en haar gesin woon in die koudste deel van die wêreld, en hulle dra klere wat van dierevelle gemaak is om warm te bly. Hulle eet walvisvet en die vleis van bere en robbe. Die ryk vet in hierdie kosse help hulle om hul liggaamshitte te behou. In die verlede het die Inuïet in sneeu-igloes of tente van dierevelle gewoon. Vandag woon hulle in verhitte huise.',
  'John woon in Engeland. Hy is nou 13, en hy gaan al skool vandat hy 3 jaar oud was. Hy hou van vis en skyfies. Hy dra skooldrag en ry in die somer per fiets skool toe. Hy is mal oor sokker.',
  'Rut woon in Israel, op ’n kibboets, ’n soort gemeenskaplike plaas. Sy is 11 jaar oud. Op ’n kibboets woon die ouers en kinders nie saam nie. Die ouers woon in ’n huis vir volwassenes en die kinders bly in ’n kinderhuis. Rut gaan op die plaas skool en eet middagete by die skool.',
  'Adel is 13 en woon op ’n dorp in Maleisië. Die dorp het net een huis. Hulle noem dit ’n “lang huis”, en dit kan tot 50 gesinne huisves. Die gesinne kies ’n hoof vir hulle lang huis.',
  'Kwi is 7 jaar oud. Hy woon in die woestyn in Botswana. Hy is ’n lid van die Sanmense. Sy pa jag wilde diere vir voedsel. Wanneer Kwi ouer is, sal hy na ’n koshuis toe gaan. Op die oomblik leer hy sy geskiedenis deur die liedjies en stories wat sy familielede hom vertel.',
  'Kofi is 11 jaar oud en kom van ’n dorpie in Ghana. Hy woon saam met sy ma en sy ma se ma in ’n Asjanti-huis. In hierdie huis noem Kofi al die vroue “ma”, en is al die kinders sy broers en susters.']
G109 = [('aardbewoners', 'Mense wat op die aarde woon.'), ('oorbevolkte', 'Met te veel mense.'), ('uiteenlopende', 'Baie verskillend.'), ('oortuigings', 'Dinge waarin iemand sterk glo.'), ('kibboets', '’n Gemeenskaplike plaas in Israel.'), ('huisves', 'Plek gee om te bly.'), ('voorouers', 'Mense uit wie se geslag ons afstam.'), ('skuiling', '’n Plek om te bly en beskerming te hê.')]

L109 = lesson(109,
  skills=[READ, WRITE],
  intro='Mense lyk verskillend, eet verskillende kos en woon op verskillende maniere – maar ons behoort almal aan een familie! Lees die stuk en leer ses kinders van oor die wêreld ken.',
  objectives=['’n Leesstuk oor mense en kulture verstaan.', 'Inligting in ’n tabel invul.', 'Meervoude en verkleinwoorde in ’n leesstuk herken en gebruik.'],
  pass_=passage('Ons behoort aan een familie', P109, glossary=G109),
  learn=[
    note('Die skrywer wys dat mense baie verskillend is, maar ook in belangrike dinge eners: ons het almal kos, veiligheid, liefde en vriendskap nodig.', title='Hoofgedagte', src='supplementary', page=92),
  ],
  acts=[
    sa('Sewe soorte plekke', 'Die outeur noem sewe verskillende soorte plekke waar mense woon. Maak ’n lys daarvan.', 'oorbevolkte stede\nklein dorpies\nwit ysvelde\ngroen, warm woude\nwoestyne\nberghange\neilande in die see', lines=7, page=92, item='1', status='derived_from_text'),
    sa('Vier opsigte waarin ons verskil', 'Noem die vier opsigte waarin mense volgens die skrywer verskil.', 'velkleur (en kleur van oë en hare)\nvorm en grootte (lank/kort, maer/mollig)\nlewenswyses, oortuigings en gewoontes (ook kos en huise)\nfamilies, groepe, stamme en nasies', lines=5, page=92, item='2', status='needs_review'),
    sa('Hoe is ons almal dieselfde?', 'In watter opsigte is ons almal dieselfde?', 'Ons het almal kos nodig om te lewe.\nOns wil almal veilig, gemaklik en gelukkig wees.\nOns het almal liefde en vriendskap nodig.\nOns hou almal van mooi goed.', lines=5, page=92, item='3', status='derived_from_text'),
    match('Wie is wie?', 'Verbind elke kind met die regte beskrywing.', [('Chloe', 'Inuïet, 12 jaar, noorde van Kanada'), ('John', '13 jaar, Engeland, mal oor sokker'), ('Rut', '11 jaar, kibboets in Israel'), ('Adel', '13 jaar, “lang huis” in Maleisië'), ('Kwi', '7 jaar, Sanmense in Botswana'), ('Kofi', '11 jaar, Asjanti-huis in Ghana')], 'Dit is die inligting uit die beskrywings op bladsy 93.', src='workbook', page=93, item='tabel', status='derived_from_text'),
    choices('Naam, land en kultuur', 'Kies die regte antwoord.', [('In watter land woon Chloe?', ['Kanada', 'Engeland', 'Ghana'], 0), ('Hoe oud is Kwi?', ['7', '11', '13'], 0), ('Waarvan maak Chloe se mense klere?', ['dierevelle', 'katoen', 'plastiek'], 0), ('Wat is ’n kibboets?', ['’n soort gemeenskaplike plaas', '’n tipe kos', '’n skool'], 0), ('Hoeveel gesinne kan in Adel se “lang huis” woon?', ['tot 50', 'net 2', 'tot 5'], 0)],
            'Elke antwoord staan in die beskrywings van die kinders.', src='workbook', page=93, item='tabel', status='derived_from_text'),
    sa('Meervoude en verkleinwoorde', 'Omkring 5 meervoudswoorde in die leesstuk. Skryf hulle en langs elke meervoud die verkleinwoord. Gebruik die verkleinwoorde in beskrywende sinne.', 'eilande – eilandjies\nvelle – velletjies\nhare – haartjies\nhuise – huisies\nstede – stedies (of: dorpies)\nVoorbeeldsin: Die klein huisie op die eilandjie was baie gesellig.', lines=6, page=92, item='4', status='needs_review'),
    tf('Waar of onwaar?', 'Die skrywer sê ons behoort almal aan een groot familie.', True, 'Dit staan in die laaste paragraaf van die leesstuk.', src='supplementary', status='official'),
  ],
  quiz=[
    q('main_idea', 'Waaroor gaan die leesstuk hoofsaaklik?', 'Mense is verskillend, maar behoort almal aan een familie', ['Hoe om ’n huis te bou', 'Waar die ysvelde is', 'Hoe om kos te kook'], 'Die skrywer sê ons is verskillend maar ook eners.', ev=['behoort almal aan een groot familie']),
    q('literal', 'Hoeveel mense is daar volgens die skrywer in die menslike familie?', 'Meer as 7 biljoen', ['Meer as 1 miljoen', 'Honderd', 'Presies 20'], 'Dit staan in die laaste paragraaf.', ev=['menslike familie van meer as 7 biljoen mense']),
    q('literal', 'Waar woon Chloe?', 'In die noorde van Kanada', ['In Engeland', 'In Ghana', 'In Botswana'], 'Sy woon in die noorde van Kanada.', ev=['Sy woon in die noorde van Kanada']),
    q('literal', 'Waarom eet die Inuïet walvisvet?', 'Die vet help hulle om hul liggaamshitte te behou', ['Dit is goedkoop', 'Dit smaak soet', 'Dit groei in sneeu'], 'Die ryk vet help hulle om warm te bly.', ev=['liggaamshitte te behou']),
    q('literal', 'Waarmee ry John in die somer skool toe?', 'Per fiets', ['Per bus', 'Per trein', 'Te voet'], 'Hy ry in die somer per fiets skool toe.', ev=['per fiets skool toe']),
    q('literal', 'Hoe leer Kwi sy geskiedenis?', 'Deur liedjies en stories van sy familielede', ['Uit boeke', 'Op die internet', 'Op skool'], 'Hy leer sy geskiedenis deur liedjies en stories.', ev=['liedjies en stories']),
    q('vocabulary', 'Wat is ’n kibboets?', '’n Soort gemeenskaplike plaas', ['’n Tipe kos', '’n Stam in Afrika', '’n Soort klere'], 'Rut woon op ’n kibboets, ’n soort gemeenskaplike plaas.', ev=['soort gemeenskaplike plaas']),
    q('inference', 'In watter opsig is alle mense eners?', 'Ons het almal liefde en vriendskap nodig', ['Ons eet dieselfde kos', 'Ons dra dieselfde klere', 'Ons het dieselfde kleur hare'], 'Die skrywer noem dat ons almal liefde en vriendskap nodig het.', ev=['liefde en vriendskap']),
  ])

# ============================================================== 110 Mevrou Ples en Little Foot
P110 = [
  'Wat is ’n erfenisterrein?',
  'Die Verenigde Nasies se Organisasie vir Wetenskap en Kultuur (UNESCO) vra dat regerings hulle moet laat weet watter terreine in hulle lande belangrik is, sodat die terreine bewaar kan word. UNESCO evalueer die terreine, en indien hulle belangrik genoeg is, word hulle tot Wêrelderfenisterreine verklaar.',
  'Suid-Afrika het agt Wêrelderfenisterreine, waarvan Robbeneiland een is. Nog ’n belangrike terrein is die Wieg van die Mensdom, wat wetenskaplikes as die oorsprong van die mens beskou.',
  'Waarom is hierdie terrein belangrik?',
  'In ’n grot wat aan Gauteng en Noordwes grens, naby Krugersdorp, is daar fossiele ontdek. Daar word geglo dat hierdie geraamtes behoort het aan party van die vroegste ampermense wat op die aarde geleef het.',
  'Hoe is die fossiele ontdek?',
  'Wetenskaplikes het in 1890 begin om die oorblyfsels van prehistoriese liggame op te grawe toe goudmynwerkers berig het dat hulle baie fossiele ondergronds kry. Die wetenskaplikes het fossiele gekry van die skelette van ampermense wat die aarde miljoene jare gelede bewandel het.',
  'In 1947 het dr Robert Broom die skedel van ’n volwasse vrou, ’n prehistoriese ampermens wat Plesianthropus transvaalensis genoem is, in die Sterkfonteingrot gevind. Hierdie naam was moeilik om te onthou, daarom het die skedel ’n bynaam gekry, naamlik Mev. Ples.',
  'Wanneer het sy geleef?',
  'Mev. Ples het miljoene jare gelede gelewe, voordat vuur ontdek of die eerste ystergereedskap gemaak is. Wetenskaplikes glo dat die eerste hominiede die voorsate van die moderne mens was, en dat die menslike ras in hierdie omgewing ontstaan het. Dit is waarom dit die Wieg van die Mensdom genoem word.',
  'Watter ander bewyse het ons dat die eerste mense uit Afrika gekom het?',
  'In 1995 het ’n ander wetenskaplike, Ronald Clarke, die oorblyfsels van nog ’n hominied in dieselfde gebied ontdek. Hierdie skelet is Little Foot genoem, omdat voetbeentjies die eerste dele van die skelet was wat die navorsers ontdek het.',
  'Weens die belangrikheid van hierdie ontdekkings het UNESCO die gebied rondom die grotte in 2000 tot Wêrelderfenisterrein verklaar.',
  'Beskerm ons Erfenis!',
  'Ons woon op ’n planeet wat gedurig besig is om te verander. Partykeer word die veranderinge deur natuurkragte soos aardbewings en die beweging van die oseane veroorsaak. Soms word die skade egter deur mense aangerig deurdat ons riviere en oseane besoedel en reënwoude verwoes. Al hierdie veranderinge veroorsaak dat ons iets verloor wat jou kinders dalk nooit sal sien nie, soos die reënwoude of koninklike diere soos die Bengaalse tier, wat byna uitgesterf het.',
  'Ons moet ons erfenis vir toekomstige generasies bewaar – vir jou kinders en kleinkinders.']
G110 = [('erfenisterrein', '’n Plek wat belangrik is vir die geskiedenis of natuur en bewaar moet word.'), ('fossiele', 'Oorblyfsels van plante of diere uit baie lank gelede.'), ('ampermense', 'Wesens wat amper soos mense was.'), ('prehistoriese', 'Van voor die geskiedenis geskryf is.'), ('hominiede', 'Mensagtige wesens uit die vroegste tye.'), ('oorsprong', 'Waar iets begin het.'), ('evalueer', 'Beoordeel of iets goed of belangrik genoeg is.'), ('uitgesterf', 'Nie meer op die aarde bestaan nie.')]

L110 = lesson(110,
  skills=[READ, LANG],
  intro='Ontmoet Mev. Ples en Little Foot – twee baie ou skelette! Lees die internetverslag oor die Wieg van die Mensdom en leer wat ’n erfenisterrein is.',
  objectives=['’n Internetverslag lees en verstaan.', 'Belangrike feite oor die Wieg van die Mensdom noem.', 'Afkortings, akronieme, samestellings en afleidings herken.'],
  pass_=passage('Mevrou Ples en Little Foot', P110, glossary=G110),
  learn=[
    note('’n **Afkorting** is ’n verkorte woord (bv. Mev., dr). ’n **Akroniem** is ’n afkorting wat as een woord uitgespreek word (bv. UNESCO).', title='Afkortings en akronieme', src='supplementary', page=95),
    note('**Samestelling** = basis + basis (bv. goudmynwerkers). **Afleiding** = basis + voor-/agtervoegsel (bv. wetenskaplikes).', title='Samestellings en afleidings', src='supplementary', page=95),
  ],
  acts=[
    match('Wanneer het dit gebeur?', 'Verbind elke gebeurtenis met die regte jaar.', [('Wetenskaplikes begin fossiele opgrawe', '1890'), ('Dr Robert Broom vind Mev. Ples', '1947'), ('Ronald Clarke ontdek Little Foot', '1995'), ('UNESCO verklaar die gebied ’n Wêrelderfenisterrein', '2000')], 'Die jare staan in die internetverslag.', src='workbook', page=94, item='verslag', status='derived_from_text'),
    choices('Wie of wat?', 'Kies die regte antwoord.', [('Hoeveel Wêrelderfenisterreine het Suid-Afrika?', ['agt', 'drie', 'twaalf'], 0), ('Hoekom is Mev. Ples se bynaam so genoem?', ['Die wetenskaplike naam was moeilik om te onthou', 'Sy was baie ryk', 'Sy het by Ples gewoon'], 0), ('Hoekom is Little Foot so genoem?', ['Voetbeentjies was die eerste dele wat ontdek is', 'Sy voete was baie klein', 'Hy kon vinnig hardloop'], 0), ('Waar is die fossiele ontdek?', ['In ’n grot naby Krugersdorp', 'In Kaapstad', 'Op Robbeneiland'], 0)],
            'Die verslag gee hierdie inligting.', src='workbook', page=94, item='verslag', status='derived_from_text'),
    fill('Afkortings en akroniem', 'In die leesstukke is die afkortings {{1}} en {{2}}, en die akroniem is {{3}}.', {1: ['Mev.', 'dr'], 2: ['dr', 'Mev.'], 3: 'UNESCO'}, 'Afkortings: Mev. (Mevrou), dr (doktor). Akroniem: UNESCO – uitgespreek as een woord.', prompt='Omkring die afkortings met blou en die akroniem met rooi.', src='workbook', page=95, item='kleur', status='derived_from_text'),
    sa('Samestellings en afleidings', 'Onderstreep 5 samestellings (groen) en 5 afleidings (oranje) in die leesstukke. Skryf hulle hier neer.', 'Samestellings: erfenisterrein, goudmynwerkers, ampermense, ystergereedskap, Wêrelderfenisterreine\nAfleidings: wetenskaplikes, veranderinge, ontdekkings, belangrikheid, besoedel', lines=4, page=95, item='kleur', status='needs_review'),
    sa('Skryf in jou eie woorde', 'Skryf in een sin waarom die Wieg van die Mensdom belangrik is.', 'Wetenskaplikes glo die menslike ras het in hierdie omgewing ontstaan, want daar is baie fossiele van die vroegste ampermense gevind.', lines=3, page=95, item='belang', status='needs_review'),
    tf('Waar of onwaar?', 'Mev. Ples is in 1995 gevind.', False, 'Mev. Ples is in 1947 gevind; Little Foot in 1995.', src='workbook', page=95, item='feit', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Waarvoor staan UNESCO se werk?', 'Dit evalueer belangrike terreine en verklaar hulle tot Wêrelderfenisterreine', ['Dit bou mense se huise', 'Dit maak fossiele', 'Dit verkoop kos'], 'UNESCO evalueer terreine.', ev=['UNESCO evalueer die terreine']),
    q('literal', 'Hoeveel Wêrelderfenisterreine het Suid-Afrika?', 'Agt', ['Drie', 'Een', 'Dertig'], 'Die verslag sê agt.', ev=['agt Wêrelderfenisterreine']),
    q('literal', 'Waar is die fossiele ontdek?', 'In ’n grot naby Krugersdorp', ['Op Robbeneiland', 'In die Kalahari', 'By ’n rivier in Natal'], 'Dit is in ’n grot naby Krugersdorp ontdek.', ev=['naby Krugersdorp']),
    q('literal', 'Wie het Mev. Ples se skedel gevind?', 'Dr Robert Broom', ['Ronald Clarke', 'UNESCO', 'Goudmynwerkers'], 'Dr Robert Broom het dit in 1947 gevind.', ev=['dr Robert Broom']),
    q('literal', 'Waarom het die skedel die bynaam “Mev. Ples” gekry?', 'Die wetenskaplike naam was moeilik om te onthou', ['Sy was mevrou', 'Dit is ’n grap', 'Sy naam was Ples'], 'Die naam Plesianthropus transvaalensis was moeilik.', ev=['moeilik om te onthou']),
    q('literal', 'Wie het Little Foot ontdek?', 'Ronald Clarke', ['Robert Broom', 'UNESCO', 'Mev. Ples'], 'In 1995 het Ronald Clarke dit ontdek.', ev=['Ronald Clarke']),
    q('inference', 'Hoekom word die gebied die “Wieg van die Mensdom” genoem?', 'Wetenskaplikes glo die menslike ras het daar ontstaan', ['Daar word baie babas gebore', 'Dit lyk soos ’n wieg', 'Dit is ’n kinderhuis'], 'Die menslike ras het in hierdie omgewing ontstaan.', ev=['menslike ras in hierdie omgewing ontstaan']),
    q('inference', 'Wat moet ons met ons erfenis doen?', 'Dit bewaar vir toekomstige generasies', ['Dit verkoop', 'Dit vergeet', 'Dit afbreek'], 'Ons moet ons erfenis bewaar.', ev=['erfenis vir toekomstige generasies bewaar']),
  ])

# ============================================================== 111 Ons erfenis
L111 = lesson(111,
  skills=[READ, WRITE],
  intro='Waarom moet ons ons erfenis beskerm? Bespreek en skryf, en maak dan ’n oorredende plakkaat om mense na die Wieg van die Mensdom te lok.',
  objectives=['Bespreek wat ’n erfenisterrein is en waarom die Wieg van die Mensdom belangrik is.', '’n Oorredende plakkaat ontwerp.', 'Oorredende woorde en prente gebruik.'],
  learn=[
    text('Wat is oorreding?', bullets=['Jou plakkaat moet **probeer om mense te oorreed** om die Wieg van die Mensdom te besoek.', 'Gebruik dus **oorredende woorde** en **prentjies**.', 'Jy kan die internetverslag en die koerantberig op bladsy 10 weer lees om jou te help.'], page=96),
    note('Oorredende woorde: “moet”, “ongelooflik”, “nooit weer”, “jy sal dit nie wil mis nie”, “kom”, “beleef”.', title='Voorbeelde', src='supplementary', page=96),
  ],
  acts=[
    sa('Bespreek en skryf: erfenisterrein', 'Bespreek met jou maat en skryf die antwoord: Wat is ’n erfenisterrein?', '’n Terrein wat so belangrik is dat dit bewaar moet word; UNESCO verklaar dit tot ’n Wêrelderfenisterrein.', lines=3, page=96, item='1', status='needs_review'),
    sa('Bespreek en skryf: Wieg van die Mensdom', 'Waarom is die Wieg van die Mensdom vir ons as Suid-Afrikaners so belangrik?', 'Daar is baie fossiele gevind, en wetenskaplikes glo die mensdom het hier ontstaan. Dit is trots, toerisme en erfenis vir ons.', lines=4, page=96, item='2', status='needs_review'),
    choices('Oorredend of net inligting?', 'Watter sin probeer jou oorreed?', [('Kom besoek die Wieg van die Mensdom – jy sal dit nooit vergeet nie!', ['oorredend', 'net inligting'], 0), ('Die Sterkfonteingrot is naby Krugersdorp.', ['oorredend', 'net inligting'], 1), ('Jy moet hierdie ongelooflike plek self beleef!', ['oorredend', 'net inligting'], 0), ('UNESCO het die gebied in 2000 tot Wêrelderfenisterrein verklaar.', ['oorredend', 'net inligting'], 1)],
            'Oorredende sinne gebruik bevele, uitroepe en sterk woorde om jou te laat wil besoek.', src='supplementary', status='derived_from_rule'),
    writing('Maak ’n plakkaat', 'Lees weer die internetverslag oor die Wieg van die Mensdom, en maak ’n plakkaat om dit as Wêrelderfenisterrein te adverteer. Gebruik oorredende woorde en prentjies.', checklist=['My plakkaat het ’n duidelike opskrif.', 'Ek het oorredende woorde gebruik.', 'Ek het ’n prent of prente.', 'Ek het gewys waar die terrein is.', 'Ek het spelfoute reggemaak.'], lines=10, page=97, item='plakkaat'),
    tf('Waar of onwaar?', 'Jou plakkaat moet net inligting gee en hoef nie oorredend te wees nie.', False, 'Die werkboek sê jou plakkaat moet probeer om mense te oorreed.', src='workbook', page=96, item='plakkaat', status='official'),
  ],
  quiz=[
    q('main_idea', 'Wat moet jou plakkaat probeer doen?', 'Mense oorreed om die Wieg van die Mensdom te besoek', ['Mense bang maak', 'Net sommer teken', 'Die grot verkoop'], 'Dit is die doel van die plakkaat.', status='official', src='workbook', page=96),
    q('literal', 'Wat moet jy op die plakkaat gebruik?', 'Oorredende woorde en prentjies', ['Net lang sinne', 'Net getalle', 'Net kaarte'], 'Gebruik oorredende woorde en prentjies.', status='official', src='workbook', page=96),
    q('literal', 'Wat kan jy lees om jou te help?', 'Die internetverslag en die koerantberig', ['Net die sportblad', 'Jou maat se plakkaat', 'Niks'], 'Jy kan die verslag en die koerantberig op bladsy 10 lees.', status='official', src='workbook', page=96),
    q('inference', 'Watter sin is oorredend?', 'Kom beleef die Wieg van die Mensdom – dis ’n onvergeetlike dag!', ['Die grot is naby Krugersdorp.', 'Dit het in 1947 gebeur.', 'UNESCO het dit verklaar.'], 'Dit gebruik ’n bevel en ’n uitroep om te oorreed.', status='derived_from_rule', src='supplementary'),
    q('inference', 'Watter woord is oorredend?', 'ongelooflik', ['gister', 'grot', 'jaar'], 'Dit is ’n sterk, aanloklike woord.', status='derived_from_rule', src='supplementary'),
    q('main_idea', 'Hoekom adverteer ons ’n erfenisterrein?', 'Sodat meer mense dit besoek en leer waarom dit belangrik is', ['Om dit te verkoop', 'Om dit te sluit', 'Om dit te vergeet'], 'Die plakkaat wil mense oorreed om te besoek.', status='derived_from_text', src='workbook', page=96),
    q('literal', 'Waar moet jy eers lees voor jy die plakkaat maak?', 'Die internetverslag oor die Wieg van die Mensdom', ['’n Storieboek', 'Die TV-gids', 'Die weerkaart'], 'Lees weer die internetverslag.', status='official', src='workbook', page=96),
    q('main_idea', 'Wat bespreek jy met jou maat?', 'Wat ’n erfenisterrein is en waarom die Wieg van die Mensdom belangrik is', ['Wat jy vir middagete het', 'Wie die beste teken', 'Hoe jy skool toe kom'], 'Dit is die twee vrae op bladsy 96.', status='official', src='workbook', page=96),
  ])

# ============================================================== 112 Beplan 'n pamflet
L112 = lesson(112,
  skills=[WRITE, READ],
  intro='Ontwerp ’n toerismebrosjure vir die Wieg van die Mensdom (of ’n ander Wêrelderfenisterrein). Beplan eers, skryf, laat ’n maat hersien en skryf dan jou finale weergawe.',
  objectives=['’n Toerismebrosjure beplan op ’n grafiese organiseerder.', 'Beskrywende taal en relevante inligting gebruik.', 'Jou werk hersien en korrigeer.'],
  learn=[
    text('Jou toerismebrosjure', bullets=['Ontwerp die brosjure om die Wieg van die Mensdom of enige ander Wêrelderfenisterrein te adverteer.', '**Voorblad:** wys die ligging van die terrein en gee ’n leuse of slagspreuk.', 'Teken op elk van die ander bladsye ’n prent en skryf ’n beskrywing van wat die besoeker sal sien.', 'Sluit die adres van die terrein, toegangsgeld en openings- en sluitingstye in.', '**Agterblad:** algemene inligting soos jou telefoonnommer, adres en e-posadres.'], page=98),
    text('Die proses', bullets=['**Beplan** jou brosjure op die grafiese organiseerder.', 'Skryf jou **eerste weergawe** in jou klaswerkboek.', 'Laat ’n maat jou werk **hersien**.', '**Korrigeer** spelfoute en punktuasie.', 'Skryf jou **finale weergawe** op die uitgeskeurde brosjure.'], page=98),
  ],
  acts=[
    order('Die skryfproses', 'Sit die stappe in die regte volgorde.', ['Beplan op die grafiese organiseerder.', 'Skryf die eerste weergawe in jou klaswerkboek.', 'Laat ’n maat jou werk hersien.', 'Korrigeer spelfoute en punktuasie.', 'Skryf die finale weergawe op die brosjure.'], 'Dit is die volgorde wat die werkboek gee.', perm=[2, 0, 4, 1, 3], src='workbook', page=98, item='proses', status='official'),
    match('Pas die blok by die inhoud', 'Verbind elke blok van die organiseerder met wat daarin hoort.', [('Blok 1', 'Voorblad en leuse/slagspreuk'), ('Blok 2 tot 5', 'Relevante inligting met ’n prent en beskrywing'), ('Blok 6', 'Kontakbesonderhede en adres')], 'Dit is hoe die organiseerder op bladsy 98 ingedeel is.', src='workbook', page=98, item='organiseerder', status='derived_from_text'),
    writing('Blok 1: voorblad en leuse', 'Wat gaan jy op jou voorblad plaas? Wat gaan jou leuse of slagspreuk wees?', checklist=['Ek het gesê wat op die voorblad kom.', 'Ek het ’n pakkende leuse geskryf.'], lines=4, page=98, item='blok 1'),
    writing('Blokke 2 tot 5: relevante inligting', 'Skryf relevante inligting vir blokke 2 tot 5. Beskryf wat die besoeker sal sien, en sluit adres, toegangsgeld en openings- en sluitingstye in.', checklist=['Ek het beskrywende woorde gebruik.', 'Ek het die adres genoem.', 'Ek het toegangsgeld en tye genoem.'], lines=12, page=98, item='blokke 2–5'),
    writing('Blok 6: kontakbesonderhede', 'Verstrek jou kontakbesonderhede en adres.', checklist=['Telefoonnommer', 'Adres', 'E-posadres'], lines=4, page=98, item='blok 6'),
    discuss('Hersien met ’n maat', 'Laat ’n maat jou eerste weergawe hersien. Wat is goed? Wat kan beter? Korrigeer dan spelfoute en punktuasie en skryf jou finale weergawe op die uitgeskeurde brosjure.', page=98, item='hersiening'),
    tf('Waar of onwaar?', 'Die agterblad bevat algemene inligting soos telefoonnommer, adres en e-posadres.', True, 'Dit staan by die agterblad (blok 6).', src='workbook', page=99, item='agterblad', status='official'),
  ],
  quiz=[
    q('main_idea', 'Wat adverteer jy met jou brosjure?', 'Die Wieg van die Mensdom of ’n ander Wêrelderfenisterrein', ['’n Winkel', '’n Skool', '’n Sokkerspan'], 'Dit is die opdrag.', status='official', src='workbook', page=98),
    q('literal', 'Wat moet op die voorblad wees?', 'Die ligging van die terrein en ’n leuse of slagspreuk', ['Net die prys', 'Die onderwyser se naam', 'Niks'], 'Die voorblad wys die ligging en bevat ’n leuse.', status='official', src='workbook', page=98),
    q('literal', 'Wat moet jy op elke ander bladsy doen?', 'Teken ’n prent en skryf ’n beskrywing van wat die besoeker sal sien', ['Net kopieer', 'Net ’n kaart teken', 'Net getalle skryf'], 'Dit is wat die werkboek vra.', status='official', src='workbook', page=98),
    q('literal', 'Watter inligting moet jy insluit?', 'Adres, toegangsgeld, openings- en sluitingstye', ['Net die datum', 'Net die ouderdom van die terrein', 'Net die naam'], 'Onthou die adres, toegangsgeld en tye.', status='official', src='workbook', page=98),
    q('literal', 'Waar skryf jy jou eerste weergawe?', 'In jou klaswerkboek', ['Op die brosjure', 'Op die bord', 'Op die plakkaat'], 'Die eerste weergawe gaan in jou klaswerkboek.', status='official', src='workbook', page=98),
    q('sequencing', 'Wat doen jy ná die eerste weergawe?', 'Laat ’n maat jou werk hersien', ['Skryf die finale weergawe', 'Gooi dit weg', 'Plak dit op die muur'], 'Eerste weergawe, dan hersien, dan korrigeer, dan finale weergawe.', status='official', src='workbook', page=98),
    q('literal', 'Wat korrigeer jy?', 'Spelfoute en punktuasie', ['Die prente', 'Die foon', 'Die kaart'], 'Korrigeer spelfoute en punktuasie.', status='official', src='workbook', page=98),
    q('literal', 'Wat moet jy in jou paragrawe gebruik?', 'Beskrywende woorde', ['Net getalle', 'Net bevele', 'Net vrae'], 'Onthou om beskrywende woorde te gebruik.', status='official', src='workbook', page=98),
  ])
