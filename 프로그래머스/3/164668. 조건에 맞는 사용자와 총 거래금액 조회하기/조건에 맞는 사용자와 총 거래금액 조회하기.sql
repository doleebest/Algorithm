-- 코드를 입력하세요
# used_goods_board는 게시글 관련 정보
# USED_GOODS_USER는 회원 관련 정보
# 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 
# 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 
# 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
SELECT u.user_id, u.nickname, sum(b.price) as total_sales
from used_goods_user u
join used_goods_board b
on u.user_id = b.writer_id
where b.status = 'done'
group by u.user_id
having sum(price) >= 700000
order by total_sales