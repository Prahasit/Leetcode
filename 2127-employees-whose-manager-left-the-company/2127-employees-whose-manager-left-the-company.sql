# Write your MySQL query statement below
SELECT employee_id
FROM Employees
where salary < 30000 
AND manager_id not in (SELECT employee_id from Employees)
ORDER BY employee_id
