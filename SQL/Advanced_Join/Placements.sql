-- Medium Level Problem

SELECT s.name
FROM Students s
JOIN Friends f USING(id)
JOIN Packages p1 USING(id)
JOIN Packages p2 ON f.friend_id = p2.id
WHERE p2.salary > p1.salary
ORDER BY p2.salary;