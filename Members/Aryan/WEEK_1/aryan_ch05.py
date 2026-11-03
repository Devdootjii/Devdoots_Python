import json

def save_scores(scores):
    with open("scores.json", "w") as file:
        json.dump(scores, file)

def load_scores():
    with open("scores.json", "r") as file:
        scores = json.load(file)
    return scores

def average(nums):
    total = 0

    for num in nums:
        total = total + num

    return total / len(nums)


scores = [90, 80, 70]

save_scores(scores)

loaded_scores = load_scores()

result = average(loaded_scores)

print("Average:", result)