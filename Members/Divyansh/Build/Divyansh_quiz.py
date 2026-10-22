import json

questions=[{"q":"6+6","ans":"12"},
           {"q":"5+5","ans":"10"},
           {"q":"4+4","ans":"8"},
           {"q":"3+3","ans":"6"},
           {"q":"2+2","ans":"4"}]

score = 0
for q in questions:
    print("Question:",q.get("q",0))
    ans = input("Enter Your Answer:")
    if ans == q.get("ans"):
        score+=1

def rank(score):
    if score >=8:
        return "Pro"
    elif score >=5:
        return "Average"
    else :
        return "Beginner"

high_score = score
try:
    with open("high.json","w") as f:
        json.dump(high_score,f)
    with open("high.json","r") as f:
        read = json.load(f)
    print(f"High Score:{read}")
    print(rank(score))
except FileNotFoundError:
    print("File dose not found!")