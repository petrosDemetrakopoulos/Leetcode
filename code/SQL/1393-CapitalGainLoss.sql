SELECT stock_name, 
 SUM(
  CASE operation
   WHEN 'Buy' THEN -price
   ELSE price
  END
 ) "capital_gain_loss"
 FROM STOCKS
GROUP BY stock_name;