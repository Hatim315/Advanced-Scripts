import random

word=random.choice(["muni","harman","karan","aman"])
guesses=''
turns=12
while turns>0:
    guess=input("Guess a word:--")
    guesses+=guess
    failed=False
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("_")
            failed=True
    if failed==False:
        print("winner")
        break
    
    if guess not in word:
        turns-=1
    if turns==0:
        print("you lose")

    