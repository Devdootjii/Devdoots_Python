
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"

def average(nums):
    total = 0
    for n in nums:
        total = total + n          
    return total / len(nums)  

students = [
    {"name": "Harsh", "marks": 95},
    {"name": "Aryan", "marks": 70},
    {"name": "Rahul", "marks": 60},
]

marks_list = []

for student in students:
    print(student["name"], grade(student["marks"]))
    marks_list.append(student["marks"])  

print("Class Average:", average(marks_list))
