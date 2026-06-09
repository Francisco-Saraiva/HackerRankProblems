-- Easy Level Problem

SELECT (
    COUNT(id) - COUNT(DISTINCT city) 
) FROM STATION;