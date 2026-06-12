-- Medium Level Problem

WITH OccupationCounts AS (
    SELECT
        name,
        occupation,
        ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rn
    FROM Occupations
)

SELECT
    MAX(CASE WHEN occupation = 'Doctor' THEN name END) AS Doc,
    MAX(CASE WHEN occupation = 'Professor' THEN name END) AS Prof,
    MAX(CASE WHEN occupation = 'Singer' THEN name END) AS Sng,
    MAX(CASE WHEN occupation = 'Actor' THEN name END) AS Act
FROM OccupationCounts
GROUP BY rn
ORDER BY rn;
