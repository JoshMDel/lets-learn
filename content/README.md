# Content notes

All reading passages, glossary entries, and quiz questions in this pilot were
authored by Claude (an AI), not by a CAPS-accredited teacher. They're intended
to demonstrate the app's engine — grade/subject coverage, tiered difficulty,
skill-tagged questions, misconception-aware wrong answers, sentence-level
citation — working correctly end to end, **not** as classroom-ready material.

**Before any real classroom or pilot use, a Western Cape Afrikaans-medium
educator should review every passage and question for**:

- CAPS curriculum alignment and grade-appropriate reading level
- Afrikaans correctness, idiom, and regional register
- Factual accuracy (Natural Sciences / Social Sciences content especially)
- Cultural appropriateness and sensitivity

## What's seeded

- **Flagship depth** (full engine demonstration): Grade 5 Afrikaans Huistaal
  and Grade 5 Mathematics (word problems), each with 3 difficulty tiers on one
  continuing topic, ~10 questions per tier.
- **Everywhere else**: every other Grade 3–7 × subject combination (Afrikaans
  Huistaal, English First Additional Language, Mathematics, Natural Sciences,
  Social Sciences, Life Skills) has one tier with a real, grade-appropriate
  topic and a 6-question pool — functional, not a dead end, but lighter.

## How to add or edit content

Content is seeded via SQL migrations that call the `public.seed_topic(...)`
Postgres function (see migration `008_content_seed_helper`), which takes a
grade, subject key, topic name, and a JSON array of tiers (each with a
passage, glossary, and questions). See any of the `010`–`016` migrations for
the exact JSON shape. There's no in-app content-authoring UI in this pass —
new content goes in via a new migration + `seed_topic()` call.
