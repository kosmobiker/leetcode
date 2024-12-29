/*
Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.


A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.
*/
WITH cte AS (
    SELECT num
    FROM mynumbers
    GROUP BY 1
    HAVING COUNT(num) = 1
)

SELECT MAX(num) AS num
FROM cte
