# Day 6: File Handling & Exception Control
# Name: Ritesh
# What I learned today: Persistent file logging using with context manager, and graceful crash control using try-except-finally.
# Where I got stuck & fixed it: Handled initial FileNotFoundError on first read and prevented crashes on invalid string salaries.
#Function 1:File me worker ka record (Append Mode)

def write_payroll_log(worker_name, final_salary):
   with open("ritesh_payroll_audit.txt"), "a" as file:
       file.write(f"Worker : {worker_name} | Salary: Rs {final_salary}\n")
   print (f"Record saved for {worker_name}")

# Function 2: File se data padhna (Read Mode + Error Control)
def read_payroll_log():
    try:
        with open("ritesh_payroll_audit.txt" ,"r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Audit log file abhi exist nahi karti . pehele audit record create kare.")

# Function 3: User se sahi numeric salary lena (ValueError Control) 
def get_vaild_salary_input(worker_name):
    while true:
        try:
            salary = float(input(f"Enter salary for {worker_name}:"))    
            return salary
        except ValueError:
            print("invalid input ! plz enter only numeric value.")
 #   main execution ( PDF flow ke mutabik)
 # Step 1 File na hone par error handle hogi
print("Step 1: Reading file (Initial Check)..")
read_payroll_log()

# Step 2 & 3: 2 Workers ka data lena aur file me save karna
print("\nStep 2 & 3: Enter Worker Details....")
name1 = input("Enter Worker 1 Name: ")
sal1 = get_valid_salary_input(name1)
write_payroll_log(name1, sal1)

name2 = input("Enter Worker 2 Name: ")
sal2 = get_valid_salary_input(name2)
write_payroll_log(name2, sal2)

# Step 4: Dubara file read karke terminal par saved record dikhaana
print("\nStep 4: Reading Saved Records from File...")
read_payroll_log()
