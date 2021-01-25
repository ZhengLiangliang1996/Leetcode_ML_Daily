WITH
HIGHEST AS (
  SELECT Name
    , Salary
    , DepartmentId
    , RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) as rnk
  FROM
    Employee
)
SELECT
  D.Name as Department,
  E.Name as Employee,
  E.Salary
FROM
  HIGHEST E
JOIN Department D on E.DepartmentId = D.Id
WHERE
  E.rnk = 1
