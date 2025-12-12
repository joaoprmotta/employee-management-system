# Employee Management System (Python)

A simple **Employee Management System** built with Python, focused on clean code, file persistence, and unit testing.  
This project was developed as a **learning and portfolio project** to practice backend fundamentals and good software engineering practices.

---

## Features

- Register new employees
- List all employees in a formatted table
- Edit employee salary (only if active)
- Deactivate employees with deactivation date tracking
- Generate summary reports:
  - Total employees
  - Active vs inactive employees
  - Total salary expense
- Persistent storage using JSON files
- Defensive programming to handle invalid or missing data
- Unit tests for core logic

---

## Project Structure

```
employee-management-system/
├── data/
│   └── employees.json
├── src/
│   ├── main.py
│   ├── employee.py
│   └── utils.py
├── tests/
│   ├── test_utils.py
│   └── test_employee.py
└── README.md
```

---

## How to Run

### Requirements
- Python 3.10 or higher

### Run the application

```bash
python src/main.py
```

You will see a menu like:

```
Employee Management System
1. Add Employee
2. List Employees
3. Edit Employee Salary
4. Deactivate Employee
5. Show Report
6. Exit
```

---

## Running Tests

This project uses Python’s built-in `unittest` module.

Run all tests with:

```bash
python -m unittest discover -s tests -v
```

Example output:

```
Ran 14 tests in 0.009s

OK
```

---

## Technologies and Concepts

- Python
- Object-Oriented Programming (OOP)
- JSON file persistence
- Command-line interface (CLI)
- Defensive programming
- Unit testing with `unittest`
- Clean project structure
- Separation of concerns

---

## Purpose of This Project

This project was created to:

- Practice backend fundamentals using Python
- Apply clean code principles
- Learn how to persist data without a database
- Write and run automated unit tests
- Serve as a portfolio project for **Junior Backend Developer** roles

---

## Future Improvements

- REST API version using FastAPI
- Database integration (SQLite or PostgreSQL)
- Authentication and authorization
- Docker support
- CI pipeline for automated testing

---

## Author

**João Pedro Motta da Rocha**  
Aspiring Backend Developer (Python)

---
