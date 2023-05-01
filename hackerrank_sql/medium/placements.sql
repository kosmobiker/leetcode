/*You are given three tables: Students, Friends and Packages. 
Students contains two columns: ID and Name. 
Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). 
Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

Write a query to output the names of those students whose best friends got offered a higher salary than them.
Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no 
two students got same salary offer.
*/
with cte1 as(
    select s.id, s.name, f.friend_id, p.salary
    from students s 
    join friends f on s.id = f.id 
    join packages p on s.id = p.id),
cte2 as (
    select s.id, s.name, f.friend_id, p.salary as friends_salary
    from students s 
    join friends f on s.id = f.id 
    join packages p on f.friend_id = p.id
)
select cte1.name
from cte1
join cte2 on cte1.id = cte2.id
where cte1.salary < cte2.friends_salary
order by cte2.friends_salary;