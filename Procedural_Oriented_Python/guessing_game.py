import random
hidden_num=random.randint(1,100)
score=100
for i in range(5):
    guess=int(input("Guess a number between 1 to 100: "))
    if guess==hidden_num:
        print("You Guessed a right number.")
        print("score: ",score)
        break
    elif guess<hidden_num:
        print("You guessed a low number")
        score-=20
    else:
        print("You guessed a high number")
        score-=20
else:
    print("You lost all the chances")