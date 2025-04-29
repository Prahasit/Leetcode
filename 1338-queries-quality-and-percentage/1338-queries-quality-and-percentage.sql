# Write your MySQL query statement below
SELECT 
    query_name, 
    round(sum(rating / position) / count(rating),2) as quality,
    round(sum(rating < 3) * 100 / count(rating) ,2) as poor_query_percentage
FROM Queries 
GROUP BY query_name