#Exercise 24 Nested List Comprehension
#Using a nested list comprehension and range(), create a variable called answer  
#with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] . 
nested_list = [[x for x in range(0,3)] for l in range(0,3)]
print(nested_list)