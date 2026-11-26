# AIML Honors &bull; Lab Portfolio & Class Practicals

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243.svg)](https://numpy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg)](https://www.sqlite.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Curated Academic Portfolio for Artificial Intelligence & Machine Learning Honors**  
Semester III &bull; Department of Computer Science & Engineering  

**Student Name:** [Pranjal Khadke](https://github.com/PranjalKhadke) &nbsp;|&nbsp; 
**Roll No:** 05 &nbsp;|&nbsp; 
**Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)

</div>

---

## Repository Index

This repository contains all five laboratory assignments as well as the class practical notebooks for the **AIML Honors** course.

### Class Practical Notebooks (AIML 05)
| Notebook | Topic | Description |
| :--- | :--- | :--- |
| **[`AIML 05 Class.ipynb`](./AIML%2005%20Class.ipynb)** | Pandas Practical Lab (Part 1) | DataFrames, custom exceptions (`PandasException`), reshaping (`melt`, `pivot_table`), merging, and aggregations |
| **[`AIML 05 Class 2.ipynb`](./AIML%2005%20Class%202.ipynb)** | NumPy Practical Lab (Part 2) | Array creation (`ones`, `zeros`), shape inspection, and in-place tensor operations |

---

### Graded Academic Assignments (1 to 5)

| Directory | Title | Core Concepts | Key Modules |
| :--- | :--- | :--- | :--- |
| **[`assignment -1/`](./assignment%20-1)** | Multi-Gateway Payment Processing Engine | Factory Pattern, Polymorphism, Data Abstraction | `abc`, `random` |
| **[`assignment-2/`](./assignment-2)** | Employee Record Management (CSV) | Flat-file I/O, CRUD Operations, PK Enforcement | `csv`, `os` |
| **[`assignment-3/`](./assignment-3)** | Relational Database Management (SQLite) | ACID Transactions, Parameterized SQL, DDL/DML, GROUP BY | `sqlite3` |
| **[`assignment-4/`](./assignment-4)** | Workforce Data Analytics (Pandas) | Vectorization, Boolean Masking, Descriptive Statistics, GroupBy | `pandas` |
| **[`assignment-5/`](./assignment-5)** | Python Function Decorators | First-Class Functions, Lexical Closures, Benchmarking, Stacking | `functools`, `time` |

---

## Assignment Summaries

### 1. [Assignment 1: Multi-Gateway Payment Engine](./assignment%20-1)
- **Objective:** Design an extensible transaction authorization and billing simulator.
- **Features:** 
  - Gateways: Razorpay (2.0% fee), Stripe (2.9% fee), Paytm (1.8% fee).
  - Modes: Debit/Credit Card (16-digit validation & masking), UPI (VPA format check), NetBanking (bank switch simulation).
  - Factory Method (`get_gateway()`) dynamically instantiating concrete gateways from string keys.
- **Run:** `python "assignment -1/main.py"`

### 2. [Assignment 2: Employee CRUD with CSV](./assignment-2)
- **Objective:** Implement flat-file persistence and record management without external databases.
- **Features:**
  - Full CRUD operations with primary key uniqueness enforcement.
  - Aligned ASCII tabular reports for terminal and notebook outputs.
  - Atomic read-modify-write file transactions.
- **Run:** `python assignment-2/employee_crud.py`

### 3. [Assignment 3: Employee CRUD with SQLite](./assignment-3)
- **Objective:** Model an enterprise employee database using Python's native SQLite engine.
- **Features:**
  - Table declaration with `INTEGER PRIMARY KEY` and `CHECK(salary >= 0)`.
  - Python context manager (`with sqlite3.connect(...) as conn:`) ensuring transaction rollbacks on failure.
  - Parameterized bindings preventing SQL injection.
  - Multi-attribute aggregations (`SELECT department, COUNT(*), AVG(salary), MAX(salary) ... GROUP BY department`).
- **Run:** `python assignment-3/emp_sqlite.py`

### 4. [Assignment 4: Workforce Analytics with Pandas](./assignment-4)
- **Objective:** Perform high-performance workforce analysis and data transformations.
- **Features:**
  - SIMD-accelerated boolean masking for multi-condition queries.
  - Split-Apply-Combine aggregations (`.groupby('department').agg(...)`).
  - Label-based cell modification via `.loc` indexer.
  - Roundtrip CSV serialization and verification.
- **Run:** `python assignment-4/emp_pandas.py`

### 5. [Assignment 5: Python Function Decorators](./assignment-5)
- **Objective:** Implement metaprogramming utilities for non-invasive function enhancement.
- **Features:**
  - `@time_execution`: Microsecond-precision benchmarking using hardware clock `time.perf_counter()`.
  - `@log_calls(tag=...)`: Introspection logging for function arguments (`*args`, `**kwargs`) and returns.
  - `@validate_positive`: Input validation guard raising `ValueError` on non-positive numerical values.
  - Multi-tier decorator chaining (`@validate_positive` + `@log_calls` + `@time_execution`).
- **Run:** `python assignment-5/decorators.py`

---

## Author Credentials

- **Student Name:** Pranjal Khadke
- **Roll No:** 05
- **Branch / Course:** AIML Honors &bull; Semester III
- **Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)
- **GitHub:** [@PranjalKhadke](https://github.com/PranjalKhadke)
