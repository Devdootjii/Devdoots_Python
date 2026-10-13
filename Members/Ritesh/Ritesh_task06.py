# Day 6: File Handling & Exception Control
# Name: Ritesh
# What I learned today: Persistent file logging using with context manager, and graceful crash control using try-except-finally.
# Where I got stuck & fixed it: Handled initial FileNotFoundError on first read and prevented crashes on invalid string salaries.
from datetime import datetime
LOG_FILE = "h4x_payroll_audit.txt" 
#function 1: Write worker record (append mode)
def write_payroll_log(worker_name , final_salary):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Worker: {worker_name}, | Net Salary: ${final_salary:.2f}\n"
    with open(LOG_FILE, "a" , encoding="utf-8") as file:
        file.write(log_entry)
    print(f"Log written successfully for {worker_name}.")

# Function 2: Read Worker Records (Read Mode + FileNotFoundError Handling)
def read_payroll_log():
    print("\n--- READING AUDIT LOG ---")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content.strip() == "":
                print("Audit log is empty.")
            else:
                print(content.strip())
    except FileNotFoundError:
        print("Audit log file not exist. please create audit record.")

    finally:
        print("--- AUDIT LOG READ OPERATION COMPLETED ---\n")

# Function 3: Input Validation for Salary (ValueError Handling)
def get_valid_salary_input(worker_name):
    while True:
        try: 
            salary = float(input(f"Enter net salary for {worker_name}: "))
            if salary <= 0:
                print("Invalid input! Salary must be greater than 0 . ")
                continue
            return salary
        except ValueError:
            print("Invalid input! Please enter a valid numeric salary.")

#  MAIN execution flow 
print("========================================")
print("     FACTORY AUDIT LOG SYSTEM   ")
print("========================================")               
# Step 1: Initial Read Test (Triggers FileNotFoundError if file is absent)
read_payroll_log()

# Step 2 & 3: Input and Write for 2 Workers
for i in range(1,3):
    worker_name = input(f"Enter worker{i} name:").strip()
    while not worker_name:
        print("Worker name cannot be empty. Please enter a valid name.")
        worker_name = input(f"Enter worker{i} name:").strip()
    salary = get_valid_salary_input(worker_name)
    write_payroll_log(worker_name, salary)

# Step 4: Final Read to display saved records from disk
print("\nStep 4: Reading Updated Audit Log from Disk...")
read_payroll_log()

print("========================================")
print("Audit Status: SUCCESSFUL")
print("========================================")
