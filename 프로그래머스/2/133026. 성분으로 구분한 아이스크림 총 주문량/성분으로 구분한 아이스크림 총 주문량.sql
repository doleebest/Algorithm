-- 코드를 입력하세요
select INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from first_half join icecream_info on first_half.flavor = icecream_info.flavor
group by INGREDIENT_TYPE
order by TOTAL_ORDER