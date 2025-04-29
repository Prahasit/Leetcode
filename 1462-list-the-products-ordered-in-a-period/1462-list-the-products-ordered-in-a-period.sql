# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) as unit
FROM Products p 
JOIN Orders o on p.product_id = o.product_id
WHERE year(o.order_date) = '2020' and month(o.order_date) = '02'
GROUP BY p.product_id
HAVING sum(o.unit) >= 100
