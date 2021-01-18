class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def getname(self):
    return self.name

  def setname(self, name):
    self.name = name

  def get_salary(self):
    return self.salary

  def setsalary(self, salary):
    if salary > 0:
      self.salary = salary

  def display(self):
    print("Name:", str(self.name))
    print("Salary:", str(self.salary))

class Company:

  def __init__(self):
    self.Employee_list = []

  def get_employee(self):
    return self.Employee_list
  
  def set_employee(self, current_list):
    if type(current_list) == list:
      self.Employee_list = current_list

  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.Employee_list.append(new_employee)

  def calc_avg_salary(self):
    total_sum = 0
    for emp in self.Employee_list:
      total_sum += emp.get_salary()
    return total_sum / len(self.employee)

  def display(self):
    for emp in self.Employee_list:
      print("Name:", str(emp.getname()))
      print("Salary:", str(emp.get_salary()))


