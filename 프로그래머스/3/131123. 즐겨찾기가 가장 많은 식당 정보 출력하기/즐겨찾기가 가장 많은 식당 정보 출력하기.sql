-- 코드를 입력하세요
# REST_INFO 테이블에서 
# 음식종류별로 즐겨찾기수가 가장 많은 식당의 
# 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 
# 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.
SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
from rest_info r
join (select food_type, max(favorites) as favorites from rest_info group by food_type) s
on r.food_type = s.food_type and r.favorites=s.favorites
order by food_type desc