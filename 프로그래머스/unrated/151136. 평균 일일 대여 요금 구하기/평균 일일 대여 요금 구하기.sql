-- 코드를 입력하세요
SELECT floor(avg(daily_fee)) AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV'
;