/*
Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.
*/
WITH cte AS (
    SELECT student_id, subject_name, COUNT(*) AS num_exams
    FROM Examinations
    GROUP BY 1, 2
)
SELECT s.student_id, s.student_name, sub.subject_name, COALESCE(cte.num_exams, 0) AS attended_exams 
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN cte ON s.student_id = cte.student_id AND sub.subject_name = cte.subject_name
ORDER BY 1, 3