import json

def save_scores(scores):
    with open("scores.json", "w") as f:
        json.dump(scores, f)

def load_scores():
    with open("scores.json", "r") as f:
        return json.load(f)

def average(nums):
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)


scores = [90, 80, 70]

save_scores(scores)         
scores = load_scores()       

print("scores:", scores)
print("average:", average(scores))
