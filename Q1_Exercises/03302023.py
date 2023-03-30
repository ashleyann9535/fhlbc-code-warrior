#Exercise 20 List Comprehension 
#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list 
#containing the first letter of each name in the list.  I would use a list comprehension, 
#though you could also loop over manually.

#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list 
#of all the even values.  Another good candidate for a list comp.

people = ["Elie", "Tim", "Matt"]
answer = [person[0].upper() for person in people]
#print(answer)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num%2 == 0]
#print(answer2)

#Exercise 21 More List Comprehension Exercises
#1. Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, which is a new list 
# that is the intersection of the two. Your output should be [3,4] .  
# Hint: use the in  operator to test whether an element is in a list.  
# For example:  5 in [1,5,2]  is True.  3 in [1,5,2]  is False.

#2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, 
# which is a new list with each word reversed and in lower case (use a slice to do the reversal!) 
# Your output should be ['eile', 'mit', 'ttam'] 

list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer3 = [x for x in list1 if x in list2]
#print(answer3)

names = ["Elie", "Tim", "Matt"]
answer4 = [name.lower() [::-1] for name in names]
#print(answer4)

#Exercise 22 Another List Comp Exercise
#For all the numbers between 1 and 100(including 100), create a variable called answer, 
# which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
answer5 = [x for x in list(range(1,101)) if x%12 == 0]
#print(answer5)

#Exercise 23 List Exercises 4
#Given the string "amazing", create a variable called answer, which is a list containing 
# all the letters from "amazing" but not the vowels (a, e, i, o, and u).  
# The answer should look like: ['m', 'z', 'n', 'g'].
answer6 = [x for x in 'amazing' if x not in 'aeiou']
print(answer6)