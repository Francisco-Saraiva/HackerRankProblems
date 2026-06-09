-- Easy Level Problem

(
    SELECT city, LENGTH(city) AS len
    FROM STATION
    ORDER BY len DESC, city
    LIMIT 1
)
UNION ALL
(
    SELECT city, LENGTH(city) AS len
    FROM STATION
    ORDER BY len ASC, city
    LIMIT 1
)