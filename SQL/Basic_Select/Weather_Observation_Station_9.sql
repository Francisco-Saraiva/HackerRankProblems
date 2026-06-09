-- Easy Level Problem

SELECT DISTINCT city
FROM STATION
WHERE UPPER(city) REGEXP '^[^AEIOU].*$';
