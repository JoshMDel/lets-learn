import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lessonkit import *

EK_KAN_T8 = ['’n verhalende teks lees.', 'vrae op grond van ’n teks beantwoord.', '’n toepaslike slot vir ’n storie bespreek.', '’n einde vir ’n storie rolspeel en dit vir die klas aanbied.', '’n alternatiewe slot vir ’n storie bedink.',
             '’n dagboekinskrywing in die eerste persoon skryf.', 'die negatiewe vorm en kontraksies gebruik.', '’n storie of sprokie skryf en op die karakters, intrige, agtergrond en gebeure konsentreer.',
             'sinne wat oorsaak en gevolg uitdruk, verbind.', 'voegwoorde gebruik.', '’n beskrywende paragraaf gebruik.', '’n biografie lees.', 'werkwoorde, bywoorde en voorsetsels identifiseer.', 'gedigte lees.',
             '’n gedig dramatiseer.', 'rymwoorde in ’n gedig identifiseer.', '’n gedig hardop lees.', '’n karakterbeskrywing bespreek.', 'vrae wat op ’n gedig gebaseer is, beantwoord.', '’n gedig skryf.',
             '’n rolspel oor ’n gedig opmaak.', 'limerieke lees.', 'vrae wat op limerieke gebaseer is, beantwoord.', '’n limeriek skryf.', 'voorbeelde van vergelykings voorsien.',
             'voorbeelde van die onderskeie digmiddele (soos metafore) voorsien.', '’n formele brief skryf.']

# ============================================================== 124 Limerieke
P124 = poem('Limerieke', [
  ['Daar was eens ’n knaap genaamd Klaas,', 'Hy dog hy weet baie maar ai tog helaas.', 'Hy glo dat ’n haai', 'Sou vlug as jy paai.', 'Toe swem hy die see in … arme dwaas!'],
  ['’n Werker woonagtig in Koffiefontein,', 'Kom af op twee pragtige meisies so klein.', 'Hy sê met ’n sug,', 'Terwyl hy vryf aan sy rug', '“Die bank waarop julle sit is pas gelym.”'],
  ['Daar was ’n jong vrou van die Kaap,', 'Sy kon net glad nie ophou gaap.', 'Sy’t alles probeer,', 'Al maak dit ook seer.', 'En nou voel sy natuurlik ’n regte swaap.']],
  glossary=[('knaap', '’n Seun of jong man.'), ('paai', 'Vriendelik probeer maak dat iemand of iets goedgesind is.'), ('dwaas', '’n Mens wat onverstandig optree.'), ('woonagtig', 'Woon in.'), ('gelym', 'Met gom vasgeplak.'), ('swaap', 'Iemand wat dom of simpel is (onvriendelike gesegde).')])

