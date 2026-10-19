def grade(marks):
    if marks > 90:
        return "A"
    elif marks >70:
        return "B"
    else:
        return "C"

def average(marks):
    total=0
    for n in marks :
        total = total + n
    total = total/len(marks)
    return total

student = [{"Name":"MohanLal","Marks":90},{"Name":"Rohani","Marks":65}]
for s in student:
    print(f"Name: {s["Name"]},Grade: {grade(s["Marks"])}")
avg=[]
for m in student:
    avg.append(m["Marks"])
avreg=sum(avg)/len(avg)
print(f"Class Average:{avreg}")