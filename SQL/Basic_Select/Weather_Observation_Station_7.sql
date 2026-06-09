-- Easy Level Problem

SELECT DISTINCT city
FROM STATION
WHERE UPPER(city) LIKE '%A' OR UPPER(city) LIKE '%E' 
    OR UPPER(city) LIKE '%I' OR UPPER(city) LIKE '%O'
    OR UPPER(city) LIKE '%U'
;