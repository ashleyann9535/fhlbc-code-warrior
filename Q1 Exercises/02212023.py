#Exercise 13 - For Loop and Range Exercise
#Use a for loop to add up every odd number from 10 to 20 (inclusive) 
#and store the result in the variable x .

sum = 0

for x in range(11, 21, 2):
    sum += x 
#print(sum)

#Extra Practice - Screaming Repeating. 
#Given a number as a input, use a loop to print a string that number of times

#num = input('How many times do I have to tell you?')
for x in range(int(num)):
    pass
    #print('Knock')

#Extra Practice Unlucky Numbers
#Loop through 1-20. 4 and 13 print 'n is unlucky, Even numbers, print 'n is even'. 
# Odd, print 'n is odd'.
for n in range(1,21):
    if n == 4 or n == 13:
        print(f'{n} is unlucky!')
    elif n % 2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
