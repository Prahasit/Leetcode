# Write your MySQL query statement below
-- Fourth solution: CTE + CASE-WHEN
with CTE_Category as
(select 
case when income  < 20000 then 'Low Salary'
when income between 20000 and 50000 then 'Average Salary'
when income > 50000 then 'High Salary'
end as category, 1 count from Accounts
union all
select 'Low Salary', 0 
union all
select 'Average Salary', 0
union all
select 'High Salary', 0
)
select category, sum(count) as accounts_count from CTE_Category group by category
