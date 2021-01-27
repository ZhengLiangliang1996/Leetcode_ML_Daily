
# Write your MySQL query statement below
WITH 

ROW1 AS (
SELECT Name
    , Salary
    , DepartmentId
    , DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS `Rank`

FROM Employee
)

SELECT D.Name AS Department
    , E.Name AS Employee
    , Salary
FROM ROW1 AS E

INNER JOIN Department AS D 
    ON E.DepartmentId = D.Id

WHERE E.Rank <= 3

