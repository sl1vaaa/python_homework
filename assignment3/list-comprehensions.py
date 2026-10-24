import csv
#Task 3

with open("./csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = [row for row in reader]

names = [name[1] + " " + name[2] for name in employees[1:]]
print(names)

employees_with_e = [name for name in names if "e" in name]

print(employees_with_e)