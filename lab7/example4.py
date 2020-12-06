employees = {}
for i in range(3):
  name = input("Enter name: ")
  salary = input("Enter salary: ")
  employees.update({name : salary})



sorted_salaries = sorted(employees.items(), reverse=True)

print(sorted_salaries)

