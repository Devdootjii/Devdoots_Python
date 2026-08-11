#task 3
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def get_average_marks(self):
        total_no=sum(self.marks.values())
        return f"{total_no}"
    def display_details(self):
        avg=sum(self.marks.values())/len(self.marks)
        return f"I am {self.name}. My roll Number is {self.roll_no}. My marks avrage is {avg}."

student1=Student("Rohan",1,{"python":20,"maths":55})
print(student1.get_average_marks())
print(student1.display_details())