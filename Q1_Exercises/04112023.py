#Exercise 24 Nested List Comprehension
#Using a nested list comprehension and range(), create a variable called answer  
#with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] . 
nested_list = [[x for x in range(0,3)] for l in range(0,3)]
print(nested_list)

#Exercise 25 One More Nested List Comp Challenge
#Using list comprehension make a 10x10 nested list.  10 rows, each row contains the numbers 0-9.
matrix = [[x for x in range(0,10)] for i in range(0,10)]
print(matrix)