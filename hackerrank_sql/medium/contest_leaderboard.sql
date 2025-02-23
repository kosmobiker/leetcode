/*You did such a great job helping Julia with her last coding contest challenge
that she wants you to work on this one, too!
The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query
to print the hacker_id, name, and total score of the hackers ordered by the descending score.
If more than one hacker achieved the same total score, then sort the result by ascending hacker_id.
Exclude all hackers with a total score of 0 from your result.
*/
WITH cte AS (
    SELECT
        h.name,
        s.hacker_id,
        s.challenge_id,
        s.score,
        row_number()
            OVER (
                PARTITION BY s.hacker_id, s.challenge_id
                ORDER BY s.score DESC
            )
        AS rn
    FROM submissions AS s
    INNER JOIN hackers AS h ON s.hacker_id = h.hacker_id
)

SELECT
    hacker_id,
    name,
    sum(score)
FROM cte
WHERE rn = 1
GROUP BY hacker_id, name
HAVING sum(score) > 0
ORDER BY sum(score) DESC, hacker_id ASC;
