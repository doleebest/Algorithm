-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(*) AS COUNT
from animal_outs
group by hour(datetime)
HAVING HOUR >= 9 AND HOUR<=19
order by HOUR ASC