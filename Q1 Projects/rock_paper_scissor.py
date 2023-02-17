print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1 =='rock':
    if player2 == 'paper':
        print('player2 win!')
    elif player2 == 'scissors':
        print('player1 wins')
elif player1 == 'scissors':
    if player2 == 'paper':
        print('player1 wins')
    elif player2 == 'rock':
        print('player2 win!')
elif player1 == 'paper':
    if player2 == 'rock':
        print('player1 wins')
    elif player2 == 'scissors':
        print('player2 win!')
elif player1 == player2:
    print('tie game')
else:
    print('please try again')

