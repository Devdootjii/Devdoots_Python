class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_average_marks(self):
        
        total_marks = sum(self.marks.values())
        total_subjects = len(self.marks)
        
        average = total_marks / total_subjects
        return average

    def display_details(self):
        avg = self.get_average_marks()
        print("Student details")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Average Marks: {avg:.2f}")


#Testing 
# Student Object Creation
student1 = Student("Khushi", 25, {"COA": 90, "DSTL": 80})

student1.display_details()