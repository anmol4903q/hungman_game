#hungman_game

stages = [
    """
       ------
       |    |
       |    
       |    
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]



import random
words = ['INDIA','DUBAI','LONDON','RUSSIA','CHINA','NEPAL']

print("                         Welcome to the hungeman game...")
print('''          as you can see there are few blanks and you have to guess
                     that which country will be fit in these blanks...
                                  *WISH YOU GOOD LUCK*...''')

ch = "Y"
while ch == "Y":
    rand= random.choice(words)

    #print(rand)
    dash=len(rand)

    print(["_" ]* dash)

    correctopt=["_"] * len(rand)

    game_over = False
    attempt=(len(rand))-2

    print("you have total", attempt, "lives")

    while not game_over and attempt > 0:
    
        correct = False
        guess=input("try to guess the country's name: ").upper()
        if len(guess) > 1:
            print("please enter 1 word at a time")
    
        for i in range(len(rand)):
            if rand[i] == guess:
                correctopt[i]=(guess)
                correct = True 
        #attempt-=1        
            
        if correct == True:
            print("correct guess!")
        
        if correct == False:
            print("wrong guess!")
            attempt-=1
            if attempt > 0:
                print(stages[len(stages) - attempt - 1])
        print(correctopt)
    
        if attempt == 0:
            print("you lose the game")
            print("the man got hunge💀")
            print(stages[-1])
            print(f"The correct word is {rand}")
            print("*" * 90)
            break
        print("you have:", attempt, "lives left")
    
        if "_" not in correctopt:
            print(f" CONGRATULATION! you guessed the word {rand}")
            print("you savedd the man")
            print("*" * 90)
            break
    ch= input("do you want to try again?(Y/N): ").upper()
    if ch != "Y":
        print("come back if you want to play more!")
    
    