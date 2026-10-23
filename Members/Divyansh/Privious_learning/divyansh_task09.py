import json

students = [{"Name":"Mohan",
             "Marks":{"Maths":90,"Sci":80},
             }]
with open("students.json","w") as f:
    json.dump(students,f,indent=4)

with open("students.json","r") as f:
    students=json.load(f)

for student in students:
    marks=student["Marks"]
    total=sum(marks.values())
    print(f"Total marks:{total}")
    count=len(marks)
    avg=total/count
    print(f"Average :{avg}")
new_student = {"Name":"Rohan",
             "Marks":{"Maths":70,"Sci":75}}
students.append(new_student)

with open("students.json","w") as f:
    json.dump(students,f,indent=4)