# Day 6: File Handling & Exception Handling
# Name: Harsh Rajbhar
# What I learned today: file handling (with open) aur try-except se error handling
# Where I got stuck & fixed it: missing file par crash ho raha tha, try-except se fix kiya

from datetime import datetime

#Function 1: Write payroll log (append mode)

def write_payroll_log(worker_name,final_salary):
    with open("payroll_audit.txt","a") as file:
        date=datetime.now().strftime("%Y-%M-%D %H:%M")
        file.write(f"{date} | {worker_name} | Rs{final_salary}\n")

# Function 2: Read payroll log (try-except FileNotFoundError) 

def read_payroll_log():
    try:
        with open("payrool_audit.txt","r") as file:
            print("\n---PAYROLL AUDIT HISTORY---")
            print(file.read())
    except FileNotFoundError:
        print("Audit log file abhi exist nahi karti ")
    finally:
        print("(Audit log check complete)")

def get_valid_salary_input():
    while True:
        try:
            salary=float(input("Enter Salary:"))
            return salary
        except ValueError:
            print("Invalid input! Kripya sirf numeric values enter karein.")

# --- Main Execution ---
print("========================================")
print("   FACTORY AUDIT LOG SYSTEM")
print("========================================")

# Step 1: read first (missing file ka exception test)
print("\n[Step 1] Reading existing audit log...")
read_payroll_log()

# Step 2: 2 workers ka input
for i in range(1, 3):
    print(f"\n--- Worker {i} ---")
    name = input("Enter Worker Name: ")
    salary = get_valid_salary_input()
    write_payroll_log(name, salary)

# Step 3: dobara read
print("\n[Step 3] Reading updated audit log...")
read_payroll_log()

print("\n========================================")
print("Audit Status: SUCCESSFUL")
