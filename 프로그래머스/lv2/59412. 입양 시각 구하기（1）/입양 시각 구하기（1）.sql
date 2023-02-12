-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(hour(datetime)) as "COUNT"
FROM animal_outs
group by HOUR
having HOUR >= 9 and HOUR < 20
order by 1