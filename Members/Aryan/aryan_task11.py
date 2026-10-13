
# Day 11: OOP - Inheritance and Method Overriding
# Name: Aryan
# What I learned today: Inheritance, super(), Method Overriding and __str__


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name} | Base Salary: ₹{self.salary}"

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
        tech = ", ".join(self.tech_stack)
        return f"{super().get_details()} | Tech Stack: {tech}"


# Creating objects
manager_instance = Manager("Rahul", 60000, "IT")
developer_instance = Developer(
    "Aryan",
    45000,
    ["Python", "FastAPI", "SQL"]
)


# Testing string representation
print("----- Manager Details -----")
print(manager_instance)

print("\n----- Developer Details -----")
print(developer_instance)


# Testing method overriding
print("\n----- Manager get_details() -----")
print(manager_instance.get_details())

print("\n----- Developer get_details() -----")
print(developer_instance.get_details())
