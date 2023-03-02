# print("...rock...")
# print("...paper...")
# print("...scissors...")

# player1 = input("(enter Player 1's choice): ")
# print('*** \n \n' * 10)
# print('your turn')
# player2 = input("(enter Player 2's choice): ")

# print("SHOOT!")

# if player1 == player2:
#     print('tie game')
# elif player1 =='rock':
#     if player2 == 'paper':
#         print('player2 win!')
#     elif player2 == 'scissors':
#         print('player1 wins')
# elif player1 == 'scissors':
#     if player2 == 'paper':
#         print('player1 wins')
#     elif player2 == 'rock':
#         print('player2 win!')
# elif player1 == 'paper':
#     if player2 == 'rock':
#         print('player1 wins')
#     elif player2 == 'scissors':
#         print('player2 win!')
# else:
#     print('please try again')


#computer game
from random import choice

options = ['rock', 'paper', 'scissors']
i = 0

while i <= 4:
    player1 = input("(enter Player 1's choice): ")
    computer = choice(options)
    print(f'computer\'s choice: {computer}')

    p1Score = 0
    computerScore = 0

    if player1 == computer:
        i -= 1
        print('its a tie')
    elif player1 =='rock':
        if computer == 'paper':
            computerScore += 1
            print('computer wins!')
        elif computer == 'scissors':
            p1Score += 1
            print('player1 wins')
    elif player1 == 'scissors':
        if computer == 'paper':
            p1Score += 1
            print('player1 wins')
        elif computer == 'rock':
            computerScore += 1
            print('computer wins!')
    elif player1 == 'paper':
        if computer == 'rock':
            p1Score += 1
            print('player1 wins')
        elif computer == 'scissors':
            computerScore += 1
            print('computer wins!')
    else:
        print('please try again')
    i += 1
if p1Score > computerScore:
    print(f'Game Over: Player 1 Wins!')
else:
    print(f'Game Over: Computer Wins!')

