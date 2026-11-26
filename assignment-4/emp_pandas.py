import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "employee.csv")
COLUMNS = ["emp_id", "name", "department", "experience_yrs", "salary"]


def load_dataset(filepath=CSV_PATH):
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        for col in COLUMNS:
            if col not in df.columns:
                df[col] = None
        df = df[COLUMNS].copy()
        df["emp_id"] = pd.to_numeric(df["emp_id"], errors="coerce")
        df["experience_yrs"] = pd.to_numeric(df["experience_yrs"], errors="coerce")
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
        df = df.dropna(subset=["emp_id"])
        df["emp_id"] = df["emp_id"].astype(int)
        return df
    return pd.DataFrame(columns=COLUMNS)


def save_dataset(df, filepath=CSV_PATH):
    df.to_csv(filepath, index=False)


def add_employee(df, emp_id, name, department, experience, salary):
    emp_id = int(emp_id)
    if not df.empty and emp_id in df["emp_id"].values:
        print(f"Error: Employee with ID {emp_id} already exists.")
        return df

    new_record = pd.DataFrame([{
        "emp_id": emp_id,
        "name": str(name).strip(),
        "department": str(department).strip(),
        "experience_yrs": float(experience),
        "salary": float(salary),
    }])
    updated_df = pd.concat([df, new_record], ignore_index=True)
    save_dataset(updated_df)
    print(f"Added employee {name} (ID: {emp_id}).")
    return updated_df


def show_records(df):
    if df.empty:
        print("No employee records found.")
        return
    print("\n" + df.to_string(index=False) + "\n")


def search_employee(df, emp_id):
    emp_id = int(emp_id)
    match = df[df["emp_id"] == emp_id]
    if match.empty:
        print(f"Employee ID {emp_id} not found.")
        return None
    print("\n" + match.to_string(index=False) + "\n")
    return match


def filter_by_dept(df, department):
    subset = df[df["department"].astype(str).str.lower() == department.strip().lower()]
    if subset.empty:
        print(f"No records found for department '{department}'.")
        return subset
    print(f"\n--- Department: {department} ---")
    print(subset.to_string(index=False) + "\n")
    return subset


def update_employee(df, emp_id, name=None, department=None, experience=None, salary=None):
    emp_id = int(emp_id)
    idx = df.index[df["emp_id"] == emp_id].tolist()
    if not idx:
        print(f"Update failed: ID {emp_id} not found.")
        return df

    row_idx = idx[0]
    if name:
        df.at[row_idx, "name"] = str(name).strip()
    if department:
        df.at[row_idx, "department"] = str(department).strip()
    if experience is not None:
        df.at[row_idx, "experience_yrs"] = float(experience)
    if salary is not None:
        df.at[row_idx, "salary"] = float(salary)

    save_dataset(df)
    print(f"Employee ID {emp_id} updated.")
    return df


def delete_employee(df, emp_id):
    emp_id = int(emp_id)
    if emp_id not in df["emp_id"].values:
        print(f"Delete failed: ID {emp_id} not found.")
        return df

    updated_df = df[df["emp_id"] != emp_id].reset_index(drop=True)
    save_dataset(updated_df)
    print(f"Employee ID {emp_id} removed.")
    return updated_df


def compute_stats(df):
    if df.empty:
        print("No data available for statistics.")
        return

    print("\n--- Overall Salary Summary ---")
    calc_df = df.copy()
    calc_df["experience_yrs"] = pd.to_numeric(calc_df["experience_yrs"], errors="coerce")
    calc_df["salary"] = pd.to_numeric(calc_df["salary"], errors="coerce")
    desc = calc_df[["experience_yrs", "salary"]].describe().T
    avail_cols = [c for c in ["count", "mean", "min", "max"] if c in desc.columns]
    print(desc[avail_cols].to_string())

    print("\n--- Department Aggregation ---")
    dept_grp = calc_df.groupby("department").agg(
        headcount=("emp_id", "count"),
        avg_exp=("experience_yrs", "mean"),
        avg_salary=("salary", "mean"),
        total_payroll=("salary", "sum"),
    )
    print(dept_grp.to_string() + "\n")


def menu():
    df = load_dataset()
    while True:
        print("\n=== Employee Management (Pandas) ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search by ID")
        print("4. Filter by Department")
        print("5. Update Employee Details")
        print("6. Delete Employee")
        print("7. View Summary & Department Stats")
        print("8. Exit")

        ch = input("Enter choice (1-8): ").strip()
        if ch == "1":
            eid = input("Enter ID: ").strip()
            nm = input("Enter Name: ").strip()
            dp = input("Enter Department: ").strip()
            exp = input("Enter Experience (years): ").strip()
            sal = input("Enter Salary: ").strip()
            df = add_employee(df, eid, nm, dp, exp, sal)
        elif ch == "2":
            show_records(df)
        elif ch == "3":
            eid = input("Enter ID to search: ").strip()
            search_employee(df, eid)
        elif ch == "4":
            dp = input("Enter Department: ").strip()
            filter_by_dept(df, dp)
        elif ch == "5":
            eid = input("Enter ID to update: ").strip()
            print("Leave blank to keep existing value.")
            nm = input("New Name: ").strip()
            dp = input("New Dept: ").strip()
            exp = input("New Experience: ").strip()
            sal = input("New Salary: ").strip()
            df = update_employee(
                df,
                eid,
                name=nm if nm else None,
                department=dp if dp else None,
                experience=float(exp) if exp else None,
                salary=float(sal) if sal else None,
            )
        elif ch == "6":
            eid = input("Enter ID to delete: ").strip()
            df = delete_employee(df, eid)
        elif ch == "7":
            compute_stats(df)
        elif ch == "8":
            print("Exiting...")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    menu()
