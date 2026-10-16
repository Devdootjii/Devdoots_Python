#day 09 task
#name: Khushi
#what I learned :JSON, json fuctions, nested dictionary, total& average, read write append
#where i stuck : JSON or json function kaise kaam krta h usme

import json

#Create student data
data = [
    {
        "name": "ananya",
        "marks": {"DSA": 80, "cs": 90}
    },
    {
        "name": "priya",
        "marks": {"DSA": 70, "cs": 80}
    }
]

#Save data into students.json
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

#Read data from students.json
with open("students.json", "r") as f:
    students = json.load(f)

#total and average
for student in students:
    marks = student["marks"]
    total = sum(marks.values())
    avg = total / len(marks)

    print("\nName:", student["name"])
    print("Total Marks:", total)
    print("Average Marks:", avg)

#Add a new student
new_student = {
    "name": "Khushi",
    "marks": {"DSA": 90, "cs": 95}
}

students.append(new_student)

#Save updated data
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("\nNew student added successfully!")