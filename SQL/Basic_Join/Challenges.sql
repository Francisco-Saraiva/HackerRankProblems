-- Medium Level Problem

WITH ChallengeCounts AS (
    SELECT h.hacker_id, h.name, COUNT(DISTINCT c.challenge_id) AS num_challenges
    FROM Hackers h
    JOIN Challenges c USING(hacker_id)
    GROUP BY hacker_id, h.name
),

Freqs AS (
    SELECT
        num_challenges,
        COUNT(*) AS freq
    FROM ChallengeCounts
    GROUP BY num_challenges
)


SELECT hacker_id, name, num_challenges
FROM ChallengeCounts
JOIN Freqs USING(num_challenges)
WHERE 
    num_challenges = (SELECT MAX(num_challenges) FROM ChallengeCounts) OR
    Freqs.freq = 1 
ORDER BY num_challenges DESC, hacker_id ASC;