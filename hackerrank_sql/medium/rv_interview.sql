/*
Three tasks regarding SQL from
Revolut hackerrank interview test
*/

SELECT count(u.id)
FROM users AS u
LEFT JOIN transactions AS t
    ON u.id = t.user_id
WHERE t.user_id IS null;

SELECT count(user_id)
FROM transactions
GROUP BY user_id
HAVING sum(amount_usd) < 10;

SELECT
    count(CASE WHEN u.country_id IS null THEN 1 END) AS null_count,
    count(CASE WHEN u.country_id IS NOT null THEN 1 END) AS not_null_count
FROM countries AS c
LEFT JOIN users AS u ON c.id = u.country_id;
