import json
import os
from employee import Developer, Manager

class EmployeeManagementSystem:
    def __init__(self):
        self.Employee=[] #store all employees (Developer and manager)
        self.data_file = 'data/employees.json'

        if not os.path.exists('data'):
            os.makedirs('data')
    
        self.read_data()

    # add employees function
    def add_employee(self,employee):
        self.Employee.append(employee)
        self.save_data()
    
    # display all employees data
    def display_all_employees(self):
        if not self.Employee:
            print('not found employees')
        else:
            for em in self.Employee:
                em.display_details()
    
    # saving the data

    def save_data(self):
        with open(self.data_file,'w') as file:
            json.dump([em.to_dict() for em in self.Employee],file)


    # read data from file function
    
    def read_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data= json.load(file)

                for item in data:
                    if item['type']=='Developer':
                        self.Employee.append(
                            Developer(item["name"], item["Age"], item["salary"], item["programming language"])
                                            )
                    elif item['type']=='Manager':
                        self.Employee.append(
                            Manager(item["name"], item["age"], item["salary"],item["department"])
                                            )
                        
















































# class EmployeeManagementSystem:
#     def __init__(self):
#         self.employees = []
#         self.data_file = 'data/employees.json'

#         if not os.path.exists('data'):
#             os.makedirs('data')
        
#         self.load_data()

#     def add_employee(self, employee):
#         self.employees.append(employee)
#         self.save_data()

#     def display_all_employees(self):
#         if not self.employees:
#             print("No employees found.")
#         else:
#             for emp in self.employees:
#                 emp.display_details()
#                 print("-" * 30)
    
#     def save_data(self):
#         with open(self.data_file, 'w') as file:
#             json.dump([emp.to_dict() for emp in self.employees], file)

#     def load_data(self):
#         if os.path.exists(self.data_file):
#             with open(self.data_file, 'r') as file:
#                 data = json.load(file)
#                 for item in data:
#                     if item["type"] == "Developer":
#                         self.employees.append(
#                             Developer(item["name"], item["age"], item["salary"], item["programming_language"])
#                         )
#                     elif item["type"] == "Manager":
#                         self.employees.append(
#                             Manager(item["name"], item["age"], item["salary"], item["department"])
#                         )
