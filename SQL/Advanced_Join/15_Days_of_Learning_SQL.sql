-- Hard Level Problem

------------------------------- For Unique Hackers -------------------------------

WITH Day_Streaks AS (
    SELECT
        s.submission_date,
        h.hacker_id,
        h.name,
        DENSE_RANK() OVER (PARTITION BY h.hacker_id ORDER BY s.submission_date) AS streak
    FROM Hackers h
    JOIN Submissions s ON h.hacker_id = s.hacker_id
    ORDER BY s.submission_date
),

Num_Unique AS (
    SELECT
        submission_date,
        COUNT(DISTINCT hacker_id) AS unique_hackers
    FROM Day_Streaks Ds
    WHERE DATEDIFF(submission_date, '2016-03-01') + 1 = streak
    GROUP BY submission_date
),
------------------------------------------------------------------------------------

-------------------------------- For Max Submissions -------------------------------

Submission_Count AS (
    SELECT 
        s.submission_date,
        s.hacker_id,
        COUNT(DISTINCT submission_id) AS submission_count
    FROM Hackers h
    JOIN Submissions s ON h.hacker_id = s.hacker_id
    GROUP BY s.submission_date, s.hacker_id
),

Max_Submissions AS (
    SELECT
        submission_date,
        MAX(submission_count) AS maximum_submissions
    FROM Submission_Count
    GROUP BY submission_date
), 

Max_Submissions_per_Day AS (
    SELECT 
        Ms.submission_date,
        MIN(Sc.hacker_id) AS hacker_id
    FROM Max_Submissions Ms
    JOIN Submission_Count Sc 
        ON Ms.submission_date = Sc.submission_date 
        AND Ms.maximum_submissions = Sc.submission_count
    GROUP BY Ms.submission_date
)

-----------------------------------------------------------------------------
-------------------------------- Final Output -------------------------------

SELECT 
    Mspd.submission_date,
    Nu.unique_hackers,
    hacker_id,
    h.name
FROM Max_Submissions_per_Day AS Mspd
JOIN Hackers h USING(hacker_id)
JOIN Num_Unique Nu ON Mspd.submission_date = Nu.submission_date
ORDER BY Mspd.submission_date;
