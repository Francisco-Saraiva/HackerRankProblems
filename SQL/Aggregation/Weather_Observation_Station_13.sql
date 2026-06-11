-- Easy Level Problem

SELECT ROUND(SUM(lat_n), 4)
FROM Station
WHERE lat_n BETWEEN 38.7880 AND 137.2345;