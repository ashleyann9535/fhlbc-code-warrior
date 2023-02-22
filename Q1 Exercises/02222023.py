#Extra Practice - Emoji Art
# use a for and while loop to create a staircase down (adds one symbol to each end when printed)
# for x in range(1, 11):
#     while x < 10:
#         print('*' * x)
#         break

#Extra Practice - Stop Copying Me
#Play the copy game until inputs "stop copying me"
start = input('Hey there! How is it going? ')
stop = 'stop copying me'

while start != stop:
    start = input(f'{start} \n').lower()