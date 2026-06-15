-- Medium Level Problem (this one was very very tough to figure out)

WITH Projects_id AS ( -- So that id mirrors start_date order
    SELECT *, 
    ROW_NUMBER() OVER() AS new_id 
    FROM Projects
    ORDER BY start_date 
), 

Project_Starts AS ( -- marking project start dates
    SELECT p2.new_id AS id,
    p2.start_date AS start_date, 
    p2.end_date AS end_date, 
    CASE 
        WHEN p1.end_date IS NULL THEN 1
        WHEN DATEDIFF(p2.start_date, p1.end_date) != 0 THEN 1 
        ELSE 0 
    END AS project_start 
FROM Projects_id p2 LEFT JOIN Projects_id p1 ON p1.new_id + 1 = p2.new_id 
), 

Project_Groups AS (  -- attributing a project id to each project via cumsum
    SELECT start_date, 
    end_date, 
    SUM(project_start) OVER(ORDER BY start_date) AS project_id 
    FROM Project_Starts 
) 

SELECT
    MIN(start_date) AS start_date,
    MAX(end_date) AS end_date
FROM Project_Groups
GROUP BY project_id
ORDER BY
    DATEDIFF(MAX(end_date), MIN(start_date)),
    MIN(start_date)
;

-- Tabibitosan Method (saw it on internet after I solved it myself)
-- SELECT 
--     MIN(Start_Date) AS start_date, 
--     MAX(End_Date) AS end_date 
-- FROM ( 
--     SELECT 
--          Start_Date, 
--          End_Date, 
--          DATE_SUB(Start_Date, INTERVAL ROW_NUMBER() OVER (ORDER BY Start_Date) DAY) AS grp 
--     FROM Projects) t 
-- GROUP BY grp 
-- ORDER BY DATEDIFF(MAX(End_Date), MIN(Start_Date)), MIN(Start_Date);