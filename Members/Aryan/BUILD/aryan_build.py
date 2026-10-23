import json


questions = [
    {"q": "Surya ke sabse paas kaunsa planet hai?", "ans": "Mercury"},
    {"q": "Computer ka brain kise kaha jata hai?", "ans": "CPU"},
    {"q": "Ek byte mein kitne bits hote hain?", "ans": "8"},
    {"q": "Paani ka chemical formula kya hai?", "ans": "H2O"},
    {"q": "Python mein remainder nikalne wala operator kaunsa hai?", "ans": "%"}
]



def play_quiz():
    score = 0

    for question in questions:
        print("\n" + question["q"])
        user_answer = input("Apna answer do: ").strip()

        # Hissa 3 - Jawab Check
        if user_answer.lower() == question["ans"].lower():
            print("Sahi jawab!")
            score += 1
        else:
            print("Galat jawab!")
            print("Sahi jawab tha:", question["ans"])

    return score



def rank(score):
    if score >= 4:
        return "Pro"
    elif score >= 3:
        return "Average"
    else:
        return "Beginner"



def load_high_score():
    try:
        with open("high.json", "r") as file:
            data = json.load(file)
            return data["high_score"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return 0



def save_high_score(score):
    data = {"high_score": score}

    with open("high.json", "w") as file:
        json.dump(data, file, indent=4)



def main():
    print("===== KNOWLEDGE QUIZ =====")

    high_score = load_high_score()
    print("Previous high score:", high_score)

    score = play_quiz()

    print("\n===== FINAL RESULT =====")
    print("Your score:", score, "/", len(questions))
    print("Your rank:", rank(score))

    if score > high_score:
        save_high_score(score)
        print("New high score saved!")
    else:
        print("High score not beaten.")


main()