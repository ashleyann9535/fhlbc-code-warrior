#Reversed Strings - Complete the solution so that it reverses the string passed into it.

def solution(string):
    reversedString = ''
    for i in range(len(string)-1, -1, -1):
        reversedString += string[i]
    return reversedString

# print(solution('hello'))

#Cat years, Dog years - Given human years, covert to dog and cat years and return all 3 in an array
# Cat Years = 15 cat years for first year +9 cat years for second year +4 cat years for each year after that
# Dog Years = 15 dog years for first year +9 dog years for second year +5 dog years for each year after that
def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    for y in range(1, human_years + 1):
        if y == 1:
            catYears += 15
            dogYears += 15
        elif y == 2:
            catYears += 9
            dogYears += 9
        else:
            catYears += 4
            dogYears += 5
    return [human_years, catYears, dogYears]

#print(human_years_cat_years_dog_years(10)) #[10,56,64]