CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT salary FROM(
        SELECT salary, dense_rank() 
        OVER(ORDER BY salary DESC)r FROM Employee) p
        WHERE r=N LIMIT 1
  );
END