/*
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.


Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The result format is in the following example.
*/
WITH cte1 AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login_date
    FROM activity
    GROUP BY player_id
),

cte2 AS (
    SELECT
        cte1.player_id,
        CASE
            WHEN EXISTS (
                SELECT 1
                FROM activity AS a
                WHERE
                    a.player_id = cte1.player_id
                    AND a.event_date = cte1.first_login_date + INTERVAL '1 day'
            ) THEN 1
            ELSE 0
        END AS logged_in_next_day
    FROM cte1
)

SELECT ROUND(SUM(logged_in_next_day)::NUMERIC / COUNT(*), 2) AS fraction
FROM cte2;
