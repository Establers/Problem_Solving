-- 코드를 입력하세요
SELECT i.NAME, i.DATETIME
FROM animal_ins i 
    LEFT JOIN animal_outs o ON i.animal_id = o.animal_id
    WHERE i.animal_id is not null and o.animal_id is null
    ORDER BY datetime asc
LIMIT 3