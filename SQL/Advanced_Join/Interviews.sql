-- Hard Level Problem

-- We need to first aggregate View_Stats by challenge_id, otherwise will get duplicate rows when grouping by contest_id
WITH Vs AS(  
    SELECT 
        challenge_id,
        SUM(total_views) AS sum_tv,
        SUM(total_unique_views) AS sum_tuv
    FROM View_Stats
    GROUP BY challenge_id
),

-- Same reasoning for Submission_Stats
Ss AS (
    SELECT
        challenge_id,
        SUM(total_submissions) AS sum_ts,
        SUM(total_accepted_submissions) AS sum_tas
    FROM Submission_Stats
    GROUP BY challenge_id
)

SELECT
    ct.contest_id,
    ct.hacker_id,
    ct.name,
    SUM(Ss.sum_ts),  -- Still need to sum, since we are summing all challenges in a contest
    SUM(Ss.sum_tas),
    SUM(Vs.sum_tv),
    SUM(Vs.sum_tuv)
FROM Contests ct
JOIN Colleges cl ON ct.contest_id = cl.contest_id
JOIN Challenges ch ON cl.college_id = ch.college_id
LEFT JOIN Vs ON ch.challenge_id = Vs.challenge_id  -- Left join makes sure that we keep rows even if there are no views or submissions for a challenge
LEFT JOIN Ss ON ch.challenge_id = Ss.challenge_id
GROUP BY ct.contest_id, ct.hacker_id, ct.name
HAVING 
    (SUM(Ss.sum_ts) + SUM(Ss.sum_tas) + SUM(Vs.sum_tv) + SUM(Vs.sum_tuv)) > 0  -- We could separate  each one, but this is more efficient and easier to read
ORDER BY ct.contest_id ASC
;

