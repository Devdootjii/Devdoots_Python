import json

def save_data(data,path):
    with open(path,"w")as f:
        json.dump(data,f)
def load_data(path):
    with open(path,"r") as f:
        return json.load(f)
save_data([90,80,70],"score.json")
total=sum(load_data("score.json"))
avg = total/len(load_data("score.json"))
print("Lists Of Score:",load_data("score.json"))
print(f"Total Score:{total}")
print(f"Average Score:{avg}")