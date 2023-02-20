-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE,"%Y-%m-%d") as PUBLISHED_DATE
FROM Book as b inner join author as a
ON b.author_id = a.author_id
where b.category = '경제'
ORDER BY b.published_date asc