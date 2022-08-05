SELECT employee_id FROM employees WHERE employee_id not in (select employee_id from salaries)
UNION
SELECT employee_id FROM salaries WHERE employee_id not in (select employee_id from employees)
ORDER BY employee_id