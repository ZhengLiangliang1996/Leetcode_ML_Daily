
WITH 

LOG AS (
    SELECT Num
        , LAG(Num) OVER() AS Lag1
        , LEAD(Num) OVER() AS Lead1
    FROM LOGS
)

SELECT DISTINCT Num AS ConsecutiveNums
FROM LOG

WHERE LOG.Num = LOG.Lag1 
AND LOG.Num = LOG.Lead1
