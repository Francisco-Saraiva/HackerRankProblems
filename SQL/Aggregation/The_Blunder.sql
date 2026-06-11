-- Easy Level Problem

SELECT 
     CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))
FROM Employees;


-- with explicit casting

-- SELECT 
--     CEIL(
--         AVG(salary) - AVG(CAST(REPLACE(CAST(salary AS CHAR), '0', '') AS DECIMAL))
--     )
-- FROM Employees;