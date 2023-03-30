#Exercise 15 Creating Lists
my_stuff = ['ribbon', 1.99, 'flower', 5]
nums = list(range(1,100))

#Exercise 16 Accessing List Data
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hannah"
people[0] = 'Hannah'
#Change "Geoffrey" to "Jeffrey"
people[4] = 'Jeffrey'
#Change "aparna" to "Aparna" (capitalize it)
people[len(people)-1] = 'Aparna'

#Exercise 17 List Iteration Exercise
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
long_sound = ''
for sound in sounds:
    long_sound += sound.upper()
#print(long_sound)

#Exercise 18 and 19 Lists Basics Exercise
# Initially create an empty list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(('Colt', 'Blue', 'Lisa'))
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0,'Done')
print(instructors)

