def get_valid_salary_input():
    try:
        salary=int(input("Enetr Your salary:"))
        return salary
    except ValueError:
        return f"Invalid Input! Please Enter Numbers Only!"

def write_payroll_log(worker_name,final_salary):
    with open("payroll_audit.txt","a") as f:
        f.write(f"{name}:{final_salary}\n")

def read_payroll_log():
    try:
        with open("payroll_audit.txt","r")as f:
            return f.read()
    except FileNotFoundError:
        return "Audit log File not Found!"
sal = get_valid_salary_input()
name = "Suresh"

# final_salary = sal

log = write_payroll_log(name,sal)
print(read_payroll_log())