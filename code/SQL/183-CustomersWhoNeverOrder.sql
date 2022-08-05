SELECT name AS 'Customers' FROM Customers WHERE id NOT IN 
(SELECT Customers.id from Customers INNER JOIN Orders ON Customers.id = Orders.customerId)