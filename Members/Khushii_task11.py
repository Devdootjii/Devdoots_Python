#day 11 task
#name : Khushi
#what i learne today: inheritance, parent class or child class, super(), method overriding, __str__
#where i got stuck: parent class samjhne me, super ka use method overriding samjhne me bhi 

#employee parent class
class Employee:
        return f"Employee: {self.name} | Base Salary: ₹{self.salary}"

# manager child class

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Employee: {self.name} | Base Salary: ₹{self.salary} | Department: {self.department}"

#developer child class
class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def get_details(self):
        skills = ", ".join(self.tech_stack)
        return f"Employee: {self.name} | Base Salary: ₹{self.salary} | Tech Stack: {skills}"

#object
manager = Manager("Khushi", 30000, "Cloud")
developer = Developer("devu", 40000, ["Python", "FastAPI"])

print(manager)
print(manager.get_details())

print(developer)
print(developer.get_details())
