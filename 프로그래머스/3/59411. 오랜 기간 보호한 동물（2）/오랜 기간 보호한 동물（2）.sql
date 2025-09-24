-- 코드를 입력하세요
# 입양을 간 동물 중, 
# 보호 기간이 가장 길었던 
# 동물 두 마리의 
# 아이디와 이름을 조회
SELECT o.animal_id, o.name
from animal_outs o
join animal_ins i on o.animal_id=i.animal_id
order by o.datetime-i.datetime desc
limit 2
