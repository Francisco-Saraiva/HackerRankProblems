-- Medium Level Problem

SET SESSION cte_max_recursion_depth = 1500;  -- the max was 1000

WITH RECURSIVE Numbers AS (
    -- Anchor Query: root or starting point
    SELECT 1 AS rn
    
    UNION ALL
    
    -- Recursive Query
    SELECT rn + 1
    FROM Numbers
    WHERE rn <= 1000
), 

Divisible AS (
    SELECT
        n1.rn AS num,
        n2.rn AS divisor,
        CASE
            WHEN n1.rn % n2.rn = 0 THEN 1
            ELSE 0
        END AS is_divisible
    FROM Numbers n1
    CROSS JOIN Numbers n2 
    WHERE n1.rn >= n2.rn AND n1.rn > 1
)


SELECT 
    GROUP_CONCAT(num ORDER BY num SEPARATOR '&')
FROM (
    SELECT num
    FROM Divisible
    GROUP BY num
    HAVING SUM(is_divisible) = 2
    ORDER BY num
) AS prime;

