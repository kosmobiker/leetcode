/*
Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).


For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.*/
SELECT
    t2.reports_to AS employee_id,
    t1.name,
    count(t1.employee_id) AS reports_count,
    round(avg(t2.age), 0) AS average_age
FROM employees AS t1
LEFT JOIN employees AS t2
    ON t1.employee_id = t2.reports_to
GROUP BY 1, 2
HAVING t2.reports_to IS NOT null
ORDER BY 1
