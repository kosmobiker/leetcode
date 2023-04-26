-- Consider P_1(a,b) and P_2(c, d) to be two points on a 2D plane 
-- where (a,b) are the respective minimum and maximum values of 
-- Northern Latitude (LAT_N) and (c, d) are the respective minimum and maximum values of 
-- Western Longitude (LONG_W) in STATION.
-- Query the Euclidean Distance between points P1 and P2 and format your answer 
-- to display 4 decimal digits.

-- The formula for Euclidean distance between two points (x1, y1) and (x2, y2) is:
--             d = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
select cast(
    sqrt(
        power(max(lat_n) - min(lat_n), 2) +
        power(max(long_w) - min(long_w), 2)
        ) as decimal(18, 4))
from station;
