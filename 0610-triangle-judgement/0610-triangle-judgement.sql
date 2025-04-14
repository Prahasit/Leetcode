# Write your MySQL query statement below
#to form a triangel a + b > c and a + c > b and b + c > a

select x, y, z, case when x + y > z and y + z > x and x + z > y then 'Yes' else 'No' end as triangle from Triangle