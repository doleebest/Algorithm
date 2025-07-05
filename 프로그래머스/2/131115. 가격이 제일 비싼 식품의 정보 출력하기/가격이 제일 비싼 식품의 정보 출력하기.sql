-- 코드를 입력하세요
SELECT f.product_id, f.product_name, f.product_cd, f.category, f.price
from food_product as f
where PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);