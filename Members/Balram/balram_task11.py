# Base class definition
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ₹{self.salary}"

    def __str__(self):
        return f"Employee: {self.name} | Base Salary: ₹{self.salary}"


# Manager child class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: ₹{self.salary}, Department: {self.department}"


# Developer child class
class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def get_details(self):
        skills = ", ".join(self.tech_stack)
        return f"Developer: {self.name}, Salary: ₹{self.salary}, Tech Stack: [{skills}]"


# --- Proof of Work (PoW) Test Block ---
if __name__ == "__main__":
    # Objects instantiate karna
    mgr = Manager("Balram Singh", 75000, "Content & Engineering")
    dev = Developer("Aryan", 55000, ["Python", "FastAPI", "PostgreSQL"])

    # Dunder __str__ check
    print(mgr)
    print(dev)

    # Method overriding check
    print(mgr.get_details())
    print(dev.get_details())