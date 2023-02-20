-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME
FROM animal_outs as o left join animal_ins as i
ON o.animal_id = i.animal_id
WHERE i.animal_id is null
ORDER BY o.ANIMAL_ID