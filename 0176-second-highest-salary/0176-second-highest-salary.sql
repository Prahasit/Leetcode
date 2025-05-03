# Write your MySQL query statement below
with cte as (
    SELECT salary as SecondHighestSalary, DENSE_RANK() over (order by salary desc) as rk
    FROM Employee
)
select CASE 
        WHEN COUNT(*) = 0 THEN NULL 
        ELSE SecondHighestSalary 
    END AS SecondHighestSalary
FROM CTE
where rk = 2 