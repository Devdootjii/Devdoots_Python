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
    {"name": "Suchi", "marks": [90,71]}
]

for student in students:
    name = student["name"]
    marks = student["marks"]
    print(f"Student: {name}")

for mark in marks:
    print(f"Marks: {mark}, Grade: {grade(mark)}")
    print(f"Average: {average(marks):.2f}")
                       
