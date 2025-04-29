# Write your MySQL query statement below
#to form a triangel a + b > c and a + c > b and b + c > a
SELECT
    x, y, z, (case when x + y > z and x + z > y and y + z > x then 'Yes' else 'No' end) as triangle
FROM Triangle
