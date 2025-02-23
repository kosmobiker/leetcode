-- A median is defined as a number separating the higher half of a data set from the 
-- lower half. Query the median of the Northern Latitudes (LAT_N) from STATION 
-- and round your answer to  decimal places.
SELECT DISTINCT
    cast(
        percentile_cont(0.5) WITHIN GROUP (
            ORDER BY lat_n
        ) OVER ()
        AS decimal(18, 4)
    )
FROM station;
