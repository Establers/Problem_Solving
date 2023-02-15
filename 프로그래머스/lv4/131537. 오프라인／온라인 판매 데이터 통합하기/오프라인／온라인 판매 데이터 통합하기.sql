-- 코드를 입력하세요
select date_format(sales_date,'%Y-%m-%d') SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from
(
    SELECT sales_date, product_id, user_id, sales_amount
    from online_sale a
    where (sales_date like '2022-03%') 

    union

    SELECT sales_date, product_id, NULL, sales_amount
    from offline_sale b
    where (sales_date like '2022-03%') 
) c
order by sales_date, product_id, user_id
;