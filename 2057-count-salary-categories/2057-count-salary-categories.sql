# Write your MySQL query statement below
SELECT 
    'Low Salary' as category, 
    sum(case when income < 20000 then 1 else 0 end) as accounts_count
FROM Accounts

UNION ALL

SELECT 
    'Average Salary' as category, 
    sum(case when income >= 20000  and income <= 50000 then 1 else 0 end) as accounts_count
FROM Accounts

UNION ALL

SELECT 
    'High Salary' as category, 
    sum(case when income > 50000 then 1 else 0 end) as accounts_count
FROM Accounts
