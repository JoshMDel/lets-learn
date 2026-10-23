"""Authoring kit for the Grade 6 Afrikaans Book 2 lessons.

Each lesson is written as a small Python spec (see specs/) using the helpers below.
`emit(lesson(...))` fills in the workbook metadata from manifest.json (term, theme,
weeks, printed/PDF pages, reference page images, topic grouping), writes
lessons/wkNNN.json and returns the JSON that public.import_workbook_lesson() takes.

Content rules baked in here:
  * source = 'workbook'      -> the item/question appears in the workbook (text kept as printed)
  * source = 'supplementary' -> extra practice written for this app (shown with an "Extra practice" badge)
  * answer_status            -> official | derived_from_text | derived_from_rule | needs_review
    The workbook has no answer key, so unless it prints the answer itself ('official'),
    answers are derived from the passage / grammar rule and flagged for teacher review.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # content/grade6-afrikaans-book2
MANIFEST = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
LESSON_META = {l['werkkaart']: l for l in MANIFEST['lessons']}
OUT_DIR = os.path.join(ROOT, 'lessons')

TOPICS = {  # manifest group -> (topic key, name_af, name_en, sort)
    (5, 'wk1-2'): ('gr6-afr-b2-t5-wk1-2', 'Tema 5 · Week 1–2: Stories en berigte', 'Theme 5 · Weeks 1–2: Stories and reports', 101),
    (5, 'wk3-4'): ('gr6-afr-b2-t5-wk3-4', 'Tema 5 · Week 3–4: Volksverhale', 'Theme 5 · Weeks 3–4: Folktales', 102),
    (6, 'wk5-6'): ('gr6-afr-b2-t6-wk5-6', 'Tema 6 · Week 5–6: Stories en briewe', 'Theme 6 · Weeks 5–6: Stories and letters', 103),
    (6, 'wk7-8'): ('gr6-afr-b2-t6-wk7-8', 'Tema 6 · Week 7–8: Strokiesprentverhale is pret', 'Theme 6 · Weeks 7–8: Comic-strip stories are fun', 104),
    (6, 'wk9-10'): ('gr6-afr-b2-t6-wk9-10', 'Tema 6 · Week 9–10: Speeltyd', 'Theme 6 · Weeks 9–10: Playtime', 105),
    (7, 'wk1-2'): ('gr6-afr-b2-t7-wk1-2', 'Tema 7 · Week 1–2: Onderhoude en taaldinge', 'Theme 7 · Weeks 1–2: Interviews and language', 106),
    (7, 'wk3-4'): ('gr6-afr-b2-t7-wk3-4', 'Tema 7 · Week 3–4: Lees om inligting te bekom', 'Theme 7 · Weeks 3–4: Reading for information', 107),
    (8, 'wk5-6'): ('gr6-afr-b2-t8-wk5-6', 'Tema 8 · Week 5–6: Storietyd', 'Theme 8 · Weeks 5–6: Story time', 108),
    (8, 'wk7-8'): ('gr6-afr-b2-t8-wk7-8', 'Tema 8 · Week 7–8: Gedigte vir kinders', 'Theme 8 · Weeks 7–8: Poems for children', 109),
}

LISTEN, READ, WRITE, LANG = 'Luister en praat', 'Lees en kyk', 'Skryf en aanbied', 'Taalstrukture en -konvensies'


def _ref(page=None, pdf=None, item=None):
    r = {}
    if page is not None:
        r['printed_page'] = page
        r['pdf_page'] = pdf if pdf is not None else page + 4
    if item is not None:
        r['item'] = str(item)
    return r or None


# ----------------------------------------------------------------- content blocks
def text(title, *paras, bullets=None, src='workbook', page=None):
    p = {}
    if paras:
        p['paragraphs'] = list(paras)
    if bullets:
        p['bullets'] = list(bullets)
    return dict(section='learn', kind='text', title_af=title, payload=p, source=src, workbook_ref=_ref(page))


def note(body, title=None, src='workbook', page=None, section='learn'):
    return dict(section=section, kind='note', title_af=title, payload={'text': body}, source=src, workbook_ref=_ref(page))


def table(title, headers, rows, src='workbook', page=None, section='learn'):
    return dict(section=section, kind='table', title_af=title, payload={'headers': headers, 'rows': rows}, source=src, workbook_ref=_ref(page))


def example(item):
    item = dict(item)
    item['section'] = 'example'
    return item


def figure(title, src, alt, caption=None, page=None, section='learn', source='workbook'):
    """A picture from the workbook (see tools/crop_figure.py)."""
    return dict(section=section, kind='image', title_af=title, payload={'src': src, 'alt': alt, **({'caption': caption} if caption else {})},
                source=source, workbook_ref=_ref(page))


# ----------------------------------------------------------------- activities
def _act(kind, title, payload, src='workbook', page=None, item=None, answer=None, feedback=None, suggested=None, status=None):
    d = dict(section='activity', kind=kind, title_af=title, payload=payload, source=src, workbook_ref=_ref(page, item=item))
    if answer is not None:
        d['answer'] = answer
    if feedback is not None:
        d['feedback'] = feedback
    if suggested is not None:
        d['suggested_answer'] = suggested
    if status:
        d['answer_status'] = status
    return d


def discuss(title, prompt, points=None, src='workbook', page=None, item=None, speak=None):
    p = {'prompt': prompt}
    if points:
        p['points'] = list(points)
    if speak == 'passage':
        p['speak_passage'] = True
    elif speak:
        p['speak'] = speak
    return _act('listen' if speak else 'discuss', title, p, src, page, item)


def mcq(title, prompt, options, correct, explain, per_option=None, src='workbook', page=None, item=None,
        ok='Reg!', hint='Lees die vraag en die teks nog een keer.', status='derived_from_text'):
    letters = 'ABCDEFGH'
    opts = [{'key': letters[i], 'text': t} for i, t in enumerate(options)]
    fb = {'correct': ok, 'incorrect': hint, 'explanation': explain}
    if per_option:
        fb['per_option'] = {letters[i]: m for i, m in per_option.items()}
    return _act('mcq', title, {'prompt': prompt, 'options': opts}, src, page, item,
                answer={'choice': letters[correct]}, feedback=fb, status=status)


def tf(title, statement, value, explain, src='supplementary', page=None, item=None, ok='Reg!', hint='Dink weer daaroor.',
       status='derived_from_text'):
    return _act('true_false', title, {'statement': statement}, src, page, item,
                answer={'value': bool(value)}, feedback={'correct': ok, 'incorrect': hint, 'explanation': explain}, status=status)


def fill(title, text_, answers, explain, bank=None, prompt=None, src='supplementary', page=None, item=None,
         ok='Mooi so!', hint='Kyk mooi na die woord se plek in die sin.', status='derived_from_text'):
    payload = {'text': text_}
    if prompt:
        payload['prompt'] = prompt
    if bank:
        payload['word_bank'] = list(bank)
    ans = {str(k): ([v] if isinstance(v, str) else list(v)) for k, v in answers.items()}
    return _act('fill_blank', title, payload, src, page, item, answer=ans,
                feedback={'correct': ok, 'incorrect': hint, 'explanation': explain}, status=status)


def match(title, prompt, pairs, explain, display_order=None, src='supplementary', page=None, item=None,
          ok='Almal reg!', hint='Probeer weer – lees die voorbeelde noukeurig.', status='derived_from_text'):
    left = [{'key': f'l{i+1}', 'text': a} for i, (a, _) in enumerate(pairs)]
    order = display_order or [(i + 1) % len(pairs) for i in range(len(pairs))]  # fixed rotation, never in the right place
    right = [{'key': f'r{j+1}', 'text': pairs[j][1]} for j in order]
    answer = {'pairs': {f'l{i+1}': f'r{i+1}' for i in range(len(pairs))}}
    return _act('match', title, {'prompt': prompt, 'left': left, 'right': right}, src, page, item, answer=answer,
                feedback={'correct': ok, 'incorrect': hint, 'explanation': explain}, status=status)


def order(title, prompt, items_in_order, explain, perm=None, src='supplementary', page=None, item=None,
          ok='Perfek!', hint='Dink: wat kom eerste, en wat laaste?', status='derived_from_text', images=None):
    n = len(items_in_order)
    perm = perm or [(i * 2 + 1) % n if n % 2 == 0 else (i * 2 + 1) % n for i in range(n)]
    if sorted(perm) != list(range(n)):
        perm = list(range(1, n)) + [0]
    shown = [{'key': f'e{j+1}', 'text': items_in_order[j], **({'image': images[j]} if images else {})} for j in perm]
    return _act('order', title, {'prompt': prompt, 'items': shown}, src, page, item,
                answer={'sequence': [f'e{j+1}' for j in range(n)]},
                feedback={'correct': ok, 'incorrect': hint, 'explanation': explain}, status=status)


def choices(title, prompt, rows, explain, src='supplementary', page=None, item=None,
            ok='Mooi so!', hint='Kyk weer – lees elke sin noukeurig.', status='derived_from_text'):
    """rows = [(text, [option, option, ...], index_of_correct_option), ...]  (set of mini multiple-choice rows)."""
    qs, ans = [], {}
    for i, (t, opts, right) in enumerate(rows, 1):
        qs.append({'key': f'q{i}', 'text': t, 'options': [{'key': 'abcdefgh'[j], 'text': o} for j, o in enumerate(opts)]})
        ans[f'q{i}'] = 'abcdefgh'[right]
    return _act('choices', title, {'prompt': prompt, 'questions': qs}, src, page, item, answer={'answers': ans},
                feedback={'correct': ok, 'incorrect': hint, 'explanation': explain}, status=status)


def sa(title, prompt, suggested=None, lines=2, src='workbook', page=None, item=None, status='derived_from_text'):
    """Short written answer. `suggested` is shown after the learner saves their own answer."""
    p = {'prompt': prompt, 'lines': lines}
    if suggested is None:  # open-ended: no model answer
        return _act('short_answer', title, p, src, page, item, suggested=None, status=None) | {'feedback': {}}
    return _act('short_answer', title, p, src, page, item, suggested=suggested, status=status)


def writing(title, prompt, checklist=None, tips=None, lines=8, src='workbook', page=None, item=None, no_text=False):
    p = {'prompt': prompt, 'lines': lines}
    if no_text:
        p['no_text'] = True
    if checklist:
        p['checklist'] = list(checklist)
    if tips:
        p['tips'] = list(tips)
    return _act('writing', title, p, src, page, item)


# ----------------------------------------------------------------- quiz
def q(skill, prompt, correct, wrong, explain, ev=None, src='supplementary', status='derived_from_text', page=None, item=None):
    """Quiz question. `wrong` = list of strings or (string, misconception) tuples. Options are shuffled at quiz time."""
    opts = [{'key': 'a', 'text': correct, 'correct': True}]
    for i, w in enumerate(wrong):
        t, m = (w, None) if isinstance(w, str) else w
        o = {'key': 'bcdefgh'[i], 'text': t}
        if m:
            o['misconception'] = m
        opts.append(o)
    d = dict(skill=skill, source=src, answer_status=status, prompt=prompt, explanation=explain, options=opts)
    if ev:
        d['_ev'] = list(ev)  # text snippets of the supporting sentences; resolved to sentence indexes in lesson()
    r = _ref(page, item=item)
    if r:
        d['workbook_ref'] = r
    return d


# ----------------------------------------------------------------- passages
def split_sentences(text_):
    text_ = re.sub(r'\s+', ' ', text_.strip())
    parts = re.split(r'(?<=[.!?”])\s+(?=[“A-ZÁÉÈÊËÍÎÏÓÔÖÚÛÜ’‘(])', text_)
    return [p.strip() for p in parts if p.strip()]


def passage(title, body, glossary=()):
    """body = one string (paragraphs separated by newlines) or a list of paragraph strings."""
    paras = body.split(chr(10)) if isinstance(body, str) else list(body)
    sentences, starts = [], []
    for para in paras:
        if not para.strip():
            continue
        parts = split_sentences(para) or [para.strip()]
        starts.append(len(sentences))
        sentences.extend(parts)
    g = []
    for term, definition in glossary:
        idx = next((i for i, s in enumerate(sentences) if re.search(r'\b' + re.escape(term), s, re.I)), None)
        e = {'term': term, 'definition': definition}
        if idx is not None:
            e['sentence_index'] = idx
        g.append(e)
    return {'title': title, 'language': 'af', 'sentences': sentences, 'paragraph_starts': starts, 'glossary': g}


def poem(title, strofes, glossary=()):
    """A poem: one sentence per line, one paragraph per strofe. Lines end with a newline so the reader keeps the line breaks."""
    sentences, starts = [], []
    for strofe in strofes:
        lines = [l.strip() for l in strofe if l.strip()]
        starts.append(len(sentences))
        sentences.extend(l + (chr(10) if i < len(lines) - 1 else '') for i, l in enumerate(lines))
    g = []
    for term, definition in glossary:
        idx = next((i for i, s in enumerate(sentences) if re.search(r'\b' + re.escape(term), s, re.I)), None)
        e = {'term': term, 'definition': definition}
        if idx is not None:
            e['sentence_index'] = idx
        g.append(e)
    return {'title': title, 'language': 'af', 'sentences': sentences, 'paragraph_starts': starts, 'glossary': g}


# ----------------------------------------------------------------- lesson
def lesson(num, intro, objectives, learn=(), examples=(), acts=(), quiz=(), pass_=None, skills=None, notes=()):
    m = LESSON_META[num]
    topic_key, name_af, name_en, sort = TOPICS[(m['tema'], m['group'])]
    siblings = [l for l in MANIFEST['lessons'] if l['tema'] == m['tema'] and l['group'] == m['group']]
    tier_number = [l['werkkaart'] for l in siblings].index(num) + 1
    labels = m['skill_labels_on_page']
    if skills is None:
        skills = []
        if labels['Luister en praat']:
            skills.append(LISTEN)
        if labels['Lees en kyk']:
            skills.append(READ)
        if labels['Skryf en aanbied']:
            skills.append(WRITE)
        if m['language_structures_by_title'] and LANG not in skills:
            skills.append(LANG)
    pdf0, pdf1 = m['pdf_pages']
    pr0 = m['printed_pages'][0]
    refs = [{'pdf': p, 'printed': pr0 + (p - pdf0), 'src': f'/workbook/gr6-afr-b2/p{p:03d}.webp'} for p in range(pdf0, pdf1 + 1)]

    items = []
    for section, group in (('learn', learn), ('example', examples), ('activity', acts)):
        n = 0
        for it in group:
            it = dict(it)
            n += 1
            it['section'] = section if it['section'] != 'example' else 'example'
            it['key'] = f"{'learn' if it['section']=='learn' else 'ex' if it['section']=='example' else 'act'}-{n:02d}"
            it['sort_order'] = n * 10
            if it.get('workbook_ref') is None:
                it.pop('workbook_ref', None)
            items.append(it)
    quiz_out = []
    sents = (pass_ or {}).get('sentences', [])
    for i, qq in enumerate(quiz, 1):
        qq = dict(qq)
        qq['key'] = f'q{i:02d}'
        ev = qq.pop('_ev', None)
        if ev:
            idx = []
            for snippet in ev:
                hit = [k for k, s in enumerate(sents) if snippet.lower() in s.lower()]
                assert hit, f'wk{num} q{i}: evidence snippet not found in passage: {snippet!r}'
                idx.append(hit[0])
            qq['supporting'] = sorted(set(idx))
        quiz_out.append(qq)

    out = dict(
        key=m['key'], workbook_key=MANIFEST['workbook']['key'], werkkaart=num, title_af=m['title_af'],
        topic=dict(key=topic_key, name_af=name_af, name_en=name_en, sort=sort), tier_number=tier_number,
        term=m['quarter'], tema=m['tema'], tema_title=m['tema_title'], weeks=m['group_title'].split(':')[0].replace(' – ', '–'),
        skill_areas=skills, printed_pages=m['printed_pages'], pdf_pages=m['pdf_pages'], reference_pages=refs,
        intro_af=intro, objectives_af=list(objectives), review_status='needs_review',
        review_notes=['Die werkboek bevat geen antwoordsleutel nie. Antwoorde is deur die program uit die teks of die taalreël afgelei en moet deur ’n onderwyser nagegaan word.'] + list(notes),
        items=items, quiz=quiz_out)
    if pass_:
        out['passage'] = pass_
    return out


def emit(lsn):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, f"wk{lsn['werkkaart']:03d}.json")
    json.dump(lsn, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n_items = len(lsn['items'])
    n_int = sum(1 for i in lsn['items'] if i['kind'] in ('mcq', 'true_false', 'fill_blank', 'match', 'order', 'choices', 'short_answer', 'writing', 'discuss', 'listen'))
    print(f"wk{lsn['werkkaart']:03d} {lsn['title_af']}: items={n_items} (interactive {n_int}) quiz={len(lsn['quiz'])} "
          f"sentences={len(lsn.get('passage', {}).get('sentences', []))} skills={lsn['skill_areas']}")
    assert len(lsn['quiz']) >= 6, 'need at least 6 quiz questions'
    for qq in lsn['quiz']:
        assert sum(1 for o in qq['options'] if o.get('correct')) == 1
    return lsn


def minified(*lessons):
    return ',\n'.join(json.dumps(l, ensure_ascii=False, separators=(',', ':')) for l in lessons)


EK_KAN_T5 = ['’n verskeidenheid tekste lees.', 'voorspellings op grond van die titel en illustrasies van ’n teks doen.', 'vrae op grond van ’n teks beantwoord.', 'gebeure in die korrekte volgorde herroep.',
             'hoof- en ondersteunende idees identifiseer.', '’n tydlyn ontwerp.', 'woorde met hul betekenisse verbind.', 'aan groepbesprekings deelneem.', 'afleidings uit teks maak.',
             '’n dagboekinskrywing skryf.', '’n verslag skryf.', '’n vriendskaplike brief skryf.', '’n brief van die nodige kenmerke voorsien.', 'woorde in lettergrepe verdeel.',
             'samestellings en afleidings identifiseer.', 'tussen hoofwerkwoorde en hulpwerkwoorde onderskei.', 'tussen enkelvoudige, saamgestelde en veelvoudige sinne onderskei.',
             'sinne in die bedrywende en lydende vorm skryf.', 'spelpatrone toepas.', 'afkortings, verkortings en akronieme gebruik.', 'vlug- en soekleesvaardighede toepas.', 'die skryfproses toepas.',
             'voegwoorde gebruik om saamgestelde sinne te vorm.', 'voor- en agtervoegsels gebruik om nuwe woorde te vorm.', 'sinonieme, antonieme, homofone en homonieme gebruik.']


def ek_kan(statements, page):
    """The workbook's end-of-theme “Ek kan” self-assessment as a save-able tick list."""
    return writing('Kontrolelys: Ek kan …', 'Merk wat jy al kan doen. Dit is net vir jou eie nagaan.', checklist=statements, no_text=True, page=page, item='Kontrolelys', lines=1)


