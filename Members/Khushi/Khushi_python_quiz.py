import json
questions = [
    {"q": "2+2?", "ans": "4"},
    {"q": "3+3?", "ans": "6"},
    {"q": "5+5?", "ans": "10"},
    {"q": "5*5?", "ans": "25"},
    {"q": "8*2?", "ans": "16"},
    {"q": "7*7?", "ans": "49"},
    {"q": "5*5-3?","ans": "22"},
    {"q": "7*5?",  "ans": "35"},
    {"q": "4*4?", "ans": "16"}
]
def check_answer(user, correct):
   if user== correct:
     return true
   else:
       return false

def rank(score):
  if score>= 8:
    return "pro"
  elif score>=5:
    return "average"
  else:
     return "biggner"

def main():
  score= 0
for question in questions:
    print(question["q"])
  user= input("your answer:")
if check_answer(user, question["ans"]):
  print("correct ")
  score+=1
else:
  print("wrong")
  print("final score:", score)
  print("your rank:", rank(score))
  try:
    with open("high.json","r") as f:
      data = json.load(f)
      high_score = data["high_score"]

  except (FileNotFoundError,KeyError)
      high_score = 0
    if score > high_score:
      high_score = score
      with open("high.json","w") as f:
        json.dump({"high_score": high_score}f)
        print("Hight score:",high_score)

if __name__ =="__main__" : main()
