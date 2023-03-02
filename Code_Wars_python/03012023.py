#Thinkful - List and Loop Drills: Grade calculator
#You're a statistics professor and the deadline for submitting your students' grades is 
#tonight at midnight. Each student's grade is determined by their mean score across all 
#of the tests they took this semester.
#You've decided to automate grade calculation by writing a function calculate_grade() 
#that takes a list of test scores as an argument and returns a one character string 
#representing the student's grade calculated

def calculate_grade(scores):
    total = 0
    for n in scores:
        total += n
    score = total / len(scores)
    print(score)
    if score >= 90:
        return 'A'
    elif score <90 and score >=80:
        return 'B'
    elif score <80 and score >=70:
        return 'C'
    elif score <70 and score >=60:
        return 'D'
    else:
        return 'F'
    
print(calculate_grade([92, 94, 99])) #A
print(calculate_grade([50, 60, 70, 80, 90])) #C
print(calculate_grade([78, 61])) #D