-- Medium Level Problem

SELECT CONCAT(name, '(', LEFT(occupation, 1), ')')
FROM Occupations
ORDER BY name;

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(occupation), 's.')
FROM Occupations
GROUP BY occupation
ORDER BY COUNT(*), occupation;