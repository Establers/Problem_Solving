-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE LIKE "intact%" then 'X' 
WHEN SEX_UPON_INTAKE LIKE "Neutered%" then 'O'
WHEN SEX_UPON_INTAKE LIKE "Spayed%" then 'O'
end as '중성화'
FROM animal_ins
ORDER BY ANIMAL_ID