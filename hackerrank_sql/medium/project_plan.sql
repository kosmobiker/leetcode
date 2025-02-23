/*You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date.
It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row
in the table.If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is
interested in finding the total number of different projects completed.

Write a query to output the start and end dates of projects listed by the number of days it took to complete
the project in ascending order. If there is more than one project that have the same number of completion days,
then order by the start date of the project
*/
-- many thanks for great idea https://stackoverflow.com/questions/20402089/detect-consecutive-dates-ranges-using-sql
-- actually not an `advanced` join
WITH cte AS (
    SELECT
        start_date AS d,
        row_number() OVER (
            ORDER BY start_date
        ) AS i
    FROM projects
    GROUP BY start_date
)

SELECT
    min(d),
    dateadd(day, 1, max(d)) --I don't want to loose a day
FROM cte
GROUP BY datediff(day, i, d)
ORDER BY datediff(day, min(d), dateadd(day, 1, max(d))), min(d)
