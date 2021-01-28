
# Write your MySQL query statement below

/*临时表 + LIMIT*/
SELECT (
SELECT DISTINCT Salary 
    FROM Employee
    ORDER BY Salary DESC 
    LIMIT 1,1
) AS SecondHighestSalary
