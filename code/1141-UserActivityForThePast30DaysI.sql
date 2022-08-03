SELECT day, SUM(active_users) AS active_users FROM 
(SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users FROM Activity 
WHERE activity_date <= '2019-07-27' AND activity_date >= '2019-06-28' GROUP BY user_id, activity_date 
HAVING COUNT(activity_type) >= 1) p GROUP BY day