-- 코드를 입력하세요
SELECT count(AGE) as "USERS"
from user_info
where date_format(joined, '%Y') = '2021' 
    and AGE between 20 and 29