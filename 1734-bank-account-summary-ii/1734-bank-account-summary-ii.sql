# Write your MySQL query statement below
Select u.name, sum(t.amount) as balance from Users u join Transactions t on u.account = t.account group by t.account having balance > 10000