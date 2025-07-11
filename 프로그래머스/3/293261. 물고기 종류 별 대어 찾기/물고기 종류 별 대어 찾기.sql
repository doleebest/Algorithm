select id, fish_name, length
from fish_info
join fish_name_info on fish_info.fish_type = fish_name_info.fish_type
where FISH_INFO.FISH_TYPE IN
(select fish_type from fish_info group by fish_type having length=max(length))
order by id