import random
list=["mango","banana","kiwi","apple","orange","pineapple","watermelon","date","fig","muskmelon","guava","grapes","papaya","cherry"]
fruit_name=random.choice(list)
i=0
point=100
while(i<5):
    guess=input("Guess the fruit name: ")
    if guess==fruit_name:
        print("Congratulations, You Won!")
        break
    else:
        if(i==0):
            print("Hint1: Fruit name starts with: ", fruit_name[0])
        elif(i==1):
            print("Hint2: Length of fruit name is ",len(fruit_name),"letters.")
        elif(i==2):
            b="_"*(len(fruit_name)-1)+fruit_name[-1]
            print("Hint4: It could be: ",b)
        elif(i==3):
            c=fruit_name[0]+"_"*(len(fruit_name)-3)+fruit_name[-2]+fruit_name[-1]
            print("Hint5: It's easy, guess fast...",c)
        else:
            print("You Lost, the fruit is :",fruit_name)
    i+=1
    point-=20
print("Score: ",point)