import os
import sys
import unittest

# Allow importing from src/ when running tests from project root
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.insert(0, SRC_DIR)

from utils import generate_sequential_id, format_address


class TestGenerateSequentialId(unittest.TestCase):
    def test_empty_list_starts_at_1(self):
        self.assertEqual(generate_sequential_id([]), 1)

    def test_simple_increment(self):
        employees = [{"employee_id": "1"}, {"employee_id": "2"}, {"employee_id": "3"}]
        self.assertEqual(generate_sequential_id(employees), 4)

    def test_ignores_invalid_ids(self):
        employees = [{"employee_id": "10"}, {"employee_id": "abc"}, {"employee_id": None}]
        self.assertEqual(generate_sequential_id(employees), 11)

    def test_missing_employee_id_key(self):
        employees = [{"name": "A"}, {"employee_id": "7"}, {"employee_id": "2"}]
        self.assertEqual(generate_sequential_id(employees), 8)

    def test_handles_numeric_and_string(self):
        employees = [{"employee_id": 5}, {"employee_id": "6"}]
        self.assertEqual(generate_sequential_id(employees), 7)


class TestFormatAddress(unittest.TestCase):
    def test_full_address(self):
        address = {"street": "Rua A", "city": "Rio de Janeiro", "state": "RJ", "zip": "26600000"}
        self.assertEqual(format_address(address), "Rua A, Rio de Janeiro - RJ, 26600000")

    def test_partial_address(self):
        address = {"city": "São Paulo", "state": "SP"}
        self.assertEqual(format_address(address), "São Paulo - SP")

    def test_missing_address_returns_na(self):
        self.assertEqual(format_address(None), "N/A")
        self.assertEqual(format_address({}), "N/A")

    def test_missing_zip(self):
        address = {"street": "Rua B", "city": "Curitiba", "state": "PR"}
        self.assertEqual(format_address(address), "Rua B, Curitiba - PR")


if __name__ == "__main__":
    unittest.main()
