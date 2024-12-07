-- Write your PostgreSQL query statement below
SELECT
    activity_date AS day, 
    COUNT(distinct user_id) AS active_users 
FROM Activity
WHERE activity_date between date '2019-07-27' - interval '29' day and date '2019-07-27'
GROUP BY 1
ORDER BY 1