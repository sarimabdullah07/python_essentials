import random
list=["rock","paper","scissor"]
score=100
i=0
out_off=100
while(i<5):
    r=random.choice(list)
    g=input("\n\nEnter: [rock, paper, scissor]\n")
    if(g==r):
        print("We guessed the same thing,",g)
        score-=20
        out_off-=20
    elif((r=="rock")and(g=="paper") or (r=="paper")and(g=="scissor") or (r=="scissor")and(g=="rock")):
        print("You win")
        print("I gussed",r)
    elif((r=="rock")and(g=="scissor") or (r=="paper")and(g=="rock") or (r=="scissor")and(g=="paper")):
        print("You lost")
        score-=20
        print("I gussed",r)
    else:
        print("Enter proper input as rock,paper,scissor")
        score-=20
        out_off-=20
    pass
    i+=1
print("\nyour score:",score,"out of",out_off)
