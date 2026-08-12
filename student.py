#task 3
class Student :
    def __init__(self,name ,roll_no, marks):
        self.name= name
        self.roll_no = roll_no
        self.marks = marks
    def get_average_marks(self):
        total_marks = sum(self.marks.values())
        total_subject = len(self.marks)
        return total_marks / total_subjects
    def display_details(self):
        avg = self.get_average_marks()
        print(f"Student : {self.name} | Roll No: {self.roll_no} | Avarage Marks : {avg:.2f}")
