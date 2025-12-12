# Employee Management System (Python)

A simple **Employee Management System** built with Python, focused on clean code, file persistence, and unit testing.
This project was developed as a **learning and portfolio project** to practice backend fundamentals and good software engineering practices.

---

## 📌 Features

- Register new employees
- List all employees in a formatted table
- Edit employee salary (only if active)
- Deactivate employees with deactivation date tracking
- Generate summary reports:
  - Total employees
  - Active vs inactive employees
  - Total salary expense
- Persistent storage using JSON files
- Defensive programming (handles missing or invalid data)
- Full unit test coverage for core logic

---

## 🗂️ Project Structure

employee-management-system/
├── data/
│ └── employees.json # Persistent employee data
├── src/
│ ├── main.py # Application entry point (CLI)
│ ├── employee.py # Employee model and file persistence
│ └── utils.py # Utility functions (IDs, address formatting)
├── tests/
│ ├── test_utils.py # Unit tests for utility functions
│ └── test_employee.py # Unit tests for Employee logic
└── README.md

---

## 🚀 How to Run

### Requirements
- Python **3.10+**

### Run the application
```bash
python src/main.py

You will see a menu like:

Employee Management System
1. Add Employee
2. List Employees
3. Edit Employee Salary
4. Deactivate Employee
5. Show Report
6. Exit

---

## 🧪 Running Tests

This project uses Python’s built-in unittest module.

### Run all tests with:

python -m unittest discover -s tests -v

### Example output:

Ran 14 tests in 0.009s

OK

---

## 🛠️ Technologies & Concepts

Python

File persistence with JSON

CLI-based application

Object-Oriented Programming (OOP)

Defensive programming

Unit testing with unittest

Clean project structure

Separation of concerns

---

## 🎯 Purpose of This Project

This project was created to:

Practice backend fundamentals with Python

Demonstrate clean code and structure

Apply unit testing in a real project

Serve as a portfolio project for Junior Backend Developer roles

---

🔮 Possible Improvements (Future Work)

REST API version using FastAPI

Database persistence (SQLite / PostgreSQL)

Authentication and authorization

Docker support

CI pipeline for automated testing

---

👤 Author

João Pedro Motta da Rocha
Aspiring Backend Developer (Python)

---

⭐ If you found this project useful, feel free to star the repository!