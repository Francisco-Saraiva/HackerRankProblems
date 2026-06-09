-- Easy Level Problem

SElECT DISTINCT city
FROM STATION
WHERE UPPER(city) REGEXP '^.*[^AEIOU]$';