-- 코드를 입력하세요
# 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 
# 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.
# 결과는 카테고리명을 기준으로 오름차순 정렬해주세요
SELECT b.category, sum(sales) as total_sales
from book b
join book_sales s on b.book_id = s.book_id
where s.SALES_DATE like '2022-01-%'
group by b.category
order by b.category