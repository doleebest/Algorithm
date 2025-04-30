# -- 코드를 작성해주세요
# select d.id, d.email, d.first_name, d.last_name
# from developers d, skillcodes s
# where (d.SKILL_CODE & s.CODE) > 0 
#     and s.name in ('Python', 'C#')
# order by d.id

SELECT DISTINCT a.ID, a.EMAIL, a.FIRST_NAME, a.LAST_NAME
FROM DEVELOPERS a, SKILLCODES b
WHERE 
    (a.SKILL_CODE & b.CODE) > 0
    AND b.NAME IN ("Python", "C#")
ORDER BY a.ID;