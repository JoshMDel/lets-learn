"""Refresh manifest.json lesson status from the lesson files (and optionally mark lessons as imported).

    python update_manifest.py              # recompute authored/activities/quiz counts
    python update_manifest.py --imported 65 66 67   # additionally mark these worksheets as imported into Supabase
"""
import glob
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANIFEST = os.path.join(ROOT, 'manifest.json')

INTERACTIVE = {'mcq', 'true_false', 'fill_blank', 'match', 'order', 'choices', 'short_answer', 'writing', 'discuss', 'listen'}


def main(argv):
    imported = set()
    if '--imported' in argv:
        imported = {int(a) for a in argv[argv.index('--imported') + 1:]}
    m = json.load(open(MANIFEST, encoding='utf-8'))
    by_num = {l['werkkaart']: l for l in m['lessons']}
    for path in sorted(glob.glob(os.path.join(ROOT, 'lessons', 'wk*.json'))):
        num = int(re.search(r'wk(\d+)\.json', path).group(1))
        les = json.load(open(path, encoding='utf-8'))
        entry = by_num[num]
        kinds = Counter(i['kind'] for i in les['items'] if i['kind'] in INTERACTIVE)
        sources = Counter(i['source'] for i in les['items'] if i['kind'] in INTERACTIVE)
        qsources = Counter(q['source'] for q in les['quiz'])
        qstatus = Counter(q['answer_status'] for q in les['quiz'])
        st = entry['status']
        st['lesson_authored'] = True
        st['activities'] = sum(kinds.values())
        st['activity_kinds'] = dict(kinds)
        st['activities_from_workbook'] = sources.get('workbook', 0)
        st['activities_supplementary'] = sources.get('supplementary', 0)
        st['quiz_questions'] = len(les['quiz'])
        st['quiz_from_workbook'] = qsources.get('workbook', 0)
        st['quiz_supplementary'] = qsources.get('supplementary', 0)
        st['quiz_answer_status'] = dict(qstatus)
        # answers are "verified" only where the workbook itself prints them; everything else is flagged for a teacher
        st['answers_verified'] = all(q['answer_status'] == 'official' for q in les['quiz'])
        st['visuals_processed'] = 'original workbook pages attached (reference_pages); interactive recreation only where noted in review_notes'
        st['review_status'] = les['review_status']
        entry['review_flags'] = [n for n in les.get('review_notes', [])][1:]
        if num in imported:
            st['imported'] = True
    done = [l for l in m['lessons'] if l['status']['lesson_authored']]
    m['progress'] = dict(lessons_total=len(m['lessons']), lessons_authored=len(done),
                         lessons_imported=sum(1 for l in m['lessons'] if l['status']['imported']),
                         interactive_activities=sum(l['status']['activities'] for l in done),
                         quiz_questions=sum(l['status']['quiz_questions'] for l in done))
    json.dump(m, open(MANIFEST, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(m['progress'])


if __name__ == '__main__':
    main(sys.argv[1:])
