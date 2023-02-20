-- 코드를 입력하세요
SELECT p.product_code, SUM(p.price * o.sales_amount) as SALES
FROM product as p inner join offline_sale as o
ON p.product_id = o.product_id
GROUP BY p.product_code
ORDER BY SALES desc, 1 asc