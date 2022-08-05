SELECT DISTINCT product_id, product_name FROM 
(SELECT p.product_id, p.product_name FROM Sales s INNER JOIN Product p ON s.product_id = p.product_id WHERE sale_date >= '2019-01-01' AND sale_date <= '2019-03-31') temp 
WHERE temp.product_id NOT IN 
(SELECT product_id FROM Sales WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31' AND quantity > 0)