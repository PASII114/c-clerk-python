import random as r

quizzes = {
    "1" : {"q" : "What is the smallest country in the world by land area?", "a" : "vatican city"},
    "2" : {"q" : "Who wrote the play Romeo and Juliet?", "a" : "william shakespeare"},
    "3" : {"q" : "Which planet is known as the “Red Planet”?", "a" : "mars"},
    "4" : {"q" : "What is the chemical symbol for gold?", "a" : "Au"},
    "5" : {"q" : "WIn which year did the Titanic sink?", "a" : "1912"},
}

print("\n Welcome to Quiz Finale")

while True:

    keys_list = [x for x in quizzes.keys()]

    question_id = r.choice(keys_list) #using list comprehension to get keys to a list

    print("Enter your answer ")

    answer = input(f"{quizzes[question_id]["q"]}: " )

    if answer == quizzes[question_id]["a"]:
        print("Congratulations!!! Your answer is correct")
    else:
        print("Learn some general knowledge")
        exit()