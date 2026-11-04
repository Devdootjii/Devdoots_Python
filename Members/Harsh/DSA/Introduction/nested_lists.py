if __name__ == '__main__':
    
    students = []
    scores = set()
for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        students.append([name, score])

scores = list(sorted(scores))
students = sorted(students)

for student in students:
        if student[1] == scores[1]:
                print(student[0])
    