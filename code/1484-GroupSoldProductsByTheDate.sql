SELECT sell_date, count(distinct product) as num_sold, GROUP_CONCAT(distinct product) as products
FROM Activities
GROUP BY sell_date