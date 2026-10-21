def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=70:
        return "B"
    else:
        return "C"

def average(nums):
    total=0
    for n in nums:
        total=total+n
        return total/len(nums)

students = [
    {"name": "Harsh", "marks": 95},
    {"name": "Aryan", "marks": 70},
]

marks_list = []
for s in students:
    print(s["name"], grade(s["marks"]))
    marks_list.append(s["marks"])

print("Class average:", average(marks_list))
