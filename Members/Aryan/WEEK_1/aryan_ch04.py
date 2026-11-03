def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"


def average(nums):
    total = 0

    for num in nums:
        total = total + num

    return total / len(nums)


students = [
    {"name": "Riya", "marks": 90},
    {"name": "Aman", "marks": 65}
]

marks_list = []

for s in students:
    name = s["name"]
    marks = s["marks"]

    result = grade(marks)
    print(name, result)

    marks_list.append(marks)

class_average = average(marks_list)
print("Class Average:", class_average)