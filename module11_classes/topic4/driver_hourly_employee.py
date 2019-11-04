from module11_classes.topic4.employee_class import Employee
from module11_classes.topic4.hourly_employee_class import HourlyEmployee

new_emp = Employee('Smith', 'Kelly', '5151234567', '123 Main St', 'Des Moines, IA')
new_emp_hourly = HourlyEmployee(new_emp.last_name, new_emp.first_name, new_emp.phone_number, new_emp.address_1, new_emp.address_2, 10.00, '10-20-2019')
print(new_emp_hourly.display())
new_emp_hourly.give_raise(12.00)
print(new_emp_hourly.display())
del new_emp
