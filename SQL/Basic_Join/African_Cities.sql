-- Easy level Problem
SELECT c.name
FROM City c
JOIN Country p ON c.countrycode = p.code
WHERE p.continent = 'Africa';