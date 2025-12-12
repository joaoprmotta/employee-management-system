import os
import sys
import json
import unittest
import tempfile
from unittest.mock import patch

# Allow importing from src/ when running tests from project root
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.insert(0, SRC_DIR)

import employee as employee_module
from employee import Employee


def make_employee(**overrides):
    """Helper to quickly create Employee instances with sensible defaults."""
    data = {
        "name": "Joao",
        "age": 25,
        "email": "joao@email.com",
        "address": {"street": "Rua A", "city": "Rio", "state": "RJ", "zip": "26600000"},
        "position": "Operador",
        "department": "Fabrica",
        "salary": 3000.0,
        "employee_id": None,  # Let the system generate it
        "date_hired": "2025-01-10",
        "active": True,
        "deactivated_date": None,
    }
    data.update(overrides)
    return Employee(
        name=data["name"],
        age=data["age"],
        email=data["email"],
        address=data["address"],
        position=data["position"],
        department=data["department"],
        salary=data["salary"],
        employee_id=data["employee_id"],
        date_hired=data["date_hired"],
        active=data["active"],
        deactivated_date=data["deactivated_date"],
    )


class TestEmployeeFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an isolated temp directory and JSON path for each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_json_path = os.path.join(self.temp_dir.name, "employees.json")

        # Patch employee.DATA_PATH so Employee reads/writes to temp JSON
        self.data_path_patcher = patch.object(employee_module, "DATA_PATH", self.temp_json_path)
        self.data_path_patcher.start()

    def tearDown(self):
        self.data_path_patcher.stop()
        self.temp_dir.cleanup()

    def test_load_employees_creates_file_and_returns_list(self):
        # File does not exist initially
        self.assertFalse(os.path.exists(self.temp_json_path))

        employees = Employee.load_employees()

        # After load, file should exist and employees should be list
        self.assertTrue(os.path.exists(self.temp_json_path))
        self.assertIsInstance(employees, list)
        self.assertEqual(employees, [])

        # File content should be valid JSON list
        with open(self.temp_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_save_to_json_appends_employee(self):
        emp = make_employee(employee_id=None)
        emp.save_to_json()

        employees = Employee.load_employees()
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]["name"], "Joao")
        self.assertIn("employee_id", employees[0])
        self.assertIsNotNone(employees[0]["employee_id"])

    def test_save_to_json_generates_sequential_ids(self):
        emp1 = make_employee()
        emp1.save_to_json()

        emp2 = make_employee(name="Maria", email="maria@email.com")
        emp2.save_to_json()

        employees = Employee.load_employees()
        self.assertEqual(len(employees), 2)

        # IDs should be sequential: 1 then 2 (as strings)
        self.assertEqual(employees[0]["employee_id"], "1")
        self.assertEqual(employees[1]["employee_id"], "2")

    def test_save_to_json_keeps_provided_id_if_set(self):
        # If you decide your Employee.save_to_json should NOT overwrite provided IDs,
        # this test will validate that behavior.
        #
        # If your current implementation always overwrites employee_id,
        # you can remove this test or adapt the expected result.
        emp = make_employee(employee_id="99")
        emp.save_to_json()

        employees = Employee.load_employees()
        self.assertEqual(len(employees), 1)

        # EXPECTATION (recommended): keep the provided ID
        self.assertEqual(employees[0]["employee_id"], "99")

    def test_to_dict_includes_deactivated_date_only_when_inactive(self):
        emp = make_employee()
        d = emp.to_dict()
        self.assertTrue(d["active"])
        self.assertNotIn("deactivated_date", d)

        emp.deactivate()
        d2 = emp.to_dict()
        self.assertFalse(d2["active"])
        self.assertIn("deactivated_date", d2)
        self.assertTrue(d2["deactivated_date"])  # should not be empty


if __name__ == "__main__":
    unittest.main()
