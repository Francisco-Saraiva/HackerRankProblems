-- Medium Level Problem

With BestScores AS (
    SELECT hacker_id, h.name, s.challenge_id, MAX(s.score) as max_score
    FROM Hackers h
    JOIN Submissions s USING(hacker_id)
    GROUP BY hacker_id, h.name, challenge_id
)

SELECT hacker_id, name, SUM(max_score) AS total_score
FROM BestScores
GROUP BY hacker_id, name
HAVING SUM(max_score) > 0
ORDER BY SUM(max_score) DESC, hacker_id ASC;
