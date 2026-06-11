-- Medium level Problem
SELECT
    CASE
        WHEN marks <= 69 THEN NULL -- Using marks because grades aren't created
        ELSE name
    END AS name, 
    CASE
        WHEN marks >= 90 THEN 10
        WHEN marks >= 80 THEN 9
        WHEN marks >= 70 THEN 8
        WHEN marks >= 60 THEN 7
        WHEN marks >= 50 THEN 6
        WHEN marks >= 40 THEN 5
        WHEN marks >= 30 THEN 4
        WHEN marks >= 20 THEN 3
        WHEN marks >= 10 THEN 2
        ELSE 1
    END AS grade,
    marks
FROM Students
ORDER BY 
    grade DESC,
    CASE WHEN grade >= 8 THEN name END ASC,
    CASE WHEN grade < 8 THEN marks END ASC;