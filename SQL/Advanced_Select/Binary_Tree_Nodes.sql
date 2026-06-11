-- Medium Level Problem

WITH InnerNodes AS(
    SELECT DISTINCT P
    FROM BST
    WHERE P IS NOT NULL
)

SELECT
    N,
    CASE 
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT P FROM InnerNodes) THEN 'Inner'
        ELSE 'Leaf'
    END AS node_type
FROM BST
ORDER BY N;