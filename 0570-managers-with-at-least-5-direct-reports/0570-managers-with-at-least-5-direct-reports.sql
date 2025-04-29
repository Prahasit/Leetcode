# Write your MySQL query statement below
SELECT e1.name
FROM Employee as e1
JOIN Employee as e2 on e1.id = e2.managerID
GROUP BY e1.id
HAVING count(e2.managerID) >= 5