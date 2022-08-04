SELECT name, IFNULL(SUM(distance), 0) AS travelled_distance FROM Rides
RIGHT JOIN Users ON Rides.user_id = Users.id
GROUP BY user_id
ORDER BY travelled_distance DESC, name ASC