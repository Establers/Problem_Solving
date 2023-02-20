-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME 
FROM animal_ins as i inner join animal_outs as o
ON i.animal_id = o.animal_id
WHERE i.datetime > o.datetime
ORDER by i.datetime asc 