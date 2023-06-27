/*
Three tasks regarding SQL from 
Revolut hackerrank interview test
*/

select count(u.id)
from users u
left join transactions t
on u.id = t.user_id
where t.user_id is null;

select count(user_id)
from transactions
group by user_id
having sum(amount_usd) < 10;

select 
    count(case when u.country_id is null then 1 end) as null_count,
    count(case when u.country_id is not null then 1 end) as not_null_count
from countries c
left join users u on c.id = u.country_id;
