#Divide and Conquer
#Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
#Return as a number.

def div_con(x):
    total = 0
    for i in x:
        if type(i) == int:
            total += i
        else:
            total -= int(i)
    return total

#print(div_con([9, 3, '7', '3'])) #2

# Find the index of the second occurrence of a letter in a string
# In this kata, you need to write a function that takes a string and a letter as input and 
# then returns the index of the second occurrence of that letter in the string. 
# If there is no such letter in the string, then the function should return -1. 
# If the letter occurs only once in the string, then -1 should also be returned.

def second_symbol(s, symbol):
    round = 0
    count = 0
    for char in s:
        round += 1
        if char == symbol:
            count +=1
        if count == 2:
            break
    if count == 2:
        return round - 1
    else:
        return -1

print(second_symbol('Hello world!!!','l')) # 3
print(second_symbol('Hello world!!!', 'A')) # -1