L124 = lesson(124,
  skills=[READ, WRITE],
  intro='Limerieke is vyfreëlige snaakse gedigte met ’n spesiale rympatroon. Lees ’n paar, beantwoord vrae en skryf jou eie!',
  objectives=['Limerieke lees en geniet.', 'Die eienskappe van ’n limeriek noem (5 reëls, rym aabba, humoristies).', 'Vergelykings en metafore uitken.', '’n Eie limeriek skryf.'],
  pass_=P124,
  learn=[
    text('Wat is ’n limeriek?', bullets=['Dit bestaan uit **5 reëls**.', 'Die rym is **aabba**: reël 1, 2 en 5 rym met mekaar en reël 3 en 4 rym met mekaar.', 'Dit is **humoristies** (snaaks).'], page=125),
    note('’n **Vergelyking** gebruik die woord **soos** om twee dinge wat eners is, met mekaar te vergelyk. Voorbeeld: Hy is so trots soos ’n pou.', title='Vergelyking', page=124),
    note('’n **Metafoor** vergelyk twee dinge deur te sê dat die een ding ’n ander ding is. Die woord “soos” word nie gebruik nie. Voorbeeld: Sy het ’n hart van goud.', title='Metafoor', page=124),
  ],
  acts=[
    discuss('Lees die limerieke', 'Lees hierdie limerieke hardop en geniet die humor.', speak='passage', page=124, item='Ons lees'),
    choices('Eienskappe van ’n limeriek', 'Is dit ’n eienskap van ’n limeriek?', [('Dit bestaan uit 5 reëls.', ['ja', 'nee'], 0), ('Die rym is aabba.', ['ja', 'nee'], 0), ('Dit is humoristies.', ['ja', 'nee'], 0), ('Dit het altyd 10 reëls.', ['ja', 'nee'], 1), ('Dit is altyd baie hartseer.', ['ja', 'nee'], 1)],
            'Die werkboek gee drie eienskappe: 5 reëls, rym aabba en humoristies.', src='workbook', page=125, item='eienskappe', status='official'),
    sa('Hoeveel reëls? Watter reëls rym?', 'Hoeveel reëls het ’n limeriek? Watter reëls rym met mekaar?', 'Vyf reëls. Reël 1, 2 en 5 rym met mekaar (a), en reël 3 en 4 rym met mekaar (b): aabba.', lines=3, page=125, item='1–2', status='derived_from_text'),
    match('Rymwoorde in die eerste limeriek', 'Verbind die woorde wat in die limeriek oor Klaas rym.', [('Klaas', 'helaas'), ('helaas', 'dwaas'), ('haai', 'paai')], 'Reël 1, 2 en 5 rym (Klaas, helaas, dwaas); reël 3 en 4 rym (haai, paai).', src='workbook', page=124, item='limeriek 1', status='derived_from_text'),
    choices('Vergelyking of metafoor?', 'Kies die regte antwoord.', [('Hy is so trots soos ’n pou.', ['vergelyking', 'metafoor'], 0), ('Sy het ’n hart van goud.', ['vergelyking', 'metafoor'], 1), ('Sy is so slim soos ’n uil.', ['vergelyking', 'metafoor'], 0), ('Die klas was ’n sirkus.', ['vergelyking', 'metafoor'], 1)],
            'Vergelyking gebruik “soos”; metafoor sê dat iets ’n ander ding ís.', src='workbook', page=124, item='beeldspraak', status='derived_from_rule'),
    writing('Skryf jou eie limeriek (San)', 'Maak ’n lys van al die woorde wat met “San” rym (bv. Jan, kan, dan). Skryf dan jou eie limeriek wat so begin: “Daar was ’n jong vrou genaamd San,”', checklist=['Ek het ’n rymlys gemaak.', 'My limeriek het 5 reëls.', 'Die rym is aabba.', 'My limeriek is snaaks.'], lines=7, page=125, item='San'),
    writing('Of probeer die “Ben”-limeriek', 'Of probeer hierdie een: “Daar was ’n jong man genaamd Ben,” en gebruik woorde wat met “Ben” rym (bv. hen, pen, ken).', checklist=['My limeriek het 5 reëls.', 'Die rym is aabba.', 'My limeriek is snaaks.'], lines=7, page=125, item='Ben'),
    tf('Waar of onwaar?', 'In ’n limeriek rym reël 3 en 4 met mekaar.', True, 'Die rym is aabba: reël 3 en 4 (b) rym.', src='workbook', page=125, item='rym', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Hoeveel reëls het ’n limeriek?', 'Vyf', ['Vier', 'Ses', 'Agt'], 'Dit bestaan uit 5 reëls.', status='official', src='workbook', page=125),
    q('literal', 'Wat is die rymskema van ’n limeriek?', 'aabba', ['aabb', 'abab', 'abcde'], 'Die rym is aabba.', status='official', src='workbook', page=125),
    q('literal', 'Hoe moet ’n limeriek wees?', 'Snaaks', ['Hartseer', 'Sag', 'Lank'], 'Dit is humoristies.', status='official', src='workbook', page=125),
    q('literal', 'Hoe heet die knaap in die eerste limeriek?', 'Klaas', ['Ben', 'Jan', 'San'], 'Daar was eens ’n knaap genaamd Klaas.', ev=['Daar was eens ’n knaap genaamd Klaas']),
    q('inference', 'Wat gebeur met Klaas?', 'Hy swem die see in omdat hy dink haaie vlug as jy paai', ['Hy word ’n haai', 'Hy leer swem', 'Hy vang ’n haai'], 'Die limeriek sê: “Toe swem hy die see in … arme dwaas!”', ev=['Toe swem hy die see in']),
    q('literal', 'Waar woon die werker in die tweede limeriek?', 'Koffiefontein', ['Kaapstad', 'Paarl', 'Durban'], 'Dit staan in reël 1.', ev=['woonagtig in Koffiefontein']),
    q('inference', 'Wat is snaaks aan die jong vrou van die Kaap?', 'Sy kon nie ophou gaap nie en voel nou soos ’n swaap', ['Sy kan nie praat nie', 'Sy slaap in die klas', 'Sy kry ’n prys'], 'Sy kon net glad nie ophou gaap nie.', ev=['Sy kon net glad nie ophou gaap']),
    q('grammar', 'Watter soort beeldspraak is “Sy het ’n hart van goud”?', 'Metafoor', ['Vergelyking', 'Personifikasie', 'Alliterasie'], 'Daar is geen “soos” nie.', status='official', src='workbook', page=124),
  ])

# ============================================================== 125 Pret met poësie
P125 = poem('Ek gaan stap met my iguana', [
  ['Ek gaan stap', 'Met my iguana', 'Wanneer die temperatuur begin', 'Styg bo tagtig en nog vyf,', 'Kry my iguana lewe', 'In sy skubbelyf.'],
  ['Dan gaan ek gou-gou see toe,', 'My iguana aan die band,', 'Daar klim hy op my skouer', 'Terwyl ons wandel langs die strand…'],
  ['As iemand op ons afkom', 'gee hulle ons meer as een kyk,', 'ek en my iguana wat', 'oor die sand aanstryk,'],
  ['Tot mense die polisie bel', 'Om ’n klag te lê', 'want mag mens ’n alligator', 'aan ’n leiband hê?'],
  ['Dis oor die stekels op sy rug', 'dat mense dink hy’s kwaai,', 'maar kielie hom onder die ken', 'dan lag hy dat hy kraai.'],
  ['En ek weet my ou iguana', 'wil beslis gaan slaap', 'as hy sy nagklere aantrek', 'En begin te gaap.'],
  ['En ek gaan stap', 'Met my iguana…', 'Met my iguana…', 'En my piranha…', 'En my chihuahua', 'En my chinchilla,', 'Met my gorilla,', 'My skoenlapperlarwe…', 'En ek gaan stap', 'Met my iguana…']],
  glossary=[('iguana', '’n Groot akkedis met stekels op sy rug.'), ('skubbelyf', 'Liggaam met skubbe.'), ('aanstryk', 'Rustig aangestap kom.'), ('alligator', '’n Reptiel soos ’n krokodil, maar met ’n korter snoet.'), ('leiband', '’n Riem om ’n dier aan te lei.'), ('stekels', 'Skerp punte op ’n dier se vel.'), ('kraai', 'Hard lag.')])

L125 = lesson(125,
  skills=[READ, LISTEN],
  intro='Kan jy met ’n iguana gaan stap? Lees ’n snaakse gedig van Brian Moses, leer snaakse dierename en beantwoord vrae oor die gedig.',
  objectives=['’n Gedig lees en geniet.', 'Dierename met hul betekenisse verbind.', 'Vrae oor die gedig beantwoord.', 'Rymwoorde in die gedig opspoor.'],
  pass_=P125,
  learn=[
    text('Die VN voeg ’n paar iguanas by sy lys van bedreigde spesies', '22 Maart 2010 – Die Verenigde Nasies se Omgewingsprogram (UNEP) het verskeie reptiele by sy lys van bedreigde spesies gevoeg. Die doel van hierdie lys is om mense oor die hele wêreld te verbied om handel te dryf met diere wat deur uitwissing bedreig word.', 'Vier iguanaspesies is by die lys gevoeg. Beskermde iguanas word gevang en veral in Europa en die Verenigde State aan mense verkoop wat hulle as ongewone, eksotiese troeteldiere wil aanhou. Omdat hierdie iguanaspesies nou op die lys verskyn, kan regerings handel in die reptiele reguleer.', page=126),
  ],
  acts=[
    discuss('Ons praat', 'Bespreek: Het jy al ooit ’n iguana gesien? Hoe lyk hulle? Hoe voel dit om aan een te vat?', page=126, item='Ons praat'),
    match('Dierename en betekenisse', 'Spreek die dierename uit en luister na die klanke. Verbind elke woord met die korrekte betekenis.', [('piranha', 'vis met skerp tande'), ('chinchilla', 'klein knaagdier met ’n welige stert'), ('chihuahua', 'klein hondsoort'), ('gorilla', 'groot aap'), ('skoenlapperlarwe', 'lyk soos ’n wurm en kan helderkleurig wees'), ('alligator', 'soos ’n krokodil maar met ’n korter snoet')], 'Hierdie dierename kom in die gedig voor.', src='workbook', page=127, item='woorde', status='derived_from_text'),
    sa('Stap hy regtig met die iguana?', 'Dink jy die skrywer gaan regtig met sy iguana stap, of is dit net ’n prettige gedig? Waarom sê jy so?', 'Dit is waarskynlik net ’n prettige gedig – dit gaan oor ’n snaakse idee, en hy stap ook met ’n piranha en ’n gorilla.', lines=3, page=127, item='1', status='needs_review'),
    fill('Temperatuur', 'Die skrywer noem dat die temperatuur bo 85 °F styg. Dit is ongeveer {{1}} °C.', {1: ['29', '29,4', '29.4']}, 'Formule: (85 – 32) × 5 ÷ 9 ≈ 29,4 °C.', prompt='Skakel 85 grade Fahrenheit om na Celsius.', src='workbook', page=127, item='2', status='derived_from_rule'),
    sa('Alligator of iguana?', 'Waarom dink jy sou mense dalk dink die iguana is ’n alligator?', 'Omdat ’n iguana ’n skubberige reptiel met stekels op sy rug is, wat soos ’n klein krokodil lyk.', lines=3, page=127, item='3', status='needs_review'),
    discuss('Jou mening', 'Sou jy verbaas wees as jy iemand met ’n troetel-iguana sien stap? Sou jy die polisie bel as jy so iets sien? Waarom?', page=127, item='4–5'),
    match('Rymwoorde in die gedig', 'Verbind die woorde wat in die gedig rym.', [('vyf', 'skubbelyf'), ('band', 'strand'), ('kyk', 'aanstryk'), ('lê', 'hê'), ('kwaai', 'kraai'), ('slaap', 'gaap')], 'Hierdie pare rym aan die einde van reëls.', src='workbook', page=127, item='6', status='derived_from_text'),
    tf('Waar of onwaar?', 'Die VN het iguanas by die lys van bedreigde spesies gevoeg om mense te verbied om met hulle handel te dryf.', True, 'Dit is wat die nuusberig sê.', src='workbook', page=127, item='nuus', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Waarmee gaan die spreker stap?', '’n Iguana', ['’n Hond', '’n Kat', '’n Perd'], 'Hy gaan stap met sy iguana.', ev=['Met my iguana']),
    q('literal', 'Waarheen gaan hulle gou-gou?', 'Die see toe', ['Skool toe', 'Winkel toe', 'Berg toe'], 'Dan gaan hy gou-gou see toe.', ev=['Dan gaan ek gou-gou see toe']),
    q('literal', 'Waar klim die iguana op?', 'Op sy skouer', ['Op sy kop', 'In sy sak', 'Op ’n boom'], 'Hy klim op die spreker se skouer.', ev=['Daar klim hy op my skouer']),
    q('inference', 'Waarom bel mense die polisie?', 'Hulle dink die iguana is ’n alligator', ['Hulle is bang vir die skrywer', 'Daar is ’n ongeluk', 'Die skrywer maak lawaai'], 'Hulle vra of mens ’n alligator aan ’n leiband mag hê.', ev=['want mag mens ’n alligator']),
    q('inference', 'Waarom dink mense die iguana is kwaai?', 'Oor sy stekels op sy rug', ['Oor sy tande', 'Oor sy geluide', 'Oor sy kleur'], 'Dis oor die stekels op sy rug.', ev=['Dis oor die stekels op sy rug']),
    q('literal', 'Wat doen die iguana as jy hom onder die ken kielie?', 'Hy lag', ['Hy byt', 'Hy loop weg', 'Hy slaap'], 'Dan lag hy dat hy kraai.', ev=['kielie hom onder die ken']),
    q('vocabulary', 'Wat is ’n piranha?', '’n Vis met skerp tande', ['’n Groot aap', '’n Klein hondsoort', '’n Knaagdier'], 'Dit is die betekenis in die werkboek.', status='derived_from_text', src='workbook', page=127, item='woorde'),
    q('main_idea', 'Hoekom is die UNEP-lys belangrik?', 'Dit verbied handel in diere wat bedreig word deur uitwissing', ['Dit verkoop iguanas', 'Dit leer mense om iguanas aan te hou', 'Dit maak iguanas kleiner'], 'Dit is die doel van die lys.', status='derived_from_text', src='workbook', page=127, item='nuus'),
  ])

# ============================================================== 126 Nuwejaar!
P126 = poem('Nuwejaar!', [
  ['Hoera! Hoera!', 'Dis Nuwejaar!', 'Hoera! Hoera! Dis Nuwejaar!', '’n Dag om te begin opnuut.', 'Daarom het ek klaar besluit', 'Om alles soos ’n kangaroe te geniet.'],
  ['Of miskien sal ek leer vlieg,', 'Probeer om deur mure te loop.', 'Miskien om onsigbaar te word,', 'Of my onder ’n waterval te laat doop.'],
  ['Ek sal myself elasties maak', 'En leer hoe om baie klein te word.', 'Of myself in water verander,', 'En in die wasbak se drein afstort.'],
  ['Ek sal ander planete besoek,', 'Die vreemdste wesens ontmoet', 'Of na die verre verlede toe reis', 'Op ’n groot dinosourus se snoet.'],
  ['Ek sal sommer dadelik begin.', 'Ja, dis die beste jaar ooit.', 'Hoera, want dis Nuwejaar!', 'En lekkerder was daar nooit!']],
  glossary=[('opnuut', 'Weer van voor af.'), ('onsigbaar', 'Iets wat jy nie kan sien nie.'), ('elasties', 'Rekbaar soos ’n rekkie.'), ('drein', 'Die pyp waardeur water uit ’n wasbak loop.'), ('wesens', 'Skepsels; lewende dinge.')])

L126 = lesson(126,
  skills=[READ, WRITE],
  intro='Dis Nuwejaar – tyd vir ’n nuwe begin! Lees die snaakse gedig, dink terug aan jou jaar en maak planne vir volgende jaar. Merk dan af wat jy al kan doen.',
  objectives=['’n Gedig lees en geniet.', 'Vrae oor die gedig beantwoord.', 'Beskryf wat jy gedurende die jaar gedoen en geleer het.', 'Planne vir volgende jaar maak.', 'Jou eie leer nagaan met die kontrolelys.'],
  pass_=P126,
  learn=[
    note('Die gedig is deur Kenn Nesbitt (verwerk). Die spreker se planne is ’n **oordrywing**: dit is snaaks omdat dit onmoontlik is.', title='Oor die gedig', src='supplementary', page=128),
    text('Jy is spesiaal – veiligheidsinligting', 'Jou hele liggaam is spesiaal. Jou liggaam behoort aan jou!', bullets=['NIEMAND behoort aan jou privaat liggaamsdele te raak nie.', 'As iemand aan jou privaat liggaamsdele raak, moet jy iemand daarvan vertel.', 'As iemand jou dinge laat doen wat jy nie wil doen nie, moet jy iemand daarvan vertel.', 'Jy kan hierdie nommers bel: Kinderlyn: 0800 05 55 55 · Life Line: 0861 322 322 · SAPD se noodnommer: 10111 · SAPD se misdaadstopnommer: 086 00 10111 · Kinderbeskermingseenheid: 012 393 2359/2362/2363'], page=130),
  ],
  acts=[
    discuss('Lees die gedig', 'Lees hierdie gedig hardop saam met jou maat of groep.', speak='passage', page=128, item='Ons lees'),
    choices('Wat sal die spreker doen?', 'Is dit een van die spreker se planne?', [('Leer vlieg.', ['ja', 'nee'], 0), ('Ander planete besoek.', ['ja', 'nee'], 0), ('Meer skoolwerk doen.', ['ja', 'nee'], 1), ('Na die verre verlede reis op ’n dinosourus.', ['ja', 'nee'], 0), ('Onsigbaar word.', ['ja', 'nee'], 0)],
            'Die planne in die gedig is snaaks omdat hulle onmoontlik is.', src='supplementary', status='derived_from_text'),
    sa('Hoe voel die spreker?', 'Hoe voel die spreker oor die nuwe jaar? Hoe weet jy?', 'Hy of sy is baie opgewonde en gelukkig: “Hoera!” en “die beste jaar ooit”.', lines=3, page=128, item='gevoel', status='needs_review'),
    writing('Wat het ek die afgelope jaar gedoen en geleer?', 'Beskryf wat jy gedurende die jaar gedoen en geleer het.', checklist=['Ek het gesê wat ek gedoen het.', 'Ek het gesê wat ek geleer het.', 'Ek het ’n paar sinne geskryf.'], lines=8, page=128, item='terugblik'),
    writing('My planne vir volgende jaar', 'Beskryf jou planne vir volgende jaar.', checklist=['Ek het my planne beskryf.', 'Ek het gesê hoekom hulle vir my belangrik is.'], lines=8, page=128, item='planne'),
    ek_kan(EK_KAN_T8, 129),
    tf('Waar of onwaar?', 'Die spreker se planne in die gedig is almal realisties.', False, 'Niemand kan deur mure loop of onsigbaar word nie – dis snaaks oordrywing.', src='supplementary', status='derived_from_text'),
  ],
  quiz=[
    q('literal', 'Watter dag vier die spreker?', 'Nuwejaar', ['Verjaarsdag', 'Kersfees', 'Boekeweek'], 'Hoera! Dis Nuwejaar!', ev=['Dis Nuwejaar']),
    q('literal', 'Waarmee wil die spreker alles geniet?', 'Soos ’n kangaroe', ['Soos ’n leeu', 'Soos ’n voël', 'Soos ’n slang'], 'Om alles soos ’n kangaroe te geniet.', ev=['soos ’n kangaroe te geniet']),
    q('literal', 'Wat sal die spreker miskien leer?', 'Vlieg', ['Swem', 'Hardloop', 'Sing'], 'Of miskien sal ek leer vlieg.', ev=['Of miskien sal ek leer vlieg']),
    q('literal', 'Waarheen sal die spreker reis?', 'Na ander planete', ['Na die see', 'Na ’n dorp', 'Na ’n skool'], 'Ek sal ander planete besoek.', ev=['Ek sal ander planete besoek']),
    q('literal', 'Waarop reis die spreker na die verlede?', '’n Dinosourus se snoet', ['’n Voël se rug', '’n Perd se rug', '’n Vliegtuig'], 'Op ’n groot dinosourus se snoet.', ev=['Op ’n groot dinosourus se snoet']),
    q('inference', 'Hoekom is die gedig snaaks?', 'Die planne is onmoontlik en oordrewe', ['Dit is baie kort', 'Dit gaan oor skool', 'Dit rym nie'], 'Niemand kan deur mure loop of onsigbaar word nie.', ev=['deur mure te loop']),
    q('inference', 'Hoe voel die spreker oor die nuwe jaar?', 'Opgewonde en gelukkig', ['Hartseer', 'Bang', 'Verveeld'], 'Hoera, die beste jaar ooit!', ev=['dis die beste jaar ooit']),
    q('grammar', 'Hoe gebruik die digter beeldspraak?', 'Hy oordryf sy planne', ['Hy gebruik net feite', 'Hy skryf ’n verslag', 'Hy gee opdragte'], 'Oordrywing is een van die gedig se maniere om humor te skep.', status='derived_from_rule', src='supplementary'),
  ])

# The workbook continues after the poem: the “Ek kan” checklist (p. 129) and a child-safety information page (p. 130).
L126['printed_pages'] = [128, 130]
L126['pdf_pages'] = [132, 134]
L126['reference_pages'] = [{'pdf': p, 'printed': p - 4, 'src': f'/workbook/gr6-afr-b2/p{p:03d}.webp'} for p in range(132, 135)]
