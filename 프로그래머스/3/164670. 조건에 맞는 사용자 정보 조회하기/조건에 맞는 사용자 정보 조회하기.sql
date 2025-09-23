-- 코드를 입력하세요
SELECT user_id, nickname, 
    concat(city, ' ', street_address1, ' ', STREET_ADDRESS2) as '전체주소',
    concat(substr(u.TLNO,1,3),'-', substr(u.TLNO,4,4),'-',substr(u.TLNO,8)) as '전화번호'
from USED_GOODS_USER u
join USED_GOODS_BOARD b on u.user_id = b.writer_id
group by u.user_id
having count(b.board_id) >=3
order by u.user_id desc
    