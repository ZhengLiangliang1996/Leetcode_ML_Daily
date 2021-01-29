# Write your MySQL query statement below
WITH 

LagT AS (
    SELECT id
        , recordDate
        , Temperature
        , LAG(Temperature, 1) OVER(ORDER BY recordDate) AS temYesterday
        , LAG(recordDate) OVER(ORDER BY recordDate) AS dateYesterday
    FROM Weather
)

SELECT id

FROM LagT

WHERE temYesterday < Temperature
    AND DATEDIFF(recordDate, dateYesterday) = 1
