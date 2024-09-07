/*
Table: Activity

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
 

There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.
*/
-- first solution with join
SELECT a1.machine_id,
    ROUND(
        CAST(
            SUM(a2.timestamp - a1.timestamp)/COUNT(a1.process_id) 
        AS numeric), 
    3) AS processing_time
FROM Activity AS a1
JOIN Activity AS a2 ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id 
WHERE a1.activity_type = 'start' AND a2.activity_type = 'end'
GROUP BY 1
--second solution
WITH cte AS (
    SELECT 
        machine_id, 
        process_id, 
        MIN(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_ts,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_ts
    FROM Activity
    GROUP BY machine_id, process_id
)
SELECT machine_id,
ROUND(
    CAST(
        SUM(end_ts - start_ts)/COUNT(process_id) 
    AS numeric), 
3) AS processing_time
FROM cte
GROUP BY 1