#Extra Practice - Emoji Art
# use a for and while loop to create a staircase down (adds one symbol to each end when printed)
# for x in range(1, 11):
#     while x < 10:
#         print('*' * x)
#         break

#Extra Practice - Stop Copying Me
#Play the copy game until inputs "stop copying me"
# start = input('Hey there! How is it going? ')
# stop = 'stop copying me'

# while start != stop:
#     start = input(f'{start} \n').lower()

#Exercise 14 - While Loop Exercise
# Use a while loop to generate a random number between 1 and 10 until you get the number 5. 
# Every time the loop runs, increment the variable i .
from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    i += 1
    number = randint(1, 10)
    print(number)
print(i)