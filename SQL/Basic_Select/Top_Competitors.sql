-- Medium Level Problem

SELECT h.hacker_id, h.name
FROM Hackers h
JOIN Submissions s USING(hacker_id)
JOIN Challenges c USING(challenge_id)
JOIN Difficulty d USING(difficulty_level)
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.submission_id) > 1
ORDER BY COUNT(DISTINCT s.submission_id) DESC, h.hacker_id ASC;