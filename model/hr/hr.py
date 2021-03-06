""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from types import new_class
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH_INDEX = 2
DEPARTMENT_INDEX = 3
CLEARANCE_INDEX = 4


def list_employees():
    table = data_manager.read_table_from_file(DATAFILE)
    table.insert(0, HEADERS)
    return table

def add_employee(new_employee):
    new_employee.insert(0, util.generate_id())
    new_table = data_manager.read_table_from_file(DATAFILE)
    new_table.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, new_table, ";")

def update_employee(updated_employee_id, updated_employee_data):
    new_table = data_manager.read_table_from_file(DATAFILE)
    for employee in new_table:
        if employee[ID_INDEX] == updated_employee_id:
            updated_employee_data.insert(0, employee[ID_INDEX])
            new_table[new_table.index(employee)] = updated_employee_data
    data_manager.write_table_to_file(DATAFILE, new_table, ";")
    
def delete_employee(deleted_employee_id):
    new_table = data_manager.read_table_from_file(DATAFILE)
    for employee in new_table:
        if employee[ID_INDEX] == deleted_employee_id:
            new_table.pop(new_table.index(employee))
    data_manager.write_table_to_file(DATAFILE, new_table, ";")

def get_oldest_and_youngest():
    table = data_manager.read_table_from_file(DATAFILE)
    date_of_birth_list = []
    for employee in table:
        date_split = [int(i) for i in employee[DATE_OF_BIRTH_INDEX].split("-")]
        date_of_birth_list.append(date_split)
    oldest_date_of_birth_index = date_of_birth_list.index(min(date_of_birth_list))
    youngest_date_of_birth_index = date_of_birth_list.index(max(date_of_birth_list))
    return(table[oldest_date_of_birth_index][NAME_INDEX], table[youngest_date_of_birth_index][NAME_INDEX])

def count_employees_with_clearance(celearance_level):
    table = data_manager.read_table_from_file(DATAFILE)
    employees_with_clearance_level = 0
    for employee in table:
        if int(employee[CLEARANCE_INDEX]) >= celearance_level:
            employees_with_clearance_level += 1
    return employees_with_clearance_level

def count_employees_per_department():
    table = data_manager.read_table_from_file(DATAFILE)
    employees_per_department = {}
    for employee in table:
        if employee[DEPARTMENT_INDEX] not in employees_per_department:
            employees_per_department[employee[DEPARTMENT_INDEX]] = 1
        elif employee[DEPARTMENT_INDEX] in employees_per_department:
            employees_per_department[employee[DEPARTMENT_INDEX]] += 1
    return employees_per_department

def get_employee_average_age():
    table = data_manager.read_table_from_file(DATAFILE)
    current_year = 2021
    list_of_age = []
    for age in table:
        list_of_age.append(current_year - int(((age[DATE_OF_BIRTH_INDEX]).split("-"))[0]))
    average_age = sum(list_of_age) / len(list_of_age)
    return int(average_age)

