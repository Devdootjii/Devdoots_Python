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
    return total / len(nums)

students = [{"name": "Riya", "marks": [90]},{"name": "Aman", "marks": [65]}]
for student in students:
    name = student["name"]
    marks = student["marks"]
    print(f"\nStudent Name: {name}")

    for mark in marks:
        print(f"Grade: {grade(mark)}")

    print(f"Average: {average(marks):.2f}")
