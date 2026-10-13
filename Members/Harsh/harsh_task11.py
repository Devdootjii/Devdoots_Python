# Day 11: OOP Inheritance & Method Overriding
# Name: Harsh Rajbhar
# What I learned today: inheritance, super(), method overriding, aur __str__
# Where I got stuck & fixed it: super() se parent ka __init__ call karna

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name} | Salary: ₹{self.salary}"

    def __str__(self):
        return f"Employee: {self.name} | Base Salary: ₹{self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()} | Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def get_details(self):
        return f"{super().get_details()} | Tech Stack: {', '.join(self.tech_stack)}"

# Test harness
manager = Manager("Harsh", 60000, "IT")
developer = Developer("Amit", 45000, ["Python", "FastAPI"])

print(manager)
print(developer)

print(manager.get_details())
print(developer.get_details())
