import os
import json
import datetime
from employee import Employee
from utils import format_address, generate_sequential_id

# ==========================
# Paths / Storage
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "employees.json"))


def ensure_data_file() -> None:
    """Ensure the JSON file exists."""
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=8, ensure_ascii=False)


def load_employees() -> list[dict]:
    """Load employees from JSON."""
    ensure_data_file()
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_employees(employees: list[dict]) -> None:
    """Save employees to JSON."""
    ensure_data_file()
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(employees, f, indent=8, ensure_ascii=False)


# ==========================
# Input helpers
# ==========================

def prompt_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def prompt_email(message: str) -> str:
    while True:
        email = input(message).strip()
        if "@" in email and "." in email:
            return email
        print("Invalid email format. Please try again.")


# ==========================
# Employee Management Logic
# ==========================

def add_employee():
    """Register a new employee and save it to the JSON file."""
    name = input("Enter employee name: ").strip()
    age = prompt_int("Enter employee age: ")
    email = prompt_email("Enter employee email: ")

    address = {
        "street": input("Enter street address: ").strip(),
        "city": input("Enter city: ").strip(),
        "state": input("Enter state: ").strip().upper(),
        "zip": input("Enter zip code: ").strip(),
    }

    position = input("Enter employee position: ").strip()
    department = input("Enter employee department: ").strip()
    salary = prompt_float("Enter employee salary: ")

    employees = load_employees()
    employee_id = str(generate_sequential_id(employees))

    employee = Employee(
        name=name,
        age=age,
        email=email,
        address=address,
        position=position,
        department=department,
        salary=salary,
        employee_id=employee_id,
        date_hired=datetime.date.today().isoformat(),
        active=True,
    )

    employees.append(employee.to_dict())
    save_employees(employees)

    print(f"Employee {name} added with ID {employee_id}.")


def list_employees():
    """Print all employees in a formatted table."""
    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    # Sort by ID (numeric)
    employees.sort(key=lambda e: int(e.get("employee_id", 0)))

    print("\nEmployee List:")
    print(
        "{:<5} {:<20} {:<5} {:<25} {:<40} {:<12} {:<15} {:<10} {:<12} {:<10} {:<16}".format(
            "ID",
            "Name",
            "Age",
            "Email",
            "Address",
            "Position",
            "Department",
            "Salary",
            "Date Hired",
            "Status",
            "Deactivated Date",
        )
    )
    print("-" * 181)

    for emp in employees:
        address_str = format_address(emp.get("address"))
        status_color = "\033[92mACTIVE\033[0m" if emp.get("active") else "\033[91mINACTIVE\033[0m"

        print(
            "{:<5} {:<20} {:<5} {:<25} {:<40} {:<12} {:<15} {:<10} {:<12} {:<20} {:<16}".format(
                emp.get("employee_id", ""),
                emp.get("name", ""),
                emp.get("age", ""),
                emp.get("email", ""),
                address_str,
                emp.get("position", ""),
                emp.get("department", ""),
                f"{float(emp.get('salary', 0.0)):.2f}",
                emp.get("date_hired", ""),
                status_color,
                emp.get("deactivated_date", "----"),
            )
        )


def edit_salary():
    """Edit the salary of an active employee."""
    employee_id = input("Enter employee ID to edit salary: ").strip()
    employees = load_employees()

    for emp in employees:
        if str(emp.get("employee_id")) == employee_id:
            if not emp.get("active", True):
                print("Cannot edit salary of an inactive employee.")
                return

            new_salary = prompt_float(f"Enter new salary for {emp.get('name', '')}: ")
            emp["salary"] = new_salary

            save_employees(employees)
            print(f"Salary updated for {emp.get('name', '')}.")
            return

    print("Employee not found.")


def deactivate_employee():
    """Deactivate an employee and register the deactivation date."""
    employee_id = input("Enter employee ID to deactivate: ").strip()
    employees = load_employees()

    for emp in employees:
        if str(emp.get("employee_id")) == employee_id:
            if not emp.get("active", True):
                print(f"Employee {emp.get('name', '')} is already inactive.")
                return

            emp["active"] = False
            emp["deactivated_date"] = datetime.date.today().isoformat()

            save_employees(employees)
            print(f"Employee {emp.get('name', '')} has been deactivated.")
            return

    print("Employee not found.")


def show_report():
    """Show a summary report of employees and salary expenses."""
    employees = load_employees()

    total_employees = len(employees)
    active_employees = sum(1 for emp in employees if emp.get("active"))
    inactive_employees = total_employees - active_employees
    total_salary = sum(float(emp.get("salary", 0.0)) for emp in employees if emp.get("active"))

    print("\nEmployee Report")
    print("------------------------------------------------------------")
    print(f"Total Employees: {total_employees} employees")
    print(f"\033[92mACTIVE\033[0m Employees: {active_employees} employees")
    print(f"\033[91mINACTIVE\033[0m Employees: {inactive_employees} employees")
    print(f"Total Salary Expense: ${total_salary:,.2f} USD")
    print("------------------------------------------------------------")


# ====================
# Main menu / entrypoint
# ====================

def main():
    ensure_data_file()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Edit Employee Salary")
        print("4. Deactivate Employee")
        print("5. Show Report")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            edit_salary()
        elif choice == "4":
            deactivate_employee()
        elif choice == "5":
            show_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
