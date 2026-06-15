-- Easy Level Problem

WITH RECURSIVE Numbers AS (
    -- Anchor Query: root or starting point
    SELECT 1 AS rn
    
    UNION ALL
    
    -- Recursive Query
    SELECT rn + 1
    FROM Numbers n1
    WHERE rn < 20
)

SELECT
    TRIM(REPEAT("* ", rn))
FROM Numbers;

