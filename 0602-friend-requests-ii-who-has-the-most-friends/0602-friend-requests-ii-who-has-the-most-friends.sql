# Write your MySQL query statement below
SELECT requester_id as id, sum(num) as num FROM
    (
        SELECT requester_id, count(*) as num FROM RequestAccepted GROUP BY requester_id
        UNION ALL
        SELECT accepter_id as requester_id, count(*) as num FROM RequestAccepted GROUP BY accepter_id
    ) name
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1