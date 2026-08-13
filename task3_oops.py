# studnt class
class Student:
    def __init__(self, nam, roll, mrks):
        self.nam = nam
        self.roll = roll
        self.mrks = mrks # dict of marks
        
    def get_avg(self):
        tot = 0
        cnt = 0
        
        for s, m in self.mrks.items():
            tot = tot + m
            cnt = cnt + 1
            
        return tot / cnt
        
    def show_dtails(self):
        avg = self.get_avg()
        print(f"Name: {self.nam}, Roll: {self.roll}, Avg: {avg}")

# test
s1 = Student("Ritesh", 101, {"Python": 85, "Maths": 90})
s2 = Student("Harsh Rajbhar", 102, {"Python": 78, "Maths": 88})
s3 = Student("Amitesh", 103, {"Python": 92, "Maths": 85})

s1.show_dtails()
s2.show_dtails()
s3.show_dtails()