# Employee Management System using OOP

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary: $", float(self.salary))


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary: $", float(self.salary))
        print("Department:", self.department)


person = None
employee = None
manager = None

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == "2":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)

        print(f"\nEmployee created with name: {name}, age: {age}, "
              f"ID: {emp_id}, and salary: ${salary}.")

    elif choice == "3":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)

        print(f"\nManager created with name: {name}, age: {age}, "
              f"ID: {emp_id}, salary: ${salary}, "
              f"and department: {department}.")

    elif choice == "4":
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        detail_choice = input("Enter your choice: ")

        if detail_choice == "1":
            if person:
                person.show_details()
            else:
                print("\nNo Person record found.")

        elif detail_choice == "2":
            if employee:
                employee.show_details()
            else:
                print("\nNo Employee record found.")

        elif detail_choice == "3":
            if manager:
                manager.show_details()
            else:
                print("\nNo Manager record found.")

        else:
            print("\nInvalid choice!")

    elif choice == "5":
        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