EK_KAN_T6 = ['die kenmerke van ’n verhaal bespreek.', 'oordrywing en stereotipes identifiseer.', '’n verhalende teks lees.', 'idiomatiese uitdrukkings identifiseer.', 'die teks soeklees en spesifieke vrae beantwoord.',
             '’n gedeelte in die teks opspoor.', 'beskryf hoe ’n karakter se gevoelens verander het.', 'die agtergrond, intrige en karakters in die storie identifiseer.', '’n mening oor verhoudinge tussen kultuurgroepe lug.',
             '’n geheuekaart oor ’n storie opstel.', 'die storie aan die hand van die geheuekaart oorskryf.', 'die eienskappe van ’n brief bespreek.', '’n vriendskaplike brief lees.',
             'die teenwoordige, verlede en toekomende tyd onderskei.', 'die brief soeklees om bepaalde frases en sinne te vind.', 'meerkeusevrae oor die brief beantwoord.', '’n geheuekaart gebruik om ’n brief te beplan.',
             '’n vriendskaplike brief skryf.', '’n e-pos lees.', 'die e-pos soeklees om bepaalde vrae te beantwoord.', 'homofone en homonieme identifiseer.', 'woordtipes identifiseer.', 'verkleinings voorsien.',
             'woordsoorte identifiseer.', 'die bedrywende en die lydende vorm gebruik.', 'woorde met hul sinonieme en antonieme verbind.', 'voegwoorde gebruik om sinne te verbind.',
             'enkelvoudige, saamgestelde en veelvoudige sinne skryf.', 'sinne in die verlede en toekomende tyd oorskryf.', 'die ontkennende vorm gebruik.', 'afkortings en akronieme voorsien.',
             '’n strokiesprentverhaal vluglees.', 'aspekte van die strokiesprentverhaal bespreek.', 'elke raam van die verhaal beskryf.', 'sinne in die direkte rede oorskryf.', '’n mening oor advertensies uitspreek.',
             '’n strokiesprent-advertensie lees.', 'die advertensie soeklees om bepaalde vrae te beantwoord.', '’n eie advertensie beplan.', '’n advertensie skryf.', '’n advertensie rolspeel.',
             'klank- en lettergrepe identifiseer.', 'sinonieme en antonieme voorsien.', 'vaste uitdrukkings met hul betekenisse verbind.', '’n eie vergelyking skryf.', 'die korrekte spelling identifiseer.',
             'meervoude en verkleinwoorde vorm.', 'hoofletters asook lees- en skryftekens in sinne invul.', '’n toneelstuk lees.', 'die toneelstuk opvoer.', 'vrae oor die toneelstuk beantwoord.',
             'die toneelstuk opsom.', 'tegnieke in die toneelstuk identifiseer.', '’n toneelstuk in groepverband skryf.']
