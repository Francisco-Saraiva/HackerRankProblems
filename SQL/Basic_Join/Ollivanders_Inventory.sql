-- Medium Level Problem

-- Solution 1: Using CTE to find the minimum coins needed for each power and age combination, then joining back to get the details of those wands.

-- WITH BestWands AS(
--     SELECT age, power, MIN(coins_needed) AS min_coins
--     FROM Wands
--     JOIN Wands_Property USING(code)
--     WHERE Wands_Property.is_evil = 0
--     GROUP BY power, age
-- )


-- SELECT w.id, wp.age, w.coins_needed, w.power
-- FROM Wands w
-- JOIN Wands_Property wp ON w.code = wp.code
-- JOIN BestWands bw 
--     ON w.power = bw.power 
--     AND bw.age = wp.age 
--     AND bw.min_coins = w.coins_needed
-- ORDER BY w.power DESC, wp.age DESC;

-- Solution 2: Using ROW_NUMBER() to rank wands by coins needed for each power and age combination, then selecting the top-ranked wands.

WITH WandsRanked AS(
    SELECT 
        w.id,
        wp.age,
        w.coins_needed,
        w.power,
        ROW_NUMBER()  OVER (
            PARTITION BY w.power, wp.age
            ORDER BY w.coins_needed
        ) AS rn
    FROM Wands w
    JOIN Wands_Property wp ON w.code = wp.code
    WHERE wp.is_evil = 0
)

SELECT id, age, coins_needed, power
FROM WandsRanked
WHERE rn = 1
ORDER BY power DESC, age DESC;




