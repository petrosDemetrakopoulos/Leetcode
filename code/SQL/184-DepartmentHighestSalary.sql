SELECT Department.name AS 'Department', Employee.name AS 'Employee', p.salary 
FROM (SELECT departmentId, MAX(salary) AS salary FROM Employee
GROUP BY departmentId) AS p 
INNER JOIN Employee ON p.salary = Employee.salary AND p.departmentId = Employee.departmentId
INNER JOIN Department ON p.departmentId = Department.id