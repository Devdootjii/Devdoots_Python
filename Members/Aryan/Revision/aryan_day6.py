
import json


# Problem 1 - Functions
def check_answer(user, correct):
    if user == correct:
        return True
    else:
        return False


print("Problem 1:")
print(check_answer("a", "a"))


# Problem 2 - Conditions
def rank(score):
    if score >= 8:
        return "Pro"
    elif score >= 5:
        return "Average"
    else:
        return "Beginner"


print("\nProblem 2:")
print(rank(9))
print(rank(6))
print(rank(3))


# Problem 3 - Loops
answers = ["a", "b", "c"]
correct_answers = ["a", "x", "c"]

correct_count = 0

for i in range(len(answers)):
    if answers[i] == correct_answers[i]:
        correct_count += 1

print("\nProblem 3:")
print("Correct answers:", correct_count)


# Problem 4 - Lists & Dicts
questions = [
    {"q": "2+2?", "ans": "4"},
    {"q": "3+3?", "ans": "6"},
    {"q": "5+5?", "ans": "10"}
]

print("\nProblem 4:")
for question in questions:
    print(question["q"])


# Problem 5 - Files & JSON
data = {"high score": 7}

with open("high.json", "w") as file:
    json.dump(data, file)

with open("high.json", "r") as file:
    loaded_data = json.load(file)

print("\nProblem 5:")
print(loaded_data)
