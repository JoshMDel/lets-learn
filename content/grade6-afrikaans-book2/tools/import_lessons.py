"""Push lesson JSON files (lessons/wkNNN.json) into Supabase. Safe to run repeatedly (idempotent upsert).

    python import_lessons.py            # every lesson file
    python import_lessons.py 66 67      # only these worksheets

Credentials (never committed):
  * Preferred / permanent:  SUPABASE_SERVICE_ROLE_KEY  -> calls public.import_workbook_lesson() directly
  * Temporary stopgap:      WORKBOOK_IMPORT_TOKEN      -> calls public.import_workbook_lesson_remote(token, lesson)
SUPABASE_URL and SUPABASE_ANON_KEY default to the values in the app's .env.local.
"""
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
LESSONS = os.path.join(os.path.dirname(HERE), 'lessons')


def env_local():
    out = {}
    path = os.path.join(APP, '.env.local')
    if os.path.exists(path):
        for line in open(path, encoding='utf-8'):
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                out[k] = v
    return out


def main(argv):
    local = env_local()
    url = os.environ.get('SUPABASE_URL') or local.get('VITE_SUPABASE_URL')
    anon = os.environ.get('SUPABASE_ANON_KEY') or local.get('VITE_SUPABASE_ANON_KEY')
    service = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')
    token = os.environ.get('WORKBOOK_IMPORT_TOKEN')
    if not url or not (service or (anon and token)):
        sys.exit('Set SUPABASE_SERVICE_ROLE_KEY (or WORKBOOK_IMPORT_TOKEN) first.')

    wanted = {int(a) for a in argv}
    files = sorted(glob.glob(os.path.join(LESSONS, 'wk*.json')))
    ok = bad = 0
    for path in files:
        num = int(re.search(r'wk(\d+)\.json', path).group(1))
        if wanted and num not in wanted:
            continue
        lesson = json.load(open(path, encoding='utf-8'))
        if service:
            endpoint, key, body = 'import_workbook_lesson', service, {'p': lesson}
        else:
            endpoint, key, body = 'import_workbook_lesson_remote', anon, {'p_token': token, 'p': lesson}
        req = urllib.request.Request(
            f'{url}/rest/v1/rpc/{endpoint}', data=json.dumps(body).encode('utf-8'), method='POST',
            headers={'apikey': key, 'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                res = json.loads(r.read().decode('utf-8'))
            print(f"wk{num:03d} ok  items={res['items']} questions={res['questions']} stale_kept={res['stale_questions_kept']}")
            ok += 1
        except urllib.error.HTTPError as e:
            print(f"wk{num:03d} FAILED {e.code}: {e.read().decode('utf-8')[:300]}")
            bad += 1
    print(f'{ok} imported, {bad} failed')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
