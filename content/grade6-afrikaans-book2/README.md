# Grade 6 Afrikaans Huistaal – Boek 2 (Kwartaal 3 & 4) → Let's Learn lessons

Source: DBE *Afrikaans Huistaal Graad 6 Boek 2* workbook (PDF pp. 1–138; printed pages = PDF page − 4).
This folder holds the **content pipeline** that turned the workbook into the 62 interactive lessons (werkkaarte 65–126) that live in the app.

```
manifest.json      cumulative manifest: source files, every PDF page, 62 lessons (status, pages, counts), open issues
lessons/wkNNN.json one generated lesson per worksheet (what the importer sends to Supabase)
tools/lessonkit.py authoring DSL (lesson, text, note, table, figure, mcq, tf, fill, match, order, choices, sa, writing, discuss, poem, q, passage, ek_kan)
tools/specs/*.py   the authored content – one `L<number> = lesson(...)` per worksheet
tools/build.py     specs → lessons/*.json            (python build.py [66 67 …])
tools/import_lessons.py   lessons/*.json → Supabase (idempotent upsert, safe to re-run)
tools/update_manifest.py  refresh counts/status in manifest.json (--imported 66 67 …)
tools/crop_figure.py      crop a picture out of a PDF page for use as a figure (needs PyMuPDF)
```

## Data model (additive – nothing existing was changed)

Topic = pair of weeks (9 topics, `topics.sequential = false`) · Tier = one werkkaart · `lessons` (1:1 with the tier) ·
`lesson_items` (learn / example / activity blocks; public payload) · `lesson_item_keys` (answers + feedback, **no RLS policy → unreadable from the browser**) ·
`lesson_responses` (a child's answers; written only by the `check_lesson_item()` RPC) · `questions`/`question_options` (the quiz; 6 random questions per attempt via the existing `/quiz/:tierId` and `submit_attempt()`).

Every item carries `source` (`workbook` or `supplementary`) and every key an `answer_status`:
`official` (the workbook prints the answer) · `derived_from_text` · `derived_from_rule` · `needs_review`.
**The workbook has no answer key.** Nothing marked other than `official` is an official DBE answer, and the app labels the status to learners/teachers.

## Re-importing / editing content

1. Edit the spec in `tools/specs/`, then `python build.py <numbers>`.
2. Import with the **service-role** key (never commit it, never put it in the frontend):
   ```
   export SUPABASE_SERVICE_ROLE_KEY=…        # from the Supabase dashboard
   python import_lessons.py <numbers>
   python update_manifest.py --imported <numbers>
   ```
   The importer calls `public.import_workbook_lesson(jsonb)` (SECURITY DEFINER, executable only by `service_role`). Items are upserted by key, so re-running never duplicates anything, and learner responses to unchanged items are kept.
3. Pictures: `python crop_figure.py NAME PDF_PAGE x0 y0 x1 y1` (coordinates in the 820 px render), then `node scripts/figures-to-webp.mjs` from the app root. Page images live in `public/workbook/gr6-afr-b2/` and are lazy-loaded, never precached.

4. Run `tools/qc.sql` in the Supabase SQL editor after every import: every query must return nothing (it catches questions or activities without answer options).

Poems are authored with `poem(title, strofes)`; line breaks are kept by `PassageReader` (`whitespace-pre-line`).
