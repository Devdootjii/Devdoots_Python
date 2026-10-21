#problem 1
def check_answer(user, correct):
    if user == correct:
        return True
    else:
        return False

print(check_answer("a", "a"))
print(check_answer("b", "a"))

#problem 2
def rank(score):
    if score >= 8:
        return "Pro"
    elif score >= 5:
        return "Average"
    else:
        return "Beginner"

print(rank(3))
print(rank(9))
print(rank(7))

#problem 3
answers = ["a", "b", "c"]
correct_answers = ["a", "x", "c"]
count = 0
for i in range(len(answers)):
    if answers[i] == correct_answers[i]:
        count += 1

print("Correct answers:", count)

#problem 4
questions = [
    {"q": "2+2?", "ans": "4"},
    {"q": "3+3?", "ans": "6"},
    {"q": "5+5?", "ans": "10"}
]

for question in questions:
    print(question["q"])

#problem 5
import json
score = {"high_score": 7}

with open("high.json", "w") as f:
    json.dump(score, f)

with open("high.json", "r") as f:
    data = json.load(f)

print(data)
