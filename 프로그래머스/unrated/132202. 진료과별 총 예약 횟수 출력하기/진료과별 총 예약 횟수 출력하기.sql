SELECT MCDP_CD as "진료과코드", COUNT(PT_NO) as "5월예약건수"
FROM appointment
where DATE_FORMAT(apnt_ymd, "%Y-%m") = '2022-05'
group by mcdp_cd
order by COUNT(pt_no) asc, mcdp_cd