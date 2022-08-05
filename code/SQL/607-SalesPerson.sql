SELECT name FROM SalesPerson where name not in (
SELECT SalesPerson.name FROM Orders INNER JOIN SalesPerson on SalesPerson.sales_id = Orders.sales_id
INNER JOIN Company on Orders.com_id = Company.com_id WHERE Company.name = 'RED')