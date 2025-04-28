# Write your MySQL query statement below
(
SELECT name as results
FROM users u
JOIN MovieRating mr
ON u.user_id = mr.user_id
GROUP BY u.user_id
ORDER BY count(mr.rating) desc, u.name asc
LIMIT 1
)

UNION ALL

(
SELECT m.title as results
FROM Movies m
JOIN MovieRating mr
ON m.movie_id = mr.movie_id
WHERE month(created_at) = 2 and year(created_at) = 2020
GROUP BY m.movie_id
ORDER BY avg(mr.rating) DESC, m.title asc
LIMIT 1
)