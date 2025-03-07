-- Consider P_1(a,b) and P_2(c, d) to be two points on a 2D plane.

--     a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
--     b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
--     c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
--     d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.

-- The formula for Manhattan distance between two points (x1, y1) and (x2, y2) is:
-- | x1 - x2 | + | y1 - y2 |
SELECT
    cast(
        abs(min(lat_n) - max(lat_n))
        + abs(min(long_w) - max(long_w)
        ) AS decimal(18, 4)
    )
FROM station;
