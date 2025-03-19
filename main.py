from employee import Developer,Manager
from system import EmployeeManagementSystem

def main():
    system = EmployeeManagementSystem()

    while True:
        print('\n------Employee Management System------')
        print('1. Add Developer')
        print('2. Add manager')
        print('3. Display all Employees')
        print('4. exit')

        choice = input('Enter your choice:')

        if choice=='1':
            name = input('enter Developer name:')
            age = input('enter Developer age:')
            salary = input('enter Developer salary:')
            prgm = input('enter Developer Programming Language:')

            developer = Developer(name,age,salary,prgm)
            system.add_employee(developer)
            print('Developer Added Successfully')

        elif choice=='2':
            name = input('enter Manager name:')
            age = input('enter Manager age:')
            salary = input('enter Manager salary:')
            department = input('enter Manager Department:')

            manager = Manager(name,age,salary,department)
            system.add_employee(manager)
            print('Manager Added Successfully')
        elif choice=='3':
            system.display_all_employees()
        
        elif choice=='4':
            print('you are succesfully exited the system')
            break
        else:
            print('invalid choice ! plz try agian later')

if __name__ == "__main__":
    main()       