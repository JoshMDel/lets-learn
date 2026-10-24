-- Content QC: run in the Supabase SQL editor after every import. Every query must return 0 rows / zeros.
-- 1. Quiz questions that a child could not answer or that have a broken key
select q.id, q.source_key, count(o.id) options, count(*) filter (where o.is_correct) correct
from questions q left join question_options o on o.question_id = q.id
group by q.id
having count(o.id) < 2 or count(*) filter (where o.is_correct) <> 1
    or count(*) filter (where coalesce(trim(o.option_text), '') = '') > 0
    or count(distinct lower(trim(o.option_text))) < count(o.id);

-- 2. Tiers with fewer than 6 questions (a quiz asks 6)
select t.id from tiers t where (select count(*) from questions q where q.tier_id = t.id) < 6;

-- 3. Lesson activities that need an answer but have no choices / no key
select l.werkkaart, i.key, i.kind
from lesson_items i join lessons l on l.id = i.lesson_id
where i.kind in ('mcq', 'choices', 'match', 'order', 'true_false', 'fill_blank')
  and (not exists (select 1 from lesson_item_keys k where k.item_id = i.id)
    or (i.kind = 'mcq' and jsonb_array_length(i.payload->'options') < 2)
    or (i.kind = 'choices' and (jsonb_array_length(i.payload->'questions') = 0
          or exists (select 1 from jsonb_array_elements(i.payload->'questions') q where jsonb_array_length(q->'options') < 2)))
    or (i.kind = 'match' and (jsonb_array_length(i.payload->'left') < 2 or jsonb_array_length(i.payload->'right') <> jsonb_array_length(i.payload->'left')))
    or (i.kind = 'order' and jsonb_array_length(i.payload->'items') < 2)
    or (i.kind = 'fill_blank' and coalesce(i.payload->>'text', '') = ''));

-- 4. Lessons that do not match the manifest
select 'lessons <> 62' where (select count(*) from lessons) <> 62;
