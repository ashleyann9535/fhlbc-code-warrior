# Exercise 4 Make Some Variables!
# Now that we've learned about variables and data types, let's get some practice.  Or, skip this! Totally up to you!

# Define a variable named city  and set it equal to any string
# Define a variable named price  and set it equal to any float
# Define a variable named high_score  and set it equal to any int
# Define a variable named is_having_fun  and set it to a boolean value
# You do not need to print them out, but can if you want.

city = "Odell"
price = 2.99
high_score = 35
is_having_fun = True

#Exercise 5 Escape Sequence
 # Set the message variable equal to any string containing a new-line escape sequence
message = "Avengers:\nInfinity Wars"
print(message)

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\"
print(mountains)

# Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "\"Just kidding\""
print(quotation)


# Exercise 6 String Concatenation Exercise
# Set the variable called greeting  to some greeting, e.g. "hello".
# Set the variable called name  to some name, e.g. "Heisenberg".
# Then set the variable called greet_name  so that it 
# concatenates greeting , name , and a space " " between them.
greeting = 'Zdravo'
name = 'Ashley'
greet_name = f'{greeting} {name}!'
print(greet_name)

#Exercise 7 Formatting Strings
# Set the variable called first  to your first name.
# Set the variable called last  to your last name.
# Then set the variable called formatted  that interpolates both using the .format()  method. 
#  Make sure you follow this pattern: "First Name: Colt, Last Name: Steele"
first = 'Ashley'
last = 'Sekulic'

formatted = 'First Name: {}, Last Name: {}'.format(first, last)
print(formatted)


#Exercise 8 Lucky Number 7
# At the top of the file is some starter code that randomly picks a number between 1 and 10, 
# and saves it to a variable called choice.  Don't touch those lines! (please)
# Your job is to write a simple conditional to check if choice  is 7.  
# If choice  is 7, print out "lucky".  Otherwise, print out "unlucky".
from random import randint
choice = randint(1,10)

if choice == 7:
    print('lucky')
else:
    print('unlucky')


#Exercise 9 Number is Odd
# You will be provided with a random number in a variable called num .
# Use a conditional statement to check if the number is odd. 
# If num  is odd, print "odd". Otherwise print "even". 
from random import randint
num = randint(1, 1000) #picks random number from 1-1000

if num % 2 == 0:
    print('even')
else:
    print('odd')


#Exercise 10 Food Classifying Exercise
# When you run the prewritten code, food will be randomly assigned. 
# You task is to write code that will classify what food is.  
# If food is set to either 'apple' or 'grape', your code should print 'fruit'.
# If food is set to either 'bacon' or 'steak', your code should print 'meat'
# If food is set to either 'dirt' or 'worm' your code should print 'yuck'
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

if food == 'apple' or food == 'grape':
    print('fruit')
if food == 'bacon' or food == 'steak':
    print('meat')
if food == 'dirt' or food == 'worm':
    print('yuck')