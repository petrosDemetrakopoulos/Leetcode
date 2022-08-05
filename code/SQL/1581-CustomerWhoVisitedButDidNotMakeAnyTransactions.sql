SELECT customer_id, count(DISTINCT(visit_id)) AS count_no_trans FROM Visits WHERE Visits.visit_id not in (SELECT Visits.visit_id FROM Visits LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id WHERE Transactions.amount > 0) group by customer_id