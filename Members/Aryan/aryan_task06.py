# Day 6: File Handling & Exception Control
# Name: Aryan
# What I learned today: File handling and exception handling


from datetime import datetime


def write_payroll_log(worker_name, final_salary):
    with open("payroll_audit.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | {worker_name} | {final_salary}\n")


def read_payroll_log():
    try:
        with open("payroll_audit.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Audit log file abhi exist nahi karti. Pehle audit record create karein.")

    finally:
        print("Audit log read operation completed.")


def get_valid_salary_input():
    while True:
        try:
            salary = int(input("Enter Your Salary: "))
            return salary

        except ValueError:
            print("Invalid input. Kripya sirf numeric values enter karein.")


read_payroll_log()


worker1_name = input("Enter Worker 1 Name: ")
worker1_salary = get_valid_salary_input()
write_payroll_log(worker1_name, worker1_salary)


worker2_name = input("Enter Worker 2 Name: ")
worker2_salary = get_valid_salary_input()
write_payroll_log(worker2_name, worker2_salary)


read_payroll_log()