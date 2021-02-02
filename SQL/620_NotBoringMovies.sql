# Write your MySQL query statement below
SELECT *

FROM cinema 

WHERE description NOT IN ('boring')
    AND  id % 2 != 0

ORDER BY rating DESC
