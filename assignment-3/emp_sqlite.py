import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "employee.db")


def get_connection(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL CHECK(salary >= 0)
            )
        """)
    return conn


def init_db(db_name=DB_NAME):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL CHECK(salary >= 0)
            )
        """)
    print(f"[SQLITE ENGINE] Connected to '{db_name}'. Verified schema for table 'employees'.")


def add_employee(emp_id, name, dept, salary, db_name=DB_NAME):
    try:
        with get_connection(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (emp_id, name, department, salary) VALUES (?, ?, ?, ?)",
                (int(emp_id), str(name).strip(), str(dept).strip(), float(salary))
            )
        print(f"  [SUCCESS] Inserted record: {name} (ID: {emp_id}, Dept: {dept}, Salary: Rs. {float(salary):,.2f})")
        return True
    except sqlite3.IntegrityError:
        print(f"  [INTEGRITY ERROR] Unique constraint violated: Employee ID {emp_id} already exists.")
        return False
    except ValueError as e:
        print(f"  [DATA ERROR] Type validation error: {e}")
        return False


def get_all_employees(db_name=DB_NAME):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, name, department, salary FROM employees ORDER BY emp_id ASC")
        rows = cursor.fetchall()

    if not rows:
        print("\n  [INFO] Database table 'employees' contains 0 records.\n")
        return []

    print("\n+--------+----------------------+------------------+----------------+")
    print("| Emp ID | Employee Name        | Department       | Salary (INR)   |")
    print("+--------+----------------------+------------------+----------------+")
    for r in rows:
        print(f"| {r[0]:<6} | {r[1]:<20} | {r[2]:<16} | Rs. {r[3]:>10,.2f} |")
    print("+--------+----------------------+------------------+----------------+\n")
    return rows


def get_employee_by_id(emp_id, db_name=DB_NAME):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id, name, department, salary FROM employees WHERE emp_id = ?", (int(emp_id),))
        row = cursor.fetchone()

    if row:
        print(f"  [RECORD] ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: Rs. {row[3]:,.2f}")
        return row
    else:
        print(f"  [NOT FOUND] No record matches Employee ID: {emp_id}.")
        return None


def update_employee(emp_id, name=None, dept=None, salary=None, db_name=DB_NAME):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, department, salary FROM employees WHERE emp_id = ?", (int(emp_id),))
        current = cursor.fetchone()

        if not current:
            print(f"  [NOT FOUND] Unable to update: Employee ID {emp_id} not found in database.")
            return False

        updated_name = str(name).strip() if name else current[0]
        updated_dept = str(dept).strip() if dept else current[1]
        updated_sal = float(salary) if salary is not None else current[2]

        cursor.execute(
            "UPDATE employees SET name = ?, department = ?, salary = ? WHERE emp_id = ?",
            (updated_name, updated_dept, updated_sal, int(emp_id))
        )
    print(f"  [SUCCESS] Updated Employee ID {emp_id} -> Name: {updated_name}, Dept: {updated_dept}, Salary: Rs. {updated_sal:,.2f}")
    return True


def delete_employee(emp_id, db_name=DB_NAME):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE emp_id = ?", (int(emp_id),))
        deleted = cursor.rowcount > 0

    if deleted:
        print(f"  [SUCCESS] Deleted Employee ID {emp_id} from SQLite database.")
        return True
    else:
        print(f"  [NOT FOUND] Unable to delete: Employee ID {emp_id} does not exist.")
        return False


def get_department_stats(db_name=DB_NAME):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT department, COUNT(*), AVG(salary), MAX(salary)
            FROM employees
            GROUP BY department
            ORDER BY department ASC
        """)
        stats = cursor.fetchall()

    if not stats:
        print("\n  [INFO] No records available for department statistics.\n")
        return []

    print("\n+------------------+-------------+----------------+----------------+")
    print("| Department       | Staff Count | Average Salary | Maximum Salary |")
    print("+------------------+-------------+----------------+----------------+")
    for s in stats:
        print(f"| {s[0]:<16} | {s[1]:<11} | Rs. {s[2]:>10,.2f} | Rs. {s[3]:>10,.2f} |")
    print("+------------------+-------------+----------------+----------------+\n")
    return stats


def menu():
    init_db()
    while True:
        print("=" * 56)
        print("          SQLITE RELATIONAL EMPLOYEE SYSTEM              ")
        print("=" * 56)
        print("  1. Add Employee Record")
        print("  2. Display All Employee Records")
        print("  3. Query by Employee ID")
        print("  4. Update Employee Details")
        print("  5. Delete Employee Record")
        print("  6. View Department Salary Statistics")
        print("  7. Exit")
        print("-" * 56)

        ch = input("Enter choice (1-7): ").strip()
        if ch == "1":
            eid = input("Enter Employee ID : ").strip()
            nm = input("Enter Full Name   : ").strip()
            dp = input("Enter Department  : ").strip()
            sl = input("Enter Salary      : ").strip()
            add_employee(eid, nm, dp, sl)
        elif ch == "2":
            get_all_employees()
        elif ch == "3":
            eid = input("Enter Target ID   : ").strip()
            get_employee_by_id(eid)
        elif ch == "4":
            eid = input("Enter Employee ID to update: ").strip()
            print("  (Leave blank to keep existing value)")
            nm = input("  New Name   : ").strip()
            dp = input("  New Dept   : ").strip()
            sl = input("  New Salary : ").strip()
            update_employee(eid, nm if nm else None, dp if dp else None, float(sl) if sl else None)
        elif ch == "5":
            eid = input("Enter Employee ID to delete: ").strip()
            delete_employee(eid)
        elif ch == "6":
            get_department_stats()
        elif ch == "7":
            print("Exiting SQLite management console.")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    menu()
