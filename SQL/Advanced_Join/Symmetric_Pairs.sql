-- Medium Level Problem

WITH Functions_id AS (
    SELECT ROW_NUMBER() OVER() AS id, X, Y
    FROM Functions
)

SELECT
    CASE
        WHEN f1.X <= f1.Y THEN f1.X
        ELSE f2.X
    END AS C1,
    CASE
        WHEN f1.Y >= f1.X THEN f1.Y
        ELSE f2.Y
    END AS C2
FROM Functions_id f1
CROSS JOIN Functions_id f2 
WHERE f1.id != f2.id -- prevents a row from matching itself
    AND f1.id < f2.id -- dont need to double check pairs
    AND f1.X = f2.Y -- problem statement conditions
    AND f2.X = f1.Y
ORDER BY C1;