# Write your MySQL query statement below
select name as employee from employee e where salary > (select salary from employee where id = e.managerId)