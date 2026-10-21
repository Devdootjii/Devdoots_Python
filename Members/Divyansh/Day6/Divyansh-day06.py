# #Problem 1
def check_answer(user,correct):
    if user==correct:
        return True
    else:
        return False

print(check_answer("a","a"))

# Problem 2

def rank(score):
    if score>=8:
        return "Pro"
    elif score>=5 and score<=7:
        return "Average"
    else:
        return "Biginner"
print(rank(7))

# #Problem 3

ans =["a","b","c"]
user_ans=["a","x","c"]
count=0
for a in ans:
    for u in user_ans:
        if a==u:
            count+=1
print(count)

# #Problem 4
qa=[{"q":"2+2","ans":"4"},{"q":"3+3","ans":"6"},{"q":"4+4","ans":"8"}]
for q in qa:
    print(q.get("q",0))
    break

# Program 5
import json
path="high.json"
score={"high_score":7}
with open(path,"w") as f:
    json.dump(score,f)

with open(path,"r") as f:
    print(json.load(f))
    

