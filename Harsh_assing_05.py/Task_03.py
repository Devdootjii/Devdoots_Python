class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_average_marks(self):
        total = 0
        for mark in self.marks.values():
            total = total + mark
        average = total / len(self.marks)
        return average
    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Average Marks:", self.get_average_marks())
student1 = Student("Harsh", 22, {"Python": 85, "Maths": 90})
student1.display_details()
