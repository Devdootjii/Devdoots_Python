#Day06 task completed : python presistant storage & fault tolerance engine
#Name = Khushi
#what i learned : file handling(read, write, apppend mode, context manager) + excrpption handling(try,except,finally block )
#where i got stuck & fixed it: context manager(with statement) + try except concept samjhne me problem hui basically error part bas

def write_payroll_log(name, salary):
    with open("payroll_audit.txt", "a") as f:
        f.write(f"Worker: {name} | Salary: {salary}\n")


def read_payroll_log():
    try:
        with open("payroll_audit.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Audit log file abhi exist nahi karti.")


def get_valid_salary_input():
    while True:
        try:
            return float(input("Salary: "))
        except ValueError:
            print("Invalid input! Sirf numeric value enter karein.")


read_payroll_log()

for i in range(2):
    name = input(f"\nWorker {i + 1} Name: ")
    salary = get_valid_salary_input()
    write_payroll_log(name, salary)

print("\n--- Audit History ---")
read_payroll_log()
