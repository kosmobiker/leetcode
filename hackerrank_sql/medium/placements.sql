/*You are given three tables: Students, Friends and Packages.
Students contains two columns: ID and Name.
Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend).
Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

Write a query to output the names of those students whose best friends got offered a higher salary than them.
Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no
two students got same salary offer.
*/
WITH cte1 AS (
    SELECT
        s.id,
        s.name,
        f.friend_id,
        p.salary
    FROM students AS s
    INNER JOIN friends AS f ON s.id = f.id
    INNER JOIN packages AS p ON s.id = p.id
),

cte2 AS (
    SELECT
        s.id,
        s.name,
        f.friend_id,
        p.salary AS friends_salary
    FROM students AS s
    INNER JOIN friends AS f ON s.id = f.id
    INNER JOIN packages AS p ON f.friend_id = p.id
)

SELECT cte1.name
FROM cte1
INNER JOIN cte2 ON cte1.id = cte2.id
WHERE cte1.salary < cte2.friends_salary
ORDER BY cte2.friends_salary;
