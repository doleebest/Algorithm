-- 코드를 작성해주세요
select a.id, 
CASE
    WHEN A.PER <= 0.25 THEN 'CRITICAL'
    WHEN A.PER <=0.5 THEN 'HIGH'
    WHEN A.PER <= 0.75 THEN 'MEDIUM'
    ELSE 'LOW'
END AS COLONY_NAME
from (
SELECT ID,
PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER FROM ECOLI_DATA) AS A
order by id asc