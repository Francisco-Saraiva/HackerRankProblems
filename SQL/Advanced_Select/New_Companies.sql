-- Medium Level Problem

SELECT 
    company_code,
    c.founder,
    COUNT(DISTINCT(lead_manager_code)),
    COUNT(DISTINCT(senior_manager_code)),
    COUNT(DISTINCT(manager_code)),
    COUNT(DISTINCT(employee_code))
FROM Employee e
JOIN Company c USING(company_code)
GROUP BY company_code, c.founder
ORDER BY company_code
; 
-- Correct ordering for numeric
-- ORDER BY CAST(SUBSTRING(company_code, 2, 100) AS UNSIGNED) ASC