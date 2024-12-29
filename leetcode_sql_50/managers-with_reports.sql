/*
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.


Write a solution to find managers with at least five direct reports.

Return the result table in any order.
*/
WITH cte AS (
    SELECT
        managerid,
        COUNT(id) AS num_reps
    FROM employee
    GROUP BY 1
)

SELECT e.name
FROM employee AS e
LEFT JOIN cte ON e.id = cte.managerid
WHERE num_reps >= 5
