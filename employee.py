from abc import ABC,abstractmethod

# employee class
class Employee(ABC):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

# developer class
class Developer(Employee):
    def __init__(self,name,age,salary,prgm_lang):
        super().__init__(name,age,salary)
        self.prgm_lang = prgm_lang

    def display_details(self):
       print(f"Developer name : {self.name}")
       print(f'Age : {self.age}')
       print(f'Salary : {self.salary}')
       print(f'Programming Language : {self.prgm_lang}')
       print()

    def to_dict(self):
        return {
            'type' : 'Developer',
            'name' : self.name ,
            'Age' : self.age ,
            'salary' :self.salary ,
            'programming language' : self.prgm_lang
        }
    
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_details(self):
        print(f"Manager Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")
        print()

    def to_dict(self):
        return {
            "type": "Manager",
            "name": self.name,
            "age": self.age,
            "salary": self.salary,
            "department": self.department
        }