# Write your MySQL query statement below
WITH CTE as(
    SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id FROM RequestAccepted
)

SELECT id, count(id) as num
FROM CTE
GROUP BY id
ORDER BY num DESC
LIMIT 1
