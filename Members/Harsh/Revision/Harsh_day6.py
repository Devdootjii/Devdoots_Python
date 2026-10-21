#program:1

def rank(score):
    if score >=9:
        return "Pro"
    elif 7>=score>=5:
        return "Average"
    else:
        return "Beginner"

print(rank(10))
print(rank(6))
print(rank(4))


# program:2

def check_answer(user, correct):
    if user == correct:
        return True
    else:
        return False

print(check_answer("a", "a"))   
print(check_answer("a", "b"))

# Program:3

answers = ["a", "b", "c"]
correct_answers = ["a", "x", "c"]

count = 0
for i in range(len(answers)):
    if answers[i] == correct_answers[i]:
        count = count + 1

print(count)  

# program : 4

questions=[
    {"q": "2+2", "ans": "4"},
    {"q": "4+4", "ans": "8"},
    {"q": "8+8", "ans": "16"}
]

for item in questions:
    print(item["q"])

# Program:5

import json 
def save_score(score,path):
    with open(path,"w") as f:
        json.dump(score,f)

def load_score(path):
    with open(path,"r") as f:
        return json.load(f)

save_score({"high_score":7},"s.json")
print(load_score("s.json"))    

