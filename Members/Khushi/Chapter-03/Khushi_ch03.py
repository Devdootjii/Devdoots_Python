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
        total += n
    count = len(nums)
    return total / count

students = [
    {"name": "Suchi", "marks": {"cs": 20, "dsa": 60}},
    {"name": "Rahul", "marks": {"cs": 95, "dsa": 85}}
]

all_marks = []
for student in students:
    name = student["name"]
    marks = student["marks"]
    print(f"\nStudent Name: {name}")

    for subject, mark in marks.items():
        print(f"Subject: {subject}, Marks: {mark}, Grade: {grade(mark)}")
        all_marks.append(mark)

print(f"\nClass Average: {average(all_marks):.2f}")
