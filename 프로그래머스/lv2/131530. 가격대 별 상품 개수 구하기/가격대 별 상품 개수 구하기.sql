-- 코드를 입력하세요
SELECT FLOOR(price / 10000) * 10000 as PRICE_GROUP, COUNT(product_id) as PRODUCTS
FROM product
GROUP BY FLOOR(price / 10000) * 10000
ORDER BY 1