import json

#Loading employees from the JSON file
def load_employees():
    with open('employees.JSON', 'r') as file:
        employees = json.load(file)
    return employees

#Saving employees to the JSON file
def save_employees(employees):
    with open('employees.JSON', 'w') as file:
        json.dump(employees, file, indent=4)


#Adding a new employee
def add_employee(emp_name, emp_id, emp_email, emp_dept, emp_salary):
    employees = load_employees()
    new_employee = {
        "emp-name": emp_name,
        "emp-id": emp_id,
        "emp-email": emp_email,
        "emp-dept": emp_dept,
        "emp-salary": emp_salary
    }

    for employee in employees:
        if employee["emp-email"] == emp_email:
            print("This email is already registered. Please use a different email.")
            return

    employees.append(new_employee)
    save_employees(employees)

#View all employees
def view_all_employees():
    employees = load_employees()
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(f"Name: {employee.get('emp-name')} | ID: {employee.get('emp-id')} | Email: {employee.get('emp-email')} | Department: {employee.get('emp-dept')} | Salary: {employee.get('emp-salary')}")

#Reading an employee's details
def read_employee(emp_id):
    employees = load_employees()
    for employee in employees:
        if employee["emp-id"] == emp_id:
            return employee
    return None

#Updating an existing employee
def update_employee(emp_id):
    employees = load_employees()
    employee_found = False

    for employee in employees:
        if str(employee["emp-id"]) == str(emp_id):
            employee_found = True

            print(f"\n--- Employee found - Name: {employee['emp-name']} ---")

            print("1. Update Name")
            print("2. Update ID")
            print("3. Update Email")
            print("4. Update Department")
            print("5. Update Salary")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                new_name = input("Enter new name: ")
                employee["emp-name"] = new_name

            elif choice == '2':
                new_id = input("Enter new ID: ")
                employee["emp-id"] = new_id

            elif choice == '3':
                while True:
                    new_email = input("Enter new email: ")

                    if any(emp["emp-email"] == new_email for emp in employees):
                        print("This email is already registered. Please use a different email.")
                    else:
                        employee["emp-email"] = new_email
                        break

            elif choice == '4':
                new_dept = input("Enter new department: ")
                employee["emp-dept"] = new_dept

            elif choice == '5':
                new_salary = input("Enter new salary: ")
                employee["emp-salary"] = new_salary

            else:
                print("Invalid choice. No updates made.")
                return False

            save_employees(employees)
            print("Employee details updated successfully.")
            return True

    print(f"Employee with ID {emp_id} not found.")
    return False

#Deleting an employee
def delete_employee(emp_id):
    employees = load_employees()

    for employee in employees:
        if employee["emp-id"] == emp_id:
            employees.remove(employee)
            save_employees(employees)
            print(f"Employee with ID {emp_id} has been deleted.")
            return
        
    print(f"Employee with ID {emp_id} not found.")

#Filtering employees based on different criteria
def filter_employees():
    employees = load_employees()
    print("\n--- Filter Employees ---")
    print("1. Filter by Name")
    print("2. Filter by Department")
    print("3. Filter by Salary Range")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        name = input("Enter name to filter: ")
        filtered_employees = [emp for emp in employees if emp["emp-name"].lower() == name.lower()]
        if filtered_employees:
            print(f"\nEmployees named {name}:")
            for employee in filtered_employees:
                print(f"Name: {employee.get('emp-name')} | ID: {employee.get('emp-id')} | Email: {employee.get('emp-email')} | Salary: {employee.get('emp-salary')}")
        else:
            print(f"No employees found named {name}.")

    elif choice == '2':
        dept = input("Enter department to filter: ")
        filtered_employees = [emp for emp in employees if emp["emp-dept"].lower() == dept.lower()]
        if filtered_employees:
            print(f"\n Employees in {dept} department:")
            for employee in filtered_employees:
                print(f"Name: {employee.get('emp-name')} | ID: {employee.get('emp-id')} | Email: {employee.get('emp-email')} | Department: {employee.get('emp-dept')} | Salary: {employee.get('emp-salary')}")
        else:
            print(f"No employees found in {dept} department.")

    elif choice == '3':
        min_salary = int(input("Enter minimum salary: "))
        max_salary = int(input("Enter maximum salary: "))
        filtered_employees = [emp for emp in employees if min_salary <= int(emp["emp-salary"]) <= max_salary]
        if filtered_employees:
            print(f"\nEmployees with salary between {min_salary} and {max_salary}:")
            for employee in filtered_employees:
                print(f"Name: {employee.get('emp-name')} | ID: {employee.get('emp-id')} | Email: {employee.get('emp-email')} | Department: {employee.get('emp-dept')} | Salary: {employee.get('emp-salary')}")
        else:
            print(f"No employees found with salary between {min_salary} and {max_salary}.")
    else:
        print("Invalid choice. Returning to main menu.")

#Menu 
def menu():
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Read Employee Details")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Filter Employees")
    print("7. Exit")

# Main Program
def main():
    while True:
        menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            emp_name = input("Enter Employee Name: ")
            emp_id = input("Enter Employee ID: ")
            emp_email = input("Enter Employee Email: ")
            emp_dept = input("Enter Employee Department: ")
            emp_salary = input("Enter Employee Salary: ")
            add_employee(emp_name, emp_id, emp_email, emp_dept, emp_salary)

        elif choice == '2':
            view_all_employees()

        elif choice == '3':
            emp_id = input("Enter employee ID to read details: ")
            employee = read_employee(emp_id)
            if employee:
                print(f"ID: {employee.get('emp-id')} | Name: {employee.get('emp-name')} | Email: {employee.get('emp-email')} | Department: {employee.get('emp-dept')} | Salary: {employee.get('emp-salary')}")
            else:
                print(f"Employee with ID {emp_id} not found.")

        elif choice == '4':
            emp_id = input("Enter employee ID to update details: ")
            update_employee(emp_id)

        elif choice == '5':
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)

        elif choice == '6':
            filter_employees()   

        elif choice == '7':
            print("Exiting the Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()