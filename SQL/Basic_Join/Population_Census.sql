-- Easy level Problem
SELECT SUM(c.population) AS total_population
FROM CITY c
JOIN COUNTRY p ON c.countrycode = p.code
WHERE p.continent = 'Asia';