import json
import os
import datetime
from utils import generate_sequential_id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "employees.json"))


class Employee:
    def __init__(
        self,
        name,
        age,
        email,
        address,
        position,
        department,
        salary,
        employee_id=None,
        date_hired=None,
        active=True,
        deactivated_date=None,
    ):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.position = position
        self.department = department
        self.salary = salary
        self.employee_id = employee_id
        self.date_hired = date_hired or datetime.date.today().isoformat()
        self.active = active
        self.deactivated_date = deactivated_date

    def to_dict(self):
        """Convert the Employee object to a dictionary."""
        data = {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "address": self.address,
            "position": self.position,
            "department": self.department,
            "salary": self.salary,
            "employee_id": self.employee_id,
            "date_hired": self.date_hired,
            "active": self.active,
        }

        # Include deactivation date only if employee is inactive
        if not self.active:
            data["deactivated_date"] = self.deactivated_date

        return data

    @staticmethod
    def load_employees():
        """Load employees from JSON file. Create file if it does not exist."""
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)

        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_to_json(self):
        """Save the employee to the JSON file."""
        employees = self.load_employees()

        # Generate sequential ID if not provided
        if not self.employee_id:
            self.employee_id = str(generate_sequential_id(employees))

        employees.append(self.to_dict())

        with open(DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4, ensure_ascii=False)

    def deactivate(self):
        """Deactivate the employee and set deactivation date."""
        self.active = False
        self.deactivated_date = datetime.date.today().isoformat()

    @staticmethod
    def save_all(employees: list[dict]) -> None:
         with open(DATA_PATH, "w", encoding="utf-8") as f:
             json.dump(employees, f, indent=8, ensure_ascii=False)
