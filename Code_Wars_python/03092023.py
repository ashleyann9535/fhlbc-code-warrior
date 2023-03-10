#Reversed Strings - Complete the solution so that it reverses the string passed into it.

def solution(string):
    reversedString = ''
    for i in range(len(string)-1, -1, -1):
        reversedString += string[i]
    return reversedString

print(solution('hello'))