# Write your MySQL query statement below
SELECT max(salary) as secondHighestSalary
FROM Employee 
WHERE Salary < (
    Select max(salary) from EMployee
)