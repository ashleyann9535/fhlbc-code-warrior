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
print(long_sound)