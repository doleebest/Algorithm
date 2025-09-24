-- 코드를 작성해주세요
# 어떤 item_id가 parent_item_id로 등장하지 않으면
select i.item_id, i.item_name, i.rarity
from item_info i
where i.item_id not in 
    (select parent_item_id from item_tree where parent_item_id is not null)
order by i.item_id desc