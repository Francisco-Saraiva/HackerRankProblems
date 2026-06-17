DROP TABLE IF EXISTS CardDraws;

CREATE TABLE IF NOT EXISTS CardDraws (
    DrawOrder INT,      -- The order the cards were pulled (1st, 2nd, 3rd...)
    PlayerName VARCHAR(50),
    CardValue INT       -- The actual number value on the card (2 through 10)
);

INSERT INTO CardDraws (DrawOrder, PlayerName, CardValue) VALUES
-- Charlie's Draws
(1, 'Charlie', 3),  -- Island 1
(2, 'Charlie', 4),  
(3, 'Charlie', 5),  
(4, 'Charlie', 2),  -- Island 2 (Gap! Dropped down to 2)
(5, 'Charlie', 8),  -- Island 3 (Gap! Jumped up to 8)
(6, 'Charlie', 9),  
(7, 'Charlie', 10), 
(8, 'Charlie', 4),  -- Island 4 (Gap! Dropped to 4)

-- Dennis's Draws
(9, 'Dennis',  5),  -- Island 1
(10, 'Dennis', 6),  
(11, 'Dennis', 8),  -- Island 2 (Gap! Skipped 7)
(12, 'Dennis', 9),  
(13, 'Dennis', 10), 

-- Mac's Draws (The tricky ones!)
(14, 'Mac', 2),  -- Island 1
(15, 'Mac', 3),  
(16, 'Mac', 3),  -- Island 2? (Tricky: He drew a 3, then another 3. That breaks a "+1" consecutive run!)
(17, 'Mac', 4),  -- Island 2 continues
(18, 'Mac', 5),  
(19, 'Mac', 2);  -- Island 3 (Gap! Dropped to 2)


-- Step 1: create an id for each element (ordered by draworder)
-- Add the previous element to compare in front of each element
-- We need to separate by each player
WITH CardDrawsId AS(
    SELECT
        DrawOrder,
        ROW_NUMBER() OVER(PARTITION BY PlayerName ORDER BY DrawOrder) AS new_id,
        PlayerName,
        CardValue,
        LAG(CardValue,1) OVER(PARTITION BY PlayerName ORDER BY DrawOrder) AS PreviousDraw

    FROM CardDraws
),

-- Step 2: create a flag for draws where there is an "island" start
-- Sequences can go up or down, but break when the card is equal
-- Example: 4 -> 5 -> 6 -> 5 -> 6 is valid; 4 -> 5 -> 5 -> 6 is invalid
DrawsFlagged AS (
    SELECT
        *,
        CASE
            WHEN PreviousDraw IS NULL THEN 1
            WHEN CardValue = PreviousDraw + 1 THEN 0
            WHEN CardValue = PreviousDraw - 1 THEN 0
            ELSE 1
        END AS sequence_start
    FROM CardDrawsId
),

-- Step 3: create an id for every group based on the flagged draws
DrawsGrouped AS (
    SELECT
        *,
        SUM(sequence_start) OVER(PARTITION BY PlayerName ORDER BY new_id) AS island_id
    FROM DrawsFlagged
)

-- Step 4: Final query, fetch whatever you need
SELECT
    PlayerName,
    MIN(CardValue) AS min_seq,
    MAX(CardValue) AS max_seq,
    COUNT(*) AS seq_length
FROM DrawsGrouped
GROUP BY PlayerName, island_id
ORDER BY PlayerName, seq_length DESC;
