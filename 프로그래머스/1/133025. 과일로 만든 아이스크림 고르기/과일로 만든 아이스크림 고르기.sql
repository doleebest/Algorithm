-- 코드를 입력하세요
SELECT fh.flavor
from first_half fh 
join icecream_info ii on ii.flavor = fh.flavor
where total_order>3000 and INGREDIENT_TYPE = 'fruit_based'
-- group by fh.flavor
order by total_order desc