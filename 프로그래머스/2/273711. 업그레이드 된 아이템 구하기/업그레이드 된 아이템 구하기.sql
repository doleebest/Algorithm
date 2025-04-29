-- 코드를 작성해주세요
select ITEM_ID, item_name, rarity
from item_info
where item_id in (select a.item_id
                 from item_info i, item_tree a
                 where a.parent_item_id = i.item_id and i.rarity='RARE') -- 부모의 정보를 in 뒤에서 뽑고, 출력하는 건 자식의 id
order by item_id desc;
