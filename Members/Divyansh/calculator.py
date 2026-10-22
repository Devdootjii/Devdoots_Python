questions = [
      {"q":"adult insaan ke kitne daat hote h ?","options":["28","30","32","36"],"ans":"32"},
     {"q":"python language ke naam kis comedy show se aya?","options":["monty python","the office","seinfeld","friends"],"ans":"monty python"},
     {"q":"duniya ki lambi nadi konsi h ?","options":["nice","amazon","ganga","yangtze"],"ans":"nile"},
     {"q":"binary 10 ka mtlb kitna hota h ?","options":["10","2","0","1"],"ans":"2"},
      {"q":"python me wapas calculate karne ke liye kiska use karte h?","options":["return","print","and","if"],"ans":"return"}
]
for question in questions:
     print(question["q"])
     user = input("your answer:")

Score = 0
for questions in questions:
    print(question["q"])
    if user == question["ans"]:
        print("correct")
        score+=1
    else:
         print("wrong")
    print("total score:",score)

def rank(score):
   if score>= 8:
      return "pro"
   elif score>=5:
      return "average"
   else:
        return"biggner"
try:
    with open("high.json","r") as f :
        data = json.load(f)
        high_score = data["high_score"]
except: (FileNotError)
    high_score = 0
if score> high_score:
   high_score = score
   with open("high.json","w") as f:
json.dump({"high_score": high_score},f)
   print("high score:", high_score)