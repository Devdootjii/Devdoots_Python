import json
questions=[{"q":"ak squre ma kitna side ho ta hai ","ans":"6"},
          {"q":"bike ma kya dala jata hai chala na ka liya ","ans":"petrol"},
          {"q":"pencil ma kya ho ta hai","ans":"led"},
          {"q":"orange ma kon sa vitamin ho ta hai ","ans":"C"},
          {"q":"1min ma hamara dil kitne baar dhadkan hai ","ans":"100 bar"}
]
def Harsh_quiz():
    score=0
    for question in questions:
        print(question["q"])
        user_answer=input("Enter answer:")
        if user_answer==question["ans"]:
            print("correct")
            score=score+1
        else:
            print("wrong answer")
    return score
def rank(score):
    if score>=8:
        return "Pro"
    elif 7>=score>=5:
        return "Average"
    else:
        return "Beginner"
def save_score(score):
    with open("high_score","w") as f:
        json.dump(score,f)
def load_score():
    try:
        with open("high_score","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return 0
def main():
    high=load_score()
    print("final_result")
    print("high_score",high)
    score=Harsh_quiz()
    print("Your score:",score)
    print("Rank:",rank(score))
    save_score(score)
main()
