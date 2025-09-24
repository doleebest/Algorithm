-- 코드를 작성해주세요
select d.DEPT_ID, d.DEPT_NAME_EN, round(avg(e.sal),0) as AVG_SAL
from HR_EMPLOYEES e join HR_DEPARTMENT d
on d.DEPT_ID=e.DEPT_ID
group by d.dept_id, d.DEPT_NAME_EN
order by AVG_SAL desc
