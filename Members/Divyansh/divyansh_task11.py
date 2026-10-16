class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary=salary

    def get_details(self):
        return f"""{self.name}|{self.salary}"""

    def __str__(self):
        return f"Employee:{self.name} | Base Salary:{self.salary}"

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def get_details(self):
        return f"""{self.name}|{self.salary}|{self.department}"""

class Developer(Employee):
    def __init__(self,name,salary,tech_stack):
        super().__init__(name,salary)
        self.tech_stack=tech_stack
    def get_details(self):
        return f"""{self.name}|{self.salary}|{self.tech_stack}"""
e1 =Employee("Mahesh",60000)
m1 = Manager("Ramesh", 50000, "HR")       
d1 = Developer("Suresh", 60000, ["Python", "FastAPI"]) 
print(e1)  
print(m1)
print(d1)
print(e1.get_details())
print(m1.get_details())
print(d1.get_details())