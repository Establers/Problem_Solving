-- 코드를 입력하세요
SELECT date_format(SALES_DATE, '%Y-%m-%d') as "SALES_DATE", PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM online_sale
where date_format(sales_date, '%Y-%m') = '2022-03'
union 
SELECT date_format(SALES_DATE, '%Y-%m-%d'), PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
FROM offline_sale
where date_format(sales_date, '%Y-%m') = '2022-03'
Order by sales_date asc, product_id asc , user_id asc