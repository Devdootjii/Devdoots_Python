# Day 6: File Handling & Exception Control
# File: Members/Balram/balram_task06.py

LOG_FILE = "payroll_audit.txt"

# worker record append karna
def write_payroll_log(worker_name, final_salary):
    with open(LOG_FILE, "a") as file:
        file.write(f"Worker: {worker_name} | Net Salary: Rs {final_salary:.2f}\n")
    print(f"Record saved for {worker_name}")

# file read karna
def read_payroll_log():
    try:
        with open(LOG_FILE, "r") as file:
            content = file.read()
            if content.strip():
                print(content.strip())
            else:
                print("File khali hai.")
    except FileNotFoundError:
        print("Audit log file abhi exist nahi karti. Pehle audit record create karein.")

# input validation function
def get_valid_salary_input(prompt):
    while True:
        try:
            salary = float(input(prompt))
            if salary < 0:
                print("Salary negative nahi ho sakti.")
                continue
            return salary
        except ValueError:
            print("Invalid input! Kripya sirf numeric values enter karein.")

if __name__ == "__main__":
    # initial read test
    print("--- Initial Read Check ---")
    read_payroll_log()
    
    # 2 workers entry
    print("\n--- Worker Entries ---")
    for i in range(1, 3):
        name = input(f"Worker 0{i} Name: ").strip()
        salary = get_valid_salary_input(f"{name} ki Net Salary (Rs): ")
        write_payroll_log(name, salary)
    
    # updated audit logs
    print("\n--- Updated Audit Logs ---")
    read_payroll_log()