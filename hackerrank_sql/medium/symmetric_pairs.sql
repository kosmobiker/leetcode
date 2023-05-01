/*You are given a table, Functions, containing two columns: X and Y.
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X. 
List the rows such that X1 ≤ Y1.*/
with cte as(
    select *, row_number() over(order by x) rnk 
    from functions
    )    
select distinct f1.x, f1.y
from cte f1
join cte f2 on f1.x = f2.y and f1.y = f2.x and f1.x <= f1.y and f1.rnk != f2.rnk
order by f1.x;