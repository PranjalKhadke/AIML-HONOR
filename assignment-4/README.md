# Assignment 4: Employee Data Management & Analysis (Pandas)

- **Author:** Pranjal Khadke
- **Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)
- **GitHub:** [@PranjalKhadke](https://github.com/PranjalKhadke)
- **Course:** AIML Honors &bull; Semester III

Data manipulation, exploratory summary, and CRUD operations implemented using the `pandas` library.

### Features
- Complete CRUD operations: Add record via `pd.concat`, view records, update using `.loc` indexing, and delete using boolean masking.
- Data filtering using combined boolean conditions (`&`, `|`).
- Summary statistics: `.describe()`, minimum, maximum, and average salary.
- Department-level aggregations (`.groupby('department')` for headcount, average experience, average salary, and total payroll).
- CSV persistence (`.to_csv()` and `.read_csv()`).

### Schema
`emp_id, name, department, experience_yrs, salary`

### Files
- `emp_pandas.py`: CLI menu and helper functions for DataFrame operations.
- `employee.csv`: CSV storage loaded and updated by Pandas.
- `assignment4.ipynb`: Fully executed Jupyter notebook with exploratory tables and metrics.

### How to Run
```bash
python emp_pandas.py
```
Or open `assignment4.ipynb` in VS Code or Jupyter Lab.
