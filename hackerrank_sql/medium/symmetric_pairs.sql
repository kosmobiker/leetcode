/*You are given a table, Functions, containing two columns: X and Y.
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X.
List the rows such that X1 ≤ Y1.*/
WITH cte AS (
    SELECT
        *,
        row_number() OVER (
            ORDER BY x
        ) AS rnk
    FROM functions
)

SELECT DISTINCT
    f1.x,
    f1.y
FROM cte AS f1
INNER JOIN
    cte AS f2
    ON f1.x = f2.y AND f1.y = f2.x AND f1.x <= f1.y AND f1.rnk != f2.rnk
ORDER BY f1.x;
