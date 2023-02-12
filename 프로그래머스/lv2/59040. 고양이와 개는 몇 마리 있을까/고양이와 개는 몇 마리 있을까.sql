-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(animal_type) as count
FROM animal_ins
where animal_type = 'Cat' or animal_type = 'Dog'
group by animal_type
order by animal_type asc
