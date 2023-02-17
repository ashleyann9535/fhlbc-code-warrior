import random

options = ['rock', 'paper', 'scissors']

player1 = input("(enter Player 1's choice): ")
computer = random.choice(options)
print(f'computer\'s choice: {computer}')

if player1 == computer:
    print('its a tie')
elif player1 =='rock':
    if computer == 'paper':
        print('computer wins!')
    elif computer == 'scissors':
        print('player1 wins')
elif player1 == 'scissors':
    if computer == 'paper':
        print('player1 wins')
    elif computer == 'rock':
        print('computer wins!')
elif player1 == 'paper':
    if computer == 'rock':
        print('player1 wins')
    elif computer == 'scissors':
        print('computer wins!')
else:
    print('please try again')

