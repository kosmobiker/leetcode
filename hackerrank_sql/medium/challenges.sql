/*Julia asked her students to create some coding challenges. Write a query to print the 
hacker_id, name, and the total number of challenges created by each student. Sort your results by the total 
number of challenges in descending order. If more than one student created the same number of challenges, 
then sort the result by hacker_id. If more than one student created the same number of challenges and the 
count is less than the maximum number of challenges created, then exclude those students from the result.*/
select hacker_id, name, ch_count
from (
    select hacker_id, name, ch_count,
           count(*) over(partition by ch_ct) as same_count,
           max(ch_ct) over() as max_count
    from (
        select h.hacker_id, h.name, count(*) as ch_ct
        from hackers h
        join challenges c on h.hacker_id = c.hacker_id
        group by h.hacker_id, h.name
        )
    )
where ch_count = max_count
or  (ch_count != max_count and same_cnt = 1)
order by ch_count desc, hacker_id; 
/* I really want Julia to go and fuck herself as much as possible. What kind of sick brain comes up with 
such tasks? For what purpose? Why? What can it teach me? Is this the revenge of nerds on normal people? 
Where does such an idiotic condition come from? It's as if the author-asshole can't get out of his university
hole and jerks off stupidly on the SQL textbooks. 
*/