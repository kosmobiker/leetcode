/*Julia asked her students to create some coding challenges. Write a query to print the
hacker_id, name, and the total number of challenges created by each student. Sort your results by the total
number of challenges in descending order. If more than one student created the same number of challenges,
then sort the result by hacker_id. If more than one student created the same number of challenges and the
count is less than the maximum number of challenges created, then exclude those students from the result.*/
SELECT
    hacker_id,
    name,
    ch_count
FROM (
    SELECT
        hacker_id,
        name,
        ch_count,
        count(*) OVER (PARTITION BY ch_ct) AS same_count,
        max(ch_ct) OVER () AS max_count
    FROM (
        SELECT
            h.hacker_id,
            h.name,
            count(*) AS ch_ct
        FROM hackers AS h
        INNER JOIN challenges AS c ON h.hacker_id = c.hacker_id
        GROUP BY h.hacker_id, h.name
    )
)
WHERE
    ch_count = max_count
    OR (ch_count != max_count AND same_cnt = 1)
ORDER BY ch_count DESC, hacker_id ASC;
/* I really want Julia to go and fuck herself as much as possible. What kind of sick brain comes up with
such tasks? For what purpose? Why? What can it teach me? Is this the revenge of nerds on normal people?
Where does such an idiotic condition come from? It's as if the author-asshole can't get out of his university
hole and jerks off stupidly on the SQL textbooks.
*/
