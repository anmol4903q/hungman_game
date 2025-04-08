# 🔠 Hangman Game — Guess the Country Name!

import random

# Hangman stages represented as ASCII art
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

# List of country names to guess
words = ['INDIA', 'DUBAI', 'LONDON', 'RUSSIA', 'CHINA', 'NEPAL','EGYPT','ITALY','JAPAN','SPAIN','BRAZIL','SWEDEN']

# Welcome Message
print("                         Welcome to the Hangman Game...")
print('''          
          As you can see there are few blanks and you have to guess
          which country name fits in those blanks...
                                  *WISH YOU GOOD LUCK*...
''')

# Game Loop
ch = "Y"
while ch == "Y":
    rand = random.choice(words)              # Select a random country
    dash = len(rand)                         # Get the number of letters
    correctopt = ["_"] * dash                # Blank spaces for the word
    game_over = False
    attempt = dash - 2                       # Number of allowed incorrect guesses

    print("Word to guess:", correctopt)
    print("You have total", attempt, "lives")

    # Round loop
    while not game_over and attempt > 0:
        correct = False
        guess = input("Try to guess a letter: ").upper()

        # Ensure only 1 letter is entered
        if len(guess) != 1:
            print("⚠️ Please enter only one letter at a time.")
            continue

        # Check guess and update correctopt
        for i in range(len(rand)):
            if rand[i] == guess:
                correctopt[i] = guess
                correct = True

        # Handle result of the guess
        if correct:
            print("✅ Correct guess!")
        else:
            print("❌ Wrong guess!")
            attempt -= 1
            if attempt > 0:
                print(stages[len(stages) - attempt - 1])

        # Show current progress
        print("Word:", correctopt)

        # Check for loss
        if attempt == 0:
            print("💀 You lost the game. The man got hanged.")
            print(stages[-1])
            print(f"The correct word was: {rand}")
            print("*" * 90)
            break

        print("❤️ Lives left:", attempt)

        # Check for win
        if "_" not in correctopt:
            print(f"🎉 CONGRATULATIONS! You guessed the word: {rand}")
            print("🥳 You saved the man!")
            print("*" * 90)
            break

    # Play again?
    ch = input("Do you want to try again? (Y/N): ").upper()
    if ch != "Y":
        print("👋 Come back anytime to play more. Thanks for playing!")
