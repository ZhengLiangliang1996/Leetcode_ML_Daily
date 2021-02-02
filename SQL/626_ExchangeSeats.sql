# Write your MySQL query statement below
WITH window1 AS(
    SELECT id
        , student
        , LAG(student, 1) OVER(ORDER BY id) AS before1
        , LEAD(student, 1) OVER(ORDER BY id) AS next1
    FROM seat
)

SELECT id
    #奇数个 到最后那个 可能没有next 则需要由原本代替
    , IF(id % 2 = 0, before1, IFNULL(next1, student)) AS student
FROM window1
