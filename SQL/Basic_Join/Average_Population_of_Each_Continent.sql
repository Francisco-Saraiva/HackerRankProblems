-- Easy level Problem
SELECT p.continent, FLOOR(AVG(c.population))
FROM CITY c
JOIN COUNTRY p ON c.countrycode = p.code
GROUP BY p.continent;