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
        total += n
    count = len(nums)
    return total / count

scores = [90, 80, 70]
save_scores(scores)
scores = load_scores()

print("Scores:", scores)
print("Total:", sum(scores))
print("Average:", average(scores))
