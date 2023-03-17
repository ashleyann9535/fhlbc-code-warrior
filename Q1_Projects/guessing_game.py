import random

def guessNumber():
    random_number = random.randint(1,10)
    playerGuess = int(input("(Guess the number): "))
    while playerGuess != random_number:
        if playerGuess > random_number:
            playerGuess = int(input("(Too high. Guess again): "))
        else:
            playerGuess = int(input("(Too low. Guess again): "))
    
    gamePlay = input('(You won! Would you like to play again?): ')
    if gamePlay == 'yes' or gamePlay == 'y':
        guessNumber()
    
    return 'Thanks for playing!'

print(guessNumber())
