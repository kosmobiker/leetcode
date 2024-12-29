/*
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.


Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.
*/
SELECT w1.id
FROM weather AS w1
INNER JOIN weather AS w2 ON w1.recorddate = w2.recorddate + INTERVAL '1' DAY
WHERE w1.temperature > w2.temperature
