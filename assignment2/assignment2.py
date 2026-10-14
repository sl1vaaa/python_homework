import csv
import os
import custom_module
from datetime import datetime

# Task 2

def read_employees():
    employees = {}
    rows = []
    try:
        with open("C:/Users/miros/CTD-repos/python_class/python_homework/csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i==0:
                    employees["fields"] = row
                else:
                    rows.append(row)
            employees["rows"] = rows
    except Exception as e:
        print(e)
        return
    else:
        return employees

employees = read_employees()
print(employees)

# Task 3

def column_index(fields):
    return employees["fields"].index(fields)

employee_id_column = column_index("employee_id")

# Task 4

def first_name(row_number):
    index = column_index("first_name")
    return employees['rows'][row_number][index]


# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row :
int(row[employee_id_column]) == employee_id , 
employees["rows"]))
    return matches

# Task 7

def sort_by_last_name():
    employees["rows"].sort(key= lambda row : row[column_index('last_name')])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8

def employee_dict(row):
    return dict(zip(employees["fields"][1:], row[1:]))

one_employee = employee_dict(['1', 'Cindy', 'Wade', '+222 656-486-3727'])
print(one_employee)

# Task 9

def all_employees_dict():
    all_employees = {}
    for i, employee in enumerate(employees["rows"]):
        all_employees[employee[0]] = employee_dict(employee)
    return all_employees

all_employees = all_employees_dict()
print(all_employees)

# Task 10

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Wohohoooo!!")

print(custom_module.secret)

# Task 12

def read_minutes():
    minutes1 = {}
    minutes2 ={}
    try:
        with open("C:/Users/miros/CTD-repos/python_class/python_homework/csv/minutes1.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            minutes1["fields"] = rows[0]
            minutes1["rows"] = [tuple(row) for row in rows[1:]]
    except Exception as e:
        print(e)
        return
    try:
        with open("C:/Users/miros/CTD-repos/python_class/python_homework/csv/minutes2.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            minutes2["fields"] = rows[0]
            minutes2["rows"] = [tuple(row) for row in rows[1:]]
    except Exception as e:
        print(e)
        return

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(minutes1, minutes2)


# Task 13

def create_minutes_set():
    return set(minutes1["rows"]) | set(minutes2["rows"])

minutes_set = create_minutes_set()

# Task 14

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x : (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()

# Task 14

def write_sorted_list():
    sorted(minutes_list, key=lambda x: x[1])

    sorted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    try:
        with open("C:/Users/miros/CTD-repos/python_class/python_homework/assignment2/minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])

            writer.writerows(sorted_list)
    except Exception as e:
        print(e)
        return
    else:
        return sorted_list

sorted_list = write_sorted_list()
print(sorted_list)