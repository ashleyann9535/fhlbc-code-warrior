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

print(div_con([9, 3, '7', '3'])) #2