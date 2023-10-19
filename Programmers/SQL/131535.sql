select count(*) as users
from user_info
where year(joined) = 2021 and 20<=age and age<=29