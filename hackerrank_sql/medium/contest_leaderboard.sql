/*You did such a great job helping Julia with her last coding contest challenge 
that she wants you to work on this one, too!
The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query 
to print the hacker_id, name, and total score of the hackers ordered by the descending score. 
If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. 
Exclude all hackers with a total score of 0 from your result.
*/
with cte as (
    select h.name, s.hacker_id, s.challenge_id, s.score,
        row_number() over (partition by s.hacker_id, s.challenge_id order by s.score desc) rn
    from submissions s
    join hackers h on  s.hacker_id = h.hacker_id
    )
select hacker_id, name, sum(score)
from cte
where rn = 1
group by hacker_id, name
having sum(score) > 0
order by sum(score) desc, hacker_id asc;
