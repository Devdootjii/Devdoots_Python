def grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"
def average(nums):
    total = 0 
    count = 0
    for num in nums:
        total =+num
        count =+1
    return total/count
students ={"name":"Aryan","marks":95},{"name":"Yash","marks":75},{"name":"Vinay","marks":60}
for student in students:
    name = student["name"]
    marks = student["marks"]

    result = grade(marks)
    print(name, result)
marks_list = []

for student in students:
    marks_list.append(student["marks"])

class_average = average(marks_list)

print("Class Average:", class_average)
