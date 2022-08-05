SELECT a.name AS Employee
FROM employee a, employee b
WHERE a.managerId = b.id AND b.salary < a.salary;