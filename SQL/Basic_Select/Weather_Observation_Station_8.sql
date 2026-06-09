-- Easy Level Problem

SELECT DISTINCT city
FROM STATION
WHERE UPPER(city) REGEXP '^[AEIOU].*[AEIOU]$';

-- ^[AEIOU].{3}[AEIOU]$ --> if it was a 3 character lenght btw start and end

-- ^: from the start of the string
-- [AEIOU]: look for one of these letters
-- . : any number of characters
-- *: repeated 0 or more times
-- [AEIOU]: look for another vowel
-- $: end string

-- [^AEIOU]: any character that IS NOT a vowel