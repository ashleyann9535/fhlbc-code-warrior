#Exercise 20 List Comprehension 
#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list 
#containing the first letter of each name in the list.  I would use a list comprehension, 
#though you could also loop over manually.

#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list 
#of all the even values.  Another good candidate for a list comp.

people = ["Elie", "Tim", "Matt"]
answer = [person[0].upper() for person in people]
print(answer)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num%2 == 0]
print(answer2)
