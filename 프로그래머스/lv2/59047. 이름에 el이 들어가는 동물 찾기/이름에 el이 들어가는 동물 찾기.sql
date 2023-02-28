-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM animal_ins
WHERE NAME like "%EL%" and ANIMAL_TYPE = 'Dog'
ORDER BY NAME