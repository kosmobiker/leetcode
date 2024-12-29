-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT
        product_id,
        MIN(year) OVER (PARTITION BY product_id) AS fy
    FROM sales
)

SELECT DISTINCT
    t1.product_id,
    t1.year AS first_year,
    t1.quantity,
    t1.price
FROM sales AS t1
INNER JOIN cte AS t2 ON t1.product_id = t2.product_id AND t1.year = t2.fy
