/*
Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! 
Write a query to print the respective hacker_id and name of hackers who achieved full scores for more 
than one challenge. Order your output in descending order by the total number of challenges in which the 
hacker earned a full score. If more than one hacker received full scores in same number of challenges, 
then sort them by ascending hacker_id.
*/
select h.hacker_id, h.name
from submissions s
join hackers h on s.hacker_id = h.hacker_id 
join challenges c on s.challenge_id = c.challenge_id
join difficulty d on c.difficulty_level = d.difficulty_level and s.score = d.score
group by h.hacker_id, h.name
having count(s.score) > 1
order by count(s.score) desc, h.hacker_id asc
