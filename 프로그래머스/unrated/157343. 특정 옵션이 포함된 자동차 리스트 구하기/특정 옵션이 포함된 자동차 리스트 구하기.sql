-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM car_rental_company_car
WHERE options LIKE "%네비게이션%"
ORDER BY CAR_ID DESC