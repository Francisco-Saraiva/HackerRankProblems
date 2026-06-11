-- Easy Level Problem

SELECT
    CASE 
        WHEN C >= (A+B) OR B >= (A+C) OR A >= (B+C) THEN 'Not A Triangle'
        WHEN A = B AND B = C AND C = A THEN 'Equilateral'
        WHEN A = B OR B = C OR C = A THEN 'Isosceles'
        ELSE 'Scalene'
    END AS triangle_type
FROM Triangles;
