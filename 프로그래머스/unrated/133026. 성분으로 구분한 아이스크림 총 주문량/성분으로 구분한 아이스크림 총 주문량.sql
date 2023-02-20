-- 코드를 입력하세요
SELECT i.ingredient_type, SUM(f.total_order) as TOTAL_ORDER 
FROM first_half as f, icecream_info as I
where (f.flavor = i.flavor)
group by ingredient_type
