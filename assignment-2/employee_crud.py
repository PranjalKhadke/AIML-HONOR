import csv
import os

CSV_FILE = "employee.csv"
HEADERS = ["emp_id", "name", "dept", "salary"]


def init_file(filepath=CSV_FILE):
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
    print(f"[SYSTEM] Initialized secure CSV repository at '{filepath}'.")


def get_all_rows(filepath=CSV_FILE):
    if not os.path.exists(filepath):
        return []
    with open(filepath, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    return rows


def add_employee(emp_id, name, dept, salary, filepath=CSV_FILE):
    if not os.path.exists(filepath):
        init_file(filepath)

    rows = get_all_rows(filepath)
    for r in rows[1:]:
        if r and r[0] == str(emp_id):
            print(f"  [ERROR] Primary Key Collision: Employee ID {emp_id} already exists.")
            return False

    try:
        sal_val = float(salary)
        if sal_val < 0:
            print("  [ERROR] Salary value cannot be negative.")
            return False
    except ValueError:
        print("  [ERROR] Salary must be a valid numeric quantity.")
        return False

    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([str(emp_id), str(name).strip(), str(dept).strip(), f"{sal_val:.2f}"])

    print(f"  [SUCCESS] Enrolled employee: {name} (ID: {emp_id}, Dept: {dept}, Salary: Rs. {sal_val:,.2f})")
    return True


def list_employees(filepath=CSV_FILE):
    rows = get_all_rows(filepath)
    if len(rows) <= 1:
        print("\n  [INFO] Employee repository is currently empty.\n")
        return

    print("\n+--------+----------------------+------------------+----------------+")
    print("| Emp ID | Employee Name        | Department       | Salary (INR)   |")
    print("+--------+----------------------+------------------+----------------+")
    for r in rows[1:]:
        if len(r) >= 4:
            sal_str = f"{float(r[3]):,.2f}" if r[3].replace(".", "", 1).isdigit() else r[3]
            print(f"| {r[0]:<6} | {r[1]:<20} | {r[2]:<16} | Rs. {sal_str:>10} |")
    print("+--------+----------------------+------------------+----------------+\n")


def find_employee(emp_id, filepath=CSV_FILE):
    rows = get_all_rows(filepath)
    for r in rows[1:]:
        if r and r[0] == str(emp_id):
            sal_formatted = f"{float(r[3]):,.2f}" if r[3].replace(".", "", 1).isdigit() else r[3]
            print(f"  [MATCH] ID: {r[0]} | Name: {r[1]} | Department: {r[2]} | Salary: Rs. {sal_formatted}")
            return r
    print(f"  [NOT FOUND] No employee matches ID: {emp_id}.")
    return None


def update_employee(emp_id, new_name=None, new_dept=None, new_salary=None, filepath=CSV_FILE):
    rows = get_all_rows(filepath)
    if len(rows) <= 1:
        print("  [ERROR] Database empty. No records available to modify.")
        return False

    updated = False
    for r in rows[1:]:
        if r and r[0] == str(emp_id):
            if new_name is not None and new_name.strip():
                r[1] = new_name.strip()
            if new_dept is not None and new_dept.strip():
                r[2] = new_dept.strip()
            if new_salary is not None:
                r[3] = f"{float(new_salary):.2f}"
            updated = True
            break

    if updated:
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"  [SUCCESS] Successfully modified record for Employee ID {emp_id}.")
        return True
    else:
        print(f"  [NOT FOUND] Unable to update: Employee ID {emp_id} does not exist.")
        return False


def remove_employee(emp_id, filepath=CSV_FILE):
    rows = get_all_rows(filepath)
    if len(rows) <= 1:
        print("  [ERROR] No records to delete.")
        return False

    header = rows[0]
    records = rows[1:]
    new_records = [r for r in records if r and r[0] != str(emp_id)]

    if len(new_records) == len(records):
        print(f"  [NOT FOUND] Unable to delete: Employee ID {emp_id} does not exist.")
        return False

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_records)

    print(f"  [SUCCESS] Successfully expunged Employee ID {emp_id} from database.")
    return True


def menu():
    while True:
        print("=" * 56)
        print("         EMPLOYEE INFORMATION MANAGEMENT SYSTEM (CSV)    ")
        print("=" * 56)
        print("  1. Initialize / Reset Database File")
        print("  2. Add New Employee Record")
        print("  3. View Full Employee Roster")
        print("  4. Search Record by Employee ID")
        print("  5. Update Employee Information")
        print("  6. Delete Employee Record")
        print("  7. Exit System")
        print("-" * 56)

        ch = input("Enter choice (1-7): ").strip()
        if ch == "1":
            init_file()
        elif ch == "2":
            eid = input("Enter Employee ID : ").strip()
            name = input("Enter Full Name   : ").strip()
            dept = input("Enter Department  : ").strip()
            sal = input("Enter Base Salary : ").strip()
            add_employee(eid, name, dept, sal)
        elif ch == "3":
            list_employees()
        elif ch == "4":
            eid = input("Enter Target ID   : ").strip()
            find_employee(eid)
        elif ch == "5":
            eid = input("Enter Employee ID to update: ").strip()
            print("  (Press Enter to leave field unchanged)")
            nm = input("  New Name   : ").strip()
            dp = input("  New Dept   : ").strip()
            sl = input("  New Salary : ").strip()
            update_employee(eid, nm if nm else None, dp if dp else None, float(sl) if sl else None)
        elif ch == "6":
            eid = input("Enter Employee ID to delete: ").strip()
            remove_employee(eid)
        elif ch == "7":
            print("Shutting down CSV database console.")
            break
        else:
            print("Invalid command. Please choose between 1 and 7.")


if __name__ == "__main__":
    menu()
