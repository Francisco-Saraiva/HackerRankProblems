-- Medium Level Problem

WITH RankedLatitudes AS (
    SELECT 
        lat_n,
        ROW_NUMBER() OVER (ORDER BY lat_n) AS rn,
        COUNT(*) OVER() AS cnt
    FROM Station
)

SELECT ROUND(AVG(lat_n), 4) AS median
FROM RankedLatitudes
WHERE rn IN (
    FLOOR((cnt+1) / 2.0),
    CEIL((cnt+1) / 2.0)
);

-- EVEN NUMBER --> 10
-- Calculation: (10+1)/2 = 11/2 = 6.5 
-- FLOOR: 6
-- CEIL: 7
-- AVERAGE both values

-- ODD NUMBER --> 11
-- Calculation: (11+1)/2 = 12/2 = 6
-- FLOOR: 6
-- CEIL: 6
-- It is just this one center value