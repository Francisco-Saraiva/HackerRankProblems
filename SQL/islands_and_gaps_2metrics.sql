DROP TABLE IF EXISTS Dates;

CREATE TABLE IF NOT EXISTS Dates (
    StartDate DATE,
    EndDate DATE
);

INSERT INTO Dates (StartDate, EndDate) VALUES
('2017-08-24', '2017-09-23'),
('2017-08-24', '2017-09-20'),
('2017-09-23', '2017-09-27'),
('2017-09-25', '2017-10-10'),
('2017-10-17', '2017-10-18'),
('2017-10-25', '2017-11-03'),
('2017-11-03', '2017-11-15');


-- Step 1: create an id for each element (ordered by date)
-- Add the previous element to compare in front of each element
WITH Dates_id AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY StartDate, EndDate) AS id,
        StartDate,
        EndDate,
        MAX(EndDate) OVER(
            ORDER BY StartDate, EndDate 
            ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
        ) AS MaxPreviousEndDate
    FROM Dates
),

-- Step 2: create a flag for dates where there is an "island" start
Dates_flagged AS (
    SELECT
        *,
        CASE
            WHEN MaxPreviousEndDate >= StartDate THEN 0
            ELSE 1
        END AS flagged_date
    FROM Dates_id
),

-- Step 3: create an id for every group based on the flagged dates
Dates_groups AS (
    SELECT
        *,
        SUM(flagged_date) OVER(ORDER BY id) AS island_id
    FROM Dates_flagged
)

-- Step 4: final query, fetching the "limits" of each island (date ranges) per island
SELECT
    MIN(StartDate) AS start_date,
    MAX(EndDate) AS end_date,
    TIMESTAMPDIFF(DAY, MIN(StartDate), MAX(EndDate)) AS day_range
FROM Dates_groups
GROUP BY island_id
ORDER BY day_range;

-- SELECT *
-- FROM Dates_groups;





