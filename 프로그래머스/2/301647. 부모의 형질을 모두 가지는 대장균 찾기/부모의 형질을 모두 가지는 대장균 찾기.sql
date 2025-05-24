-- 코드를 작성해주세요
select a.id, a.genotype, B.GENOTYPE AS PARENT_GENOTYPE
from ecoli_data as a, ecoli_data as b
where a.parent_id = b.id
    and B.GENOTYPE & A.GENOTYPE = B.GENOTYPE
order by id