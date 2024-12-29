-- Write your PostgreSQL query statement below
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM activity
WHERE
    activity_date BETWEEN date '2019-07-27'
    - INTERVAL '29' DAY AND date '2019-07-27'
GROUP BY 1
ORDER BY 1
