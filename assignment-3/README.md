# Assignment 3: Employee CRUD System (SQLite Database)

- **Author:** Pranjal Khadke
- **Roll No:** 10
- **Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)
- **GitHub:** [@PranjalKhadke](https://github.com/PranjalKhadke)
- **Course:** AIML Honors &bull; Semester III

Relational database CRUD management implementing primary key constraints, aggregate grouping queries, and transaction management using Python's standard `sqlite3` module.

### Features
- Complete CRUD operations: Add, List, Search by ID, Update (name/department/salary), Delete.
- Primary key enforcement and duplicate prevention (`IntegrityError`).
- Aggregate SQL query: department-wise staff count, average salary, and max salary.
- Parameterized SQL queries to prevent SQL injection.

### Schema
```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL CHECK(salary >= 0)
);
```

### Files
- `emp_sqlite.py`: SQLite connection helpers, CRUD functions, and CLI menu.
- `employee.db`: SQLite database file.
- `assignment3.ipynb`: Fully executed Jupyter notebook with test outputs and SQL queries.

### How to Run
```bash
python emp_sqlite.py
```
Or open `assignment3.ipynb` in VS Code or Jupyter Lab.
